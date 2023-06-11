
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

class SETUP_VALIDATE_ESS_LAYOUT_SCREEN(ClinicalIntegrationTestProcedure):
    # default variable values
    name = "Confirm that MCR_Service_ESS_Layout (ess_layout.v) is displayed"
    bs2_out_btn_visibility_expected = "1"
    mcr_rtieecubtcu_bcm1_lowdata_visibility_init_1 = True
    bs1_61_fdbk_visibility_expected = "1"
    mcr_ecubtcu_bs1_cfeedback_init_1 = 1
    bs1_61_fdbk_value_expected = 1
    mcr_ecubtcu_bs1_cfeedback_init_2 = 1
    bs1_fdbk_value_expected = 1
    mcr_rtieecubtcu_bcm1_highdata_visibility_init_1 = True
    bs1_fdbk_visibility_expected = "1"
    d1_golastpos_cmdenable_init_1 = True
    d1_golastpos_disable_visibility_expected = "0"
    d1_gopt_cmdenable_init_1 = True
    d1_gopt_disable_visibility_expected = "0"
    d1_gobs_cmdenable_init_1 = True
    d1_gobs_disable_visibility_expected = "0"
    d1_gobpm_cmdenable_init_1 = True
    d1_gobpm_disable_visibility_expected = "0"
    d1_gohome_cmdenable_init_1 = True
    d1_gohome_disable_visibility_expected = "0"
    d1_golastpos_visibility_expected = "1"
    d1_gobs_visibility_expected = "1"
    mcr_ecubtcu_bpm3_instatus_init_1 = True
    bpm3_in_visibility_expected = "1"
    b1_visibility_expected = "1"
    q1_visibility_expected = "1"
    q11_visibility_expected = "1"
    q10_visibility_expected = "1"
    q2_visibility_expected = "1"
    b2_visibility_expected = "1"
    q12_visibility_expected = "1"
    q20_visibility_expected = "1"
    q14_visibility_expected = "1"
    q13_visibility_expected = "1"
    q15_visibility_expected = "1"
    b3_visibility_expected = "1"
    b4_visibility_expected = "1"
    q21_visibility_expected = "1"
    q22_visibility_expected = "1"
    q9_visibility_expected = "1"
    degrader_visibility_expected = "1"
    T6_visibility_expected = "1"
    T7_visibility_expected = "1"
    T2_visibility_expected = "1"
    sl1_visibility_expected = "1"
    sl2_visibility_expected = "1"
    mcr_ecubtcu_sstech_ps_status_init_1 = 1
    ext_int_txt_foreground_color_expected = "0"
    mcr_ecubtcu_sstech_ps_status_init_2 = 1
    ext_int_chk_subobject_name_expected = "iba_check_ok.sd"
    bs2_in_btn_visibility_expected = "1"
    mcr_ecubtcu_bs2_instatus_init_1 = True
    bs2_in_led_visibility_expected = "1"
    mcr_ecubtcu_bs2_outstatus_init_1 = True
    bs2_out_led_visibility_expected = "1"
    mcr_ecubtcu_piraniess_mbarvacuum_init_1 = 0
    pirani_gauge_xxx_visibility_expected = "1"
    mcr_ecubtcu_piraniess_mbarvacuum_init_3 = 0
    pirani_gauge_mbar_visibility_expected = "1"
    d1_gopt_visibility_expected = "1"
    d1_gobpm_visibility_expected = "1"
    mcr_ecubtcu_degrader_status_init_1 = 0
    d1_gobpm_led_visibility_expected = "0"
    mcr_ecubtcu_degrader_status_init_2 = 0
    d1_gobs_led_visibility_expected = "0"
    mcr_ecubtcu_degrader_status_init_3 = 0
    d1_gopt_led_visibility_expected = "0"
    BPM3_out_btn_visibility_expected = "1"
    BPM3_in_btn_visibility_expected = "1"
    mcr_ecubtcu_bpm3_instatus_init_2 = True
    BPM3_in_led_visibility_expected = "1"
    mcr_ecubtcu_bpm3_outstatus_init_1 = True
    BPM3_out_led_visibility_expected = "1"
    mcr_ecubtcu_degrader_status_init_4 = 0
    is_moving_txt_visibility_expected = "0"
    mcr_acu_vacuumess_status_init_1 = True
    pirani_Gauge_foreground_color_expected = "13"
    mcr_ecubtcu_bpm3_outstatus_init_2 = True
    bpm3_out_visibility_expected = "1"
    mcr_ecubtcu_piraniess_mbarvacuum_init_4 = 0
    pirani_gauge_out_of_range_txt_visibility_expected = "0"
    cyclone_gif_visibility_expected = "1"
    bts1_layout_btn_visibility_expected = "1"
    mcr_rtieecubtcu_bcm1_lowdata_visibility_init_2 = True
    c2_61_fdbk_visibility_expected = "1"
    mcr_ecubtcu_c2_cfeedback_init_1 = 1.5
    c2_61_fdbk_value_expected = 1.5
    mcr_rtieecubtcu_bcm1_highdata_visibility_init_2 = True
    c2_fdbk_visibility_expected = "1"
    mcr_ecubtcu_c2_cfeedback_init_2 = 1.5
    c2_fdbk_value_expected = 1.5
    mcr_ecubtcu_degrader_status_init_5 = 1.5
    d1_golastpos_led_visibility_expected = "0"
    mcr_ecubtcu_degrader_feedbackstep_init_1 = 1.5
    step_txt_value_expected = 1.5
    mcr_scu_safety_ess_bsoutenable_init_1 = True
    safety_interlocks_btn_foreground_color_expected = "112"
    mcr_acu_b1_waterflow_init_1 = True
    B1_waterflow_visibility_expected = "0"
    mcr_acu_b2_waterflow_init_1 = True
    B2_waterflow_visibility_expected = "0"
    mcr_acu_b4_waterflow_init_1 = True
    B4_waterflow_visibility_expected = "0"
    mcr_acu_b3_waterflow_init_1 = True
    B3_waterflow_visibility_expected = "0"
    mcr_rtieecubtcu_bcm2_lowdata_visibility_init_1 = True
    bs2_61_fdbk_visibility_expected = "1"
    mcr_ecubtcu_bs2_cfeedback_init_1 = 1.5
    bs2_61_fdbk_value_expected = 1.5
    mcr_ecubtcu_bs2_cfeedback_init_2 = 1.5
    bs2_fdbk_value_expected = 1.5
    mcr_rtieecubtcu_bcm2_highdata_visibility_init_1 = True
    bs2_fdbk_visibility_expected = "1"
    d1_gohome_visibility_expected = "1"
    title_btn_visibility_expected = "1"

    def __init__(self, test):
        cls = type(self)
        name = cls.name
        bs2_out_btn_visibility_expected = cls.bs2_out_btn_visibility_expected
        mcr_rtieecubtcu_bcm1_lowdata_visibility_init_1 = cls.mcr_rtieecubtcu_bcm1_lowdata_visibility_init_1
        bs1_61_fdbk_visibility_expected = cls.bs1_61_fdbk_visibility_expected
        mcr_ecubtcu_bs1_cfeedback_init_1 = cls.mcr_ecubtcu_bs1_cfeedback_init_1
        bs1_61_fdbk_value_expected = cls.bs1_61_fdbk_value_expected
        mcr_ecubtcu_bs1_cfeedback_init_2 = cls.mcr_ecubtcu_bs1_cfeedback_init_2
        bs1_fdbk_value_expected = cls.bs1_fdbk_value_expected
        mcr_rtieecubtcu_bcm1_highdata_visibility_init_1 = cls.mcr_rtieecubtcu_bcm1_highdata_visibility_init_1
        bs1_fdbk_visibility_expected = cls.bs1_fdbk_visibility_expected
        d1_golastpos_cmdenable_init_1 = cls.d1_golastpos_cmdenable_init_1
        d1_golastpos_disable_visibility_expected = cls.d1_golastpos_disable_visibility_expected
        d1_gopt_cmdenable_init_1 = cls.d1_gopt_cmdenable_init_1
        d1_gopt_disable_visibility_expected = cls.d1_gopt_disable_visibility_expected
        d1_gobs_cmdenable_init_1 = cls.d1_gobs_cmdenable_init_1
        d1_gobs_disable_visibility_expected = cls.d1_gobs_disable_visibility_expected
        d1_gobpm_cmdenable_init_1 = cls.d1_gobpm_cmdenable_init_1
        d1_gobpm_disable_visibility_expected = cls.d1_gobpm_disable_visibility_expected
        d1_gohome_cmdenable_init_1 = cls.d1_gohome_cmdenable_init_1
        d1_gohome_disable_visibility_expected = cls.d1_gohome_disable_visibility_expected
        d1_golastpos_visibility_expected = cls.d1_golastpos_visibility_expected
        d1_gobs_visibility_expected = cls.d1_gobs_visibility_expected
        mcr_ecubtcu_bpm3_instatus_init_1 = cls.mcr_ecubtcu_bpm3_instatus_init_1
        bpm3_in_visibility_expected = cls.bpm3_in_visibility_expected
        b1_visibility_expected = cls.b1_visibility_expected
        q1_visibility_expected = cls.q1_visibility_expected
        q11_visibility_expected = cls.q11_visibility_expected
        q10_visibility_expected = cls.q10_visibility_expected
        q2_visibility_expected = cls.q2_visibility_expected
        b2_visibility_expected = cls.b2_visibility_expected
        q12_visibility_expected = cls.q12_visibility_expected
        q20_visibility_expected = cls.q20_visibility_expected
        q14_visibility_expected = cls.q14_visibility_expected
        q13_visibility_expected = cls.q13_visibility_expected
        q15_visibility_expected = cls.q15_visibility_expected
        b3_visibility_expected = cls.b3_visibility_expected
        b4_visibility_expected = cls.b4_visibility_expected
        q21_visibility_expected = cls.q21_visibility_expected
        q22_visibility_expected = cls.q22_visibility_expected
        q9_visibility_expected = cls.q9_visibility_expected
        degrader_visibility_expected = cls.degrader_visibility_expected
        T6_visibility_expected = cls.T6_visibility_expected
        T7_visibility_expected = cls.T7_visibility_expected
        T2_visibility_expected = cls.T2_visibility_expected
        sl1_visibility_expected = cls.sl1_visibility_expected
        sl2_visibility_expected = cls.sl2_visibility_expected
        mcr_ecubtcu_sstech_ps_status_init_1 = cls.mcr_ecubtcu_sstech_ps_status_init_1
        ext_int_txt_foreground_color_expected = cls.ext_int_txt_foreground_color_expected
        mcr_ecubtcu_sstech_ps_status_init_2 = cls.mcr_ecubtcu_sstech_ps_status_init_2
        ext_int_chk_subobject_name_expected = cls.ext_int_chk_subobject_name_expected
        bs2_in_btn_visibility_expected = cls.bs2_in_btn_visibility_expected
        mcr_ecubtcu_bs2_instatus_init_1 = cls.mcr_ecubtcu_bs2_instatus_init_1
        bs2_in_led_visibility_expected = cls.bs2_in_led_visibility_expected
        mcr_ecubtcu_bs2_outstatus_init_1 = cls.mcr_ecubtcu_bs2_outstatus_init_1
        bs2_out_led_visibility_expected = cls.bs2_out_led_visibility_expected
        mcr_ecubtcu_piraniess_mbarvacuum_init_1 = cls.mcr_ecubtcu_piraniess_mbarvacuum_init_1
        pirani_gauge_xxx_visibility_expected = cls.pirani_gauge_xxx_visibility_expected
        mcr_ecubtcu_piraniess_mbarvacuum_init_3 = cls.mcr_ecubtcu_piraniess_mbarvacuum_init_3
        pirani_gauge_mbar_visibility_expected = cls.pirani_gauge_mbar_visibility_expected
        d1_gopt_visibility_expected = cls.d1_gopt_visibility_expected
        d1_gobpm_visibility_expected = cls.d1_gobpm_visibility_expected
        mcr_ecubtcu_degrader_status_init_1 = cls.mcr_ecubtcu_degrader_status_init_1
        d1_gobpm_led_visibility_expected = cls.d1_gobpm_led_visibility_expected
        mcr_ecubtcu_degrader_status_init_2 = cls.mcr_ecubtcu_degrader_status_init_2
        d1_gobs_led_visibility_expected = cls.d1_gobs_led_visibility_expected
        mcr_ecubtcu_degrader_status_init_3 = cls.mcr_ecubtcu_degrader_status_init_3
        d1_gopt_led_visibility_expected = cls.d1_gopt_led_visibility_expected
        BPM3_out_btn_visibility_expected = cls.BPM3_out_btn_visibility_expected
        BPM3_in_btn_visibility_expected = cls.BPM3_in_btn_visibility_expected
        mcr_ecubtcu_bpm3_instatus_init_2 = cls.mcr_ecubtcu_bpm3_instatus_init_2
        BPM3_in_led_visibility_expected = cls.BPM3_in_led_visibility_expected
        mcr_ecubtcu_bpm3_outstatus_init_1 = cls.mcr_ecubtcu_bpm3_outstatus_init_1
        BPM3_out_led_visibility_expected = cls.BPM3_out_led_visibility_expected
        mcr_ecubtcu_degrader_status_init_4 = cls.mcr_ecubtcu_degrader_status_init_4
        is_moving_txt_visibility_expected = cls.is_moving_txt_visibility_expected
        mcr_acu_vacuumess_status_init_1 = cls.mcr_acu_vacuumess_status_init_1
        pirani_Gauge_foreground_color_expected = cls.pirani_Gauge_foreground_color_expected
        mcr_ecubtcu_bpm3_outstatus_init_2 = cls.mcr_ecubtcu_bpm3_outstatus_init_2
        bpm3_out_visibility_expected = cls.bpm3_out_visibility_expected
        mcr_ecubtcu_piraniess_mbarvacuum_init_4 = cls.mcr_ecubtcu_piraniess_mbarvacuum_init_4
        pirani_gauge_out_of_range_txt_visibility_expected = cls.pirani_gauge_out_of_range_txt_visibility_expected
        cyclone_gif_visibility_expected = cls.cyclone_gif_visibility_expected
        bts1_layout_btn_visibility_expected = cls.bts1_layout_btn_visibility_expected
        mcr_rtieecubtcu_bcm1_lowdata_visibility_init_2 = cls.mcr_rtieecubtcu_bcm1_lowdata_visibility_init_2
        c2_61_fdbk_visibility_expected = cls.c2_61_fdbk_visibility_expected
        mcr_ecubtcu_c2_cfeedback_init_1 = cls.mcr_ecubtcu_c2_cfeedback_init_1
        c2_61_fdbk_value_expected = cls.c2_61_fdbk_value_expected
        mcr_rtieecubtcu_bcm1_highdata_visibility_init_2 = cls.mcr_rtieecubtcu_bcm1_highdata_visibility_init_2
        c2_fdbk_visibility_expected = cls.c2_fdbk_visibility_expected
        mcr_ecubtcu_c2_cfeedback_init_2 = cls.mcr_ecubtcu_c2_cfeedback_init_2
        c2_fdbk_value_expected = cls.c2_fdbk_value_expected
        mcr_ecubtcu_degrader_status_init_5 = cls.mcr_ecubtcu_degrader_status_init_5
        d1_golastpos_led_visibility_expected = cls.d1_golastpos_led_visibility_expected
        mcr_ecubtcu_degrader_feedbackstep_init_1 = cls.mcr_ecubtcu_degrader_feedbackstep_init_1
        step_txt_value_expected = cls.step_txt_value_expected
        mcr_scu_safety_ess_bsoutenable_init_1 = cls.mcr_scu_safety_ess_bsoutenable_init_1
        safety_interlocks_btn_foreground_color_expected = cls.safety_interlocks_btn_foreground_color_expected
        mcr_acu_b1_waterflow_init_1 = cls.mcr_acu_b1_waterflow_init_1
        B1_waterflow_visibility_expected = cls.B1_waterflow_visibility_expected
        mcr_acu_b2_waterflow_init_1 = cls.mcr_acu_b2_waterflow_init_1
        B2_waterflow_visibility_expected = cls.B2_waterflow_visibility_expected
        mcr_acu_b4_waterflow_init_1 = cls.mcr_acu_b4_waterflow_init_1
        B4_waterflow_visibility_expected = cls.B4_waterflow_visibility_expected
        mcr_acu_b3_waterflow_init_1 = cls.mcr_acu_b3_waterflow_init_1
        B3_waterflow_visibility_expected = cls.B3_waterflow_visibility_expected
        mcr_rtieecubtcu_bcm2_lowdata_visibility_init_1 = cls.mcr_rtieecubtcu_bcm2_lowdata_visibility_init_1
        bs2_61_fdbk_visibility_expected = cls.bs2_61_fdbk_visibility_expected
        mcr_ecubtcu_bs2_cfeedback_init_1 = cls.mcr_ecubtcu_bs2_cfeedback_init_1
        bs2_61_fdbk_value_expected = cls.bs2_61_fdbk_value_expected
        mcr_ecubtcu_bs2_cfeedback_init_2 = cls.mcr_ecubtcu_bs2_cfeedback_init_2
        bs2_fdbk_value_expected = cls.bs2_fdbk_value_expected
        mcr_rtieecubtcu_bcm2_highdata_visibility_init_1 = cls.mcr_rtieecubtcu_bcm2_highdata_visibility_init_1
        bs2_fdbk_visibility_expected = cls.bs2_fdbk_visibility_expected
        d1_gohome_visibility_expected = cls.d1_gohome_visibility_expected
        title_btn_visibility_expected = cls.title_btn_visibility_expected

        #set initial values
        set_mcr_rtieecubtcu_bcm1_lowdata_visibility_1 = MsgTypeBoolean("mcr_rtieecubtcu_bcm1_lowdata_visibility", mcr_rtieecubtcu_bcm1_lowdata_visibility_init_1)
        set_mcr_ecubtcu_bs1_cfeedback_1 = MsgTypeNumeric("mcr_ecubtcu_bs1_cfeedback", mcr_ecubtcu_bs1_cfeedback_init_1)
        set_mcr_ecubtcu_bs1_cfeedback_2 = MsgTypeNumeric("mcr_ecubtcu_bs1_cfeedback", mcr_ecubtcu_bs1_cfeedback_init_2)
        set_mcr_rtieecubtcu_bcm1_highdata_visibility_1 = MsgTypeBoolean("mcr_rtieecubtcu_bcm1_highdata_visibility", mcr_rtieecubtcu_bcm1_highdata_visibility_init_1)
        set_d1_golastpos_cmdenable_1 = MsgTypeBoolean("d1_golastpos_cmdenable", d1_golastpos_cmdenable_init_1)
        set_d1_gopt_cmdenable_1 = MsgTypeBoolean("d1_gopt_cmdenable", d1_gopt_cmdenable_init_1)
        set_d1_gobs_cmdenable_1 = MsgTypeBoolean("d1_gobs_cmdenable", d1_gobs_cmdenable_init_1)
        set_d1_gobpm_cmdenable_1 = MsgTypeBoolean("d1_gobpm_cmdenable", d1_gobpm_cmdenable_init_1)
        set_d1_gohome_cmdenable_1 = MsgTypeBoolean("d1_gohome_cmdenable", d1_gohome_cmdenable_init_1)
        set_mcr_ecubtcu_bpm3_instatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpm3_instatus", mcr_ecubtcu_bpm3_instatus_init_1)
        set_mcr_ecubtcu_sstech_ps_status_1 = MsgTypeNumeric("mcr_ecubtcu_sstech_ps_status", mcr_ecubtcu_sstech_ps_status_init_1)
        set_mcr_ecubtcu_sstech_ps_status_2 = MsgTypeNumeric("mcr_ecubtcu_sstech_ps_status", mcr_ecubtcu_sstech_ps_status_init_2)
        set_mcr_ecubtcu_bs2_instatus_1 = MsgTypeBoolean("mcr_ecubtcu_bs2_instatus", mcr_ecubtcu_bs2_instatus_init_1)
        set_mcr_ecubtcu_bs2_outstatus_1 = MsgTypeBoolean("mcr_ecubtcu_bs2_outstatus", mcr_ecubtcu_bs2_outstatus_init_1)
        set_mcr_ecubtcu_piraniess_mbarvacuum_1 = MsgTypeNumeric("mcr_ecubtcu_piraniess_mbarvacuum", mcr_ecubtcu_piraniess_mbarvacuum_init_1)
        set_mcr_ecubtcu_piraniess_mbarvacuum_3 = MsgTypeNumeric("mcr_ecubtcu_piraniess_mbarvacuum", mcr_ecubtcu_piraniess_mbarvacuum_init_3)
        set_mcr_ecubtcu_degrader_status_1 = MsgTypeNumeric("mcr_ecubtcu_degrader_status", mcr_ecubtcu_degrader_status_init_1)
        set_mcr_ecubtcu_degrader_status_2 = MsgTypeNumeric("mcr_ecubtcu_degrader_status", mcr_ecubtcu_degrader_status_init_2)
        set_mcr_ecubtcu_degrader_status_3 = MsgTypeNumeric("mcr_ecubtcu_degrader_status", mcr_ecubtcu_degrader_status_init_3)
        set_mcr_ecubtcu_bpm3_instatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpm3_instatus", mcr_ecubtcu_bpm3_instatus_init_2)
        set_mcr_ecubtcu_bpm3_outstatus_1 = MsgTypeBoolean("mcr_ecubtcu_bpm3_outstatus", mcr_ecubtcu_bpm3_outstatus_init_1)
        set_mcr_ecubtcu_degrader_status_4 = MsgTypeNumeric("mcr_ecubtcu_degrader_status", mcr_ecubtcu_degrader_status_init_4)
        set_mcr_acu_vacuumess_status_1 = MsgTypeBoolean("mcr_acu_vacuumess_status", mcr_acu_vacuumess_status_init_1)
        set_mcr_ecubtcu_bpm3_outstatus_2 = MsgTypeBoolean("mcr_ecubtcu_bpm3_outstatus", mcr_ecubtcu_bpm3_outstatus_init_2)
        set_mcr_ecubtcu_piraniess_mbarvacuum_4 = MsgTypeNumeric("mcr_ecubtcu_piraniess_mbarvacuum", mcr_ecubtcu_piraniess_mbarvacuum_init_4)
        set_mcr_rtieecubtcu_bcm1_lowdata_visibility_2 = MsgTypeBoolean("mcr_rtieecubtcu_bcm1_lowdata_visibility", mcr_rtieecubtcu_bcm1_lowdata_visibility_init_2)
        set_mcr_ecubtcu_c2_cfeedback_1 = MsgTypeNumeric("mcr_ecubtcu_c2_cfeedback", mcr_ecubtcu_c2_cfeedback_init_1)
        set_mcr_rtieecubtcu_bcm1_highdata_visibility_2 = MsgTypeBoolean("mcr_rtieecubtcu_bcm1_highdata_visibility", mcr_rtieecubtcu_bcm1_highdata_visibility_init_2)
        set_mcr_ecubtcu_c2_cfeedback_2 = MsgTypeNumeric("mcr_ecubtcu_c2_cfeedback", mcr_ecubtcu_c2_cfeedback_init_2)
        set_mcr_ecubtcu_degrader_status_5 = MsgTypeNumeric("mcr_ecubtcu_degrader_status", mcr_ecubtcu_degrader_status_init_5)
        set_mcr_ecubtcu_degrader_feedbackstep_1 = MsgTypeNumeric("mcr_ecubtcu_degrader_feedbackstep", mcr_ecubtcu_degrader_feedbackstep_init_1)
        set_mcr_scu_safety_ess_bsoutenable_1 = MsgTypeBoolean("mcr_scu_safety_ess_bsoutenable", mcr_scu_safety_ess_bsoutenable_init_1)
        set_mcr_acu_b1_waterflow_1 = MsgTypeBoolean("mcr_acu_b1_waterflow", mcr_acu_b1_waterflow_init_1)
        set_mcr_acu_b2_waterflow_1 = MsgTypeBoolean("mcr_acu_b2_waterflow", mcr_acu_b2_waterflow_init_1)
        set_mcr_acu_b4_waterflow_1 = MsgTypeBoolean("mcr_acu_b4_waterflow", mcr_acu_b4_waterflow_init_1)
        set_mcr_acu_b3_waterflow_1 = MsgTypeBoolean("mcr_acu_b3_waterflow", mcr_acu_b3_waterflow_init_1)
        set_mcr_rtieecubtcu_bcm2_lowdata_visibility_1 = MsgTypeBoolean("mcr_rtieecubtcu_bcm2_lowdata_visibility", mcr_rtieecubtcu_bcm2_lowdata_visibility_init_1)
        set_mcr_ecubtcu_bs2_cfeedback_1 = MsgTypeNumeric("mcr_ecubtcu_bs2_cfeedback", mcr_ecubtcu_bs2_cfeedback_init_1)
        set_mcr_ecubtcu_bs2_cfeedback_2 = MsgTypeNumeric("mcr_ecubtcu_bs2_cfeedback", mcr_ecubtcu_bs2_cfeedback_init_2)
        set_mcr_rtieecubtcu_bcm2_highdata_visibility_1 = MsgTypeBoolean("mcr_rtieecubtcu_bcm2_highdata_visibility", mcr_rtieecubtcu_bcm2_highdata_visibility_init_1)

        #get values
        get_bs2_out_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bs2_out_btn")
        get_bs1_61_fdbk_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bs1_61_fdbk")
        get_bs1_61_fdbk_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "bs1_61_fdbk")
        get_bs1_fdbk_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "bs1_fdbk")
        get_bs1_fdbk_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bs1_fdbk")
        get_d1_golastpos_disable_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "d1_golastpos_disable")
        get_d1_gopt_disable_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "d1_gopt_disable")
        get_d1_gobs_disable_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "d1_gobs_disable")
        get_d1_gobpm_disable_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "d1_gobpm_disable")
        get_d1_gohome_disable_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "d1_gohome_disable")
        get_d1_golastpos_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "d1_golastpos")
        get_d1_gobs_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "d1_gobs")
        get_bpm3_in_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm3_in")
        get_b1_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "b1")
        get_q1_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q1")
        get_q11_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q11")
        get_q10_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q10")
        get_q2_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q2")
        get_b2_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "b2")
        get_q12_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q12")
        get_q20_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q20")
        get_q14_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q14")
        get_q13_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q13")
        get_q15_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q15")
        get_b3_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "b3")
        get_b4_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "b4")
        get_q21_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q21")
        get_q22_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q22")
        get_q9_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "q9")
        get_degrader_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "degrader")
        get_T6_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "T6")
        get_T7_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "T7")
        get_T2_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "T2")
        get_sl1_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "sl1")
        get_sl2_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "sl2")
        get_ext_int_txt_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "ext_int_txt")
        get_ext_int_chk_subobject_name = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "ext_int_chk")
        get_bs2_in_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bs2_in_btn")
        get_bs2_in_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bs2_in_led")
        get_bs2_out_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bs2_out_led")
        get_pirani_gauge_xxx_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "pirani_gauge_xxx")
        get_pirani_gauge_mbar_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "pirani_gauge_mbar")
        get_d1_gopt_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "d1_gopt")
        get_d1_gobpm_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "d1_gobpm")
        get_d1_gobpm_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "d1_gobpm_led")
        get_d1_gobs_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "d1_gobs_led")
        get_d1_gopt_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "d1_gopt_led")
        get_BPM3_out_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "BPM3_out_btn")
        get_BPM3_in_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "BPM3_in_btn")
        get_BPM3_in_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "BPM3_in_led")
        get_BPM3_out_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "BPM3_out_led")
        get_is_moving_txt_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "is_moving_txt")
        get_pirani_Gauge_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "pirani_Gauge")
        get_bpm3_out_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bpm3_out")
        get_pirani_gauge_out_of_range_txt_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "pirani_gauge_out_of_range_txt")
        get_cyclone_gif_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "cyclone_gif")
        get_bts1_layout_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_layout_btn")
        get_c2_61_fdbk_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "c2_61_fdbk")
        get_c2_61_fdbk_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "c2_61_fdbk")
        get_c2_fdbk_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "c2_fdbk")
        get_c2_fdbk_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "c2_fdbk")
        get_d1_golastpos_led_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "d1_golastpos_led")
        get_step_txt_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "step_txt")
        get_safety_interlocks_btn_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "safety_interlocks_btn")
        get_B1_waterflow_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "B1_waterflow")
        get_B2_waterflow_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "B2_waterflow")
        get_B4_waterflow_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "B4_waterflow")
        get_B3_waterflow_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "B3_waterflow")
        get_bs2_61_fdbk_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bs2_61_fdbk")
        get_bs2_61_fdbk_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "bs2_61_fdbk")
        get_bs2_fdbk_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "bs2_fdbk")
        get_bs2_fdbk_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bs2_fdbk")
        get_d1_gohome_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "d1_gohome")
        get_title_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "title_btn")

        #validate
        validate_bs2_out_btn_visibility = MsgTypeString("bs2_out_btn:TMMI_MCR_IS_VISIBLE", value=bs2_out_btn_visibility_expected)
        validate_bs1_61_fdbk_visibility = MsgTypeString("bs1_61_fdbk:TMMI_MCR_IS_VISIBLE", value=bs1_61_fdbk_visibility_expected)
        validate_bs1_61_fdbk_value = MsgTypeNumeric("bs1_61_fdbk:TMMI_MCR_OBJECT_GET_VALUE", value=bs1_61_fdbk_value_expected)
        validate_bs1_fdbk_value = MsgTypeNumeric("bs1_fdbk:TMMI_MCR_OBJECT_GET_VALUE", value=bs1_fdbk_value_expected)
        validate_bs1_fdbk_visibility = MsgTypeString("bs1_fdbk:TMMI_MCR_IS_VISIBLE", value=bs1_fdbk_visibility_expected)
        validate_d1_golastpos_disable_visibility = MsgTypeString("d1_golastpos_disable:TMMI_MCR_IS_VISIBLE", value=d1_golastpos_disable_visibility_expected)
        validate_d1_gopt_disable_visibility = MsgTypeString("d1_gopt_disable:TMMI_MCR_IS_VISIBLE", value=d1_gopt_disable_visibility_expected)
        validate_d1_gobs_disable_visibility = MsgTypeString("d1_gobs_disable:TMMI_MCR_IS_VISIBLE", value=d1_gobs_disable_visibility_expected)
        validate_d1_gobpm_disable_visibility = MsgTypeString("d1_gobpm_disable:TMMI_MCR_IS_VISIBLE", value=d1_gobpm_disable_visibility_expected)
        validate_d1_gohome_disable_visibility = MsgTypeString("d1_gohome_disable:TMMI_MCR_IS_VISIBLE", value=d1_gohome_disable_visibility_expected)
        validate_d1_golastpos_visibility = MsgTypeString("d1_golastpos:TMMI_MCR_IS_VISIBLE", value=d1_golastpos_visibility_expected)
        validate_d1_gobs_visibility = MsgTypeString("d1_gobs:TMMI_MCR_IS_VISIBLE", value=d1_gobs_visibility_expected)
        validate_bpm3_in_visibility = MsgTypeString("bpm3_in:TMMI_MCR_IS_VISIBLE", value=bpm3_in_visibility_expected)
        validate_b1_visibility = MsgTypeString("b1:TMMI_MCR_IS_VISIBLE", value=b1_visibility_expected)
        validate_q1_visibility = MsgTypeString("q1:TMMI_MCR_IS_VISIBLE", value=q1_visibility_expected)
        validate_q11_visibility = MsgTypeString("q11:TMMI_MCR_IS_VISIBLE", value=q11_visibility_expected)
        validate_q10_visibility = MsgTypeString("q10:TMMI_MCR_IS_VISIBLE", value=q10_visibility_expected)
        validate_q2_visibility = MsgTypeString("q2:TMMI_MCR_IS_VISIBLE", value=q2_visibility_expected)
        validate_b2_visibility = MsgTypeString("b2:TMMI_MCR_IS_VISIBLE", value=b2_visibility_expected)
        validate_q12_visibility = MsgTypeString("q12:TMMI_MCR_IS_VISIBLE", value=q12_visibility_expected)
        validate_q20_visibility = MsgTypeString("q20:TMMI_MCR_IS_VISIBLE", value=q20_visibility_expected)
        validate_q14_visibility = MsgTypeString("q14:TMMI_MCR_IS_VISIBLE", value=q14_visibility_expected)
        validate_q13_visibility = MsgTypeString("q13:TMMI_MCR_IS_VISIBLE", value=q13_visibility_expected)
        validate_q15_visibility = MsgTypeString("q15:TMMI_MCR_IS_VISIBLE", value=q15_visibility_expected)
        validate_b3_visibility = MsgTypeString("b3:TMMI_MCR_IS_VISIBLE", value=b3_visibility_expected)
        validate_b4_visibility = MsgTypeString("b4:TMMI_MCR_IS_VISIBLE", value=b4_visibility_expected)
        validate_q21_visibility = MsgTypeString("q21:TMMI_MCR_IS_VISIBLE", value=q21_visibility_expected)
        validate_q22_visibility = MsgTypeString("q22:TMMI_MCR_IS_VISIBLE", value=q22_visibility_expected)
        validate_q9_visibility = MsgTypeString("q9:TMMI_MCR_IS_VISIBLE", value=q9_visibility_expected)
        validate_degrader_visibility = MsgTypeString("degrader:TMMI_MCR_IS_VISIBLE", value=degrader_visibility_expected)
        validate_T6_visibility = MsgTypeString("T6:TMMI_MCR_IS_VISIBLE", value=T6_visibility_expected)
        validate_T7_visibility = MsgTypeString("T7:TMMI_MCR_IS_VISIBLE", value=T7_visibility_expected)
        validate_T2_visibility = MsgTypeString("T2:TMMI_MCR_IS_VISIBLE", value=T2_visibility_expected)
        validate_sl1_visibility = MsgTypeString("sl1:TMMI_MCR_IS_VISIBLE", value=sl1_visibility_expected)
        validate_sl2_visibility = MsgTypeString("sl2:TMMI_MCR_IS_VISIBLE", value=sl2_visibility_expected)
        validate_ext_int_txt_foreground_color = MsgTypeString("ext_int_txt:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=ext_int_txt_foreground_color_expected)
        validate_ext_int_chk_subobject_name = MsgTypeString("ext_int_chk:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=ext_int_chk_subobject_name_expected)
        validate_bs2_in_btn_visibility = MsgTypeString("bs2_in_btn:TMMI_MCR_IS_VISIBLE", value=bs2_in_btn_visibility_expected)
        validate_bs2_in_led_visibility = MsgTypeString("bs2_in_led:TMMI_MCR_IS_VISIBLE", value=bs2_in_led_visibility_expected)
        validate_bs2_out_led_visibility = MsgTypeString("bs2_out_led:TMMI_MCR_IS_VISIBLE", value=bs2_out_led_visibility_expected)
        validate_pirani_gauge_xxx_visibility = MsgTypeString("pirani_gauge_xxx:TMMI_MCR_IS_VISIBLE", value=pirani_gauge_xxx_visibility_expected)
        validate_pirani_gauge_mbar_visibility = MsgTypeString("pirani_gauge_mbar:TMMI_MCR_IS_VISIBLE", value=pirani_gauge_mbar_visibility_expected)
        validate_d1_gopt_visibility = MsgTypeString("d1_gopt:TMMI_MCR_IS_VISIBLE", value=d1_gopt_visibility_expected)
        validate_d1_gobpm_visibility = MsgTypeString("d1_gobpm:TMMI_MCR_IS_VISIBLE", value=d1_gobpm_visibility_expected)
        validate_d1_gobpm_led_visibility = MsgTypeString("d1_gobpm_led:TMMI_MCR_IS_VISIBLE", value=d1_gobpm_led_visibility_expected)
        validate_d1_gobs_led_visibility = MsgTypeString("d1_gobs_led:TMMI_MCR_IS_VISIBLE", value=d1_gobs_led_visibility_expected)
        validate_d1_gopt_led_visibility = MsgTypeString("d1_gopt_led:TMMI_MCR_IS_VISIBLE", value=d1_gopt_led_visibility_expected)
        validate_BPM3_out_btn_visibility = MsgTypeString("BPM3_out_btn:TMMI_MCR_IS_VISIBLE", value=BPM3_out_btn_visibility_expected)
        validate_BPM3_in_btn_visibility = MsgTypeString("BPM3_in_btn:TMMI_MCR_IS_VISIBLE", value=BPM3_in_btn_visibility_expected)
        validate_BPM3_in_led_visibility = MsgTypeString("BPM3_in_led:TMMI_MCR_IS_VISIBLE", value=BPM3_in_led_visibility_expected)
        validate_BPM3_out_led_visibility = MsgTypeString("BPM3_out_led:TMMI_MCR_IS_VISIBLE", value=BPM3_out_led_visibility_expected)
        validate_is_moving_txt_visibility = MsgTypeString("is_moving_txt:TMMI_MCR_IS_VISIBLE", value=is_moving_txt_visibility_expected)
        validate_pirani_Gauge_foreground_color = MsgTypeString("pirani_Gauge:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=pirani_Gauge_foreground_color_expected)
        validate_bpm3_out_visibility = MsgTypeString("bpm3_out:TMMI_MCR_IS_VISIBLE", value=bpm3_out_visibility_expected)
        validate_pirani_gauge_out_of_range_txt_visibility = MsgTypeString("pirani_gauge_out_of_range_txt:TMMI_MCR_IS_VISIBLE", value=pirani_gauge_out_of_range_txt_visibility_expected)
        validate_cyclone_gif_visibility = MsgTypeString("cyclone_gif:TMMI_MCR_IS_VISIBLE", value=cyclone_gif_visibility_expected)
        validate_bts1_layout_btn_visibility = MsgTypeString("bts1_layout_btn:TMMI_MCR_IS_VISIBLE", value=bts1_layout_btn_visibility_expected)
        validate_c2_61_fdbk_visibility = MsgTypeString("c2_61_fdbk:TMMI_MCR_IS_VISIBLE", value=c2_61_fdbk_visibility_expected)
        validate_c2_61_fdbk_value = MsgTypeNumeric("c2_61_fdbk:TMMI_MCR_OBJECT_GET_VALUE", value=c2_61_fdbk_value_expected)
        validate_c2_fdbk_visibility = MsgTypeString("c2_fdbk:TMMI_MCR_IS_VISIBLE", value=c2_fdbk_visibility_expected)
        validate_c2_fdbk_value = MsgTypeNumeric("c2_fdbk:TMMI_MCR_OBJECT_GET_VALUE", value=c2_fdbk_value_expected)
        validate_d1_golastpos_led_visibility = MsgTypeString("d1_golastpos_led:TMMI_MCR_IS_VISIBLE", value=d1_golastpos_led_visibility_expected)
        validate_step_txt_value = MsgTypeNumeric("step_txt:TMMI_MCR_OBJECT_GET_VALUE", value=step_txt_value_expected)
        validate_safety_interlocks_btn_foreground_color = MsgTypeString("safety_interlocks_btn:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=safety_interlocks_btn_foreground_color_expected)
        validate_B1_waterflow_visibility = MsgTypeString("B1_waterflow:TMMI_MCR_IS_VISIBLE", value=B1_waterflow_visibility_expected)
        validate_B2_waterflow_visibility = MsgTypeString("B2_waterflow:TMMI_MCR_IS_VISIBLE", value=B2_waterflow_visibility_expected)
        validate_B4_waterflow_visibility = MsgTypeString("B4_waterflow:TMMI_MCR_IS_VISIBLE", value=B4_waterflow_visibility_expected)
        validate_B3_waterflow_visibility = MsgTypeString("B3_waterflow:TMMI_MCR_IS_VISIBLE", value=B3_waterflow_visibility_expected)
        validate_bs2_61_fdbk_visibility = MsgTypeString("bs2_61_fdbk:TMMI_MCR_IS_VISIBLE", value=bs2_61_fdbk_visibility_expected)
        validate_bs2_61_fdbk_value = MsgTypeNumeric("bs2_61_fdbk:TMMI_MCR_OBJECT_GET_VALUE", value=bs2_61_fdbk_value_expected)
        validate_bs2_fdbk_value = MsgTypeNumeric("bs2_fdbk:TMMI_MCR_OBJECT_GET_VALUE", value=bs2_fdbk_value_expected)
        validate_bs2_fdbk_visibility = MsgTypeString("bs2_fdbk:TMMI_MCR_IS_VISIBLE", value=bs2_fdbk_visibility_expected)
        validate_d1_gohome_visibility = MsgTypeString("d1_gohome:TMMI_MCR_IS_VISIBLE", value=d1_gohome_visibility_expected)
        validate_title_btn_visibility = MsgTypeString("title_btn:TMMI_MCR_IS_VISIBLE", value=title_btn_visibility_expected)
        info_exchange = [
                        InformationSet("get bs2_out_btn visibility", "thriver", "mcrhci", get_bs2_out_btn_visibility),
                        InformationSet("validate bs2_out_btn visibility = " + str(bs2_out_btn_visibility_expected), "mcrhci", "hcitracer", validate_bs2_out_btn_visibility),
                        InformationSet("set mcr_rtieecubtcu_bcm1_lowdata_visibility = "+ str(mcr_rtieecubtcu_bcm1_lowdata_visibility_init_1), "thriver", "mcrhci", set_mcr_rtieecubtcu_bcm1_lowdata_visibility_1),
                        InformationSet("get bs1_61_fdbk visibility", "thriver", "mcrhci", get_bs1_61_fdbk_visibility),
                        InformationSet("validate bs1_61_fdbk visibility = " + str(bs1_61_fdbk_visibility_expected), "mcrhci", "hcitracer", validate_bs1_61_fdbk_visibility),
                        InformationSet("set mcr_ecubtcu_bs1_cfeedback = "+ str(mcr_ecubtcu_bs1_cfeedback_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bs1_cfeedback_1),
                        InformationSet("get bs1_61_fdbk value", "thriver", "mcrhci", get_bs1_61_fdbk_value),
                        InformationSet("validate bs1_61_fdbk value = " + str(bs1_61_fdbk_value_expected), "mcrhci", "hcitracer", validate_bs1_61_fdbk_value),
                        InformationSet("set mcr_ecubtcu_bs1_cfeedback = "+ str(mcr_ecubtcu_bs1_cfeedback_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bs1_cfeedback_2),
                        InformationSet("get bs1_fdbk value", "thriver", "mcrhci", get_bs1_fdbk_value),
                        InformationSet("validate bs1_fdbk value = " + str(bs1_fdbk_value_expected), "mcrhci", "hcitracer", validate_bs1_fdbk_value),
                        InformationSet("set mcr_rtieecubtcu_bcm1_highdata_visibility = "+ str(mcr_rtieecubtcu_bcm1_highdata_visibility_init_1), "thriver", "mcrhci", set_mcr_rtieecubtcu_bcm1_highdata_visibility_1),
                        InformationSet("get bs1_fdbk visibility", "thriver", "mcrhci", get_bs1_fdbk_visibility),
                        InformationSet("validate bs1_fdbk visibility = " + str(bs1_fdbk_visibility_expected), "mcrhci", "hcitracer", validate_bs1_fdbk_visibility),
                        InformationSet("set d1_golastpos_cmdenable = "+ str(d1_golastpos_cmdenable_init_1), "thriver", "mcrhci", set_d1_golastpos_cmdenable_1),
                        InformationSet("get d1_golastpos_disable visibility", "thriver", "mcrhci", get_d1_golastpos_disable_visibility),
                        InformationSet("validate d1_golastpos_disable visibility = " + str(d1_golastpos_disable_visibility_expected), "mcrhci", "hcitracer", validate_d1_golastpos_disable_visibility),
                        InformationSet("set d1_gopt_cmdenable = "+ str(d1_gopt_cmdenable_init_1), "thriver", "mcrhci", set_d1_gopt_cmdenable_1),
                        InformationSet("get d1_gopt_disable visibility", "thriver", "mcrhci", get_d1_gopt_disable_visibility),
                        InformationSet("validate d1_gopt_disable visibility = " + str(d1_gopt_disable_visibility_expected), "mcrhci", "hcitracer", validate_d1_gopt_disable_visibility),
                        InformationSet("set d1_gobs_cmdenable = "+ str(d1_gobs_cmdenable_init_1), "thriver", "mcrhci", set_d1_gobs_cmdenable_1),
                        InformationSet("get d1_gobs_disable visibility", "thriver", "mcrhci", get_d1_gobs_disable_visibility),
                        InformationSet("validate d1_gobs_disable visibility = " + str(d1_gobs_disable_visibility_expected), "mcrhci", "hcitracer", validate_d1_gobs_disable_visibility),
                        InformationSet("set d1_gobpm_cmdenable = "+ str(d1_gobpm_cmdenable_init_1), "thriver", "mcrhci", set_d1_gobpm_cmdenable_1),
                        InformationSet("get d1_gobpm_disable visibility", "thriver", "mcrhci", get_d1_gobpm_disable_visibility),
                        InformationSet("validate d1_gobpm_disable visibility = " + str(d1_gobpm_disable_visibility_expected), "mcrhci", "hcitracer", validate_d1_gobpm_disable_visibility),
                        InformationSet("set d1_gohome_cmdenable = "+ str(d1_gohome_cmdenable_init_1), "thriver", "mcrhci", set_d1_gohome_cmdenable_1),
                        InformationSet("get d1_gohome_disable visibility", "thriver", "mcrhci", get_d1_gohome_disable_visibility),
                        InformationSet("validate d1_gohome_disable visibility = " + str(d1_gohome_disable_visibility_expected), "mcrhci", "hcitracer", validate_d1_gohome_disable_visibility),
                        InformationSet("get d1_golastpos visibility", "thriver", "mcrhci", get_d1_golastpos_visibility),
                        InformationSet("validate d1_golastpos visibility = " + str(d1_golastpos_visibility_expected), "mcrhci", "hcitracer", validate_d1_golastpos_visibility),
                        InformationSet("get d1_gobs visibility", "thriver", "mcrhci", get_d1_gobs_visibility),
                        InformationSet("validate d1_gobs visibility = " + str(d1_gobs_visibility_expected), "mcrhci", "hcitracer", validate_d1_gobs_visibility),
                        InformationSet("set mcr_ecubtcu_bpm3_instatus = "+ str(mcr_ecubtcu_bpm3_instatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpm3_instatus_1),
                        InformationSet("get bpm3_in visibility", "thriver", "mcrhci", get_bpm3_in_visibility),
                        InformationSet("validate bpm3_in visibility = " + str(bpm3_in_visibility_expected), "mcrhci", "hcitracer", validate_bpm3_in_visibility),
                        InformationSet("get b1 visibility", "thriver", "mcrhci", get_b1_visibility),
                        InformationSet("validate b1 visibility = " + str(b1_visibility_expected), "mcrhci", "hcitracer", validate_b1_visibility),
                        InformationSet("get q1 visibility", "thriver", "mcrhci", get_q1_visibility),
                        InformationSet("validate q1 visibility = " + str(q1_visibility_expected), "mcrhci", "hcitracer", validate_q1_visibility),
                        InformationSet("get q11 visibility", "thriver", "mcrhci", get_q11_visibility),
                        InformationSet("validate q11 visibility = " + str(q11_visibility_expected), "mcrhci", "hcitracer", validate_q11_visibility),
                        InformationSet("get q10 visibility", "thriver", "mcrhci", get_q10_visibility),
                        InformationSet("validate q10 visibility = " + str(q10_visibility_expected), "mcrhci", "hcitracer", validate_q10_visibility),
                        InformationSet("get q2 visibility", "thriver", "mcrhci", get_q2_visibility),
                        InformationSet("validate q2 visibility = " + str(q2_visibility_expected), "mcrhci", "hcitracer", validate_q2_visibility),
                        InformationSet("get b2 visibility", "thriver", "mcrhci", get_b2_visibility),
                        InformationSet("validate b2 visibility = " + str(b2_visibility_expected), "mcrhci", "hcitracer", validate_b2_visibility),
                        InformationSet("get q12 visibility", "thriver", "mcrhci", get_q12_visibility),
                        InformationSet("validate q12 visibility = " + str(q12_visibility_expected), "mcrhci", "hcitracer", validate_q12_visibility),
                        InformationSet("get q20 visibility", "thriver", "mcrhci", get_q20_visibility),
                        InformationSet("validate q20 visibility = " + str(q20_visibility_expected), "mcrhci", "hcitracer", validate_q20_visibility),
                        InformationSet("get q14 visibility", "thriver", "mcrhci", get_q14_visibility),
                        InformationSet("validate q14 visibility = " + str(q14_visibility_expected), "mcrhci", "hcitracer", validate_q14_visibility),
                        InformationSet("get q13 visibility", "thriver", "mcrhci", get_q13_visibility),
                        InformationSet("validate q13 visibility = " + str(q13_visibility_expected), "mcrhci", "hcitracer", validate_q13_visibility),
                        InformationSet("get q15 visibility", "thriver", "mcrhci", get_q15_visibility),
                        InformationSet("validate q15 visibility = " + str(q15_visibility_expected), "mcrhci", "hcitracer", validate_q15_visibility),
                        InformationSet("get b3 visibility", "thriver", "mcrhci", get_b3_visibility),
                        InformationSet("validate b3 visibility = " + str(b3_visibility_expected), "mcrhci", "hcitracer", validate_b3_visibility),
                        InformationSet("get b4 visibility", "thriver", "mcrhci", get_b4_visibility),
                        InformationSet("validate b4 visibility = " + str(b4_visibility_expected), "mcrhci", "hcitracer", validate_b4_visibility),
                        InformationSet("get q21 visibility", "thriver", "mcrhci", get_q21_visibility),
                        InformationSet("validate q21 visibility = " + str(q21_visibility_expected), "mcrhci", "hcitracer", validate_q21_visibility),
                        InformationSet("get q22 visibility", "thriver", "mcrhci", get_q22_visibility),
                        InformationSet("validate q22 visibility = " + str(q22_visibility_expected), "mcrhci", "hcitracer", validate_q22_visibility),
                        InformationSet("get q9 visibility", "thriver", "mcrhci", get_q9_visibility),
                        InformationSet("validate q9 visibility = " + str(q9_visibility_expected), "mcrhci", "hcitracer", validate_q9_visibility),
                        InformationSet("get degrader visibility", "thriver", "mcrhci", get_degrader_visibility),
                        InformationSet("validate degrader visibility = " + str(degrader_visibility_expected), "mcrhci", "hcitracer", validate_degrader_visibility),
                        InformationSet("get T6 visibility", "thriver", "mcrhci", get_T6_visibility),
                        InformationSet("validate T6 visibility = " + str(T6_visibility_expected), "mcrhci", "hcitracer", validate_T6_visibility),
                        InformationSet("get T7 visibility", "thriver", "mcrhci", get_T7_visibility),
                        InformationSet("validate T7 visibility = " + str(T7_visibility_expected), "mcrhci", "hcitracer", validate_T7_visibility),
                        InformationSet("get T2 visibility", "thriver", "mcrhci", get_T2_visibility),
                        InformationSet("validate T2 visibility = " + str(T2_visibility_expected), "mcrhci", "hcitracer", validate_T2_visibility),
                        InformationSet("get sl1 visibility", "thriver", "mcrhci", get_sl1_visibility),
                        InformationSet("validate sl1 visibility = " + str(sl1_visibility_expected), "mcrhci", "hcitracer", validate_sl1_visibility),
                        InformationSet("get sl2 visibility", "thriver", "mcrhci", get_sl2_visibility),
                        InformationSet("validate sl2 visibility = " + str(sl2_visibility_expected), "mcrhci", "hcitracer", validate_sl2_visibility),
                        InformationSet("set mcr_ecubtcu_sstech_ps_status = "+ str(mcr_ecubtcu_sstech_ps_status_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_sstech_ps_status_1),
                        InformationSet("get ext_int_txt foreground_color", "thriver", "mcrhci", get_ext_int_txt_foreground_color),
                        InformationSet("validate ext_int_txt foreground_color = " + str(ext_int_txt_foreground_color_expected), "mcrhci", "hcitracer", validate_ext_int_txt_foreground_color),
                        InformationSet("set mcr_ecubtcu_sstech_ps_status = "+ str(mcr_ecubtcu_sstech_ps_status_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_sstech_ps_status_2),
                        InformationSet("get ext_int_chk subobject_name", "thriver", "mcrhci", get_ext_int_chk_subobject_name),
                        InformationSet("validate ext_int_chk subobject_name = " + str(ext_int_chk_subobject_name_expected), "mcrhci", "hcitracer", validate_ext_int_chk_subobject_name),
                        InformationSet("get bs2_in_btn visibility", "thriver", "mcrhci", get_bs2_in_btn_visibility),
                        InformationSet("validate bs2_in_btn visibility = " + str(bs2_in_btn_visibility_expected), "mcrhci", "hcitracer", validate_bs2_in_btn_visibility),
                        InformationSet("set mcr_ecubtcu_bs2_instatus = "+ str(mcr_ecubtcu_bs2_instatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bs2_instatus_1),
                        InformationSet("get bs2_in_led visibility", "thriver", "mcrhci", get_bs2_in_led_visibility),
                        InformationSet("validate bs2_in_led visibility = " + str(bs2_in_led_visibility_expected), "mcrhci", "hcitracer", validate_bs2_in_led_visibility),
                        InformationSet("set mcr_ecubtcu_bs2_outstatus = "+ str(mcr_ecubtcu_bs2_outstatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bs2_outstatus_1),
                        InformationSet("get bs2_out_led visibility", "thriver", "mcrhci", get_bs2_out_led_visibility),
                        InformationSet("validate bs2_out_led visibility = " + str(bs2_out_led_visibility_expected), "mcrhci", "hcitracer", validate_bs2_out_led_visibility),
                        InformationSet("set mcr_ecubtcu_piraniess_mbarvacuum = "+ str(mcr_ecubtcu_piraniess_mbarvacuum_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_piraniess_mbarvacuum_1),
                        InformationSet("get pirani_gauge_xxx visibility", "thriver", "mcrhci", get_pirani_gauge_xxx_visibility),
                        InformationSet("validate pirani_gauge_xxx visibility = " + str(pirani_gauge_xxx_visibility_expected), "mcrhci", "hcitracer", validate_pirani_gauge_xxx_visibility),
                        InformationSet("set mcr_ecubtcu_piraniess_mbarvacuum = "+ str(mcr_ecubtcu_piraniess_mbarvacuum_init_3), "thriver", "mcrhci", set_mcr_ecubtcu_piraniess_mbarvacuum_3),
                        InformationSet("get pirani_gauge_mbar visibility", "thriver", "mcrhci", get_pirani_gauge_mbar_visibility),
                        InformationSet("validate pirani_gauge_mbar visibility = " + str(pirani_gauge_mbar_visibility_expected), "mcrhci", "hcitracer", validate_pirani_gauge_mbar_visibility),
                        InformationSet("get d1_gopt visibility", "thriver", "mcrhci", get_d1_gopt_visibility),
                        InformationSet("validate d1_gopt visibility = " + str(d1_gopt_visibility_expected), "mcrhci", "hcitracer", validate_d1_gopt_visibility),
                        InformationSet("get d1_gobpm visibility", "thriver", "mcrhci", get_d1_gobpm_visibility),
                        InformationSet("validate d1_gobpm visibility = " + str(d1_gobpm_visibility_expected), "mcrhci", "hcitracer", validate_d1_gobpm_visibility),
                        InformationSet("set mcr_ecubtcu_degrader_status = "+ str(mcr_ecubtcu_degrader_status_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_degrader_status_1),
                        InformationSet("get d1_gobpm_led visibility", "thriver", "mcrhci", get_d1_gobpm_led_visibility),
                        InformationSet("validate d1_gobpm_led visibility = " + str(d1_gobpm_led_visibility_expected), "mcrhci", "hcitracer", validate_d1_gobpm_led_visibility),
                        InformationSet("set mcr_ecubtcu_degrader_status = "+ str(mcr_ecubtcu_degrader_status_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_degrader_status_2),
                        InformationSet("get d1_gobs_led visibility", "thriver", "mcrhci", get_d1_gobs_led_visibility),
                        # Bug - cannot get the visibility of d1_gobs_led
                        # InformationSet("validate d1_gobs_led visibility = " + str(d1_gobs_led_visibility_expected), "mcrhci", "hcitracer", validate_d1_gobs_led_visibility),
                        InformationSet("set mcr_ecubtcu_degrader_status = "+ str(mcr_ecubtcu_degrader_status_init_3), "thriver", "mcrhci", set_mcr_ecubtcu_degrader_status_3),
                        InformationSet("get d1_gopt_led visibility", "thriver", "mcrhci", get_d1_gopt_led_visibility),
                        InformationSet("validate d1_gopt_led visibility = " + str(d1_gopt_led_visibility_expected), "mcrhci", "hcitracer", validate_d1_gopt_led_visibility),
                        InformationSet("get BPM3_out_btn visibility", "thriver", "mcrhci", get_BPM3_out_btn_visibility),
                        InformationSet("validate BPM3_out_btn visibility = " + str(BPM3_out_btn_visibility_expected), "mcrhci", "hcitracer", validate_BPM3_out_btn_visibility),
                        InformationSet("get BPM3_in_btn visibility", "thriver", "mcrhci", get_BPM3_in_btn_visibility),
                        InformationSet("validate BPM3_in_btn visibility = " + str(BPM3_in_btn_visibility_expected), "mcrhci", "hcitracer", validate_BPM3_in_btn_visibility),
                        InformationSet("set mcr_ecubtcu_bpm3_instatus = "+ str(mcr_ecubtcu_bpm3_instatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpm3_instatus_2),
                        InformationSet("get BPM3_in_led visibility", "thriver", "mcrhci", get_BPM3_in_led_visibility),
                        InformationSet("validate BPM3_in_led visibility = " + str(BPM3_in_led_visibility_expected), "mcrhci", "hcitracer", validate_BPM3_in_led_visibility),
                        InformationSet("set mcr_ecubtcu_bpm3_outstatus = "+ str(mcr_ecubtcu_bpm3_outstatus_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bpm3_outstatus_1),
                        InformationSet("get BPM3_out_led visibility", "thriver", "mcrhci", get_BPM3_out_led_visibility),
                        InformationSet("validate BPM3_out_led visibility = " + str(BPM3_out_led_visibility_expected), "mcrhci", "hcitracer", validate_BPM3_out_led_visibility),
                        InformationSet("set mcr_ecubtcu_degrader_status = "+ str(mcr_ecubtcu_degrader_status_init_4), "thriver", "mcrhci", set_mcr_ecubtcu_degrader_status_4),
                        InformationSet("get is_moving_txt visibility", "thriver", "mcrhci", get_is_moving_txt_visibility),
                        InformationSet("validate is_moving_txt visibility = " + str(is_moving_txt_visibility_expected), "mcrhci", "hcitracer", validate_is_moving_txt_visibility),
                        InformationSet("set mcr_acu_vacuumess_status = "+ str(mcr_acu_vacuumess_status_init_1), "thriver", "mcrhci", set_mcr_acu_vacuumess_status_1),
                        InformationSet("get pirani_Gauge foreground_color", "thriver", "mcrhci", get_pirani_Gauge_foreground_color),
                        InformationSet("validate pirani_Gauge foreground_color = " + str(pirani_Gauge_foreground_color_expected), "mcrhci", "hcitracer", validate_pirani_Gauge_foreground_color),
                        InformationSet("set mcr_ecubtcu_bpm3_outstatus = "+ str(mcr_ecubtcu_bpm3_outstatus_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bpm3_outstatus_2),
                        InformationSet("get bpm3_out visibility", "thriver", "mcrhci", get_bpm3_out_visibility),
                        InformationSet("validate bpm3_out visibility = " + str(bpm3_out_visibility_expected), "mcrhci", "hcitracer", validate_bpm3_out_visibility),
                        InformationSet("set mcr_ecubtcu_piraniess_mbarvacuum = "+ str(mcr_ecubtcu_piraniess_mbarvacuum_init_4), "thriver", "mcrhci", set_mcr_ecubtcu_piraniess_mbarvacuum_4),
                        InformationSet("get pirani_gauge_out_of_range_txt visibility", "thriver", "mcrhci", get_pirani_gauge_out_of_range_txt_visibility),
                        InformationSet("validate pirani_gauge_out_of_range_txt visibility = " + str(pirani_gauge_out_of_range_txt_visibility_expected), "mcrhci", "hcitracer", validate_pirani_gauge_out_of_range_txt_visibility),
                        InformationSet("get cyclone_gif visibility", "thriver", "mcrhci", get_cyclone_gif_visibility),
                        InformationSet("validate cyclone_gif visibility = " + str(cyclone_gif_visibility_expected), "mcrhci", "hcitracer", validate_cyclone_gif_visibility),
                        InformationSet("get bts1_layout_btn visibility", "thriver", "mcrhci", get_bts1_layout_btn_visibility),
                        InformationSet("validate bts1_layout_btn visibility = " + str(bts1_layout_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts1_layout_btn_visibility),
                        InformationSet("set mcr_rtieecubtcu_bcm1_lowdata_visibility = "+ str(mcr_rtieecubtcu_bcm1_lowdata_visibility_init_2), "thriver", "mcrhci", set_mcr_rtieecubtcu_bcm1_lowdata_visibility_2),
                        InformationSet("get c2_61_fdbk visibility", "thriver", "mcrhci", get_c2_61_fdbk_visibility),
                        InformationSet("validate c2_61_fdbk visibility = " + str(c2_61_fdbk_visibility_expected), "mcrhci", "hcitracer", validate_c2_61_fdbk_visibility),
                        InformationSet("set mcr_ecubtcu_c2_cfeedback = "+ str(mcr_ecubtcu_c2_cfeedback_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_c2_cfeedback_1),
                        InformationSet("get c2_61_fdbk value", "thriver", "mcrhci", get_c2_61_fdbk_value),
                        InformationSet("validate c2_61_fdbk value = " + str(c2_61_fdbk_value_expected), "mcrhci", "hcitracer", validate_c2_61_fdbk_value),
                        InformationSet("set mcr_rtieecubtcu_bcm1_highdata_visibility = "+ str(mcr_rtieecubtcu_bcm1_highdata_visibility_init_2), "thriver", "mcrhci", set_mcr_rtieecubtcu_bcm1_highdata_visibility_2),
                        InformationSet("get c2_fdbk visibility", "thriver", "mcrhci", get_c2_fdbk_visibility),
                        InformationSet("validate c2_fdbk visibility = " + str(c2_fdbk_visibility_expected), "mcrhci", "hcitracer", validate_c2_fdbk_visibility),
                        InformationSet("set mcr_ecubtcu_c2_cfeedback = "+ str(mcr_ecubtcu_c2_cfeedback_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_c2_cfeedback_2),
                        InformationSet("get c2_fdbk value", "thriver", "mcrhci", get_c2_fdbk_value),
                        InformationSet("validate c2_fdbk value = " + str(c2_fdbk_value_expected), "mcrhci", "hcitracer", validate_c2_fdbk_value),
                        InformationSet("set mcr_ecubtcu_degrader_status = "+ str(mcr_ecubtcu_degrader_status_init_5), "thriver", "mcrhci", set_mcr_ecubtcu_degrader_status_5),
                        InformationSet("get d1_golastpos_led visibility", "thriver", "mcrhci", get_d1_golastpos_led_visibility),
                        # Bug - cannot get the visibility of d1_golastpos_led
                        # InformationSet("validate d1_golastpos_led visibility = " + str(d1_golastpos_led_visibility_expected), "mcrhci", "hcitracer", validate_d1_golastpos_led_visibility),
                        InformationSet("set mcr_ecubtcu_degrader_feedbackstep = "+ str(mcr_ecubtcu_degrader_feedbackstep_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_degrader_feedbackstep_1),
                        InformationSet("get step_txt value", "thriver", "mcrhci", get_step_txt_value),
                        InformationSet("validate step_txt value = " + str(step_txt_value_expected), "mcrhci", "hcitracer", validate_step_txt_value),
                        InformationSet("set mcr_scu_safety_ess_bsoutenable = "+ str(mcr_scu_safety_ess_bsoutenable_init_1), "thriver", "mcrhci", set_mcr_scu_safety_ess_bsoutenable_1),
                        InformationSet("get safety_interlocks_btn foreground_color", "thriver", "mcrhci", get_safety_interlocks_btn_foreground_color),
                        InformationSet("validate safety_interlocks_btn foreground_color = " + str(safety_interlocks_btn_foreground_color_expected), "mcrhci", "hcitracer", validate_safety_interlocks_btn_foreground_color),
                        InformationSet("set mcr_acu_b1_waterflow = "+ str(mcr_acu_b1_waterflow_init_1), "thriver", "mcrhci", set_mcr_acu_b1_waterflow_1),
                        InformationSet("get B1_waterflow visibility", "thriver", "mcrhci", get_B1_waterflow_visibility),
                        InformationSet("validate B1_waterflow visibility = " + str(B1_waterflow_visibility_expected), "mcrhci", "hcitracer", validate_B1_waterflow_visibility),
                        InformationSet("set mcr_acu_b2_waterflow = "+ str(mcr_acu_b2_waterflow_init_1), "thriver", "mcrhci", set_mcr_acu_b2_waterflow_1),
                        InformationSet("get B2_waterflow visibility", "thriver", "mcrhci", get_B2_waterflow_visibility),
                        InformationSet("validate B2_waterflow visibility = " + str(B2_waterflow_visibility_expected), "mcrhci", "hcitracer", validate_B2_waterflow_visibility),
                        InformationSet("set mcr_acu_b4_waterflow = "+ str(mcr_acu_b4_waterflow_init_1), "thriver", "mcrhci", set_mcr_acu_b4_waterflow_1),
                        InformationSet("get B4_waterflow visibility", "thriver", "mcrhci", get_B4_waterflow_visibility),
                        InformationSet("validate B4_waterflow visibility = " + str(B4_waterflow_visibility_expected), "mcrhci", "hcitracer", validate_B4_waterflow_visibility),
                        InformationSet("set mcr_acu_b3_waterflow = "+ str(mcr_acu_b3_waterflow_init_1), "thriver", "mcrhci", set_mcr_acu_b3_waterflow_1),
                        InformationSet("get B3_waterflow visibility", "thriver", "mcrhci", get_B3_waterflow_visibility),
                        InformationSet("validate B3_waterflow visibility = " + str(B3_waterflow_visibility_expected), "mcrhci", "hcitracer", validate_B3_waterflow_visibility),
                        InformationSet("set mcr_rtieecubtcu_bcm2_lowdata_visibility = "+ str(mcr_rtieecubtcu_bcm2_lowdata_visibility_init_1), "thriver", "mcrhci", set_mcr_rtieecubtcu_bcm2_lowdata_visibility_1),
                        InformationSet("get bs2_61_fdbk visibility", "thriver", "mcrhci", get_bs2_61_fdbk_visibility),
                        InformationSet("validate bs2_61_fdbk visibility = " + str(bs2_61_fdbk_visibility_expected), "mcrhci", "hcitracer", validate_bs2_61_fdbk_visibility),
                        InformationSet("set mcr_ecubtcu_bs2_cfeedback = "+ str(mcr_ecubtcu_bs2_cfeedback_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_bs2_cfeedback_1),
                        InformationSet("get bs2_61_fdbk value", "thriver", "mcrhci", get_bs2_61_fdbk_value),
                        InformationSet("validate bs2_61_fdbk value = " + str(bs2_61_fdbk_value_expected), "mcrhci", "hcitracer", validate_bs2_61_fdbk_value),
                        InformationSet("set mcr_ecubtcu_bs2_cfeedback = "+ str(mcr_ecubtcu_bs2_cfeedback_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_bs2_cfeedback_2),
                        InformationSet("get bs2_fdbk value", "thriver", "mcrhci", get_bs2_fdbk_value),
                        InformationSet("validate bs2_fdbk value = " + str(bs2_fdbk_value_expected), "mcrhci", "hcitracer", validate_bs2_fdbk_value),
                        InformationSet("set mcr_rtieecubtcu_bcm2_highdata_visibility = "+ str(mcr_rtieecubtcu_bcm2_highdata_visibility_init_1), "thriver", "mcrhci", set_mcr_rtieecubtcu_bcm2_highdata_visibility_1),
                        InformationSet("get bs2_fdbk visibility", "thriver", "mcrhci", get_bs2_fdbk_visibility),
                        InformationSet("validate bs2_fdbk visibility = " + str(bs2_fdbk_visibility_expected), "mcrhci", "hcitracer", validate_bs2_fdbk_visibility),
                        InformationSet("get d1_gohome visibility", "thriver", "mcrhci", get_d1_gohome_visibility),
                        InformationSet("validate d1_gohome visibility = " + str(d1_gohome_visibility_expected), "mcrhci", "hcitracer", validate_d1_gohome_visibility),
                        InformationSet("get title_btn visibility", "thriver", "mcrhci", get_title_btn_visibility),
                        InformationSet("validate title_btn visibility = " + str(title_btn_visibility_expected), "mcrhci", "hcitracer", validate_title_btn_visibility),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []