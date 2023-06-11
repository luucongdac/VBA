from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import SETUP_SET_VARIABLE, SETUP_VALIDATE_OBJECT_INFO, COLORS

VISIBLE = "1"
INVISIBLE = "0"
COLOR_RED = COLORS.colorDict["RED_3"] 			#"40"
COLOR_YELLOW = COLORS.colorDict["YELLOW_2"] 	#"28" 
COLOR_GRAY_2 = COLORS.colorDict["WHITE_4"] 		#"49"
COLOR_ORANGE = COLORS.colorDict["ORANGE_1"] 	#"9" 
COLOR_GRAY = COLORS.colorDict["WHITE_6"] 		#"81" 
COLOR_BLUE= COLORS.colorDict["BLUE_1"]			#"3" 

class SET_MESSAGE_ACTUALMU_IC2_FIRST_LAYER(SETUP_SET_VARIABLE):
	var_name = "tr2_pbs_iceu2_beamdose"
	value = 0.5

class VALIDATE_ACTUALMU_IC2_FIRST_LAYER(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2_treatment_pbs_1"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class SET_MESSAGE_ACTUALMU_IC2_FIRST_LAYER_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 2.5

class VALIDATE_ACTUALMU_IC2_FIRST_LAYER_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2_treatment_pbs_1"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_ACTUALMU_IC2_FIRST_LAYER_INVISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 0.5

class VALIDATE_ACTUALMU_IC2_FIRST_LAYER_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2_treatment_pbs_1"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_ACTUALMU_IC2_SECOND_LAYER(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_iceu2_wbtotaldose"
	value = 0.6

class VALIDATE_ACTUALMU_IC2_SECOND_LAYER(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2_treatment_wb_1"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.6

class SET_MESSAGE_ACTUALMU_IC2_SECOND_LAYER_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 1.2

class VALIDATE_ACTUALMU_IC2_SECOND_LAYER_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2_treatment_wb_1"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_ACTUALMU_IC2_SECOND_LAYER_INVISIBLE_1(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 2.0

class VALIDATE_ACTUALMU_IC2_SECOND_LAYER_INVISIBLE_1(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2_treatment_wb_1"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_ACTUALMU_IC2_SECOND_LAYER_INVISIBLE_2(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 0.5

class VALIDATE_ACTUALMU_IC2_SECOND_LAYER_INVISIBLE_2(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2_treatment_wb_1"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_ACTUALMU_IC2_THIRD_LAYER(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_iceu2_dose"
	value = 0.5

class VALIDATE_ACTUALMU_IC2_THIRD_LAYER(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2_treatment_ds"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class SET_MESSAGE_ACTUALMU_IC2_THIRD_LAYER_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 1.5

class VALIDATE_ACTUALMU_IC2_THIRD_LAYER_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2_treatment_ds"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_ACTUALMU_IC2_THIRD_LAYER_INVISIBLE_1(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 2.5

class VALIDATE_ACTUALMU_IC2_THIRD_LAYER_INVISIBLE_1(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2_treatment_ds"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_ACTUALMU_IC2_THIRD_LAYER_INVISIBLE_2(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 0.5

class VALIDATE_ACTUALMU_IC2_THIRD_LAYER_INVISIBLE_2(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2_treatment_ds"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_ACTUALMU_IC2_FOURTH_LAYER(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_iceu2_servicedose"
	value = 0.6

class VALIDATE_ACTUALMU_IC2_FOURTH_LAYER(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2_service"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.6

class SET_MESSAGE_ACTUALMU_IC2_FOURTH_LAYER_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "mcr_sysmgr_sw_tcr2servicesession"
	value = True

class VALIDATE_ACTUALMU_IC2_FOURTH_LAYER_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2_service"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_ACTUALMU_IC2_FOURTH_LAYER_INVISIBLE(SETUP_SET_VARIABLE):
	var_name = "mcr_sysmgr_sw_tcr2servicesession"
	value = False

class VALIDATE_ACTUALMU_IC2_FOURTH_LAYER_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2_service"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_ACTUALMU_IC3_FIRST_LAYER(SETUP_SET_VARIABLE):
	var_name = "tr2_pbs_iceu3_beamdose"
	value = 0.5

class VALIDATE_ACTUALMU_IC3_FIRST_LAYER(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic3_treatment_pbs"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class SET_MESSAGE_ACTUALMU_IC3_FIRST_LAYER_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 2.5

class VALIDATE_ACTUALMU_IC3_FIRST_LAYER_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic3_treatment_pbs"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_ACTUALMU_IC3_FIRST_LAYER_INVISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 0.5

class VALIDATE_ACTUALMU_IC3_FIRST_LAYER_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic3_treatment_pbs"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_ACTUALMU_IC3_SECOND_LAYER(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_iceu3_wbtotaldose"
	value = 0.6

class VALIDATE_ACTUALMU_IC3_SECOND_LAYER(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic3_treatment_wb"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.6

class SET_MESSAGE_ACTUALMU_IC3_SECOND_LAYER_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 1.0

class VALIDATE_ACTUALMU_IC3_SECOND_LAYER_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic3_treatment_wb"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_ACTUALMU_IC3_SECOND_LAYER_INVISIBLE_1(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 2.5

class VALIDATE_ACTUALMU_IC3_SECOND_LAYER_INVISIBLE_1(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic3_treatment_wb"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_ACTUALMU_IC3_SECOND_LAYER_INVISIBLE_2(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 0.3

class VALIDATE_ACTUALMU_IC3_SECOND_LAYER_INVISIBLE_2(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic3_treatment_wb"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_ACTUALMU_IC3_THIRD_LAYER(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_iceu3_dose"
	value = 0.6

class VALIDATE_ACTUALMU_IC3_THIRD_LAYER(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic3_treatment_ds"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.6

class SET_MESSAGE_ACTUALMU_IC3_THIRD_LAYER_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 1.5

class VALIDATE_ACTUALMU_IC3_THIRD_LAYER_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic3_treatment_ds"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_ACTUALMU_IC3_THIRD_LAYER_INVISIBLE_1(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 2.5

class VALIDATE_ACTUALMU_IC3_THIRD_LAYER_INVISIBLE_1(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic3_treatment_ds"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_ACTUALMU_IC3_THIRD_LAYER_INVISIBLE_2(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 0.4

class VALIDATE_ACTUALMU_IC3_THIRD_LAYER_INVISIBLE_2(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic3_treatment_ds"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_ACTUALMU_IC3_FOURTH_LAYER(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_iceu3_servicedose"
	value = 0.6

class VALIDATE_ACTUALMU_IC3_FOURTH_LAYER(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic3_service"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.6

class SET_MESSAGE_ACTUALMU_IC3_FOURTH_LAYER_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "mcr_sysmgr_sw_tcr2servicesession"
	value = True

class VALIDATE_ACTUALMU_IC3_FOURTH_LAYER_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic3_service"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_ACTUALMU_IC3_FOURTH_LAYER_INVISIBLE(SETUP_SET_VARIABLE):
	var_name = "mcr_sysmgr_sw_tcr2servicesession"
	value = False

class VALIDATE_ACTUALMU_IC3_FOURTH_LAYER_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic3_service"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_ACTUALMU_IC2_IC3_FIRST_LAYER_RED_1(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_iceu_servicedoseIC2IC3"
	value = 0.5

class VALIDATE_ACTUALMU_IC2_IC3_FIRST_LAYER_RED_1(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2ic3_service"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_ACTUALMU_IC2_IC3_FIRST_LAYER_BACKGROUND_COLOR_RED_1(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2ic3_service"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR"
	expected_value = COLOR_RED

class SET_MESSAGE_ACTUALMU_IC2_IC3_FIRST_LAYER_RED_2(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_iceu_servicedoseIC2IC3"
	value = 1.5

class VALIDATE_ACTUALMU_IC2_IC3_FIRST_LAYER_RED_2(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2ic3_service"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 1.5

class VALIDATE_ACTUALMU_IC2_IC3_FIRST_LAYER_BACKGROUND_COLOR_RED_2(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2ic3_service"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR"
	expected_value = COLOR_RED

class SET_MESSAGE_ACTUALMU_IC2_IC3_FIRST_LAYER_YELLOW_1(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_iceu_servicedoseIC2IC3"
	value = 0.85

class VALIDATE_ACTUALMU_IC2_IC3_FIRST_LAYER_YELLOW_1(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2ic3_service"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.85

class VALIDATE_ACTUALMU_IC2_IC3_FIRST_LAYER_BACKGROUND_COLOR_YELLOW_1(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2ic3_service"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR"
	expected_value = COLOR_YELLOW

class SET_MESSAGE_ACTUALMU_IC2_IC3_FIRST_LAYER_YELLOW_2(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_iceu_servicedoseIC2IC3"
	value = 1.15

class VALIDATE_ACTUALMU_IC2_IC3_FIRST_LAYER_YELLOW_2(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2ic3_service"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 1.15

class VALIDATE_ACTUALMU_IC2_IC3_FIRST_LAYER_BACKGROUND_COLOR_YELLOW_2(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2ic3_service"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR"
	expected_value = COLOR_YELLOW

class SET_MESSAGE_ACTUALMU_IC2_IC3_FIRST_LAYER_GRAY(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_iceu_servicedoseIC2IC3"
	value = 1.0

class VALIDATE_ACTUALMU_IC2_IC3_FIRST_LAYER_GRAY(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2ic3_service"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value =  1.0

class VALIDATE_ACTUALMU_IC2_IC3_FIRST_LAYER_BACKGROUND_COLOR_GRAY(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2ic3_service"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR"
	expected_value = COLOR_GRAY

class SET_MESSAGE_ACTUALMU_IC2_IC3_FIRST_LAYER_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "mcr_sysmgr_sw_tcr2servicesession"
	value = True

class VALIDATE_ACTUALMU_IC2_IC3_FIRST_LAYER_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2ic3_service"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_ACTUALMU_IC2_IC3_FIRST_LAYER_INVISIBLE(SETUP_SET_VARIABLE):
	var_name = "mcr_sysmgr_sw_tcr2servicesession"
	value = False

class VALIDATE_ACTUALMU_IC2_IC3_FIRST_LAYER_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2ic3_service"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_ACTUALMU_IC2_IC3_SECOND_LAYER_RED_1(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_iceu_doseIC2IC3"
	value = 0.5

class VALIDATE_ACTUALMU_IC2_IC3_SECOND_LAYER_RED_1(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2ic3_treatment"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_ACTUALMU_IC2_IC3_SECOND_LAYER_BACKGROUND_COLOR_RED_1(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2ic3_treatment"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR"
	expected_value = COLOR_RED

class SET_MESSAGE_ACTUALMU_IC2_IC3_SECOND_LAYER_RED_2(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_iceu_doseIC2IC3"
	value = 1.5

class VALIDATE_ACTUALMU_IC2_IC3_SECOND_LAYER_RED_2(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2ic3_treatment"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 1.5

class VALIDATE_ACTUALMU_IC2_IC3_SECOND_LAYER_BACKGROUND_COLOR_RED_2(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2ic3_treatment"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR"
	expected_value = COLOR_RED

class SET_MESSAGE_ACTUALMU_IC2_IC3_SECOND_LAYER_YELLOW_1(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_iceu_doseIC2IC3"
	value = 0.85

class VALIDATE_ACTUALMU_IC2_IC3_SECOND_LAYER_YELLOW_1(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2ic3_treatment"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.85

class VALIDATE_ACTUALMU_IC2_IC3_SECOND_LAYER_BACKGROUND_COLOR_YELLOW_1(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2ic3_treatment"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR"
	expected_value = COLOR_YELLOW

class SET_MESSAGE_ACTUALMU_IC2_IC3_SECOND_LAYER_YELLOW_2(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_iceu_doseIC2IC3"
	value = 1.15

class VALIDATE_ACTUALMU_IC2_IC3_SECOND_LAYER_YELLOW_2(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2ic3_treatment"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 1.15

class VALIDATE_ACTUALMU_IC2_IC3_SECOND_LAYER_BACKGROUND_COLOR_YELLOW_2(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2ic3_treatment"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR"
	expected_value = COLOR_YELLOW

class SET_MESSAGE_ACTUALMU_IC2_IC3_SECOND_LAYER_GRAY(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_iceu_doseIC2IC3"
	value = 1.0

class VALIDATE_ACTUALMU_IC2_IC3_SECOND_LAYER_GRAY(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2ic3_treatment"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value =  1.0

class VALIDATE_ACTUALMU_IC2_IC3_SECOND_LAYER_BACKGROUND_COLOR_GRAY(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2ic3_treatment"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR"
	expected_value = COLOR_GRAY

class SET_MESSAGE_ACTUALMU_IC2_IC3_SECOND_LAYER_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "mcr_sysmgr_sw_tcr2servicesession"
	value = False

class VALIDATE_ACTUALMU_IC2_IC3_SECOND_LAYER_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2ic3_treatment"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_ACTUALMU_IC2_IC3_SECOND_LAYER_INVISIBLE(SETUP_SET_VARIABLE):
	var_name = "mcr_sysmgr_sw_tcr2servicesession"
	value = True

class VALIDATE_ACTUALMU_IC2_IC3_SECOND_LAYER_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2ic3_treatment"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_ACTUALMU_TIME_SEC(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_sw_actualIrradTime_s"
	value = 0.6

class VALIDATE_ACTUALMU_TIME_SEC(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_time"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.6

class SET_MESSAGE_ACTUALMU_TIME_SEC_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "mcr_sysmgr_sw_tcr2servicesession"
	value = False

class VALIDATE_ACTUALMU_TIME_SEC_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_time"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_ACTUALMU_TIME_SEC_INVISIBLE(SETUP_SET_VARIABLE):
	var_name = "mcr_sysmgr_sw_tcr2servicesession"
	value = True

class VALIDATE_ACTUALMU_TIME_SEC_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_time"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_ACTUALMU_TIME_SEC_STRING_NA_INVISIBLE(SETUP_SET_VARIABLE):
	var_name = "mcr_sysmgr_sw_tcr2servicesession"
	value = True

class VALIDATE_ACTUALMU_TIME_SEC_STRING_NA_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_time_visibility"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_ACTUALMU_TIME_SEC_STRING_NA_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "mcr_sysmgr_sw_tcr2servicesession"
	value = False

class VALIDATE_ACTUALMU_TIME_SEC_STRING_NA_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_actual_time_visibility"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_PRESETMU_IC2_FIRST_LAYER(SETUP_SET_VARIABLE):
	var_name = "tr2_trmgr_sw_pbstotal_presetdoseic2"
	value = 0.6

class VALIDATE_PRESETMU_IC2_FIRST_LAYER(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_preset_ic2_pbs"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.6

class SET_MESSAGE_PRESETMU_IC2_FIRST_LAYER_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_mcrdisplay"
	value = 2.5

class VALIDATE_PRESETMU_IC2_FIRST_LAYER_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_preset_ic2_pbs"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_PRESETMU_IC2_FIRST_LAYER_INVISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_mcrdisplay"
	value = 0.5

class VALIDATE_PRESETMU_IC2_FIRST_LAYER_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_preset_ic2_pbs"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_PRESETMU_IC2_SECOND_LAYER(SETUP_SET_VARIABLE):
	var_name = "tr2_trmgr_sw_wbpresetdoseic2"
	value = 0.5

class VALIDATE_PRESETMU_IC2_SECOND_LAYER(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_preset_ic2_wb_1"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class SET_MESSAGE_PRESETMU_IC2_SECOND_LAYER_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_mcrdisplay"
	value = 1.0

class VALIDATE_PRESETMU_IC2_SECOND_LAYER_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_preset_ic2_wb_1"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_PRESETMU_IC2_SECOND_LAYER_INVISIBLE_1(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_mcrdisplay"
	value = 0.4

class VALIDATE_PRESETMU_IC2_SECOND_LAYER_INVISIBLE_1(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_preset_ic2_wb_1"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_PRESETMU_IC2_SECOND_LAYER_INVISIBLE_2(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_mcrdisplay"
	value = 1.5

class VALIDATE_PRESETMU_IC2_SECOND_LAYER_INVISIBLE_2(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_preset_ic2_wb_1"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_PRESETMU_IC2_THIRD_LAYER(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_iceu2_presetdose"
	value = 0.5

class VALIDATE_PRESETMU_IC2_THIRD_LAYER(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_preset_ic2_ds"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class SET_MESSAGE_PRESETMU_IC2_THIRD_LAYER_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_mcrdisplay"
	value = 1.5

class VALIDATE_PRESETMU_IC2_THIRD_LAYER_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_preset_ic2_ds"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_PRESETMU_IC2_THIRD_LAYER_INVISIBLE_1(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_mcrdisplay"
	value = 0.4

class VALIDATE_PRESETMU_IC2_THIRD_LAYER_INVISIBLE_1(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_preset_ic2_ds"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_PRESETMU_IC2_THIRD_LAYER_INVISIBLE_2(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_mcrdisplay"
	value = 2.5

class VALIDATE_PRESETMU_IC2_THIRD_LAYER_INVISIBLE_2(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_preset_ic2_ds"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_PRESETMU_IC2_STRING_NOTLOADER_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_mcrdisplay"
	value = 0.4

class VALIDATE_PRESETMU_IC2_STRING_NOTLOADER_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_preset_ic2_visibility_1"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_PRESETMU_IC2_STRING_NOTLOADER_INVISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_mcrdisplay"
	value = 1.0

class VALIDATE_PRESETMU_IC2_STRING_NOTLOADER_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_preset_ic2_visibility_1"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_PRESETMU_IC3_FIRST_LAYER(SETUP_SET_VARIABLE):
	var_name = "tr2_trmgr_sw_pbstotal_presetdoseic3"
	value = 0.6

class VALIDATE_PRESETMU_IC3_FIRST_LAYER(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_preset_ic3_treatment_pbs_1"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.6

class SET_MESSAGE_PRESETMU_IC3_FIRST_LAYER_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_mcrdisplay"
	value = 2.5

class VALIDATE_PRESETMU_IC3_FIRST_LAYER_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_preset_ic3_treatment_pbs_1"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_PRESETMU_IC3_FIRST_LAYER_INVISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_mcrdisplay"
	value = 0.5

class VALIDATE_PRESETMU_IC3_FIRST_LAYER_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_preset_ic3_treatment_pbs_1"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_PRESETMU_IC3_SECOND_LAYER(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_iceu3_presetdose"
	value = 0.5

class VALIDATE_PRESETMU_IC3_SECOND_LAYER(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_preset_ic3_treatment_ds"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class SET_MESSAGE_PRESETMU_IC3_SECOND_LAYER_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_mcrdisplay"
	value = 2.0

class VALIDATE_PRESETMU_IC3_SECOND_LAYER_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_dos_preset_ic3_treatment_ds"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_PRESETMU_IC3_SECOND_LAYER_INVISIBLE_1(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_mcrdisplay"
	value = 0.4

class VALIDATE_PRESETMU_IC3_SECOND_LAYER_INVISIBLE_1(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_preset_ic3_treatment_ds"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_PRESETMU_IC3_SECOND_LAYER_INVISIBLE_2(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_mcrdisplay"
	value = 2.5

class VALIDATE_PRESETMU_IC3_SECOND_LAYER_INVISIBLE_2(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_preset_ic3_treatment_ds"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_PRESETMU_IC3_THIRD_LAYER(SETUP_SET_VARIABLE):
	var_name = "tr2_trmgr_sw_wbpresetdoseic3"
	value = 0.6

class VALIDATE_PRESETMU_IC3_THIRD_LAYER(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_preset_ic3_treatment_wb_1"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.6

class SET_MESSAGE_PRESETMU_IC3_THIRD_LAYER_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_mcrdisplay"
	value = 1.0

class VALIDATE_PRESETMU_IC3_THIRD_LAYER_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_preset_ic3_treatment_wb_1"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_PRESETMU_IC3_THIRD_LAYER_INVISIBLE_1(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_mcrdisplay"
	value = 0.4

class VALIDATE_PRESETMU_IC3_THIRD_LAYER_INVISIBLE_1(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_preset_ic3_treatment_wb_1"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_PRESETMU_IC3_THIRD_LAYER_INVISIBLE_2(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_mcrdisplay"
	value = 1.5

class VALIDATE_PRESETMU_IC3_THIRD_LAYER_INVISIBLE_2(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_preset_ic3_treatment_wb_1"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_PRESETMU_IC3_STRING_NOTLOADER_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_mcrdisplay"
	value = 0.4

class VALIDATE_PRESETMU_IC3_STRING_NOTLOADER_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_preset_ic3_visibility_1"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_PRESETMU_IC3_STRING_NOTLOADER_INVISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_mcrdisplay"
	value = 1.5

class VALIDATE_PRESETMU_IC3_STRING_NOTLOADER_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_preset_ic3_visibility_1"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_PRESETMU_IC2IC3_FIRST_LAYER(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_iceu_presetdoseIC2IC3"
	value = 0.6

class VALIDATE_PRESETMU_IC2IC3_FIRST_LAYER(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_preset_ic2ic3"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.6

class SET_MESSAGE_PRESETMU_IC2IC3_FIRST_LAYER_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_mcrdisplay"
	value = 0.8

class VALIDATE_PRESETMU_IC2IC3_FIRST_LAYER_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_preset_ic2ic3"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_PRESETMU_IC2IC3_FIRST_LAYER_INVISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_mcrdisplay"
	value = 0.4

class VALIDATE_PRESETMU_IC2IC3_FIRST_LAYER_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_preset_ic2ic3"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_PRESETMU_IC2IC3_STRING_NOTLOADER_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_mcrdisplay"
	value = 0.4

class VALIDATE_PRESETMU_IC2IC3_STRING_NOTLOADER_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_preset_ic2ic3_visibility"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_PRESETMU_IC2IC3_STRING_NOTLOADER_INVISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_mcrdisplay"
	value = 0.8

class VALIDATE_PRESETMU_IC2IC3_STRING_NOTLOADER_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_preset_ic2ic3_visibility"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_PRESETMU_TIMESEC(SETUP_SET_VARIABLE):
	var_name = "tr2_trmgr_sw_maxIrradTime"
	value = 0.6

class VALIDATE_PRESETMU_TIMESEC(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_preset_time"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.6

class SET_MESSAGE_PRESETMU_TIMESEC_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "mcr_sysmgr_sw_tcr2servicesession"
	value = False

class VALIDATE_PRESETMU_TIMESEC_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_preset_time"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_PRESETMU_TIMESEC_INVISIBLE(SETUP_SET_VARIABLE):
	var_name = "mcr_sysmgr_sw_tcr2servicesession"
	value = True

class VALIDATE_PRESETMU_TIMESEC_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_preset_time"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_PRESETMU_TIMESEC_STRING_NA_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "mcr_sysmgr_sw_tcr2servicesession"
	value = True

class VALIDATE_PRESETMU_TIMESEC_STRING_NA_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_preset_time_visibility"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_PRESETMU_TIMESEC_STRING_NA_INVISIBLE(SETUP_SET_VARIABLE):
	var_name = "mcr_sysmgr_sw_tcr2servicesession"
	value = False

class VALIDATE_PRESETMU_TIMESEC_STRING_NA_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_preset_time_visibility"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_PPS_LAT(SETUP_SET_VARIABLE):
	var_name = "tr2_pcu_pps_lateral_cmfeedback"
	value = 0.5

class VALIDATE_PPS_LAT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_field_pps_x"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class SET_MESSAGE_PITCH_DEG(SETUP_SET_VARIABLE):
	var_name = "tr2_pcu_pps_pitch_degfeedback"
	value = 0.5

class VALIDATE_PITCH_DEG(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_field_pitch"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class SET_MESSAGE_ANGLE_DEG(SETUP_SET_VARIABLE):
	var_name = "tr2_pcu_gantry_position_degfeedback"
	value = 0.5

class VALIDATE_ANGLE_DEG(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_field_gantryangle"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class SET_MESSAGE_PPS_LONG(SETUP_SET_VARIABLE):
	var_name = "tr2_pcu_pps_longitudinal_cmfeedback"
	value = 0.5

class VALIDATE_PPS_LONG(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_field_pps_y"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class SET_MESSAGE_ROLL_DEG(SETUP_SET_VARIABLE):
	var_name = "tr2_pcu_pps_roll_degfeedback"
	value = 0.5

class VALIDATE_ROLL_DEG(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_field_roll"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class SET_MESSAGE_SNOUTT_CM(SETUP_SET_VARIABLE):
	var_name = "tr2_pcu_steu_trans_cmfeedback"
	value = 0.5

class VALIDATE_SNOUTT_CM(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_field_snouttranslation"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class SET_MESSAGE_PPS_VERT_CM(SETUP_SET_VARIABLE):
	var_name = "tr2_pcu_pps_vertical_cmfeedback"
	value = 0.5

class VALIDATE_PPS_VERT_CM(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_field_pps_z"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class SET_MESSAGE_ROTN_DEG(SETUP_SET_VARIABLE):
	var_name = "tr2_pcu_pps_rotational_degfeedback"
	value = 0.5

class VALIDATE_MCR2_ROTN_DEG(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_field_rotation"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class SET_MESSAGE_SNOUTR_DEG(SETUP_SET_VARIABLE):
	var_name = "tr2_pcu_sreu_rot_degfeedback"
	value = 0.5

class VALIDATE_SNOUTR_DEG(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_field_snoutrotation"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class SET_MESSAGE_RPM(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rmeu_sw_speed"
	value = 0.5

class VALIDATE_RPM(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_rmeu_sw_speed_1"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class SET_MESSAGE_WHEEL(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rmeu_wheel_selected_return"
	value = 0.5

class VALIDATE_WHEEL(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_rmeu_sw_speed_2"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class SET_MESSAGE_TRACK(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rmeu_lw_feedback"
	value = 0.5

class VALIDATE_TRACK(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_rmeu_sw_speed_3"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class SET_MESSAGE_MEAN_MM_IC1X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu1_Xmean"
	value = 0.1

class VALIDATE_MEAN_MM_IC1X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_ic1x_mean"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.1

class SET_MESSAGE_RMS_MM_IC1X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu1_Xrms"
	value = 0.1

class VALIDATE_RMS_MM_IC1X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_ic1x_rms"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.1

class SET_MESSAGE_SKEWNESS_MM_IC3X_ORANGE1(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu3_skewness_percent"
	value = 5.0

class VALIDATE_SKEWNESS_MM_IC3X_ORANGE1(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_ic3x_skewness_1"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 5.0

class VALIDATE_SKEWNESS_MM_IC3X_BACKGROUND_COLOR_ORANGE1(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_ic3x_skewness_1"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR"
	expected_value = COLOR_ORANGE

class SET_MESSAGE_SKEWNESS_MM_IC3X_ORANGE2(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu3_skewness_percent"
	value = -5.0

class VALIDATE_SKEWNESS_MM_IC3X_ORANGE2(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_ic3x_skewness_1"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = -5.0

class VALIDATE_SKEWNESS_MM_IC3X_BACKGROUND_COLOR_ORANGE2(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_ic3x_skewness_1"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR"
	expected_value = COLOR_ORANGE

class SET_MESSAGE_SKEWNESS_MM_IC3X_GRAY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu3_skewness_percent"
	value = -1.0

class VALIDATE_SKEWNESS_MM_IC3X_GRAY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_ic3x_skewness_1"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = -1.0

class VALIDATE_SKEWNESS_MM_IC3X_BACKGROUND_COLOR_GRAY(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_ic3x_skewness_1"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR"
	expected_value = COLOR_GRAY_2

class SET_MESSAGE_MEAN_IC3X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu3_mean"
	value = 0.5

class VALIDATE_MEAN_IC3X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_ic3x_skewness_2"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class SET_MESSAGE_RMS_MM_IC3X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu3_rms"
	value = 0.5

class VALIDATE_RMS_MM_IC3X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_ic3x_rms"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class SET_MESSAGE_MEAN_MM_IC1Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu1_Ymean"
	value = 0.5

class VALIDATE_MEAN_MM_IC1Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_ic1y_mean"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class SET_MESSAGE_RMS_MM_IC1Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu1_Yrms"
	value = 0.5

class VALIDATE_RMS_MM_IC1Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_ic1y_rms"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class SET_MESSAGE_SKEWNESS_MM_IC2Y_ORANGE1(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu2_skewness_percent"
	value = 5.0

class VALIDATE_SKEWNESS_MM_IC2Y_ORANGE1(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_ic2y_skewness_1"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 5.0

class VALIDATE_SKEWNESS_MM_IC2Y_BACKGROUND_COLOR_ORANGE1(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_ic2y_skewness_1"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR"
	expected_value = COLOR_ORANGE

class SET_MESSAGE_SKEWNESS_MM_IC2Y_ORANGE2(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu2_skewness_percent"
	value = -5.0

class VALIDATE_SKEWNESS_MM_IC2Y_ORANGE2(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_ic2y_skewness_1"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = -5.0

class VALIDATE_SKEWNESS_MM_IC2Y_BACKGROUND_COLOR_ORANGE2(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_ic2y_skewness_1"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR"
	expected_value = COLOR_ORANGE

class SET_MESSAGE_SKEWNESS_MM_IC2Y_GRAY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu2_skewness_percent"
	value = -1.0

class VALIDATE_SKEWNESS_MM_IC2Y_GRAY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_ic2y_skewness_1"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = -1.0

class VALIDATE_SKEWNESS_MM_IC2Y_BACKGROUND_COLOR_GRAY(SETUP_VALIDATE_OBJECT_INFO):
	object_name ="mcr_treatment_beam_profiles2:mcr2_ic2y_skewness_1"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR"
	expected_value = COLOR_GRAY_2

class SET_MESSAGE_MEAN_IC2Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu2_mean"
	value = 0.5

class VALIDATE_MEAN_IC2Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_ic2y_skewness_2"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class SET_MESSAGE_RMS_MM_IC2Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu2_rms"
	value = 0.5

class VALIDATE_RMS_MM_IC2Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_ic2y_rms"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class SET_MESSAGE_ACTUALR_G_CM2(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_rveu_actualRange"
	value = 0.5

class VALIDATE_ACTUALR_G_CM2(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_rangeactual_r_treatment"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class SET_MESSAGE_ACTUAL_R_PERCENT(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu2_largestError10bins"
	value = 0.6

class VALIDATE_ACTUAL_R_PERCENT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_rangeactual_deltar"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.6

class SET_MESSAGE_ACTUAL_R_PERCENT_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "mcr_sysmgr_sw_tcr2servicesession"
	value = False

class VALIDATE_ACTUAL_R_PERCENT_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_rangeactual_deltar"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_ACTUAL_R_PERCENT_INVISIBLE(SETUP_SET_VARIABLE):
	var_name = "mcr_sysmgr_sw_tcr2servicesession"
	value = True

class VALIDATE_ACTUAL_R_PERCENT_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_rangeactual_deltar"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_ACTUAL_R_PERCENT_STRING_NA_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "mcr_sysmgr_sw_tcr2servicesession"
	value = True

class VALIDATE_ACTUAL_R_PERCENT_STRING_NA_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_rangeactual_delta_visibility"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_ACTUAL_R_PERCENT_STRING_NA_INVISIBLE(SETUP_SET_VARIABLE):
	var_name = "mcr_sysmgr_sw_tcr2servicesession"
	value = False

class VALIDATE_ACTUAL_R_PERCENT_STRING_NA_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_rangeactual_delta_visibility"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_ACTUAL_B1B2_TESLA(SETUP_SET_VARIABLE):
	var_name = "mcr_ecubtcu_group3_corrected_ffeedback"
	value = 0.5

class VALIDATE_ACTUAL_B1B2_TESLA(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_rangeactual_b1b2"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class SET_MESSAGE_EXPECTED_R_G_CM2_FIRST_LAYER(SETUP_SET_VARIABLE):
	var_name = "tr2_beamline_range_sp"
	value = 0.5

class VALIDATE_EXPECTED_R_G_CM2_FIRST_LAYER(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_rangeactual_r_service"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class SET_MESSAGE_EXPECTED_R_G_CM2_FIRST_LAYER_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "mcr_sysmgr_sw_tcr2servicesession"
	value = True

class VALIDATE_EXPECTED_R_G_CM2_FIRST_LAYER_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_rangeactual_r_service"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_EXPECTED_R_G_CM2_FIRST_LAYER_INVISIBLE(SETUP_SET_VARIABLE):
	var_name = "mcr_sysmgr_sw_tcr2servicesession"
	value = False

class VALIDATE_EXPECTED_R_G_CM2_FIRST_LAYER_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_rangeactual_r_service"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE


class SET_MESSAGE_EXPECTED_R_G_CM2_SECOND_LAYER(SETUP_SET_VARIABLE):
	var_name = "tr2_trmgr_sw_rangePat"
	value = 0.6

class VALIDATE_EXPECTED_R_G_CM2_SECOND_LAYER(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_rangeexpected_r"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.6

class SET_MESSAGE_EXPECTED_R_G_CM2_SECOND_LAYER_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "mcr_sysmgr_sw_tcr2servicesession"
	value = False

class VALIDATE_EXPECTED_R_G_CM2_SECOND_LAYER_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_rangeexpected_r"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_EXPECTED_R_G_CM2_SECOND_LAYER_INVISIBLE(SETUP_SET_VARIABLE):
	var_name = "mcr_sysmgr_sw_tcr2servicesession"
	value = True

class VALIDATE_EXPECTED_R_G_CM2_SECOND_LAYER_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_rangeexpected_r"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_EXPECTED_R_PERCENT_STRING_00_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "mcr_sysmgr_sw_tcr2servicesession"
	value = False

class VALIDATE_EXPECTED_R_PERCENT_STRING_00_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_rangeexpect_delta_default"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_EXPECTED_R_PERCENT_STRING_00_INVISIBLE(SETUP_SET_VARIABLE):
	var_name = "mcr_sysmgr_sw_tcr2servicesession"
	value = True

class VALIDATE_EXPECTED_R_PERCENT_STRING_00_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_rangeexpect_delta_default"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_EXPECTED_R_PERCENT_STRING_NA_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "mcr_sysmgr_sw_tcr2servicesession"
	value = True

class VALIDATE_EXPECTED_R_PERCENT_STRING_NA_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_rangeexpect_delta_visibility"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_EXPECTED_R_PERCENT_STRING_NA_INVISIBLE(SETUP_SET_VARIABLE):
	var_name = "mcr_sysmgr_sw_tcr2servicesession"
	value = False

class VALIDATE_EXPECTED_R_PERCENT_STRING_NA_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_rangeexpect_delta_visibility"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_EXPECTED_B1B2_TESLA(SETUP_SET_VARIABLE):
	var_name = "tr2_trmgr_sw_expectedB1B2"
	value = 0.6

class VALIDATE_EXPECTED_B1B2_TESLA(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_rangeexpected_b1b2"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.6

class SET_MESSAGE_EXPECTED_B1B2_TESLA_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "mcr_sysmgr_sw_tcr2servicesession"
	value = False

class VALIDATE_EXPECTED_B1B2_TESLA_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_rangeexpected_b1b2"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_EXPECTED_B1B2_TESLA_INVISIBLE(SETUP_SET_VARIABLE):
	var_name = "mcr_sysmgr_sw_tcr2servicesession"
	value = True

class VALIDATE_EXPECTED_B1B2_TESLA_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_rangeexpected_b1b2"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_EXPECTED_B1B2_TESLA_STRING_NA_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "mcr_sysmgr_sw_tcr2servicesession"
	value = True

class VALIDATE_EXPECTED_B1B2_TESLA_STRING_NA_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_rangeexpect_b1b2_visibility"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_EXPECTED_B1B2_TESLA_STRING_NA_INVISIBLE(SETUP_SET_VARIABLE):
	var_name = "mcr_sysmgr_sw_tcr2servicesession"
	value = False

class VALIDATE_EXPECTED_B1B2_TESLA_STRING_NA_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_rangeexpect_b1b2_visibility"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_RECTANGLE_HIDE_LAYER_DOSIMETRY_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_sw_mode"
	value = 2.0

class VALIDATE_RECTANGLE_HIDE_LAYER_DOSIMETRY_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_area_layer_dosimetry_visibility"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_RECTANGLE_HIDE_LAYER_DOSIMETRY_INVISIBLE_1(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_sw_mode"
	value = 2.8

class VALIDATE_RECTANGLE_HIDE_LAYER_DOSIMETRY_INVISIBLE_1(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_area_layer_dosimetry_visibility"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_RECTANGLE_HIDE_LAYER_DOSIMETRY_INVISIBLE_2(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_sw_mode"
	value = 0.7

class VALIDATE_RECTANGLE_HIDE_LAYER_DOSIMETRY_INVISIBLE_2(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_area_layer_dosimetry_visibility"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_TEXT_LAYER_DOSIMETRY_INVISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_sw_mode"
	value = 2.0

class VALIDATE_TEXT_LAYER_DOSIMETRY_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_text_layer_dosimetry_visibility"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_TEXT_LAYER_DOSIMETRY_VISIBLE_1(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_sw_mode"
	value = 2.8

class SET_MESSAGE_TEXT_LAYER_DOSIMETRY_VISIBLE_2(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_sw_mode"
	value = 0.5

class VALIDATE_TEXT_LAYER_DOSIMETRY_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_text_layer_dosimetry_visibility"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_ACTUALMU_IC2_LAYER_DOSIMETRY_FIRST_LAYER(SETUP_SET_VARIABLE):
	var_name = "tr2_pbs_iceu2_layerdose"
	value = 0.5

class VALIDATE_ACTUALMU_IC2_LAYER_DOSIMETRY_FIRST_LAYER(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2_treatment_pbs_2"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class SET_MESSAGE_ACTUALMU_IC2_LAYER_DOSIMETRY_FIRST_LAYER_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 2.5

class VALIDATE_ACTUALMU_IC2_LAYER_DOSIMETRY_FIRST_LAYER_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2_treatment_pbs_2"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_ACTUALMU_IC2_LAYER_DOSIMETRY_FIRST_LAYER_INVISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 2.0

class VALIDATE_ACTUALMU_IC2_LAYER_DOSIMETRY_FIRST_LAYER_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2_treatment_pbs_2"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_ACTUALMU_IC2_LAYER_DOSIMETRY_SECOND_LAYER(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_iceu2_dose"
	value = 0.5

class VALIDATE_ACTUALMU_IC2_LAYER_DOSIMETRY_SECOND_LAYER(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2_treatment_wb_2"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class SET_MESSAGE_ACTUALMU_IC2_LAYER_DOSIMETRY_SECOND_LAYER_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 1.0

class VALIDATE_ACTUALMU_IC2_LAYER_DOSIMETRY_SECOND_LAYER_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2_treatment_wb_2"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_ACTUALMU_IC2_LAYER_DOSIMETRY_SECOND_LAYER_INVISIBLE_1(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 0.3

class VALIDATE_ACTUALMU_IC2_LAYER_DOSIMETRY_SECOND_LAYER_INVISIBLE_1(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2_treatment_wb_2"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_ACTUALMU_IC2_LAYER_DOSIMETRY_SECOND_LAYER_INVISIBLE_2(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 2.5

class VALIDATE_ACTUALMU_IC2_LAYER_DOSIMETRY_SECOND_LAYER_INVISIBLE_2(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_actual_ic2_treatment_wb_2"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_ACTUALMU_IC3_FIRST_LAYER_DOSIMETRY(SETUP_SET_VARIABLE):
	var_name = "tr2_pbs_iceu3_layerdose"
	value = 0.5

class VALIDATE_ACTUALMU_IC3_FIRST_LAYER_DOSIMETRY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_actual_ic3_service_pbs"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class SET_MESSAGE_ACTUALMU_IC3_FIRST_LAYER_DOSIMETRY_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 2.7

class VALIDATE_ACTUALMU_IC3_FIRST_LAYER_DOSIMETRY_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_actual_ic3_service_pbs"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_ACTUALMU_IC3_FIRST_LAYER_DOSIMETRY_INVISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 0.3

class VALIDATE_ACTUALMU_IC3_FIRST_LAYER_DOSIMETRY_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_actual_ic3_service_pbs"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE


class SET_MESSAGE_ACTUALMU_IC3_SECOND_LAYER_DOSIMETRY(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_iceu3_dose"
	value = 0.5

class VALIDATE_ACTUALMU_IC3_SECOND_LAYER_DOSIMETRY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_actual_ic3_service_wb"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class SET_MESSAGE_ACTUALMU_IC3_SECOND_LAYER_DOSIMETRY_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 1.0

class VALIDATE_ACTUALMU_IC3_SECOND_LAYER_DOSIMETRY_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_actual_ic3_service_wb"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_ACTUALMU_IC3_SECOND_LAYER_DOSIMETRY_INVISIBLE_1(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 0.3

class VALIDATE_ACTUALMU_IC3_SECOND_LAYER_DOSIMETRY_INVISIBLE_1(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_actual_ic3_service_wb"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_ACTUALMU_IC3_SECOND_LAYER_DOSIMETRY_INVISIBLE_2(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 2.0

class VALIDATE_ACTUALMU_IC3_SECOND_LAYER_DOSIMETRY_INVISIBLE_2(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_actual_ic3_service_wb"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_PRESETMU_IC2_LAYERDOSIMETRY_STRING_NOTLOADED_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 0.3

class VALIDATE_PRESETMU_IC2_LAYERDOSIMETRY_STRING_NOTLOADED_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_preset_ic2_visibility_2"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_PRESETMU_IC2_LAYERDOSIMETRY_STRING_NOTLOADED_INVISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 2.0

class VALIDATE_PRESETMU_IC2_LAYERDOSIMETRY_STRING_NOTLOADED_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_preset_ic2_visibility_2"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_PRESETMU_IC2_FIRST_LAYER_DOSIMETRY(SETUP_SET_VARIABLE):
	var_name = "tr2_trmgr_sw_pbslayer_presetdoseic2"
	value = 0.5

class VALIDATE_PRESETMU_IC2_FIRST_LAYER_DOSIMETRY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_preset_ic2_wb_2"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class SET_MESSAGE_PRESETMU_IC2_FIRST_LAYER_DOSIMETRY_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 2.7

class VALIDATE_PRESETMU_IC2_FIRST_LAYER_DOSIMETRY_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_preset_ic2_wb_2"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_PRESETMU_IC2_FIRST_LAYER_DOSIMETRY_INVISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 0.3

class VALIDATE_PRESETMU_IC2_FIRST_LAYER_DOSIMETRY_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_preset_ic2_wb_2"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_PRESETMU_IC2_SECOND_LAYER_DOSIMETRY(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_iceu2_presetdose"
	value = 0.5

class VALIDATE_PRESETMU_IC2_SECOND_LAYER_DOSIMETRY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_preset_ic2_wb_3"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class SET_MESSAGE_PRESETMU_IC2_SECOND_LAYER_DOSIMETRY_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 1.0

class VALIDATE_PRESETMU_IC2_SECOND_LAYER_DOSIMETRY_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_preset_ic2_wb_3"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_PRESETMU_IC2_SECOND_LAYER_DOSIMETRY_INVISIBLE_1(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 0.3

class VALIDATE_PRESETMU_IC2_SECOND_LAYER_DOSIMETRY_INVISIBLE_1(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_preset_ic2_wb_3"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_PRESETMU_IC2_SECOND_LAYER_DOSIMETRY_INVISIBLE_2(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 0.3
class VALIDATE_PRESETMU_IC2_SECOND_LAYER_DOSIMETRY_INVISIBLE_2(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_preset_ic2_wb_3"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_PRESETMU_IC3_LAYERDOSIMETRY_STRING_NOTLOADER_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 0.3

class VALIDATE_PRESETMU_IC3_LAYERDOSIMETRY_STRING_NOTLOADER_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_preset_ic3_visibility_2"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_PRESETMU_IC3_LAYERDOSIMETRY_STRING_NOTLOADER_INVISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 2.0

class VALIDATE_PRESETMU_IC3_LAYERDOSIMETRY_STRING_NOTLOADER_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_preset_ic3_visibility_2"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_PRESETMU_IC3_FIRST_LAYER_DOSIMETRY(SETUP_SET_VARIABLE):
	var_name = "tr2_trmgr_sw_pbslayer_presetdoseic3"
	value = 0.5

class VALIDATE_PRESETMU_IC3_FIRST_LAYER_DOSIMETRY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_preset_ic3_treatment_pbs_2"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class SET_MESSAGE_PRESETMU_IC3_FIRST_LAYER_DOSIMETRY_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 2.7

class VALIDATE_PRESETMU_IC3_FIRST_LAYER_DOSIMETRY_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_preset_ic3_treatment_pbs_2"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_PRESETMU_IC3_FIRST_LAYER_DOSIMETRY_INVISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 0.3

class VALIDATE_PRESETMU_IC3_FIRST_LAYER_DOSIMETRY_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_preset_ic3_treatment_pbs_2"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_PRESETMU_IC3_SECOND_LAYER_DOSIMETRY(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_iceu3_presetdose"
	value = 0.5

class VALIDATE_PRESETMU_IC3_SECOND_LAYER_DOSIMETRY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_preset_ic3_treatment_wb_2"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class SET_MESSAGE_PRESETMU_IC3_SECOND_LAYER_DOSIMETRY_VISIBLE(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 0.8

class VALIDATE_PRESETMU_IC3_SECOND_LAYER_DOSIMETRY_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_preset_ic3_treatment_wb_2"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = VISIBLE

class SET_MESSAGE_PRESETMU_IC3_SECOND_LAYER_DOSIMETRY_INVISIBLE_1(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 0.3

class VALIDATE_PRESETMU_IC3_SECOND_LAYER_DOSIMETRY_INVISIBLE_1(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_preset_ic3_treatment_wb_2"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_PRESETMU_IC3_SECOND_LAYER_DOSIMETRY_INVISIBLE_2(SETUP_SET_VARIABLE):
	var_name = "tr2_rtietcu_presetdose_visible"
	value = 2.0

class VALIDATE_PRESETMU_IC3_SECOND_LAYER_DOSIMETRY_INVISIBLE_2(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_dos_preset_ic3_treatment_wb_2"
	info_type = "TMMI_MCR_IS_VISIBLE"
	expected_value = INVISIBLE

class SET_MESSAGE_TOTALLAYER_LAYERDOSIMETRY(SETUP_SET_VARIABLE):
	var_name = "tr2_trmgr_sw_numberlayer"
	value = 0.5

class VALIDATE_TOTALLAYER_LAYERDOSIMETRY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_total_layer_dosimetry"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class SET_MESSAGE_CURRENTLAYER_LAYERDOSIMETRY(SETUP_SET_VARIABLE):
	var_name = "tr2_trmgr_sw_currentlayer"
	value = 0.5

class VALIDATE_CURRENTLAYER_LAYERDOSIMETRY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_current_layer_dosimetry"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class SET_MESSAGE_MCR2_TR2_ICEU1_QC1_IC1X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu1_QC01"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC1_IC1X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc1"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC1_IC1X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc1"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU1_QC1_IC1X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc1"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU1_QC1_IC1X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc1"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU1_QC2_IC1X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu1_QC02"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC2_IC1X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc2"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC2_IC1X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc2"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU1_QC2_IC1X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc2"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU1_QC2_IC1X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc2"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU1_QC3_IC1X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu1_QC03"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC3_IC1X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc3"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC3_IC1X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc3"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU1_QC3_IC1X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc3"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU1_QC3_IC1X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc3"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU1_QC4_IC1X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu1_QC04"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC4_IC1X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc4"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC4_IC1X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc4"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU1_QC4_IC1X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc4"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU1_QC4_IC1X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc4"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU1_QC5_IC1X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu1_QC05"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC5_IC1X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc5"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC5_IC1X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc5"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU1_QC5_IC1X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc5"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU1_QC5_IC1X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc5"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU1_QC6_IC1X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu1_QC06"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC6_IC1X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc6"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC6_IC1X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc6"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU1_QC6_IC1X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc6"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU1_QC6_IC1X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc6"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU1_QC7_IC1X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu1_QC07"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC7_IC1X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc7"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC7_IC1X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc7"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU1_QC7_IC1X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc7"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU1_QC7_IC1X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc7"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU1_QC8_IC1X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu1_QC08"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC8_IC1X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc8"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC8_IC1X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc8"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU1_QC8_IC1X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc8"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU1_QC8_IC1X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc8"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU1_QC9_IC1X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu1_QC09"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC9_IC1X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc9"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC9_IC1X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc9"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU1_QC9_IC1X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc9"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU1_QC9_IC1X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc9"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU1_QC10_IC1X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu1_QC10"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC10_IC1X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc10"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC10_IC1X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc10"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU1_QC10_IC1X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc10"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU1_QC10_IC1X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc10"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU1_QC11_IC1X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu1_QC11"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC11_IC1X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc11"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC11_IC1X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc11"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU1_QC11_IC1X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc11"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU1_QC11_IC1X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc11"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU1_QC12_IC1X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu1_QC12"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC12_IC1X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc12"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC12_IC1X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc12"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU1_QC12_IC1X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc12"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU1_QC12_IC1X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc12"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"

class SET_MESSAGE_MCR2_TR2_ICEU3_QC1_IC3X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu3_QC01"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC1_IC3X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc1"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC1_IC3X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc1"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU3_QC1_IC3X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc1"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU3_QC1_IC3X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc1"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU3_QC2_IC3X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu3_QC02"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC2_IC3X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc2"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC2_IC3X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc2"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU3_QC2_IC3X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc2"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU3_QC2_IC3X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc2"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU3_QC3_IC3X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu3_QC03"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC3_IC3X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc3"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC3_IC3X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc3"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU3_QC3_IC3X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc3"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU3_QC3_IC3X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc3"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU3_QC4_IC3X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu3_QC04"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC4_IC3X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc4"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC4_IC3X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc4"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU3_QC4_IC3X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc4"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU3_QC4_IC3X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc4"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU3_QC5_IC3X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu3_QC05"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC5_IC3X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc5"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC5_IC3X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc5"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU3_QC5_IC3X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc5"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU3_QC5_IC3X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc5"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU3_QC6_IC3X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu3_QC06"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC6_IC3X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc6"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC6_IC3X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc6"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU3_QC6_IC3X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc6"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU3_QC6_IC3X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc6"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU3_QC7_IC3X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu3_QC07"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC7_IC3X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc7"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC7_IC3X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc7"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU3_QC7_IC3X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc7"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU3_QC7_IC3X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc7"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU3_QC8_IC3X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu3_QC08"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC8_IC3X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc8"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC8_IC3X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc8"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU3_QC8_IC3X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc8"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU3_QC8_IC3X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc8"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU3_QC9_IC3X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu3_QC09"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC9_IC3X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc9"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC9_IC3X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc9"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU3_QC9_IC3X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc9"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU3_QC9_IC3X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc9"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU3_QC10_IC3X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu3_QC10"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC10_IC3X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc10"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC10_IC3X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc10"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU3_QC10_IC3X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc10"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU3_QC10_IC3X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc10"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU3_QC11_IC3X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu3_QC11"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC11_IC3X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc11"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC11_IC3X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc11"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU3_QC11_IC3X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc11"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU3_QC11_IC3X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc11"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU3_QC12_IC3X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu3_QC12"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC12_IC3X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc12"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC12_IC3X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc12"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU3_QC12_IC3X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc12"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU3_QC12_IC3X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc12"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU3_QC13_IC3X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu3_QC13"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC13_IC3X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc13"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC13_IC3X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc13"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU3_QC13_IC3X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc13"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU3_QC13_IC3X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc13"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU3_QC14_IC3X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu3_QC14"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC14_IC3X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc14"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC14_IC3X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc14"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU3_QC14_IC3X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc14"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU3_QC14_IC3X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc14"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU3_QC15_IC3X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu3_QC15"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC15_IC3X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc15"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC15_IC3X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc15"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU3_QC15_IC3X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc15"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU3_QC15_IC3X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc15"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU3_QC16_IC3X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu3_QC16"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC16_IC3X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc16"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC16_IC3X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc16"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU3_QC16_IC3X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc16"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU3_QC16_IC3X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc16"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU3_QC17_IC3X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu3_QC17"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC17_IC3X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc17"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC17_IC3X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc17"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU3_QC17_IC3X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc17"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU3_QC17_IC3X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc17"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU3_QC18_IC3X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu3_QC18"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC18_IC3X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc18"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC18_IC3X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc18"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU3_QC18_IC3X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc18"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU3_QC18_IC3X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc18"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU3_QC19_IC3X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu3_QC19"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC19_IC3X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc19"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC19_IC3X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc19"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU3_QC19_IC3X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc19"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU3_QC19_IC3X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc19"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU3_QC20_IC3X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu3_QC20"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC20_IC3X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc20"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC20_IC3X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc20"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU3_QC20_IC3X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc20"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU3_QC20_IC3X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc20"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU3_QC21_IC3X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu3_QC21"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC21_IC3X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc21"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC21_IC3X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc21"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU3_QC21_IC3X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc21"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU3_QC21_IC3X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc21"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU3_QC22_IC3X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu3_QC22"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC22_IC3X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc22"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC22_IC3X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc22"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU3_QC22_IC3X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc22"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU3_QC22_IC3X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc22"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU3_QC23_IC3X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu3_QC23"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC23_IC3X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc23"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC23_IC3X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc23"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU3_QC23_IC3X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc23"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU3_QC23_IC3X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc23"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU3_QC24_IC3X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu3_QC24"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC24_IC3X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc24"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC24_IC3X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc24"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU3_QC24_IC3X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc24"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU3_QC24_IC3X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc24"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU3_QC25_IC3X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu3_QC25"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC25_IC3X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc25"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC25_IC3X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc25"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU3_QC25_IC3X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc25"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU3_QC25_IC3X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc25"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU3_QC26_IC3X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu3_QC26"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC26_IC3X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc26"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC26_IC3X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc26"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU3_QC26_IC3X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc26"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU3_QC26_IC3X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc26"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU3_QC27_IC3X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu3_QC27"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC27_IC3X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc27"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC27_IC3X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc27"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU3_QC27_IC3X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc27"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU3_QC27_IC3X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc27"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU3_QC28_IC3X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu3_QC28"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC28_IC3X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc28"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC28_IC3X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc28"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU3_QC28_IC3X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc28"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU3_QC28_IC3X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc28"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU3_QC29_IC3X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu3_QC29"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC29_IC3X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc29"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC29_IC3X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc29"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU3_QC29_IC3X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc29"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU3_QC29_IC3X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc29"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU3_QC30_IC3X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu3_QC30"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC30_IC3X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc30"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC30_IC3X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc30"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU3_QC30_IC3X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc30"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU3_QC30_IC3X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc30"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU3_QC31_IC3X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu3_QC31"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC31_IC3X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc31"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC31_IC3X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc31"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU3_QC31_IC3X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc31"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU3_QC31_IC3X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc31"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU3_QC32_IC3X(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu3_QC32"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC32_IC3X(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc32"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU3_QC32_IC3X_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc32"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU3_QC32_IC3X_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc32"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU3_QC32_IC3X_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu3_qc32"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_ICEU1_QC13_IC1Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu1_QC13"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC13_IC1Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc13"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC13_IC1Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc13"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU1_QC13_IC1Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc13"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU1_QC13_IC1Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc13"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU1_QC14_IC1Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu1_QC14"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC14_IC1Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc14"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC14_IC1Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc14"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU1_QC14_IC1Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc14"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU1_QC14_IC1Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc14"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU1_QC15_IC1Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu1_QC15"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC15_IC1Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc15"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC15_IC1Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc15"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU1_QC15_IC1Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc15"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU1_QC15_IC1Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc15"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU1_QC16_IC1Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu1_QC16"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC16_IC1Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc16"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC16_IC1Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc16"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU1_QC16_IC1Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc16"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU1_QC16_IC1Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc16"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU1_QC17_IC1Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu1_QC17"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC17_IC1Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc17"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC17_IC1Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc17"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU1_QC17_IC1Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc17"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU1_QC17_IC1Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc17"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU1_QC18_IC1Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu1_QC18"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC18_IC1Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc18"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC18_IC1Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc18"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU1_QC18_IC1Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc18"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU1_QC18_IC1Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc18"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU1_QC19_IC1Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu1_QC19"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC19_IC1Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc19"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC19_IC1Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc19"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU1_QC19_IC1Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc19"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU1_QC19_IC1Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc19"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU1_QC20_IC1Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu1_QC20"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC20_IC1Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc20"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC20_IC1Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc20"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU1_QC20_IC1Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc20"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU1_QC20_IC1Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc20"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU1_QC21_IC1Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu1_QC21"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC21_IC1Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc21"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC21_IC1Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc21"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU1_QC21_IC1Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc21"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU1_QC21_IC1Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc21"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU1_QC22_IC1Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu1_QC22"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC22_IC1Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc22"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC22_IC1Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc22"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU1_QC22_IC1Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc22"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU1_QC22_IC1Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc22"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU1_QC23_IC1Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu1_QC23"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC23_IC1Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc23"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC23_IC1Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc23"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU1_QC23_IC1Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc23"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU1_QC23_IC1Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc23"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU1_QC24_IC1Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu1_QC24"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC24_IC1Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc24"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU1_QC24_IC1Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc24"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU1_QC24_IC1Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc24"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU1_QC24_IC1Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu1_qc24"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"

class SET_MESSAGE_MCR2_TR2_ICEU2_QC1_IC3Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu2_QC01"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC1_IC3Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc1"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC1_IC3Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc1"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU2_QC1_IC3Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc1"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU2_QC1_IC3Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc1"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU2_QC2_IC3Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu2_QC02"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC2_IC3Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc2"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC2_IC3Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc2"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU2_QC2_IC3Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc2"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU2_QC2_IC3Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc2"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU2_QC3_IC3Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu2_QC03"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC3_IC3Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc3"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC3_IC3Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc3"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU2_QC3_IC3Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc3"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU2_QC3_IC3Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc3"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU2_QC4_IC3Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu2_QC04"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC4_IC3Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc4"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC4_IC3Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc4"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU2_QC4_IC3Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc4"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU2_QC4_IC3Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc4"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU2_QC5_IC3Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu2_QC05"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC5_IC3Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc5"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC5_IC3Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc5"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU2_QC5_IC3Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc5"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU2_QC5_IC3Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc5"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU2_QC6_IC3Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu2_QC06"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC6_IC3Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc6"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC6_IC3Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc6"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU2_QC6_IC3Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc6"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU2_QC6_IC3Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc6"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU2_QC7_IC3Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu2_QC07"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC7_IC3Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc7"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC7_IC3Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc7"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU2_QC7_IC3Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc7"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU2_QC7_IC3Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc7"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU2_QC8_IC3Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu2_QC08"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC8_IC3Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc8"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC8_IC3Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc8"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU2_QC8_IC3Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc8"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU2_QC8_IC3Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc8"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU2_QC9_IC3Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu2_QC09"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC9_IC3Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc9"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC9_IC3Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc9"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU2_QC9_IC3Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc9"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU2_QC9_IC3Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc9"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU2_QC10_IC3Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu2_QC10"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC10_IC3Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc10"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC10_IC3Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc10"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU2_QC10_IC3Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc10"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU2_QC10_IC3Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc10"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU2_QC11_IC3Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu2_QC11"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC11_IC3Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc11"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC11_IC3Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc11"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU2_QC11_IC3Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc11"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU2_QC11_IC3Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc11"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU2_QC12_IC3Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu2_QC12"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC12_IC3Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc12"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC12_IC3Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc12"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU2_QC12_IC3Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc12"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU2_QC12_IC3Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc12"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU2_QC13_IC3Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu2_QC13"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC13_IC3Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc13"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC13_IC3Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc13"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU2_QC13_IC3Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc13"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU2_QC13_IC3Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc13"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU2_QC14_IC3Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu2_QC14"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC14_IC3Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc14"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC14_IC3Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc14"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU2_QC14_IC3Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc14"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU2_QC14_IC3Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc14"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU2_QC15_IC3Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu2_QC15"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC15_IC3Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc15"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC15_IC3Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc15"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU2_QC15_IC3Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc15"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU2_QC15_IC3Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc15"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU2_QC16_IC3Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu2_QC16"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC16_IC3Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc16"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC16_IC3Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc16"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU2_QC16_IC3Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc16"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU2_QC16_IC3Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc16"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU2_QC17_IC3Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu2_QC17"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC17_IC3Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc17"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC17_IC3Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc17"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU2_QC17_IC3Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc17"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU2_QC17_IC3Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc17"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU2_QC18_IC3Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu2_QC18"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC18_IC3Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc18"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC18_IC3Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc18"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU2_QC18_IC3Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc18"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU2_QC18_IC3Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc18"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU2_QC19_IC3Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu2_QC19"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC19_IC3Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc19"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC19_IC3Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc19"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU2_QC19_IC3Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc19"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU2_QC19_IC3Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc19"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU2_QC20_IC3Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu2_QC20"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC20_IC3Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc20"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC20_IC3Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc20"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU2_QC20_IC3Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc20"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU2_QC20_IC3Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc20"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU2_QC21_IC3Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu2_QC21"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC21_IC3Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc21"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC21_IC3Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc21"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU2_QC21_IC3Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc21"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU2_QC21_IC3Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc21"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU2_QC22_IC3Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu2_QC22"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC22_IC3Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc22"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC22_IC3Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc22"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU2_QC22_IC3Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc22"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU2_QC22_IC3Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc22"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU2_QC23_IC3Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu2_QC23"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC23_IC3Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc23"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC23_IC3Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc23"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU2_QC23_IC3Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc23"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU2_QC23_IC3Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc23"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU2_QC24_IC3Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu2_QC24"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC24_IC3Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc24"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC24_IC3Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc24"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU2_QC24_IC3Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc24"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU2_QC24_IC3Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc24"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU2_QC25_IC3Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu2_QC25"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC25_IC3Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc25"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC25_IC3Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc25"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU2_QC25_IC3Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc25"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU2_QC25_IC3Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc25"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU2_QC26_IC3Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu2_QC26"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC26_IC3Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc26"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC26_IC3Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc26"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU2_QC26_IC3Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc26"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU2_QC26_IC3Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc26"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU2_QC27_IC3Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu2_QC27"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC27_IC3Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc27"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC27_IC3Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc27"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU2_QC27_IC3Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc27"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU2_QC27_IC3Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc27"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU2_QC28_IC3Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu2_QC28"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC28_IC3Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc28"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC28_IC3Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc28"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU2_QC28_IC3Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc28"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU2_QC28_IC3Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc28"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU2_QC29_IC3Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu2_QC29"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC29_IC3Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc29"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC29_IC3Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc29"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU2_QC29_IC3Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc29"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU2_QC29_IC3Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc29"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU2_QC30_IC3Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu2_QC30"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC30_IC3Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc30"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC30_IC3Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc30"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU2_QC30_IC3Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc30"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU2_QC30_IC3Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc30"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU2_QC31_IC3Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu2_QC31"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC31_IC3Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc31"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC31_IC3Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc31"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU2_QC31_IC3Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc31"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU2_QC31_IC3Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc31"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"


class SET_MESSAGE_MCR2_TR2_ICEU2_QC32_IC3Y(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_iceu2_QC32"
	value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC32_IC3Y(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc32"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_ICEU2_QC32_IC3Y_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc32"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_ICEU2_QC32_IC3Y_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc32"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_ICEU2_QC32_IC3Y_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_iceu2_qc32"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "RIGHT"

class SET_MESSAGE_MCR2_TR2_RVEU_QC1_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC01"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC1_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc1"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC1_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc1"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC1_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc1"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC1_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc1"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC2_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC02"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC2_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc2"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC2_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc2"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC2_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc2"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC2_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc2"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC3_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC03"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC3_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc3"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC3_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc3"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC3_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc3"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC3_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc3"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC4_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC04"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC4_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc4"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC4_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc4"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC4_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc4"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC4_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc4"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC5_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC05"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC5_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc5"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC5_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc5"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC5_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc5"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC5_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc5"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC6_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC06"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC6_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc6"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC6_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc6"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC6_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc6"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC6_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc6"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC7_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC07"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC7_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc7"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC7_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc7"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC7_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc7"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC7_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc7"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC8_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC08"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC8_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc8"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC8_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc8"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC8_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc8"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC8_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc8"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC9_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC09"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC9_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc9"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC9_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc9"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC9_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc9"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC9_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc9"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC10_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC10"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC10_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc10"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC10_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc10"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC10_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc10"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC10_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc10"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC11_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC11"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC11_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc11"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC11_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc11"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC11_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc11"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC11_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc11"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC12_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC12"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC12_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc12"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC12_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc12"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC12_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc12"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC12_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc12"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC13_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC13"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC13_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc13"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC13_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc13"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC13_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc13"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC13_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc13"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC14_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC14"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC14_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc14"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC14_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc14"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC14_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc14"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC14_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc14"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC15_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC15"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC15_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc15"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC15_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc15"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC15_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc15"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC15_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc15"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC16_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC16"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC16_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc16"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC16_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc16"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC16_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc16"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC16_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc16"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC17_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC17"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC17_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc17"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC17_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc17"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC17_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc17"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC17_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc17"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC18_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC18"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC18_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc18"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC18_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc18"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC18_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc18"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC18_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc18"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC19_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC19"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC19_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc19"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC19_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc19"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC19_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc19"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC19_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc19"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC20_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC20"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC20_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc20"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC20_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc20"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC20_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc20"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC20_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc20"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC21_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC21"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC21_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc21"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC21_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc21"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC21_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc21"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC21_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc21"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC22_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC22"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC22_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc22"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC22_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc22"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC22_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc22"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC22_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc22"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC23_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC23"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC23_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc23"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC23_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc23"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC23_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc23"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC23_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc23"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC24_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC24"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC24_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc24"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC24_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc24"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC24_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc24"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC24_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc24"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC25_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC25"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC25_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc25"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC25_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc25"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC25_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc25"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC25_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc25"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC26_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC26"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC26_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc26"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC26_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc26"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC26_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc26"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC26_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc26"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC27_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC27"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC27_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc27"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC27_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc27"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC27_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc27"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC27_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc27"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC28_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC28"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC28_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc28"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC28_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc28"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC28_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc28"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC28_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc28"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC29_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC29"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC29_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc29"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC29_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc29"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC29_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc29"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC29_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc29"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC30_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC30"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC30_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc30"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC30_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc30"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC30_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc30"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC30_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc30"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC31_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC31"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC31_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc31"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC31_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc31"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC31_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc31"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC31_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc31"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC32_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC32"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC32_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc32"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC32_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc32"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC32_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc32"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC32_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc32"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"

class SET_MESSAGE_MCR2_TR2_RVEU_QC33_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC33"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC33_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc33"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC33_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc33"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC33_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc33"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC33_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc33"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC34_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC34"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC34_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc34"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC34_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc34"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC34_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc34"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC34_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc34"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC35_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC35"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC35_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc35"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC35_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc35"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC35_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc35"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC35_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc35"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC36_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC36"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC36_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc36"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC36_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc36"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC36_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc36"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC36_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc36"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC37_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC37"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC37_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc37"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC37_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc37"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC37_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc37"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC37_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc37"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC38_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC38"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC38_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc38"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC38_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc38"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC38_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc38"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC38_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc38"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC39_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC39"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC39_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc39"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC39_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc39"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC39_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc39"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC39_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc39"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC40_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC40"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC40_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc40"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC40_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc40"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC40_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc40"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC40_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc40"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC41_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC41"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC41_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc41"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC41_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc41"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC41_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc41"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC41_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc41"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC42_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC42"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC42_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc42"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC42_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc42"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC42_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc42"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC42_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc42"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC43_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC43"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC43_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc43"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC43_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc43"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC43_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc43"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC43_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc43"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC44_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC44"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC44_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc44"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC44_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc44"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC44_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc44"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC44_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc44"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC45_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC45"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC45_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc45"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC45_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc45"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC45_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc45"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC45_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc45"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC46_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC46"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC46_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc46"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC46_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc46"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC46_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc46"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC46_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc46"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC47_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC47"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC47_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc47"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC47_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc47"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC47_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc47"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC47_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc47"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC48_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC48"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC48_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc48"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC48_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc48"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC48_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc48"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC48_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc48"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC49_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC49"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC49_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc49"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC49_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc49"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC49_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc49"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC49_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc49"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC50_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC50"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC50_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc50"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC50_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc50"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC50_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc50"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC50_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc50"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC51_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC51"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC51_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc51"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC51_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc51"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC51_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc51"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC51_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc51"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC52_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC52"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC52_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc52"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC52_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc52"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC52_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc52"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC52_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc52"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC53_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC53"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC53_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc53"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC53_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc53"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC53_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc53"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC53_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc53"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC54_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC54"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC54_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc54"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC54_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc54"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC54_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc54"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC54_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc54"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC55_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC55"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC55_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc55"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC55_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc55"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC55_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc55"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC55_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc55"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC56_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC56"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC56_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc56"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC56_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc56"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC56_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc56"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC56_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc56"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"


class SET_MESSAGE_MCR2_TR2_RVEU_QC57_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC57"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC57_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc57"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC57_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc57"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC57_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc57"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC57_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc57"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"

class SET_MESSAGE_MCR2_TR2_RVEU_QC58_RANGEVERIFY(SETUP_SET_VARIABLE):
	var_name = "tr2_tcu_rveu_QC58"
	value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC58_RANGEVERIFY(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc58"
	info_type = "TMMI_MCR_OBJECT_GET_VALUE"
	expected_value = 0.5

class VALIDATE_MCR2_TR2_RVEU_QC58_RANGEVERIFY_FOREGROUND_COLOR(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc58"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR"
	expected_value = COLOR_BLUE

class VALIDATE_MCR2_TR2_RVEU_QC58_RANGEVERIFY_FILL_AMOUNT(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc58"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"
	expected_value = "16383"

class VALIDATE_MCR2_TR2_RVEU_QC58_RANGEVERIFY_FILL_DIRECTION(SETUP_VALIDATE_OBJECT_INFO):
	object_name = "mcr_treatment_beam_profiles2:mcr2_tr2_rveu_qc58"
	info_type = "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"
	expected_value = "UP"

class __M_BF2_5__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Actual(MU) IC2 Firt Layer in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_ACTUALMU_IC2_FIRST_LAYER,
						VALIDATE_ACTUALMU_IC2_FIRST_LAYER,
						SET_MESSAGE_ACTUALMU_IC2_FIRST_LAYER_VISIBLE,
						VALIDATE_ACTUALMU_IC2_FIRST_LAYER_VISIBLE,
						SET_MESSAGE_ACTUALMU_IC2_FIRST_LAYER_INVISIBLE,
						VALIDATE_ACTUALMU_IC2_FIRST_LAYER_INVISIBLE,
						]
		self.teardown_path = []

class __M_BF2_6__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Actual(MU) IC2 Second Layer in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_ACTUALMU_IC2_SECOND_LAYER,
						VALIDATE_ACTUALMU_IC2_SECOND_LAYER,
						SET_MESSAGE_ACTUALMU_IC2_SECOND_LAYER_VISIBLE,
						VALIDATE_ACTUALMU_IC2_SECOND_LAYER_VISIBLE,
						SET_MESSAGE_ACTUALMU_IC2_SECOND_LAYER_INVISIBLE_1, 
						VALIDATE_ACTUALMU_IC2_SECOND_LAYER_INVISIBLE_1,
						SET_MESSAGE_ACTUALMU_IC2_SECOND_LAYER_INVISIBLE_2,
						VALIDATE_ACTUALMU_IC2_SECOND_LAYER_INVISIBLE_2,
						]
		self.teardown_path = []

class __M_BF2_7__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Actual(MU) IC2 Third Layer in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_ACTUALMU_IC2_THIRD_LAYER,
						VALIDATE_ACTUALMU_IC2_THIRD_LAYER,
						SET_MESSAGE_ACTUALMU_IC2_THIRD_LAYER_VISIBLE,
						VALIDATE_ACTUALMU_IC2_THIRD_LAYER_VISIBLE,
						SET_MESSAGE_ACTUALMU_IC2_THIRD_LAYER_INVISIBLE_1,
						VALIDATE_ACTUALMU_IC2_THIRD_LAYER_INVISIBLE_1,
						SET_MESSAGE_ACTUALMU_IC2_THIRD_LAYER_INVISIBLE_2,
						VALIDATE_ACTUALMU_IC2_THIRD_LAYER_INVISIBLE_2,
						]
		self.teardown_path = []

class __M_BF2_8__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Actual(MU) IC2 Fourth Layer in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_ACTUALMU_IC2_FOURTH_LAYER,
						VALIDATE_ACTUALMU_IC2_FOURTH_LAYER,
						SET_MESSAGE_ACTUALMU_IC2_FOURTH_LAYER_VISIBLE,
						VALIDATE_ACTUALMU_IC2_FOURTH_LAYER_VISIBLE,
						SET_MESSAGE_ACTUALMU_IC2_FOURTH_LAYER_INVISIBLE,
						VALIDATE_ACTUALMU_IC2_FOURTH_LAYER_INVISIBLE,
						]
		self.teardown_path = []

class __M_BF2_9__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Actual(MU) IC3 Firt Layer in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_ACTUALMU_IC3_FIRST_LAYER,
						VALIDATE_ACTUALMU_IC3_FIRST_LAYER,
						SET_MESSAGE_ACTUALMU_IC3_FIRST_LAYER_VISIBLE,
						VALIDATE_ACTUALMU_IC3_FIRST_LAYER_VISIBLE,
						SET_MESSAGE_ACTUALMU_IC3_FIRST_LAYER_INVISIBLE,
						VALIDATE_ACTUALMU_IC3_FIRST_LAYER_INVISIBLE,
						]
		self.teardown_path = []

class __M_BF2_10__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Actual(MU) IC3 Second Layer in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_ACTUALMU_IC3_SECOND_LAYER,
						VALIDATE_ACTUALMU_IC3_SECOND_LAYER,
						SET_MESSAGE_ACTUALMU_IC3_SECOND_LAYER_VISIBLE,
						VALIDATE_ACTUALMU_IC3_SECOND_LAYER_VISIBLE,
						SET_MESSAGE_ACTUALMU_IC3_SECOND_LAYER_INVISIBLE_1,
						VALIDATE_ACTUALMU_IC3_SECOND_LAYER_INVISIBLE_1,
						SET_MESSAGE_ACTUALMU_IC3_SECOND_LAYER_INVISIBLE_2,
						VALIDATE_ACTUALMU_IC3_SECOND_LAYER_INVISIBLE_2,
						]
		self.teardown_path = []

class __M_BF2_11__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Actual(MU) IC3 Thrid Layer in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_ACTUALMU_IC3_THIRD_LAYER,
						VALIDATE_ACTUALMU_IC3_THIRD_LAYER,
						SET_MESSAGE_ACTUALMU_IC3_THIRD_LAYER_VISIBLE,
						VALIDATE_ACTUALMU_IC3_THIRD_LAYER_VISIBLE,
						SET_MESSAGE_ACTUALMU_IC3_THIRD_LAYER_INVISIBLE_1,
						VALIDATE_ACTUALMU_IC3_THIRD_LAYER_INVISIBLE_1,
						SET_MESSAGE_ACTUALMU_IC3_THIRD_LAYER_INVISIBLE_2,
						VALIDATE_ACTUALMU_IC3_THIRD_LAYER_INVISIBLE_2
						]
		self.teardown_path = []

class __M_BF2_12__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Actual(MU) IC3 Fourth Layer in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_ACTUALMU_IC3_FOURTH_LAYER,
						VALIDATE_ACTUALMU_IC3_FOURTH_LAYER,
						SET_MESSAGE_ACTUALMU_IC3_FOURTH_LAYER_VISIBLE,
						VALIDATE_ACTUALMU_IC3_FOURTH_LAYER_VISIBLE,
						SET_MESSAGE_ACTUALMU_IC3_FOURTH_LAYER_INVISIBLE,
						VALIDATE_ACTUALMU_IC3_FOURTH_LAYER_INVISIBLE,
						]
		self.teardown_path = []

class __M_BF2_13__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Actual(MU) IC2/IC3 Firt Layer in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_ACTUALMU_IC2_IC3_FIRST_LAYER_RED_1,
						VALIDATE_ACTUALMU_IC2_IC3_FIRST_LAYER_RED_1,
						VALIDATE_ACTUALMU_IC2_IC3_FIRST_LAYER_BACKGROUND_COLOR_RED_1,
						SET_MESSAGE_ACTUALMU_IC2_IC3_FIRST_LAYER_RED_2,
						VALIDATE_ACTUALMU_IC2_IC3_FIRST_LAYER_RED_2,
						VALIDATE_ACTUALMU_IC2_IC3_FIRST_LAYER_BACKGROUND_COLOR_RED_2,
						SET_MESSAGE_ACTUALMU_IC2_IC3_FIRST_LAYER_YELLOW_1,
						VALIDATE_ACTUALMU_IC2_IC3_FIRST_LAYER_YELLOW_1,
						VALIDATE_ACTUALMU_IC2_IC3_FIRST_LAYER_BACKGROUND_COLOR_YELLOW_1,
						SET_MESSAGE_ACTUALMU_IC2_IC3_FIRST_LAYER_YELLOW_2,
						VALIDATE_ACTUALMU_IC2_IC3_FIRST_LAYER_YELLOW_2,
						VALIDATE_ACTUALMU_IC2_IC3_FIRST_LAYER_BACKGROUND_COLOR_YELLOW_2,
						SET_MESSAGE_ACTUALMU_IC2_IC3_FIRST_LAYER_GRAY,
						VALIDATE_ACTUALMU_IC2_IC3_FIRST_LAYER_GRAY,
						VALIDATE_ACTUALMU_IC2_IC3_FIRST_LAYER_BACKGROUND_COLOR_GRAY,
						SET_MESSAGE_ACTUALMU_IC2_IC3_FIRST_LAYER_VISIBLE,
						VALIDATE_ACTUALMU_IC2_IC3_FIRST_LAYER_VISIBLE,
						SET_MESSAGE_ACTUALMU_IC2_IC3_FIRST_LAYER_INVISIBLE,
						VALIDATE_ACTUALMU_IC2_IC3_FIRST_LAYER_INVISIBLE,
						]
		self.teardown_path = []

class __M_BF2_14__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Actual(MU) IC2/IC3 Second Layer in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_ACTUALMU_IC2_IC3_SECOND_LAYER_RED_1,
						VALIDATE_ACTUALMU_IC2_IC3_SECOND_LAYER_RED_1,
						VALIDATE_ACTUALMU_IC2_IC3_SECOND_LAYER_BACKGROUND_COLOR_RED_1,
						SET_MESSAGE_ACTUALMU_IC2_IC3_SECOND_LAYER_RED_2,
						VALIDATE_ACTUALMU_IC2_IC3_SECOND_LAYER_RED_2,
						VALIDATE_ACTUALMU_IC2_IC3_SECOND_LAYER_BACKGROUND_COLOR_RED_2,
						SET_MESSAGE_ACTUALMU_IC2_IC3_SECOND_LAYER_YELLOW_1,
						VALIDATE_ACTUALMU_IC2_IC3_SECOND_LAYER_YELLOW_1,
						VALIDATE_ACTUALMU_IC2_IC3_SECOND_LAYER_BACKGROUND_COLOR_YELLOW_1,
						SET_MESSAGE_ACTUALMU_IC2_IC3_SECOND_LAYER_YELLOW_2,
						VALIDATE_ACTUALMU_IC2_IC3_SECOND_LAYER_YELLOW_2,
						VALIDATE_ACTUALMU_IC2_IC3_SECOND_LAYER_BACKGROUND_COLOR_YELLOW_2,
						SET_MESSAGE_ACTUALMU_IC2_IC3_SECOND_LAYER_GRAY,
						VALIDATE_ACTUALMU_IC2_IC3_SECOND_LAYER_GRAY,
						VALIDATE_ACTUALMU_IC2_IC3_SECOND_LAYER_BACKGROUND_COLOR_GRAY,
						SET_MESSAGE_ACTUALMU_IC2_IC3_SECOND_LAYER_VISIBLE,
						VALIDATE_ACTUALMU_IC2_IC3_SECOND_LAYER_VISIBLE,
						SET_MESSAGE_ACTUALMU_IC2_IC3_SECOND_LAYER_INVISIBLE,
						VALIDATE_ACTUALMU_IC2_IC3_SECOND_LAYER_INVISIBLE,
						]
		self.teardown_path = []

class __M_BF2_15__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Actual(MU) time Spec in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_ACTUALMU_TIME_SEC,
						VALIDATE_ACTUALMU_TIME_SEC,
						SET_MESSAGE_ACTUALMU_TIME_SEC_VISIBLE,
						VALIDATE_ACTUALMU_TIME_SEC_VISIBLE,
						SET_MESSAGE_ACTUALMU_TIME_SEC_INVISIBLE,
						VALIDATE_ACTUALMU_TIME_SEC_INVISIBLE,
						]
		self.teardown_path = []

class __M_BF2_16__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Actual(MU) Time Spec with String NA in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_ACTUALMU_TIME_SEC_STRING_NA_INVISIBLE,
						VALIDATE_ACTUALMU_TIME_SEC_STRING_NA_INVISIBLE,
						SET_MESSAGE_ACTUALMU_TIME_SEC_STRING_NA_VISIBLE,
						VALIDATE_ACTUALMU_TIME_SEC_STRING_NA_VISIBLE,
						]
		self.teardown_path = []

class __M_BF2_17__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Preset(MU) IC2 Firt Layer in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_PRESETMU_IC2_FIRST_LAYER,
						VALIDATE_PRESETMU_IC2_FIRST_LAYER,
						SET_MESSAGE_PRESETMU_IC2_FIRST_LAYER_VISIBLE,
						VALIDATE_PRESETMU_IC2_FIRST_LAYER_VISIBLE,
						SET_MESSAGE_PRESETMU_IC2_FIRST_LAYER_INVISIBLE,
						VALIDATE_PRESETMU_IC2_FIRST_LAYER_INVISIBLE,
						]
		self.teardown_path = []

class __M_BF2_18__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Actual(MU) IC2 Second Layer in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_PRESETMU_IC2_SECOND_LAYER,
						VALIDATE_PRESETMU_IC2_SECOND_LAYER,
						SET_MESSAGE_PRESETMU_IC2_SECOND_LAYER_VISIBLE,
						VALIDATE_PRESETMU_IC2_SECOND_LAYER_VISIBLE,
						SET_MESSAGE_PRESETMU_IC2_SECOND_LAYER_INVISIBLE_1,
						VALIDATE_PRESETMU_IC2_SECOND_LAYER_INVISIBLE_1,
						SET_MESSAGE_PRESETMU_IC2_SECOND_LAYER_INVISIBLE_2,
						VALIDATE_PRESETMU_IC2_SECOND_LAYER_INVISIBLE_2,
						]
		self.teardown_path = []

class __M_BF2_19__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Preset(MU) IC2 Third Layer in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_PRESETMU_IC2_THIRD_LAYER,
						VALIDATE_PRESETMU_IC2_THIRD_LAYER,
						SET_MESSAGE_PRESETMU_IC2_THIRD_LAYER_VISIBLE,
						VALIDATE_PRESETMU_IC2_THIRD_LAYER_VISIBLE,
						SET_MESSAGE_PRESETMU_IC2_THIRD_LAYER_INVISIBLE_1,
						VALIDATE_PRESETMU_IC2_THIRD_LAYER_INVISIBLE_1,
						SET_MESSAGE_PRESETMU_IC2_THIRD_LAYER_INVISIBLE_2,
						VALIDATE_PRESETMU_IC2_THIRD_LAYER_INVISIBLE_2,
						]
		self.teardown_path = []

class __M_BF2_20__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Preset(MU) IC2 string Not loader in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_PRESETMU_IC2_STRING_NOTLOADER_VISIBLE,
						VALIDATE_PRESETMU_IC2_STRING_NOTLOADER_VISIBLE,
						SET_MESSAGE_PRESETMU_IC2_STRING_NOTLOADER_INVISIBLE,
						VALIDATE_PRESETMU_IC2_STRING_NOTLOADER_INVISIBLE
						]
		self.teardown_path = []

class __M_BF2_21__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Preset(MU) IC2 Firt Layer in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_PRESETMU_IC3_FIRST_LAYER,
						VALIDATE_PRESETMU_IC3_FIRST_LAYER,
						SET_MESSAGE_PRESETMU_IC3_FIRST_LAYER_VISIBLE,
						VALIDATE_PRESETMU_IC3_FIRST_LAYER_VISIBLE,
						SET_MESSAGE_PRESETMU_IC3_FIRST_LAYER_INVISIBLE,
						VALIDATE_PRESETMU_IC3_FIRST_LAYER_INVISIBLE,
						]
		self.teardown_path = []

class __M_BF2_22__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Preset(MU) IC3 Second Layer in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_PRESETMU_IC3_SECOND_LAYER,
						VALIDATE_PRESETMU_IC3_SECOND_LAYER,
						SET_MESSAGE_PRESETMU_IC3_SECOND_LAYER_VISIBLE,
						VALIDATE_PRESETMU_IC3_SECOND_LAYER_VISIBLE,
						SET_MESSAGE_PRESETMU_IC3_SECOND_LAYER_INVISIBLE_1,
						VALIDATE_PRESETMU_IC3_SECOND_LAYER_INVISIBLE_1,
						SET_MESSAGE_PRESETMU_IC3_SECOND_LAYER_INVISIBLE_2,
						VALIDATE_PRESETMU_IC3_SECOND_LAYER_INVISIBLE_2,
						]
		self.teardown_path = []

class __M_BF2_23__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Preset(MU) IC3 Second Layer in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_PRESETMU_IC3_THIRD_LAYER,
						VALIDATE_PRESETMU_IC3_THIRD_LAYER,
						SET_MESSAGE_PRESETMU_IC3_THIRD_LAYER_VISIBLE,
						VALIDATE_PRESETMU_IC3_THIRD_LAYER_VISIBLE,
						SET_MESSAGE_PRESETMU_IC3_THIRD_LAYER_INVISIBLE_1,
						VALIDATE_PRESETMU_IC3_THIRD_LAYER_INVISIBLE_1,
						SET_MESSAGE_PRESETMU_IC3_THIRD_LAYER_INVISIBLE_2,
						VALIDATE_PRESETMU_IC3_THIRD_LAYER_INVISIBLE_2,
						]
		self.teardown_path = []

class __M_BF2_24__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Preset(MU) IC3 Second Layer in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_PRESETMU_IC3_STRING_NOTLOADER_VISIBLE,
						VALIDATE_PRESETMU_IC3_STRING_NOTLOADER_VISIBLE,
						SET_MESSAGE_PRESETMU_IC3_STRING_NOTLOADER_INVISIBLE,
						VALIDATE_PRESETMU_IC3_STRING_NOTLOADER_INVISIBLE,
						]
		self.teardown_path = []

class __M_BF2_25__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Preset(MU) IC2/IC3 First Layer in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_PRESETMU_IC2IC3_FIRST_LAYER,
						VALIDATE_PRESETMU_IC2IC3_FIRST_LAYER,
						SET_MESSAGE_PRESETMU_IC2IC3_FIRST_LAYER_VISIBLE,
						VALIDATE_PRESETMU_IC2IC3_FIRST_LAYER_VISIBLE,
						SET_MESSAGE_PRESETMU_IC2IC3_FIRST_LAYER_INVISIBLE,
						VALIDATE_PRESETMU_IC2IC3_FIRST_LAYER_INVISIBLE
						]
		self.teardown_path = []

class __M_BF2_26__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Preset(MU) IC2/IC3 String Not Loader in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_PRESETMU_IC2IC3_STRING_NOTLOADER_VISIBLE,
						VALIDATE_PRESETMU_IC2IC3_STRING_NOTLOADER_VISIBLE,
						SET_MESSAGE_PRESETMU_IC2IC3_STRING_NOTLOADER_INVISIBLE,
						VALIDATE_PRESETMU_IC2IC3_STRING_NOTLOADER_INVISIBLE
						]
		self.teardown_path = []

class __M_BF2_27__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Preset(MU) TimeSec in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_PRESETMU_TIMESEC,
						VALIDATE_PRESETMU_TIMESEC,
						SET_MESSAGE_PRESETMU_TIMESEC_VISIBLE,
						VALIDATE_PRESETMU_TIMESEC_VISIBLE,
						SET_MESSAGE_PRESETMU_TIMESEC_INVISIBLE,
						VALIDATE_PRESETMU_TIMESEC_INVISIBLE,
						]
		self.teardown_path = []

class __M_BF2_28__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Preset(MU) TimeSec in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_PRESETMU_TIMESEC_STRING_NA_VISIBLE,
						VALIDATE_PRESETMU_TIMESEC_STRING_NA_VISIBLE,
						SET_MESSAGE_PRESETMU_TIMESEC_STRING_NA_INVISIBLE,
						VALIDATE_PRESETMU_TIMESEC_STRING_NA_INVISIBLE,
						]
		self.teardown_path = []

class __M_BF2_29__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox PPS lat (cm) in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_PPS_LAT,
						VALIDATE_PPS_LAT,
						]
		self.teardown_path = []

class __M_BF2_30__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Pitch (deg) in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_PITCH_DEG,
						VALIDATE_PITCH_DEG,
						]
		self.teardown_path = []

class __M_BF2_31__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Angle (deg) in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_ANGLE_DEG,
						VALIDATE_ANGLE_DEG,
						]
		self.teardown_path = []

class __M_BF2_32__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox PPS Long(cm) in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_PPS_LONG,
						VALIDATE_PPS_LONG,
						]
		self.teardown_path = []

class __M_BF2_33__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Roll (deg) in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_ROLL_DEG,
						VALIDATE_ROLL_DEG,
						]
		self.teardown_path = []

class __M_BF2_34__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Snout T(cm) in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_ROLL_DEG,
						VALIDATE_ROLL_DEG,
						]
		self.teardown_path = []

class __M_BF2_35__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox PPS Vert(cm) in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_PPS_VERT_CM,
						VALIDATE_PPS_VERT_CM,
						]
		self.teardown_path = []

class __M_BF2_36__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Rotn(cm) in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_ROTN_DEG,
						VALIDATE_MCR2_ROTN_DEG,
						]
		self.teardown_path = []

class __M_BF2_37__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Snout R(cm) in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_SNOUTR_DEG,
						VALIDATE_SNOUTR_DEG,
						]
		self.teardown_path = []

class __M_BF2_38__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox (RPM) in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_RPM,
						VALIDATE_RPM,
						]
		self.teardown_path = []

class __M_BF2_39__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox (Wheel) in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_WHEEL,
						VALIDATE_WHEEL,
						]
		self.teardown_path = []

class __M_BF2_40__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox (Track) in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_TRACK,
						VALIDATE_TRACK,
						]
		self.teardown_path = []

class __M_BF2_43__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Mean (mm) IC1 X in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_MEAN_MM_IC1X,
						VALIDATE_MEAN_MM_IC1X,
						]
		self.teardown_path = []

class __M_BF2_44__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox RMS (mm) IC1 X in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_RMS_MM_IC1X,
						VALIDATE_RMS_MM_IC1X,
						]
		self.teardown_path = []

class __M_BF2_45__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Skewness(mm) IC3 X in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_SKEWNESS_MM_IC3X_ORANGE1,
						VALIDATE_SKEWNESS_MM_IC3X_ORANGE1,
						VALIDATE_SKEWNESS_MM_IC3X_BACKGROUND_COLOR_ORANGE1,
						SET_MESSAGE_SKEWNESS_MM_IC3X_ORANGE2,
						VALIDATE_SKEWNESS_MM_IC3X_ORANGE2,
						VALIDATE_SKEWNESS_MM_IC3X_BACKGROUND_COLOR_ORANGE2,
						SET_MESSAGE_SKEWNESS_MM_IC3X_GRAY,
						VALIDATE_SKEWNESS_MM_IC3X_GRAY,
						VALIDATE_SKEWNESS_MM_IC3X_BACKGROUND_COLOR_GRAY,
						]
		self.teardown_path = []

class __M_BF2_46__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Mean IC3 X in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_MEAN_IC3X,
						VALIDATE_MEAN_IC3X,
						]
		self.teardown_path = []

class __M_BF2_47__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox RMS(mm) IC3 X in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_RMS_MM_IC3X,
						VALIDATE_RMS_MM_IC3X,
						]
		self.teardown_path = []

class __M_BF2_50__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox mean(mm) IC1 Y in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_MEAN_MM_IC1Y,
						VALIDATE_MEAN_MM_IC1Y,
						]
		self.teardown_path = []

class __M_BF2_51__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox RMS(mm) IC1 Y in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_RMS_MM_IC1Y,
						VALIDATE_RMS_MM_IC1Y,
						]
		self.teardown_path = []

class __M_BF2_52__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Skewness(mm) IC2 Y in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_SKEWNESS_MM_IC2Y_ORANGE1,
						VALIDATE_SKEWNESS_MM_IC2Y_ORANGE1,
						VALIDATE_SKEWNESS_MM_IC2Y_BACKGROUND_COLOR_ORANGE1,
						SET_MESSAGE_SKEWNESS_MM_IC2Y_ORANGE2,
						VALIDATE_SKEWNESS_MM_IC2Y_ORANGE2,
						VALIDATE_SKEWNESS_MM_IC2Y_BACKGROUND_COLOR_ORANGE2,
						SET_MESSAGE_SKEWNESS_MM_IC2Y_GRAY,
						VALIDATE_SKEWNESS_MM_IC2Y_GRAY,
						VALIDATE_SKEWNESS_MM_IC2Y_BACKGROUND_COLOR_GRAY,
						]
		self.teardown_path = []

class __M_BF2_53__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Mean IC2 Y in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_MEAN_IC2Y,
						VALIDATE_MEAN_IC2Y,
						]
		self.teardown_path = []

class __M_BF2_54__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox RMS(mm) IC2 Y in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_ACTUALR_G_CM2,
						VALIDATE_ACTUALR_G_CM2,
						]
		self.teardown_path = []


class __M_BF2_56__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Actual R(g/cm2) in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_RMS_MM_IC2Y,
						VALIDATE_RMS_MM_IC2Y,
						]
		self.teardown_path = []

class __M_BF2_57__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Actual R(%) in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_ACTUAL_R_PERCENT,
						VALIDATE_ACTUAL_R_PERCENT,
						SET_MESSAGE_ACTUAL_R_PERCENT_VISIBLE,
						VALIDATE_ACTUAL_R_PERCENT_VISIBLE,
						SET_MESSAGE_ACTUAL_R_PERCENT_INVISIBLE,
						VALIDATE_ACTUAL_R_PERCENT_INVISIBLE,
						]
		self.teardown_path = []

class __M_BF2_58__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Actual R(%) string NA in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_ACTUAL_R_PERCENT_STRING_NA_VISIBLE,
						VALIDATE_ACTUAL_R_PERCENT_STRING_NA_VISIBLE,
						SET_MESSAGE_ACTUAL_R_PERCENT_STRING_NA_INVISIBLE,
						VALIDATE_ACTUAL_R_PERCENT_STRING_NA_INVISIBLE
						]
		self.teardown_path = []

class __M_BF2_59__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Actual B1B2 (Tesla) in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_ACTUAL_B1B2_TESLA,
						VALIDATE_ACTUAL_B1B2_TESLA,
						]
		self.teardown_path = []

class __M_BF2_60__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Expected R(g/cm2) First layer in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_EXPECTED_R_G_CM2_FIRST_LAYER,
						VALIDATE_EXPECTED_R_G_CM2_FIRST_LAYER,
						SET_MESSAGE_EXPECTED_R_G_CM2_FIRST_LAYER_VISIBLE,
						VALIDATE_EXPECTED_R_G_CM2_FIRST_LAYER_VISIBLE,
						SET_MESSAGE_EXPECTED_R_G_CM2_FIRST_LAYER_INVISIBLE,
						VALIDATE_EXPECTED_R_G_CM2_FIRST_LAYER_INVISIBLE
						]
		self.teardown_path = []

class __M_BF2_61__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Expected R(g/cm2) Second layer in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_EXPECTED_R_G_CM2_SECOND_LAYER,
						VALIDATE_EXPECTED_R_G_CM2_SECOND_LAYER,
						SET_MESSAGE_EXPECTED_R_G_CM2_SECOND_LAYER_VISIBLE,
						VALIDATE_EXPECTED_R_G_CM2_SECOND_LAYER_VISIBLE,
						SET_MESSAGE_EXPECTED_R_G_CM2_SECOND_LAYER_INVISIBLE,
						VALIDATE_EXPECTED_R_G_CM2_SECOND_LAYER_INVISIBLE
						]
		self.teardown_path = []

class __M_BF2_62__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Expected R(%) String 0.00 in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_EXPECTED_R_PERCENT_STRING_00_VISIBLE,
						VALIDATE_EXPECTED_R_PERCENT_STRING_00_VISIBLE,
						SET_MESSAGE_EXPECTED_R_PERCENT_STRING_00_INVISIBLE,
						VALIDATE_EXPECTED_R_PERCENT_STRING_00_INVISIBLE,

						]
		self.teardown_path = []

class __M_BF2_63__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Expected R(%) String NA in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_EXPECTED_R_PERCENT_STRING_NA_VISIBLE,
						VALIDATE_EXPECTED_R_PERCENT_STRING_NA_VISIBLE,
						SET_MESSAGE_EXPECTED_R_PERCENT_STRING_NA_INVISIBLE,
						VALIDATE_EXPECTED_R_PERCENT_STRING_NA_INVISIBLE,
						]
		self.teardown_path = []

class __M_BF2_64__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Expected B1B2 (Tesla) in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_EXPECTED_B1B2_TESLA,
						VALIDATE_EXPECTED_B1B2_TESLA,
						SET_MESSAGE_EXPECTED_B1B2_TESLA_VISIBLE,
						VALIDATE_EXPECTED_B1B2_TESLA_VISIBLE,
						SET_MESSAGE_EXPECTED_B1B2_TESLA_INVISIBLE,
						VALIDATE_EXPECTED_B1B2_TESLA_INVISIBLE,
						]
		self.teardown_path = []

class __M_BF2_65__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Expected B1B2 (Tesla) String NA in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_EXPECTED_B1B2_TESLA_STRING_NA_VISIBLE,
						VALIDATE_EXPECTED_B1B2_TESLA_STRING_NA_VISIBLE,
						SET_MESSAGE_EXPECTED_B1B2_TESLA_STRING_NA_INVISIBLE,
						VALIDATE_EXPECTED_B1B2_TESLA_STRING_NA_INVISIBLE,
						]
		self.teardown_path = []

class __M_BF2_66__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate Rectangle Layer dosimetry in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_RECTANGLE_HIDE_LAYER_DOSIMETRY_VISIBLE,
						VALIDATE_RECTANGLE_HIDE_LAYER_DOSIMETRY_VISIBLE,
						SET_MESSAGE_RECTANGLE_HIDE_LAYER_DOSIMETRY_INVISIBLE_1,
						VALIDATE_RECTANGLE_HIDE_LAYER_DOSIMETRY_INVISIBLE_1,
						SET_MESSAGE_RECTANGLE_HIDE_LAYER_DOSIMETRY_INVISIBLE_2,
						VALIDATE_RECTANGLE_HIDE_LAYER_DOSIMETRY_INVISIBLE_2,
						]
		self.teardown_path = []

class __M_BF2_67__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate Text Layer dosimetry in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_TEXT_LAYER_DOSIMETRY_VISIBLE_1,
						VALIDATE_TEXT_LAYER_DOSIMETRY_VISIBLE,
						SET_MESSAGE_TEXT_LAYER_DOSIMETRY_VISIBLE_2,
						VALIDATE_TEXT_LAYER_DOSIMETRY_VISIBLE,
						SET_MESSAGE_TEXT_LAYER_DOSIMETRY_INVISIBLE,
						VALIDATE_TEXT_LAYER_DOSIMETRY_INVISIBLE,
						]
		self.teardown_path = []

class __M_BF2_68__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Actual(MU) IC2 - Layer dosimetry First layer in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_ACTUALMU_IC2_LAYER_DOSIMETRY_FIRST_LAYER,
						VALIDATE_ACTUALMU_IC2_LAYER_DOSIMETRY_FIRST_LAYER,
						SET_MESSAGE_ACTUALMU_IC2_LAYER_DOSIMETRY_FIRST_LAYER_VISIBLE,
						VALIDATE_ACTUALMU_IC2_LAYER_DOSIMETRY_FIRST_LAYER_VISIBLE,
						SET_MESSAGE_ACTUALMU_IC2_LAYER_DOSIMETRY_FIRST_LAYER_INVISIBLE,
						VALIDATE_ACTUALMU_IC2_LAYER_DOSIMETRY_FIRST_LAYER_INVISIBLE,
						]
		self.teardown_path = []

class __M_BF2_69__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Actual(MU) IC2 - Layer dosimetry Second layer in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_ACTUALMU_IC2_LAYER_DOSIMETRY_SECOND_LAYER,
						VALIDATE_ACTUALMU_IC2_LAYER_DOSIMETRY_SECOND_LAYER,
						SET_MESSAGE_ACTUALMU_IC2_LAYER_DOSIMETRY_SECOND_LAYER_VISIBLE,
						VALIDATE_ACTUALMU_IC2_LAYER_DOSIMETRY_SECOND_LAYER_VISIBLE,
						SET_MESSAGE_ACTUALMU_IC2_LAYER_DOSIMETRY_SECOND_LAYER_INVISIBLE_1,
						VALIDATE_ACTUALMU_IC2_LAYER_DOSIMETRY_SECOND_LAYER_INVISIBLE_1,
						SET_MESSAGE_ACTUALMU_IC2_LAYER_DOSIMETRY_SECOND_LAYER_INVISIBLE_2,
						VALIDATE_ACTUALMU_IC2_LAYER_DOSIMETRY_SECOND_LAYER_INVISIBLE_2,
						]
		self.teardown_path = []

class __M_BF2_70__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Actual(MU) IC3 - Layer dosimetry First layer in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_ACTUALMU_IC3_FIRST_LAYER_DOSIMETRY,
						VALIDATE_ACTUALMU_IC3_FIRST_LAYER_DOSIMETRY,
						SET_MESSAGE_ACTUALMU_IC3_FIRST_LAYER_DOSIMETRY_VISIBLE,
						VALIDATE_ACTUALMU_IC3_FIRST_LAYER_DOSIMETRY_VISIBLE,
						SET_MESSAGE_ACTUALMU_IC3_FIRST_LAYER_DOSIMETRY_INVISIBLE,
						VALIDATE_ACTUALMU_IC3_FIRST_LAYER_DOSIMETRY_INVISIBLE,
						]
		self.teardown_path = []

class __M_BF2_71__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Actual(MU) IC3 - Layer dosimetry Second layer in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_ACTUALMU_IC3_SECOND_LAYER_DOSIMETRY,
						VALIDATE_ACTUALMU_IC3_SECOND_LAYER_DOSIMETRY,
						SET_MESSAGE_ACTUALMU_IC3_SECOND_LAYER_DOSIMETRY_VISIBLE,
						VALIDATE_ACTUALMU_IC3_SECOND_LAYER_DOSIMETRY_VISIBLE,
						SET_MESSAGE_ACTUALMU_IC3_SECOND_LAYER_DOSIMETRY_INVISIBLE_1,
						VALIDATE_ACTUALMU_IC3_SECOND_LAYER_DOSIMETRY_INVISIBLE_1,
						SET_MESSAGE_ACTUALMU_IC3_SECOND_LAYER_DOSIMETRY_INVISIBLE_2,
						VALIDATE_ACTUALMU_IC3_SECOND_LAYER_DOSIMETRY_INVISIBLE_2,
						]
		self.teardown_path = []

class __M_BF2_72__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Preset(MU) IC2 - Layer dosimetry String Not Loaded in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_PRESETMU_IC2_LAYERDOSIMETRY_STRING_NOTLOADED_VISIBLE,
						VALIDATE_PRESETMU_IC2_LAYERDOSIMETRY_STRING_NOTLOADED_VISIBLE,
						SET_MESSAGE_PRESETMU_IC2_LAYERDOSIMETRY_STRING_NOTLOADED_INVISIBLE,
						VALIDATE_PRESETMU_IC2_LAYERDOSIMETRY_STRING_NOTLOADED_INVISIBLE,
						]
		self.teardown_path = []

class __M_BF2_73__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Preset(MU) IC2 - Layer dosimetry First layer in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_PRESETMU_IC2_FIRST_LAYER_DOSIMETRY,
						VALIDATE_PRESETMU_IC2_FIRST_LAYER_DOSIMETRY,
						SET_MESSAGE_PRESETMU_IC2_FIRST_LAYER_DOSIMETRY_VISIBLE,
						VALIDATE_PRESETMU_IC2_FIRST_LAYER_DOSIMETRY_VISIBLE,
						SET_MESSAGE_PRESETMU_IC2_FIRST_LAYER_DOSIMETRY_INVISIBLE,
						VALIDATE_PRESETMU_IC2_FIRST_LAYER_DOSIMETRY_INVISIBLE,
						]
		self.teardown_path = []

class __M_BF2_74__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Preset(MU) IC2 - Layer dosimetry Second layer in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_PRESETMU_IC2_SECOND_LAYER_DOSIMETRY,
						VALIDATE_PRESETMU_IC2_SECOND_LAYER_DOSIMETRY,
						SET_MESSAGE_PRESETMU_IC2_SECOND_LAYER_DOSIMETRY_VISIBLE,
						VALIDATE_PRESETMU_IC2_SECOND_LAYER_DOSIMETRY_VISIBLE,
						SET_MESSAGE_PRESETMU_IC2_SECOND_LAYER_DOSIMETRY_INVISIBLE_1,
						VALIDATE_PRESETMU_IC2_SECOND_LAYER_DOSIMETRY_INVISIBLE_1,
						SET_MESSAGE_PRESETMU_IC2_SECOND_LAYER_DOSIMETRY_INVISIBLE_2,
						VALIDATE_PRESETMU_IC2_SECOND_LAYER_DOSIMETRY_INVISIBLE_2,
						]
		self.teardown_path = []

class __M_BF2_75__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Preset(MU) IC3 - Layer dosimetry String Not Loader in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_PRESETMU_IC3_LAYERDOSIMETRY_STRING_NOTLOADER_VISIBLE,
						VALIDATE_PRESETMU_IC3_LAYERDOSIMETRY_STRING_NOTLOADER_VISIBLE,
						SET_MESSAGE_PRESETMU_IC3_LAYERDOSIMETRY_STRING_NOTLOADER_INVISIBLE,
						VALIDATE_PRESETMU_IC3_LAYERDOSIMETRY_STRING_NOTLOADER_INVISIBLE,
						]
		self.teardown_path = []

class __M_BF2_76__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Preset(MU) IC3 - Layer dosimetry First layer in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_PRESETMU_IC3_FIRST_LAYER_DOSIMETRY,
						VALIDATE_PRESETMU_IC3_FIRST_LAYER_DOSIMETRY,
						SET_MESSAGE_PRESETMU_IC3_FIRST_LAYER_DOSIMETRY_VISIBLE,
						VALIDATE_PRESETMU_IC3_FIRST_LAYER_DOSIMETRY_VISIBLE,
						SET_MESSAGE_PRESETMU_IC3_FIRST_LAYER_DOSIMETRY_INVISIBLE,
						VALIDATE_PRESETMU_IC3_FIRST_LAYER_DOSIMETRY_INVISIBLE,
						]
		self.teardown_path = []

class __M_BF2_77__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Preset(MU) IC3 - Layer dosimetry Second layer in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_PRESETMU_IC3_SECOND_LAYER_DOSIMETRY,
						VALIDATE_PRESETMU_IC3_SECOND_LAYER_DOSIMETRY,
						SET_MESSAGE_PRESETMU_IC3_SECOND_LAYER_DOSIMETRY_VISIBLE,
						VALIDATE_PRESETMU_IC3_SECOND_LAYER_DOSIMETRY_VISIBLE,
						SET_MESSAGE_PRESETMU_IC3_SECOND_LAYER_DOSIMETRY_INVISIBLE_1,
						VALIDATE_PRESETMU_IC3_SECOND_LAYER_DOSIMETRY_INVISIBLE_1,
						SET_MESSAGE_PRESETMU_IC3_SECOND_LAYER_DOSIMETRY_INVISIBLE_2,
						VALIDATE_PRESETMU_IC3_SECOND_LAYER_DOSIMETRY_INVISIBLE_2,
						]
		self.teardown_path = []

class __M_BF2_78__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Total layer - Layer dosimetry in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_TOTALLAYER_LAYERDOSIMETRY,
						VALIDATE_TOTALLAYER_LAYERDOSIMETRY,
						]
		self.teardown_path = []

class __M_BF2_79__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate TextBox Current layer - Layer dosimetry in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_CURRENTLAYER_LAYERDOSIMETRY,
						VALIDATE_CURRENTLAYER_LAYERDOSIMETRY,
						]
		self.teardown_path = []

class __M_BF2_41__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate Graph IC1 X in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_MCR2_TR2_ICEU1_QC1_IC1X,
						VALIDATE_MCR2_TR2_ICEU1_QC1_IC1X,
						VALIDATE_MCR2_TR2_ICEU1_QC1_IC1X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU1_QC1_IC1X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU1_QC1_IC1X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU1_QC2_IC1X,
						VALIDATE_MCR2_TR2_ICEU1_QC2_IC1X,
						VALIDATE_MCR2_TR2_ICEU1_QC2_IC1X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU1_QC2_IC1X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU1_QC2_IC1X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU1_QC3_IC1X,
						VALIDATE_MCR2_TR2_ICEU1_QC3_IC1X,
						VALIDATE_MCR2_TR2_ICEU1_QC3_IC1X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU1_QC3_IC1X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU1_QC3_IC1X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU1_QC4_IC1X,
						VALIDATE_MCR2_TR2_ICEU1_QC4_IC1X,
						VALIDATE_MCR2_TR2_ICEU1_QC4_IC1X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU1_QC4_IC1X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU1_QC4_IC1X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU1_QC5_IC1X,
						VALIDATE_MCR2_TR2_ICEU1_QC5_IC1X,
						VALIDATE_MCR2_TR2_ICEU1_QC5_IC1X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU1_QC5_IC1X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU1_QC5_IC1X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU1_QC6_IC1X,
						VALIDATE_MCR2_TR2_ICEU1_QC6_IC1X,
						VALIDATE_MCR2_TR2_ICEU1_QC6_IC1X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU1_QC6_IC1X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU1_QC6_IC1X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU1_QC7_IC1X,
						VALIDATE_MCR2_TR2_ICEU1_QC7_IC1X,
						VALIDATE_MCR2_TR2_ICEU1_QC7_IC1X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU1_QC7_IC1X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU1_QC7_IC1X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU1_QC8_IC1X,
						VALIDATE_MCR2_TR2_ICEU1_QC8_IC1X,
						VALIDATE_MCR2_TR2_ICEU1_QC8_IC1X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU1_QC8_IC1X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU1_QC8_IC1X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU1_QC9_IC1X,
						VALIDATE_MCR2_TR2_ICEU1_QC9_IC1X,
						VALIDATE_MCR2_TR2_ICEU1_QC9_IC1X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU1_QC9_IC1X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU1_QC9_IC1X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU1_QC10_IC1X,
						VALIDATE_MCR2_TR2_ICEU1_QC10_IC1X,
						VALIDATE_MCR2_TR2_ICEU1_QC10_IC1X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU1_QC10_IC1X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU1_QC10_IC1X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU1_QC11_IC1X,
						VALIDATE_MCR2_TR2_ICEU1_QC11_IC1X,
						VALIDATE_MCR2_TR2_ICEU1_QC11_IC1X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU1_QC11_IC1X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU1_QC11_IC1X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU1_QC12_IC1X,
						VALIDATE_MCR2_TR2_ICEU1_QC12_IC1X,
						VALIDATE_MCR2_TR2_ICEU1_QC12_IC1X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU1_QC12_IC1X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU1_QC12_IC1X_FILL_DIRECTION,
						]
		self.teardown_path = []

class __M_BF2_42__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate Graph IC3 X in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_MCR2_TR2_ICEU3_QC1_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC1_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC1_IC3X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU3_QC1_IC3X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU3_QC1_IC3X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU3_QC2_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC2_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC2_IC3X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU3_QC2_IC3X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU3_QC2_IC3X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU3_QC3_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC3_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC3_IC3X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU3_QC3_IC3X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU3_QC3_IC3X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU3_QC4_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC4_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC4_IC3X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU3_QC4_IC3X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU3_QC4_IC3X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU3_QC5_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC5_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC5_IC3X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU3_QC5_IC3X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU3_QC5_IC3X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU3_QC6_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC6_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC6_IC3X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU3_QC6_IC3X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU3_QC6_IC3X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU3_QC7_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC7_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC7_IC3X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU3_QC7_IC3X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU3_QC7_IC3X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU3_QC8_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC8_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC8_IC3X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU3_QC8_IC3X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU3_QC8_IC3X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU3_QC9_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC9_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC9_IC3X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU3_QC9_IC3X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU3_QC9_IC3X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU3_QC10_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC10_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC10_IC3X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU3_QC10_IC3X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU3_QC10_IC3X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU3_QC11_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC11_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC11_IC3X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU3_QC11_IC3X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU3_QC11_IC3X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU3_QC12_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC12_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC12_IC3X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU3_QC12_IC3X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU3_QC12_IC3X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU3_QC13_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC13_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC13_IC3X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU3_QC13_IC3X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU3_QC13_IC3X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU3_QC14_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC14_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC14_IC3X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU3_QC14_IC3X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU3_QC14_IC3X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU3_QC15_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC15_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC15_IC3X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU3_QC15_IC3X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU3_QC15_IC3X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU3_QC16_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC16_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC16_IC3X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU3_QC16_IC3X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU3_QC16_IC3X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU3_QC17_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC17_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC17_IC3X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU3_QC17_IC3X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU3_QC17_IC3X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU3_QC18_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC18_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC18_IC3X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU3_QC18_IC3X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU3_QC18_IC3X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU3_QC19_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC19_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC19_IC3X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU3_QC19_IC3X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU3_QC19_IC3X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU3_QC20_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC20_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC20_IC3X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU3_QC20_IC3X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU3_QC20_IC3X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU3_QC21_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC21_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC21_IC3X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU3_QC21_IC3X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU3_QC21_IC3X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU3_QC22_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC22_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC22_IC3X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU3_QC22_IC3X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU3_QC22_IC3X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU3_QC23_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC23_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC23_IC3X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU3_QC23_IC3X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU3_QC23_IC3X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU3_QC24_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC24_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC24_IC3X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU3_QC24_IC3X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU3_QC24_IC3X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU3_QC25_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC25_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC25_IC3X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU3_QC25_IC3X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU3_QC25_IC3X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU3_QC26_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC26_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC26_IC3X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU3_QC26_IC3X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU3_QC26_IC3X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU3_QC27_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC27_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC27_IC3X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU3_QC27_IC3X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU3_QC27_IC3X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU3_QC28_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC28_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC28_IC3X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU3_QC28_IC3X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU3_QC28_IC3X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU3_QC29_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC29_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC29_IC3X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU3_QC29_IC3X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU3_QC29_IC3X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU3_QC30_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC30_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC30_IC3X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU3_QC30_IC3X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU3_QC30_IC3X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU3_QC31_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC31_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC31_IC3X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU3_QC31_IC3X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU3_QC31_IC3X_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU3_QC32_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC32_IC3X,
						VALIDATE_MCR2_TR2_ICEU3_QC32_IC3X_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU3_QC32_IC3X_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU3_QC32_IC3X_FILL_DIRECTION,
						]
		self.teardown_path = []

class __M_BF2_48__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate Graph IC1 Y in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_MCR2_TR2_ICEU1_QC13_IC1Y,
						VALIDATE_MCR2_TR2_ICEU1_QC13_IC1Y,
						VALIDATE_MCR2_TR2_ICEU1_QC13_IC1Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU1_QC13_IC1Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU1_QC13_IC1Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU1_QC14_IC1Y,
						VALIDATE_MCR2_TR2_ICEU1_QC14_IC1Y,
						VALIDATE_MCR2_TR2_ICEU1_QC14_IC1Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU1_QC14_IC1Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU1_QC14_IC1Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU1_QC15_IC1Y,
						VALIDATE_MCR2_TR2_ICEU1_QC15_IC1Y,
						VALIDATE_MCR2_TR2_ICEU1_QC15_IC1Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU1_QC15_IC1Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU1_QC15_IC1Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU1_QC16_IC1Y,
						VALIDATE_MCR2_TR2_ICEU1_QC16_IC1Y,
						VALIDATE_MCR2_TR2_ICEU1_QC16_IC1Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU1_QC16_IC1Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU1_QC16_IC1Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU1_QC17_IC1Y,
						VALIDATE_MCR2_TR2_ICEU1_QC17_IC1Y,
						VALIDATE_MCR2_TR2_ICEU1_QC17_IC1Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU1_QC17_IC1Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU1_QC17_IC1Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU1_QC18_IC1Y,
						VALIDATE_MCR2_TR2_ICEU1_QC18_IC1Y,
						VALIDATE_MCR2_TR2_ICEU1_QC18_IC1Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU1_QC18_IC1Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU1_QC18_IC1Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU1_QC19_IC1Y,
						VALIDATE_MCR2_TR2_ICEU1_QC19_IC1Y,
						VALIDATE_MCR2_TR2_ICEU1_QC19_IC1Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU1_QC19_IC1Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU1_QC19_IC1Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU1_QC20_IC1Y,
						VALIDATE_MCR2_TR2_ICEU1_QC20_IC1Y,
						VALIDATE_MCR2_TR2_ICEU1_QC20_IC1Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU1_QC20_IC1Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU1_QC20_IC1Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU1_QC21_IC1Y,
						VALIDATE_MCR2_TR2_ICEU1_QC21_IC1Y,
						VALIDATE_MCR2_TR2_ICEU1_QC21_IC1Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU1_QC21_IC1Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU1_QC21_IC1Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU1_QC22_IC1Y,
						VALIDATE_MCR2_TR2_ICEU1_QC22_IC1Y,
						VALIDATE_MCR2_TR2_ICEU1_QC22_IC1Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU1_QC22_IC1Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU1_QC22_IC1Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU1_QC23_IC1Y,
						VALIDATE_MCR2_TR2_ICEU1_QC23_IC1Y,
						VALIDATE_MCR2_TR2_ICEU1_QC23_IC1Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU1_QC23_IC1Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU1_QC23_IC1Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU1_QC24_IC1Y,
						VALIDATE_MCR2_TR2_ICEU1_QC24_IC1Y,
						VALIDATE_MCR2_TR2_ICEU1_QC24_IC1Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU1_QC24_IC1Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU1_QC24_IC1Y_FILL_DIRECTION,
						]
		self.teardown_path = []

class __M_BF2_49__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate Graph IC2 Y in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_MCR2_TR2_ICEU2_QC1_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC1_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC1_IC3Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU2_QC1_IC3Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU2_QC1_IC3Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU2_QC2_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC2_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC2_IC3Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU2_QC2_IC3Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU2_QC2_IC3Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU2_QC3_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC3_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC3_IC3Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU2_QC3_IC3Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU2_QC3_IC3Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU2_QC4_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC4_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC4_IC3Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU2_QC4_IC3Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU2_QC4_IC3Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU2_QC5_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC5_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC5_IC3Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU2_QC5_IC3Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU2_QC5_IC3Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU2_QC6_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC6_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC6_IC3Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU2_QC6_IC3Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU2_QC6_IC3Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU2_QC7_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC7_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC7_IC3Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU2_QC7_IC3Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU2_QC7_IC3Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU2_QC8_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC8_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC8_IC3Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU2_QC8_IC3Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU2_QC8_IC3Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU2_QC9_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC9_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC9_IC3Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU2_QC9_IC3Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU2_QC9_IC3Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU2_QC10_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC10_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC10_IC3Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU2_QC10_IC3Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU2_QC10_IC3Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU2_QC11_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC11_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC11_IC3Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU2_QC11_IC3Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU2_QC11_IC3Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU2_QC12_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC12_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC12_IC3Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU2_QC12_IC3Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU2_QC12_IC3Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU2_QC13_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC13_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC13_IC3Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU2_QC13_IC3Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU2_QC13_IC3Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU2_QC14_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC14_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC14_IC3Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU2_QC14_IC3Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU2_QC14_IC3Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU2_QC15_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC15_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC15_IC3Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU2_QC15_IC3Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU2_QC15_IC3Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU2_QC16_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC16_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC16_IC3Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU2_QC16_IC3Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU2_QC16_IC3Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU2_QC17_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC17_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC17_IC3Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU2_QC17_IC3Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU2_QC17_IC3Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU2_QC18_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC18_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC18_IC3Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU2_QC18_IC3Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU2_QC18_IC3Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU2_QC19_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC19_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC19_IC3Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU2_QC19_IC3Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU2_QC19_IC3Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU2_QC20_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC20_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC20_IC3Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU2_QC20_IC3Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU2_QC20_IC3Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU2_QC21_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC21_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC21_IC3Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU2_QC21_IC3Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU2_QC21_IC3Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU2_QC22_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC22_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC22_IC3Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU2_QC22_IC3Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU2_QC22_IC3Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU2_QC23_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC23_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC23_IC3Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU2_QC23_IC3Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU2_QC23_IC3Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU2_QC24_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC24_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC24_IC3Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU2_QC24_IC3Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU2_QC24_IC3Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU2_QC25_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC25_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC25_IC3Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU2_QC25_IC3Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU2_QC25_IC3Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU2_QC26_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC26_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC26_IC3Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU2_QC26_IC3Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU2_QC26_IC3Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU2_QC27_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC27_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC27_IC3Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU2_QC27_IC3Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU2_QC27_IC3Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU2_QC28_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC28_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC28_IC3Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU2_QC28_IC3Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU2_QC28_IC3Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU2_QC29_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC29_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC29_IC3Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU2_QC29_IC3Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU2_QC29_IC3Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU2_QC30_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC30_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC30_IC3Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU2_QC30_IC3Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU2_QC30_IC3Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU2_QC31_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC31_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC31_IC3Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU2_QC31_IC3Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU2_QC31_IC3Y_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_ICEU2_QC32_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC32_IC3Y,
						VALIDATE_MCR2_TR2_ICEU2_QC32_IC3Y_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_ICEU2_QC32_IC3Y_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_ICEU2_QC32_IC3Y_FILL_DIRECTION,

						]
		self.teardown_path = []

class __M_BF2_55__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Simulate and validate Graph Range Verify in Beam Profile 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_MCR2_TR2_RVEU_QC1_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC1_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC1_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC1_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC1_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC2_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC2_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC2_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC2_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC2_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC3_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC3_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC3_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC3_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC3_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC4_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC4_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC4_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC4_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC4_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC5_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC5_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC5_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC5_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC5_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC6_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC6_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC6_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC6_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC6_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC7_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC7_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC7_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC7_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC7_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC8_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC8_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC8_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC8_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC8_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC9_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC9_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC9_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC9_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC9_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC10_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC10_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC10_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC10_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC10_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC11_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC11_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC11_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC11_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC11_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC12_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC12_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC12_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC12_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC12_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC13_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC13_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC13_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC13_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC13_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC14_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC14_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC14_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC14_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC14_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC15_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC15_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC15_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC15_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC15_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC16_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC16_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC16_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC16_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC16_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC17_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC17_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC17_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC17_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC17_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC18_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC18_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC18_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC18_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC18_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC19_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC19_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC19_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC19_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC19_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC20_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC20_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC20_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC20_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC20_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC21_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC21_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC21_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC21_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC21_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC22_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC22_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC22_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC22_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC22_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC23_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC23_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC23_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC23_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC23_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC24_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC24_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC24_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC24_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC24_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC25_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC25_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC25_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC25_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC25_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC26_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC26_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC26_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC26_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC26_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC27_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC27_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC27_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC27_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC27_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC28_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC28_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC28_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC28_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC28_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC29_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC29_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC29_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC29_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC29_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC30_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC30_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC30_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC30_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC30_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC31_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC31_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC31_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC31_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC31_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC32_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC32_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC32_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC32_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC32_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC33_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC33_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC33_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC33_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC33_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC34_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC34_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC34_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC34_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC34_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC35_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC35_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC35_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC35_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC35_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC36_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC36_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC36_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC36_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC36_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC37_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC37_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC37_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC37_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC37_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC38_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC38_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC38_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC38_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC38_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC39_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC39_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC39_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC39_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC39_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC40_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC40_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC40_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC40_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC40_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC41_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC41_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC41_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC41_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC41_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC42_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC42_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC42_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC42_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC42_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC43_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC43_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC43_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC43_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC43_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC44_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC44_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC44_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC44_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC44_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC45_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC45_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC45_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC45_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC45_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC46_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC46_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC46_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC46_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC46_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC47_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC47_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC47_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC47_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC47_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC48_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC48_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC48_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC48_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC48_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC49_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC49_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC49_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC49_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC49_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC50_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC50_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC50_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC50_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC50_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC51_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC51_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC51_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC51_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC51_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC52_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC52_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC52_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC52_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC52_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC53_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC53_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC53_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC53_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC53_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC54_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC54_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC54_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC54_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC54_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC55_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC55_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC55_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC55_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC55_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC56_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC56_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC56_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC56_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC56_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC57_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC57_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC57_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC57_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC57_RANGEVERIFY_FILL_DIRECTION,
						SET_MESSAGE_MCR2_TR2_RVEU_QC58_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC58_RANGEVERIFY,
						VALIDATE_MCR2_TR2_RVEU_QC58_RANGEVERIFY_FOREGROUND_COLOR,
						VALIDATE_MCR2_TR2_RVEU_QC58_RANGEVERIFY_FILL_AMOUNT,
						VALIDATE_MCR2_TR2_RVEU_QC58_RANGEVERIFY_FILL_DIRECTION,

						]
		self.teardown_path = []