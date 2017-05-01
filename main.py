from smile.common import *

from genstim import genRuns, defaultLocal

import config as Cg

runs = genRuns()

locRuns = defaultLocal()


def waitRun():
    return 0


exp = Experiment()

RstDocument(text=Cg.instructions)


with Loop(runs) as run:
    Wait(1.)
    with Parallel():
        Label("Please wait while the experiment start starts the run",
              blocking=False)
        Func(waitRun)
    Wait(1.)
    with Loop(run.current) as trial:

with Loop():
