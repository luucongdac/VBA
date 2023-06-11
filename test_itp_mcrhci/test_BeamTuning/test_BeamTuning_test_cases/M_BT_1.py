from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_thriver_wait import SETUP_THRIVER_WAIT
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_msg_dialog_screen import SETUP_CLICK_OK_BUTTON_MSG_DIALOG 
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_login_screen import SETUP_INPUT_USERNAME
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_login_screen import SETUP_INPUT_PASSWORD
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_login_screen import SETUP_CLICK_OK_LOGIN_BUTTON
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_select_session_screen import SETUP_SELECT_SERVICE_SESSION
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_pts_layout_screen import SETUP_CLICK_ESS_IMAGE
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_beam_tuning import SETUP_VALIDATE_OPEN_BEAM_TUNING
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_service_ess_menu import SETUP_OPEN_BEAM_TUNING_SCREEN


class THRIVER_WAIT_10_SECONDS(SETUP_THRIVER_WAIT):
	time = 10
class THRIVER_WAIT_3_SECONDS(SETUP_THRIVER_WAIT):
	time = 3
class CLICK_OK_BUTTON_MSG_DIALOG(SETUP_CLICK_OK_BUTTON_MSG_DIALOG): pass
class INPUT_USERNAME(SETUP_INPUT_USERNAME): pass
class INPUT_PASSWORD(SETUP_INPUT_PASSWORD): pass
class CLICK_OK_LOGIN_BUTTON(SETUP_CLICK_OK_LOGIN_BUTTON): pass
class SELECT_SERVICE_SESSION(SETUP_SELECT_SERVICE_SESSION): pass
class OPEN_ESS_LAYOUT(SETUP_CLICK_ESS_IMAGE): pass
class OPEN_BEAM_TUNING_SCREEN(SETUP_OPEN_BEAM_TUNING_SCREEN): pass
class VALIDATE_OPEN_BEAM_TUNING(SETUP_VALIDATE_OPEN_BEAM_TUNING): pass


class __M_BT_1__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = 'Start MCR GUI and navigate to Beam Tuning screen'

		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						THRIVER_WAIT_10_SECONDS,
						CLICK_OK_BUTTON_MSG_DIALOG,
						INPUT_USERNAME,
						INPUT_PASSWORD,
						CLICK_OK_LOGIN_BUTTON,
						SELECT_SERVICE_SESSION,
						THRIVER_WAIT_10_SECONDS,
						OPEN_ESS_LAYOUT,
						THRIVER_WAIT_3_SECONDS,
						OPEN_BEAM_TUNING_SCREEN,
						THRIVER_WAIT_3_SECONDS,
						VALIDATE_OPEN_BEAM_TUNING,
						]
		self.teardown_path = []