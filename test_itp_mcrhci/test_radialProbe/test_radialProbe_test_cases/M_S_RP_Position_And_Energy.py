from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_radial_probe_screen import SETUP_VALIDATE_RP_POSITION_FEEDBACK
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_radial_probe_screen import SETUP_VALIDATE_RP_ENERGY_FEEDBACK

from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import * 

class SET_POSITION_FEEDBACK(SETUP_SET_VARIABLE):
    name = "Set position feedback to 200.0"
    var_name = "mcr_acu_radialprobe_mmfeedback"
    value = 200.0

class SET_ENERGY_FEEDBACK(SETUP_SET_VARIABLE):
    name = "Set energy feedback to 100.0"
    var_name = "mcr_rtieacu_radialprobe_energy"
    value = 100.0

class VALIDATE_POSITION_FEEDBACK(SETUP_VALIDATE_RP_POSITION_FEEDBACK): pass
class VALIDATE_ENERGY_FEEDBACK(SETUP_VALIDATE_RP_ENERGY_FEEDBACK): pass    

class __M_S_RP_36__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate Position feedback"
        info_exchange = [
                        ] 
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [
                        SET_POSITION_FEEDBACK,
                        VALIDATE_POSITION_FEEDBACK,
                        ]
        self.teardown_path = []

class __M_S_RP_37__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate Energy feedback"
        info_exchange = [
                        ] 
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [
                        SET_ENERGY_FEEDBACK,
                        VALIDATE_ENERGY_FEEDBACK,
                        ]
        self.teardown_path = []