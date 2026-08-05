(*=====================================================================
  CA GLUE FILLING STATION - STRUCTURED TEXT MIRROR OF THE LADDER
  Target: CODESYS 3.5 (IEC 61131-3), language: ST
  ---------------------------------------------------------------------
  This program is a 1:1 mirror of PLC_PRG_Ladder.txt (same variables,
  same network order, same semantics). Use it to:
    * validate the logic quickly (paste into an ST POU and simulate),
    * cross-reference while transcribing the ladder networks.
  Comments give the ladder NETWORK number each block mirrors.
  Requires the global variable list GVL_IO (see GVL_IO.txt).
  =====================================================================*)

PROGRAM PLC_PRG
VAR
    (* A: flasher *)
    tBlinkA, tBlinkB : TON;
    Blink            : BOOL;

    (* B: input conditioning *)
    tDbBotPres, tDbSyrPres, tDbSyrLock, tDbTipPres : TON;
    tDbModeB, tDbModeS, tDbPotLow, tDbSpill        : TON;
    dbBottlePresent, dbSyrPresent, dbSyrLocked, dbTipPresent : BOOL;
    ModeBottle, ModeSyringe, PotLow                : BOOL;

    (* C: two-hand control *)
    tDiscL, tDiscR : TON;
    ftTwoHand      : F_TRIG;
    THC_Lockout    : BOOL;
    TwoHandOK      : BOOL;
    trigStart      : R_TRIG;
    StartPulse     : BOOL;
    ResetArmed     : BOOL;
    tResetHold     : TON;
    trigReset      : R_TRIG;
    ResetPulse     : BOOL;

    (* D: safety latches *)
    EStopTrip, SpillTrip : BOOL;

    (* E: plausibility *)
    tDbBerr, tDbSerr : TON;
    BottleSensErr, SyrSensErr, SensorErr : BOOL;

    (* F: permissives *)
    ReadyBottle, ReadySyringe, SafetyOK, PermStart : BOOL;

    (* G: sequence state machine *)
    StIdle, StLocking, StFilling, StComplete : BOOL;
    CycBottle, CycSyringe, CycTopOff         : BOOL;
    MDoneEvent                               : BOOL;
    tLockTO, tFillB, tFillS                  : TON;

    (* H: faults *)
    FaultLatched : BOOL;

    (* I: lamps *)
    AttnReq : BOOL;

    (* J: counters *)
    ctrBottle, ctrSyringe : CTU;
END_VAR


(*=============== SECTION A - SYSTEM UTILITIES ===============*)

(* N01/N02: 1 Hz flasher - two cross-coupled on-delay timers *)
tBlinkA(IN := NOT tBlinkB.Q, PT := GVL_IO.cfgBlinkHalfPeriod);
tBlinkB(IN := tBlinkA.Q,     PT := GVL_IO.cfgBlinkHalfPeriod);
Blink := tBlinkA.Q;


(*=============== SECTION B - INPUT CONDITIONING ===============*)

(* N03-N06: debounce ON-edge only; drop-out is instant (fail-safe) *)
tDbBotPres(IN := GVL_IO.I_BottlePresent, PT := GVL_IO.cfgDebPresence);
dbBottlePresent := tDbBotPres.Q;

tDbSyrPres(IN := GVL_IO.I_SyrPresent, PT := GVL_IO.cfgDebPresence);
dbSyrPresent := tDbSyrPres.Q;

tDbSyrLock(IN := GVL_IO.I_SyrLocked, PT := GVL_IO.cfgDebPresence);
dbSyrLocked := tDbSyrLock.Q;

tDbTipPres(IN := GVL_IO.I_TipPresent, PT := GVL_IO.cfgDebPresence);
dbTipPresent := tDbTipPres.Q;

(* N07/N08: fixture mode - both FALSE while the signal settles *)
tDbModeB(IN := GVL_IO.I_BottleMode,     PT := GVL_IO.cfgDebMode);
ModeBottle := tDbModeB.Q;
tDbModeS(IN := NOT GVL_IO.I_BottleMode, PT := GVL_IO.cfgDebMode);
ModeSyringe := tDbModeS.Q;

(* N09: pot low with anti-slosh delay *)
tDbPotLow(IN := NOT GVL_IO.I_PotLevelOK, PT := GVL_IO.cfgDebPotLow);
PotLow := tDbPotLow.Q;


(*=============== SECTION C - TWO-HAND CONTROL ===============*)

(* N10/N11: discordance timers - one button held alone too long *)
tDiscL(IN := GVL_IO.I_BtnLeft  AND NOT GVL_IO.I_BtnRight, PT := GVL_IO.cfgSyncWindow);
tDiscR(IN := GVL_IO.I_BtnRight AND NOT GVL_IO.I_BtnLeft,  PT := GVL_IO.cfgSyncWindow);

