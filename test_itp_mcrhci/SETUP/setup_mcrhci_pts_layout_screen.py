
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

class SETUP_VALIDATE_DEFAULT_PTS_LAYOUT_SCREEN(ClinicalIntegrationTestProcedure):
    # default variable values
    name = "Confirm that PTS layout (pts_layout.v) is displayed"

    def __init__(self, test):
        cls = type(self)
        name = cls.name
        ess_visibility_expected = "1"
        ess_btn_visibility_expected = "0"
        cyclotron_visibility_expected = "1"
        cyclotron_btn_visibility_expected = "0"
        Title_string_visibility_expected = "1"
        PlainView_Logo_visibility_expected = "1"
        pts_layout_ctrl_unit_btn_visibility_expected = "1"
        gts1_visibility_expected = "1"
        bts1_visibility_expected = "1"
        bts1_btn_visibility_expected = "0"
        gts1_btn_visibility_expected = "0"
        pts_layout_saveEqt_btn_visibility_expected = "1"
        pts_layout_editEqt_btn_visibility_expected = "1"
        gts2_visibility_expected = "1"
        gts2_btn_visibility_expected = "0"
        PlainView_hidden_object_visibility_expected = "1"
        pts_layout_appstatus_btn_visibility_expected = "1"
        pts_layout_tss_scu_interlocks_btn_visibility_expected = "1"
        pts_layout_tr1_beam_intlks_btn_visibility_expected = "1"
        pts_layout_save_tr1_nozzle_btn_visibility_expected = "1"
        pts_layout_edit_tr1_nozzle_btn_visibility_expected = "1"
        pts_layout_mantune_btn_visibility_expected = "1"
        bts3abc_visibility_expected = "1"
        bts3abc_btn_visibility_expected = "0"
        bts2_visibility_expected = "1"
        bts2_btn_visibility_expected = "0"
        pts_layout_phasespace_btn_visibility_expected = "1"
        pts_layout_save_tr2_nozzle_btn_visibility_expected = "1"
        pts_layout_edit_tr2_nozzle_btn_visibility_expected = "1"
        pts_layout_tr2_beam_intlks_btn_visibility_expected = "1"
        bts3_visibility_expected = "1"
        bts3_btn_visibility_expected = "0"
        pts_layout_tr1_tol_check_data_btn_visibility_expected = "1"
        pts_layout_tr2_tol_check_data_btn_visibility_expected = "1"
        pts_layout_tr1_pps_data_btn_visibility_expected = "1"
        pts_layout_tr2_pps_data_btn_visibility_expected = "1"
        pts_layout_tr1_tolerance_check_btn_visibility_expected = "1"
        pts_layout_tr2_tolerance_check_btn_visibility_expected = "1"
        pts_layout_acu_db_50a_btn_visibility_expected = "1"
        pts_layout_acu_db_60b_btn_visibility_expected = "1"
        pts_layout_acu_db_60c_btn_visibility_expected = "1"
        pts_layout_acu_db_20_btn_visibility_expected = "1"
        pts_layout_acu_db_10_btn_visibility_expected = "1"
        pts_layout_acu_db_50b60a_btn_visibility_expected = "1"

        #get values
        get_ess_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "ess")
        get_ess_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "ess_btn")
        get_cyclotron_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "cyclotron")
        get_cyclotron_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "cyclotron_btn")
        get_Title_string_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "Title_string")
        get_PlainView_Logo_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "PlainView_Logo")
        get_pts_layout_ctrl_unit_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "pts_layout_ctrl_unit_btn")
        get_gts1_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "gts1")
        get_bts1_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1")
        get_bts1_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts1_btn")
        get_gts1_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "gts1_btn")
        get_pts_layout_saveEqt_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "pts_layout_saveEqt_btn")
        get_pts_layout_editEqt_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "pts_layout_editEqt_btn")
        get_gts2_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "gts2")
        get_gts2_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "gts2_btn")
        get_PlainView_hidden_object_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "PlainView_hidden_object")
        get_pts_layout_appstatus_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "pts_layout_appstatus_btn")
        get_pts_layout_tss_scu_interlocks_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "pts_layout_tss_scu_interlocks_btn")
        get_pts_layout_tr1_beam_intlks_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "pts_layout_tr1_beam_intlks_btn")
        get_pts_layout_save_tr1_nozzle_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "pts_layout_save_tr1_nozzle_btn")
        get_pts_layout_edit_tr1_nozzle_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "pts_layout_edit_tr1_nozzle_btn")
        get_pts_layout_mantune_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "pts_layout_mantune_btn")
        get_bts3abc_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3abc")
        get_bts3abc_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3abc_btn")
        get_bts2_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts2")
        get_bts2_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts2_btn")
        get_pts_layout_phasespace_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "pts_layout_phasespace_btn")
        get_pts_layout_save_tr2_nozzle_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "pts_layout_save_tr2_nozzle_btn")
        get_pts_layout_edit_tr2_nozzle_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "pts_layout_edit_tr2_nozzle_btn")
        get_pts_layout_tr2_beam_intlks_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "pts_layout_tr2_beam_intlks_btn")
        get_bts3_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3")
        get_bts3_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "bts3_btn")
        get_pts_layout_tr1_tol_check_data_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "pts_layout_tr1_tol_check_data_btn")
        get_pts_layout_tr2_tol_check_data_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "pts_layout_tr2_tol_check_data_btn")
        get_pts_layout_tr1_pps_data_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "pts_layout_tr1_pps_data_btn")
        get_pts_layout_tr2_pps_data_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "pts_layout_tr2_pps_data_btn")
        get_pts_layout_tr1_tolerance_check_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "pts_layout_tr1_tolerance_check_btn")
        get_pts_layout_tr2_tolerance_check_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "pts_layout_tr2_tolerance_check_btn")
        get_pts_layout_acu_db_50a_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "pts_layout_acu_db_50a_btn")
        get_pts_layout_acu_db_60b_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "pts_layout_acu_db_60b_btn")
        get_pts_layout_acu_db_60c_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "pts_layout_acu_db_60c_btn")
        get_pts_layout_acu_db_20_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "pts_layout_acu_db_20_btn")
        get_pts_layout_acu_db_10_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "pts_layout_acu_db_10_btn")
        get_pts_layout_acu_db_50b60a_btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "pts_layout_acu_db_50b60a_btn")

        #validate
        validate_ess_visibility = MsgTypeString("ess:TMMI_MCR_IS_VISIBLE", value=ess_visibility_expected)
        validate_ess_btn_visibility = MsgTypeString("ess_btn:TMMI_MCR_IS_VISIBLE", value=ess_btn_visibility_expected)
        validate_cyclotron_visibility = MsgTypeString("cyclotron:TMMI_MCR_IS_VISIBLE", value=cyclotron_visibility_expected)
        validate_cyclotron_btn_visibility = MsgTypeString("cyclotron_btn:TMMI_MCR_IS_VISIBLE", value=cyclotron_btn_visibility_expected)
        validate_Title_string_visibility = MsgTypeString("Title_string:TMMI_MCR_IS_VISIBLE", value=Title_string_visibility_expected)
        validate_PlainView_Logo_visibility = MsgTypeString("PlainView_Logo:TMMI_MCR_IS_VISIBLE", value=PlainView_Logo_visibility_expected)
        validate_pts_layout_ctrl_unit_btn_visibility = MsgTypeString("pts_layout_ctrl_unit_btn:TMMI_MCR_IS_VISIBLE", value=pts_layout_ctrl_unit_btn_visibility_expected)
        validate_gts1_visibility = MsgTypeString("gts1:TMMI_MCR_IS_VISIBLE", value=gts1_visibility_expected)
        validate_bts1_visibility = MsgTypeString("bts1:TMMI_MCR_IS_VISIBLE", value=bts1_visibility_expected)
        validate_bts1_btn_visibility = MsgTypeString("bts1_btn:TMMI_MCR_IS_VISIBLE", value=bts1_btn_visibility_expected)
        validate_gts1_btn_visibility = MsgTypeString("gts1_btn:TMMI_MCR_IS_VISIBLE", value=gts1_btn_visibility_expected)
        validate_pts_layout_saveEqt_btn_visibility = MsgTypeString("pts_layout_saveEqt_btn:TMMI_MCR_IS_VISIBLE", value=pts_layout_saveEqt_btn_visibility_expected)
        validate_pts_layout_editEqt_btn_visibility = MsgTypeString("pts_layout_editEqt_btn:TMMI_MCR_IS_VISIBLE", value=pts_layout_editEqt_btn_visibility_expected)
        validate_gts2_visibility = MsgTypeString("gts2:TMMI_MCR_IS_VISIBLE", value=gts2_visibility_expected)
        validate_gts2_btn_visibility = MsgTypeString("gts2_btn:TMMI_MCR_IS_VISIBLE", value=gts2_btn_visibility_expected)
        validate_PlainView_hidden_object_visibility = MsgTypeString("PlainView_hidden_object:TMMI_MCR_IS_VISIBLE", value=PlainView_hidden_object_visibility_expected)
        validate_pts_layout_appstatus_btn_visibility = MsgTypeString("pts_layout_appstatus_btn:TMMI_MCR_IS_VISIBLE", value=pts_layout_appstatus_btn_visibility_expected)
        validate_pts_layout_tss_scu_interlocks_btn_visibility = MsgTypeString("pts_layout_tss_scu_interlocks_btn:TMMI_MCR_IS_VISIBLE", value=pts_layout_tss_scu_interlocks_btn_visibility_expected)
        validate_pts_layout_tr1_beam_intlks_btn_visibility = MsgTypeString("pts_layout_tr1_beam_intlks_btn:TMMI_MCR_IS_VISIBLE", value=pts_layout_tr1_beam_intlks_btn_visibility_expected)
        validate_pts_layout_save_tr1_nozzle_btn_visibility = MsgTypeString("pts_layout_save_tr1_nozzle_btn:TMMI_MCR_IS_VISIBLE", value=pts_layout_save_tr1_nozzle_btn_visibility_expected)
        validate_pts_layout_edit_tr1_nozzle_btn_visibility = MsgTypeString("pts_layout_edit_tr1_nozzle_btn:TMMI_MCR_IS_VISIBLE", value=pts_layout_edit_tr1_nozzle_btn_visibility_expected)
        validate_pts_layout_mantune_btn_visibility = MsgTypeString("pts_layout_mantune_btn:TMMI_MCR_IS_VISIBLE", value=pts_layout_mantune_btn_visibility_expected)
        validate_bts3abc_visibility = MsgTypeString("bts3abc:TMMI_MCR_IS_VISIBLE", value=bts3abc_visibility_expected)
        validate_bts3abc_btn_visibility = MsgTypeString("bts3abc_btn:TMMI_MCR_IS_VISIBLE", value=bts3abc_btn_visibility_expected)
        validate_bts2_visibility = MsgTypeString("bts2:TMMI_MCR_IS_VISIBLE", value=bts2_visibility_expected)
        validate_bts2_btn_visibility = MsgTypeString("bts2_btn:TMMI_MCR_IS_VISIBLE", value=bts2_btn_visibility_expected)
        validate_pts_layout_phasespace_btn_visibility = MsgTypeString("pts_layout_phasespace_btn:TMMI_MCR_IS_VISIBLE", value=pts_layout_phasespace_btn_visibility_expected)
        validate_pts_layout_save_tr2_nozzle_btn_visibility = MsgTypeString("pts_layout_save_tr2_nozzle_btn:TMMI_MCR_IS_VISIBLE", value=pts_layout_save_tr2_nozzle_btn_visibility_expected)
        validate_pts_layout_edit_tr2_nozzle_btn_visibility = MsgTypeString("pts_layout_edit_tr2_nozzle_btn:TMMI_MCR_IS_VISIBLE", value=pts_layout_edit_tr2_nozzle_btn_visibility_expected)
        validate_pts_layout_tr2_beam_intlks_btn_visibility = MsgTypeString("pts_layout_tr2_beam_intlks_btn:TMMI_MCR_IS_VISIBLE", value=pts_layout_tr2_beam_intlks_btn_visibility_expected)
        validate_bts3_visibility = MsgTypeString("bts3:TMMI_MCR_IS_VISIBLE", value=bts3_visibility_expected)
        validate_bts3_btn_visibility = MsgTypeString("bts3_btn:TMMI_MCR_IS_VISIBLE", value=bts3_btn_visibility_expected)
        validate_pts_layout_tr1_tol_check_data_btn_visibility = MsgTypeString("pts_layout_tr1_tol_check_data_btn:TMMI_MCR_IS_VISIBLE", value=pts_layout_tr1_tol_check_data_btn_visibility_expected)
        validate_pts_layout_tr2_tol_check_data_btn_visibility = MsgTypeString("pts_layout_tr2_tol_check_data_btn:TMMI_MCR_IS_VISIBLE", value=pts_layout_tr2_tol_check_data_btn_visibility_expected)
        validate_pts_layout_tr1_pps_data_btn_visibility = MsgTypeString("pts_layout_tr1_pps_data_btn:TMMI_MCR_IS_VISIBLE", value=pts_layout_tr1_pps_data_btn_visibility_expected)
        validate_pts_layout_tr2_pps_data_btn_visibility = MsgTypeString("pts_layout_tr2_pps_data_btn:TMMI_MCR_IS_VISIBLE", value=pts_layout_tr2_pps_data_btn_visibility_expected)
        validate_pts_layout_tr1_tolerance_check_btn_visibility = MsgTypeString("pts_layout_tr1_tolerance_check_btn:TMMI_MCR_IS_VISIBLE", value=pts_layout_tr1_tolerance_check_btn_visibility_expected)
        validate_pts_layout_tr2_tolerance_check_btn_visibility = MsgTypeString("pts_layout_tr2_tolerance_check_btn:TMMI_MCR_IS_VISIBLE", value=pts_layout_tr2_tolerance_check_btn_visibility_expected)
        validate_pts_layout_acu_db_50a_btn_visibility = MsgTypeString("pts_layout_acu_db_50a_btn:TMMI_MCR_IS_VISIBLE", value=pts_layout_acu_db_50a_btn_visibility_expected)
        validate_pts_layout_acu_db_60b_btn_visibility = MsgTypeString("pts_layout_acu_db_60b_btn:TMMI_MCR_IS_VISIBLE", value=pts_layout_acu_db_60b_btn_visibility_expected)
        validate_pts_layout_acu_db_60c_btn_visibility = MsgTypeString("pts_layout_acu_db_60c_btn:TMMI_MCR_IS_VISIBLE", value=pts_layout_acu_db_60c_btn_visibility_expected)
        validate_pts_layout_acu_db_20_btn_visibility = MsgTypeString("pts_layout_acu_db_20_btn:TMMI_MCR_IS_VISIBLE", value=pts_layout_acu_db_20_btn_visibility_expected)
        validate_pts_layout_acu_db_10_btn_visibility = MsgTypeString("pts_layout_acu_db_10_btn:TMMI_MCR_IS_VISIBLE", value=pts_layout_acu_db_10_btn_visibility_expected)
        validate_pts_layout_acu_db_50b60a_btn_visibility = MsgTypeString("pts_layout_acu_db_50b60a_btn:TMMI_MCR_IS_VISIBLE", value=pts_layout_acu_db_50b60a_btn_visibility_expected)

        info_exchange = [
                        InformationSet("get ess visibility", "thriver", "mcrhci", get_ess_visibility),
                        InformationSet("validate ess visibility = " + str(ess_visibility_expected), "mcrhci", "hcitracer", validate_ess_visibility),
                        InformationSet("get ess_btn visibility", "thriver", "mcrhci", get_ess_btn_visibility),
                        InformationSet("validate ess_btn visibility = " + str(ess_btn_visibility_expected), "mcrhci", "hcitracer", validate_ess_btn_visibility),
                        InformationSet("get cyclotron visibility", "thriver", "mcrhci", get_cyclotron_visibility),
                        InformationSet("validate cyclotron visibility = " + str(cyclotron_visibility_expected), "mcrhci", "hcitracer", validate_cyclotron_visibility),
                        InformationSet("get cyclotron_btn visibility", "thriver", "mcrhci", get_cyclotron_btn_visibility),
                        InformationSet("validate cyclotron_btn visibility = " + str(cyclotron_btn_visibility_expected), "mcrhci", "hcitracer", validate_cyclotron_btn_visibility),
                        InformationSet("get Title_string visibility", "thriver", "mcrhci", get_Title_string_visibility),
                        InformationSet("validate Title_string visibility = " + str(Title_string_visibility_expected), "mcrhci", "hcitracer", validate_Title_string_visibility),
                        InformationSet("get PlainView_Logo visibility", "thriver", "mcrhci", get_PlainView_Logo_visibility),
                        InformationSet("validate PlainView_Logo visibility = " + str(PlainView_Logo_visibility_expected), "mcrhci", "hcitracer", validate_PlainView_Logo_visibility),
                        InformationSet("get pts_layout_ctrl_unit_btn visibility", "thriver", "mcrhci", get_pts_layout_ctrl_unit_btn_visibility),
                        InformationSet("validate pts_layout_ctrl_unit_btn visibility = " + str(pts_layout_ctrl_unit_btn_visibility_expected), "mcrhci", "hcitracer", validate_pts_layout_ctrl_unit_btn_visibility),
                        InformationSet("get gts1 visibility", "thriver", "mcrhci", get_gts1_visibility),
                        InformationSet("validate gts1 visibility = " + str(gts1_visibility_expected), "mcrhci", "hcitracer", validate_gts1_visibility),
                        InformationSet("get bts1 visibility", "thriver", "mcrhci", get_bts1_visibility),
                        InformationSet("validate bts1 visibility = " + str(bts1_visibility_expected), "mcrhci", "hcitracer", validate_bts1_visibility),
                        InformationSet("get bts1_btn visibility", "thriver", "mcrhci", get_bts1_btn_visibility),
                        InformationSet("validate bts1_btn visibility = " + str(bts1_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts1_btn_visibility),
                        InformationSet("get gts1_btn visibility", "thriver", "mcrhci", get_gts1_btn_visibility),
                        InformationSet("validate gts1_btn visibility = " + str(gts1_btn_visibility_expected), "mcrhci", "hcitracer", validate_gts1_btn_visibility),
                        InformationSet("get pts_layout_saveEqt_btn visibility", "thriver", "mcrhci", get_pts_layout_saveEqt_btn_visibility),
                        InformationSet("validate pts_layout_saveEqt_btn visibility = " + str(pts_layout_saveEqt_btn_visibility_expected), "mcrhci", "hcitracer", validate_pts_layout_saveEqt_btn_visibility),
                        InformationSet("get pts_layout_editEqt_btn visibility", "thriver", "mcrhci", get_pts_layout_editEqt_btn_visibility),
                        InformationSet("validate pts_layout_editEqt_btn visibility = " + str(pts_layout_editEqt_btn_visibility_expected), "mcrhci", "hcitracer", validate_pts_layout_editEqt_btn_visibility),
                        InformationSet("get gts2 visibility", "thriver", "mcrhci", get_gts2_visibility),
                        InformationSet("validate gts2 visibility = " + str(gts2_visibility_expected), "mcrhci", "hcitracer", validate_gts2_visibility),
                        InformationSet("get gts2_btn visibility", "thriver", "mcrhci", get_gts2_btn_visibility),
                        InformationSet("validate gts2_btn visibility = " + str(gts2_btn_visibility_expected), "mcrhci", "hcitracer", validate_gts2_btn_visibility),
                        InformationSet("get PlainView_hidden_object visibility", "thriver", "mcrhci", get_PlainView_hidden_object_visibility),
                        InformationSet("validate PlainView_hidden_object visibility = " + str(PlainView_hidden_object_visibility_expected), "mcrhci", "hcitracer", validate_PlainView_hidden_object_visibility),
                        InformationSet("get pts_layout_appstatus_btn visibility", "thriver", "mcrhci", get_pts_layout_appstatus_btn_visibility),
                        InformationSet("validate pts_layout_appstatus_btn visibility = " + str(pts_layout_appstatus_btn_visibility_expected), "mcrhci", "hcitracer", validate_pts_layout_appstatus_btn_visibility),
                        InformationSet("get pts_layout_tss_scu_interlocks_btn visibility", "thriver", "mcrhci", get_pts_layout_tss_scu_interlocks_btn_visibility),
                        InformationSet("validate pts_layout_tss_scu_interlocks_btn visibility = " + str(pts_layout_tss_scu_interlocks_btn_visibility_expected), "mcrhci", "hcitracer", validate_pts_layout_tss_scu_interlocks_btn_visibility),
                        InformationSet("get pts_layout_tr1_beam_intlks_btn visibility", "thriver", "mcrhci", get_pts_layout_tr1_beam_intlks_btn_visibility),
                        InformationSet("validate pts_layout_tr1_beam_intlks_btn visibility = " + str(pts_layout_tr1_beam_intlks_btn_visibility_expected), "mcrhci", "hcitracer", validate_pts_layout_tr1_beam_intlks_btn_visibility),
                        InformationSet("get pts_layout_save_tr1_nozzle_btn visibility", "thriver", "mcrhci", get_pts_layout_save_tr1_nozzle_btn_visibility),
                        InformationSet("validate pts_layout_save_tr1_nozzle_btn visibility = " + str(pts_layout_save_tr1_nozzle_btn_visibility_expected), "mcrhci", "hcitracer", validate_pts_layout_save_tr1_nozzle_btn_visibility),
                        InformationSet("get pts_layout_edit_tr1_nozzle_btn visibility", "thriver", "mcrhci", get_pts_layout_edit_tr1_nozzle_btn_visibility),
                        InformationSet("validate pts_layout_edit_tr1_nozzle_btn visibility = " + str(pts_layout_edit_tr1_nozzle_btn_visibility_expected), "mcrhci", "hcitracer", validate_pts_layout_edit_tr1_nozzle_btn_visibility),
                        InformationSet("get pts_layout_mantune_btn visibility", "thriver", "mcrhci", get_pts_layout_mantune_btn_visibility),
                        InformationSet("validate pts_layout_mantune_btn visibility = " + str(pts_layout_mantune_btn_visibility_expected), "mcrhci", "hcitracer", validate_pts_layout_mantune_btn_visibility),
                        InformationSet("get bts3abc visibility", "thriver", "mcrhci", get_bts3abc_visibility),
                        InformationSet("validate bts3abc visibility = " + str(bts3abc_visibility_expected), "mcrhci", "hcitracer", validate_bts3abc_visibility),
                        InformationSet("get bts3abc_btn visibility", "thriver", "mcrhci", get_bts3abc_btn_visibility),
                        InformationSet("validate bts3abc_btn visibility = " + str(bts3abc_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts3abc_btn_visibility),
                        InformationSet("get bts2 visibility", "thriver", "mcrhci", get_bts2_visibility),
                        InformationSet("validate bts2 visibility = " + str(bts2_visibility_expected), "mcrhci", "hcitracer", validate_bts2_visibility),
                        InformationSet("get bts2_btn visibility", "thriver", "mcrhci", get_bts2_btn_visibility),
                        InformationSet("validate bts2_btn visibility = " + str(bts2_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts2_btn_visibility),
                        InformationSet("get pts_layout_phasespace_btn visibility", "thriver", "mcrhci", get_pts_layout_phasespace_btn_visibility),
                        InformationSet("validate pts_layout_phasespace_btn visibility = " + str(pts_layout_phasespace_btn_visibility_expected), "mcrhci", "hcitracer", validate_pts_layout_phasespace_btn_visibility),
                        InformationSet("get pts_layout_save_tr2_nozzle_btn visibility", "thriver", "mcrhci", get_pts_layout_save_tr2_nozzle_btn_visibility),
                        InformationSet("validate pts_layout_save_tr2_nozzle_btn visibility = " + str(pts_layout_save_tr2_nozzle_btn_visibility_expected), "mcrhci", "hcitracer", validate_pts_layout_save_tr2_nozzle_btn_visibility),
                        InformationSet("get pts_layout_edit_tr2_nozzle_btn visibility", "thriver", "mcrhci", get_pts_layout_edit_tr2_nozzle_btn_visibility),
                        InformationSet("validate pts_layout_edit_tr2_nozzle_btn visibility = " + str(pts_layout_edit_tr2_nozzle_btn_visibility_expected), "mcrhci", "hcitracer", validate_pts_layout_edit_tr2_nozzle_btn_visibility),
                        InformationSet("get pts_layout_tr2_beam_intlks_btn visibility", "thriver", "mcrhci", get_pts_layout_tr2_beam_intlks_btn_visibility),
                        InformationSet("validate pts_layout_tr2_beam_intlks_btn visibility = " + str(pts_layout_tr2_beam_intlks_btn_visibility_expected), "mcrhci", "hcitracer", validate_pts_layout_tr2_beam_intlks_btn_visibility),
                        InformationSet("get bts3 visibility", "thriver", "mcrhci", get_bts3_visibility),
                        InformationSet("validate bts3 visibility = " + str(bts3_visibility_expected), "mcrhci", "hcitracer", validate_bts3_visibility),
                        InformationSet("get bts3_btn visibility", "thriver", "mcrhci", get_bts3_btn_visibility),
                        InformationSet("validate bts3_btn visibility = " + str(bts3_btn_visibility_expected), "mcrhci", "hcitracer", validate_bts3_btn_visibility),
                        InformationSet("get pts_layout_tr1_tol_check_data_btn visibility", "thriver", "mcrhci", get_pts_layout_tr1_tol_check_data_btn_visibility),
                        InformationSet("validate pts_layout_tr1_tol_check_data_btn visibility = " + str(pts_layout_tr1_tol_check_data_btn_visibility_expected), "mcrhci", "hcitracer", validate_pts_layout_tr1_tol_check_data_btn_visibility),
                        InformationSet("get pts_layout_tr2_tol_check_data_btn visibility", "thriver", "mcrhci", get_pts_layout_tr2_tol_check_data_btn_visibility),
                        InformationSet("validate pts_layout_tr2_tol_check_data_btn visibility = " + str(pts_layout_tr2_tol_check_data_btn_visibility_expected), "mcrhci", "hcitracer", validate_pts_layout_tr2_tol_check_data_btn_visibility),
                        InformationSet("get pts_layout_tr1_pps_data_btn visibility", "thriver", "mcrhci", get_pts_layout_tr1_pps_data_btn_visibility),
                        InformationSet("validate pts_layout_tr1_pps_data_btn visibility = " + str(pts_layout_tr1_pps_data_btn_visibility_expected), "mcrhci", "hcitracer", validate_pts_layout_tr1_pps_data_btn_visibility),
                        InformationSet("get pts_layout_tr2_pps_data_btn visibility", "thriver", "mcrhci", get_pts_layout_tr2_pps_data_btn_visibility),
                        InformationSet("validate pts_layout_tr2_pps_data_btn visibility = " + str(pts_layout_tr2_pps_data_btn_visibility_expected), "mcrhci", "hcitracer", validate_pts_layout_tr2_pps_data_btn_visibility),
                        InformationSet("get pts_layout_tr1_tolerance_check_btn visibility", "thriver", "mcrhci", get_pts_layout_tr1_tolerance_check_btn_visibility),
                        InformationSet("validate pts_layout_tr1_tolerance_check_btn visibility = " + str(pts_layout_tr1_tolerance_check_btn_visibility_expected), "mcrhci", "hcitracer", validate_pts_layout_tr1_tolerance_check_btn_visibility),
                        InformationSet("get pts_layout_tr2_tolerance_check_btn visibility", "thriver", "mcrhci", get_pts_layout_tr2_tolerance_check_btn_visibility),
                        InformationSet("validate pts_layout_tr2_tolerance_check_btn visibility = " + str(pts_layout_tr2_tolerance_check_btn_visibility_expected), "mcrhci", "hcitracer", validate_pts_layout_tr2_tolerance_check_btn_visibility),
                        InformationSet("get pts_layout_acu_db_50a_btn visibility", "thriver", "mcrhci", get_pts_layout_acu_db_50a_btn_visibility),
                        InformationSet("validate pts_layout_acu_db_50a_btn visibility = " + str(pts_layout_acu_db_50a_btn_visibility_expected), "mcrhci", "hcitracer", validate_pts_layout_acu_db_50a_btn_visibility),
                        InformationSet("get pts_layout_acu_db_60b_btn visibility", "thriver", "mcrhci", get_pts_layout_acu_db_60b_btn_visibility),
                        InformationSet("validate pts_layout_acu_db_60b_btn visibility = " + str(pts_layout_acu_db_60b_btn_visibility_expected), "mcrhci", "hcitracer", validate_pts_layout_acu_db_60b_btn_visibility),
                        InformationSet("get pts_layout_acu_db_60c_btn visibility", "thriver", "mcrhci", get_pts_layout_acu_db_60c_btn_visibility),
                        InformationSet("validate pts_layout_acu_db_60c_btn visibility = " + str(pts_layout_acu_db_60c_btn_visibility_expected), "mcrhci", "hcitracer", validate_pts_layout_acu_db_60c_btn_visibility),
                        InformationSet("get pts_layout_acu_db_20_btn visibility", "thriver", "mcrhci", get_pts_layout_acu_db_20_btn_visibility),
                        InformationSet("validate pts_layout_acu_db_20_btn visibility = " + str(pts_layout_acu_db_20_btn_visibility_expected), "mcrhci", "hcitracer", validate_pts_layout_acu_db_20_btn_visibility),
                        InformationSet("get pts_layout_acu_db_10_btn visibility", "thriver", "mcrhci", get_pts_layout_acu_db_10_btn_visibility),
                        InformationSet("validate pts_layout_acu_db_10_btn visibility = " + str(pts_layout_acu_db_10_btn_visibility_expected), "mcrhci", "hcitracer", validate_pts_layout_acu_db_10_btn_visibility),
                        InformationSet("get pts_layout_acu_db_50b60a_btn visibility", "thriver", "mcrhci", get_pts_layout_acu_db_50b60a_btn_visibility),
                        InformationSet("validate pts_layout_acu_db_50b60a_btn visibility = " + str(pts_layout_acu_db_50b60a_btn_visibility_expected), "mcrhci", "hcitracer", validate_pts_layout_acu_db_50b60a_btn_visibility),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_CLICK_CYCLOTRON_IMAGE(ClinicalIntegrationTestProcedure):
    name = "Click on Cyclotron image"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonNameEvent(0,[["pts_layout:cyclotron_btn"]])
        info_exchange = [ 
                        InformationSet("Click on Cyclotron image", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_CLICK_ESS_IMAGE(ClinicalIntegrationTestProcedure):
    name = "Click on ESS image"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonNameEvent(0,[["pts_layout:ess_btn"]])
        info_exchange = [ 
                        InformationSet("Click on Ess image", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_CLICK_GTS1_IMAGE(ClinicalIntegrationTestProcedure):
    name = "Click on GTS1 image"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonNameEvent(0,[["pts_layout:gts1_btn"]])
        info_exchange = [ 
                        InformationSet("Click on GTS1 image", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_CLICK_GTS2_IMAGE(ClinicalIntegrationTestProcedure):
    name = "Click on GTS2 image"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonNameEvent(0,[["pts_layout:gts2_btn"]])
        info_exchange = [ 
                        InformationSet("Click on GTS2 image", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_CLICK_BTS1_IMAGE(ClinicalIntegrationTestProcedure):
    name = "Click on BTS1 image"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonNameEvent(0,[["pts_layout:bts1_btn"]])
        info_exchange = [ 
                        InformationSet("Click on BTS1 image", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_CLICK_BTS2_IMAGE(ClinicalIntegrationTestProcedure):
    name = "Click on BTS2 image"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonNameEvent(0,[["pts_layout:bts2_btn"]])
        info_exchange = [ 
                        InformationSet("Click on BTS2 image", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_CLICK_BTS3_IMAGE(ClinicalIntegrationTestProcedure):
    name = "Click on BTS3 image"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonNameEvent(0,[["pts_layout:bts3_btn"]])
        info_exchange = [ 
                        InformationSet("Click on BTS3 image", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_CLICK_BTS3ABC_IMAGE(ClinicalIntegrationTestProcedure):
    name = "Click on BTS3ABC image"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonNameEvent(0,[["pts_layout:bts3abc_btn"]])
        info_exchange = [ 
                        InformationSet("Click on BTS3ABC image", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_CLICK_CTRL_UNIT_STATUS_BUTTON(ClinicalIntegrationTestProcedure):
    name = "Click on Ctrl Unit Status button"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonNameEvent(0,[["pts_layout:pts_layout_ctrl_unit_btn"]])
        info_exchange = [ 
                        InformationSet("Click on Ctrl Unit Status button", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_CLICK_SAVE_EQT_PARAMS_BUTTON(ClinicalIntegrationTestProcedure):
    name = "Click on Save Eqt Params button"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonNameEvent(0,[["pts_layout:pts_layout_saveEqt_btn"]])
        info_exchange = [ 
                        InformationSet("Click on Save Eqt Params button", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_CLICK_EDIT_EQT_PARAMS_BUTTON(ClinicalIntegrationTestProcedure):
    name = "Click on Edit Eqt Params button"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonNameEvent(0,[["pts_layout:pts_layout_editEqt_btn"]])
        info_exchange = [ 
                        InformationSet("Click on Edit Eqt Params button", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_CLICK_APPLICATIONS_STATUS_BUTTON(ClinicalIntegrationTestProcedure):
    name = "Click on Application Status button"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonNameEvent(0,[["pts_layout:pts_layout_appstatus_btn"]])
        info_exchange = [ 
                        InformationSet("Click on Applications Status button", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_CLICK_TSS_SCU_INTERLOCKS_BUTTON(ClinicalIntegrationTestProcedure):
    name = "Click on TSS SCU Interlocks button"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonNameEvent(0,[["pts_layout:pts_layout_tss_scu_interlocks_btn"]])
        info_exchange = [ 
                        InformationSet("Click on TSS/SCU Interlocks button", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_CLICK_TR1_INTLKS_BUTTON(ClinicalIntegrationTestProcedure):
    name = "Click on TR1 IntLks button"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonNameEvent(0,[["pts_layout:pts_layout_tr1_beam_intlks_btn"]])
        info_exchange = [ 
                        InformationSet("Click on TR1 Intlks button", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_CLICK_TR2_INTLKS_BUTTON(ClinicalIntegrationTestProcedure):
    name = "Click on TR2 IntLks button"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonNameEvent(0,[["pts_layout:pts_layout_tr2_beam_intlks_btn"]])
        info_exchange = [ 
                        InformationSet("Click on TR2 Intlks button", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_CLICK_TR1_TOL_CHECK_DATA_BUTTON(ClinicalIntegrationTestProcedure):
    name = "Click on TR1 Tol Check Data button"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonNameEvent(0,[["pts_layout:pts_layout_tr1_tol_check_data_btn"]])
        info_exchange = [ 
                        InformationSet("Click on TR1 Tol Check Data button", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_CLICK_TR2_TOL_CHECK_DATA_BUTTON(ClinicalIntegrationTestProcedure):
    name = "Click on TR2 Tol Check Data button"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonNameEvent(0,[["pts_layout:pts_layout_tr2_tol_check_data_btn"]])
        info_exchange = [ 
                        InformationSet("Click on TR2 Tol Check Data button", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_CLICK_TR1_PPS_DATA_BUTTON(ClinicalIntegrationTestProcedure):
    name = "Click on TR1 PPS Data button"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonNameEvent(0,[["pts_layout:pts_layout_tr1_pps_data_btn"]])
        info_exchange = [ 
                        InformationSet("Click on TR1 PPS Data button", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_CLICK_TR2_PPS_DATA_BUTTON(ClinicalIntegrationTestProcedure):
    name = "Click on TR2 PPS Data button"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonNameEvent(0,[["pts_layout:pts_layout_tr2_pps_data_btn"]])
        info_exchange = [ 
                        InformationSet("Click on TR2 PPS Data button", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_CLICK_TR1_TOLERANCE_CHECK_BUTTON(ClinicalIntegrationTestProcedure):
    name = "Click on TR1 Tolerance Check button"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonNameEvent(0,[["pts_layout:pts_layout_tr1_tolerance_check_btn"]])
        info_exchange = [ 
                        InformationSet("Click on TR1 Tolerance Check button", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_CLICK_TR2_TOLERANCE_CHECK_BUTTON(ClinicalIntegrationTestProcedure):
    name = "Click on TR2 Tolerance Check button"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonNameEvent(0,[["pts_layout:pts_layout_tr2_tolerance_check_btn"]])
        info_exchange = [ 
                        InformationSet("Click on TR2 Tolerance Check button", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_CLICK_ACU_DB_50A_BUTTON(ClinicalIntegrationTestProcedure):
    name = "Click on ACU DB 50a button"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonNameEvent(0,[["pts_layout:pts_layout_acu_db_50a_btn"]])
        info_exchange = [ 
                        InformationSet("Click on ACU DB's 50a button", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_CLICK_ACU_DB_60B_BUTTON(ClinicalIntegrationTestProcedure):
    name = "Click on ACU DB 60b button"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonNameEvent(0,[["pts_layout:pts_layout_acu_db_60b_btn"]])
        info_exchange = [ 
                        InformationSet("Click on ACU DB's 60b button", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_CLICK_ACU_DB_60C_BUTTON(ClinicalIntegrationTestProcedure):
    name = "Click on ACU DB 60c button"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonNameEvent(0,[["pts_layout:pts_layout_acu_db_60c_btn"]])
        info_exchange = [ 
                        InformationSet("Click on ACU DB's 60c button", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_CLICK_ACU_DB_10_BUTTON(ClinicalIntegrationTestProcedure):
    name = "Click on ACU DB 10 button"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonNameEvent(0,[["pts_layout:pts_layout_acu_db_10_btn"]])
        info_exchange = [ 
                        InformationSet("Click on ACU DB's 10 button", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_CLICK_ACU_DB_20_BUTTON(ClinicalIntegrationTestProcedure):
    name = "Click on ACU DB 20 button"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonNameEvent(0,[["pts_layout:pts_layout_acu_db_20_btn"]])
        info_exchange = [ 
                        InformationSet("Click on ACU DB's 20 button", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_CLICK_ACU_DB_50B_60A_BUTTON(ClinicalIntegrationTestProcedure):
    name = "Click on ACU DB 50b/60a button"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonNameEvent(0,[["pts_layout:pts_layout_acu_db_50b60a_btn"]])
        info_exchange = [ 
                        InformationSet("Click on ACU DB's 50b/60a button", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_CLICK_MAN_TUNE_BUTTON(ClinicalIntegrationTestProcedure):
    name = "Click on Man Tune button"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonNameEvent(0,[["pts_layout:pts_layout_mantune_btn"]])
        info_exchange = [ 
                        InformationSet("Click on Man Tune button", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_CLICK_PHASE_SPACE_BUTTON(ClinicalIntegrationTestProcedure):
    name = "Click on Phase space button"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonNameEvent(0,[["pts_layout:pts_layout_phasespace_btn"]])
        info_exchange = [ 
                        InformationSet("Click on Phase Space button", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_CLICK_SQUARE_BUTTON(ClinicalIntegrationTestProcedure):
    name = "Click on small square button on the top right corner"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonNameEvent(0,[["pts_layout:PlainView_hidden_object"]])
        info_exchange = [ 
                        InformationSet("Click on small square button on the top right corner", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_CLICK_SAVE_TR1_NOZZLE_BUTTON(ClinicalIntegrationTestProcedure):
    name = "Click on Save TR1 Nozzle button"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonNameEvent(0,[["pts_layout:pts_layout_save_tr1_nozzle_btn"]])
        info_exchange = [ 
                        InformationSet("Click on button 'Save TR1 Nozzle'", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []        

class SETUP_CLICK_EDIT_TR1_NOZZLE_BUTTON(ClinicalIntegrationTestProcedure):
    name = "Click on Edit TR1 Nozzle button"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonNameEvent(0,[["pts_layout:pts_layout_edit_tr1_nozzle_btn"]])
        info_exchange = [ 
                        InformationSet("Click on button 'Edit TR1 Nozzle'", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []           

class SETUP_CLICK_SAVE_TR2_NOZZLE_BUTTON(ClinicalIntegrationTestProcedure):
    name = "Click on Save TR2 Nozzle button"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonNameEvent(0,[["pts_layout:pts_layout_save_tr2_nozzle_btn"]])
        info_exchange = [ 
                        InformationSet("Click on button 'Save TR2 Nozzle'", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []        

class SETUP_CLICK_EDIT_TR2_NOZZLE_BUTTON(ClinicalIntegrationTestProcedure):
    name = "Click on Edit TR2 Nozzle button"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonNameEvent(0,[["pts_layout:pts_layout_edit_tr2_nozzle_btn"]])
        info_exchange = [ 
                        InformationSet("Click on button 'Edit TR2 Nozzle'", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []          

class SETUP_KILL_NEDIT_EDITOR(ClinicalIntegrationTestProcedure):
    name = "Kill nedit editor process"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        kill_nedit = "ps -ef | grep nedit | grep -v -e grep | awk '{print $2}' | xargs kill"
        # kill_editor_nedit_hp_ux = MsgMCRHciDumpGuiData(type_in = MCR_HP_SEND_CMD, variable_in = kill_nedit) 
        kill_editor_nedit_hp_ux = MsgExecuteHpUxCmd(option = "", cmd_in = kill_nedit) 

        info_exchange = [ 
                        InformationSet("kill editor 'nedit' on hp_ux", "thriver", "mcrhci", kill_editor_nedit_hp_ux), 
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []          

class SETUP_EXECUTE_CMD_LINUX(ClinicalIntegrationTestProcedure):
    name = "Execute Linux command"
    cmd = None
    def __init__(self, test):
        cls = type(self)
        name = cls.name
        sms1 = TcsExecuteExtCmd(self.cmd)
        info_exchange = [            
                        InformationSet("excecute cmd = {cmd}".format(cmd = self.cmd), "thriver", "mcrhci", sms1),
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup_path = []
        self.teardown_path = []

class SETUP_CLICK_TO_PLANVIEW_MENU_BUTTON(ClinicalIntegrationTestProcedure):
    name = "Click on planview menu button"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonPositionEvent(9, [[120, 220]])    

        info_exchange = [
                        InformationSet("Click to Plainview button on the main menu", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []        