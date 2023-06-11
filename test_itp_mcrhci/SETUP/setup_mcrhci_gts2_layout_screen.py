
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

class SETUP_VALIDATE_GTS2_LAYOUT_SCREEN(ClinicalIntegrationTestProcedure):
    # default variable values
    name = "Confirm that MCR_Service_GTS2_Layout (gts2_layout.v) is displayed"
    q0m2_visibility_expected = "1"
    q1m2_visibility_expected = "1"
    q3m2_visibility_expected = "1"
    q2m2_visibility_expected = "1"
    t10_visibility_expected = "1"
    q1g2_visibility_expected = "1"
    q2g2_visibility_expected = "1"
    q3g2_visibility_expected = "1"
    q4g2_visibility_expected = "1"
    q5g2_visibility_expected = "1"
    t9g2_visibility_expected = "1"
    t10g2_visibility_expected = "1"
    b1g2_visibility_expected = "1"
    mcr_ecubtcu_bpm5m2_instatus_init_1 = True
    bpm5m2_in_visibility_expected = "1"
    bpm5m2_out_btn_visibility_expected = "1"
    bpm5m2_in_btn_visibility_expected = "1"
    mcr_ecubtcu_bpm5m2_instatus_init_2 = False
    bpm5m2_in_btn_led_visibility_expected = "0"
    mcr_ecubtcu_bpm5m2_outstatus_init_1 = True
    bpm5m2_out_btn_led_visibility_expected = "1"
    mcr_ecubtcu_bpm5m2_outstatus_init_2 = False
    bpm5m2_out_visibility_expected = "0"
    mcr_ecubtcu_bpm7g2_instatus_init_1 = True
    bpm7g2_in_visibility_expected = "1"
    bpm7g2_out_btn_visibility_expected = "1"
    bpm7g2_in_btn_visibility_expected = "1"
    mcr_ecubtcu_bpm7g2_instatus_init_2 = False
    bpm7g2_btn_led_visibility_expected = "0"
    mcr_ecubtcu_bpm7g2_outstatus_init_1 = True
    bpm7g2_out_btn_led_visibility_expected = "1"
    mcr_ecubtcu_bpm7g2_outstatus_init_2 = False
    bpm7g2_out_visibility_expected = "0"
    mcr_ecubtcu_bpm8g2_instatus_init_1 = True
    bpm8g2_in_visibility_expected = "1"
    bpm8g2_out_btn_visibility_expected = "1"
    bpm8g2_in_btn_visibility_expected = "1"
    mcr_ecubtcu_bpm8g2_instatus_init_2 = False
    bpm8g2_in_btn_led_visibility_expected = "0"
    mcr_ecubtcu_bpm8g2_outstatus_init_1 = True
    bpm8g2_out_btn_led_visibility_expected = "1"
    mcr_ecubtcu_bpm8g2_outstatus_init_2 = False
    bpm8g2_out_visibility_expected = "0"
    mcr_ecubtcu_bpm9g2_instatus_init_1 = True
    bpm9g2_in_visibility_expected = "1"
    bpm9g2_out_btn_visibility_expected = "1"
    bpm9g2_in_btn_visibility_expected = "1"
    mcr_ecubtcu_bpm9g2_instatus_init_2 = False
    bpm9g2_in_btn_led_visibility_expected = "0"
    mcr_ecubtcu_bpm9g2_outstatus_init_1 = True
    bpm9g2_out_btn_led_visibility_expected = "1"
    mcr_ecubtcu_bpm9g2_outstatus_init_2 = False
    bpm9g2_out_visibility_expected = "0"
    b2g2_visibility_expected = "1"
    bts2_layout_btn_visibility_expected = "1"

    def __init__(self, test):
        cls = type(self)
        name = cls.name
        q0m2_visibility_expected = cls.q0m2_visibility_expected
        q1m2_visibility_expected = cls.q1m2_visibility_expected
        q3m2_visibility_expected = cls.q3m2_visibility_expected
        q2m2_visibility_expected = cls.q2m2_visibility_expected
        t10_visibility_expected = cls.t10_visibility_expected
        q1g2_visibility_expected = cls.q1g2_visibility_expected
        q2g2_visibility_expected = cls.q2g2_visibility_expected
        q3g2_visibility_expected = cls.q3g2_visibility_expected
        q4g2_visibility_expected = cls.q4g2_visibility_expected
        q5g2_visibility_expected = cls.q5g2_visibility_expected
        t9g2_visibility_expected = cls.t9g2_visibility_expected
        t10g2_visibility_expected = cls.t10g2_visibility_expected
        b1g2_visibility_expected = cls.b1g2_visibility_expected
        mcr_ecubtcu_bpm5m2_instatus_init_1 = cls.mcr_ecubtcu_bpm5m2_instatus_init_1
        bpm5m2_in_visibility_expected = cls.bpm5m2_in_visibility_expected
        bpm5m2_out_btn_visibility_expected = cls.bpm5m2_out_btn_visibility_expected
        bpm5m2_in_btn_visibility_expected = cls.bpm5m2_in_btn_visibility_expected
        mcr_ecubtcu_bpm5m2_instatus_init_2 = cls.mcr_ecubtcu_bpm5m2_instatus_init_2
        bpm5m2_in_btn_led_visibility_expected = cls.bpm5m2_in_btn_led_visibility_expected
        mcr_ecubtcu_bpm5m2_outstatus_init_1 = cls.mcr_ecubtcu_bpm5m2_outstatus_init_1
        bpm5m2_out_btn_led_visibility_expected = cls.bpm5m2_out_btn_led_visibility_expected
        mcr_ecubtcu_bpm5m2_outstatus_init_2 = cls.mcr_ecubtcu_bpm5m2_outstatus_init_2
        bpm5m2_out_visibility_expected = cls.bpm5m2_out_visibility_expected
        mcr_ecubtcu_bpm7g2_instatus_init_1 = cls.mcr_ecubtcu_bpm7g2_instatus_init_1
        bpm7g2_in_visibility_expected = cls.bpm7g2_in_visibility_expected
        bpm7g2_out_btn_visibility_expected = cls.bpm7g2_out_btn_visibility_expected
        bpm7g2_in_btn_visibility_expected = cls.bpm7g2_in_btn_visibility_expected
        mcr_ecubtcu_bpm7g2_instatus_init_2 = cls.mcr_ecubtcu_bpm7g2_instatus_init_2
        bpm7g2_btn_led_visibility_expected = cls.bpm7g2_btn_led_visibility_expected
        mcr_ecubtcu_bpm7g2_outstatus_init_1 = cls.mcr_ecubtcu_bpm7g2_outstatus_init_1
        bpm7g2_out_btn_led_visibility_expected = cls.bpm7g2_out_btn_led_visibility_expected
        mcr_ecubtcu_bpm7g2_outstatus_init_2 = cls.mcr_ecubtcu_bpm7g2_outstatus_init_2
        bpm7g2_out_visibility_expected = cls.bpm7g2_out_visibility_expected
        mcr_ecubtcu_bpm8g2_instatus_init_1 = cls.mcr_ecubtcu_bpm8g2_instatus_init_1
        bpm8g2_in_visibility_expected = cls.bpm8g2_in_visibility_expected
        bpm8g2_out_btn_visibility_expected = cls.bpm8g2_out_btn_visibility_expected
        bpm8g2_in_btn_visibility_expected = cls.bpm8g2_in_btn_visibility_expected
        mcr_ecubtcu_bpm8g2_instatus_init_2 = cls.mcr_ecubtcu_bpm8g2_instatus_init_2
        bpm8g2_in_btn_led_visibility_expected = cls.bpm8g2_in_btn_led_visibility_expected
        mcr_ecubtcu_bpm8g2_outstatus_init_1 = cls.mcr_ecubtcu_bpm8g2_outstatus_init_1
        bpm8g2_out_btn_led_visibility_expected = cls.bpm8g2_out_btn_led_visibility_expected
        mcr_ecubtcu_bpm8g2_outstatus_init_2 = cls.mcr_ecubtcu_bpm8g2_outstatus_init_2
        bpm8g2_out_visibility_expected = cls.bpm8g2_out_visibility_expected
        mcr_ecubtcu_bpm9g2_instatus_init_1 = cls.mcr_ecubtcu_bpm9g2_instatus_init_1
        bpm9g2_in_visibility_expected = cls.bpm9g2_in_visibility_expected
        bpm9g2_out_btn_visibility_expected = cls.bpm9g2_out_btn_visibility_expected
        bpm9g2_in_btn_visibility_expected = cls.bpm9g2_in_btn_visibility_expected
        mcr_ecubtcu_bpm9g2_instatus_init_2 = cls.mcr_ecubtcu_bpm9g2_instatus_init_2
        bpm9g2_in_btn_led_visibility_expected = cls.bpm9g2_in_btn_led_visibility_expected
        mcr_ecubtcu_bpm9g2_outstatus_init_1 = cls.mcr_ecubtcu_bpm9g2_outstatus_init_1
        bpm9g2_out_btn_led_visibility_expected = cls.bpm9g2_out_btn_led_visibility_expected
        mcr_ecubtcu_bpm9g2_outstatus_init_2 = cls.mcr_ecubtcu_bpm9g2_outstatus_init_2
        bpm9g2_out_visibility_expected = cls.bpm9g2_out_visibility_expected
        b2g2_visibility_expected = cls.b2g2_visibility_expected
        bts2_layout_btn_visibility_expected = cls.bts2_layout_btn_visibility_expected

        #set initial values
        set_mcr_ecubtcu_bpm5m2_instatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpm5m2_instatus", mcr_ecubtcu_bpm5m2_instatus_init_1)
        set_mcr_ecubtcu_bpm5m2_instatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpm5m2_instatus", mcr_ecubtcu_bpm5m2_instatus_init_2)
        set_mcr_ecubtcu_bpm5m2_outstatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpm5m2_outstatus", mcr_ecubtcu_bpm5m2_outstatus_init_1)
        set_mcr_ecubtcu_bpm5m2_outstatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpm5m2_outstatus", mcr_ecubtcu_bpm5m2_outstatus_init_2)
        set_mcr_ecubtcu_bpm7g2_instatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpm7g2_instatus", mcr_ecubtcu_bpm7g2_instatus_init_1)
        set_mcr_ecubtcu_bpm7g2_instatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpm7g2_instatus", mcr_ecubtcu_bpm7g2_instatus_init_2)
        set_mcr_ecubtcu_bpm7g2_outstatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpm7g2_outstatus", mcr_ecubtcu_bpm7g2_outstatus_init_1)
        set_mcr_ecubtcu_bpm7g2_outstatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpm7g2_outstatus", mcr_ecubtcu_bpm7g2_outstatus_init_2)
        set_mcr_ecubtcu_bpm8g2_instatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpm8g2_instatus", mcr_ecubtcu_bpm8g2_instatus_init_1)
        set_mcr_ecubtcu_bpm8g2_instatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpm8g2_instatus", mcr_ecubtcu_bpm8g2_instatus_init_2)
        set_mcr_ecubtcu_bpm8g2_outstatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpm8g2_outstatus", mcr_ecubtcu_bpm8g2_outstatus_init_1)
        set_mcr_ecubtcu_bpm8g2_outstatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpm8g2_outstatus", mcr_ecubtcu_bpm8g2_outstatus_init_2)
        set_mcr_ecubtcu_bpm9g2_instatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpm9g2_instatus", mcr_ecubtcu_bpm9g2_instatus_init_1)
        set_mcr_ecubtcu_bpm9g2_instatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpm9g2_instatus", mcr_ecubtcu_bpm9g2_instatus_init_2)
        set_mcr_ecubtcu_bpm9g2_outstatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpm9g2_outstatus", mcr_ecubtcu_bpm9g2_outstatus_init_1)
        set_mcr_ecubtcu_bpm9g2_outstatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpm9g2_outstatus", mcr_ecubtcu_bpm9g2_outstatus_init_2)

        #get values
        get_q0m2_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q0m2")
        get_q1m2_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q1m2")
        get_q3m2_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q3m2")
        get_q2m2_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q2m2")
        get_t10_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "t10")
        get_q1g2_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q1g2")
        get_q2g2_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q2g2")
        get_q3g2_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q3g2")
        get_q4g2_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q4g2")
        get_q5g2_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q5g2")
        get_t9g2_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "t9g2")
        get_t10g2_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "t10g2")
        get_b1g2_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "b1g2")
        get_bpm5m2_in_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm5m2_in")
        get_bpm5m2_out_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm5m2_out_btn")
        get_bpm5m2_in_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm5m2_in_btn")
        get_bpm5m2_in_btn_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm5m2_in_btn_led")
        get_bpm5m2_out_btn_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm5m2_out_btn_led")
        get_bpm5m2_out_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm5m2_out")
        get_bpm7g2_in_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm7g2_in")
        get_bpm7g2_out_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm7g2_out_btn")
        get_bpm7g2_in_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm7g2_in_btn")
        get_bpm7g2_btn_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm7g2_btn_led")
        get_bpm7g2_out_btn_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm7g2_out_btn_led")
        get_bpm7g2_out_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm7g2_out")
        get_bpm8g2_in_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm8g2_in")
        get_bpm8g2_out_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm8g2_out_btn")
        get_bpm8g2_in_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm8g2_in_btn")
        get_bpm8g2_in_btn_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm8g2_in_btn_led")
        get_bpm8g2_out_btn_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm8g2_out_btn_led")
        get_bpm8g2_out_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm8g2_out")
        get_bpm9g2_in_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm9g2_in")
        get_bpm9g2_out_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm9g2_out_btn")
        get_bpm9g2_in_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm9g2_in_btn")
        get_bpm9g2_in_btn_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm9g2_in_btn_led")
        get_bpm9g2_out_btn_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm9g2_out_btn_led")
        get_bpm9g2_out_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm9g2_out")
        get_b2g2_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "b2g2")
        get_bts2_layout_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts2_layout_btn")

        #validate
        validate_q0m2_visibility = MsgTypeString("q0m2:TMMI_MCR_IS_VISIBLE", value=q0m2_visibility_expected)
        validate_q1m2_visibility = MsgTypeString("q1m2:TMMI_MCR_IS_VISIBLE", value=q1m2_visibility_expected)
        validate_q3m2_visibility = MsgTypeString("q3m2:TMMI_MCR_IS_VISIBLE", value=q3m2_visibility_expected)
        validate_q2m2_visibility = MsgTypeString("q2m2:TMMI_MCR_IS_VISIBLE", value=q2m2_visibility_expected)
        validate_t10_visibility = MsgTypeString("t10:TMMI_MCR_IS_VISIBLE", value=t10_visibility_expected)
        validate_q1g2_visibility = MsgTypeString("q1g2:TMMI_MCR_IS_VISIBLE", value=q1g2_visibility_expected)
        validate_q2g2_visibility = MsgTypeString("q2g2:TMMI_MCR_IS_VISIBLE", value=q2g2_visibility_expected)
        validate_q3g2_visibility = MsgTypeString("q3g2:TMMI_MCR_IS_VISIBLE", value=q3g2_visibility_expected)
        validate_q4g2_visibility = MsgTypeString("q4g2:TMMI_MCR_IS_VISIBLE", value=q4g2_visibility_expected)
        validate_q5g2_visibility = MsgTypeString("q5g2:TMMI_MCR_IS_VISIBLE", value=q5g2_visibility_expected)
        validate_t9g2_visibility = MsgTypeString("t9g2:TMMI_MCR_IS_VISIBLE", value=t9g2_visibility_expected)
        validate_t10g2_visibility = MsgTypeString("t10g2:TMMI_MCR_IS_VISIBLE", value=t10g2_visibility_expected)
        validate_b1g2_visibility = MsgTypeString("b1g2:TMMI_MCR_IS_VISIBLE", value=b1g2_visibility_expected)
        validate_bpm5m2_in_visibility = MsgTypeString("bpm5m2_in:TMMI_MCR_IS_VISIBLE", value=bpm5m2_in_visibility_expected)
        validate_bpm5m2_out_btn_visibility = MsgTypeString("bpm5m2_out_btn:TMMI_MCR_IS_VISIBLE", value=bpm5m2_out_btn_visibility_expected)
        validate_bpm5m2_in_btn_visibility = MsgTypeString("bpm5m2_in_btn:TMMI_MCR_IS_VISIBLE", value=bpm5m2_in_btn_visibility_expected)
        validate_bpm5m2_in_btn_led_visibility = MsgTypeString("bpm5m2_in_btn_led:TMMI_MCR_IS_VISIBLE", value=bpm5m2_in_btn_led_visibility_expected)
        validate_bpm5m2_out_btn_led_visibility = MsgTypeString("bpm5m2_out_btn_led:TMMI_MCR_IS_VISIBLE", value=bpm5m2_out_btn_led_visibility_expected)
        validate_bpm5m2_out_visibility = MsgTypeString("bpm5m2_out:TMMI_MCR_IS_VISIBLE", value=bpm5m2_out_visibility_expected)
        validate_bpm7g2_in_visibility = MsgTypeString("bpm7g2_in:TMMI_MCR_IS_VISIBLE", value=bpm7g2_in_visibility_expected)
        validate_bpm7g2_out_btn_visibility = MsgTypeString("bpm7g2_out_btn:TMMI_MCR_IS_VISIBLE", value=bpm7g2_out_btn_visibility_expected)
        validate_bpm7g2_in_btn_visibility = MsgTypeString("bpm7g2_in_btn:TMMI_MCR_IS_VISIBLE", value=bpm7g2_in_btn_visibility_expected)
        validate_bpm7g2_btn_led_visibility = MsgTypeString("bpm7g2_btn_led:TMMI_MCR_IS_VISIBLE", value=bpm7g2_btn_led_visibility_expected)
        validate_bpm7g2_out_btn_led_visibility = MsgTypeString("bpm7g2_out_btn_led:TMMI_MCR_IS_VISIBLE", value=bpm7g2_out_btn_led_visibility_expected)
        validate_bpm7g2_out_visibility = MsgTypeString("bpm7g2_out:TMMI_MCR_IS_VISIBLE", value=bpm7g2_out_visibility_expected)
        validate_bpm8g2_in_visibility = MsgTypeString("bpm8g2_in:TMMI_MCR_IS_VISIBLE", value=bpm8g2_in_visibility_expected)
        validate_bpm8g2_out_btn_visibility = MsgTypeString("bpm8g2_out_btn:TMMI_MCR_IS_VISIBLE", value=bpm8g2_out_btn_visibility_expected)
        validate_bpm8g2_in_btn_visibility = MsgTypeString("bpm8g2_in_btn:TMMI_MCR_IS_VISIBLE", value=bpm8g2_in_btn_visibility_expected)
        validate_bpm8g2_in_btn_led_visibility = MsgTypeString("bpm8g2_in_btn_led:TMMI_MCR_IS_VISIBLE", value=bpm8g2_in_btn_led_visibility_expected)
        validate_bpm8g2_out_btn_led_visibility = MsgTypeString("bpm8g2_out_btn_led:TMMI_MCR_IS_VISIBLE", value=bpm8g2_out_btn_led_visibility_expected)
        validate_bpm8g2_out_visibility = MsgTypeString("bpm8g2_out:TMMI_MCR_IS_VISIBLE", value=bpm8g2_out_visibility_expected)
        validate_bpm9g2_in_visibility = MsgTypeString("bpm9g2_in:TMMI_MCR_IS_VISIBLE", value=bpm9g2_in_visibility_expected)
        validate_bpm9g2_out_btn_visibility = MsgTypeString("bpm9g2_out_btn:TMMI_MCR_IS_VISIBLE", value=bpm9g2_out_btn_visibility_expected)
        validate_bpm9g2_in_btn_visibility = MsgTypeString("bpm9g2_in_btn:TMMI_MCR_IS_VISIBLE", value=bpm9g2_in_btn_visibility_expected)
        validate_bpm9g2_in_btn_led_visibility = MsgTypeString("bpm9g2_in_btn_led:TMMI_MCR_IS_VISIBLE", value=bpm9g2_in_btn_led_visibility_expected)
        validate_bpm9g2_out_btn_led_visibility = MsgTypeString("bpm9g2_out_btn_led:TMMI_MCR_IS_VISIBLE", value=bpm9g2_out_btn_led_visibility_expected)
        validate_bpm9g2_out_visibility = MsgTypeString("bpm9g2_out:TMMI_MCR_IS_VISIBLE", value=bpm9g2_out_visibility_expected)
        validate_b2g2_visibility = MsgTypeString("b2g2:TMMI_MCR_IS_VISIBLE", value=b2g2_visibility_expected)
        validate_bts2_layout_btn_visibility = MsgTypeString("bts2_layout_btn:TMMI_MCR_IS_VISIBLE", value=bts2_layout_btn_visibility_expected)

        info_exchange = [
                        InformationSet("get q0m2 visibility", "thriver", "mcrhci", get_q0m2_visibility),
                        InformationSet("validate q0m2 visibility = " + str(q0m2_visibility_expected), "mcrhci", "hcitracer", validate_q0m2_visibility),
                        InformationSet("get q1m2 visibility", "thriver", "mcrhci", get_q1m2_visibility),
                        InformationSet("validate q1m2 visibility = " + str(q1m2_visibility_expected), "mcrhci", "hcitracer", validate_q1m2_visibility),
                        InformationSet("get q3m2 visibility", "thriver", "mcrhci", get_q3m2_visibility),
                        InformationSet("validate q3m2 visibility = " + str(q3m2_visibility_expected), "mcrhci", "hcitracer", validate_q3m2_visibility),
                        InformationSet("get q2m2 visibility", "thriver", "mcrhci", get_q2m2_visibility),
                        InformationSet("validate q2m2 visibility = " + str(q2m2_visibility_expected), "mcrhci", "hcitracer", validate_q2m2_visibility),
                        InformationSet("get t10 visibility", "thriver", "mcrhci", get_t10_visibility),
                        InformationSet("validate t10 visibility = " + str(t10_visibility_expected), "mcrhci", "hcitracer", validate_t10_visibility),
                        InformationSet("get q1g2 visibility", "thriver", "mcrhci", get_q1g2_visibility),
                        InformationSet("validate q1g2 visibility = " + str(q1g2_visibility_expected), "mcrhci", "hcitracer", validate_q1g2_visibility),
                        InformationSet("get q2g2 visibility", "thriver", "mcrhci", get_q2g2_visibility),
                        InformationSet("validate q2g2 visibility = " + str(q2g2_visibility_expected), "mcrhci", "hcitracer", validate_q2g2_visibility),
                        InformationSet("get q3g2 visibility", "thriver", "mcrhci", get_q3g2_visibility),
                        InformationSet("validate q3g2 visibility = " + str(q3g2_visibility_expected), "mcrhci", "hcitracer", validate_q3g2_visibility),
                        InformationSet("get q4g2 visibility", "thriver", "mcrhci", get_q4g2_visibility),
                        InformationSet("validate q4g2 visibility = " + str(q4g2_visibility_expected), "mcrhci", "hcitracer", validate_q4g2_visibility),
                        InformationSet("get q5g2 visibility", "thriver", "mcrhci", get_q5g2_visibility),
                        InformationSet("validate q5g2 visibility = " + str(q5g2_visibility_expected), "mcrhci", "hcitracer", validate_q5g2_visibility),
                        InformationSet("get t9g2 visibility", "thriver", "mcrhci", get_t9g2_visibility),
                        InformationSet("validate t9g2 visibility = " + str(t9g2_visibility_expected), "mcrhci", "hcitracer", validate_t9g2_visibility),
                        InformationSet("get t10g2 visibility", "thriver", "mcrhci", get_t10g2_visibility),
                        InformationSet("validate t10g2 visibility = " + str(t10g2_visibility_expected), "mcrhci", "hcitracer", validate_t10g2_visibility),
                        InformationSet("get b1g2 visibility", "thriver", "mcrhci", get_b1g2_visibility),
                        # Bug: cannot get the visibility of b1g2
                        # InformationSet("validate b1g2 visibility = " + str(b1g2_visibility_expected), "mcrhci", "hcitracer", validate_b1g2_visibility),
                        InformationSet("set mcr_ecubtcu_bpm5m2_instatus = "+ str(mcr_ecubtcu_bpm5m2_instatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpm5m2_instatus_1),
                        InformationSet("get bpm5m2_in visibility", "thriver", "mcrhci", get_bpm5m2_in_visibility),
                        InformationSet("validate bpm5m2_in visibility = " + str(bpm5m2_in_visibility_expected), "mcrhci", "hcitracer", validate_bpm5m2_in_visibility),
                        InformationSet("get bpm5m2_out_btn visibility", "thriver", "mcrhci", get_bpm5m2_out_btn_visibility),
                        InformationSet("validate bpm5m2_out_btn visibility = " + str(bpm5m2_out_btn_visibility_expected), "mcrhci", "hcitracer", validate_bpm5m2_out_btn_visibility),
                        InformationSet("get bpm5m2_in_btn visibility", "thriver", "mcrhci", get_bpm5m2_in_btn_visibility),
                        InformationSet("validate bpm5m2_in_btn visibility = " + str(bpm5m2_in_btn_visibility_expected), "mcrhci", "hcitracer", validate_bpm5m2_in_btn_visibility),
                        InformationSet("set mcr_ecubtcu_bpm5m2_instatus = "+ str(mcr_ecubtcu_bpm5m2_instatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpm5m2_instatus_2),
                        InformationSet("get bpm5m2_in_btn_led visibility", "thriver", "mcrhci", get_bpm5m2_in_btn_led_visibility),
                        InformationSet("validate bpm5m2_in_btn_led visibility = " + str(bpm5m2_in_btn_led_visibility_expected), "mcrhci", "hcitracer", validate_bpm5m2_in_btn_led_visibility),
                        InformationSet("set mcr_ecubtcu_bpm5m2_outstatus = "+ str(mcr_ecubtcu_bpm5m2_outstatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpm5m2_outstatus_1),
                        InformationSet("get bpm5m2_out_btn_led visibility", "thriver", "mcrhci", get_bpm5m2_out_btn_led_visibility),
                        InformationSet("validate bpm5m2_out_btn_led visibility = " + str(bpm5m2_out_btn_led_visibility_expected), "mcrhci", "hcitracer", validate_bpm5m2_out_btn_led_visibility),
                        InformationSet("set mcr_ecubtcu_bpm5m2_outstatus = "+ str(mcr_ecubtcu_bpm5m2_outstatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpm5m2_outstatus_2),
                        InformationSet("get bpm5m2_out visibility", "thriver", "mcrhci", get_bpm5m2_out_visibility),
                        InformationSet("validate bpm5m2_out visibility = " + str(bpm5m2_out_visibility_expected), "mcrhci", "hcitracer", validate_bpm5m2_out_visibility),
                        InformationSet("set mcr_ecubtcu_bpm7g2_instatus = "+ str(mcr_ecubtcu_bpm7g2_instatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpm7g2_instatus_1),
                        InformationSet("get bpm7g2_in visibility", "thriver", "mcrhci", get_bpm7g2_in_visibility),
                        InformationSet("validate bpm7g2_in visibility = " + str(bpm7g2_in_visibility_expected), "mcrhci", "hcitracer", validate_bpm7g2_in_visibility),
                        InformationSet("get bpm7g2_out_btn visibility", "thriver", "mcrhci", get_bpm7g2_out_btn_visibility),
                        InformationSet("validate bpm7g2_out_btn visibility = " + str(bpm7g2_out_btn_visibility_expected), "mcrhci", "hcitracer", validate_bpm7g2_out_btn_visibility),
                        InformationSet("get bpm7g2_in_btn visibility", "thriver", "mcrhci", get_bpm7g2_in_btn_visibility),
                        InformationSet("validate bpm7g2_in_btn visibility = " + str(bpm7g2_in_btn_visibility_expected), "mcrhci", "hcitracer", validate_bpm7g2_in_btn_visibility),
                        InformationSet("set mcr_ecubtcu_bpm7g2_instatus = "+ str(mcr_ecubtcu_bpm7g2_instatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpm7g2_instatus_2),
                        InformationSet("get bpm7g2_btn_led visibility", "thriver", "mcrhci", get_bpm7g2_btn_led_visibility),
                        InformationSet("validate bpm7g2_btn_led visibility = " + str(bpm7g2_btn_led_visibility_expected), "mcrhci", "hcitracer", validate_bpm7g2_btn_led_visibility),
                        InformationSet("set mcr_ecubtcu_bpm7g2_outstatus = "+ str(mcr_ecubtcu_bpm7g2_outstatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpm7g2_outstatus_1),
                        InformationSet("get bpm7g2_out_btn_led visibility", "thriver", "mcrhci", get_bpm7g2_out_btn_led_visibility),
                        InformationSet("validate bpm7g2_out_btn_led visibility = " + str(bpm7g2_out_btn_led_visibility_expected), "mcrhci", "hcitracer", validate_bpm7g2_out_btn_led_visibility),
                        InformationSet("set mcr_ecubtcu_bpm7g2_outstatus = "+ str(mcr_ecubtcu_bpm7g2_outstatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpm7g2_outstatus_2),
                        InformationSet("get bpm7g2_out visibility", "thriver", "mcrhci", get_bpm7g2_out_visibility),
                        InformationSet("validate bpm7g2_out visibility = " + str(bpm7g2_out_visibility_expected), "mcrhci", "hcitracer", validate_bpm7g2_out_visibility),
                        InformationSet("set mcr_ecubtcu_bpm8g2_instatus = "+ str(mcr_ecubtcu_bpm8g2_instatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpm8g2_instatus_1),
                        InformationSet("get bpm8g2_in visibility", "thriver", "mcrhci", get_bpm8g2_in_visibility),
                        InformationSet("validate bpm8g2_in visibility = " + str(bpm8g2_in_visibility_expected), "mcrhci", "hcitracer", validate_bpm8g2_in_visibility),
                        InformationSet("get bpm8g2_out_btn visibility", "thriver", "mcrhci", get_bpm8g2_out_btn_visibility),
                        InformationSet("validate bpm8g2_out_btn visibility = " + str(bpm8g2_out_btn_visibility_expected), "mcrhci", "hcitracer", validate_bpm8g2_out_btn_visibility),
                        InformationSet("get bpm8g2_in_btn visibility", "thriver", "mcrhci", get_bpm8g2_in_btn_visibility),
                        InformationSet("validate bpm8g2_in_btn visibility = " + str(bpm8g2_in_btn_visibility_expected), "mcrhci", "hcitracer", validate_bpm8g2_in_btn_visibility),
                        InformationSet("set mcr_ecubtcu_bpm8g2_instatus = "+ str(mcr_ecubtcu_bpm8g2_instatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpm8g2_instatus_2),
                        InformationSet("get bpm8g2_in_btn_led visibility", "thriver", "mcrhci", get_bpm8g2_in_btn_led_visibility),
                        InformationSet("validate bpm8g2_in_btn_led visibility = " + str(bpm8g2_in_btn_led_visibility_expected), "mcrhci", "hcitracer", validate_bpm8g2_in_btn_led_visibility),
                        InformationSet("set mcr_ecubtcu_bpm8g2_outstatus = "+ str(mcr_ecubtcu_bpm8g2_outstatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpm8g2_outstatus_1),
                        InformationSet("get bpm8g2_out_btn_led visibility", "thriver", "mcrhci", get_bpm8g2_out_btn_led_visibility),
                        InformationSet("validate bpm8g2_out_btn_led visibility = " + str(bpm8g2_out_btn_led_visibility_expected), "mcrhci", "hcitracer", validate_bpm8g2_out_btn_led_visibility),
                        InformationSet("set mcr_ecubtcu_bpm8g2_outstatus = "+ str(mcr_ecubtcu_bpm8g2_outstatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpm8g2_outstatus_2),
                        InformationSet("get bpm8g2_out visibility", "thriver", "mcrhci", get_bpm8g2_out_visibility),
                        InformationSet("validate bpm8g2_out visibility = " + str(bpm8g2_out_visibility_expected), "mcrhci", "hcitracer", validate_bpm8g2_out_visibility),
                        InformationSet("set mcr_ecubtcu_bpm9g2_instatus = "+ str(mcr_ecubtcu_bpm9g2_instatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpm9g2_instatus_1),
                        InformationSet("get bpm9g2_in visibility", "thriver", "mcrhci", get_bpm9g2_in_visibility),
                        InformationSet("validate bpm9g2_in visibility = " + str(bpm9g2_in_visibility_expected), "mcrhci", "hcitracer", validate_bpm9g2_in_visibility),
                        InformationSet("get bpm9g2_out_btn visibility", "thriver", "mcrhci", get_bpm9g2_out_btn_visibility),
                        InformationSet("validate bpm9g2_out_btn visibility = " + str(bpm9g2_out_btn_visibility_expected), "mcrhci", "hcitracer", validate_bpm9g2_out_btn_visibility),
                        InformationSet("get bpm9g2_in_btn visibility", "thriver", "mcrhci", get_bpm9g2_in_btn_visibility),
                        InformationSet("validate bpm9g2_in_btn visibility = " + str(bpm9g2_in_btn_visibility_expected), "mcrhci", "hcitracer", validate_bpm9g2_in_btn_visibility),
                        InformationSet("set mcr_ecubtcu_bpm9g2_instatus = "+ str(mcr_ecubtcu_bpm9g2_instatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpm9g2_instatus_2),
                        InformationSet("get bpm9g2_in_btn_led visibility", "thriver", "mcrhci", get_bpm9g2_in_btn_led_visibility),
                        InformationSet("validate bpm9g2_in_btn_led visibility = " + str(bpm9g2_in_btn_led_visibility_expected), "mcrhci", "hcitracer", validate_bpm9g2_in_btn_led_visibility),
                        InformationSet("set mcr_ecubtcu_bpm9g2_outstatus = "+ str(mcr_ecubtcu_bpm9g2_outstatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpm9g2_outstatus_1),
                        InformationSet("get bpm9g2_out_btn_led visibility", "thriver", "mcrhci", get_bpm9g2_out_btn_led_visibility),
                        InformationSet("validate bpm9g2_out_btn_led visibility = " + str(bpm9g2_out_btn_led_visibility_expected), "mcrhci", "hcitracer", validate_bpm9g2_out_btn_led_visibility),
                        InformationSet("set mcr_ecubtcu_bpm9g2_outstatus = "+ str(mcr_ecubtcu_bpm9g2_outstatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpm9g2_outstatus_2),
                        InformationSet("get bpm9g2_out visibility", "thriver", "mcrhci", get_bpm9g2_out_visibility),
                        InformationSet("validate bpm9g2_out visibility = " + str(bpm9g2_out_visibility_expected), "mcrhci", "hcitracer", validate_bpm9g2_out_visibility),
                        InformationSet("get b2g2 visibility", "thriver", "mcrhci", get_b2g2_visibility),
                        InformationSet("validate b2g2 visibility = " + str(b2g2_visibility_expected), "mcrhci", "hcitracer", validate_b2g2_visibility),
                        InformationSet("get bts2_layout_btn visibility", "thriver", "mcrhci", get_bts2_layout_btn_visibility),
                        InformationSet("validate bts2_layout_btn visibility = " + str(bts2_layout_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts2_layout_btn_visibility),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []