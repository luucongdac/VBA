from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *


from procedures.thriver.test_itp_mcrhci.test_LoadcellGraph1.test_LoadcellGraph1_test_cases.M_T_LG1_navigateToLG1 import __M_T_LG1_1__
from procedures.thriver.test_itp_mcrhci.test_LoadcellGraph1.test_LoadcellGraph1_test_cases.M_T_LG1_showForceX    import __M_T_LG1_2__
from procedures.thriver.test_itp_mcrhci.test_LoadcellGraph1.test_LoadcellGraph1_test_cases.M_T_LG1_unShowForceX  import __M_T_LG1_3__
from procedures.thriver.test_itp_mcrhci.test_LoadcellGraph1.test_LoadcellGraph1_test_cases.M_T_LG1_showForceZ    import __M_T_LG1_4__
from procedures.thriver.test_itp_mcrhci.test_LoadcellGraph1.test_LoadcellGraph1_test_cases.M_T_LG1_unShowForceZ  import __M_T_LG1_5__
from procedures.thriver.test_itp_mcrhci.test_LoadcellGraph1.test_LoadcellGraph1_test_cases.M_T_LG1_showTorqueX   import __M_T_LG1_6__
from procedures.thriver.test_itp_mcrhci.test_LoadcellGraph1.test_LoadcellGraph1_test_cases.M_T_LG1_unShowTorqueX import __M_T_LG1_7__
from procedures.thriver.test_itp_mcrhci.test_LoadcellGraph1.test_LoadcellGraph1_test_cases.M_T_LG1_showTorqueY   import __M_T_LG1_8__
from procedures.thriver.test_itp_mcrhci.test_LoadcellGraph1.test_LoadcellGraph1_test_cases.M_T_LG1_unShowTorqueY import __M_T_LG1_9__
from procedures.thriver.test_itp_mcrhci.test_LoadcellGraph1.test_LoadcellGraph1_test_cases.M_T_LG1_showTorqueZ   import __M_T_LG1_10__
from procedures.thriver.test_itp_mcrhci.test_LoadcellGraph1.test_LoadcellGraph1_test_cases.M_T_LG1_unShowTorqueZ import __M_T_LG1_11__

class test_LoadcellGraph1(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "test_LoadcellGraph1"
        treatment_test_list = ["mcr_treatment_beam_control",
                               "mcr_treatment_set_range1",
                               "mcr_treatment_beam_tuning",
                               "mcr_treatment_beam_menu",
                               "mcr_treatment_main_menu",
                               "mcr_treatment_pps_ctrl1",
                               "mcr_treatment_pps_loadcell_graph1",
                               "pts_layout",]
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange, treatment_test_list=treatment_test_list)
        self.applicable_rooms = ['mcr']
        self.setup =    [  
                        __M_T_LG1_1__,
                        __M_T_LG1_2__,
                        __M_T_LG1_3__,
                        __M_T_LG1_4__,
                        __M_T_LG1_5__,
                        __M_T_LG1_6__,
                        __M_T_LG1_7__,
                        __M_T_LG1_8__,
                        __M_T_LG1_9__,
                        __M_T_LG1_10__,
                        __M_T_LG1_11__,
                        ]
        self.teardown_path = []
