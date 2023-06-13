from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_thriver_wait import SETUP_THRIVER_WAIT
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_pts_layout_screen import *
from procedures.thriver.test_itp_mcrhci.SETUP.setup_file_folder_manipulation import *
from procedures.thriver.test_itp_mcrhci.SETUP.setup_popup import *

class THRIVER_WAIT_1_SECONDS(SETUP_THRIVER_WAIT):
    time = 1
class THRIVER_WAIT_2_SECONDS(SETUP_THRIVER_WAIT):
    time = 2
class THRIVER_WAIT_3_SECONDS(SETUP_THRIVER_WAIT):
    time = 3

class DELETE_TR2_NOZZLE_FILE(SETUP_DELETE_FILE):
    name = "Delete nozzle2_parameters.txt file in /hp/log/system/"
    path_check = ''.join([os.environ['TCS_ROOT'], '/runtime/hp/log/system/nozzle2_parameters.txt'])

class CLICK_EDIT_TR2_NOZZLE_BUTTON(SETUP_CLICK_EDIT_TR2_NOZZLE_BUTTON): pass

class CLICK_TO_PLANVIEW_MENU_BUTTON(SETUP_CLICK_TO_PLANVIEW_MENU_BUTTON): pass

class KILL_NEDIT_EDITOR_ON_HP_UX(SETUP_KILL_NEDIT_EDITOR):  pass
'''
Pre-Condition:
App started successfully in Service session
nozzle2_parameters.txt hasn't exist.

Testing procedure:
 (1) Navigate to PTS_Layout screen
 (2) delete nozzle2_parameters.txt file in /hp/log/system/
 (3) Click on Edit TR2 Nozzle button
* Confirm after step (3)
  + Confirm error message pop up "Error: could not start edit Program"
'''    
    
'''
Confirm error message pop up ""Error: could not start edit Program
===============> manual check on the HP-UX screen
'''    
class __M_PL_30__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = 'Simulate & Validate "Edit TR2 Nozzle Button(B17), nozzle2_parameters.txt file not exist in /hp/log/system/ for editing'
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [
                        CLICK_TO_PLANVIEW_MENU_BUTTON,  
                        THRIVER_WAIT_1_SECONDS,       
                        DELETE_TR2_NOZZLE_FILE,
                        THRIVER_WAIT_1_SECONDS,
                        CLICK_EDIT_TR2_NOZZLE_BUTTON,
                        THRIVER_WAIT_3_SECONDS,
                        KILL_NEDIT_EDITOR_ON_HP_UX
                        ]
        self.teardown_path = []

