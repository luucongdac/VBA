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

class CREATE_EMPTY_NOZZLE2_PARAMETERS_FILE(SETUP_CREATE_NEW_EMPTY_FILE):
    name = "Create nozzle2_parameters.txt file with empty content"
    path_file = ''.join([os.environ['TCS_ROOT'], '/runtime/hp/log/system/nozzle2_parameters.txt'])

class CHECK_EMPTY_CONTENT_NOZZLE2_PARAMETERS_FILE(SETUP_CHECK_CONTENT_FILE):
    name = "Confirm that nozzle2_parameters.txt is existed with empty content"
    path_check = ''.join([os.environ['TCS_ROOT'], '/runtime/hp/log/system/nozzle2_parameters.txt'])
    content_file = ""

class CLICK_SAVE_TR2_NOZZLE_BUTTON(SETUP_CLICK_SAVE_TR2_NOZZLE_BUTTON): pass

class CLICK_TO_PLANVIEW_MENU_BUTTON(SETUP_CLICK_TO_PLANVIEW_MENU_BUTTON): pass

class CHECK_CONTENT_NOZZLE2_PARAMETERS_FILE(SETUP_CHECK_CONTENT_FILE):
    name = "Confirm that the existing nozzle2_parameters.txt in ./hp/log/system/ is updated."
    path_check = ''.join([os.environ['TCS_ROOT'], '/runtime/hp/log/system/nozzle2_parameters.txt'])
    content_file = \
'''Fri Feb 10 02:42:37 ICT 2023
Jay Presents :
tr2 Nozzle Parameters
User Comments Here 

Range tr2:                           0.000 cm
Calculated energy:                  0.000 Mev
Calculated field in B1234:        0.00000 Tesla
Gantry2 position feedback:         0.00  degree

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
nozzle2_parameters.txt already exist.

Testing procedure:
 (1) Navigate to PTS_Layout screen
 (2) Click on Save TR2 Nozzle button
* Confirm after step (2)
  + Confirm existing nozzle2_parameters.txt in ./hp/log/system/ is updated.
'''    



class __M_PL_27__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = 'Simulate & Validate "Save TR2 Nozzle Button(B14), Update existing nozzle2_parameters.txt file in ./hp/log/system/ '
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [
                        CLICK_TO_PLANVIEW_MENU_BUTTON,  
                        THRIVER_WAIT_1_SECONDS,      
                        CREATE_EMPTY_NOZZLE2_PARAMETERS_FILE,
                        THRIVER_WAIT_1_SECONDS,
                        CHECK_EMPTY_CONTENT_NOZZLE2_PARAMETERS_FILE,
                        CLICK_SAVE_TR2_NOZZLE_BUTTON,
                        THRIVER_WAIT_5_SECONDS,
                        CHECK_CONTENT_NOZZLE2_PARAMETERS_FILE,
                        ]
        self.teardown_path = []

