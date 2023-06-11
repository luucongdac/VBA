
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

class SETUP_VALIDATE_BTS3_LAYOUT_SCREEN(ClinicalIntegrationTestProcedure):
    # default variable values
    name = "Confirm that MCR_Service_BTS3_Layout (bts3_layout.v) is displayed"
    mcr_ecubtcu_bcm4_data_type_init_1 = 1.0
    bts1_layout_bs3_nA1_txt_visibility_expected = "1"
    bts1_layout_bs3_out_btn_visibility_expected = "1"
    q40_visibility_expected = "1"
    q41_visibility_expected = "1"
    bts3_layout_ps_canbus_status_txt_visibility_expected = "1"
    mcr_ecubtcu_sstech_ps_status_init_1 = 1.0
    bts3_layout_ps_canbus_status_ind_subobject_name_expected = "iba_check_ok.sd"
    q43_visibility_expected = "1"
    q44_visibility_expected = "1"
    q42_visibility_expected = "1"
    sc1a_visibility_expected = "1"
    mcr_acu_selectiong12_status_init_1 = True
    bts3_layout_gantry12_selection_txt_foreground_color_expected = "24"
    mcr_acu_selectiong12_status_init_2 = False
    bts3_layout_gantry12_selection_ind_subobject_name_expected = "iba_check_ok.sd"
    bts1_layout_bss_in_btn_visibility_expected = "1"
    mcr_ecubtcu_bsc1_instatus_init_1 = True
    bts3_layout_bsc1_in_led_visibility_expected = "1"
    mcr_ecubtcu_bsc1_outstatus_init_1 = True
    bts3_layout_bsc1_out_led_visibility_expected = "1"
    mcr_ecubtcu_bcm4_data_type_init_2 = 1.0
    bts1_layout_bs3_nA_txt_visibility_expected = "0"
    bts3_layout_bts2_layout_btn_visibility_expected = "1"
    tr3_scu_beamstop1_out_enabled_init_1 = True
    bts3_layout_safety_interlocks_btn_foreground_color_expected = "112"
    bts1_layout_hidden_obj_visibility_expected = "1"
    b9_visibility_expected = "1"
    mcr_ecubtcu_bsc1_outstatus_init_2 = True
    bts3_layout_bsc1_out_visibility_expected = "1"
    mcr_ecubtcu_bsc1_instatus_init_2 = True
    bts3_layout_bsc1_in_visibility_expected = "1"
    mcr_ecubtcu_bsc2_instatus_init_1 = True
    bts3_layout_bsc2_in_visibility_expected = "1"
    mcr_ecubtcu_bsc2_outstatus_init_1 = True
    bts3_layout_bsc2_out_visibility_expected = "1"
    mcr_ecubtcu_bsc2_instatus_init_2 = True
    bts3_layout_bsc2_in_led_visibility_expected = "1"
    mcr_ecubtcu_bsc2_outstatus_init_2 = True
    bts3_layout_bsc2_out_led_visibility_expected = "1"
    SC1B_visibility_expected = "1"
    mcr_ecubtcu_bpmc1_outstatus_init_1 = True
    bts3_layout_bpmc1_out_visibility_expected = "1"
    mcr_ecubtcu_bpmc1_instatus_init_1 = True
    bts3_layout_bpmc1_in_visibility_expected = "1"
    SC2A_visibility_expected = "1"
    bts3_layout_bpmc1_out_btn_visibility_expected = "1"
    bts3_layout_bpmc1_in_btn_visibility_expected = "1"
    mcr_ecubtcu_bpmc1_instatus_init_2 = True
    bts3_layout_bpmc1_in_led_visibility_expected = "1"
    mcr_ecubtcu_bpmc1_outstatus_init_2 = True
    bts3_layout_bpmc1_out_led_visibility_expected = "1"
    mcr_ecubtcu_bpmc2_outstatus_init_1 = True
    bts3_layout_bpmc2_out_visibility_expected = "1"
    mcr_ecubtcu_bpmc2_instatus_init_1 = True
    bts3_layout_bpmc2_in_visibility_expected = "1"
    bts3_layout_bpmc2_out_btn_visibility_expected = "1"
    bts3_layout_bpmc2_in_btn_visibility_expected = "1"
    mcr_ecubtcu_bpmc2_instatus_init_2 = True
    bts3_layout_bpmc2_in_led_visibility_expected = "1"
    mcr_ecubtcu_bpmc2_outstatus_init_2 = True
    bts3_layout_bpmc2_out_led_visibility_expected = "1"

    def __init__(self, test):
        cls = type(self)
        name = cls.__name__
        mcr_ecubtcu_bcm4_data_type_init_1 = cls.mcr_ecubtcu_bcm4_data_type_init_1
        bts1_layout_bs3_nA1_txt_visibility_expected = cls.bts1_layout_bs3_nA1_txt_visibility_expected
        bts1_layout_bs3_out_btn_visibility_expected = cls.bts1_layout_bs3_out_btn_visibility_expected
        q40_visibility_expected = cls.q40_visibility_expected
        q41_visibility_expected = cls.q41_visibility_expected
        bts3_layout_ps_canbus_status_txt_visibility_expected = cls.bts3_layout_ps_canbus_status_txt_visibility_expected
        mcr_ecubtcu_sstech_ps_status_init_1 = cls.mcr_ecubtcu_sstech_ps_status_init_1
        bts3_layout_ps_canbus_status_ind_subobject_name_expected = cls.bts3_layout_ps_canbus_status_ind_subobject_name_expected
        q43_visibility_expected = cls.q43_visibility_expected
        q44_visibility_expected = cls.q44_visibility_expected
        q42_visibility_expected = cls.q42_visibility_expected
        sc1a_visibility_expected = cls.sc1a_visibility_expected
        mcr_acu_selectiong12_status_init_1 = cls.mcr_acu_selectiong12_status_init_1
        bts3_layout_gantry12_selection_txt_foreground_color_expected = cls.bts3_layout_gantry12_selection_txt_foreground_color_expected
        mcr_acu_selectiong12_status_init_2 = cls.mcr_acu_selectiong12_status_init_2
        bts3_layout_gantry12_selection_ind_subobject_name_expected = cls.bts3_layout_gantry12_selection_ind_subobject_name_expected
        bts1_layout_bss_in_btn_visibility_expected = cls.bts1_layout_bss_in_btn_visibility_expected
        mcr_ecubtcu_bsc1_instatus_init_1 = cls.mcr_ecubtcu_bsc1_instatus_init_1
        bts3_layout_bsc1_in_led_visibility_expected = cls.bts3_layout_bsc1_in_led_visibility_expected
        mcr_ecubtcu_bsc1_outstatus_init_1 = cls.mcr_ecubtcu_bsc1_outstatus_init_1
        bts3_layout_bsc1_out_led_visibility_expected = cls.bts3_layout_bsc1_out_led_visibility_expected
        mcr_ecubtcu_bcm4_data_type_init_2 = cls.mcr_ecubtcu_bcm4_data_type_init_2
        bts1_layout_bs3_nA_txt_visibility_expected = cls.bts1_layout_bs3_nA_txt_visibility_expected
        bts3_layout_bts2_layout_btn_visibility_expected = cls.bts3_layout_bts2_layout_btn_visibility_expected
        tr3_scu_beamstop1_out_enabled_init_1 = cls.tr3_scu_beamstop1_out_enabled_init_1
        bts3_layout_safety_interlocks_btn_foreground_color_expected = cls.bts3_layout_safety_interlocks_btn_foreground_color_expected
        bts1_layout_hidden_obj_visibility_expected = cls.bts1_layout_hidden_obj_visibility_expected
        b9_visibility_expected = cls.b9_visibility_expected
        mcr_ecubtcu_bsc1_outstatus_init_2 = cls.mcr_ecubtcu_bsc1_outstatus_init_2
        bts3_layout_bsc1_out_visibility_expected = cls.bts3_layout_bsc1_out_visibility_expected
        mcr_ecubtcu_bsc1_instatus_init_2 = cls.mcr_ecubtcu_bsc1_instatus_init_2
        bts3_layout_bsc1_in_visibility_expected = cls.bts3_layout_bsc1_in_visibility_expected
        mcr_ecubtcu_bsc2_instatus_init_1 = cls.mcr_ecubtcu_bsc2_instatus_init_1
        bts3_layout_bsc2_in_visibility_expected = cls.bts3_layout_bsc2_in_visibility_expected
        mcr_ecubtcu_bsc2_outstatus_init_1 = cls.mcr_ecubtcu_bsc2_outstatus_init_1
        bts3_layout_bsc2_out_visibility_expected = cls.bts3_layout_bsc2_out_visibility_expected
        mcr_ecubtcu_bsc2_instatus_init_2 = cls.mcr_ecubtcu_bsc2_instatus_init_2
        bts3_layout_bsc2_in_led_visibility_expected = cls.bts3_layout_bsc2_in_led_visibility_expected
        mcr_ecubtcu_bsc2_outstatus_init_2 = cls.mcr_ecubtcu_bsc2_outstatus_init_2
        bts3_layout_bsc2_out_led_visibility_expected = cls.bts3_layout_bsc2_out_led_visibility_expected
        SC1B_visibility_expected = cls.SC1B_visibility_expected
        mcr_ecubtcu_bpmc1_outstatus_init_1 = cls.mcr_ecubtcu_bpmc1_outstatus_init_1
        bts3_layout_bpmc1_out_visibility_expected = cls.bts3_layout_bpmc1_out_visibility_expected
        mcr_ecubtcu_bpmc1_instatus_init_1 = cls.mcr_ecubtcu_bpmc1_instatus_init_1
        bts3_layout_bpmc1_in_visibility_expected = cls.bts3_layout_bpmc1_in_visibility_expected
        SC2A_visibility_expected = cls.SC2A_visibility_expected
        bts3_layout_bpmc1_out_btn_visibility_expected = cls.bts3_layout_bpmc1_out_btn_visibility_expected
        bts3_layout_bpmc1_in_btn_visibility_expected = cls.bts3_layout_bpmc1_in_btn_visibility_expected
        mcr_ecubtcu_bpmc1_instatus_init_2 = cls.mcr_ecubtcu_bpmc1_instatus_init_2
        bts3_layout_bpmc1_in_led_visibility_expected = cls.bts3_layout_bpmc1_in_led_visibility_expected
        mcr_ecubtcu_bpmc1_outstatus_init_2 = cls.mcr_ecubtcu_bpmc1_outstatus_init_2
        bts3_layout_bpmc1_out_led_visibility_expected = cls.bts3_layout_bpmc1_out_led_visibility_expected
        mcr_ecubtcu_bpmc2_outstatus_init_1 = cls.mcr_ecubtcu_bpmc2_outstatus_init_1
        bts3_layout_bpmc2_out_visibility_expected = cls.bts3_layout_bpmc2_out_visibility_expected
        mcr_ecubtcu_bpmc2_instatus_init_1 = cls.mcr_ecubtcu_bpmc2_instatus_init_1
        bts3_layout_bpmc2_in_visibility_expected = cls.bts3_layout_bpmc2_in_visibility_expected
        bts3_layout_bpmc2_out_btn_visibility_expected = cls.bts3_layout_bpmc2_out_btn_visibility_expected
        bts3_layout_bpmc2_in_btn_visibility_expected = cls.bts3_layout_bpmc2_in_btn_visibility_expected
        mcr_ecubtcu_bpmc2_instatus_init_2 = cls.mcr_ecubtcu_bpmc2_instatus_init_2
        bts3_layout_bpmc2_in_led_visibility_expected = cls.bts3_layout_bpmc2_in_led_visibility_expected
        mcr_ecubtcu_bpmc2_outstatus_init_2 = cls.mcr_ecubtcu_bpmc2_outstatus_init_2
        bts3_layout_bpmc2_out_led_visibility_expected = cls.bts3_layout_bpmc2_out_led_visibility_expected

        #set initial values
        set_mcr_ecubtcu_bcm4_data_type_1 = MsgTypeNumeric("mcr_ecubtcu_bcm4_data_type", mcr_ecubtcu_bcm4_data_type_init_1)
        set_mcr_ecubtcu_sstech_ps_status_1 = MsgTypeNumeric("mcr_ecubtcu_sstech_ps_status", mcr_ecubtcu_sstech_ps_status_init_1)
        set_mcr_acu_selectiong12_status_1 = MsgTypeBoolean("mcr_acu_selectiong12_status", mcr_acu_selectiong12_status_init_1)
        set_mcr_acu_selectiong12_status_2 = MsgTypeBoolean("mcr_acu_selectiong12_status", mcr_acu_selectiong12_status_init_2)
        set_mcr_ecubtcu_bsc1_instatus_1 = MsgTypeBoolean("mcr_ecubtcu_bsc1_instatus", mcr_ecubtcu_bsc1_instatus_init_1)
        set_mcr_ecubtcu_bsc1_outstatus_1 = MsgTypeBoolean("mcr_ecubtcu_bsc1_outstatus", mcr_ecubtcu_bsc1_outstatus_init_1)
        set_mcr_ecubtcu_bcm4_data_type_2 = MsgTypeNumeric("mcr_ecubtcu_bcm4_data_type", mcr_ecubtcu_bcm4_data_type_init_2)
        set_tr3_scu_beamstop1_out_enabled_1 = MsgTypeBoolean("tr3_scu_beamstop1_out_enabled", tr3_scu_beamstop1_out_enabled_init_1)
        set_mcr_ecubtcu_bsc1_outstatus_2 = MsgTypeBoolean("mcr_ecubtcu_bsc1_outstatus", mcr_ecubtcu_bsc1_outstatus_init_2)
        set_mcr_ecubtcu_bsc1_instatus_2 = MsgTypeBoolean("mcr_ecubtcu_bsc1_instatus", mcr_ecubtcu_bsc1_instatus_init_2)
        set_mcr_ecubtcu_bsc2_instatus_1 = MsgTypeBoolean("mcr_ecubtcu_bsc2_instatus", mcr_ecubtcu_bsc2_instatus_init_1)
        set_mcr_ecubtcu_bsc2_outstatus_1 = MsgTypeBoolean("mcr_ecubtcu_bsc2_outstatus", mcr_ecubtcu_bsc2_outstatus_init_1)
        set_mcr_ecubtcu_bsc2_instatus_2 = MsgTypeBoolean("mcr_ecubtcu_bsc2_instatus", mcr_ecubtcu_bsc2_instatus_init_2)
        set_mcr_ecubtcu_bsc2_outstatus_2 = MsgTypeBoolean("mcr_ecubtcu_bsc2_outstatus", mcr_ecubtcu_bsc2_outstatus_init_2)
        set_mcr_ecubtcu_bpmc1_outstatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpmc1_outstatus", mcr_ecubtcu_bpmc1_outstatus_init_1)
        set_mcr_ecubtcu_bpmc1_instatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpmc1_instatus", mcr_ecubtcu_bpmc1_instatus_init_1)
        set_mcr_ecubtcu_bpmc1_instatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpmc1_instatus", mcr_ecubtcu_bpmc1_instatus_init_2)
        set_mcr_ecubtcu_bpmc1_outstatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpmc1_outstatus", mcr_ecubtcu_bpmc1_outstatus_init_2)
        set_mcr_ecubtcu_bpmc2_outstatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpmc2_outstatus", mcr_ecubtcu_bpmc2_outstatus_init_1)
        set_mcr_ecubtcu_bpmc2_instatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpmc2_instatus", mcr_ecubtcu_bpmc2_instatus_init_1)
        set_mcr_ecubtcu_bpmc2_instatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpmc2_instatus", mcr_ecubtcu_bpmc2_instatus_init_2)
        set_mcr_ecubtcu_bpmc2_outstatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpmc2_outstatus", mcr_ecubtcu_bpmc2_outstatus_init_2)

        #get values
        get_bts1_layout_bs3_nA1_txt_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_bs3_nA1_txt")
        get_bts1_layout_bs3_out_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_bs3_out_btn")
        get_q40_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q40")
        get_q41_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q41")
        get_bts3_layout_ps_canbus_status_txt_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_ps_canbus_status_txt")
        get_bts3_layout_ps_canbus_status_ind_subobject_name = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "bts3_layout_ps_canbus_status_ind")
        get_q43_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q43")
        get_q44_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q44")
        get_q42_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q42")
        get_sc1a_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "sc1a")
        get_bts3_layout_gantry12_selection_txt_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "bts3_layout_gantry12_selection_txt")
        get_bts3_layout_gantry12_selection_ind_subobject_name = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "bts3_layout_gantry12_selection_ind")
        get_bts1_layout_bss_in_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_bss_in_btn")
        get_bts3_layout_bsc1_in_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bsc1_in_led")
        get_bts3_layout_bsc1_out_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bsc1_out_led")
        get_bts1_layout_bs3_nA_txt_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_bs3_nA_txt")
        get_bts3_layout_bts2_layout_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bts2_layout_btn")
        get_bts3_layout_safety_interlocks_btn_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "bts3_layout_safety_interlocks_btn")
        get_bts1_layout_hidden_obj_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_hidden_obj")
        get_b9_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "b9")
        get_bts3_layout_bsc1_out_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bsc1_out")
        get_bts3_layout_bsc1_in_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bsc1_in")
        get_bts3_layout_bsc2_in_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bsc2_in")
        get_bts3_layout_bsc2_out_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bsc2_out")
        get_bts3_layout_bsc2_in_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bsc2_in_led")
        get_bts3_layout_bsc2_out_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bsc2_out_led")
        get_SC1B_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "SC1B")
        get_bts3_layout_bpmc1_out_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bpmc1_out")
        get_bts3_layout_bpmc1_in_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bpmc1_in")
        get_SC2A_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "SC2A")
        get_bts3_layout_bpmc1_out_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bpmc1_out_btn")
        get_bts3_layout_bpmc1_in_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bpmc1_in_btn")
        get_bts3_layout_bpmc1_in_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bpmc1_in_led")
        get_bts3_layout_bpmc1_out_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bpmc1_out_led")
        get_bts3_layout_bpmc2_out_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bpmc2_out")
        get_bts3_layout_bpmc2_in_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bpmc2_in")
        get_bts3_layout_bpmc2_out_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bpmc2_out_btn")
        get_bts3_layout_bpmc2_in_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bpmc2_in_btn")
        get_bts3_layout_bpmc2_in_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bpmc2_in_led")
        get_bts3_layout_bpmc2_out_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_layout_bpmc2_out_led")

        #validate
        validate_bts1_layout_bs3_nA1_txt_visibility = MsgTypeString("bts1_layout_bs3_nA1_txt:TMMI_MCR_IS_VISIBLE", value=bts1_layout_bs3_nA1_txt_visibility_expected)
        validate_bts1_layout_bs3_out_btn_visibility = MsgTypeString("bts1_layout_bs3_out_btn:TMMI_MCR_IS_VISIBLE", value=bts1_layout_bs3_out_btn_visibility_expected)
        validate_q40_visibility = MsgTypeString("q40:TMMI_MCR_IS_VISIBLE", value=q40_visibility_expected)
        validate_q41_visibility = MsgTypeString("q41:TMMI_MCR_IS_VISIBLE", value=q41_visibility_expected)
        validate_bts3_layout_ps_canbus_status_txt_visibility = MsgTypeString("bts3_layout_ps_canbus_status_txt:TMMI_MCR_IS_VISIBLE", value=bts3_layout_ps_canbus_status_txt_visibility_expected)
        validate_bts3_layout_ps_canbus_status_ind_subobject_name = MsgTypeString("bts3_layout_ps_canbus_status_ind:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=bts3_layout_ps_canbus_status_ind_subobject_name_expected)
        validate_q43_visibility = MsgTypeString("q43:TMMI_MCR_IS_VISIBLE", value=q43_visibility_expected)
        validate_q44_visibility = MsgTypeString("q44:TMMI_MCR_IS_VISIBLE", value=q44_visibility_expected)
        validate_q42_visibility = MsgTypeString("q42:TMMI_MCR_IS_VISIBLE", value=q42_visibility_expected)
        validate_sc1a_visibility = MsgTypeString("sc1a:TMMI_MCR_IS_VISIBLE", value=sc1a_visibility_expected)
        validate_bts3_layout_gantry12_selection_txt_foreground_color = MsgTypeString("bts3_layout_gantry12_selection_txt:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=bts3_layout_gantry12_selection_txt_foreground_color_expected)
        validate_bts3_layout_gantry12_selection_ind_subobject_name = MsgTypeString("bts3_layout_gantry12_selection_ind:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=bts3_layout_gantry12_selection_ind_subobject_name_expected)
        validate_bts1_layout_bss_in_btn_visibility = MsgTypeString("bts1_layout_bss_in_btn:TMMI_MCR_IS_VISIBLE", value=bts1_layout_bss_in_btn_visibility_expected)
        validate_bts3_layout_bsc1_in_led_visibility = MsgTypeString("bts3_layout_bsc1_in_led:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bsc1_in_led_visibility_expected)
        validate_bts3_layout_bsc1_out_led_visibility = MsgTypeString("bts3_layout_bsc1_out_led:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bsc1_out_led_visibility_expected)
        validate_bts1_layout_bs3_nA_txt_visibility = MsgTypeString("bts1_layout_bs3_nA_txt:TMMI_MCR_IS_VISIBLE", value=bts1_layout_bs3_nA_txt_visibility_expected)
        validate_bts3_layout_bts2_layout_btn_visibility = MsgTypeString("bts3_layout_bts2_layout_btn:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bts2_layout_btn_visibility_expected)
        validate_bts3_layout_safety_interlocks_btn_foreground_color = MsgTypeString("bts3_layout_safety_interlocks_btn:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=bts3_layout_safety_interlocks_btn_foreground_color_expected)
        validate_bts1_layout_hidden_obj_visibility = MsgTypeString("bts1_layout_hidden_obj:TMMI_MCR_IS_VISIBLE", value=bts1_layout_hidden_obj_visibility_expected)
        validate_b9_visibility = MsgTypeString("b9:TMMI_MCR_IS_VISIBLE", value=b9_visibility_expected)
        validate_bts3_layout_bsc1_out_visibility = MsgTypeString("bts3_layout_bsc1_out:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bsc1_out_visibility_expected)
        validate_bts3_layout_bsc1_in_visibility = MsgTypeString("bts3_layout_bsc1_in:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bsc1_in_visibility_expected)
        validate_bts3_layout_bsc2_in_visibility = MsgTypeString("bts3_layout_bsc2_in:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bsc2_in_visibility_expected)
        validate_bts3_layout_bsc2_out_visibility = MsgTypeString("bts3_layout_bsc2_out:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bsc2_out_visibility_expected)
        validate_bts3_layout_bsc2_in_led_visibility = MsgTypeString("bts3_layout_bsc2_in_led:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bsc2_in_led_visibility_expected)
        validate_bts3_layout_bsc2_out_led_visibility = MsgTypeString("bts3_layout_bsc2_out_led:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bsc2_out_led_visibility_expected)
        validate_SC1B_visibility = MsgTypeString("SC1B:TMMI_MCR_IS_VISIBLE", value=SC1B_visibility_expected)
        validate_bts3_layout_bpmc1_out_visibility = MsgTypeString("bts3_layout_bpmc1_out:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bpmc1_out_visibility_expected)
        validate_bts3_layout_bpmc1_in_visibility = MsgTypeString("bts3_layout_bpmc1_in:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bpmc1_in_visibility_expected)
        validate_SC2A_visibility = MsgTypeString("SC2A:TMMI_MCR_IS_VISIBLE", value=SC2A_visibility_expected)
        validate_bts3_layout_bpmc1_out_btn_visibility = MsgTypeString("bts3_layout_bpmc1_out_btn:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bpmc1_out_btn_visibility_expected)
        validate_bts3_layout_bpmc1_in_btn_visibility = MsgTypeString("bts3_layout_bpmc1_in_btn:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bpmc1_in_btn_visibility_expected)
        validate_bts3_layout_bpmc1_in_led_visibility = MsgTypeString("bts3_layout_bpmc1_in_led:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bpmc1_in_led_visibility_expected)
        validate_bts3_layout_bpmc1_out_led_visibility = MsgTypeString("bts3_layout_bpmc1_out_led:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bpmc1_out_led_visibility_expected)
        validate_bts3_layout_bpmc2_out_visibility = MsgTypeString("bts3_layout_bpmc2_out:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bpmc2_out_visibility_expected)
        validate_bts3_layout_bpmc2_in_visibility = MsgTypeString("bts3_layout_bpmc2_in:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bpmc2_in_visibility_expected)
        validate_bts3_layout_bpmc2_out_btn_visibility = MsgTypeString("bts3_layout_bpmc2_out_btn:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bpmc2_out_btn_visibility_expected)
        validate_bts3_layout_bpmc2_in_btn_visibility = MsgTypeString("bts3_layout_bpmc2_in_btn:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bpmc2_in_btn_visibility_expected)
        validate_bts3_layout_bpmc2_in_led_visibility = MsgTypeString("bts3_layout_bpmc2_in_led:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bpmc2_in_led_visibility_expected)
        validate_bts3_layout_bpmc2_out_led_visibility = MsgTypeString("bts3_layout_bpmc2_out_led:TMMI_MCR_IS_VISIBLE", value=bts3_layout_bpmc2_out_led_visibility_expected)

        info_exchange = [
                        InformationSet("set mcr_ecubtcu_bcm4_data_type = "+ str(mcr_ecubtcu_bcm4_data_type_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bcm4_data_type_1),
                        InformationSet("get bts1_layout_bs3_nA1_txt visibility", "thriver", "mcrhci", get_bts1_layout_bs3_nA1_txt_visibility),
                        # Bug: Not able to check visibility of bts1_layout_bs3_nA1_txt, there are 2 objects with the same name - To be covered when TMMI is updated
                        # InformationSet("validate bts1_layout_bs3_nA1_txt visibility = " + str(bts1_layout_bs3_nA1_txt_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_bs3_nA1_txt_visibility),
                        InformationSet("get bts1_layout_bs3_out_btn visibility", "thriver", "mcrhci", get_bts1_layout_bs3_out_btn_visibility),
                        # Bug: Not able to check visibility of bts3_layout_ps_canbus_status_txt, there are 4 objects with the same name - To be covered when TMMI is updated                        
                        # InformationSet("validate bts1_layout_bs3_out_btn visibility = " + str(bts1_layout_bs3_out_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_bs3_out_btn_visibility),
                        InformationSet("get q40 visibility", "thriver", "mcrhci", get_q40_visibility),
                        InformationSet("validate q40 visibility = " + str(q40_visibility_expected), "mcrhci", "hcitracer", validate_q40_visibility),
                        InformationSet("get q41 visibility", "thriver", "mcrhci", get_q41_visibility),
                        InformationSet("validate q41 visibility = " + str(q41_visibility_expected), "mcrhci", "hcitracer", validate_q41_visibility),
                        InformationSet("get bts3_layout_ps_canbus_status_txt visibility", "thriver", "mcrhci", get_bts3_layout_ps_canbus_status_txt_visibility),
                        InformationSet("validate bts3_layout_ps_canbus_status_txt visibility = " + str(bts3_layout_ps_canbus_status_txt_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_ps_canbus_status_txt_visibility),
                        InformationSet("set mcr_ecubtcu_sstech_ps_status = "+ str(mcr_ecubtcu_sstech_ps_status_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_sstech_ps_status_1),
                        InformationSet("get bts3_layout_ps_canbus_status_ind subobject_name", "thriver", "mcrhci", get_bts3_layout_ps_canbus_status_ind_subobject_name),
                        InformationSet("validate bts3_layout_ps_canbus_status_ind subobject_name = " + str(bts3_layout_ps_canbus_status_ind_subobject_name_expected), "mcrhci", "hcitracer", validate_bts3_layout_ps_canbus_status_ind_subobject_name),
                        InformationSet("get q43 visibility", "thriver", "mcrhci", get_q43_visibility),
                        InformationSet("validate q43 visibility = " + str(q43_visibility_expected), "mcrhci", "hcitracer", validate_q43_visibility),
                        InformationSet("get q44 visibility", "thriver", "mcrhci", get_q44_visibility),
                        InformationSet("validate q44 visibility = " + str(q44_visibility_expected), "mcrhci", "hcitracer", validate_q44_visibility),
                        InformationSet("get q42 visibility", "thriver", "mcrhci", get_q42_visibility),
                        InformationSet("validate q42 visibility = " + str(q42_visibility_expected), "mcrhci", "hcitracer", validate_q42_visibility),
                        InformationSet("get sc1a visibility", "thriver", "mcrhci", get_sc1a_visibility),
                        InformationSet("validate sc1a visibility = " + str(sc1a_visibility_expected), "mcrhci", "hcitracer", validate_sc1a_visibility),
                        InformationSet("set mcr_acu_selectiong12_status = "+ str(mcr_acu_selectiong12_status_init_1), "thriver", "mcrhci", set_mcr_acu_selectiong12_status_1),
                        InformationSet("get bts3_layout_gantry12_selection_txt foreground_color", "thriver", "mcrhci", get_bts3_layout_gantry12_selection_txt_foreground_color),
                        InformationSet("validate bts3_layout_gantry12_selection_txt foreground_color = " + str(bts3_layout_gantry12_selection_txt_foreground_color_expected), "mcrhci", "hcitracer", validate_bts3_layout_gantry12_selection_txt_foreground_color),
                        InformationSet("set mcr_acu_selectiong12_status = "+ str(mcr_acu_selectiong12_status_init_2), "thriver", "mcrhci", set_mcr_acu_selectiong12_status_2),
                        InformationSet("get bts3_layout_gantry12_selection_ind subobject_name", "thriver", "mcrhci", get_bts3_layout_gantry12_selection_ind_subobject_name),
                        InformationSet("validate bts3_layout_gantry12_selection_ind subobject_name = " + str(bts3_layout_gantry12_selection_ind_subobject_name_expected), "mcrhci", "hcitracer", validate_bts3_layout_gantry12_selection_ind_subobject_name),
                        InformationSet("get bts1_layout_bss_in_btn visibility", "thriver", "mcrhci", get_bts1_layout_bss_in_btn_visibility),
                        # Bug: Not able to check visibility of bts1_layout_bss_in_btn, there are 2 objects with the same name - To be covered when TMMI is updated
                        # InformationSet("validate bts1_layout_bss_in_btn visibility = " + str(bts1_layout_bss_in_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_bss_in_btn_visibility),
                        InformationSet("set mcr_ecubtcu_bsc1_instatus = "+ str(mcr_ecubtcu_bsc1_instatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bsc1_instatus_1),
                        InformationSet("get bts3_layout_bsc1_in_led visibility", "thriver", "mcrhci", get_bts3_layout_bsc1_in_led_visibility),
                        InformationSet("validate bts3_layout_bsc1_in_led visibility = " + str(bts3_layout_bsc1_in_led_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bsc1_in_led_visibility),
                        InformationSet("set mcr_ecubtcu_bsc1_outstatus = "+ str(mcr_ecubtcu_bsc1_outstatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bsc1_outstatus_1),
                        InformationSet("get bts3_layout_bsc1_out_led visibility", "thriver", "mcrhci", get_bts3_layout_bsc1_out_led_visibility),
                        InformationSet("validate bts3_layout_bsc1_out_led visibility = " + str(bts3_layout_bsc1_out_led_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bsc1_out_led_visibility),
                        InformationSet("set mcr_ecubtcu_bcm4_data_type = "+ str(mcr_ecubtcu_bcm4_data_type_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bcm4_data_type_2),
                        InformationSet("get bts1_layout_bs3_nA_txt visibility", "thriver", "mcrhci", get_bts1_layout_bs3_nA_txt_visibility),
                        # Bug: Not able to check visibility of bts1_layout_bs3_nA_txt, there are 2 objects with the same name - To be covered when TMMI is updated
                        # InformationSet("validate bts1_layout_bs3_nA_txt visibility = " + str(bts1_layout_bs3_nA_txt_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_bs3_nA_txt_visibility),
                        InformationSet("get bts3_layout_bts2_layout_btn visibility", "thriver", "mcrhci", get_bts3_layout_bts2_layout_btn_visibility),
                        InformationSet("validate bts3_layout_bts2_layout_btn visibility = " + str(bts3_layout_bts2_layout_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bts2_layout_btn_visibility),
                        InformationSet("set tr3_scu_beamstop1_out_enabled = "+ str(tr3_scu_beamstop1_out_enabled_init_1), "thriver", "mcrhci", set_tr3_scu_beamstop1_out_enabled_1),
                        InformationSet("get bts3_layout_safety_interlocks_btn foreground_color", "thriver", "mcrhci", get_bts3_layout_safety_interlocks_btn_foreground_color),
                        InformationSet("validate bts3_layout_safety_interlocks_btn foreground_color = " + str(bts3_layout_safety_interlocks_btn_foreground_color_expected), "mcrhci", "hcitracer", validate_bts3_layout_safety_interlocks_btn_foreground_color),
                        InformationSet("get bts1_layout_hidden_obj visibility", "thriver", "mcrhci", get_bts1_layout_hidden_obj_visibility),
                        # Bug: cannot get the visibility of bts1_layout_hidden_obj
                        # InformationSet("validate bts1_layout_hidden_obj visibility = " + str(bts1_layout_hidden_obj_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_hidden_obj_visibility),
                        InformationSet("get b9 visibility", "thriver", "mcrhci", get_b9_visibility),
                        # Bug: cannot get the visibility of b9
                        # InformationSet("validate b9 visibility = " + str(b9_visibility_expected), "mcrhci", "hcitracer", validate_b9_visibility),
                        InformationSet("set mcr_ecubtcu_bsc1_outstatus = "+ str(mcr_ecubtcu_bsc1_outstatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bsc1_outstatus_2),
                        InformationSet("get bts3_layout_bsc1_out visibility", "thriver", "mcrhci", get_bts3_layout_bsc1_out_visibility),
                        InformationSet("validate bts3_layout_bsc1_out visibility = " + str(bts3_layout_bsc1_out_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bsc1_out_visibility),
                        InformationSet("set mcr_ecubtcu_bsc1_instatus = "+ str(mcr_ecubtcu_bsc1_instatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bsc1_instatus_2),
                        InformationSet("get bts3_layout_bsc1_in visibility", "thriver", "mcrhci", get_bts3_layout_bsc1_in_visibility),
                        InformationSet("validate bts3_layout_bsc1_in visibility = " + str(bts3_layout_bsc1_in_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bsc1_in_visibility),
                        InformationSet("set mcr_ecubtcu_bsc2_instatus = "+ str(mcr_ecubtcu_bsc2_instatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bsc2_instatus_1),
                        InformationSet("get bts3_layout_bsc2_in visibility", "thriver", "mcrhci", get_bts3_layout_bsc2_in_visibility),
                        InformationSet("validate bts3_layout_bsc2_in visibility = " + str(bts3_layout_bsc2_in_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bsc2_in_visibility),
                        InformationSet("set mcr_ecubtcu_bsc2_outstatus = "+ str(mcr_ecubtcu_bsc2_outstatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bsc2_outstatus_1),
                        InformationSet("get bts3_layout_bsc2_out visibility", "thriver", "mcrhci", get_bts3_layout_bsc2_out_visibility),
                        InformationSet("validate bts3_layout_bsc2_out visibility = " + str(bts3_layout_bsc2_out_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bsc2_out_visibility),
                        InformationSet("set mcr_ecubtcu_bsc2_instatus = "+ str(mcr_ecubtcu_bsc2_instatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bsc2_instatus_2),
                        InformationSet("get bts3_layout_bsc2_in_led visibility", "thriver", "mcrhci", get_bts3_layout_bsc2_in_led_visibility),
                        InformationSet("validate bts3_layout_bsc2_in_led visibility = " + str(bts3_layout_bsc2_in_led_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bsc2_in_led_visibility),
                        InformationSet("set mcr_ecubtcu_bsc2_outstatus = "+ str(mcr_ecubtcu_bsc2_outstatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bsc2_outstatus_2),
                        InformationSet("get bts3_layout_bsc2_out_led visibility", "thriver", "mcrhci", get_bts3_layout_bsc2_out_led_visibility),
                        InformationSet("validate bts3_layout_bsc2_out_led visibility = " + str(bts3_layout_bsc2_out_led_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bsc2_out_led_visibility),
                        InformationSet("get SC1B visibility", "thriver", "mcrhci", get_SC1B_visibility),
                        InformationSet("validate SC1B visibility = " + str(SC1B_visibility_expected), "mcrhci", "hcitracer", validate_SC1B_visibility),
                        InformationSet("set mcr_ecubtcu_bpmc1_outstatus = "+ str(mcr_ecubtcu_bpmc1_outstatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpmc1_outstatus_1),
                        InformationSet("get bts3_layout_bpmc1_out visibility", "thriver", "mcrhci", get_bts3_layout_bpmc1_out_visibility),
                        InformationSet("validate bts3_layout_bpmc1_out visibility = " + str(bts3_layout_bpmc1_out_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bpmc1_out_visibility),
                        InformationSet("set mcr_ecubtcu_bpmc1_instatus = "+ str(mcr_ecubtcu_bpmc1_instatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpmc1_instatus_1),
                        InformationSet("get bts3_layout_bpmc1_in visibility", "thriver", "mcrhci", get_bts3_layout_bpmc1_in_visibility),
                        InformationSet("validate bts3_layout_bpmc1_in visibility = " + str(bts3_layout_bpmc1_in_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bpmc1_in_visibility),
                        InformationSet("get SC2A visibility", "thriver", "mcrhci", get_SC2A_visibility),
                        InformationSet("validate SC2A visibility = " + str(SC2A_visibility_expected), "mcrhci", "hcitracer", validate_SC2A_visibility),
                        InformationSet("get bts3_layout_bpmc1_out_btn visibility", "thriver", "mcrhci", get_bts3_layout_bpmc1_out_btn_visibility),
                        InformationSet("validate bts3_layout_bpmc1_out_btn visibility = " + str(bts3_layout_bpmc1_out_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bpmc1_out_btn_visibility),
                        InformationSet("get bts3_layout_bpmc1_in_btn visibility", "thriver", "mcrhci", get_bts3_layout_bpmc1_in_btn_visibility),
                        InformationSet("validate bts3_layout_bpmc1_in_btn visibility = " + str(bts3_layout_bpmc1_in_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bpmc1_in_btn_visibility),
                        InformationSet("set mcr_ecubtcu_bpmc1_instatus = "+ str(mcr_ecubtcu_bpmc1_instatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpmc1_instatus_2),
                        InformationSet("get bts3_layout_bpmc1_in_led visibility", "thriver", "mcrhci", get_bts3_layout_bpmc1_in_led_visibility),
                        InformationSet("validate bts3_layout_bpmc1_in_led visibility = " + str(bts3_layout_bpmc1_in_led_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bpmc1_in_led_visibility),
                        InformationSet("set mcr_ecubtcu_bpmc1_outstatus = "+ str(mcr_ecubtcu_bpmc1_outstatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpmc1_outstatus_2),
                        InformationSet("get bts3_layout_bpmc1_out_led visibility", "thriver", "mcrhci", get_bts3_layout_bpmc1_out_led_visibility),
                        InformationSet("validate bts3_layout_bpmc1_out_led visibility = " + str(bts3_layout_bpmc1_out_led_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bpmc1_out_led_visibility),
                        InformationSet("set mcr_ecubtcu_bpmc2_outstatus = "+ str(mcr_ecubtcu_bpmc2_outstatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpmc2_outstatus_1),
                        InformationSet("get bts3_layout_bpmc2_out visibility", "thriver", "mcrhci", get_bts3_layout_bpmc2_out_visibility),
                        InformationSet("validate bts3_layout_bpmc2_out visibility = " + str(bts3_layout_bpmc2_out_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bpmc2_out_visibility),
                        InformationSet("set mcr_ecubtcu_bpmc2_instatus = "+ str(mcr_ecubtcu_bpmc2_instatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpmc2_instatus_1),
                        InformationSet("get bts3_layout_bpmc2_in visibility", "thriver", "mcrhci", get_bts3_layout_bpmc2_in_visibility),
                        InformationSet("validate bts3_layout_bpmc2_in visibility = " + str(bts3_layout_bpmc2_in_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bpmc2_in_visibility),
                        InformationSet("get bts3_layout_bpmc2_out_btn visibility", "thriver", "mcrhci", get_bts3_layout_bpmc2_out_btn_visibility),
                        InformationSet("validate bts3_layout_bpmc2_out_btn visibility = " + str(bts3_layout_bpmc2_out_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bpmc2_out_btn_visibility),
                        InformationSet("get bts3_layout_bpmc2_in_btn visibility", "thriver", "mcrhci", get_bts3_layout_bpmc2_in_btn_visibility),
                        InformationSet("validate bts3_layout_bpmc2_in_btn visibility = " + str(bts3_layout_bpmc2_in_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bpmc2_in_btn_visibility),
                        InformationSet("set mcr_ecubtcu_bpmc2_instatus = "+ str(mcr_ecubtcu_bpmc2_instatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpmc2_instatus_2),
                        InformationSet("get bts3_layout_bpmc2_in_led visibility", "thriver", "mcrhci", get_bts3_layout_bpmc2_in_led_visibility),
                        InformationSet("validate bts3_layout_bpmc2_in_led visibility = " + str(bts3_layout_bpmc2_in_led_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bpmc2_in_led_visibility),
                        InformationSet("set mcr_ecubtcu_bpmc2_outstatus = "+ str(mcr_ecubtcu_bpmc2_outstatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpmc2_outstatus_2),
                        InformationSet("get bts3_layout_bpmc2_out_led visibility", "thriver", "mcrhci", get_bts3_layout_bpmc2_out_led_visibility),
                        InformationSet("validate bts3_layout_bpmc2_out_led visibility = " + str(bts3_layout_bpmc2_out_led_visibility_expected), "mcrhci", "hcitracer", validate_bts3_layout_bpmc2_out_led_visibility),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []