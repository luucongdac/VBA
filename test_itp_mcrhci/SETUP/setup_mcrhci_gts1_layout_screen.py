
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

class SETUP_VALIDATE_GTS1_LAYOUT_SCREEN(ClinicalIntegrationTestProcedure):
    # default variable values
    name = "Confirm that MCR_Service_GTS1_Layout (gts1_layout.v) is displayed."
    Title_visibility_expected = "1"
    q0m1_visibility_expected = "1"
    q1m1_visibility_expected = "1"
    q3m1_visibility_expected = "1"
    q2m1_visibility_expected = "1"
    q1g1_visibility_expected = "1"
    q2g1_visibility_expected = "1"
    q3g1_visibility_expected = "1"
    q4g1_visibility_expected = "1"
    q5g1_visibility_expected = "1"
    t9g1_visibility_expected = "1"
    t10g1_visibility_expected = "1"
    b1g1_visibility_expected = "1"
    mcr_ecubtcu_bpm5m1_instatus_init_1 = True
    bpm5m1_in_visibility_expected = "1"
    bpm5m1_out_btn_visibility_expected = "1"
    bpm5m1_in_btn_visibility_expected = "1"
    mcr_ecubtcu_bpm5m1_instatus_init_2 = True
    bpm5m1_in_btn_led_visibility_expected = "1"
    mcr_ecubtcu_bpm5m1_outstatus_init_1 = True
    bpm5m1_out_btn_led_visibility_expected = "1"
    mcr_ecubtcu_bpm5m1_outstatus_init_2 = True
    bpm5m1_out_visibility_expected = "1"
    mcr_ecubtcu_bpm7g1_instatus_init_1 = True
    bpm7g1_in_visibility_expected = "1"
    bpm7g1_out_btn_visibility_expected = "1"
    bpm7g1_in_btn_visibility_expected = "1"
    mcr_ecubtcu_bpm7g1_instatus_init_2 = True
    bpm7g1_in_btn_led_visibility_expected = "1"
    mcr_ecubtcu_bpm7g1_outstatus_init_1 = True
    bpm7g1_out_btn_led_visibility_expected = "1"
    mcr_ecubtcu_bpm7g1_outstatus_init_2 = True
    bpm7g1_out_visibility_expected = "1"
    mcr_ecubtcu_bpm8g1_instatus_init_1 = True
    bpm8g1_in_visibility_expected = "1"
    bpm8g1_out_btn_visibility_expected = "1"
    bpm8g1_in_btn_visibility_expected = "1"
    mcr_ecubtcu_bpm8g1_instatus_init_2 = True
    bpm8g1_in_btn_led_visibility_expected = "1"
    mcr_ecubtcu_bpm8g1_outstatus_init_1 = True
    bpm8g1_out_btn_led_visibility_expected = "1"
    mcr_ecubtcu_bpm8g1_outstatus_init_2 = True
    bpm8g1_out_visibility_expected = "1"
    mcr_ecubtcu_bpm9g1_instatus_init_1 = True
    bpm9g1_in_visibility_expected = "1"
    bpm9g1_out_btn_visibility_expected = "1"
    bpm9g1_in_btn_visibility_expected = "1"
    mcr_ecubtcu_bpm9g1_instatus_init_2 = True
    bpm9g1_in_btn_led_visibility_expected = "1"
    mcr_ecubtcu_bpm9g1_outstatus_init_1 = True
    bpm9g1_out_btn_led_visibility_expected = "1"
    mcr_ecubtcu_bpm9g1_outstatus_init_2 = True
    bpm9g1_out_visibility_expected = "1"
    b2g1_visibility_expected = "1"
    bts1_layout_btn_visibility_expected = "1"

    def __init__(self, test):
        cls = type(self)
        name = cls.name
        q0m1_visibility_expected = cls.q0m1_visibility_expected
        q1m1_visibility_expected = cls.q1m1_visibility_expected
        q3m1_visibility_expected = cls.q3m1_visibility_expected
        q2m1_visibility_expected = cls.q2m1_visibility_expected
        q1g1_visibility_expected = cls.q1g1_visibility_expected
        q2g1_visibility_expected = cls.q2g1_visibility_expected
        q3g1_visibility_expected = cls.q3g1_visibility_expected
        q4g1_visibility_expected = cls.q4g1_visibility_expected
        q5g1_visibility_expected = cls.q5g1_visibility_expected
        t9g1_visibility_expected = cls.t9g1_visibility_expected
        t10g1_visibility_expected = cls.t10g1_visibility_expected
        b1g1_visibility_expected = cls.b1g1_visibility_expected
        mcr_ecubtcu_bpm5m1_instatus_init_1 = cls.mcr_ecubtcu_bpm5m1_instatus_init_1
        bpm5m1_in_visibility_expected = cls.bpm5m1_in_visibility_expected
        bpm5m1_out_btn_visibility_expected = cls.bpm5m1_out_btn_visibility_expected
        bpm5m1_in_btn_visibility_expected = cls.bpm5m1_in_btn_visibility_expected
        mcr_ecubtcu_bpm5m1_instatus_init_2 = cls.mcr_ecubtcu_bpm5m1_instatus_init_2
        bpm5m1_in_btn_led_visibility_expected = cls.bpm5m1_in_btn_led_visibility_expected
        mcr_ecubtcu_bpm5m1_outstatus_init_1 = cls.mcr_ecubtcu_bpm5m1_outstatus_init_1
        bpm5m1_out_btn_led_visibility_expected = cls.bpm5m1_out_btn_led_visibility_expected
        mcr_ecubtcu_bpm5m1_outstatus_init_2 = cls.mcr_ecubtcu_bpm5m1_outstatus_init_2
        bpm5m1_out_visibility_expected = cls.bpm5m1_out_visibility_expected
        mcr_ecubtcu_bpm7g1_instatus_init_1 = cls.mcr_ecubtcu_bpm7g1_instatus_init_1
        bpm7g1_in_visibility_expected = cls.bpm7g1_in_visibility_expected
        bpm7g1_out_btn_visibility_expected = cls.bpm7g1_out_btn_visibility_expected
        bpm7g1_in_btn_visibility_expected = cls.bpm7g1_in_btn_visibility_expected
        mcr_ecubtcu_bpm7g1_instatus_init_2 = cls.mcr_ecubtcu_bpm7g1_instatus_init_2
        bpm7g1_in_btn_led_visibility_expected = cls.bpm7g1_in_btn_led_visibility_expected
        mcr_ecubtcu_bpm7g1_outstatus_init_1 = cls.mcr_ecubtcu_bpm7g1_outstatus_init_1
        bpm7g1_out_btn_led_visibility_expected = cls.bpm7g1_out_btn_led_visibility_expected
        mcr_ecubtcu_bpm7g1_outstatus_init_2 = cls.mcr_ecubtcu_bpm7g1_outstatus_init_2
        bpm7g1_out_visibility_expected = cls.bpm7g1_out_visibility_expected
        mcr_ecubtcu_bpm8g1_instatus_init_1 = cls.mcr_ecubtcu_bpm8g1_instatus_init_1
        bpm8g1_in_visibility_expected = cls.bpm8g1_in_visibility_expected
        bpm8g1_out_btn_visibility_expected = cls.bpm8g1_out_btn_visibility_expected
        bpm8g1_in_btn_visibility_expected = cls.bpm8g1_in_btn_visibility_expected
        mcr_ecubtcu_bpm8g1_instatus_init_2 = cls.mcr_ecubtcu_bpm8g1_instatus_init_2
        bpm8g1_in_btn_led_visibility_expected = cls.bpm8g1_in_btn_led_visibility_expected
        mcr_ecubtcu_bpm8g1_outstatus_init_1 = cls.mcr_ecubtcu_bpm8g1_outstatus_init_1
        bpm8g1_out_btn_led_visibility_expected = cls.bpm8g1_out_btn_led_visibility_expected
        mcr_ecubtcu_bpm8g1_outstatus_init_2 = cls.mcr_ecubtcu_bpm8g1_outstatus_init_2
        bpm8g1_out_visibility_expected = cls.bpm8g1_out_visibility_expected
        mcr_ecubtcu_bpm9g1_instatus_init_1 = cls.mcr_ecubtcu_bpm9g1_instatus_init_1
        bpm9g1_in_visibility_expected = cls.bpm9g1_in_visibility_expected
        bpm9g1_out_btn_visibility_expected = cls.bpm9g1_out_btn_visibility_expected
        bpm9g1_in_btn_visibility_expected = cls.bpm9g1_in_btn_visibility_expected
        mcr_ecubtcu_bpm9g1_instatus_init_2 = cls.mcr_ecubtcu_bpm9g1_instatus_init_2
        bpm9g1_in_btn_led_visibility_expected = cls.bpm9g1_in_btn_led_visibility_expected
        mcr_ecubtcu_bpm9g1_outstatus_init_1 = cls.mcr_ecubtcu_bpm9g1_outstatus_init_1
        bpm9g1_out_btn_led_visibility_expected = cls.bpm9g1_out_btn_led_visibility_expected
        mcr_ecubtcu_bpm9g1_outstatus_init_2 = cls.mcr_ecubtcu_bpm9g1_outstatus_init_2
        bpm9g1_out_visibility_expected = cls.bpm9g1_out_visibility_expected
        b2g1_visibility_expected = cls.b2g1_visibility_expected
        bts1_layout_btn_visibility_expected = cls.bts1_layout_btn_visibility_expected

        #set initial values
        set_mcr_ecubtcu_bpm5m1_instatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpm5m1_instatus", mcr_ecubtcu_bpm5m1_instatus_init_1)
        set_mcr_ecubtcu_bpm5m1_instatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpm5m1_instatus", mcr_ecubtcu_bpm5m1_instatus_init_2)
        set_mcr_ecubtcu_bpm5m1_outstatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpm5m1_outstatus", mcr_ecubtcu_bpm5m1_outstatus_init_1)
        set_mcr_ecubtcu_bpm5m1_outstatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpm5m1_outstatus", mcr_ecubtcu_bpm5m1_outstatus_init_2)
        set_mcr_ecubtcu_bpm7g1_instatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpm7g1_instatus", mcr_ecubtcu_bpm7g1_instatus_init_1)
        set_mcr_ecubtcu_bpm7g1_instatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpm7g1_instatus", mcr_ecubtcu_bpm7g1_instatus_init_2)
        set_mcr_ecubtcu_bpm7g1_outstatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpm7g1_outstatus", mcr_ecubtcu_bpm7g1_outstatus_init_1)
        set_mcr_ecubtcu_bpm7g1_outstatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpm7g1_outstatus", mcr_ecubtcu_bpm7g1_outstatus_init_2)
        set_mcr_ecubtcu_bpm8g1_instatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpm8g1_instatus", mcr_ecubtcu_bpm8g1_instatus_init_1)
        set_mcr_ecubtcu_bpm8g1_instatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpm8g1_instatus", mcr_ecubtcu_bpm8g1_instatus_init_2)
        set_mcr_ecubtcu_bpm8g1_outstatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpm8g1_outstatus", mcr_ecubtcu_bpm8g1_outstatus_init_1)
        set_mcr_ecubtcu_bpm8g1_outstatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpm8g1_outstatus", mcr_ecubtcu_bpm8g1_outstatus_init_2)
        set_mcr_ecubtcu_bpm9g1_instatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpm9g1_instatus", mcr_ecubtcu_bpm9g1_instatus_init_1)
        set_mcr_ecubtcu_bpm9g1_instatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpm9g1_instatus", mcr_ecubtcu_bpm9g1_instatus_init_2)
        set_mcr_ecubtcu_bpm9g1_outstatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpm9g1_outstatus", mcr_ecubtcu_bpm9g1_outstatus_init_1)
        set_mcr_ecubtcu_bpm9g1_outstatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpm9g1_outstatus", mcr_ecubtcu_bpm9g1_outstatus_init_2)

        #get values
        get_q0m1_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q0m1")
        get_q1m1_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q1m1")
        get_q3m1_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q3m1")
        get_q2m1_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q2m1")
        get_q1g1_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q1g1")
        get_q2g1_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q2g1")
        get_q3g1_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q3g1")
        get_q4g1_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q4g1")
        get_q5g1_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q5g1")
        get_t9g1_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "t9g1")
        get_t10g1_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "t10g1")
        get_b1g1_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "b1g1")
        get_bpm5m1_in_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm5m1_in")
        get_bpm5m1_out_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm5m1_out_btn")
        get_bpm5m1_in_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm5m1_in_btn")
        get_bpm5m1_in_btn_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm5m1_in_btn_led")
        get_bpm5m1_out_btn_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm5m1_out_btn_led")
        get_bpm5m1_out_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm5m1_out")
        get_bpm7g1_in_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm7g1_in")
        get_bpm7g1_out_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm7g1_out_btn")
        get_bpm7g1_in_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm7g1_in_btn")
        get_bpm7g1_in_btn_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm7g1_in_btn_led")
        get_bpm7g1_out_btn_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm7g1_out_btn_led")
        get_bpm7g1_out_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm7g1_out")
        get_bpm8g1_in_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm8g1_in")
        get_bpm8g1_out_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm8g1_out_btn")
        get_bpm8g1_in_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm8g1_in_btn")
        get_bpm8g1_in_btn_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm8g1_in_btn_led")
        get_bpm8g1_out_btn_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm8g1_out_btn_led")
        get_bpm8g1_out_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm8g1_out")
        get_bpm9g1_in_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm9g1_in")
        get_bpm9g1_out_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm9g1_out_btn")
        get_bpm9g1_in_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm9g1_in_btn")
        get_bpm9g1_in_btn_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm9g1_in_btn_led")
        get_bpm9g1_out_btn_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm9g1_out_btn_led")
        get_bpm9g1_out_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm9g1_out")
        get_b2g1_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "b2g1")
        get_bts1_layout_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_btn")

        #validate
        validate_q0m1_visibility = MsgTypeString("q0m1:TMMI_MCR_IS_VISIBLE", value=q0m1_visibility_expected)
        validate_q1m1_visibility = MsgTypeString("q1m1:TMMI_MCR_IS_VISIBLE", value=q1m1_visibility_expected)
        validate_q3m1_visibility = MsgTypeString("q3m1:TMMI_MCR_IS_VISIBLE", value=q3m1_visibility_expected)
        validate_q2m1_visibility = MsgTypeString("q2m1:TMMI_MCR_IS_VISIBLE", value=q2m1_visibility_expected)
        validate_q1g1_visibility = MsgTypeString("q1g1:TMMI_MCR_IS_VISIBLE", value=q1g1_visibility_expected)
        validate_q2g1_visibility = MsgTypeString("q2g1:TMMI_MCR_IS_VISIBLE", value=q2g1_visibility_expected)
        validate_q3g1_visibility = MsgTypeString("q3g1:TMMI_MCR_IS_VISIBLE", value=q3g1_visibility_expected)
        validate_q4g1_visibility = MsgTypeString("q4g1:TMMI_MCR_IS_VISIBLE", value=q4g1_visibility_expected)
        validate_q5g1_visibility = MsgTypeString("q5g1:TMMI_MCR_IS_VISIBLE", value=q5g1_visibility_expected)
        validate_t9g1_visibility = MsgTypeString("t9g1:TMMI_MCR_IS_VISIBLE", value=t9g1_visibility_expected)
        validate_t10g1_visibility = MsgTypeString("t10g1:TMMI_MCR_IS_VISIBLE", value=t10g1_visibility_expected)
        validate_b1g1_visibility = MsgTypeString("b1g1:TMMI_MCR_IS_VISIBLE", value=b1g1_visibility_expected)
        validate_bpm5m1_in_visibility = MsgTypeString("bpm5m1_in:TMMI_MCR_IS_VISIBLE", value=bpm5m1_in_visibility_expected)
        validate_bpm5m1_out_btn_visibility = MsgTypeString("bpm5m1_out_btn:TMMI_MCR_IS_VISIBLE", value=bpm5m1_out_btn_visibility_expected)
        validate_bpm5m1_in_btn_visibility = MsgTypeString("bpm5m1_in_btn:TMMI_MCR_IS_VISIBLE", value=bpm5m1_in_btn_visibility_expected)
        validate_bpm5m1_in_btn_led_visibility = MsgTypeString("bpm5m1_in_btn_led:TMMI_MCR_IS_VISIBLE", value=bpm5m1_in_btn_led_visibility_expected)
        validate_bpm5m1_out_btn_led_visibility = MsgTypeString("bpm5m1_out_btn_led:TMMI_MCR_IS_VISIBLE", value=bpm5m1_out_btn_led_visibility_expected)
        validate_bpm5m1_out_visibility = MsgTypeString("bpm5m1_out:TMMI_MCR_IS_VISIBLE", value=bpm5m1_out_visibility_expected)
        validate_bpm7g1_in_visibility = MsgTypeString("bpm7g1_in:TMMI_MCR_IS_VISIBLE", value=bpm7g1_in_visibility_expected)
        validate_bpm7g1_out_btn_visibility = MsgTypeString("bpm7g1_out_btn:TMMI_MCR_IS_VISIBLE", value=bpm7g1_out_btn_visibility_expected)
        validate_bpm7g1_in_btn_visibility = MsgTypeString("bpm7g1_in_btn:TMMI_MCR_IS_VISIBLE", value=bpm7g1_in_btn_visibility_expected)
        validate_bpm7g1_in_btn_led_visibility = MsgTypeString("bpm7g1_in_btn_led:TMMI_MCR_IS_VISIBLE", value=bpm7g1_in_btn_led_visibility_expected)
        validate_bpm7g1_out_btn_led_visibility = MsgTypeString("bpm7g1_out_btn_led:TMMI_MCR_IS_VISIBLE", value=bpm7g1_out_btn_led_visibility_expected)
        validate_bpm7g1_out_visibility = MsgTypeString("bpm7g1_out:TMMI_MCR_IS_VISIBLE", value=bpm7g1_out_visibility_expected)
        validate_bpm8g1_in_visibility = MsgTypeString("bpm8g1_in:TMMI_MCR_IS_VISIBLE", value=bpm8g1_in_visibility_expected)
        validate_bpm8g1_out_btn_visibility = MsgTypeString("bpm8g1_out_btn:TMMI_MCR_IS_VISIBLE", value=bpm8g1_out_btn_visibility_expected)
        validate_bpm8g1_in_btn_visibility = MsgTypeString("bpm8g1_in_btn:TMMI_MCR_IS_VISIBLE", value=bpm8g1_in_btn_visibility_expected)
        validate_bpm8g1_in_btn_led_visibility = MsgTypeString("bpm8g1_in_btn_led:TMMI_MCR_IS_VISIBLE", value=bpm8g1_in_btn_led_visibility_expected)
        validate_bpm8g1_out_btn_led_visibility = MsgTypeString("bpm8g1_out_btn_led:TMMI_MCR_IS_VISIBLE", value=bpm8g1_out_btn_led_visibility_expected)
        validate_bpm8g1_out_visibility = MsgTypeString("bpm8g1_out:TMMI_MCR_IS_VISIBLE", value=bpm8g1_out_visibility_expected)
        validate_bpm9g1_in_visibility = MsgTypeString("bpm9g1_in:TMMI_MCR_IS_VISIBLE", value=bpm9g1_in_visibility_expected)
        validate_bpm9g1_out_btn_visibility = MsgTypeString("bpm9g1_out_btn:TMMI_MCR_IS_VISIBLE", value=bpm9g1_out_btn_visibility_expected)
        validate_bpm9g1_in_btn_visibility = MsgTypeString("bpm9g1_in_btn:TMMI_MCR_IS_VISIBLE", value=bpm9g1_in_btn_visibility_expected)
        validate_bpm9g1_in_btn_led_visibility = MsgTypeString("bpm9g1_in_btn_led:TMMI_MCR_IS_VISIBLE", value=bpm9g1_in_btn_led_visibility_expected)
        validate_bpm9g1_out_btn_led_visibility = MsgTypeString("bpm9g1_out_btn_led:TMMI_MCR_IS_VISIBLE", value=bpm9g1_out_btn_led_visibility_expected)
        validate_bpm9g1_out_visibility = MsgTypeString("bpm9g1_out:TMMI_MCR_IS_VISIBLE", value=bpm9g1_out_visibility_expected)
        validate_b2g1_visibility = MsgTypeString("b2g1:TMMI_MCR_IS_VISIBLE", value=b2g1_visibility_expected)
        validate_bts1_layout_btn_visibility = MsgTypeString("bts1_layout_btn:TMMI_MCR_IS_VISIBLE", value=bts1_layout_btn_visibility_expected)

        info_exchange = [
                        InformationSet("get q0m1 visibility", "thriver", "mcrhci", get_q0m1_visibility),
                        InformationSet("validate q0m1 visibility = " + str(q0m1_visibility_expected), "mcrhci", "hcitracer", validate_q0m1_visibility),
                        InformationSet("get q1m1 visibility", "thriver", "mcrhci", get_q1m1_visibility),
                        InformationSet("validate q1m1 visibility = " + str(q1m1_visibility_expected), "mcrhci", "hcitracer", validate_q1m1_visibility),
                        InformationSet("get q3m1 visibility", "thriver", "mcrhci", get_q3m1_visibility),
                        InformationSet("validate q3m1 visibility = " + str(q3m1_visibility_expected), "mcrhci", "hcitracer", validate_q3m1_visibility),
                        InformationSet("get q2m1 visibility", "thriver", "mcrhci", get_q2m1_visibility),
                        InformationSet("validate q2m1 visibility = " + str(q2m1_visibility_expected), "mcrhci", "hcitracer", validate_q2m1_visibility),
                        InformationSet("get q1g1 visibility", "thriver", "mcrhci", get_q1g1_visibility),
                        InformationSet("validate q1g1 visibility = " + str(q1g1_visibility_expected), "mcrhci", "hcitracer", validate_q1g1_visibility),
                        InformationSet("get q2g1 visibility", "thriver", "mcrhci", get_q2g1_visibility),
                        InformationSet("validate q2g1 visibility = " + str(q2g1_visibility_expected), "mcrhci", "hcitracer", validate_q2g1_visibility),
                        InformationSet("get q3g1 visibility", "thriver", "mcrhci", get_q3g1_visibility),
                        InformationSet("validate q3g1 visibility = " + str(q3g1_visibility_expected), "mcrhci", "hcitracer", validate_q3g1_visibility),
                        InformationSet("get q4g1 visibility", "thriver", "mcrhci", get_q4g1_visibility),
                        InformationSet("validate q4g1 visibility = " + str(q4g1_visibility_expected), "mcrhci", "hcitracer", validate_q4g1_visibility),
                        InformationSet("get q5g1 visibility", "thriver", "mcrhci", get_q5g1_visibility),
                        InformationSet("validate q5g1 visibility = " + str(q5g1_visibility_expected), "mcrhci", "hcitracer", validate_q5g1_visibility),
                        InformationSet("get t9g1 visibility", "thriver", "mcrhci", get_t9g1_visibility),
                        InformationSet("validate t9g1 visibility = " + str(t9g1_visibility_expected), "mcrhci", "hcitracer", validate_t9g1_visibility),
                        InformationSet("get t10g1 visibility", "thriver", "mcrhci", get_t10g1_visibility),
                        InformationSet("validate t10g1 visibility = " + str(t10g1_visibility_expected), "mcrhci", "hcitracer", validate_t10g1_visibility),
                        InformationSet("get b1g1 visibility", "thriver", "mcrhci", get_b1g1_visibility),
                        # Bug: cannot get the visibility of b1g1
                        # InformationSet("validate b1g1 visibility = " + str(b1g1_visibility_expected), "mcrhci", "hcitracer", validate_b1g1_visibility),
                        InformationSet("set mcr_ecubtcu_bpm5m1_instatus = "+ str(mcr_ecubtcu_bpm5m1_instatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpm5m1_instatus_1),
                        InformationSet("get bpm5m1_in visibility", "thriver", "mcrhci", get_bpm5m1_in_visibility),
                        InformationSet("validate bpm5m1_in visibility = " + str(bpm5m1_in_visibility_expected), "mcrhci", "hcitracer", validate_bpm5m1_in_visibility),
                        InformationSet("get bpm5m1_out_btn visibility", "thriver", "mcrhci", get_bpm5m1_out_btn_visibility),
                        InformationSet("validate bpm5m1_out_btn visibility = " + str(bpm5m1_out_btn_visibility_expected), "mcrhci", "hcitracer", validate_bpm5m1_out_btn_visibility),
                        InformationSet("get bpm5m1_in_btn visibility", "thriver", "mcrhci", get_bpm5m1_in_btn_visibility),
                        InformationSet("validate bpm5m1_in_btn visibility = " + str(bpm5m1_in_btn_visibility_expected), "mcrhci", "hcitracer", validate_bpm5m1_in_btn_visibility),
                        InformationSet("set mcr_ecubtcu_bpm5m1_instatus = "+ str(mcr_ecubtcu_bpm5m1_instatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpm5m1_instatus_2),
                        InformationSet("get bpm5m1_in_btn_led visibility", "thriver", "mcrhci", get_bpm5m1_in_btn_led_visibility),
                        InformationSet("validate bpm5m1_in_btn_led visibility = " + str(bpm5m1_in_btn_led_visibility_expected), "mcrhci", "hcitracer", validate_bpm5m1_in_btn_led_visibility),
                        InformationSet("set mcr_ecubtcu_bpm5m1_outstatus = "+ str(mcr_ecubtcu_bpm5m1_outstatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpm5m1_outstatus_1),
                        InformationSet("get bpm5m1_out_btn_led visibility", "thriver", "mcrhci", get_bpm5m1_out_btn_led_visibility),
                        InformationSet("validate bpm5m1_out_btn_led visibility = " + str(bpm5m1_out_btn_led_visibility_expected), "mcrhci", "hcitracer", validate_bpm5m1_out_btn_led_visibility),
                        InformationSet("set mcr_ecubtcu_bpm5m1_outstatus = "+ str(mcr_ecubtcu_bpm5m1_outstatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpm5m1_outstatus_2),
                        InformationSet("get bpm5m1_out visibility", "thriver", "mcrhci", get_bpm5m1_out_visibility),
                        InformationSet("validate bpm5m1_out visibility = " + str(bpm5m1_out_visibility_expected), "mcrhci", "hcitracer", validate_bpm5m1_out_visibility),
                        InformationSet("set mcr_ecubtcu_bpm7g1_instatus = "+ str(mcr_ecubtcu_bpm7g1_instatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpm7g1_instatus_1),
                        InformationSet("get bpm7g1_in visibility", "thriver", "mcrhci", get_bpm7g1_in_visibility),
                        InformationSet("validate bpm7g1_in visibility = " + str(bpm7g1_in_visibility_expected), "mcrhci", "hcitracer", validate_bpm7g1_in_visibility),
                        InformationSet("get bpm7g1_out_btn visibility", "thriver", "mcrhci", get_bpm7g1_out_btn_visibility),
                        InformationSet("validate bpm7g1_out_btn visibility = " + str(bpm7g1_out_btn_visibility_expected), "mcrhci", "hcitracer", validate_bpm7g1_out_btn_visibility),
                        InformationSet("get bpm7g1_in_btn visibility", "thriver", "mcrhci", get_bpm7g1_in_btn_visibility),
                        InformationSet("validate bpm7g1_in_btn visibility = " + str(bpm7g1_in_btn_visibility_expected), "mcrhci", "hcitracer", validate_bpm7g1_in_btn_visibility),
                        InformationSet("set mcr_ecubtcu_bpm7g1_instatus = "+ str(mcr_ecubtcu_bpm7g1_instatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpm7g1_instatus_2),
                        InformationSet("get bpm7g1_in_btn_led visibility", "thriver", "mcrhci", get_bpm7g1_in_btn_led_visibility),
                        InformationSet("validate bpm7g1_in_btn_led visibility = " + str(bpm7g1_in_btn_led_visibility_expected), "mcrhci", "hcitracer", validate_bpm7g1_in_btn_led_visibility),
                        InformationSet("set mcr_ecubtcu_bpm7g1_outstatus = "+ str(mcr_ecubtcu_bpm7g1_outstatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpm7g1_outstatus_1),
                        InformationSet("get bpm7g1_out_btn_led visibility", "thriver", "mcrhci", get_bpm7g1_out_btn_led_visibility),
                        InformationSet("validate bpm7g1_out_btn_led visibility = " + str(bpm7g1_out_btn_led_visibility_expected), "mcrhci", "hcitracer", validate_bpm7g1_out_btn_led_visibility),
                        InformationSet("set mcr_ecubtcu_bpm7g1_outstatus = "+ str(mcr_ecubtcu_bpm7g1_outstatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpm7g1_outstatus_2),
                        InformationSet("get bpm7g1_out visibility", "thriver", "mcrhci", get_bpm7g1_out_visibility),
                        InformationSet("validate bpm7g1_out visibility = " + str(bpm7g1_out_visibility_expected), "mcrhci", "hcitracer", validate_bpm7g1_out_visibility),
                        InformationSet("set mcr_ecubtcu_bpm8g1_instatus = "+ str(mcr_ecubtcu_bpm8g1_instatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpm8g1_instatus_1),
                        InformationSet("get bpm8g1_in visibility", "thriver", "mcrhci", get_bpm8g1_in_visibility),
                        InformationSet("validate bpm8g1_in visibility = " + str(bpm8g1_in_visibility_expected), "mcrhci", "hcitracer", validate_bpm8g1_in_visibility),
                        InformationSet("get bpm8g1_out_btn visibility", "thriver", "mcrhci", get_bpm8g1_out_btn_visibility),
                        InformationSet("validate bpm8g1_out_btn visibility = " + str(bpm8g1_out_btn_visibility_expected), "mcrhci", "hcitracer", validate_bpm8g1_out_btn_visibility),
                        InformationSet("get bpm8g1_in_btn visibility", "thriver", "mcrhci", get_bpm8g1_in_btn_visibility),
                        InformationSet("validate bpm8g1_in_btn visibility = " + str(bpm8g1_in_btn_visibility_expected), "mcrhci", "hcitracer", validate_bpm8g1_in_btn_visibility),
                        InformationSet("set mcr_ecubtcu_bpm8g1_instatus = "+ str(mcr_ecubtcu_bpm8g1_instatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpm8g1_instatus_2),
                        InformationSet("get bpm8g1_in_btn_led visibility", "thriver", "mcrhci", get_bpm8g1_in_btn_led_visibility),
                        InformationSet("validate bpm8g1_in_btn_led visibility = " + str(bpm8g1_in_btn_led_visibility_expected), "mcrhci", "hcitracer", validate_bpm8g1_in_btn_led_visibility),
                        InformationSet("set mcr_ecubtcu_bpm8g1_outstatus = "+ str(mcr_ecubtcu_bpm8g1_outstatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpm8g1_outstatus_1),
                        InformationSet("get bpm8g1_out_btn_led visibility", "thriver", "mcrhci", get_bpm8g1_out_btn_led_visibility),
                        InformationSet("validate bpm8g1_out_btn_led visibility = " + str(bpm8g1_out_btn_led_visibility_expected), "mcrhci", "hcitracer", validate_bpm8g1_out_btn_led_visibility),
                        InformationSet("set mcr_ecubtcu_bpm8g1_outstatus = "+ str(mcr_ecubtcu_bpm8g1_outstatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpm8g1_outstatus_2),
                        InformationSet("get bpm8g1_out visibility", "thriver", "mcrhci", get_bpm8g1_out_visibility),
                        InformationSet("validate bpm8g1_out visibility = " + str(bpm8g1_out_visibility_expected), "mcrhci", "hcitracer", validate_bpm8g1_out_visibility),
                        InformationSet("set mcr_ecubtcu_bpm9g1_instatus = "+ str(mcr_ecubtcu_bpm9g1_instatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpm9g1_instatus_1),
                        InformationSet("get bpm9g1_in visibility", "thriver", "mcrhci", get_bpm9g1_in_visibility),
                        InformationSet("validate bpm9g1_in visibility = " + str(bpm9g1_in_visibility_expected), "mcrhci", "hcitracer", validate_bpm9g1_in_visibility),
                        InformationSet("get bpm9g1_out_btn visibility", "thriver", "mcrhci", get_bpm9g1_out_btn_visibility),
                        InformationSet("validate bpm9g1_out_btn visibility = " + str(bpm9g1_out_btn_visibility_expected), "mcrhci", "hcitracer", validate_bpm9g1_out_btn_visibility),
                        InformationSet("get bpm9g1_in_btn visibility", "thriver", "mcrhci", get_bpm9g1_in_btn_visibility),
                        InformationSet("validate bpm9g1_in_btn visibility = " + str(bpm9g1_in_btn_visibility_expected), "mcrhci", "hcitracer", validate_bpm9g1_in_btn_visibility),
                        InformationSet("set mcr_ecubtcu_bpm9g1_instatus = "+ str(mcr_ecubtcu_bpm9g1_instatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpm9g1_instatus_2),
                        InformationSet("get bpm9g1_in_btn_led visibility", "thriver", "mcrhci", get_bpm9g1_in_btn_led_visibility),
                        InformationSet("validate bpm9g1_in_btn_led visibility = " + str(bpm9g1_in_btn_led_visibility_expected), "mcrhci", "hcitracer", validate_bpm9g1_in_btn_led_visibility),
                        InformationSet("set mcr_ecubtcu_bpm9g1_outstatus = "+ str(mcr_ecubtcu_bpm9g1_outstatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpm9g1_outstatus_1),
                        InformationSet("get bpm9g1_out_btn_led visibility", "thriver", "mcrhci", get_bpm9g1_out_btn_led_visibility),
                        InformationSet("validate bpm9g1_out_btn_led visibility = " + str(bpm9g1_out_btn_led_visibility_expected), "mcrhci", "hcitracer", validate_bpm9g1_out_btn_led_visibility),
                        InformationSet("set mcr_ecubtcu_bpm9g1_outstatus = "+ str(mcr_ecubtcu_bpm9g1_outstatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpm9g1_outstatus_2),
                        InformationSet("get bpm9g1_out visibility", "thriver", "mcrhci", get_bpm9g1_out_visibility),
                        InformationSet("validate bpm9g1_out visibility = " + str(bpm9g1_out_visibility_expected), "mcrhci", "hcitracer", validate_bpm9g1_out_visibility),
                        InformationSet("get b2g1 visibility", "thriver", "mcrhci", get_b2g1_visibility),
                        InformationSet("validate b2g1 visibility = " + str(b2g1_visibility_expected), "mcrhci", "hcitracer", validate_b2g1_visibility),
                        InformationSet("get bts1_layout_btn visibility", "thriver", "mcrhci", get_bts1_layout_btn_visibility),
                        # Bug: cannot get the visibility of bts1_layout_btn
                        # InformationSet("validate bts1_layout_btn visibility = " + str(bts1_layout_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_btn_visibility),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []