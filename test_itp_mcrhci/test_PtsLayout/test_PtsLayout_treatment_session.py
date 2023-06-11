from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.test_PtsLayout.test_PtsLayout_test_cases.M_PL_50 import __M_PL_50__
from procedures.thriver.test_itp_mcrhci.test_PtsLayout.test_PtsLayout_test_cases.M_PL_51 import __M_PL_51__
from procedures.thriver.test_itp_mcrhci.test_PtsLayout.test_PtsLayout_test_cases.M_PL_52 import __M_PL_52__
from procedures.thriver.test_itp_mcrhci.test_PtsLayout.test_PtsLayout_test_cases.M_PL_53 import __M_PL_53__
from procedures.thriver.test_itp_mcrhci.test_PtsLayout.test_PtsLayout_test_cases.M_PL_54 import __M_PL_54__
from procedures.thriver.test_itp_mcrhci.test_PtsLayout.test_PtsLayout_test_cases.M_PL_55 import __M_PL_55__
from procedures.thriver.test_itp_mcrhci.test_PtsLayout.test_PtsLayout_test_cases.M_PL_56 import __M_PL_56__
from procedures.thriver.test_itp_mcrhci.test_PtsLayout.test_PtsLayout_test_cases.M_PL_57 import __M_PL_57__

class test_PtsLayout_treatment_session(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "test_PtsLayout"
        treatment_test_list =   [
                                "pts_layout",
                                "mcr_treatment_bts1_menu",
                                "mcr_treatment_bts2_menu",
                                "mcr_treatment_bts3_menu",
                                "mcr_treatment_ess_menu",
                                "mcr_treatment_cyclo_menu",
                                "mcr_treatment_main_menu",
                                ]
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange, treatment_test_list=treatment_test_list)
        self.applicable_rooms = ['mcr']
        self.setup =    [  
                        __M_PL_50__,
                        __M_PL_51__,
                        __M_PL_52__,
                        __M_PL_53__,
                        __M_PL_54__,
                        __M_PL_55__,
                        __M_PL_56__,
                        __M_PL_57__
                        ]
        self.teardown_path = []