(* N12: anti-tie-down lockout, seal-in; clears only when both released.
   ftTwoHand adds full-release re-initiation: if the two-hand condition
   drops while either button is still pressed, the lockout latches, so
   a new TwoHandOK always needs BOTH buttons freshly applied.
   (ftTwoHand reads last scan's TwoHandOK - same as the ladder, where
   network 12 executes before network 13.) *)
ftTwoHand(CLK := TwoHandOK);
THC_Lockout := (tDiscL.Q OR tDiscR.Q OR ftTwoHand.Q OR THC_Lockout)
               AND (GVL_IO.I_BtnLeft OR GVL_IO.I_BtnRight);

(* N13: two-hand valid *)
TwoHandOK := GVL_IO.I_BtnLeft AND GVL_IO.I_BtnRight AND NOT THC_Lockout;

(* N14: start pulse - rising edge gives anti-repeat *)
trigStart(CLK := TwoHandOK);
StartPulse := trigStart.Q;

(* N15: fault-reset gesture. ResetArmed latches only once both buttons
   have been RELEASED while a trip is latched - holding the buttons
   through a fault can never auto-acknowledge it. Then: hold both for
   cfgResetHold to fire the one-scan ResetPulse. *)
ResetArmed := ((NOT GVL_IO.I_BtnLeft AND NOT GVL_IO.I_BtnRight) OR ResetArmed)
              AND (FaultLatched OR EStopTrip OR SpillTrip);
tResetHold(IN := ResetArmed AND TwoHandOK, PT := GVL_IO.cfgResetHold);
trigReset(CLK := tResetHold.Q);
ResetPulse := trigReset.Q;


(*=============== SECTION D - SAFETY-EVENT LATCHES ===============*)

(* N16: E-stop trip latch; the seal breaks only on a reset gesture
   delivered while the E-stop circuit is healthy *)
EStopTrip := (NOT GVL_IO.I_EStopOK OR EStopTrip)
             AND NOT (ResetPulse AND GVL_IO.I_EStopOK);

(* N17/N18: spill debounce + latch; reset refused while tray still wet *)
tDbSpill(IN := GVL_IO.I_SpillDetect, PT := GVL_IO.cfgDebSpill);
SpillTrip := (tDbSpill.Q OR SpillTrip)
             AND NOT (ResetPulse AND NOT GVL_IO.I_SpillDetect);


(*=============== SECTION E - SENSOR PLAUSIBILITY ===============*)

(* N19: impossible bottle sensor combinations, 0.5 s confirmed *)
tDbBerr(IN := (GVL_IO.I_BottleHigh AND NOT GVL_IO.I_BottleLow)
           OR (GVL_IO.I_BottleLow  AND NOT dbBottlePresent)
           OR (GVL_IO.I_BottleHigh AND NOT dbBottlePresent),
        PT := GVL_IO.cfgDebSensorErr);
BottleSensErr := tDbBerr.Q;

(* N20: impossible syringe sensor combinations, 0.5 s confirmed *)
tDbSerr(IN := (GVL_IO.I_PlungerLow  AND GVL_IO.I_PlungerHigh)
           OR (GVL_IO.I_PlungerLow  AND NOT dbSyrPresent)
           OR (GVL_IO.I_PlungerHigh AND NOT dbSyrPresent)
           OR (dbSyrLocked  AND NOT dbSyrPresent)
           OR (dbTipPresent AND NOT dbSyrPresent),
        PT := GVL_IO.cfgDebSensorErr);
SyrSensErr := tDbSerr.Q;

(* N21: any plausibility error *)
SensorErr := BottleSensErr OR SyrSensErr;


(*=============== SECTION F - READY & PERMISSIVE ===============*)

(* N22: bottle ready - full bottle refused, top-off allowed *)
ReadyBottle := ModeBottle AND dbBottlePresent
               AND NOT GVL_IO.I_BottleHigh AND NOT SensorErr;

(* N23: syringe ready *)
ReadySyringe := ModeSyringe AND dbSyrPresent AND dbSyrLocked AND dbTipPresent
                AND NOT GVL_IO.I_PlungerHigh AND NOT SensorErr;

(* N24: safety chain healthy *)
SafetyOK := GVL_IO.I_EStopOK AND NOT EStopTrip AND NOT SpillTrip
            AND NOT FaultLatched;

(* N25: start permissive - PotLow blocks NEW fills only *)
PermStart := SafetyOK AND GVL_IO.I_DoorClosed AND NOT PotLow AND StIdle
             AND (ReadyBottle OR ReadySyringe);


