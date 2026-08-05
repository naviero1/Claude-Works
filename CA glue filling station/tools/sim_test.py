"""Scan-accurate Python simulation of PLC_PRG.st for the CA glue filler.

Mirrors the ST source network-for-network (same order, same semantics) with
IEC-style TON / R_TRIG / CTU function blocks, then runs the key scenarios and
asserts the expected behaviour.  Scan time: 10 ms per step.
"""

DT = 0.010  # 10 ms scan


class TON:
    def __init__(self):
        self.Q = False
        self.ET = 0.0

    def __call__(self, IN, PT):
        if IN:
            self.ET = min(self.ET + DT, PT)
            self.Q = self.ET >= PT
        else:
            self.ET = 0.0
            self.Q = False


class R_TRIG:
    def __init__(self):
        self.Q = False
        self._m = False

    def __call__(self, CLK):
        self.Q = CLK and not self._m
        self._m = CLK


class F_TRIG:
    def __init__(self):
        self.Q = False
        self._m = False

    def __call__(self, CLK):
        self.Q = (not CLK) and self._m
        self._m = CLK


class CTU:
    def __init__(self):
        self.Q = False
        self.CV = 0
        self._m = False

    def __call__(self, CU, RESET, PV):
        if RESET:
            self.CV = 0
        elif CU and not self._m and self.CV < PV:
            self.CV += 1
        self._m = CU
        self.Q = self.CV >= PV


class GVL:
    def __init__(self):
        # inputs (fail-safe defaults: healthy, idle station, syringe absent)
        self.I_BtnLeft = False
        self.I_BtnRight = False
        self.I_DoorClosed = True
        self.I_DoorLocked = False
        self.I_PotLevelOK = True
        self.I_BottleMode = True
        self.I_BottleLow = False
        self.I_BottleHigh = False
        self.I_BottlePresent = False
        self.I_TipPresent = False
        self.I_PlungerLow = False
        self.I_PlungerHigh = False
        self.I_SyrPresent = False
        self.I_SyrLocked = False
        self.I_EStopOK = True
        self.I_SpillDetect = False
        # outputs
        self.Q_ValveSyringe = False
        self.Q_ValveBottle = False
        self.Q_LampBottle = False
        self.Q_LampSyringe = False
        self.Q_LampFilling = False
        self.Q_LampDone = False
        self.Q_LampEStop = False
        self.Q_LampAttention = False
        self.Q_DoorLock = False
        # config
        self.cfgSyncWindow = 0.5
        self.cfgResetHold = 3.0
        self.cfgDebPresence = 0.1
        self.cfgDebMode = 0.2
        self.cfgDebSpill = 0.05
        self.cfgDebPotLow = 2.0
        self.cfgDebSensorErr = 0.5
        self.cfgLockTimeout = 2.0
        self.cfgFillTimeoutBottle = 30.0
        self.cfgFillTimeoutSyr = 20.0
        self.cfgBlinkHalfPeriod = 0.5
        # diagnostics
        self.FaultCode = 0
        self.CntBottlesFilled = 0
        self.CntSyringesFilled = 0
        self.cmdCounterReset = False


