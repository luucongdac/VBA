from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import *
from procedures.thriver.test_itp_mcrhci.SETUP.setup_thriver_wait import *

class THRIVER_WAIT_1_SECOND(SETUP_THRIVER_WAIT):
    time = 1

class CLICK_TITLE_BUTTON(SETUP_CLICK_BUTTON_BY_NAME):
    name = "Click on Title button"
    button_name = "pts_layout:PlainView_hidden_object"

class VALIDATE_TITLE_VIEW_IS_DISPLAYED(SETUP_POPUP_VIEW_STATUS_CHECK):
    name = "Confirm that title.v is displayed"
    view_name = "pts_layout"
    popup_view = "title"
    expected_result = "1"

class VALIDATE_TITLE_TEXT(SETUP_VALIDATE_VALUE_OF_SLOT):
    name = "Confirm that title is Pts_layout V1"
    slot_name = "view_name"
    expected_value = "pts_layout V1"

class __M_PL_49__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = 'Simulate & Validate "Title button (A11)" - Show title'
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [  
                        CLICK_TITLE_BUTTON,
                        THRIVER_WAIT_1_SECOND,
                        VALIDATE_TITLE_VIEW_IS_DISPLAYED,
                        VALIDATE_TITLE_TEXT
                        ]
        self.teardown_path = []