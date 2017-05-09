from smile.common import *
import config as Cg
from genstim import genBlocks, getDefaultLocalizer

with open(Cg.IMAGE_LIST) as f:
    content = f.readlines()
content = [x.strip() for x in content]

runs = genRuns(low=content,
               )
locRuns = getDefaultLocalizer()

exp = Experiment()

RstDocument(text=Cg.MAIN_INSTRUCTIONS)
with UntilDone():
    KeyPress(keys=Cg.FMRI_BUTTONS)

with Loop(runs) as run:
    Wait(1.)

    # Check in on the participant
    Label(text="Please wait for the experimenter to start.")
    with UntilDone():
        KeyPress(keys=Cg.RUN_START_KEYS)

    # TR Wait
    Label(Text="Please wait.")
    with UntilDone():
        KeyPress(keys=Cg.TR_KEYS)

    Wait(1.)

    # Start the Study Phase
    with Loop(run.current['study']) as mainTrialStudy:
        mainStudyImage = Image(source=mainTrialStudy.current,
                               duration=Cg.MAIN_STIM_DUR)
        Wait(until=mainStudyImage.disappear_time)
        ResetClock(mainStudyImage.disappear_time['time'])
        Wait(duration=Cg.ISI_DUR, jitter=Cg.ISI_JIT)
        Log(mainTrialStudy.current,
            name="StudyList",
            stim=MainTrialStudy.current,
            appear=mainStudyImage.appear_time,
            disappear=mainStudyImage.disappear_time
            )
    # Math Distractor
    Wait(1.0)
    MathDistract(duration=Cg.MD_DUR, num_var=Cg.MD_NUM_VAR,
                 plus_and_minus=Cg.MD_PAM, keys=Cg.MD_KEYS)
    Wait(1.0)
    Label(text="Testing Phase", duration=2.)
    Wait(1.0)

    # Start the Test Phase
    with Loop(run.current['test']) as mainTrialTest:
        mainTestImage = Image(source=mainTrialTest.current['stim'],
                              font_size=Cg.FONT_SIZE)
        with UntilDone():
            Wait(until=mainTestImage.appear_time)
            ResetClock(mainTestImage.appear_time['time'])
            Wait(Cg.RESP_DELAY)
            mainTestResp = KeyPress(keys=Cg.BUTTON_BOX_KEYS,
                                    base_time=mainTestImage.appear_time['time'],
                                    duration=Cg.RESP_DUR-Cg.RESP_DELAY,
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
            )

RstDocument(text=Cg.LOC_INSTRUCTIONS)
with UntilDone():
    KeyPress(keys=Cg.FMRI_BUTTONS)

with Loop(locRun) as locTrial:
    with Serial():
        locImage = Image(source=locTrial.current['stim'],
                         duration=Cg.LOC_STIM_DUR)
        Wait(until=locImage.disappear_time)
        ResetClock(locImage.disappear_time['time'])
        Wait(cg.LOC_INTER_STIM_DUR)
    with Meanwhile():
        KeyPress(keys=Cg.LOC_KEYS)

exp.run()