class PLC:
    def __init__(self):
        self.g = GVL()
        # local VAR
        self.tBlinkA, self.tBlinkB = TON(), TON()
        self.Blink = False
        self.tDbBotPres, self.tDbSyrPres = TON(), TON()
        self.tDbSyrLock, self.tDbTipPres = TON(), TON()
        self.tDbModeB, self.tDbModeS = TON(), TON()
        self.tDbPotLow, self.tDbSpill = TON(), TON()
        self.dbBottlePresent = self.dbSyrPresent = False
        self.dbSyrLocked = self.dbTipPresent = False
        self.ModeBottle = self.ModeSyringe = False
        self.PotLow = False
        self.tDiscL, self.tDiscR = TON(), TON()
        self.ftTwoHand = F_TRIG()
        self.THC_Lockout = False
        self.TwoHandOK = False
        self.trigStart = R_TRIG()
        self.StartPulse = False
        self.ResetArmed = False
        self.tResetHold = TON()
        self.trigReset = R_TRIG()
        self.ResetPulse = False
        self.EStopTrip = self.SpillTrip = False
        self.tDbBerr, self.tDbSerr = TON(), TON()
        self.BottleSensErr = self.SyrSensErr = self.SensorErr = False
        self.ReadyBottle = self.ReadySyringe = False
        self.SafetyOK = self.PermStart = False
        self.StIdle = self.StLocking = self.StFilling = self.StComplete = False
        self.CycBottle = self.CycSyringe = self.CycTopOff = False
        self.MDoneEvent = False
        self.tLockTO, self.tFillB, self.tFillS = TON(), TON(), TON()
        self.FaultLatched = False
        self.AttnReq = False
        self.ctrBottle, self.ctrSyringe = CTU(), CTU()
        self.t = 0.0

    def scan(self):
        g = self.g
        # A
        self.tBlinkA(not self.tBlinkB.Q, g.cfgBlinkHalfPeriod)
        self.tBlinkB(self.tBlinkA.Q, g.cfgBlinkHalfPeriod)
        self.Blink = self.tBlinkA.Q
        # B
        self.tDbBotPres(g.I_BottlePresent, g.cfgDebPresence)
        self.dbBottlePresent = self.tDbBotPres.Q
        self.tDbSyrPres(g.I_SyrPresent, g.cfgDebPresence)
        self.dbSyrPresent = self.tDbSyrPres.Q
        self.tDbSyrLock(g.I_SyrLocked, g.cfgDebPresence)
        self.dbSyrLocked = self.tDbSyrLock.Q
        self.tDbTipPres(g.I_TipPresent, g.cfgDebPresence)
        self.dbTipPresent = self.tDbTipPres.Q
        self.tDbModeB(g.I_BottleMode, g.cfgDebMode)
        self.ModeBottle = self.tDbModeB.Q
        self.tDbModeS(not g.I_BottleMode, g.cfgDebMode)
        self.ModeSyringe = self.tDbModeS.Q
        self.tDbPotLow(not g.I_PotLevelOK, g.cfgDebPotLow)
        self.PotLow = self.tDbPotLow.Q
        # C
        self.tDiscL(g.I_BtnLeft and not g.I_BtnRight, g.cfgSyncWindow)
        self.tDiscR(g.I_BtnRight and not g.I_BtnLeft, g.cfgSyncWindow)
        self.ftTwoHand(self.TwoHandOK)
        self.THC_Lockout = ((self.tDiscL.Q or self.tDiscR.Q or self.ftTwoHand.Q
                             or self.THC_Lockout)
                            and (g.I_BtnLeft or g.I_BtnRight))
        self.TwoHandOK = g.I_BtnLeft and g.I_BtnRight and not self.THC_Lockout
        self.trigStart(self.TwoHandOK)
        self.StartPulse = self.trigStart.Q
        self.ResetArmed = (((not g.I_BtnLeft and not g.I_BtnRight) or self.ResetArmed)
                           and (self.FaultLatched or self.EStopTrip or self.SpillTrip))
        self.tResetHold(self.ResetArmed and self.TwoHandOK, g.cfgResetHold)
        self.trigReset(self.tResetHold.Q)
        self.ResetPulse = self.trigReset.Q
        # D
        self.EStopTrip = ((not g.I_EStopOK or self.EStopTrip)
                          and not (self.ResetPulse and g.I_EStopOK))
        self.tDbSpill(g.I_SpillDetect, g.cfgDebSpill)
        self.SpillTrip = ((self.tDbSpill.Q or self.SpillTrip)
                          and not (self.ResetPulse and not g.I_SpillDetect))
        # E
        self.tDbBerr((g.I_BottleHigh and not g.I_BottleLow)
                     or (g.I_BottleLow and not self.dbBottlePresent)
                     or (g.I_BottleHigh and not self.dbBottlePresent),
                     g.cfgDebSensorErr)
        self.BottleSensErr = self.tDbBerr.Q
        self.tDbSerr((g.I_PlungerLow and g.I_PlungerHigh)
                     or (g.I_PlungerLow and not self.dbSyrPresent)
                     or (g.I_PlungerHigh and not self.dbSyrPresent)
                     or (self.dbSyrLocked and not self.dbSyrPresent)
                     or (self.dbTipPresent and not self.dbSyrPresent),
                     g.cfgDebSensorErr)
        self.SyrSensErr = self.tDbSerr.Q
        self.SensorErr = self.BottleSensErr or self.SyrSensErr
        # F
        self.ReadyBottle = (self.ModeBottle and self.dbBottlePresent
                            and not g.I_BottleHigh and not self.SensorErr)
        self.ReadySyringe = (self.ModeSyringe and self.dbSyrPresent
                             and self.dbSyrLocked and self.dbTipPresent
                             and not g.I_PlungerHigh and not self.SensorErr)
        self.SafetyOK = (g.I_EStopOK and not self.EStopTrip
                         and not self.SpillTrip and not self.FaultLatched)
        self.PermStart = (self.SafetyOK and g.I_DoorClosed and not self.PotLow
                          and self.StIdle
                          and (self.ReadyBottle or self.ReadySyringe))
        # G
        if self.StartPulse and self.PermStart:
            self.StLocking = True
        if self.StartPulse and self.PermStart and self.ReadyBottle:
            self.CycBottle = True
            if g.I_BottleLow:
                self.CycTopOff = True
        if self.StartPulse and self.PermStart and self.ReadySyringe:
            self.CycSyringe = True
            if not g.I_PlungerLow:
                self.CycTopOff = True
        self.tLockTO(self.StLocking, self.g.cfgLockTimeout)
        if self.StLocking and g.I_DoorClosed and g.I_DoorLocked:
            self.StFilling = True
            self.StLocking = False
        self.tFillB(self.StFilling and self.CycBottle, g.cfgFillTimeoutBottle)
        self.tFillS(self.StFilling and self.CycSyringe, g.cfgFillTimeoutSyr)
        if self.StFilling and ((self.CycBottle and self.dbBottlePresent
                                and g.I_BottleHigh)
                               or (self.CycSyringe and self.dbSyrPresent
                                   and g.I_PlungerHigh)):
            self.StComplete = True
            self.StFilling = False
            self.MDoneEvent = True
        if (self.StComplete and not g.I_BtnLeft and not g.I_BtnRight
                and ((self.CycBottle and not self.dbBottlePresent)
                     or (self.CycSyringe and not self.dbSyrPresent))):
            self.StComplete = False
            self.CycBottle = False
            self.CycSyringe = False
            self.CycTopOff = False
        self.StIdle = (not self.StLocking and not self.StFilling
                       and not self.StComplete and not self.FaultLatched
                       and not self.EStopTrip and not self.SpillTrip)
        # H
        def fault(code, cond):
            if cond:
                if g.FaultCode == 0:
                    g.FaultCode = code
                self.FaultLatched = True
        fault(1, self.EStopTrip)
        fault(3, self.SpillTrip)
        fault(2, ((self.StLocking or self.StFilling) and not g.I_DoorClosed)
                 or (self.StFilling and not g.I_DoorLocked))
        fault(8, self.tLockTO.Q)
        fault(4, self.tFillB.Q or self.tFillS.Q)
        fault(5, self.SensorErr and (self.StLocking or self.StFilling))
        fault(6, (self.StLocking or self.StFilling)
                 and ((self.CycBottle and not self.ModeBottle)
                      or (self.CycSyringe and not self.ModeSyringe)))
        fault(7, (self.StLocking or self.StFilling)
                 and ((self.CycBottle and not self.dbBottlePresent)
                      or (self.CycSyringe and (not self.dbSyrPresent
                                               or not self.dbSyrLocked
                                               or not self.dbTipPresent))))
        if self.FaultLatched or self.EStopTrip or self.SpillTrip:
            self.StLocking = False
            self.StFilling = False
            self.StComplete = False
        if self.ResetPulse and g.I_EStopOK and not g.I_SpillDetect:
            self.FaultLatched = False
            self.CycBottle = False
            self.CycSyringe = False
            self.CycTopOff = False
            g.FaultCode = 0
        # I
        g.Q_ValveBottle = (self.StFilling and self.CycBottle and self.SafetyOK
                           and g.I_DoorClosed and g.I_DoorLocked
                           and not g.I_BottleHigh)
        g.Q_ValveSyringe = (self.StFilling and self.CycSyringe and self.SafetyOK
                            and g.I_DoorClosed and g.I_DoorLocked
                            and not g.I_PlungerHigh)
        g.Q_DoorLock = self.StLocking or self.StFilling
        g.Q_LampBottle = self.ModeBottle
        g.Q_LampSyringe = self.ModeSyringe
        g.Q_LampFilling = g.Q_ValveBottle or g.Q_ValveSyringe
        g.Q_LampDone = self.StComplete
        g.Q_LampEStop = not g.I_EStopOK or self.EStopTrip
        self.AttnReq = (self.FaultLatched or self.SpillTrip or self.PotLow
                        or self.SensorErr or self.THC_Lockout
                        or (self.EStopTrip and g.I_EStopOK))
        g.Q_LampAttention = self.AttnReq and self.Blink
        # J
        self.ctrBottle(self.MDoneEvent and self.CycBottle, g.cmdCounterReset, 65535)
        self.ctrSyringe(self.MDoneEvent and self.CycSyringe, g.cmdCounterReset, 65535)
        g.CntBottlesFilled = self.ctrBottle.CV
        g.CntSyringesFilled = self.ctrSyringe.CV
        if self.MDoneEvent:
            self.MDoneEvent = False
        if g.cmdCounterReset:
            g.cmdCounterReset = False
        self.t += DT

    def run(self, seconds, hook=None):
        n = int(round(seconds / DT))
        for _ in range(n):
            if hook:
                hook(self)
            self.scan()


