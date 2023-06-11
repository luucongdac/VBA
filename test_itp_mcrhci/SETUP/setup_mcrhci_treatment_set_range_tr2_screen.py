
"""
File:
======================================

This module implements set up path for tcrtrmgr test

Copyright (c) MGH 2023

Test for setup ClinicalIntegrationTestProcedure

"""



from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.infoset.tcsobject.dba_objects import *
from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import * 
from procedures.thriver.test_itp_mcrhci.SETUP.setup_thriver_wait import SETUP_THRIVER_WAIT

class SETUP_VALIDATE_OPEN_TREATMENT_SET_RANGE_TR2(ClinicalIntegrationTestProcedure):
    # default variable values
    name = "Validate Treatment Set Range Tr2 Screen"

    def __init__(self, test):
        cls = type(self)
        name = cls.name
        mcr7_range_feedback_visibility_expected= "1"
        mcr7_range_feedback_value_expected= -1
        mcr7_range_feedback_foreground_color_expected= "3"
        mcr7_range_feedback_background_color_expected= "65"
        mcr7_q9_visibility_expected= "1"
        mcr7_q9_value_expected= 0
        mcr7_q9_foreground_color_expected= "0"
        mcr7_q9_background_color_expected= "0"
        mcr7_q10_visibility_expected= "1"
        mcr7_q10_value_expected= 0
        mcr7_q10_foreground_color_expected= "0"
        mcr7_q10_background_color_expected= "0"
        mcr7_q11_visibility_expected= "1"
        mcr7_q11_value_expected= 0
        mcr7_q11_foreground_color_expected= "0"
        mcr7_q11_background_color_expected= "0"
        mcr7_q12_visibility_expected= "1"
        mcr7_q12_value_expected= 0
        mcr7_q12_foreground_color_expected= "0"
        mcr7_q12_background_color_expected= "0"
        mcr7_q13_visibility_expected= "1"
        mcr7_q13_value_expected= 0
        mcr7_q13_foreground_color_expected= "0"
        mcr7_q13_background_color_expected= "0"
        mcr7_q14_visibility_expected= "1"
        mcr7_q14_value_expected= 0
        mcr7_q14_foreground_color_expected= "0"
        mcr7_q14_background_color_expected= "0"
        mcr7_q15_visibility_expected= "1"
        mcr7_q15_value_expected= 0
        mcr7_q15_foreground_color_expected= "0"
        mcr7_q15_background_color_expected= "0"
        mcr7_q20_visibility_expected= "1"
        mcr7_q20_value_expected= 0
        mcr7_q20_foreground_color_expected= "0"
        mcr7_q20_background_color_expected= "0"
        mcr7_q21_visibility_expected= "1"
        mcr7_q21_value_expected= 0
        mcr7_q21_foreground_color_expected= "0"
        mcr7_q21_background_color_expected= "0"
        mcr7_q22_visibility_expected= "1"
        mcr7_q22_value_expected= 0
        mcr7_q22_foreground_color_expected= "0"
        mcr7_q22_background_color_expected= "0"
        mcr7_b1234_visibility_expected= "1"
        mcr7_b1234_value_expected= 0
        mcr7_b1234_foreground_color_expected= "0"
        mcr7_b1234_background_color_expected= "0"
        mcr7_t6y_visibility_expected= "1"
        mcr7_t6y_value_expected= 0
        mcr7_t6y_foreground_color_expected= "0"
        mcr7_t6y_background_color_expected= "0"
        mcr7_t7y_visibility_expected= "1"
        mcr7_t7y_value_expected= 0
        mcr7_t7y_foreground_color_expected= "0"
        mcr7_t7y_background_color_expected= "0"
        mcr7_trb1_visibility_expected= "1"
        mcr7_trb1_value_expected= 0
        mcr7_trb1_foreground_color_expected= "0"
        mcr7_trb1_background_color_expected= "0"
        mcr7_trb34_visibility_expected= "1"
        mcr7_trb34_value_expected= 0
        mcr7_trb34_foreground_color_expected= "0"
        mcr7_trb34_background_color_expected= "0"
        mcr7_q35_visibility_expected= "1"
        mcr7_q35_value_expected= 0
        mcr7_q35_foreground_color_expected= "0"
        mcr7_q35_background_color_expected= "0"
        mcr7_q36_visibility_expected= "1"
        mcr7_q36_value_expected= 0
        mcr7_q36_foreground_color_expected= "0"
        mcr7_q36_background_color_expected= "0"
        mcr7_q37_visibility_expected= "1"
        mcr7_q37_value_expected= 0
        mcr7_q37_foreground_color_expected= "0"
        mcr7_q37_background_color_expected= "0"
        mcr7_b78_visibility_expected= "1"
        mcr7_b78_value_expected= 0
        mcr7_b78_foreground_color_expected= "0"
        mcr7_b78_background_color_expected= "0"
        mcr7_trb7_visibility_expected= "1"
        mcr7_trb7_value_expected= 0
        mcr7_trb7_foreground_color_expected= "0"
        mcr7_trb7_background_color_expected= "0"
        mcr7_trb8_visibility_expected= "1"
        mcr7_trb8_value_expected= 0
        mcr7_trb8_foreground_color_expected= "0"
        mcr7_trb8_background_color_expected= "0"
        mcr7_q0m2_visibility_expected= "1"
        mcr7_q0m2_value_expected= 0
        mcr7_q0m2_foreground_color_expected= "0"
        mcr7_q0m2_background_color_expected= "0"
        mcr7_q1m2_visibility_expected= "1"
        mcr7_q1m2_value_expected= 0
        mcr7_q1m2_foreground_color_expected= "0"
        mcr7_q1m2_background_color_expected= "0"
        mcr7_q2m2_visibility_expected= "1"
        mcr7_q2m2_value_expected= 0
        mcr7_q2m2_foreground_color_expected= "0"
        mcr7_q2m2_background_color_expected= "0"
        mcr7_q3m2_visibility_expected= "1"
        mcr7_q3m2_value_expected= 0
        mcr7_q3m2_foreground_color_expected= "0"
        mcr7_q3m2_background_color_expected= "0"
        mcr7_q1g2_visibility_expected= "1"
        mcr7_q1g2_value_expected= 0
        mcr7_q1g2_foreground_color_expected= "0"
        mcr7_q1g2_background_color_expected= "0"
        mcr7_q2g2_visibility_expected= "1"
        mcr7_q2g2_value_expected= 0
        mcr7_q2g2_foreground_color_expected= "0"
        mcr7_q2g2_background_color_expected= "0"
        mcr7_q3g2_visibility_expected= "1"
        mcr7_q3g2_value_expected= 0
        mcr7_q3g2_foreground_color_expected= "0"
        mcr7_q3g2_background_color_expected= "0"
        mcr7_q4g2_visibility_expected= "1"
        mcr7_q4g2_value_expected= 0
        mcr7_q4g2_foreground_color_expected= "0"
        mcr7_q4g2_background_color_expected= "0"
        mcr7_q5g2_visibility_expected= "1"
        mcr7_q5g2_value_expected= 0
        mcr7_q5g2_foreground_color_expected= "0"
        mcr7_q5g2_background_color_expected= "0"
        mcr7_b1g2_visibility_expected= "1"
        mcr7_b1g2_value_expected= 0
        mcr7_b1g2_foreground_color_expected= "0"
        mcr7_b1g2_background_color_expected= "0"
        mcr7_b2g2_visibility_expected= "1"
        mcr7_b2g2_value_expected= 0
        mcr7_b2g2_foreground_color_expected= "0"
        mcr7_b2g2_background_color_expected= "0"
        mcr7_t9g2_visibility_expected= "1"
        mcr7_t9g2_value_expected= 0
        mcr7_t9g2_foreground_color_expected= "0"
        mcr7_t9g2_background_color_expected= "0"
        mcr7_t10g2_visibility_expected= "1"
        mcr7_t10g2_value_expected= 0
        mcr7_t10g2_foreground_color_expected= "0"
        mcr7_t10g2_background_color_expected= "0"
        Label1_visibility_expected= "1"
        Label1_foreground_color_expected= "0"
        Label1_background_color_expected= "65"
        mcr7_range_energy_visibility_expected= "1"
        mcr7_range_energy_value_expected= 0
        mcr7_range_energy_foreground_color_expected= "3"
        mcr7_range_energy_background_color_expected= "65"
        Label2_visibility_expected= "1"
        Label2_foreground_color_expected= "0"
        Label2_background_color_expected= "65"
        feedback_rectangle_visibility_expected= "1"
        feedback_rectangle_foreground_color_expected= "0"
        feedback_rectangle_background_color_expected= "0"
        mcr7_global_range_status_visibility_expected= "1"
        mcr7_global_range_status_value_expected= 0
        mcr7_global_range_status_foreground_color_expected= "0"
        mcr7_global_range_status_background_color_expected= "0"
        mcr7_range_field_visibility_expected= "1"
        mcr7_range_field_value_expected= 0
        mcr7_range_field_foreground_color_expected= "3"
        mcr7_range_field_background_color_expected= "65"
        mcr7_sl1x_visibility_expected= "1"
        mcr7_sl1x_value_expected= 0
        mcr7_sl1x_foreground_color_expected= "0"
        mcr7_sl1x_background_color_expected= "0"
        mcr7_sl1y_visibility_expected= "1"
        mcr7_sl1y_value_expected= 0
        mcr7_sl1y_foreground_color_expected= "0"
        mcr7_sl1y_background_color_expected= "0"
        mcr7_sl2x_visibility_expected= "1"
        mcr7_sl2x_value_expected= 0
        mcr7_sl2x_foreground_color_expected= "0"
        mcr7_sl2x_background_color_expected= "0"
        mcr7_graphite_step_label_visibility_expected= "0"
        mcr7_graphite_step_label_value_expected= 0
        mcr7_graphite_step_label_foreground_color_expected= "3"
        mcr7_graphite_step_label_background_color_expected= "65"
        mcr7_iseu2btn_visibility_expected= "1"
        mcr7_iseu2btn_foreground_color_expected= "0"
        mcr7_iseu2btn_background_color_expected= "0"
        mcr7_graphite_step_visibility_expected= "0"
        mcr7_graphite_step_value_expected= 0
        mcr7_graphite_step_foreground_color_expected= "3"
        mcr7_graphite_step_background_color_expected= "65"
        mcr7_setrange2btn_visibility_expected= "1"
        mcr7_setrange2btn_foreground_color_expected= "0"
        mcr7_setrange2btn_background_color_expected= "0"
        mcr7_gantry_angle_visibility_expected= "1"
        mcr7_gantry_angle_value_expected= -1
        mcr7_gantry_angle_foreground_color_expected= "3"
        mcr7_gantry_angle_background_color_expected= "65"
        mcr7_q30_visibility_expected= "1"
        mcr7_q30_value_expected= 0
        mcr7_q30_foreground_color_expected= "0"
        mcr7_q30_background_color_expected= "0"
        mcr7_q31_visibility_expected= "1"
        mcr7_q31_value_expected= 0
        mcr7_q31_foreground_color_expected= "0"
        mcr7_q31_background_color_expected= "0"
        mcr7_q32_visibility_expected= "1"
        mcr7_q32_value_expected= 0
        mcr7_q32_foreground_color_expected= "0"
        mcr7_q32_background_color_expected= "0"
        mcr7_q33_visibility_expected= "1"
        mcr7_q33_value_expected= 0
        mcr7_q33_foreground_color_expected= "0"
        mcr7_q33_background_color_expected= "0"
        mcr7_q34_visibility_expected= "1"
        mcr7_q34_value_expected= 0
        mcr7_q34_foreground_color_expected= "0"
        mcr7_q34_background_color_expected= "0"
        mcr7_t10_visibility_expected= "1"
        mcr7_t10_value_expected= 0
        mcr7_t10_foreground_color_expected= "0"
        mcr7_t10_background_color_expected= "0"
        mcr7_t11_visibility_expected= "1"
        mcr7_t11_value_expected= 0
        mcr7_t11_foreground_color_expected= "0"
        mcr7_t11_background_color_expected= "0"
        mcr7_t12_visibility_expected= "1"
        mcr7_t12_value_expected= 0
        mcr7_t12_foreground_color_expected= "0"
        mcr7_t12_background_color_expected= "0"
        mcr7_degrader_status_visibility_expected= "1"
        mcr7_degrader_status_value_expected= 0
        mcr7_degrader_status_foreground_color_expected= "0"
        mcr7_degrader_status_background_color_expected= "0"
        mcr7_cugantryposfbk_visibility_expected= "1"
        mcr7_cugantryposfbk_value_expected= 0
        mcr7_cugantryposfbk_foreground_color_expected= "3"
        mcr7_cugantryposfbk_background_color_expected= "65"
        DS_US_mode_text_visibility_expected= "0"
        DS_US_mode_text_foreground_color_expected= "3"
        DS_US_mode_text_background_color_expected= "65"
        PBS_mode_text_visibility_expected= "1"
        PBS_mode_text_foreground_color_expected= "3"
        PBS_mode_text_background_color_expected= "65"
        mcr7_trb5_visibility_expected= "1"
        mcr7_trb5_value_expected= 0
        mcr7_trb5_foreground_color_expected= "0"
        mcr7_trb5_background_color_expected= "0"

        # get values
        get_mcr7_range_feedback_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_range_feedback")
        get_mcr7_range_feedback_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_range_feedback")
        get_mcr7_range_feedback_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_range_feedback")
        get_mcr7_range_feedback_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_range_feedback")
        get_mcr7_q9_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_q9")
        get_mcr7_q9_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_q9")
        get_mcr7_q9_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q9")
        get_mcr7_q9_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q9")
        get_mcr7_q10_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_q10")
        get_mcr7_q10_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_q10")
        get_mcr7_q10_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q10")
        get_mcr7_q10_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q10")
        get_mcr7_q11_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_q11")
        get_mcr7_q11_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_q11")
        get_mcr7_q11_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q11")
        get_mcr7_q11_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q11")
        get_mcr7_q12_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_q12")
        get_mcr7_q12_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_q12")
        get_mcr7_q12_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q12")
        get_mcr7_q12_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q12")
        get_mcr7_q13_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_q13")
        get_mcr7_q13_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_q13")
        get_mcr7_q13_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q13")
        get_mcr7_q13_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q13")
        get_mcr7_q14_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_q14")
        get_mcr7_q14_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_q14")
        get_mcr7_q14_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q14")
        get_mcr7_q14_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q14")
        get_mcr7_q15_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_q15")
        get_mcr7_q15_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_q15")
        get_mcr7_q15_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q15")
        get_mcr7_q15_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q15")
        get_mcr7_q20_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_q20")
        get_mcr7_q20_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_q20")
        get_mcr7_q20_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q20")
        get_mcr7_q20_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q20")
        get_mcr7_q21_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_q21")
        get_mcr7_q21_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_q21")
        get_mcr7_q21_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q21")
        get_mcr7_q21_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q21")
        get_mcr7_q22_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_q22")
        get_mcr7_q22_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_q22")
        get_mcr7_q22_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q22")
        get_mcr7_q22_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q22")
        get_mcr7_b1234_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_b1234")
        get_mcr7_b1234_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_b1234")
        get_mcr7_b1234_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_b1234")
        get_mcr7_b1234_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_b1234")
        get_mcr7_t6y_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_t6y")
        get_mcr7_t6y_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_t6y")
        get_mcr7_t6y_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_t6y")
        get_mcr7_t6y_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_t6y")
        get_mcr7_t7y_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_t7y")
        get_mcr7_t7y_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_t7y")
        get_mcr7_t7y_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_t7y")
        get_mcr7_t7y_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_t7y")
        get_mcr7_trb1_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_trb1")
        get_mcr7_trb1_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_trb1")
        get_mcr7_trb1_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_trb1")
        get_mcr7_trb1_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_trb1")
        get_mcr7_trb34_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_trb34")
        get_mcr7_trb34_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_trb34")
        get_mcr7_trb34_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_trb34")
        get_mcr7_trb34_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_trb34")
        get_mcr7_q35_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_q35")
        get_mcr7_q35_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_q35")
        get_mcr7_q35_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q35")
        get_mcr7_q35_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q35")
        get_mcr7_q36_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_q36")
        get_mcr7_q36_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_q36")
        get_mcr7_q36_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q36")
        get_mcr7_q36_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q36")
        get_mcr7_q37_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_q37")
        get_mcr7_q37_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_q37")
        get_mcr7_q37_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q37")
        get_mcr7_q37_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q37")
        get_mcr7_b78_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_b78")
        get_mcr7_b78_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_b78")
        get_mcr7_b78_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_b78")
        get_mcr7_b78_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_b78")
        get_mcr7_trb7_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_trb7")
        get_mcr7_trb7_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_trb7")
        get_mcr7_trb7_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_trb7")
        get_mcr7_trb7_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_trb7")
        get_mcr7_trb8_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_trb8")
        get_mcr7_trb8_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_trb8")
        get_mcr7_trb8_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_trb8")
        get_mcr7_trb8_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_trb8")
        get_mcr7_q0m2_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_q0m2")
        get_mcr7_q0m2_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_q0m2")
        get_mcr7_q0m2_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q0m2")
        get_mcr7_q0m2_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q0m2")
        get_mcr7_q1m2_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_q1m2")
        get_mcr7_q1m2_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_q1m2")
        get_mcr7_q1m2_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q1m2")
        get_mcr7_q1m2_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q1m2")
        get_mcr7_q2m2_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_q2m2")
        get_mcr7_q2m2_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_q2m2")
        get_mcr7_q2m2_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q2m2")
        get_mcr7_q2m2_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q2m2")
        get_mcr7_q3m2_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_q3m2")
        get_mcr7_q3m2_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_q3m2")
        get_mcr7_q3m2_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q3m2")
        get_mcr7_q3m2_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q3m2")
        get_mcr7_q1g2_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_q1g2")
        get_mcr7_q1g2_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_q1g2")
        get_mcr7_q1g2_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q1g2")
        get_mcr7_q1g2_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q1g2")
        get_mcr7_q2g2_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_q2g2")
        get_mcr7_q2g2_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_q2g2")
        get_mcr7_q2g2_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q2g2")
        get_mcr7_q2g2_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q2g2")
        get_mcr7_q3g2_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_q3g2")
        get_mcr7_q3g2_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_q3g2")
        get_mcr7_q3g2_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q3g2")
        get_mcr7_q3g2_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q3g2")
        get_mcr7_q4g2_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_q4g2")
        get_mcr7_q4g2_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_q4g2")
        get_mcr7_q4g2_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q4g2")
        get_mcr7_q4g2_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q4g2")
        get_mcr7_q5g2_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_q5g2")
        get_mcr7_q5g2_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_q5g2")
        get_mcr7_q5g2_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q5g2")
        get_mcr7_q5g2_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q5g2")
        get_mcr7_b1g2_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_b1g2")
        get_mcr7_b1g2_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_b1g2")
        get_mcr7_b1g2_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_b1g2")
        get_mcr7_b1g2_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_b1g2")
        get_mcr7_b2g2_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_b2g2")
        get_mcr7_b2g2_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_b2g2")
        get_mcr7_b2g2_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_b2g2")
        get_mcr7_b2g2_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_b2g2")
        get_mcr7_t9g2_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_t9g2")
        get_mcr7_t9g2_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_t9g2")
        get_mcr7_t9g2_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_t9g2")
        get_mcr7_t9g2_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_t9g2")
        get_mcr7_t10g2_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_t10g2")
        get_mcr7_t10g2_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_t10g2")
        get_mcr7_t10g2_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_t10g2")
        get_mcr7_t10g2_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_t10g2")
        get_Label1_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:Label1")
        get_Label1_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:Label1")
        get_Label1_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:Label1")
        get_mcr7_range_energy_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_range_energy")
        get_mcr7_range_energy_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_range_energy")
        get_mcr7_range_energy_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_range_energy")
        get_mcr7_range_energy_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_range_energy")
        get_Label2_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:Label2")
        get_Label2_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:Label2")
        get_Label2_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:Label2")
        get_feedback_rectangle_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:feedback_rectangle")
        get_feedback_rectangle_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:feedback_rectangle")
        get_feedback_rectangle_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:feedback_rectangle")
        get_mcr7_global_range_status_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_global_range_status")
        get_mcr7_global_range_status_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_global_range_status")
        get_mcr7_global_range_status_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_global_range_status")
        get_mcr7_global_range_status_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_global_range_status")
        get_mcr7_range_field_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_range_field")
        get_mcr7_range_field_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_range_field")
        get_mcr7_range_field_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_range_field")
        get_mcr7_range_field_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_range_field")
        get_mcr7_sl1x_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_sl1x")
        get_mcr7_sl1x_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_sl1x")
        get_mcr7_sl1x_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_sl1x")
        get_mcr7_sl1x_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_sl1x")
        get_mcr7_sl1y_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_sl1y")
        get_mcr7_sl1y_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_sl1y")
        get_mcr7_sl1y_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_sl1y")
        get_mcr7_sl1y_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_sl1y")
        get_mcr7_sl2x_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_sl2x")
        get_mcr7_sl2x_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_sl2x")
        get_mcr7_sl2x_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_sl2x")
        get_mcr7_sl2x_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_sl2x")
        get_mcr7_graphite_step_label_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_graphite_step_label")
        get_mcr7_graphite_step_label_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_graphite_step_label")
        get_mcr7_graphite_step_label_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_graphite_step_label")
        get_mcr7_graphite_step_label_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_graphite_step_label")
        get_mcr7_iseu2btn_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_iseu2btn")
        get_mcr7_iseu2btn_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_iseu2btn")
        get_mcr7_iseu2btn_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_iseu2btn")
        get_mcr7_graphite_step_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_graphite_step")
        get_mcr7_graphite_step_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_graphite_step")
        get_mcr7_graphite_step_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_graphite_step")
        get_mcr7_graphite_step_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_graphite_step")
        get_mcr7_setrange2btn_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_setrange2btn")
        get_mcr7_setrange2btn_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_setrange2btn")
        get_mcr7_setrange2btn_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_setrange2btn")
        get_mcr7_gantry_angle_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_gantry_angle")
        get_mcr7_gantry_angle_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_gantry_angle")
        get_mcr7_gantry_angle_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_gantry_angle")
        get_mcr7_gantry_angle_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_gantry_angle")
        get_mcr7_q30_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_q30")
        get_mcr7_q30_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_q30")
        get_mcr7_q30_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q30")
        get_mcr7_q30_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q30")
        get_mcr7_q31_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_q31")
        get_mcr7_q31_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_q31")
        get_mcr7_q31_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q31")
        get_mcr7_q31_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q31")
        get_mcr7_q32_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_q32")
        get_mcr7_q32_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_q32")
        get_mcr7_q32_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q32")
        get_mcr7_q32_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q32")
        get_mcr7_q33_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_q33")
        get_mcr7_q33_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_q33")
        get_mcr7_q33_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q33")
        get_mcr7_q33_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q33")
        get_mcr7_q34_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_q34")
        get_mcr7_q34_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_q34")
        get_mcr7_q34_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q34")
        get_mcr7_q34_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_q34")
        get_mcr7_t10_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_t10")
        get_mcr7_t10_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_t10")
        get_mcr7_t10_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_t10")
        get_mcr7_t10_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_t10")
        get_mcr7_t11_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_t11")
        get_mcr7_t11_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_t11")
        get_mcr7_t11_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_t11")
        get_mcr7_t11_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_t11")
        get_mcr7_t12_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_t12")
        get_mcr7_t12_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_t12")
        get_mcr7_t12_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_t12")
        get_mcr7_t12_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_t12")
        get_mcr7_degrader_status_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_degrader_status")
        get_mcr7_degrader_status_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_degrader_status")
        get_mcr7_degrader_status_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_degrader_status")
        get_mcr7_degrader_status_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_degrader_status")
        get_mcr7_cugantryposfbk_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_cugantryposfbk")
        get_mcr7_cugantryposfbk_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_cugantryposfbk")
        get_mcr7_cugantryposfbk_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_cugantryposfbk")
        get_mcr7_cugantryposfbk_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_cugantryposfbk")
        get_DS_US_mode_text_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:DS_US_mode_text")
        get_DS_US_mode_text_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:DS_US_mode_text")
        get_DS_US_mode_text_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:DS_US_mode_text")
        get_PBS_mode_text_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:PBS_mode_text")
        get_PBS_mode_text_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:PBS_mode_text")
        get_PBS_mode_text_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:PBS_mode_text")
        get_mcr7_trb5_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_set_range2:mcr7_trb5")
        get_mcr7_trb5_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_set_range2:mcr7_trb5")
        get_mcr7_trb5_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_trb5")
        get_mcr7_trb5_background_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_set_range2:mcr7_trb5")

        # validate
        validate_mcr7_range_feedback_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_range_feedback:TMMI_MCR_IS_VISIBLE", value=mcr7_range_feedback_visibility_expected)
        validate_mcr7_range_feedback_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_range_feedback:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_range_feedback_value_expected)
        validate_mcr7_range_feedback_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_range_feedback:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_range_feedback_foreground_color_expected)
        validate_mcr7_range_feedback_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_range_feedback:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_range_feedback_background_color_expected)
        validate_mcr7_q9_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_q9:TMMI_MCR_IS_VISIBLE", value=mcr7_q9_visibility_expected)
        validate_mcr7_q9_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_q9:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_q9_value_expected)
        validate_mcr7_q9_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q9:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_q9_foreground_color_expected)
        validate_mcr7_q9_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q9:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_q9_background_color_expected)
        validate_mcr7_q10_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_q10:TMMI_MCR_IS_VISIBLE", value=mcr7_q10_visibility_expected)
        validate_mcr7_q10_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_q10:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_q10_value_expected)
        validate_mcr7_q10_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q10:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_q10_foreground_color_expected)
        validate_mcr7_q10_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q10:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_q10_background_color_expected)
        validate_mcr7_q11_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_q11:TMMI_MCR_IS_VISIBLE", value=mcr7_q11_visibility_expected)
        validate_mcr7_q11_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_q11:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_q11_value_expected)
        validate_mcr7_q11_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q11:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_q11_foreground_color_expected)
        validate_mcr7_q11_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q11:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_q11_background_color_expected)
        validate_mcr7_q12_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_q12:TMMI_MCR_IS_VISIBLE", value=mcr7_q12_visibility_expected)
        validate_mcr7_q12_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_q12:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_q12_value_expected)
        validate_mcr7_q12_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q12:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_q12_foreground_color_expected)
        validate_mcr7_q12_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q12:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_q12_background_color_expected)
        validate_mcr7_q13_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_q13:TMMI_MCR_IS_VISIBLE", value=mcr7_q13_visibility_expected)
        validate_mcr7_q13_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_q13:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_q13_value_expected)
        validate_mcr7_q13_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q13:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_q13_foreground_color_expected)
        validate_mcr7_q13_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q13:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_q13_background_color_expected)
        validate_mcr7_q14_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_q14:TMMI_MCR_IS_VISIBLE", value=mcr7_q14_visibility_expected)
        validate_mcr7_q14_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_q14:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_q14_value_expected)
        validate_mcr7_q14_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q14:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_q14_foreground_color_expected)
        validate_mcr7_q14_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q14:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_q14_background_color_expected)
        validate_mcr7_q15_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_q15:TMMI_MCR_IS_VISIBLE", value=mcr7_q15_visibility_expected)
        validate_mcr7_q15_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_q15:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_q15_value_expected)
        validate_mcr7_q15_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q15:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_q15_foreground_color_expected)
        validate_mcr7_q15_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q15:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_q15_background_color_expected)
        validate_mcr7_q20_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_q20:TMMI_MCR_IS_VISIBLE", value=mcr7_q20_visibility_expected)
        validate_mcr7_q20_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_q20:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_q20_value_expected)
        validate_mcr7_q20_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q20:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_q20_foreground_color_expected)
        validate_mcr7_q20_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q20:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_q20_background_color_expected)
        validate_mcr7_q21_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_q21:TMMI_MCR_IS_VISIBLE", value=mcr7_q21_visibility_expected)
        validate_mcr7_q21_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_q21:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_q21_value_expected)
        validate_mcr7_q21_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q21:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_q21_foreground_color_expected)
        validate_mcr7_q21_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q21:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_q21_background_color_expected)
        validate_mcr7_q22_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_q22:TMMI_MCR_IS_VISIBLE", value=mcr7_q22_visibility_expected)
        validate_mcr7_q22_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_q22:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_q22_value_expected)
        validate_mcr7_q22_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q22:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_q22_foreground_color_expected)
        validate_mcr7_q22_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q22:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_q22_background_color_expected)
        validate_mcr7_b1234_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_b1234:TMMI_MCR_IS_VISIBLE", value=mcr7_b1234_visibility_expected)
        validate_mcr7_b1234_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_b1234:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_b1234_value_expected)
        validate_mcr7_b1234_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_b1234:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_b1234_foreground_color_expected)
        validate_mcr7_b1234_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_b1234:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_b1234_background_color_expected)
        validate_mcr7_t6y_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_t6y:TMMI_MCR_IS_VISIBLE", value=mcr7_t6y_visibility_expected)
        validate_mcr7_t6y_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_t6y:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_t6y_value_expected)
        validate_mcr7_t6y_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_t6y:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_t6y_foreground_color_expected)
        validate_mcr7_t6y_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_t6y:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_t6y_background_color_expected)
        validate_mcr7_t7y_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_t7y:TMMI_MCR_IS_VISIBLE", value=mcr7_t7y_visibility_expected)
        validate_mcr7_t7y_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_t7y:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_t7y_value_expected)
        validate_mcr7_t7y_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_t7y:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_t7y_foreground_color_expected)
        validate_mcr7_t7y_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_t7y:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_t7y_background_color_expected)
        validate_mcr7_trb1_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_trb1:TMMI_MCR_IS_VISIBLE", value=mcr7_trb1_visibility_expected)
        validate_mcr7_trb1_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_trb1:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_trb1_value_expected)
        validate_mcr7_trb1_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_trb1:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_trb1_foreground_color_expected)
        validate_mcr7_trb1_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_trb1:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_trb1_background_color_expected)
        validate_mcr7_trb34_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_trb34:TMMI_MCR_IS_VISIBLE", value=mcr7_trb34_visibility_expected)
        validate_mcr7_trb34_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_trb34:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_trb34_value_expected)
        validate_mcr7_trb34_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_trb34:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_trb34_foreground_color_expected)
        validate_mcr7_trb34_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_trb34:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_trb34_background_color_expected)
        validate_mcr7_q35_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_q35:TMMI_MCR_IS_VISIBLE", value=mcr7_q35_visibility_expected)
        validate_mcr7_q35_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_q35:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_q35_value_expected)
        validate_mcr7_q35_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q35:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_q35_foreground_color_expected)
        validate_mcr7_q35_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q35:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_q35_background_color_expected)
        validate_mcr7_q36_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_q36:TMMI_MCR_IS_VISIBLE", value=mcr7_q36_visibility_expected)
        validate_mcr7_q36_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_q36:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_q36_value_expected)
        validate_mcr7_q36_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q36:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_q36_foreground_color_expected)
        validate_mcr7_q36_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q36:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_q36_background_color_expected)
        validate_mcr7_q37_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_q37:TMMI_MCR_IS_VISIBLE", value=mcr7_q37_visibility_expected)
        validate_mcr7_q37_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_q37:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_q37_value_expected)
        validate_mcr7_q37_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q37:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_q37_foreground_color_expected)
        validate_mcr7_q37_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q37:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_q37_background_color_expected)
        validate_mcr7_b78_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_b78:TMMI_MCR_IS_VISIBLE", value=mcr7_b78_visibility_expected)
        validate_mcr7_b78_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_b78:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_b78_value_expected)
        validate_mcr7_b78_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_b78:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_b78_foreground_color_expected)
        validate_mcr7_b78_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_b78:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_b78_background_color_expected)
        validate_mcr7_trb7_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_trb7:TMMI_MCR_IS_VISIBLE", value=mcr7_trb7_visibility_expected)
        validate_mcr7_trb7_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_trb7:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_trb7_value_expected)
        validate_mcr7_trb7_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_trb7:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_trb7_foreground_color_expected)
        validate_mcr7_trb7_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_trb7:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_trb7_background_color_expected)
        validate_mcr7_trb8_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_trb8:TMMI_MCR_IS_VISIBLE", value=mcr7_trb8_visibility_expected)
        validate_mcr7_trb8_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_trb8:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_trb8_value_expected)
        validate_mcr7_trb8_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_trb8:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_trb8_foreground_color_expected)
        validate_mcr7_trb8_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_trb8:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_trb8_background_color_expected)
        validate_mcr7_q0m2_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_q0m2:TMMI_MCR_IS_VISIBLE", value=mcr7_q0m2_visibility_expected)
        validate_mcr7_q0m2_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_q0m2:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_q0m2_value_expected)
        validate_mcr7_q0m2_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q0m2:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_q0m2_foreground_color_expected)
        validate_mcr7_q0m2_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q0m2:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_q0m2_background_color_expected)
        validate_mcr7_q1m2_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_q1m2:TMMI_MCR_IS_VISIBLE", value=mcr7_q1m2_visibility_expected)
        validate_mcr7_q1m2_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_q1m2:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_q1m2_value_expected)
        validate_mcr7_q1m2_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q1m2:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_q1m2_foreground_color_expected)
        validate_mcr7_q1m2_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q1m2:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_q1m2_background_color_expected)
        validate_mcr7_q2m2_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_q2m2:TMMI_MCR_IS_VISIBLE", value=mcr7_q2m2_visibility_expected)
        validate_mcr7_q2m2_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_q2m2:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_q2m2_value_expected)
        validate_mcr7_q2m2_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q2m2:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_q2m2_foreground_color_expected)
        validate_mcr7_q2m2_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q2m2:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_q2m2_background_color_expected)
        validate_mcr7_q3m2_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_q3m2:TMMI_MCR_IS_VISIBLE", value=mcr7_q3m2_visibility_expected)
        validate_mcr7_q3m2_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_q3m2:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_q3m2_value_expected)
        validate_mcr7_q3m2_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q3m2:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_q3m2_foreground_color_expected)
        validate_mcr7_q3m2_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q3m2:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_q3m2_background_color_expected)
        validate_mcr7_q1g2_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_q1g2:TMMI_MCR_IS_VISIBLE", value=mcr7_q1g2_visibility_expected)
        validate_mcr7_q1g2_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_q1g2:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_q1g2_value_expected)
        validate_mcr7_q1g2_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q1g2:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_q1g2_foreground_color_expected)
        validate_mcr7_q1g2_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q1g2:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_q1g2_background_color_expected)
        validate_mcr7_q2g2_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_q2g2:TMMI_MCR_IS_VISIBLE", value=mcr7_q2g2_visibility_expected)
        validate_mcr7_q2g2_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_q2g2:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_q2g2_value_expected)
        validate_mcr7_q2g2_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q2g2:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_q2g2_foreground_color_expected)
        validate_mcr7_q2g2_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q2g2:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_q2g2_background_color_expected)
        validate_mcr7_q3g2_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_q3g2:TMMI_MCR_IS_VISIBLE", value=mcr7_q3g2_visibility_expected)
        validate_mcr7_q3g2_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_q3g2:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_q3g2_value_expected)
        validate_mcr7_q3g2_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q3g2:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_q3g2_foreground_color_expected)
        validate_mcr7_q3g2_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q3g2:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_q3g2_background_color_expected)
        validate_mcr7_q4g2_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_q4g2:TMMI_MCR_IS_VISIBLE", value=mcr7_q4g2_visibility_expected)
        validate_mcr7_q4g2_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_q4g2:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_q4g2_value_expected)
        validate_mcr7_q4g2_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q4g2:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_q4g2_foreground_color_expected)
        validate_mcr7_q4g2_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q4g2:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_q4g2_background_color_expected)
        validate_mcr7_q5g2_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_q5g2:TMMI_MCR_IS_VISIBLE", value=mcr7_q5g2_visibility_expected)
        validate_mcr7_q5g2_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_q5g2:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_q5g2_value_expected)
        validate_mcr7_q5g2_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q5g2:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_q5g2_foreground_color_expected)
        validate_mcr7_q5g2_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q5g2:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_q5g2_background_color_expected)
        validate_mcr7_b1g2_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_b1g2:TMMI_MCR_IS_VISIBLE", value=mcr7_b1g2_visibility_expected)
        validate_mcr7_b1g2_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_b1g2:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_b1g2_value_expected)
        validate_mcr7_b1g2_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_b1g2:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_b1g2_foreground_color_expected)
        validate_mcr7_b1g2_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_b1g2:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_b1g2_background_color_expected)
        validate_mcr7_b2g2_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_b2g2:TMMI_MCR_IS_VISIBLE", value=mcr7_b2g2_visibility_expected)
        validate_mcr7_b2g2_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_b2g2:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_b2g2_value_expected)
        validate_mcr7_b2g2_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_b2g2:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_b2g2_foreground_color_expected)
        validate_mcr7_b2g2_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_b2g2:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_b2g2_background_color_expected)
        validate_mcr7_t9g2_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_t9g2:TMMI_MCR_IS_VISIBLE", value=mcr7_t9g2_visibility_expected)
        validate_mcr7_t9g2_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_t9g2:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_t9g2_value_expected)
        validate_mcr7_t9g2_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_t9g2:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_t9g2_foreground_color_expected)
        validate_mcr7_t9g2_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_t9g2:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_t9g2_background_color_expected)
        validate_mcr7_t10g2_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_t10g2:TMMI_MCR_IS_VISIBLE", value=mcr7_t10g2_visibility_expected)
        validate_mcr7_t10g2_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_t10g2:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_t10g2_value_expected)
        validate_mcr7_t10g2_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_t10g2:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_t10g2_foreground_color_expected)
        validate_mcr7_t10g2_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_t10g2:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_t10g2_background_color_expected)
        validate_Label1_visibility= MsgTypeString("mcr_treatment_set_range2:Label1:TMMI_MCR_IS_VISIBLE", value=Label1_visibility_expected)
        validate_Label1_foreground_color= MsgTypeString("mcr_treatment_set_range2:Label1:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=Label1_foreground_color_expected)
        validate_Label1_background_color= MsgTypeString("mcr_treatment_set_range2:Label1:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=Label1_background_color_expected)
        validate_mcr7_range_energy_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_range_energy:TMMI_MCR_IS_VISIBLE", value=mcr7_range_energy_visibility_expected)
        validate_mcr7_range_energy_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_range_energy:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_range_energy_value_expected)
        validate_mcr7_range_energy_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_range_energy:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_range_energy_foreground_color_expected)
        validate_mcr7_range_energy_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_range_energy:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_range_energy_background_color_expected)
        validate_Label2_visibility= MsgTypeString("mcr_treatment_set_range2:Label2:TMMI_MCR_IS_VISIBLE", value=Label2_visibility_expected)
        validate_Label2_foreground_color= MsgTypeString("mcr_treatment_set_range2:Label2:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=Label2_foreground_color_expected)
        validate_Label2_background_color= MsgTypeString("mcr_treatment_set_range2:Label2:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=Label2_background_color_expected)
        validate_feedback_rectangle_visibility= MsgTypeString("mcr_treatment_set_range2:feedback_rectangle:TMMI_MCR_IS_VISIBLE", value=feedback_rectangle_visibility_expected)
        validate_feedback_rectangle_foreground_color= MsgTypeString("mcr_treatment_set_range2:feedback_rectangle:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=feedback_rectangle_foreground_color_expected)
        validate_feedback_rectangle_background_color= MsgTypeString("mcr_treatment_set_range2:feedback_rectangle:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=feedback_rectangle_background_color_expected)
        validate_mcr7_global_range_status_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_global_range_status:TMMI_MCR_IS_VISIBLE", value=mcr7_global_range_status_visibility_expected)
        validate_mcr7_global_range_status_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_global_range_status:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_global_range_status_value_expected)
        validate_mcr7_global_range_status_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_global_range_status:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_global_range_status_foreground_color_expected)
        validate_mcr7_global_range_status_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_global_range_status:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_global_range_status_background_color_expected)
        validate_mcr7_range_field_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_range_field:TMMI_MCR_IS_VISIBLE", value=mcr7_range_field_visibility_expected)
        validate_mcr7_range_field_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_range_field:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_range_field_value_expected)
        validate_mcr7_range_field_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_range_field:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_range_field_foreground_color_expected)
        validate_mcr7_range_field_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_range_field:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_range_field_background_color_expected)
        validate_mcr7_sl1x_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_sl1x:TMMI_MCR_IS_VISIBLE", value=mcr7_sl1x_visibility_expected)
        validate_mcr7_sl1x_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_sl1x:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_sl1x_value_expected)
        validate_mcr7_sl1x_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_sl1x:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_sl1x_foreground_color_expected)
        validate_mcr7_sl1x_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_sl1x:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_sl1x_background_color_expected)
        validate_mcr7_sl1y_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_sl1y:TMMI_MCR_IS_VISIBLE", value=mcr7_sl1y_visibility_expected)
        validate_mcr7_sl1y_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_sl1y:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_sl1y_value_expected)
        validate_mcr7_sl1y_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_sl1y:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_sl1y_foreground_color_expected)
        validate_mcr7_sl1y_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_sl1y:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_sl1y_background_color_expected)
        validate_mcr7_sl2x_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_sl2x:TMMI_MCR_IS_VISIBLE", value=mcr7_sl2x_visibility_expected)
        validate_mcr7_sl2x_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_sl2x:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_sl2x_value_expected)
        validate_mcr7_sl2x_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_sl2x:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_sl2x_foreground_color_expected)
        validate_mcr7_sl2x_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_sl2x:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_sl2x_background_color_expected)
        validate_mcr7_graphite_step_label_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_graphite_step_label:TMMI_MCR_IS_VISIBLE", value=mcr7_graphite_step_label_visibility_expected)
        validate_mcr7_graphite_step_label_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_graphite_step_label:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_graphite_step_label_value_expected)
        validate_mcr7_graphite_step_label_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_graphite_step_label:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_graphite_step_label_foreground_color_expected)
        validate_mcr7_graphite_step_label_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_graphite_step_label:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_graphite_step_label_background_color_expected)
        validate_mcr7_iseu2btn_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_iseu2btn:TMMI_MCR_IS_VISIBLE", value=mcr7_iseu2btn_visibility_expected)
        validate_mcr7_iseu2btn_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_iseu2btn:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_iseu2btn_foreground_color_expected)
        validate_mcr7_iseu2btn_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_iseu2btn:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_iseu2btn_background_color_expected)
        validate_mcr7_graphite_step_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_graphite_step:TMMI_MCR_IS_VISIBLE", value=mcr7_graphite_step_visibility_expected)
        validate_mcr7_graphite_step_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_graphite_step:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_graphite_step_value_expected)
        validate_mcr7_graphite_step_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_graphite_step:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_graphite_step_foreground_color_expected)
        validate_mcr7_graphite_step_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_graphite_step:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_graphite_step_background_color_expected)
        validate_mcr7_setrange2btn_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_setrange2btn:TMMI_MCR_IS_VISIBLE", value=mcr7_setrange2btn_visibility_expected)
        validate_mcr7_setrange2btn_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_setrange2btn:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_setrange2btn_foreground_color_expected)
        validate_mcr7_setrange2btn_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_setrange2btn:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_setrange2btn_background_color_expected)
        validate_mcr7_gantry_angle_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_gantry_angle:TMMI_MCR_IS_VISIBLE", value=mcr7_gantry_angle_visibility_expected)
        validate_mcr7_gantry_angle_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_gantry_angle:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_gantry_angle_value_expected)
        validate_mcr7_gantry_angle_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_gantry_angle:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_gantry_angle_foreground_color_expected)
        validate_mcr7_gantry_angle_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_gantry_angle:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_gantry_angle_background_color_expected)
        validate_mcr7_q30_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_q30:TMMI_MCR_IS_VISIBLE", value=mcr7_q30_visibility_expected)
        validate_mcr7_q30_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_q30:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_q30_value_expected)
        validate_mcr7_q30_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q30:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_q30_foreground_color_expected)
        validate_mcr7_q30_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q30:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_q30_background_color_expected)
        validate_mcr7_q31_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_q31:TMMI_MCR_IS_VISIBLE", value=mcr7_q31_visibility_expected)
        validate_mcr7_q31_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_q31:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_q31_value_expected)
        validate_mcr7_q31_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q31:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_q31_foreground_color_expected)
        validate_mcr7_q31_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q31:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_q31_background_color_expected)
        validate_mcr7_q32_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_q32:TMMI_MCR_IS_VISIBLE", value=mcr7_q32_visibility_expected)
        validate_mcr7_q32_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_q32:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_q32_value_expected)
        validate_mcr7_q32_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q32:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_q32_foreground_color_expected)
        validate_mcr7_q32_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q32:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_q32_background_color_expected)
        validate_mcr7_q33_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_q33:TMMI_MCR_IS_VISIBLE", value=mcr7_q33_visibility_expected)
        validate_mcr7_q33_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_q33:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_q33_value_expected)
        validate_mcr7_q33_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q33:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_q33_foreground_color_expected)
        validate_mcr7_q33_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q33:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_q33_background_color_expected)
        validate_mcr7_q34_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_q34:TMMI_MCR_IS_VISIBLE", value=mcr7_q34_visibility_expected)
        validate_mcr7_q34_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_q34:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_q34_value_expected)
        validate_mcr7_q34_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q34:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_q34_foreground_color_expected)
        validate_mcr7_q34_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_q34:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_q34_background_color_expected)
        validate_mcr7_t10_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_t10:TMMI_MCR_IS_VISIBLE", value=mcr7_t10_visibility_expected)
        validate_mcr7_t10_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_t10:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_t10_value_expected)
        validate_mcr7_t10_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_t10:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_t10_foreground_color_expected)
        validate_mcr7_t10_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_t10:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_t10_background_color_expected)
        validate_mcr7_t11_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_t11:TMMI_MCR_IS_VISIBLE", value=mcr7_t11_visibility_expected)
        validate_mcr7_t11_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_t11:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_t11_value_expected)
        validate_mcr7_t11_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_t11:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_t11_foreground_color_expected)
        validate_mcr7_t11_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_t11:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_t11_background_color_expected)
        validate_mcr7_t12_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_t12:TMMI_MCR_IS_VISIBLE", value=mcr7_t12_visibility_expected)
        validate_mcr7_t12_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_t12:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_t12_value_expected)
        validate_mcr7_t12_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_t12:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_t12_foreground_color_expected)
        validate_mcr7_t12_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_t12:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_t12_background_color_expected)
        validate_mcr7_degrader_status_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_degrader_status:TMMI_MCR_IS_VISIBLE", value=mcr7_degrader_status_visibility_expected)
        validate_mcr7_degrader_status_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_degrader_status:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_degrader_status_value_expected)
        validate_mcr7_degrader_status_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_degrader_status:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_degrader_status_foreground_color_expected)
        validate_mcr7_degrader_status_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_degrader_status:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_degrader_status_background_color_expected)
        validate_mcr7_cugantryposfbk_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_cugantryposfbk:TMMI_MCR_IS_VISIBLE", value=mcr7_cugantryposfbk_visibility_expected)
        validate_mcr7_cugantryposfbk_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_cugantryposfbk:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_cugantryposfbk_value_expected)
        validate_mcr7_cugantryposfbk_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_cugantryposfbk:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_cugantryposfbk_foreground_color_expected)
        validate_mcr7_cugantryposfbk_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_cugantryposfbk:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_cugantryposfbk_background_color_expected)
        validate_DS_US_mode_text_visibility= MsgTypeString("mcr_treatment_set_range2:DS_US_mode_text:TMMI_MCR_IS_VISIBLE", value=DS_US_mode_text_visibility_expected)
        validate_DS_US_mode_text_foreground_color= MsgTypeString("mcr_treatment_set_range2:DS_US_mode_text:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=DS_US_mode_text_foreground_color_expected)
        validate_DS_US_mode_text_background_color= MsgTypeString("mcr_treatment_set_range2:DS_US_mode_text:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=DS_US_mode_text_background_color_expected)
        validate_PBS_mode_text_visibility= MsgTypeString("mcr_treatment_set_range2:PBS_mode_text:TMMI_MCR_IS_VISIBLE", value=PBS_mode_text_visibility_expected)
        validate_PBS_mode_text_foreground_color= MsgTypeString("mcr_treatment_set_range2:PBS_mode_text:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=PBS_mode_text_foreground_color_expected)
        validate_PBS_mode_text_background_color= MsgTypeString("mcr_treatment_set_range2:PBS_mode_text:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=PBS_mode_text_background_color_expected)
        validate_mcr7_trb5_visibility= MsgTypeString("mcr_treatment_set_range2:mcr7_trb5:TMMI_MCR_IS_VISIBLE", value=mcr7_trb5_visibility_expected)
        validate_mcr7_trb5_value= MsgTypeNumeric("mcr_treatment_set_range2:mcr7_trb5:TMMI_MCR_OBJECT_GET_VALUE", value=mcr7_trb5_value_expected)
        validate_mcr7_trb5_foreground_color= MsgTypeString("mcr_treatment_set_range2:mcr7_trb5:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr7_trb5_foreground_color_expected)
        validate_mcr7_trb5_background_color= MsgTypeString("mcr_treatment_set_range2:mcr7_trb5:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr7_trb5_background_color_expected)

        info_exchange = [
                        InformationSet("get mcr7_range_feedbackvisibility", "thriver", "mcrhci", get_mcr7_range_feedback_visibility),
                        InformationSet("validate mcr7_range_feedbackvisibility is equal to {mcr7_range_feedback_visibility_expected}".format(mcr7_range_feedback_visibility_expected=mcr7_range_feedback_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_range_feedback_visibility),
                        InformationSet("get mcr7_range_feedbackvalue", "thriver", "mcrhci", get_mcr7_range_feedback_value),
                        InformationSet("validate mcr7_range_feedbackvalue is equal to {mcr7_range_feedback_value_expected}".format(mcr7_range_feedback_value_expected=mcr7_range_feedback_value_expected), "mcrhci", "hcitracer", validate_mcr7_range_feedback_value),
                        InformationSet("get mcr7_range_feedbackforeground_color", "thriver", "mcrhci", get_mcr7_range_feedback_foreground_color),
                        InformationSet("validate mcr7_range_feedbackforeground_color is equal to {mcr7_range_feedback_foreground_color_expected}".format(mcr7_range_feedback_foreground_color_expected=mcr7_range_feedback_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_range_feedback_foreground_color),
                        InformationSet("get mcr7_range_feedbackbackground_color", "thriver", "mcrhci", get_mcr7_range_feedback_background_color),
                        InformationSet("validate mcr7_range_feedbackbackground_color is equal to {mcr7_range_feedback_background_color_expected}".format(mcr7_range_feedback_background_color_expected=mcr7_range_feedback_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_range_feedback_background_color),
                        InformationSet("get mcr7_q9visibility", "thriver", "mcrhci", get_mcr7_q9_visibility),
                        InformationSet("validate mcr7_q9visibility is equal to {mcr7_q9_visibility_expected}".format(mcr7_q9_visibility_expected=mcr7_q9_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_q9_visibility),
                        InformationSet("get mcr7_q9value", "thriver", "mcrhci", get_mcr7_q9_value),
                        InformationSet("validate mcr7_q9value is equal to {mcr7_q9_value_expected}".format(mcr7_q9_value_expected=mcr7_q9_value_expected), "mcrhci", "hcitracer", validate_mcr7_q9_value),
                        InformationSet("get mcr7_q9foreground_color", "thriver", "mcrhci", get_mcr7_q9_foreground_color),
                        InformationSet("validate mcr7_q9foreground_color is equal to {mcr7_q9_foreground_color_expected}".format(mcr7_q9_foreground_color_expected=mcr7_q9_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_q9_foreground_color),
                        InformationSet("get mcr7_q9background_color", "thriver", "mcrhci", get_mcr7_q9_background_color),
                        InformationSet("validate mcr7_q9background_color is equal to {mcr7_q9_background_color_expected}".format(mcr7_q9_background_color_expected=mcr7_q9_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_q9_background_color),
                        InformationSet("get mcr7_q10visibility", "thriver", "mcrhci", get_mcr7_q10_visibility),
                        InformationSet("validate mcr7_q10visibility is equal to {mcr7_q10_visibility_expected}".format(mcr7_q10_visibility_expected=mcr7_q10_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_q10_visibility),
                        InformationSet("get mcr7_q10value", "thriver", "mcrhci", get_mcr7_q10_value),
                        InformationSet("validate mcr7_q10value is equal to {mcr7_q10_value_expected}".format(mcr7_q10_value_expected=mcr7_q10_value_expected), "mcrhci", "hcitracer", validate_mcr7_q10_value),
                        InformationSet("get mcr7_q10foreground_color", "thriver", "mcrhci", get_mcr7_q10_foreground_color),
                        InformationSet("validate mcr7_q10foreground_color is equal to {mcr7_q10_foreground_color_expected}".format(mcr7_q10_foreground_color_expected=mcr7_q10_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_q10_foreground_color),
                        InformationSet("get mcr7_q10background_color", "thriver", "mcrhci", get_mcr7_q10_background_color),
                        InformationSet("validate mcr7_q10background_color is equal to {mcr7_q10_background_color_expected}".format(mcr7_q10_background_color_expected=mcr7_q10_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_q10_background_color),
                        InformationSet("get mcr7_q11visibility", "thriver", "mcrhci", get_mcr7_q11_visibility),
                        InformationSet("validate mcr7_q11visibility is equal to {mcr7_q11_visibility_expected}".format(mcr7_q11_visibility_expected=mcr7_q11_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_q11_visibility),
                        InformationSet("get mcr7_q11value", "thriver", "mcrhci", get_mcr7_q11_value),
                        InformationSet("validate mcr7_q11value is equal to {mcr7_q11_value_expected}".format(mcr7_q11_value_expected=mcr7_q11_value_expected), "mcrhci", "hcitracer", validate_mcr7_q11_value),
                        InformationSet("get mcr7_q11foreground_color", "thriver", "mcrhci", get_mcr7_q11_foreground_color),
                        InformationSet("validate mcr7_q11foreground_color is equal to {mcr7_q11_foreground_color_expected}".format(mcr7_q11_foreground_color_expected=mcr7_q11_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_q11_foreground_color),
                        InformationSet("get mcr7_q11background_color", "thriver", "mcrhci", get_mcr7_q11_background_color),
                        InformationSet("validate mcr7_q11background_color is equal to {mcr7_q11_background_color_expected}".format(mcr7_q11_background_color_expected=mcr7_q11_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_q11_background_color),
                        InformationSet("get mcr7_q12visibility", "thriver", "mcrhci", get_mcr7_q12_visibility),
                        InformationSet("validate mcr7_q12visibility is equal to {mcr7_q12_visibility_expected}".format(mcr7_q12_visibility_expected=mcr7_q12_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_q12_visibility),
                        InformationSet("get mcr7_q12value", "thriver", "mcrhci", get_mcr7_q12_value),
                        InformationSet("validate mcr7_q12value is equal to {mcr7_q12_value_expected}".format(mcr7_q12_value_expected=mcr7_q12_value_expected), "mcrhci", "hcitracer", validate_mcr7_q12_value),
                        InformationSet("get mcr7_q12foreground_color", "thriver", "mcrhci", get_mcr7_q12_foreground_color),
                        InformationSet("validate mcr7_q12foreground_color is equal to {mcr7_q12_foreground_color_expected}".format(mcr7_q12_foreground_color_expected=mcr7_q12_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_q12_foreground_color),
                        InformationSet("get mcr7_q12background_color", "thriver", "mcrhci", get_mcr7_q12_background_color),
                        InformationSet("validate mcr7_q12background_color is equal to {mcr7_q12_background_color_expected}".format(mcr7_q12_background_color_expected=mcr7_q12_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_q12_background_color),
                        InformationSet("get mcr7_q13visibility", "thriver", "mcrhci", get_mcr7_q13_visibility),
                        InformationSet("validate mcr7_q13visibility is equal to {mcr7_q13_visibility_expected}".format(mcr7_q13_visibility_expected=mcr7_q13_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_q13_visibility),
                        InformationSet("get mcr7_q13value", "thriver", "mcrhci", get_mcr7_q13_value),
                        InformationSet("validate mcr7_q13value is equal to {mcr7_q13_value_expected}".format(mcr7_q13_value_expected=mcr7_q13_value_expected), "mcrhci", "hcitracer", validate_mcr7_q13_value),
                        InformationSet("get mcr7_q13foreground_color", "thriver", "mcrhci", get_mcr7_q13_foreground_color),
                        InformationSet("validate mcr7_q13foreground_color is equal to {mcr7_q13_foreground_color_expected}".format(mcr7_q13_foreground_color_expected=mcr7_q13_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_q13_foreground_color),
                        InformationSet("get mcr7_q13background_color", "thriver", "mcrhci", get_mcr7_q13_background_color),
                        InformationSet("validate mcr7_q13background_color is equal to {mcr7_q13_background_color_expected}".format(mcr7_q13_background_color_expected=mcr7_q13_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_q13_background_color),
                        InformationSet("get mcr7_q14visibility", "thriver", "mcrhci", get_mcr7_q14_visibility),
                        InformationSet("validate mcr7_q14visibility is equal to {mcr7_q14_visibility_expected}".format(mcr7_q14_visibility_expected=mcr7_q14_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_q14_visibility),
                        InformationSet("get mcr7_q14value", "thriver", "mcrhci", get_mcr7_q14_value),
                        InformationSet("validate mcr7_q14value is equal to {mcr7_q14_value_expected}".format(mcr7_q14_value_expected=mcr7_q14_value_expected), "mcrhci", "hcitracer", validate_mcr7_q14_value),
                        InformationSet("get mcr7_q14foreground_color", "thriver", "mcrhci", get_mcr7_q14_foreground_color),
                        InformationSet("validate mcr7_q14foreground_color is equal to {mcr7_q14_foreground_color_expected}".format(mcr7_q14_foreground_color_expected=mcr7_q14_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_q14_foreground_color),
                        InformationSet("get mcr7_q14background_color", "thriver", "mcrhci", get_mcr7_q14_background_color),
                        InformationSet("validate mcr7_q14background_color is equal to {mcr7_q14_background_color_expected}".format(mcr7_q14_background_color_expected=mcr7_q14_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_q14_background_color),
                        InformationSet("get mcr7_q15visibility", "thriver", "mcrhci", get_mcr7_q15_visibility),
                        InformationSet("validate mcr7_q15visibility is equal to {mcr7_q15_visibility_expected}".format(mcr7_q15_visibility_expected=mcr7_q15_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_q15_visibility),
                        InformationSet("get mcr7_q15value", "thriver", "mcrhci", get_mcr7_q15_value),
                        InformationSet("validate mcr7_q15value is equal to {mcr7_q15_value_expected}".format(mcr7_q15_value_expected=mcr7_q15_value_expected), "mcrhci", "hcitracer", validate_mcr7_q15_value),
                        InformationSet("get mcr7_q15foreground_color", "thriver", "mcrhci", get_mcr7_q15_foreground_color),
                        InformationSet("validate mcr7_q15foreground_color is equal to {mcr7_q15_foreground_color_expected}".format(mcr7_q15_foreground_color_expected=mcr7_q15_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_q15_foreground_color),
                        InformationSet("get mcr7_q15background_color", "thriver", "mcrhci", get_mcr7_q15_background_color),
                        InformationSet("validate mcr7_q15background_color is equal to {mcr7_q15_background_color_expected}".format(mcr7_q15_background_color_expected=mcr7_q15_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_q15_background_color),
                        InformationSet("get mcr7_q20visibility", "thriver", "mcrhci", get_mcr7_q20_visibility),
                        InformationSet("validate mcr7_q20visibility is equal to {mcr7_q20_visibility_expected}".format(mcr7_q20_visibility_expected=mcr7_q20_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_q20_visibility),
                        InformationSet("get mcr7_q20value", "thriver", "mcrhci", get_mcr7_q20_value),
                        InformationSet("validate mcr7_q20value is equal to {mcr7_q20_value_expected}".format(mcr7_q20_value_expected=mcr7_q20_value_expected), "mcrhci", "hcitracer", validate_mcr7_q20_value),
                        InformationSet("get mcr7_q20foreground_color", "thriver", "mcrhci", get_mcr7_q20_foreground_color),
                        InformationSet("validate mcr7_q20foreground_color is equal to {mcr7_q20_foreground_color_expected}".format(mcr7_q20_foreground_color_expected=mcr7_q20_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_q20_foreground_color),
                        InformationSet("get mcr7_q20background_color", "thriver", "mcrhci", get_mcr7_q20_background_color),
                        InformationSet("validate mcr7_q20background_color is equal to {mcr7_q20_background_color_expected}".format(mcr7_q20_background_color_expected=mcr7_q20_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_q20_background_color),
                        InformationSet("get mcr7_q21visibility", "thriver", "mcrhci", get_mcr7_q21_visibility),
                        InformationSet("validate mcr7_q21visibility is equal to {mcr7_q21_visibility_expected}".format(mcr7_q21_visibility_expected=mcr7_q21_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_q21_visibility),
                        InformationSet("get mcr7_q21value", "thriver", "mcrhci", get_mcr7_q21_value),
                        InformationSet("validate mcr7_q21value is equal to {mcr7_q21_value_expected}".format(mcr7_q21_value_expected=mcr7_q21_value_expected), "mcrhci", "hcitracer", validate_mcr7_q21_value),
                        InformationSet("get mcr7_q21foreground_color", "thriver", "mcrhci", get_mcr7_q21_foreground_color),
                        InformationSet("validate mcr7_q21foreground_color is equal to {mcr7_q21_foreground_color_expected}".format(mcr7_q21_foreground_color_expected=mcr7_q21_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_q21_foreground_color),
                        InformationSet("get mcr7_q21background_color", "thriver", "mcrhci", get_mcr7_q21_background_color),
                        InformationSet("validate mcr7_q21background_color is equal to {mcr7_q21_background_color_expected}".format(mcr7_q21_background_color_expected=mcr7_q21_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_q21_background_color),
                        InformationSet("get mcr7_q22visibility", "thriver", "mcrhci", get_mcr7_q22_visibility),
                        InformationSet("validate mcr7_q22visibility is equal to {mcr7_q22_visibility_expected}".format(mcr7_q22_visibility_expected=mcr7_q22_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_q22_visibility),
                        InformationSet("get mcr7_q22value", "thriver", "mcrhci", get_mcr7_q22_value),
                        InformationSet("validate mcr7_q22value is equal to {mcr7_q22_value_expected}".format(mcr7_q22_value_expected=mcr7_q22_value_expected), "mcrhci", "hcitracer", validate_mcr7_q22_value),
                        InformationSet("get mcr7_q22foreground_color", "thriver", "mcrhci", get_mcr7_q22_foreground_color),
                        InformationSet("validate mcr7_q22foreground_color is equal to {mcr7_q22_foreground_color_expected}".format(mcr7_q22_foreground_color_expected=mcr7_q22_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_q22_foreground_color),
                        InformationSet("get mcr7_q22background_color", "thriver", "mcrhci", get_mcr7_q22_background_color),
                        InformationSet("validate mcr7_q22background_color is equal to {mcr7_q22_background_color_expected}".format(mcr7_q22_background_color_expected=mcr7_q22_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_q22_background_color),
                        InformationSet("get mcr7_b1234visibility", "thriver", "mcrhci", get_mcr7_b1234_visibility),
                        InformationSet("validate mcr7_b1234visibility is equal to {mcr7_b1234_visibility_expected}".format(mcr7_b1234_visibility_expected=mcr7_b1234_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_b1234_visibility),
                        InformationSet("get mcr7_b1234value", "thriver", "mcrhci", get_mcr7_b1234_value),
                        InformationSet("validate mcr7_b1234value is equal to {mcr7_b1234_value_expected}".format(mcr7_b1234_value_expected=mcr7_b1234_value_expected), "mcrhci", "hcitracer", validate_mcr7_b1234_value),
                        InformationSet("get mcr7_b1234foreground_color", "thriver", "mcrhci", get_mcr7_b1234_foreground_color),
                        InformationSet("validate mcr7_b1234foreground_color is equal to {mcr7_b1234_foreground_color_expected}".format(mcr7_b1234_foreground_color_expected=mcr7_b1234_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_b1234_foreground_color),
                        InformationSet("get mcr7_b1234background_color", "thriver", "mcrhci", get_mcr7_b1234_background_color),
                        InformationSet("validate mcr7_b1234background_color is equal to {mcr7_b1234_background_color_expected}".format(mcr7_b1234_background_color_expected=mcr7_b1234_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_b1234_background_color),
                        InformationSet("get mcr7_t6yvisibility", "thriver", "mcrhci", get_mcr7_t6y_visibility),
                        InformationSet("validate mcr7_t6yvisibility is equal to {mcr7_t6y_visibility_expected}".format(mcr7_t6y_visibility_expected=mcr7_t6y_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_t6y_visibility),
                        InformationSet("get mcr7_t6yvalue", "thriver", "mcrhci", get_mcr7_t6y_value),
                        InformationSet("validate mcr7_t6yvalue is equal to {mcr7_t6y_value_expected}".format(mcr7_t6y_value_expected=mcr7_t6y_value_expected), "mcrhci", "hcitracer", validate_mcr7_t6y_value),
                        InformationSet("get mcr7_t6yforeground_color", "thriver", "mcrhci", get_mcr7_t6y_foreground_color),
                        InformationSet("validate mcr7_t6yforeground_color is equal to {mcr7_t6y_foreground_color_expected}".format(mcr7_t6y_foreground_color_expected=mcr7_t6y_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_t6y_foreground_color),
                        InformationSet("get mcr7_t6ybackground_color", "thriver", "mcrhci", get_mcr7_t6y_background_color),
                        InformationSet("validate mcr7_t6ybackground_color is equal to {mcr7_t6y_background_color_expected}".format(mcr7_t6y_background_color_expected=mcr7_t6y_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_t6y_background_color),
                        InformationSet("get mcr7_t7yvisibility", "thriver", "mcrhci", get_mcr7_t7y_visibility),
                        InformationSet("validate mcr7_t7yvisibility is equal to {mcr7_t7y_visibility_expected}".format(mcr7_t7y_visibility_expected=mcr7_t7y_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_t7y_visibility),
                        InformationSet("get mcr7_t7yvalue", "thriver", "mcrhci", get_mcr7_t7y_value),
                        InformationSet("validate mcr7_t7yvalue is equal to {mcr7_t7y_value_expected}".format(mcr7_t7y_value_expected=mcr7_t7y_value_expected), "mcrhci", "hcitracer", validate_mcr7_t7y_value),
                        InformationSet("get mcr7_t7yforeground_color", "thriver", "mcrhci", get_mcr7_t7y_foreground_color),
                        InformationSet("validate mcr7_t7yforeground_color is equal to {mcr7_t7y_foreground_color_expected}".format(mcr7_t7y_foreground_color_expected=mcr7_t7y_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_t7y_foreground_color),
                        InformationSet("get mcr7_t7ybackground_color", "thriver", "mcrhci", get_mcr7_t7y_background_color),
                        InformationSet("validate mcr7_t7ybackground_color is equal to {mcr7_t7y_background_color_expected}".format(mcr7_t7y_background_color_expected=mcr7_t7y_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_t7y_background_color),
                        InformationSet("get mcr7_trb1visibility", "thriver", "mcrhci", get_mcr7_trb1_visibility),
                        InformationSet("validate mcr7_trb1visibility is equal to {mcr7_trb1_visibility_expected}".format(mcr7_trb1_visibility_expected=mcr7_trb1_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_trb1_visibility),
                        InformationSet("get mcr7_trb1value", "thriver", "mcrhci", get_mcr7_trb1_value),
                        InformationSet("validate mcr7_trb1value is equal to {mcr7_trb1_value_expected}".format(mcr7_trb1_value_expected=mcr7_trb1_value_expected), "mcrhci", "hcitracer", validate_mcr7_trb1_value),
                        InformationSet("get mcr7_trb1foreground_color", "thriver", "mcrhci", get_mcr7_trb1_foreground_color),
                        InformationSet("validate mcr7_trb1foreground_color is equal to {mcr7_trb1_foreground_color_expected}".format(mcr7_trb1_foreground_color_expected=mcr7_trb1_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_trb1_foreground_color),
                        InformationSet("get mcr7_trb1background_color", "thriver", "mcrhci", get_mcr7_trb1_background_color),
                        InformationSet("validate mcr7_trb1background_color is equal to {mcr7_trb1_background_color_expected}".format(mcr7_trb1_background_color_expected=mcr7_trb1_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_trb1_background_color),
                        InformationSet("get mcr7_trb34visibility", "thriver", "mcrhci", get_mcr7_trb34_visibility),
                        InformationSet("validate mcr7_trb34visibility is equal to {mcr7_trb34_visibility_expected}".format(mcr7_trb34_visibility_expected=mcr7_trb34_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_trb34_visibility),
                        InformationSet("get mcr7_trb34value", "thriver", "mcrhci", get_mcr7_trb34_value),
                        InformationSet("validate mcr7_trb34value is equal to {mcr7_trb34_value_expected}".format(mcr7_trb34_value_expected=mcr7_trb34_value_expected), "mcrhci", "hcitracer", validate_mcr7_trb34_value),
                        InformationSet("get mcr7_trb34foreground_color", "thriver", "mcrhci", get_mcr7_trb34_foreground_color),
                        InformationSet("validate mcr7_trb34foreground_color is equal to {mcr7_trb34_foreground_color_expected}".format(mcr7_trb34_foreground_color_expected=mcr7_trb34_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_trb34_foreground_color),
                        InformationSet("get mcr7_trb34background_color", "thriver", "mcrhci", get_mcr7_trb34_background_color),
                        InformationSet("validate mcr7_trb34background_color is equal to {mcr7_trb34_background_color_expected}".format(mcr7_trb34_background_color_expected=mcr7_trb34_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_trb34_background_color),
                        InformationSet("get mcr7_q35visibility", "thriver", "mcrhci", get_mcr7_q35_visibility),
                        InformationSet("validate mcr7_q35visibility is equal to {mcr7_q35_visibility_expected}".format(mcr7_q35_visibility_expected=mcr7_q35_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_q35_visibility),
                        InformationSet("get mcr7_q35value", "thriver", "mcrhci", get_mcr7_q35_value),
                        InformationSet("validate mcr7_q35value is equal to {mcr7_q35_value_expected}".format(mcr7_q35_value_expected=mcr7_q35_value_expected), "mcrhci", "hcitracer", validate_mcr7_q35_value),
                        InformationSet("get mcr7_q35foreground_color", "thriver", "mcrhci", get_mcr7_q35_foreground_color),
                        InformationSet("validate mcr7_q35foreground_color is equal to {mcr7_q35_foreground_color_expected}".format(mcr7_q35_foreground_color_expected=mcr7_q35_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_q35_foreground_color),
                        InformationSet("get mcr7_q35background_color", "thriver", "mcrhci", get_mcr7_q35_background_color),
                        InformationSet("validate mcr7_q35background_color is equal to {mcr7_q35_background_color_expected}".format(mcr7_q35_background_color_expected=mcr7_q35_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_q35_background_color),
                        InformationSet("get mcr7_q36visibility", "thriver", "mcrhci", get_mcr7_q36_visibility),
                        InformationSet("validate mcr7_q36visibility is equal to {mcr7_q36_visibility_expected}".format(mcr7_q36_visibility_expected=mcr7_q36_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_q36_visibility),
                        InformationSet("get mcr7_q36value", "thriver", "mcrhci", get_mcr7_q36_value),
                        InformationSet("validate mcr7_q36value is equal to {mcr7_q36_value_expected}".format(mcr7_q36_value_expected=mcr7_q36_value_expected), "mcrhci", "hcitracer", validate_mcr7_q36_value),
                        InformationSet("get mcr7_q36foreground_color", "thriver", "mcrhci", get_mcr7_q36_foreground_color),
                        InformationSet("validate mcr7_q36foreground_color is equal to {mcr7_q36_foreground_color_expected}".format(mcr7_q36_foreground_color_expected=mcr7_q36_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_q36_foreground_color),
                        InformationSet("get mcr7_q36background_color", "thriver", "mcrhci", get_mcr7_q36_background_color),
                        InformationSet("validate mcr7_q36background_color is equal to {mcr7_q36_background_color_expected}".format(mcr7_q36_background_color_expected=mcr7_q36_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_q36_background_color),
                        InformationSet("get mcr7_q37visibility", "thriver", "mcrhci", get_mcr7_q37_visibility),
                        InformationSet("validate mcr7_q37visibility is equal to {mcr7_q37_visibility_expected}".format(mcr7_q37_visibility_expected=mcr7_q37_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_q37_visibility),
                        InformationSet("get mcr7_q37value", "thriver", "mcrhci", get_mcr7_q37_value),
                        InformationSet("validate mcr7_q37value is equal to {mcr7_q37_value_expected}".format(mcr7_q37_value_expected=mcr7_q37_value_expected), "mcrhci", "hcitracer", validate_mcr7_q37_value),
                        InformationSet("get mcr7_q37foreground_color", "thriver", "mcrhci", get_mcr7_q37_foreground_color),
                        InformationSet("validate mcr7_q37foreground_color is equal to {mcr7_q37_foreground_color_expected}".format(mcr7_q37_foreground_color_expected=mcr7_q37_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_q37_foreground_color),
                        InformationSet("get mcr7_q37background_color", "thriver", "mcrhci", get_mcr7_q37_background_color),
                        InformationSet("validate mcr7_q37background_color is equal to {mcr7_q37_background_color_expected}".format(mcr7_q37_background_color_expected=mcr7_q37_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_q37_background_color),
                        InformationSet("get mcr7_b78visibility", "thriver", "mcrhci", get_mcr7_b78_visibility),
                        InformationSet("validate mcr7_b78visibility is equal to {mcr7_b78_visibility_expected}".format(mcr7_b78_visibility_expected=mcr7_b78_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_b78_visibility),
                        InformationSet("get mcr7_b78value", "thriver", "mcrhci", get_mcr7_b78_value),
                        InformationSet("validate mcr7_b78value is equal to {mcr7_b78_value_expected}".format(mcr7_b78_value_expected=mcr7_b78_value_expected), "mcrhci", "hcitracer", validate_mcr7_b78_value),
                        InformationSet("get mcr7_b78foreground_color", "thriver", "mcrhci", get_mcr7_b78_foreground_color),
                        InformationSet("validate mcr7_b78foreground_color is equal to {mcr7_b78_foreground_color_expected}".format(mcr7_b78_foreground_color_expected=mcr7_b78_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_b78_foreground_color),
                        InformationSet("get mcr7_b78background_color", "thriver", "mcrhci", get_mcr7_b78_background_color),
                        InformationSet("validate mcr7_b78background_color is equal to {mcr7_b78_background_color_expected}".format(mcr7_b78_background_color_expected=mcr7_b78_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_b78_background_color),
                        InformationSet("get mcr7_trb7visibility", "thriver", "mcrhci", get_mcr7_trb7_visibility),
                        InformationSet("validate mcr7_trb7visibility is equal to {mcr7_trb7_visibility_expected}".format(mcr7_trb7_visibility_expected=mcr7_trb7_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_trb7_visibility),
                        InformationSet("get mcr7_trb7value", "thriver", "mcrhci", get_mcr7_trb7_value),
                        InformationSet("validate mcr7_trb7value is equal to {mcr7_trb7_value_expected}".format(mcr7_trb7_value_expected=mcr7_trb7_value_expected), "mcrhci", "hcitracer", validate_mcr7_trb7_value),
                        InformationSet("get mcr7_trb7foreground_color", "thriver", "mcrhci", get_mcr7_trb7_foreground_color),
                        InformationSet("validate mcr7_trb7foreground_color is equal to {mcr7_trb7_foreground_color_expected}".format(mcr7_trb7_foreground_color_expected=mcr7_trb7_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_trb7_foreground_color),
                        InformationSet("get mcr7_trb7background_color", "thriver", "mcrhci", get_mcr7_trb7_background_color),
                        InformationSet("validate mcr7_trb7background_color is equal to {mcr7_trb7_background_color_expected}".format(mcr7_trb7_background_color_expected=mcr7_trb7_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_trb7_background_color),
                        InformationSet("get mcr7_trb8visibility", "thriver", "mcrhci", get_mcr7_trb8_visibility),
                        InformationSet("validate mcr7_trb8visibility is equal to {mcr7_trb8_visibility_expected}".format(mcr7_trb8_visibility_expected=mcr7_trb8_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_trb8_visibility),
                        InformationSet("get mcr7_trb8value", "thriver", "mcrhci", get_mcr7_trb8_value),
                        InformationSet("validate mcr7_trb8value is equal to {mcr7_trb8_value_expected}".format(mcr7_trb8_value_expected=mcr7_trb8_value_expected), "mcrhci", "hcitracer", validate_mcr7_trb8_value),
                        InformationSet("get mcr7_trb8foreground_color", "thriver", "mcrhci", get_mcr7_trb8_foreground_color),
                        InformationSet("validate mcr7_trb8foreground_color is equal to {mcr7_trb8_foreground_color_expected}".format(mcr7_trb8_foreground_color_expected=mcr7_trb8_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_trb8_foreground_color),
                        InformationSet("get mcr7_trb8background_color", "thriver", "mcrhci", get_mcr7_trb8_background_color),
                        InformationSet("validate mcr7_trb8background_color is equal to {mcr7_trb8_background_color_expected}".format(mcr7_trb8_background_color_expected=mcr7_trb8_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_trb8_background_color),
                        InformationSet("get mcr7_q0m2visibility", "thriver", "mcrhci", get_mcr7_q0m2_visibility),
                        InformationSet("validate mcr7_q0m2visibility is equal to {mcr7_q0m2_visibility_expected}".format(mcr7_q0m2_visibility_expected=mcr7_q0m2_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_q0m2_visibility),
                        InformationSet("get mcr7_q0m2value", "thriver", "mcrhci", get_mcr7_q0m2_value),
                        InformationSet("validate mcr7_q0m2value is equal to {mcr7_q0m2_value_expected}".format(mcr7_q0m2_value_expected=mcr7_q0m2_value_expected), "mcrhci", "hcitracer", validate_mcr7_q0m2_value),
                        InformationSet("get mcr7_q0m2foreground_color", "thriver", "mcrhci", get_mcr7_q0m2_foreground_color),
                        InformationSet("validate mcr7_q0m2foreground_color is equal to {mcr7_q0m2_foreground_color_expected}".format(mcr7_q0m2_foreground_color_expected=mcr7_q0m2_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_q0m2_foreground_color),
                        InformationSet("get mcr7_q0m2background_color", "thriver", "mcrhci", get_mcr7_q0m2_background_color),
                        InformationSet("validate mcr7_q0m2background_color is equal to {mcr7_q0m2_background_color_expected}".format(mcr7_q0m2_background_color_expected=mcr7_q0m2_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_q0m2_background_color),
                        InformationSet("get mcr7_q1m2visibility", "thriver", "mcrhci", get_mcr7_q1m2_visibility),
                        InformationSet("validate mcr7_q1m2visibility is equal to {mcr7_q1m2_visibility_expected}".format(mcr7_q1m2_visibility_expected=mcr7_q1m2_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_q1m2_visibility),
                        InformationSet("get mcr7_q1m2value", "thriver", "mcrhci", get_mcr7_q1m2_value),
                        InformationSet("validate mcr7_q1m2value is equal to {mcr7_q1m2_value_expected}".format(mcr7_q1m2_value_expected=mcr7_q1m2_value_expected), "mcrhci", "hcitracer", validate_mcr7_q1m2_value),
                        InformationSet("get mcr7_q1m2foreground_color", "thriver", "mcrhci", get_mcr7_q1m2_foreground_color),
                        InformationSet("validate mcr7_q1m2foreground_color is equal to {mcr7_q1m2_foreground_color_expected}".format(mcr7_q1m2_foreground_color_expected=mcr7_q1m2_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_q1m2_foreground_color),
                        InformationSet("get mcr7_q1m2background_color", "thriver", "mcrhci", get_mcr7_q1m2_background_color),
                        InformationSet("validate mcr7_q1m2background_color is equal to {mcr7_q1m2_background_color_expected}".format(mcr7_q1m2_background_color_expected=mcr7_q1m2_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_q1m2_background_color),
                        InformationSet("get mcr7_q2m2visibility", "thriver", "mcrhci", get_mcr7_q2m2_visibility),
                        InformationSet("validate mcr7_q2m2visibility is equal to {mcr7_q2m2_visibility_expected}".format(mcr7_q2m2_visibility_expected=mcr7_q2m2_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_q2m2_visibility),
                        InformationSet("get mcr7_q2m2value", "thriver", "mcrhci", get_mcr7_q2m2_value),
                        InformationSet("validate mcr7_q2m2value is equal to {mcr7_q2m2_value_expected}".format(mcr7_q2m2_value_expected=mcr7_q2m2_value_expected), "mcrhci", "hcitracer", validate_mcr7_q2m2_value),
                        InformationSet("get mcr7_q2m2foreground_color", "thriver", "mcrhci", get_mcr7_q2m2_foreground_color),
                        InformationSet("validate mcr7_q2m2foreground_color is equal to {mcr7_q2m2_foreground_color_expected}".format(mcr7_q2m2_foreground_color_expected=mcr7_q2m2_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_q2m2_foreground_color),
                        InformationSet("get mcr7_q2m2background_color", "thriver", "mcrhci", get_mcr7_q2m2_background_color),
                        InformationSet("validate mcr7_q2m2background_color is equal to {mcr7_q2m2_background_color_expected}".format(mcr7_q2m2_background_color_expected=mcr7_q2m2_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_q2m2_background_color),
                        InformationSet("get mcr7_q3m2visibility", "thriver", "mcrhci", get_mcr7_q3m2_visibility),
                        InformationSet("validate mcr7_q3m2visibility is equal to {mcr7_q3m2_visibility_expected}".format(mcr7_q3m2_visibility_expected=mcr7_q3m2_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_q3m2_visibility),
                        InformationSet("get mcr7_q3m2value", "thriver", "mcrhci", get_mcr7_q3m2_value),
                        InformationSet("validate mcr7_q3m2value is equal to {mcr7_q3m2_value_expected}".format(mcr7_q3m2_value_expected=mcr7_q3m2_value_expected), "mcrhci", "hcitracer", validate_mcr7_q3m2_value),
                        InformationSet("get mcr7_q3m2foreground_color", "thriver", "mcrhci", get_mcr7_q3m2_foreground_color),
                        InformationSet("validate mcr7_q3m2foreground_color is equal to {mcr7_q3m2_foreground_color_expected}".format(mcr7_q3m2_foreground_color_expected=mcr7_q3m2_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_q3m2_foreground_color),
                        InformationSet("get mcr7_q3m2background_color", "thriver", "mcrhci", get_mcr7_q3m2_background_color),
                        InformationSet("validate mcr7_q3m2background_color is equal to {mcr7_q3m2_background_color_expected}".format(mcr7_q3m2_background_color_expected=mcr7_q3m2_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_q3m2_background_color),
                        InformationSet("get mcr7_q1g2visibility", "thriver", "mcrhci", get_mcr7_q1g2_visibility),
                        InformationSet("validate mcr7_q1g2visibility is equal to {mcr7_q1g2_visibility_expected}".format(mcr7_q1g2_visibility_expected=mcr7_q1g2_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_q1g2_visibility),
                        InformationSet("get mcr7_q1g2value", "thriver", "mcrhci", get_mcr7_q1g2_value),
                        InformationSet("validate mcr7_q1g2value is equal to {mcr7_q1g2_value_expected}".format(mcr7_q1g2_value_expected=mcr7_q1g2_value_expected), "mcrhci", "hcitracer", validate_mcr7_q1g2_value),
                        InformationSet("get mcr7_q1g2foreground_color", "thriver", "mcrhci", get_mcr7_q1g2_foreground_color),
                        InformationSet("validate mcr7_q1g2foreground_color is equal to {mcr7_q1g2_foreground_color_expected}".format(mcr7_q1g2_foreground_color_expected=mcr7_q1g2_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_q1g2_foreground_color),
                        InformationSet("get mcr7_q1g2background_color", "thriver", "mcrhci", get_mcr7_q1g2_background_color),
                        InformationSet("validate mcr7_q1g2background_color is equal to {mcr7_q1g2_background_color_expected}".format(mcr7_q1g2_background_color_expected=mcr7_q1g2_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_q1g2_background_color),
                        InformationSet("get mcr7_q2g2visibility", "thriver", "mcrhci", get_mcr7_q2g2_visibility),
                        InformationSet("validate mcr7_q2g2visibility is equal to {mcr7_q2g2_visibility_expected}".format(mcr7_q2g2_visibility_expected=mcr7_q2g2_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_q2g2_visibility),
                        InformationSet("get mcr7_q2g2value", "thriver", "mcrhci", get_mcr7_q2g2_value),
                        InformationSet("validate mcr7_q2g2value is equal to {mcr7_q2g2_value_expected}".format(mcr7_q2g2_value_expected=mcr7_q2g2_value_expected), "mcrhci", "hcitracer", validate_mcr7_q2g2_value),
                        InformationSet("get mcr7_q2g2foreground_color", "thriver", "mcrhci", get_mcr7_q2g2_foreground_color),
                        InformationSet("validate mcr7_q2g2foreground_color is equal to {mcr7_q2g2_foreground_color_expected}".format(mcr7_q2g2_foreground_color_expected=mcr7_q2g2_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_q2g2_foreground_color),
                        InformationSet("get mcr7_q2g2background_color", "thriver", "mcrhci", get_mcr7_q2g2_background_color),
                        InformationSet("validate mcr7_q2g2background_color is equal to {mcr7_q2g2_background_color_expected}".format(mcr7_q2g2_background_color_expected=mcr7_q2g2_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_q2g2_background_color),
                        InformationSet("get mcr7_q3g2visibility", "thriver", "mcrhci", get_mcr7_q3g2_visibility),
                        InformationSet("validate mcr7_q3g2visibility is equal to {mcr7_q3g2_visibility_expected}".format(mcr7_q3g2_visibility_expected=mcr7_q3g2_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_q3g2_visibility),
                        InformationSet("get mcr7_q3g2value", "thriver", "mcrhci", get_mcr7_q3g2_value),
                        InformationSet("validate mcr7_q3g2value is equal to {mcr7_q3g2_value_expected}".format(mcr7_q3g2_value_expected=mcr7_q3g2_value_expected), "mcrhci", "hcitracer", validate_mcr7_q3g2_value),
                        InformationSet("get mcr7_q3g2foreground_color", "thriver", "mcrhci", get_mcr7_q3g2_foreground_color),
                        InformationSet("validate mcr7_q3g2foreground_color is equal to {mcr7_q3g2_foreground_color_expected}".format(mcr7_q3g2_foreground_color_expected=mcr7_q3g2_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_q3g2_foreground_color),
                        InformationSet("get mcr7_q3g2background_color", "thriver", "mcrhci", get_mcr7_q3g2_background_color),
                        InformationSet("validate mcr7_q3g2background_color is equal to {mcr7_q3g2_background_color_expected}".format(mcr7_q3g2_background_color_expected=mcr7_q3g2_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_q3g2_background_color),
                        InformationSet("get mcr7_q4g2visibility", "thriver", "mcrhci", get_mcr7_q4g2_visibility),
                        InformationSet("validate mcr7_q4g2visibility is equal to {mcr7_q4g2_visibility_expected}".format(mcr7_q4g2_visibility_expected=mcr7_q4g2_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_q4g2_visibility),
                        InformationSet("get mcr7_q4g2value", "thriver", "mcrhci", get_mcr7_q4g2_value),
                        InformationSet("validate mcr7_q4g2value is equal to {mcr7_q4g2_value_expected}".format(mcr7_q4g2_value_expected=mcr7_q4g2_value_expected), "mcrhci", "hcitracer", validate_mcr7_q4g2_value),
                        InformationSet("get mcr7_q4g2foreground_color", "thriver", "mcrhci", get_mcr7_q4g2_foreground_color),
                        InformationSet("validate mcr7_q4g2foreground_color is equal to {mcr7_q4g2_foreground_color_expected}".format(mcr7_q4g2_foreground_color_expected=mcr7_q4g2_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_q4g2_foreground_color),
                        InformationSet("get mcr7_q4g2background_color", "thriver", "mcrhci", get_mcr7_q4g2_background_color),
                        InformationSet("validate mcr7_q4g2background_color is equal to {mcr7_q4g2_background_color_expected}".format(mcr7_q4g2_background_color_expected=mcr7_q4g2_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_q4g2_background_color),
                        InformationSet("get mcr7_q5g2visibility", "thriver", "mcrhci", get_mcr7_q5g2_visibility),
                        InformationSet("validate mcr7_q5g2visibility is equal to {mcr7_q5g2_visibility_expected}".format(mcr7_q5g2_visibility_expected=mcr7_q5g2_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_q5g2_visibility),
                        InformationSet("get mcr7_q5g2value", "thriver", "mcrhci", get_mcr7_q5g2_value),
                        InformationSet("validate mcr7_q5g2value is equal to {mcr7_q5g2_value_expected}".format(mcr7_q5g2_value_expected=mcr7_q5g2_value_expected), "mcrhci", "hcitracer", validate_mcr7_q5g2_value),
                        InformationSet("get mcr7_q5g2foreground_color", "thriver", "mcrhci", get_mcr7_q5g2_foreground_color),
                        InformationSet("validate mcr7_q5g2foreground_color is equal to {mcr7_q5g2_foreground_color_expected}".format(mcr7_q5g2_foreground_color_expected=mcr7_q5g2_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_q5g2_foreground_color),
                        InformationSet("get mcr7_q5g2background_color", "thriver", "mcrhci", get_mcr7_q5g2_background_color),
                        InformationSet("validate mcr7_q5g2background_color is equal to {mcr7_q5g2_background_color_expected}".format(mcr7_q5g2_background_color_expected=mcr7_q5g2_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_q5g2_background_color),
                        InformationSet("get mcr7_b1g2visibility", "thriver", "mcrhci", get_mcr7_b1g2_visibility),
                        InformationSet("validate mcr7_b1g2visibility is equal to {mcr7_b1g2_visibility_expected}".format(mcr7_b1g2_visibility_expected=mcr7_b1g2_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_b1g2_visibility),
                        InformationSet("get mcr7_b1g2value", "thriver", "mcrhci", get_mcr7_b1g2_value),
                        InformationSet("validate mcr7_b1g2value is equal to {mcr7_b1g2_value_expected}".format(mcr7_b1g2_value_expected=mcr7_b1g2_value_expected), "mcrhci", "hcitracer", validate_mcr7_b1g2_value),
                        InformationSet("get mcr7_b1g2foreground_color", "thriver", "mcrhci", get_mcr7_b1g2_foreground_color),
                        InformationSet("validate mcr7_b1g2foreground_color is equal to {mcr7_b1g2_foreground_color_expected}".format(mcr7_b1g2_foreground_color_expected=mcr7_b1g2_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_b1g2_foreground_color),
                        InformationSet("get mcr7_b1g2background_color", "thriver", "mcrhci", get_mcr7_b1g2_background_color),
                        InformationSet("validate mcr7_b1g2background_color is equal to {mcr7_b1g2_background_color_expected}".format(mcr7_b1g2_background_color_expected=mcr7_b1g2_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_b1g2_background_color),
                        InformationSet("get mcr7_b2g2visibility", "thriver", "mcrhci", get_mcr7_b2g2_visibility),
                        InformationSet("validate mcr7_b2g2visibility is equal to {mcr7_b2g2_visibility_expected}".format(mcr7_b2g2_visibility_expected=mcr7_b2g2_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_b2g2_visibility),
                        InformationSet("get mcr7_b2g2value", "thriver", "mcrhci", get_mcr7_b2g2_value),
                        InformationSet("validate mcr7_b2g2value is equal to {mcr7_b2g2_value_expected}".format(mcr7_b2g2_value_expected=mcr7_b2g2_value_expected), "mcrhci", "hcitracer", validate_mcr7_b2g2_value),
                        InformationSet("get mcr7_b2g2foreground_color", "thriver", "mcrhci", get_mcr7_b2g2_foreground_color),
                        InformationSet("validate mcr7_b2g2foreground_color is equal to {mcr7_b2g2_foreground_color_expected}".format(mcr7_b2g2_foreground_color_expected=mcr7_b2g2_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_b2g2_foreground_color),
                        InformationSet("get mcr7_b2g2background_color", "thriver", "mcrhci", get_mcr7_b2g2_background_color),
                        InformationSet("validate mcr7_b2g2background_color is equal to {mcr7_b2g2_background_color_expected}".format(mcr7_b2g2_background_color_expected=mcr7_b2g2_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_b2g2_background_color),
                        InformationSet("get mcr7_t9g2visibility", "thriver", "mcrhci", get_mcr7_t9g2_visibility),
                        InformationSet("validate mcr7_t9g2visibility is equal to {mcr7_t9g2_visibility_expected}".format(mcr7_t9g2_visibility_expected=mcr7_t9g2_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_t9g2_visibility),
                        InformationSet("get mcr7_t9g2value", "thriver", "mcrhci", get_mcr7_t9g2_value),
                        InformationSet("validate mcr7_t9g2value is equal to {mcr7_t9g2_value_expected}".format(mcr7_t9g2_value_expected=mcr7_t9g2_value_expected), "mcrhci", "hcitracer", validate_mcr7_t9g2_value),
                        InformationSet("get mcr7_t9g2foreground_color", "thriver", "mcrhci", get_mcr7_t9g2_foreground_color),
                        InformationSet("validate mcr7_t9g2foreground_color is equal to {mcr7_t9g2_foreground_color_expected}".format(mcr7_t9g2_foreground_color_expected=mcr7_t9g2_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_t9g2_foreground_color),
                        InformationSet("get mcr7_t9g2background_color", "thriver", "mcrhci", get_mcr7_t9g2_background_color),
                        InformationSet("validate mcr7_t9g2background_color is equal to {mcr7_t9g2_background_color_expected}".format(mcr7_t9g2_background_color_expected=mcr7_t9g2_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_t9g2_background_color),
                        InformationSet("get mcr7_t10g2visibility", "thriver", "mcrhci", get_mcr7_t10g2_visibility),
                        InformationSet("validate mcr7_t10g2visibility is equal to {mcr7_t10g2_visibility_expected}".format(mcr7_t10g2_visibility_expected=mcr7_t10g2_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_t10g2_visibility),
                        InformationSet("get mcr7_t10g2value", "thriver", "mcrhci", get_mcr7_t10g2_value),
                        InformationSet("validate mcr7_t10g2value is equal to {mcr7_t10g2_value_expected}".format(mcr7_t10g2_value_expected=mcr7_t10g2_value_expected), "mcrhci", "hcitracer", validate_mcr7_t10g2_value),
                        InformationSet("get mcr7_t10g2foreground_color", "thriver", "mcrhci", get_mcr7_t10g2_foreground_color),
                        InformationSet("validate mcr7_t10g2foreground_color is equal to {mcr7_t10g2_foreground_color_expected}".format(mcr7_t10g2_foreground_color_expected=mcr7_t10g2_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_t10g2_foreground_color),
                        InformationSet("get mcr7_t10g2background_color", "thriver", "mcrhci", get_mcr7_t10g2_background_color),
                        InformationSet("validate mcr7_t10g2background_color is equal to {mcr7_t10g2_background_color_expected}".format(mcr7_t10g2_background_color_expected=mcr7_t10g2_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_t10g2_background_color),
                        InformationSet("get Label1visibility", "thriver", "mcrhci", get_Label1_visibility),
                        InformationSet("validate Label1visibility is equal to {Label1_visibility_expected}".format(Label1_visibility_expected=Label1_visibility_expected), "mcrhci", "hcitracer", validate_Label1_visibility),
                        InformationSet("get Label1foreground_color", "thriver", "mcrhci", get_Label1_foreground_color),
                        InformationSet("validate Label1foreground_color is equal to {Label1_foreground_color_expected}".format(Label1_foreground_color_expected=Label1_foreground_color_expected), "mcrhci", "hcitracer", validate_Label1_foreground_color),
                        InformationSet("get Label1background_color", "thriver", "mcrhci", get_Label1_background_color),
                        InformationSet("validate Label1background_color is equal to {Label1_background_color_expected}".format(Label1_background_color_expected=Label1_background_color_expected), "mcrhci", "hcitracer", validate_Label1_background_color),
                        InformationSet("get mcr7_range_energyvisibility", "thriver", "mcrhci", get_mcr7_range_energy_visibility),
                        InformationSet("validate mcr7_range_energyvisibility is equal to {mcr7_range_energy_visibility_expected}".format(mcr7_range_energy_visibility_expected=mcr7_range_energy_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_range_energy_visibility),
                        InformationSet("get mcr7_range_energyvalue", "thriver", "mcrhci", get_mcr7_range_energy_value),
                        InformationSet("validate mcr7_range_energyvalue is equal to {mcr7_range_energy_value_expected}".format(mcr7_range_energy_value_expected=mcr7_range_energy_value_expected), "mcrhci", "hcitracer", validate_mcr7_range_energy_value),
                        InformationSet("get mcr7_range_energyforeground_color", "thriver", "mcrhci", get_mcr7_range_energy_foreground_color),
                        InformationSet("validate mcr7_range_energyforeground_color is equal to {mcr7_range_energy_foreground_color_expected}".format(mcr7_range_energy_foreground_color_expected=mcr7_range_energy_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_range_energy_foreground_color),
                        InformationSet("get mcr7_range_energybackground_color", "thriver", "mcrhci", get_mcr7_range_energy_background_color),
                        InformationSet("validate mcr7_range_energybackground_color is equal to {mcr7_range_energy_background_color_expected}".format(mcr7_range_energy_background_color_expected=mcr7_range_energy_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_range_energy_background_color),
                        InformationSet("get Label2visibility", "thriver", "mcrhci", get_Label2_visibility),
                        InformationSet("validate Label2visibility is equal to {Label2_visibility_expected}".format(Label2_visibility_expected=Label2_visibility_expected), "mcrhci", "hcitracer", validate_Label2_visibility),
                        InformationSet("get Label2foreground_color", "thriver", "mcrhci", get_Label2_foreground_color),
                        InformationSet("validate Label2foreground_color is equal to {Label2_foreground_color_expected}".format(Label2_foreground_color_expected=Label2_foreground_color_expected), "mcrhci", "hcitracer", validate_Label2_foreground_color),
                        InformationSet("get Label2background_color", "thriver", "mcrhci", get_Label2_background_color),
                        InformationSet("validate Label2background_color is equal to {Label2_background_color_expected}".format(Label2_background_color_expected=Label2_background_color_expected), "mcrhci", "hcitracer", validate_Label2_background_color),
                        InformationSet("get feedback_rectanglevisibility", "thriver", "mcrhci", get_feedback_rectangle_visibility),
                        InformationSet("validate feedback_rectanglevisibility is equal to {feedback_rectangle_visibility_expected}".format(feedback_rectangle_visibility_expected=feedback_rectangle_visibility_expected), "mcrhci", "hcitracer", validate_feedback_rectangle_visibility),
                        InformationSet("get feedback_rectangleforeground_color", "thriver", "mcrhci", get_feedback_rectangle_foreground_color),
                        InformationSet("validate feedback_rectangleforeground_color is equal to {feedback_rectangle_foreground_color_expected}".format(feedback_rectangle_foreground_color_expected=feedback_rectangle_foreground_color_expected), "mcrhci", "hcitracer", validate_feedback_rectangle_foreground_color),
                        InformationSet("get feedback_rectanglebackground_color", "thriver", "mcrhci", get_feedback_rectangle_background_color),
                        InformationSet("validate feedback_rectanglebackground_color is equal to {feedback_rectangle_background_color_expected}".format(feedback_rectangle_background_color_expected=feedback_rectangle_background_color_expected), "mcrhci", "hcitracer", validate_feedback_rectangle_background_color),
                        InformationSet("get mcr7_global_range_statusvisibility", "thriver", "mcrhci", get_mcr7_global_range_status_visibility),
                        InformationSet("validate mcr7_global_range_statusvisibility is equal to {mcr7_global_range_status_visibility_expected}".format(mcr7_global_range_status_visibility_expected=mcr7_global_range_status_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_global_range_status_visibility),
                        InformationSet("get mcr7_global_range_statusvalue", "thriver", "mcrhci", get_mcr7_global_range_status_value),
                        InformationSet("validate mcr7_global_range_statusvalue is equal to {mcr7_global_range_status_value_expected}".format(mcr7_global_range_status_value_expected=mcr7_global_range_status_value_expected), "mcrhci", "hcitracer", validate_mcr7_global_range_status_value),
                        InformationSet("get mcr7_global_range_statusforeground_color", "thriver", "mcrhci", get_mcr7_global_range_status_foreground_color),
                        InformationSet("validate mcr7_global_range_statusforeground_color is equal to {mcr7_global_range_status_foreground_color_expected}".format(mcr7_global_range_status_foreground_color_expected=mcr7_global_range_status_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_global_range_status_foreground_color),
                        InformationSet("get mcr7_global_range_statusbackground_color", "thriver", "mcrhci", get_mcr7_global_range_status_background_color),
                        InformationSet("validate mcr7_global_range_statusbackground_color is equal to {mcr7_global_range_status_background_color_expected}".format(mcr7_global_range_status_background_color_expected=mcr7_global_range_status_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_global_range_status_background_color),
                        InformationSet("get mcr7_range_fieldvisibility", "thriver", "mcrhci", get_mcr7_range_field_visibility),
                        InformationSet("validate mcr7_range_fieldvisibility is equal to {mcr7_range_field_visibility_expected}".format(mcr7_range_field_visibility_expected=mcr7_range_field_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_range_field_visibility),
                        InformationSet("get mcr7_range_fieldvalue", "thriver", "mcrhci", get_mcr7_range_field_value),
                        InformationSet("validate mcr7_range_fieldvalue is equal to {mcr7_range_field_value_expected}".format(mcr7_range_field_value_expected=mcr7_range_field_value_expected), "mcrhci", "hcitracer", validate_mcr7_range_field_value),
                        InformationSet("get mcr7_range_fieldforeground_color", "thriver", "mcrhci", get_mcr7_range_field_foreground_color),
                        InformationSet("validate mcr7_range_fieldforeground_color is equal to {mcr7_range_field_foreground_color_expected}".format(mcr7_range_field_foreground_color_expected=mcr7_range_field_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_range_field_foreground_color),
                        InformationSet("get mcr7_range_fieldbackground_color", "thriver", "mcrhci", get_mcr7_range_field_background_color),
                        InformationSet("validate mcr7_range_fieldbackground_color is equal to {mcr7_range_field_background_color_expected}".format(mcr7_range_field_background_color_expected=mcr7_range_field_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_range_field_background_color),
                        InformationSet("get mcr7_sl1xvisibility", "thriver", "mcrhci", get_mcr7_sl1x_visibility),
                        InformationSet("validate mcr7_sl1xvisibility is equal to {mcr7_sl1x_visibility_expected}".format(mcr7_sl1x_visibility_expected=mcr7_sl1x_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_sl1x_visibility),
                        InformationSet("get mcr7_sl1xvalue", "thriver", "mcrhci", get_mcr7_sl1x_value),
                        InformationSet("validate mcr7_sl1xvalue is equal to {mcr7_sl1x_value_expected}".format(mcr7_sl1x_value_expected=mcr7_sl1x_value_expected), "mcrhci", "hcitracer", validate_mcr7_sl1x_value),
                        InformationSet("get mcr7_sl1xforeground_color", "thriver", "mcrhci", get_mcr7_sl1x_foreground_color),
                        InformationSet("validate mcr7_sl1xforeground_color is equal to {mcr7_sl1x_foreground_color_expected}".format(mcr7_sl1x_foreground_color_expected=mcr7_sl1x_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_sl1x_foreground_color),
                        InformationSet("get mcr7_sl1xbackground_color", "thriver", "mcrhci", get_mcr7_sl1x_background_color),
                        InformationSet("validate mcr7_sl1xbackground_color is equal to {mcr7_sl1x_background_color_expected}".format(mcr7_sl1x_background_color_expected=mcr7_sl1x_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_sl1x_background_color),
                        InformationSet("get mcr7_sl1yvisibility", "thriver", "mcrhci", get_mcr7_sl1y_visibility),
                        InformationSet("validate mcr7_sl1yvisibility is equal to {mcr7_sl1y_visibility_expected}".format(mcr7_sl1y_visibility_expected=mcr7_sl1y_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_sl1y_visibility),
                        InformationSet("get mcr7_sl1yvalue", "thriver", "mcrhci", get_mcr7_sl1y_value),
                        InformationSet("validate mcr7_sl1yvalue is equal to {mcr7_sl1y_value_expected}".format(mcr7_sl1y_value_expected=mcr7_sl1y_value_expected), "mcrhci", "hcitracer", validate_mcr7_sl1y_value),
                        InformationSet("get mcr7_sl1yforeground_color", "thriver", "mcrhci", get_mcr7_sl1y_foreground_color),
                        InformationSet("validate mcr7_sl1yforeground_color is equal to {mcr7_sl1y_foreground_color_expected}".format(mcr7_sl1y_foreground_color_expected=mcr7_sl1y_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_sl1y_foreground_color),
                        InformationSet("get mcr7_sl1ybackground_color", "thriver", "mcrhci", get_mcr7_sl1y_background_color),
                        InformationSet("validate mcr7_sl1ybackground_color is equal to {mcr7_sl1y_background_color_expected}".format(mcr7_sl1y_background_color_expected=mcr7_sl1y_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_sl1y_background_color),
                        InformationSet("get mcr7_sl2xvisibility", "thriver", "mcrhci", get_mcr7_sl2x_visibility),
                        InformationSet("validate mcr7_sl2xvisibility is equal to {mcr7_sl2x_visibility_expected}".format(mcr7_sl2x_visibility_expected=mcr7_sl2x_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_sl2x_visibility),
                        InformationSet("get mcr7_sl2xvalue", "thriver", "mcrhci", get_mcr7_sl2x_value),
                        InformationSet("validate mcr7_sl2xvalue is equal to {mcr7_sl2x_value_expected}".format(mcr7_sl2x_value_expected=mcr7_sl2x_value_expected), "mcrhci", "hcitracer", validate_mcr7_sl2x_value),
                        InformationSet("get mcr7_sl2xforeground_color", "thriver", "mcrhci", get_mcr7_sl2x_foreground_color),
                        InformationSet("validate mcr7_sl2xforeground_color is equal to {mcr7_sl2x_foreground_color_expected}".format(mcr7_sl2x_foreground_color_expected=mcr7_sl2x_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_sl2x_foreground_color),
                        InformationSet("get mcr7_sl2xbackground_color", "thriver", "mcrhci", get_mcr7_sl2x_background_color),
                        InformationSet("validate mcr7_sl2xbackground_color is equal to {mcr7_sl2x_background_color_expected}".format(mcr7_sl2x_background_color_expected=mcr7_sl2x_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_sl2x_background_color),
                        InformationSet("get mcr7_graphite_step_labelvisibility", "thriver", "mcrhci", get_mcr7_graphite_step_label_visibility),
                        InformationSet("validate mcr7_graphite_step_labelvisibility is equal to {mcr7_graphite_step_label_visibility_expected}".format(mcr7_graphite_step_label_visibility_expected=mcr7_graphite_step_label_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_graphite_step_label_visibility),
                        InformationSet("get mcr7_graphite_step_labelvalue", "thriver", "mcrhci", get_mcr7_graphite_step_label_value),
                        InformationSet("validate mcr7_graphite_step_labelvalue is equal to {mcr7_graphite_step_label_value_expected}".format(mcr7_graphite_step_label_value_expected=mcr7_graphite_step_label_value_expected), "mcrhci", "hcitracer", validate_mcr7_graphite_step_label_value),
                        InformationSet("get mcr7_graphite_step_labelforeground_color", "thriver", "mcrhci", get_mcr7_graphite_step_label_foreground_color),
                        InformationSet("validate mcr7_graphite_step_labelforeground_color is equal to {mcr7_graphite_step_label_foreground_color_expected}".format(mcr7_graphite_step_label_foreground_color_expected=mcr7_graphite_step_label_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_graphite_step_label_foreground_color),
                        InformationSet("get mcr7_graphite_step_labelbackground_color", "thriver", "mcrhci", get_mcr7_graphite_step_label_background_color),
                        InformationSet("validate mcr7_graphite_step_labelbackground_color is equal to {mcr7_graphite_step_label_background_color_expected}".format(mcr7_graphite_step_label_background_color_expected=mcr7_graphite_step_label_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_graphite_step_label_background_color),
                        InformationSet("get mcr7_iseu2btnvisibility", "thriver", "mcrhci", get_mcr7_iseu2btn_visibility),
                        InformationSet("validate mcr7_iseu2btnvisibility is equal to {mcr7_iseu2btn_visibility_expected}".format(mcr7_iseu2btn_visibility_expected=mcr7_iseu2btn_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_iseu2btn_visibility),
                        InformationSet("get mcr7_iseu2btnforeground_color", "thriver", "mcrhci", get_mcr7_iseu2btn_foreground_color),
                        InformationSet("validate mcr7_iseu2btnforeground_color is equal to {mcr7_iseu2btn_foreground_color_expected}".format(mcr7_iseu2btn_foreground_color_expected=mcr7_iseu2btn_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_iseu2btn_foreground_color),
                        InformationSet("get mcr7_iseu2btnbackground_color", "thriver", "mcrhci", get_mcr7_iseu2btn_background_color),
                        InformationSet("validate mcr7_iseu2btnbackground_color is equal to {mcr7_iseu2btn_background_color_expected}".format(mcr7_iseu2btn_background_color_expected=mcr7_iseu2btn_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_iseu2btn_background_color),
                        InformationSet("get mcr7_graphite_stepvisibility", "thriver", "mcrhci", get_mcr7_graphite_step_visibility),
                        InformationSet("validate mcr7_graphite_stepvisibility is equal to {mcr7_graphite_step_visibility_expected}".format(mcr7_graphite_step_visibility_expected=mcr7_graphite_step_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_graphite_step_visibility),
                        InformationSet("get mcr7_graphite_stepvalue", "thriver", "mcrhci", get_mcr7_graphite_step_value),
                        InformationSet("validate mcr7_graphite_stepvalue is equal to {mcr7_graphite_step_value_expected}".format(mcr7_graphite_step_value_expected=mcr7_graphite_step_value_expected), "mcrhci", "hcitracer", validate_mcr7_graphite_step_value),
                        InformationSet("get mcr7_graphite_stepforeground_color", "thriver", "mcrhci", get_mcr7_graphite_step_foreground_color),
                        InformationSet("validate mcr7_graphite_stepforeground_color is equal to {mcr7_graphite_step_foreground_color_expected}".format(mcr7_graphite_step_foreground_color_expected=mcr7_graphite_step_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_graphite_step_foreground_color),
                        InformationSet("get mcr7_graphite_stepbackground_color", "thriver", "mcrhci", get_mcr7_graphite_step_background_color),
                        InformationSet("validate mcr7_graphite_stepbackground_color is equal to {mcr7_graphite_step_background_color_expected}".format(mcr7_graphite_step_background_color_expected=mcr7_graphite_step_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_graphite_step_background_color),
                        InformationSet("get mcr7_setrange2btnvisibility", "thriver", "mcrhci", get_mcr7_setrange2btn_visibility),
                        InformationSet("validate mcr7_setrange2btnvisibility is equal to {mcr7_setrange2btn_visibility_expected}".format(mcr7_setrange2btn_visibility_expected=mcr7_setrange2btn_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_setrange2btn_visibility),
                        InformationSet("get mcr7_setrange2btnforeground_color", "thriver", "mcrhci", get_mcr7_setrange2btn_foreground_color),
                        InformationSet("validate mcr7_setrange2btnforeground_color is equal to {mcr7_setrange2btn_foreground_color_expected}".format(mcr7_setrange2btn_foreground_color_expected=mcr7_setrange2btn_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_setrange2btn_foreground_color),
                        InformationSet("get mcr7_setrange2btnbackground_color", "thriver", "mcrhci", get_mcr7_setrange2btn_background_color),
                        InformationSet("validate mcr7_setrange2btnbackground_color is equal to {mcr7_setrange2btn_background_color_expected}".format(mcr7_setrange2btn_background_color_expected=mcr7_setrange2btn_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_setrange2btn_background_color),
                        InformationSet("get mcr7_gantry_anglevisibility", "thriver", "mcrhci", get_mcr7_gantry_angle_visibility),
                        InformationSet("validate mcr7_gantry_anglevisibility is equal to {mcr7_gantry_angle_visibility_expected}".format(mcr7_gantry_angle_visibility_expected=mcr7_gantry_angle_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_gantry_angle_visibility),
                        InformationSet("get mcr7_gantry_anglevalue", "thriver", "mcrhci", get_mcr7_gantry_angle_value),
                        InformationSet("validate mcr7_gantry_anglevalue is equal to {mcr7_gantry_angle_value_expected}".format(mcr7_gantry_angle_value_expected=mcr7_gantry_angle_value_expected), "mcrhci", "hcitracer", validate_mcr7_gantry_angle_value),
                        InformationSet("get mcr7_gantry_angleforeground_color", "thriver", "mcrhci", get_mcr7_gantry_angle_foreground_color),
                        InformationSet("validate mcr7_gantry_angleforeground_color is equal to {mcr7_gantry_angle_foreground_color_expected}".format(mcr7_gantry_angle_foreground_color_expected=mcr7_gantry_angle_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_gantry_angle_foreground_color),
                        InformationSet("get mcr7_gantry_anglebackground_color", "thriver", "mcrhci", get_mcr7_gantry_angle_background_color),
                        InformationSet("validate mcr7_gantry_anglebackground_color is equal to {mcr7_gantry_angle_background_color_expected}".format(mcr7_gantry_angle_background_color_expected=mcr7_gantry_angle_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_gantry_angle_background_color),
                        InformationSet("get mcr7_q30visibility", "thriver", "mcrhci", get_mcr7_q30_visibility),
                        InformationSet("validate mcr7_q30visibility is equal to {mcr7_q30_visibility_expected}".format(mcr7_q30_visibility_expected=mcr7_q30_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_q30_visibility),
                        InformationSet("get mcr7_q30value", "thriver", "mcrhci", get_mcr7_q30_value),
                        InformationSet("validate mcr7_q30value is equal to {mcr7_q30_value_expected}".format(mcr7_q30_value_expected=mcr7_q30_value_expected), "mcrhci", "hcitracer", validate_mcr7_q30_value),
                        InformationSet("get mcr7_q30foreground_color", "thriver", "mcrhci", get_mcr7_q30_foreground_color),
                        InformationSet("validate mcr7_q30foreground_color is equal to {mcr7_q30_foreground_color_expected}".format(mcr7_q30_foreground_color_expected=mcr7_q30_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_q30_foreground_color),
                        InformationSet("get mcr7_q30background_color", "thriver", "mcrhci", get_mcr7_q30_background_color),
                        InformationSet("validate mcr7_q30background_color is equal to {mcr7_q30_background_color_expected}".format(mcr7_q30_background_color_expected=mcr7_q30_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_q30_background_color),
                        InformationSet("get mcr7_q31visibility", "thriver", "mcrhci", get_mcr7_q31_visibility),
                        InformationSet("validate mcr7_q31visibility is equal to {mcr7_q31_visibility_expected}".format(mcr7_q31_visibility_expected=mcr7_q31_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_q31_visibility),
                        InformationSet("get mcr7_q31value", "thriver", "mcrhci", get_mcr7_q31_value),
                        InformationSet("validate mcr7_q31value is equal to {mcr7_q31_value_expected}".format(mcr7_q31_value_expected=mcr7_q31_value_expected), "mcrhci", "hcitracer", validate_mcr7_q31_value),
                        InformationSet("get mcr7_q31foreground_color", "thriver", "mcrhci", get_mcr7_q31_foreground_color),
                        InformationSet("validate mcr7_q31foreground_color is equal to {mcr7_q31_foreground_color_expected}".format(mcr7_q31_foreground_color_expected=mcr7_q31_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_q31_foreground_color),
                        InformationSet("get mcr7_q31background_color", "thriver", "mcrhci", get_mcr7_q31_background_color),
                        InformationSet("validate mcr7_q31background_color is equal to {mcr7_q31_background_color_expected}".format(mcr7_q31_background_color_expected=mcr7_q31_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_q31_background_color),
                        InformationSet("get mcr7_q32visibility", "thriver", "mcrhci", get_mcr7_q32_visibility),
                        InformationSet("validate mcr7_q32visibility is equal to {mcr7_q32_visibility_expected}".format(mcr7_q32_visibility_expected=mcr7_q32_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_q32_visibility),
                        InformationSet("get mcr7_q32value", "thriver", "mcrhci", get_mcr7_q32_value),
                        InformationSet("validate mcr7_q32value is equal to {mcr7_q32_value_expected}".format(mcr7_q32_value_expected=mcr7_q32_value_expected), "mcrhci", "hcitracer", validate_mcr7_q32_value),
                        InformationSet("get mcr7_q32foreground_color", "thriver", "mcrhci", get_mcr7_q32_foreground_color),
                        InformationSet("validate mcr7_q32foreground_color is equal to {mcr7_q32_foreground_color_expected}".format(mcr7_q32_foreground_color_expected=mcr7_q32_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_q32_foreground_color),
                        InformationSet("get mcr7_q32background_color", "thriver", "mcrhci", get_mcr7_q32_background_color),
                        InformationSet("validate mcr7_q32background_color is equal to {mcr7_q32_background_color_expected}".format(mcr7_q32_background_color_expected=mcr7_q32_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_q32_background_color),
                        InformationSet("get mcr7_q33visibility", "thriver", "mcrhci", get_mcr7_q33_visibility),
                        InformationSet("validate mcr7_q33visibility is equal to {mcr7_q33_visibility_expected}".format(mcr7_q33_visibility_expected=mcr7_q33_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_q33_visibility),
                        InformationSet("get mcr7_q33value", "thriver", "mcrhci", get_mcr7_q33_value),
                        InformationSet("validate mcr7_q33value is equal to {mcr7_q33_value_expected}".format(mcr7_q33_value_expected=mcr7_q33_value_expected), "mcrhci", "hcitracer", validate_mcr7_q33_value),
                        InformationSet("get mcr7_q33foreground_color", "thriver", "mcrhci", get_mcr7_q33_foreground_color),
                        InformationSet("validate mcr7_q33foreground_color is equal to {mcr7_q33_foreground_color_expected}".format(mcr7_q33_foreground_color_expected=mcr7_q33_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_q33_foreground_color),
                        InformationSet("get mcr7_q33background_color", "thriver", "mcrhci", get_mcr7_q33_background_color),
                        InformationSet("validate mcr7_q33background_color is equal to {mcr7_q33_background_color_expected}".format(mcr7_q33_background_color_expected=mcr7_q33_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_q33_background_color),
                        InformationSet("get mcr7_q34visibility", "thriver", "mcrhci", get_mcr7_q34_visibility),
                        InformationSet("validate mcr7_q34visibility is equal to {mcr7_q34_visibility_expected}".format(mcr7_q34_visibility_expected=mcr7_q34_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_q34_visibility),
                        InformationSet("get mcr7_q34value", "thriver", "mcrhci", get_mcr7_q34_value),
                        InformationSet("validate mcr7_q34value is equal to {mcr7_q34_value_expected}".format(mcr7_q34_value_expected=mcr7_q34_value_expected), "mcrhci", "hcitracer", validate_mcr7_q34_value),
                        InformationSet("get mcr7_q34foreground_color", "thriver", "mcrhci", get_mcr7_q34_foreground_color),
                        InformationSet("validate mcr7_q34foreground_color is equal to {mcr7_q34_foreground_color_expected}".format(mcr7_q34_foreground_color_expected=mcr7_q34_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_q34_foreground_color),
                        InformationSet("get mcr7_q34background_color", "thriver", "mcrhci", get_mcr7_q34_background_color),
                        InformationSet("validate mcr7_q34background_color is equal to {mcr7_q34_background_color_expected}".format(mcr7_q34_background_color_expected=mcr7_q34_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_q34_background_color),
                        InformationSet("get mcr7_t10visibility", "thriver", "mcrhci", get_mcr7_t10_visibility),
                        InformationSet("validate mcr7_t10visibility is equal to {mcr7_t10_visibility_expected}".format(mcr7_t10_visibility_expected=mcr7_t10_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_t10_visibility),
                        InformationSet("get mcr7_t10value", "thriver", "mcrhci", get_mcr7_t10_value),
                        InformationSet("validate mcr7_t10value is equal to {mcr7_t10_value_expected}".format(mcr7_t10_value_expected=mcr7_t10_value_expected), "mcrhci", "hcitracer", validate_mcr7_t10_value),
                        InformationSet("get mcr7_t10foreground_color", "thriver", "mcrhci", get_mcr7_t10_foreground_color),
                        InformationSet("validate mcr7_t10foreground_color is equal to {mcr7_t10_foreground_color_expected}".format(mcr7_t10_foreground_color_expected=mcr7_t10_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_t10_foreground_color),
                        InformationSet("get mcr7_t10background_color", "thriver", "mcrhci", get_mcr7_t10_background_color),
                        InformationSet("validate mcr7_t10background_color is equal to {mcr7_t10_background_color_expected}".format(mcr7_t10_background_color_expected=mcr7_t10_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_t10_background_color),
                        InformationSet("get mcr7_t11visibility", "thriver", "mcrhci", get_mcr7_t11_visibility),
                        InformationSet("validate mcr7_t11visibility is equal to {mcr7_t11_visibility_expected}".format(mcr7_t11_visibility_expected=mcr7_t11_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_t11_visibility),
                        InformationSet("get mcr7_t11value", "thriver", "mcrhci", get_mcr7_t11_value),
                        InformationSet("validate mcr7_t11value is equal to {mcr7_t11_value_expected}".format(mcr7_t11_value_expected=mcr7_t11_value_expected), "mcrhci", "hcitracer", validate_mcr7_t11_value),
                        InformationSet("get mcr7_t11foreground_color", "thriver", "mcrhci", get_mcr7_t11_foreground_color),
                        InformationSet("validate mcr7_t11foreground_color is equal to {mcr7_t11_foreground_color_expected}".format(mcr7_t11_foreground_color_expected=mcr7_t11_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_t11_foreground_color),
                        InformationSet("get mcr7_t11background_color", "thriver", "mcrhci", get_mcr7_t11_background_color),
                        InformationSet("validate mcr7_t11background_color is equal to {mcr7_t11_background_color_expected}".format(mcr7_t11_background_color_expected=mcr7_t11_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_t11_background_color),
                        InformationSet("get mcr7_t12visibility", "thriver", "mcrhci", get_mcr7_t12_visibility),
                        InformationSet("validate mcr7_t12visibility is equal to {mcr7_t12_visibility_expected}".format(mcr7_t12_visibility_expected=mcr7_t12_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_t12_visibility),
                        InformationSet("get mcr7_t12value", "thriver", "mcrhci", get_mcr7_t12_value),
                        InformationSet("validate mcr7_t12value is equal to {mcr7_t12_value_expected}".format(mcr7_t12_value_expected=mcr7_t12_value_expected), "mcrhci", "hcitracer", validate_mcr7_t12_value),
                        InformationSet("get mcr7_t12foreground_color", "thriver", "mcrhci", get_mcr7_t12_foreground_color),
                        InformationSet("validate mcr7_t12foreground_color is equal to {mcr7_t12_foreground_color_expected}".format(mcr7_t12_foreground_color_expected=mcr7_t12_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_t12_foreground_color),
                        InformationSet("get mcr7_t12background_color", "thriver", "mcrhci", get_mcr7_t12_background_color),
                        InformationSet("validate mcr7_t12background_color is equal to {mcr7_t12_background_color_expected}".format(mcr7_t12_background_color_expected=mcr7_t12_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_t12_background_color),
                        InformationSet("get mcr7_degrader_statusvisibility", "thriver", "mcrhci", get_mcr7_degrader_status_visibility),
                        InformationSet("validate mcr7_degrader_statusvisibility is equal to {mcr7_degrader_status_visibility_expected}".format(mcr7_degrader_status_visibility_expected=mcr7_degrader_status_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_degrader_status_visibility),
                        InformationSet("get mcr7_degrader_statusvalue", "thriver", "mcrhci", get_mcr7_degrader_status_value),
                        InformationSet("validate mcr7_degrader_statusvalue is equal to {mcr7_degrader_status_value_expected}".format(mcr7_degrader_status_value_expected=mcr7_degrader_status_value_expected), "mcrhci", "hcitracer", validate_mcr7_degrader_status_value),
                        InformationSet("get mcr7_degrader_statusforeground_color", "thriver", "mcrhci", get_mcr7_degrader_status_foreground_color),
                        InformationSet("validate mcr7_degrader_statusforeground_color is equal to {mcr7_degrader_status_foreground_color_expected}".format(mcr7_degrader_status_foreground_color_expected=mcr7_degrader_status_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_degrader_status_foreground_color),
                        InformationSet("get mcr7_degrader_statusbackground_color", "thriver", "mcrhci", get_mcr7_degrader_status_background_color),
                        InformationSet("validate mcr7_degrader_statusbackground_color is equal to {mcr7_degrader_status_background_color_expected}".format(mcr7_degrader_status_background_color_expected=mcr7_degrader_status_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_degrader_status_background_color),
                        InformationSet("get mcr7_cugantryposfbkvisibility", "thriver", "mcrhci", get_mcr7_cugantryposfbk_visibility),
                        InformationSet("validate mcr7_cugantryposfbkvisibility is equal to {mcr7_cugantryposfbk_visibility_expected}".format(mcr7_cugantryposfbk_visibility_expected=mcr7_cugantryposfbk_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_cugantryposfbk_visibility),
                        InformationSet("get mcr7_cugantryposfbkvalue", "thriver", "mcrhci", get_mcr7_cugantryposfbk_value),
                        InformationSet("validate mcr7_cugantryposfbkvalue is equal to {mcr7_cugantryposfbk_value_expected}".format(mcr7_cugantryposfbk_value_expected=mcr7_cugantryposfbk_value_expected), "mcrhci", "hcitracer", validate_mcr7_cugantryposfbk_value),
                        InformationSet("get mcr7_cugantryposfbkforeground_color", "thriver", "mcrhci", get_mcr7_cugantryposfbk_foreground_color),
                        InformationSet("validate mcr7_cugantryposfbkforeground_color is equal to {mcr7_cugantryposfbk_foreground_color_expected}".format(mcr7_cugantryposfbk_foreground_color_expected=mcr7_cugantryposfbk_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_cugantryposfbk_foreground_color),
                        InformationSet("get mcr7_cugantryposfbkbackground_color", "thriver", "mcrhci", get_mcr7_cugantryposfbk_background_color),
                        InformationSet("validate mcr7_cugantryposfbkbackground_color is equal to {mcr7_cugantryposfbk_background_color_expected}".format(mcr7_cugantryposfbk_background_color_expected=mcr7_cugantryposfbk_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_cugantryposfbk_background_color),
                        InformationSet("get DS_US_mode_textvisibility", "thriver", "mcrhci", get_DS_US_mode_text_visibility),
                        InformationSet("validate DS_US_mode_textvisibility is equal to {DS_US_mode_text_visibility_expected}".format(DS_US_mode_text_visibility_expected=DS_US_mode_text_visibility_expected), "mcrhci", "hcitracer", validate_DS_US_mode_text_visibility),
                        InformationSet("get DS_US_mode_textforeground_color", "thriver", "mcrhci", get_DS_US_mode_text_foreground_color),
                        InformationSet("validate DS_US_mode_textforeground_color is equal to {DS_US_mode_text_foreground_color_expected}".format(DS_US_mode_text_foreground_color_expected=DS_US_mode_text_foreground_color_expected), "mcrhci", "hcitracer", validate_DS_US_mode_text_foreground_color),
                        InformationSet("get DS_US_mode_textbackground_color", "thriver", "mcrhci", get_DS_US_mode_text_background_color),
                        InformationSet("validate DS_US_mode_textbackground_color is equal to {DS_US_mode_text_background_color_expected}".format(DS_US_mode_text_background_color_expected=DS_US_mode_text_background_color_expected), "mcrhci", "hcitracer", validate_DS_US_mode_text_background_color),
                        InformationSet("get PBS_mode_textvisibility", "thriver", "mcrhci", get_PBS_mode_text_visibility),
                        InformationSet("validate PBS_mode_textvisibility is equal to {PBS_mode_text_visibility_expected}".format(PBS_mode_text_visibility_expected=PBS_mode_text_visibility_expected), "mcrhci", "hcitracer", validate_PBS_mode_text_visibility),
                        InformationSet("get PBS_mode_textforeground_color", "thriver", "mcrhci", get_PBS_mode_text_foreground_color),
                        InformationSet("validate PBS_mode_textforeground_color is equal to {PBS_mode_text_foreground_color_expected}".format(PBS_mode_text_foreground_color_expected=PBS_mode_text_foreground_color_expected), "mcrhci", "hcitracer", validate_PBS_mode_text_foreground_color),
                        InformationSet("get PBS_mode_textbackground_color", "thriver", "mcrhci", get_PBS_mode_text_background_color),
                        InformationSet("validate PBS_mode_textbackground_color is equal to {PBS_mode_text_background_color_expected}".format(PBS_mode_text_background_color_expected=PBS_mode_text_background_color_expected), "mcrhci", "hcitracer", validate_PBS_mode_text_background_color),
                        InformationSet("get mcr7_trb5visibility", "thriver", "mcrhci", get_mcr7_trb5_visibility),
                        InformationSet("validate mcr7_trb5visibility is equal to {mcr7_trb5_visibility_expected}".format(mcr7_trb5_visibility_expected=mcr7_trb5_visibility_expected), "mcrhci", "hcitracer", validate_mcr7_trb5_visibility),
                        InformationSet("get mcr7_trb5value", "thriver", "mcrhci", get_mcr7_trb5_value),
                        InformationSet("validate mcr7_trb5value is equal to {mcr7_trb5_value_expected}".format(mcr7_trb5_value_expected=mcr7_trb5_value_expected), "mcrhci", "hcitracer", validate_mcr7_trb5_value),
                        InformationSet("get mcr7_trb5foreground_color", "thriver", "mcrhci", get_mcr7_trb5_foreground_color),
                        InformationSet("validate mcr7_trb5foreground_color is equal to {mcr7_trb5_foreground_color_expected}".format(mcr7_trb5_foreground_color_expected=mcr7_trb5_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr7_trb5_foreground_color),
                        InformationSet("get mcr7_trb5background_color", "thriver", "mcrhci", get_mcr7_trb5_background_color),
                        InformationSet("validate mcr7_trb5background_color is equal to {mcr7_trb5_background_color_expected}".format(mcr7_trb5_background_color_expected=mcr7_trb5_background_color_expected), "mcrhci", "hcitracer", validate_mcr7_trb5_background_color),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []



