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
class THRIVER_WAIT_5_SECONDS(SETUP_THRIVER_WAIT):
    time = 5

class CREATE_EMPTY_NOZZLE1_PARAMETERS_FILE(SETUP_CREATE_NEW_EMPTY_FILE):
    name = "Create nozzle1_parameters.txt file with empty content"
    path_file = ''.join([os.environ['TCS_ROOT'], '/runtime/hp/log/system/nozzle1_parameters.txt'])

class CHECK_EMPTY_CONTENT_NOZZLE1_PARAMETERS_FILE(SETUP_CHECK_CONTENT_FILE):
    name = "Check empty content of file nozzle1_parameters.txt"
    path_check = ''.join([os.environ['TCS_ROOT'], '/runtime/hp/log/system/nozzle1_parameters.txt'])
    content_file = ""

class CHANGE_PERMISSION_000_TO_NOZZLE1_PARAMETERS_FILE_AND_RECHECK(SETUP_CHANGE_PERMISSION_AND_RECHECK_FILE):
    name = "Remove all permissons of file nozzle1_parameters.txt to 000"
    path_check = ''.join([os.environ['TCS_ROOT'], '/runtime/hp/log/system/nozzle1_parameters.txt'])
    permission_check = "000"

class CHANGE_PERMISSION_777_TO_NOZZLE1_PARAMETERS_FILE_AND_RECHECK(SETUP_CHANGE_PERMISSION_AND_RECHECK_FILE):
    name = "Restore all permissions of file nozzle1_parameters.txt to 777"
    path_check = ''.join([os.environ['TCS_ROOT'], '/runtime/hp/log/system/nozzle1_parameters.txt'])
    permission_check = "777"

class CLICK_SAVE_TR1_NOZZLE_BUTTON(SETUP_CLICK_SAVE_TR1_NOZZLE_BUTTON): pass

class VALIDATE_CONTENT_POP_UP(SETUP_VALIDATE_POP_UP_CONTENT):
    name = 'Confirm warining message pop up "Failed to open  nozzle1_parameters.txt for writing"'
    content_popup = "Failed to open nozzle1_parameters.txt for writing"
    screen_popup = "Treatment Information"

class CLICK_OK_POP_UP(SETUP_CLICK_OK_POPUP): pass

class CLICK_TO_PLANVIEW_MENU_BUTTON(SETUP_CLICK_TO_PLANVIEW_MENU_BUTTON): pass

class CHECK_CONTENT_NOZZLE1_PARAMETERS_FILE(SETUP_CHECK_CONTENT_FILE):
    path_check = ''.join([os.environ['TCS_ROOT'], '/runtime/hp/log/system/nozzle1_parameters.txt'])
    content_file = \
'''Fri Feb 10 02:41:58 ICT 2023
Jay Presents :
tr1 Nozzle Parameters
User Comments Here 

Range tr1:                           0.000 cm
Calculated energy:                  0.000 Mev
Calculated field in B1234:        0.00000 Tesla
Gantry1 position feedback:         0.00  degree

1- Fixed Scatterers (Lollipops)
===================================
Lollipop Settings (0=Inserted, 1=Retracted
___1___2___3___4___5___6___7___8___9
---0---0---0---0---0---0---0---0---0
===================================

2a- Range Modulator Parameters
===================================
RMEU Wheel Settings
Large Wheel Position Feedback------------   0
Wheel Selected (0-LW;1-SW1;2-SW2;3-SW3)--   0
Small Wheel SW Stop Setpoint (0-255)-----   0
Setpoint of SW (degrees)----------------- 0.0
Setpoint of SW (#)-----------------------   0
Beam Current Modulation file Loaded------ BCMA????
Setpoint of SW Speed (rpm)---------------   0
===================================

2b- Range Modulator TIMING Parameters
===================================
Measured width of 10hz period (msec)--------------------     0.00
Delay between FE of 10Hz and RE of Box B (msec)---------     0.00
Measured Width of Box B (msec)--------------------------     0.00
Delay between RE of Box B and FE of ICEU1 beam(msec)----     0.00
Delay between FE of Box B and RE of ICEU1 beam(msec)----     0.00
Delay between FE of 10Hz and RE of Photocell (msec)-----     0.00
===================================

3- Second Scatterer Parameters
===================================
Second Scatterer Position Setpoint--------- 0
Second Scatterer Position Feedback (1=In Position)
___1___2___3___4
---0---0---0---0----Second Scatterer Position Feedback (Volts)---  0.00
===================================

4- Variable Collimator Parameters
===================================
Spacing Between X Jaws Feedback(cm)----------------  0.00
Spacing Between X Jaws Redundant Feedback(cm))-----  0.00
Spacing Between Y Jaws Feedback(cm)----------------  0.00
Spacing Between Y Jaws Redundant Feedback(cm)------  0.00
===================================

5- X-Ray Tube Position
===================================
(0=Uninitialized; 1=Inserting; 2=Inserted; 3=Failure; 4=Extracting;
5=Extracted; 6=Stopped)
XRay Tube Status------  0
===== End of Nozzle Data =====
'''

'''
Pre-Condition:
App started successfully in Service session
nozzle1_parameters.txt hasn't exist.

Testing procedure:
 (1) Navigate to PTS_Layout screen
 (2) Remove R/W/X permission fo the file nozzle1_parameters.txt
 (3) Click on Save TR1 Nozzle param button
* Confirm after step (3)
  + Confirm warining message pop up "Failed to open nozzle1_parameters.txt for writing"
'''    
    
class __M_PL_22__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = 'Simulate & Validate "Save TR1 Nozzle Button(B13), nozzle1_parameters.txt file is busy in /hp/log/system/ for editing  '
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [
                        CLICK_TO_PLANVIEW_MENU_BUTTON,  
                        THRIVER_WAIT_1_SECONDS,       
                        CREATE_EMPTY_NOZZLE1_PARAMETERS_FILE,
                        THRIVER_WAIT_1_SECONDS,
                        CHECK_EMPTY_CONTENT_NOZZLE1_PARAMETERS_FILE,
                        THRIVER_WAIT_1_SECONDS,
                        CHANGE_PERMISSION_000_TO_NOZZLE1_PARAMETERS_FILE_AND_RECHECK,
                        THRIVER_WAIT_1_SECONDS,
                        CLICK_SAVE_TR1_NOZZLE_BUTTON,
                        THRIVER_WAIT_5_SECONDS,
                        VALIDATE_CONTENT_POP_UP,
                        CLICK_OK_POP_UP,
                        CHANGE_PERMISSION_777_TO_NOZZLE1_PARAMETERS_FILE_AND_RECHECK,
                        ]
        self.teardown_path = []