# ---------------------------------------------------------------------------
# scenario helpers
# ---------------------------------------------------------------------------
FAIL = []


def check(name, cond):
    status = "ok " if cond else "FAIL"
    print(f"  [{status}] {name}")
    if not cond:
        FAIL.append(name)


def door_lock_follows(plc):
    """Simulate guard-lock hardware: bolt engages 150 ms after command."""
    if not hasattr(plc, "_lock_t"):
        plc._lock_t = 0.0
    if plc.g.Q_DoorLock:
        plc._lock_t += DT
    else:
        plc._lock_t = 0.0
    plc.g.I_DoorLocked = plc._lock_t >= 0.15


def press_both(plc, stagger=0.05):
    plc.g.I_BtnLeft = True
    plc.run(stagger, door_lock_follows)
    plc.g.I_BtnRight = True


def release_both(plc):
    plc.g.I_BtnLeft = plc.g.I_BtnRight = False


def reset_gesture(plc):
    release_both(plc)
    plc.run(0.2, door_lock_follows)      # ResetArmed needs a seen release
    press_both(plc)
    plc.run(3.3, door_lock_follows)
    release_both(plc)
    plc.run(0.2, door_lock_follows)


# ---------------------------------------------------------------------------
print("SCENARIO 1: normal bottle fill (incl. glue rise + removal)")
p = PLC()
p.run(0.5, door_lock_follows)                    # power-up settle
check("idle after power-up", p.StIdle)
check("bottle mode lamp on", p.g.Q_LampBottle and not p.g.Q_LampSyringe)
p.g.I_BottlePresent = True
p.run(0.3, door_lock_follows)
check("ReadyBottle", p.ReadyBottle)
press_both(p)
p.run(0.05, door_lock_follows)
check("locking entered", p.StLocking or p.StFilling)
p.run(0.5, door_lock_follows)
check("filling, valve on", p.StFilling and p.g.Q_ValveBottle)
check("door locked during fill", p.g.Q_DoorLock and p.g.I_DoorLocked)
check("filling lamp on", p.g.Q_LampFilling)
release_both(p)
p.run(2.0, door_lock_follows)                    # glue rising...
p.g.I_BottleLow = True
p.run(2.0, door_lock_follows)
p.g.I_BottleHigh = True                          # reaches fill line
p.run(0.05, door_lock_follows)
check("valve closed on high level", not p.g.Q_ValveBottle)
check("complete state + done lamp", p.StComplete and p.g.Q_LampDone)
check("door released in complete", not p.g.Q_DoorLock)
check("no fault", p.g.FaultCode == 0 and not p.FaultLatched)
p.g.I_BottlePresent = False                      # remove bottle
p.g.I_BottleLow = p.g.I_BottleHigh = False
p.run(0.3, door_lock_follows)
check("back to idle", p.StIdle and not p.g.Q_LampDone)
check("bottle counted once", p.g.CntBottlesFilled == 1)

