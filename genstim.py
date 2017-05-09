import random
import config as Cg
import csv


def genBlocks(low,
              num_blocks,
              num_study_items,):
    random.shuffle(low)
    blocks = []
    for i in range(num_blocks):
        study = []
        test = []

        for y in range(num_study_items*2):
            temp = low.pop()
            tempS = {'stim': os.join(Cg.STIM_PATHS, temp)}

            # BUTTON_BOX_KEYS[0] Is assumed left, and [1] is assumed right.
            if y < num_study_items:
                study.append(tempS)
                tempS['corr_resp'] = Cg.BUTTON_BOX_KEYS[0]
            else:
                tempS['corr_resp'] = Cg.BUTTON_BOX_KEYS[1]
            test.append(tempS)

        blocks.append({'study': study,
                       'test': test})

    return blocks


def getDefaultLocalizer():
    with open(Cg.LOCALIZER_FILE) as f:
        a = [{k: v for k, v in row.items()}
             for row in csv.DictReader(f, skipinitialspace=True)]
    return a
