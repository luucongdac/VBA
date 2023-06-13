from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *


from procedures.thriver.test_itp_mcrhci.test_LoadcellGraph2.test_LoadcellGraph2_test_cases.M_T_LG2_navigateToLG2 import __M_T_LG2_1__
from procedures.thriver.test_itp_mcrhci.test_LoadcellGraph2.test_LoadcellGraph2_test_cases.M_T_LG2_showForceX    import __M_T_LG2_2__
from procedures.thriver.test_itp_mcrhci.test_LoadcellGraph2.test_LoadcellGraph2_test_cases.M_T_LG2_unShowForceX  import __M_T_LG2_3__
from procedures.thriver.test_itp_mcrhci.test_LoadcellGraph2.test_LoadcellGraph2_test_cases.M_T_LG2_showForceZ    import __M_T_LG2_4__
from procedures.thriver.test_itp_mcrhci.test_LoadcellGraph2.test_LoadcellGraph2_test_cases.M_T_LG2_unShowForceZ  import __M_T_LG2_5__
from procedures.thriver.test_itp_mcrhci.test_LoadcellGraph2.test_LoadcellGraph2_test_cases.M_T_LG2_showTorqueX   import __M_T_LG2_6__
from procedures.thriver.test_itp_mcrhci.test_LoadcellGraph2.test_LoadcellGraph2_test_cases.M_T_LG2_unShowTorqueX import __M_T_LG2_7__
from procedures.thriver.test_itp_mcrhci.test_LoadcellGraph2.test_LoadcellGraph2_test_cases.M_T_LG2_showTorqueY   import __M_T_LG2_8__
from procedures.thriver.test_itp_mcrhci.test_LoadcellGraph2.test_LoadcellGraph2_test_cases.M_T_LG2_unShowTorqueY import __M_T_LG2_9__
from procedures.thriver.test_itp_mcrhci.test_LoadcellGraph2.test_LoadcellGraph2_test_cases.M_T_LG2_showTorqueZ   import __M_T_LG2_10__
from procedures.thriver.test_itp_mcrhci.test_LoadcellGraph2.test_LoadcellGraph2_test_cases.M_T_LG2_unShowTorqueZ import __M_T_LG2_11__

class test_LoadcellGraph2(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "test_LoadcellGraph2"
        treatment_test_list = ["mcr_treatment_beam_control",
                               "mcr_treatment_set_range1",
                               "mcr_treatment_beam_tuning",
                               "mcr_treatment_beam_menu",
                               "mcr_treatment_main_menu",
                               "mcr_treatment_pps_ctrl2",
                               "pts_layout",
                               "mcr_treatment_pps_loadcell_graph2",]
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange, treatment_test_list=treatment_test_list)
        self.applicable_rooms = ['mcr']
        self.setup =    [  
                        __M_T_LG2_1__,
                        __M_T_LG2_2__,
                        __M_T_LG2_3__,
                        __M_T_LG2_4__,
                        __M_T_LG2_5__,
                        __M_T_LG2_6__,
                        __M_T_LG2_7__,
                        __M_T_LG2_8__,
                        __M_T_LG2_9__,
                        __M_T_LG2_10__,
                        __M_T_LG2_11__,
                        ]
        self.teardown_path = []