print("SCENARIO 2: top-off of a partially full bottle")
p2 = PLC()
p2.run(0.5, door_lock_follows)
p2.g.I_BottlePresent = True
p2.g.I_BottleLow = True                          # already partly full
p2.run(0.7, door_lock_follows)
check("no sensor error for legit top-off", not p2.SensorErr)
check("ReadyBottle for top-off", p2.ReadyBottle)
press_both(p2)
p2.run(0.5, door_lock_follows)
check("top-off filling", p2.StFilling and p2.g.Q_ValveBottle)
check("top-off captured (CycTopOff)", p2.CycTopOff)

print("SCENARIO 3: refuse an already-full bottle")
p3 = PLC()
p3.run(0.5, door_lock_follows)
p3.g.I_BottlePresent = True
p3.g.I_BottleLow = p3.g.I_BottleHigh = True
p3.run(0.7, door_lock_follows)
check("full bottle not ready", not p3.ReadyBottle)
press_both(p3)
p3.run(0.5, door_lock_follows)
check("no start on full bottle", p3.StIdle)

print("SCENARIO 4: syringe fill with clamp + tip permissives")
p4 = PLC()
p4.g.I_BottleMode = False
p4.run(0.5, door_lock_follows)
check("syringe mode lamp", p4.g.Q_LampSyringe and not p4.g.Q_LampBottle)
p4.g.I_SyrPresent = True
p4.g.I_PlungerLow = True
p4.run(0.3, door_lock_follows)
check("not ready without clamp/tip", not p4.ReadySyringe)
p4.g.I_SyrLocked = True
p4.g.I_TipPresent = True
p4.run(0.3, door_lock_follows)
check("ready with clamp+tip", p4.ReadySyringe)
press_both(p4)
p4.run(0.5, door_lock_follows)
check("syringe valve on", p4.g.Q_ValveSyringe and not p4.g.Q_ValveBottle)
release_both(p4)
p4.g.I_PlungerLow = False
p4.run(1.0, door_lock_follows)
p4.g.I_PlungerHigh = True
p4.run(0.05, door_lock_follows)
check("syringe complete", p4.StComplete and not p4.g.Q_ValveSyringe)
p4.g.I_SyrPresent = p4.g.I_SyrLocked = p4.g.I_TipPresent = False
p4.g.I_PlungerHigh = False
p4.run(0.3, door_lock_follows)
check("syringe counted", p4.g.CntSyringesFilled == 1)
check("unlock-without-syringe transient did not latch a fault",
      p4.g.FaultCode == 0)

