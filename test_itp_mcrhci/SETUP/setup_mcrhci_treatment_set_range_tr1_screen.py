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
from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import COLORS

class SETUP_VALIDATE_OPEN_TREATMENT_SET_RANGE_TR1(ClinicalIntegrationTestProcedure):
    name = 'Validate Treatment Set Range Tr1 Screen'
    # Color Id
    visible = "1"
    notVisible = "0"
    # expected default values
    mcr6_cugantryposfbk_visibility_expected = visible
    mcr6_cugantryposfbk_value_expected = 0
    mcr6_cugantryposfbk_foreground_color_expected = COLORS.colorDict["BLUE_1"] 
    mcr6_cugantryposfbk_background_color_expected = COLORS.colorDict["WHITE_5"] 
    mcr6_range_feedbacktxt_visibility_expected = visible
    mcr6_range_feedbacktxt_value_expected = -1
    mcr6_range_feedbacktxt_foreground_color_expected = COLORS.colorDict["BLUE_1"] 
    mcr6_range_feedbacktxt_background_color_expected = COLORS.colorDict["WHITE_5"] 
    mcr6_q9_visibility_expected = visible
    mcr6_q9_value_expected = 0
    mcr6_q9_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_q9_background_color_expected = COLORS.colorDict["BLACK_1"]
    mcr6_q10_visibility_expected = visible
    mcr6_q10_value_expected = 0
    mcr6_q10_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_q10_background_color_expected = COLORS.colorDict["BLACK_1"]  
    mcr6_q11_visibility_expected = visible
    mcr6_q11_value_expected = 0
    mcr6_q11_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_q11_background_color_expected = COLORS.colorDict["BLACK_1"]
    mcr6_q12_visibility_expected = visible
    mcr6_q12_value_expected = 0
    mcr6_q12_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_q12_background_color_expected = COLORS.colorDict["BLACK_1"]
    mcr6_q13_visibility_expected = visible
    mcr6_q13_value_expected = 0
    mcr6_q13_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_q13_background_color_expected = COLORS.colorDict["BLACK_1"]
    mcr6_q14_visibility_expected = visible
    mcr6_q14_value_expected = 0
    mcr6_q14_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_q14_background_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_q15_visibility_expected = visible
    mcr6_q15_value_expected = 0
    mcr6_q15_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_q15_background_color_expected = COLORS.colorDict["BLACK_1"]   
    mcr6_q20_visibility_expected = visible
    mcr6_q20_value_expected = 0
    mcr6_q20_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_q20_background_color_expected = COLORS.colorDict["BLACK_1"]
    mcr6_q21_visibility_expected = visible
    mcr6_q21_value_expected = 0
    mcr6_q21_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_q21_background_color_expected = COLORS.colorDict["BLACK_1"]
    mcr6_q22_visibility_expected = visible
    mcr6_q22_value_expected = 0
    mcr6_q22_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_q22_background_color_expected = COLORS.colorDict["BLACK_1"]
    mcr6_b1234_visibility_expected = visible
    mcr6_b1234_value_expected = 0
    mcr6_b1234_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_b1234_background_color_expected = COLORS.colorDict["BLACK_1"]  
    mcr6_t6_visibility_expected = visible
    mcr6_t6_value_expected = 0
    mcr6_t6_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_t6_background_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_t7_visibility_expected = visible
    mcr6_t7_value_expected = 0
    mcr6_t7_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_t7_background_color_expected = COLORS.colorDict["BLACK_1"]
    mcr6_trb1_visibility_expected = visible
    mcr6_trb1_value_expected = 0
    mcr6_trb1_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_trb1_background_color_expected = COLORS.colorDict["BLACK_1"]
    mcr6_trb34_visibility_expected = visible
    mcr6_trb34_value_expected = 0
    mcr6_trb34_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_trb34_background_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_q25_visibility_expected = visible
    mcr6_q25_value_expected = 0
    mcr6_q25_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_q25_background_color_expected = COLORS.colorDict["BLACK_1"]
    mcr6_q26_visibility_expected = visible
    mcr6_q26_value_expected = 0
    mcr6_q26_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_q26_background_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_q27_visibility_expected = visible
    mcr6_q27_value_expected = 0
    mcr6_q27_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_q27_background_color_expected = COLORS.colorDict["BLACK_1"]  
    mcr6_b56_visibility_expected = visible
    mcr6_b56_value_expected = 0
    mcr6_b56_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_b56_background_color_expected = COLORS.colorDict["BLACK_1"]
    mcr6_t8_visibility_expected = visible
    mcr6_t8_value_expected = 0
    mcr6_t8_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_t8_background_color_expected = COLORS.colorDict["BLACK_1"]  
    mcr6_trb5_visibility_expected = visible
    mcr6_trb5_value_expected = 0
    mcr6_trb5_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_trb5_background_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_trb6_visibility_expected = visible
    mcr6_trb6_value_expected = 0
    mcr6_trb6_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_trb6_background_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_q0m1_visibility_expected = visible
    mcr6_q0m1_value_expected = 0
    mcr6_q0m1_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_q0m1_background_color_expected = COLORS.colorDict["BLACK_1"]
    mcr6_q1m1_visibility_expected = visible
    mcr6_q1m1_value_expected = 0
    mcr6_q1m1_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_q1m1_background_color_expected = COLORS.colorDict["BLACK_1"]
    mcr6_q2m1_visibility_expected = visible
    mcr6_q2m1_value_expected = 0
    mcr6_q2m1_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_q2m1_background_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_q3m1_visibility_expected = visible
    mcr6_q3m1_value_expected = 0
    mcr6_q3m1_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_q3m1_background_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_q1g1_visibility_expected = visible
    mcr6_q1g1_value_expected = 0
    mcr6_q1g1_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_q1g1_background_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_q2g1_visibility_expected = visible
    mcr6_q2g1_value_expected = 0
    mcr6_q2g1_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_q2g1_background_color_expected = COLORS.colorDict["BLACK_1"]
    mcr6_q3g1_visibility_expected = visible
    mcr6_q3g1_value_expected = 0
    mcr6_q3g1_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_q3g1_background_color_expected = COLORS.colorDict["BLACK_1"]
    mcr6_q4g1_visibility_expected = visible
    mcr6_q4g1_value_expected = 0
    mcr6_q4g1_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_q4g1_background_color_expected = COLORS.colorDict["BLACK_1"]  
    mcr6_q5g1_visibility_expected = visible
    mcr6_q5g1_value_expected = 0
    mcr6_q5g1_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_q5g1_background_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_b1g1_visibility_expected = visible
    mcr6_b1g1_value_expected = 0
    mcr6_b1g1_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_b1g1_background_color_expected = COLORS.colorDict["BLACK_1"]
    mcr6_b2g1_visibility_expected = visible
    mcr6_b2g1_value_expected = 0
    mcr6_b2g1_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_b2g1_background_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_t9g1_visibility_expected = visible
    mcr6_t9g1_value_expected = 0
    mcr6_t9g1_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_t9g1_background_color_expected = COLORS.colorDict["BLACK_1"]  
    mcr6_t10g1_visibility_expected = visible
    mcr6_t10g1_value_expected = 0
    mcr6_t10g1_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_t10g1_background_color_expected = COLORS.colorDict["BLACK_1"] 
    Label1_visibility_expected = visible
    Label1_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    Label1_background_color_expected = COLORS.colorDict["WHITE_5"]
    mcr6_energytxt_visibility_expected = visible
    mcr6_energytxt_value_expected = 0
    mcr6_energytxt_foreground_color_expected = COLORS.colorDict["BLUE_1"] 
    mcr6_energytxt_background_color_expected = COLORS.colorDict["WHITE_5"] 
    Label2_visibility_expected = visible
    Label2_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    Label2_background_color_expected = COLORS.colorDict["WHITE_5"] 
    energy_shape_visibility_expected = visible
    energy_shape_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    energy_shape_background_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_gantry1positiontxt_visibility_expected = visible
    mcr6_gantry1positiontxt_value_expected = -1
    mcr6_gantry1positiontxt_foreground_color_expected = COLORS.colorDict["BLUE_1"] 
    mcr6_gantry1positiontxt_background_color_expected = COLORS.colorDict["WHITE_5"] 
    gantry_shape_visibility_expected = visible
    gantry_shape_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    gantry_shape_background_color_expected = COLORS.colorDict["BLACK_1"] 
    range_edit_shape_visibility_expected = visible
    range_edit_shape_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    range_edit_shape_background_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_global_range_status_visibility_expected = visible
    mcr6_global_range_status_value_expected = 0
    mcr6_global_range_status_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_global_range_status_background_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_fieldtxt_visibility_expected = visible
    mcr6_fieldtxt_value_expected = 0
    mcr6_fieldtxt_foreground_color_expected = COLORS.colorDict["BLUE_1"] 
    mcr6_fieldtxt_background_color_expected = COLORS.colorDict["WHITE_5"] 
    field_shape_visibility_expected = visible
    field_shape_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    field_shape_background_color_expected = COLORS.colorDict["BLACK_1"]
    mcr6_sl1x_visibility_expected = visible
    mcr6_sl1x_value_expected = 0
    mcr6_sl1x_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_sl1x_background_color_expected = COLORS.colorDict["BLACK_1"]
    mcr6_sl1y_visibility_expected = visible
    mcr6_sl1y_value_expected = 0
    mcr6_sl1y_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_sl1y_background_color_expected = COLORS.colorDict["BLACK_1"]   
    mcr6_sl2x_visibility_expected = visible
    mcr6_sl2x_value_expected = 0
    mcr6_sl2x_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_sl2x_background_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_graphitestepreached_visibility_expected = notVisible
    mcr6_graphitestepreached_value_expected = 0
    mcr6_graphitestepreached_foreground_color_expected = COLORS.colorDict["BLUE_1"] 
    mcr6_graphitestepreached_background_color_expected = COLORS.colorDict["WHITE_5"] 
    mcr6_graphitestepreached_value_visibility_expected = notVisible
    mcr6_graphitestepreached_value_value_expected = 0
    mcr6_graphitestepreached_value_foreground_color_expected = COLORS.colorDict["BLUE_1"] 
    mcr6_graphitestepreached_value_background_color_expected = COLORS.colorDict["WHITE_5"] 
    mcr6_setrangebtn_visibility_expected = visible
    mcr6_setrangebtn_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_setrangebtn_background_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_degrader_status_visibility_expected = visible
    mcr6_degrader_status_value_expected = 0
    mcr6_degrader_status_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_degrader_status_background_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_iseu1btn_visibility_expected = visible
    mcr6_iseu1btn_foreground_color_expected = COLORS.colorDict["BLACK_1"] 
    mcr6_iseu1btn_background_color_expected = COLORS.colorDict["BLACK_1"] 

    def __init__(self, test):   
        cls = type(self)
        # Modify data from parents class purpose
        name = cls.name 
        mcr6_cugantryposfbk_visibility_expected  = cls.mcr6_cugantryposfbk_visibility_expected
        mcr6_cugantryposfbk_value_expected = cls.mcr6_cugantryposfbk_value_expected
        mcr6_cugantryposfbk_foreground_color_expected = cls.mcr6_cugantryposfbk_foreground_color_expected
        mcr6_cugantryposfbk_background_color_expected = cls.mcr6_cugantryposfbk_background_color_expected 
        mcr6_range_feedbacktxt_visibility_expected  = cls.mcr6_range_feedbacktxt_visibility_expected
        mcr6_range_feedbacktxt_value_expected = cls.mcr6_range_feedbacktxt_value_expected
        mcr6_range_feedbacktxt_foreground_color_expected = cls.mcr6_range_feedbacktxt_foreground_color_expected
        mcr6_range_feedbacktxt_background_color_expected = cls.mcr6_range_feedbacktxt_background_color_expected 
        mcr6_q9_visibility_expected  = cls.mcr6_q9_visibility_expected
        mcr6_q9_value_expected = cls.mcr6_q9_value_expected
        mcr6_q9_foreground_color_expected = cls.mcr6_q9_foreground_color_expected
        mcr6_q9_background_color_expected = cls.mcr6_q9_background_color_expected
        mcr6_q10_visibility_expected  = cls.mcr6_q10_visibility_expected
        mcr6_q10_value_expected = cls.mcr6_q10_value_expected
        mcr6_q10_foreground_color_expected = cls.mcr6_q10_foreground_color_expected
        mcr6_q10_background_color_expected = cls.mcr6_q10_background_color_expected
        mcr6_q11_visibility_expected  = cls.mcr6_q11_visibility_expected
        mcr6_q11_value_expected = cls.mcr6_q11_value_expected
        mcr6_q11_foreground_color_expected = cls.mcr6_q11_foreground_color_expected
        mcr6_q11_background_color_expected = cls.mcr6_q11_background_color_expected
        mcr6_q12_visibility_expected  = cls.mcr6_q12_visibility_expected
        mcr6_q12_value_expected = cls.mcr6_q12_value_expected
        mcr6_q12_foreground_color_expected = cls.mcr6_q12_foreground_color_expected
        mcr6_q12_background_color_expected = cls.mcr6_q12_background_color_expected 
        mcr6_q13_visibility_expected  = cls.mcr6_q13_visibility_expected
        mcr6_q13_value_expected = cls.mcr6_q13_value_expected
        mcr6_q13_foreground_color_expected = cls.mcr6_q13_foreground_color_expected
        mcr6_q13_background_color_expected = cls.mcr6_q13_background_color_expected 
        mcr6_q14_visibility_expected  = cls.mcr6_q14_visibility_expected
        mcr6_q14_value_expected = cls.mcr6_q14_value_expected
        mcr6_q14_foreground_color_expected = cls.mcr6_q14_foreground_color_expected
        mcr6_q14_background_color_expected = cls.mcr6_q14_background_color_expected 
        mcr6_q15_visibility_expected  = cls.mcr6_q15_visibility_expected
        mcr6_q15_value_expected = cls.mcr6_q15_value_expected
        mcr6_q15_foreground_color_expected = cls.mcr6_q15_foreground_color_expected
        mcr6_q15_background_color_expected = cls.mcr6_q15_background_color_expected
        mcr6_q20_visibility_expected  = cls.mcr6_q20_visibility_expected
        mcr6_q20_value_expected = cls.mcr6_q20_value_expected
        mcr6_q20_foreground_color_expected = cls.mcr6_q20_foreground_color_expected
        mcr6_q20_background_color_expected = cls.mcr6_q20_background_color_expected
        mcr6_q21_visibility_expected  = cls.mcr6_q21_visibility_expected
        mcr6_q21_value_expected = cls.mcr6_q21_value_expected
        mcr6_q21_foreground_color_expected = cls.mcr6_q21_foreground_color_expected
        mcr6_q21_background_color_expected = cls.mcr6_q21_background_color_expected
        mcr6_q22_visibility_expected  = cls.mcr6_q22_visibility_expected
        mcr6_q22_value_expected = cls.mcr6_q22_value_expected
        mcr6_q22_foreground_color_expected = cls.mcr6_q22_foreground_color_expected
        mcr6_q22_background_color_expected = cls.mcr6_q22_background_color_expected
        mcr6_b1234_visibility_expected  = cls.mcr6_b1234_visibility_expected
        mcr6_b1234_value_expected = cls.mcr6_b1234_value_expected
        mcr6_b1234_foreground_color_expected = cls.mcr6_b1234_foreground_color_expected
        mcr6_b1234_background_color_expected = cls.mcr6_b1234_background_color_expected 
        mcr6_t6_visibility_expected  = cls.mcr6_t6_visibility_expected
        mcr6_t6_value_expected = cls.mcr6_t6_value_expected
        mcr6_t6_foreground_color_expected = cls.mcr6_t6_foreground_color_expected
        mcr6_t6_background_color_expected = cls.mcr6_t6_background_color_expected
        mcr6_t7_visibility_expected  = cls.mcr6_t7_visibility_expected
        mcr6_t7_value_expected = cls.mcr6_t7_value_expected
        mcr6_t7_foreground_color_expected = cls.mcr6_t7_foreground_color_expected
        mcr6_t7_background_color_expected = cls.mcr6_t7_background_color_expected
        mcr6_trb1_visibility_expected  = cls.mcr6_trb1_visibility_expected
        mcr6_trb1_value_expected = cls.mcr6_trb1_value_expected
        mcr6_trb1_foreground_color_expected = cls.mcr6_trb1_foreground_color_expected
        mcr6_trb1_background_color_expected = cls.mcr6_trb1_background_color_expected 
        mcr6_trb34_visibility_expected  = cls.mcr6_trb34_visibility_expected
        mcr6_trb34_value_expected = cls.mcr6_trb34_value_expected
        mcr6_trb34_foreground_color_expected = cls.mcr6_trb34_foreground_color_expected
        mcr6_trb34_background_color_expected = cls.mcr6_trb34_background_color_expected 
        mcr6_q25_visibility_expected  = cls.mcr6_q25_visibility_expected
        mcr6_q25_value_expected = cls.mcr6_q25_value_expected
        mcr6_q25_foreground_color_expected = cls.mcr6_q25_foreground_color_expected
        mcr6_q25_background_color_expected = cls.mcr6_q25_background_color_expected 
        mcr6_q26_visibility_expected  = cls.mcr6_q26_visibility_expected
        mcr6_q26_value_expected = cls.mcr6_q26_value_expected
        mcr6_q26_foreground_color_expected = cls.mcr6_q26_foreground_color_expected
        mcr6_q26_background_color_expected = cls.mcr6_q26_background_color_expected
        mcr6_q27_visibility_expected  = cls.mcr6_q27_visibility_expected
        mcr6_q27_value_expected = cls.mcr6_q27_value_expected
        mcr6_q27_foreground_color_expected = cls.mcr6_q27_foreground_color_expected
        mcr6_q27_background_color_expected = cls.mcr6_q27_background_color_expected
        mcr6_b56_visibility_expected  = cls.mcr6_b56_visibility_expected
        mcr6_b56_value_expected = cls.mcr6_b56_value_expected
        mcr6_b56_foreground_color_expected = cls.mcr6_b56_foreground_color_expected
        mcr6_b56_background_color_expected = cls.mcr6_b56_background_color_expected
        mcr6_t8_visibility_expected  = cls.mcr6_t8_visibility_expected
        mcr6_t8_value_expected = cls.mcr6_t8_value_expected
        mcr6_t8_foreground_color_expected = cls.mcr6_t8_foreground_color_expected
        mcr6_t8_background_color_expected = cls.mcr6_t8_background_color_expected 
        mcr6_trb5_visibility_expected  = cls.mcr6_trb5_visibility_expected
        mcr6_trb5_value_expected = cls.mcr6_trb5_value_expected
        mcr6_trb5_foreground_color_expected = cls.mcr6_trb5_foreground_color_expected
        mcr6_trb5_background_color_expected = cls.mcr6_trb5_background_color_expected 
        mcr6_trb6_visibility_expected  = cls.mcr6_trb6_visibility_expected
        mcr6_trb6_value_expected = cls.mcr6_trb6_value_expected
        mcr6_trb6_foreground_color_expected = cls.mcr6_trb6_foreground_color_expected
        mcr6_trb6_background_color_expected = cls.mcr6_trb6_background_color_expected 
        mcr6_q0m1_visibility_expected  = cls.mcr6_q0m1_visibility_expected
        mcr6_q0m1_value_expected = cls.mcr6_q0m1_value_expected
        mcr6_q0m1_foreground_color_expected = cls.mcr6_q0m1_foreground_color_expected
        mcr6_q0m1_background_color_expected = cls.mcr6_q0m1_background_color_expected 
        mcr6_q1m1_visibility_expected  = cls.mcr6_q1m1_visibility_expected
        mcr6_q1m1_value_expected = cls.mcr6_q1m1_value_expected
        mcr6_q1m1_foreground_color_expected = cls.mcr6_q1m1_foreground_color_expected
        mcr6_q1m1_background_color_expected = cls.mcr6_q1m1_background_color_expected 
        mcr6_q2m1_visibility_expected  = cls.mcr6_q2m1_visibility_expected
        mcr6_q2m1_value_expected = cls.mcr6_q2m1_value_expected
        mcr6_q2m1_foreground_color_expected = cls.mcr6_q2m1_foreground_color_expected
        mcr6_q2m1_background_color_expected = cls.mcr6_q2m1_background_color_expected 
        mcr6_q3m1_visibility_expected  = cls.mcr6_q3m1_visibility_expected
        mcr6_q3m1_value_expected = cls.mcr6_q3m1_value_expected
        mcr6_q3m1_foreground_color_expected = cls.mcr6_q3m1_foreground_color_expected
        mcr6_q3m1_background_color_expected = cls.mcr6_q3m1_background_color_expected
        mcr6_q1g1_visibility_expected  = cls.mcr6_q1g1_visibility_expected
        mcr6_q1g1_value_expected = cls.mcr6_q1g1_value_expected
        mcr6_q1g1_foreground_color_expected = cls.mcr6_q1g1_foreground_color_expected
        mcr6_q1g1_background_color_expected = cls.mcr6_q1g1_background_color_expected 
        mcr6_q2g1_visibility_expected  = cls.mcr6_q2g1_visibility_expected
        mcr6_q2g1_value_expected = cls.mcr6_q2g1_value_expected
        mcr6_q2g1_foreground_color_expected = cls.mcr6_q2g1_foreground_color_expected
        mcr6_q2g1_background_color_expected = cls.mcr6_q2g1_background_color_expected 
        mcr6_q3g1_visibility_expected  = cls.mcr6_q3g1_visibility_expected
        mcr6_q3g1_value_expected = cls.mcr6_q3g1_value_expected
        mcr6_q3g1_foreground_color_expected = cls.mcr6_q3g1_foreground_color_expected
        mcr6_q3g1_background_color_expected = cls.mcr6_q3g1_background_color_expected 
        mcr6_q4g1_visibility_expected  = cls.mcr6_q4g1_visibility_expected
        mcr6_q4g1_value_expected = cls.mcr6_q4g1_value_expected
        mcr6_q4g1_foreground_color_expected = cls.mcr6_q4g1_foreground_color_expected
        mcr6_q4g1_background_color_expected = cls.mcr6_q4g1_background_color_expected 
        mcr6_q5g1_visibility_expected  = cls.mcr6_q5g1_visibility_expected
        mcr6_q5g1_value_expected = cls.mcr6_q5g1_value_expected
        mcr6_q5g1_foreground_color_expected = cls.mcr6_q5g1_foreground_color_expected
        mcr6_q5g1_background_color_expected = cls.mcr6_q5g1_background_color_expected 
        mcr6_b1g1_visibility_expected  = cls.mcr6_b1g1_visibility_expected
        mcr6_b1g1_value_expected = cls.mcr6_b1g1_value_expected
        mcr6_b1g1_foreground_color_expected = cls.mcr6_b1g1_foreground_color_expected
        mcr6_b1g1_background_color_expected = cls.mcr6_b1g1_background_color_expected 
        mcr6_b2g1_visibility_expected  = cls.mcr6_b2g1_visibility_expected
        mcr6_b2g1_value_expected = cls.mcr6_b2g1_value_expected
        mcr6_b2g1_foreground_color_expected = cls.mcr6_b2g1_foreground_color_expected
        mcr6_b2g1_background_color_expected = cls.mcr6_b2g1_background_color_expected 
        mcr6_t9g1_visibility_expected  = cls.mcr6_t9g1_visibility_expected
        mcr6_t9g1_value_expected = cls.mcr6_t9g1_value_expected
        mcr6_t9g1_foreground_color_expected = cls.mcr6_t9g1_foreground_color_expected
        mcr6_t9g1_background_color_expected = cls.mcr6_t9g1_background_color_expected 
        mcr6_t10g1_visibility_expected  = cls.mcr6_t10g1_visibility_expected
        mcr6_t10g1_value_expected = cls.mcr6_t10g1_value_expected
        mcr6_t10g1_foreground_color_expected = cls.mcr6_t10g1_foreground_color_expected
        mcr6_t10g1_background_color_expected = cls.mcr6_t10g1_background_color_expected 
        Label1_visibility_expected  = cls.Label1_visibility_expected
        Label1_foreground_color_expected = cls.Label1_foreground_color_expected
        Label1_background_color_expected = cls.Label1_background_color_expected 
        mcr6_energytxt_visibility_expected  = cls.mcr6_energytxt_visibility_expected
        mcr6_energytxt_value_expected = cls.mcr6_energytxt_value_expected
        mcr6_energytxt_foreground_color_expected = cls.mcr6_energytxt_foreground_color_expected
        mcr6_energytxt_background_color_expected = cls.mcr6_energytxt_background_color_expected
        Label2_visibility_expected  = cls.Label2_visibility_expected
        Label2_foreground_color_expected = cls.Label2_foreground_color_expected
        Label2_background_color_expected = cls.Label2_background_color_expected 
        energy_shape_visibility_expected  = cls.energy_shape_visibility_expected
        energy_shape_foreground_color_expected = cls.energy_shape_foreground_color_expected
        energy_shape_background_color_expected = cls.energy_shape_background_color_expected 
        mcr6_gantry1positiontxt_visibility_expected  = cls.mcr6_gantry1positiontxt_visibility_expected
        mcr6_gantry1positiontxt_value_expected = cls.mcr6_gantry1positiontxt_value_expected
        mcr6_gantry1positiontxt_foreground_color_expected = cls.mcr6_gantry1positiontxt_foreground_color_expected
        mcr6_gantry1positiontxt_background_color_expected = cls.mcr6_gantry1positiontxt_background_color_expected 
        gantry_shape_visibility_expected  = cls.gantry_shape_visibility_expected
        gantry_shape_foreground_color_expected = cls.gantry_shape_foreground_color_expected
        gantry_shape_background_color_expected = cls.gantry_shape_background_color_expected 
        range_edit_shape_visibility_expected  = cls.range_edit_shape_visibility_expected
        range_edit_shape_foreground_color_expected = cls.range_edit_shape_foreground_color_expected
        range_edit_shape_background_color_expected = cls.range_edit_shape_background_color_expected
        mcr6_global_range_status_visibility_expected  = cls.mcr6_global_range_status_visibility_expected
        mcr6_global_range_status_value_expected = cls.mcr6_global_range_status_value_expected
        mcr6_global_range_status_foreground_color_expected = cls.mcr6_global_range_status_foreground_color_expected
        mcr6_global_range_status_background_color_expected = cls.mcr6_global_range_status_background_color_expected
        mcr6_fieldtxt_visibility_expected  = cls.mcr6_fieldtxt_visibility_expected
        mcr6_fieldtxt_value_expected = cls.mcr6_fieldtxt_value_expected
        mcr6_fieldtxt_foreground_color_expected = cls.mcr6_fieldtxt_foreground_color_expected
        mcr6_fieldtxt_background_color_expected = cls.mcr6_fieldtxt_background_color_expected 
        field_shape_visibility_expected  = cls.field_shape_visibility_expected
        field_shape_foreground_color_expected = cls.field_shape_foreground_color_expected
        field_shape_background_color_expected = cls.field_shape_background_color_expected 
        mcr6_sl1x_visibility_expected  = cls.mcr6_sl1x_visibility_expected
        mcr6_sl1x_value_expected = cls.mcr6_sl1x_value_expected
        mcr6_sl1x_foreground_color_expected = cls.mcr6_sl1x_foreground_color_expected
        mcr6_sl1x_background_color_expected = cls.mcr6_sl1x_background_color_expected 
        mcr6_sl1y_visibility_expected  = cls.mcr6_sl1y_visibility_expected
        mcr6_sl1y_value_expected = cls.mcr6_sl1y_value_expected
        mcr6_sl1y_foreground_color_expected = cls.mcr6_sl1y_foreground_color_expected
        mcr6_sl1y_background_color_expected = cls.mcr6_sl1y_background_color_expected 
        mcr6_sl2x_visibility_expected  = cls.mcr6_sl2x_visibility_expected
        mcr6_sl2x_value_expected = cls.mcr6_sl2x_value_expected
        mcr6_sl2x_foreground_color_expected = cls.mcr6_sl2x_foreground_color_expected
        mcr6_sl2x_background_color_expected = cls.mcr6_sl2x_background_color_expected 
        mcr6_graphitestepreached_visibility_expected  = cls.mcr6_graphitestepreached_visibility_expected
        mcr6_graphitestepreached_value_expected = cls.mcr6_graphitestepreached_value_expected
        mcr6_graphitestepreached_foreground_color_expected = cls.mcr6_graphitestepreached_foreground_color_expected
        mcr6_graphitestepreached_background_color_expected = cls.mcr6_graphitestepreached_background_color_expected 
        mcr6_graphitestepreached_value_visibility_expected  = cls.mcr6_graphitestepreached_value_visibility_expected
        mcr6_graphitestepreached_value_value_expected = cls.mcr6_graphitestepreached_value_value_expected
        mcr6_graphitestepreached_value_foreground_color_expected = cls.mcr6_graphitestepreached_value_foreground_color_expected
        mcr6_graphitestepreached_value_background_color_expected = cls.mcr6_graphitestepreached_value_background_color_expected 
        mcr6_setrangebtn_visibility_expected  = cls.mcr6_setrangebtn_visibility_expected
        mcr6_setrangebtn_foreground_color_expected = cls.mcr6_setrangebtn_foreground_color_expected
        mcr6_setrangebtn_background_color_expected = cls.mcr6_setrangebtn_background_color_expected 
        mcr6_degrader_status_visibility_expected  = cls.mcr6_degrader_status_visibility_expected
        mcr6_degrader_status_value_expected = cls.mcr6_degrader_status_value_expected
        mcr6_degrader_status_foreground_color_expected = cls.mcr6_degrader_status_foreground_color_expected
        mcr6_degrader_status_background_color_expected = cls.mcr6_degrader_status_background_color_expected 
        mcr6_iseu1btn_visibility_expected  = cls.mcr6_iseu1btn_visibility_expected
        mcr6_iseu1btn_foreground_color_expected = cls.mcr6_iseu1btn_foreground_color_expected
        mcr6_iseu1btn_background_color_expected = cls.mcr6_iseu1btn_background_color_expected 


        # get values
        get_mcr6_cugantryposfbk_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_cugantryposfbk")
        get_mcr6_cugantryposfbk_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_cugantryposfbk")
        get_mcr6_cugantryposfbk_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_cugantryposfbk")
        get_mcr6_cugantryposfbk_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_cugantryposfbk")
        get_mcr6_range_feedbacktxt_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_range_feedbacktxt")
        get_mcr6_range_feedbacktxt_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_range_feedbacktxt")
        get_mcr6_range_feedbacktxt_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_range_feedbacktxt")
        get_mcr6_range_feedbacktxt_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_range_feedbacktxt")
        get_mcr6_q9_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_q9")
        get_mcr6_q9_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_q9")
        get_mcr6_q9_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q9")
        get_mcr6_q9_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q9")
        get_mcr6_q10_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_q10")
        get_mcr6_q10_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_q10")
        get_mcr6_q10_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q10")
        get_mcr6_q10_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q10")
        get_mcr6_q11_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_q11")
        get_mcr6_q11_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_q11")
        get_mcr6_q11_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q11")
        get_mcr6_q11_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q11")
        get_mcr6_q12_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_q12")
        get_mcr6_q12_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_q12")
        get_mcr6_q12_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q12")
        get_mcr6_q12_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q12")
        get_mcr6_q13_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_q13")
        get_mcr6_q13_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_q13")
        get_mcr6_q13_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q13")
        get_mcr6_q13_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q13")
        get_mcr6_q14_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_q14")
        get_mcr6_q14_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_q14")
        get_mcr6_q14_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q14")
        get_mcr6_q14_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q14")
        get_mcr6_q15_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_q15")
        get_mcr6_q15_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_q15")
        get_mcr6_q15_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q15")
        get_mcr6_q15_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q15")
        get_mcr6_q20_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_q20")
        get_mcr6_q20_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_q20")
        get_mcr6_q20_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q20")
        get_mcr6_q20_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q20")
        get_mcr6_q21_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_q21")
        get_mcr6_q21_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_q21")
        get_mcr6_q21_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q21")
        get_mcr6_q21_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q21")
        get_mcr6_q22_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_q22")
        get_mcr6_q22_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_q22")
        get_mcr6_q22_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q22")
        get_mcr6_q22_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q22")
        get_mcr6_b1234_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_b1234")
        get_mcr6_b1234_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_b1234")
        get_mcr6_b1234_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_b1234")
        get_mcr6_b1234_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_b1234")      
        get_mcr6_t6_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_t6")
        get_mcr6_t6_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_t6")
        get_mcr6_t6_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_t6")
        get_mcr6_t6_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_t6")
        get_mcr6_t7_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_t7")
        get_mcr6_t7_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_t7")
        get_mcr6_t7_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_t7")
        get_mcr6_t7_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_t7")
        get_mcr6_trb1_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_trb1")
        get_mcr6_trb1_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_trb1")
        get_mcr6_trb1_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_trb1")
        get_mcr6_trb1_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_trb1")
        get_mcr6_trb34_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_trb34")
        get_mcr6_trb34_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_trb34")
        get_mcr6_trb34_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_trb34")
        get_mcr6_trb34_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_trb34")
        get_mcr6_q25_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_q25")
        get_mcr6_q25_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_q25")
        get_mcr6_q25_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q25")
        get_mcr6_q25_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q25")
        get_mcr6_q26_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_q26")
        get_mcr6_q26_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_q26")
        get_mcr6_q26_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q26")
        get_mcr6_q26_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q26")
        get_mcr6_q27_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_q27")
        get_mcr6_q27_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_q27")
        get_mcr6_q27_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q27")
        get_mcr6_q27_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q27")
        get_mcr6_b56_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_b56")
        get_mcr6_b56_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_b56")
        get_mcr6_b56_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_b56")
        get_mcr6_b56_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_b56")
        get_mcr6_t8_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_t8")
        get_mcr6_t8_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_t8")
        get_mcr6_t8_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_t8")
        get_mcr6_t8_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_t8")
        get_mcr6_trb5_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_trb5")
        get_mcr6_trb5_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_trb5")
        get_mcr6_trb5_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_trb5")
        get_mcr6_trb5_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_trb5")
        get_mcr6_trb6_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_trb6")
        get_mcr6_trb6_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_trb6")
        get_mcr6_trb6_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_trb6")
        get_mcr6_trb6_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_trb6")
        get_mcr6_q0m1_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_q0m1")
        get_mcr6_q0m1_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_q0m1")
        get_mcr6_q0m1_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q0m1")
        get_mcr6_q0m1_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q0m1")
        get_mcr6_q1m1_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_q1m1")
        get_mcr6_q1m1_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_q1m1")
        get_mcr6_q1m1_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q1m1")
        get_mcr6_q1m1_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q1m1")
        get_mcr6_q2m1_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_q2m1")
        get_mcr6_q2m1_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_q2m1")
        get_mcr6_q2m1_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q2m1")
        get_mcr6_q2m1_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q2m1")
        get_mcr6_q3m1_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_q3m1")
        get_mcr6_q3m1_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_q3m1")
        get_mcr6_q3m1_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q3m1")
        get_mcr6_q3m1_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q3m1")
        get_mcr6_q1g1_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_q1g1")
        get_mcr6_q1g1_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_q1g1")
        get_mcr6_q1g1_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q1g1")
        get_mcr6_q1g1_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q1g1")
        get_mcr6_q2g1_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_q2g1")
        get_mcr6_q2g1_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_q2g1")
        get_mcr6_q2g1_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q2g1")
        get_mcr6_q2g1_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q2g1")
        get_mcr6_q3g1_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_q3g1")
        get_mcr6_q3g1_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_q3g1")
        get_mcr6_q3g1_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q3g1")
        get_mcr6_q3g1_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q3g1")
        get_mcr6_q4g1_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_q4g1")
        get_mcr6_q4g1_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_q4g1")
        get_mcr6_q4g1_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q4g1")
        get_mcr6_q4g1_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q4g1")
        get_mcr6_q5g1_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_q5g1")
        get_mcr6_q5g1_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_q5g1")
        get_mcr6_q5g1_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q5g1")
        get_mcr6_q5g1_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_q5g1")
        get_mcr6_b1g1_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_b1g1")
        get_mcr6_b1g1_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_b1g1")
        get_mcr6_b1g1_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_b1g1")
        get_mcr6_b1g1_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_b1g1")
        get_mcr6_b2g1_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_b2g1")
        get_mcr6_b2g1_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_b2g1")
        get_mcr6_b2g1_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_b2g1")
        get_mcr6_b2g1_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_b2g1")
        get_mcr6_t9g1_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_t9g1")
        get_mcr6_t9g1_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_t9g1")
        get_mcr6_t9g1_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_t9g1")
        get_mcr6_t9g1_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_t9g1")
        get_mcr6_t10g1_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_t10g1")
        get_mcr6_t10g1_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_t10g1")
        get_mcr6_t10g1_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_t10g1")
        get_mcr6_t10g1_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_t10g1")
        get_Label1_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "Label1")
        get_Label1_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "Label1")
        get_Label1_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "Label1")
        get_mcr6_energytxt_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_energytxt")
        get_mcr6_energytxt_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_energytxt")
        get_mcr6_energytxt_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_energytxt")
        get_mcr6_energytxt_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_energytxt")
        get_Label2_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "Label2")
        get_Label2_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "Label2")
        get_Label2_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "Label2")
        get_energy_shape_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "energy_shape")
        get_energy_shape_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "energy_shape")
        get_energy_shape_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "energy_shape")
        get_mcr6_gantry1positiontxt_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_gantry1positiontxt")
        get_mcr6_gantry1positiontxt_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_gantry1positiontxt")
        get_mcr6_gantry1positiontxt_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_gantry1positiontxt")
        get_mcr6_gantry1positiontxt_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_gantry1positiontxt")
        get_gantry_shape_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "gantry_shape")
        get_gantry_shape_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "gantry_shape")
        get_gantry_shape_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "gantry_shape")
        get_range_edit_shape_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "range_edit_shape")
        get_range_edit_shape_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "range_edit_shape")
        get_range_edit_shape_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "range_edit_shape")
        get_mcr6_global_range_status_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_global_range_status")
        get_mcr6_global_range_status_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_global_range_status")
        get_mcr6_global_range_status_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_global_range_status")
        get_mcr6_global_range_status_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_global_range_status")
        get_mcr6_fieldtxt_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_fieldtxt")
        get_mcr6_fieldtxt_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_fieldtxt")
        get_mcr6_fieldtxt_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_fieldtxt")
        get_mcr6_fieldtxt_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_fieldtxt")
        get_field_shape_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "field_shape")
        get_field_shape_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "field_shape")
        get_field_shape_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "field_shape")
        get_mcr6_sl1x_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_sl1x")
        get_mcr6_sl1x_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_sl1x")
        get_mcr6_sl1x_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_sl1x")
        get_mcr6_sl1x_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_sl1x")
        get_mcr6_sl1y_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_sl1y")
        get_mcr6_sl1y_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_sl1y")
        get_mcr6_sl1y_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_sl1y")
        get_mcr6_sl1y_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_sl1y")
        get_mcr6_sl2x_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_sl2x")
        get_mcr6_sl2x_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_sl2x")
        get_mcr6_sl2x_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_sl2x")
        get_mcr6_sl2x_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_sl2x")
        get_mcr6_graphitestepreached_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_graphitestepreached")
        get_mcr6_graphitestepreached_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_graphitestepreached")
        get_mcr6_graphitestepreached_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_graphitestepreached")
        get_mcr6_graphitestepreached_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_graphitestepreached")
        get_mcr6_graphitestepreached_value_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_graphitestepreached_value")
        get_mcr6_graphitestepreached_value_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_graphitestepreached_value")
        get_mcr6_graphitestepreached_value_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_graphitestepreached_value")
        get_mcr6_graphitestepreached_value_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_graphitestepreached_value")
        get_mcr6_setrangebtn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_setrangebtn")
        get_mcr6_setrangebtn_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_setrangebtn")
        get_mcr6_setrangebtn_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_setrangebtn")
        get_mcr6_degrader_status_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_degrader_status")
        get_mcr6_degrader_status_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr6_degrader_status")
        get_mcr6_degrader_status_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_degrader_status")
        get_mcr6_degrader_status_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_degrader_status")
        get_mcr6_iseu1btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr6_iseu1btn")
        get_mcr6_iseu1btn_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_iseu1btn")
        get_mcr6_iseu1btn_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr6_iseu1btn")


        # validate
        validate_mcr6_cugantryposfbk_visibility = MsgTypeString("mcr6_cugantryposfbk:TMMI_MCR_IS_VISIBLE", value=mcr6_cugantryposfbk_visibility_expected)
        validate_mcr6_cugantryposfbk_value = MsgTypeNumeric("mcr6_cugantryposfbk:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_cugantryposfbk_value_expected)
        validate_mcr6_cugantryposfbk_foreground_color = MsgTypeString("mcr6_cugantryposfbk:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_cugantryposfbk_foreground_color_expected)
        validate_mcr6_cugantryposfbk_background_color = MsgTypeString("mcr6_cugantryposfbk:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_cugantryposfbk_background_color_expected)     
        validate_mcr6_range_feedbacktxt_visibility = MsgTypeString("mcr6_range_feedbacktxt:TMMI_MCR_IS_VISIBLE", value=mcr6_range_feedbacktxt_visibility_expected)
        validate_mcr6_range_feedbacktxt_value = MsgTypeNumeric("mcr6_range_feedbacktxt:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_range_feedbacktxt_value_expected)
        validate_mcr6_range_feedbacktxt_foreground_color = MsgTypeString("mcr6_range_feedbacktxt:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_range_feedbacktxt_foreground_color_expected)
        validate_mcr6_range_feedbacktxt_background_color = MsgTypeString("mcr6_range_feedbacktxt:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_range_feedbacktxt_background_color_expected)    
        validate_mcr6_q9_visibility = MsgTypeString("mcr6_q9:TMMI_MCR_IS_VISIBLE", value=mcr6_q9_visibility_expected)
        validate_mcr6_q9_value = MsgTypeNumeric("mcr6_q9:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_q9_value_expected)
        validate_mcr6_q9_foreground_color = MsgTypeString("mcr6_q9:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_q9_foreground_color_expected)
        validate_mcr6_q9_background_color = MsgTypeString("mcr6_q9:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_q9_background_color_expected)
        validate_mcr6_q10_visibility = MsgTypeString("mcr6_q10:TMMI_MCR_IS_VISIBLE", value=mcr6_q10_visibility_expected)
        validate_mcr6_q10_value = MsgTypeNumeric("mcr6_q10:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_q10_value_expected)
        validate_mcr6_q10_foreground_color = MsgTypeString("mcr6_q10:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_q10_foreground_color_expected)
        validate_mcr6_q10_background_color = MsgTypeString("mcr6_q10:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_q10_background_color_expected)
        validate_mcr6_q11_visibility = MsgTypeString("mcr6_q11:TMMI_MCR_IS_VISIBLE", value=mcr6_q11_visibility_expected)
        validate_mcr6_q11_value = MsgTypeNumeric("mcr6_q11:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_q11_value_expected)
        validate_mcr6_q11_foreground_color = MsgTypeString("mcr6_q11:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_q11_foreground_color_expected)
        validate_mcr6_q11_background_color = MsgTypeString("mcr6_q11:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_q11_background_color_expected)
        validate_mcr6_q12_visibility = MsgTypeString("mcr6_q12:TMMI_MCR_IS_VISIBLE", value=mcr6_q12_visibility_expected)
        validate_mcr6_q12_value = MsgTypeNumeric("mcr6_q12:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_q12_value_expected)
        validate_mcr6_q12_foreground_color = MsgTypeString("mcr6_q12:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_q12_foreground_color_expected)
        validate_mcr6_q12_background_color = MsgTypeString("mcr6_q12:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_q12_background_color_expected)      
        validate_mcr6_q13_visibility = MsgTypeString("mcr6_q13:TMMI_MCR_IS_VISIBLE", value=mcr6_q13_visibility_expected)
        validate_mcr6_q13_value = MsgTypeNumeric("mcr6_q13:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_q13_value_expected)
        validate_mcr6_q13_foreground_color = MsgTypeString("mcr6_q13:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_q13_foreground_color_expected)
        validate_mcr6_q13_background_color = MsgTypeString("mcr6_q13:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_q13_background_color_expected)
        validate_mcr6_q14_visibility = MsgTypeString("mcr6_q14:TMMI_MCR_IS_VISIBLE", value=mcr6_q14_visibility_expected)
        validate_mcr6_q14_value = MsgTypeNumeric("mcr6_q14:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_q14_value_expected)
        validate_mcr6_q14_foreground_color = MsgTypeString("mcr6_q14:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_q14_foreground_color_expected)
        validate_mcr6_q14_background_color = MsgTypeString("mcr6_q14:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_q14_background_color_expected)
        validate_mcr6_q15_visibility = MsgTypeString("mcr6_q15:TMMI_MCR_IS_VISIBLE", value=mcr6_q15_visibility_expected)
        validate_mcr6_q15_value = MsgTypeNumeric("mcr6_q15:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_q15_value_expected)
        validate_mcr6_q15_foreground_color = MsgTypeString("mcr6_q15:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_q15_foreground_color_expected)
        validate_mcr6_q15_background_color = MsgTypeString("mcr6_q15:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_q15_background_color_expected)
        validate_mcr6_q20_visibility = MsgTypeString("mcr6_q20:TMMI_MCR_IS_VISIBLE", value=mcr6_q20_visibility_expected)
        validate_mcr6_q20_value = MsgTypeNumeric("mcr6_q20:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_q20_value_expected)
        validate_mcr6_q20_foreground_color = MsgTypeString("mcr6_q20:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_q20_foreground_color_expected)
        validate_mcr6_q20_background_color = MsgTypeString("mcr6_q20:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_q20_background_color_expected)
        validate_mcr6_q21_visibility = MsgTypeString("mcr6_q21:TMMI_MCR_IS_VISIBLE", value=mcr6_q21_visibility_expected)
        validate_mcr6_q21_value = MsgTypeNumeric("mcr6_q21:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_q21_value_expected)
        validate_mcr6_q21_foreground_color = MsgTypeString("mcr6_q21:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_q21_foreground_color_expected)
        validate_mcr6_q21_background_color = MsgTypeString("mcr6_q21:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_q21_background_color_expected)
        validate_mcr6_q22_visibility = MsgTypeString("mcr6_q22:TMMI_MCR_IS_VISIBLE", value=mcr6_q22_visibility_expected)
        validate_mcr6_q22_value = MsgTypeNumeric("mcr6_q22:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_q22_value_expected)
        validate_mcr6_q22_foreground_color = MsgTypeString("mcr6_q22:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_q22_foreground_color_expected)
        validate_mcr6_q22_background_color = MsgTypeString("mcr6_q22:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_q22_background_color_expected)
        validate_mcr6_b1234_visibility = MsgTypeString("mcr6_b1234:TMMI_MCR_IS_VISIBLE", value=mcr6_b1234_visibility_expected)
        validate_mcr6_b1234_value = MsgTypeNumeric("mcr6_b1234:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_b1234_value_expected)
        validate_mcr6_b1234_foreground_color = MsgTypeString("mcr6_b1234:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_b1234_foreground_color_expected)
        validate_mcr6_b1234_background_color = MsgTypeString("mcr6_b1234:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_b1234_background_color_expected)
        validate_mcr6_t6_visibility = MsgTypeString("mcr6_t6:TMMI_MCR_IS_VISIBLE", value=mcr6_t6_visibility_expected)
        validate_mcr6_t6_value = MsgTypeNumeric("mcr6_t6:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_t6_value_expected)
        validate_mcr6_t6_foreground_color = MsgTypeString("mcr6_t6:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_t6_foreground_color_expected)
        validate_mcr6_t6_background_color = MsgTypeString("mcr6_t6:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_t6_background_color_expected)
        validate_mcr6_t7_visibility = MsgTypeString("mcr6_t7:TMMI_MCR_IS_VISIBLE", value=mcr6_t7_visibility_expected)
        validate_mcr6_t7_value = MsgTypeNumeric("mcr6_t7:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_t7_value_expected)
        validate_mcr6_t7_foreground_color = MsgTypeString("mcr6_t7:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_t7_foreground_color_expected)
        validate_mcr6_t7_background_color = MsgTypeString("mcr6_t7:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_t7_background_color_expected)
        validate_mcr6_trb1_visibility = MsgTypeString("mcr6_trb1:TMMI_MCR_IS_VISIBLE", value=mcr6_trb1_visibility_expected)
        validate_mcr6_trb1_value = MsgTypeNumeric("mcr6_trb1:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_trb1_value_expected)
        validate_mcr6_trb1_foreground_color = MsgTypeString("mcr6_trb1:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_trb1_foreground_color_expected)
        validate_mcr6_trb1_background_color = MsgTypeString("mcr6_trb1:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_trb1_background_color_expected)
        validate_mcr6_trb34_visibility = MsgTypeString("mcr6_trb34:TMMI_MCR_IS_VISIBLE", value=mcr6_trb34_visibility_expected)
        validate_mcr6_trb34_value = MsgTypeNumeric("mcr6_trb34:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_trb34_value_expected)
        validate_mcr6_trb34_foreground_color = MsgTypeString("mcr6_trb34:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_trb34_foreground_color_expected)
        validate_mcr6_trb34_background_color = MsgTypeString("mcr6_trb34:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_trb34_background_color_expected)
        validate_mcr6_q25_visibility = MsgTypeString("mcr6_q25:TMMI_MCR_IS_VISIBLE", value=mcr6_q25_visibility_expected)
        validate_mcr6_q25_value = MsgTypeNumeric("mcr6_q25:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_q25_value_expected)
        validate_mcr6_q25_foreground_color = MsgTypeString("mcr6_q25:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_q25_foreground_color_expected)
        validate_mcr6_q25_background_color = MsgTypeString("mcr6_q25:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_q25_background_color_expected)
        validate_mcr6_q26_visibility = MsgTypeString("mcr6_q26:TMMI_MCR_IS_VISIBLE", value=mcr6_q26_visibility_expected)
        validate_mcr6_q26_value = MsgTypeNumeric("mcr6_q26:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_q26_value_expected)
        validate_mcr6_q26_foreground_color = MsgTypeString("mcr6_q26:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_q26_foreground_color_expected)
        validate_mcr6_q26_background_color = MsgTypeString("mcr6_q26:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_q26_background_color_expected)
        validate_mcr6_q27_visibility = MsgTypeString("mcr6_q27:TMMI_MCR_IS_VISIBLE", value=mcr6_q27_visibility_expected)
        validate_mcr6_q27_value = MsgTypeNumeric("mcr6_q27:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_q27_value_expected)
        validate_mcr6_q27_foreground_color = MsgTypeString("mcr6_q27:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_q27_foreground_color_expected)
        validate_mcr6_q27_background_color = MsgTypeString("mcr6_q27:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_q27_background_color_expected)
        validate_mcr6_b56_visibility = MsgTypeString("mcr6_b56:TMMI_MCR_IS_VISIBLE", value=mcr6_b56_visibility_expected)
        validate_mcr6_b56_value = MsgTypeNumeric("mcr6_b56:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_b56_value_expected)
        validate_mcr6_b56_foreground_color = MsgTypeString("mcr6_b56:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_b56_foreground_color_expected)
        validate_mcr6_b56_background_color = MsgTypeString("mcr6_b56:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_b56_background_color_expected)
        validate_mcr6_t8_visibility = MsgTypeString("mcr6_t8:TMMI_MCR_IS_VISIBLE", value=mcr6_t8_visibility_expected)
        validate_mcr6_t8_value = MsgTypeNumeric("mcr6_t8:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_t8_value_expected)
        validate_mcr6_t8_foreground_color = MsgTypeString("mcr6_t8:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_t8_foreground_color_expected)
        validate_mcr6_t8_background_color = MsgTypeString("mcr6_t8:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_t8_background_color_expected)
        validate_mcr6_trb5_visibility = MsgTypeString("mcr6_trb5:TMMI_MCR_IS_VISIBLE", value=mcr6_trb5_visibility_expected)
        validate_mcr6_trb5_value = MsgTypeNumeric("mcr6_trb5:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_trb5_value_expected)
        validate_mcr6_trb5_foreground_color = MsgTypeString("mcr6_trb5:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_trb5_foreground_color_expected)
        validate_mcr6_trb5_background_color = MsgTypeString("mcr6_trb5:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_trb5_background_color_expected)
        validate_mcr6_trb6_visibility = MsgTypeString("mcr6_trb6:TMMI_MCR_IS_VISIBLE", value=mcr6_trb6_visibility_expected)
        validate_mcr6_trb6_value = MsgTypeNumeric("mcr6_trb6:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_trb6_value_expected)
        validate_mcr6_trb6_foreground_color = MsgTypeString("mcr6_trb6:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_trb6_foreground_color_expected)
        validate_mcr6_trb6_background_color = MsgTypeString("mcr6_trb6:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_trb6_background_color_expected)
        validate_mcr6_q0m1_visibility = MsgTypeString("mcr6_q0m1:TMMI_MCR_IS_VISIBLE", value=mcr6_q0m1_visibility_expected)
        validate_mcr6_q0m1_value = MsgTypeNumeric("mcr6_q0m1:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_q0m1_value_expected)
        validate_mcr6_q0m1_foreground_color = MsgTypeString("mcr6_q0m1:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_q0m1_foreground_color_expected)
        validate_mcr6_q0m1_background_color = MsgTypeString("mcr6_q0m1:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_q0m1_background_color_expected)
        validate_mcr6_q1m1_visibility = MsgTypeString("mcr6_q1m1:TMMI_MCR_IS_VISIBLE", value=mcr6_q1m1_visibility_expected)
        validate_mcr6_q1m1_value = MsgTypeNumeric("mcr6_q1m1:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_q1m1_value_expected)
        validate_mcr6_q1m1_foreground_color = MsgTypeString("mcr6_q1m1:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_q1m1_foreground_color_expected)
        validate_mcr6_q1m1_background_color = MsgTypeString("mcr6_q1m1:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_q1m1_background_color_expected)
        validate_mcr6_q2m1_visibility = MsgTypeString("mcr6_q2m1:TMMI_MCR_IS_VISIBLE", value=mcr6_q2m1_visibility_expected)
        validate_mcr6_q2m1_value = MsgTypeNumeric("mcr6_q2m1:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_q2m1_value_expected)
        validate_mcr6_q2m1_foreground_color = MsgTypeString("mcr6_q2m1:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_q2m1_foreground_color_expected)
        validate_mcr6_q2m1_background_color = MsgTypeString("mcr6_q2m1:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_q2m1_background_color_expected)
        validate_mcr6_q3m1_visibility = MsgTypeString("mcr6_q3m1:TMMI_MCR_IS_VISIBLE", value=mcr6_q3m1_visibility_expected)
        validate_mcr6_q3m1_value = MsgTypeNumeric("mcr6_q3m1:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_q3m1_value_expected)
        validate_mcr6_q3m1_foreground_color = MsgTypeString("mcr6_q3m1:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_q3m1_foreground_color_expected)
        validate_mcr6_q3m1_background_color = MsgTypeString("mcr6_q3m1:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_q3m1_background_color_expected)
        validate_mcr6_q1g1_visibility = MsgTypeString("mcr6_q1g1:TMMI_MCR_IS_VISIBLE", value=mcr6_q1g1_visibility_expected)
        validate_mcr6_q1g1_value = MsgTypeNumeric("mcr6_q1g1:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_q1g1_value_expected)
        validate_mcr6_q1g1_foreground_color = MsgTypeString("mcr6_q1g1:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_q1g1_foreground_color_expected)
        validate_mcr6_q1g1_background_color = MsgTypeString("mcr6_q1g1:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_q1g1_background_color_expected)
        validate_mcr6_q2g1_visibility = MsgTypeString("mcr6_q2g1:TMMI_MCR_IS_VISIBLE", value=mcr6_q2g1_visibility_expected)
        validate_mcr6_q2g1_value = MsgTypeNumeric("mcr6_q2g1:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_q2g1_value_expected)
        validate_mcr6_q2g1_foreground_color = MsgTypeString("mcr6_q2g1:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_q2g1_foreground_color_expected)
        validate_mcr6_q2g1_background_color = MsgTypeString("mcr6_q2g1:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_q2g1_background_color_expected)
        validate_mcr6_q3g1_visibility = MsgTypeString("mcr6_q3g1:TMMI_MCR_IS_VISIBLE", value=mcr6_q3g1_visibility_expected)
        validate_mcr6_q3g1_value = MsgTypeNumeric("mcr6_q3g1:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_q3g1_value_expected)
        validate_mcr6_q3g1_foreground_color = MsgTypeString("mcr6_q3g1:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_q3g1_foreground_color_expected)
        validate_mcr6_q3g1_background_color = MsgTypeString("mcr6_q3g1:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_q3g1_background_color_expected)
        validate_mcr6_q4g1_visibility = MsgTypeString("mcr6_q4g1:TMMI_MCR_IS_VISIBLE", value=mcr6_q4g1_visibility_expected)
        validate_mcr6_q4g1_value = MsgTypeNumeric("mcr6_q4g1:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_q4g1_value_expected)
        validate_mcr6_q4g1_foreground_color = MsgTypeString("mcr6_q4g1:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_q4g1_foreground_color_expected)
        validate_mcr6_q4g1_background_color = MsgTypeString("mcr6_q4g1:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_q4g1_background_color_expected)
        validate_mcr6_q5g1_visibility = MsgTypeString("mcr6_q5g1:TMMI_MCR_IS_VISIBLE", value=mcr6_q5g1_visibility_expected)
        validate_mcr6_q5g1_value = MsgTypeNumeric("mcr6_q5g1:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_q5g1_value_expected)
        validate_mcr6_q5g1_foreground_color = MsgTypeString("mcr6_q5g1:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_q5g1_foreground_color_expected)
        validate_mcr6_q5g1_background_color = MsgTypeString("mcr6_q5g1:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_q5g1_background_color_expected)
        validate_mcr6_b1g1_visibility = MsgTypeString("mcr6_b1g1:TMMI_MCR_IS_VISIBLE", value=mcr6_b1g1_visibility_expected)
        validate_mcr6_b1g1_value = MsgTypeNumeric("mcr6_b1g1:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_b1g1_value_expected)
        validate_mcr6_b1g1_foreground_color = MsgTypeString("mcr6_b1g1:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_b1g1_foreground_color_expected)
        validate_mcr6_b1g1_background_color = MsgTypeString("mcr6_b1g1:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_b1g1_background_color_expected)
        validate_mcr6_b2g1_visibility = MsgTypeString("mcr6_b2g1:TMMI_MCR_IS_VISIBLE", value=mcr6_b2g1_visibility_expected)
        validate_mcr6_b2g1_value = MsgTypeNumeric("mcr6_b2g1:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_b2g1_value_expected)
        validate_mcr6_b2g1_foreground_color = MsgTypeString("mcr6_b2g1:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_b2g1_foreground_color_expected)
        validate_mcr6_b2g1_background_color = MsgTypeString("mcr6_b2g1:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_b2g1_background_color_expected)
        validate_mcr6_t9g1_visibility = MsgTypeString("mcr6_t9g1:TMMI_MCR_IS_VISIBLE", value=mcr6_t9g1_visibility_expected)
        validate_mcr6_t9g1_value = MsgTypeNumeric("mcr6_t9g1:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_t9g1_value_expected)
        validate_mcr6_t9g1_foreground_color = MsgTypeString("mcr6_t9g1:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_t9g1_foreground_color_expected)
        validate_mcr6_t9g1_background_color = MsgTypeString("mcr6_t9g1:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_t9g1_background_color_expected)
        validate_mcr6_t10g1_visibility = MsgTypeString("mcr6_t10g1:TMMI_MCR_IS_VISIBLE", value=mcr6_t10g1_visibility_expected)
        validate_mcr6_t10g1_value = MsgTypeNumeric("mcr6_t10g1:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_t10g1_value_expected)
        validate_mcr6_t10g1_foreground_color = MsgTypeString("mcr6_t10g1:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_t10g1_foreground_color_expected)
        validate_mcr6_t10g1_background_color = MsgTypeString("mcr6_t10g1:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_t10g1_background_color_expected)
        validate_Label1_visibility = MsgTypeString("Label1:TMMI_MCR_IS_VISIBLE", value=Label1_visibility_expected)
        validate_Label1_foreground_color = MsgTypeString("Label1:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=Label1_foreground_color_expected)
        validate_Label1_background_color = MsgTypeString("Label1:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=Label1_background_color_expected)
        validate_mcr6_energytxt_visibility = MsgTypeString("mcr6_energytxt:TMMI_MCR_IS_VISIBLE", value=mcr6_energytxt_visibility_expected)
        validate_mcr6_energytxt_value = MsgTypeNumeric("mcr6_energytxt:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_energytxt_value_expected)
        validate_mcr6_energytxt_foreground_color = MsgTypeString("mcr6_energytxt:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_energytxt_foreground_color_expected)
        validate_mcr6_energytxt_background_color = MsgTypeString("mcr6_energytxt:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_energytxt_background_color_expected)
        validate_Label2_visibility = MsgTypeString("Label2:TMMI_MCR_IS_VISIBLE", value=Label2_visibility_expected)
        validate_Label2_foreground_color = MsgTypeString("Label2:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=Label2_foreground_color_expected)
        validate_Label2_background_color = MsgTypeString("Label2:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=Label2_background_color_expected)
        validate_energy_shape_visibility = MsgTypeString("energy_shape:TMMI_MCR_IS_VISIBLE", value=energy_shape_visibility_expected)
        validate_energy_shape_foreground_color = MsgTypeString("energy_shape:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=energy_shape_foreground_color_expected)
        validate_energy_shape_background_color = MsgTypeString("energy_shape:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=energy_shape_background_color_expected)
        validate_mcr6_gantry1positiontxt_visibility = MsgTypeString("mcr6_gantry1positiontxt:TMMI_MCR_IS_VISIBLE", value=mcr6_gantry1positiontxt_visibility_expected)
        validate_mcr6_gantry1positiontxt_value = MsgTypeNumeric("mcr6_gantry1positiontxt:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_gantry1positiontxt_value_expected)
        validate_mcr6_gantry1positiontxt_foreground_color = MsgTypeString("mcr6_gantry1positiontxt:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_gantry1positiontxt_foreground_color_expected)
        validate_mcr6_gantry1positiontxt_background_color = MsgTypeString("mcr6_gantry1positiontxt:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_gantry1positiontxt_background_color_expected)
        validate_gantry_shape_visibility = MsgTypeString("gantry_shape:TMMI_MCR_IS_VISIBLE", value=gantry_shape_visibility_expected)
        validate_gantry_shape_foreground_color = MsgTypeString("gantry_shape:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=gantry_shape_foreground_color_expected)
        validate_gantry_shape_background_color = MsgTypeString("gantry_shape:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=gantry_shape_background_color_expected)
        validate_range_edit_shape_visibility = MsgTypeString("range_edit_shape:TMMI_MCR_IS_VISIBLE", value=range_edit_shape_visibility_expected)
        validate_range_edit_shape_foreground_color = MsgTypeString("range_edit_shape:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=range_edit_shape_foreground_color_expected)
        validate_range_edit_shape_background_color = MsgTypeString("range_edit_shape:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=range_edit_shape_background_color_expected)
        validate_mcr6_global_range_status_visibility = MsgTypeString("mcr6_global_range_status:TMMI_MCR_IS_VISIBLE", value=mcr6_global_range_status_visibility_expected)
        validate_mcr6_global_range_status_value = MsgTypeNumeric("mcr6_global_range_status:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_global_range_status_value_expected)
        validate_mcr6_global_range_status_foreground_color = MsgTypeString("mcr6_global_range_status:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_global_range_status_foreground_color_expected)
        validate_mcr6_global_range_status_background_color = MsgTypeString("mcr6_global_range_status:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_global_range_status_background_color_expected)
        validate_mcr6_fieldtxt_visibility = MsgTypeString("mcr6_fieldtxt:TMMI_MCR_IS_VISIBLE", value=mcr6_fieldtxt_visibility_expected)
        validate_mcr6_fieldtxt_value = MsgTypeNumeric("mcr6_fieldtxt:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_fieldtxt_value_expected)
        validate_mcr6_fieldtxt_foreground_color = MsgTypeString("mcr6_fieldtxt:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_fieldtxt_foreground_color_expected)
        validate_mcr6_fieldtxt_background_color = MsgTypeString("mcr6_fieldtxt:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_fieldtxt_background_color_expected)
        validate_field_shape_visibility = MsgTypeString("field_shape:TMMI_MCR_IS_VISIBLE", value=field_shape_visibility_expected)
        validate_field_shape_foreground_color = MsgTypeString("field_shape:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=field_shape_foreground_color_expected)
        validate_field_shape_background_color = MsgTypeString("field_shape:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=field_shape_background_color_expected)
        validate_mcr6_sl1x_visibility = MsgTypeString("mcr6_sl1x:TMMI_MCR_IS_VISIBLE", value=mcr6_sl1x_visibility_expected)
        validate_mcr6_sl1x_value = MsgTypeNumeric("mcr6_sl1x:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_sl1x_value_expected)
        validate_mcr6_sl1x_foreground_color = MsgTypeString("mcr6_sl1x:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_sl1x_foreground_color_expected)
        validate_mcr6_sl1x_background_color = MsgTypeString("mcr6_sl1x:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_sl1x_background_color_expected)
        validate_mcr6_sl1y_visibility = MsgTypeString("mcr6_sl1y:TMMI_MCR_IS_VISIBLE", value=mcr6_sl1y_visibility_expected)
        validate_mcr6_sl1y_value = MsgTypeNumeric("mcr6_sl1y:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_sl1y_value_expected)
        validate_mcr6_sl1y_foreground_color = MsgTypeString("mcr6_sl1y:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_sl1y_foreground_color_expected)
        validate_mcr6_sl1y_background_color = MsgTypeString("mcr6_sl1y:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_sl1y_background_color_expected)
        validate_mcr6_sl2x_visibility = MsgTypeString("mcr6_sl2x:TMMI_MCR_IS_VISIBLE", value=mcr6_sl2x_visibility_expected)
        validate_mcr6_sl2x_value = MsgTypeNumeric("mcr6_sl2x:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_sl2x_value_expected)
        validate_mcr6_sl2x_foreground_color = MsgTypeString("mcr6_sl2x:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_sl2x_foreground_color_expected)
        validate_mcr6_sl2x_background_color = MsgTypeString("mcr6_sl2x:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_sl2x_background_color_expected)
        validate_mcr6_graphitestepreached_visibility = MsgTypeString("mcr6_graphitestepreached:TMMI_MCR_IS_VISIBLE", value=mcr6_graphitestepreached_visibility_expected)
        validate_mcr6_graphitestepreached_value = MsgTypeNumeric("mcr6_graphitestepreached:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_graphitestepreached_value_expected)
        validate_mcr6_graphitestepreached_foreground_color = MsgTypeString("mcr6_graphitestepreached:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_graphitestepreached_foreground_color_expected)
        validate_mcr6_graphitestepreached_background_color = MsgTypeString("mcr6_graphitestepreached:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_graphitestepreached_background_color_expected)
        validate_mcr6_graphitestepreached_value_visibility = MsgTypeString("mcr6_graphitestepreached_value:TMMI_MCR_IS_VISIBLE", value=mcr6_graphitestepreached_value_visibility_expected)
        validate_mcr6_graphitestepreached_value_value = MsgTypeNumeric("mcr6_graphitestepreached_value:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_graphitestepreached_value_value_expected)
        validate_mcr6_graphitestepreached_value_foreground_color = MsgTypeString("mcr6_graphitestepreached_value:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_graphitestepreached_value_foreground_color_expected)
        validate_mcr6_graphitestepreached_value_background_color = MsgTypeString("mcr6_graphitestepreached_value:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_graphitestepreached_value_background_color_expected)
        validate_mcr6_setrangebtn_visibility = MsgTypeString("mcr6_setrangebtn:TMMI_MCR_IS_VISIBLE", value=mcr6_setrangebtn_visibility_expected)
        validate_mcr6_setrangebtn_foreground_color = MsgTypeString("mcr6_setrangebtn:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_setrangebtn_foreground_color_expected)
        validate_mcr6_setrangebtn_background_color = MsgTypeString("mcr6_setrangebtn:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_setrangebtn_background_color_expected)
        validate_mcr6_degrader_status_visibility = MsgTypeString("mcr6_degrader_status:TMMI_MCR_IS_VISIBLE", value=mcr6_degrader_status_visibility_expected)
        validate_mcr6_degrader_status_value = MsgTypeNumeric("mcr6_degrader_status:TMMI_MCR_OBJECT_GET_VALUE", value=mcr6_degrader_status_value_expected)
        validate_mcr6_degrader_status_foreground_color = MsgTypeString("mcr6_degrader_status:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_degrader_status_foreground_color_expected)
        validate_mcr6_degrader_status_background_color = MsgTypeString("mcr6_degrader_status:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_degrader_status_background_color_expected)
        validate_mcr6_iseu1btn_visibility = MsgTypeString("mcr6_iseu1btn:TMMI_MCR_IS_VISIBLE", value=mcr6_iseu1btn_visibility_expected)
        validate_mcr6_iseu1btn_foreground_color = MsgTypeString("mcr6_iseu1btn:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr6_iseu1btn_foreground_color_expected)
        validate_mcr6_iseu1btn_background_color = MsgTypeString("mcr6_iseu1btn:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr6_iseu1btn_background_color_expected)


        info_exchange = [
                        InformationSet("get mcr6_cugantryposfbk visibility", "thriver", "mcrhci", get_mcr6_cugantryposfbk_visibility),
                        InformationSet("validate mcr6_cugantryposfbk visibility is equal to {mcr6_cugantryposfbk_visibility_expected}".format(mcr6_cugantryposfbk_visibility_expected=mcr6_cugantryposfbk_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_cugantryposfbk_visibility),
                        InformationSet("get mcr6_cugantryposfbk value", "thriver", "mcrhci", get_mcr6_cugantryposfbk_value),
                        InformationSet("validate mcr6_cugantryposfbk value is equal to {mcr6_cugantryposfbk_value_expected}".format(mcr6_cugantryposfbk_value_expected=mcr6_cugantryposfbk_value_expected), "mcrhci", "hcitracer", validate_mcr6_cugantryposfbk_value),
                        InformationSet("get mcr6_cugantryposfbk foreground_color", "thriver", "mcrhci", get_mcr6_cugantryposfbk_foreground_color),
                        InformationSet("validate mcr6_cugantryposfbk foreground_color is equal to {mcr6_cugantryposfbk_foreground_color_expected}".format(mcr6_cugantryposfbk_foreground_color_expected=mcr6_cugantryposfbk_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_cugantryposfbk_foreground_color),
                        InformationSet("get mcr6_cugantryposfbk background_color", "thriver", "mcrhci", get_mcr6_cugantryposfbk_background_color),
                        InformationSet("validate mcr6_cugantryposfbk background_color is equal to {mcr6_cugantryposfbk_background_color_expected}".format(mcr6_cugantryposfbk_background_color_expected=mcr6_cugantryposfbk_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_cugantryposfbk_background_color),
                        InformationSet("get mcr6_range_feedbacktxt visibility", "thriver", "mcrhci", get_mcr6_range_feedbacktxt_visibility),
                        InformationSet("validate mcr6_range_feedbacktxt visibility is equal to {mcr6_range_feedbacktxt_visibility_expected}".format(mcr6_range_feedbacktxt_visibility_expected=mcr6_range_feedbacktxt_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_range_feedbacktxt_visibility),
                        InformationSet("get mcr6_range_feedbacktxt value", "thriver", "mcrhci", get_mcr6_range_feedbacktxt_value),
                        InformationSet("validate mcr6_range_feedbacktxt value is equal to {mcr6_range_feedbacktxt_value_expected}".format(mcr6_range_feedbacktxt_value_expected=mcr6_range_feedbacktxt_value_expected), "mcrhci", "hcitracer", validate_mcr6_range_feedbacktxt_value),
                        InformationSet("get mcr6_range_feedbacktxt foreground_color", "thriver", "mcrhci", get_mcr6_range_feedbacktxt_foreground_color),
                        InformationSet("validate mcr6_range_feedbacktxt foreground_color is equal to {mcr6_range_feedbacktxt_foreground_color_expected}".format(mcr6_range_feedbacktxt_foreground_color_expected=mcr6_range_feedbacktxt_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_range_feedbacktxt_foreground_color),
                        InformationSet("get mcr6_range_feedbacktxt background_color", "thriver", "mcrhci", get_mcr6_range_feedbacktxt_background_color),
                        InformationSet("validate mcr6_range_feedbacktxt background_color is equal to {mcr6_range_feedbacktxt_background_color_expected}".format(mcr6_range_feedbacktxt_background_color_expected=mcr6_range_feedbacktxt_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_range_feedbacktxt_background_color),
                        InformationSet("get mcr6_q9 visibility", "thriver", "mcrhci", get_mcr6_q9_visibility),
                        InformationSet("validate mcr6_q9 visibility is equal to {mcr6_q9_visibility_expected}".format(mcr6_q9_visibility_expected=mcr6_q9_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_q9_visibility),
                        InformationSet("get mcr6_q9 value", "thriver", "mcrhci", get_mcr6_q9_value),
                        InformationSet("validate mcr6_q9 value is equal to {mcr6_q9_value_expected}".format(mcr6_q9_value_expected=mcr6_q9_value_expected), "mcrhci", "hcitracer", validate_mcr6_q9_value),
                        InformationSet("get mcr6_q9 foreground_color", "thriver", "mcrhci", get_mcr6_q9_foreground_color),
                        InformationSet("validate mcr6_q9 foreground_color is equal to {mcr6_q9_foreground_color_expected}".format(mcr6_q9_foreground_color_expected=mcr6_q9_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_q9_foreground_color),
                        InformationSet("get mcr6_q9 background_color", "thriver", "mcrhci", get_mcr6_q9_background_color),
                        InformationSet("validate mcr6_q9 background_color is equal to {mcr6_q9_background_color_expected}".format(mcr6_q9_background_color_expected=mcr6_q9_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_q9_background_color),
                        InformationSet("get mcr6_q10 visibility", "thriver", "mcrhci", get_mcr6_q10_visibility),
                        InformationSet("validate mcr6_q10 visibility is equal to {mcr6_q10_visibility_expected}".format(mcr6_q10_visibility_expected=mcr6_q10_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_q10_visibility),
                        InformationSet("get mcr6_q10 value", "thriver", "mcrhci", get_mcr6_q10_value),
                        InformationSet("validate mcr6_q10 value is equal to {mcr6_q10_value_expected}".format(mcr6_q10_value_expected=mcr6_q10_value_expected), "mcrhci", "hcitracer", validate_mcr6_q10_value),
                        InformationSet("get mcr6_q10 foreground_color", "thriver", "mcrhci", get_mcr6_q10_foreground_color),
                        InformationSet("validate mcr6_q10 foreground_color is equal to {mcr6_q10_foreground_color_expected}".format(mcr6_q10_foreground_color_expected=mcr6_q10_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_q10_foreground_color),
                        InformationSet("get mcr6_q10 background_color", "thriver", "mcrhci", get_mcr6_q10_background_color),
                        InformationSet("validate mcr6_q10 background_color is equal to {mcr6_q10_background_color_expected}".format(mcr6_q10_background_color_expected=mcr6_q10_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_q10_background_color),                     
                        InformationSet("get mcr6_q11 visibility", "thriver", "mcrhci", get_mcr6_q11_visibility),
                        InformationSet("validate mcr6_q11 visibility is equal to {mcr6_q11_visibility_expected}".format(mcr6_q11_visibility_expected=mcr6_q11_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_q11_visibility),
                        InformationSet("get mcr6_q11 value", "thriver", "mcrhci", get_mcr6_q11_value),
                        InformationSet("validate mcr6_q11 value is equal to {mcr6_q11_value_expected}".format(mcr6_q11_value_expected=mcr6_q11_value_expected), "mcrhci", "hcitracer", validate_mcr6_q11_value),
                        InformationSet("get mcr6_q11 foreground_color", "thriver", "mcrhci", get_mcr6_q11_foreground_color),
                        InformationSet("validate mcr6_q11 foreground_color is equal to {mcr6_q11_foreground_color_expected}".format(mcr6_q11_foreground_color_expected=mcr6_q11_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_q11_foreground_color),
                        InformationSet("get mcr6_q11 background_color", "thriver", "mcrhci", get_mcr6_q11_background_color),
                        InformationSet("validate mcr6_q11 background_color is equal to {mcr6_q11_background_color_expected}".format(mcr6_q11_background_color_expected=mcr6_q11_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_q11_background_color),
                        InformationSet("get mcr6_q12 visibility", "thriver", "mcrhci", get_mcr6_q12_visibility),
                        InformationSet("validate mcr6_q12 visibility is equal to {mcr6_q12_visibility_expected}".format(mcr6_q12_visibility_expected=mcr6_q12_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_q12_visibility),
                        InformationSet("get mcr6_q12 value", "thriver", "mcrhci", get_mcr6_q12_value),
                        InformationSet("validate mcr6_q12 value is equal to {mcr6_q12_value_expected}".format(mcr6_q12_value_expected=mcr6_q12_value_expected), "mcrhci", "hcitracer", validate_mcr6_q12_value),
                        InformationSet("get mcr6_q12 foreground_color", "thriver", "mcrhci", get_mcr6_q12_foreground_color),
                        InformationSet("validate mcr6_q12 foreground_color is equal to {mcr6_q12_foreground_color_expected}".format(mcr6_q12_foreground_color_expected=mcr6_q12_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_q12_foreground_color),
                        InformationSet("get mcr6_q12 background_color", "thriver", "mcrhci", get_mcr6_q12_background_color),
                        InformationSet("validate mcr6_q12 background_color is equal to {mcr6_q12_background_color_expected}".format(mcr6_q12_background_color_expected=mcr6_q12_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_q12_background_color),                     
                        InformationSet("get mcr6_q13 visibility", "thriver", "mcrhci", get_mcr6_q13_visibility),
                        InformationSet("validate mcr6_q13 visibility is equal to {mcr6_q13_visibility_expected}".format(mcr6_q13_visibility_expected=mcr6_q13_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_q13_visibility),
                        InformationSet("get mcr6_q13 value", "thriver", "mcrhci", get_mcr6_q13_value),
                        InformationSet("validate mcr6_q13 value is equal to {mcr6_q13_value_expected}".format(mcr6_q13_value_expected=mcr6_q13_value_expected), "mcrhci", "hcitracer", validate_mcr6_q13_value),
                        InformationSet("get mcr6_q13 foreground_color", "thriver", "mcrhci", get_mcr6_q13_foreground_color),
                        InformationSet("validate mcr6_q13 foreground_color is equal to {mcr6_q13_foreground_color_expected}".format(mcr6_q13_foreground_color_expected=mcr6_q13_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_q13_foreground_color),
                        InformationSet("get mcr6_q13 background_color", "thriver", "mcrhci", get_mcr6_q13_background_color),
                        InformationSet("validate mcr6_q13 background_color is equal to {mcr6_q13_background_color_expected}".format(mcr6_q13_background_color_expected=mcr6_q13_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_q13_background_color),                     
                        InformationSet("get mcr6_q14 visibility", "thriver", "mcrhci", get_mcr6_q14_visibility),
                        InformationSet("validate mcr6_q14 visibility is equal to {mcr6_q14_visibility_expected}".format(mcr6_q14_visibility_expected=mcr6_q14_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_q14_visibility),
                        InformationSet("get mcr6_q14 value", "thriver", "mcrhci", get_mcr6_q14_value),
                        InformationSet("validate mcr6_q14 value is equal to {mcr6_q14_value_expected}".format(mcr6_q14_value_expected=mcr6_q14_value_expected), "mcrhci", "hcitracer", validate_mcr6_q14_value),
                        InformationSet("get mcr6_q14 foreground_color", "thriver", "mcrhci", get_mcr6_q14_foreground_color),
                        InformationSet("validate mcr6_q14 foreground_color is equal to {mcr6_q14_foreground_color_expected}".format(mcr6_q14_foreground_color_expected=mcr6_q14_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_q14_foreground_color),
                        InformationSet("get mcr6_q14 background_color", "thriver", "mcrhci", get_mcr6_q14_background_color),
                        InformationSet("validate mcr6_q14 background_color is equal to {mcr6_q14_background_color_expected}".format(mcr6_q14_background_color_expected=mcr6_q14_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_q14_background_color),
                        InformationSet("get mcr6_q15 visibility", "thriver", "mcrhci", get_mcr6_q15_visibility),
                        InformationSet("validate mcr6_q15 visibility is equal to {mcr6_q15_visibility_expected}".format(mcr6_q15_visibility_expected=mcr6_q15_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_q15_visibility),
                        InformationSet("get mcr6_q15 value", "thriver", "mcrhci", get_mcr6_q15_value),
                        InformationSet("validate mcr6_q15 value is equal to {mcr6_q15_value_expected}".format(mcr6_q15_value_expected=mcr6_q15_value_expected), "mcrhci", "hcitracer", validate_mcr6_q15_value),
                        InformationSet("get mcr6_q15 foreground_color", "thriver", "mcrhci", get_mcr6_q15_foreground_color),
                        InformationSet("validate mcr6_q15 foreground_color is equal to {mcr6_q15_foreground_color_expected}".format(mcr6_q15_foreground_color_expected=mcr6_q15_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_q15_foreground_color),
                        InformationSet("get mcr6_q15 background_color", "thriver", "mcrhci", get_mcr6_q15_background_color),
                        InformationSet("validate mcr6_q15 background_color is equal to {mcr6_q15_background_color_expected}".format(mcr6_q15_background_color_expected=mcr6_q15_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_q15_background_color),                     
                        InformationSet("get mcr6_q20 visibility", "thriver", "mcrhci", get_mcr6_q20_visibility),
                        InformationSet("validate mcr6_q20 visibility is equal to {mcr6_q20_visibility_expected}".format(mcr6_q20_visibility_expected=mcr6_q20_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_q20_visibility),
                        InformationSet("get mcr6_q20 value", "thriver", "mcrhci", get_mcr6_q20_value),
                        InformationSet("validate mcr6_q20 value is equal to {mcr6_q20_value_expected}".format(mcr6_q20_value_expected=mcr6_q20_value_expected), "mcrhci", "hcitracer", validate_mcr6_q20_value),
                        InformationSet("get mcr6_q20 foreground_color", "thriver", "mcrhci", get_mcr6_q20_foreground_color),
                        InformationSet("validate mcr6_q20 foreground_color is equal to {mcr6_q20_foreground_color_expected}".format(mcr6_q20_foreground_color_expected=mcr6_q20_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_q20_foreground_color),
                        InformationSet("get mcr6_q20 background_color", "thriver", "mcrhci", get_mcr6_q20_background_color),
                        InformationSet("validate mcr6_q20 background_color is equal to {mcr6_q20_background_color_expected}".format(mcr6_q20_background_color_expected=mcr6_q20_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_q20_background_color),                     
                        InformationSet("get mcr6_q21 visibility", "thriver", "mcrhci", get_mcr6_q21_visibility),
                        InformationSet("validate mcr6_q21 visibility is equal to {mcr6_q21_visibility_expected}".format(mcr6_q21_visibility_expected=mcr6_q21_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_q21_visibility),
                        InformationSet("get mcr6_q21 value", "thriver", "mcrhci", get_mcr6_q21_value),
                        InformationSet("validate mcr6_q21 value is equal to {mcr6_q21_value_expected}".format(mcr6_q21_value_expected=mcr6_q21_value_expected), "mcrhci", "hcitracer", validate_mcr6_q21_value),
                        InformationSet("get mcr6_q21 foreground_color", "thriver", "mcrhci", get_mcr6_q21_foreground_color),
                        InformationSet("validate mcr6_q21 foreground_color is equal to {mcr6_q21_foreground_color_expected}".format(mcr6_q21_foreground_color_expected=mcr6_q21_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_q21_foreground_color),
                        InformationSet("get mcr6_q21 background_color", "thriver", "mcrhci", get_mcr6_q21_background_color),
                        InformationSet("validate mcr6_q21 background_color is equal to {mcr6_q21_background_color_expected}".format(mcr6_q21_background_color_expected=mcr6_q21_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_q21_background_color),                     
                        InformationSet("get mcr6_q22 visibility", "thriver", "mcrhci", get_mcr6_q22_visibility),
                        InformationSet("validate mcr6_q22 visibility is equal to {mcr6_q22_visibility_expected}".format(mcr6_q22_visibility_expected=mcr6_q22_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_q22_visibility),
                        InformationSet("get mcr6_q22 value", "thriver", "mcrhci", get_mcr6_q22_value),
                        InformationSet("validate mcr6_q22 value is equal to {mcr6_q22_value_expected}".format(mcr6_q22_value_expected=mcr6_q22_value_expected), "mcrhci", "hcitracer", validate_mcr6_q22_value),
                        InformationSet("get mcr6_q22 foreground_color", "thriver", "mcrhci", get_mcr6_q22_foreground_color),
                        InformationSet("validate mcr6_q22 foreground_color is equal to {mcr6_q22_foreground_color_expected}".format(mcr6_q22_foreground_color_expected=mcr6_q22_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_q22_foreground_color),
                        InformationSet("get mcr6_q22 background_color", "thriver", "mcrhci", get_mcr6_q22_background_color),
                        InformationSet("validate mcr6_q22 background_color is equal to {mcr6_q22_background_color_expected}".format(mcr6_q22_background_color_expected=mcr6_q22_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_q22_background_color),                     
                        InformationSet("get mcr6_b1234 visibility", "thriver", "mcrhci", get_mcr6_b1234_visibility),
                        InformationSet("validate mcr6_b1234 visibility is equal to {mcr6_b1234_visibility_expected}".format(mcr6_b1234_visibility_expected=mcr6_b1234_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_b1234_visibility),
                        InformationSet("get mcr6_b1234 value", "thriver", "mcrhci", get_mcr6_b1234_value),
                        InformationSet("validate mcr6_b1234 value is equal to {mcr6_b1234_value_expected}".format(mcr6_b1234_value_expected=mcr6_b1234_value_expected), "mcrhci", "hcitracer", validate_mcr6_b1234_value),
                        InformationSet("get mcr6_b1234 foreground_color", "thriver", "mcrhci", get_mcr6_b1234_foreground_color),
                        InformationSet("validate mcr6_b1234 foreground_color is equal to {mcr6_b1234_foreground_color_expected}".format(mcr6_b1234_foreground_color_expected=mcr6_b1234_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_b1234_foreground_color),
                        InformationSet("get mcr6_b1234 background_color", "thriver", "mcrhci", get_mcr6_b1234_background_color),
                        InformationSet("validate mcr6_b1234 background_color is equal to {mcr6_b1234_background_color_expected}".format(mcr6_b1234_background_color_expected=mcr6_b1234_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_b1234_background_color),
                        InformationSet("get mcr6_t6 visibility", "thriver", "mcrhci", get_mcr6_t6_visibility),
                        InformationSet("validate mcr6_t6 visibility is equal to {mcr6_t6_visibility_expected}".format(mcr6_t6_visibility_expected=mcr6_t6_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_t6_visibility),
                        InformationSet("get mcr6_t6 value", "thriver", "mcrhci", get_mcr6_t6_value),
                        InformationSet("validate mcr6_t6 value is equal to {mcr6_t6_value_expected}".format(mcr6_t6_value_expected=mcr6_t6_value_expected), "mcrhci", "hcitracer", validate_mcr6_t6_value),
                        InformationSet("get mcr6_t6 foreground_color", "thriver", "mcrhci", get_mcr6_t6_foreground_color),
                        InformationSet("validate mcr6_t6 foreground_color is equal to {mcr6_t6_foreground_color_expected}".format(mcr6_t6_foreground_color_expected=mcr6_t6_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_t6_foreground_color),
                        InformationSet("get mcr6_t6 background_color", "thriver", "mcrhci", get_mcr6_t6_background_color),
                        InformationSet("validate mcr6_t6 background_color is equal to {mcr6_t6_background_color_expected}".format(mcr6_t6_background_color_expected=mcr6_t6_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_t6_background_color),
                        InformationSet("get mcr6_t7 visibility", "thriver", "mcrhci", get_mcr6_t7_visibility),
                        InformationSet("validate mcr6_t7 visibility is equal to {mcr6_t7_visibility_expected}".format(mcr6_t7_visibility_expected=mcr6_t7_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_t7_visibility),
                        InformationSet("get mcr6_t7 value", "thriver", "mcrhci", get_mcr6_t7_value),
                        InformationSet("validate mcr6_t7 value is equal to {mcr6_t7_value_expected}".format(mcr6_t7_value_expected=mcr6_t7_value_expected), "mcrhci", "hcitracer", validate_mcr6_t7_value),
                        InformationSet("get mcr6_t7 foreground_color", "thriver", "mcrhci", get_mcr6_t7_foreground_color),
                        InformationSet("validate mcr6_t7 foreground_color is equal to {mcr6_t7_foreground_color_expected}".format(mcr6_t7_foreground_color_expected=mcr6_t7_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_t7_foreground_color),
                        InformationSet("get mcr6_t7 background_color", "thriver", "mcrhci", get_mcr6_t7_background_color),
                        InformationSet("validate mcr6_t7 background_color is equal to {mcr6_t7_background_color_expected}".format(mcr6_t7_background_color_expected=mcr6_t7_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_t7_background_color),
                        InformationSet("get mcr6_trb1 visibility", "thriver", "mcrhci", get_mcr6_trb1_visibility),
                        InformationSet("validate mcr6_trb1 visibility is equal to {mcr6_trb1_visibility_expected}".format(mcr6_trb1_visibility_expected=mcr6_trb1_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_trb1_visibility),
                        InformationSet("get mcr6_trb1 value", "thriver", "mcrhci", get_mcr6_trb1_value),
                        InformationSet("validate mcr6_trb1 value is equal to {mcr6_trb1_value_expected}".format(mcr6_trb1_value_expected=mcr6_trb1_value_expected), "mcrhci", "hcitracer", validate_mcr6_trb1_value),
                        InformationSet("get mcr6_trb1 foreground_color", "thriver", "mcrhci", get_mcr6_trb1_foreground_color),
                        InformationSet("validate mcr6_trb1 foreground_color is equal to {mcr6_trb1_foreground_color_expected}".format(mcr6_trb1_foreground_color_expected=mcr6_trb1_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_trb1_foreground_color),
                        InformationSet("get mcr6_trb1 background_color", "thriver", "mcrhci", get_mcr6_trb1_background_color),
                        InformationSet("validate mcr6_trb1 background_color is equal to {mcr6_trb1_background_color_expected}".format(mcr6_trb1_background_color_expected=mcr6_trb1_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_trb1_background_color),                        
                        InformationSet("get mcr6_trb34 visibility", "thriver", "mcrhci", get_mcr6_trb34_visibility),
                        InformationSet("validate mcr6_trb34 visibility is equal to {mcr6_trb34_visibility_expected}".format(mcr6_trb34_visibility_expected=mcr6_trb34_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_trb34_visibility),
                        InformationSet("get mcr6_trb34 value", "thriver", "mcrhci", get_mcr6_trb34_value),
                        InformationSet("validate mcr6_trb34 value is equal to {mcr6_trb34_value_expected}".format(mcr6_trb34_value_expected=mcr6_trb34_value_expected), "mcrhci", "hcitracer", validate_mcr6_trb34_value),
                        InformationSet("get mcr6_trb34 foreground_color", "thriver", "mcrhci", get_mcr6_trb34_foreground_color),
                        InformationSet("validate mcr6_trb34 foreground_color is equal to {mcr6_trb34_foreground_color_expected}".format(mcr6_trb34_foreground_color_expected=mcr6_trb34_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_trb34_foreground_color),
                        InformationSet("get mcr6_trb34 background_color", "thriver", "mcrhci", get_mcr6_trb34_background_color),
                        InformationSet("validate mcr6_trb34 background_color is equal to {mcr6_trb34_background_color_expected}".format(mcr6_trb34_background_color_expected=mcr6_trb34_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_trb34_background_color),
                        InformationSet("get mcr6_q25 visibility", "thriver", "mcrhci", get_mcr6_q25_visibility),
                        InformationSet("validate mcr6_q25 visibility is equal to {mcr6_q25_visibility_expected}".format(mcr6_q25_visibility_expected=mcr6_q25_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_q25_visibility),
                        InformationSet("get mcr6_q25 value", "thriver", "mcrhci", get_mcr6_q25_value),
                        InformationSet("validate mcr6_q25 value is equal to {mcr6_q25_value_expected}".format(mcr6_q25_value_expected=mcr6_q25_value_expected), "mcrhci", "hcitracer", validate_mcr6_q25_value),
                        InformationSet("get mcr6_q25 foreground_color", "thriver", "mcrhci", get_mcr6_q25_foreground_color),
                        InformationSet("validate mcr6_q25 foreground_color is equal to {mcr6_q25_foreground_color_expected}".format(mcr6_q25_foreground_color_expected=mcr6_q25_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_q25_foreground_color),
                        InformationSet("get mcr6_q25 background_color", "thriver", "mcrhci", get_mcr6_q25_background_color),
                        InformationSet("validate mcr6_q25 background_color is equal to {mcr6_q25_background_color_expected}".format(mcr6_q25_background_color_expected=mcr6_q25_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_q25_background_color),
                        InformationSet("get mcr6_q26 visibility", "thriver", "mcrhci", get_mcr6_q26_visibility),
                        InformationSet("validate mcr6_q26 visibility is equal to {mcr6_q26_visibility_expected}".format(mcr6_q26_visibility_expected=mcr6_q26_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_q26_visibility),
                        InformationSet("get mcr6_q26 value", "thriver", "mcrhci", get_mcr6_q26_value),
                        InformationSet("validate mcr6_q26 value is equal to {mcr6_q26_value_expected}".format(mcr6_q26_value_expected=mcr6_q26_value_expected), "mcrhci", "hcitracer", validate_mcr6_q26_value),
                        InformationSet("get mcr6_q26 foreground_color", "thriver", "mcrhci", get_mcr6_q26_foreground_color),
                        InformationSet("validate mcr6_q26 foreground_color is equal to {mcr6_q26_foreground_color_expected}".format(mcr6_q26_foreground_color_expected=mcr6_q26_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_q26_foreground_color),
                        InformationSet("get mcr6_q26 background_color", "thriver", "mcrhci", get_mcr6_q26_background_color),
                        InformationSet("validate mcr6_q26 background_color is equal to {mcr6_q26_background_color_expected}".format(mcr6_q26_background_color_expected=mcr6_q26_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_q26_background_color),
                        InformationSet("get mcr6_q27 visibility", "thriver", "mcrhci", get_mcr6_q27_visibility),
                        InformationSet("validate mcr6_q27 visibility is equal to {mcr6_q27_visibility_expected}".format(mcr6_q27_visibility_expected=mcr6_q27_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_q27_visibility),
                        InformationSet("get mcr6_q27 value", "thriver", "mcrhci", get_mcr6_q27_value),
                        InformationSet("validate mcr6_q27 value is equal to {mcr6_q27_value_expected}".format(mcr6_q27_value_expected=mcr6_q27_value_expected), "mcrhci", "hcitracer", validate_mcr6_q27_value),
                        InformationSet("get mcr6_q27 foreground_color", "thriver", "mcrhci", get_mcr6_q27_foreground_color),
                        InformationSet("validate mcr6_q27 foreground_color is equal to {mcr6_q27_foreground_color_expected}".format(mcr6_q27_foreground_color_expected=mcr6_q27_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_q27_foreground_color),
                        InformationSet("get mcr6_q27 background_color", "thriver", "mcrhci", get_mcr6_q27_background_color),
                        InformationSet("validate mcr6_q27 background_color is equal to {mcr6_q27_background_color_expected}".format(mcr6_q27_background_color_expected=mcr6_q27_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_q27_background_color),
                        InformationSet("get mcr6_b56 visibility", "thriver", "mcrhci", get_mcr6_b56_visibility),
                        InformationSet("validate mcr6_b56 visibility is equal to {mcr6_b56_visibility_expected}".format(mcr6_b56_visibility_expected=mcr6_b56_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_b56_visibility),
                        InformationSet("get mcr6_b56 value", "thriver", "mcrhci", get_mcr6_b56_value),
                        InformationSet("validate mcr6_b56 value is equal to {mcr6_b56_value_expected}".format(mcr6_b56_value_expected=mcr6_b56_value_expected), "mcrhci", "hcitracer", validate_mcr6_b56_value),
                        InformationSet("get mcr6_b56 foreground_color", "thriver", "mcrhci", get_mcr6_b56_foreground_color),
                        InformationSet("validate mcr6_b56 foreground_color is equal to {mcr6_b56_foreground_color_expected}".format(mcr6_b56_foreground_color_expected=mcr6_b56_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_b56_foreground_color),
                        InformationSet("get mcr6_b56 background_color", "thriver", "mcrhci", get_mcr6_b56_background_color),
                        InformationSet("validate mcr6_b56 background_color is equal to {mcr6_b56_background_color_expected}".format(mcr6_b56_background_color_expected=mcr6_b56_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_b56_background_color),
                        InformationSet("get mcr6_t8 visibility", "thriver", "mcrhci", get_mcr6_t8_visibility),
                        InformationSet("validate mcr6_t8 visibility is equal to {mcr6_t8_visibility_expected}".format(mcr6_t8_visibility_expected=mcr6_t8_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_t8_visibility),
                        InformationSet("get mcr6_t8 value", "thriver", "mcrhci", get_mcr6_t8_value),
                        InformationSet("validate mcr6_t8 value is equal to {mcr6_t8_value_expected}".format(mcr6_t8_value_expected=mcr6_t8_value_expected), "mcrhci", "hcitracer", validate_mcr6_t8_value),
                        InformationSet("get mcr6_t8 foreground_color", "thriver", "mcrhci", get_mcr6_t8_foreground_color),
                        InformationSet("validate mcr6_t8 foreground_color is equal to {mcr6_t8_foreground_color_expected}".format(mcr6_t8_foreground_color_expected=mcr6_t8_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_t8_foreground_color),
                        InformationSet("get mcr6_t8 background_color", "thriver", "mcrhci", get_mcr6_t8_background_color),
                        InformationSet("validate mcr6_t8 background_color is equal to {mcr6_t8_background_color_expected}".format(mcr6_t8_background_color_expected=mcr6_t8_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_t8_background_color),
                        InformationSet("get mcr6_trb5 visibility", "thriver", "mcrhci", get_mcr6_trb5_visibility),
                        InformationSet("validate mcr6_trb5 visibility is equal to {mcr6_trb5_visibility_expected}".format(mcr6_trb5_visibility_expected=mcr6_trb5_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_trb5_visibility),
                        InformationSet("get mcr6_trb5 value", "thriver", "mcrhci", get_mcr6_trb5_value),
                        InformationSet("validate mcr6_trb5 value is equal to {mcr6_trb5_value_expected}".format(mcr6_trb5_value_expected=mcr6_trb5_value_expected), "mcrhci", "hcitracer", validate_mcr6_trb5_value),
                        InformationSet("get mcr6_trb5 foreground_color", "thriver", "mcrhci", get_mcr6_trb5_foreground_color),
                        InformationSet("validate mcr6_trb5 foreground_color is equal to {mcr6_trb5_foreground_color_expected}".format(mcr6_trb5_foreground_color_expected=mcr6_trb5_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_trb5_foreground_color),
                        InformationSet("get mcr6_trb5 background_color", "thriver", "mcrhci", get_mcr6_trb5_background_color),
                        InformationSet("validate mcr6_trb5 background_color is equal to {mcr6_trb5_background_color_expected}".format(mcr6_trb5_background_color_expected=mcr6_trb5_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_trb5_background_color),
                        InformationSet("get mcr6_trb6 visibility", "thriver", "mcrhci", get_mcr6_trb6_visibility),
                        InformationSet("validate mcr6_trb6 visibility is equal to {mcr6_trb6_visibility_expected}".format(mcr6_trb6_visibility_expected=mcr6_trb6_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_trb6_visibility),
                        InformationSet("get mcr6_trb6 value", "thriver", "mcrhci", get_mcr6_trb6_value),
                        InformationSet("validate mcr6_trb6 value is equal to {mcr6_trb6_value_expected}".format(mcr6_trb6_value_expected=mcr6_trb6_value_expected), "mcrhci", "hcitracer", validate_mcr6_trb6_value),
                        InformationSet("get mcr6_trb6 foreground_color", "thriver", "mcrhci", get_mcr6_trb6_foreground_color),
                        InformationSet("validate mcr6_trb6 foreground_color is equal to {mcr6_trb6_foreground_color_expected}".format(mcr6_trb6_foreground_color_expected=mcr6_trb6_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_trb6_foreground_color),
                        InformationSet("get mcr6_trb6 background_color", "thriver", "mcrhci", get_mcr6_trb6_background_color),
                        InformationSet("validate mcr6_trb6 background_color is equal to {mcr6_trb6_background_color_expected}".format(mcr6_trb6_background_color_expected=mcr6_trb6_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_trb6_background_color),
                        InformationSet("get mcr6_q0m1 visibility", "thriver", "mcrhci", get_mcr6_q0m1_visibility),
                        InformationSet("validate mcr6_q0m1 visibility is equal to {mcr6_q0m1_visibility_expected}".format(mcr6_q0m1_visibility_expected=mcr6_q0m1_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_q0m1_visibility),
                        InformationSet("get mcr6_q0m1 value", "thriver", "mcrhci", get_mcr6_q0m1_value),
                        InformationSet("validate mcr6_q0m1 value is equal to {mcr6_q0m1_value_expected}".format(mcr6_q0m1_value_expected=mcr6_q0m1_value_expected), "mcrhci", "hcitracer", validate_mcr6_q0m1_value),
                        InformationSet("get mcr6_q0m1 foreground_color", "thriver", "mcrhci", get_mcr6_q0m1_foreground_color),
                        InformationSet("validate mcr6_q0m1 foreground_color is equal to {mcr6_q0m1_foreground_color_expected}".format(mcr6_q0m1_foreground_color_expected=mcr6_q0m1_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_q0m1_foreground_color),
                        InformationSet("get mcr6_q0m1 background_color", "thriver", "mcrhci", get_mcr6_q0m1_background_color),
                        InformationSet("validate mcr6_q0m1 background_color is equal to {mcr6_q0m1_background_color_expected}".format(mcr6_q0m1_background_color_expected=mcr6_q0m1_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_q0m1_background_color),
                        InformationSet("get mcr6_q1m1 visibility", "thriver", "mcrhci", get_mcr6_q1m1_visibility),
                        InformationSet("validate mcr6_q1m1 visibility is equal to {mcr6_q1m1_visibility_expected}".format(mcr6_q1m1_visibility_expected=mcr6_q1m1_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_q1m1_visibility),
                        InformationSet("get mcr6_q1m1 value", "thriver", "mcrhci", get_mcr6_q1m1_value),
                        InformationSet("validate mcr6_q1m1 value is equal to {mcr6_q1m1_value_expected}".format(mcr6_q1m1_value_expected=mcr6_q1m1_value_expected), "mcrhci", "hcitracer", validate_mcr6_q1m1_value),
                        InformationSet("get mcr6_q1m1 foreground_color", "thriver", "mcrhci", get_mcr6_q1m1_foreground_color),
                        InformationSet("validate mcr6_q1m1 foreground_color is equal to {mcr6_q1m1_foreground_color_expected}".format(mcr6_q1m1_foreground_color_expected=mcr6_q1m1_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_q1m1_foreground_color),
                        InformationSet("get mcr6_q1m1 background_color", "thriver", "mcrhci", get_mcr6_q1m1_background_color),
                        InformationSet("validate mcr6_q1m1 background_color is equal to {mcr6_q1m1_background_color_expected}".format(mcr6_q1m1_background_color_expected=mcr6_q1m1_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_q1m1_background_color),
                        InformationSet("get mcr6_q2m1 visibility", "thriver", "mcrhci", get_mcr6_q2m1_visibility),
                        InformationSet("validate mcr6_q2m1 visibility is equal to {mcr6_q2m1_visibility_expected}".format(mcr6_q2m1_visibility_expected=mcr6_q2m1_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_q2m1_visibility),
                        InformationSet("get mcr6_q2m1 value", "thriver", "mcrhci", get_mcr6_q2m1_value),
                        InformationSet("validate mcr6_q2m1 value is equal to {mcr6_q2m1_value_expected}".format(mcr6_q2m1_value_expected=mcr6_q2m1_value_expected), "mcrhci", "hcitracer", validate_mcr6_q2m1_value),
                        InformationSet("get mcr6_q2m1 foreground_color", "thriver", "mcrhci", get_mcr6_q2m1_foreground_color),
                        InformationSet("validate mcr6_q2m1 foreground_color is equal to {mcr6_q2m1_foreground_color_expected}".format(mcr6_q2m1_foreground_color_expected=mcr6_q2m1_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_q2m1_foreground_color),
                        InformationSet("get mcr6_q2m1 background_color", "thriver", "mcrhci", get_mcr6_q2m1_background_color),
                        InformationSet("validate mcr6_q2m1 background_color is equal to {mcr6_q2m1_background_color_expected}".format(mcr6_q2m1_background_color_expected=mcr6_q2m1_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_q2m1_background_color),
                        InformationSet("get mcr6_q3m1 visibility", "thriver", "mcrhci", get_mcr6_q3m1_visibility),
                        InformationSet("validate mcr6_q3m1 visibility is equal to {mcr6_q3m1_visibility_expected}".format(mcr6_q3m1_visibility_expected=mcr6_q3m1_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_q3m1_visibility),
                        InformationSet("get mcr6_q3m1 value", "thriver", "mcrhci", get_mcr6_q3m1_value),
                        InformationSet("validate mcr6_q3m1 value is equal to {mcr6_q3m1_value_expected}".format(mcr6_q3m1_value_expected=mcr6_q3m1_value_expected), "mcrhci", "hcitracer", validate_mcr6_q3m1_value),
                        InformationSet("get mcr6_q3m1 foreground_color", "thriver", "mcrhci", get_mcr6_q3m1_foreground_color),
                        InformationSet("validate mcr6_q3m1 foreground_color is equal to {mcr6_q3m1_foreground_color_expected}".format(mcr6_q3m1_foreground_color_expected=mcr6_q3m1_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_q3m1_foreground_color),
                        InformationSet("get mcr6_q3m1 background_color", "thriver", "mcrhci", get_mcr6_q3m1_background_color),
                        InformationSet("validate mcr6_q3m1 background_color is equal to {mcr6_q3m1_background_color_expected}".format(mcr6_q3m1_background_color_expected=mcr6_q3m1_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_q3m1_background_color),
                        InformationSet("get mcr6_q1g1 visibility", "thriver", "mcrhci", get_mcr6_q1g1_visibility),
                        InformationSet("validate mcr6_q1g1 visibility is equal to {mcr6_q1g1_visibility_expected}".format(mcr6_q1g1_visibility_expected=mcr6_q1g1_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_q1g1_visibility),
                        InformationSet("get mcr6_q1g1 value", "thriver", "mcrhci", get_mcr6_q1g1_value),
                        InformationSet("validate mcr6_q1g1 value is equal to {mcr6_q1g1_value_expected}".format(mcr6_q1g1_value_expected=mcr6_q1g1_value_expected), "mcrhci", "hcitracer", validate_mcr6_q1g1_value),
                        InformationSet("get mcr6_q1g1 foreground_color", "thriver", "mcrhci", get_mcr6_q1g1_foreground_color),
                        InformationSet("validate mcr6_q1g1 foreground_color is equal to {mcr6_q1g1_foreground_color_expected}".format(mcr6_q1g1_foreground_color_expected=mcr6_q1g1_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_q1g1_foreground_color),
                        InformationSet("get mcr6_q1g1 background_color", "thriver", "mcrhci", get_mcr6_q1g1_background_color),
                        InformationSet("validate mcr6_q1g1 background_color is equal to {mcr6_q1g1_background_color_expected}".format(mcr6_q1g1_background_color_expected=mcr6_q1g1_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_q1g1_background_color),
                        InformationSet("get mcr6_q2g1 visibility", "thriver", "mcrhci", get_mcr6_q2g1_visibility),
                        InformationSet("validate mcr6_q2g1 visibility is equal to {mcr6_q2g1_visibility_expected}".format(mcr6_q2g1_visibility_expected=mcr6_q2g1_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_q2g1_visibility),
                        InformationSet("get mcr6_q2g1 value", "thriver", "mcrhci", get_mcr6_q2g1_value),
                        InformationSet("validate mcr6_q2g1 value is equal to {mcr6_q2g1_value_expected}".format(mcr6_q2g1_value_expected=mcr6_q2g1_value_expected), "mcrhci", "hcitracer", validate_mcr6_q2g1_value),
                        InformationSet("get mcr6_q2g1 foreground_color", "thriver", "mcrhci", get_mcr6_q2g1_foreground_color),
                        InformationSet("validate mcr6_q2g1 foreground_color is equal to {mcr6_q2g1_foreground_color_expected}".format(mcr6_q2g1_foreground_color_expected=mcr6_q2g1_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_q2g1_foreground_color),
                        InformationSet("get mcr6_q2g1 background_color", "thriver", "mcrhci", get_mcr6_q2g1_background_color),
                        InformationSet("validate mcr6_q2g1 background_color is equal to {mcr6_q2g1_background_color_expected}".format(mcr6_q2g1_background_color_expected=mcr6_q2g1_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_q2g1_background_color),
                        InformationSet("get mcr6_q3g1 visibility", "thriver", "mcrhci", get_mcr6_q3g1_visibility),
                        InformationSet("validate mcr6_q3g1 visibility is equal to {mcr6_q3g1_visibility_expected}".format(mcr6_q3g1_visibility_expected=mcr6_q3g1_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_q3g1_visibility),
                        InformationSet("get mcr6_q3g1 value", "thriver", "mcrhci", get_mcr6_q3g1_value),
                        InformationSet("validate mcr6_q3g1 value is equal to {mcr6_q3g1_value_expected}".format(mcr6_q3g1_value_expected=mcr6_q3g1_value_expected), "mcrhci", "hcitracer", validate_mcr6_q3g1_value),
                        InformationSet("get mcr6_q3g1 foreground_color", "thriver", "mcrhci", get_mcr6_q3g1_foreground_color),
                        InformationSet("validate mcr6_q3g1 foreground_color is equal to {mcr6_q3g1_foreground_color_expected}".format(mcr6_q3g1_foreground_color_expected=mcr6_q3g1_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_q3g1_foreground_color),
                        InformationSet("get mcr6_q3g1 background_color", "thriver", "mcrhci", get_mcr6_q3g1_background_color),
                        InformationSet("validate mcr6_q3g1 background_color is equal to {mcr6_q3g1_background_color_expected}".format(mcr6_q3g1_background_color_expected=mcr6_q3g1_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_q3g1_background_color),
                        InformationSet("get mcr6_q4g1 visibility", "thriver", "mcrhci", get_mcr6_q4g1_visibility),
                        InformationSet("validate mcr6_q4g1 visibility is equal to {mcr6_q4g1_visibility_expected}".format(mcr6_q4g1_visibility_expected=mcr6_q4g1_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_q4g1_visibility),
                        InformationSet("get mcr6_q4g1 value", "thriver", "mcrhci", get_mcr6_q4g1_value),
                        InformationSet("validate mcr6_q4g1 value is equal to {mcr6_q4g1_value_expected}".format(mcr6_q4g1_value_expected=mcr6_q4g1_value_expected), "mcrhci", "hcitracer", validate_mcr6_q4g1_value),
                        InformationSet("get mcr6_q4g1 foreground_color", "thriver", "mcrhci", get_mcr6_q4g1_foreground_color),
                        InformationSet("validate mcr6_q4g1 foreground_color is equal to {mcr6_q4g1_foreground_color_expected}".format(mcr6_q4g1_foreground_color_expected=mcr6_q4g1_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_q4g1_foreground_color),
                        InformationSet("get mcr6_q4g1 background_color", "thriver", "mcrhci", get_mcr6_q4g1_background_color),
                        InformationSet("validate mcr6_q4g1 background_color is equal to {mcr6_q4g1_background_color_expected}".format(mcr6_q4g1_background_color_expected=mcr6_q4g1_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_q4g1_background_color),
                        InformationSet("get mcr6_q5g1 visibility", "thriver", "mcrhci", get_mcr6_q5g1_visibility),
                        InformationSet("validate mcr6_q5g1 visibility is equal to {mcr6_q5g1_visibility_expected}".format(mcr6_q5g1_visibility_expected=mcr6_q5g1_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_q5g1_visibility),
                        InformationSet("get mcr6_q5g1 value", "thriver", "mcrhci", get_mcr6_q5g1_value),
                        InformationSet("validate mcr6_q5g1 value is equal to {mcr6_q5g1_value_expected}".format(mcr6_q5g1_value_expected=mcr6_q5g1_value_expected), "mcrhci", "hcitracer", validate_mcr6_q5g1_value),
                        InformationSet("get mcr6_q5g1 foreground_color", "thriver", "mcrhci", get_mcr6_q5g1_foreground_color),
                        InformationSet("validate mcr6_q5g1 foreground_color is equal to {mcr6_q5g1_foreground_color_expected}".format(mcr6_q5g1_foreground_color_expected=mcr6_q5g1_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_q5g1_foreground_color),
                        InformationSet("get mcr6_q5g1 background_color", "thriver", "mcrhci", get_mcr6_q5g1_background_color),
                        InformationSet("validate mcr6_q5g1 background_color is equal to {mcr6_q5g1_background_color_expected}".format(mcr6_q5g1_background_color_expected=mcr6_q5g1_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_q5g1_background_color),
                        InformationSet("get mcr6_b1g1 visibility", "thriver", "mcrhci", get_mcr6_b1g1_visibility),
                        InformationSet("validate mcr6_b1g1 visibility is equal to {mcr6_b1g1_visibility_expected}".format(mcr6_b1g1_visibility_expected=mcr6_b1g1_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_b1g1_visibility),
                        InformationSet("get mcr6_b1g1 value", "thriver", "mcrhci", get_mcr6_b1g1_value),
                        InformationSet("validate mcr6_b1g1 value is equal to {mcr6_b1g1_value_expected}".format(mcr6_b1g1_value_expected=mcr6_b1g1_value_expected), "mcrhci", "hcitracer", validate_mcr6_b1g1_value),
                        InformationSet("get mcr6_b1g1 foreground_color", "thriver", "mcrhci", get_mcr6_b1g1_foreground_color),
                        InformationSet("validate mcr6_b1g1 foreground_color is equal to {mcr6_b1g1_foreground_color_expected}".format(mcr6_b1g1_foreground_color_expected=mcr6_b1g1_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_b1g1_foreground_color),
                        InformationSet("get mcr6_b1g1 background_color", "thriver", "mcrhci", get_mcr6_b1g1_background_color),
                        InformationSet("validate mcr6_b1g1 background_color is equal to {mcr6_b1g1_background_color_expected}".format(mcr6_b1g1_background_color_expected=mcr6_b1g1_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_b1g1_background_color),
                        InformationSet("get mcr6_b2g1 visibility", "thriver", "mcrhci", get_mcr6_b2g1_visibility),
                        InformationSet("validate mcr6_b2g1 visibility is equal to {mcr6_b2g1_visibility_expected}".format(mcr6_b2g1_visibility_expected=mcr6_b2g1_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_b2g1_visibility),
                        InformationSet("get mcr6_b2g1 value", "thriver", "mcrhci", get_mcr6_b2g1_value),
                        InformationSet("validate mcr6_b2g1 value is equal to {mcr6_b2g1_value_expected}".format(mcr6_b2g1_value_expected=mcr6_b2g1_value_expected), "mcrhci", "hcitracer", validate_mcr6_b2g1_value),
                        InformationSet("get mcr6_b2g1 foreground_color", "thriver", "mcrhci", get_mcr6_b2g1_foreground_color),
                        InformationSet("validate mcr6_b2g1 foreground_color is equal to {mcr6_b2g1_foreground_color_expected}".format(mcr6_b2g1_foreground_color_expected=mcr6_b2g1_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_b2g1_foreground_color),
                        InformationSet("get mcr6_b2g1 background_color", "thriver", "mcrhci", get_mcr6_b2g1_background_color),
                        InformationSet("validate mcr6_b2g1 background_color is equal to {mcr6_b2g1_background_color_expected}".format(mcr6_b2g1_background_color_expected=mcr6_b2g1_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_b2g1_background_color),
                        InformationSet("get mcr6_t9g1 visibility", "thriver", "mcrhci", get_mcr6_t9g1_visibility),
                        InformationSet("validate mcr6_t9g1 visibility is equal to {mcr6_t9g1_visibility_expected}".format(mcr6_t9g1_visibility_expected=mcr6_t9g1_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_t9g1_visibility),
                        InformationSet("get mcr6_t9g1 value", "thriver", "mcrhci", get_mcr6_t9g1_value),
                        InformationSet("validate mcr6_t9g1 value is equal to {mcr6_t9g1_value_expected}".format(mcr6_t9g1_value_expected=mcr6_t9g1_value_expected), "mcrhci", "hcitracer", validate_mcr6_t9g1_value),
                        InformationSet("get mcr6_t9g1 foreground_color", "thriver", "mcrhci", get_mcr6_t9g1_foreground_color),
                        InformationSet("validate mcr6_t9g1 foreground_color is equal to {mcr6_t9g1_foreground_color_expected}".format(mcr6_t9g1_foreground_color_expected=mcr6_t9g1_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_t9g1_foreground_color),
                        InformationSet("get mcr6_t9g1 background_color", "thriver", "mcrhci", get_mcr6_t9g1_background_color),
                        InformationSet("validate mcr6_t9g1 background_color is equal to {mcr6_t9g1_background_color_expected}".format(mcr6_t9g1_background_color_expected=mcr6_t9g1_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_t9g1_background_color),
                        InformationSet("get mcr6_t10g1 visibility", "thriver", "mcrhci", get_mcr6_t10g1_visibility),
                        InformationSet("validate mcr6_t10g1 visibility is equal to {mcr6_t10g1_visibility_expected}".format(mcr6_t10g1_visibility_expected=mcr6_t10g1_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_t10g1_visibility),
                        InformationSet("get mcr6_t10g1 value", "thriver", "mcrhci", get_mcr6_t10g1_value),
                        InformationSet("validate mcr6_t10g1 value is equal to {mcr6_t10g1_value_expected}".format(mcr6_t10g1_value_expected=mcr6_t10g1_value_expected), "mcrhci", "hcitracer", validate_mcr6_t10g1_value),
                        InformationSet("get mcr6_t10g1 foreground_color", "thriver", "mcrhci", get_mcr6_t10g1_foreground_color),
                        InformationSet("validate mcr6_t10g1 foreground_color is equal to {mcr6_t10g1_foreground_color_expected}".format(mcr6_t10g1_foreground_color_expected=mcr6_t10g1_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_t10g1_foreground_color),
                        InformationSet("get mcr6_t10g1 background_color", "thriver", "mcrhci", get_mcr6_t10g1_background_color),
                        InformationSet("validate mcr6_t10g1 background_color is equal to {mcr6_t10g1_background_color_expected}".format(mcr6_t10g1_background_color_expected=mcr6_t10g1_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_t10g1_background_color),
                        InformationSet("get Label1 visibility", "thriver", "mcrhci", get_Label1_visibility),
                        InformationSet("validate Label1 visibility is equal to {Label1_visibility_expected}".format(Label1_visibility_expected=Label1_visibility_expected), "mcrhci", "hcitracer", validate_Label1_visibility),
                        InformationSet("get Label1 foreground_color", "thriver", "mcrhci", get_Label1_foreground_color),
                        InformationSet("validate Label1 foreground_color is equal to {Label1_foreground_color_expected}".format(Label1_foreground_color_expected=Label1_foreground_color_expected), "mcrhci", "hcitracer", validate_Label1_foreground_color),
                        InformationSet("get Label1 background_color", "thriver", "mcrhci", get_Label1_background_color),
                        InformationSet("validate Label1 background_color is equal to {Label1_background_color_expected}".format(Label1_background_color_expected=Label1_background_color_expected), "mcrhci", "hcitracer", validate_Label1_background_color),
                        InformationSet("get mcr6_energytxt visibility", "thriver", "mcrhci", get_mcr6_energytxt_visibility),
                        InformationSet("validate mcr6_energytxt visibility is equal to {mcr6_energytxt_visibility_expected}".format(mcr6_energytxt_visibility_expected=mcr6_energytxt_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_energytxt_visibility),
                        InformationSet("get mcr6_energytxt value", "thriver", "mcrhci", get_mcr6_energytxt_value),
                        InformationSet("validate mcr6_energytxt value is equal to {mcr6_energytxt_value_expected}".format(mcr6_energytxt_value_expected=mcr6_energytxt_value_expected), "mcrhci", "hcitracer", validate_mcr6_energytxt_value),
                        InformationSet("get mcr6_energytxt foreground_color", "thriver", "mcrhci", get_mcr6_energytxt_foreground_color),
                        InformationSet("validate mcr6_energytxt foreground_color is equal to {mcr6_energytxt_foreground_color_expected}".format(mcr6_energytxt_foreground_color_expected=mcr6_energytxt_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_energytxt_foreground_color),
                        InformationSet("get mcr6_energytxt background_color", "thriver", "mcrhci", get_mcr6_energytxt_background_color),
                        InformationSet("validate mcr6_energytxt background_color is equal to {mcr6_energytxt_background_color_expected}".format(mcr6_energytxt_background_color_expected=mcr6_energytxt_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_energytxt_background_color),
                        InformationSet("get Label2 visibility", "thriver", "mcrhci", get_Label2_visibility),
                        InformationSet("validate Label2 visibility is equal to {Label2_visibility_expected}".format(Label2_visibility_expected=Label2_visibility_expected), "mcrhci", "hcitracer", validate_Label2_visibility),
                        InformationSet("get Label2 foreground_color", "thriver", "mcrhci", get_Label2_foreground_color),
                        InformationSet("validate Label2 foreground_color is equal to {Label2_foreground_color_expected}".format(Label2_foreground_color_expected=Label2_foreground_color_expected), "mcrhci", "hcitracer", validate_Label2_foreground_color),
                        InformationSet("get Label2 background_color", "thriver", "mcrhci", get_Label2_background_color),
                        InformationSet("validate Label2 background_color is equal to {Label2_background_color_expected}".format(Label2_background_color_expected=Label2_background_color_expected), "mcrhci", "hcitracer", validate_Label2_background_color),
                        InformationSet("get energy_shape visibility", "thriver", "mcrhci", get_energy_shape_visibility),
                        InformationSet("validate energy_shape visibility is equal to {energy_shape_visibility_expected}".format(energy_shape_visibility_expected=energy_shape_visibility_expected), "mcrhci", "hcitracer", validate_energy_shape_visibility),
                        InformationSet("get energy_shape foreground_color", "thriver", "mcrhci", get_energy_shape_foreground_color),
                        InformationSet("validate energy_shape foreground_color is equal to {energy_shape_foreground_color_expected}".format(energy_shape_foreground_color_expected=energy_shape_foreground_color_expected), "mcrhci", "hcitracer", validate_energy_shape_foreground_color),
                        InformationSet("get energy_shape background_color", "thriver", "mcrhci", get_energy_shape_background_color),
                        InformationSet("validate energy_shape background_color is equal to {energy_shape_background_color_expected}".format(energy_shape_background_color_expected=energy_shape_background_color_expected), "mcrhci", "hcitracer", validate_energy_shape_background_color),
                        InformationSet("get mcr6_gantry1positiontxt visibility", "thriver", "mcrhci", get_mcr6_gantry1positiontxt_visibility),
                        InformationSet("validate mcr6_gantry1positiontxt visibility is equal to {mcr6_gantry1positiontxt_visibility_expected}".format(mcr6_gantry1positiontxt_visibility_expected=mcr6_gantry1positiontxt_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_gantry1positiontxt_visibility),
                        InformationSet("get mcr6_gantry1positiontxt value", "thriver", "mcrhci", get_mcr6_gantry1positiontxt_value),
                        InformationSet("validate mcr6_gantry1positiontxt value is equal to {mcr6_gantry1positiontxt_value_expected}".format(mcr6_gantry1positiontxt_value_expected=mcr6_gantry1positiontxt_value_expected), "mcrhci", "hcitracer", validate_mcr6_gantry1positiontxt_value),
                        InformationSet("get mcr6_gantry1positiontxt foreground_color", "thriver", "mcrhci", get_mcr6_gantry1positiontxt_foreground_color),
                        InformationSet("validate mcr6_gantry1positiontxt foreground_color is equal to {mcr6_gantry1positiontxt_foreground_color_expected}".format(mcr6_gantry1positiontxt_foreground_color_expected=mcr6_gantry1positiontxt_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_gantry1positiontxt_foreground_color),
                        InformationSet("get mcr6_gantry1positiontxt background_color", "thriver", "mcrhci", get_mcr6_gantry1positiontxt_background_color),
                        InformationSet("validate mcr6_gantry1positiontxt background_color is equal to {mcr6_gantry1positiontxt_background_color_expected}".format(mcr6_gantry1positiontxt_background_color_expected=mcr6_gantry1positiontxt_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_gantry1positiontxt_background_color),
                        InformationSet("get gantry_shape visibility", "thriver", "mcrhci", get_gantry_shape_visibility),
                        InformationSet("validate gantry_shape visibility is equal to {gantry_shape_visibility_expected}".format(gantry_shape_visibility_expected=gantry_shape_visibility_expected), "mcrhci", "hcitracer", validate_gantry_shape_visibility),
                        InformationSet("get gantry_shape foreground_color", "thriver", "mcrhci", get_gantry_shape_foreground_color),
                        InformationSet("validate gantry_shape foreground_color is equal to {gantry_shape_foreground_color_expected}".format(gantry_shape_foreground_color_expected=gantry_shape_foreground_color_expected), "mcrhci", "hcitracer", validate_gantry_shape_foreground_color),
                        InformationSet("get gantry_shape background_color", "thriver", "mcrhci", get_gantry_shape_background_color),
                        InformationSet("validate gantry_shape background_color is equal to {gantry_shape_background_color_expected}".format(gantry_shape_background_color_expected=gantry_shape_background_color_expected), "mcrhci", "hcitracer", validate_gantry_shape_background_color),                     
                        InformationSet("get range_edit_shape visibility", "thriver", "mcrhci", get_range_edit_shape_visibility),
                        InformationSet("validate range_edit_shape visibility is equal to {range_edit_shape_visibility_expected}".format(range_edit_shape_visibility_expected=range_edit_shape_visibility_expected), "mcrhci", "hcitracer", validate_range_edit_shape_visibility),
                        InformationSet("get range_edit_shape foreground_color", "thriver", "mcrhci", get_range_edit_shape_foreground_color),
                        InformationSet("validate range_edit_shape foreground_color is equal to {range_edit_shape_foreground_color_expected}".format(range_edit_shape_foreground_color_expected=range_edit_shape_foreground_color_expected), "mcrhci", "hcitracer", validate_range_edit_shape_foreground_color),
                        InformationSet("get range_edit_shape background_color", "thriver", "mcrhci", get_range_edit_shape_background_color),
                        InformationSet("validate range_edit_shape background_color is equal to {range_edit_shape_background_color_expected}".format(range_edit_shape_background_color_expected=range_edit_shape_background_color_expected), "mcrhci", "hcitracer", validate_range_edit_shape_background_color),
                        InformationSet("get mcr6_global_range_status visibility", "thriver", "mcrhci", get_mcr6_global_range_status_visibility),
                        InformationSet("validate mcr6_global_range_status visibility is equal to {mcr6_global_range_status_visibility_expected}".format(mcr6_global_range_status_visibility_expected=mcr6_global_range_status_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_global_range_status_visibility),
                        InformationSet("get mcr6_global_range_status value", "thriver", "mcrhci", get_mcr6_global_range_status_value),
                        InformationSet("validate mcr6_global_range_status value is equal to {mcr6_global_range_status_value_expected}".format(mcr6_global_range_status_value_expected=mcr6_global_range_status_value_expected), "mcrhci", "hcitracer", validate_mcr6_global_range_status_value),
                        InformationSet("get mcr6_global_range_status foreground_color", "thriver", "mcrhci", get_mcr6_global_range_status_foreground_color),
                        InformationSet("validate mcr6_global_range_status foreground_color is equal to {mcr6_global_range_status_foreground_color_expected}".format(mcr6_global_range_status_foreground_color_expected=mcr6_global_range_status_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_global_range_status_foreground_color),
                        InformationSet("get mcr6_global_range_status background_color", "thriver", "mcrhci", get_mcr6_global_range_status_background_color),
                        InformationSet("validate mcr6_global_range_status background_color is equal to {mcr6_global_range_status_background_color_expected}".format(mcr6_global_range_status_background_color_expected=mcr6_global_range_status_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_global_range_status_background_color),
                        InformationSet("get mcr6_fieldtxt visibility", "thriver", "mcrhci", get_mcr6_fieldtxt_visibility),
                        InformationSet("validate mcr6_fieldtxt visibility is equal to {mcr6_fieldtxt_visibility_expected}".format(mcr6_fieldtxt_visibility_expected=mcr6_fieldtxt_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_fieldtxt_visibility),
                        InformationSet("get mcr6_fieldtxt value", "thriver", "mcrhci", get_mcr6_fieldtxt_value),
                        InformationSet("validate mcr6_fieldtxt value is equal to {mcr6_fieldtxt_value_expected}".format(mcr6_fieldtxt_value_expected=mcr6_fieldtxt_value_expected), "mcrhci", "hcitracer", validate_mcr6_fieldtxt_value),
                        InformationSet("get mcr6_fieldtxt foreground_color", "thriver", "mcrhci", get_mcr6_fieldtxt_foreground_color),
                        InformationSet("validate mcr6_fieldtxt foreground_color is equal to {mcr6_fieldtxt_foreground_color_expected}".format(mcr6_fieldtxt_foreground_color_expected=mcr6_fieldtxt_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_fieldtxt_foreground_color),
                        InformationSet("get mcr6_fieldtxt background_color", "thriver", "mcrhci", get_mcr6_fieldtxt_background_color),
                        InformationSet("validate mcr6_fieldtxt background_color is equal to {mcr6_fieldtxt_background_color_expected}".format(mcr6_fieldtxt_background_color_expected=mcr6_fieldtxt_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_fieldtxt_background_color),
                        InformationSet("get field_shape visibility", "thriver", "mcrhci", get_field_shape_visibility),
                        InformationSet("validate field_shape visibility is equal to {field_shape_visibility_expected}".format(field_shape_visibility_expected=field_shape_visibility_expected), "mcrhci", "hcitracer", validate_field_shape_visibility),
                        InformationSet("get field_shape foreground_color", "thriver", "mcrhci", get_field_shape_foreground_color),
                        InformationSet("validate field_shape foreground_color is equal to {field_shape_foreground_color_expected}".format(field_shape_foreground_color_expected=field_shape_foreground_color_expected), "mcrhci", "hcitracer", validate_field_shape_foreground_color),
                        InformationSet("get field_shape background_color", "thriver", "mcrhci", get_field_shape_background_color),
                        InformationSet("validate field_shape background_color is equal to {field_shape_background_color_expected}".format(field_shape_background_color_expected=field_shape_background_color_expected), "mcrhci", "hcitracer", validate_field_shape_background_color),
                        InformationSet("get mcr6_sl1x visibility", "thriver", "mcrhci", get_mcr6_sl1x_visibility),
                        InformationSet("validate mcr6_sl1x visibility is equal to {mcr6_sl1x_visibility_expected}".format(mcr6_sl1x_visibility_expected=mcr6_sl1x_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_sl1x_visibility),
                        InformationSet("get mcr6_sl1x value", "thriver", "mcrhci", get_mcr6_sl1x_value),
                        InformationSet("validate mcr6_sl1x value is equal to {mcr6_sl1x_value_expected}".format(mcr6_sl1x_value_expected=mcr6_sl1x_value_expected), "mcrhci", "hcitracer", validate_mcr6_sl1x_value),
                        InformationSet("get mcr6_sl1x foreground_color", "thriver", "mcrhci", get_mcr6_sl1x_foreground_color),
                        InformationSet("validate mcr6_sl1x foreground_color is equal to {mcr6_sl1x_foreground_color_expected}".format(mcr6_sl1x_foreground_color_expected=mcr6_sl1x_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_sl1x_foreground_color),
                        InformationSet("get mcr6_sl1x background_color", "thriver", "mcrhci", get_mcr6_sl1x_background_color),
                        InformationSet("validate mcr6_sl1x background_color is equal to {mcr6_sl1x_background_color_expected}".format(mcr6_sl1x_background_color_expected=mcr6_sl1x_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_sl1x_background_color),
                        InformationSet("get mcr6_sl1y visibility", "thriver", "mcrhci", get_mcr6_sl1y_visibility),
                        InformationSet("validate mcr6_sl1y visibility is equal to {mcr6_sl1y_visibility_expected}".format(mcr6_sl1y_visibility_expected=mcr6_sl1y_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_sl1y_visibility),
                        InformationSet("get mcr6_sl1y value", "thriver", "mcrhci", get_mcr6_sl1y_value),
                        InformationSet("validate mcr6_sl1y value is equal to {mcr6_sl1y_value_expected}".format(mcr6_sl1y_value_expected=mcr6_sl1y_value_expected), "mcrhci", "hcitracer", validate_mcr6_sl1y_value),
                        InformationSet("get mcr6_sl1y foreground_color", "thriver", "mcrhci", get_mcr6_sl1y_foreground_color),
                        InformationSet("validate mcr6_sl1y foreground_color is equal to {mcr6_sl1y_foreground_color_expected}".format(mcr6_sl1y_foreground_color_expected=mcr6_sl1y_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_sl1y_foreground_color),
                        InformationSet("get mcr6_sl1y background_color", "thriver", "mcrhci", get_mcr6_sl1y_background_color),
                        InformationSet("validate mcr6_sl1y background_color is equal to {mcr6_sl1y_background_color_expected}".format(mcr6_sl1y_background_color_expected=mcr6_sl1y_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_sl1y_background_color),
                        InformationSet("get mcr6_sl2x visibility", "thriver", "mcrhci", get_mcr6_sl2x_visibility),
                        InformationSet("validate mcr6_sl2x visibility is equal to {mcr6_sl2x_visibility_expected}".format(mcr6_sl2x_visibility_expected=mcr6_sl2x_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_sl2x_visibility),
                        InformationSet("get mcr6_sl2x value", "thriver", "mcrhci", get_mcr6_sl2x_value),
                        InformationSet("validate mcr6_sl2x value is equal to {mcr6_sl2x_value_expected}".format(mcr6_sl2x_value_expected=mcr6_sl2x_value_expected), "mcrhci", "hcitracer", validate_mcr6_sl2x_value),
                        InformationSet("get mcr6_sl2x foreground_color", "thriver", "mcrhci", get_mcr6_sl2x_foreground_color),
                        InformationSet("validate mcr6_sl2x foreground_color is equal to {mcr6_sl2x_foreground_color_expected}".format(mcr6_sl2x_foreground_color_expected=mcr6_sl2x_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_sl2x_foreground_color),
                        InformationSet("get mcr6_sl2x background_color", "thriver", "mcrhci", get_mcr6_sl2x_background_color),
                        InformationSet("validate mcr6_sl2x background_color is equal to {mcr6_sl2x_background_color_expected}".format(mcr6_sl2x_background_color_expected=mcr6_sl2x_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_sl2x_background_color),
                        InformationSet("get mcr6_graphitestepreached visibility", "thriver", "mcrhci", get_mcr6_graphitestepreached_visibility),
                        InformationSet("validate mcr6_graphitestepreached visibility is equal to {mcr6_graphitestepreached_visibility_expected}".format(mcr6_graphitestepreached_visibility_expected=mcr6_graphitestepreached_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_graphitestepreached_visibility),
                        InformationSet("get mcr6_graphitestepreached value", "thriver", "mcrhci", get_mcr6_graphitestepreached_value),
                        InformationSet("validate mcr6_graphitestepreached value is equal to {mcr6_graphitestepreached_value_expected}".format(mcr6_graphitestepreached_value_expected=mcr6_graphitestepreached_value_expected), "mcrhci", "hcitracer", validate_mcr6_graphitestepreached_value),
                        InformationSet("get mcr6_graphitestepreached foreground_color", "thriver", "mcrhci", get_mcr6_graphitestepreached_foreground_color),
                        InformationSet("validate mcr6_graphitestepreached foreground_color is equal to {mcr6_graphitestepreached_foreground_color_expected}".format(mcr6_graphitestepreached_foreground_color_expected=mcr6_graphitestepreached_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_graphitestepreached_foreground_color),
                        InformationSet("get mcr6_graphitestepreached background_color", "thriver", "mcrhci", get_mcr6_graphitestepreached_background_color),
                        InformationSet("validate mcr6_graphitestepreached background_color is equal to {mcr6_graphitestepreached_background_color_expected}".format(mcr6_graphitestepreached_background_color_expected=mcr6_graphitestepreached_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_graphitestepreached_background_color),
                        InformationSet("get mcr6_graphitestepreached_value visibility", "thriver", "mcrhci", get_mcr6_graphitestepreached_value_visibility),
                        InformationSet("validate mcr6_graphitestepreached_value visibility is equal to {mcr6_graphitestepreached_value_visibility_expected}".format(mcr6_graphitestepreached_value_visibility_expected=mcr6_graphitestepreached_value_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_graphitestepreached_value_visibility),
                        InformationSet("get mcr6_graphitestepreached_value value", "thriver", "mcrhci", get_mcr6_graphitestepreached_value_value),
                        InformationSet("validate mcr6_graphitestepreached_value value is equal to {mcr6_graphitestepreached_value_value_expected}".format(mcr6_graphitestepreached_value_value_expected=mcr6_graphitestepreached_value_value_expected), "mcrhci", "hcitracer", validate_mcr6_graphitestepreached_value_value),
                        InformationSet("get mcr6_graphitestepreached_value foreground_color", "thriver", "mcrhci", get_mcr6_graphitestepreached_value_foreground_color),
                        InformationSet("validate mcr6_graphitestepreached_value foreground_color is equal to {mcr6_graphitestepreached_value_foreground_color_expected}".format(mcr6_graphitestepreached_value_foreground_color_expected=mcr6_graphitestepreached_value_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_graphitestepreached_value_foreground_color),
                        InformationSet("get mcr6_graphitestepreached_value background_color", "thriver", "mcrhci", get_mcr6_graphitestepreached_value_background_color),
                        InformationSet("validate mcr6_graphitestepreached_value background_color is equal to {mcr6_graphitestepreached_value_background_color_expected}".format(mcr6_graphitestepreached_value_background_color_expected=mcr6_graphitestepreached_value_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_graphitestepreached_value_background_color),
                        InformationSet("get mcr6_setrangebtn visibility", "thriver", "mcrhci", get_mcr6_setrangebtn_visibility),
                        InformationSet("validate mcr6_setrangebtn visibility is equal to {mcr6_setrangebtn_visibility_expected}".format(mcr6_setrangebtn_visibility_expected=mcr6_setrangebtn_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_setrangebtn_visibility),
                        InformationSet("get mcr6_setrangebtn foreground_color", "thriver", "mcrhci", get_mcr6_setrangebtn_foreground_color),
                        InformationSet("validate mcr6_setrangebtn foreground_color is equal to {mcr6_setrangebtn_foreground_color_expected}".format(mcr6_setrangebtn_foreground_color_expected=mcr6_setrangebtn_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_setrangebtn_foreground_color),
                        InformationSet("get mcr6_setrangebtn background_color", "thriver", "mcrhci", get_mcr6_setrangebtn_background_color),
                        InformationSet("validate mcr6_setrangebtn background_color is equal to {mcr6_setrangebtn_background_color_expected}".format(mcr6_setrangebtn_background_color_expected=mcr6_setrangebtn_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_setrangebtn_background_color),                     
                        InformationSet("get mcr6_degrader_status visibility", "thriver", "mcrhci", get_mcr6_degrader_status_visibility),
                        InformationSet("validate mcr6_degrader_status visibility is equal to {mcr6_degrader_status_visibility_expected}".format(mcr6_degrader_status_visibility_expected=mcr6_degrader_status_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_degrader_status_visibility),
                        InformationSet("get mcr6_degrader_status value", "thriver", "mcrhci", get_mcr6_degrader_status_value),
                        InformationSet("validate mcr6_degrader_status value is equal to {mcr6_degrader_status_value_expected}".format(mcr6_degrader_status_value_expected=mcr6_degrader_status_value_expected), "mcrhci", "hcitracer", validate_mcr6_degrader_status_value),
                        InformationSet("get mcr6_degrader_status foreground_color", "thriver", "mcrhci", get_mcr6_degrader_status_foreground_color),
                        InformationSet("validate mcr6_degrader_status foreground_color is equal to {mcr6_degrader_status_foreground_color_expected}".format(mcr6_degrader_status_foreground_color_expected=mcr6_degrader_status_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_degrader_status_foreground_color),
                        InformationSet("get mcr6_degrader_status background_color", "thriver", "mcrhci", get_mcr6_degrader_status_background_color),
                        InformationSet("validate mcr6_degrader_status background_color is equal to {mcr6_degrader_status_background_color_expected}".format(mcr6_degrader_status_background_color_expected=mcr6_degrader_status_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_degrader_status_background_color),
                        InformationSet("get mcr6_iseu1btn visibility", "thriver", "mcrhci", get_mcr6_iseu1btn_visibility),
                        InformationSet("validate mcr6_iseu1btn visibility is equal to {mcr6_iseu1btn_visibility_expected}".format(mcr6_iseu1btn_visibility_expected=mcr6_iseu1btn_visibility_expected), "mcrhci", "hcitracer", validate_mcr6_iseu1btn_visibility),
                        InformationSet("get mcr6_iseu1btn foreground_color", "thriver", "mcrhci", get_mcr6_iseu1btn_foreground_color),
                        InformationSet("validate mcr6_iseu1btn foreground_color is equal to {mcr6_iseu1btn_foreground_color_expected}".format(mcr6_iseu1btn_foreground_color_expected=mcr6_iseu1btn_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr6_iseu1btn_foreground_color),
                        InformationSet("get mcr6_iseu1btn background_color", "thriver", "mcrhci", get_mcr6_iseu1btn_background_color),
                        InformationSet("validate mcr6_iseu1btn background_color is equal to {mcr6_iseu1btn_background_color_expected}".format(mcr6_iseu1btn_background_color_expected=mcr6_iseu1btn_background_color_expected), "mcrhci", "hcitracer", validate_mcr6_iseu1btn_background_color),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [  
                        ]
        self.teardown_path = []