from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_thriver_wait import SETUP_THRIVER_WAIT
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_treatment_set_range_tr1_screen import *
from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import *

class THRIVER_WAIT_5_SECONDS(SETUP_THRIVER_WAIT):
    time = 5

class NAVIGATE_TO_SET_RANGE_TR1(SETUP_CLICK_BUTTON_BY_POSITION):
    name = "Navigate to Set Range tr1"
    button_pos_x = 100
    button_pos_y = 400

class SET_MCR_SYSMGR_SW_TCR1SERVICESESSION_0(SETUP_SET_VARIABLE):
    name = "Set mcr_sysmgr_sw_tcr1servicesession to False"
    var_name = "mcr_sysmgr_sw_tcr1servicesession"
    value = False

class SET_MCR_SYSMGR_SW_TCR1SERVICESESSION_1(SETUP_SET_VARIABLE):
    name = "Set mcr_sysmgr_sw_tcr1servicesession to True"
    var_name = "mcr_sysmgr_sw_tcr1servicesession"
    value = True

class SET_RANGE_VALUE_TO_1(SETUP_SET_VARIABLE):
    name = "Set tr1_trmgr_sw_rangeAtNozzle to 1"
    var_name = "tr1_trmgr_sw_rangeAtNozzle"
    value = 1

class SET_VALUE_GANTRY1_POSITION_TO_2(SETUP_SET_VARIABLE):
    name = "Set tr1_trmgr_sw_gantryangle to 2"
    var_name = "tr1_trmgr_sw_gantryangle"
    value = 2

class SET_RANGE_VALUE_TO_5(SETUP_SET_VARIABLE):
    name = "Set tr1_trmgr_sw_rangeAtNozzle to 5"
    var_name = "tr1_trmgr_sw_rangeAtNozzle"
    value = 5

class SET_VALUE_GANTRY1_POSITION_TO_6(SETUP_SET_VARIABLE):
    name = "Set tr1_trmgr_sw_gantryangle to 6"
    var_name = "tr1_trmgr_sw_gantryangle"
    value = 6

class SET_VALUE_MCR_MCRHCI_BEAM_TUNING_TREATMENT_MODE(SETUP_SET_VARIABLE):
    name = "Set mcr_mcrhci_beamtuning_treatmentmode to 3"
    var_name = "mcr_mcrhci_beamtuning_treatmentmode"
    value = 3

# click in screen
class CLICK_SET_RANGE_BUTTON(SETUP_CLICK_BUTTON_BY_NAME):
    name = "In Treatment Set Range Tr1 screen, Click <Set Range> button "
    button_name = "mcr_treatment_set_range1:mcr6_setrangebtn"
    clear_stub = False

class CLICK_TO_OPEN_TUNE_ISEU_SCREEN(SETUP_CLICK_BUTTON_BY_NAME):
    name = "In Treatment Set Range Tr1 screen, Click <Man Tune Screen> button "
    button_name = "mcr_treatment_set_range1:mcr6_iseu1btn"

#validate
class VALIDATE_SET_RANGE_BUTTON(SETUP_VALIDATE_RPC_CALL_FUNCTION):
    name = "Validate <Set Range> button button when the variable mcr_sysmgr_sw_tcr1servicesession is set to False"
    rpc_message_name = "beamLineSetRange"
    destination = "ecubtcu2"
    value = [5, 6]

class VALIDATE_SET_RANGE_BUTTON_TCR1SERVICESESSION_1(SETUP_VALIDATE_RPC_CALL_FUNCTION):
    name = "Validate <Set Range> button when the variable mcr_sysmgr_sw_tcr1servicesession is set to True"
    rpc_message_name = "beamLineSetRange"
    destination = "ecubtcu2"
    value = [1, 2]

class VALIDATE_OPEN_TUNE_ISEU_SCREEN(SETUP_VIEW_DISPLAY_STATUS_CHECK):
    view_name = "tune_iseu"
    expected_result = "1"


class __M_T_SRTR1_2__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = 'Simulate and validate <Set Range> button in Set Range Tr1 screen and function treatmentsetrangebyroom is called'
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = [ 
                     THRIVER_WAIT_5_SECONDS, 
                     SET_MCR_SYSMGR_SW_TCR1SERVICESESSION_0,
                     SET_RANGE_VALUE_TO_5,
                     SET_VALUE_GANTRY1_POSITION_TO_6,
                     THRIVER_WAIT_5_SECONDS,
                     CLICK_SET_RANGE_BUTTON,
                     VALIDATE_SET_RANGE_BUTTON,
                     ]
        self.teardown_path = []	


class __M_T_SRTR1_3__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = 'Simulate and validate <Set Range> button in Set Range Tr1 screen and function setrange is called'
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = [  
                     THRIVER_WAIT_5_SECONDS,
                     SET_MCR_SYSMGR_SW_TCR1SERVICESESSION_1,
                     SET_RANGE_VALUE_TO_1,
                     SET_VALUE_GANTRY1_POSITION_TO_2,
                     SET_VALUE_MCR_MCRHCI_BEAM_TUNING_TREATMENT_MODE,
                     THRIVER_WAIT_5_SECONDS,
                     CLICK_SET_RANGE_BUTTON,
                     VALIDATE_SET_RANGE_BUTTON_TCR1SERVICESESSION_1,
                     ]
        self.teardown_path = []	


class __M_T_SRTR1_51__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = 'Click button Man Tune Screen in Set Range Tr1 screen'
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = [  
                     THRIVER_WAIT_5_SECONDS,
                     CLICK_TO_OPEN_TUNE_ISEU_SCREEN,
                     THRIVER_WAIT_5_SECONDS,
                     VALIDATE_OPEN_TUNE_ISEU_SCREEN,
                     THRIVER_WAIT_5_SECONDS,
                     NAVIGATE_TO_SET_RANGE_TR1,
                     ]
        self.teardown_path = []