print("SCENARIO 5: E-stop mid-fill, then reset gesture")
p5 = PLC()
p5.run(0.5, door_lock_follows)
p5.g.I_BottlePresent = True
p5.run(0.3, door_lock_follows)
press_both(p5)
p5.run(0.5, door_lock_follows)
check("filling", p5.StFilling)
p5.g.I_EStopOK = False                           # E-STOP!
p5.run(0.05, door_lock_follows)
check("valve off within a scan", not p5.g.Q_ValveBottle)
check("fault code 1 (first out)", p5.g.FaultCode == 1)
check("e-stop lamp", p5.g.Q_LampEStop)
release_both(p5)
p5.run(0.5, door_lock_follows)
p5.g.I_EStopOK = True                            # twist out
p5.run(0.5, door_lock_follows)
check("still latched after release", p5.EStopTrip and p5.g.Q_LampEStop)
check("attention flashes while reset owed", p5.AttnReq)
reset_gesture(p5)
check("one gesture clears everything",
      not p5.EStopTrip and not p5.FaultLatched and p5.g.FaultCode == 0)
check("back to idle-ish (bottle still in)", p5.StIdle)
check("no auto-restart of the fill", not p5.StFilling and not p5.StLocking)

print("SCENARIO 6: two-hand discordance + tie-down")
p6 = PLC()
p6.run(0.5, door_lock_follows)
p6.g.I_BottlePresent = True
p6.run(0.3, door_lock_follows)
p6.g.I_BtnLeft = True                            # hold left alone…
p6.run(0.8, door_lock_follows)                   # …longer than 0.5 s
p6.g.I_BtnRight = True                           # tie-down attempt
p6.run(0.5, door_lock_follows)
check("lockout active", p6.THC_Lockout)
check("no start on tie-down", p6.StIdle and not p6.StLocking)
p6.g.I_BtnRight = False                          # release only one
p6.run(0.3, door_lock_follows)
p6.g.I_BtnRight = True
p6.run(0.3, door_lock_follows)
check("still locked out until BOTH released", p6.THC_Lockout)
release_both(p6)
p6.run(0.2, door_lock_follows)
check("lockout clears on full release", not p6.THC_Lockout)
press_both(p6)
p6.run(0.5, door_lock_follows)
check("clean press now starts", p6.StFilling or p6.StLocking)

