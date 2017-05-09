
_ins_filename = "main_instruct.rst"
MAIN_INSTRUCTIONS = open(_ins_filename).read()
_ins_filename = "loc_instruct.rst"
LOC_INSTRUCTIONS = open(_ins_filename).read()
LOCALIZER_FILE = "localizer.csv"
IMAGE_LIST = "imagelist.txt"
STIM_PATHS = "OBJECTSALL"

FONT_SIZE = 35

LOC_STIM_DUR = 0.500
LOC_INTER_STIM_DUR = 1.0

MAIN_STIM_DUR = 2.0
MAIN_INTER_JITTER = 1.0
MAIN_INTER_STIM_DUR = 0.50

BUTTON_BOX_KEYS = ["_1", "_2"]
LOC_KEYS = ["_1", "_2"]
TR_KEYS = ["_5"]
RUN_START_KEYS = ["0"]

MD_NUM_VAR = 3
MD_DUR = 20
MD_PRAC_DUR = 12
MD_PAM = True  # plus AND minus?
MD_KEYS = {'True': BUTTON_BOX_KEYS[0],
           'False': BUTTON_BOX_KEYS[1]}
