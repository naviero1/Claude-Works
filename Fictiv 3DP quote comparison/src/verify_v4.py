import openpyxl
from q5_data import Q5, STATED
wb = openpyxl.load_workbook('../Fictiv_Quote_Comparison_V4.xlsx', data_only=True)
C, D, S = wb['Five-Quote Comparison'], wb['Quote 5 Detail'], wb['Summary']
fails = []
def chk(label, got, want, tol=0.02):
    ok = (got is not None) and abs(got - want) <= tol
    print(f'{"PASS" if ok else "FAIL":4}  {label:<62} got={got!r:>16}  want={want!r}')
    if not ok: fails.append(label)

print('--- Q5 unit prices land on the right part row in the comparison tab ---')
q5u = {r[0]: r[2] for r in Q5}
for r in range(6, 21):
    pn = C[f'B{r}'].value
    chk(f'row {r} {pn} Q5 unit', C[f'I{r}'].value, q5u[pn])

print('\n--- Q5 extended @ Q2 qty, computed independently ---')
qty = {C[f'B{r}'].value: C[f'D{r}'].value for r in range(6, 21)}
exp_total = round(sum(q5u[pn] * qty[pn] for pn in q5u), 2)
chk('Q5 total ext (N21)', C['N21'].value, exp_total)
chk('Q1 total ext (J21) unchanged from V3', C['J21'].value, 27518.22)
chk('Q2 total ext (K21) unchanged from V3', C['K21'].value, 11101.20)
chk('Q3 total ext (L21) unchanged from V3', C['L21'].value, 11235.80)
chk('Q4 total ext (M21) unchanged from V3', C['M21'].value, 10394.00)
chk('Xometry total ext (T21) unchanged from V3', C['T21'].value, 8915.44)

print('\n--- detail tab: tier reconciliation against the as-quoted totals ---')
for r, tier in ((13,'t1'), (14,'t2')):
    s = STATED[tier]
    chk(f'row {r} parts subtotal', D[f'D{r}'].value, s['parts'])
    chk(f'row {r} landed total', D[f'G{r}'].value, s['total'])
    v = D[f'I{r}'].value
    print(f'{"PASS" if v=="OK" else "FAIL":4}  row {r} reconciliation check{"":38} got={v!r}  want=\'OK\'')
    if v != 'OK': fails.append(f'row {r} check')

print('\n--- detail tab: landed-cost block ties back to the tier totals ---')
chk('F53 T1 landed ext total = G13', D['F53'].value, STATED['t1']['total'])
chk('J53 T2 landed ext total = G14', D['J53'].value, STATED['t2']['total'])
chk('G53 T1 blended landed / piece', D['G53'].value, STATED['t1']['total']/30)
chk('K53 T2 blended landed / piece', D['K53'].value, STATED['t2']['total']/450)

print('\n--- detail tab: audit findings ---')
print('   D57 min ratio :', D['D57'].value)
print('   D58 max ratio :', D['D58'].value)
print('   D59 spread    :', D['D59'].value)
print('   D60 vol disc  :', D['D60'].value)
chk('D61 round-base part count', D['D61'].value, 13, 0)
chk('D62 implied margin', D['D62'].value, 0.15, 1e-9)
print('   D65 freight %T1:', D['D65'].value)
print('   D66 freight %T2:', D['D66'].value)
nonround = [D[f'B{r}'].value for r in range(19,34) if str(D[f'K{r}'].value).startswith('NO')]
print('   parts breaking the round-$ pattern:', nonround)
if sorted(nonround) != ['670832','670833']: fails.append('round-$ exception set')

print('\n--- summary tab ---')
for r in range(4, 9):   print(f'   B{r} {S[f"A{r}"].value[:58]:<58} = {S[f"B{r}"].value}')
for r in range(19, 27): print(f'   B{r} {S[f"A{r}"].value[:58]:<58} = {S[f"B{r}"].value}')
for r in range(41, 47): print(f'   B{r} {S[f"A{r}"].value[:58]:<58} = {S[f"B{r}"].value}')
chk('Summary B8 = Q5 total', S['B8'].value, exp_total)
chk('Summary B37 rolled-back part count', S['B37'].value, 12, 0)
chk('Summary B38 MP-discount part count', S['B38'].value, 3, 0)

print('\n--- sources tab ---')
for r in range(8, 14):
    print(f'   row {r}: {str(wb["Sources"][f"A{r}"].value)[:46]:<46} | {wb["Sources"][f"C{r}"].value}')
chk('Sources C32 total parts still sums the qty block', wb['Sources']['C32'].value, 40, 0)

print('\n=== ' + ('ALL CHECKS PASSED' if not fails else f'{len(fails)} FAILURES: {fails}') + ' ===')
