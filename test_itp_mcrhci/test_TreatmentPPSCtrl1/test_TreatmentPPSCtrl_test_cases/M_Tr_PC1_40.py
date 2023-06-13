from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_thriver_wait import SETUP_THRIVER_WAIT
from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import *

class THRIVER_WAIT_10_SECONDS(SETUP_THRIVER_WAIT):
    time = 10

class SET_VARIABLE_LONG_INVISIBLE(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_couch_long"
    value    = False

class SET_VARIABLE_LONG_VISIBLE(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_couch_long"
    value    = True

class VALIDATE_LONG_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl1:pcu4_couchlong"
    expected_value = "0"
    info_type = "TMMI_MCR_IS_VISIBLE"

class VALIDATE_LONG_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
    object_name = "mcr_treatment_pps_ctrl1:pcu4_couchlong"
    expected_value = "1"
    info_type = "TMMI_MCR_IS_VISIBLE"

class __M_Tr_PC1_40__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Validate visibility of label Long in Treatment PPS Ctrl1 screen"
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [  
                        SET_VARIABLE_LONG_VISIBLE,
                        VALIDATE_LONG_VISIBLE,
                        SET_VARIABLE_LONG_INVISIBLE,
                        VALIDATE_LONG_INVISIBLE,
                        ]
        self.teardown_path = []
