from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_radial_probe_screen import SETUP_VALIDATE_RP_INIT_POSITION_FEEDBACK
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_radial_probe_screen import SETUP_VALIDATE_RP_SPEED_FEEDBACK
from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import * 

class SET_INIT_POSITION_FEEDBACK(SETUP_SET_VARIABLE):
    name = "Set init position feedback to 100.0"
    var_name = "mcr_acu_radialprobe_initposition"
    value = 100.0

class SET_SPEED_FEEDBACK(SETUP_SET_VARIABLE):
    name = "Set speed feedback to 100.0"
    var_name = "mcr_acu_radialprobe_speedsetpoint"
    value = 100.0

class VALIDATE_INIT_POSITION_FEEDBACK(SETUP_VALIDATE_RP_INIT_POSITION_FEEDBACK): pass
class VALIDATE_SPEED_FEEDBACK(SETUP_VALIDATE_RP_SPEED_FEEDBACK): pass

class __M_S_RP_23__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate Init position feedback"
        info_exchange = [
                        ] 
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [
                        SET_INIT_POSITION_FEEDBACK,
                        VALIDATE_INIT_POSITION_FEEDBACK,
                        ]
        self.teardown_path = []

class __M_S_RP_26__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate Speed feedback"
        info_exchange = [
                        ] 
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [
                        SET_SPEED_FEEDBACK,
                        VALIDATE_SPEED_FEEDBACK,
                        ]
        self.teardown_path = []