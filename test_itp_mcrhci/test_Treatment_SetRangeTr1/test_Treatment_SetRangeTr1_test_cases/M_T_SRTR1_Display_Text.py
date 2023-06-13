from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_treatment_set_range_tr1_screen import *
from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import * 

#set
class SET_RANGE_VALUE(SETUP_SET_VARIABLE):
    name = "Set tr1_trmgr_sw_rangeAtNozzle to 8"
    var_name = "tr1_trmgr_sw_rangeAtNozzle"
    value = 8

class SET_VALUE_GANTRY1_POSITION(SETUP_SET_VARIABLE):
    name = "Set tr1_trmgr_sw_gantryangle to 9"
    var_name = "tr1_trmgr_sw_gantryangle"
    value = 9

class SET_VALUE_GANTRY1_POSITION_FEEDBACK(SETUP_SET_VARIABLE):
    name = "Set tr1_pcu_gantry_position_degfeedback to 10"
    var_name = "tr1_pcu_gantry_position_degfeedback"
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

#validate
class VALIDATE_SRTR1_RANGE_VALUE(SETUP_VALIDATE_OBJECT_INFO):
    object_name= "mcr6_range_feedbacktxt"
    info_type = "TMMI_MCR_OBJECT_GET_VALUE"
    expected_value = 8


class VALIDATE_SRTR1_GANTRY1_POSITION_VALUE(SETUP_VALIDATE_OBJECT_INFO):
    object_name= "mcr6_gantry1positiontxt"
    info_type = "TMMI_MCR_OBJECT_GET_VALUE"
    expected_value = 9


class VALIDATE_SRTR1_GANTRY1_POSITION_FEEDBACK_VALUE(SETUP_VALIDATE_OBJECT_INFO):
    object_name= "mcr6_cugantryposfbk"
    info_type = "TMMI_MCR_OBJECT_GET_VALUE"
    expected_value = 10


class VALIDATE_SRTR1_CACULATED_ENERGY_VALUE(SETUP_VALIDATE_OBJECT_INFO):
    object_name= "mcr6_energytxt"
    info_type = "TMMI_MCR_OBJECT_GET_VALUE"
    expected_value = 12


class VALIDATE_SRTR1_CACULATED_FIELD_IN_B1234_VALUE(SETUP_VALIDATE_OBJECT_INFO):
    object_name= "mcr6_fieldtxt"
    info_type = "TMMI_MCR_OBJECT_GET_VALUE"
    expected_value = 15


class VALIDATE_GRAPHITE_STEP_LABEL_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
    object_name= "mcr6_graphitestepreached"
    info_type = "TMMI_MCR_IS_VISIBLE"
    expected_value = "0"


class VALIDATE_GRAPHITE_STEP_LABEL_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
    object_name= "mcr6_graphitestepreached"
    info_type = "TMMI_MCR_IS_VISIBLE"
    expected_value = "1"


class VALIDATE_GRAPHITE_STEP_VALUE_INVISIBLE(SETUP_VALIDATE_OBJECT_INFO):
    object_name= "mcr6_graphitestepreached_value"
    info_type = "TMMI_MCR_IS_VISIBLE"
    expected_value = "0"


class VALIDATE_GRAPHITE_STEP_VALUE_VISIBLE(SETUP_VALIDATE_OBJECT_INFO):
    object_name= "mcr6_graphitestepreached_value"
    info_type = "TMMI_MCR_IS_VISIBLE"
    expected_value = "1"

# Todo: The class SETUP_VALIDATE_VALUE_OF_OBJECT_SLOT needs to investigate more.
# Because the class does not receive full RTvar "mcr_ecubtcu_degrader_feedbackstep" 
# when filling into the "slot_name" but when using the word "feedback" in the 
# RTvar "mcr_ecubtcu_degrader_feedbackstep", it is able to be validated.
class VALIDATE_GRAPHITE_STEP_VALUE(SETUP_VALIDATE_VALUE_OF_OBJECT_SLOT):
    object_name= "mcr6_graphitestepreached_value"
    slot_name = "feedback"
    expected_value = 20

class __M_T_SRTR1_43__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate <Graphite Step Reached:> label on Treatment Set range tr1 "
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


class __M_T_SRTR1_44__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate <Graphite Step Reached:> value on Treatment Set range tr1 "
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

class __M_T_SRTR1_46__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate the <Range> text on Treatment Set range tr1 "
        info_exchange = [
                        ] 
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [
                        SET_RANGE_VALUE,
                        VALIDATE_SRTR1_RANGE_VALUE,
                        ]
        self.teardown_path = []

class __M_T_SRTR1_47__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate the Gantry1 position on Treatment Set range tr1 "
        info_exchange = [
                        ] 
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [
                        SET_VALUE_GANTRY1_POSITION,
                        VALIDATE_SRTR1_GANTRY1_POSITION_VALUE,
                        ]
        self.teardown_path = []

class __M_T_SRTR1_48__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate the Gantry1 position feedback on Treatment Set range tr1 "
        info_exchange = [
                        ] 
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [
                        SET_VALUE_GANTRY1_POSITION_FEEDBACK,
                        VALIDATE_SRTR1_GANTRY1_POSITION_FEEDBACK_VALUE,
                        ]
        self.teardown_path = []

class __M_T_SRTR1_49__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate the Caculated Energy on Treatment Set range tr1 "
        info_exchange = [
                        ] 
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [
                        SET_VALUE_CACULATED_ENERGY,
                        VALIDATE_SRTR1_CACULATED_ENERGY_VALUE,
                        ]
        self.teardown_path = []

class __M_T_SRTR1_50__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate the Caculated field in B1234 on Treatment Set range tr1 "
        info_exchange = [
                        ] 
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [
                        SET_VALUE_CACULATED_FIELD_IN_B1234,
                        VALIDATE_SRTR1_CACULATED_FIELD_IN_B1234_VALUE,
                        ]
        self.teardown_path = []


