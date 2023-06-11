from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *


from procedures.thriver.test_itp_mcrhci.test_Treatment_SetRangeTr1.test_Treatment_SetRangeTr1_test_cases.M_T_SRTR1_Navigate_To_Treatment_Set_Range_Tr1 import __M_T_SRTR1_1__
from procedures.thriver.test_itp_mcrhci.test_Treatment_SetRangeTr1.test_Treatment_SetRangeTr1_test_cases.M_T_SRTR1_Display_Text import __M_T_SRTR1_43__
from procedures.thriver.test_itp_mcrhci.test_Treatment_SetRangeTr1.test_Treatment_SetRangeTr1_test_cases.M_T_SRTR1_Display_Text import __M_T_SRTR1_44__
from procedures.thriver.test_itp_mcrhci.test_Treatment_SetRangeTr1.test_Treatment_SetRangeTr1_test_cases.M_T_SRTR1_Display_Text import __M_T_SRTR1_46__
from procedures.thriver.test_itp_mcrhci.test_Treatment_SetRangeTr1.test_Treatment_SetRangeTr1_test_cases.M_T_SRTR1_Display_Text import __M_T_SRTR1_47__
from procedures.thriver.test_itp_mcrhci.test_Treatment_SetRangeTr1.test_Treatment_SetRangeTr1_test_cases.M_T_SRTR1_Display_Text import __M_T_SRTR1_48__
from procedures.thriver.test_itp_mcrhci.test_Treatment_SetRangeTr1.test_Treatment_SetRangeTr1_test_cases.M_T_SRTR1_Display_Text import __M_T_SRTR1_49__
from procedures.thriver.test_itp_mcrhci.test_Treatment_SetRangeTr1.test_Treatment_SetRangeTr1_test_cases.M_T_SRTR1_Display_Text import __M_T_SRTR1_50__
from procedures.thriver.test_itp_mcrhci.test_Treatment_SetRangeTr1.test_Treatment_SetRangeTr1_test_cases.M_T_SRTR1_Click_Button import __M_T_SRTR1_2__
from procedures.thriver.test_itp_mcrhci.test_Treatment_SetRangeTr1.test_Treatment_SetRangeTr1_test_cases.M_T_SRTR1_Click_Button import __M_T_SRTR1_3__
from procedures.thriver.test_itp_mcrhci.test_Treatment_SetRangeTr1.test_Treatment_SetRangeTr1_test_cases.M_T_SRTR1_Click_Button import __M_T_SRTR1_51__

class test_Treatment_SetRangeTr1(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "test_Treatment_SetRangeTr1"
        treatment_test_list = [
                              "mcr_treatment_main_menu",
                              "pts_layout",
                              "tune_iseu",
                              "mcr_treatment_set_range1",                              
                              ]
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange, treatment_test_list=treatment_test_list)
        self.applicable_rooms = ['mcr']
        self.setup =    [  
                        __M_T_SRTR1_1__,
                        __M_T_SRTR1_2__,
                        __M_T_SRTR1_3__,
                        __M_T_SRTR1_43__,
                        # __M_T_SRTR1_44__,
                        __M_T_SRTR1_46__,
                        __M_T_SRTR1_47__,
                        __M_T_SRTR1_48__,
                        __M_T_SRTR1_49__,
                        __M_T_SRTR1_50__,
                        __M_T_SRTR1_51__,
                        ]
        self.teardown_path = []