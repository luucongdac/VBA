from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *
from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import * 

#set
class SET_Q14_RANGE_STATUS_TO_0(SETUP_SET_VARIABLE):
    name = "Set mcr_ecubtcu_q14_range_status to 0"
    var_name = "mcr_ecubtcu_q14_range_status"
    value = 0

class SET_Q14_RANGE_STATUS_TO_1(SETUP_SET_VARIABLE):
    name = "Set mcr_ecubtcu_q14_range_status to 1"
    var_name = "mcr_ecubtcu_q14_range_status"
    value = 1
    
class SET_Q14_RANGE_STATUS_TO_2(SETUP_SET_VARIABLE):
    name = "Set mcr_ecubtcu_q14_range_status to 2"
    var_name = "mcr_ecubtcu_q14_range_status"
    value = 2
    
class SET_Q14_RANGE_STATUS_TO_3(SETUP_SET_VARIABLE):
    name = "Set mcr_ecubtcu_q14_range_status to 3"
    var_name = "mcr_ecubtcu_q14_range_status"
    value = 3
    
class SET_Q14_RANGE_STATUS_TO_4(SETUP_SET_VARIABLE):
    name = "Set mcr_ecubtcu_q14_range_status to 4"
    var_name = "mcr_ecubtcu_q14_range_status"
    value = 4
    
class SET_Q14_RANGE_STATUS_TO_5(SETUP_SET_VARIABLE):
    name = "Set mcr_ecubtcu_q14_range_status to 5"
    var_name = "mcr_ecubtcu_q14_range_status"
    value = 5

class SET_Q14_RANGE_STATUS_TO_6(SETUP_SET_VARIABLE):
    name = "Set mcr_ecubtcu_q14_range_status to 6"
    var_name = "mcr_ecubtcu_q14_range_status"
    value = 6
    
#validate
class VALIDATE_Q14_RANGE_STATUS_TO_0(SETUP_VALIDATE_VALUE_OF_OBJECT_SLOT):
    object_name = "mcr6_q14"
    slot_name = "mcr_ecubtcu_q14_range_status"
    expected_value = 0

class VALIDATE_Q14_RANGE_STATUS_TO_1(SETUP_VALIDATE_VALUE_OF_OBJECT_SLOT):
    object_name = "mcr6_q14"
    slot_name = "mcr_ecubtcu_q14_range_status"
    expected_value = 1
    
class VALIDATE_Q14_RANGE_STATUS_TO_2(SETUP_VALIDATE_VALUE_OF_OBJECT_SLOT):
    object_name = "mcr6_q14"
    slot_name = "mcr_ecubtcu_q14_range_status"
    expected_value = 2
    
class VALIDATE_Q14_RANGE_STATUS_TO_3(SETUP_VALIDATE_VALUE_OF_OBJECT_SLOT):
    object_name = "mcr6_q14"
    slot_name = "mcr_ecubtcu_q14_range_status"
    expected_value = 3
    
class VALIDATE_Q14_RANGE_STATUS_TO_4(SETUP_VALIDATE_VALUE_OF_OBJECT_SLOT):
    object_name = "mcr6_q14"
    slot_name = "mcr_ecubtcu_q14_range_status"
    expected_value = 4
    
class VALIDATE_Q14_RANGE_STATUS_TO_5(SETUP_VALIDATE_VALUE_OF_OBJECT_SLOT):
    object_name = "mcr6_q14"
    slot_name = "mcr_ecubtcu_q14_range_status"
    expected_value = 5
    
class VALIDATE_Q14_RANGE_STATUS_TO_6(SETUP_VALIDATE_VALUE_OF_OBJECT_SLOT):
    object_name = "mcr6_q14"
    slot_name = "mcr_ecubtcu_q14_range_status"
    expected_value = 6

#Todo: Need to add step validation for displayed text of Q14    
class __M_T_SRTR1_9__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate Q14 range status "
        info_exchange = [
                        ] 
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [                      
                        SET_Q14_RANGE_STATUS_TO_0,
                        VALIDATE_Q14_RANGE_STATUS_TO_0,
                        SET_Q14_RANGE_STATUS_TO_1,
                        VALIDATE_Q14_RANGE_STATUS_TO_1,
                        SET_Q14_RANGE_STATUS_TO_2,
                        VALIDATE_Q14_RANGE_STATUS_TO_2,
                        SET_Q14_RANGE_STATUS_TO_3,
                        VALIDATE_Q14_RANGE_STATUS_TO_3,
                        SET_Q14_RANGE_STATUS_TO_4,
                        VALIDATE_Q14_RANGE_STATUS_TO_4,
                        SET_Q14_RANGE_STATUS_TO_5,
                        VALIDATE_Q14_RANGE_STATUS_TO_5,
                        SET_Q14_RANGE_STATUS_TO_6,
                        VALIDATE_Q14_RANGE_STATUS_TO_6,                        
                        ]
        self.teardown_path = []