from smile.common import *
import config as Cg
from genstim import genRuns, getDefaultLocalizer
from mathdistract import MathDistract

with open(Cg.IMAGE_LIST) as f:
    content = f.readlines()
content = [x.strip() for x in content]

runs = genRuns(low=content,
               num_blocks=Cg.MAIN_NUM_BLOCKS,
               num_study_items=Cg.MAIN_NUM_TARGETS)

locRuns = getDefaultLocalizer()

exp = Experiment()

RstDocument(text=Cg.MAIN_INSTRUCTIONS, width=exp.screen.width*2/3,
            height=exp.screen.height)
with UntilDone():
    KeyPress(keys=Cg.BUTTON_BOX_KEYS)

RstDocument(text=Cg.MAIN_STUDY_INSTRUCTIONS, width=exp.screen.width*2/3,
            height=exp.screen.height)
with UntilDone():
    KeyPress(keys=Cg.BUTTON_BOX_KEYS)

Wait(0.5)

# Check in on the participant
Label(text="Please wait for the experimenter to start.",
      font_size=Cg.FONT_SIZE)
with UntilDone():
    KeyPress(keys=Cg.RUN_START_KEYS)

# TR Wait
Label(text="Please wait.", font_size=Cg.FONT_SIZE)
with UntilDone():
    studyTR = KeyPress(keys=Cg.TR_KEYS)

Wait(1.0)

with Loop(runs['study']) as sRun:
    mainStudyImage = Image(source=sRun.current['stim'],
                           duration=Cg.MAIN_STIM_DUR)
    Wait(until=mainStudyImage.disappear_time)
    ResetClock(mainStudyImage.disappear_time['time'])
    Wait(duration=Cg.MAIN_INTER_STIM_DUR, jitter=Cg.MAIN_INTER_JITTER)
    Log(name="StudyList",
        stim=sRun.current['stim'],
        appear=mainStudyImage.appear_time,
        disappear=mainStudyImage.disappear_time,
        original_tr=studyTR.press_time)

Wait(0.500)
RstDocument(text=Cg.MAIN_MATHD_INSTRUCTIONS, width=exp.screen.width*2/3,
            height=exp.screen.height)
with UntilDone():
    KeyPress(keys=Cg.BUTTON_BOX_KEYS)

# Math Distractor
Wait(1.0)
MathDistract(duration=Cg.MD_DUR, num_vars=Cg.MD_NUM_VAR,
             plus_and_minus=Cg.MD_PAM, keys=Cg.MD_KEYS)
Wait(0.500)

RstDocument(text=Cg.MAIN_TEST_INSTRUCTIONS, width=exp.screen.width*2/3,
            height=exp.screen.height)
with UntilDone():
    KeyPress(keys=Cg.BUTTON_BOX_KEYS)

with Loop(runs['test']) as tRun:
    Wait(0.500)

    # Check in on the participant
    Label(text="Please wait for the experimenter to start.",
          font_size=Cg.FONT_SIZE)
    with UntilDone():
        KeyPress(keys=Cg.RUN_START_KEYS)

    # TR Wait
    Label(text="Please wait.", font_size=Cg.FONT_SIZE)
    with UntilDone():
        testTR = KeyPress(keys=Cg.TR_KEYS)

    Wait(1.0)
    # Start the Test Phase
    with Loop(tRun.current) as mainTrialTest:
        mainTestImage = Image(source=mainTrialTest.current['stim'],
                              font_size=Cg.FONT_SIZE, duration=Cg.RESP_DUR)
        with Meanwhile():
            Wait(until=mainTestImage.appear_time)
            ResetClock(mainTestImage.appear_time['time'])
            Wait(Cg.RESP_DELAY)
            mainTestResp = KeyPress(keys=Cg.BUTTON_BOX_KEYS,
                                    base_time=mainTestImage.appear_time['time'],

                                    correct_resp=mainTrialTest.current['corr_resp'])
        Wait(until=mainTestImage.disappear_time)
        ResetClock(mainTestImage.disappear_time['time'])
        Wait(Cg.ISI_DUR, Cg.ISI_JIT)
        Log(mainTrialTest.current,
            name="TestList",
            appear=mainTestImage.appear_time,
            disappear=mainTestImage.disappear_time,
            correct=mainTestResp.correct,
            rt=mainTestResp.rt,
            base=mainTestResp.base_time,
            press=mainTestResp.press_time,
            pressed=mainTestResp.pressed,
            original_tr=testTR.press_time
            )

# DTI
Wait(1.0)
Label(text="Please wait.", font_size=Cg.FONT_SIZE)
with UntilDone():
    KeyPress(keys=Cg.TR_KEYS)
Label(text="+", font_size=Cg.FONT_SIZE)
with UntilDone():
    KeyPress(keys=Cg.RUN_START_KEYS)


# RESTING STATE
Wait(1.0)
Label(text="Please wait.", font_size=Cg.FONT_SIZE)
with UntilDone():
    KeyPress(keys=Cg.TR_KEYS)
Label(text="+", font_size=Cg.FONT_SIZE)
with UntilDone():
    KeyPress(keys=Cg.RUN_START_KEYS)

# LOCALIZER
RstDocument(text=Cg.LOC_INSTRUCTIONS, width=exp.screen.width*2/3,
            height=exp.screen.height)
with UntilDone():
    KeyPress(keys=Cg.BUTTON_BOX_KEYS)

Wait(0.5)

# TR Wait
Label(text="Please wait.", font_size=Cg.FONT_SIZE)
with UntilDone():
    locTR = KeyPress(keys=Cg.TR_KEYS)

with Loop(locRuns) as locTrial:
    with Serial():
        locImage = Image(source=locTrial.current['stim'],
                         duration=Cg.LOC_STIM_DUR)
        Wait(until=locImage.disappear_time)
        ResetClock(locImage.disappear_time['time'])
        Wait(Cg.LOC_INTER_STIM_DUR)
    with Meanwhile():
        Wait(until=locImage.appear_time)
        locKP = KeyPress(keys=Cg.LOC_KEYS,
                         correct_resp=Ref.cond(locTrial.current['presentation'] == "2",
                                            Cg.LOC_KEYS[0], Cg.LOC_KEYS[1]),
                         base_time=locImage.appear_time['time']
                         )
    Log(locTrial.current,
        name="LOC",
        appear=locImage.appear_time,
        disappear=locImage.disappear_time,
        press=locKP.press_time,
        pressed=locKP.pressed,
        base=locKP.base_time,
        rt=locKP.rt,
        correct=locKP.correct,
        original_tr=locTR.press_time)

Label(text="The experiment is complete! Please wait!")
with UntilDone():
    KeyPress(keys=Cg.RUN_START_KEYS)
exp.run()
