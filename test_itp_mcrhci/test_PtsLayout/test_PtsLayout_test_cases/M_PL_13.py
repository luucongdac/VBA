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
class THRIVER_WAIT_5_SECONDS(SETUP_THRIVER_WAIT):
    time = 5

class CREATE_EMPTY_EQUIPMENT_PARAMETERS_FILE(SETUP_CREATE_NEW_EMPTY_FILE):
    name = "Create equipment_parameters.txt file with empty content"
    path_file = ''.join([os.environ['TCS_ROOT'], '/runtime/hp/log/system/equipment_parameters.txt'])

class CHECK_EMPTY_CONTENT_EQUIPMENT_PARAMETERS_FILE(SETUP_CHECK_CONTENT_FILE):
    name = "Check empty content of file equipment_parameters.txt"
    path_check = ''.join([os.environ['TCS_ROOT'], '/runtime/hp/log/system/equipment_parameters.txt'])
    content_file = ""

class CHANGE_PERMISSION_000_TO_EQUIPMENT_PARAMETERS_FILE_AND_RECHECK(SETUP_CHANGE_PERMISSION_AND_RECHECK_FILE):
    name = "Remove all permissons of file equipment_parameters.txt to 000"
    path_check = ''.join([os.environ['TCS_ROOT'], '/runtime/hp/log/system/equipment_parameters.txt'])
    permission_check = "000"

class CHANGE_PERMISSION_777_TO_EQUIPMENT_PARAMETERS_FILE_AND_RECHECK(SETUP_CHANGE_PERMISSION_AND_RECHECK_FILE):
    name = "Restore all permissions of file equipment_parameters.txt to 777"
    path_check = ''.join([os.environ['TCS_ROOT'], '/runtime/hp/log/system/equipment_parameters.txt'])
    permission_check = "777"

class CLICK_SAVE_EQT_PARAMS_BUTTON(SETUP_CLICK_SAVE_EQT_PARAMS_BUTTON): pass

class VALIDATE_CONTENT_POP_UP(SETUP_VALIDATE_POP_UP_CONTENT):
    name = 'Confirm warining message pop up "Failed to open equipment_parameters.txt for writing"'
    content_popup = "Failed to open equipment_parameters.txt for writing"
    screen_popup = "Treatment Information"

class CLICK_OK_POP_UP(SETUP_CLICK_OK_POPUP): pass

class CLICK_TO_PLANVIEW_MENU_BUTTON(SETUP_CLICK_TO_PLANVIEW_MENU_BUTTON): pass

class CHECK_CONTENT_EQUIPMENT_PARAMETERS_FILE(SETUP_CHECK_CONTENT_FILE):
    path_check = ''.join([os.environ['TCS_ROOT'], '/runtime/hp/log/system/equipment_parameters.txt'])
    content_file = \
