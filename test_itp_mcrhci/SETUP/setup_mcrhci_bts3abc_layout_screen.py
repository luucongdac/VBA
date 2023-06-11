
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

class SETUP_VALIDATE_BTS3ABC_LAYOUT_SCREEN(ClinicalIntegrationTestProcedure):
    # default variable values
    name = "Confirm that MCR_Service_BTS3ABC_Layout (bts3abc_layout.v) is displayed"
    SC3A_visibility_expected = "1"
    SC3B_visibility_expected = "1"
    q47_visibility_expected = "1"
    q46_visibility_expected = "1"
    q45_visibility_expected = "1"
    bts3_layout_ps_canbus_status_txt_visibility_expected = "1"
    mcr_ecubtcu_sstech_ps_status_init_1 = 0.1
    bts3_layout_ps_canbus_status_ind_subobject_name_expected = "iba_check_notok.sd"
    mcr_acu_selectiong12_status_init_1 = False
    bts3_layout_gantry12_selection_txt_foreground_color_expected = "0"
    mcr_acu_selectiong12_status_init_2 = False
    bts3_layout_gantry12_selection_ind_subobject_name_expected = "iba_check_ok.sd"
    mcr_ecubtcu_bpme3_instatus_init_1 = True
    bts3_layout_bpme3_in_visibility_expected = "1"
    bts3_layout_bpme3_out_btn_visibility_expected = "1"
    bts3_layout_bpme3_in_btn_visibility_expected = "1"
    mcr_ecubtcu_bpme3_instatus_init_2 = True
    bts3_layout_bpme3_in_led_visibility_expected = "1"
    mcr_ecubtcu_bpme3_outstatus_init_1 = True
    bts3_layout_bpme3_out_led_visibility_expected = "1"
    mcr_ecubtcu_bpme3_outstatus_init_2 = True
    bts3_layout_bpme3_out_visibility_expected = "1"
    mcr_ecubtcu_bpme1_instatus_init_1 = True
    bts3_layout_bpme1_in_visibility_expected = "1"
    bts3_layout_bpme1_out_btn_visibility_expected = "1"
    bts3_layout_bpme1_in_btn_visibility_expected = "1"
    mcr_ecubtcu_bpme1_instatus_init_2 = False
    bts3_layout_bpme1_in_led_visibility_expected = "0"
    mcr_ecubtcu_bpme1_outstatus_init_1 = True
    bts3_layout_bpme1_out_led_visibility_expected = "1"
    mcr_ecubtcu_bpme1_outstatus_init_2 = True
    bts3_layout_bpme1_out_visibility_expected = "1"
    bts3_layout_bts2_layout_btn_visibility_expected = "1"
    bts3_layout_hidden_obj_visibility_expected = "1"
    b9_visibility_expected = "1"
    q0m4_visibility_expected = "1"
    q1m4_visibility_expected = "1"
    q50_visibility_expected = "1"
    q48_visibility_expected = "1"
    q49_visibility_expected = "1"
    SC4A_visibility_expected = "1"
    mcr_ecubtcu_bpme2_outstatus_init_1 = False
    bts3_layout_bpme2_out_visibility_expected = "0"
    mcr_ecubtcu_bpme2_instatus_init_1 = True
    bts3_layout_bpme2_in_visibility_expected = "1"
    bts3_layout_bpme2_out_btn_visibility_expected = "1"
    bts3_layout_bpme2_in_btn_visibility_expected = "1"
    mcr_ecubtcu_bpme2_instatus_init_2 = False
    bts3_layout_bpme2_in_led_visibility_expected = "0"
    mcr_ecubtcu_bpme2_outstatus_init_2 = True
    bts3_layout_bpme2_out_led_visibility_expected = "1"
    SC4B_visibility_expected = "1"
    SC6A_visibility_expected = "1"
    b10_visibility_expected = "1"
    q1m3_visibility_expected = "1"
    q2m3_visibility_expected = "1"
    tr3_scu_b9_on_enable_init_1 = True
    bts3_layout_safety_interlocks_btn_foreground_color_expected = "0"
    bts3_layout_bpms1_in_visibility_expected = "1"

    def __init__(self, test):
        cls = type(self)
        name = cls.name
        SC3A_visibility_expected = cls.SC3A_visibility_expected
        SC3B_visibility_expected = cls.SC3B_visibility_expected
        q47_visibility_expected = cls.q47_visibility_expected
        q46_visibility_expected = cls.q46_visibility_expected
        q45_visibility_expected = cls.q45_visibility_expected
        bts3_layout_ps_canbus_status_txt_visibility_expected = cls.bts3_layout_ps_canbus_status_txt_visibility_expected
        mcr_ecubtcu_sstech_ps_status_init_1 = cls.mcr_ecubtcu_sstech_ps_status_init_1
        bts3_layout_ps_canbus_status_ind_subobject_name_expected = cls.bts3_layout_ps_canbus_status_ind_subobject_name_expected
        mcr_acu_selectiong12_status_init_1 = cls.mcr_acu_selectiong12_status_init_1
        bts3_layout_gantry12_selection_txt_foreground_color_expected = cls.bts3_layout_gantry12_selection_txt_foreground_color_expected
        mcr_acu_selectiong12_status_init_2 = cls.mcr_acu_selectiong12_status_init_2
        bts3_layout_gantry12_selection_ind_subobject_name_expected = cls.bts3_layout_gantry12_selection_ind_subobject_name_expected
        mcr_ecubtcu_bpme3_instatus_init_1 = cls.mcr_ecubtcu_bpme3_instatus_init_1
        bts3_layout_bpme3_in_visibility_expected = cls.bts3_layout_bpme3_in_visibility_expected
        bts3_layout_bpme3_out_btn_visibility_expected = cls.bts3_layout_bpme3_out_btn_visibility_expected
        bts3_layout_bpme3_in_btn_visibility_expected = cls.bts3_layout_bpme3_in_btn_visibility_expected
        mcr_ecubtcu_bpme3_instatus_init_2 = cls.mcr_ecubtcu_bpme3_instatus_init_2
        bts3_layout_bpme3_in_led_visibility_expected = cls.bts3_layout_bpme3_in_led_visibility_expected
        mcr_ecubtcu_bpme3_outstatus_init_1 = cls.mcr_ecubtcu_bpme3_outstatus_init_1
        bts3_layout_bpme3_out_led_visibility_expected = cls.bts3_layout_bpme3_out_led_visibility_expected
        mcr_ecubtcu_bpme3_outstatus_init_2 = cls.mcr_ecubtcu_bpme3_outstatus_init_2
        bts3_layout_bpme3_out_visibility_expected = cls.bts3_layout_bpme3_out_visibility_expected
        mcr_ecubtcu_bpme1_instatus_init_1 = cls.mcr_ecubtcu_bpme1_instatus_init_1
        bts3_layout_bpme1_in_visibility_expected = cls.bts3_layout_bpme1_in_visibility_expected
        bts3_layout_bpme1_out_btn_visibility_expected = cls.bts3_layout_bpme1_out_btn_visibility_expected
        bts3_layout_bpme1_in_btn_visibility_expected = cls.bts3_layout_bpme1_in_btn_visibility_expected
        mcr_ecubtcu_bpme1_instatus_init_2 = cls.mcr_ecubtcu_bpme1_instatus_init_2
        bts3_layout_bpme1_in_led_visibility_expected = cls.bts3_layout_bpme1_in_led_visibility_expected
        mcr_ecubtcu_bpme1_outstatus_init_1 = cls.mcr_ecubtcu_bpme1_outstatus_init_1
        bts3_layout_bpme1_out_led_visibility_expected = cls.bts3_layout_bpme1_out_led_visibility_expected
        mcr_ecubtcu_bpme1_outstatus_init_2 = cls.mcr_ecubtcu_bpme1_outstatus_init_2
        bts3_layout_bpme1_out_visibility_expected = cls.bts3_layout_bpme1_out_visibility_expected
        bts3_layout_bts2_layout_btn_visibility_expected = cls.bts3_layout_bts2_layout_btn_visibility_expected
        bts3_layout_hidden_obj_visibility_expected = cls.bts3_layout_hidden_obj_visibility_expected
        b9_visibility_expected = cls.b9_visibility_expected
        q0m4_visibility_expected = cls.q0m4_visibility_expected
        q1m4_visibility_expected = cls.q1m4_visibility_expected
        q50_visibility_expected = cls.q50_visibility_expected
        q48_visibility_expected = cls.q48_visibility_expected
        q49_visibility_expected = cls.q49_visibility_expected
        SC4A_visibility_expected = cls.SC4A_visibility_expected
        mcr_ecubtcu_bpme2_outstatus_init_1 = cls.mcr_ecubtcu_bpme2_outstatus_init_1
        bts3_layout_bpme2_out_visibility_expected = cls.bts3_layout_bpme2_out_visibility_expected
        mcr_ecubtcu_bpme2_instatus_init_1 = cls.mcr_ecubtcu_bpme2_instatus_init_1
        bts3_layout_bpme2_in_visibility_expected = cls.bts3_layout_bpme2_in_visibility_expected
        bts3_layout_bpme2_out_btn_visibility_expected = cls.bts3_layout_bpme2_out_btn_visibility_expected
        bts3_layout_bpme2_in_btn_visibility_expected = cls.bts3_layout_bpme2_in_btn_visibility_expected
        mcr_ecubtcu_bpme2_instatus_init_2 = cls.mcr_ecubtcu_bpme2_instatus_init_2
        bts3_layout_bpme2_in_led_visibility_expected = cls.bts3_layout_bpme2_in_led_visibility_expected
        mcr_ecubtcu_bpme2_outstatus_init_2 = cls.mcr_ecubtcu_bpme2_outstatus_init_2
        bts3_layout_bpme2_out_led_visibility_expected = cls.bts3_layout_bpme2_out_led_visibility_expected
        SC4B_visibility_expected = cls.SC4B_visibility_expected
        SC6A_visibility_expected = cls.SC6A_visibility_expected
        b10_visibility_expected = cls.b10_visibility_expected
        q1m3_visibility_expected = cls.q1m3_visibility_expected
        q2m3_visibility_expected = cls.q2m3_visibility_expected
        tr3_scu_b9_on_enable_init_1 = cls.tr3_scu_b9_on_enable_init_1
        bts3_layout_safety_interlocks_btn_foreground_color_expected = cls.bts3_layout_safety_interlocks_btn_foreground_color_expected
        bts3_layout_bpms1_in_visibility_expected = cls.bts3_layout_bpms1_in_visibility_expected

        #set initial values
        set_mcr_ecubtcu_sstech_ps_status_1 = MsgTypeNumeric("mcr_ecubtcu_sstech_ps_status", mcr_ecubtcu_sstech_ps_status_init_1)
        set_mcr_acu_selectiong12_status_1 = MsgTypeBoolean("mcr_acu_selectiong12_status", mcr_acu_selectiong12_status_init_1)
        set_mcr_acu_selectiong12_status_2 = MsgTypeBoolean("mcr_acu_selectiong12_status", mcr_acu_selectiong12_status_init_2)
        set_mcr_ecubtcu_bpme3_instatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpme3_instatus", mcr_ecubtcu_bpme3_instatus_init_1)
        set_mcr_ecubtcu_bpme3_instatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpme3_instatus", mcr_ecubtcu_bpme3_instatus_init_2)
        set_mcr_ecubtcu_bpme3_outstatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpme3_outstatus", mcr_ecubtcu_bpme3_outstatus_init_1)
        set_mcr_ecubtcu_bpme3_outstatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpme3_outstatus", mcr_ecubtcu_bpme3_outstatus_init_2)
        set_mcr_ecubtcu_bpme1_instatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpme1_instatus", mcr_ecubtcu_bpme1_instatus_init_1)
        set_mcr_ecubtcu_bpme1_instatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpme1_instatus", mcr_ecubtcu_bpme1_instatus_init_2)
        set_mcr_ecubtcu_bpme1_outstatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpme1_outstatus", mcr_ecubtcu_bpme1_outstatus_init_1)
        set_mcr_ecubtcu_bpme1_outstatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpme1_outstatus", mcr_ecubtcu_bpme1_outstatus_init_2)
        set_mcr_ecubtcu_bpme2_outstatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpme2_outstatus", mcr_ecubtcu_bpme2_outstatus_init_1)
        set_mcr_ecubtcu_bpme2_instatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpme2_instatus", mcr_ecubtcu_bpme2_instatus_init_1)
        set_mcr_ecubtcu_bpme2_instatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpme2_instatus", mcr_ecubtcu_bpme2_instatus_init_2)
        set_mcr_ecubtcu_bpme2_outstatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpme2_outstatus", mcr_ecubtcu_bpme2_outstatus_init_2)
        set_tr3_scu_b9_on_enable_1 = MsgTypeBoolean("tr3_scu_b9_on_enable", tr3_scu_b9_on_enable_init_1)

        #get values
        get_SC3A_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "SC3A")
        get_SC3B_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "SC3B")
        get_q47_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q47")
        get_q46_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q46")
        get_q45_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q45")
        get_bts3_layout_ps_canbus_status_txt_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_ps_canbus_status_txt")
        get_bts3_layout_ps_canbus_status_ind_subobject_name = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "bts3_layout_ps_canbus_status_ind")
        get_bts3_layout_gantry12_selection_txt_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "bts3_layout_gantry12_selection_txt")
        get_bts3_layout_gantry12_selection_ind_subobject_name = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "bts3_layout_gantry12_selection_ind")
        get_bts3_layout_bpme3_in_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bpme3_in")
        get_bts3_layout_bpme3_out_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bpme3_out_btn")
        get_bts3_layout_bpme3_in_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bpme3_in_btn")
        get_bts3_layout_bpme3_in_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bpme3_in_led")
        get_bts3_layout_bpme3_out_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bpme3_out_led")
        get_bts3_layout_bpme3_out_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bpme3_out")
        get_bts3_layout_bpme1_in_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bpme1_in")
        get_bts3_layout_bpme1_out_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bpme1_out_btn")
        get_bts3_layout_bpme1_in_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bpme1_in_btn")
        get_bts3_layout_bpme1_in_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bpme1_in_led")
        get_bts3_layout_bpme1_out_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bpme1_out_led")
        get_bts3_layout_bpme1_out_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bpme1_out")
        get_bts3_layout_bts2_layout_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bts2_layout_btn")
        get_bts3_layout_hidden_obj_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_hidden_obj")
        get_b9_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "b9")
        get_q0m4_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q0m4")
        get_q1m4_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q1m4")
        get_q50_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q50")
        get_q48_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q48")
        get_q49_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q49")
        get_SC4A_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "SC4A")
        get_bts3_layout_bpme2_out_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bpme2_out")
        get_bts3_layout_bpme2_in_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bpme2_in")
        get_bts3_layout_bpme2_out_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bpme2_out_btn")
        get_bts3_layout_bpme2_in_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bpme2_in_btn")
        get_bts3_layout_bpme2_in_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bpme2_in_led")
        get_bts3_layout_bpme2_out_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bpme2_out_led")
        get_SC4B_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "SC4B")
        get_SC6A_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "SC6A")
        get_b10_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "b10")
        get_q1m3_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q1m3")
        get_q2m3_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q2m3")
        get_bts3_layout_safety_interlocks_btn_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "bts3_layout_safety_interlocks_btn")
        get_bts3_layout_bpms1_in_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bpms1_in")

        #validate
        validate_SC3A_visibility = MsgTypeString("SC3A:TMMI_MCR_IS_VISIBLE", value=SC3A_visibility_expected)
        validate_SC3B_visibility = MsgTypeString("SC3B:TMMI_MCR_IS_VISIBLE", value=SC3B_visibility_expected)
        validate_q47_visibility = MsgTypeString("q47:TMMI_MCR_IS_VISIBLE", value=q47_visibility_expected)
        validate_q46_visibility = MsgTypeString("q46:TMMI_MCR_IS_VISIBLE", value=q46_visibility_expected)
        validate_q45_visibility = MsgTypeString("q45:TMMI_MCR_IS_VISIBLE", value=q45_visibility_expected)
        validate_bts3_layout_ps_canbus_status_txt_visibility = MsgTypeString("bts3_layout_ps_canbus_status_txt:TMMI_MCR_IS_VISIBLE", value=bts3_layout_ps_canbus_status_txt_visibility_expected)
        validate_bts3_layout_ps_canbus_status_ind_subobject_name = MsgTypeString("bts3_layout_ps_canbus_status_ind:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=bts3_layout_ps_canbus_status_ind_subobject_name_expected)
        validate_bts3_layout_gantry12_selection_txt_foreground_color = MsgTypeString("bts3_layout_gantry12_selection_txt:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=bts3_layout_gantry12_selection_txt_foreground_color_expected)
        validate_bts3_layout_gantry12_selection_ind_subobject_name = MsgTypeString("bts3_layout_gantry12_selection_ind:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=bts3_layout_gantry12_selection_ind_subobject_name_expected)
        validate_bts3_layout_bpme3_in_visibility = MsgTypeString("bts3_layout_bpme3_in:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bpme3_in_visibility_expected)
        validate_bts3_layout_bpme3_out_btn_visibility = MsgTypeString("bts3_layout_bpme3_out_btn:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bpme3_out_btn_visibility_expected)
        validate_bts3_layout_bpme3_in_btn_visibility = MsgTypeString("bts3_layout_bpme3_in_btn:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bpme3_in_btn_visibility_expected)
        validate_bts3_layout_bpme3_in_led_visibility = MsgTypeString("bts3_layout_bpme3_in_led:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bpme3_in_led_visibility_expected)
        validate_bts3_layout_bpme3_out_led_visibility = MsgTypeString("bts3_layout_bpme3_out_led:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bpme3_out_led_visibility_expected)
        validate_bts3_layout_bpme3_out_visibility = MsgTypeString("bts3_layout_bpme3_out:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bpme3_out_visibility_expected)
        validate_bts3_layout_bpme1_in_visibility = MsgTypeString("bts3_layout_bpme1_in:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bpme1_in_visibility_expected)
        validate_bts3_layout_bpme1_out_btn_visibility = MsgTypeString("bts3_layout_bpme1_out_btn:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bpme1_out_btn_visibility_expected)
        validate_bts3_layout_bpme1_in_btn_visibility = MsgTypeString("bts3_layout_bpme1_in_btn:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bpme1_in_btn_visibility_expected)
        validate_bts3_layout_bpme1_in_led_visibility = MsgTypeString("bts3_layout_bpme1_in_led:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bpme1_in_led_visibility_expected)
        validate_bts3_layout_bpme1_out_led_visibility = MsgTypeString("bts3_layout_bpme1_out_led:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bpme1_out_led_visibility_expected)
        validate_bts3_layout_bpme1_out_visibility = MsgTypeString("bts3_layout_bpme1_out:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bpme1_out_visibility_expected)
        validate_bts3_layout_bts2_layout_btn_visibility = MsgTypeString("bts3_layout_bts2_layout_btn:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bts2_layout_btn_visibility_expected)
        validate_bts3_layout_hidden_obj_visibility = MsgTypeString("bts3_layout_hidden_obj:TMMI_MCR_IS_VISIBLE", value=bts3_layout_hidden_obj_visibility_expected)
        validate_b9_visibility = MsgTypeString("b9:TMMI_MCR_IS_VISIBLE", value=b9_visibility_expected)
        validate_q0m4_visibility = MsgTypeString("q0m4:TMMI_MCR_IS_VISIBLE", value=q0m4_visibility_expected)
        validate_q1m4_visibility = MsgTypeString("q1m4:TMMI_MCR_IS_VISIBLE", value=q1m4_visibility_expected)
        validate_q50_visibility = MsgTypeString("q50:TMMI_MCR_IS_VISIBLE", value=q50_visibility_expected)
        validate_q48_visibility = MsgTypeString("q48:TMMI_MCR_IS_VISIBLE", value=q48_visibility_expected)
        validate_q49_visibility = MsgTypeString("q49:TMMI_MCR_IS_VISIBLE", value=q49_visibility_expected)
        validate_SC4A_visibility = MsgTypeString("SC4A:TMMI_MCR_IS_VISIBLE", value=SC4A_visibility_expected)
        validate_bts3_layout_bpme2_out_visibility = MsgTypeString("bts3_layout_bpme2_out:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bpme2_out_visibility_expected)
        validate_bts3_layout_bpme2_in_visibility = MsgTypeString("bts3_layout_bpme2_in:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bpme2_in_visibility_expected)
        validate_bts3_layout_bpme2_out_btn_visibility = MsgTypeString("bts3_layout_bpme2_out_btn:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bpme2_out_btn_visibility_expected)
        validate_bts3_layout_bpme2_in_btn_visibility = MsgTypeString("bts3_layout_bpme2_in_btn:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bpme2_in_btn_visibility_expected)
        validate_bts3_layout_bpme2_in_led_visibility = MsgTypeString("bts3_layout_bpme2_in_led:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bpme2_in_led_visibility_expected)
        validate_bts3_layout_bpme2_out_led_visibility = MsgTypeString("bts3_layout_bpme2_out_led:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bpme2_out_led_visibility_expected)
        validate_SC4B_visibility = MsgTypeString("SC4B:TMMI_MCR_IS_VISIBLE", value=SC4B_visibility_expected)
        validate_SC6A_visibility = MsgTypeString("SC6A:TMMI_MCR_IS_VISIBLE", value=SC6A_visibility_expected)
        validate_b10_visibility = MsgTypeString("b10:TMMI_MCR_IS_VISIBLE", value=b10_visibility_expected)
        validate_q1m3_visibility = MsgTypeString("q1m3:TMMI_MCR_IS_VISIBLE", value=q1m3_visibility_expected)
        validate_q2m3_visibility = MsgTypeString("q2m3:TMMI_MCR_IS_VISIBLE", value=q2m3_visibility_expected)
        validate_bts3_layout_safety_interlocks_btn_foreground_color = MsgTypeString("bts3_layout_safety_interlocks_btn:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=bts3_layout_safety_interlocks_btn_foreground_color_expected)
        validate_bts3_layout_bpms1_in_visibility = MsgTypeString("bts3_layout_bpms1_in:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bpms1_in_visibility_expected)

        info_exchange = [
                        InformationSet("get SC3A visibility", "thriver", "mcrhci", get_SC3A_visibility),
                        InformationSet("validate SC3A visibility = " + str(SC3A_visibility_expected), "mcrhci", "hcitracer", validate_SC3A_visibility),
                        InformationSet("get SC3B visibility", "thriver", "mcrhci", get_SC3B_visibility),
                        InformationSet("validate SC3B visibility = " + str(SC3B_visibility_expected), "mcrhci", "hcitracer", validate_SC3B_visibility),
                        InformationSet("get q47 visibility", "thriver", "mcrhci", get_q47_visibility),
                        InformationSet("validate q47 visibility = " + str(q47_visibility_expected), "mcrhci", "hcitracer", validate_q47_visibility),
                        InformationSet("get q46 visibility", "thriver", "mcrhci", get_q46_visibility),
                        InformationSet("validate q46 visibility = " + str(q46_visibility_expected), "mcrhci", "hcitracer", validate_q46_visibility),
                        InformationSet("get q45 visibility", "thriver", "mcrhci", get_q45_visibility),
                        InformationSet("validate q45 visibility = " + str(q45_visibility_expected), "mcrhci", "hcitracer", validate_q45_visibility),
                        InformationSet("get bts3_layout_ps_canbus_status_txt visibility", "thriver", "mcrhci", get_bts3_layout_ps_canbus_status_txt_visibility),
                        # Bug: Not able to check visibility of bts3_layout_ps_canbus_status_txt, there are 4 objects with the same name - To be covered when TMMI is updated
                        # InformationSet("validate bts3_layout_ps_canbus_status_txt visibility = " + str(bts3_layout_ps_canbus_status_txt_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_ps_canbus_status_txt_visibility),
                        InformationSet("set mcr_ecubtcu_sstech_ps_status = "+ str(mcr_ecubtcu_sstech_ps_status_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_sstech_ps_status_1),
                        InformationSet("get bts3_layout_ps_canbus_status_ind subobject_name", "thriver", "mcrhci", get_bts3_layout_ps_canbus_status_ind_subobject_name),
                        InformationSet("validate bts3_layout_ps_canbus_status_ind subobject_name = " + str(bts3_layout_ps_canbus_status_ind_subobject_name_expected), "mcrhci", "hcitracer", validate_bts3_layout_ps_canbus_status_ind_subobject_name),
                        InformationSet("set mcr_acu_selectiong12_status = "+ str(mcr_acu_selectiong12_status_init_1), "thriver", "mcrhci", set_mcr_acu_selectiong12_status_1),
                        InformationSet("get bts3_layout_gantry12_selection_txt foreground_color", "thriver", "mcrhci", get_bts3_layout_gantry12_selection_txt_foreground_color),
                        InformationSet("validate bts3_layout_gantry12_selection_txt foreground_color = " + str(bts3_layout_gantry12_selection_txt_foreground_color_expected), "mcrhci", "hcitracer", validate_bts3_layout_gantry12_selection_txt_foreground_color),
                        InformationSet("set mcr_acu_selectiong12_status = "+ str(mcr_acu_selectiong12_status_init_2), "thriver", "mcrhci", set_mcr_acu_selectiong12_status_2),
                        InformationSet("get bts3_layout_gantry12_selection_ind subobject_name", "thriver", "mcrhci", get_bts3_layout_gantry12_selection_ind_subobject_name),
                        InformationSet("validate bts3_layout_gantry12_selection_ind subobject_name = " + str(bts3_layout_gantry12_selection_ind_subobject_name_expected), "mcrhci", "hcitracer", validate_bts3_layout_gantry12_selection_ind_subobject_name),
                        InformationSet("set mcr_ecubtcu_bpme3_instatus = "+ str(mcr_ecubtcu_bpme3_instatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpme3_instatus_1),
                        InformationSet("get bts3_layout_bpme3_in visibility", "thriver", "mcrhci", get_bts3_layout_bpme3_in_visibility),
                        InformationSet("validate bts3_layout_bpme3_in visibility = " + str(bts3_layout_bpme3_in_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bpme3_in_visibility),
                        InformationSet("get bts3_layout_bpme3_out_btn visibility", "thriver", "mcrhci", get_bts3_layout_bpme3_out_btn_visibility),
                        InformationSet("validate bts3_layout_bpme3_out_btn visibility = " + str(bts3_layout_bpme3_out_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bpme3_out_btn_visibility),
                        InformationSet("get bts3_layout_bpme3_in_btn visibility", "thriver", "mcrhci", get_bts3_layout_bpme3_in_btn_visibility),
                        InformationSet("validate bts3_layout_bpme3_in_btn visibility = " + str(bts3_layout_bpme3_in_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bpme3_in_btn_visibility),
                        InformationSet("set mcr_ecubtcu_bpme3_instatus = "+ str(mcr_ecubtcu_bpme3_instatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpme3_instatus_2),
                        InformationSet("get bts3_layout_bpme3_in_led visibility", "thriver", "mcrhci", get_bts3_layout_bpme3_in_led_visibility),
                        InformationSet("validate bts3_layout_bpme3_in_led visibility = " + str(bts3_layout_bpme3_in_led_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bpme3_in_led_visibility),
                        InformationSet("set mcr_ecubtcu_bpme3_outstatus = "+ str(mcr_ecubtcu_bpme3_outstatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpme3_outstatus_1),
                        InformationSet("get bts3_layout_bpme3_out_led visibility", "thriver", "mcrhci", get_bts3_layout_bpme3_out_led_visibility),
                        InformationSet("validate bts3_layout_bpme3_out_led visibility = " + str(bts3_layout_bpme3_out_led_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bpme3_out_led_visibility),
                        InformationSet("set mcr_ecubtcu_bpme3_outstatus = "+ str(mcr_ecubtcu_bpme3_outstatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpme3_outstatus_2),
                        InformationSet("get bts3_layout_bpme3_out visibility", "thriver", "mcrhci", get_bts3_layout_bpme3_out_visibility),
                        InformationSet("validate bts3_layout_bpme3_out visibility = " + str(bts3_layout_bpme3_out_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bpme3_out_visibility),
                        InformationSet("set mcr_ecubtcu_bpme1_instatus = "+ str(mcr_ecubtcu_bpme1_instatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpme1_instatus_1),
                        InformationSet("get bts3_layout_bpme1_in visibility", "thriver", "mcrhci", get_bts3_layout_bpme1_in_visibility),
                        InformationSet("validate bts3_layout_bpme1_in visibility = " + str(bts3_layout_bpme1_in_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bpme1_in_visibility),
                        InformationSet("get bts3_layout_bpme1_out_btn visibility", "thriver", "mcrhci", get_bts3_layout_bpme1_out_btn_visibility),
                        InformationSet("validate bts3_layout_bpme1_out_btn visibility = " + str(bts3_layout_bpme1_out_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bpme1_out_btn_visibility),
                        InformationSet("get bts3_layout_bpme1_in_btn visibility", "thriver", "mcrhci", get_bts3_layout_bpme1_in_btn_visibility),
                        InformationSet("validate bts3_layout_bpme1_in_btn visibility = " + str(bts3_layout_bpme1_in_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bpme1_in_btn_visibility),
                        InformationSet("set mcr_ecubtcu_bpme1_instatus = "+ str(mcr_ecubtcu_bpme1_instatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpme1_instatus_2),
                        InformationSet("get bts3_layout_bpme1_in_led visibility", "thriver", "mcrhci", get_bts3_layout_bpme1_in_led_visibility),
                        InformationSet("validate bts3_layout_bpme1_in_led visibility = " + str(bts3_layout_bpme1_in_led_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bpme1_in_led_visibility),
                        InformationSet("set mcr_ecubtcu_bpme1_outstatus = "+ str(mcr_ecubtcu_bpme1_outstatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpme1_outstatus_1),
                        InformationSet("get bts3_layout_bpme1_out_led visibility", "thriver", "mcrhci", get_bts3_layout_bpme1_out_led_visibility),
                        InformationSet("validate bts3_layout_bpme1_out_led visibility = " + str(bts3_layout_bpme1_out_led_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bpme1_out_led_visibility),
                        InformationSet("set mcr_ecubtcu_bpme1_outstatus = "+ str(mcr_ecubtcu_bpme1_outstatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpme1_outstatus_2),
                        InformationSet("get bts3_layout_bpme1_out visibility", "thriver", "mcrhci", get_bts3_layout_bpme1_out_visibility),
                        InformationSet("validate bts3_layout_bpme1_out visibility = " + str(bts3_layout_bpme1_out_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bpme1_out_visibility),
                        InformationSet("get bts3_layout_bts2_layout_btn visibility", "thriver", "mcrhci", get_bts3_layout_bts2_layout_btn_visibility),
                        # Bug: cannot get the visibility of bts3_layout_bts2_layout_btn
                        # InformationSet("validate bts3_layout_bts2_layout_btn visibility = " + str(bts3_layout_bts2_layout_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bts2_layout_btn_visibility),
                        InformationSet("get bts3_layout_hidden_obj visibility", "thriver", "mcrhci", get_bts3_layout_hidden_obj_visibility),
                        InformationSet("validate bts3_layout_hidden_obj visibility = " + str(bts3_layout_hidden_obj_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_hidden_obj_visibility),
                        InformationSet("get b9 visibility", "thriver", "mcrhci", get_b9_visibility),
                        # Bug: cannot get the visibility of b9
                        # InformationSet("validate b9 visibility = " + str(b9_visibility_expected), "mcrhci", "hcitracer", validate_b9_visibility),
                        InformationSet("get q0m4 visibility", "thriver", "mcrhci", get_q0m4_visibility),
                        InformationSet("validate q0m4 visibility = " + str(q0m4_visibility_expected), "mcrhci", "hcitracer", validate_q0m4_visibility),
                        InformationSet("get q1m4 visibility", "thriver", "mcrhci", get_q1m4_visibility),
                        InformationSet("validate q1m4 visibility = " + str(q1m4_visibility_expected), "mcrhci", "hcitracer", validate_q1m4_visibility),
                        InformationSet("get q50 visibility", "thriver", "mcrhci", get_q50_visibility),
                        InformationSet("validate q50 visibility = " + str(q50_visibility_expected), "mcrhci", "hcitracer", validate_q50_visibility),
                        InformationSet("get q48 visibility", "thriver", "mcrhci", get_q48_visibility),
                        InformationSet("validate q48 visibility = " + str(q48_visibility_expected), "mcrhci", "hcitracer", validate_q48_visibility),
                        InformationSet("get q49 visibility", "thriver", "mcrhci", get_q49_visibility),
                        InformationSet("validate q49 visibility = " + str(q49_visibility_expected), "mcrhci", "hcitracer", validate_q49_visibility),
                        InformationSet("get SC4A visibility", "thriver", "mcrhci", get_SC4A_visibility),
                        InformationSet("validate SC4A visibility = " + str(SC4A_visibility_expected), "mcrhci", "hcitracer", validate_SC4A_visibility),
                        InformationSet("set mcr_ecubtcu_bpme2_outstatus = "+ str(mcr_ecubtcu_bpme2_outstatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpme2_outstatus_1),
                        InformationSet("get bts3_layout_bpme2_out visibility", "thriver", "mcrhci", get_bts3_layout_bpme2_out_visibility),
                        InformationSet("validate bts3_layout_bpme2_out visibility = " + str(bts3_layout_bpme2_out_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bpme2_out_visibility),
                        InformationSet("set mcr_ecubtcu_bpme2_instatus = "+ str(mcr_ecubtcu_bpme2_instatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpme2_instatus_1),
                        InformationSet("get bts3_layout_bpme2_in visibility", "thriver", "mcrhci", get_bts3_layout_bpme2_in_visibility),
                        InformationSet("validate bts3_layout_bpme2_in visibility = " + str(bts3_layout_bpme2_in_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bpme2_in_visibility),
                        InformationSet("get bts3_layout_bpme2_out_btn visibility", "thriver", "mcrhci", get_bts3_layout_bpme2_out_btn_visibility),
                        InformationSet("validate bts3_layout_bpme2_out_btn visibility = " + str(bts3_layout_bpme2_out_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bpme2_out_btn_visibility),
                        InformationSet("get bts3_layout_bpme2_in_btn visibility", "thriver", "mcrhci", get_bts3_layout_bpme2_in_btn_visibility),
                        InformationSet("validate bts3_layout_bpme2_in_btn visibility = " + str(bts3_layout_bpme2_in_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bpme2_in_btn_visibility),
                        InformationSet("set mcr_ecubtcu_bpme2_instatus = "+ str(mcr_ecubtcu_bpme2_instatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpme2_instatus_2),
                        InformationSet("get bts3_layout_bpme2_in_led visibility", "thriver", "mcrhci", get_bts3_layout_bpme2_in_led_visibility),
                        InformationSet("validate bts3_layout_bpme2_in_led visibility = " + str(bts3_layout_bpme2_in_led_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bpme2_in_led_visibility),
                        InformationSet("set mcr_ecubtcu_bpme2_outstatus = "+ str(mcr_ecubtcu_bpme2_outstatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpme2_outstatus_2),
                        InformationSet("get bts3_layout_bpme2_out_led visibility", "thriver", "mcrhci", get_bts3_layout_bpme2_out_led_visibility),
                        InformationSet("validate bts3_layout_bpme2_out_led visibility = " + str(bts3_layout_bpme2_out_led_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bpme2_out_led_visibility),
                        InformationSet("get SC4B visibility", "thriver", "mcrhci", get_SC4B_visibility),
                        InformationSet("validate SC4B visibility = " + str(SC4B_visibility_expected), "mcrhci", "hcitracer", validate_SC4B_visibility),
                        InformationSet("get SC6A visibility", "thriver", "mcrhci", get_SC6A_visibility),
                        InformationSet("validate SC6A visibility = " + str(SC6A_visibility_expected), "mcrhci", "hcitracer", validate_SC6A_visibility),
                        InformationSet("get b10 visibility", "thriver", "mcrhci", get_b10_visibility),
                        InformationSet("validate b10 visibility = " + str(b10_visibility_expected), "mcrhci", "hcitracer", validate_b10_visibility),
                        InformationSet("get q1m3 visibility", "thriver", "mcrhci", get_q1m3_visibility),
                        InformationSet("validate q1m3 visibility = " + str(q1m3_visibility_expected), "mcrhci", "hcitracer", validate_q1m3_visibility),
                        InformationSet("get q2m3 visibility", "thriver", "mcrhci", get_q2m3_visibility),
                        InformationSet("validate q2m3 visibility = " + str(q2m3_visibility_expected), "mcrhci", "hcitracer", validate_q2m3_visibility),
                        InformationSet("set tr3_scu_b9_on_enable = "+ str(tr3_scu_b9_on_enable_init_1), "thriver", "mcrhci", set_tr3_scu_b9_on_enable_1),
                        InformationSet("get bts3_layout_safety_interlocks_btn foreground_color", "thriver", "mcrhci", get_bts3_layout_safety_interlocks_btn_foreground_color),
                        InformationSet("validate bts3_layout_safety_interlocks_btn foreground_color = " + str(bts3_layout_safety_interlocks_btn_foreground_color_expected), "mcrhci", "hcitracer", validate_bts3_layout_safety_interlocks_btn_foreground_color),
                        InformationSet("get bts3_layout_bpms1_in visibility", "thriver", "mcrhci", get_bts3_layout_bpms1_in_visibility),
                        InformationSet("validate bts3_layout_bpms1_in visibility = " + str(bts3_layout_bpms1_in_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bpms1_in_visibility),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []