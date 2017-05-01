from smile.common import *

from genstim import genRuns, defaultLocal

import config as Cg

runs = genRuns()

locRuns = defaultLocal()


def waitRun():
    return 0


exp = Experiment()

RstDocument(text=Cg.instructions)
with UntilDone():
    KeyPress(keys=Cg.FMRI_BUTTONS)

with Loop(runs) as run:
    Wait(1.)
    with Parallel():
        Label("Please wait while the experiment start starts the run",
              blocking=False)
        Func(waitRun)
    Wait(1.)
    with Loop(run.current) as mainTrial:
        Func(waitTR)
        mainImage = Image(source=mainTrial.current['stim'],
                          duration=Cg.MAIN_STIM_DUR)
        Wait(until=mainImage.disappear_time)
        ResetClock(mainImage.disappear_time['time'])
        Wait(duration=Cg.MAIN_INTER_STIM_DUR, jitter=Cg.MAIN_INTER_JITTER)


RstDocument(text=Cg.loc_instructions)
with UntilDone():
    KeyPress(keys=Cg.FMRI_BUTTONS)

with Loop(locRun) as locTrial:
    locImage = Image(source=locTrial.current['stim'],
                     duration=Cg.LOC_STIM_DUR)
    Wait(until=locImage.disappear_time)
    ResetClock(locImage.disappear_time['time'])
    Wait(Cg.LOC_INTER_STIM_DUR)
