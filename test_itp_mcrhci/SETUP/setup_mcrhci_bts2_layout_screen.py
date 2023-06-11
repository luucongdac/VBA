
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

class SETUP_VALIDATE_BTS2_LAYOUT_SCREEN(ClinicalIntegrationTestProcedure):
    # default variable values
    name = "Confirm that MCR_Service_BTS2_Layout (bts2_layout.v) is displayed"
    bts2_layout_bs4_out_btn_visibility_expected = "1"
    q37_visibility_expected = "1"
    q36_visibility_expected = "1"
    b7_visibility_expected = "1"
    q35_visibility_expected = "1"
    mcr_ecubtcu_sstech_ps_status_init_1 = 0.9
    bts2_layout_ps_canbus_status_txt_foreground_color_expected = "0"
    mcr_ecubtcu_sstech_ps_status_init_2 = 0.1
    bts2_layout_ps_canbus_status_ind_subobject_name_expected = "iba_check_notok.sd"
    bts2_layout_gantry2_close_btn_visibility_expected = "1"
    bts2_layout_gantry2_open_btn_visibility_expected = "1"
    mcr_acu_valvegts2_opened_status_init_1 = True
    bts2_layout_gantry2_open_led_visibility_expected = "1"
    mcr_acu_valvegts2_closed_status_init_1 = True
    bts2_layout_gantry2_close_led_visibility_expected = "1"
    mcr_acu_selectiong12_status_init_1 = True
    bts2_layout_gantry12_selection_txt_foreground_color_expected = "0"
    mcr_acu_selectiong12_status_init_2 = False
    bts2_layout_gantry12_selection_ind_subobject_name_expected = "iba_check_notok.sd"
    mcr_ecubtcu_bpm14_instatus_init_1 = True
    bts2_layout_bpm14_in_visibility_expected = "1"
    bts2_layout_bpm14_out_btn_visibility_expected = "1"
    bts2_layout_bpm14_in_btn_visibility_expected = "1"
    mcr_ecubtcu_bpm14_instatus_init_2 = False
    bts2_layout_bpm14_in_led_visibility_expected = "0"
    mcr_ecubtcu_bpm14_outstatus_init_1 = True
    bts2_layout_bpm14_out_led_visibility_expected = "1"
    mcr_ecubtcu_bpm14_outstatus_init_2 = False
    bts2_layout_bpm14_out_visibility_expected = "0"
    b8_visibility_expected = "1"
    mcr_ecubtcu_bpm12_instatus_init_1 = False
    bts2_layout_bpm12_in_visibility_expected = "0"
    bts2_layout_bpm12_out_btn_visibility_expected = "1"
    bts2_layout_bpm12_in_btn_visibility_expected = "1"
    mcr_ecubtcu_bpm12_instatus_init_2 = True
    bts2_layout_bpm12_in_led_visibility_expected = "1"
    mcr_ecubtcu_bpm12_outstatus_init_1 = False
    bts2_layout_bpm12_out_led_visibility_expected = "0"
    mcr_ecubtcu_bpm12_outstatus_init_2 = True
    bts2_layout_bpm12_out_visibility_expected = "1"
    mcr_ecubtcu_bs4_instatus_init_1 = True
    bts2_layout_bs4_in_visibility_expected = "1"
    bts2_layout_bs4_in_btn_visibility_expected = "1"
    mcr_ecubtcu_bs4_instatus_init_2 = False
    bts2_layout_bs4_in_led_visibility_expected = "0"
    mcr_ecubtcu_bs4_outstatus_init_1 = True
    bts2_layout_bs4_out_led_visibility_expected = "1"
    mcr_ecubtcu_bs4_outstatus_init_2 = False
    bts2_layout_bs4_out_visibility_expected = "0"
    mcr_acu_valvegts2_opened_status_init_2 = True
    bts2_layout_gantry2_valve_foreground_color_expected = "13"
    mcr_ecubtcu_bs4_cfeedback_init_1 = 1.5
    bts2_layout_bs4_nA1_txt_value_expected = 1.5
    mcr_rtieecubtcu_bcm4_highdata_visibility_init_1 = True
    bts2_layout_bs4_nA1_txt_visibility_expected = "1"
    mcr_ecubtcu_bs4_cfeedback_init_2 = 0.5
    bts2_layout_bs4_nA_txt_value_expected = 0.5
    mcr_rtieecubtcu_bcm4_lowdata_visibility_init_1 = True
    bts2_layout_bs4_nA_txt_visibility_expected = "1"
    bts2_layout_GTS2_layout_btn_visibility_expected = "1"
    bts2_layout_bts1_layout_btn_visibility_expected = "1"
    mcr_scu_safety_bts2_interlocksstatus_init_1 = True
    bts2_layout_safety_interlocks_btn_foreground_color_expected = "112"
    mcr_acu_valvesl2_opened_status_init_1 = True
    bts2_layout_sl2_valve_foreground_color_expected = "13"
    bts2_layout_SL2_close_btn_visibility_expected = "1"
    bts2_layout_SL2_open_btn_visibility_expected = "1"
    mcr_acu_valvesl2_opened_status_init_2 = False
    bts2_layout_sl2_open_led_visibility_expected = "0"
    mcr_acu_valvesl2_closed_status_init_1 = True
    bts2_layout_sl2_close_led_visibility_expected = "1"
    bts2_layout_hidden_obj_visibility_expected = "1"
    bts2_layout_bts3_layout_btn_visibility_expected = "1"

    def __init__(self, test):
        cls = type(self)
        name = cls.name
        bts2_layout_bs4_out_btn_visibility_expected = cls.bts2_layout_bs4_out_btn_visibility_expected
        q37_visibility_expected = cls.q37_visibility_expected
        q36_visibility_expected = cls.q36_visibility_expected
        b7_visibility_expected = cls.b7_visibility_expected
        q35_visibility_expected = cls.q35_visibility_expected
        mcr_ecubtcu_sstech_ps_status_init_1 = cls.mcr_ecubtcu_sstech_ps_status_init_1
        bts2_layout_ps_canbus_status_txt_foreground_color_expected = cls.bts2_layout_ps_canbus_status_txt_foreground_color_expected
        mcr_ecubtcu_sstech_ps_status_init_2 = cls.mcr_ecubtcu_sstech_ps_status_init_2
        bts2_layout_ps_canbus_status_ind_subobject_name_expected = cls.bts2_layout_ps_canbus_status_ind_subobject_name_expected
        bts2_layout_gantry2_close_btn_visibility_expected = cls.bts2_layout_gantry2_close_btn_visibility_expected
        bts2_layout_gantry2_open_btn_visibility_expected = cls.bts2_layout_gantry2_open_btn_visibility_expected
        mcr_acu_valvegts2_opened_status_init_1 = cls.mcr_acu_valvegts2_opened_status_init_1
        bts2_layout_gantry2_open_led_visibility_expected = cls.bts2_layout_gantry2_open_led_visibility_expected
        mcr_acu_valvegts2_closed_status_init_1 = cls.mcr_acu_valvegts2_closed_status_init_1
        bts2_layout_gantry2_close_led_visibility_expected = cls.bts2_layout_gantry2_close_led_visibility_expected
        mcr_acu_selectiong12_status_init_1 = cls.mcr_acu_selectiong12_status_init_1
        bts2_layout_gantry12_selection_txt_foreground_color_expected = cls.bts2_layout_gantry12_selection_txt_foreground_color_expected
        mcr_acu_selectiong12_status_init_2 = cls.mcr_acu_selectiong12_status_init_2
        bts2_layout_gantry12_selection_ind_subobject_name_expected = cls.bts2_layout_gantry12_selection_ind_subobject_name_expected
        mcr_ecubtcu_bpm14_instatus_init_1 = cls.mcr_ecubtcu_bpm14_instatus_init_1
        bts2_layout_bpm14_in_visibility_expected = cls.bts2_layout_bpm14_in_visibility_expected
        bts2_layout_bpm14_out_btn_visibility_expected = cls.bts2_layout_bpm14_out_btn_visibility_expected
        bts2_layout_bpm14_in_btn_visibility_expected = cls.bts2_layout_bpm14_in_btn_visibility_expected
        mcr_ecubtcu_bpm14_instatus_init_2 = cls.mcr_ecubtcu_bpm14_instatus_init_2
        bts2_layout_bpm14_in_led_visibility_expected = cls.bts2_layout_bpm14_in_led_visibility_expected
        mcr_ecubtcu_bpm14_outstatus_init_1 = cls.mcr_ecubtcu_bpm14_outstatus_init_1
        bts2_layout_bpm14_out_led_visibility_expected = cls.bts2_layout_bpm14_out_led_visibility_expected
        mcr_ecubtcu_bpm14_outstatus_init_2 = cls.mcr_ecubtcu_bpm14_outstatus_init_2
        bts2_layout_bpm14_out_visibility_expected = cls.bts2_layout_bpm14_out_visibility_expected
        b8_visibility_expected = cls.b8_visibility_expected
        mcr_ecubtcu_bpm12_instatus_init_1 = cls.mcr_ecubtcu_bpm12_instatus_init_1
        bts2_layout_bpm12_in_visibility_expected = cls.bts2_layout_bpm12_in_visibility_expected
        bts2_layout_bpm12_out_btn_visibility_expected = cls.bts2_layout_bpm12_out_btn_visibility_expected
        bts2_layout_bpm12_in_btn_visibility_expected = cls.bts2_layout_bpm12_in_btn_visibility_expected
        mcr_ecubtcu_bpm12_instatus_init_2 = cls.mcr_ecubtcu_bpm12_instatus_init_2
        bts2_layout_bpm12_in_led_visibility_expected = cls.bts2_layout_bpm12_in_led_visibility_expected
        mcr_ecubtcu_bpm12_outstatus_init_1 = cls.mcr_ecubtcu_bpm12_outstatus_init_1
        bts2_layout_bpm12_out_led_visibility_expected = cls.bts2_layout_bpm12_out_led_visibility_expected
        mcr_ecubtcu_bpm12_outstatus_init_2 = cls.mcr_ecubtcu_bpm12_outstatus_init_2
        bts2_layout_bpm12_out_visibility_expected = cls.bts2_layout_bpm12_out_visibility_expected
        mcr_ecubtcu_bs4_instatus_init_1 = cls.mcr_ecubtcu_bs4_instatus_init_1
        bts2_layout_bs4_in_visibility_expected = cls.bts2_layout_bs4_in_visibility_expected
        bts2_layout_bs4_in_btn_visibility_expected = cls.bts2_layout_bs4_in_btn_visibility_expected
        mcr_ecubtcu_bs4_instatus_init_2 = cls.mcr_ecubtcu_bs4_instatus_init_2
        bts2_layout_bs4_in_led_visibility_expected = cls.bts2_layout_bs4_in_led_visibility_expected
        mcr_ecubtcu_bs4_outstatus_init_1 = cls.mcr_ecubtcu_bs4_outstatus_init_1
        bts2_layout_bs4_out_led_visibility_expected = cls.bts2_layout_bs4_out_led_visibility_expected
        mcr_ecubtcu_bs4_outstatus_init_2 = cls.mcr_ecubtcu_bs4_outstatus_init_2
        bts2_layout_bs4_out_visibility_expected = cls.bts2_layout_bs4_out_visibility_expected
        mcr_acu_valvegts2_opened_status_init_2 = cls.mcr_acu_valvegts2_opened_status_init_2
        bts2_layout_gantry2_valve_foreground_color_expected = cls.bts2_layout_gantry2_valve_foreground_color_expected
        mcr_ecubtcu_bs4_cfeedback_init_1 = cls.mcr_ecubtcu_bs4_cfeedback_init_1
        bts2_layout_bs4_nA1_txt_value_expected = cls.bts2_layout_bs4_nA1_txt_value_expected
        mcr_rtieecubtcu_bcm4_highdata_visibility_init_1 = cls.mcr_rtieecubtcu_bcm4_highdata_visibility_init_1
        bts2_layout_bs4_nA1_txt_visibility_expected = cls.bts2_layout_bs4_nA1_txt_visibility_expected
        mcr_ecubtcu_bs4_cfeedback_init_2 = cls.mcr_ecubtcu_bs4_cfeedback_init_2
        bts2_layout_bs4_nA_txt_value_expected = cls.bts2_layout_bs4_nA_txt_value_expected
        mcr_rtieecubtcu_bcm4_lowdata_visibility_init_1 = cls.mcr_rtieecubtcu_bcm4_lowdata_visibility_init_1
        bts2_layout_bs4_nA_txt_visibility_expected = cls.bts2_layout_bs4_nA_txt_visibility_expected
        bts2_layout_GTS2_layout_btn_visibility_expected = cls.bts2_layout_GTS2_layout_btn_visibility_expected
        bts2_layout_bts1_layout_btn_visibility_expected = cls.bts2_layout_bts1_layout_btn_visibility_expected
        mcr_scu_safety_bts2_interlocksstatus_init_1 = cls.mcr_scu_safety_bts2_interlocksstatus_init_1
        bts2_layout_safety_interlocks_btn_foreground_color_expected = cls.bts2_layout_safety_interlocks_btn_foreground_color_expected
        mcr_acu_valvesl2_opened_status_init_1 = cls.mcr_acu_valvesl2_opened_status_init_1
        bts2_layout_sl2_valve_foreground_color_expected = cls.bts2_layout_sl2_valve_foreground_color_expected
        bts2_layout_SL2_close_btn_visibility_expected = cls.bts2_layout_SL2_close_btn_visibility_expected
        bts2_layout_SL2_open_btn_visibility_expected = cls.bts2_layout_SL2_open_btn_visibility_expected
        mcr_acu_valvesl2_opened_status_init_2 = cls.mcr_acu_valvesl2_opened_status_init_2
        bts2_layout_sl2_open_led_visibility_expected = cls.bts2_layout_sl2_open_led_visibility_expected
        mcr_acu_valvesl2_closed_status_init_1 = cls.mcr_acu_valvesl2_closed_status_init_1
        bts2_layout_sl2_close_led_visibility_expected = cls.bts2_layout_sl2_close_led_visibility_expected
        bts2_layout_hidden_obj_visibility_expected = cls.bts2_layout_hidden_obj_visibility_expected
        bts2_layout_bts3_layout_btn_visibility_expected = cls.bts2_layout_bts3_layout_btn_visibility_expected

        #set initial values
        set_mcr_ecubtcu_sstech_ps_status_1 = MsgTypeNumeric("mcr_ecubtcu_sstech_ps_status", mcr_ecubtcu_sstech_ps_status_init_1)
        set_mcr_ecubtcu_sstech_ps_status_2 = MsgTypeNumeric("mcr_ecubtcu_sstech_ps_status", mcr_ecubtcu_sstech_ps_status_init_2)
        set_mcr_acu_valvegts2_opened_status_1 = MsgTypeBoolean("mcr_acu_valvegts2_opened_status", mcr_acu_valvegts2_opened_status_init_1)
        set_mcr_acu_valvegts2_closed_status_1 = MsgTypeBoolean("mcr_acu_valvegts2_closed_status", mcr_acu_valvegts2_closed_status_init_1)
        set_mcr_acu_selectiong12_status_1 = MsgTypeBoolean("mcr_acu_selectiong12_status", mcr_acu_selectiong12_status_init_1)
        set_mcr_acu_selectiong12_status_2 = MsgTypeBoolean("mcr_acu_selectiong12_status", mcr_acu_selectiong12_status_init_2)
        set_mcr_ecubtcu_bpm14_instatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpm14_instatus", mcr_ecubtcu_bpm14_instatus_init_1)
        set_mcr_ecubtcu_bpm14_instatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpm14_instatus", mcr_ecubtcu_bpm14_instatus_init_2)
        set_mcr_ecubtcu_bpm14_outstatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpm14_outstatus", mcr_ecubtcu_bpm14_outstatus_init_1)
        set_mcr_ecubtcu_bpm14_outstatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpm14_outstatus", mcr_ecubtcu_bpm14_outstatus_init_2)
        set_mcr_ecubtcu_bpm12_instatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpm12_instatus", mcr_ecubtcu_bpm12_instatus_init_1)
        set_mcr_ecubtcu_bpm12_instatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpm12_instatus", mcr_ecubtcu_bpm12_instatus_init_2)
        set_mcr_ecubtcu_bpm12_outstatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpm12_outstatus", mcr_ecubtcu_bpm12_outstatus_init_1)
        set_mcr_ecubtcu_bpm12_outstatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpm12_outstatus", mcr_ecubtcu_bpm12_outstatus_init_2)
        set_mcr_ecubtcu_bs4_instatus_1 = MsgTypeBoolean("mcr_ecubtcu_bs4_instatus", mcr_ecubtcu_bs4_instatus_init_1)
        set_mcr_ecubtcu_bs4_instatus_2 = MsgTypeBoolean("mcr_ecubtcu_bs4_instatus", mcr_ecubtcu_bs4_instatus_init_2)
        set_mcr_ecubtcu_bs4_outstatus_1 = MsgTypeBoolean("mcr_ecubtcu_bs4_outstatus", mcr_ecubtcu_bs4_outstatus_init_1)
        set_mcr_ecubtcu_bs4_outstatus_2 = MsgTypeBoolean("mcr_ecubtcu_bs4_outstatus", mcr_ecubtcu_bs4_outstatus_init_2)
        set_mcr_acu_valvegts2_opened_status_2 = MsgTypeBoolean("mcr_acu_valvegts2_opened_status", mcr_acu_valvegts2_opened_status_init_2)
        set_mcr_ecubtcu_bs4_cfeedback_1 = MsgTypeNumeric("mcr_ecubtcu_bs4_cfeedback", mcr_ecubtcu_bs4_cfeedback_init_1)
        set_mcr_rtieecubtcu_bcm4_highdata_visibility_1 = MsgTypeBoolean("mcr_rtieecubtcu_bcm4_highdata_visibility", mcr_rtieecubtcu_bcm4_highdata_visibility_init_1)
        set_mcr_ecubtcu_bs4_cfeedback_2 = MsgTypeNumeric("mcr_ecubtcu_bs4_cfeedback", mcr_ecubtcu_bs4_cfeedback_init_2)
        set_mcr_rtieecubtcu_bcm4_lowdata_visibility_1 = MsgTypeBoolean("mcr_rtieecubtcu_bcm4_lowdata_visibility", mcr_rtieecubtcu_bcm4_lowdata_visibility_init_1)
        set_mcr_scu_safety_bts2_interlocksstatus_1 = MsgTypeBoolean("mcr_scu_safety_bts2_interlocksstatus", mcr_scu_safety_bts2_interlocksstatus_init_1)
        set_mcr_acu_valvesl2_opened_status_1 = MsgTypeBoolean("mcr_acu_valvesl2_opened_status", mcr_acu_valvesl2_opened_status_init_1)
        set_mcr_acu_valvesl2_opened_status_2 = MsgTypeBoolean("mcr_acu_valvesl2_opened_status", mcr_acu_valvesl2_opened_status_init_2)
        set_mcr_acu_valvesl2_closed_status_1 = MsgTypeBoolean("mcr_acu_valvesl2_closed_status", mcr_acu_valvesl2_closed_status_init_1)

        #get values
        get_bts2_layout_bs4_out_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts2_layout_bs4_out_btn")
        get_q37_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q37")
        get_q36_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q36")
        get_b7_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "b7")
        get_q35_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q35")
        get_bts2_layout_ps_canbus_status_txt_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "bts2_layout_ps_canbus_status_txt")
        get_bts2_layout_ps_canbus_status_ind_subobject_name = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "bts2_layout_ps_canbus_status_ind")
        get_bts2_layout_gantry2_close_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts2_layout_gantry2_close_btn")
        get_bts2_layout_gantry2_open_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts2_layout_gantry2_open_btn")
        get_bts2_layout_gantry2_open_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts2_layout_gantry2_open_led")
        get_bts2_layout_gantry2_close_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts2_layout_gantry2_close_led")
        get_bts2_layout_gantry12_selection_txt_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "bts2_layout_gantry12_selection_txt")
        get_bts2_layout_gantry12_selection_ind_subobject_name = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "bts2_layout_gantry12_selection_ind")
        get_bts2_layout_bpm14_in_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts2_layout_bpm14_in")
        get_bts2_layout_bpm14_out_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts2_layout_bpm14_out_btn")
        get_bts2_layout_bpm14_in_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts2_layout_bpm14_in_btn")
        get_bts2_layout_bpm14_in_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts2_layout_bpm14_in_led")
        get_bts2_layout_bpm14_out_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts2_layout_bpm14_out_led")
        get_bts2_layout_bpm14_out_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts2_layout_bpm14_out")
        get_b8_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "b8")
        get_bts2_layout_bpm12_in_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts2_layout_bpm12_in")
        get_bts2_layout_bpm12_out_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts2_layout_bpm12_out_btn")
        get_bts2_layout_bpm12_in_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts2_layout_bpm12_in_btn")
        get_bts2_layout_bpm12_in_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts2_layout_bpm12_in_led")
        get_bts2_layout_bpm12_out_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts2_layout_bpm12_out_led")
        get_bts2_layout_bpm12_out_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts2_layout_bpm12_out")
        get_bts2_layout_bs4_in_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts2_layout_bs4_in")
        get_bts2_layout_bs4_in_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts2_layout_bs4_in_btn")
        get_bts2_layout_bs4_in_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts2_layout_bs4_in_led")
        get_bts2_layout_bs4_out_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts2_layout_bs4_out_led")
        get_bts2_layout_bs4_out_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts2_layout_bs4_out")
        get_bts2_layout_gantry2_valve_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "bts2_layout_gantry2_valve")
        get_bts2_layout_bs4_nA1_txt_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "bts2_layout_bs4_nA1_txt")
        get_bts2_layout_bs4_nA1_txt_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts2_layout_bs4_nA1_txt")
        get_bts2_layout_bs4_nA_txt_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "bts2_layout_bs4_nA_txt")
        get_bts2_layout_bs4_nA_txt_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts2_layout_bs4_nA_txt")
        get_bts2_layout_GTS2_layout_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts2_layout_GTS2_layout_btn")
        get_bts2_layout_bts1_layout_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts2_layout_bts1_layout_btn")
        get_bts2_layout_safety_interlocks_btn_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "bts2_layout_safety_interlocks_btn")
        get_bts2_layout_sl2_valve_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "bts2_layout_sl2_valve")
        get_bts2_layout_SL2_close_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts2_layout_SL2_close_btn")
        get_bts2_layout_SL2_open_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts2_layout_SL2_open_btn")
        get_bts2_layout_sl2_open_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts2_layout_sl2_open_led")
        get_bts2_layout_sl2_close_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts2_layout_sl2_close_led")
        get_bts2_layout_hidden_obj_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts2_layout_hidden_obj")
        get_bts2_layout_bts3_layout_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts2_layout_bts3_layout_btn")

        #validate
        validate_bts2_layout_bs4_out_btn_visibility = MsgTypeString("bts2_layout_bs4_out_btn:TMMI_MCR_IS_VISIBLE", value=bts2_layout_bs4_out_btn_visibility_expected)
        validate_q37_visibility = MsgTypeString("q37:TMMI_MCR_IS_VISIBLE", value=q37_visibility_expected)
        validate_q36_visibility = MsgTypeString("q36:TMMI_MCR_IS_VISIBLE", value=q36_visibility_expected)
        validate_b7_visibility = MsgTypeString("b7:TMMI_MCR_IS_VISIBLE", value=b7_visibility_expected)
        validate_q35_visibility = MsgTypeString("q35:TMMI_MCR_IS_VISIBLE", value=q35_visibility_expected)
        validate_bts2_layout_ps_canbus_status_txt_foreground_color = MsgTypeString("bts2_layout_ps_canbus_status_txt:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=bts2_layout_ps_canbus_status_txt_foreground_color_expected)
        validate_bts2_layout_ps_canbus_status_ind_subobject_name = MsgTypeString("bts2_layout_ps_canbus_status_ind:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=bts2_layout_ps_canbus_status_ind_subobject_name_expected)
        validate_bts2_layout_gantry2_close_btn_visibility = MsgTypeString("bts2_layout_gantry2_close_btn:TMMI_MCR_IS_VISIBLE", value=bts2_layout_gantry2_close_btn_visibility_expected)
        validate_bts2_layout_gantry2_open_btn_visibility = MsgTypeString("bts2_layout_gantry2_open_btn:TMMI_MCR_IS_VISIBLE", value=bts2_layout_gantry2_open_btn_visibility_expected)
        validate_bts2_layout_gantry2_open_led_visibility = MsgTypeString("bts2_layout_gantry2_open_led:TMMI_MCR_IS_VISIBLE", value=bts2_layout_gantry2_open_led_visibility_expected)
        validate_bts2_layout_gantry2_close_led_visibility = MsgTypeString("bts2_layout_gantry2_close_led:TMMI_MCR_IS_VISIBLE", value=bts2_layout_gantry2_close_led_visibility_expected)
        validate_bts2_layout_gantry12_selection_txt_foreground_color = MsgTypeString("bts2_layout_gantry12_selection_txt:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=bts2_layout_gantry12_selection_txt_foreground_color_expected)
        validate_bts2_layout_gantry12_selection_ind_subobject_name = MsgTypeString("bts2_layout_gantry12_selection_ind:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=bts2_layout_gantry12_selection_ind_subobject_name_expected)
        validate_bts2_layout_bpm14_in_visibility = MsgTypeString("bts2_layout_bpm14_in:TMMI_MCR_IS_VISIBLE", value=bts2_layout_bpm14_in_visibility_expected)
        validate_bts2_layout_bpm14_out_btn_visibility = MsgTypeString("bts2_layout_bpm14_out_btn:TMMI_MCR_IS_VISIBLE", value=bts2_layout_bpm14_out_btn_visibility_expected)
        validate_bts2_layout_bpm14_in_btn_visibility = MsgTypeString("bts2_layout_bpm14_in_btn:TMMI_MCR_IS_VISIBLE", value=bts2_layout_bpm14_in_btn_visibility_expected)
        validate_bts2_layout_bpm14_in_led_visibility = MsgTypeString("bts2_layout_bpm14_in_led:TMMI_MCR_IS_VISIBLE", value=bts2_layout_bpm14_in_led_visibility_expected)
        validate_bts2_layout_bpm14_out_led_visibility = MsgTypeString("bts2_layout_bpm14_out_led:TMMI_MCR_IS_VISIBLE", value=bts2_layout_bpm14_out_led_visibility_expected)
        validate_bts2_layout_bpm14_out_visibility = MsgTypeString("bts2_layout_bpm14_out:TMMI_MCR_IS_VISIBLE", value=bts2_layout_bpm14_out_visibility_expected)
        validate_b8_visibility = MsgTypeString("b8:TMMI_MCR_IS_VISIBLE", value=b8_visibility_expected)
        validate_bts2_layout_bpm12_in_visibility = MsgTypeString("bts2_layout_bpm12_in:TMMI_MCR_IS_VISIBLE", value=bts2_layout_bpm12_in_visibility_expected)
        validate_bts2_layout_bpm12_out_btn_visibility = MsgTypeString("bts2_layout_bpm12_out_btn:TMMI_MCR_IS_VISIBLE", value=bts2_layout_bpm12_out_btn_visibility_expected)
        validate_bts2_layout_bpm12_in_btn_visibility = MsgTypeString("bts2_layout_bpm12_in_btn:TMMI_MCR_IS_VISIBLE", value=bts2_layout_bpm12_in_btn_visibility_expected)
        validate_bts2_layout_bpm12_in_led_visibility = MsgTypeString("bts2_layout_bpm12_in_led:TMMI_MCR_IS_VISIBLE", value=bts2_layout_bpm12_in_led_visibility_expected)
        validate_bts2_layout_bpm12_out_led_visibility = MsgTypeString("bts2_layout_bpm12_out_led:TMMI_MCR_IS_VISIBLE", value=bts2_layout_bpm12_out_led_visibility_expected)
        validate_bts2_layout_bpm12_out_visibility = MsgTypeString("bts2_layout_bpm12_out:TMMI_MCR_IS_VISIBLE", value=bts2_layout_bpm12_out_visibility_expected)
        validate_bts2_layout_bs4_in_visibility = MsgTypeString("bts2_layout_bs4_in:TMMI_MCR_IS_VISIBLE", value=bts2_layout_bs4_in_visibility_expected)
        validate_bts2_layout_bs4_in_btn_visibility = MsgTypeString("bts2_layout_bs4_in_btn:TMMI_MCR_IS_VISIBLE", value=bts2_layout_bs4_in_btn_visibility_expected)
        validate_bts2_layout_bs4_in_led_visibility = MsgTypeString("bts2_layout_bs4_in_led:TMMI_MCR_IS_VISIBLE", value=bts2_layout_bs4_in_led_visibility_expected)
        validate_bts2_layout_bs4_out_led_visibility = MsgTypeString("bts2_layout_bs4_out_led:TMMI_MCR_IS_VISIBLE", value=bts2_layout_bs4_out_led_visibility_expected)
        validate_bts2_layout_bs4_out_visibility = MsgTypeString("bts2_layout_bs4_out:TMMI_MCR_IS_VISIBLE", value=bts2_layout_bs4_out_visibility_expected)
        validate_bts2_layout_gantry2_valve_foreground_color = MsgTypeString("bts2_layout_gantry2_valve:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=bts2_layout_gantry2_valve_foreground_color_expected)
        validate_bts2_layout_bs4_nA1_txt_value = MsgTypeNumeric("bts2_layout_bs4_nA1_txt:TMMI_MCR_OBJECT_GET_VALUE", value=bts2_layout_bs4_nA1_txt_value_expected)
        validate_bts2_layout_bs4_nA1_txt_visibility = MsgTypeString("bts2_layout_bs4_nA1_txt:TMMI_MCR_IS_VISIBLE", value=bts2_layout_bs4_nA1_txt_visibility_expected)
        validate_bts2_layout_bs4_nA_txt_value = MsgTypeNumeric("bts2_layout_bs4_nA_txt:TMMI_MCR_OBJECT_GET_VALUE", value=bts2_layout_bs4_nA_txt_value_expected)
        validate_bts2_layout_bs4_nA_txt_visibility = MsgTypeString("bts2_layout_bs4_nA_txt:TMMI_MCR_IS_VISIBLE", value=bts2_layout_bs4_nA_txt_visibility_expected)
        validate_bts2_layout_GTS2_layout_btn_visibility = MsgTypeString("bts2_layout_GTS2_layout_btn:TMMI_MCR_IS_VISIBLE", value=bts2_layout_GTS2_layout_btn_visibility_expected)
        validate_bts2_layout_bts1_layout_btn_visibility = MsgTypeString("bts2_layout_bts1_layout_btn:TMMI_MCR_IS_VISIBLE", value=bts2_layout_bts1_layout_btn_visibility_expected)
        validate_bts2_layout_safety_interlocks_btn_foreground_color = MsgTypeString("bts2_layout_safety_interlocks_btn:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=bts2_layout_safety_interlocks_btn_foreground_color_expected)
        validate_bts2_layout_sl2_valve_foreground_color = MsgTypeString("bts2_layout_sl2_valve:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=bts2_layout_sl2_valve_foreground_color_expected)
        validate_bts2_layout_SL2_close_btn_visibility = MsgTypeString("bts2_layout_SL2_close_btn:TMMI_MCR_IS_VISIBLE", value=bts2_layout_SL2_close_btn_visibility_expected)
        validate_bts2_layout_SL2_open_btn_visibility = MsgTypeString("bts2_layout_SL2_open_btn:TMMI_MCR_IS_VISIBLE", value=bts2_layout_SL2_open_btn_visibility_expected)
        validate_bts2_layout_sl2_open_led_visibility = MsgTypeString("bts2_layout_sl2_open_led:TMMI_MCR_IS_VISIBLE", value=bts2_layout_sl2_open_led_visibility_expected)
        validate_bts2_layout_sl2_close_led_visibility = MsgTypeString("bts2_layout_sl2_close_led:TMMI_MCR_IS_VISIBLE", value=bts2_layout_sl2_close_led_visibility_expected)
        validate_bts2_layout_hidden_obj_visibility = MsgTypeString("bts2_layout_hidden_obj:TMMI_MCR_IS_VISIBLE", value=bts2_layout_hidden_obj_visibility_expected)
        validate_bts2_layout_bts3_layout_btn_visibility = MsgTypeString("bts2_layout_bts3_layout_btn:TMMI_MCR_IS_VISIBLE", value=bts2_layout_bts3_layout_btn_visibility_expected)

        info_exchange = [
                        InformationSet("get bts2_layout_bs4_out_btn visibility", "thriver", "mcrhci", get_bts2_layout_bs4_out_btn_visibility),
                        InformationSet("validate bts2_layout_bs4_out_btn visibility = " + str(bts2_layout_bs4_out_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts2_layout_bs4_out_btn_visibility),
                        InformationSet("get q37 visibility", "thriver", "mcrhci", get_q37_visibility),
                        InformationSet("validate q37 visibility = " + str(q37_visibility_expected), "mcrhci", "hcitracer", validate_q37_visibility),
                        InformationSet("get q36 visibility", "thriver", "mcrhci", get_q36_visibility),
                        InformationSet("validate q36 visibility = " + str(q36_visibility_expected), "mcrhci", "hcitracer", validate_q36_visibility),
                        InformationSet("get b7 visibility", "thriver", "mcrhci", get_b7_visibility),
                        InformationSet("validate b7 visibility = " + str(b7_visibility_expected), "mcrhci", "hcitracer", validate_b7_visibility),
                        InformationSet("get q35 visibility", "thriver", "mcrhci", get_q35_visibility),
                        InformationSet("validate q35 visibility = " + str(q35_visibility_expected), "mcrhci", "hcitracer", validate_q35_visibility),
                        InformationSet("set mcr_ecubtcu_sstech_ps_status = "+ str(mcr_ecubtcu_sstech_ps_status_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_sstech_ps_status_1),
                        InformationSet("get bts2_layout_ps_canbus_status_txt foreground_color", "thriver", "mcrhci", get_bts2_layout_ps_canbus_status_txt_foreground_color),
                        InformationSet("validate bts2_layout_ps_canbus_status_txt foreground_color = " + str(bts2_layout_ps_canbus_status_txt_foreground_color_expected), "mcrhci", "hcitracer", validate_bts2_layout_ps_canbus_status_txt_foreground_color),
                        InformationSet("set mcr_ecubtcu_sstech_ps_status = "+ str(mcr_ecubtcu_sstech_ps_status_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_sstech_ps_status_2),
                        InformationSet("get bts2_layout_ps_canbus_status_ind subobject_name", "thriver", "mcrhci", get_bts2_layout_ps_canbus_status_ind_subobject_name),
                        InformationSet("validate bts2_layout_ps_canbus_status_ind subobject_name = " + str(bts2_layout_ps_canbus_status_ind_subobject_name_expected), "mcrhci", "hcitracer", validate_bts2_layout_ps_canbus_status_ind_subobject_name),
                        InformationSet("get bts2_layout_gantry2_close_btn visibility", "thriver", "mcrhci", get_bts2_layout_gantry2_close_btn_visibility),
                        InformationSet("validate bts2_layout_gantry2_close_btn visibility = " + str(bts2_layout_gantry2_close_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts2_layout_gantry2_close_btn_visibility),
                        InformationSet("get bts2_layout_gantry2_open_btn visibility", "thriver", "mcrhci", get_bts2_layout_gantry2_open_btn_visibility),
                        InformationSet("validate bts2_layout_gantry2_open_btn visibility = " + str(bts2_layout_gantry2_open_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts2_layout_gantry2_open_btn_visibility),
                        InformationSet("set mcr_acu_valvegts2_opened_status = "+ str(mcr_acu_valvegts2_opened_status_init_1), "thriver", "mcrhci", set_mcr_acu_valvegts2_opened_status_1),
                        InformationSet("get bts2_layout_gantry2_open_led visibility", "thriver", "mcrhci", get_bts2_layout_gantry2_open_led_visibility),
                        InformationSet("validate bts2_layout_gantry2_open_led visibility = " + str(bts2_layout_gantry2_open_led_visibility_expected), "mcrhci", "hcitracer", validate_bts2_layout_gantry2_open_led_visibility),
                        InformationSet("set mcr_acu_valvegts2_closed_status = "+ str(mcr_acu_valvegts2_closed_status_init_1), "thriver", "mcrhci", set_mcr_acu_valvegts2_closed_status_1),
                        InformationSet("get bts2_layout_gantry2_close_led visibility", "thriver", "mcrhci", get_bts2_layout_gantry2_close_led_visibility),
                        InformationSet("validate bts2_layout_gantry2_close_led visibility = " + str(bts2_layout_gantry2_close_led_visibility_expected), "mcrhci", "hcitracer", validate_bts2_layout_gantry2_close_led_visibility),
                        InformationSet("set mcr_acu_selectiong12_status = "+ str(mcr_acu_selectiong12_status_init_1), "thriver", "mcrhci", set_mcr_acu_selectiong12_status_1),
                        InformationSet("get bts2_layout_gantry12_selection_txt foreground_color", "thriver", "mcrhci", get_bts2_layout_gantry12_selection_txt_foreground_color),
                        InformationSet("validate bts2_layout_gantry12_selection_txt foreground_color = " + str(bts2_layout_gantry12_selection_txt_foreground_color_expected), "mcrhci", "hcitracer", validate_bts2_layout_gantry12_selection_txt_foreground_color),
                        InformationSet("set mcr_acu_selectiong12_status = "+ str(mcr_acu_selectiong12_status_init_2), "thriver", "mcrhci", set_mcr_acu_selectiong12_status_2),
                        InformationSet("get bts2_layout_gantry12_selection_ind subobject_name", "thriver", "mcrhci", get_bts2_layout_gantry12_selection_ind_subobject_name),
                        InformationSet("validate bts2_layout_gantry12_selection_ind subobject_name = " + str(bts2_layout_gantry12_selection_ind_subobject_name_expected), "mcrhci", "hcitracer", validate_bts2_layout_gantry12_selection_ind_subobject_name),
                        InformationSet("set mcr_ecubtcu_bpm14_instatus = "+ str(mcr_ecubtcu_bpm14_instatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpm14_instatus_1),
                        InformationSet("get bts2_layout_bpm14_in visibility", "thriver", "mcrhci", get_bts2_layout_bpm14_in_visibility),
                        InformationSet("validate bts2_layout_bpm14_in visibility = " + str(bts2_layout_bpm14_in_visibility_expected), "mcrhci", "hcitracer", validate_bts2_layout_bpm14_in_visibility),
                        InformationSet("get bts2_layout_bpm14_out_btn visibility", "thriver", "mcrhci", get_bts2_layout_bpm14_out_btn_visibility),
                        InformationSet("validate bts2_layout_bpm14_out_btn visibility = " + str(bts2_layout_bpm14_out_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts2_layout_bpm14_out_btn_visibility),
                        InformationSet("get bts2_layout_bpm14_in_btn visibility", "thriver", "mcrhci", get_bts2_layout_bpm14_in_btn_visibility),
                        InformationSet("validate bts2_layout_bpm14_in_btn visibility = " + str(bts2_layout_bpm14_in_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts2_layout_bpm14_in_btn_visibility),
                        InformationSet("set mcr_ecubtcu_bpm14_instatus = "+ str(mcr_ecubtcu_bpm14_instatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpm14_instatus_2),
                        InformationSet("get bts2_layout_bpm14_in_led visibility", "thriver", "mcrhci", get_bts2_layout_bpm14_in_led_visibility),
                        InformationSet("validate bts2_layout_bpm14_in_led visibility = " + str(bts2_layout_bpm14_in_led_visibility_expected), "mcrhci", "hcitracer", validate_bts2_layout_bpm14_in_led_visibility),
                        InformationSet("set mcr_ecubtcu_bpm14_outstatus = "+ str(mcr_ecubtcu_bpm14_outstatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpm14_outstatus_1),
                        InformationSet("get bts2_layout_bpm14_out_led visibility", "thriver", "mcrhci", get_bts2_layout_bpm14_out_led_visibility),
                        InformationSet("validate bts2_layout_bpm14_out_led visibility = " + str(bts2_layout_bpm14_out_led_visibility_expected), "mcrhci", "hcitracer", validate_bts2_layout_bpm14_out_led_visibility),
                        InformationSet("set mcr_ecubtcu_bpm14_outstatus = "+ str(mcr_ecubtcu_bpm14_outstatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpm14_outstatus_2),
                        InformationSet("get bts2_layout_bpm14_out visibility", "thriver", "mcrhci", get_bts2_layout_bpm14_out_visibility),
                        InformationSet("validate bts2_layout_bpm14_out visibility = " + str(bts2_layout_bpm14_out_visibility_expected), "mcrhci", "hcitracer", validate_bts2_layout_bpm14_out_visibility),
                        InformationSet("get b8 visibility", "thriver", "mcrhci", get_b8_visibility),
                        InformationSet("validate b8 visibility = " + str(b8_visibility_expected), "mcrhci", "hcitracer", validate_b8_visibility),
                        InformationSet("set mcr_ecubtcu_bpm12_instatus = "+ str(mcr_ecubtcu_bpm12_instatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpm12_instatus_1),
                        InformationSet("get bts2_layout_bpm12_in visibility", "thriver", "mcrhci", get_bts2_layout_bpm12_in_visibility),
                        InformationSet("validate bts2_layout_bpm12_in visibility = " + str(bts2_layout_bpm12_in_visibility_expected), "mcrhci", "hcitracer", validate_bts2_layout_bpm12_in_visibility),
                        InformationSet("get bts2_layout_bpm12_out_btn visibility", "thriver", "mcrhci", get_bts2_layout_bpm12_out_btn_visibility),
                        InformationSet("validate bts2_layout_bpm12_out_btn visibility = " + str(bts2_layout_bpm12_out_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts2_layout_bpm12_out_btn_visibility),
                        InformationSet("get bts2_layout_bpm12_in_btn visibility", "thriver", "mcrhci", get_bts2_layout_bpm12_in_btn_visibility),
                        InformationSet("validate bts2_layout_bpm12_in_btn visibility = " + str(bts2_layout_bpm12_in_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts2_layout_bpm12_in_btn_visibility),
                        InformationSet("set mcr_ecubtcu_bpm12_instatus = "+ str(mcr_ecubtcu_bpm12_instatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpm12_instatus_2),
                        InformationSet("get bts2_layout_bpm12_in_led visibility", "thriver", "mcrhci", get_bts2_layout_bpm12_in_led_visibility),
                        InformationSet("validate bts2_layout_bpm12_in_led visibility = " + str(bts2_layout_bpm12_in_led_visibility_expected), "mcrhci", "hcitracer", validate_bts2_layout_bpm12_in_led_visibility),
                        InformationSet("set mcr_ecubtcu_bpm12_outstatus = "+ str(mcr_ecubtcu_bpm12_outstatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpm12_outstatus_1),
                        InformationSet("get bts2_layout_bpm12_out_led visibility", "thriver", "mcrhci", get_bts2_layout_bpm12_out_led_visibility),
                        InformationSet("validate bts2_layout_bpm12_out_led visibility = " + str(bts2_layout_bpm12_out_led_visibility_expected), "mcrhci", "hcitracer", validate_bts2_layout_bpm12_out_led_visibility),
                        InformationSet("set mcr_ecubtcu_bpm12_outstatus = "+ str(mcr_ecubtcu_bpm12_outstatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpm12_outstatus_2),
                        InformationSet("get bts2_layout_bpm12_out visibility", "thriver", "mcrhci", get_bts2_layout_bpm12_out_visibility),
                        InformationSet("validate bts2_layout_bpm12_out visibility = " + str(bts2_layout_bpm12_out_visibility_expected), "mcrhci", "hcitracer", validate_bts2_layout_bpm12_out_visibility),
                        InformationSet("set mcr_ecubtcu_bs4_instatus = "+ str(mcr_ecubtcu_bs4_instatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bs4_instatus_1),
                        InformationSet("get bts2_layout_bs4_in visibility", "thriver", "mcrhci", get_bts2_layout_bs4_in_visibility),
                        InformationSet("validate bts2_layout_bs4_in visibility = " + str(bts2_layout_bs4_in_visibility_expected), "mcrhci", "hcitracer", validate_bts2_layout_bs4_in_visibility),
                        InformationSet("get bts2_layout_bs4_in_btn visibility", "thriver", "mcrhci", get_bts2_layout_bs4_in_btn_visibility),
                        InformationSet("validate bts2_layout_bs4_in_btn visibility = " + str(bts2_layout_bs4_in_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts2_layout_bs4_in_btn_visibility),
                        InformationSet("set mcr_ecubtcu_bs4_instatus = "+ str(mcr_ecubtcu_bs4_instatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bs4_instatus_2),
                        InformationSet("get bts2_layout_bs4_in_led visibility", "thriver", "mcrhci", get_bts2_layout_bs4_in_led_visibility),
                        InformationSet("validate bts2_layout_bs4_in_led visibility = " + str(bts2_layout_bs4_in_led_visibility_expected), "mcrhci", "hcitracer", validate_bts2_layout_bs4_in_led_visibility),
                        InformationSet("set mcr_ecubtcu_bs4_outstatus = "+ str(mcr_ecubtcu_bs4_outstatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bs4_outstatus_1),
                        InformationSet("get bts2_layout_bs4_out_led visibility", "thriver", "mcrhci", get_bts2_layout_bs4_out_led_visibility),
                        InformationSet("validate bts2_layout_bs4_out_led visibility = " + str(bts2_layout_bs4_out_led_visibility_expected), "mcrhci", "hcitracer", validate_bts2_layout_bs4_out_led_visibility),
                        InformationSet("set mcr_ecubtcu_bs4_outstatus = "+ str(mcr_ecubtcu_bs4_outstatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bs4_outstatus_2),
                        InformationSet("get bts2_layout_bs4_out visibility", "thriver", "mcrhci", get_bts2_layout_bs4_out_visibility),
                        InformationSet("validate bts2_layout_bs4_out visibility = " + str(bts2_layout_bs4_out_visibility_expected), "mcrhci", "hcitracer", validate_bts2_layout_bs4_out_visibility),
                        InformationSet("set mcr_acu_valvegts2_opened_status = "+ str(mcr_acu_valvegts2_opened_status_init_2), "thriver", "mcrhci", set_mcr_acu_valvegts2_opened_status_2),
                        InformationSet("get bts2_layout_gantry2_valve foreground_color", "thriver", "mcrhci", get_bts2_layout_gantry2_valve_foreground_color),
                        InformationSet("validate bts2_layout_gantry2_valve foreground_color = " + str(bts2_layout_gantry2_valve_foreground_color_expected), "mcrhci", "hcitracer", validate_bts2_layout_gantry2_valve_foreground_color),
                        InformationSet("set mcr_ecubtcu_bs4_cfeedback = "+ str(mcr_ecubtcu_bs4_cfeedback_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bs4_cfeedback_1),
                        InformationSet("get bts2_layout_bs4_nA1_txt value", "thriver", "mcrhci", get_bts2_layout_bs4_nA1_txt_value),
                        InformationSet("validate bts2_layout_bs4_nA1_txt value = " + str(bts2_layout_bs4_nA1_txt_value_expected), "mcrhci", "hcitracer", validate_bts2_layout_bs4_nA1_txt_value),
                        InformationSet("set mcr_rtieecubtcu_bcm4_highdata_visibility = "+ str(mcr_rtieecubtcu_bcm4_highdata_visibility_init_1), "thriver", "mcrhci", set_mcr_rtieecubtcu_bcm4_highdata_visibility_1),
                        InformationSet("get bts2_layout_bs4_nA1_txt visibility", "thriver", "mcrhci", get_bts2_layout_bs4_nA1_txt_visibility),
                        InformationSet("validate bts2_layout_bs4_nA1_txt visibility = " + str(bts2_layout_bs4_nA1_txt_visibility_expected), "mcrhci", "hcitracer", validate_bts2_layout_bs4_nA1_txt_visibility),
                        InformationSet("set mcr_ecubtcu_bs4_cfeedback = "+ str(mcr_ecubtcu_bs4_cfeedback_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bs4_cfeedback_2),
                        InformationSet("get bts2_layout_bs4_nA_txt value", "thriver", "mcrhci", get_bts2_layout_bs4_nA_txt_value),
                        InformationSet("validate bts2_layout_bs4_nA_txt value = " + str(bts2_layout_bs4_nA_txt_value_expected), "mcrhci", "hcitracer", validate_bts2_layout_bs4_nA_txt_value),
                        InformationSet("set mcr_rtieecubtcu_bcm4_lowdata_visibility = "+ str(mcr_rtieecubtcu_bcm4_lowdata_visibility_init_1), "thriver", "mcrhci", set_mcr_rtieecubtcu_bcm4_lowdata_visibility_1),
                        InformationSet("get bts2_layout_bs4_nA_txt visibility", "thriver", "mcrhci", get_bts2_layout_bs4_nA_txt_visibility),
                        InformationSet("validate bts2_layout_bs4_nA_txt visibility = " + str(bts2_layout_bs4_nA_txt_visibility_expected), "mcrhci", "hcitracer", validate_bts2_layout_bs4_nA_txt_visibility),
                        InformationSet("get bts2_layout_GTS2_layout_btn visibility", "thriver", "mcrhci", get_bts2_layout_GTS2_layout_btn_visibility),
                        InformationSet("validate bts2_layout_GTS2_layout_btn visibility = " + str(bts2_layout_GTS2_layout_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts2_layout_GTS2_layout_btn_visibility),
                        InformationSet("get bts2_layout_bts1_layout_btn visibility", "thriver", "mcrhci", get_bts2_layout_bts1_layout_btn_visibility),
                        InformationSet("validate bts2_layout_bts1_layout_btn visibility = " + str(bts2_layout_bts1_layout_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts2_layout_bts1_layout_btn_visibility),
                        InformationSet("set mcr_scu_safety_bts2_interlocksstatus = "+ str(mcr_scu_safety_bts2_interlocksstatus_init_1), "thriver", "mcrhci", set_mcr_scu_safety_bts2_interlocksstatus_1),
                        InformationSet("get bts2_layout_safety_interlocks_btn foreground_color", "thriver", "mcrhci", get_bts2_layout_safety_interlocks_btn_foreground_color),
                        InformationSet("validate bts2_layout_safety_interlocks_btn foreground_color = " + str(bts2_layout_safety_interlocks_btn_foreground_color_expected), "mcrhci", "hcitracer", validate_bts2_layout_safety_interlocks_btn_foreground_color),
                        InformationSet("set mcr_acu_valvesl2_opened_status = "+ str(mcr_acu_valvesl2_opened_status_init_1), "thriver", "mcrhci", set_mcr_acu_valvesl2_opened_status_1),
                        InformationSet("get bts2_layout_sl2_valve foreground_color", "thriver", "mcrhci", get_bts2_layout_sl2_valve_foreground_color),
                        InformationSet("validate bts2_layout_sl2_valve foreground_color = " + str(bts2_layout_sl2_valve_foreground_color_expected), "mcrhci", "hcitracer", validate_bts2_layout_sl2_valve_foreground_color),
                        InformationSet("get bts2_layout_SL2_close_btn visibility", "thriver", "mcrhci", get_bts2_layout_SL2_close_btn_visibility),
                        InformationSet("validate bts2_layout_SL2_close_btn visibility = " + str(bts2_layout_SL2_close_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts2_layout_SL2_close_btn_visibility),
                        InformationSet("get bts2_layout_SL2_open_btn visibility", "thriver", "mcrhci", get_bts2_layout_SL2_open_btn_visibility),
                        InformationSet("validate bts2_layout_SL2_open_btn visibility = " + str(bts2_layout_SL2_open_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts2_layout_SL2_open_btn_visibility),
                        InformationSet("set mcr_acu_valvesl2_opened_status = "+ str(mcr_acu_valvesl2_opened_status_init_2), "thriver", "mcrhci", set_mcr_acu_valvesl2_opened_status_2),
                        InformationSet("get bts2_layout_sl2_open_led visibility", "thriver", "mcrhci", get_bts2_layout_sl2_open_led_visibility),
                        InformationSet("validate bts2_layout_sl2_open_led visibility = " + str(bts2_layout_sl2_open_led_visibility_expected), "mcrhci", "hcitracer", validate_bts2_layout_sl2_open_led_visibility),
                        InformationSet("set mcr_acu_valvesl2_closed_status = "+ str(mcr_acu_valvesl2_closed_status_init_1), "thriver", "mcrhci", set_mcr_acu_valvesl2_closed_status_1),
                        InformationSet("get bts2_layout_sl2_close_led visibility", "thriver", "mcrhci", get_bts2_layout_sl2_close_led_visibility),
                        InformationSet("validate bts2_layout_sl2_close_led visibility = " + str(bts2_layout_sl2_close_led_visibility_expected), "mcrhci", "hcitracer", validate_bts2_layout_sl2_close_led_visibility),
                        InformationSet("get bts2_layout_hidden_obj visibility", "thriver", "mcrhci", get_bts2_layout_hidden_obj_visibility),
                        InformationSet("validate bts2_layout_hidden_obj visibility = " + str(bts2_layout_hidden_obj_visibility_expected), "mcrhci", "hcitracer", validate_bts2_layout_hidden_obj_visibility),
                        InformationSet("get bts2_layout_bts3_layout_btn visibility", "thriver", "mcrhci", get_bts2_layout_bts3_layout_btn_visibility),
                        InformationSet("validate bts2_layout_bts3_layout_btn visibility = " + str(bts2_layout_bts3_layout_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts2_layout_bts3_layout_btn_visibility),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []