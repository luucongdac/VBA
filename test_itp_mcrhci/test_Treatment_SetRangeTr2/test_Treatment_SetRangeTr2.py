from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *


from procedures.thriver.test_itp_mcrhci.test_Treatment_SetRangeTr2.test_Treatment_SetRangeTr2_test_cases.M_T_SRTR2_Navigate_To_Treatment_Set_Range_Tr2 import __M_T_SRTR2_1__
from procedures.thriver.test_itp_mcrhci.test_Treatment_SetRangeTr2.test_Treatment_SetRangeTr2_test_cases.M_T_SRTR2_Display_Text import __M_T_SRTR2_50__
from procedures.thriver.test_itp_mcrhci.test_Treatment_SetRangeTr2.test_Treatment_SetRangeTr2_test_cases.M_T_SRTR2_Display_Text import __M_T_SRTR2_51__
from procedures.thriver.test_itp_mcrhci.test_Treatment_SetRangeTr2.test_Treatment_SetRangeTr2_test_cases.M_T_SRTR2_Display_Text import __M_T_SRTR2_53__
from procedures.thriver.test_itp_mcrhci.test_Treatment_SetRangeTr2.test_Treatment_SetRangeTr2_test_cases.M_T_SRTR2_Display_Text import __M_T_SRTR2_54__
from procedures.thriver.test_itp_mcrhci.test_Treatment_SetRangeTr2.test_Treatment_SetRangeTr2_test_cases.M_T_SRTR2_Display_Text import __M_T_SRTR2_55__
from procedures.thriver.test_itp_mcrhci.test_Treatment_SetRangeTr2.test_Treatment_SetRangeTr2_test_cases.M_T_SRTR2_Display_Text import __M_T_SRTR2_56__
from procedures.thriver.test_itp_mcrhci.test_Treatment_SetRangeTr2.test_Treatment_SetRangeTr2_test_cases.M_T_SRTR2_Display_Text import __M_T_SRTR2_57__
from procedures.thriver.test_itp_mcrhci.test_Treatment_SetRangeTr2.test_Treatment_SetRangeTr2_test_cases.M_T_SRTR2_Display_Text import __M_T_SRTR2_59__
from procedures.thriver.test_itp_mcrhci.test_Treatment_SetRangeTr2.test_Treatment_SetRangeTr2_test_cases.M_T_SRTR2_Display_Text import __M_T_SRTR2_60__
from procedures.thriver.test_itp_mcrhci.test_Treatment_SetRangeTr2.test_Treatment_SetRangeTr2_test_cases.M_T_SRTR2_Click_Button import __M_T_SRTR2_2__
from procedures.thriver.test_itp_mcrhci.test_Treatment_SetRangeTr2.test_Treatment_SetRangeTr2_test_cases.M_T_SRTR2_Click_Button import __M_T_SRTR2_3__
from procedures.thriver.test_itp_mcrhci.test_Treatment_SetRangeTr2.test_Treatment_SetRangeTr2_test_cases.M_T_SRTR2_Click_Button import __M_T_SRTR2_58__

class test_Treatment_SetRangeTr2(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "test_Treatment_SetRangeTr2"
        treatment_test_list = [
                              "mcr_treatment_main_menu",
                              "pts_layout",
                              "tune_iseu",
                              "mcr_treatment_set_range2",                              
                              ]
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange, treatment_test_list=treatment_test_list)
        self.applicable_rooms = ['mcr']
        self.setup =    [  
                        __M_T_SRTR2_1__,
                        __M_T_SRTR2_2__,
                        __M_T_SRTR2_3__,
                        __M_T_SRTR2_50__,
                        # __M_T_SRTR2_51__,
                        __M_T_SRTR2_53__,
                        __M_T_SRTR2_54__,
                        __M_T_SRTR2_55__,
                        __M_T_SRTR2_56__,
                        __M_T_SRTR2_57__,
                        __M_T_SRTR2_58__,                        
                        __M_T_SRTR2_59__,
                        __M_T_SRTR2_60__,
                        ]
        self.teardown_path = []