# Fetches brand favicons for referential use on slides (internal training deck).
# Primary: Google s2 favicon service (official site favicons at 128px).
# Fallback: a drawn monogram chip is used at deck-build time when a file is missing —
# deck_lib.js H.logo handles that, so a failed fetch never breaks the build.
import os
import urllib.request

OUT = os.path.join(os.path.dirname(__file__), 'assets', 'logos')
os.makedirs(OUT, exist_ok=True)

BRANDS = {
    'claude': 'claude.ai', 'openai': 'openai.com', 'gemini': 'gemini.google.com',
    'copilot': 'copilot.microsoft.com', 'perplexity': 'perplexity.ai', 'grok': 'x.ai',
    'deepseek': 'deepseek.com', 'notion': 'notion.com', 'manus': 'manus.im',
    'gamma': 'gamma.app', 'canva': 'canva.com', 'adobe': 'adobe.com',
    'lovable': 'lovable.dev', 'elevenlabs': 'elevenlabs.io', 'deepl': 'deepl.com',
    'toyota': 'toyota.com', 'google': 'google.com', 'microsoft': 'microsoft.com',
    'zapier': 'zapier.com', 'n8n': 'n8n.io', 'qwen': 'qwen.ai', 'kimi': 'kimi.com', 'nvidia': 'nvidia.com',
}

ok, fail = [], []
for name, domain in BRANDS.items():
    dest = os.path.join(OUT, f'{name}.png')
    url = f'https://www.google.com/s2/favicons?domain={domain}&sz=128'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        data = urllib.request.urlopen(req, timeout=20).read()
        if len(data) > 400:  # tiny responses are the generic globe placeholder
            open(dest, 'wb').write(data)
            ok.append(name)
        else:
            fail.append(name)
    except Exception as e:
        fail.append(f'{name} ({e})')
print('fetched:', ', '.join(ok) if ok else 'none')
print('fallback-to-monogram:', ', '.join(str(f) for f in fail) if fail else 'none')
