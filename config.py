import os

_ins_path = "instructions"
_main_ins_filename = "main_instruct.rst"
_mathd_ins_filename = "mathd_instruct.rst"
_study_ins_filename = "study_instruct.rst"
_test_ins_filename = "test_instruct.rst"
_loc_ins_filename = "loc_instruct.rst"

MAIN_INSTRUCTIONS = open(os.path.join(_ins_path,
                                      _main_ins_filename)).read()
MAIN_STUDY_INSTRUCTIONS = open(os.path.join(_ins_path,
                                            _study_ins_filename)).read()
MAIN_TEST_INSTRUCTIONS = open(os.path.join(_ins_path,
                                           _test_ins_filename)).read()
MAIN_MATHD_INSTRUCTIONS = open(os.path.join(_ins_path,
                                            _mathd_ins_filename)).read()
LOC_INSTRUCTIONS = open(os.path.join(_ins_path,
                                     _loc_ins_filename)).read()

LOCALIZER_FILE = "localizer.csv"
IMAGE_LIST = "imagelist.txt"
STIM_PATHS = "OBJECTSALL"

FONT_SIZE = 35
RST_FONT_SIZE = 35
LOC_STIM_DUR = 0.500
LOC_INTER_STIM_DUR = 0.500

MAIN_STIM_DUR = 2.0
MAIN_INTER_JITTER = 4.0
MAIN_INTER_STIM_DUR = 2.0
RESP_DELAY = 0.200
RESP_DUR = 2.0
ISI_DUR = 2.0
ISI_JIT = 4.0

MAIN_NUM_BLOCKS = 5
MAIN_NUM_TARGETS = 30

BUTTON_BOX_KEYS = ["1", "2", "3", "4"]#["_1", "_2", "_3", "_4"]
LOC_KEYS = ["1", "2"]#["_1", "_2"]
TR_KEYS = ["5"]#["_5"]
RUN_START_KEYS = ["0"]

MD_NUM_VAR = 3
MD_DUR = 20
MD_PRAC_DUR = 12
MD_PAM = True  # plus AND minus?
MD_KEYS = {'True': BUTTON_BOX_KEYS[0],
           'False': BUTTON_BOX_KEYS[1]}
