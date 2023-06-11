from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_thriver_wait import *
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_pts_layout_screen import *
from procedures.thriver.test_itp_mcrhci.SETUP.setup_file_folder_manipulation import *
from procedures.thriver.test_itp_mcrhci.SETUP.setup_popup import *

class THRIVER_WAIT_1_SECONDS(SETUP_THRIVER_WAIT):
    time = 1
class THRIVER_WAIT_20_SECONDS(SETUP_THRIVER_WAIT):
    time = 20
class THRIVER_WAIT_3_SECONDS(SETUP_THRIVER_WAIT):
    time = 3

class CREATE_EMPTY_EQUIPMENT_PARAMETERS_FILE(SETUP_CREATE_NEW_EMPTY_FILE):
    path_file = ''.join([os.environ['TCS_ROOT'], '/runtime/hp/log/system/equipment_parameters.txt'])

class CLICK_EDIT_EQT_PARAMS_BUTTON(SETUP_CLICK_EDIT_EQT_PARAMS_BUTTON): pass

class CLICK_SAVE_EQT_PARAMS_BUTTON(SETUP_CLICK_SAVE_EQT_PARAMS_BUTTON): pass

class CLICK_TO_PLANVIEW_MENU_BUTTON(SETUP_CLICK_TO_PLANVIEW_MENU_BUTTON): pass

class KILL_NEDIT_EDITOR_ON_HP_UX(SETUP_KILL_NEDIT_EDITOR):  pass
'''
Pre-Condition:
App started successfully in Service session
equipment_parameters.txt already exist.

Testing procedure:
 (1) Navigate to PTS_Layout screen
 (2) Click on Edit Eqt Params button
* Confirm after step (2)
  + Confirm file equipment_parameters is opened for editing
'''    
    
'''
Confirm file equipment_parameters is opened for editing
===============> manual check on the HP-UX screen
'''    
class __M_PL_14__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = 'Simulate & Validate "Edit Eqt Params Button(B15), File equipment_parameters.txt in ./hp/log/system/ open for editing'
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [
                        CLICK_TO_PLANVIEW_MENU_BUTTON,  
                        THRIVER_WAIT_1_SECONDS,      
                        CREATE_EMPTY_EQUIPMENT_PARAMETERS_FILE,
                        THRIVER_WAIT_1_SECONDS,
                        CLICK_SAVE_EQT_PARAMS_BUTTON,
                        THRIVER_WAIT_20_SECONDS,
                        CLICK_EDIT_EQT_PARAMS_BUTTON,
                        THRIVER_WAIT_3_SECONDS,
                        KILL_NEDIT_EDITOR_ON_HP_UX
                        ]
        self.teardown_path = []

