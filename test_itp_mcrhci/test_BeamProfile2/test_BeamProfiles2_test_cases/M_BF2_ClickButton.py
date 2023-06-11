from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_thriver_wait import SETUP_THRIVER_WAIT
from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import SETUP_CLICK_BUTTON_BY_POSITION, SETUP_CLICK_BUTTON_BY_NAME, SETUP_VIEW_DISPLAY_STATUS_CHECK

class THRIVER_WAIT_5_SECONDS(SETUP_THRIVER_WAIT):
	time = 5

class NAVIGATE_TO_BEAM_PROFILES_2(SETUP_CLICK_BUTTON_BY_POSITION):
    name = "Navigate to Beam Profiles 2"
    button_pos_x = 130
    button_pos_y = 760
    
class OPEN_TR2_RMEU_TIMING_SCREEN(SETUP_CLICK_BUTTON_BY_NAME):
	button_name = "mcr_treatment_beam_profiles2:rmeu_display_btn_1"

class VALIDATE_OPEN_TR2_RMEU_TIMING_SCREEN(SETUP_VIEW_DISPLAY_STATUS_CHECK):
	view_name = "tr2_rmeu_timing"
	expected_result = "1"

class __M_BF2_2__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Click RMEU Timings button in Beam Profiles 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						THRIVER_WAIT_5_SECONDS,
						OPEN_TR2_RMEU_TIMING_SCREEN,
						THRIVER_WAIT_5_SECONDS,
						VALIDATE_OPEN_TR2_RMEU_TIMING_SCREEN,
						THRIVER_WAIT_5_SECONDS,
						NAVIGATE_TO_BEAM_PROFILES_2,
						]
		self.teardown_path = []


class OPEN_TUNE_ISEU_SCREEN(SETUP_CLICK_BUTTON_BY_NAME):
	button_name = "mcr_treatment_beam_profiles2:rmeu_display_btn_2"

class VALIDATE_OPEN_TUNE_ISEU_SCREEN(SETUP_VIEW_DISPLAY_STATUS_CHECK):
	view_name = "tune_iseu"
	expected_result = "1"

class __M_BF2_3__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Click Manual Tune button in Beam Profiles 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						THRIVER_WAIT_5_SECONDS,
						OPEN_TUNE_ISEU_SCREEN,
						THRIVER_WAIT_5_SECONDS,
						VALIDATE_OPEN_TUNE_ISEU_SCREEN,
						THRIVER_WAIT_5_SECONDS,
						NAVIGATE_TO_BEAM_PROFILES_2,
						]
		self.teardown_path = []

class OPEN_TR2_IC2_10BINS_SCREEN(SETUP_CLICK_BUTTON_BY_NAME):
	button_name = "mcr_treatment_beam_profiles2:display_10bin_btn"

class VALIDATE_OPEN_TR2_IC2_10BINS_SCREEN(SETUP_VIEW_DISPLAY_STATUS_CHECK):
	view_name = "tr2_ic2_10bins"
	expected_result = "1"

class __M_BF2_4__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "Click 10Bin Histogrm button in Beam Profiles 2"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						THRIVER_WAIT_5_SECONDS,
						OPEN_TR2_IC2_10BINS_SCREEN,
						THRIVER_WAIT_5_SECONDS,
						VALIDATE_OPEN_TR2_IC2_10BINS_SCREEN,
						THRIVER_WAIT_5_SECONDS,
						NAVIGATE_TO_BEAM_PROFILES_2,
						]
		self.teardown_path = []