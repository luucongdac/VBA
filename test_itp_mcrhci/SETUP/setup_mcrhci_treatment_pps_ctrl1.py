from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.infoset.tcsobject.dba_objects import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_thriver_wait import SETUP_THRIVER_WAIT
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_msg_dialog_screen import SETUP_CLICK_OK_BUTTON_MSG_DIALOG 
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_login_screen import SETUP_INPUT_USERNAME
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_login_screen import SETUP_INPUT_PASSWORD
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_login_screen import SETUP_CLICK_OK_LOGIN_BUTTON
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_select_session_screen import SETUP_SELECT_TREATMENT_SESSION
from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import *

class THRIVER_WAIT_10_SECONDS(SETUP_THRIVER_WAIT):
    time = 10 

class THRIVER_WAIT_5_SECONDS(SETUP_THRIVER_WAIT):
    time = 5

class SETUP_CLICK_PLAN_VIEW_IN_MAIN_MENU(SETUP_CLICK_BUTTON_BY_POSITION):
    name = "Click Plan View in Treatment Main Menu according to its position"
    button_pos_x = 120
    button_pos_y = 220

class SETUP_CLICK_TR1_PPS_DATA_BTN(SETUP_CLICK_BUTTON_BY_NAME):
    name = "Click TR1 PPS Data button in ptslayout screen according to its name"
    button_name = "pts_layout:pts_layout_tr1_pps_data_btn"

class SETUP_OPEN_VIEW_PPS_CTRL1(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Navigate to Treatment PPS Ctrl 1 Screen"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =[
					SETUP_CLICK_PLAN_VIEW_IN_MAIN_MENU,
					THRIVER_WAIT_5_SECONDS,
					SETUP_CLICK_TR1_PPS_DATA_BTN,
					THRIVER_WAIT_5_SECONDS,
					]
		self.teardown_path = []

