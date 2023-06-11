from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_thriver_wait import SETUP_THRIVER_WAIT
from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_treatment_set_range_tr2_screen import *
from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import * 

class THRIVER_WAIT_5_SECONDS(SETUP_THRIVER_WAIT):
    time = 5

#set
class SET_RANGE_VALUE(SETUP_SET_VARIABLE):
    name = "Set tr2_trmgr_sw_rangeAtNozzle to 8"
    var_name = "tr2_trmgr_sw_rangeAtNozzle"
    value = 8

class SET_VALUE_GANTRY2_POSITION(SETUP_SET_VARIABLE):
    name = "Set tr2_trmgr_sw_gantryangle to 9"
    var_name = "tr2_trmgr_sw_gantryangle"
    value = 9

class SET_VALUE_GANTRY2_POSITION_FEEDBACK(SETUP_SET_VARIABLE):
    name = "Set tr2_pcu_gantry_position_degfeedback to 10"
    var_name = "tr2_pcu_gantry_position_degfeedback"
    value = 10

class SET_VALUE_CACULATED_ENERGY(SETUP_SET_VARIABLE):
    name = "Set mcr_ecubtcu_beamline_range_energy to 12"
    var_name = "mcr_ecubtcu_beamline_range_energy"
    value = 12

class SET_VALUE_CACULATED_FIELD_IN_B1234(SETUP_SET_VARIABLE):
    name = "Set mcr_ecubtcu_beamline_range_fieldb1234 to 15"
    var_name = "mcr_ecubtcu_beamline_range_fieldb1234"
    value = 15

class SET_DEGRADER_STATUS_TO_0_GRAPHITE_STEP(SETUP_SET_VARIABLE):
    name = "Set mcr_ecubtcu_degrader_status to random value in range [0 - 3.5]"
    var_name = "mcr_ecubtcu_degrader_status"
    value = 0

class SET_DEGRADER_STATUS_TO_4_GRAPHITE_STEP(SETUP_SET_VARIABLE):
    name = "Set mcr_ecubtcu_degrader_status to random value in range (3.5 - 4.5]"
    var_name = "mcr_ecubtcu_degrader_status"
    value = 4

class SET_DEGRADER_STATUS_TO_5_GRAPHITE_STEP(SETUP_SET_VARIABLE):
    name = "Set mcr_ecubtcu_degrader_status to random value in range (4.5 - 5]"
    var_name = "mcr_ecubtcu_degrader_status"
    value = 5

class SET_DEGRADER_FEEDBACK_VALUE(SETUP_SET_VARIABLE):
    name = "Set mcr_ecubtcu_degrader_feedbackstep to 20"
    var_name = "mcr_ecubtcu_degrader_feedbackstep"
    value = 20

class SET_VALUE_MCR_MCRHCI_BEAM_TUNING_TREATMENT_MODE_TO_1(SETUP_SET_VARIABLE):
    name = "Set mcr_mcrhci_beamtuning_treatmentmode to 1"
    var_name = "mcr_mcrhci_beamtuning_treatmentmode"
    value = 1
    
class SET_VALUE_MCR_MCRHCI_BEAM_TUNING_TREATMENT_MODE_TO_3(SETUP_SET_VARIABLE):
    name = "Set mcr_mcrhci_beamtuning_treatmentmode to 3"
    var_name = "mcr_mcrhci_beamtuning_treatmentmode"
    value = 3

#validate
class VALIDATE_SRTR2_RANGE_VALUE(SETUP_VALIDATE_OBJECT_INFO):
    object_name= "mcr7_range_feedback"
    info_type = "TMMI_MCR_OBJECT_GET_VALUE"
    expected_value = 8

class VALIDATE_SRTR2_GANTRY2_POSITION_VALUE(SETUP_VALIDATE_OBJECT_INFO):
    object_name= "mcr7_gantry_angle"
    info_type = "TMMI_MCR_OBJECT_GET_VALUE"
    expected_value = 9