(*=============== SECTION G - SEQUENCE STATE MACHINE ===============*)

(* N26: Idle -> Locking *)
IF StartPulse AND PermStart THEN
    StLocking := TRUE;
END_IF;

(* N27: register the package type for this cycle; also capture whether
   this is a top-off (bottle already at low level / syringe plunger
   already off its empty stop) - diagnostic for expected fill time *)
IF StartPulse AND PermStart AND ReadyBottle THEN
    CycBottle := TRUE;
    IF GVL_IO.I_BottleLow THEN
        CycTopOff := TRUE;
    END_IF;
END_IF;
IF StartPulse AND PermStart AND ReadySyringe THEN
    CycSyringe := TRUE;
    IF NOT GVL_IO.I_PlungerLow THEN
        CycTopOff := TRUE;
    END_IF;
END_IF;

(* N28: door lock supervision timer *)
tLockTO(IN := StLocking, PT := GVL_IO.cfgLockTimeout);

(* N29: Locking -> Filling once the bolt is confirmed *)
IF StLocking AND GVL_IO.I_DoorClosed AND GVL_IO.I_DoorLocked THEN
    StFilling := TRUE;
    StLocking := FALSE;
END_IF;

(* N30/N31: fill watchdogs *)
tFillB(IN := StFilling AND CycBottle,  PT := GVL_IO.cfgFillTimeoutBottle);
tFillS(IN := StFilling AND CycSyringe, PT := GVL_IO.cfgFillTimeoutSyr);

(* N32: Filling -> Complete on the RAW high-level signal (no debounce -
   the valve rungs cut off the same scan) - but only while the package
   is verifiably still present, so a sensor glint during a mid-fill
   removal cannot masquerade as a successful fill. MDoneEvent hands the
   completion to the counters even if a trip clears StComplete in this
   same scan. *)
IF StFilling AND (   (CycBottle  AND dbBottlePresent AND GVL_IO.I_BottleHigh)
                  OR (CycSyringe AND dbSyrPresent    AND GVL_IO.I_PlungerHigh)) THEN
    StComplete := TRUE;
    StFilling  := FALSE;
    MDoneEvent := TRUE;
END_IF;

(* N33: Complete -> Idle when package removed and buttons released *)
IF StComplete AND NOT GVL_IO.I_BtnLeft AND NOT GVL_IO.I_BtnRight
   AND (   (CycBottle  AND NOT dbBottlePresent)
        OR (CycSyringe AND NOT dbSyrPresent)) THEN
    StComplete := FALSE;
    CycBottle  := FALSE;
    CycSyringe := FALSE;
    CycTopOff  := FALSE;
END_IF;

(* N34: derived idle state *)
StIdle := NOT StLocking AND NOT StFilling AND NOT StComplete
          AND NOT FaultLatched AND NOT EStopTrip AND NOT SpillTrip;


(*=============== SECTION H - FAULT CAPTURE & ABORT ===============*)

(* N35: fault 1 - E-stop *)
IF EStopTrip THEN
    IF GVL_IO.FaultCode = 0 THEN GVL_IO.FaultCode := 1; END_IF;
    FaultLatched := TRUE;
END_IF;

(* N36: fault 3 - spill *)
IF SpillTrip THEN
    IF GVL_IO.FaultCode = 0 THEN GVL_IO.FaultCode := 3; END_IF;
    FaultLatched := TRUE;
END_IF;

(* N37: fault 2 - door opened/unlocked during cycle *)
IF ((StLocking OR StFilling) AND NOT GVL_IO.I_DoorClosed)
   OR (StFilling AND NOT GVL_IO.I_DoorLocked) THEN
    IF GVL_IO.FaultCode = 0 THEN GVL_IO.FaultCode := 2; END_IF;
    FaultLatched := TRUE;
END_IF;

(* N38: fault 8 - door lock failed to engage *)
IF tLockTO.Q THEN
    IF GVL_IO.FaultCode = 0 THEN GVL_IO.FaultCode := 8; END_IF;
    FaultLatched := TRUE;
END_IF;

(* N39: fault 4 - fill watchdog timeout *)
IF tFillB.Q OR tFillS.Q THEN
    IF GVL_IO.FaultCode = 0 THEN GVL_IO.FaultCode := 4; END_IF;
    FaultLatched := TRUE;
END_IF;

(* N40: fault 5 - sensor plausibility error during cycle *)
IF SensorErr AND (StLocking OR StFilling) THEN
    IF GVL_IO.FaultCode = 0 THEN GVL_IO.FaultCode := 5; END_IF;
    FaultLatched := TRUE;