print("SCENARIO 7: door forced open mid-fill")
p7 = PLC()
p7.run(0.5, door_lock_follows)
p7.g.I_BottlePresent = True
p7.run(0.3, door_lock_follows)
press_both(p7)
p7.run(0.5, door_lock_follows)
check("filling", p7.StFilling)
p7.g.I_DoorClosed = False
p7.g.I_DoorLocked = False
p7.run(0.05)
check("abort, valve off", not p7.g.Q_ValveBottle and not p7.StFilling)
check("fault code 2", p7.g.FaultCode == 2)

print("SCENARIO 8: lock never engages -> fault 8")
p8 = PLC()
p8.run(0.5)                                      # NOTE: no door_lock hook
p8.g.I_BottlePresent = True
p8.run(0.3)
press_both(p8)
p8.g.I_BtnRight = True
p8.run(2.5)
check("fault code 8 after lock timeout", p8.g.FaultCode == 8)
check("not stuck in locking", not p8.StLocking)

print("SCENARIO 9: fill watchdog -> fault 4")
p9 = PLC()
p9.run(0.5, door_lock_follows)
p9.g.I_BottlePresent = True
p9.run(0.3, door_lock_follows)
press_both(p9)
p9.run(31.5, door_lock_follows)                  # high level never comes
check("fault code 4", p9.g.FaultCode == 4)
check("valve off after watchdog", not p9.g.Q_ValveBottle)
release_both(p9)
reset_gesture(p9)
check("watchdog fault resettable", p9.g.FaultCode == 0 and p9.StIdle)

print("SCENARIO 10: spill during fill; reset refused while wet")
p10 = PLC()
p10.run(0.5, door_lock_follows)
p10.g.I_BottlePresent = True
p10.run(0.3, door_lock_follows)
press_both(p10)
p10.run(0.5, door_lock_follows)
p10.g.I_SpillDetect = True
p10.run(0.2, door_lock_follows)
check("fault code 3, valve off", p10.g.FaultCode == 3 and not p10.g.Q_ValveBottle)
release_both(p10)
p10.run(0.2, door_lock_follows)
reset_gesture(p10)                               # tray still wet!
check("reset refused while wet", p10.SpillTrip and p10.g.FaultCode == 3)
p10.g.I_SpillDetect = False                      # clean the tray
p10.run(0.2, door_lock_follows)
reset_gesture(p10)
check("reset accepted when dry", not p10.SpillTrip and p10.g.FaultCode == 0)

print("SCENARIO 11: sensor plausibility - level signal with no bottle")
p11 = PLC()
p11.run(0.5, door_lock_follows)
p11.g.I_BottleHigh = True                        # residue on sensor, no bottle
p11.run(0.7, door_lock_follows)
check("SensorErr raised", p11.SensorErr)
check("attention condition", p11.AttnReq)
check("no start possible", not p11.ReadyBottle)
p11.g.I_BottleHigh = False
p11.run(0.1, door_lock_follows)
check("self-clears when cause gone", not p11.SensorErr)

print("SCENARIO 12: bottle yanked mid-fill -> fault 7")
p12 = PLC()
p12.run(0.5, door_lock_follows)
p12.g.I_BottlePresent = True
p12.run(0.3, door_lock_follows)
press_both(p12)
p12.run(0.5, door_lock_follows)
p12.g.I_BottlePresent = False
p12.run(0.05, door_lock_follows)
check("fault 7, valve off", p12.g.FaultCode == 7 and not p12.g.Q_ValveBottle)

