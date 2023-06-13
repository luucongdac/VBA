from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_thriver_wait import SETUP_THRIVER_WAIT
from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import *

class THRIVER_WAIT_10_SECONDS(SETUP_THRIVER_WAIT):
    time = 10

class SET_VARIABLE_SHORT_INVISIBLE(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_couch_short"
    value    = False

class SET_VARIABLE_SHORT_VISIBLE(SETUP_SET_VARIABLE):
    var_name = "tr2_pcu_couch_short"
    value    = True

class VALIDATE_SHORT_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl2:pcu4_couchshort"
    expected_value = "0"
    info_type = "TMMI_MCR_IS_VISIBLE"

class VALIDATE_SHORT_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl2:pcu4_couchshort"
    expected_value = "1"
    info_type = "TMMI_MCR_IS_VISIBLE"

class __M_Tr_PC2_39__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Validate visibility of label Short in Treatment PPS Ctrl2 screen"
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [  
                        SET_VARIABLE_SHORT_VISIBLE,
                        VALIDATE_SHORT_VISIBLE,
                        SET_VARIABLE_SHORT_INVISIBLE,
                        VALIDATE_SHORT_INVISIBLE,
                        ]
        self.teardown_path = []