class VALIDATE_SRTR2_GANTRY2_POSITION_FEEDBACK_VALUE(SETUP_VALIDATE_OBJECT_INFO):
    object_name= "mcr7_cugantryposfbk"
    info_type = "TMMI_MCR_OBJECT_GET_VALUE"
    expected_value = 10

class VALIDATE_SRTR2_CACULATED_ENERGY_VALUE(SETUP_VALIDATE_OBJECT_INFO):
    object_name= "mcr7_range_energy"
    info_type = "TMMI_MCR_OBJECT_GET_VALUE"
    expected_value = 12

class VALIDATE_SRTR2_CACULATED_FIELD_IN_B1234_VALUE(SETUP_VALIDATE_OBJECT_INFO):
    object_name= "mcr7_range_field"
    info_type = "TMMI_MCR_OBJECT_GET_VALUE"
    expected_value = 15

class VALIDATE_GRAPHITE_STEP_LABEL_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
    object_name= "mcr7_graphite_step_label"
    info_type = "TMMI_MCR_IS_VISIBLE"
    expected_value = "0"

class VALIDATE_GRAPHITE_STEP_LABEL_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
    object_name= "mcr7_graphite_step_label"
    info_type = "TMMI_MCR_IS_VISIBLE"
    expected_value = "1"

class VALIDATE_GRAPHITE_STEP_VALUE_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
    object_name= "mcr7_graphite_step"
    info_type = "TMMI_MCR_IS_VISIBLE"
    expected_value = "0"

class VALIDATE_GRAPHITE_STEP_VALUE_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
    object_name= "mcr7_graphite_step"
    info_type = "TMMI_MCR_IS_VISIBLE"
    expected_value = "1"

# Todo: The class SETUP_VALIDATE_VALUE_OF_OBJECT_SLOT needs to investigate more.
# Because the class does not receive full RTvar "mcr_ecubtcu_degrader_feedbackstep" 
# when filling into the "slot_name" but when using the word "feedback" in the 
# RTvar "mcr_ecubtcu_degrader_feedbackstep", it is able to be validated.
class VALIDATE_GRAPHITE_STEP_VALUE(SETUP_VALIDATE_VALUE_OF_OBJECT_SLOT):
    object_name= "mcr7_graphite_step"
    slot_name = "feedback"
    expected_value = 20
        
class VALIDATE_CURRENT_TREATMENT_MODE_DS_US_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
    object_name= "DS_US_mode_text"
    info_type = "TMMI_MCR_IS_VISIBLE"
    expected_value = "1"

class VALIDATE_CURRENT_TREATMENT_MODE_DS_US_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
    object_name= "DS_US_mode_text"
    info_type = "TMMI_MCR_IS_VISIBLE"
    expected_value = "0"

class VALIDATE_CURRENT_TREATMENT_MODE_PBS_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
    object_name= "PBS_mode_text"
    info_type = "TMMI_MCR_IS_VISIBLE"
    expected_value = "1"
        
class VALIDATE_CURRENT_TREATMENT_MODE_PBS_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
    object_name= "PBS_mode_text"
    info_type = "TMMI_MCR_IS_VISIBLE"
    expected_value = "0"

class __M_T_SRTR2_50__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate <Graphite Step Reached:> label on Treatment Set range tr2 "
        info_exchange = [
                        ] 
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [                        
                        SET_DEGRADER_STATUS_TO_0_GRAPHITE_STEP,
                        VALIDATE_GRAPHITE_STEP_LABEL_INVISIBLE,
                        SET_DEGRADER_STATUS_TO_5_GRAPHITE_STEP,
                        VALIDATE_GRAPHITE_STEP_LABEL_INVISIBLE,
                        SET_DEGRADER_STATUS_TO_4_GRAPHITE_STEP,
                        VALIDATE_GRAPHITE_STEP_LABEL_VISIBLE,
                        ]
        self.teardown_path = []

