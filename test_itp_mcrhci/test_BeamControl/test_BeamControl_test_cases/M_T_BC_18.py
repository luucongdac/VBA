from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import SETUP_SET_VALIDATE_NUMERIC_VAR_FOREGROUND_COLOR
from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import SETUP_CONSTANT
import random
class SET_VALIDATE_NUMERIC_VAR_FOREGROUND_COLOR_0(SETUP_SET_VALIDATE_NUMERIC_VAR_FOREGROUND_COLOR):
    variable_name = "tr4_reject_led"
    variable_set = random.uniform(0,0.5)
    object_name = "mcr1_releasetr3b_led"
    color_code = SETUP_CONSTANT.BLACK_COLOR;
class SET_VALIDATE_NUMERIC_VAR_FOREGROUND_COLOR_1(SETUP_SET_VALIDATE_NUMERIC_VAR_FOREGROUND_COLOR):
    variable_name = "tr4_reject_led"
    variable_set = random.uniform(0.6,1)
    object_name = "mcr1_releasetr3b_led"
    color_code = SETUP_CONSTANT.YELLOW_COLOR
    
class __M_T_BC_18__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = 'Simulate and Validate Led status of "Reject" button.'
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [ 
                        SET_VALIDATE_NUMERIC_VAR_FOREGROUND_COLOR_0,
                        SET_VALIDATE_NUMERIC_VAR_FOREGROUND_COLOR_1,                        
                        ]
        self.teardown_path = []