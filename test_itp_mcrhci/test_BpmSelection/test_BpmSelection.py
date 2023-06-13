from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *


from procedures.thriver.test_itp_mcrhci.test_BpmSelection.test_BpmSelection_test_cases.M_BPM_1 import __M_BPM_1__
from procedures.thriver.test_itp_mcrhci.test_BpmSelection.test_BpmSelection_test_cases.M_BPM_2 import __M_BPM_2__

class test_BpmSelection(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "test_BpmSelection"
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [
                        __M_BPM_1__,  
                        __M_BPM_2__,  
                        ]
        self.teardown_path = []