END_IF;

(* N41: fault 6 - fixture/mode signal lost during cycle *)
IF (StLocking OR StFilling)
   AND (   (CycBottle  AND NOT ModeBottle)
        OR (CycSyringe AND NOT ModeSyringe)) THEN
    IF GVL_IO.FaultCode = 0 THEN GVL_IO.FaultCode := 6; END_IF;
    FaultLatched := TRUE;
END_IF;

(* N42: fault 7 - packaging lost/unclamped during cycle *)
IF (StLocking OR StFilling)
   AND (   (CycBottle  AND NOT dbBottlePresent)
        OR (CycSyringe AND (NOT dbSyrPresent OR NOT dbSyrLocked
                            OR NOT dbTipPresent))) THEN
    IF GVL_IO.FaultCode = 0 THEN GVL_IO.FaultCode := 7; END_IF;
    FaultLatched := TRUE;
END_IF;

(* N43: any trip aborts the cycle *)
IF FaultLatched OR EStopTrip OR SpillTrip THEN
    StLocking  := FALSE;
    StFilling  := FALSE;
    StComplete := FALSE;
END_IF;

(* N44: fault reset (gesture already release-armed in N15). NOTE: the
   E-stop and spill latches additionally demand their own cause is
   gone (N16/N18). Other causes may be acknowledged with the door
   still open etc. - starting again is blocked by PermStart anyway. *)
IF ResetPulse AND GVL_IO.I_EStopOK AND NOT GVL_IO.I_SpillDetect THEN
    FaultLatched := FALSE;
    CycBottle    := FALSE;
    CycSyringe   := FALSE;
    CycTopOff    := FALSE;
    GVL_IO.FaultCode := 0;
END_IF;


(*=============== SECTION I - OUTPUTS ===============*)

(* N45/N46: fill valves - the full safety chain (SafetyOK = raw E-stop
   AND no latched trip) plus the door and level interlocks are repeated
   in series with the state machine's permission: defence in depth *)
GVL_IO.Q_ValveBottle := StFilling AND CycBottle AND SafetyOK
    AND GVL_IO.I_DoorClosed AND GVL_IO.I_DoorLocked
    AND NOT GVL_IO.I_BottleHigh;

GVL_IO.Q_ValveSyringe := StFilling AND CycSyringe AND SafetyOK
    AND GVL_IO.I_DoorClosed AND GVL_IO.I_DoorLocked
    AND NOT GVL_IO.I_PlungerHigh;

(* N47: door lock solenoid (energise-to-lock; see GVL note) *)
GVL_IO.Q_DoorLock := StLocking OR StFilling;

(* N48-N51: indicator lamps *)
GVL_IO.Q_LampBottle  := ModeBottle;
GVL_IO.Q_LampSyringe := ModeSyringe;
GVL_IO.Q_LampFilling := GVL_IO.Q_ValveBottle OR GVL_IO.Q_ValveSyringe;
GVL_IO.Q_LampDone    := StComplete;

(* N52: E-stop lamp, steady *)
GVL_IO.Q_LampEStop := NOT GVL_IO.I_EStopOK OR EStopTrip;

(* N53/N54: flashing attention lamp *)
AttnReq := FaultLatched OR SpillTrip OR PotLow OR SensorErr OR THC_Lockout
           OR (EStopTrip AND GVL_IO.I_EStopOK);
GVL_IO.Q_LampAttention := AttnReq AND Blink;


(*=============== SECTION J - PRODUCTION COUNTERS ===============*)

(* N55/N56: count completed fills per package type. MDoneEvent is the
   one-scan completion event latched by N32 itself, so a completion
   that a same-scan trip immediately knocks out of StComplete is still
   counted. NOTE: the CODESYS Standard-library CTU stops counting when
   CV reaches PV and its reset pin is named RESET - hence PV:=65535
   for a free-running counter. *)
ctrBottle (CU := MDoneEvent AND CycBottle,  RESET := GVL_IO.cmdCounterReset, PV := 65535);
ctrSyringe(CU := MDoneEvent AND CycSyringe, RESET := GVL_IO.cmdCounterReset, PV := 65535);
GVL_IO.CntBottlesFilled  := WORD_TO_UINT(ctrBottle.CV);
GVL_IO.CntSyringesFilled := WORD_TO_UINT(ctrSyringe.CV);

(* N57: consume the completion event (producer/consumer handshake) *)
IF MDoneEvent THEN
    MDoneEvent := FALSE;
END_IF;

(* N58: consume the HMI counter-reset command *)
IF GVL_IO.cmdCounterReset THEN
    GVL_IO.cmdCounterReset := FALSE;
END_IF;
