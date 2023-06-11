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
class THRIVER_WAIT_5_SECONDS(SETUP_THRIVER_WAIT):
    time = 5

class CREATE_EMPTY_TR1_NOZZLE_FILE(SETUP_CREATE_NEW_EMPTY_FILE):
    name = "Create nozzle1_parameters.txt file with empty content"
    path_file = ''.join([os.environ['TCS_ROOT'], '/runtime/hp/log/system/nozzle1_parameters.txt'])

class CHANGE_PERMISSION_000_TO_TR1_NOZZLE_FILE_AND_RECHECK(SETUP_CHANGE_PERMISSION_AND_RECHECK_FILE):
    name = "Remove all permissons of file nozzle1_parameters.txt to 000"
    path_check = ''.join([os.environ['TCS_ROOT'], '/runtime/hp/log/system/nozzle1_parameters.txt'])
    permission_check = "000"

class CHANGE_PERMISSION_777_TO_TR1_NOZZLE_FILE_AND_RECHECK(SETUP_CHANGE_PERMISSION_AND_RECHECK_FILE):
    name = "Restore all permissions of file nozzle1_parameters.txt to 777"
    path_check = ''.join([os.environ['TCS_ROOT'], '/runtime/hp/log/system/nozzle1_parameters.txt'])
    permission_check = "777"

class CLICK_EDIT_TR1_NOZZLE_BUTTON(SETUP_CLICK_EDIT_TR1_NOZZLE_BUTTON): pass

class CLICK_SAVE_TR1_NOZZLE_BUTTON(SETUP_CLICK_SAVE_TR1_NOZZLE_BUTTON): pass

class CLICK_TO_PLANVIEW_MENU_BUTTON(SETUP_CLICK_TO_PLANVIEW_MENU_BUTTON): pass

class KILL_NEDIT_EDITOR_ON_HP_UX(SETUP_KILL_NEDIT_EDITOR):  pass
'''
Pre-Condition:
App started successfully in Service session
nozzle1_parameters.txt hasn't exist.

Testing procedure:
 (1) Navigate to PTS_Layout screen
 (2) Remove R/W/X permission fo the file nozzle1_parameters.txt
 (3) Click on Edit TR1 Nozzle button
* Confirm after step (3)
  + Confirm warining message pop up "Failed to open nozzle1_parameters.txt for writing"
'''    
    
'''
Confirm warining message pop up "Failed to open nozzle1_parameters.txt for writing
===============> manual check on the HP-UX screen
'''    
class __M_PL_25__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = 'Simulate & Validate "Edit TR1 Nozzle Button(B16),nozzle1_parameters.txt file is busy in /hp/log/system/ for editing'
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [
                        CLICK_TO_PLANVIEW_MENU_BUTTON,  
                        THRIVER_WAIT_1_SECONDS,      
                        CREATE_EMPTY_TR1_NOZZLE_FILE,
                        THRIVER_WAIT_1_SECONDS,
                        CLICK_SAVE_TR1_NOZZLE_BUTTON,
                        THRIVER_WAIT_5_SECONDS,
                        CHANGE_PERMISSION_000_TO_TR1_NOZZLE_FILE_AND_RECHECK,
                        THRIVER_WAIT_1_SECONDS,
                        CLICK_EDIT_TR1_NOZZLE_BUTTON,
                        THRIVER_WAIT_2_SECONDS,
                        CHANGE_PERMISSION_777_TO_TR1_NOZZLE_FILE_AND_RECHECK,
                        THRIVER_WAIT_3_SECONDS,
                        KILL_NEDIT_EDITOR_ON_HP_UX
                        ]
        self.teardown_path = []

