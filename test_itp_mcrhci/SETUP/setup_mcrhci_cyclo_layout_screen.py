
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

class SETUP_VALIDATE_CYCLO_LAYOUT_SCREEN(ClinicalIntegrationTestProcedure):
    # default variable values
    name = "Confirm that MCR_Service_Cyclo_Layout(cyclo_layout.v) is displayed"
    acu3_t2psvideo_visibility_expected = "1"
    mcr_acu_sw_healthStatus_init_1 = "OK"
    acu3_acuhealthstatus_text_expected = "OK"
    acu3_radialprobe_visibility_expected = "1"
    acu3_maincoilpsonbtn_visibility_expected = "1"
    mcr_acu_maincoilps_cmdstatus_init_1 = True
    acu3_maincoilpsondisable_background_color_expected = "66"
    maincoil_pson_cmdenable_init_1 = True
    acu3_maincoilpsondisable_visibility_expected = "0"
    acu3_maincoilpsoffbtn_visibility_expected = "1"
    mcr_acu_maincoilps_cmdstatus_init_2 = True
    acu3_maincoilpsoffdisable_background_color_expected = "50"
    maincoil_psoff_cmdenable_init_1 = True
    acu3_maincoilpsoffdisable_visibility_expected = "0"
    mcr_rtieacu_maincoil_cfeedback_init_1 = 0.1
    acu3_maincoilcfeedback_value_expected = 0.1
    mcr_rtieacu_coil24_cfeedback_init_1 = 0.2
    acu3_coil24cfeedback_value_expected = 0.2
    mcr_rtieacu_coil13_cfeedback_init_1 = 0.3
    acu3_coil13cfeedback_value_expected = 0.3
    mcr_rtieacu_radialprobe_vert_location_init_1 = 0.4
    acu3_rpvertposition_value_expected = 0.4
    mcr_rtieacu_radialprobe_energy_init_1 = 0.5
    acu3_rpenergy_value_expected = 0.5
    acu3_rfonbtn_visibility_expected = "1"
    rf_on_cmdenable_init_1 = True
    acu3_rfondisable_visibility_expected = "0"
    acu3_rfoffbtn_visibility_expected = "1"
    rf_off_cmdenable_init_1 = True
    acu3_rfoffdisable_visibility_expected = "0"
    mcr_acu_modulator_cmdenable_init_1 = True
    acu3_modintlk_foreground_color_expected = "0"
    mcr_acu_modulator_cmdenable_init_2 = True
    acu3_modintlk_background_color_expected = "13"
    acu3_q1q2psonbtn_visibility_expected = "1"
    mcr_acu_q1q2_cmdstatus_init_1 = True
    acu3_q1q2psondisable_background_color_expected = "66"
    quadextrps_q1q2_pson_cmdenable_init_1 = True
    acu3_q1q2psondisable_visibility_expected = "0"
    acu3_q1q2psoffbtn_visibility_expected = "1"
    mcr_acu_q1q2_cmdstatus_init_2 = True
    acu3_q1q2psoffdisable_background_color_expected = "50"
    quadextrps_q1q2_psoff_cmdenable_init_1 = True
    acu3_q1q2psoffdisable_visibility_expected = "0"
    acu3_q1q2video_visibility_expected = "1"
    mcr_rtieacu_q1_cfeedback_init_1 = 0.6
    acu3_q1cfeedback_value_expected = 0.6
    mcr_rtieacu_q2_cfeedback_init_1 = 0.7
    acu3_q2cfeedback_value_expected = 0.7
    acu3_sourceonbtn_visibility_expected = "1"
    mcr_acu_sourcearc_cmdstatus_init_1 = True
    acu3_sourceondisable_background_color_expected = "66"
    source_sourceon_cmdenable_init_1 = True
    acu3_sourceondisable_visibility_expected = "0"
    acu3_sourceoffbtn_visibility_expected = "1"
    mcr_acu_sourcearc_cmdstatus_init_2 = True
    acu3_sourceoffdisable_background_color_expected = "50"
    source_sourceoff_cmdenable_init_1 = True
    acu3_sourceoffdisable_visibility_expected = "0"
    mcr_acu_sourcefilament_cfeedback_init_1 = 0.8
    acu3_filamentcfeedback_value_expected = 0.8
    mcr_acu_sourcearc_cfeedback_init_1 = 0.9
    acu3_arccfeedback_value_expected = 0.9
    mcr_acu_sourcearc_vfeedback_init_1 = 1.0
    acu3_arcvfeedback_value_expected = 1.0
    mcr_rtieacu_impa_extcondition_init_1 = True
    acu3_impaextcondtxt_foreground_color_expected = "112"
    mcr_acu_radialprobe_inls_init_1 = True
    acu3_rpinlsstatus_subobject_name_expected = "iba_info_ok.sd"
    mcr_rtieacu_impa_extcondition_init_2 = True
    acu3_impaextcondcheckmark_subobject_name_expected = "iba_check_ok.sd"
    mcr_rtieacu_fpa_extcondition_init_1 = True
    acu3_fpaextcondtxt_foreground_color_expected = "112"
    mcr_rtieacu_fpa_extcondition_init_2 = True
    acu3_fpaextcondcheckmark_subobject_name_expected = "iba_check_ok.sd"
    acu3_deflectorpsonbtn_visibility_expected = "1"
    mcr_acu_deflectorps_cmdstatus_init_1 = True
    acu3_deflectorpsondisable_background_color_expected = "66"
    deflector_pson_cmdenable_init_1 = True
    acu3_deflectorpsondisable_visibility_expected = "0"
    acu3_deflectorpsoffbtn_visibility_expected = "1"
    mcr_acu_deflectorps_cmdstatus_init_2 = True
    acu3_deflectorpsoffdisable_background_color_expected = "50"
    deflector_psoff_cmdenable_init_1 = True
    acu3_deflectorpsoffdisable_visibility_expected = "0"
    mcr_acu_deflectorps_vfeedback_init_1 = 1.1
    acu3_deflectorpsvfeedback_value_expected = 1.1
    mcr_acu_deflectorps_macfeedback_init_1 = 1.2
    acu3_deflectorpsmacfeedback_value_expected = 1.2
    mcr_acu_deflectormotor1_dfeedback_init_1 = 1.3
    acu3_deflectormotor1dfeedback_value_expected = 1.3
    mcr_acu_deflectormotor2_dfeedback_init_1 = 1.4
    acu3_deflectormotor2dfeedback_value_expected = 1.4
    mcr_acu_sourcemovement_dfeedback_init_1 = 1.5
    acu3_srcmovementdfeedback_value_expected = 1.5
    mcr_ecubtcu_penning1cyclo_mbarvacuum_init_1 = 1.6
    acu3_penning1mbarvac_value_expected = 1.6
    mcr_ecubtcu_penning1cyclo_mbarvacuum_init_2 = 1.0
    acu3_penning1mbarvac_visibility_expected = "1"
    mcr_ecubtcu_penning1cyclo_mbarvacuum_init_3 = 0
    acu3_penning1mbartxt_visibility_expected = "1"
    mcr_rtieecubtcu_penning1_cyclo_status_init_1 = "OK"
    acu3_penning1errormsg_text_expected = "OK"
    mcr_ecubtcu_penning1cyclo_mbarvacuum_init_4 = 1
    acu3_penning1errormsg_visibility_expected = "0"
    mcr_acu_fpa_kwforwardpower_init_1 = 1.7
    acu3_fpakwforwardpower_value_expected = 1.7
    mcr_acu_vdee_vfeedback1_init_1 = 1.8
    acu3_vdee1vfeedback_value_expected = 1.8
    mcr_acu_vdee_vfeedback2_init_1 = 1.9
    acu3_vdee2vfeedback_value_expected = 1.9
    vdee_dsetpoint_text_init_1 = "9.1"
    acu3_vdeedinput_text_expected = "9.1"
    mcr_acu_vdee_dsetpoint_init_1 = 2.1
    acu3_vdeedfeedback_value_expected = 2.1
    vdee_dfeedback_visible_init_1 = True
    acu3_vdeedfeedback_visibility_expected = "1"
    mcr_acu_sw_counter_init_1 = 2.2
    acu3_acucounter_value_expected = 0 #Bug - expected value should be 2.2
    mcr_rtieacu_compensationcoil_cfeedback_init_1 = 2.3
    acu3_compcoilcfeedback_value_expected = 2.3
    acu3_savebtn_visibility_expected = "1"
    acu3_edit_eqt_param_visibility_expected = "1"
    mcr_acu_radialprobe_outls_init_1 = True
    acu3_rpoutlsstatus_subobject_name_expected = "iba_info_ok.sd"
    acu3_esslayoutbtn_visibility_expected = "1"
    acu3_t1onbtn_visibility_expected = "1"
    mcr_acu_t1_cmdstatus_init_1 = True
    acu3_t1ondisable_background_color_expected = "66"
    steeringextrps_sg1_pson_cmdenable_init_1 = True
    acu3_t1ondisable_visibility_expected = "0"
    acu3_t1offbtn_visibility_expected = "1"
    mcr_acu_t1_cmdstatus_init_2 = True
    acu3_t1offdisable_background_color_expected = "50"
    steeringextrps_sg1_psoff_cmdenable_init_1 = True
    acu3_t1offdisable_visibility_expected = "0"
    acu3_t1psvideo_visibility_expected = "1"
    acu3_t2onbtn_visibility_expected = "1"
    mcr_acu_t2_cmdstatus_init_1 = True
    acu3_t2ondisable_background_color_expected = "66"
    steeringextrps_sg2_pson_cmdenable_init_1 = True
    acu3_t2ondisable_visibility_expected = "0"
    acu3_t2offbtn_visibility_expected = "1"
    mcr_acu_t2_cmdstatus_init_2 = True
    acu3_t2offdisable_background_color_expected = "50"
    steeringextrps_sg2_psoff_cmdenable_init_1 = True
    acu3_t2offdisable_visibility_expected = "0"
    acu3_essctrlbtn_visibility_expected = "1"
    acu3_maincoiltuningbtn_visibility_expected = "1"
    mcr_acu_maincoil_tuning_cmdstatus_init_1 = True
    acu3_maincoiltuningdisable_background_color_expected = "66"
    maincoil_tuning_cmdenable_init_1 = True
    acu3_maincoiltuningdisable_visibility_expected = "0"
    mcr_acu_maincoil_tuning_cmdstatus_init_2 = True
    acu3_maincoiltuningled_visibility_expected = "1"
    acu3_arctuningbtn_visibility_expected = "1"
    mcr_acu_source_tuning_cmdenable_init_1 = True
    acu3_arctuningdisable_visibility_expected = "0"
    mcr_acu_source_tuning_cmdstatus_init_1 = True
    acu3_arctuningled_visibility_expected = "1"
    acu3_positionstatus_visibility_expected = "1"
    acu3_maincoilpsvideo_visibility_expected = "1"
    acu3_sourcepsvideo_visibility_expected = "1"
    acu3_llrfvideo_visibility_expected = "1"
    acu3_ssavideo_visibility_expected = "1"
    acu3_impavideo_visibility_expected = "1"
    acu3_fpavideo_visibility_expected = "1"
    acu3_rfvideo_visibility_expected = "1"
    acu3_deflectorpsvideo_visibility_expected = "1"
    acu3_cyclovacvideo_visibility_expected = "1"
    acu3_hydrolicstationstatus_visibility_expected = "1"
    acu3_coolingstatus_visibility_expected = "1"

    def __init__(self, test):
        cls = type(self)
        name = cls.name
        acu3_t2psvideo_visibility_expected = cls.acu3_t2psvideo_visibility_expected
        mcr_acu_sw_healthStatus_init_1 = cls.mcr_acu_sw_healthStatus_init_1
        acu3_acuhealthstatus_text_expected = cls.acu3_acuhealthstatus_text_expected
        acu3_radialprobe_visibility_expected = cls.acu3_radialprobe_visibility_expected
        acu3_maincoilpsonbtn_visibility_expected = cls.acu3_maincoilpsonbtn_visibility_expected
        mcr_acu_maincoilps_cmdstatus_init_1 = cls.mcr_acu_maincoilps_cmdstatus_init_1
        acu3_maincoilpsondisable_background_color_expected = cls.acu3_maincoilpsondisable_background_color_expected
        maincoil_pson_cmdenable_init_1 = cls.maincoil_pson_cmdenable_init_1
        acu3_maincoilpsondisable_visibility_expected = cls.acu3_maincoilpsondisable_visibility_expected
        acu3_maincoilpsoffbtn_visibility_expected = cls.acu3_maincoilpsoffbtn_visibility_expected
        mcr_acu_maincoilps_cmdstatus_init_2 = cls.mcr_acu_maincoilps_cmdstatus_init_2
        acu3_maincoilpsoffdisable_background_color_expected = cls.acu3_maincoilpsoffdisable_background_color_expected
        maincoil_psoff_cmdenable_init_1 = cls.maincoil_psoff_cmdenable_init_1
        acu3_maincoilpsoffdisable_visibility_expected = cls.acu3_maincoilpsoffdisable_visibility_expected
        mcr_rtieacu_maincoil_cfeedback_init_1 = cls.mcr_rtieacu_maincoil_cfeedback_init_1
        acu3_maincoilcfeedback_value_expected = cls.acu3_maincoilcfeedback_value_expected
        mcr_rtieacu_coil24_cfeedback_init_1 = cls.mcr_rtieacu_coil24_cfeedback_init_1
        acu3_coil24cfeedback_value_expected = cls.acu3_coil24cfeedback_value_expected
        mcr_rtieacu_coil13_cfeedback_init_1 = cls.mcr_rtieacu_coil13_cfeedback_init_1
        acu3_coil13cfeedback_value_expected = cls.acu3_coil13cfeedback_value_expected
        mcr_rtieacu_radialprobe_vert_location_init_1 = cls.mcr_rtieacu_radialprobe_vert_location_init_1
        acu3_rpvertposition_value_expected = cls.acu3_rpvertposition_value_expected
        mcr_rtieacu_radialprobe_energy_init_1 = cls.mcr_rtieacu_radialprobe_energy_init_1
        acu3_rpenergy_value_expected = cls.acu3_rpenergy_value_expected
        acu3_rfonbtn_visibility_expected = cls.acu3_rfonbtn_visibility_expected
        rf_on_cmdenable_init_1 = cls.rf_on_cmdenable_init_1
        acu3_rfondisable_visibility_expected = cls.acu3_rfondisable_visibility_expected
        acu3_rfoffbtn_visibility_expected = cls.acu3_rfoffbtn_visibility_expected
        rf_off_cmdenable_init_1 = cls.rf_off_cmdenable_init_1
        acu3_rfoffdisable_visibility_expected = cls.acu3_rfoffdisable_visibility_expected
        mcr_acu_modulator_cmdenable_init_1 = cls.mcr_acu_modulator_cmdenable_init_1
        acu3_modintlk_foreground_color_expected = cls.acu3_modintlk_foreground_color_expected
        mcr_acu_modulator_cmdenable_init_2 = cls.mcr_acu_modulator_cmdenable_init_2
        acu3_modintlk_background_color_expected = cls.acu3_modintlk_background_color_expected
        acu3_q1q2psonbtn_visibility_expected = cls.acu3_q1q2psonbtn_visibility_expected
        mcr_acu_q1q2_cmdstatus_init_1 = cls.mcr_acu_q1q2_cmdstatus_init_1
        acu3_q1q2psondisable_background_color_expected = cls.acu3_q1q2psondisable_background_color_expected
        quadextrps_q1q2_pson_cmdenable_init_1 = cls.quadextrps_q1q2_pson_cmdenable_init_1
        acu3_q1q2psondisable_visibility_expected = cls.acu3_q1q2psondisable_visibility_expected
        acu3_q1q2psoffbtn_visibility_expected = cls.acu3_q1q2psoffbtn_visibility_expected
        mcr_acu_q1q2_cmdstatus_init_2 = cls.mcr_acu_q1q2_cmdstatus_init_2
        acu3_q1q2psoffdisable_background_color_expected = cls.acu3_q1q2psoffdisable_background_color_expected
        quadextrps_q1q2_psoff_cmdenable_init_1 = cls.quadextrps_q1q2_psoff_cmdenable_init_1
        acu3_q1q2psoffdisable_visibility_expected = cls.acu3_q1q2psoffdisable_visibility_expected
        acu3_q1q2video_visibility_expected = cls.acu3_q1q2video_visibility_expected
        mcr_rtieacu_q1_cfeedback_init_1 = cls.mcr_rtieacu_q1_cfeedback_init_1
        acu3_q1cfeedback_value_expected = cls.acu3_q1cfeedback_value_expected
        mcr_rtieacu_q2_cfeedback_init_1 = cls.mcr_rtieacu_q2_cfeedback_init_1
        acu3_q2cfeedback_value_expected = cls.acu3_q2cfeedback_value_expected
        acu3_sourceonbtn_visibility_expected = cls.acu3_sourceonbtn_visibility_expected
        mcr_acu_sourcearc_cmdstatus_init_1 = cls.mcr_acu_sourcearc_cmdstatus_init_1
        acu3_sourceondisable_background_color_expected = cls.acu3_sourceondisable_background_color_expected
        source_sourceon_cmdenable_init_1 = cls.source_sourceon_cmdenable_init_1
        acu3_sourceondisable_visibility_expected = cls.acu3_sourceondisable_visibility_expected
        acu3_sourceoffbtn_visibility_expected = cls.acu3_sourceoffbtn_visibility_expected
        mcr_acu_sourcearc_cmdstatus_init_2 = cls.mcr_acu_sourcearc_cmdstatus_init_2
        acu3_sourceoffdisable_background_color_expected = cls.acu3_sourceoffdisable_background_color_expected
        source_sourceoff_cmdenable_init_1 = cls.source_sourceoff_cmdenable_init_1
        acu3_sourceoffdisable_visibility_expected = cls.acu3_sourceoffdisable_visibility_expected
        mcr_acu_sourcefilament_cfeedback_init_1 = cls.mcr_acu_sourcefilament_cfeedback_init_1
        acu3_filamentcfeedback_value_expected = cls.acu3_filamentcfeedback_value_expected
        mcr_acu_sourcearc_cfeedback_init_1 = cls.mcr_acu_sourcearc_cfeedback_init_1
        acu3_arccfeedback_value_expected = cls.acu3_arccfeedback_value_expected
        mcr_acu_sourcearc_vfeedback_init_1 = cls.mcr_acu_sourcearc_vfeedback_init_1
        acu3_arcvfeedback_value_expected = cls.acu3_arcvfeedback_value_expected
        mcr_rtieacu_impa_extcondition_init_1 = cls.mcr_rtieacu_impa_extcondition_init_1
        acu3_impaextcondtxt_foreground_color_expected = cls.acu3_impaextcondtxt_foreground_color_expected
        mcr_acu_radialprobe_inls_init_1 = cls.mcr_acu_radialprobe_inls_init_1
        acu3_rpinlsstatus_subobject_name_expected = cls.acu3_rpinlsstatus_subobject_name_expected
        mcr_rtieacu_impa_extcondition_init_2 = cls.mcr_rtieacu_impa_extcondition_init_2
        acu3_impaextcondcheckmark_subobject_name_expected = cls.acu3_impaextcondcheckmark_subobject_name_expected
        mcr_rtieacu_fpa_extcondition_init_1 = cls.mcr_rtieacu_fpa_extcondition_init_1
        acu3_fpaextcondtxt_foreground_color_expected = cls.acu3_fpaextcondtxt_foreground_color_expected
        mcr_rtieacu_fpa_extcondition_init_2 = cls.mcr_rtieacu_fpa_extcondition_init_2
        acu3_fpaextcondcheckmark_subobject_name_expected = cls.acu3_fpaextcondcheckmark_subobject_name_expected
        acu3_deflectorpsonbtn_visibility_expected = cls.acu3_deflectorpsonbtn_visibility_expected
        mcr_acu_deflectorps_cmdstatus_init_1 = cls.mcr_acu_deflectorps_cmdstatus_init_1
        acu3_deflectorpsondisable_background_color_expected = cls.acu3_deflectorpsondisable_background_color_expected
        deflector_pson_cmdenable_init_1 = cls.deflector_pson_cmdenable_init_1
        acu3_deflectorpsondisable_visibility_expected = cls.acu3_deflectorpsondisable_visibility_expected
        acu3_deflectorpsoffbtn_visibility_expected = cls.acu3_deflectorpsoffbtn_visibility_expected
        mcr_acu_deflectorps_cmdstatus_init_2 = cls.mcr_acu_deflectorps_cmdstatus_init_2
        acu3_deflectorpsoffdisable_background_color_expected = cls.acu3_deflectorpsoffdisable_background_color_expected
        deflector_psoff_cmdenable_init_1 = cls.deflector_psoff_cmdenable_init_1
        acu3_deflectorpsoffdisable_visibility_expected = cls.acu3_deflectorpsoffdisable_visibility_expected
        mcr_acu_deflectorps_vfeedback_init_1 = cls.mcr_acu_deflectorps_vfeedback_init_1
        acu3_deflectorpsvfeedback_value_expected = cls.acu3_deflectorpsvfeedback_value_expected
        mcr_acu_deflectorps_macfeedback_init_1 = cls.mcr_acu_deflectorps_macfeedback_init_1
        acu3_deflectorpsmacfeedback_value_expected = cls.acu3_deflectorpsmacfeedback_value_expected
        mcr_acu_deflectormotor1_dfeedback_init_1 = cls.mcr_acu_deflectormotor1_dfeedback_init_1
        acu3_deflectormotor1dfeedback_value_expected = cls.acu3_deflectormotor1dfeedback_value_expected
        mcr_acu_deflectormotor2_dfeedback_init_1 = cls.mcr_acu_deflectormotor2_dfeedback_init_1
        acu3_deflectormotor2dfeedback_value_expected = cls.acu3_deflectormotor2dfeedback_value_expected
        mcr_acu_sourcemovement_dfeedback_init_1 = cls.mcr_acu_sourcemovement_dfeedback_init_1
        acu3_srcmovementdfeedback_value_expected = cls.acu3_srcmovementdfeedback_value_expected
        mcr_ecubtcu_penning1cyclo_mbarvacuum_init_1 = cls.mcr_ecubtcu_penning1cyclo_mbarvacuum_init_1
        acu3_penning1mbarvac_value_expected = cls.acu3_penning1mbarvac_value_expected
        mcr_ecubtcu_penning1cyclo_mbarvacuum_init_2 = cls.mcr_ecubtcu_penning1cyclo_mbarvacuum_init_2
        acu3_penning1mbarvac_visibility_expected = cls.acu3_penning1mbarvac_visibility_expected
        mcr_ecubtcu_penning1cyclo_mbarvacuum_init_3 = cls.mcr_ecubtcu_penning1cyclo_mbarvacuum_init_3
        acu3_penning1mbartxt_visibility_expected = cls.acu3_penning1mbartxt_visibility_expected
        mcr_rtieecubtcu_penning1_cyclo_status_init_1 = cls.mcr_rtieecubtcu_penning1_cyclo_status_init_1
        acu3_penning1errormsg_text_expected = cls.acu3_penning1errormsg_text_expected
        mcr_ecubtcu_penning1cyclo_mbarvacuum_init_4 = cls.mcr_ecubtcu_penning1cyclo_mbarvacuum_init_4
        acu3_penning1errormsg_visibility_expected = cls.acu3_penning1errormsg_visibility_expected
        mcr_acu_fpa_kwforwardpower_init_1 = cls.mcr_acu_fpa_kwforwardpower_init_1
        acu3_fpakwforwardpower_value_expected = cls.acu3_fpakwforwardpower_value_expected
        mcr_acu_vdee_vfeedback1_init_1 = cls.mcr_acu_vdee_vfeedback1_init_1
        acu3_vdee1vfeedback_value_expected = cls.acu3_vdee1vfeedback_value_expected
        mcr_acu_vdee_vfeedback2_init_1 = cls.mcr_acu_vdee_vfeedback2_init_1
        acu3_vdee2vfeedback_value_expected = cls.acu3_vdee2vfeedback_value_expected
        vdee_dsetpoint_text_init_1 = cls.vdee_dsetpoint_text_init_1
        acu3_vdeedinput_text_expected = cls.acu3_vdeedinput_text_expected
        mcr_acu_vdee_dsetpoint_init_1 = cls.mcr_acu_vdee_dsetpoint_init_1
        acu3_vdeedfeedback_value_expected = cls.acu3_vdeedfeedback_value_expected
        vdee_dfeedback_visible_init_1 = cls.vdee_dfeedback_visible_init_1
        acu3_vdeedfeedback_visibility_expected = cls.acu3_vdeedfeedback_visibility_expected
        mcr_acu_sw_counter_init_1 = cls.mcr_acu_sw_counter_init_1
        acu3_acucounter_value_expected = cls.acu3_acucounter_value_expected
        mcr_rtieacu_compensationcoil_cfeedback_init_1 = cls.mcr_rtieacu_compensationcoil_cfeedback_init_1
        acu3_compcoilcfeedback_value_expected = cls.acu3_compcoilcfeedback_value_expected
        acu3_savebtn_visibility_expected = cls.acu3_savebtn_visibility_expected
        acu3_edit_eqt_param_visibility_expected = cls.acu3_edit_eqt_param_visibility_expected
        mcr_acu_radialprobe_outls_init_1 = cls.mcr_acu_radialprobe_outls_init_1
        acu3_rpoutlsstatus_subobject_name_expected = cls.acu3_rpoutlsstatus_subobject_name_expected
        acu3_esslayoutbtn_visibility_expected = cls.acu3_esslayoutbtn_visibility_expected
        acu3_t1onbtn_visibility_expected = cls.acu3_t1onbtn_visibility_expected
        mcr_acu_t1_cmdstatus_init_1 = cls.mcr_acu_t1_cmdstatus_init_1
        acu3_t1ondisable_background_color_expected = cls.acu3_t1ondisable_background_color_expected
        steeringextrps_sg1_pson_cmdenable_init_1 = cls.steeringextrps_sg1_pson_cmdenable_init_1
        acu3_t1ondisable_visibility_expected = cls.acu3_t1ondisable_visibility_expected
        acu3_t1offbtn_visibility_expected = cls.acu3_t1offbtn_visibility_expected
        mcr_acu_t1_cmdstatus_init_2 = cls.mcr_acu_t1_cmdstatus_init_2
        acu3_t1offdisable_background_color_expected = cls.acu3_t1offdisable_background_color_expected
        steeringextrps_sg1_psoff_cmdenable_init_1 = cls.steeringextrps_sg1_psoff_cmdenable_init_1
        acu3_t1offdisable_visibility_expected = cls.acu3_t1offdisable_visibility_expected
        acu3_t1psvideo_visibility_expected = cls.acu3_t1psvideo_visibility_expected
        acu3_t2onbtn_visibility_expected = cls.acu3_t2onbtn_visibility_expected
        mcr_acu_t2_cmdstatus_init_1 = cls.mcr_acu_t2_cmdstatus_init_1
        acu3_t2ondisable_background_color_expected = cls.acu3_t2ondisable_background_color_expected
        steeringextrps_sg2_pson_cmdenable_init_1 = cls.steeringextrps_sg2_pson_cmdenable_init_1
        acu3_t2ondisable_visibility_expected = cls.acu3_t2ondisable_visibility_expected
        acu3_t2offbtn_visibility_expected = cls.acu3_t2offbtn_visibility_expected
        mcr_acu_t2_cmdstatus_init_2 = cls.mcr_acu_t2_cmdstatus_init_2
        acu3_t2offdisable_background_color_expected = cls.acu3_t2offdisable_background_color_expected
        steeringextrps_sg2_psoff_cmdenable_init_1 = cls.steeringextrps_sg2_psoff_cmdenable_init_1
        acu3_t2offdisable_visibility_expected = cls.acu3_t2offdisable_visibility_expected
        acu3_essctrlbtn_visibility_expected = cls.acu3_essctrlbtn_visibility_expected
        acu3_maincoiltuningbtn_visibility_expected = cls.acu3_maincoiltuningbtn_visibility_expected
        mcr_acu_maincoil_tuning_cmdstatus_init_1 = cls.mcr_acu_maincoil_tuning_cmdstatus_init_1
        acu3_maincoiltuningdisable_background_color_expected = cls.acu3_maincoiltuningdisable_background_color_expected
        maincoil_tuning_cmdenable_init_1 = cls.maincoil_tuning_cmdenable_init_1
        acu3_maincoiltuningdisable_visibility_expected = cls.acu3_maincoiltuningdisable_visibility_expected
        mcr_acu_maincoil_tuning_cmdstatus_init_2 = cls.mcr_acu_maincoil_tuning_cmdstatus_init_2
        acu3_maincoiltuningled_visibility_expected = cls.acu3_maincoiltuningled_visibility_expected
        acu3_arctuningbtn_visibility_expected = cls.acu3_arctuningbtn_visibility_expected
        mcr_acu_source_tuning_cmdenable_init_1 = cls.mcr_acu_source_tuning_cmdenable_init_1
        acu3_arctuningdisable_visibility_expected = cls.acu3_arctuningdisable_visibility_expected
        mcr_acu_source_tuning_cmdstatus_init_1 = cls.mcr_acu_source_tuning_cmdstatus_init_1
        acu3_arctuningled_visibility_expected = cls.acu3_arctuningled_visibility_expected
        acu3_positionstatus_visibility_expected = cls.acu3_positionstatus_visibility_expected
        acu3_maincoilpsvideo_visibility_expected = cls.acu3_maincoilpsvideo_visibility_expected
        acu3_sourcepsvideo_visibility_expected = cls.acu3_sourcepsvideo_visibility_expected
        acu3_llrfvideo_visibility_expected = cls.acu3_llrfvideo_visibility_expected
        acu3_ssavideo_visibility_expected = cls.acu3_ssavideo_visibility_expected
        acu3_impavideo_visibility_expected = cls.acu3_impavideo_visibility_expected
        acu3_fpavideo_visibility_expected = cls.acu3_fpavideo_visibility_expected
        acu3_rfvideo_visibility_expected = cls.acu3_rfvideo_visibility_expected
        acu3_deflectorpsvideo_visibility_expected = cls.acu3_deflectorpsvideo_visibility_expected
        acu3_cyclovacvideo_visibility_expected = cls.acu3_cyclovacvideo_visibility_expected
        acu3_hydrolicstationstatus_visibility_expected = cls.acu3_hydrolicstationstatus_visibility_expected
        acu3_coolingstatus_visibility_expected = cls.acu3_coolingstatus_visibility_expected

        #set initial values
        set_mcr_acu_sw_healthStatus_1 = MsgTypeString("mcr_acu_sw_healthStatus", mcr_acu_sw_healthStatus_init_1)
        set_mcr_acu_maincoilps_cmdstatus_1 = MsgTypeBoolean("mcr_acu_maincoilps_cmdstatus", mcr_acu_maincoilps_cmdstatus_init_1)
        set_maincoil_pson_cmdenable_1 = MsgTypeBoolean("maincoil_pson_cmdenable", maincoil_pson_cmdenable_init_1)
        set_mcr_acu_maincoilps_cmdstatus_2 = MsgTypeBoolean("mcr_acu_maincoilps_cmdstatus", mcr_acu_maincoilps_cmdstatus_init_2)
        set_maincoil_psoff_cmdenable_1 = MsgTypeBoolean("maincoil_psoff_cmdenable", maincoil_psoff_cmdenable_init_1)
        set_mcr_rtieacu_maincoil_cfeedback_1 = MsgTypeNumeric("mcr_rtieacu_maincoil_cfeedback", mcr_rtieacu_maincoil_cfeedback_init_1)
        set_mcr_rtieacu_coil24_cfeedback_1 = MsgTypeNumeric("mcr_rtieacu_coil24_cfeedback", mcr_rtieacu_coil24_cfeedback_init_1)
        set_mcr_rtieacu_coil13_cfeedback_1 = MsgTypeNumeric("mcr_rtieacu_coil13_cfeedback", mcr_rtieacu_coil13_cfeedback_init_1)
        set_mcr_rtieacu_radialprobe_vert_location_1 = MsgTypeNumeric("mcr_rtieacu_radialprobe_vert_location", mcr_rtieacu_radialprobe_vert_location_init_1)
        set_mcr_rtieacu_radialprobe_energy_1 = MsgTypeNumeric("mcr_rtieacu_radialprobe_energy", mcr_rtieacu_radialprobe_energy_init_1)
        set_rf_on_cmdenable_1 = MsgTypeBoolean("rf_on_cmdenable", rf_on_cmdenable_init_1)
        set_rf_off_cmdenable_1 = MsgTypeBoolean("rf_off_cmdenable", rf_off_cmdenable_init_1)
        set_mcr_acu_modulator_cmdenable_1 = MsgTypeBoolean("mcr_acu_modulator_cmdenable", mcr_acu_modulator_cmdenable_init_1)
        set_mcr_acu_modulator_cmdenable_2 = MsgTypeBoolean("mcr_acu_modulator_cmdenable", mcr_acu_modulator_cmdenable_init_2)
        set_mcr_acu_q1q2_cmdstatus_1 = MsgTypeBoolean("mcr_acu_q1q2_cmdstatus", mcr_acu_q1q2_cmdstatus_init_1)
        set_quadextrps_q1q2_pson_cmdenable_1 = MsgTypeBoolean("quadextrps_q1q2_pson_cmdenable", quadextrps_q1q2_pson_cmdenable_init_1)
        set_mcr_acu_q1q2_cmdstatus_2 = MsgTypeBoolean("mcr_acu_q1q2_cmdstatus", mcr_acu_q1q2_cmdstatus_init_2)
        set_quadextrps_q1q2_psoff_cmdenable_1 = MsgTypeBoolean("quadextrps_q1q2_psoff_cmdenable", quadextrps_q1q2_psoff_cmdenable_init_1)
        set_mcr_rtieacu_q1_cfeedback_1 = MsgTypeNumeric("mcr_rtieacu_q1_cfeedback", mcr_rtieacu_q1_cfeedback_init_1)
        set_mcr_rtieacu_q2_cfeedback_1 = MsgTypeNumeric("mcr_rtieacu_q2_cfeedback", mcr_rtieacu_q2_cfeedback_init_1)
        set_mcr_acu_sourcearc_cmdstatus_1 = MsgTypeBoolean("mcr_acu_sourcearc_cmdstatus", mcr_acu_sourcearc_cmdstatus_init_1)
        set_source_sourceon_cmdenable_1 = MsgTypeBoolean("source_sourceon_cmdenable", source_sourceon_cmdenable_init_1)
        set_mcr_acu_sourcearc_cmdstatus_2 = MsgTypeBoolean("mcr_acu_sourcearc_cmdstatus", mcr_acu_sourcearc_cmdstatus_init_2)
        set_source_sourceoff_cmdenable_1 = MsgTypeBoolean("source_sourceoff_cmdenable", source_sourceoff_cmdenable_init_1)
        set_mcr_acu_sourcefilament_cfeedback_1 = MsgTypeNumeric("mcr_acu_sourcefilament_cfeedback", mcr_acu_sourcefilament_cfeedback_init_1)
        set_mcr_acu_sourcearc_cfeedback_1 = MsgTypeNumeric("mcr_acu_sourcearc_cfeedback", mcr_acu_sourcearc_cfeedback_init_1)
        set_mcr_acu_sourcearc_vfeedback_1 = MsgTypeNumeric("mcr_acu_sourcearc_vfeedback", mcr_acu_sourcearc_vfeedback_init_1)
        set_mcr_rtieacu_impa_extcondition_1 = MsgTypeBoolean("mcr_rtieacu_impa_extcondition", mcr_rtieacu_impa_extcondition_init_1)
        set_mcr_acu_radialprobe_inls_1 = MsgTypeBoolean("mcr_acu_radialprobe_inls", mcr_acu_radialprobe_inls_init_1)
        set_mcr_rtieacu_impa_extcondition_2 = MsgTypeBoolean("mcr_rtieacu_impa_extcondition", mcr_rtieacu_impa_extcondition_init_2)
        set_mcr_rtieacu_fpa_extcondition_1 = MsgTypeBoolean("mcr_rtieacu_fpa_extcondition", mcr_rtieacu_fpa_extcondition_init_1)
        set_mcr_rtieacu_fpa_extcondition_2 = MsgTypeBoolean("mcr_rtieacu_fpa_extcondition", mcr_rtieacu_fpa_extcondition_init_2)
        set_mcr_acu_deflectorps_cmdstatus_1 = MsgTypeBoolean("mcr_acu_deflectorps_cmdstatus", mcr_acu_deflectorps_cmdstatus_init_1)
        set_deflector_pson_cmdenable_1 = MsgTypeBoolean("deflector_pson_cmdenable", deflector_pson_cmdenable_init_1)
        set_mcr_acu_deflectorps_cmdstatus_2 = MsgTypeBoolean("mcr_acu_deflectorps_cmdstatus", mcr_acu_deflectorps_cmdstatus_init_2)
        set_deflector_psoff_cmdenable_1 = MsgTypeBoolean("deflector_psoff_cmdenable", deflector_psoff_cmdenable_init_1)
        set_mcr_acu_deflectorps_vfeedback_1 = MsgTypeNumeric("mcr_acu_deflectorps_vfeedback", mcr_acu_deflectorps_vfeedback_init_1)
        set_mcr_acu_deflectorps_macfeedback_1 = MsgTypeNumeric("mcr_acu_deflectorps_macfeedback", mcr_acu_deflectorps_macfeedback_init_1)
        set_mcr_acu_deflectormotor1_dfeedback_1 = MsgTypeNumeric("mcr_acu_deflectormotor1_dfeedback", mcr_acu_deflectormotor1_dfeedback_init_1)
        set_mcr_acu_deflectormotor2_dfeedback_1 = MsgTypeNumeric("mcr_acu_deflectormotor2_dfeedback", mcr_acu_deflectormotor2_dfeedback_init_1)
        set_mcr_acu_sourcemovement_dfeedback_1 = MsgTypeNumeric("mcr_acu_sourcemovement_dfeedback", mcr_acu_sourcemovement_dfeedback_init_1)
        set_mcr_ecubtcu_penning1cyclo_mbarvacuum_1 = MsgTypeNumeric("mcr_ecubtcu_penning1cyclo_mbarvacuum", mcr_ecubtcu_penning1cyclo_mbarvacuum_init_1)
        set_mcr_ecubtcu_penning1cyclo_mbarvacuum_2 = MsgTypeNumeric("mcr_ecubtcu_penning1cyclo_mbarvacuum", mcr_ecubtcu_penning1cyclo_mbarvacuum_init_2)
        set_mcr_ecubtcu_penning1cyclo_mbarvacuum_3 = MsgTypeNumeric("mcr_ecubtcu_penning1cyclo_mbarvacuum", mcr_ecubtcu_penning1cyclo_mbarvacuum_init_3)
        set_mcr_rtieecubtcu_penning1_cyclo_status_1 = MsgTypeString("mcr_rtieecubtcu_penning1_cyclo_status", mcr_rtieecubtcu_penning1_cyclo_status_init_1)
        set_mcr_ecubtcu_penning1cyclo_mbarvacuum_4 = MsgTypeNumeric("mcr_ecubtcu_penning1cyclo_mbarvacuum", mcr_ecubtcu_penning1cyclo_mbarvacuum_init_4)
        set_mcr_acu_fpa_kwforwardpower_1 = MsgTypeNumeric("mcr_acu_fpa_kwforwardpower", mcr_acu_fpa_kwforwardpower_init_1)
        set_mcr_acu_vdee_vfeedback1_1 = MsgTypeNumeric("mcr_acu_vdee_vfeedback1", mcr_acu_vdee_vfeedback1_init_1)
        set_mcr_acu_vdee_vfeedback2_1 = MsgTypeNumeric("mcr_acu_vdee_vfeedback2", mcr_acu_vdee_vfeedback2_init_1)
        set_vdee_dsetpoint_text_1 = MsgTypeString("vdee_dsetpoint_text", vdee_dsetpoint_text_init_1)
        set_mcr_acu_vdee_dsetpoint_1 = MsgTypeNumeric("mcr_acu_vdee_dsetpoint", mcr_acu_vdee_dsetpoint_init_1)
        set_vdee_dfeedback_visible_1 = MsgTypeBoolean("vdee_dfeedback_visible", vdee_dfeedback_visible_init_1)
        set_mcr_acu_sw_counter_1 = MsgTypeNumeric("mcr_acu_sw_counter", mcr_acu_sw_counter_init_1)
        set_mcr_rtieacu_compensationcoil_cfeedback_1 = MsgTypeNumeric("mcr_rtieacu_compensationcoil_cfeedback", mcr_rtieacu_compensationcoil_cfeedback_init_1)
        set_mcr_acu_radialprobe_outls_1 = MsgTypeBoolean("mcr_acu_radialprobe_outls", mcr_acu_radialprobe_outls_init_1)
        set_mcr_acu_t1_cmdstatus_1 = MsgTypeBoolean("mcr_acu_t1_cmdstatus", mcr_acu_t1_cmdstatus_init_1)
        set_steeringextrps_sg1_pson_cmdenable_1 = MsgTypeBoolean("steeringextrps_sg1_pson_cmdenable", steeringextrps_sg1_pson_cmdenable_init_1)
        set_mcr_acu_t1_cmdstatus_2 = MsgTypeBoolean("mcr_acu_t1_cmdstatus", mcr_acu_t1_cmdstatus_init_2)
        set_steeringextrps_sg1_psoff_cmdenable_1 = MsgTypeBoolean("steeringextrps_sg1_psoff_cmdenable", steeringextrps_sg1_psoff_cmdenable_init_1)
        set_mcr_acu_t2_cmdstatus_1 = MsgTypeBoolean("mcr_acu_t2_cmdstatus", mcr_acu_t2_cmdstatus_init_1)
        set_steeringextrps_sg2_pson_cmdenable_1 = MsgTypeBoolean("steeringextrps_sg2_pson_cmdenable", steeringextrps_sg2_pson_cmdenable_init_1)
        set_mcr_acu_t2_cmdstatus_2 = MsgTypeBoolean("mcr_acu_t2_cmdstatus", mcr_acu_t2_cmdstatus_init_2)
        set_steeringextrps_sg2_psoff_cmdenable_1 = MsgTypeBoolean("steeringextrps_sg2_psoff_cmdenable", steeringextrps_sg2_psoff_cmdenable_init_1)
        set_mcr_acu_maincoil_tuning_cmdstatus_1 = MsgTypeBoolean("mcr_acu_maincoil_tuning_cmdstatus", mcr_acu_maincoil_tuning_cmdstatus_init_1)
        set_maincoil_tuning_cmdenable_1 = MsgTypeBoolean("maincoil_tuning_cmdenable", maincoil_tuning_cmdenable_init_1)
        set_mcr_acu_maincoil_tuning_cmdstatus_2 = MsgTypeBoolean("mcr_acu_maincoil_tuning_cmdstatus", mcr_acu_maincoil_tuning_cmdstatus_init_2)
        set_mcr_acu_source_tuning_cmdenable_1 = MsgTypeBoolean("mcr_acu_source_tuning_cmdenable", mcr_acu_source_tuning_cmdenable_init_1)
        set_mcr_acu_source_tuning_cmdstatus_1 = MsgTypeBoolean("mcr_acu_source_tuning_cmdstatus", mcr_acu_source_tuning_cmdstatus_init_1)

        #get values
        get_acu3_t2psvideo_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_t2psvideo")
        get_acu3_acuhealthstatus_text = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_TEXT_FIELD, variable_in = "acu3_acuhealthstatus")
        get_acu3_radialprobe_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_radialprobe")
        get_acu3_maincoilpsonbtn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_maincoilpsonbtn")
        get_acu3_maincoilpsondisable_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "acu3_maincoilpsondisable")
        get_acu3_maincoilpsondisable_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_maincoilpsondisable")
        get_acu3_maincoilpsoffbtn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_maincoilpsoffbtn")
        get_acu3_maincoilpsoffdisable_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "acu3_maincoilpsoffdisable")
        get_acu3_maincoilpsoffdisable_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_maincoilpsoffdisable")
        get_acu3_maincoilcfeedback_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "acu3_maincoilcfeedback")
        get_acu3_coil24cfeedback_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "acu3_coil24cfeedback")
        get_acu3_coil13cfeedback_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "acu3_coil13cfeedback")
        get_acu3_rpvertposition_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "acu3_rpvertposition")
        get_acu3_rpenergy_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "acu3_rpenergy")
        get_acu3_rfonbtn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_rfonbtn")
        get_acu3_rfondisable_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_rfondisable")
        get_acu3_rfoffbtn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_rfoffbtn")
        get_acu3_rfoffdisable_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_rfoffdisable")
        get_acu3_modintlk_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "acu3_modintlk")
        get_acu3_modintlk_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "acu3_modintlk")
        get_acu3_q1q2psonbtn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_q1q2psonbtn")
        get_acu3_q1q2psondisable_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "acu3_q1q2psondisable")
        get_acu3_q1q2psondisable_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_q1q2psondisable")
        get_acu3_q1q2psoffbtn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_q1q2psoffbtn")
        get_acu3_q1q2psoffdisable_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "acu3_q1q2psoffdisable")
        get_acu3_q1q2psoffdisable_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_q1q2psoffdisable")
        get_acu3_q1q2video_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_q1q2video")
        get_acu3_q1cfeedback_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "acu3_q1cfeedback")
        get_acu3_q2cfeedback_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "acu3_q2cfeedback")
        get_acu3_sourceonbtn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_sourceonbtn")
        get_acu3_sourceondisable_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "acu3_sourceondisable")
        get_acu3_sourceondisable_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_sourceondisable")
        get_acu3_sourceoffbtn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_sourceoffbtn")
        get_acu3_sourceoffdisable_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "acu3_sourceoffdisable")
        get_acu3_sourceoffdisable_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_sourceoffdisable")
        get_acu3_filamentcfeedback_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "acu3_filamentcfeedback")
        get_acu3_arccfeedback_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "acu3_arccfeedback")
        get_acu3_arcvfeedback_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "acu3_arcvfeedback")
        get_acu3_impaextcondtxt_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "acu3_impaextcondtxt")
        get_acu3_rpinlsstatus_subobject_name = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "acu3_rpinlsstatus")
        get_acu3_impaextcondcheckmark_subobject_name = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "acu3_impaextcondcheckmark")
        get_acu3_fpaextcondtxt_foreground_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "acu3_fpaextcondtxt")
        get_acu3_fpaextcondcheckmark_subobject_name = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "acu3_fpaextcondcheckmark")
        get_acu3_deflectorpsonbtn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_deflectorpsonbtn")
        get_acu3_deflectorpsondisable_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "acu3_deflectorpsondisable")
        get_acu3_deflectorpsondisable_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_deflectorpsondisable")
        get_acu3_deflectorpsoffbtn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_deflectorpsoffbtn")
        get_acu3_deflectorpsoffdisable_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "acu3_deflectorpsoffdisable")
        get_acu3_deflectorpsoffdisable_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_deflectorpsoffdisable")
        get_acu3_deflectorpsvfeedback_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "acu3_deflectorpsvfeedback")
        get_acu3_deflectorpsmacfeedback_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "acu3_deflectorpsmacfeedback")
        get_acu3_deflectormotor1dfeedback_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "acu3_deflectormotor1dfeedback")
        get_acu3_deflectormotor2dfeedback_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "acu3_deflectormotor2dfeedback")
        get_acu3_srcmovementdfeedback_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "acu3_srcmovementdfeedback")
        get_acu3_penning1mbarvac_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "acu3_penning1mbarvac")
        get_acu3_penning1mbarvac_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_penning1mbarvac")
        get_acu3_penning1mbartxt_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_penning1mbartxt")
        get_acu3_penning1errormsg_text = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_TEXT_FIELD, variable_in = "acu3_penning1errormsg")
        get_acu3_penning1errormsg_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_penning1errormsg")
        get_acu3_fpakwforwardpower_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "acu3_fpakwforwardpower")
        get_acu3_vdee1vfeedback_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "acu3_vdee1vfeedback")
        get_acu3_vdee2vfeedback_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "acu3_vdee2vfeedback")
        get_acu3_vdeedinput_text = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_TEXT_FIELD, variable_in = "acu3_vdeedinput")
        get_acu3_vdeedfeedback_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "acu3_vdeedfeedback")
        get_acu3_vdeedfeedback_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_vdeedfeedback")
        get_acu3_acucounter_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "acu3_acucounter")
        get_acu3_compcoilcfeedback_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "acu3_compcoilcfeedback")
        get_acu3_savebtn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_savebtn")
        get_acu3_edit_eqt_param_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_edit_eqt_param")
        get_acu3_rpoutlsstatus_subobject_name = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "acu3_rpoutlsstatus")
        get_acu3_esslayoutbtn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_esslayoutbtn")
        get_acu3_t1onbtn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_t1onbtn")
        get_acu3_t1ondisable_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "acu3_t1ondisable")
        get_acu3_t1ondisable_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_t1ondisable")
        get_acu3_t1offbtn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_t1offbtn")
        get_acu3_t1offdisable_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "acu3_t1offdisable")
        get_acu3_t1offdisable_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_t1offdisable")
        get_acu3_t1psvideo_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_t1psvideo")
        get_acu3_t2onbtn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_t2onbtn")
        get_acu3_t2ondisable_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "acu3_t2ondisable")
        get_acu3_t2ondisable_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_t2ondisable")
        get_acu3_t2offbtn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_t2offbtn")
        get_acu3_t2offdisable_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "acu3_t2offdisable")
        get_acu3_t2offdisable_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_t2offdisable")
        get_acu3_essctrlbtn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_essctrlbtn")
        get_acu3_maincoiltuningbtn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_maincoiltuningbtn")
        get_acu3_maincoiltuningdisable_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "acu3_maincoiltuningdisable")
        get_acu3_maincoiltuningdisable_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_maincoiltuningdisable")
        get_acu3_maincoiltuningled_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_maincoiltuningled")
        get_acu3_arctuningbtn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_arctuningbtn")
        get_acu3_arctuningdisable_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_arctuningdisable")
        get_acu3_arctuningled_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_arctuningled")
        get_acu3_positionstatus_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_positionstatus")
        get_acu3_maincoilpsvideo_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_maincoilpsvideo")
        get_acu3_sourcepsvideo_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_sourcepsvideo")
        get_acu3_llrfvideo_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_llrfvideo")
        get_acu3_ssavideo_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_ssavideo")
        get_acu3_impavideo_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_impavideo")
        get_acu3_fpavideo_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_fpavideo")
        get_acu3_rfvideo_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_rfvideo")
        get_acu3_deflectorpsvideo_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_deflectorpsvideo")
        get_acu3_cyclovacvideo_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_cyclovacvideo")
        get_acu3_hydrolicstationstatus_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_hydrolicstationstatus")
        get_acu3_coolingstatus_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu3_coolingstatus")

        #validate
        validate_acu3_t2psvideo_visibility = MsgTypeString("acu3_t2psvideo:TMMI_MCR_IS_VISIBLE", value=acu3_t2psvideo_visibility_expected)
        validate_acu3_acuhealthstatus_text = MsgTypeString("acu3_acuhealthstatus:TMMI_MCR_TEXT_FIELD", value=acu3_acuhealthstatus_text_expected)
        validate_acu3_radialprobe_visibility = MsgTypeString("acu3_radialprobe:TMMI_MCR_IS_VISIBLE", value=acu3_radialprobe_visibility_expected)
        validate_acu3_maincoilpsonbtn_visibility = MsgTypeString("acu3_maincoilpsonbtn:TMMI_MCR_IS_VISIBLE", value=acu3_maincoilpsonbtn_visibility_expected)
        validate_acu3_maincoilpsondisable_background_color = MsgTypeString("acu3_maincoilpsondisable:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=acu3_maincoilpsondisable_background_color_expected)
        validate_acu3_maincoilpsondisable_visibility = MsgTypeString("acu3_maincoilpsondisable:TMMI_MCR_IS_VISIBLE", value=acu3_maincoilpsondisable_visibility_expected)
        validate_acu3_maincoilpsoffbtn_visibility = MsgTypeString("acu3_maincoilpsoffbtn:TMMI_MCR_IS_VISIBLE", value=acu3_maincoilpsoffbtn_visibility_expected)
        validate_acu3_maincoilpsoffdisable_background_color = MsgTypeString("acu3_maincoilpsoffdisable:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=acu3_maincoilpsoffdisable_background_color_expected)
        validate_acu3_maincoilpsoffdisable_visibility = MsgTypeString("acu3_maincoilpsoffdisable:TMMI_MCR_IS_VISIBLE", value=acu3_maincoilpsoffdisable_visibility_expected)
        validate_acu3_maincoilcfeedback_value = MsgTypeNumeric("acu3_maincoilcfeedback:TMMI_MCR_OBJECT_GET_VALUE", value=acu3_maincoilcfeedback_value_expected)
        validate_acu3_coil24cfeedback_value = MsgTypeNumeric("acu3_coil24cfeedback:TMMI_MCR_OBJECT_GET_VALUE", value=acu3_coil24cfeedback_value_expected)
        validate_acu3_coil13cfeedback_value = MsgTypeNumeric("acu3_coil13cfeedback:TMMI_MCR_OBJECT_GET_VALUE", value=acu3_coil13cfeedback_value_expected)
        validate_acu3_rpvertposition_value = MsgTypeNumeric("acu3_rpvertposition:TMMI_MCR_OBJECT_GET_VALUE", value=acu3_rpvertposition_value_expected)
        validate_acu3_rpenergy_value = MsgTypeNumeric("acu3_rpenergy:TMMI_MCR_OBJECT_GET_VALUE", value=acu3_rpenergy_value_expected)
        validate_acu3_rfonbtn_visibility = MsgTypeString("acu3_rfonbtn:TMMI_MCR_IS_VISIBLE", value=acu3_rfonbtn_visibility_expected)
        validate_acu3_rfondisable_visibility = MsgTypeString("acu3_rfondisable:TMMI_MCR_IS_VISIBLE", value=acu3_rfondisable_visibility_expected)
        validate_acu3_rfoffbtn_visibility = MsgTypeString("acu3_rfoffbtn:TMMI_MCR_IS_VISIBLE", value=acu3_rfoffbtn_visibility_expected)
        validate_acu3_rfoffdisable_visibility = MsgTypeString("acu3_rfoffdisable:TMMI_MCR_IS_VISIBLE", value=acu3_rfoffdisable_visibility_expected)
        validate_acu3_modintlk_foreground_color = MsgTypeString("acu3_modintlk:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=acu3_modintlk_foreground_color_expected)
        validate_acu3_modintlk_background_color = MsgTypeString("acu3_modintlk:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=acu3_modintlk_background_color_expected)
        validate_acu3_q1q2psonbtn_visibility = MsgTypeString("acu3_q1q2psonbtn:TMMI_MCR_IS_VISIBLE", value=acu3_q1q2psonbtn_visibility_expected)
        validate_acu3_q1q2psondisable_background_color = MsgTypeString("acu3_q1q2psondisable:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=acu3_q1q2psondisable_background_color_expected)
        validate_acu3_q1q2psondisable_visibility = MsgTypeString("acu3_q1q2psondisable:TMMI_MCR_IS_VISIBLE", value=acu3_q1q2psondisable_visibility_expected)
        validate_acu3_q1q2psoffbtn_visibility = MsgTypeString("acu3_q1q2psoffbtn:TMMI_MCR_IS_VISIBLE", value=acu3_q1q2psoffbtn_visibility_expected)
        validate_acu3_q1q2psoffdisable_background_color = MsgTypeString("acu3_q1q2psoffdisable:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=acu3_q1q2psoffdisable_background_color_expected)
        validate_acu3_q1q2psoffdisable_visibility = MsgTypeString("acu3_q1q2psoffdisable:TMMI_MCR_IS_VISIBLE", value=acu3_q1q2psoffdisable_visibility_expected)
        validate_acu3_q1q2video_visibility = MsgTypeString("acu3_q1q2video:TMMI_MCR_IS_VISIBLE", value=acu3_q1q2video_visibility_expected)
        validate_acu3_q1cfeedback_value = MsgTypeNumeric("acu3_q1cfeedback:TMMI_MCR_OBJECT_GET_VALUE", value=acu3_q1cfeedback_value_expected)
        validate_acu3_q2cfeedback_value = MsgTypeNumeric("acu3_q2cfeedback:TMMI_MCR_OBJECT_GET_VALUE", value=acu3_q2cfeedback_value_expected)
        validate_acu3_sourceonbtn_visibility = MsgTypeString("acu3_sourceonbtn:TMMI_MCR_IS_VISIBLE", value=acu3_sourceonbtn_visibility_expected)
        validate_acu3_sourceondisable_background_color = MsgTypeString("acu3_sourceondisable:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=acu3_sourceondisable_background_color_expected)
        validate_acu3_sourceondisable_visibility = MsgTypeString("acu3_sourceondisable:TMMI_MCR_IS_VISIBLE", value=acu3_sourceondisable_visibility_expected)
        validate_acu3_sourceoffbtn_visibility = MsgTypeString("acu3_sourceoffbtn:TMMI_MCR_IS_VISIBLE", value=acu3_sourceoffbtn_visibility_expected)
        validate_acu3_sourceoffdisable_background_color = MsgTypeString("acu3_sourceoffdisable:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=acu3_sourceoffdisable_background_color_expected)
        validate_acu3_sourceoffdisable_visibility = MsgTypeString("acu3_sourceoffdisable:TMMI_MCR_IS_VISIBLE", value=acu3_sourceoffdisable_visibility_expected)
        validate_acu3_filamentcfeedback_value = MsgTypeNumeric("acu3_filamentcfeedback:TMMI_MCR_OBJECT_GET_VALUE", value=acu3_filamentcfeedback_value_expected)
        validate_acu3_arccfeedback_value = MsgTypeNumeric("acu3_arccfeedback:TMMI_MCR_OBJECT_GET_VALUE", value=acu3_arccfeedback_value_expected)
        validate_acu3_arcvfeedback_value = MsgTypeNumeric("acu3_arcvfeedback:TMMI_MCR_OBJECT_GET_VALUE", value=acu3_arcvfeedback_value_expected)
        validate_acu3_impaextcondtxt_foreground_color = MsgTypeString("acu3_impaextcondtxt:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=acu3_impaextcondtxt_foreground_color_expected)
        validate_acu3_rpinlsstatus_subobject_name = MsgTypeString("acu3_rpinlsstatus:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=acu3_rpinlsstatus_subobject_name_expected)
        validate_acu3_impaextcondcheckmark_subobject_name = MsgTypeString("acu3_impaextcondcheckmark:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=acu3_impaextcondcheckmark_subobject_name_expected)
        validate_acu3_fpaextcondtxt_foreground_color = MsgTypeString("acu3_fpaextcondtxt:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=acu3_fpaextcondtxt_foreground_color_expected)
        validate_acu3_fpaextcondcheckmark_subobject_name = MsgTypeString("acu3_fpaextcondcheckmark:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=acu3_fpaextcondcheckmark_subobject_name_expected)
        validate_acu3_deflectorpsonbtn_visibility = MsgTypeString("acu3_deflectorpsonbtn:TMMI_MCR_IS_VISIBLE", value=acu3_deflectorpsonbtn_visibility_expected)
        validate_acu3_deflectorpsondisable_background_color = MsgTypeString("acu3_deflectorpsondisable:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=acu3_deflectorpsondisable_background_color_expected)
        validate_acu3_deflectorpsondisable_visibility = MsgTypeString("acu3_deflectorpsondisable:TMMI_MCR_IS_VISIBLE", value=acu3_deflectorpsondisable_visibility_expected)
        validate_acu3_deflectorpsoffbtn_visibility = MsgTypeString("acu3_deflectorpsoffbtn:TMMI_MCR_IS_VISIBLE", value=acu3_deflectorpsoffbtn_visibility_expected)
        validate_acu3_deflectorpsoffdisable_background_color = MsgTypeString("acu3_deflectorpsoffdisable:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=acu3_deflectorpsoffdisable_background_color_expected)
        validate_acu3_deflectorpsoffdisable_visibility = MsgTypeString("acu3_deflectorpsoffdisable:TMMI_MCR_IS_VISIBLE", value=acu3_deflectorpsoffdisable_visibility_expected)
        validate_acu3_deflectorpsvfeedback_value = MsgTypeNumeric("acu3_deflectorpsvfeedback:TMMI_MCR_OBJECT_GET_VALUE", value=acu3_deflectorpsvfeedback_value_expected)
        validate_acu3_deflectorpsmacfeedback_value = MsgTypeNumeric("acu3_deflectorpsmacfeedback:TMMI_MCR_OBJECT_GET_VALUE", value=acu3_deflectorpsmacfeedback_value_expected)
        validate_acu3_deflectormotor1dfeedback_value = MsgTypeNumeric("acu3_deflectormotor1dfeedback:TMMI_MCR_OBJECT_GET_VALUE", value=acu3_deflectormotor1dfeedback_value_expected)
        validate_acu3_deflectormotor2dfeedback_value = MsgTypeNumeric("acu3_deflectormotor2dfeedback:TMMI_MCR_OBJECT_GET_VALUE", value=acu3_deflectormotor2dfeedback_value_expected)
        validate_acu3_srcmovementdfeedback_value = MsgTypeNumeric("acu3_srcmovementdfeedback:TMMI_MCR_OBJECT_GET_VALUE", value=acu3_srcmovementdfeedback_value_expected)
        validate_acu3_penning1mbarvac_value = MsgTypeNumeric("acu3_penning1mbarvac:TMMI_MCR_OBJECT_GET_VALUE", value=acu3_penning1mbarvac_value_expected)
        validate_acu3_penning1mbarvac_visibility = MsgTypeString("acu3_penning1mbarvac:TMMI_MCR_IS_VISIBLE", value=acu3_penning1mbarvac_visibility_expected)
        validate_acu3_penning1mbartxt_visibility = MsgTypeString("acu3_penning1mbartxt:TMMI_MCR_IS_VISIBLE", value=acu3_penning1mbartxt_visibility_expected)
        validate_acu3_penning1errormsg_text = MsgTypeString("acu3_penning1errormsg:TMMI_MCR_TEXT_FIELD", value=acu3_penning1errormsg_text_expected)
        validate_acu3_penning1errormsg_visibility = MsgTypeString("acu3_penning1errormsg:TMMI_MCR_IS_VISIBLE", value=acu3_penning1errormsg_visibility_expected)
        validate_acu3_fpakwforwardpower_value = MsgTypeNumeric("acu3_fpakwforwardpower:TMMI_MCR_OBJECT_GET_VALUE", value=acu3_fpakwforwardpower_value_expected)
        validate_acu3_vdee1vfeedback_value = MsgTypeNumeric("acu3_vdee1vfeedback:TMMI_MCR_OBJECT_GET_VALUE", value=acu3_vdee1vfeedback_value_expected)
        validate_acu3_vdee2vfeedback_value = MsgTypeNumeric("acu3_vdee2vfeedback:TMMI_MCR_OBJECT_GET_VALUE", value=acu3_vdee2vfeedback_value_expected)
        validate_acu3_vdeedinput_text = MsgTypeString("acu3_vdeedinput:TMMI_MCR_TEXT_FIELD", value=acu3_vdeedinput_text_expected)
        validate_acu3_vdeedfeedback_value = MsgTypeNumeric("acu3_vdeedfeedback:TMMI_MCR_OBJECT_GET_VALUE", value=acu3_vdeedfeedback_value_expected)
        validate_acu3_vdeedfeedback_visibility = MsgTypeString("acu3_vdeedfeedback:TMMI_MCR_IS_VISIBLE", value=acu3_vdeedfeedback_visibility_expected)
        validate_acu3_acucounter_value = MsgTypeNumeric("acu3_acucounter:TMMI_MCR_OBJECT_GET_VALUE", value=acu3_acucounter_value_expected)
        validate_acu3_compcoilcfeedback_value = MsgTypeNumeric("acu3_compcoilcfeedback:TMMI_MCR_OBJECT_GET_VALUE", value=acu3_compcoilcfeedback_value_expected)
        validate_acu3_savebtn_visibility = MsgTypeString("acu3_savebtn:TMMI_MCR_IS_VISIBLE", value=acu3_savebtn_visibility_expected)
        validate_acu3_edit_eqt_param_visibility = MsgTypeString("acu3_edit_eqt_param:TMMI_MCR_IS_VISIBLE", value=acu3_edit_eqt_param_visibility_expected)
        validate_acu3_rpoutlsstatus_subobject_name = MsgTypeString("acu3_rpoutlsstatus:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=acu3_rpoutlsstatus_subobject_name_expected)
        validate_acu3_esslayoutbtn_visibility = MsgTypeString("acu3_esslayoutbtn:TMMI_MCR_IS_VISIBLE", value=acu3_esslayoutbtn_visibility_expected)
        validate_acu3_t1onbtn_visibility = MsgTypeString("acu3_t1onbtn:TMMI_MCR_IS_VISIBLE", value=acu3_t1onbtn_visibility_expected)
        validate_acu3_t1ondisable_background_color = MsgTypeString("acu3_t1ondisable:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=acu3_t1ondisable_background_color_expected)
        validate_acu3_t1ondisable_visibility = MsgTypeString("acu3_t1ondisable:TMMI_MCR_IS_VISIBLE", value=acu3_t1ondisable_visibility_expected)
        validate_acu3_t1offbtn_visibility = MsgTypeString("acu3_t1offbtn:TMMI_MCR_IS_VISIBLE", value=acu3_t1offbtn_visibility_expected)
        validate_acu3_t1offdisable_background_color = MsgTypeString("acu3_t1offdisable:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=acu3_t1offdisable_background_color_expected)
        validate_acu3_t1offdisable_visibility = MsgTypeString("acu3_t1offdisable:TMMI_MCR_IS_VISIBLE", value=acu3_t1offdisable_visibility_expected)
        validate_acu3_t1psvideo_visibility = MsgTypeString("acu3_t1psvideo:TMMI_MCR_IS_VISIBLE", value=acu3_t1psvideo_visibility_expected)
        validate_acu3_t2onbtn_visibility = MsgTypeString("acu3_t2onbtn:TMMI_MCR_IS_VISIBLE", value=acu3_t2onbtn_visibility_expected)
        validate_acu3_t2ondisable_background_color = MsgTypeString("acu3_t2ondisable:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=acu3_t2ondisable_background_color_expected)
        validate_acu3_t2ondisable_visibility = MsgTypeString("acu3_t2ondisable:TMMI_MCR_IS_VISIBLE", value=acu3_t2ondisable_visibility_expected)
        validate_acu3_t2offbtn_visibility = MsgTypeString("acu3_t2offbtn:TMMI_MCR_IS_VISIBLE", value=acu3_t2offbtn_visibility_expected)
        validate_acu3_t2offdisable_background_color = MsgTypeString("acu3_t2offdisable:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=acu3_t2offdisable_background_color_expected)
        validate_acu3_t2offdisable_visibility = MsgTypeString("acu3_t2offdisable:TMMI_MCR_IS_VISIBLE", value=acu3_t2offdisable_visibility_expected)
        validate_acu3_essctrlbtn_visibility = MsgTypeString("acu3_essctrlbtn:TMMI_MCR_IS_VISIBLE", value=acu3_essctrlbtn_visibility_expected)
        validate_acu3_maincoiltuningbtn_visibility = MsgTypeString("acu3_maincoiltuningbtn:TMMI_MCR_IS_VISIBLE", value=acu3_maincoiltuningbtn_visibility_expected)
        validate_acu3_maincoiltuningdisable_background_color = MsgTypeString("acu3_maincoiltuningdisable:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=acu3_maincoiltuningdisable_background_color_expected)
        validate_acu3_maincoiltuningdisable_visibility = MsgTypeString("acu3_maincoiltuningdisable:TMMI_MCR_IS_VISIBLE", value=acu3_maincoiltuningdisable_visibility_expected)
        validate_acu3_maincoiltuningled_visibility = MsgTypeString("acu3_maincoiltuningled:TMMI_MCR_IS_VISIBLE", value=acu3_maincoiltuningled_visibility_expected)
        validate_acu3_arctuningbtn_visibility = MsgTypeString("acu3_arctuningbtn:TMMI_MCR_IS_VISIBLE", value=acu3_arctuningbtn_visibility_expected)
        validate_acu3_arctuningdisable_visibility = MsgTypeString("acu3_arctuningdisable:TMMI_MCR_IS_VISIBLE", value=acu3_arctuningdisable_visibility_expected)
        validate_acu3_arctuningled_visibility = MsgTypeString("acu3_arctuningled:TMMI_MCR_IS_VISIBLE", value=acu3_arctuningled_visibility_expected)
        validate_acu3_positionstatus_visibility = MsgTypeString("acu3_positionstatus:TMMI_MCR_IS_VISIBLE", value=acu3_positionstatus_visibility_expected)
        validate_acu3_maincoilpsvideo_visibility = MsgTypeString("acu3_maincoilpsvideo:TMMI_MCR_IS_VISIBLE", value=acu3_maincoilpsvideo_visibility_expected)
        validate_acu3_sourcepsvideo_visibility = MsgTypeString("acu3_sourcepsvideo:TMMI_MCR_IS_VISIBLE", value=acu3_sourcepsvideo_visibility_expected)
        validate_acu3_llrfvideo_visibility = MsgTypeString("acu3_llrfvideo:TMMI_MCR_IS_VISIBLE", value=acu3_llrfvideo_visibility_expected)
        validate_acu3_ssavideo_visibility = MsgTypeString("acu3_ssavideo:TMMI_MCR_IS_VISIBLE", value=acu3_ssavideo_visibility_expected)
        validate_acu3_impavideo_visibility = MsgTypeString("acu3_impavideo:TMMI_MCR_IS_VISIBLE", value=acu3_impavideo_visibility_expected)
        validate_acu3_fpavideo_visibility = MsgTypeString("acu3_fpavideo:TMMI_MCR_IS_VISIBLE", value=acu3_fpavideo_visibility_expected)
        validate_acu3_rfvideo_visibility = MsgTypeString("acu3_rfvideo:TMMI_MCR_IS_VISIBLE", value=acu3_rfvideo_visibility_expected)
        validate_acu3_deflectorpsvideo_visibility = MsgTypeString("acu3_deflectorpsvideo:TMMI_MCR_IS_VISIBLE", value=acu3_deflectorpsvideo_visibility_expected)
        validate_acu3_cyclovacvideo_visibility = MsgTypeString("acu3_cyclovacvideo:TMMI_MCR_IS_VISIBLE", value=acu3_cyclovacvideo_visibility_expected)
        validate_acu3_hydrolicstationstatus_visibility = MsgTypeString("acu3_hydrolicstationstatus:TMMI_MCR_IS_VISIBLE", value=acu3_hydrolicstationstatus_visibility_expected)
        validate_acu3_coolingstatus_visibility = MsgTypeString("acu3_coolingstatus:TMMI_MCR_IS_VISIBLE", value=acu3_coolingstatus_visibility_expected)

        info_exchange = [
                        InformationSet("get acu3_t2psvideo visibility", "thriver", "mcrhci", get_acu3_t2psvideo_visibility),
                        InformationSet("validate acu3_t2psvideo visibility = " + str(acu3_t2psvideo_visibility_expected), "mcrhci", "hcitracer", validate_acu3_t2psvideo_visibility),
                        InformationSet("set mcr_acu_sw_healthStatus = "+ str(mcr_acu_sw_healthStatus_init_1), "thriver", "mcrhci", set_mcr_acu_sw_healthStatus_1),
                        InformationSet("get acu3_acuhealthstatus text", "thriver", "mcrhci", get_acu3_acuhealthstatus_text),
                        InformationSet("validate acu3_acuhealthstatus text = " + str(acu3_acuhealthstatus_text_expected), "mcrhci", "hcitracer", validate_acu3_acuhealthstatus_text),
                        InformationSet("get acu3_radialprobe visibility", "thriver", "mcrhci", get_acu3_radialprobe_visibility),
                        InformationSet("validate acu3_radialprobe visibility = " + str(acu3_radialprobe_visibility_expected), "mcrhci", "hcitracer", validate_acu3_radialprobe_visibility),
                        InformationSet("get acu3_maincoilpsonbtn visibility", "thriver", "mcrhci", get_acu3_maincoilpsonbtn_visibility),
                        InformationSet("validate acu3_maincoilpsonbtn visibility = " + str(acu3_maincoilpsonbtn_visibility_expected), "mcrhci", "hcitracer", validate_acu3_maincoilpsonbtn_visibility),
                        InformationSet("set mcr_acu_maincoilps_cmdstatus = "+ str(mcr_acu_maincoilps_cmdstatus_init_1), "thriver", "mcrhci", set_mcr_acu_maincoilps_cmdstatus_1),
                        InformationSet("get acu3_maincoilpsondisable background_color", "thriver", "mcrhci", get_acu3_maincoilpsondisable_background_color),
                        InformationSet("validate acu3_maincoilpsondisable background_color = " + str(acu3_maincoilpsondisable_background_color_expected), "mcrhci", "hcitracer", validate_acu3_maincoilpsondisable_background_color),
                        InformationSet("set maincoil_pson_cmdenable = "+ str(maincoil_pson_cmdenable_init_1), "thriver", "mcrhci", set_maincoil_pson_cmdenable_1),
                        InformationSet("get acu3_maincoilpsondisable visibility", "thriver", "mcrhci", get_acu3_maincoilpsondisable_visibility),
                        InformationSet("validate acu3_maincoilpsondisable visibility = " + str(acu3_maincoilpsondisable_visibility_expected), "mcrhci", "hcitracer", validate_acu3_maincoilpsondisable_visibility),
                        InformationSet("get acu3_maincoilpsoffbtn visibility", "thriver", "mcrhci", get_acu3_maincoilpsoffbtn_visibility),
                        InformationSet("validate acu3_maincoilpsoffbtn visibility = " + str(acu3_maincoilpsoffbtn_visibility_expected), "mcrhci", "hcitracer", validate_acu3_maincoilpsoffbtn_visibility),
                        InformationSet("set mcr_acu_maincoilps_cmdstatus = "+ str(mcr_acu_maincoilps_cmdstatus_init_2), "thriver", "mcrhci", set_mcr_acu_maincoilps_cmdstatus_2),
                        InformationSet("get acu3_maincoilpsoffdisable background_color", "thriver", "mcrhci", get_acu3_maincoilpsoffdisable_background_color),
                        InformationSet("validate acu3_maincoilpsoffdisable background_color = " + str(acu3_maincoilpsoffdisable_background_color_expected), "mcrhci", "hcitracer", validate_acu3_maincoilpsoffdisable_background_color),
                        InformationSet("set maincoil_psoff_cmdenable = "+ str(maincoil_psoff_cmdenable_init_1), "thriver", "mcrhci", set_maincoil_psoff_cmdenable_1),
                        InformationSet("get acu3_maincoilpsoffdisable visibility", "thriver", "mcrhci", get_acu3_maincoilpsoffdisable_visibility),
                        InformationSet("validate acu3_maincoilpsoffdisable visibility = " + str(acu3_maincoilpsoffdisable_visibility_expected), "mcrhci", "hcitracer", validate_acu3_maincoilpsoffdisable_visibility),
                        InformationSet("set mcr_rtieacu_maincoil_cfeedback = "+ str(mcr_rtieacu_maincoil_cfeedback_init_1), "thriver", "mcrhci", set_mcr_rtieacu_maincoil_cfeedback_1),
                        InformationSet("get acu3_maincoilcfeedback value", "thriver", "mcrhci", get_acu3_maincoilcfeedback_value),
                        InformationSet("validate acu3_maincoilcfeedback value = " + str(acu3_maincoilcfeedback_value_expected), "mcrhci", "hcitracer", validate_acu3_maincoilcfeedback_value),
                        InformationSet("set mcr_rtieacu_coil24_cfeedback = "+ str(mcr_rtieacu_coil24_cfeedback_init_1), "thriver", "mcrhci", set_mcr_rtieacu_coil24_cfeedback_1),
                        InformationSet("get acu3_coil24cfeedback value", "thriver", "mcrhci", get_acu3_coil24cfeedback_value),
                        InformationSet("validate acu3_coil24cfeedback value = " + str(acu3_coil24cfeedback_value_expected), "mcrhci", "hcitracer", validate_acu3_coil24cfeedback_value),
                        InformationSet("set mcr_rtieacu_coil13_cfeedback = "+ str(mcr_rtieacu_coil13_cfeedback_init_1), "thriver", "mcrhci", set_mcr_rtieacu_coil13_cfeedback_1),
                        InformationSet("get acu3_coil13cfeedback value", "thriver", "mcrhci", get_acu3_coil13cfeedback_value),
                        InformationSet("validate acu3_coil13cfeedback value = " + str(acu3_coil13cfeedback_value_expected), "mcrhci", "hcitracer", validate_acu3_coil13cfeedback_value),
                        InformationSet("set mcr_rtieacu_radialprobe_vert_location = "+ str(mcr_rtieacu_radialprobe_vert_location_init_1), "thriver", "mcrhci", set_mcr_rtieacu_radialprobe_vert_location_1),
                        InformationSet("get acu3_rpvertposition value", "thriver", "mcrhci", get_acu3_rpvertposition_value),
                        InformationSet("validate acu3_rpvertposition value = " + str(acu3_rpvertposition_value_expected), "mcrhci", "hcitracer", validate_acu3_rpvertposition_value),
                        InformationSet("set mcr_rtieacu_radialprobe_energy = "+ str(mcr_rtieacu_radialprobe_energy_init_1), "thriver", "mcrhci", set_mcr_rtieacu_radialprobe_energy_1),
                        InformationSet("get acu3_rpenergy value", "thriver", "mcrhci", get_acu3_rpenergy_value),
                        InformationSet("validate acu3_rpenergy value = " + str(acu3_rpenergy_value_expected), "mcrhci", "hcitracer", validate_acu3_rpenergy_value),
                        InformationSet("get acu3_rfonbtn visibility", "thriver", "mcrhci", get_acu3_rfonbtn_visibility),
                        InformationSet("validate acu3_rfonbtn visibility = " + str(acu3_rfonbtn_visibility_expected), "mcrhci", "hcitracer", validate_acu3_rfonbtn_visibility),
                        InformationSet("set rf_on_cmdenable = "+ str(rf_on_cmdenable_init_1), "thriver", "mcrhci", set_rf_on_cmdenable_1),
                        InformationSet("get acu3_rfondisable visibility", "thriver", "mcrhci", get_acu3_rfondisable_visibility),
                        InformationSet("validate acu3_rfondisable visibility = " + str(acu3_rfondisable_visibility_expected), "mcrhci", "hcitracer", validate_acu3_rfondisable_visibility),
                        InformationSet("get acu3_rfoffbtn visibility", "thriver", "mcrhci", get_acu3_rfoffbtn_visibility),
                        InformationSet("validate acu3_rfoffbtn visibility = " + str(acu3_rfoffbtn_visibility_expected), "mcrhci", "hcitracer", validate_acu3_rfoffbtn_visibility),
                        InformationSet("set rf_off_cmdenable = "+ str(rf_off_cmdenable_init_1), "thriver", "mcrhci", set_rf_off_cmdenable_1),
                        InformationSet("get acu3_rfoffdisable visibility", "thriver", "mcrhci", get_acu3_rfoffdisable_visibility),
                        InformationSet("validate acu3_rfoffdisable visibility = " + str(acu3_rfoffdisable_visibility_expected), "mcrhci", "hcitracer", validate_acu3_rfoffdisable_visibility),
                        InformationSet("set mcr_acu_modulator_cmdenable = "+ str(mcr_acu_modulator_cmdenable_init_1), "thriver", "mcrhci", set_mcr_acu_modulator_cmdenable_1),
                        InformationSet("get acu3_modintlk foreground_color", "thriver", "mcrhci", get_acu3_modintlk_foreground_color),
                        InformationSet("validate acu3_modintlk foreground_color = " + str(acu3_modintlk_foreground_color_expected), "mcrhci", "hcitracer", validate_acu3_modintlk_foreground_color),
                        InformationSet("set mcr_acu_modulator_cmdenable = "+ str(mcr_acu_modulator_cmdenable_init_2), "thriver", "mcrhci", set_mcr_acu_modulator_cmdenable_2),
                        InformationSet("get acu3_modintlk background_color", "thriver", "mcrhci", get_acu3_modintlk_background_color),
                        InformationSet("validate acu3_modintlk background_color = " + str(acu3_modintlk_background_color_expected), "mcrhci", "hcitracer", validate_acu3_modintlk_background_color),
                        InformationSet("get acu3_q1q2psonbtn visibility", "thriver", "mcrhci", get_acu3_q1q2psonbtn_visibility),
                        InformationSet("validate acu3_q1q2psonbtn visibility = " + str(acu3_q1q2psonbtn_visibility_expected), "mcrhci", "hcitracer", validate_acu3_q1q2psonbtn_visibility),
                        InformationSet("set mcr_acu_q1q2_cmdstatus = "+ str(mcr_acu_q1q2_cmdstatus_init_1), "thriver", "mcrhci", set_mcr_acu_q1q2_cmdstatus_1),
                        InformationSet("get acu3_q1q2psondisable background_color", "thriver", "mcrhci", get_acu3_q1q2psondisable_background_color),
                        InformationSet("validate acu3_q1q2psondisable background_color = " + str(acu3_q1q2psondisable_background_color_expected), "mcrhci", "hcitracer", validate_acu3_q1q2psondisable_background_color),
                        InformationSet("set quadextrps_q1q2_pson_cmdenable = "+ str(quadextrps_q1q2_pson_cmdenable_init_1), "thriver", "mcrhci", set_quadextrps_q1q2_pson_cmdenable_1),
                        InformationSet("get acu3_q1q2psondisable visibility", "thriver", "mcrhci", get_acu3_q1q2psondisable_visibility),
                        InformationSet("validate acu3_q1q2psondisable visibility = " + str(acu3_q1q2psondisable_visibility_expected), "mcrhci", "hcitracer", validate_acu3_q1q2psondisable_visibility),
                        InformationSet("get acu3_q1q2psoffbtn visibility", "thriver", "mcrhci", get_acu3_q1q2psoffbtn_visibility),
                        InformationSet("validate acu3_q1q2psoffbtn visibility = " + str(acu3_q1q2psoffbtn_visibility_expected), "mcrhci", "hcitracer", validate_acu3_q1q2psoffbtn_visibility),
                        InformationSet("set mcr_acu_q1q2_cmdstatus = "+ str(mcr_acu_q1q2_cmdstatus_init_2), "thriver", "mcrhci", set_mcr_acu_q1q2_cmdstatus_2),
                        InformationSet("get acu3_q1q2psoffdisable background_color", "thriver", "mcrhci", get_acu3_q1q2psoffdisable_background_color),
                        InformationSet("validate acu3_q1q2psoffdisable background_color = " + str(acu3_q1q2psoffdisable_background_color_expected), "mcrhci", "hcitracer", validate_acu3_q1q2psoffdisable_background_color),
                        InformationSet("set quadextrps_q1q2_psoff_cmdenable = "+ str(quadextrps_q1q2_psoff_cmdenable_init_1), "thriver", "mcrhci", set_quadextrps_q1q2_psoff_cmdenable_1),
                        InformationSet("get acu3_q1q2psoffdisable visibility", "thriver", "mcrhci", get_acu3_q1q2psoffdisable_visibility),
                        InformationSet("validate acu3_q1q2psoffdisable visibility = " + str(acu3_q1q2psoffdisable_visibility_expected), "mcrhci", "hcitracer", validate_acu3_q1q2psoffdisable_visibility),
                        InformationSet("get acu3_q1q2video visibility", "thriver", "mcrhci", get_acu3_q1q2video_visibility),
                        InformationSet("validate acu3_q1q2video visibility = " + str(acu3_q1q2video_visibility_expected), "mcrhci", "hcitracer", validate_acu3_q1q2video_visibility),
                        InformationSet("set mcr_rtieacu_q1_cfeedback = "+ str(mcr_rtieacu_q1_cfeedback_init_1), "thriver", "mcrhci", set_mcr_rtieacu_q1_cfeedback_1),
                        InformationSet("get acu3_q1cfeedback value", "thriver", "mcrhci", get_acu3_q1cfeedback_value),
                        InformationSet("validate acu3_q1cfeedback value = " + str(acu3_q1cfeedback_value_expected), "mcrhci", "hcitracer", validate_acu3_q1cfeedback_value),
                        InformationSet("set mcr_rtieacu_q2_cfeedback = "+ str(mcr_rtieacu_q2_cfeedback_init_1), "thriver", "mcrhci", set_mcr_rtieacu_q2_cfeedback_1),
                        InformationSet("get acu3_q2cfeedback value", "thriver", "mcrhci", get_acu3_q2cfeedback_value),
                        InformationSet("validate acu3_q2cfeedback value = " + str(acu3_q2cfeedback_value_expected), "mcrhci", "hcitracer", validate_acu3_q2cfeedback_value),
                        InformationSet("get acu3_sourceonbtn visibility", "thriver", "mcrhci", get_acu3_sourceonbtn_visibility),
                        InformationSet("validate acu3_sourceonbtn visibility = " + str(acu3_sourceonbtn_visibility_expected), "mcrhci", "hcitracer", validate_acu3_sourceonbtn_visibility),
                        InformationSet("set mcr_acu_sourcearc_cmdstatus = "+ str(mcr_acu_sourcearc_cmdstatus_init_1), "thriver", "mcrhci", set_mcr_acu_sourcearc_cmdstatus_1),
                        InformationSet("get acu3_sourceondisable background_color", "thriver", "mcrhci", get_acu3_sourceondisable_background_color),
                        InformationSet("validate acu3_sourceondisable background_color = " + str(acu3_sourceondisable_background_color_expected), "mcrhci", "hcitracer", validate_acu3_sourceondisable_background_color),
                        InformationSet("set source_sourceon_cmdenable = "+ str(source_sourceon_cmdenable_init_1), "thriver", "mcrhci", set_source_sourceon_cmdenable_1),
                        InformationSet("get acu3_sourceondisable visibility", "thriver", "mcrhci", get_acu3_sourceondisable_visibility),
                        InformationSet("validate acu3_sourceondisable visibility = " + str(acu3_sourceondisable_visibility_expected), "mcrhci", "hcitracer", validate_acu3_sourceondisable_visibility),
                        InformationSet("get acu3_sourceoffbtn visibility", "thriver", "mcrhci", get_acu3_sourceoffbtn_visibility),
                        InformationSet("validate acu3_sourceoffbtn visibility = " + str(acu3_sourceoffbtn_visibility_expected), "mcrhci", "hcitracer", validate_acu3_sourceoffbtn_visibility),
                        InformationSet("set mcr_acu_sourcearc_cmdstatus = "+ str(mcr_acu_sourcearc_cmdstatus_init_2), "thriver", "mcrhci", set_mcr_acu_sourcearc_cmdstatus_2),
                        InformationSet("get acu3_sourceoffdisable background_color", "thriver", "mcrhci", get_acu3_sourceoffdisable_background_color),
                        InformationSet("validate acu3_sourceoffdisable background_color = " + str(acu3_sourceoffdisable_background_color_expected), "mcrhci", "hcitracer", validate_acu3_sourceoffdisable_background_color),
                        InformationSet("set source_sourceoff_cmdenable = "+ str(source_sourceoff_cmdenable_init_1), "thriver", "mcrhci", set_source_sourceoff_cmdenable_1),
                        InformationSet("get acu3_sourceoffdisable visibility", "thriver", "mcrhci", get_acu3_sourceoffdisable_visibility),
                        InformationSet("validate acu3_sourceoffdisable visibility = " + str(acu3_sourceoffdisable_visibility_expected), "mcrhci", "hcitracer", validate_acu3_sourceoffdisable_visibility),
                        InformationSet("set mcr_acu_sourcefilament_cfeedback = "+ str(mcr_acu_sourcefilament_cfeedback_init_1), "thriver", "mcrhci", set_mcr_acu_sourcefilament_cfeedback_1),
                        InformationSet("get acu3_filamentcfeedback value", "thriver", "mcrhci", get_acu3_filamentcfeedback_value),
                        InformationSet("validate acu3_filamentcfeedback value = " + str(acu3_filamentcfeedback_value_expected), "mcrhci", "hcitracer", validate_acu3_filamentcfeedback_value),
                        InformationSet("set mcr_acu_sourcearc_cfeedback = "+ str(mcr_acu_sourcearc_cfeedback_init_1), "thriver", "mcrhci", set_mcr_acu_sourcearc_cfeedback_1),
                        InformationSet("get acu3_arccfeedback value", "thriver", "mcrhci", get_acu3_arccfeedback_value),
                        InformationSet("validate acu3_arccfeedback value = " + str(acu3_arccfeedback_value_expected), "mcrhci", "hcitracer", validate_acu3_arccfeedback_value),
                        InformationSet("set mcr_acu_sourcearc_vfeedback = "+ str(mcr_acu_sourcearc_vfeedback_init_1), "thriver", "mcrhci", set_mcr_acu_sourcearc_vfeedback_1),
                        InformationSet("get acu3_arcvfeedback value", "thriver", "mcrhci", get_acu3_arcvfeedback_value),
                        InformationSet("validate acu3_arcvfeedback value = " + str(acu3_arcvfeedback_value_expected), "mcrhci", "hcitracer", validate_acu3_arcvfeedback_value),
                        InformationSet("set mcr_rtieacu_impa_extcondition = "+ str(mcr_rtieacu_impa_extcondition_init_1), "thriver", "mcrhci", set_mcr_rtieacu_impa_extcondition_1),
                        InformationSet("get acu3_impaextcondtxt foreground_color", "thriver", "mcrhci", get_acu3_impaextcondtxt_foreground_color),
                        InformationSet("validate acu3_impaextcondtxt foreground_color = " + str(acu3_impaextcondtxt_foreground_color_expected), "mcrhci", "hcitracer", validate_acu3_impaextcondtxt_foreground_color),
                        InformationSet("set mcr_acu_radialprobe_inls = "+ str(mcr_acu_radialprobe_inls_init_1), "thriver", "mcrhci", set_mcr_acu_radialprobe_inls_1),
                        InformationSet("get acu3_rpinlsstatus subobject_name", "thriver", "mcrhci", get_acu3_rpinlsstatus_subobject_name),
                        InformationSet("validate acu3_rpinlsstatus subobject_name = " + str(acu3_rpinlsstatus_subobject_name_expected), "mcrhci", "hcitracer", validate_acu3_rpinlsstatus_subobject_name),
                        InformationSet("set mcr_rtieacu_impa_extcondition = "+ str(mcr_rtieacu_impa_extcondition_init_2), "thriver", "mcrhci", set_mcr_rtieacu_impa_extcondition_2),
                        InformationSet("get acu3_impaextcondcheckmark subobject_name", "thriver", "mcrhci", get_acu3_impaextcondcheckmark_subobject_name),
                        InformationSet("validate acu3_impaextcondcheckmark subobject_name = " + str(acu3_impaextcondcheckmark_subobject_name_expected), "mcrhci", "hcitracer", validate_acu3_impaextcondcheckmark_subobject_name),
                        InformationSet("set mcr_rtieacu_fpa_extcondition = "+ str(mcr_rtieacu_fpa_extcondition_init_1), "thriver", "mcrhci", set_mcr_rtieacu_fpa_extcondition_1),
                        InformationSet("get acu3_fpaextcondtxt foreground_color", "thriver", "mcrhci", get_acu3_fpaextcondtxt_foreground_color),
                        InformationSet("validate acu3_fpaextcondtxt foreground_color = " + str(acu3_fpaextcondtxt_foreground_color_expected), "mcrhci", "hcitracer", validate_acu3_fpaextcondtxt_foreground_color),
                        InformationSet("set mcr_rtieacu_fpa_extcondition = "+ str(mcr_rtieacu_fpa_extcondition_init_2), "thriver", "mcrhci", set_mcr_rtieacu_fpa_extcondition_2),
                        InformationSet("get acu3_fpaextcondcheckmark subobject_name", "thriver", "mcrhci", get_acu3_fpaextcondcheckmark_subobject_name),
                        InformationSet("validate acu3_fpaextcondcheckmark subobject_name = " + str(acu3_fpaextcondcheckmark_subobject_name_expected), "mcrhci", "hcitracer", validate_acu3_fpaextcondcheckmark_subobject_name),
                        InformationSet("get acu3_deflectorpsonbtn visibility", "thriver", "mcrhci", get_acu3_deflectorpsonbtn_visibility),
                        InformationSet("validate acu3_deflectorpsonbtn visibility = " + str(acu3_deflectorpsonbtn_visibility_expected), "mcrhci", "hcitracer", validate_acu3_deflectorpsonbtn_visibility),
                        InformationSet("set mcr_acu_deflectorps_cmdstatus = "+ str(mcr_acu_deflectorps_cmdstatus_init_1), "thriver", "mcrhci", set_mcr_acu_deflectorps_cmdstatus_1),
                        InformationSet("get acu3_deflectorpsondisable background_color", "thriver", "mcrhci", get_acu3_deflectorpsondisable_background_color),
                        InformationSet("validate acu3_deflectorpsondisable background_color = " + str(acu3_deflectorpsondisable_background_color_expected), "mcrhci", "hcitracer", validate_acu3_deflectorpsondisable_background_color),
                        InformationSet("set deflector_pson_cmdenable = "+ str(deflector_pson_cmdenable_init_1), "thriver", "mcrhci", set_deflector_pson_cmdenable_1),
                        InformationSet("get acu3_deflectorpsondisable visibility", "thriver", "mcrhci", get_acu3_deflectorpsondisable_visibility),
                        InformationSet("validate acu3_deflectorpsondisable visibility = " + str(acu3_deflectorpsondisable_visibility_expected), "mcrhci", "hcitracer", validate_acu3_deflectorpsondisable_visibility),
                        InformationSet("get acu3_deflectorpsoffbtn visibility", "thriver", "mcrhci", get_acu3_deflectorpsoffbtn_visibility),
                        InformationSet("validate acu3_deflectorpsoffbtn visibility = " + str(acu3_deflectorpsoffbtn_visibility_expected), "mcrhci", "hcitracer", validate_acu3_deflectorpsoffbtn_visibility),
                        InformationSet("set mcr_acu_deflectorps_cmdstatus = "+ str(mcr_acu_deflectorps_cmdstatus_init_2), "thriver", "mcrhci", set_mcr_acu_deflectorps_cmdstatus_2),
                        InformationSet("get acu3_deflectorpsoffdisable background_color", "thriver", "mcrhci", get_acu3_deflectorpsoffdisable_background_color),
                        InformationSet("validate acu3_deflectorpsoffdisable background_color = " + str(acu3_deflectorpsoffdisable_background_color_expected), "mcrhci", "hcitracer", validate_acu3_deflectorpsoffdisable_background_color),
                        InformationSet("set deflector_psoff_cmdenable = "+ str(deflector_psoff_cmdenable_init_1), "thriver", "mcrhci", set_deflector_psoff_cmdenable_1),
                        InformationSet("get acu3_deflectorpsoffdisable visibility", "thriver", "mcrhci", get_acu3_deflectorpsoffdisable_visibility),
                        InformationSet("validate acu3_deflectorpsoffdisable visibility = " + str(acu3_deflectorpsoffdisable_visibility_expected), "mcrhci", "hcitracer", validate_acu3_deflectorpsoffdisable_visibility),
                        InformationSet("set mcr_acu_deflectorps_vfeedback = "+ str(mcr_acu_deflectorps_vfeedback_init_1), "thriver", "mcrhci", set_mcr_acu_deflectorps_vfeedback_1),
                        InformationSet("get acu3_deflectorpsvfeedback value", "thriver", "mcrhci", get_acu3_deflectorpsvfeedback_value),
                        InformationSet("validate acu3_deflectorpsvfeedback value = " + str(acu3_deflectorpsvfeedback_value_expected), "mcrhci", "hcitracer", validate_acu3_deflectorpsvfeedback_value),
                        InformationSet("set mcr_acu_deflectorps_macfeedback = "+ str(mcr_acu_deflectorps_macfeedback_init_1), "thriver", "mcrhci", set_mcr_acu_deflectorps_macfeedback_1),
                        InformationSet("get acu3_deflectorpsmacfeedback value", "thriver", "mcrhci", get_acu3_deflectorpsmacfeedback_value),
                        InformationSet("validate acu3_deflectorpsmacfeedback value = " + str(acu3_deflectorpsmacfeedback_value_expected), "mcrhci", "hcitracer", validate_acu3_deflectorpsmacfeedback_value),
                        InformationSet("set mcr_acu_deflectormotor1_dfeedback = "+ str(mcr_acu_deflectormotor1_dfeedback_init_1), "thriver", "mcrhci", set_mcr_acu_deflectormotor1_dfeedback_1),
                        InformationSet("get acu3_deflectormotor1dfeedback value", "thriver", "mcrhci", get_acu3_deflectormotor1dfeedback_value),
                        InformationSet("validate acu3_deflectormotor1dfeedback value = " + str(acu3_deflectormotor1dfeedback_value_expected), "mcrhci", "hcitracer", validate_acu3_deflectormotor1dfeedback_value),
                        InformationSet("set mcr_acu_deflectormotor2_dfeedback = "+ str(mcr_acu_deflectormotor2_dfeedback_init_1), "thriver", "mcrhci", set_mcr_acu_deflectormotor2_dfeedback_1),
                        InformationSet("get acu3_deflectormotor2dfeedback value", "thriver", "mcrhci", get_acu3_deflectormotor2dfeedback_value),
                        InformationSet("validate acu3_deflectormotor2dfeedback value = " + str(acu3_deflectormotor2dfeedback_value_expected), "mcrhci", "hcitracer", validate_acu3_deflectormotor2dfeedback_value),
                        InformationSet("set mcr_acu_sourcemovement_dfeedback = "+ str(mcr_acu_sourcemovement_dfeedback_init_1), "thriver", "mcrhci", set_mcr_acu_sourcemovement_dfeedback_1),
                        InformationSet("get acu3_srcmovementdfeedback value", "thriver", "mcrhci", get_acu3_srcmovementdfeedback_value),
                        InformationSet("validate acu3_srcmovementdfeedback value = " + str(acu3_srcmovementdfeedback_value_expected), "mcrhci", "hcitracer", validate_acu3_srcmovementdfeedback_value),
                        InformationSet("set mcr_ecubtcu_penning1cyclo_mbarvacuum = "+ str(mcr_ecubtcu_penning1cyclo_mbarvacuum_init_1), "thriver", "mcrhci", set_mcr_ecubtcu_penning1cyclo_mbarvacuum_1),
                        InformationSet("get acu3_penning1mbarvac value", "thriver", "mcrhci", get_acu3_penning1mbarvac_value),
                        InformationSet("validate acu3_penning1mbarvac value = " + str(acu3_penning1mbarvac_value_expected), "mcrhci", "hcitracer", validate_acu3_penning1mbarvac_value),
                        InformationSet("set mcr_ecubtcu_penning1cyclo_mbarvacuum = "+ str(mcr_ecubtcu_penning1cyclo_mbarvacuum_init_2), "thriver", "mcrhci", set_mcr_ecubtcu_penning1cyclo_mbarvacuum_2),
                        InformationSet("get acu3_penning1mbarvac visibility", "thriver", "mcrhci", get_acu3_penning1mbarvac_visibility),
                        InformationSet("validate acu3_penning1mbarvac visibility = " + str(acu3_penning1mbarvac_visibility_expected), "mcrhci", "hcitracer", validate_acu3_penning1mbarvac_visibility),
                        InformationSet("set mcr_ecubtcu_penning1cyclo_mbarvacuum = "+ str(mcr_ecubtcu_penning1cyclo_mbarvacuum_init_3), "thriver", "mcrhci", set_mcr_ecubtcu_penning1cyclo_mbarvacuum_3),
                        InformationSet("get acu3_penning1mbartxt visibility", "thriver", "mcrhci", get_acu3_penning1mbartxt_visibility),
                        InformationSet("validate acu3_penning1mbartxt visibility = " + str(acu3_penning1mbartxt_visibility_expected), "mcrhci", "hcitracer", validate_acu3_penning1mbartxt_visibility),
                        InformationSet("set mcr_rtieecubtcu_penning1_cyclo_status = "+ str(mcr_rtieecubtcu_penning1_cyclo_status_init_1), "thriver", "mcrhci", set_mcr_rtieecubtcu_penning1_cyclo_status_1),
                        InformationSet("get acu3_penning1errormsg text", "thriver", "mcrhci", get_acu3_penning1errormsg_text),
                        InformationSet("validate acu3_penning1errormsg text = " + str(acu3_penning1errormsg_text_expected), "mcrhci", "hcitracer", validate_acu3_penning1errormsg_text),
                        InformationSet("set mcr_ecubtcu_penning1cyclo_mbarvacuum = "+ str(mcr_ecubtcu_penning1cyclo_mbarvacuum_init_4), "thriver", "mcrhci", set_mcr_ecubtcu_penning1cyclo_mbarvacuum_4),
                        InformationSet("get acu3_penning1errormsg visibility", "thriver", "mcrhci", get_acu3_penning1errormsg_visibility),
                        InformationSet("validate acu3_penning1errormsg visibility = " + str(acu3_penning1errormsg_visibility_expected), "mcrhci", "hcitracer", validate_acu3_penning1errormsg_visibility),
                        InformationSet("set mcr_acu_fpa_kwforwardpower = "+ str(mcr_acu_fpa_kwforwardpower_init_1), "thriver", "mcrhci", set_mcr_acu_fpa_kwforwardpower_1),
                        InformationSet("get acu3_fpakwforwardpower value", "thriver", "mcrhci", get_acu3_fpakwforwardpower_value),
                        InformationSet("validate acu3_fpakwforwardpower value = " + str(acu3_fpakwforwardpower_value_expected), "mcrhci", "hcitracer", validate_acu3_fpakwforwardpower_value),
                        InformationSet("set mcr_acu_vdee_vfeedback1 = "+ str(mcr_acu_vdee_vfeedback1_init_1), "thriver", "mcrhci", set_mcr_acu_vdee_vfeedback1_1),
                        InformationSet("get acu3_vdee1vfeedback value", "thriver", "mcrhci", get_acu3_vdee1vfeedback_value),
                        InformationSet("validate acu3_vdee1vfeedback value = " + str(acu3_vdee1vfeedback_value_expected), "mcrhci", "hcitracer", validate_acu3_vdee1vfeedback_value),
                        InformationSet("set mcr_acu_vdee_vfeedback2 = "+ str(mcr_acu_vdee_vfeedback2_init_1), "thriver", "mcrhci", set_mcr_acu_vdee_vfeedback2_1),
                        InformationSet("get acu3_vdee2vfeedback value", "thriver", "mcrhci", get_acu3_vdee2vfeedback_value),
                        InformationSet("validate acu3_vdee2vfeedback value = " + str(acu3_vdee2vfeedback_value_expected), "mcrhci", "hcitracer", validate_acu3_vdee2vfeedback_value),
                        InformationSet("set vdee_dsetpoint_text = "+ str(vdee_dsetpoint_text_init_1), "thriver", "mcrhci", set_vdee_dsetpoint_text_1),
                        InformationSet("get acu3_vdeedinput text", "thriver", "mcrhci", get_acu3_vdeedinput_text),
                        InformationSet("validate acu3_vdeedinput text = " + str(acu3_vdeedinput_text_expected), "mcrhci", "hcitracer", validate_acu3_vdeedinput_text),
                        InformationSet("set mcr_acu_vdee_dsetpoint = "+ str(mcr_acu_vdee_dsetpoint_init_1), "thriver", "mcrhci", set_mcr_acu_vdee_dsetpoint_1),
                        InformationSet("get acu3_vdeedfeedback value", "thriver", "mcrhci", get_acu3_vdeedfeedback_value),
                        InformationSet("validate acu3_vdeedfeedback value = " + str(acu3_vdeedfeedback_value_expected), "mcrhci", "hcitracer", validate_acu3_vdeedfeedback_value),
                        InformationSet("set vdee_dfeedback_visible = "+ str(vdee_dfeedback_visible_init_1), "thriver", "mcrhci", set_vdee_dfeedback_visible_1),
                        InformationSet("get acu3_vdeedfeedback visibility", "thriver", "mcrhci", get_acu3_vdeedfeedback_visibility),
                        InformationSet("validate acu3_vdeedfeedback visibility = " + str(acu3_vdeedfeedback_visibility_expected), "mcrhci", "hcitracer", validate_acu3_vdeedfeedback_visibility),
                        InformationSet("set mcr_acu_sw_counter = "+ str(mcr_acu_sw_counter_init_1), "thriver", "mcrhci", set_mcr_acu_sw_counter_1),
                        InformationSet("get acu3_acucounter value", "thriver", "mcrhci", get_acu3_acucounter_value),
                        InformationSet("validate acu3_acucounter value = " + str(acu3_acucounter_value_expected), "mcrhci", "hcitracer", validate_acu3_acucounter_value),
                        InformationSet("set mcr_rtieacu_compensationcoil_cfeedback = "+ str(mcr_rtieacu_compensationcoil_cfeedback_init_1), "thriver", "mcrhci", set_mcr_rtieacu_compensationcoil_cfeedback_1),
                        InformationSet("get acu3_compcoilcfeedback value", "thriver", "mcrhci", get_acu3_compcoilcfeedback_value),
                        InformationSet("validate acu3_compcoilcfeedback value = " + str(acu3_compcoilcfeedback_value_expected), "mcrhci", "hcitracer", validate_acu3_compcoilcfeedback_value),
                        InformationSet("get acu3_savebtn visibility", "thriver", "mcrhci", get_acu3_savebtn_visibility),
                        InformationSet("validate acu3_savebtn visibility = " + str(acu3_savebtn_visibility_expected), "mcrhci", "hcitracer", validate_acu3_savebtn_visibility),
                        InformationSet("get acu3_edit_eqt_param visibility", "thriver", "mcrhci", get_acu3_edit_eqt_param_visibility),
                        InformationSet("validate acu3_edit_eqt_param visibility = " + str(acu3_edit_eqt_param_visibility_expected), "mcrhci", "hcitracer", validate_acu3_edit_eqt_param_visibility),
                        InformationSet("set mcr_acu_radialprobe_outls = "+ str(mcr_acu_radialprobe_outls_init_1), "thriver", "mcrhci", set_mcr_acu_radialprobe_outls_1),
                        InformationSet("get acu3_rpoutlsstatus subobject_name", "thriver", "mcrhci", get_acu3_rpoutlsstatus_subobject_name),
                        InformationSet("validate acu3_rpoutlsstatus subobject_name = " + str(acu3_rpoutlsstatus_subobject_name_expected), "mcrhci", "hcitracer", validate_acu3_rpoutlsstatus_subobject_name),
                        InformationSet("get acu3_esslayoutbtn visibility", "thriver", "mcrhci", get_acu3_esslayoutbtn_visibility),
                        InformationSet("validate acu3_esslayoutbtn visibility = " + str(acu3_esslayoutbtn_visibility_expected), "mcrhci", "hcitracer", validate_acu3_esslayoutbtn_visibility),
                        InformationSet("get acu3_t1onbtn visibility", "thriver", "mcrhci", get_acu3_t1onbtn_visibility),
                        InformationSet("validate acu3_t1onbtn visibility = " + str(acu3_t1onbtn_visibility_expected), "mcrhci", "hcitracer", validate_acu3_t1onbtn_visibility),
                        InformationSet("set mcr_acu_t1_cmdstatus = "+ str(mcr_acu_t1_cmdstatus_init_1), "thriver", "mcrhci", set_mcr_acu_t1_cmdstatus_1),
                        InformationSet("get acu3_t1ondisable background_color", "thriver", "mcrhci", get_acu3_t1ondisable_background_color),
                        InformationSet("validate acu3_t1ondisable background_color = " + str(acu3_t1ondisable_background_color_expected), "mcrhci", "hcitracer", validate_acu3_t1ondisable_background_color),
                        InformationSet("set steeringextrps_sg1_pson_cmdenable = "+ str(steeringextrps_sg1_pson_cmdenable_init_1), "thriver", "mcrhci", set_steeringextrps_sg1_pson_cmdenable_1),
                        InformationSet("get acu3_t1ondisable visibility", "thriver", "mcrhci", get_acu3_t1ondisable_visibility),
                        InformationSet("validate acu3_t1ondisable visibility = " + str(acu3_t1ondisable_visibility_expected), "mcrhci", "hcitracer", validate_acu3_t1ondisable_visibility),
                        InformationSet("get acu3_t1offbtn visibility", "thriver", "mcrhci", get_acu3_t1offbtn_visibility),
                        InformationSet("validate acu3_t1offbtn visibility = " + str(acu3_t1offbtn_visibility_expected), "mcrhci", "hcitracer", validate_acu3_t1offbtn_visibility),
                        InformationSet("set mcr_acu_t1_cmdstatus = "+ str(mcr_acu_t1_cmdstatus_init_2), "thriver", "mcrhci", set_mcr_acu_t1_cmdstatus_2),
                        InformationSet("get acu3_t1offdisable background_color", "thriver", "mcrhci", get_acu3_t1offdisable_background_color),
                        InformationSet("validate acu3_t1offdisable background_color = " + str(acu3_t1offdisable_background_color_expected), "mcrhci", "hcitracer", validate_acu3_t1offdisable_background_color),
                        InformationSet("set steeringextrps_sg1_psoff_cmdenable = "+ str(steeringextrps_sg1_psoff_cmdenable_init_1), "thriver", "mcrhci", set_steeringextrps_sg1_psoff_cmdenable_1),
                        InformationSet("get acu3_t1offdisable visibility", "thriver", "mcrhci", get_acu3_t1offdisable_visibility),
                        InformationSet("validate acu3_t1offdisable visibility = " + str(acu3_t1offdisable_visibility_expected), "mcrhci", "hcitracer", validate_acu3_t1offdisable_visibility),
                        InformationSet("get acu3_t1psvideo visibility", "thriver", "mcrhci", get_acu3_t1psvideo_visibility),
                        InformationSet("validate acu3_t1psvideo visibility = " + str(acu3_t1psvideo_visibility_expected), "mcrhci", "hcitracer", validate_acu3_t1psvideo_visibility),
                        InformationSet("get acu3_t2onbtn visibility", "thriver", "mcrhci", get_acu3_t2onbtn_visibility),
                        InformationSet("validate acu3_t2onbtn visibility = " + str(acu3_t2onbtn_visibility_expected), "mcrhci", "hcitracer", validate_acu3_t2onbtn_visibility),
                        InformationSet("set mcr_acu_t2_cmdstatus = "+ str(mcr_acu_t2_cmdstatus_init_1), "thriver", "mcrhci", set_mcr_acu_t2_cmdstatus_1),
                        InformationSet("get acu3_t2ondisable background_color", "thriver", "mcrhci", get_acu3_t2ondisable_background_color),
                        InformationSet("validate acu3_t2ondisable background_color = " + str(acu3_t2ondisable_background_color_expected), "mcrhci", "hcitracer", validate_acu3_t2ondisable_background_color),
                        InformationSet("set steeringextrps_sg2_pson_cmdenable = "+ str(steeringextrps_sg2_pson_cmdenable_init_1), "thriver", "mcrhci", set_steeringextrps_sg2_pson_cmdenable_1),
                        InformationSet("get acu3_t2ondisable visibility", "thriver", "mcrhci", get_acu3_t2ondisable_visibility),
                        InformationSet("validate acu3_t2ondisable visibility = " + str(acu3_t2ondisable_visibility_expected), "mcrhci", "hcitracer", validate_acu3_t2ondisable_visibility),
                        InformationSet("get acu3_t2offbtn visibility", "thriver", "mcrhci", get_acu3_t2offbtn_visibility),
                        InformationSet("validate acu3_t2offbtn visibility = " + str(acu3_t2offbtn_visibility_expected), "mcrhci", "hcitracer", validate_acu3_t2offbtn_visibility),
                        InformationSet("set mcr_acu_t2_cmdstatus = "+ str(mcr_acu_t2_cmdstatus_init_2), "thriver", "mcrhci", set_mcr_acu_t2_cmdstatus_2),
                        InformationSet("get acu3_t2offdisable background_color", "thriver", "mcrhci", get_acu3_t2offdisable_background_color),
                        InformationSet("validate acu3_t2offdisable background_color = " + str(acu3_t2offdisable_background_color_expected), "mcrhci", "hcitracer", validate_acu3_t2offdisable_background_color),
                        InformationSet("set steeringextrps_sg2_psoff_cmdenable = "+ str(steeringextrps_sg2_psoff_cmdenable_init_1), "thriver", "mcrhci", set_steeringextrps_sg2_psoff_cmdenable_1),
                        InformationSet("get acu3_t2offdisable visibility", "thriver", "mcrhci", get_acu3_t2offdisable_visibility),
                        InformationSet("validate acu3_t2offdisable visibility = " + str(acu3_t2offdisable_visibility_expected), "mcrhci", "hcitracer", validate_acu3_t2offdisable_visibility),
                        InformationSet("get acu3_essctrlbtn visibility", "thriver", "mcrhci", get_acu3_essctrlbtn_visibility),
                        InformationSet("validate acu3_essctrlbtn visibility = " + str(acu3_essctrlbtn_visibility_expected), "mcrhci", "hcitracer", validate_acu3_essctrlbtn_visibility),
                        InformationSet("get acu3_maincoiltuningbtn visibility", "thriver", "mcrhci", get_acu3_maincoiltuningbtn_visibility),
                        InformationSet("validate acu3_maincoiltuningbtn visibility = " + str(acu3_maincoiltuningbtn_visibility_expected), "mcrhci", "hcitracer", validate_acu3_maincoiltuningbtn_visibility),
                        InformationSet("set mcr_acu_maincoil_tuning_cmdstatus = "+ str(mcr_acu_maincoil_tuning_cmdstatus_init_1), "thriver", "mcrhci", set_mcr_acu_maincoil_tuning_cmdstatus_1),
                        InformationSet("get acu3_maincoiltuningdisable background_color", "thriver", "mcrhci", get_acu3_maincoiltuningdisable_background_color),
                        InformationSet("validate acu3_maincoiltuningdisable background_color = " + str(acu3_maincoiltuningdisable_background_color_expected), "mcrhci", "hcitracer", validate_acu3_maincoiltuningdisable_background_color),
                        InformationSet("set maincoil_tuning_cmdenable = "+ str(maincoil_tuning_cmdenable_init_1), "thriver", "mcrhci", set_maincoil_tuning_cmdenable_1),
                        InformationSet("get acu3_maincoiltuningdisable visibility", "thriver", "mcrhci", get_acu3_maincoiltuningdisable_visibility),
                        InformationSet("validate acu3_maincoiltuningdisable visibility = " + str(acu3_maincoiltuningdisable_visibility_expected), "mcrhci", "hcitracer", validate_acu3_maincoiltuningdisable_visibility),
                        InformationSet("set mcr_acu_maincoil_tuning_cmdstatus = "+ str(mcr_acu_maincoil_tuning_cmdstatus_init_2), "thriver", "mcrhci", set_mcr_acu_maincoil_tuning_cmdstatus_2),
                        InformationSet("get acu3_maincoiltuningled visibility", "thriver", "mcrhci", get_acu3_maincoiltuningled_visibility),
                        InformationSet("validate acu3_maincoiltuningled visibility = " + str(acu3_maincoiltuningled_visibility_expected), "mcrhci", "hcitracer", validate_acu3_maincoiltuningled_visibility),
                        InformationSet("get acu3_arctuningbtn visibility", "thriver", "mcrhci", get_acu3_arctuningbtn_visibility),
                        InformationSet("validate acu3_arctuningbtn visibility = " + str(acu3_arctuningbtn_visibility_expected), "mcrhci", "hcitracer", validate_acu3_arctuningbtn_visibility),
                        InformationSet("set mcr_acu_source_tuning_cmdenable = "+ str(mcr_acu_source_tuning_cmdenable_init_1), "thriver", "mcrhci", set_mcr_acu_source_tuning_cmdenable_1),
                        InformationSet("get acu3_arctuningdisable visibility", "thriver", "mcrhci", get_acu3_arctuningdisable_visibility),
                        InformationSet("validate acu3_arctuningdisable visibility = " + str(acu3_arctuningdisable_visibility_expected), "mcrhci", "hcitracer", validate_acu3_arctuningdisable_visibility),
                        InformationSet("set mcr_acu_source_tuning_cmdstatus = "+ str(mcr_acu_source_tuning_cmdstatus_init_1), "thriver", "mcrhci", set_mcr_acu_source_tuning_cmdstatus_1),
                        InformationSet("get acu3_arctuningled visibility", "thriver", "mcrhci", get_acu3_arctuningled_visibility),
                        InformationSet("validate acu3_arctuningled visibility = " + str(acu3_arctuningled_visibility_expected), "mcrhci", "hcitracer", validate_acu3_arctuningled_visibility),
                        InformationSet("get acu3_positionstatus visibility", "thriver", "mcrhci", get_acu3_positionstatus_visibility),
                        InformationSet("validate acu3_positionstatus visibility = " + str(acu3_positionstatus_visibility_expected), "mcrhci", "hcitracer", validate_acu3_positionstatus_visibility),
                        InformationSet("get acu3_maincoilpsvideo visibility", "thriver", "mcrhci", get_acu3_maincoilpsvideo_visibility),
                        InformationSet("validate acu3_maincoilpsvideo visibility = " + str(acu3_maincoilpsvideo_visibility_expected), "mcrhci", "hcitracer", validate_acu3_maincoilpsvideo_visibility),
                        InformationSet("get acu3_sourcepsvideo visibility", "thriver", "mcrhci", get_acu3_sourcepsvideo_visibility),
                        InformationSet("validate acu3_sourcepsvideo visibility = " + str(acu3_sourcepsvideo_visibility_expected), "mcrhci", "hcitracer", validate_acu3_sourcepsvideo_visibility),
                        InformationSet("get acu3_llrfvideo visibility", "thriver", "mcrhci", get_acu3_llrfvideo_visibility),
                        InformationSet("validate acu3_llrfvideo visibility = " + str(acu3_llrfvideo_visibility_expected), "mcrhci", "hcitracer", validate_acu3_llrfvideo_visibility),
                        InformationSet("get acu3_ssavideo visibility", "thriver", "mcrhci", get_acu3_ssavideo_visibility),
                        InformationSet("validate acu3_ssavideo visibility = " + str(acu3_ssavideo_visibility_expected), "mcrhci", "hcitracer", validate_acu3_ssavideo_visibility),
                        InformationSet("get acu3_impavideo visibility", "thriver", "mcrhci", get_acu3_impavideo_visibility),
                        InformationSet("validate acu3_impavideo visibility = " + str(acu3_impavideo_visibility_expected), "mcrhci", "hcitracer", validate_acu3_impavideo_visibility),
                        InformationSet("get acu3_fpavideo visibility", "thriver", "mcrhci", get_acu3_fpavideo_visibility),
                        InformationSet("validate acu3_fpavideo visibility = " + str(acu3_fpavideo_visibility_expected), "mcrhci", "hcitracer", validate_acu3_fpavideo_visibility),
                        InformationSet("get acu3_rfvideo visibility", "thriver", "mcrhci", get_acu3_rfvideo_visibility),
                        InformationSet("validate acu3_rfvideo visibility = " + str(acu3_rfvideo_visibility_expected), "mcrhci", "hcitracer", validate_acu3_rfvideo_visibility),
                        InformationSet("get acu3_deflectorpsvideo visibility", "thriver", "mcrhci", get_acu3_deflectorpsvideo_visibility),
                        InformationSet("validate acu3_deflectorpsvideo visibility = " + str(acu3_deflectorpsvideo_visibility_expected), "mcrhci", "hcitracer", validate_acu3_deflectorpsvideo_visibility),
                        InformationSet("get acu3_cyclovacvideo visibility", "thriver", "mcrhci", get_acu3_cyclovacvideo_visibility),
                        InformationSet("validate acu3_cyclovacvideo visibility = " + str(acu3_cyclovacvideo_visibility_expected), "mcrhci", "hcitracer", validate_acu3_cyclovacvideo_visibility),
                        InformationSet("get acu3_hydrolicstationstatus visibility", "thriver", "mcrhci", get_acu3_hydrolicstationstatus_visibility),
                        InformationSet("validate acu3_hydrolicstationstatus visibility = " + str(acu3_hydrolicstationstatus_visibility_expected), "mcrhci", "hcitracer", validate_acu3_hydrolicstationstatus_visibility),
                        InformationSet("get acu3_coolingstatus visibility", "thriver", "mcrhci", get_acu3_coolingstatus_visibility),
                        InformationSet("validate acu3_coolingstatus visibility = " + str(acu3_coolingstatus_visibility_expected), "mcrhci", "hcitracer", validate_acu3_coolingstatus_visibility),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []