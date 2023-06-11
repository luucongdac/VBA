from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_radial_probe_screen import SETUP_VALIDATE_RP_GAIN_STATUS
from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import * 


class SET_GAIN_STATUS(SETUP_SET_VARIABLE):
    name = "Set status label to high gain"
    var_name = "mcr_ecubtcu_bcm1_data_type"
    value = 1.0

class VALIDATE_RP_GAIN_STATUS(SETUP_VALIDATE_RP_GAIN_STATUS): pass

class __M_S_RP_28__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate Gain status labels"
        info_exchange = [
                        ] 
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [
                        SET_GAIN_STATUS,
                        VALIDATE_RP_GAIN_STATUS,
                        ]
        self.teardown_path = []
