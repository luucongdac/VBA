
"""
File:
======================================

This module implements set up path for mcrhci test

Copyright (c) MGH 2023

Test for setup ClinicalIntegrationTestProcedure

"""



from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.infoset.tcsobject.dba_objects import *

class SETUP_VALIDATE_BTS1_LAYOUT_SCREEN(ClinicalIntegrationTestProcedure):
    # default variable values
    name = "Confirm that MCR_Service_BTS1_Layout (bts1_layout.v) is displayed"
    bts1_layout_bs3_out_btn_visibility_expected = "1"
    q27_visibility_expected = "1"
    q26_visibility_expected = "1"
    q30_visibility_expected = "1"
    b5_visibility_expected = "1"
    q31_visibility_expected = "1"
    q25_visibility_expected = "1"
    mcr_ecubtcu_sstech_ps_status_init_1 = 1
    bts1_layout_ps_canbus_status_txt_foreground_color_expected = "0"
    mcr_ecubtcu_sstech_ps_status_init_2 = 0.6
    bts1_layout_ps_canbus_status_ind_subobject_name_expected = "iba_check_ok.sd"
    q33_visibility_expected = "1"
    q34_visibility_expected = "1"
    q32_visibility_expected = "1"
    t11_visibility_expected = "1"
    mcr_ecubtcu_piranigts1_mbarvacuum_init_1 = 0.1
    bts1_layout_mbar_number_txt_value_expected = 0.1
    mcr_ecubtcu_piranigts1_mbarvacuum_init_2 = 0.1
    bts1_layout_mbar_number_txt_visibility_expected = "1"
    mcr_ecubtcu_piranigts1_mbarvacuum_init_3 = 0.1
    bts1_layout_mbar_txt_visibility_expected = "1"
    mcr_acu_vacuumbts1_status_init_1 = True
    bts1_layout_pirani_gauge_foreground_color_expected = "13"
    bts1_layout_gantry1_close_btn_visibility_expected = "1"
    bts1_layout_gantry1_open_btn_visibility_expected = "1"
    mcr_acu_valvegts1_opened_status_init_1 = True
    bts1_layout_gantry1_open_led_visibility_expected = "1"
    mcr_acu_valvegts1_closed_status_init_1 = True
    bts1_layout_gantry1_close_led_visibility_expected = "1"
    mcr_acu_selectiong12_status_init_1 = True
    bts1_layout_gantry12_selection_txt_foreground_color_expected = "0"
    mcr_acu_selectiong12_status_init_2 = True
    bts1_layout_gantry12_selection_ind_subobject_name_expected = "iba_check_ok.sd"
    mcr_ecubtcu_bpm13_instatus_init_1 = True
    bts1_layout_bpm13_in_visibility_expected = "1"
    bts1_layout_bpm13_out_btn_visibility_expected = "1"
    bts1_layout_bpm13_in_btn_visibility_expected = "1"
    mcr_ecubtcu_bpm13_instatus_init_2 = True
    bts1_layout_bpm13_in_led_visibility_expected = "1"
    mcr_ecubtcu_bpm13_outstatus_init_1 = True
    bts1_layout_bpm13_out_led_visibility_expected = "1"
    mcr_ecubtcu_bpm13_outstatus_init_2 = True
    bts1_layout_bpm13_out_visibility_expected = "1"
    b6_visibility_expected = "1"
    mcr_ecubtcu_bpm4_instatus_init_1 = True
    bts1_layout_bpm4_in_visibility_expected = "1"
    bts1_layout_bpm4_out_btn_visibility_expected = "1"
    bts1_layout_bpm4_in_btn_visibility_expected = "1"
    mcr_ecubtcu_bpm4_instatus_init_2 = True
    bts1_layout_bpm4_in_led_visibility_expected = "1"
    mcr_ecubtcu_bpm4_outstatus_init_1 = True
    bts1_layout_bpm4_out_led_visibility_expected = "1"
    mcr_ecubtcu_bpm4_outstatus_init_2 = True
    bts1_layout_bpm4_out_visibility_expected = "1"
    mcr_ecubtcu_bs3_instatus_init_1 = True
    bts1_layout_bs3_in_visibility_expected = "1"
    bts1_layout_bss_in_btn_visibility_expected = "1"
    mcr_ecubtcu_bs3_instatus_init_2 = True
    bts1_layout_bss_in_led_visibility_expected = "1"
    mcr_ecubtcu_bs3_outstatus_init_1 = True
    bts1_layout_bss_out_led_visibility_expected = "1"
    mcr_ecubtcu_bs3_outstatus_init_2 = True
    bts1_layout_bs3_out_visibility_expected = "1"
    mcr_ecubtcu_bpm10_instatus_init_1 = True
    bts1_layout_bpm10_in_visibility_expected = "1"
    bts1_layout_bpm10_out_btn_visibility_expected = "1"
    bts1_layout_bpm10_in_btn_visibility_expected = "1"
    mcr_ecubtcu_bpm10_instatus_init_2 = True
    bts1_layout_bpm10_in_led_visibility_expected = "1"
    mcr_ecubtcu_bpm10_outstatus_init_1 = True
    bts1_layout_bpm10_out_led_visibility_expected = "1"
    mcr_ecubtcu_bpm10_outstatus_init_2 = True
    bts1_layout_bpm10_out_visibility_expected = "1"
    mcr_acu_valvegts1_opened_status_init_2 = True
    bts1_layout_gantry1_valve_foreground_color_expected = "13"
    mcr_acu_valvesl1_opened_status_init_1 = True
    bts1_layout_sl1_valve_foreground_color_expected = "13"
    mcr_ecubtcu_piranigts1_mbarvacuum_init_4 = 0.1
    bts1_layout_out_of_range_txt_visibility_expected = "0"
    mcr_ecubtcu_bs3_cfeedback_init_1 = 0.2
    bts1_layout_bs3_nA1_txt_value_expected = 0.2
    mcr_rtieecubtcu_bcm3_highdata_visibility_init_1 = True
    bts1_layout_bs3_nA1_txt_visibility_expected = "1"
    mcr_ecubtcu_bs3_cfeedback_init_2 = 0.3
    bts1_layout_bs3_nA_txt_value_expected = 0.3
    mcr_rtieecubtcu_bcm3_lowdata_visibility_init_1 = True
    bts1_layout_bs3_nA_txt_visibility_expected = "1"
    bts1_layout_GTS1_layout_btn_visibility_expected = "1"
    bts1_layout_ess_layout_btn_visibility_expected = "1"
    bts1_layout_bts2_layout_btn_visibility_expected = "1"
    mcr_scu_safety_bts1_interlocksstatus_init_1 = True
    bts1_layout_safety_interlocks_btn_foreground_color_expected = "112"
    t12_visibility_expected = "1"
    bts1_layout_bpm11_out_btn_visibility_expected = "1"
    bts1_layout_bpm11_in_btn_visibility_expected = "1"
    mcr_ecubtcu_bpm11_instatus_init_1 = True
    bts1_layout_bpm11_in_led_visibility_expected = "1"
    mcr_ecubtcu_bpm11_outstatus_init_1 = True
    bts1_layout_bpm11_out_led_visibility_expected = "1"
    mcr_ecubtcu_bpm11_instatus_init_2 = True
    bts1_layout_bpm11_in_visibility_expected = "1"
    mcr_ecubtcu_bpm11_outstatus_init_2 = True
    bts1_layout_bpm11_out_visibility_expected = "1"
    bts1_layout_SL1_close_btn_visibility_expected = "1"
    bts1_layout_SL1_open_btn_visibility_expected = "1"
    mcr_acu_valvesl1_opened_status_init_2 = True
    bts1_layout_SL1_open_led_visibility_expected = "1"
    mcr_acu_valvesl1_closed_status_init_1 = True
    bts1_layout_SL1_close_led_visibility_expected = "1"
    bts1_layout_hidden_obj_visibility_expected = "1"
    SC5B_visibility_expected = "1"
    SC6B_visibility_expected = "1"

    def __init__(self, test):
        cls = type(self)
        name = cls.name
        bts1_layout_bs3_out_btn_visibility_expected = cls.bts1_layout_bs3_out_btn_visibility_expected
        q27_visibility_expected = cls.q27_visibility_expected
        q26_visibility_expected = cls.q26_visibility_expected
        q30_visibility_expected = cls.q30_visibility_expected
        b5_visibility_expected = cls.b5_visibility_expected
        q31_visibility_expected = cls.q31_visibility_expected
        q25_visibility_expected = cls.q25_visibility_expected
        mcr_ecubtcu_sstech_ps_status_init_1 = cls.mcr_ecubtcu_sstech_ps_status_init_1
        bts1_layout_ps_canbus_status_txt_foreground_color_expected = cls.bts1_layout_ps_canbus_status_txt_foreground_color_expected
        mcr_ecubtcu_sstech_ps_status_init_2 = cls.mcr_ecubtcu_sstech_ps_status_init_2
        bts1_layout_ps_canbus_status_ind_subobject_name_expected = cls.bts1_layout_ps_canbus_status_ind_subobject_name_expected
        q33_visibility_expected = cls.q33_visibility_expected
        q34_visibility_expected = cls.q34_visibility_expected
        q32_visibility_expected = cls.q32_visibility_expected
        t11_visibility_expected = cls.t11_visibility_expected
        mcr_ecubtcu_piranigts1_mbarvacuum_init_1 = cls.mcr_ecubtcu_piranigts1_mbarvacuum_init_1
        bts1_layout_mbar_number_txt_value_expected = cls.bts1_layout_mbar_number_txt_value_expected
        mcr_ecubtcu_piranigts1_mbarvacuum_init_2 = cls.mcr_ecubtcu_piranigts1_mbarvacuum_init_2
        bts1_layout_mbar_number_txt_visibility_expected = cls.bts1_layout_mbar_number_txt_visibility_expected
        mcr_ecubtcu_piranigts1_mbarvacuum_init_3 = cls.mcr_ecubtcu_piranigts1_mbarvacuum_init_3
        bts1_layout_mbar_txt_visibility_expected = cls.bts1_layout_mbar_txt_visibility_expected
        mcr_acu_vacuumbts1_status_init_1 = cls.mcr_acu_vacuumbts1_status_init_1
        bts1_layout_pirani_gauge_foreground_color_expected = cls.bts1_layout_pirani_gauge_foreground_color_expected
        bts1_layout_gantry1_close_btn_visibility_expected = cls.bts1_layout_gantry1_close_btn_visibility_expected
        bts1_layout_gantry1_open_btn_visibility_expected = cls.bts1_layout_gantry1_open_btn_visibility_expected
        mcr_acu_valvegts1_opened_status_init_1 = cls.mcr_acu_valvegts1_opened_status_init_1
        bts1_layout_gantry1_open_led_visibility_expected = cls.bts1_layout_gantry1_open_led_visibility_expected
        mcr_acu_valvegts1_closed_status_init_1 = cls.mcr_acu_valvegts1_closed_status_init_1
        bts1_layout_gantry1_close_led_visibility_expected = cls.bts1_layout_gantry1_close_led_visibility_expected
        mcr_acu_selectiong12_status_init_1 = cls.mcr_acu_selectiong12_status_init_1
        bts1_layout_gantry12_selection_txt_foreground_color_expected = cls.bts1_layout_gantry12_selection_txt_foreground_color_expected
        mcr_acu_selectiong12_status_init_2 = cls.mcr_acu_selectiong12_status_init_2
        bts1_layout_gantry12_selection_ind_subobject_name_expected = cls.bts1_layout_gantry12_selection_ind_subobject_name_expected
        mcr_ecubtcu_bpm13_instatus_init_1 = cls.mcr_ecubtcu_bpm13_instatus_init_1
        bts1_layout_bpm13_in_visibility_expected = cls.bts1_layout_bpm13_in_visibility_expected
        bts1_layout_bpm13_out_btn_visibility_expected = cls.bts1_layout_bpm13_out_btn_visibility_expected
        bts1_layout_bpm13_in_btn_visibility_expected = cls.bts1_layout_bpm13_in_btn_visibility_expected
        mcr_ecubtcu_bpm13_instatus_init_2 = cls.mcr_ecubtcu_bpm13_instatus_init_2
        bts1_layout_bpm13_in_led_visibility_expected = cls.bts1_layout_bpm13_in_led_visibility_expected
        mcr_ecubtcu_bpm13_outstatus_init_1 = cls.mcr_ecubtcu_bpm13_outstatus_init_1
        bts1_layout_bpm13_out_led_visibility_expected = cls.bts1_layout_bpm13_out_led_visibility_expected
        mcr_ecubtcu_bpm13_outstatus_init_2 = cls.mcr_ecubtcu_bpm13_outstatus_init_2
        bts1_layout_bpm13_out_visibility_expected = cls.bts1_layout_bpm13_out_visibility_expected
        b6_visibility_expected = cls.b6_visibility_expected
        mcr_ecubtcu_bpm4_instatus_init_1 = cls.mcr_ecubtcu_bpm4_instatus_init_1
        bts1_layout_bpm4_in_visibility_expected = cls.bts1_layout_bpm4_in_visibility_expected
        bts1_layout_bpm4_out_btn_visibility_expected = cls.bts1_layout_bpm4_out_btn_visibility_expected
        bts1_layout_bpm4_in_btn_visibility_expected = cls.bts1_layout_bpm4_in_btn_visibility_expected
        mcr_ecubtcu_bpm4_instatus_init_2 = cls.mcr_ecubtcu_bpm4_instatus_init_2
        bts1_layout_bpm4_in_led_visibility_expected = cls.bts1_layout_bpm4_in_led_visibility_expected
        mcr_ecubtcu_bpm4_outstatus_init_1 = cls.mcr_ecubtcu_bpm4_outstatus_init_1
        bts1_layout_bpm4_out_led_visibility_expected = cls.bts1_layout_bpm4_out_led_visibility_expected
        mcr_ecubtcu_bpm4_outstatus_init_2 = cls.mcr_ecubtcu_bpm4_outstatus_init_2
        bts1_layout_bpm4_out_visibility_expected = cls.bts1_layout_bpm4_out_visibility_expected
        mcr_ecubtcu_bs3_instatus_init_1 = cls.mcr_ecubtcu_bs3_instatus_init_1
        bts1_layout_bs3_in_visibility_expected = cls.bts1_layout_bs3_in_visibility_expected
        bts1_layout_bss_in_btn_visibility_expected = cls.bts1_layout_bss_in_btn_visibility_expected
        mcr_ecubtcu_bs3_instatus_init_2 = cls.mcr_ecubtcu_bs3_instatus_init_2
        bts1_layout_bss_in_led_visibility_expected = cls.bts1_layout_bss_in_led_visibility_expected
        mcr_ecubtcu_bs3_outstatus_init_1 = cls.mcr_ecubtcu_bs3_outstatus_init_1
        bts1_layout_bss_out_led_visibility_expected = cls.bts1_layout_bss_out_led_visibility_expected
        mcr_ecubtcu_bs3_outstatus_init_2 = cls.mcr_ecubtcu_bs3_outstatus_init_2
        bts1_layout_bs3_out_visibility_expected = cls.bts1_layout_bs3_out_visibility_expected
        mcr_ecubtcu_bpm10_instatus_init_1 = cls.mcr_ecubtcu_bpm10_instatus_init_1
        bts1_layout_bpm10_in_visibility_expected = cls.bts1_layout_bpm10_in_visibility_expected
        bts1_layout_bpm10_out_btn_visibility_expected = cls.bts1_layout_bpm10_out_btn_visibility_expected
        bts1_layout_bpm10_in_btn_visibility_expected = cls.bts1_layout_bpm10_in_btn_visibility_expected
        mcr_ecubtcu_bpm10_instatus_init_2 = cls.mcr_ecubtcu_bpm10_instatus_init_2
        bts1_layout_bpm10_in_led_visibility_expected = cls.bts1_layout_bpm10_in_led_visibility_expected
        mcr_ecubtcu_bpm10_outstatus_init_1 = cls.mcr_ecubtcu_bpm10_outstatus_init_1
        bts1_layout_bpm10_out_led_visibility_expected = cls.bts1_layout_bpm10_out_led_visibility_expected
        mcr_ecubtcu_bpm10_outstatus_init_2 = cls.mcr_ecubtcu_bpm10_outstatus_init_2
        bts1_layout_bpm10_out_visibility_expected = cls.bts1_layout_bpm10_out_visibility_expected
        mcr_acu_valvegts1_opened_status_init_2 = cls.mcr_acu_valvegts1_opened_status_init_2
        bts1_layout_gantry1_valve_foreground_color_expected = cls.bts1_layout_gantry1_valve_foreground_color_expected
        mcr_acu_valvesl1_opened_status_init_1 = cls.mcr_acu_valvesl1_opened_status_init_1
        bts1_layout_sl1_valve_foreground_color_expected = cls.bts1_layout_sl1_valve_foreground_color_expected
        mcr_ecubtcu_piranigts1_mbarvacuum_init_4 = cls.mcr_ecubtcu_piranigts1_mbarvacuum_init_4
        bts1_layout_out_of_range_txt_visibility_expected = cls.bts1_layout_out_of_range_txt_visibility_expected
        mcr_ecubtcu_bs3_cfeedback_init_1 = cls.mcr_ecubtcu_bs3_cfeedback_init_1
        bts1_layout_bs3_nA1_txt_value_expected = cls.bts1_layout_bs3_nA1_txt_value_expected
        mcr_rtieecubtcu_bcm3_highdata_visibility_init_1 = cls.mcr_rtieecubtcu_bcm3_highdata_visibility_init_1
        bts1_layout_bs3_nA1_txt_visibility_expected = cls.bts1_layout_bs3_nA1_txt_visibility_expected
        mcr_ecubtcu_bs3_cfeedback_init_2 = cls.mcr_ecubtcu_bs3_cfeedback_init_2
        bts1_layout_bs3_nA_txt_value_expected = cls.bts1_layout_bs3_nA_txt_value_expected
        mcr_rtieecubtcu_bcm3_lowdata_visibility_init_1 = cls.mcr_rtieecubtcu_bcm3_lowdata_visibility_init_1
        bts1_layout_bs3_nA_txt_visibility_expected = cls.bts1_layout_bs3_nA_txt_visibility_expected
        bts1_layout_GTS1_layout_btn_visibility_expected = cls.bts1_layout_GTS1_layout_btn_visibility_expected
        bts1_layout_ess_layout_btn_visibility_expected = cls.bts1_layout_ess_layout_btn_visibility_expected
        bts1_layout_bts2_layout_btn_visibility_expected = cls.bts1_layout_bts2_layout_btn_visibility_expected
        mcr_scu_safety_bts1_interlocksstatus_init_1 = cls.mcr_scu_safety_bts1_interlocksstatus_init_1
        bts1_layout_safety_interlocks_btn_foreground_color_expected = cls.bts1_layout_safety_interlocks_btn_foreground_color_expected
        t12_visibility_expected = cls.t12_visibility_expected
        bts1_layout_bpm11_out_btn_visibility_expected = cls.bts1_layout_bpm11_out_btn_visibility_expected
        bts1_layout_bpm11_in_btn_visibility_expected = cls.bts1_layout_bpm11_in_btn_visibility_expected
        mcr_ecubtcu_bpm11_instatus_init_1 = cls.mcr_ecubtcu_bpm11_instatus_init_1
        bts1_layout_bpm11_in_led_visibility_expected = cls.bts1_layout_bpm11_in_led_visibility_expected
        mcr_ecubtcu_bpm11_outstatus_init_1 = cls.mcr_ecubtcu_bpm11_outstatus_init_1
        bts1_layout_bpm11_out_led_visibility_expected = cls.bts1_layout_bpm11_out_led_visibility_expected
        mcr_ecubtcu_bpm11_instatus_init_2 = cls.mcr_ecubtcu_bpm11_instatus_init_2
        bts1_layout_bpm11_in_visibility_expected = cls.bts1_layout_bpm11_in_visibility_expected
        mcr_ecubtcu_bpm11_outstatus_init_2 = cls.mcr_ecubtcu_bpm11_outstatus_init_2
        bts1_layout_bpm11_out_visibility_expected = cls.bts1_layout_bpm11_out_visibility_expected
        bts1_layout_SL1_close_btn_visibility_expected = cls.bts1_layout_SL1_close_btn_visibility_expected
        bts1_layout_SL1_open_btn_visibility_expected = cls.bts1_layout_SL1_open_btn_visibility_expected
        mcr_acu_valvesl1_opened_status_init_2 = cls.mcr_acu_valvesl1_opened_status_init_2
        bts1_layout_SL1_open_led_visibility_expected = cls.bts1_layout_SL1_open_led_visibility_expected
        mcr_acu_valvesl1_closed_status_init_1 = cls.mcr_acu_valvesl1_closed_status_init_1
        bts1_layout_SL1_close_led_visibility_expected = cls.bts1_layout_SL1_close_led_visibility_expected
        bts1_layout_hidden_obj_visibility_expected = cls.bts1_layout_hidden_obj_visibility_expected
        SC5B_visibility_expected = cls.SC5B_visibility_expected
        SC6B_visibility_expected = cls.SC6B_visibility_expected

        #set initial values
        set_mcr_ecubtcu_sstech_ps_status_1 = MsgTypeNumeric("mcr_ecubtcu_sstech_ps_status", mcr_ecubtcu_sstech_ps_status_init_1)
        set_mcr_ecubtcu_sstech_ps_status_2 = MsgTypeNumeric("mcr_ecubtcu_sstech_ps_status", mcr_ecubtcu_sstech_ps_status_init_2)
        set_mcr_ecubtcu_piranigts1_mbarvacuum_1 = MsgTypeNumeric("mcr_ecubtcu_piranigts1_mbarvacuum", mcr_ecubtcu_piranigts1_mbarvacuum_init_1)
        set_mcr_ecubtcu_piranigts1_mbarvacuum_2 = MsgTypeNumeric("mcr_ecubtcu_piranigts1_mbarvacuum", mcr_ecubtcu_piranigts1_mbarvacuum_init_2)
        set_mcr_ecubtcu_piranigts1_mbarvacuum_3 = MsgTypeNumeric("mcr_ecubtcu_piranigts1_mbarvacuum", mcr_ecubtcu_piranigts1_mbarvacuum_init_3)
        set_mcr_acu_vacuumbts1_status_1 = MsgTypeBoolean("mcr_acu_vacuumbts1_status", mcr_acu_vacuumbts1_status_init_1)
        set_mcr_acu_valvegts1_opened_status_1 = MsgTypeBoolean("mcr_acu_valvegts1_opened_status", mcr_acu_valvegts1_opened_status_init_1)
        set_mcr_acu_valvegts1_closed_status_1 = MsgTypeBoolean("mcr_acu_valvegts1_closed_status", mcr_acu_valvegts1_closed_status_init_1)
        set_mcr_acu_selectiong12_status_1 = MsgTypeBoolean("mcr_acu_selectiong12_status", mcr_acu_selectiong12_status_init_1)
        set_mcr_acu_selectiong12_status_2 = MsgTypeBoolean("mcr_acu_selectiong12_status", mcr_acu_selectiong12_status_init_2)
        set_mcr_ecubtcu_bpm13_instatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpm13_instatus", mcr_ecubtcu_bpm13_instatus_init_1)
        set_mcr_ecubtcu_bpm13_instatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpm13_instatus", mcr_ecubtcu_bpm13_instatus_init_2)
        set_mcr_ecubtcu_bpm13_outstatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpm13_outstatus", mcr_ecubtcu_bpm13_outstatus_init_1)
        set_mcr_ecubtcu_bpm13_outstatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpm13_outstatus", mcr_ecubtcu_bpm13_outstatus_init_2)
        set_mcr_ecubtcu_bpm4_instatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpm4_instatus", mcr_ecubtcu_bpm4_instatus_init_1)
        set_mcr_ecubtcu_bpm4_instatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpm4_instatus", mcr_ecubtcu_bpm4_instatus_init_2)
        set_mcr_ecubtcu_bpm4_outstatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpm4_outstatus", mcr_ecubtcu_bpm4_outstatus_init_1)
        set_mcr_ecubtcu_bpm4_outstatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpm4_outstatus", mcr_ecubtcu_bpm4_outstatus_init_2)
        set_mcr_ecubtcu_bs3_instatus_1 = MsgTypeBoolean("mcr_ecubtcu_bs3_instatus", mcr_ecubtcu_bs3_instatus_init_1)
        set_mcr_ecubtcu_bs3_instatus_2 = MsgTypeBoolean("mcr_ecubtcu_bs3_instatus", mcr_ecubtcu_bs3_instatus_init_2)
        set_mcr_ecubtcu_bs3_outstatus_1 = MsgTypeBoolean("mcr_ecubtcu_bs3_outstatus", mcr_ecubtcu_bs3_outstatus_init_1)
        set_mcr_ecubtcu_bs3_outstatus_2 = MsgTypeBoolean("mcr_ecubtcu_bs3_outstatus", mcr_ecubtcu_bs3_outstatus_init_2)
        set_mcr_ecubtcu_bpm10_instatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpm10_instatus", mcr_ecubtcu_bpm10_instatus_init_1)
        set_mcr_ecubtcu_bpm10_instatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpm10_instatus", mcr_ecubtcu_bpm10_instatus_init_2)
        set_mcr_ecubtcu_bpm10_outstatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpm10_outstatus", mcr_ecubtcu_bpm10_outstatus_init_1)
        set_mcr_ecubtcu_bpm10_outstatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpm10_outstatus", mcr_ecubtcu_bpm10_outstatus_init_2)
        set_mcr_acu_valvegts1_opened_status_2 = MsgTypeBoolean("mcr_acu_valvegts1_opened_status", mcr_acu_valvegts1_opened_status_init_2)
        set_mcr_acu_valvesl1_opened_status_1 = MsgTypeBoolean("mcr_acu_valvesl1_opened_status", mcr_acu_valvesl1_opened_status_init_1)
        set_mcr_ecubtcu_piranigts1_mbarvacuum_4 = MsgTypeNumeric("mcr_ecubtcu_piranigts1_mbarvacuum", mcr_ecubtcu_piranigts1_mbarvacuum_init_4)
        set_mcr_ecubtcu_bs3_cfeedback_1 = MsgTypeNumeric("mcr_ecubtcu_bs3_cfeedback", mcr_ecubtcu_bs3_cfeedback_init_1)
        set_mcr_rtieecubtcu_bcm3_highdata_visibility_1 = MsgTypeBoolean("mcr_rtieecubtcu_bcm3_highdata_visibility", mcr_rtieecubtcu_bcm3_highdata_visibility_init_1)
        set_mcr_ecubtcu_bs3_cfeedback_2 = MsgTypeNumeric("mcr_ecubtcu_bs3_cfeedback", mcr_ecubtcu_bs3_cfeedback_init_2)
        set_mcr_rtieecubtcu_bcm3_lowdata_visibility_1 = MsgTypeBoolean("mcr_rtieecubtcu_bcm3_lowdata_visibility", mcr_rtieecubtcu_bcm3_lowdata_visibility_init_1)
        set_mcr_scu_safety_bts1_interlocksstatus_1 = MsgTypeBoolean("mcr_scu_safety_bts1_interlocksstatus", mcr_scu_safety_bts1_interlocksstatus_init_1)
        set_mcr_ecubtcu_bpm11_instatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpm11_instatus", mcr_ecubtcu_bpm11_instatus_init_1)
        set_mcr_ecubtcu_bpm11_outstatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpm11_outstatus", mcr_ecubtcu_bpm11_outstatus_init_1)
        set_mcr_ecubtcu_bpm11_instatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpm11_instatus", mcr_ecubtcu_bpm11_instatus_init_2)
        set_mcr_ecubtcu_bpm11_outstatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpm11_outstatus", mcr_ecubtcu_bpm11_outstatus_init_2)
        set_mcr_acu_valvesl1_opened_status_2 = MsgTypeBoolean("mcr_acu_valvesl1_opened_status", mcr_acu_valvesl1_opened_status_init_2)
        set_mcr_acu_valvesl1_closed_status_1 = MsgTypeBoolean("mcr_acu_valvesl1_closed_status", mcr_acu_valvesl1_closed_status_init_1)

        #get values
        get_bts1_layout_bs3_out_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_bs3_out_btn")
        get_q27_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q27")
        get_q26_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q26")
        get_q30_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q30")
        get_b5_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "b5")
        get_q31_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q31")
        get_q25_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q25")
        get_bts1_layout_ps_canbus_status_txt_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "bts1_layout_ps_canbus_status_txt")
        get_bts1_layout_ps_canbus_status_ind_subobject_name = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "bts1_layout_ps_canbus_status_ind")
        get_q33_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q33")
        get_q34_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q34")
        get_q32_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q32")
        get_t11_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "t11")
        get_bts1_layout_mbar_number_txt_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "bts1_layout_mbar_number_txt")
        get_bts1_layout_mbar_number_txt_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_mbar_number_txt")
        get_bts1_layout_mbar_txt_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_mbar_txt")
        get_bts1_layout_pirani_gauge_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "bts1_layout_pirani_gauge")
        get_bts1_layout_gantry1_close_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_gantry1_close_btn")
        get_bts1_layout_gantry1_open_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_gantry1_open_btn")
        get_bts1_layout_gantry1_open_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_gantry1_open_led")
        get_bts1_layout_gantry1_close_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_gantry1_close_led")
        get_bts1_layout_gantry12_selection_txt_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "bts1_layout_gantry12_selection_txt")
        get_bts1_layout_gantry12_selection_ind_subobject_name = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "bts1_layout_gantry12_selection_ind")
        get_bts1_layout_bpm13_in_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_bpm13_in")
        get_bts1_layout_bpm13_out_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_bpm13_out_btn")
        get_bts1_layout_bpm13_in_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_bpm13_in_btn")
        get_bts1_layout_bpm13_in_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_bpm13_in_led")
        get_bts1_layout_bpm13_out_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_bpm13_out_led")
        get_bts1_layout_bpm13_out_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_bpm13_out")
        get_b6_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "b6")
        get_bts1_layout_bpm4_in_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_bpm4_in")
        get_bts1_layout_bpm4_out_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_bpm4_out_btn")
        get_bts1_layout_bpm4_in_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_bpm4_in_btn")
        get_bts1_layout_bpm4_in_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_bpm4_in_led")
        get_bts1_layout_bpm4_out_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_bpm4_out_led")
        get_bts1_layout_bpm4_out_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_bpm4_out")
        get_bts1_layout_bs3_in_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_bs3_in")
        get_bts1_layout_bss_in_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_bss_in_btn")
        get_bts1_layout_bss_in_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_bss_in_led")
        get_bts1_layout_bss_out_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_bss_out_led")
        get_bts1_layout_bs3_out_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_bs3_out")
        get_bts1_layout_bpm10_in_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_bpm10_in")
        get_bts1_layout_bpm10_out_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_bpm10_out_btn")
        get_bts1_layout_bpm10_in_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_bpm10_in_btn")
        get_bts1_layout_bpm10_in_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_bpm10_in_led")
        get_bts1_layout_bpm10_out_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_bpm10_out_led")
        get_bts1_layout_bpm10_out_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_bpm10_out")
        get_bts1_layout_gantry1_valve_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "bts1_layout_gantry1_valve")
        get_bts1_layout_sl1_valve_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "bts1_layout_sl1_valve")
        get_bts1_layout_out_of_range_txt_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_out_of_range_txt")
        get_bts1_layout_bs3_nA1_txt_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "bts1_layout_bs3_nA1_txt")
        get_bts1_layout_bs3_nA1_txt_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_bs3_nA1_txt")
        get_bts1_layout_bs3_nA_txt_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "bts1_layout_bs3_nA_txt")
        get_bts1_layout_bs3_nA_txt_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_bs3_nA_txt")
        get_bts1_layout_GTS1_layout_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_GTS1_layout_btn")
        get_bts1_layout_ess_layout_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_ess_layout_btn")
        get_bts1_layout_bts2_layout_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_bts2_layout_btn")
        get_bts1_layout_safety_interlocks_btn_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "bts1_layout_safety_interlocks_btn")
        get_t12_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "t12")
        get_bts1_layout_bpm11_out_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_bpm11_out_btn")
        get_bts1_layout_bpm11_in_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_bpm11_in_btn")
        get_bts1_layout_bpm11_in_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_bpm11_in_led")
        get_bts1_layout_bpm11_out_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_bpm11_out_led")
        get_bts1_layout_bpm11_in_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_bpm11_in")
        get_bts1_layout_bpm11_out_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_bpm11_out")
        get_bts1_layout_SL1_close_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_SL1_close_btn")
        get_bts1_layout_SL1_open_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_SL1_open_btn")
        get_bts1_layout_SL1_open_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_SL1_open_led")
        get_bts1_layout_SL1_close_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_SL1_close_led")
        get_bts1_layout_hidden_obj_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_hidden_obj")
        get_SC5B_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "SC5B")
        get_SC6B_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "SC6B")

        #validate
        validate_bts1_layout_bs3_out_btn_visibility = MsgTypeString("bts1_layout_bs3_out_btn:TMMI_MCR_IS_VISIBLE", value=bts1_layout_bs3_out_btn_visibility_expected)
        validate_q27_visibility = MsgTypeString("q27:TMMI_MCR_IS_VISIBLE", value=q27_visibility_expected)
        validate_q26_visibility = MsgTypeString("q26:TMMI_MCR_IS_VISIBLE", value=q26_visibility_expected)
        validate_q30_visibility = MsgTypeString("q30:TMMI_MCR_IS_VISIBLE", value=q30_visibility_expected)
        validate_b5_visibility = MsgTypeString("b5:TMMI_MCR_IS_VISIBLE", value=b5_visibility_expected)
        validate_q31_visibility = MsgTypeString("q31:TMMI_MCR_IS_VISIBLE", value=q31_visibility_expected)
        validate_q25_visibility = MsgTypeString("q25:TMMI_MCR_IS_VISIBLE", value=q25_visibility_expected)
        validate_bts1_layout_ps_canbus_status_txt_foreground_color = MsgTypeString("bts1_layout_ps_canbus_status_txt:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=bts1_layout_ps_canbus_status_txt_foreground_color_expected)
        validate_bts1_layout_ps_canbus_status_ind_subobject_name = MsgTypeString("bts1_layout_ps_canbus_status_ind:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=bts1_layout_ps_canbus_status_ind_subobject_name_expected)
        validate_q33_visibility = MsgTypeString("q33:TMMI_MCR_IS_VISIBLE", value=q33_visibility_expected)
        validate_q34_visibility = MsgTypeString("q34:TMMI_MCR_IS_VISIBLE", value=q34_visibility_expected)
        validate_q32_visibility = MsgTypeString("q32:TMMI_MCR_IS_VISIBLE", value=q32_visibility_expected)
        validate_t11_visibility = MsgTypeString("t11:TMMI_MCR_IS_VISIBLE", value=t11_visibility_expected)
        validate_bts1_layout_mbar_number_txt_value = MsgTypeNumeric("bts1_layout_mbar_number_txt:TMMI_MCR_OBJECT_GET_VALUE", value=bts1_layout_mbar_number_txt_value_expected)
        validate_bts1_layout_mbar_number_txt_visibility = MsgTypeString("bts1_layout_mbar_number_txt:TMMI_MCR_IS_VISIBLE", value=bts1_layout_mbar_number_txt_visibility_expected)
        validate_bts1_layout_mbar_txt_visibility = MsgTypeString("bts1_layout_mbar_txt:TMMI_MCR_IS_VISIBLE", value=bts1_layout_mbar_txt_visibility_expected)
        validate_bts1_layout_pirani_gauge_foreground_color = MsgTypeString("bts1_layout_pirani_gauge:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=bts1_layout_pirani_gauge_foreground_color_expected)
        validate_bts1_layout_gantry1_close_btn_visibility = MsgTypeString("bts1_layout_gantry1_close_btn:TMMI_MCR_IS_VISIBLE", value=bts1_layout_gantry1_close_btn_visibility_expected)
        validate_bts1_layout_gantry1_open_btn_visibility = MsgTypeString("bts1_layout_gantry1_open_btn:TMMI_MCR_IS_VISIBLE", value=bts1_layout_gantry1_open_btn_visibility_expected)
        validate_bts1_layout_gantry1_open_led_visibility = MsgTypeString("bts1_layout_gantry1_open_led:TMMI_MCR_IS_VISIBLE", value=bts1_layout_gantry1_open_led_visibility_expected)
        validate_bts1_layout_gantry1_close_led_visibility = MsgTypeString("bts1_layout_gantry1_close_led:TMMI_MCR_IS_VISIBLE", value=bts1_layout_gantry1_close_led_visibility_expected)
        validate_bts1_layout_gantry12_selection_txt_foreground_color = MsgTypeString("bts1_layout_gantry12_selection_txt:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=bts1_layout_gantry12_selection_txt_foreground_color_expected)
        validate_bts1_layout_gantry12_selection_ind_subobject_name = MsgTypeString("bts1_layout_gantry12_selection_ind:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=bts1_layout_gantry12_selection_ind_subobject_name_expected)
        validate_bts1_layout_bpm13_in_visibility = MsgTypeString("bts1_layout_bpm13_in:TMMI_MCR_IS_VISIBLE", value=bts1_layout_bpm13_in_visibility_expected)
        validate_bts1_layout_bpm13_out_btn_visibility = MsgTypeString("bts1_layout_bpm13_out_btn:TMMI_MCR_IS_VISIBLE", value=bts1_layout_bpm13_out_btn_visibility_expected)
        validate_bts1_layout_bpm13_in_btn_visibility = MsgTypeString("bts1_layout_bpm13_in_btn:TMMI_MCR_IS_VISIBLE", value=bts1_layout_bpm13_in_btn_visibility_expected)
        validate_bts1_layout_bpm13_in_led_visibility = MsgTypeString("bts1_layout_bpm13_in_led:TMMI_MCR_IS_VISIBLE", value=bts1_layout_bpm13_in_led_visibility_expected)
        validate_bts1_layout_bpm13_out_led_visibility = MsgTypeString("bts1_layout_bpm13_out_led:TMMI_MCR_IS_VISIBLE", value=bts1_layout_bpm13_out_led_visibility_expected)
        validate_bts1_layout_bpm13_out_visibility = MsgTypeString("bts1_layout_bpm13_out:TMMI_MCR_IS_VISIBLE", value=bts1_layout_bpm13_out_visibility_expected)
        validate_b6_visibility = MsgTypeString("b6:TMMI_MCR_IS_VISIBLE", value=b6_visibility_expected)
        validate_bts1_layout_bpm4_in_visibility = MsgTypeString("bts1_layout_bpm4_in:TMMI_MCR_IS_VISIBLE", value=bts1_layout_bpm4_in_visibility_expected)
        validate_bts1_layout_bpm4_out_btn_visibility = MsgTypeString("bts1_layout_bpm4_out_btn:TMMI_MCR_IS_VISIBLE", value=bts1_layout_bpm4_out_btn_visibility_expected)
        validate_bts1_layout_bpm4_in_btn_visibility = MsgTypeString("bts1_layout_bpm4_in_btn:TMMI_MCR_IS_VISIBLE", value=bts1_layout_bpm4_in_btn_visibility_expected)
        validate_bts1_layout_bpm4_in_led_visibility = MsgTypeString("bts1_layout_bpm4_in_led:TMMI_MCR_IS_VISIBLE", value=bts1_layout_bpm4_in_led_visibility_expected)
        validate_bts1_layout_bpm4_out_led_visibility = MsgTypeString("bts1_layout_bpm4_out_led:TMMI_MCR_IS_VISIBLE", value=bts1_layout_bpm4_out_led_visibility_expected)
        validate_bts1_layout_bpm4_out_visibility = MsgTypeString("bts1_layout_bpm4_out:TMMI_MCR_IS_VISIBLE", value=bts1_layout_bpm4_out_visibility_expected)
        validate_bts1_layout_bs3_in_visibility = MsgTypeString("bts1_layout_bs3_in:TMMI_MCR_IS_VISIBLE", value=bts1_layout_bs3_in_visibility_expected)
        validate_bts1_layout_bss_in_btn_visibility = MsgTypeString("bts1_layout_bss_in_btn:TMMI_MCR_IS_VISIBLE", value=bts1_layout_bss_in_btn_visibility_expected)
        validate_bts1_layout_bss_in_led_visibility = MsgTypeString("bts1_layout_bss_in_led:TMMI_MCR_IS_VISIBLE", value=bts1_layout_bss_in_led_visibility_expected)
        validate_bts1_layout_bss_out_led_visibility = MsgTypeString("bts1_layout_bss_out_led:TMMI_MCR_IS_VISIBLE", value=bts1_layout_bss_out_led_visibility_expected)
        validate_bts1_layout_bs3_out_visibility = MsgTypeString("bts1_layout_bs3_out:TMMI_MCR_IS_VISIBLE", value=bts1_layout_bs3_out_visibility_expected)
        validate_bts1_layout_bpm10_in_visibility = MsgTypeString("bts1_layout_bpm10_in:TMMI_MCR_IS_VISIBLE", value=bts1_layout_bpm10_in_visibility_expected)
        validate_bts1_layout_bpm10_out_btn_visibility = MsgTypeString("bts1_layout_bpm10_out_btn:TMMI_MCR_IS_VISIBLE", value=bts1_layout_bpm10_out_btn_visibility_expected)
        validate_bts1_layout_bpm10_in_btn_visibility = MsgTypeString("bts1_layout_bpm10_in_btn:TMMI_MCR_IS_VISIBLE", value=bts1_layout_bpm10_in_btn_visibility_expected)
        validate_bts1_layout_bpm10_in_led_visibility = MsgTypeString("bts1_layout_bpm10_in_led:TMMI_MCR_IS_VISIBLE", value=bts1_layout_bpm10_in_led_visibility_expected)
        validate_bts1_layout_bpm10_out_led_visibility = MsgTypeString("bts1_layout_bpm10_out_led:TMMI_MCR_IS_VISIBLE", value=bts1_layout_bpm10_out_led_visibility_expected)
        validate_bts1_layout_bpm10_out_visibility = MsgTypeString("bts1_layout_bpm10_out:TMMI_MCR_IS_VISIBLE", value=bts1_layout_bpm10_out_visibility_expected)
        validate_bts1_layout_gantry1_valve_foreground_color = MsgTypeString("bts1_layout_gantry1_valve:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=bts1_layout_gantry1_valve_foreground_color_expected)
        validate_bts1_layout_sl1_valve_foreground_color = MsgTypeString("bts1_layout_sl1_valve:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=bts1_layout_sl1_valve_foreground_color_expected)
        validate_bts1_layout_out_of_range_txt_visibility = MsgTypeString("bts1_layout_out_of_range_txt:TMMI_MCR_IS_VISIBLE", value=bts1_layout_out_of_range_txt_visibility_expected)
        validate_bts1_layout_bs3_nA1_txt_value = MsgTypeNumeric("bts1_layout_bs3_nA1_txt:TMMI_MCR_OBJECT_GET_VALUE", value=bts1_layout_bs3_nA1_txt_value_expected)
        validate_bts1_layout_bs3_nA1_txt_visibility = MsgTypeString("bts1_layout_bs3_nA1_txt:TMMI_MCR_IS_VISIBLE", value=bts1_layout_bs3_nA1_txt_visibility_expected)
        validate_bts1_layout_bs3_nA_txt_value = MsgTypeNumeric("bts1_layout_bs3_nA_txt:TMMI_MCR_OBJECT_GET_VALUE", value=bts1_layout_bs3_nA_txt_value_expected)
        validate_bts1_layout_bs3_nA_txt_visibility = MsgTypeString("bts1_layout_bs3_nA_txt:TMMI_MCR_IS_VISIBLE", value=bts1_layout_bs3_nA_txt_visibility_expected)
        validate_bts1_layout_GTS1_layout_btn_visibility = MsgTypeString("bts1_layout_GTS1_layout_btn:TMMI_MCR_IS_VISIBLE", value=bts1_layout_GTS1_layout_btn_visibility_expected)
        validate_bts1_layout_ess_layout_btn_visibility = MsgTypeString("bts1_layout_ess_layout_btn:TMMI_MCR_IS_VISIBLE", value=bts1_layout_ess_layout_btn_visibility_expected)
        validate_bts1_layout_bts2_layout_btn_visibility = MsgTypeString("bts1_layout_bts2_layout_btn:TMMI_MCR_IS_VISIBLE", value=bts1_layout_bts2_layout_btn_visibility_expected)
        validate_bts1_layout_safety_interlocks_btn_foreground_color = MsgTypeString("bts1_layout_safety_interlocks_btn:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=bts1_layout_safety_interlocks_btn_foreground_color_expected)
        validate_t12_visibility = MsgTypeString("t12:TMMI_MCR_IS_VISIBLE", value=t12_visibility_expected)
        validate_bts1_layout_bpm11_out_btn_visibility = MsgTypeString("bts1_layout_bpm11_out_btn:TMMI_MCR_IS_VISIBLE", value=bts1_layout_bpm11_out_btn_visibility_expected)
        validate_bts1_layout_bpm11_in_btn_visibility = MsgTypeString("bts1_layout_bpm11_in_btn:TMMI_MCR_IS_VISIBLE", value=bts1_layout_bpm11_in_btn_visibility_expected)
        validate_bts1_layout_bpm11_in_led_visibility = MsgTypeString("bts1_layout_bpm11_in_led:TMMI_MCR_IS_VISIBLE", value=bts1_layout_bpm11_in_led_visibility_expected)
        validate_bts1_layout_bpm11_out_led_visibility = MsgTypeString("bts1_layout_bpm11_out_led:TMMI_MCR_IS_VISIBLE", value=bts1_layout_bpm11_out_led_visibility_expected)
        validate_bts1_layout_bpm11_in_visibility = MsgTypeString("bts1_layout_bpm11_in:TMMI_MCR_IS_VISIBLE", value=bts1_layout_bpm11_in_visibility_expected)
        validate_bts1_layout_bpm11_out_visibility = MsgTypeString("bts1_layout_bpm11_out:TMMI_MCR_IS_VISIBLE", value=bts1_layout_bpm11_out_visibility_expected)
        validate_bts1_layout_SL1_close_btn_visibility = MsgTypeString("bts1_layout_SL1_close_btn:TMMI_MCR_IS_VISIBLE", value=bts1_layout_SL1_close_btn_visibility_expected)
        validate_bts1_layout_SL1_open_btn_visibility = MsgTypeString("bts1_layout_SL1_open_btn:TMMI_MCR_IS_VISIBLE", value=bts1_layout_SL1_open_btn_visibility_expected)
        validate_bts1_layout_SL1_open_led_visibility = MsgTypeString("bts1_layout_SL1_open_led:TMMI_MCR_IS_VISIBLE", value=bts1_layout_SL1_open_led_visibility_expected)
        validate_bts1_layout_SL1_close_led_visibility = MsgTypeString("bts1_layout_SL1_close_led:TMMI_MCR_IS_VISIBLE", value=bts1_layout_SL1_close_led_visibility_expected)
        validate_bts1_layout_hidden_obj_visibility = MsgTypeString("bts1_layout_hidden_obj:TMMI_MCR_IS_VISIBLE", value=bts1_layout_hidden_obj_visibility_expected)
        validate_SC5B_visibility = MsgTypeString("SC5B:TMMI_MCR_IS_VISIBLE", value=SC5B_visibility_expected)
        validate_SC6B_visibility = MsgTypeString("SC6B:TMMI_MCR_IS_VISIBLE", value=SC6B_visibility_expected)

        info_exchange = [
                        InformationSet("get bts1_layout_bs3_out_btn visibility", "thriver", "mcrhci", get_bts1_layout_bs3_out_btn_visibility),
                        InformationSet("validate bts1_layout_bs3_out_btn visibility = " + str(bts1_layout_bs3_out_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_bs3_out_btn_visibility),
                        InformationSet("get q27 visibility", "thriver", "mcrhci", get_q27_visibility),
                        InformationSet("validate q27 visibility = " + str(q27_visibility_expected), "mcrhci", "hcitracer", validate_q27_visibility),
                        InformationSet("get q26 visibility", "thriver", "mcrhci", get_q26_visibility),
                        InformationSet("validate q26 visibility = " + str(q26_visibility_expected), "mcrhci", "hcitracer", validate_q26_visibility),
                        InformationSet("get q30 visibility", "thriver", "mcrhci", get_q30_visibility),
                        InformationSet("validate q30 visibility = " + str(q30_visibility_expected), "mcrhci", "hcitracer", validate_q30_visibility),
                        InformationSet("get b5 visibility", "thriver", "mcrhci", get_b5_visibility),
                        InformationSet("validate b5 visibility = " + str(b5_visibility_expected), "mcrhci", "hcitracer", validate_b5_visibility),
                        InformationSet("get q31 visibility", "thriver", "mcrhci", get_q31_visibility),
                        InformationSet("validate q31 visibility = " + str(q31_visibility_expected), "mcrhci", "hcitracer", validate_q31_visibility),
                        InformationSet("get q25 visibility", "thriver", "mcrhci", get_q25_visibility),
                        InformationSet("validate q25 visibility = " + str(q25_visibility_expected), "mcrhci", "hcitracer", validate_q25_visibility),
                        InformationSet("set mcr_ecubtcu_sstech_ps_status = "+ str(mcr_ecubtcu_sstech_ps_status_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_sstech_ps_status_1),
                        InformationSet("get bts1_layout_ps_canbus_status_txt foreground_color", "thriver", "mcrhci", get_bts1_layout_ps_canbus_status_txt_foreground_color),
                        InformationSet("validate bts1_layout_ps_canbus_status_txt foreground_color = " + str(bts1_layout_ps_canbus_status_txt_foreground_color_expected), "mcrhci", "hcitracer", validate_bts1_layout_ps_canbus_status_txt_foreground_color),
                        InformationSet("set mcr_ecubtcu_sstech_ps_status = "+ str(mcr_ecubtcu_sstech_ps_status_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_sstech_ps_status_2),
                        InformationSet("get bts1_layout_ps_canbus_status_ind subobject_name", "thriver", "mcrhci", get_bts1_layout_ps_canbus_status_ind_subobject_name),
                        InformationSet("validate bts1_layout_ps_canbus_status_ind subobject_name = " + str(bts1_layout_ps_canbus_status_ind_subobject_name_expected), "mcrhci", "hcitracer", validate_bts1_layout_ps_canbus_status_ind_subobject_name),
                        InformationSet("get q33 visibility", "thriver", "mcrhci", get_q33_visibility),
                        InformationSet("validate q33 visibility = " + str(q33_visibility_expected), "mcrhci", "hcitracer", validate_q33_visibility),
                        InformationSet("get q34 visibility", "thriver", "mcrhci", get_q34_visibility),
                        InformationSet("validate q34 visibility = " + str(q34_visibility_expected), "mcrhci", "hcitracer", validate_q34_visibility),
                        InformationSet("get q32 visibility", "thriver", "mcrhci", get_q32_visibility),
                        InformationSet("validate q32 visibility = " + str(q32_visibility_expected), "mcrhci", "hcitracer", validate_q32_visibility),
                        InformationSet("get t11 visibility", "thriver", "mcrhci", get_t11_visibility),
                        InformationSet("validate t11 visibility = " + str(t11_visibility_expected), "mcrhci", "hcitracer", validate_t11_visibility),
                        InformationSet("set mcr_ecubtcu_piranigts1_mbarvacuum = "+ str(mcr_ecubtcu_piranigts1_mbarvacuum_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_piranigts1_mbarvacuum_1),
                        InformationSet("get bts1_layout_mbar_number_txt value", "thriver", "mcrhci", get_bts1_layout_mbar_number_txt_value),
                        InformationSet("validate bts1_layout_mbar_number_txt value = " + str(bts1_layout_mbar_number_txt_value_expected), "mcrhci", "hcitracer", validate_bts1_layout_mbar_number_txt_value),
                        InformationSet("set mcr_ecubtcu_piranigts1_mbarvacuum = "+ str(mcr_ecubtcu_piranigts1_mbarvacuum_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_piranigts1_mbarvacuum_2),
                        InformationSet("get bts1_layout_mbar_number_txt visibility", "thriver", "mcrhci", get_bts1_layout_mbar_number_txt_visibility),
                        InformationSet("validate bts1_layout_mbar_number_txt visibility = " + str(bts1_layout_mbar_number_txt_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_mbar_number_txt_visibility),
                        InformationSet("set mcr_ecubtcu_piranigts1_mbarvacuum = "+ str(mcr_ecubtcu_piranigts1_mbarvacuum_init_3), "thriver", "mcrhci", set_mcr_ecubtcu_piranigts1_mbarvacuum_3),
                        InformationSet("get bts1_layout_mbar_txt visibility", "thriver", "mcrhci", get_bts1_layout_mbar_txt_visibility),
                        InformationSet("validate bts1_layout_mbar_txt visibility = " + str(bts1_layout_mbar_txt_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_mbar_txt_visibility),
                        InformationSet("set mcr_acu_vacuumbts1_status = "+ str(mcr_acu_vacuumbts1_status_init_1), "thriver", "mcrhci", set_mcr_acu_vacuumbts1_status_1),
                        InformationSet("get bts1_layout_pirani_gauge foreground_color", "thriver", "mcrhci", get_bts1_layout_pirani_gauge_foreground_color),
                        InformationSet("validate bts1_layout_pirani_gauge foreground_color = " + str(bts1_layout_pirani_gauge_foreground_color_expected), "mcrhci", "hcitracer", validate_bts1_layout_pirani_gauge_foreground_color),
                        InformationSet("get bts1_layout_gantry1_close_btn visibility", "thriver", "mcrhci", get_bts1_layout_gantry1_close_btn_visibility),
                        InformationSet("validate bts1_layout_gantry1_close_btn visibility = " + str(bts1_layout_gantry1_close_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_gantry1_close_btn_visibility),
                        InformationSet("get bts1_layout_gantry1_open_btn visibility", "thriver", "mcrhci", get_bts1_layout_gantry1_open_btn_visibility),
                        InformationSet("validate bts1_layout_gantry1_open_btn visibility = " + str(bts1_layout_gantry1_open_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_gantry1_open_btn_visibility),
                        InformationSet("set mcr_acu_valvegts1_opened_status = "+ str(mcr_acu_valvegts1_opened_status_init_1), "thriver", "mcrhci", set_mcr_acu_valvegts1_opened_status_1),
                        InformationSet("get bts1_layout_gantry1_open_led visibility", "thriver", "mcrhci", get_bts1_layout_gantry1_open_led_visibility),
                        InformationSet("validate bts1_layout_gantry1_open_led visibility = " + str(bts1_layout_gantry1_open_led_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_gantry1_open_led_visibility),
                        InformationSet("set mcr_acu_valvegts1_closed_status = "+ str(mcr_acu_valvegts1_closed_status_init_1), "thriver", "mcrhci", set_mcr_acu_valvegts1_closed_status_1),
                        InformationSet("get bts1_layout_gantry1_close_led visibility", "thriver", "mcrhci", get_bts1_layout_gantry1_close_led_visibility),
                        InformationSet("validate bts1_layout_gantry1_close_led visibility = " + str(bts1_layout_gantry1_close_led_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_gantry1_close_led_visibility),
                        InformationSet("set mcr_acu_selectiong12_status = "+ str(mcr_acu_selectiong12_status_init_1), "thriver", "mcrhci", set_mcr_acu_selectiong12_status_1),
                        InformationSet("get bts1_layout_gantry12_selection_txt foreground_color", "thriver", "mcrhci", get_bts1_layout_gantry12_selection_txt_foreground_color),
                        InformationSet("validate bts1_layout_gantry12_selection_txt foreground_color = " + str(bts1_layout_gantry12_selection_txt_foreground_color_expected), "mcrhci", "hcitracer", validate_bts1_layout_gantry12_selection_txt_foreground_color),
                        InformationSet("set mcr_acu_selectiong12_status = "+ str(mcr_acu_selectiong12_status_init_2), "thriver", "mcrhci", set_mcr_acu_selectiong12_status_2),
                        InformationSet("get bts1_layout_gantry12_selection_ind subobject_name", "thriver", "mcrhci", get_bts1_layout_gantry12_selection_ind_subobject_name),
                        InformationSet("validate bts1_layout_gantry12_selection_ind subobject_name = " + str(bts1_layout_gantry12_selection_ind_subobject_name_expected), "mcrhci", "hcitracer", validate_bts1_layout_gantry12_selection_ind_subobject_name),
                        InformationSet("set mcr_ecubtcu_bpm13_instatus = "+ str(mcr_ecubtcu_bpm13_instatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpm13_instatus_1),
                        InformationSet("get bts1_layout_bpm13_in visibility", "thriver", "mcrhci", get_bts1_layout_bpm13_in_visibility),
                        InformationSet("validate bts1_layout_bpm13_in visibility = " + str(bts1_layout_bpm13_in_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_bpm13_in_visibility),
                        InformationSet("get bts1_layout_bpm13_out_btn visibility", "thriver", "mcrhci", get_bts1_layout_bpm13_out_btn_visibility),
                        InformationSet("validate bts1_layout_bpm13_out_btn visibility = " + str(bts1_layout_bpm13_out_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_bpm13_out_btn_visibility),
                        InformationSet("get bts1_layout_bpm13_in_btn visibility", "thriver", "mcrhci", get_bts1_layout_bpm13_in_btn_visibility),
                        InformationSet("validate bts1_layout_bpm13_in_btn visibility = " + str(bts1_layout_bpm13_in_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_bpm13_in_btn_visibility),
                        InformationSet("set mcr_ecubtcu_bpm13_instatus = "+ str(mcr_ecubtcu_bpm13_instatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpm13_instatus_2),
                        InformationSet("get bts1_layout_bpm13_in_led visibility", "thriver", "mcrhci", get_bts1_layout_bpm13_in_led_visibility),
                        InformationSet("validate bts1_layout_bpm13_in_led visibility = " + str(bts1_layout_bpm13_in_led_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_bpm13_in_led_visibility),
                        InformationSet("set mcr_ecubtcu_bpm13_outstatus = "+ str(mcr_ecubtcu_bpm13_outstatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpm13_outstatus_1),
                        InformationSet("get bts1_layout_bpm13_out_led visibility", "thriver", "mcrhci", get_bts1_layout_bpm13_out_led_visibility),
                        InformationSet("validate bts1_layout_bpm13_out_led visibility = " + str(bts1_layout_bpm13_out_led_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_bpm13_out_led_visibility),
                        InformationSet("set mcr_ecubtcu_bpm13_outstatus = "+ str(mcr_ecubtcu_bpm13_outstatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpm13_outstatus_2),
                        InformationSet("get bts1_layout_bpm13_out visibility", "thriver", "mcrhci", get_bts1_layout_bpm13_out_visibility),
                        InformationSet("validate bts1_layout_bpm13_out visibility = " + str(bts1_layout_bpm13_out_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_bpm13_out_visibility),
                        InformationSet("get b6 visibility", "thriver", "mcrhci", get_b6_visibility),
                        InformationSet("validate b6 visibility = " + str(b6_visibility_expected), "mcrhci", "hcitracer", validate_b6_visibility),
                        InformationSet("set mcr_ecubtcu_bpm4_instatus = "+ str(mcr_ecubtcu_bpm4_instatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpm4_instatus_1),
                        InformationSet("get bts1_layout_bpm4_in visibility", "thriver", "mcrhci", get_bts1_layout_bpm4_in_visibility),
                        InformationSet("validate bts1_layout_bpm4_in visibility = " + str(bts1_layout_bpm4_in_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_bpm4_in_visibility),
                        InformationSet("get bts1_layout_bpm4_out_btn visibility", "thriver", "mcrhci", get_bts1_layout_bpm4_out_btn_visibility),
                        InformationSet("validate bts1_layout_bpm4_out_btn visibility = " + str(bts1_layout_bpm4_out_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_bpm4_out_btn_visibility),
                        InformationSet("get bts1_layout_bpm4_in_btn visibility", "thriver", "mcrhci", get_bts1_layout_bpm4_in_btn_visibility),
                        InformationSet("validate bts1_layout_bpm4_in_btn visibility = " + str(bts1_layout_bpm4_in_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_bpm4_in_btn_visibility),
                        InformationSet("set mcr_ecubtcu_bpm4_instatus = "+ str(mcr_ecubtcu_bpm4_instatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpm4_instatus_2),
                        InformationSet("get bts1_layout_bpm4_in_led visibility", "thriver", "mcrhci", get_bts1_layout_bpm4_in_led_visibility),
                        InformationSet("validate bts1_layout_bpm4_in_led visibility = " + str(bts1_layout_bpm4_in_led_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_bpm4_in_led_visibility),
                        InformationSet("set mcr_ecubtcu_bpm4_outstatus = "+ str(mcr_ecubtcu_bpm4_outstatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpm4_outstatus_1),
                        InformationSet("get bts1_layout_bpm4_out_led visibility", "thriver", "mcrhci", get_bts1_layout_bpm4_out_led_visibility),
                        InformationSet("validate bts1_layout_bpm4_out_led visibility = " + str(bts1_layout_bpm4_out_led_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_bpm4_out_led_visibility),
                        InformationSet("set mcr_ecubtcu_bpm4_outstatus = "+ str(mcr_ecubtcu_bpm4_outstatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpm4_outstatus_2),
                        InformationSet("get bts1_layout_bpm4_out visibility", "thriver", "mcrhci", get_bts1_layout_bpm4_out_visibility),
                        InformationSet("validate bts1_layout_bpm4_out visibility = " + str(bts1_layout_bpm4_out_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_bpm4_out_visibility),
                        InformationSet("set mcr_ecubtcu_bs3_instatus = "+ str(mcr_ecubtcu_bs3_instatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bs3_instatus_1),
                        InformationSet("get bts1_layout_bs3_in visibility", "thriver", "mcrhci", get_bts1_layout_bs3_in_visibility),
                        InformationSet("validate bts1_layout_bs3_in visibility = " + str(bts1_layout_bs3_in_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_bs3_in_visibility),
                        InformationSet("get bts1_layout_bss_in_btn visibility", "thriver", "mcrhci", get_bts1_layout_bss_in_btn_visibility),
                        InformationSet("validate bts1_layout_bss_in_btn visibility = " + str(bts1_layout_bss_in_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_bss_in_btn_visibility),
                        InformationSet("set mcr_ecubtcu_bs3_instatus = "+ str(mcr_ecubtcu_bs3_instatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bs3_instatus_2),
                        InformationSet("get bts1_layout_bss_in_led visibility", "thriver", "mcrhci", get_bts1_layout_bss_in_led_visibility),
                        InformationSet("validate bts1_layout_bss_in_led visibility = " + str(bts1_layout_bss_in_led_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_bss_in_led_visibility),
                        InformationSet("set mcr_ecubtcu_bs3_outstatus = "+ str(mcr_ecubtcu_bs3_outstatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bs3_outstatus_1),
                        InformationSet("get bts1_layout_bss_out_led visibility", "thriver", "mcrhci", get_bts1_layout_bss_out_led_visibility),
                        InformationSet("validate bts1_layout_bss_out_led visibility = " + str(bts1_layout_bss_out_led_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_bss_out_led_visibility),
                        InformationSet("set mcr_ecubtcu_bs3_outstatus = "+ str(mcr_ecubtcu_bs3_outstatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bs3_outstatus_2),
                        InformationSet("get bts1_layout_bs3_out visibility", "thriver", "mcrhci", get_bts1_layout_bs3_out_visibility),
                        InformationSet("validate bts1_layout_bs3_out visibility = " + str(bts1_layout_bs3_out_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_bs3_out_visibility),
                        InformationSet("set mcr_ecubtcu_bpm10_instatus = "+ str(mcr_ecubtcu_bpm10_instatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpm10_instatus_1),
                        InformationSet("get bts1_layout_bpm10_in visibility", "thriver", "mcrhci", get_bts1_layout_bpm10_in_visibility),
                        InformationSet("validate bts1_layout_bpm10_in visibility = " + str(bts1_layout_bpm10_in_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_bpm10_in_visibility),
                        InformationSet("get bts1_layout_bpm10_out_btn visibility", "thriver", "mcrhci", get_bts1_layout_bpm10_out_btn_visibility),
                        InformationSet("validate bts1_layout_bpm10_out_btn visibility = " + str(bts1_layout_bpm10_out_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_bpm10_out_btn_visibility),
                        InformationSet("get bts1_layout_bpm10_in_btn visibility", "thriver", "mcrhci", get_bts1_layout_bpm10_in_btn_visibility),
                        InformationSet("validate bts1_layout_bpm10_in_btn visibility = " + str(bts1_layout_bpm10_in_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_bpm10_in_btn_visibility),
                        InformationSet("set mcr_ecubtcu_bpm10_instatus = "+ str(mcr_ecubtcu_bpm10_instatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpm10_instatus_2),
                        InformationSet("get bts1_layout_bpm10_in_led visibility", "thriver", "mcrhci", get_bts1_layout_bpm10_in_led_visibility),
                        InformationSet("validate bts1_layout_bpm10_in_led visibility = " + str(bts1_layout_bpm10_in_led_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_bpm10_in_led_visibility),
                        InformationSet("set mcr_ecubtcu_bpm10_outstatus = "+ str(mcr_ecubtcu_bpm10_outstatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpm10_outstatus_1),
                        InformationSet("get bts1_layout_bpm10_out_led visibility", "thriver", "mcrhci", get_bts1_layout_bpm10_out_led_visibility),
                        InformationSet("validate bts1_layout_bpm10_out_led visibility = " + str(bts1_layout_bpm10_out_led_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_bpm10_out_led_visibility),
                        InformationSet("set mcr_ecubtcu_bpm10_outstatus = "+ str(mcr_ecubtcu_bpm10_outstatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpm10_outstatus_2),
                        InformationSet("get bts1_layout_bpm10_out visibility", "thriver", "mcrhci", get_bts1_layout_bpm10_out_visibility),
                        InformationSet("validate bts1_layout_bpm10_out visibility = " + str(bts1_layout_bpm10_out_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_bpm10_out_visibility),
                        InformationSet("set mcr_acu_valvegts1_opened_status = "+ str(mcr_acu_valvegts1_opened_status_init_2), "thriver", "mcrhci", set_mcr_acu_valvegts1_opened_status_2),
                        InformationSet("get bts1_layout_gantry1_valve foreground_color", "thriver", "mcrhci", get_bts1_layout_gantry1_valve_foreground_color),
                        InformationSet("validate bts1_layout_gantry1_valve foreground_color = " + str(bts1_layout_gantry1_valve_foreground_color_expected), "mcrhci", "hcitracer", validate_bts1_layout_gantry1_valve_foreground_color),
                        InformationSet("set mcr_acu_valvesl1_opened_status = "+ str(mcr_acu_valvesl1_opened_status_init_1), "thriver", "mcrhci", set_mcr_acu_valvesl1_opened_status_1),
                        InformationSet("get bts1_layout_sl1_valve foreground_color", "thriver", "mcrhci", get_bts1_layout_sl1_valve_foreground_color),
                        InformationSet("validate bts1_layout_sl1_valve foreground_color = " + str(bts1_layout_sl1_valve_foreground_color_expected), "mcrhci", "hcitracer", validate_bts1_layout_sl1_valve_foreground_color),
                        InformationSet("set mcr_ecubtcu_piranigts1_mbarvacuum = "+ str(mcr_ecubtcu_piranigts1_mbarvacuum_init_4), "thriver", "mcrhci", set_mcr_ecubtcu_piranigts1_mbarvacuum_4),
                        InformationSet("get bts1_layout_out_of_range_txt visibility", "thriver", "mcrhci", get_bts1_layout_out_of_range_txt_visibility),
                        InformationSet("validate bts1_layout_out_of_range_txt visibility = " + str(bts1_layout_out_of_range_txt_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_out_of_range_txt_visibility),
                        InformationSet("set mcr_ecubtcu_bs3_cfeedback = "+ str(mcr_ecubtcu_bs3_cfeedback_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bs3_cfeedback_1),
                        InformationSet("get bts1_layout_bs3_nA1_txt value", "thriver", "mcrhci", get_bts1_layout_bs3_nA1_txt_value),
                        InformationSet("validate bts1_layout_bs3_nA1_txt value = " + str(bts1_layout_bs3_nA1_txt_value_expected), "mcrhci", "hcitracer", validate_bts1_layout_bs3_nA1_txt_value),
                        InformationSet("set mcr_rtieecubtcu_bcm3_highdata_visibility = "+ str(mcr_rtieecubtcu_bcm3_highdata_visibility_init_1), "thriver", "mcrhci", set_mcr_rtieecubtcu_bcm3_highdata_visibility_1),
                        InformationSet("get bts1_layout_bs3_nA1_txt visibility", "thriver", "mcrhci", get_bts1_layout_bs3_nA1_txt_visibility),
                        InformationSet("validate bts1_layout_bs3_nA1_txt visibility = " + str(bts1_layout_bs3_nA1_txt_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_bs3_nA1_txt_visibility),
                        InformationSet("set mcr_ecubtcu_bs3_cfeedback = "+ str(mcr_ecubtcu_bs3_cfeedback_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bs3_cfeedback_2),
                        InformationSet("get bts1_layout_bs3_nA_txt value", "thriver", "mcrhci", get_bts1_layout_bs3_nA_txt_value),
                        InformationSet("validate bts1_layout_bs3_nA_txt value = " + str(bts1_layout_bs3_nA_txt_value_expected), "mcrhci", "hcitracer", validate_bts1_layout_bs3_nA_txt_value),
                        InformationSet("set mcr_rtieecubtcu_bcm3_lowdata_visibility = "+ str(mcr_rtieecubtcu_bcm3_lowdata_visibility_init_1), "thriver", "mcrhci", set_mcr_rtieecubtcu_bcm3_lowdata_visibility_1),
                        InformationSet("get bts1_layout_bs3_nA_txt visibility", "thriver", "mcrhci", get_bts1_layout_bs3_nA_txt_visibility),
                        InformationSet("validate bts1_layout_bs3_nA_txt visibility = " + str(bts1_layout_bs3_nA_txt_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_bs3_nA_txt_visibility),
                        InformationSet("get bts1_layout_GTS1_layout_btn visibility", "thriver", "mcrhci", get_bts1_layout_GTS1_layout_btn_visibility),
                        InformationSet("validate bts1_layout_GTS1_layout_btn visibility = " + str(bts1_layout_GTS1_layout_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_GTS1_layout_btn_visibility),
                        InformationSet("get bts1_layout_ess_layout_btn visibility", "thriver", "mcrhci", get_bts1_layout_ess_layout_btn_visibility),
                        InformationSet("validate bts1_layout_ess_layout_btn visibility = " + str(bts1_layout_ess_layout_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_ess_layout_btn_visibility),
                        InformationSet("get bts1_layout_bts2_layout_btn visibility", "thriver", "mcrhci", get_bts1_layout_bts2_layout_btn_visibility),
                        InformationSet("validate bts1_layout_bts2_layout_btn visibility = " + str(bts1_layout_bts2_layout_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_bts2_layout_btn_visibility),
                        InformationSet("set mcr_scu_safety_bts1_interlocksstatus = "+ str(mcr_scu_safety_bts1_interlocksstatus_init_1), "thriver", "mcrhci", set_mcr_scu_safety_bts1_interlocksstatus_1),
                        InformationSet("get bts1_layout_safety_interlocks_btn foreground_color", "thriver", "mcrhci", get_bts1_layout_safety_interlocks_btn_foreground_color),
                        InformationSet("validate bts1_layout_safety_interlocks_btn foreground_color = " + str(bts1_layout_safety_interlocks_btn_foreground_color_expected), "mcrhci", "hcitracer", validate_bts1_layout_safety_interlocks_btn_foreground_color),
                        InformationSet("get t12 visibility", "thriver", "mcrhci", get_t12_visibility),
                        InformationSet("validate t12 visibility = " + str(t12_visibility_expected), "mcrhci", "hcitracer", validate_t12_visibility),
                        InformationSet("get bts1_layout_bpm11_out_btn visibility", "thriver", "mcrhci", get_bts1_layout_bpm11_out_btn_visibility),
                        InformationSet("validate bts1_layout_bpm11_out_btn visibility = " + str(bts1_layout_bpm11_out_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_bpm11_out_btn_visibility),
                        InformationSet("get bts1_layout_bpm11_in_btn visibility", "thriver", "mcrhci", get_bts1_layout_bpm11_in_btn_visibility),
                        InformationSet("validate bts1_layout_bpm11_in_btn visibility = " + str(bts1_layout_bpm11_in_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_bpm11_in_btn_visibility),
                        InformationSet("set mcr_ecubtcu_bpm11_instatus = "+ str(mcr_ecubtcu_bpm11_instatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpm11_instatus_1),
                        InformationSet("get bts1_layout_bpm11_in_led visibility", "thriver", "mcrhci", get_bts1_layout_bpm11_in_led_visibility),
                        InformationSet("validate bts1_layout_bpm11_in_led visibility = " + str(bts1_layout_bpm11_in_led_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_bpm11_in_led_visibility),
                        InformationSet("set mcr_ecubtcu_bpm11_outstatus = "+ str(mcr_ecubtcu_bpm11_outstatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpm11_outstatus_1),
                        InformationSet("get bts1_layout_bpm11_out_led visibility", "thriver", "mcrhci", get_bts1_layout_bpm11_out_led_visibility),
                        InformationSet("validate bts1_layout_bpm11_out_led visibility = " + str(bts1_layout_bpm11_out_led_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_bpm11_out_led_visibility),
                        InformationSet("set mcr_ecubtcu_bpm11_instatus = "+ str(mcr_ecubtcu_bpm11_instatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpm11_instatus_2),
                        InformationSet("get bts1_layout_bpm11_in visibility", "thriver", "mcrhci", get_bts1_layout_bpm11_in_visibility),
                        InformationSet("validate bts1_layout_bpm11_in visibility = " + str(bts1_layout_bpm11_in_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_bpm11_in_visibility),
                        InformationSet("set mcr_ecubtcu_bpm11_outstatus = "+ str(mcr_ecubtcu_bpm11_outstatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpm11_outstatus_2),
                        InformationSet("get bts1_layout_bpm11_out visibility", "thriver", "mcrhci", get_bts1_layout_bpm11_out_visibility),
                        InformationSet("validate bts1_layout_bpm11_out visibility = " + str(bts1_layout_bpm11_out_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_bpm11_out_visibility),
                        InformationSet("get bts1_layout_SL1_close_btn visibility", "thriver", "mcrhci", get_bts1_layout_SL1_close_btn_visibility),
                        InformationSet("validate bts1_layout_SL1_close_btn visibility = " + str(bts1_layout_SL1_close_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_SL1_close_btn_visibility),
                        InformationSet("get bts1_layout_SL1_open_btn visibility", "thriver", "mcrhci", get_bts1_layout_SL1_open_btn_visibility),
                        InformationSet("validate bts1_layout_SL1_open_btn visibility = " + str(bts1_layout_SL1_open_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_SL1_open_btn_visibility),
                        InformationSet("set mcr_acu_valvesl1_opened_status = "+ str(mcr_acu_valvesl1_opened_status_init_2), "thriver", "mcrhci", set_mcr_acu_valvesl1_opened_status_2),
                        InformationSet("get bts1_layout_SL1_open_led visibility", "thriver", "mcrhci", get_bts1_layout_SL1_open_led_visibility),
                        InformationSet("validate bts1_layout_SL1_open_led visibility = " + str(bts1_layout_SL1_open_led_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_SL1_open_led_visibility),
                        InformationSet("set mcr_acu_valvesl1_closed_status = "+ str(mcr_acu_valvesl1_closed_status_init_1), "thriver", "mcrhci", set_mcr_acu_valvesl1_closed_status_1),
                        InformationSet("get bts1_layout_SL1_close_led visibility", "thriver", "mcrhci", get_bts1_layout_SL1_close_led_visibility),
                        InformationSet("validate bts1_layout_SL1_close_led visibility = " + str(bts1_layout_SL1_close_led_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_SL1_close_led_visibility),
                        InformationSet("get bts1_layout_hidden_obj visibility", "thriver", "mcrhci", get_bts1_layout_hidden_obj_visibility),
                        InformationSet("validate bts1_layout_hidden_obj visibility = " + str(bts1_layout_hidden_obj_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_hidden_obj_visibility),
                        InformationSet("get SC5B visibility", "thriver", "mcrhci", get_SC5B_visibility),
                        InformationSet("validate SC5B visibility = " + str(SC5B_visibility_expected), "mcrhci", "hcitracer", validate_SC5B_visibility),
                        InformationSet("get SC6B visibility", "thriver", "mcrhci", get_SC6B_visibility),
                        InformationSet("validate SC6B visibility = " + str(SC6B_visibility_expected), "mcrhci", "hcitracer", validate_SC6B_visibility),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []