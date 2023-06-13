from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_radial_probe_screen import SETUP_VALIDATE_RP1_FULLSCALE_LABEL
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_radial_probe_screen import SETUP_VALIDATE_RP2_FULLSCALE_LABEL
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_radial_probe_screen import SETUP_VALIDATE_COL_FULLSCALE_LABEL
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_radial_probe_screen import SETUP_VALIDATE_BS1_FULLSCALE_LABEL
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_radial_probe_screen import SETUP_VALIDATE_RP1_CURRENT_FEEDBACK
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_radial_probe_screen import SETUP_VALIDATE_RP2_CURRENT_FEEDBACK
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_radial_probe_screen import SETUP_VALIDATE_COL_CURRENT_FEEDBACK
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_radial_probe_screen import SETUP_VALIDATE_BS1_CURRENT_FEEDBACK
from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import * 

class VALIDATE_RP1_FULLSCALE_LABEL(SETUP_VALIDATE_RP1_FULLSCALE_LABEL): pass
class VALIDATE_RP2_FULLSCALE_LABEL(SETUP_VALIDATE_RP2_FULLSCALE_LABEL): pass
class VALIDATE_COL_FULLSCALE_LABEL(SETUP_VALIDATE_COL_FULLSCALE_LABEL): pass
class VALIDATE_BS1_FULLSCALE_LABEL(SETUP_VALIDATE_BS1_FULLSCALE_LABEL): pass
class VALIDATE_RP1_CURRENT_FEEDBACK(SETUP_VALIDATE_RP1_CURRENT_FEEDBACK): pass
class VALIDATE_RP2_CURRENT_FEEDBACK(SETUP_VALIDATE_RP2_CURRENT_FEEDBACK): pass
class VALIDATE_COL_CURRENT_FEEDBACK(SETUP_VALIDATE_COL_CURRENT_FEEDBACK): pass
class VALIDATE_BS1_CURRENT_FEEDBACK(SETUP_VALIDATE_BS1_CURRENT_FEEDBACK): pass

class SET_VISIBLE_CALIBRATION_LABEL(SETUP_SET_VARIABLE):
    name = "Set a variable to make the cabliration label invisible"
    var_name = "mcr_ecubtcu_bcm1_calibration_status"
    value = 1.0

class SET_BCM1_DATA_TYPE(SETUP_SET_VARIABLE):
    name = "Set BCM1 data type to 1.0"
    var_name = "mcr_ecubtcu_bcm1_data_type"
    value = 1.0

class SET_RP1_CURRENT_FEEDBACK(SETUP_SET_VARIABLE):
    name = "Set RP1 current feedback to 50.0"
    var_name = "mcr_ecubtcu_rp1_cfeedback"
    value = 50.0

class SET_RP2_CURRENT_FEEDBACK(SETUP_SET_VARIABLE):
    name = "Set RP2 current feedback to 50.0"
    var_name = "mcr_ecubtcu_rp2_cfeedback"
    value = 50.0

class SET_COL_CURRENT_FEEDBACK(SETUP_SET_VARIABLE):
    name = "Set current feedback on Inside Collimator to 50.0"
    var_name = "mcr_ecubtcu_cextr1_cfeedback"
    value = 50.0

class SET_BS1_CURRENT_FEEDBACK(SETUP_SET_VARIABLE):
    name = "Set current feedback on Beam Stop Degrader to 50.0"
    var_name = "mcr_ecubtcu_bs1_cfeedback"
    value = 50.0

class __M_S_RP_30__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Validate fullscale labels "
        info_exchange = [
                        ] 
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [
                        SET_BCM1_DATA_TYPE,
                        VALIDATE_RP1_FULLSCALE_LABEL,
                        VALIDATE_RP2_FULLSCALE_LABEL,
                        VALIDATE_COL_FULLSCALE_LABEL,
                        VALIDATE_BS1_FULLSCALE_LABEL,
                        ]
        self.teardown_path = []

class __M_S_RP_32__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate the current feedback on radial probe 1 "
        info_exchange = [
                        ] 
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [
                        SET_VISIBLE_CALIBRATION_LABEL,
                        SET_RP1_CURRENT_FEEDBACK,
                        VALIDATE_RP1_CURRENT_FEEDBACK,
                        ]
        self.teardown_path = []

class __M_S_RP_33__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate the current feedback on radial probe 2 "
        info_exchange = [
                        ] 
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [
                        SET_VISIBLE_CALIBRATION_LABEL,
                        SET_RP2_CURRENT_FEEDBACK,
                        VALIDATE_RP2_CURRENT_FEEDBACK,
                        ]
        self.teardown_path = []

class __M_S_RP_34__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate the current feedback on Inside Collimator "
        info_exchange = [
                        ] 
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [
                        SET_VISIBLE_CALIBRATION_LABEL,
                        SET_COL_CURRENT_FEEDBACK,
                        VALIDATE_COL_CURRENT_FEEDBACK,
                        ]
        self.teardown_path = []

class __M_S_RP_35__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate the current feedback on Beam Stop Degrader "
        info_exchange = [
                        ] 
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [
                        SET_VISIBLE_CALIBRATION_LABEL,
                        SET_BS1_CURRENT_FEEDBACK,
                        VALIDATE_BS1_CURRENT_FEEDBACK,
                        ]
        self.teardown_path = []