print("SCENARIO 13: pot low blocks new fill but not running fill")
p13 = PLC()
p13.run(0.5, door_lock_follows)
p13.g.I_BottlePresent = True
p13.run(0.3, door_lock_follows)
press_both(p13)
p13.run(0.5, door_lock_follows)
check("filling", p13.StFilling)
p13.g.I_PotLevelOK = False                       # pot runs low mid-fill
p13.run(2.5, door_lock_follows)
check("running fill unaffected by PotLow", p13.StFilling and p13.g.FaultCode == 0)
p13.g.I_BottleHigh = True
p13.run(0.05, door_lock_follows)
release_both(p13)
p13.g.I_BottlePresent = False
p13.g.I_BottleHigh = False
p13.run(0.3, door_lock_follows)
p13.g.I_BottlePresent = True                     # next bottle
p13.run(0.3, door_lock_follows)
press_both(p13)
p13.run(0.5, door_lock_follows)
check("new start refused while pot low", p13.StIdle and not p13.StFilling)
check("attention flashing for refill", p13.AttnReq)

print("SCENARIO 14: flasher runs", )
p14 = PLC()
seen = set()
for _ in range(300):
    p14.scan()
    seen.add(p14.Blink)
check("blink toggles", seen == {True, False})

print("SCENARIO 15: holding buttons through a fault must NOT auto-acknowledge")
p15 = PLC()
p15.run(0.5, door_lock_follows)
p15.g.I_BottlePresent = True
p15.run(0.3, door_lock_follows)
press_both(p15)
p15.run(0.5, door_lock_follows)
check("filling", p15.StFilling)
p15.g.I_DoorClosed = False               # door forced open, hands still on buttons
p15.g.I_DoorLocked = False
p15.run(5.0)                             # keep holding well past 3 s
check("fault 2 still latched while holding", p15.FaultLatched and p15.g.FaultCode == 2)
release_both(p15)
p15.g.I_DoorClosed = True
p15.run(0.2, door_lock_follows)
reset_gesture(p15)
check("release-then-hold clears the fault", not p15.FaultLatched and p15.g.FaultCode == 0)

print("SCENARIO 16: full-release re-initiation of the two-hand condition")
p16 = PLC()
p16.run(0.5, door_lock_follows)          # no package: TwoHandOK can form, no start
press_both(p16)
p16.run(0.2, door_lock_follows)
check("two-hand condition formed", p16.TwoHandOK)
p16.g.I_BtnLeft = False                  # release ONE button briefly
p16.run(0.2, door_lock_follows)
p16.g.I_BtnLeft = True                   # re-press within the 0.5 s window
p16.run(0.3, door_lock_follows)
check("re-press without full release refused", not p16.TwoHandOK and p16.THC_Lockout)
release_both(p16)
p16.run(0.2, door_lock_follows)
press_both(p16)
p16.run(0.2, door_lock_follows)
check("fresh press after full release accepted", p16.TwoHandOK)

print("SCENARIO 17: high-level glint while bottle is yanked = fault 7, not success")
p17 = PLC()
p17.run(0.5, door_lock_follows)
p17.g.I_BottlePresent = True
p17.run(0.3, door_lock_follows)
press_both(p17)
p17.run(0.5, door_lock_follows)
check("filling", p17.StFilling)
p17.g.I_BottlePresent = False            # yank...
p17.g.I_BottleHigh = True                # ...with a same-scan sensor glint
p17.run(0.05, door_lock_follows)
check("not counted as success", p17.g.CntBottlesFilled == 0 and not p17.StComplete)
check("fault 7 latched", p17.g.FaultCode == 7)

print("SCENARIO 18: stuck-ON plunger sensor with empty nest is annunciated")
p18 = PLC()
p18.g.I_BottleMode = False
p18.run(0.5, door_lock_follows)
p18.g.I_PlungerHigh = True               # no syringe present
p18.run(0.7, door_lock_follows)
check("SensorErr for plunger-without-syringe", p18.SensorErr)

print()
if FAIL:
    print("FAILURES:", len(FAIL))
    for f in FAIL:
        print(" -", f)
    raise SystemExit(1)
print("ALL SCENARIOS PASS")
