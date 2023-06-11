from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import SETUP_SET_VALIDATE_NUMERIC_VAR_FOREGROUND_COLOR
from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import SETUP_CONSTANT
import random
class SET_VALIDATE_NUMERIC_VAR_FOREGROUND_COLOR_0(SETUP_SET_VALIDATE_NUMERIC_VAR_FOREGROUND_COLOR):
    variable_name = "tr4_allocation_status"
    variable_set = random.uniform(0,0.5)
    object_name = "mcr1_beamrequest_tr3b"
    color_code = SETUP_CONSTANT.GRAY_COLOR;
class SET_VALIDATE_NUMERIC_VAR_FOREGROUND_COLOR_1(SETUP_SET_VALIDATE_NUMERIC_VAR_FOREGROUND_COLOR):
    variable_name = "tr4_allocation_status"
    variable_set = random.uniform(0.6,1.5)
    object_name = "mcr1_beamrequest_tr3b"
    color_code = SETUP_CONSTANT.ORANGE_COLOR
class SET_VALIDATE_NUMERIC_VAR_FOREGROUND_COLOR_2(SETUP_SET_VALIDATE_NUMERIC_VAR_FOREGROUND_COLOR):
    variable_name = "tr4_allocation_status"
    variable_set = random.uniform(1.6,2)
    object_name = "mcr1_beamrequest_tr3b"
    color_code = SETUP_CONSTANT.GREEN_COLOR
class __M_T_BC_17__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = 'Simulate and Validate TR1 led status.'
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [ 
                        SET_VALIDATE_NUMERIC_VAR_FOREGROUND_COLOR_0,
                        SET_VALIDATE_NUMERIC_VAR_FOREGROUND_COLOR_1,
                        SET_VALIDATE_NUMERIC_VAR_FOREGROUND_COLOR_2,
                        ]
        self.teardown_path = []
        