'''Fri Feb 10 02:42:38 ICT 2023
Presents :

Equipment Parameters
====================

Range BEAM_LINE_1:           0.000 cm
Range BEAM_LINE_2:           0.000 cm
Calculated energy:        0.000 Mev
Calculated field in B1234:  0.00000 Tesla
Gantry1 position feedback:    0.00 degree
Gantry2 position feedback:    0.00 degree

1- VACUUM SYSTEM
    Cyclo Penning 1: 0.0E+00 mbar   Cyclo Penning 2: 0.0E+00 mbar

2- CYCLO MAGNETS
    Maincoil SP:      0 Dig. /   0.000 A    FB:      0 Dig. /   0.000 A
    Compensation Coil SP:     0 Dig.    FB:  0.00 A

    Yoke Temperature:    0 Dig.

    Harmonic Coil 1-3 SP:    0 Dig.     FB:    0 Dig. /  0.00 A
    Harmonic Coil 2-4 SP:    0 Dig.     FB:    0 Dig. /  0.00 A

3- DEFLECTOR
    Defl. PS SP: 0 Dig. Defl.volt.FB: 0.0 V FB: 0 Dig. / 0.000 mA

    Defl. entrance SP: 0 Dig.       FB: 0 Dig. / 0.0 mm
    Defl. exit SP:     0 Dig.       FB: 0 Dig. / 0.0 mm

4- RF
    Vdee SP: 0 Dig. Vdee1 FB: 0.00 kV   Vdee2 FB: 0.00 kV
    Forward Power: 0 kW I anode: 0.00 A
    External frequency:          MHz

5- SOURCE
    Source position SP: 0 Dig.      FB: 0 Dig. / 0.0 mm
    Filament SP: 0 Dig.         FB: 0 Dig. / 0.0 A
    Arc SP: 0 Dig.
    Arc FB: 0 Dig / 0.00 mA / 0.00 V
    Vref arc: 0 V

6- EXTRACTION QUADRUPOLES
    Q1 SP: 0 Dig.               FB: 0 Dig. / 0.00 A
    Q2 SP: 0 Dig.               FB: 0 Dig. / 0.00 A
7- Cyclo steering magnets
    SG1X SP: 0 Dig.         FB: 0.00 A
    SG1Y SP: 0 Dig.         FB: 0.00 A
    SG2X SP: 0 Dig.         FB: 0.00 A
    SG2Y SP: 0 Dig.         FB: 0.00 A
ESS/BTS PARAMETERS
==================
8- ESS magnets
    Q9     SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q10    SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q11    SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q12    SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q13    SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q14    SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q15    SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q20    SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q21    SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q22    SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla

    B1234  SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla

    SG6Y   SP: 0.00 A           FB: 0.00 A
    SG7Y   SP: 0.00 A           FB: 0.00 A

    TRB34  SP: 0.00 A           FB: 0.00 A
    TRB1   SP: 0.00 A           FB: 0.00 A

9- Degrader/Slits/Group3 parameters
    Deg. Motor FB: 0 step           Pot FB: 0
    Deg. Graphite step FB: 0            Energy: 0.00 Mev

    SLIT 1X feedback: 0.0 mm
    SLIT 1Y feedback: 0.0 mm
    SLIT 2X feedback: 0.0 mm

    GROUP3 corrected feedback: 0.0000 Tesla

10- BTS1 magnets
    B56    SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla

    Q25    SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q26    SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q27    SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla

    SG8    SP: 0.00 A           FB: 0.00 A

    TRB5   SP: 0.00 A           FB: 0.00 A
    TRB6   SP: 0.00 A           FB: 0.00 A

11- GTS1 magnets
    Q0M1   SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q1M1   SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q2M1   SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q3M1   SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    B1G1   SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla

    Q1G1   SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q2G1   SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q3G1   SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q4G1   SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q5G1   SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    B2G1   SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla

    SG9G1  SP: 0.00 A           FB: 0.00 A
    SG10G1 SP: 0.00 A           FB: 0.00 A

12- G1-G2 straight beamline magnets
    Q30    SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q31    SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q32    SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q33    SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q34    SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla

    SG11   SP: 0.00 A           FB: 0.00 A
    SC5B   SP: 0.00 A           FB: 0.00 A
    SC6B   SP: 0.00 A           FB: 0.00 A
    SG12   SP: 0.00 A           FB: 0.00 A

13- BTS2 magnets
    B78    SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla

    Q35    SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q36    SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q37    SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    TRB7   SP: 0.00 A           FB: 0.00 A
    TRB8   SP: 0.00 A           FB: 0.00 A

14- GTS2 magnets
    Q0M2   SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q1M2   SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q2M2   SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q3M2   SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    B1G2   SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla

    Q1G2   SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q2G2   SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q3G2   SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q4G2   SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q5G2   SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    B2G2   SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla

    SG10   SP: 0.00 A           FB: 0.00 A
    SG9G2  SP: 0.00 A           FB: 0.00 A
    SG10G2 SP: 0.00 A           FB: 0.00 A

15- BTS3 magnets
    Q40    SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q41    SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q42    SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q43    SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q44    SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    B9     SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla

    Q45    SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q46    SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q47    SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q0M4   SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q1M4   SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla

    Q48    SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q49    SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla
    Q50    SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla

    SC1B   SP: 0.00 A           FB: 0.00 A
    SC1A   SP: 0.00 A           FB: 0.00 A

    SC2A   SP: 0.00 A           FB: 0.00 A

    SC3A   SP: 0.00 A           FB: 0.00 A
    SC3B   SP: 0.00 A           FB: 0.00 A

    SC4A   SP: 0.00 A           FB: 0.00 A
    SC4B   SP: 0.00 A           FB: 0.00 A

    SC6A   SP: 0.00 A           FB: 0.00 A
    B10    SP: 0.00 A / 0.0000 Tesla    FB: 0.00 A / 0.0000 Tesla

    Q1M3    SP: 0.00 A / 0.0000 Tesla   FB: 0.00 A / 0.0000 Tesla
    Q2M3    SP: 0.00 A / 0.0000 Tesla   FB: 0.00 A / 0.0000 Tesla

=== End ===
'''

'''
Pre-Condition:
App started successfully in Service session
equipment_parameters.txt has permisson 000

Testing procedure:
 (1) Navigate to PTS_Layout screen
 (2) Remove R/W/X permission fo the file equipment_parameters.txt
 (3) Click on Save Eqt Params button"

* Confirm after step (3)
  + Confirm warining message pop up "Failed to open equipment_parameters.txt for writing"
'''    
    
class __M_PL_13__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = 'Simulate & Validate "Save Eqt Params Button(B12)", equipment_parameters.txt file in ./hp/log/system/  is busy'
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [
                        CLICK_TO_PLANVIEW_MENU_BUTTON,  
                        THRIVER_WAIT_1_SECONDS, 
                        CREATE_EMPTY_EQUIPMENT_PARAMETERS_FILE,
                        THRIVER_WAIT_1_SECONDS,
                        CHECK_EMPTY_CONTENT_EQUIPMENT_PARAMETERS_FILE,
                        THRIVER_WAIT_1_SECONDS,
                        CHANGE_PERMISSION_000_TO_EQUIPMENT_PARAMETERS_FILE_AND_RECHECK,
                        THRIVER_WAIT_1_SECONDS,
                        CLICK_SAVE_EQT_PARAMS_BUTTON,
                        THRIVER_WAIT_5_SECONDS,
                        VALIDATE_CONTENT_POP_UP,
                        CLICK_OK_POP_UP,
                        CHANGE_PERMISSION_777_TO_EQUIPMENT_PARAMETERS_FILE_AND_RECHECK,
                        ]
        self.teardown_path = []