class SETUP_VALIDATE_DEFAULT_PPS_CTRL1(ClinicalIntegrationTestProcedure):
    # default variable values
    name = "Set up to validate default of objects when opening view PPS Ctrl 1"

    def __init__(self, test):
        cls = type(self)
        name = cls.name
        mcr_treatment_pps_ctrl1_pps_ctrl1_2_visibility_expected= "1"
        mcr_treatment_pps_ctrl1_pcu4_longtxt_visibility_expected= "1"
        mcr_treatment_pps_ctrl1_pcu4_longtxt_value_expected= 0
        mcr_treatment_pps_ctrl1_pps_ctrl1_6_visibility_expected= "1"
        mcr_treatment_pps_ctrl1_pcu4_rolltxt_visibility_expected= "1"
        mcr_treatment_pps_ctrl1_pcu4_rolltxt_value_expected= 0
        mcr_treatment_pps_ctrl1_pps_ctrl1_1_visibility_expected= "1"
        mcr_treatment_pps_ctrl1_pps_ctrl1_3_visibility_expected= "1"
        mcr_treatment_pps_ctrl1_pps_ctrl1_4_visibility_expected= "1"
        mcr_treatment_pps_ctrl1_pps_ctrl1_5_visibility_expected= "1"
        mcr_treatment_pps_ctrl1_pcu4_pitchtxt_visibility_expected= "1"
        mcr_treatment_pps_ctrl1_pcu4_pitchtxt_value_expected= 0
        mcr_treatment_pps_ctrl1_pcu4_rottxt_visibility_expected= "1"
        mcr_treatment_pps_ctrl1_pcu4_rottxt_value_expected= 0
        mcr_treatment_pps_ctrl1_pcu4_verttxt_visibility_expected= "1"
        mcr_treatment_pps_ctrl1_pcu4_verttxt_value_expected= 0
        mcr_treatment_pps_ctrl1_pcu4_lattxt_visibility_expected= "1"
        mcr_treatment_pps_ctrl1_pcu4_lattxt_value_expected= 0
        mcr_treatment_pps_ctrl1_pcu4_xnel_subobject_name_expected= "iba_check_notok.sd"
        mcr_treatment_pps_ctrl1_pcu4_xhomels_subobject_name_expected= "iba_check_notok.sd"
        mcr_treatment_pps_ctrl1_pcu4_xpel_subobject_name_expected= "iba_check_notok.sd"
        mcr_treatment_pps_ctrl1_pcu4_safetyintlk_subobject_name_expected= "iba_check_notok.sd"
        mcr_treatment_pps_ctrl1_pcu4_xactivated_subobject_name_expected= "iba_check_notok.sd"
        mcr_treatment_pps_ctrl1_pcu4_ynel_subobject_name_expected= "iba_check_notok.sd"
        mcr_treatment_pps_ctrl1_pcu4_yhomels_subobject_name_expected= "iba_check_notok.sd"
        mcr_treatment_pps_ctrl1_pcu4_ypel_subobject_name_expected= "iba_check_notok.sd"
        mcr_treatment_pps_ctrl1_pcu4_yactivated_subobject_name_expected= "iba_check_notok.sd"
        mcr_treatment_pps_ctrl1_pcu4_znel_subobject_name_expected= "iba_check_notok.sd"
        mcr_treatment_pps_ctrl1_pcu4_zhomels_subobject_name_expected= "iba_check_notok.sd"
        mcr_treatment_pps_ctrl1_pcu4_zpel_subobject_name_expected= "iba_check_notok.sd"
        mcr_treatment_pps_ctrl1_pcu4_zactivated_subobject_name_expected= "iba_check_notok.sd"
        mcr_treatment_pps_ctrl1_pcu4_rotnel_subobject_name_expected= "iba_check_notok.sd"
        mcr_treatment_pps_ctrl1_pcu4_rothomels_subobject_name_expected= "iba_check_notok.sd"
        mcr_treatment_pps_ctrl1_pcu4_rotpel_subobject_name_expected= "iba_check_notok.sd"
        mcr_treatment_pps_ctrl1_pcu4_rotactivated_subobject_name_expected= "iba_check_notok.sd"
        mcr_treatment_pps_ctrl1_pcu4_pitchnel_subobject_name_expected= "iba_check_notok.sd"
        mcr_treatment_pps_ctrl1_pcu4_pitchhomels_subobject_name_expected= "iba_check_notok.sd"
        mcr_treatment_pps_ctrl1_pcu4_pitchpel_subobject_name_expected= "iba_check_notok.sd"
        mcr_treatment_pps_ctrl1_pcu4_pitchactivated_subobject_name_expected= "iba_check_notok.sd"
        mcr_treatment_pps_ctrl1_pcu4_rollnel_subobject_name_expected= "iba_check_notok.sd"
        mcr_treatment_pps_ctrl1_pcu4_rollhomels_subobject_name_expected= "iba_check_notok.sd"
        mcr_treatment_pps_ctrl1_pcu4_rollpel_subobject_name_expected= "iba_check_notok.sd"
        mcr_treatment_pps_ctrl1_pcu4_rollactivated_subobject_name_expected= "iba_check_notok.sd"
        mcr_treatment_pps_ctrl1_pcu4_safetyintlklbl_foreground_color_expected= "8"
        mcr_treatment_pps_ctrl1_pcu4_xcmfbk_value_expected= 0
        mcr_treatment_pps_ctrl1_pcu4_xcmmonitoringfbk_value_expected= 0
        mcr_treatment_pps_ctrl1_pcu4_xfollowingerrfbk_value_expected= 0
        mcr_treatment_pps_ctrl1_pcu4_ycmfbk_value_expected= 0
        mcr_treatment_pps_ctrl1_pcu4_ycmmonitoringfbk_value_expected= 0
        mcr_treatment_pps_ctrl1_pcu4_yfollowingerrfbk_value_expected= 0
        mcr_treatment_pps_ctrl1_pcu4_zcmfbk_value_expected= 0
        mcr_treatment_pps_ctrl1_pcu4_zcmmonitoringfbk_value_expected= 0
        mcr_treatment_pps_ctrl1_pcu4_zfollowingerrfbk_value_expected= 0
        mcr_treatment_pps_ctrl1_pcu4_rotdegfbk_value_expected= 0
        mcr_treatment_pps_ctrl1_pcu4_rotdegmonitoringfbk_value_expected= 0
        mcr_treatment_pps_ctrl1_pcu4_rotfollowingerrfbk_value_expected= 0
        mcr_treatment_pps_ctrl1_pcu4_pitchdegfbk_value_expected= 0
        mcr_treatment_pps_ctrl1_pcu4_pitchdegmonitoringfbk_value_expected= 0
        mcr_treatment_pps_ctrl1_pcu4_pitchfollowingerrfbk_value_expected= 0
        mcr_treatment_pps_ctrl1_pcu4_rolldegfbk_value_expected= 0
        mcr_treatment_pps_ctrl1_pcu4_rolldegmonitoringfbk_value_expected= 0
        mcr_treatment_pps_ctrl1_pcu4_rollfollowingerrfbk_value_expected= 0
        mcr_treatment_pps_ctrl1_pcu4_xforceeng_value_expected= 0
        mcr_treatment_pps_ctrl1_pcu4_yforceeng_text_expected= "N/A"
        mcr_treatment_pps_ctrl1_pcu4_zforceeng_value_expected= 0
        mcr_treatment_pps_ctrl1_pcu4_xtorqueeng_value_expected= 0
        mcr_treatment_pps_ctrl1_pcu4_ytorqueeng_value_expected= 0
        mcr_treatment_pps_ctrl1_pcu4_ztorqueeng_value_expected= 0
        mcr_treatment_pps_ctrl1_pcu4_xforceraw_value_expected= 0
        mcr_treatment_pps_ctrl1_pcu4_yforceraw_text_expected= "N/A"
        mcr_treatment_pps_ctrl1_pcu4_zforceraw_value_expected= 0
        mcr_treatment_pps_ctrl1_pcu4_xtorqueraw_value_expected= 0
        mcr_treatment_pps_ctrl1_pcu4_ytorqueraw_value_expected= 0
        mcr_treatment_pps_ctrl1_pcu4_ztorqueraw_value_expected= 0
        mcr_treatment_pps_ctrl1_pcu4_motionmode_value_expected= 0
        mcr_treatment_pps_ctrl1_pcu4_couchlong_visibility_expected= "0"
        mcr_treatment_pps_ctrl1_pcu4_couchshort_visibility_expected= "0"
        mcr_treatment_pps_ctrl1_pcu4_couchext_visibility_expected= "0"
        mcr_treatment_pps_ctrl1_pcu4_coldetected_subobject_name_expected= "iba_info_notok.sd"
        mcr_treatment_pps_ctrl1_pcu4_proxdetected_subobject_name_expected= "iba_info_notok.sd"
        mcr_treatment_pps_ctrl1_pcu4_xnel_1_subobject_name_expected= "iba_check_ok.sd"
        mcr_treatment_pps_ctrl1_pcu4_xtorquerawoffset_value_expected= 0
        mcr_treatment_pps_ctrl1_pcu4_ytorquerawoffset_value_expected= 0
        mcr_treatment_pps_ctrl1_pcu4_ztorquerawoffset_value_expected= 0
        mcr_treatment_pps_ctrl1_pcu4_xforcerawoffset_value_expected= 0
        mcr_treatment_pps_ctrl1_pcu4_yforcerawoffset_text_expected= "N/A"
        mcr_treatment_pps_ctrl1_pcu4_zforcerawoffset_value_expected= 0

        # get values
        get_mcr_treatment_pps_ctrl1_pps_ctrl1_2_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_pps_ctrl1:pps_ctrl1_2")
        get_mcr_treatment_pps_ctrl1_pcu4_longtxt_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_longtxt")
        get_mcr_treatment_pps_ctrl1_pcu4_longtxt_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_longtxt")
        get_mcr_treatment_pps_ctrl1_pps_ctrl1_6_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_pps_ctrl1:pps_ctrl1_6")
        get_mcr_treatment_pps_ctrl1_pcu4_rolltxt_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_rolltxt")
        get_mcr_treatment_pps_ctrl1_pcu4_rolltxt_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_rolltxt")
        get_mcr_treatment_pps_ctrl1_pps_ctrl1_1_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_pps_ctrl1:pps_ctrl1_1")
        get_mcr_treatment_pps_ctrl1_pps_ctrl1_3_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_pps_ctrl1:pps_ctrl1_3")
        get_mcr_treatment_pps_ctrl1_pps_ctrl1_4_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_pps_ctrl1:pps_ctrl1_4")
        get_mcr_treatment_pps_ctrl1_pps_ctrl1_5_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_pps_ctrl1:pps_ctrl1_5")
        get_mcr_treatment_pps_ctrl1_pcu4_pitchtxt_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_pitchtxt")
        get_mcr_treatment_pps_ctrl1_pcu4_pitchtxt_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_pitchtxt")
        get_mcr_treatment_pps_ctrl1_pcu4_rottxt_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_rottxt")
        get_mcr_treatment_pps_ctrl1_pcu4_rottxt_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_rottxt")
        get_mcr_treatment_pps_ctrl1_pcu4_verttxt_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_verttxt")
        get_mcr_treatment_pps_ctrl1_pcu4_verttxt_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_verttxt")
        get_mcr_treatment_pps_ctrl1_pcu4_lattxt_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_lattxt")
        get_mcr_treatment_pps_ctrl1_pcu4_lattxt_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_lattxt")
        get_mcr_treatment_pps_ctrl1_pcu4_xnel_subobject_name= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "mcr_treatment_pps_ctrl1:pcu4_xnel")
        get_mcr_treatment_pps_ctrl1_pcu4_xhomels_subobject_name= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "mcr_treatment_pps_ctrl1:pcu4_xhomels")
        get_mcr_treatment_pps_ctrl1_pcu4_xpel_subobject_name= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "mcr_treatment_pps_ctrl1:pcu4_xpel")
        get_mcr_treatment_pps_ctrl1_pcu4_safetyintlk_subobject_name= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "mcr_treatment_pps_ctrl1:pcu4_safetyintlk")
        get_mcr_treatment_pps_ctrl1_pcu4_xactivated_subobject_name= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "mcr_treatment_pps_ctrl1:pcu4_xactivated")
        get_mcr_treatment_pps_ctrl1_pcu4_ynel_subobject_name= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "mcr_treatment_pps_ctrl1:pcu4_ynel")
        get_mcr_treatment_pps_ctrl1_pcu4_yhomels_subobject_name= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "mcr_treatment_pps_ctrl1:pcu4_yhomels")
        get_mcr_treatment_pps_ctrl1_pcu4_ypel_subobject_name= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "mcr_treatment_pps_ctrl1:pcu4_ypel")
        get_mcr_treatment_pps_ctrl1_pcu4_yactivated_subobject_name= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "mcr_treatment_pps_ctrl1:pcu4_yactivated")
        get_mcr_treatment_pps_ctrl1_pcu4_znel_subobject_name= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "mcr_treatment_pps_ctrl1:pcu4_znel")
        get_mcr_treatment_pps_ctrl1_pcu4_zhomels_subobject_name= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "mcr_treatment_pps_ctrl1:pcu4_zhomels")
        get_mcr_treatment_pps_ctrl1_pcu4_zpel_subobject_name= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "mcr_treatment_pps_ctrl1:pcu4_zpel")
        get_mcr_treatment_pps_ctrl1_pcu4_zactivated_subobject_name= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "mcr_treatment_pps_ctrl1:pcu4_zactivated")
        get_mcr_treatment_pps_ctrl1_pcu4_rotnel_subobject_name= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "mcr_treatment_pps_ctrl1:pcu4_rotnel")
        get_mcr_treatment_pps_ctrl1_pcu4_rothomels_subobject_name= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "mcr_treatment_pps_ctrl1:pcu4_rothomels")
        get_mcr_treatment_pps_ctrl1_pcu4_rotpel_subobject_name= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "mcr_treatment_pps_ctrl1:pcu4_rotpel")
        get_mcr_treatment_pps_ctrl1_pcu4_rotactivated_subobject_name= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "mcr_treatment_pps_ctrl1:pcu4_rotactivated")
        get_mcr_treatment_pps_ctrl1_pcu4_pitchnel_subobject_name= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "mcr_treatment_pps_ctrl1:pcu4_pitchnel")
        get_mcr_treatment_pps_ctrl1_pcu4_pitchhomels_subobject_name= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "mcr_treatment_pps_ctrl1:pcu4_pitchhomels")
        get_mcr_treatment_pps_ctrl1_pcu4_pitchpel_subobject_name= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "mcr_treatment_pps_ctrl1:pcu4_pitchpel")
        get_mcr_treatment_pps_ctrl1_pcu4_pitchactivated_subobject_name= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "mcr_treatment_pps_ctrl1:pcu4_pitchactivated")
        get_mcr_treatment_pps_ctrl1_pcu4_rollnel_subobject_name= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "mcr_treatment_pps_ctrl1:pcu4_rollnel")
        get_mcr_treatment_pps_ctrl1_pcu4_rollhomels_subobject_name= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "mcr_treatment_pps_ctrl1:pcu4_rollhomels")
        get_mcr_treatment_pps_ctrl1_pcu4_rollpel_subobject_name= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "mcr_treatment_pps_ctrl1:pcu4_rollpel")
        get_mcr_treatment_pps_ctrl1_pcu4_rollactivated_subobject_name= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "mcr_treatment_pps_ctrl1:pcu4_rollactivated")
        get_mcr_treatment_pps_ctrl1_pcu4_safetyintlklbl_foreground_color= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_treatment_pps_ctrl1:pcu4_safetyintlklbl")
        get_mcr_treatment_pps_ctrl1_pcu4_xcmfbk_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_xcmfbk")
        get_mcr_treatment_pps_ctrl1_pcu4_xcmmonitoringfbk_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_xcmmonitoringfbk")
        get_mcr_treatment_pps_ctrl1_pcu4_xfollowingerrfbk_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_xfollowingerrfbk")
        get_mcr_treatment_pps_ctrl1_pcu4_ycmfbk_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_ycmfbk")
        get_mcr_treatment_pps_ctrl1_pcu4_ycmmonitoringfbk_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_ycmmonitoringfbk")
        get_mcr_treatment_pps_ctrl1_pcu4_yfollowingerrfbk_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_yfollowingerrfbk")
        get_mcr_treatment_pps_ctrl1_pcu4_zcmfbk_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_zcmfbk")
        get_mcr_treatment_pps_ctrl1_pcu4_zcmmonitoringfbk_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_zcmmonitoringfbk")
        get_mcr_treatment_pps_ctrl1_pcu4_zfollowingerrfbk_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_zfollowingerrfbk")
        get_mcr_treatment_pps_ctrl1_pcu4_rotdegfbk_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_rotdegfbk")
        get_mcr_treatment_pps_ctrl1_pcu4_rotdegmonitoringfbk_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_rotdegmonitoringfbk")
        get_mcr_treatment_pps_ctrl1_pcu4_rotfollowingerrfbk_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_rotfollowingerrfbk")
        get_mcr_treatment_pps_ctrl1_pcu4_pitchdegfbk_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_pitchdegfbk")
        get_mcr_treatment_pps_ctrl1_pcu4_pitchdegmonitoringfbk_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_pitchdegmonitoringfbk")
        get_mcr_treatment_pps_ctrl1_pcu4_pitchfollowingerrfbk_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_pitchfollowingerrfbk")
        get_mcr_treatment_pps_ctrl1_pcu4_rolldegfbk_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_rolldegfbk")
        get_mcr_treatment_pps_ctrl1_pcu4_rolldegmonitoringfbk_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_rolldegmonitoringfbk")
        get_mcr_treatment_pps_ctrl1_pcu4_rollfollowingerrfbk_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_rollfollowingerrfbk")
        get_mcr_treatment_pps_ctrl1_pcu4_xforceeng_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_xforceeng")
        get_mcr_treatment_pps_ctrl1_pcu4_yforceeng_text= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_TEXT_FIELD, variable_in = "mcr_treatment_pps_ctrl1:pcu4_yforceeng")
        get_mcr_treatment_pps_ctrl1_pcu4_zforceeng_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_zforceeng")
        get_mcr_treatment_pps_ctrl1_pcu4_xtorqueeng_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_xtorqueeng")
        get_mcr_treatment_pps_ctrl1_pcu4_ytorqueeng_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_ytorqueeng")
        get_mcr_treatment_pps_ctrl1_pcu4_ztorqueeng_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_ztorqueeng")
        get_mcr_treatment_pps_ctrl1_pcu4_xforceraw_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_xforceraw")
        get_mcr_treatment_pps_ctrl1_pcu4_yforceraw_text= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_TEXT_FIELD, variable_in = "mcr_treatment_pps_ctrl1:pcu4_yforceraw")
        get_mcr_treatment_pps_ctrl1_pcu4_zforceraw_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_zforceraw")
        get_mcr_treatment_pps_ctrl1_pcu4_xtorqueraw_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_xtorqueraw")
        get_mcr_treatment_pps_ctrl1_pcu4_ytorqueraw_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_ytorqueraw")
        get_mcr_treatment_pps_ctrl1_pcu4_ztorqueraw_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_ztorqueraw")
        get_mcr_treatment_pps_ctrl1_pcu4_motionmode_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_motionmode")
        get_mcr_treatment_pps_ctrl1_pcu4_couchlong_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_couchlong")
        get_mcr_treatment_pps_ctrl1_pcu4_couchshort_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_couchshort")
        get_mcr_treatment_pps_ctrl1_pcu4_couchext_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_couchext")
        get_mcr_treatment_pps_ctrl1_pcu4_coldetected_subobject_name= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "mcr_treatment_pps_ctrl1:pcu4_coldetected")
        get_mcr_treatment_pps_ctrl1_pcu4_proxdetected_subobject_name= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "mcr_treatment_pps_ctrl1:pcu4_proxdetected")
        get_mcr_treatment_pps_ctrl1_pcu4_xnel_1_subobject_name= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME, variable_in = "mcr_treatment_pps_ctrl1:pcu4_xnel_1")
        get_mcr_treatment_pps_ctrl1_pcu4_xtorquerawoffset_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_xtorquerawoffset")
        get_mcr_treatment_pps_ctrl1_pcu4_ytorquerawoffset_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_ytorquerawoffset")
        get_mcr_treatment_pps_ctrl1_pcu4_ztorquerawoffset_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_ztorquerawoffset")
        get_mcr_treatment_pps_ctrl1_pcu4_xforcerawoffset_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_xforcerawoffset")
        get_mcr_treatment_pps_ctrl1_pcu4_yforcerawoffset_text= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_TEXT_FIELD, variable_in = "mcr_treatment_pps_ctrl1:pcu4_yforcerawoffset")
        get_mcr_treatment_pps_ctrl1_pcu4_zforcerawoffset_value= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "mcr_treatment_pps_ctrl1:pcu4_zforcerawoffset")

        # validate
        validate_mcr_treatment_pps_ctrl1_pps_ctrl1_2_visibility= MsgTypeString("mcr_treatment_pps_ctrl1:pps_ctrl1_2:TMMI_MCR_IS_VISIBLE", value=mcr_treatment_pps_ctrl1_pps_ctrl1_2_visibility_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_longtxt_visibility= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_longtxt:TMMI_MCR_IS_VISIBLE", value=mcr_treatment_pps_ctrl1_pcu4_longtxt_visibility_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_longtxt_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_longtxt:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_longtxt_value_expected)
        validate_mcr_treatment_pps_ctrl1_pps_ctrl1_6_visibility= MsgTypeString("mcr_treatment_pps_ctrl1:pps_ctrl1_6:TMMI_MCR_IS_VISIBLE", value=mcr_treatment_pps_ctrl1_pps_ctrl1_6_visibility_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_rolltxt_visibility= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_rolltxt:TMMI_MCR_IS_VISIBLE", value=mcr_treatment_pps_ctrl1_pcu4_rolltxt_visibility_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_rolltxt_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_rolltxt:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_rolltxt_value_expected)
        validate_mcr_treatment_pps_ctrl1_pps_ctrl1_1_visibility= MsgTypeString("mcr_treatment_pps_ctrl1:pps_ctrl1_1:TMMI_MCR_IS_VISIBLE", value=mcr_treatment_pps_ctrl1_pps_ctrl1_1_visibility_expected)
        validate_mcr_treatment_pps_ctrl1_pps_ctrl1_3_visibility= MsgTypeString("mcr_treatment_pps_ctrl1:pps_ctrl1_3:TMMI_MCR_IS_VISIBLE", value=mcr_treatment_pps_ctrl1_pps_ctrl1_3_visibility_expected)
        validate_mcr_treatment_pps_ctrl1_pps_ctrl1_4_visibility= MsgTypeString("mcr_treatment_pps_ctrl1:pps_ctrl1_4:TMMI_MCR_IS_VISIBLE", value=mcr_treatment_pps_ctrl1_pps_ctrl1_4_visibility_expected)
        validate_mcr_treatment_pps_ctrl1_pps_ctrl1_5_visibility= MsgTypeString("mcr_treatment_pps_ctrl1:pps_ctrl1_5:TMMI_MCR_IS_VISIBLE", value=mcr_treatment_pps_ctrl1_pps_ctrl1_5_visibility_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_pitchtxt_visibility= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_pitchtxt:TMMI_MCR_IS_VISIBLE", value=mcr_treatment_pps_ctrl1_pcu4_pitchtxt_visibility_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_pitchtxt_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_pitchtxt:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_pitchtxt_value_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_rottxt_visibility= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_rottxt:TMMI_MCR_IS_VISIBLE", value=mcr_treatment_pps_ctrl1_pcu4_rottxt_visibility_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_rottxt_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_rottxt:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_rottxt_value_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_verttxt_visibility= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_verttxt:TMMI_MCR_IS_VISIBLE", value=mcr_treatment_pps_ctrl1_pcu4_verttxt_visibility_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_verttxt_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_verttxt:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_verttxt_value_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_lattxt_visibility= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_lattxt:TMMI_MCR_IS_VISIBLE", value=mcr_treatment_pps_ctrl1_pcu4_lattxt_visibility_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_lattxt_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_lattxt:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_lattxt_value_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_xnel_subobject_name= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_xnel:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=mcr_treatment_pps_ctrl1_pcu4_xnel_subobject_name_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_xhomels_subobject_name= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_xhomels:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=mcr_treatment_pps_ctrl1_pcu4_xhomels_subobject_name_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_xpel_subobject_name= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_xpel:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=mcr_treatment_pps_ctrl1_pcu4_xpel_subobject_name_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_safetyintlk_subobject_name= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_safetyintlk:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=mcr_treatment_pps_ctrl1_pcu4_safetyintlk_subobject_name_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_xactivated_subobject_name= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_xactivated:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=mcr_treatment_pps_ctrl1_pcu4_xactivated_subobject_name_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_ynel_subobject_name= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_ynel:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=mcr_treatment_pps_ctrl1_pcu4_ynel_subobject_name_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_yhomels_subobject_name= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_yhomels:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=mcr_treatment_pps_ctrl1_pcu4_yhomels_subobject_name_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_ypel_subobject_name= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_ypel:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=mcr_treatment_pps_ctrl1_pcu4_ypel_subobject_name_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_yactivated_subobject_name= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_yactivated:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=mcr_treatment_pps_ctrl1_pcu4_yactivated_subobject_name_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_znel_subobject_name= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_znel:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=mcr_treatment_pps_ctrl1_pcu4_znel_subobject_name_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_zhomels_subobject_name= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_zhomels:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=mcr_treatment_pps_ctrl1_pcu4_zhomels_subobject_name_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_zpel_subobject_name= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_zpel:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=mcr_treatment_pps_ctrl1_pcu4_zpel_subobject_name_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_zactivated_subobject_name= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_zactivated:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=mcr_treatment_pps_ctrl1_pcu4_zactivated_subobject_name_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_rotnel_subobject_name= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_rotnel:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=mcr_treatment_pps_ctrl1_pcu4_rotnel_subobject_name_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_rothomels_subobject_name= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_rothomels:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=mcr_treatment_pps_ctrl1_pcu4_rothomels_subobject_name_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_rotpel_subobject_name= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_rotpel:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=mcr_treatment_pps_ctrl1_pcu4_rotpel_subobject_name_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_rotactivated_subobject_name= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_rotactivated:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=mcr_treatment_pps_ctrl1_pcu4_rotactivated_subobject_name_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_pitchnel_subobject_name= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_pitchnel:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=mcr_treatment_pps_ctrl1_pcu4_pitchnel_subobject_name_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_pitchhomels_subobject_name= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_pitchhomels:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=mcr_treatment_pps_ctrl1_pcu4_pitchhomels_subobject_name_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_pitchpel_subobject_name= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_pitchpel:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=mcr_treatment_pps_ctrl1_pcu4_pitchpel_subobject_name_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_pitchactivated_subobject_name= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_pitchactivated:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=mcr_treatment_pps_ctrl1_pcu4_pitchactivated_subobject_name_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_rollnel_subobject_name= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_rollnel:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=mcr_treatment_pps_ctrl1_pcu4_rollnel_subobject_name_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_rollhomels_subobject_name= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_rollhomels:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=mcr_treatment_pps_ctrl1_pcu4_rollhomels_subobject_name_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_rollpel_subobject_name= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_rollpel:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=mcr_treatment_pps_ctrl1_pcu4_rollpel_subobject_name_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_rollactivated_subobject_name= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_rollactivated:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=mcr_treatment_pps_ctrl1_pcu4_rollactivated_subobject_name_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_safetyintlklbl_foreground_color= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_safetyintlklbl:TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value=mcr_treatment_pps_ctrl1_pcu4_safetyintlklbl_foreground_color_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_xcmfbk_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_xcmfbk:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_xcmfbk_value_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_xcmmonitoringfbk_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_xcmmonitoringfbk:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_xcmmonitoringfbk_value_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_xfollowingerrfbk_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_xfollowingerrfbk:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_xfollowingerrfbk_value_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_ycmfbk_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_ycmfbk:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_ycmfbk_value_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_ycmmonitoringfbk_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_ycmmonitoringfbk:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_ycmmonitoringfbk_value_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_yfollowingerrfbk_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_yfollowingerrfbk:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_yfollowingerrfbk_value_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_zcmfbk_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_zcmfbk:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_zcmfbk_value_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_zcmmonitoringfbk_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_zcmmonitoringfbk:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_zcmmonitoringfbk_value_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_zfollowingerrfbk_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_zfollowingerrfbk:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_zfollowingerrfbk_value_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_rotdegfbk_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_rotdegfbk:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_rotdegfbk_value_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_rotdegmonitoringfbk_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_rotdegmonitoringfbk:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_rotdegmonitoringfbk_value_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_rotfollowingerrfbk_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_rotfollowingerrfbk:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_rotfollowingerrfbk_value_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_pitchdegfbk_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_pitchdegfbk:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_pitchdegfbk_value_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_pitchdegmonitoringfbk_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_pitchdegmonitoringfbk:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_pitchdegmonitoringfbk_value_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_pitchfollowingerrfbk_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_pitchfollowingerrfbk:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_pitchfollowingerrfbk_value_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_rolldegfbk_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_rolldegfbk:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_rolldegfbk_value_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_rolldegmonitoringfbk_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_rolldegmonitoringfbk:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_rolldegmonitoringfbk_value_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_rollfollowingerrfbk_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_rollfollowingerrfbk:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_rollfollowingerrfbk_value_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_xforceeng_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_xforceeng:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_xforceeng_value_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_yforceeng_text= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_yforceeng:TMMI_MCR_TEXT_FIELD", value=mcr_treatment_pps_ctrl1_pcu4_yforceeng_text_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_zforceeng_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_zforceeng:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_zforceeng_value_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_xtorqueeng_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_xtorqueeng:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_xtorqueeng_value_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_ytorqueeng_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_ytorqueeng:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_ytorqueeng_value_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_ztorqueeng_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_ztorqueeng:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_ztorqueeng_value_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_xforceraw_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_xforceraw:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_xforceraw_value_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_yforceraw_text= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_yforceraw:TMMI_MCR_TEXT_FIELD", value=mcr_treatment_pps_ctrl1_pcu4_yforceraw_text_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_zforceraw_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_zforceraw:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_zforceraw_value_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_xtorqueraw_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_xtorqueraw:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_xtorqueraw_value_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_ytorqueraw_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_ytorqueraw:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_ytorqueraw_value_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_ztorqueraw_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_ztorqueraw:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_ztorqueraw_value_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_motionmode_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_motionmode:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_motionmode_value_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_couchlong_visibility= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_couchlong:TMMI_MCR_IS_VISIBLE", value=mcr_treatment_pps_ctrl1_pcu4_couchlong_visibility_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_couchshort_visibility= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_couchshort:TMMI_MCR_IS_VISIBLE", value=mcr_treatment_pps_ctrl1_pcu4_couchshort_visibility_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_couchext_visibility= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_couchext:TMMI_MCR_IS_VISIBLE", value=mcr_treatment_pps_ctrl1_pcu4_couchext_visibility_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_coldetected_subobject_name= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_coldetected:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=mcr_treatment_pps_ctrl1_pcu4_coldetected_subobject_name_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_proxdetected_subobject_name= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_proxdetected:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=mcr_treatment_pps_ctrl1_pcu4_proxdetected_subobject_name_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_xnel_1_subobject_name= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_xnel_1:TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME", value=mcr_treatment_pps_ctrl1_pcu4_xnel_1_subobject_name_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_xtorquerawoffset_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_xtorquerawoffset:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_xtorquerawoffset_value_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_ytorquerawoffset_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_ytorquerawoffset:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_ytorquerawoffset_value_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_ztorquerawoffset_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_ztorquerawoffset:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_ztorquerawoffset_value_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_xforcerawoffset_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_xforcerawoffset:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_xforcerawoffset_value_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_yforcerawoffset_text= MsgTypeString("mcr_treatment_pps_ctrl1:pcu4_yforcerawoffset:TMMI_MCR_TEXT_FIELD", value=mcr_treatment_pps_ctrl1_pcu4_yforcerawoffset_text_expected)
        validate_mcr_treatment_pps_ctrl1_pcu4_zforcerawoffset_value= MsgTypeNumeric("mcr_treatment_pps_ctrl1:pcu4_zforcerawoffset:TMMI_MCR_OBJECT_GET_VALUE", value=mcr_treatment_pps_ctrl1_pcu4_zforcerawoffset_value_expected)

        info_exchange = [
                        InformationSet("get mcr_treatment_pps_ctrl1:pps_ctrl1_2visibility", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pps_ctrl1_2_visibility),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pps_ctrl1_2visibilityis equal to {mcr_treatment_pps_ctrl1_pps_ctrl1_2_visibility_expected}".format(mcr_treatment_pps_ctrl1_pps_ctrl1_2_visibility_expected=mcr_treatment_pps_ctrl1_pps_ctrl1_2_visibility_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pps_ctrl1_2_visibility),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_longtxtvisibility", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_longtxt_visibility),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_longtxtvisibilityis equal to {mcr_treatment_pps_ctrl1_pcu4_longtxt_visibility_expected}".format(mcr_treatment_pps_ctrl1_pcu4_longtxt_visibility_expected=mcr_treatment_pps_ctrl1_pcu4_longtxt_visibility_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_longtxt_visibility),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_longtxtvalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_longtxt_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_longtxtvalueis equal to {mcr_treatment_pps_ctrl1_pcu4_longtxt_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_longtxt_value_expected=mcr_treatment_pps_ctrl1_pcu4_longtxt_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_longtxt_value),
                        InformationSet("get mcr_treatment_pps_ctrl1:pps_ctrl1_6visibility", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pps_ctrl1_6_visibility),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pps_ctrl1_6visibilityis equal to {mcr_treatment_pps_ctrl1_pps_ctrl1_6_visibility_expected}".format(mcr_treatment_pps_ctrl1_pps_ctrl1_6_visibility_expected=mcr_treatment_pps_ctrl1_pps_ctrl1_6_visibility_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pps_ctrl1_6_visibility),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_rolltxtvisibility", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_rolltxt_visibility),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_rolltxtvisibilityis equal to {mcr_treatment_pps_ctrl1_pcu4_rolltxt_visibility_expected}".format(mcr_treatment_pps_ctrl1_pcu4_rolltxt_visibility_expected=mcr_treatment_pps_ctrl1_pcu4_rolltxt_visibility_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_rolltxt_visibility),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_rolltxtvalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_rolltxt_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_rolltxtvalueis equal to {mcr_treatment_pps_ctrl1_pcu4_rolltxt_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_rolltxt_value_expected=mcr_treatment_pps_ctrl1_pcu4_rolltxt_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_rolltxt_value),
                        InformationSet("get mcr_treatment_pps_ctrl1:pps_ctrl1_1visibility", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pps_ctrl1_1_visibility),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pps_ctrl1_1visibilityis equal to {mcr_treatment_pps_ctrl1_pps_ctrl1_1_visibility_expected}".format(mcr_treatment_pps_ctrl1_pps_ctrl1_1_visibility_expected=mcr_treatment_pps_ctrl1_pps_ctrl1_1_visibility_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pps_ctrl1_1_visibility),
                        InformationSet("get mcr_treatment_pps_ctrl1:pps_ctrl1_3visibility", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pps_ctrl1_3_visibility),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pps_ctrl1_3visibilityis equal to {mcr_treatment_pps_ctrl1_pps_ctrl1_3_visibility_expected}".format(mcr_treatment_pps_ctrl1_pps_ctrl1_3_visibility_expected=mcr_treatment_pps_ctrl1_pps_ctrl1_3_visibility_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pps_ctrl1_3_visibility),
                        InformationSet("get mcr_treatment_pps_ctrl1:pps_ctrl1_4visibility", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pps_ctrl1_4_visibility),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pps_ctrl1_4visibilityis equal to {mcr_treatment_pps_ctrl1_pps_ctrl1_4_visibility_expected}".format(mcr_treatment_pps_ctrl1_pps_ctrl1_4_visibility_expected=mcr_treatment_pps_ctrl1_pps_ctrl1_4_visibility_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pps_ctrl1_4_visibility),
                        InformationSet("get mcr_treatment_pps_ctrl1:pps_ctrl1_5visibility", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pps_ctrl1_5_visibility),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pps_ctrl1_5visibilityis equal to {mcr_treatment_pps_ctrl1_pps_ctrl1_5_visibility_expected}".format(mcr_treatment_pps_ctrl1_pps_ctrl1_5_visibility_expected=mcr_treatment_pps_ctrl1_pps_ctrl1_5_visibility_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pps_ctrl1_5_visibility),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_pitchtxtvisibility", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_pitchtxt_visibility),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_pitchtxtvisibilityis equal to {mcr_treatment_pps_ctrl1_pcu4_pitchtxt_visibility_expected}".format(mcr_treatment_pps_ctrl1_pcu4_pitchtxt_visibility_expected=mcr_treatment_pps_ctrl1_pcu4_pitchtxt_visibility_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_pitchtxt_visibility),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_pitchtxtvalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_pitchtxt_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_pitchtxtvalueis equal to {mcr_treatment_pps_ctrl1_pcu4_pitchtxt_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_pitchtxt_value_expected=mcr_treatment_pps_ctrl1_pcu4_pitchtxt_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_pitchtxt_value),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_rottxtvisibility", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_rottxt_visibility),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_rottxtvisibilityis equal to {mcr_treatment_pps_ctrl1_pcu4_rottxt_visibility_expected}".format(mcr_treatment_pps_ctrl1_pcu4_rottxt_visibility_expected=mcr_treatment_pps_ctrl1_pcu4_rottxt_visibility_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_rottxt_visibility),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_rottxtvalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_rottxt_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_rottxtvalueis equal to {mcr_treatment_pps_ctrl1_pcu4_rottxt_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_rottxt_value_expected=mcr_treatment_pps_ctrl1_pcu4_rottxt_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_rottxt_value),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_verttxtvisibility", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_verttxt_visibility),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_verttxtvisibilityis equal to {mcr_treatment_pps_ctrl1_pcu4_verttxt_visibility_expected}".format(mcr_treatment_pps_ctrl1_pcu4_verttxt_visibility_expected=mcr_treatment_pps_ctrl1_pcu4_verttxt_visibility_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_verttxt_visibility),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_verttxtvalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_verttxt_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_verttxtvalueis equal to {mcr_treatment_pps_ctrl1_pcu4_verttxt_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_verttxt_value_expected=mcr_treatment_pps_ctrl1_pcu4_verttxt_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_verttxt_value),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_lattxtvisibility", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_lattxt_visibility),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_lattxtvisibilityis equal to {mcr_treatment_pps_ctrl1_pcu4_lattxt_visibility_expected}".format(mcr_treatment_pps_ctrl1_pcu4_lattxt_visibility_expected=mcr_treatment_pps_ctrl1_pcu4_lattxt_visibility_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_lattxt_visibility),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_lattxtvalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_lattxt_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_lattxtvalueis equal to {mcr_treatment_pps_ctrl1_pcu4_lattxt_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_lattxt_value_expected=mcr_treatment_pps_ctrl1_pcu4_lattxt_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_lattxt_value),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_xnelsubobject_name", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_xnel_subobject_name),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_xnelsubobject_nameis equal to {mcr_treatment_pps_ctrl1_pcu4_xnel_subobject_name_expected}".format(mcr_treatment_pps_ctrl1_pcu4_xnel_subobject_name_expected=mcr_treatment_pps_ctrl1_pcu4_xnel_subobject_name_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_xnel_subobject_name),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_xhomelssubobject_name", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_xhomels_subobject_name),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_xhomelssubobject_nameis equal to {mcr_treatment_pps_ctrl1_pcu4_xhomels_subobject_name_expected}".format(mcr_treatment_pps_ctrl1_pcu4_xhomels_subobject_name_expected=mcr_treatment_pps_ctrl1_pcu4_xhomels_subobject_name_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_xhomels_subobject_name),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_xpelsubobject_name", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_xpel_subobject_name),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_xpelsubobject_nameis equal to {mcr_treatment_pps_ctrl1_pcu4_xpel_subobject_name_expected}".format(mcr_treatment_pps_ctrl1_pcu4_xpel_subobject_name_expected=mcr_treatment_pps_ctrl1_pcu4_xpel_subobject_name_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_xpel_subobject_name),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_safetyintlksubobject_name", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_safetyintlk_subobject_name),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_safetyintlksubobject_nameis equal to {mcr_treatment_pps_ctrl1_pcu4_safetyintlk_subobject_name_expected}".format(mcr_treatment_pps_ctrl1_pcu4_safetyintlk_subobject_name_expected=mcr_treatment_pps_ctrl1_pcu4_safetyintlk_subobject_name_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_safetyintlk_subobject_name),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_xactivatedsubobject_name", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_xactivated_subobject_name),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_xactivatedsubobject_nameis equal to {mcr_treatment_pps_ctrl1_pcu4_xactivated_subobject_name_expected}".format(mcr_treatment_pps_ctrl1_pcu4_xactivated_subobject_name_expected=mcr_treatment_pps_ctrl1_pcu4_xactivated_subobject_name_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_xactivated_subobject_name),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_ynelsubobject_name", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_ynel_subobject_name),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_ynelsubobject_nameis equal to {mcr_treatment_pps_ctrl1_pcu4_ynel_subobject_name_expected}".format(mcr_treatment_pps_ctrl1_pcu4_ynel_subobject_name_expected=mcr_treatment_pps_ctrl1_pcu4_ynel_subobject_name_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_ynel_subobject_name),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_yhomelssubobject_name", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_yhomels_subobject_name),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_yhomelssubobject_nameis equal to {mcr_treatment_pps_ctrl1_pcu4_yhomels_subobject_name_expected}".format(mcr_treatment_pps_ctrl1_pcu4_yhomels_subobject_name_expected=mcr_treatment_pps_ctrl1_pcu4_yhomels_subobject_name_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_yhomels_subobject_name),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_ypelsubobject_name", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_ypel_subobject_name),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_ypelsubobject_nameis equal to {mcr_treatment_pps_ctrl1_pcu4_ypel_subobject_name_expected}".format(mcr_treatment_pps_ctrl1_pcu4_ypel_subobject_name_expected=mcr_treatment_pps_ctrl1_pcu4_ypel_subobject_name_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_ypel_subobject_name),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_yactivatedsubobject_name", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_yactivated_subobject_name),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_yactivatedsubobject_nameis equal to {mcr_treatment_pps_ctrl1_pcu4_yactivated_subobject_name_expected}".format(mcr_treatment_pps_ctrl1_pcu4_yactivated_subobject_name_expected=mcr_treatment_pps_ctrl1_pcu4_yactivated_subobject_name_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_yactivated_subobject_name),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_znelsubobject_name", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_znel_subobject_name),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_znelsubobject_nameis equal to {mcr_treatment_pps_ctrl1_pcu4_znel_subobject_name_expected}".format(mcr_treatment_pps_ctrl1_pcu4_znel_subobject_name_expected=mcr_treatment_pps_ctrl1_pcu4_znel_subobject_name_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_znel_subobject_name),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_zhomelssubobject_name", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_zhomels_subobject_name),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_zhomelssubobject_nameis equal to {mcr_treatment_pps_ctrl1_pcu4_zhomels_subobject_name_expected}".format(mcr_treatment_pps_ctrl1_pcu4_zhomels_subobject_name_expected=mcr_treatment_pps_ctrl1_pcu4_zhomels_subobject_name_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_zhomels_subobject_name),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_zpelsubobject_name", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_zpel_subobject_name),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_zpelsubobject_nameis equal to {mcr_treatment_pps_ctrl1_pcu4_zpel_subobject_name_expected}".format(mcr_treatment_pps_ctrl1_pcu4_zpel_subobject_name_expected=mcr_treatment_pps_ctrl1_pcu4_zpel_subobject_name_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_zpel_subobject_name),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_zactivatedsubobject_name", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_zactivated_subobject_name),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_zactivatedsubobject_nameis equal to {mcr_treatment_pps_ctrl1_pcu4_zactivated_subobject_name_expected}".format(mcr_treatment_pps_ctrl1_pcu4_zactivated_subobject_name_expected=mcr_treatment_pps_ctrl1_pcu4_zactivated_subobject_name_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_zactivated_subobject_name),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_rotnelsubobject_name", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_rotnel_subobject_name),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_rotnelsubobject_nameis equal to {mcr_treatment_pps_ctrl1_pcu4_rotnel_subobject_name_expected}".format(mcr_treatment_pps_ctrl1_pcu4_rotnel_subobject_name_expected=mcr_treatment_pps_ctrl1_pcu4_rotnel_subobject_name_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_rotnel_subobject_name),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_rothomelssubobject_name", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_rothomels_subobject_name),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_rothomelssubobject_nameis equal to {mcr_treatment_pps_ctrl1_pcu4_rothomels_subobject_name_expected}".format(mcr_treatment_pps_ctrl1_pcu4_rothomels_subobject_name_expected=mcr_treatment_pps_ctrl1_pcu4_rothomels_subobject_name_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_rothomels_subobject_name),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_rotpelsubobject_name", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_rotpel_subobject_name),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_rotpelsubobject_nameis equal to {mcr_treatment_pps_ctrl1_pcu4_rotpel_subobject_name_expected}".format(mcr_treatment_pps_ctrl1_pcu4_rotpel_subobject_name_expected=mcr_treatment_pps_ctrl1_pcu4_rotpel_subobject_name_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_rotpel_subobject_name),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_rotactivatedsubobject_name", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_rotactivated_subobject_name),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_rotactivatedsubobject_nameis equal to {mcr_treatment_pps_ctrl1_pcu4_rotactivated_subobject_name_expected}".format(mcr_treatment_pps_ctrl1_pcu4_rotactivated_subobject_name_expected=mcr_treatment_pps_ctrl1_pcu4_rotactivated_subobject_name_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_rotactivated_subobject_name),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_pitchnelsubobject_name", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_pitchnel_subobject_name),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_pitchnelsubobject_nameis equal to {mcr_treatment_pps_ctrl1_pcu4_pitchnel_subobject_name_expected}".format(mcr_treatment_pps_ctrl1_pcu4_pitchnel_subobject_name_expected=mcr_treatment_pps_ctrl1_pcu4_pitchnel_subobject_name_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_pitchnel_subobject_name),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_pitchhomelssubobject_name", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_pitchhomels_subobject_name),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_pitchhomelssubobject_nameis equal to {mcr_treatment_pps_ctrl1_pcu4_pitchhomels_subobject_name_expected}".format(mcr_treatment_pps_ctrl1_pcu4_pitchhomels_subobject_name_expected=mcr_treatment_pps_ctrl1_pcu4_pitchhomels_subobject_name_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_pitchhomels_subobject_name),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_pitchpelsubobject_name", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_pitchpel_subobject_name),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_pitchpelsubobject_nameis equal to {mcr_treatment_pps_ctrl1_pcu4_pitchpel_subobject_name_expected}".format(mcr_treatment_pps_ctrl1_pcu4_pitchpel_subobject_name_expected=mcr_treatment_pps_ctrl1_pcu4_pitchpel_subobject_name_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_pitchpel_subobject_name),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_pitchactivatedsubobject_name", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_pitchactivated_subobject_name),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_pitchactivatedsubobject_nameis equal to {mcr_treatment_pps_ctrl1_pcu4_pitchactivated_subobject_name_expected}".format(mcr_treatment_pps_ctrl1_pcu4_pitchactivated_subobject_name_expected=mcr_treatment_pps_ctrl1_pcu4_pitchactivated_subobject_name_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_pitchactivated_subobject_name),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_rollnelsubobject_name", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_rollnel_subobject_name),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_rollnelsubobject_nameis equal to {mcr_treatment_pps_ctrl1_pcu4_rollnel_subobject_name_expected}".format(mcr_treatment_pps_ctrl1_pcu4_rollnel_subobject_name_expected=mcr_treatment_pps_ctrl1_pcu4_rollnel_subobject_name_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_rollnel_subobject_name),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_rollhomelssubobject_name", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_rollhomels_subobject_name),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_rollhomelssubobject_nameis equal to {mcr_treatment_pps_ctrl1_pcu4_rollhomels_subobject_name_expected}".format(mcr_treatment_pps_ctrl1_pcu4_rollhomels_subobject_name_expected=mcr_treatment_pps_ctrl1_pcu4_rollhomels_subobject_name_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_rollhomels_subobject_name),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_rollpelsubobject_name", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_rollpel_subobject_name),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_rollpelsubobject_nameis equal to {mcr_treatment_pps_ctrl1_pcu4_rollpel_subobject_name_expected}".format(mcr_treatment_pps_ctrl1_pcu4_rollpel_subobject_name_expected=mcr_treatment_pps_ctrl1_pcu4_rollpel_subobject_name_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_rollpel_subobject_name),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_rollactivatedsubobject_name", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_rollactivated_subobject_name),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_rollactivatedsubobject_nameis equal to {mcr_treatment_pps_ctrl1_pcu4_rollactivated_subobject_name_expected}".format(mcr_treatment_pps_ctrl1_pcu4_rollactivated_subobject_name_expected=mcr_treatment_pps_ctrl1_pcu4_rollactivated_subobject_name_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_rollactivated_subobject_name),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_safetyintlklblforeground_color", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_safetyintlklbl_foreground_color),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_safetyintlklblforeground_coloris equal to {mcr_treatment_pps_ctrl1_pcu4_safetyintlklbl_foreground_color_expected}".format(mcr_treatment_pps_ctrl1_pcu4_safetyintlklbl_foreground_color_expected=mcr_treatment_pps_ctrl1_pcu4_safetyintlklbl_foreground_color_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_safetyintlklbl_foreground_color),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_xcmfbkvalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_xcmfbk_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_xcmfbkvalueis equal to {mcr_treatment_pps_ctrl1_pcu4_xcmfbk_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_xcmfbk_value_expected=mcr_treatment_pps_ctrl1_pcu4_xcmfbk_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_xcmfbk_value),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_xcmmonitoringfbkvalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_xcmmonitoringfbk_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_xcmmonitoringfbkvalueis equal to {mcr_treatment_pps_ctrl1_pcu4_xcmmonitoringfbk_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_xcmmonitoringfbk_value_expected=mcr_treatment_pps_ctrl1_pcu4_xcmmonitoringfbk_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_xcmmonitoringfbk_value),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_xfollowingerrfbkvalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_xfollowingerrfbk_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_xfollowingerrfbkvalueis equal to {mcr_treatment_pps_ctrl1_pcu4_xfollowingerrfbk_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_xfollowingerrfbk_value_expected=mcr_treatment_pps_ctrl1_pcu4_xfollowingerrfbk_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_xfollowingerrfbk_value),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_ycmfbkvalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_ycmfbk_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_ycmfbkvalueis equal to {mcr_treatment_pps_ctrl1_pcu4_ycmfbk_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_ycmfbk_value_expected=mcr_treatment_pps_ctrl1_pcu4_ycmfbk_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_ycmfbk_value),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_ycmmonitoringfbkvalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_ycmmonitoringfbk_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_ycmmonitoringfbkvalueis equal to {mcr_treatment_pps_ctrl1_pcu4_ycmmonitoringfbk_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_ycmmonitoringfbk_value_expected=mcr_treatment_pps_ctrl1_pcu4_ycmmonitoringfbk_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_ycmmonitoringfbk_value),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_yfollowingerrfbkvalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_yfollowingerrfbk_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_yfollowingerrfbkvalueis equal to {mcr_treatment_pps_ctrl1_pcu4_yfollowingerrfbk_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_yfollowingerrfbk_value_expected=mcr_treatment_pps_ctrl1_pcu4_yfollowingerrfbk_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_yfollowingerrfbk_value),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_zcmfbkvalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_zcmfbk_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_zcmfbkvalueis equal to {mcr_treatment_pps_ctrl1_pcu4_zcmfbk_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_zcmfbk_value_expected=mcr_treatment_pps_ctrl1_pcu4_zcmfbk_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_zcmfbk_value),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_zcmmonitoringfbkvalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_zcmmonitoringfbk_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_zcmmonitoringfbkvalueis equal to {mcr_treatment_pps_ctrl1_pcu4_zcmmonitoringfbk_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_zcmmonitoringfbk_value_expected=mcr_treatment_pps_ctrl1_pcu4_zcmmonitoringfbk_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_zcmmonitoringfbk_value),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_zfollowingerrfbkvalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_zfollowingerrfbk_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_zfollowingerrfbkvalueis equal to {mcr_treatment_pps_ctrl1_pcu4_zfollowingerrfbk_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_zfollowingerrfbk_value_expected=mcr_treatment_pps_ctrl1_pcu4_zfollowingerrfbk_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_zfollowingerrfbk_value),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_rotdegfbkvalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_rotdegfbk_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_rotdegfbkvalueis equal to {mcr_treatment_pps_ctrl1_pcu4_rotdegfbk_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_rotdegfbk_value_expected=mcr_treatment_pps_ctrl1_pcu4_rotdegfbk_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_rotdegfbk_value),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_rotdegmonitoringfbkvalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_rotdegmonitoringfbk_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_rotdegmonitoringfbkvalueis equal to {mcr_treatment_pps_ctrl1_pcu4_rotdegmonitoringfbk_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_rotdegmonitoringfbk_value_expected=mcr_treatment_pps_ctrl1_pcu4_rotdegmonitoringfbk_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_rotdegmonitoringfbk_value),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_rotfollowingerrfbkvalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_rotfollowingerrfbk_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_rotfollowingerrfbkvalueis equal to {mcr_treatment_pps_ctrl1_pcu4_rotfollowingerrfbk_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_rotfollowingerrfbk_value_expected=mcr_treatment_pps_ctrl1_pcu4_rotfollowingerrfbk_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_rotfollowingerrfbk_value),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_pitchdegfbkvalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_pitchdegfbk_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_pitchdegfbkvalueis equal to {mcr_treatment_pps_ctrl1_pcu4_pitchdegfbk_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_pitchdegfbk_value_expected=mcr_treatment_pps_ctrl1_pcu4_pitchdegfbk_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_pitchdegfbk_value),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_pitchdegmonitoringfbkvalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_pitchdegmonitoringfbk_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_pitchdegmonitoringfbkvalueis equal to {mcr_treatment_pps_ctrl1_pcu4_pitchdegmonitoringfbk_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_pitchdegmonitoringfbk_value_expected=mcr_treatment_pps_ctrl1_pcu4_pitchdegmonitoringfbk_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_pitchdegmonitoringfbk_value),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_pitchfollowingerrfbkvalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_pitchfollowingerrfbk_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_pitchfollowingerrfbkvalueis equal to {mcr_treatment_pps_ctrl1_pcu4_pitchfollowingerrfbk_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_pitchfollowingerrfbk_value_expected=mcr_treatment_pps_ctrl1_pcu4_pitchfollowingerrfbk_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_pitchfollowingerrfbk_value),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_rolldegfbkvalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_rolldegfbk_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_rolldegfbkvalueis equal to {mcr_treatment_pps_ctrl1_pcu4_rolldegfbk_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_rolldegfbk_value_expected=mcr_treatment_pps_ctrl1_pcu4_rolldegfbk_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_rolldegfbk_value),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_rolldegmonitoringfbkvalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_rolldegmonitoringfbk_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_rolldegmonitoringfbkvalueis equal to {mcr_treatment_pps_ctrl1_pcu4_rolldegmonitoringfbk_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_rolldegmonitoringfbk_value_expected=mcr_treatment_pps_ctrl1_pcu4_rolldegmonitoringfbk_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_rolldegmonitoringfbk_value),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_rollfollowingerrfbkvalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_rollfollowingerrfbk_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_rollfollowingerrfbkvalueis equal to {mcr_treatment_pps_ctrl1_pcu4_rollfollowingerrfbk_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_rollfollowingerrfbk_value_expected=mcr_treatment_pps_ctrl1_pcu4_rollfollowingerrfbk_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_rollfollowingerrfbk_value),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_xforceengvalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_xforceeng_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_xforceengvalueis equal to {mcr_treatment_pps_ctrl1_pcu4_xforceeng_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_xforceeng_value_expected=mcr_treatment_pps_ctrl1_pcu4_xforceeng_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_xforceeng_value),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_yforceengtext", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_yforceeng_text),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_yforceengtextis equal to {mcr_treatment_pps_ctrl1_pcu4_yforceeng_text_expected}".format(mcr_treatment_pps_ctrl1_pcu4_yforceeng_text_expected=mcr_treatment_pps_ctrl1_pcu4_yforceeng_text_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_yforceeng_text),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_zforceengvalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_zforceeng_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_zforceengvalueis equal to {mcr_treatment_pps_ctrl1_pcu4_zforceeng_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_zforceeng_value_expected=mcr_treatment_pps_ctrl1_pcu4_zforceeng_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_zforceeng_value),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_xtorqueengvalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_xtorqueeng_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_xtorqueengvalueis equal to {mcr_treatment_pps_ctrl1_pcu4_xtorqueeng_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_xtorqueeng_value_expected=mcr_treatment_pps_ctrl1_pcu4_xtorqueeng_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_xtorqueeng_value),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_ytorqueengvalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_ytorqueeng_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_ytorqueengvalueis equal to {mcr_treatment_pps_ctrl1_pcu4_ytorqueeng_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_ytorqueeng_value_expected=mcr_treatment_pps_ctrl1_pcu4_ytorqueeng_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_ytorqueeng_value),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_ztorqueengvalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_ztorqueeng_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_ztorqueengvalueis equal to {mcr_treatment_pps_ctrl1_pcu4_ztorqueeng_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_ztorqueeng_value_expected=mcr_treatment_pps_ctrl1_pcu4_ztorqueeng_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_ztorqueeng_value),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_xforcerawvalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_xforceraw_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_xforcerawvalueis equal to {mcr_treatment_pps_ctrl1_pcu4_xforceraw_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_xforceraw_value_expected=mcr_treatment_pps_ctrl1_pcu4_xforceraw_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_xforceraw_value),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_yforcerawtext", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_yforceraw_text),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_yforcerawtextis equal to {mcr_treatment_pps_ctrl1_pcu4_yforceraw_text_expected}".format(mcr_treatment_pps_ctrl1_pcu4_yforceraw_text_expected=mcr_treatment_pps_ctrl1_pcu4_yforceraw_text_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_yforceraw_text),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_zforcerawvalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_zforceraw_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_zforcerawvalueis equal to {mcr_treatment_pps_ctrl1_pcu4_zforceraw_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_zforceraw_value_expected=mcr_treatment_pps_ctrl1_pcu4_zforceraw_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_zforceraw_value),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_xtorquerawvalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_xtorqueraw_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_xtorquerawvalueis equal to {mcr_treatment_pps_ctrl1_pcu4_xtorqueraw_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_xtorqueraw_value_expected=mcr_treatment_pps_ctrl1_pcu4_xtorqueraw_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_xtorqueraw_value),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_ytorquerawvalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_ytorqueraw_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_ytorquerawvalueis equal to {mcr_treatment_pps_ctrl1_pcu4_ytorqueraw_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_ytorqueraw_value_expected=mcr_treatment_pps_ctrl1_pcu4_ytorqueraw_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_ytorqueraw_value),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_ztorquerawvalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_ztorqueraw_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_ztorquerawvalueis equal to {mcr_treatment_pps_ctrl1_pcu4_ztorqueraw_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_ztorqueraw_value_expected=mcr_treatment_pps_ctrl1_pcu4_ztorqueraw_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_ztorqueraw_value),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_motionmodevalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_motionmode_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_motionmodevalueis equal to {mcr_treatment_pps_ctrl1_pcu4_motionmode_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_motionmode_value_expected=mcr_treatment_pps_ctrl1_pcu4_motionmode_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_motionmode_value),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_couchlongvisibility", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_couchlong_visibility),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_couchlongvisibilityis equal to {mcr_treatment_pps_ctrl1_pcu4_couchlong_visibility_expected}".format(mcr_treatment_pps_ctrl1_pcu4_couchlong_visibility_expected=mcr_treatment_pps_ctrl1_pcu4_couchlong_visibility_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_couchlong_visibility),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_couchshortvisibility", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_couchshort_visibility),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_couchshortvisibilityis equal to {mcr_treatment_pps_ctrl1_pcu4_couchshort_visibility_expected}".format(mcr_treatment_pps_ctrl1_pcu4_couchshort_visibility_expected=mcr_treatment_pps_ctrl1_pcu4_couchshort_visibility_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_couchshort_visibility),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_couchextvisibility", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_couchext_visibility),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_couchextvisibilityis equal to {mcr_treatment_pps_ctrl1_pcu4_couchext_visibility_expected}".format(mcr_treatment_pps_ctrl1_pcu4_couchext_visibility_expected=mcr_treatment_pps_ctrl1_pcu4_couchext_visibility_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_couchext_visibility),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_coldetectedsubobject_name", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_coldetected_subobject_name),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_coldetectedsubobject_nameis equal to {mcr_treatment_pps_ctrl1_pcu4_coldetected_subobject_name_expected}".format(mcr_treatment_pps_ctrl1_pcu4_coldetected_subobject_name_expected=mcr_treatment_pps_ctrl1_pcu4_coldetected_subobject_name_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_coldetected_subobject_name),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_proxdetectedsubobject_name", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_proxdetected_subobject_name),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_proxdetectedsubobject_nameis equal to {mcr_treatment_pps_ctrl1_pcu4_proxdetected_subobject_name_expected}".format(mcr_treatment_pps_ctrl1_pcu4_proxdetected_subobject_name_expected=mcr_treatment_pps_ctrl1_pcu4_proxdetected_subobject_name_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_proxdetected_subobject_name),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_xnel_1subobject_name", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_xnel_1_subobject_name),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_xnel_1subobject_nameis equal to {mcr_treatment_pps_ctrl1_pcu4_xnel_1_subobject_name_expected}".format(mcr_treatment_pps_ctrl1_pcu4_xnel_1_subobject_name_expected=mcr_treatment_pps_ctrl1_pcu4_xnel_1_subobject_name_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_xnel_1_subobject_name),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_xtorquerawoffsetvalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_xtorquerawoffset_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_xtorquerawoffsetvalueis equal to {mcr_treatment_pps_ctrl1_pcu4_xtorquerawoffset_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_xtorquerawoffset_value_expected=mcr_treatment_pps_ctrl1_pcu4_xtorquerawoffset_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_xtorquerawoffset_value),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_ytorquerawoffsetvalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_ytorquerawoffset_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_ytorquerawoffsetvalueis equal to {mcr_treatment_pps_ctrl1_pcu4_ytorquerawoffset_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_ytorquerawoffset_value_expected=mcr_treatment_pps_ctrl1_pcu4_ytorquerawoffset_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_ytorquerawoffset_value),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_ztorquerawoffsetvalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_ztorquerawoffset_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_ztorquerawoffsetvalueis equal to {mcr_treatment_pps_ctrl1_pcu4_ztorquerawoffset_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_ztorquerawoffset_value_expected=mcr_treatment_pps_ctrl1_pcu4_ztorquerawoffset_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_ztorquerawoffset_value),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_xforcerawoffsetvalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_xforcerawoffset_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_xforcerawoffsetvalueis equal to {mcr_treatment_pps_ctrl1_pcu4_xforcerawoffset_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_xforcerawoffset_value_expected=mcr_treatment_pps_ctrl1_pcu4_xforcerawoffset_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_xforcerawoffset_value),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_yforcerawoffsettext", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_yforcerawoffset_text),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_yforcerawoffsettextis equal to {mcr_treatment_pps_ctrl1_pcu4_yforcerawoffset_text_expected}".format(mcr_treatment_pps_ctrl1_pcu4_yforcerawoffset_text_expected=mcr_treatment_pps_ctrl1_pcu4_yforcerawoffset_text_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_yforcerawoffset_text),
                        InformationSet("get mcr_treatment_pps_ctrl1:pcu4_zforcerawoffsetvalue", "thriver", "mcrhci", get_mcr_treatment_pps_ctrl1_pcu4_zforcerawoffset_value),
                        InformationSet("validate mcr_treatment_pps_ctrl1:pcu4_zforcerawoffsetvalueis equal to {mcr_treatment_pps_ctrl1_pcu4_zforcerawoffset_value_expected}".format(mcr_treatment_pps_ctrl1_pcu4_zforcerawoffset_value_expected=mcr_treatment_pps_ctrl1_pcu4_zforcerawoffset_value_expected), "mcrhci", "hcitracer", validate_mcr_treatment_pps_ctrl1_pcu4_zforcerawoffset_value),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []
  

