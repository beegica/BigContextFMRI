import random
import config as Cg
import csv
from copy import deepcopy
import os

def genRuns(low,
              num_blocks,
              num_study_items):
    random.shuffle(low)
    exp = {"study": None,
           "test": None}
    study = []
    lure = []
    for i in range(num_blocks):
        for y in range(num_study_items*2):
            temp = low.pop()
            tempS = {'stim': os.path.join(Cg.STIM_PATHS, temp)}

            # BUTTON_BOX_KEYS[0] Is assumed left, and [1] is assumed right.
            if y < num_study_items:
                tempS['corr_resp'] = Cg.BUTTON_BOX_KEYS[0:2]
                tempS['cata'] = "OLD"
                study.append(tempS)
            else:
                tempS['corr_resp'] = Cg.BUTTON_BOX_KEYS[2:4]
                tempS['cata'] = "NEW"
                lure.append(tempS)

    random.shuffle(lure)
    random.shuffle(study)

    testing_blocks = [[] for x in xrange(num_blocks)]
    for x in range(len(lure)):
        temp = lure.pop()
        i = random.randint(0, num_blocks-1)
        while(len(testing_blocks[i]) >= num_study_items):
            i = random.randint(0, num_blocks-1)
        testing_blocks[i].append(temp)

    stemp = deepcopy(study)
    for y in range(len(stemp)):
        temp = stemp.pop()
        i = random.randint(0, num_blocks-1)
        while(len(testing_blocks[i]) >= num_study_items*2):
            i = random.randint(0, num_blocks-1)
        testing_blocks[i].append(temp)

    for z in range(len(testing_blocks)):
        random.shuffle(testing_blocks[z])
    random.shuffle(study)

    exp = {"study": study,
           "test": testing_blocks}
    return exp


def getDefaultLocalizer():
    with open(Cg.LOCALIZER_FILE) as f:
        a = [{k: v for k, v in row.items()}
             for row in csv.DictReader(f, skipinitialspace=True)]
    for trial in a:
        trial['stim'] = os.path.join(Cg.STIM_PATHS, trial['stim'])
    print type(a[0]['presentation'])
    return a