class __M_T_SRTR2_51__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate <Graphite Step Reached:> value on Treatment Set range tr2 "
        info_exchange = [
                        ] 
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [                       
                        SET_DEGRADER_STATUS_TO_0_GRAPHITE_STEP,
                        VALIDATE_GRAPHITE_STEP_VALUE_INVISIBLE,
                        SET_DEGRADER_STATUS_TO_5_GRAPHITE_STEP,
                        VALIDATE_GRAPHITE_STEP_VALUE_INVISIBLE,
                        SET_DEGRADER_STATUS_TO_4_GRAPHITE_STEP,
                        VALIDATE_GRAPHITE_STEP_VALUE_VISIBLE,
                        SET_DEGRADER_FEEDBACK_VALUE,
                        VALIDATE_GRAPHITE_STEP_VALUE,
                        ]
        self.teardown_path = []

class __M_T_SRTR2_53__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate the <Range> text on Treatment Set range tr2 "
        info_exchange = [
                        ] 
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [
                        SET_RANGE_VALUE,
                        VALIDATE_SRTR2_RANGE_VALUE,
                        ]
        self.teardown_path = []

class __M_T_SRTR2_54__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate the Gantry2 position on Treatment Set range tr2 "
        info_exchange = [
                        ] 
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [
                        SET_VALUE_GANTRY2_POSITION,
                        VALIDATE_SRTR2_GANTRY2_POSITION_VALUE,
                        ]
        self.teardown_path = []

class __M_T_SRTR2_55__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate the Gantry2 position feedback on Treatment Set range tr2 "
        info_exchange = [
                        ] 
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [
                        SET_VALUE_GANTRY2_POSITION_FEEDBACK,
                        VALIDATE_SRTR2_GANTRY2_POSITION_FEEDBACK_VALUE,
                        ]
        self.teardown_path = []

class __M_T_SRTR2_56__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate the Caculated Energy on Treatment Set range tr2 "
        info_exchange = [
                        ] 
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [
                        SET_VALUE_CACULATED_ENERGY,
                        VALIDATE_SRTR2_CACULATED_ENERGY_VALUE,
                        ]
        self.teardown_path = []

class __M_T_SRTR2_57__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate the Caculated field in B1234 on Treatment Set range tr2 "
        info_exchange = [
                        ] 
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [
                        SET_VALUE_CACULATED_FIELD_IN_B1234,
                        VALIDATE_SRTR2_CACULATED_FIELD_IN_B1234_VALUE,
                        ]
        self.teardown_path = []

class __M_T_SRTR2_59__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate the Current treatment mode: DS/US on Treatment Set range tr2 "
        info_exchange = [
                        ] 
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [
                        THRIVER_WAIT_5_SECONDS,
                        SET_VALUE_MCR_MCRHCI_BEAM_TUNING_TREATMENT_MODE_TO_1,
                        VALIDATE_CURRENT_TREATMENT_MODE_DS_US_VISIBLE,
                        THRIVER_WAIT_5_SECONDS,
                        SET_VALUE_MCR_MCRHCI_BEAM_TUNING_TREATMENT_MODE_TO_3,
                        VALIDATE_CURRENT_TREATMENT_MODE_DS_US_INVISIBLE,
                        ]
        self.teardown_path = []

class __M_T_SRTR2_60__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate the Current treatment mode: PBS on Treatment Set range tr2 "
        info_exchange = [
                        ] 
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [
                        THRIVER_WAIT_5_SECONDS,
                        SET_VALUE_MCR_MCRHCI_BEAM_TUNING_TREATMENT_MODE_TO_3,
                        VALIDATE_CURRENT_TREATMENT_MODE_PBS_VISIBLE,
                        THRIVER_WAIT_5_SECONDS,
                        SET_VALUE_MCR_MCRHCI_BEAM_TUNING_TREATMENT_MODE_TO_1,
                        VALIDATE_CURRENT_TREATMENT_MODE_PBS_INVISIBLE,
                        ]
        self.teardown_path = []