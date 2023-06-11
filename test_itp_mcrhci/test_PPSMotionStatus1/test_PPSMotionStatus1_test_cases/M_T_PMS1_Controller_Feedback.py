from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_thriver_wait import SETUP_THRIVER_WAIT
from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import SETUP_SET_VARIABLE
from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import SETUP_VALIDATE_OBJECT_INFO

class THRIVER_WAIT_1_SECONDS(SETUP_THRIVER_WAIT):
    time = 1

class SET_MOTOR_ACTIVATED_X_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_xmotor_activated"
    value    = True

class SET_MOTOR_ACTIVATED_Y_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_ymotor_activated"
    value    = True

class SET_MOTOR_ACTIVATED_Z_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_zmotor_activated"
    value    = True

class SET_MOTOR_ACTIVATED_RT_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rotmotor_activated"
    value    = True

class SET_MOTOR_ACTIVATED_PCH_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_pitchmotor_activated"
    value    = True

class SET_MOTOR_ACTIVATED_ROLL_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rollmotor_activated"
    value    = True

class SET_MOTOR_ACTIVATED_GANTRY_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_gantry_motor_activated"
    value    = True

class SET_VELOCITY_ZERO_NO_REQUESTED_X_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_xmotor_desired_v0"
    value    = False

class SET_VELOCITY_ZERO_NO_REQUESTED_Y_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_ymotor_desired_v0"
    value    = False

class SET_VELOCITY_ZERO_NO_REQUESTED_Z_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_zmotor_desired_v0"
    value    = False

class SET_VELOCITY_ZERO_NO_REQUESTED_RT_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rotmotor_desired_v0"
    value    = False

class SET_VELOCITY_ZERO_NO_REQUESTED_PCH_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_pitchmotor_desired_v0"
    value    = False

class SET_VELOCITY_ZERO_NO_REQUESTED_ROLL_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rollmotor_desired_v0"
    value    = False

class SET_VELOCITY_ZERO_NO_REQUESTED_GANTRY_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_gantry_motor_desired_v0"
    value    = False

class SET_NO_ABORT_DECELERATION_X_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_xmotor_abort_dec"
    value    = False

class SET_NO_ABORT_DECELERATION_Y_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_ymotor_abort_dec"
    value    = False

class SET_NO_ABORT_DECELERATION_Z_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_zmotor_abort_dec"
    value    = False
    
class SET_NO_ABORT_DECELERATION_RT_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rotmotor_abort_dec"
    value    = False
    
class SET_NO_ABORT_DECELERATION_PCH_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_pitchmotor_abort_dec"
    value    = False
    
class SET_NO_ABORT_DECELERATION_ROLL_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rollmotor_abort_dec"
    value    = False
    
class SET_NO_ABORT_DECELERATION_GANTRY_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_gantry_motor_abort_dec"
    value    = False
    
class SET_AMPLIFIER_ENABLE_X_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_xmotor_ampli_enable"
    value    = True
    
class SET_AMPLIFIER_ENABLE_Y_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_ymotor_ampli_enable"
    value    = True
    
class SET_AMPLIFIER_ENABLE_Z_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_zmotor_ampli_enable"
    value    = True
    
class SET_AMPLIFIER_ENABLE_RT_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rotmotor_ampli_enable"
    value    = True
    
class SET_AMPLIFIER_ENABLE_PCH_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_pitchmotor_ampli_enable"
    value    = True
    
class SET_AMPLIFIER_ENABLE_ROLL_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rollmotor_ampli_enable"
    value    = True
    
class SET_AMPLIFIER_ENABLE_GANTRY_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_gantry_motor_ampli_enable"
    value    = True
    
class SET_NO_AMPLIFIER_FAULT_X_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_xmotor_ampli_fault"
    value    = False
    
class SET_NO_AMPLIFIER_FAULT_Y_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_ymotor_ampli_fault"
    value    = False
    
class SET_NO_AMPLIFIER_FAULT_Z_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_zmotor_ampli_fault"
    value    = False
    
class SET_NO_AMPLIFIER_FAULT_RT_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rotmotor_ampli_fault"
    value    = False
    
class SET_NO_AMPLIFIER_FAULT_PCH_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_pitchmotor_ampli_fault"
    value    = False
    
class SET_NO_AMPLIFIER_FAULT_ROLL_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rollmotor_ampli_fault"
    value    = False
    
class SET_NO_AMPLIFIER_FAULT_GANTRY_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_gantry_motor_ampli_fault"
    value    = False
    
class SET_CLOSE_LOOP_MODE_X_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_xmotor_openloop_mode"
    value    = False
    
class SET_CLOSE_LOOP_MODE_Y_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_ymotor_openloop_mode"
    value    = False
    
class SET_CLOSE_LOOP_MODE_Z_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_zmotor_openloop_mode"
    value    = False
    
class SET_CLOSE_LOOP_MODE_RT_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rotmotor_openloop_mode"
    value    = False
    
class SET_CLOSE_LOOP_MODE_PCH_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_pitchmotor_openloop_mode"
    value    = False
    
class SET_CLOSE_LOOP_MODE_ROLL_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rollmotor_openloop_mode"
    value    = False
    
class SET_CLOSE_LOOP_MODE_GANTRY_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_gantry_motor_openloop_mode"
    value    = False
    
class SET_NO_FATAL_FOLLOWING_ERROR_X_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_xmotor_fatal_following"
    value    = False
    
class SET_NO_FATAL_FOLLOWING_ERROR_Y_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_ymotor_fatal_following"
    value    = False
    
class SET_NO_FATAL_FOLLOWING_ERROR_Z_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_zmotor_fatal_following"
    value    = False
    
class SET_NO_FATAL_FOLLOWING_ERROR_RT_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rotmotor_fatal_following"
    value    = False
    
class SET_NO_FATAL_FOLLOWING_ERROR_PCH_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_pitchmotor_fatal_following"
    value    = False
    
class SET_NO_FATAL_FOLLOWING_ERROR_ROLL_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rollmotor_fatal_following"
    value    = False
    
class SET_NO_FATAL_FOLLOWING_ERROR_GANTRY_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_gantry_motor_fatal_following"
    value    = False
    
class SET_NO_WARNING_FOLLOWING_ERROR_X_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_xmotor_warning_following"
    value    = False
    
class SET_NO_WARNING_FOLLOWING_ERROR_Y_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_ymotor_warning_following"
    value    = False
    
class SET_NO_WARNING_FOLLOWING_ERROR_Z_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_zmotor_warning_following"
    value    = False
    
class SET_NO_WARNING_FOLLOWING_ERROR_RT_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rotmotor_warning_following"
    value    = False
    
class SET_NO_WARNING_FOLLOWING_ERROR_PCH_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_pitchmotor_warning_following"
    value    = False
    
class SET_NO_WARNING_FOLLOWING_ERROR_ROLL_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rollmotor_warning_following"
    value    = False
    
class SET_NO_WARNING_FOLLOWING_ERROR_GANTRY_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_gantry_motor_warning_following"
    value    = False
    
class SET_IN_POSITION_X_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_xmotor_in_position"
    value    = True
    
class SET_IN_POSITION_Y_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_ymotor_in_position"
    value    = True
    
class SET_IN_POSITION_Z_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_zmotor_in_position"
    value    = True
    
class SET_IN_POSITION_RT_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rotmotor_in_position"
    value    = True
    
class SET_IN_POSITION_PCH_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_pitchmotor_in_position"
    value    = True
    
class SET_IN_POSITION_ROLL_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rollmotor_in_position"
    value    = True
    
class SET_IN_POSITION_GANTRY_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_gantry_motor_in_position"
    value    = True
    
class SET_STOP_ON_POSITION_LIMIT_X_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_xmotor_stop_poslimit"
    value    = True
    
class SET_STOP_ON_POSITION_LIMIT_Y_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_ymotor_stop_poslimit"
    value    = True
    
class SET_STOP_ON_POSITION_LIMIT_Z_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_zmotor_stop_poslimit"
    value    = True
    
class SET_STOP_ON_POSITION_LIMIT_RT_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rotmotor_stop_poslimit"
    value    = True
    
class SET_STOP_ON_POSITION_LIMIT_PCH_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_pitchmotor_stop_poslimit"
    value    = True
    
class SET_STOP_ON_POSITION_LIMIT_ROLL_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rollmotor_stop_poslimit"
    value    = True
    
class SET_STOP_ON_POSITION_LIMIT_GANTRY_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_gantry_motor_stop_poslimit"
    value    = True
    
class SET_POSITIVE_EOT_NOT_REACHED_X_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_xmotor_positive_endlimit"
    value    = False
    
class SET_POSITIVE_EOT_NOT_REACHED_Y_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_ymotor_positive_endlimit"
    value    = False
    
class SET_POSITIVE_EOT_NOT_REACHED_Z_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_zmotor_positive_endlimit"
    value    = False
    
class SET_POSITIVE_EOT_NOT_REACHED_RT_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rotmotor_positive_endlimit"
    value    = False
    
class SET_POSITIVE_EOT_NOT_REACHED_PCH_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_pitchmotor_positive_endlimit"
    value    = False
    
class SET_POSITIVE_EOT_NOT_REACHED_ROLL_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rollmotor_positive_endlimit"
    value    = False
    
class SET_POSITIVE_EOT_NOT_REACHED_GANTRY_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_gantry_eot_cw"
    value    = False
    
class SET_NEGATIVE_EOT_NOT_REACHED_X_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_xmotor_negative_endlimit"
    value    = False
    
class SET_NEGATIVE_EOT_NOT_REACHED_Y_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_ymotor_negative_endlimit"
    value    = False
    
class SET_NEGATIVE_EOT_NOT_REACHED_Z_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_zmotor_negative_endlimit"
    value    = False
    
class SET_NEGATIVE_EOT_NOT_REACHED_RT_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rotmotor_negative_endlimit"
    value    = False
    
class SET_NEGATIVE_EOT_NOT_REACHED_PCH_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_pitchmotor_negative_endlimit"
    value    = False
    
class SET_NEGATIVE_EOT_NOT_REACHED_ROLL_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rollmotor_negative_endlimit"
    value    = False
    
class SET_NEGATIVE_EOT_NOT_REACHED_GANTRY_CHECK_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_gantry_eot_ccw"
    value    = False

class SET_MOTOR_ACTIVATED_X_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_xmotor_activated"
    value    = False
    
class SET_MOTOR_ACTIVATED_Y_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_ymotor_activated"
    value    = False
    
class SET_MOTOR_ACTIVATED_Z_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_zmotor_activated"
    value    = False
    
class SET_MOTOR_ACTIVATED_RT_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rotmotor_activated"
    value    = False
    
class SET_MOTOR_ACTIVATED_PCH_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_pitchmotor_activated"
    value    = False
    
class SET_MOTOR_ACTIVATED_ROLL_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rollmotor_activated"
    value    = False
    
class SET_MOTOR_ACTIVATED_GANTRY_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_gantry_motor_activated"
    value    = False
    
class SET_VELOCITY_ZERO_NO_REQUESTED_X_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_xmotor_desired_v0"
    value    = True
    
class SET_VELOCITY_ZERO_NO_REQUESTED_Y_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_ymotor_desired_v0"
    value    = True
    
class SET_VELOCITY_ZERO_NO_REQUESTED_Z_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_zmotor_desired_v0"
    value    = True
    
class SET_VELOCITY_ZERO_NO_REQUESTED_RT_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rotmotor_desired_v0"
    value    = True
    
class SET_VELOCITY_ZERO_NO_REQUESTED_PCH_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_pitchmotor_desired_v0"
    value    = True
    
class SET_VELOCITY_ZERO_NO_REQUESTED_ROLL_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rollmotor_desired_v0"
    value    = True
    
class SET_VELOCITY_ZERO_NO_REQUESTED_GANTRY_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_gantry_motor_desired_v0"
    value    = True
    
class SET_NO_ABORT_DECELERATION_X_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_xmotor_abort_dec"
    value    = True
    
class SET_NO_ABORT_DECELERATION_Y_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_ymotor_abort_dec"
    value    = True
    
class SET_NO_ABORT_DECELERATION_Z_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_zmotor_abort_dec"
    value    = True
    
class SET_NO_ABORT_DECELERATION_RT_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rotmotor_abort_dec"
    value    = True
    
class SET_NO_ABORT_DECELERATION_PCH_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_pitchmotor_abort_dec"
    value    = True
    
class SET_NO_ABORT_DECELERATION_ROLL_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rollmotor_abort_dec"
    value    = True
    
class SET_NO_ABORT_DECELERATION_GANTRY_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_gantry_motor_abort_dec"
    value    = True
    
class SET_AMPLIFIER_ENABLE_X_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_xmotor_ampli_enable"
    value    = False
    
class SET_AMPLIFIER_ENABLE_Y_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_ymotor_ampli_enable"
    value    = False
    
class SET_AMPLIFIER_ENABLE_Z_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_zmotor_ampli_enable"
    value    = False
    
class SET_AMPLIFIER_ENABLE_RT_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rotmotor_ampli_enable"
    value    = False
    
class SET_AMPLIFIER_ENABLE_PCH_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_pitchmotor_ampli_enable"
    value    = False
    
class SET_AMPLIFIER_ENABLE_ROLL_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rollmotor_ampli_enable"
    value    = False
    
class SET_AMPLIFIER_ENABLE_GANTRY_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_gantry_motor_ampli_enable"
    value    = False
    
class SET_NO_AMPLIFIER_FAULT_X_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_xmotor_ampli_fault"
    value    = True
    
class SET_NO_AMPLIFIER_FAULT_Y_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_ymotor_ampli_fault"
    value    = True
    
class SET_NO_AMPLIFIER_FAULT_Z_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_zmotor_ampli_fault"
    value    = True
    
class SET_NO_AMPLIFIER_FAULT_RT_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rotmotor_ampli_fault"
    value    = True
    
class SET_NO_AMPLIFIER_FAULT_PCH_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_pitchmotor_ampli_fault"
    value    = True
    
class SET_NO_AMPLIFIER_FAULT_ROLL_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rollmotor_ampli_fault"
    value    = True
    
class SET_NO_AMPLIFIER_FAULT_GANTRY_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_gantry_motor_ampli_fault"
    value    = True
    
class SET_CLOSE_LOOP_MODE_X_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_xmotor_openloop_mode"
    value    = True
    
class SET_CLOSE_LOOP_MODE_Y_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_ymotor_openloop_mode"
    value    = True
    
class SET_CLOSE_LOOP_MODE_Z_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_zmotor_openloop_mode"
    value    = True
    
class SET_CLOSE_LOOP_MODE_RT_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rotmotor_openloop_mode"
    value    = True
    
class SET_CLOSE_LOOP_MODE_PCH_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_pitchmotor_openloop_mode"
    value    = True
    
class SET_CLOSE_LOOP_MODE_ROLL_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rollmotor_openloop_mode"
    value    = True
    
class SET_CLOSE_LOOP_MODE_GANTRY_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_gantry_motor_openloop_mode"
    value    = True
    
class SET_NO_FATAL_FOLLOWING_ERROR_X_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_xmotor_fatal_following"
    value    = True
    
class SET_NO_FATAL_FOLLOWING_ERROR_Y_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_ymotor_fatal_following"
    value    = True
    
class SET_NO_FATAL_FOLLOWING_ERROR_Z_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_zmotor_fatal_following"
    value    = True
    
class SET_NO_FATAL_FOLLOWING_ERROR_RT_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rotmotor_fatal_following"
    value    = True
    
class SET_NO_FATAL_FOLLOWING_ERROR_PCH_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_pitchmotor_fatal_following"
    value    = True
    
class SET_NO_FATAL_FOLLOWING_ERROR_ROLL_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rollmotor_fatal_following"
    value    = True
    
class SET_NO_FATAL_FOLLOWING_ERROR_GANTRY_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_gantry_motor_fatal_following"
    value    = True
    
class SET_NO_WARNING_FOLLOWING_ERROR_X_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_xmotor_warning_following"
    value    = True
    
class SET_NO_WARNING_FOLLOWING_ERROR_Y_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_ymotor_warning_following"
    value    = True
    
class SET_NO_WARNING_FOLLOWING_ERROR_Z_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_zmotor_warning_following"
    value    = True
    
class SET_NO_WARNING_FOLLOWING_ERROR_RT_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rotmotor_warning_following"
    value    = True
    
class SET_NO_WARNING_FOLLOWING_ERROR_PCH_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_pitchmotor_warning_following"
    value    = True
    
class SET_NO_WARNING_FOLLOWING_ERROR_ROLL_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rollmotor_warning_following"
    value    = True
    
class SET_NO_WARNING_FOLLOWING_ERROR_GANTRY_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_gantry_motor_warning_following"
    value    = True
    
class SET_IN_POSITION_X_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_xmotor_in_position"
    value    = False
    
class SET_IN_POSITION_Y_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_ymotor_in_position"
    value    = False
    
class SET_IN_POSITION_Z_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_zmotor_in_position"
    value    = False
    
class SET_IN_POSITION_RT_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rotmotor_in_position"
    value    = False
    
class SET_IN_POSITION_PCH_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_pitchmotor_in_position"
    value    = False
    
class SET_IN_POSITION_ROLL_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rollmotor_in_position"
    value    = False
    
class SET_IN_POSITION_GANTRY_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_gantry_motor_in_position"
    value    = False
    
class SET_STOP_ON_POSITION_LIMIT_X_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_xmotor_stop_poslimit"
    value    = False
    
class SET_STOP_ON_POSITION_LIMIT_Y_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_ymotor_stop_poslimit"
    value    = False
    
class SET_STOP_ON_POSITION_LIMIT_Z_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_zmotor_stop_poslimit"
    value    = False
    
class SET_STOP_ON_POSITION_LIMIT_RT_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rotmotor_stop_poslimit"
    value    = False
    
class SET_STOP_ON_POSITION_LIMIT_PCH_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_pitchmotor_stop_poslimit"
    value    = False
    
class SET_STOP_ON_POSITION_LIMIT_ROLL_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rollmotor_stop_poslimit"
    value    = False
    
class SET_STOP_ON_POSITION_LIMIT_GANTRY_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_gantry_motor_stop_poslimit"
    value    = False
    
class SET_POSITIVE_EOT_NOT_REACHED_X_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_xmotor_positive_endlimit"
    value    = True
    
class SET_POSITIVE_EOT_NOT_REACHED_Y_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_ymotor_positive_endlimit"
    value    = True
    
class SET_POSITIVE_EOT_NOT_REACHED_Z_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_zmotor_positive_endlimit"
    value    = True
    
class SET_POSITIVE_EOT_NOT_REACHED_RT_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rotmotor_positive_endlimit"
    value    = True
    
class SET_POSITIVE_EOT_NOT_REACHED_PCH_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_pitchmotor_positive_endlimit"
    value    = True
    
class SET_POSITIVE_EOT_NOT_REACHED_ROLL_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rollmotor_positive_endlimit"
    value    = True
    
class SET_POSITIVE_EOT_NOT_REACHED_GANTRY_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_gantry_eot_cw"
    value    = True
    
class SET_NEGATIVE_EOT_NOT_REACHED_X_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_xmotor_negative_endlimit"
    value    = True
    
class SET_NEGATIVE_EOT_NOT_REACHED_Y_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_ymotor_negative_endlimit"
    value    = True
    
class SET_NEGATIVE_EOT_NOT_REACHED_Z_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_zmotor_negative_endlimit"
    value    = True
    
class SET_NEGATIVE_EOT_NOT_REACHED_RT_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rotmotor_negative_endlimit"
    value    = True
    
class SET_NEGATIVE_EOT_NOT_REACHED_PCH_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_pitchmotor_negative_endlimit"
    value    = True
    
class SET_NEGATIVE_EOT_NOT_REACHED_ROLL_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_pps_rollmotor_negative_endlimit"
    value    = True
    
class SET_NEGATIVE_EOT_NOT_REACHED_GANTRY_CHECK_NOT_OK(SETUP_SET_VARIABLE):
    var_name = "tr1_pcu_gantry_eot_ccw"
    value    = True
    
class VALIDATE_MOTOR_ACTIVATED_X_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate MOTOR_ACTIVATED_X check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_xactivated"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_MOTOR_ACTIVATED_Y_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate MOTOR_ACTIVATED_Y check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_yactivated"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_MOTOR_ACTIVATED_Z_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate MOTOR_ACTIVATED_Z check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_zactivated"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_MOTOR_ACTIVATED_RT_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate MOTOR_ACTIVATED_RT check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_rotactivated"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_MOTOR_ACTIVATED_PCH_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate MOTOR_ACTIVATED_PCH check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_pitchactivated"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_MOTOR_ACTIVATED_ROLL_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate MOTOR_ACTIVATED_ROLL check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_rollactivated"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_MOTOR_ACTIVATED_GANTRY_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate MOTOR_ACTIVATED_GANTRY check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_gantryactivated"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_VELOCITY_ZERO_NO_REQUESTED_X_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate VELOCITY_ZERO_NO_REQUESTED_X check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_xv0"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_VELOCITY_ZERO_NO_REQUESTED_Y_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate VELOCITY_ZERO_NO_REQUESTED_Y check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_yv0"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_VELOCITY_ZERO_NO_REQUESTED_Z_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate VELOCITY_ZERO_NO_REQUESTED_Z check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_zv0"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_VELOCITY_ZERO_NO_REQUESTED_RT_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate VELOCITY_ZERO_NO_REQUESTED_RT check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rotv0"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_VELOCITY_ZERO_NO_REQUESTED_PCH_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate VELOCITY_ZERO_NO_REQUESTED_PCH check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_pitchv0"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_VELOCITY_ZERO_NO_REQUESTED_ROLL_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate VELOCITY_ZERO_NO_REQUESTED_ROLL check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rollv0"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_VELOCITY_ZERO_NO_REQUESTED_GANTRY_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate VELOCITY_ZERO_NO_REQUESTED_GANTRY check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_gantryv0"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_NO_ABORT_DECELERATION_X_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_ABORT_DECELERATION_X check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_xabortdec"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_NO_ABORT_DECELERATION_Y_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_ABORT_DECELERATION_Y check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_yabortdec"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_NO_ABORT_DECELERATION_Z_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_ABORT_DECELERATION_Z check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_zabortdec"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_NO_ABORT_DECELERATION_RT_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_ABORT_DECELERATION_RT check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rotabortdec"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_NO_ABORT_DECELERATION_PCH_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_ABORT_DECELERATION_PCH check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_pitchabortdec"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_NO_ABORT_DECELERATION_ROLL_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_ABORT_DECELERATION_ROLL check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rollabortdec"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_NO_ABORT_DECELERATION_GANTRY_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_ABORT_DECELERATION_GANTRY check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_gantryabortdec"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_AMPLIFIER_ENABLE_X_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate AMPLIFIER_ENABLE_X check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_xamplienable"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_AMPLIFIER_ENABLE_Y_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate AMPLIFIER_ENABLE_Y check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_yamplienable"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_AMPLIFIER_ENABLE_Z_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate AMPLIFIER_ENABLE_Z check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_zamplienable"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_AMPLIFIER_ENABLE_RT_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate AMPLIFIER_ENABLE_RT check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rotamplienable"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_AMPLIFIER_ENABLE_PCH_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate AMPLIFIER_ENABLE_PCH check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_pitchamplienable"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_AMPLIFIER_ENABLE_ROLL_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate AMPLIFIER_ENABLE_ROLL check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rollamplienable"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_AMPLIFIER_ENABLE_GANTRY_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate AMPLIFIER_ENABLE_GANTRY check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_gantryamplienable"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_NO_AMPLIFIER_FAULT_X_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_AMPLIFIER_FAULT_X check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_xfaulterror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_NO_AMPLIFIER_FAULT_Y_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_AMPLIFIER_FAULT_Y check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_yfaulterror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_NO_AMPLIFIER_FAULT_Z_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_AMPLIFIER_FAULT_Z check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_zfaulterror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_NO_AMPLIFIER_FAULT_RT_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_AMPLIFIER_FAULT_RT check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rotfaulterror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_NO_AMPLIFIER_FAULT_PCH_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_AMPLIFIER_FAULT_PCH check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_pitchfaulterror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_NO_AMPLIFIER_FAULT_ROLL_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_AMPLIFIER_FAULT_ROLL check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rollfaulterror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_NO_AMPLIFIER_FAULT_GANTRY_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_AMPLIFIER_FAULT_GANTRY check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_gantryfaulterror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_CLOSE_LOOP_MODE_X_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate CLOSE_LOOP_MODE_X check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_xopenloop"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_CLOSE_LOOP_MODE_Y_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate CLOSE_LOOP_MODE_Y check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_yopenloop"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_CLOSE_LOOP_MODE_Z_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate CLOSE_LOOP_MODE_Z check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_zopenloop"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_CLOSE_LOOP_MODE_RT_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate CLOSE_LOOP_MODE_RT check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rotopenloop"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_CLOSE_LOOP_MODE_PCH_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate CLOSE_LOOP_MODE_PCH check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_pitchopenloop"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_CLOSE_LOOP_MODE_ROLL_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate CLOSE_LOOP_MODE_ROLL check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rollopenloop"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_CLOSE_LOOP_MODE_GANTRY_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate CLOSE_LOOP_MODE_GANTRY check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_gantryopenloop"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_NO_FATAL_FOLLOWING_ERROR_X_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_FATAL_FOLLOWING_ERROR_X check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_xfatalerror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_NO_FATAL_FOLLOWING_ERROR_Y_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_FATAL_FOLLOWING_ERROR_Y check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_yfatalerror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_NO_FATAL_FOLLOWING_ERROR_Z_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_FATAL_FOLLOWING_ERROR_Z check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_zfatalerror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_NO_FATAL_FOLLOWING_ERROR_RT_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_FATAL_FOLLOWING_ERROR_RT check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rotfatalerror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_NO_FATAL_FOLLOWING_ERROR_PCH_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_FATAL_FOLLOWING_ERROR_PCH check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_pitchfatalerror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_NO_FATAL_FOLLOWING_ERROR_ROLL_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_FATAL_FOLLOWING_ERROR_ROLL check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rollfatalerror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_NO_FATAL_FOLLOWING_ERROR_GANTRY_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_FATAL_FOLLOWING_ERROR_GANTRY check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_gantryfatalerror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_NO_WARNING_FOLLOWING_ERROR_X_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_WARNING_FOLLOWING_ERROR_X check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_xwarningerror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_NO_WARNING_FOLLOWING_ERROR_Y_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_WARNING_FOLLOWING_ERROR_Y check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_ywarningerror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_NO_WARNING_FOLLOWING_ERROR_Z_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_WARNING_FOLLOWING_ERROR_Z check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_zwarningerror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_NO_WARNING_FOLLOWING_ERROR_RT_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_WARNING_FOLLOWING_ERROR_RT check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rotwarningerror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_NO_WARNING_FOLLOWING_ERROR_PCH_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_WARNING_FOLLOWING_ERROR_PCH check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_pitchwarningerror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_NO_WARNING_FOLLOWING_ERROR_ROLL_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_WARNING_FOLLOWING_ERROR_ROLL check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rollwarningerror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_NO_WARNING_FOLLOWING_ERROR_GANTRY_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_WARNING_FOLLOWING_ERROR_GANTRY check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_gantrywarningerror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_IN_POSITION_X_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate IN_POSITION_X check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_xinpos"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_IN_POSITION_Y_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate IN_POSITION_Y check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_yinpos"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_IN_POSITION_Z_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate IN_POSITION_Z check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_zinpos"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_IN_POSITION_RT_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate IN_POSITION_RT check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rotinpos"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_IN_POSITION_PCH_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate IN_POSITION_PCH check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_pitchinpos"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_IN_POSITION_ROLL_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate IN_POSITION_ROLL check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rollinpos"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_IN_POSITION_GANTRY_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate IN_POSITION_GANTRY check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_gantryinpos"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_STOP_ON_POSITION_LIMIT_X_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate STOP_ON_POSITION_LIMIT_X check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_xstoppl"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_STOP_ON_POSITION_LIMIT_Y_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate STOP_ON_POSITION_LIMIT_Y check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_ystoppl"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_STOP_ON_POSITION_LIMIT_Z_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate STOP_ON_POSITION_LIMIT_Z check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_zstoppl"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_STOP_ON_POSITION_LIMIT_RT_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate STOP_ON_POSITION_LIMIT_RT check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rotstoppl"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_STOP_ON_POSITION_LIMIT_PCH_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate STOP_ON_POSITION_LIMIT_PCH check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_pitchstoppl"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_STOP_ON_POSITION_LIMIT_ROLL_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate STOP_ON_POSITION_LIMIT_ROLL check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rollstoppl"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_STOP_ON_POSITION_LIMIT_GANTRY_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate STOP_ON_POSITION_LIMIT_GANTRY check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_gantrystoppl"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_POSITIVE_EOT_NOT_REACHED_X_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate POSITIVE_EOT_NOT_REACHED_X check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_xpel"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_POSITIVE_EOT_NOT_REACHED_Y_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate POSITIVE_EOT_NOT_REACHED_Y check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_ypel"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_POSITIVE_EOT_NOT_REACHED_Z_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate POSITIVE_EOT_NOT_REACHED_Z check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_zpel"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_POSITIVE_EOT_NOT_REACHED_RT_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate POSITIVE_EOT_NOT_REACHED_RT check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rotpel"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_POSITIVE_EOT_NOT_REACHED_PCH_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate POSITIVE_EOT_NOT_REACHED_PCH check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_pitchpel"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_POSITIVE_EOT_NOT_REACHED_ROLL_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate POSITIVE_EOT_NOT_REACHED_ROLL check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rollpel"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_POSITIVE_EOT_NOT_REACHED_GANTRY_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate POSITIVE_EOT_NOT_REACHED_GANTRY check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_gantrypel"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_NEGATIVE_EOT_NOT_REACHED_X_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NEGATIVE_EOT_NOT_REACHED_X check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_xnel"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_NEGATIVE_EOT_NOT_REACHED_Y_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NEGATIVE_EOT_NOT_REACHED_Y check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_ynel"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_NEGATIVE_EOT_NOT_REACHED_Z_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NEGATIVE_EOT_NOT_REACHED_Z check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_znel"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_NEGATIVE_EOT_NOT_REACHED_RT_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NEGATIVE_EOT_NOT_REACHED_RT check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rotnel"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_NEGATIVE_EOT_NOT_REACHED_PCH_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NEGATIVE_EOT_NOT_REACHED_PCH check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_pitchnel"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_NEGATIVE_EOT_NOT_REACHED_ROLL_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NEGATIVE_EOT_NOT_REACHED_ROLL check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rollnel"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_NEGATIVE_EOT_NOT_REACHED_GANTRY_CHECK_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NEGATIVE_EOT_NOT_REACHED_GANTRY check ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_gantrynel"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_ok.sd"

class VALIDATE_MOTOR_ACTIVATED_X_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate MOTOR_ACTIVATED_X check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_xactivated"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_MOTOR_ACTIVATED_Y_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate MOTOR_ACTIVATED_Y check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_yactivated"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_MOTOR_ACTIVATED_Z_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate MOTOR_ACTIVATED_Z check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_zactivated"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_MOTOR_ACTIVATED_RT_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate MOTOR_ACTIVATED_RT check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_rotactivated"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_MOTOR_ACTIVATED_PCH_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate MOTOR_ACTIVATED_PCH check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_pitchactivated"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_MOTOR_ACTIVATED_ROLL_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate MOTOR_ACTIVATED_ROLL check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_rollactivated"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_MOTOR_ACTIVATED_GANTRY_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate MOTOR_ACTIVATED_GANTRY check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_gantryactivated"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_VELOCITY_ZERO_NO_REQUESTED_X_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate VELOCITY_ZERO_NO_REQUESTED_X check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_xv0"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_VELOCITY_ZERO_NO_REQUESTED_Y_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate VELOCITY_ZERO_NO_REQUESTED_Y check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_yv0"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_VELOCITY_ZERO_NO_REQUESTED_Z_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate VELOCITY_ZERO_NO_REQUESTED_Z check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_zv0"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_VELOCITY_ZERO_NO_REQUESTED_RT_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate VELOCITY_ZERO_NO_REQUESTED_RT check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rotv0"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_VELOCITY_ZERO_NO_REQUESTED_PCH_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate VELOCITY_ZERO_NO_REQUESTED_PCH check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_pitchv0"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_VELOCITY_ZERO_NO_REQUESTED_ROLL_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate VELOCITY_ZERO_NO_REQUESTED_ROLL check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rollv0"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_VELOCITY_ZERO_NO_REQUESTED_GANTRY_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate VELOCITY_ZERO_NO_REQUESTED_GANTRY check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_gantryv0"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_NO_ABORT_DECELERATION_X_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_ABORT_DECELERATION_X check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_xabortdec"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_NO_ABORT_DECELERATION_Y_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_ABORT_DECELERATION_Y check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_yabortdec"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_NO_ABORT_DECELERATION_Z_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_ABORT_DECELERATION_Z check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_zabortdec"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_NO_ABORT_DECELERATION_RT_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_ABORT_DECELERATION_RT check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rotabortdec"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_NO_ABORT_DECELERATION_PCH_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_ABORT_DECELERATION_PCH check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_pitchabortdec"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_NO_ABORT_DECELERATION_ROLL_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_ABORT_DECELERATION_ROLL check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rollabortdec"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_NO_ABORT_DECELERATION_GANTRY_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_ABORT_DECELERATION_GANTRY check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_gantryabortdec"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_AMPLIFIER_ENABLE_X_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate AMPLIFIER_ENABLE_X check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_xamplienable"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_AMPLIFIER_ENABLE_Y_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate AMPLIFIER_ENABLE_Y check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_yamplienable"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_AMPLIFIER_ENABLE_Z_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate AMPLIFIER_ENABLE_Z check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_zamplienable"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_AMPLIFIER_ENABLE_RT_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate AMPLIFIER_ENABLE_RT check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rotamplienable"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_AMPLIFIER_ENABLE_PCH_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate AMPLIFIER_ENABLE_PCH check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_pitchamplienable"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_AMPLIFIER_ENABLE_ROLL_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate AMPLIFIER_ENABLE_ROLL check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rollamplienable"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_AMPLIFIER_ENABLE_GANTRY_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate AMPLIFIER_ENABLE_GANTRY check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_gantryamplienable"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_NO_AMPLIFIER_FAULT_X_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_AMPLIFIER_FAULT_X check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_xfaulterror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_NO_AMPLIFIER_FAULT_Y_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_AMPLIFIER_FAULT_Y check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_yfaulterror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_NO_AMPLIFIER_FAULT_Z_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_AMPLIFIER_FAULT_Z check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_zfaulterror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_NO_AMPLIFIER_FAULT_RT_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_AMPLIFIER_FAULT_RT check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rotfaulterror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_NO_AMPLIFIER_FAULT_PCH_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_AMPLIFIER_FAULT_PCH check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_pitchfaulterror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_NO_AMPLIFIER_FAULT_ROLL_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_AMPLIFIER_FAULT_ROLL check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rollfaulterror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_NO_AMPLIFIER_FAULT_GANTRY_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_AMPLIFIER_FAULT_GANTRY check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_gantryfaulterror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_CLOSE_LOOP_MODE_X_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate CLOSE_LOOP_MODE_X check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_xopenloop"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_CLOSE_LOOP_MODE_Y_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate CLOSE_LOOP_MODE_Y check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_yopenloop"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_CLOSE_LOOP_MODE_Z_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate CLOSE_LOOP_MODE_Z check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_zopenloop"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_CLOSE_LOOP_MODE_RT_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate CLOSE_LOOP_MODE_RT check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rotopenloop"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_CLOSE_LOOP_MODE_PCH_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate CLOSE_LOOP_MODE_PCH check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_pitchopenloop"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_CLOSE_LOOP_MODE_ROLL_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate CLOSE_LOOP_MODE_ROLL check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rollopenloop"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_CLOSE_LOOP_MODE_GANTRY_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate CLOSE_LOOP_MODE_GANTRY check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_gantryopenloop"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_NO_FATAL_FOLLOWING_ERROR_X_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_FATAL_FOLLOWING_ERROR_X check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_xfatalerror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_NO_FATAL_FOLLOWING_ERROR_Y_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_FATAL_FOLLOWING_ERROR_Y check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_yfatalerror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_NO_FATAL_FOLLOWING_ERROR_Z_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_FATAL_FOLLOWING_ERROR_Z check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_zfatalerror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_NO_FATAL_FOLLOWING_ERROR_RT_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_FATAL_FOLLOWING_ERROR_RT check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rotfatalerror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_NO_FATAL_FOLLOWING_ERROR_PCH_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_FATAL_FOLLOWING_ERROR_PCH check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_pitchfatalerror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_NO_FATAL_FOLLOWING_ERROR_ROLL_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_FATAL_FOLLOWING_ERROR_ROLL check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rollfatalerror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_NO_FATAL_FOLLOWING_ERROR_GANTRY_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_FATAL_FOLLOWING_ERROR_GANTRY check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_gantryfatalerror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_NO_WARNING_FOLLOWING_ERROR_X_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_WARNING_FOLLOWING_ERROR_X check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_xwarningerror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_NO_WARNING_FOLLOWING_ERROR_Y_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_WARNING_FOLLOWING_ERROR_Y check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_ywarningerror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_NO_WARNING_FOLLOWING_ERROR_Z_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_WARNING_FOLLOWING_ERROR_Z check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_zwarningerror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_NO_WARNING_FOLLOWING_ERROR_RT_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_WARNING_FOLLOWING_ERROR_RT check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rotwarningerror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_NO_WARNING_FOLLOWING_ERROR_PCH_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_WARNING_FOLLOWING_ERROR_PCH check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_pitchwarningerror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_NO_WARNING_FOLLOWING_ERROR_ROLL_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_WARNING_FOLLOWING_ERROR_ROLL check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rollwarningerror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_NO_WARNING_FOLLOWING_ERROR_GANTRY_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NO_WARNING_FOLLOWING_ERROR_GANTRY check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_gantrywarningerror"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_IN_POSITION_X_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate IN_POSITION_X check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_xinpos"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_IN_POSITION_Y_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate IN_POSITION_Y check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_yinpos"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_IN_POSITION_Z_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate IN_POSITION_Z check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_zinpos"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_IN_POSITION_RT_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate IN_POSITION_RT check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rotinpos"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_IN_POSITION_PCH_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate IN_POSITION_PCH check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_pitchinpos"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_IN_POSITION_ROLL_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate IN_POSITION_ROLL check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rollinpos"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_IN_POSITION_GANTRY_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate IN_POSITION_GANTRY check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_gantryinpos"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_STOP_ON_POSITION_LIMIT_X_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate STOP_ON_POSITION_LIMIT_X check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_xstoppl"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_STOP_ON_POSITION_LIMIT_Y_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate STOP_ON_POSITION_LIMIT_Y check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_ystoppl"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_STOP_ON_POSITION_LIMIT_Z_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate STOP_ON_POSITION_LIMIT_Z check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_zstoppl"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_STOP_ON_POSITION_LIMIT_RT_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate STOP_ON_POSITION_LIMIT_RT check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rotstoppl"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_STOP_ON_POSITION_LIMIT_PCH_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate STOP_ON_POSITION_LIMIT_PCH check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_pitchstoppl"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_STOP_ON_POSITION_LIMIT_ROLL_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate STOP_ON_POSITION_LIMIT_ROLL check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rollstoppl"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_STOP_ON_POSITION_LIMIT_GANTRY_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate STOP_ON_POSITION_LIMIT_GANTRY check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_gantrystoppl"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_POSITIVE_EOT_NOT_REACHED_X_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate POSITIVE_EOT_NOT_REACHED_X check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_xpel"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_POSITIVE_EOT_NOT_REACHED_Y_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate POSITIVE_EOT_NOT_REACHED_Y check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_ypel"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_POSITIVE_EOT_NOT_REACHED_Z_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate POSITIVE_EOT_NOT_REACHED_Z check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_zpel"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_POSITIVE_EOT_NOT_REACHED_RT_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate POSITIVE_EOT_NOT_REACHED_RT check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rotpel"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_POSITIVE_EOT_NOT_REACHED_PCH_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate POSITIVE_EOT_NOT_REACHED_PCH check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_pitchpel"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_POSITIVE_EOT_NOT_REACHED_ROLL_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate POSITIVE_EOT_NOT_REACHED_ROLL check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rollpel"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_POSITIVE_EOT_NOT_REACHED_GANTRY_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate POSITIVE_EOT_NOT_REACHED_GANTRY check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_gantrypel"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_NEGATIVE_EOT_NOT_REACHED_X_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NEGATIVE_EOT_NOT_REACHED_X check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_xnel"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_NEGATIVE_EOT_NOT_REACHED_Y_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NEGATIVE_EOT_NOT_REACHED_Y check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu_tr1_ynel"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_NEGATIVE_EOT_NOT_REACHED_Z_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NEGATIVE_EOT_NOT_REACHED_Z check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_znel"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_NEGATIVE_EOT_NOT_REACHED_RT_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NEGATIVE_EOT_NOT_REACHED_RT check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rotnel"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_NEGATIVE_EOT_NOT_REACHED_PCH_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NEGATIVE_EOT_NOT_REACHED_PCH check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_pitchnel"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_NEGATIVE_EOT_NOT_REACHED_ROLL_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NEGATIVE_EOT_NOT_REACHED_ROLL check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_rollnel"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class VALIDATE_NEGATIVE_EOT_NOT_REACHED_GANTRY_CHECK_NOT_OK(SETUP_VALIDATE_OBJECT_INFO):
    name           = "Validate NEGATIVE_EOT_NOT_REACHED_GANTRY check not ok" 
    object_name    = "mcr_treatment_pps_motion_status1:pcu5_gantrynel"
    info_type      = "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"
    expected_value = "iba_check_notok.sd"

class __M_T_PMS1_2__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate MOTOR_ACTIVATED_X"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_MOTOR_ACTIVATED_X_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_MOTOR_ACTIVATED_X_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_MOTOR_ACTIVATED_X_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_MOTOR_ACTIVATED_X_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_3__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate MOTOR_ACTIVATED_Y"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_MOTOR_ACTIVATED_Y_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_MOTOR_ACTIVATED_Y_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_MOTOR_ACTIVATED_Y_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_MOTOR_ACTIVATED_Y_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_4__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate MOTOR_ACTIVATED_Z"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_MOTOR_ACTIVATED_Z_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_MOTOR_ACTIVATED_Z_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_MOTOR_ACTIVATED_Z_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_MOTOR_ACTIVATED_Z_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_5__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate MOTOR_ACTIVATED_RT"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_MOTOR_ACTIVATED_RT_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_MOTOR_ACTIVATED_RT_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_MOTOR_ACTIVATED_RT_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_MOTOR_ACTIVATED_RT_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_6__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate MOTOR_ACTIVATED_PCH"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_MOTOR_ACTIVATED_PCH_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_MOTOR_ACTIVATED_PCH_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_MOTOR_ACTIVATED_PCH_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_MOTOR_ACTIVATED_PCH_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_7__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate MOTOR_ACTIVATED_ROLL"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_MOTOR_ACTIVATED_ROLL_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_MOTOR_ACTIVATED_ROLL_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_MOTOR_ACTIVATED_ROLL_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_MOTOR_ACTIVATED_ROLL_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_8__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate MOTOR_ACTIVATED_GANTRY"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_MOTOR_ACTIVATED_GANTRY_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_MOTOR_ACTIVATED_GANTRY_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_MOTOR_ACTIVATED_GANTRY_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_MOTOR_ACTIVATED_GANTRY_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_9__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate VELOCITY_ZERO_NO_REQUESTED_X"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_VELOCITY_ZERO_NO_REQUESTED_X_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_VELOCITY_ZERO_NO_REQUESTED_X_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_VELOCITY_ZERO_NO_REQUESTED_X_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_VELOCITY_ZERO_NO_REQUESTED_X_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_10__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate VELOCITY_ZERO_NO_REQUESTED_Y"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_VELOCITY_ZERO_NO_REQUESTED_Y_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_VELOCITY_ZERO_NO_REQUESTED_Y_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_VELOCITY_ZERO_NO_REQUESTED_Y_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_VELOCITY_ZERO_NO_REQUESTED_Y_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_11__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate VELOCITY_ZERO_NO_REQUESTED_Z"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_VELOCITY_ZERO_NO_REQUESTED_Z_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_VELOCITY_ZERO_NO_REQUESTED_Z_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_VELOCITY_ZERO_NO_REQUESTED_Z_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_VELOCITY_ZERO_NO_REQUESTED_Z_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_12__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate VELOCITY_ZERO_NO_REQUESTED_RT"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_VELOCITY_ZERO_NO_REQUESTED_RT_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_VELOCITY_ZERO_NO_REQUESTED_RT_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_VELOCITY_ZERO_NO_REQUESTED_RT_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_VELOCITY_ZERO_NO_REQUESTED_RT_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_13__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate VELOCITY_ZERO_NO_REQUESTED_PCH"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_VELOCITY_ZERO_NO_REQUESTED_PCH_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_VELOCITY_ZERO_NO_REQUESTED_PCH_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_VELOCITY_ZERO_NO_REQUESTED_PCH_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_VELOCITY_ZERO_NO_REQUESTED_PCH_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_14__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate VELOCITY_ZERO_NO_REQUESTED_ROLL"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_VELOCITY_ZERO_NO_REQUESTED_ROLL_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_VELOCITY_ZERO_NO_REQUESTED_ROLL_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_VELOCITY_ZERO_NO_REQUESTED_ROLL_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_VELOCITY_ZERO_NO_REQUESTED_ROLL_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_15__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate VELOCITY_ZERO_NO_REQUESTED_GANTRY"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_VELOCITY_ZERO_NO_REQUESTED_GANTRY_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_VELOCITY_ZERO_NO_REQUESTED_GANTRY_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_VELOCITY_ZERO_NO_REQUESTED_GANTRY_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_VELOCITY_ZERO_NO_REQUESTED_GANTRY_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_16__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate NO_ABORT_DECELERATION_X"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_NO_ABORT_DECELERATION_X_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_ABORT_DECELERATION_X_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_NO_ABORT_DECELERATION_X_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_ABORT_DECELERATION_X_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_17__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate NO_ABORT_DECELERATION_Y"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_NO_ABORT_DECELERATION_Y_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_ABORT_DECELERATION_Y_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_NO_ABORT_DECELERATION_Y_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_ABORT_DECELERATION_Y_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_18__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate NO_ABORT_DECELERATION_Z"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_NO_ABORT_DECELERATION_Z_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_ABORT_DECELERATION_Z_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_NO_ABORT_DECELERATION_Z_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_ABORT_DECELERATION_Z_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_19__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate NO_ABORT_DECELERATION_RT"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_NO_ABORT_DECELERATION_RT_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_ABORT_DECELERATION_RT_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_NO_ABORT_DECELERATION_RT_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_ABORT_DECELERATION_RT_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_20__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate NO_ABORT_DECELERATION_PCH"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_NO_ABORT_DECELERATION_PCH_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_ABORT_DECELERATION_PCH_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_NO_ABORT_DECELERATION_PCH_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_ABORT_DECELERATION_PCH_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_21__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate NO_ABORT_DECELERATION_ROLL"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_NO_ABORT_DECELERATION_ROLL_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_ABORT_DECELERATION_ROLL_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_NO_ABORT_DECELERATION_ROLL_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_ABORT_DECELERATION_ROLL_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_22__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate NO_ABORT_DECELERATION_GANTRY"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_NO_ABORT_DECELERATION_GANTRY_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_ABORT_DECELERATION_GANTRY_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_NO_ABORT_DECELERATION_GANTRY_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_ABORT_DECELERATION_GANTRY_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_23__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate AMPLIFIER_ENABLE_X"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_AMPLIFIER_ENABLE_X_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_AMPLIFIER_ENABLE_X_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_AMPLIFIER_ENABLE_X_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_AMPLIFIER_ENABLE_X_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_24__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate AMPLIFIER_ENABLE_Y"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_AMPLIFIER_ENABLE_Y_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_AMPLIFIER_ENABLE_Y_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_AMPLIFIER_ENABLE_Y_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_AMPLIFIER_ENABLE_Y_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_25__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate AMPLIFIER_ENABLE_Z"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_AMPLIFIER_ENABLE_Z_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_AMPLIFIER_ENABLE_Z_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_AMPLIFIER_ENABLE_Z_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_AMPLIFIER_ENABLE_Z_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_26__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate AMPLIFIER_ENABLE_RT"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_AMPLIFIER_ENABLE_RT_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_AMPLIFIER_ENABLE_RT_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_AMPLIFIER_ENABLE_RT_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_AMPLIFIER_ENABLE_RT_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_27__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate AMPLIFIER_ENABLE_PCH"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_AMPLIFIER_ENABLE_PCH_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_AMPLIFIER_ENABLE_PCH_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_AMPLIFIER_ENABLE_PCH_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_AMPLIFIER_ENABLE_PCH_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_28__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate AMPLIFIER_ENABLE_ROLL"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_AMPLIFIER_ENABLE_ROLL_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_AMPLIFIER_ENABLE_ROLL_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_AMPLIFIER_ENABLE_ROLL_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_AMPLIFIER_ENABLE_ROLL_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_29__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate AMPLIFIER_ENABLE_GANTRY"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_AMPLIFIER_ENABLE_GANTRY_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_AMPLIFIER_ENABLE_GANTRY_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_AMPLIFIER_ENABLE_GANTRY_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_AMPLIFIER_ENABLE_GANTRY_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_30__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate NO_AMPLIFIER_FAULT_X"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_NO_AMPLIFIER_FAULT_X_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_AMPLIFIER_FAULT_X_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_NO_AMPLIFIER_FAULT_X_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_AMPLIFIER_FAULT_X_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_31__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate NO_AMPLIFIER_FAULT_Y"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_NO_AMPLIFIER_FAULT_Y_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_AMPLIFIER_FAULT_Y_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_NO_AMPLIFIER_FAULT_Y_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_AMPLIFIER_FAULT_Y_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_32__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate NO_AMPLIFIER_FAULT_Z"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_NO_AMPLIFIER_FAULT_Z_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_AMPLIFIER_FAULT_Z_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_NO_AMPLIFIER_FAULT_Z_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_AMPLIFIER_FAULT_Z_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_33__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate NO_AMPLIFIER_FAULT_RT"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_NO_AMPLIFIER_FAULT_RT_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_AMPLIFIER_FAULT_RT_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_NO_AMPLIFIER_FAULT_RT_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_AMPLIFIER_FAULT_RT_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_34__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate NO_AMPLIFIER_FAULT_PCH"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_NO_AMPLIFIER_FAULT_PCH_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_AMPLIFIER_FAULT_PCH_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_NO_AMPLIFIER_FAULT_PCH_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_AMPLIFIER_FAULT_PCH_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_35__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate NO_AMPLIFIER_FAULT_ROLL"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_NO_AMPLIFIER_FAULT_ROLL_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_AMPLIFIER_FAULT_ROLL_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_NO_AMPLIFIER_FAULT_ROLL_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_AMPLIFIER_FAULT_ROLL_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_36__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate NO_AMPLIFIER_FAULT_GANTRY"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_NO_AMPLIFIER_FAULT_GANTRY_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_AMPLIFIER_FAULT_GANTRY_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_NO_AMPLIFIER_FAULT_GANTRY_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_AMPLIFIER_FAULT_GANTRY_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_37__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate CLOSE_LOOP_MODE_X"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_CLOSE_LOOP_MODE_X_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_CLOSE_LOOP_MODE_X_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_CLOSE_LOOP_MODE_X_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_CLOSE_LOOP_MODE_X_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_38__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate CLOSE_LOOP_MODE_Y"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_CLOSE_LOOP_MODE_Y_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_CLOSE_LOOP_MODE_Y_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_CLOSE_LOOP_MODE_Y_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_CLOSE_LOOP_MODE_Y_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_39__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate CLOSE_LOOP_MODE_Z"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_CLOSE_LOOP_MODE_Z_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_CLOSE_LOOP_MODE_Z_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_CLOSE_LOOP_MODE_Z_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_CLOSE_LOOP_MODE_Z_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_40__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate CLOSE_LOOP_MODE_RT"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_CLOSE_LOOP_MODE_RT_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_CLOSE_LOOP_MODE_RT_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_CLOSE_LOOP_MODE_RT_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_CLOSE_LOOP_MODE_RT_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_41__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate CLOSE_LOOP_MODE_PCH"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_CLOSE_LOOP_MODE_PCH_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_CLOSE_LOOP_MODE_PCH_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_CLOSE_LOOP_MODE_PCH_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_CLOSE_LOOP_MODE_PCH_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_42__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate CLOSE_LOOP_MODE_ROLL"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_CLOSE_LOOP_MODE_ROLL_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_CLOSE_LOOP_MODE_ROLL_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_CLOSE_LOOP_MODE_ROLL_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_CLOSE_LOOP_MODE_ROLL_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_43__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate CLOSE_LOOP_MODE_GANTRY"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_CLOSE_LOOP_MODE_GANTRY_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_CLOSE_LOOP_MODE_GANTRY_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_CLOSE_LOOP_MODE_GANTRY_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_CLOSE_LOOP_MODE_GANTRY_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_44__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate NO_FATAL_FOLLOWING_ERROR_X"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_NO_FATAL_FOLLOWING_ERROR_X_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_FATAL_FOLLOWING_ERROR_X_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_NO_FATAL_FOLLOWING_ERROR_X_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_FATAL_FOLLOWING_ERROR_X_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_45__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate NO_FATAL_FOLLOWING_ERROR_Y"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_NO_FATAL_FOLLOWING_ERROR_Y_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_FATAL_FOLLOWING_ERROR_Y_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_NO_FATAL_FOLLOWING_ERROR_Y_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_FATAL_FOLLOWING_ERROR_Y_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_46__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate NO_FATAL_FOLLOWING_ERROR_Z"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_NO_FATAL_FOLLOWING_ERROR_Z_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_FATAL_FOLLOWING_ERROR_Z_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_NO_FATAL_FOLLOWING_ERROR_Z_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_FATAL_FOLLOWING_ERROR_Z_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_47__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate NO_FATAL_FOLLOWING_ERROR_RT"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_NO_FATAL_FOLLOWING_ERROR_RT_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_FATAL_FOLLOWING_ERROR_RT_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_NO_FATAL_FOLLOWING_ERROR_RT_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_FATAL_FOLLOWING_ERROR_RT_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_48__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate NO_FATAL_FOLLOWING_ERROR_PCH"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_NO_FATAL_FOLLOWING_ERROR_PCH_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_FATAL_FOLLOWING_ERROR_PCH_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_NO_FATAL_FOLLOWING_ERROR_PCH_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_FATAL_FOLLOWING_ERROR_PCH_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_49__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate NO_FATAL_FOLLOWING_ERROR_ROLL"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_NO_FATAL_FOLLOWING_ERROR_ROLL_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_FATAL_FOLLOWING_ERROR_ROLL_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_NO_FATAL_FOLLOWING_ERROR_ROLL_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_FATAL_FOLLOWING_ERROR_ROLL_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_50__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate NO_FATAL_FOLLOWING_ERROR_GANTRY"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_NO_FATAL_FOLLOWING_ERROR_GANTRY_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_FATAL_FOLLOWING_ERROR_GANTRY_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_NO_FATAL_FOLLOWING_ERROR_GANTRY_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_FATAL_FOLLOWING_ERROR_GANTRY_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_51__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate NO_WARNING_FOLLOWING_ERROR_X"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_NO_WARNING_FOLLOWING_ERROR_X_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_WARNING_FOLLOWING_ERROR_X_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_NO_WARNING_FOLLOWING_ERROR_X_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_WARNING_FOLLOWING_ERROR_X_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_52__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate NO_WARNING_FOLLOWING_ERROR_Y"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_NO_WARNING_FOLLOWING_ERROR_Y_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_WARNING_FOLLOWING_ERROR_Y_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_NO_WARNING_FOLLOWING_ERROR_Y_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_WARNING_FOLLOWING_ERROR_Y_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_53__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate NO_WARNING_FOLLOWING_ERROR_Z"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_NO_WARNING_FOLLOWING_ERROR_Z_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_WARNING_FOLLOWING_ERROR_Z_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_NO_WARNING_FOLLOWING_ERROR_Z_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_WARNING_FOLLOWING_ERROR_Z_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_54__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate NO_WARNING_FOLLOWING_ERROR_RT"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_NO_WARNING_FOLLOWING_ERROR_RT_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_WARNING_FOLLOWING_ERROR_RT_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_NO_WARNING_FOLLOWING_ERROR_RT_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_WARNING_FOLLOWING_ERROR_RT_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_55__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate NO_WARNING_FOLLOWING_ERROR_PCH"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_NO_WARNING_FOLLOWING_ERROR_PCH_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_WARNING_FOLLOWING_ERROR_PCH_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_NO_WARNING_FOLLOWING_ERROR_PCH_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_WARNING_FOLLOWING_ERROR_PCH_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_56__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate NO_WARNING_FOLLOWING_ERROR_ROLL"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_NO_WARNING_FOLLOWING_ERROR_ROLL_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_WARNING_FOLLOWING_ERROR_ROLL_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_NO_WARNING_FOLLOWING_ERROR_ROLL_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_WARNING_FOLLOWING_ERROR_ROLL_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_57__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate NO_WARNING_FOLLOWING_ERROR_GANTRY"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_NO_WARNING_FOLLOWING_ERROR_GANTRY_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_WARNING_FOLLOWING_ERROR_GANTRY_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_NO_WARNING_FOLLOWING_ERROR_GANTRY_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NO_WARNING_FOLLOWING_ERROR_GANTRY_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_58__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate IN_POSITION_X"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_IN_POSITION_X_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_IN_POSITION_X_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_IN_POSITION_X_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_IN_POSITION_X_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_59__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate IN_POSITION_Y"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_IN_POSITION_Y_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_IN_POSITION_Y_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_IN_POSITION_Y_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_IN_POSITION_Y_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_60__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate IN_POSITION_Z"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_IN_POSITION_Z_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_IN_POSITION_Z_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_IN_POSITION_Z_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_IN_POSITION_Z_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_61__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate IN_POSITION_RT"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_IN_POSITION_RT_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_IN_POSITION_RT_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_IN_POSITION_RT_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_IN_POSITION_RT_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_62__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate IN_POSITION_PCH"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_IN_POSITION_PCH_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_IN_POSITION_PCH_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_IN_POSITION_PCH_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_IN_POSITION_PCH_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_63__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate IN_POSITION_ROLL"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_IN_POSITION_ROLL_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_IN_POSITION_ROLL_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_IN_POSITION_ROLL_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_IN_POSITION_ROLL_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_64__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate IN_POSITION_GANTRY"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_IN_POSITION_GANTRY_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_IN_POSITION_GANTRY_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_IN_POSITION_GANTRY_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_IN_POSITION_GANTRY_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_65__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate STOP_ON_POSITION_LIMIT_X"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_STOP_ON_POSITION_LIMIT_X_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_STOP_ON_POSITION_LIMIT_X_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_STOP_ON_POSITION_LIMIT_X_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_STOP_ON_POSITION_LIMIT_X_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_66__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate STOP_ON_POSITION_LIMIT_Y"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_STOP_ON_POSITION_LIMIT_Y_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_STOP_ON_POSITION_LIMIT_Y_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_STOP_ON_POSITION_LIMIT_Y_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_STOP_ON_POSITION_LIMIT_Y_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_67__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate STOP_ON_POSITION_LIMIT_Z"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_STOP_ON_POSITION_LIMIT_Z_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_STOP_ON_POSITION_LIMIT_Z_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_STOP_ON_POSITION_LIMIT_Z_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_STOP_ON_POSITION_LIMIT_Z_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_68__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate STOP_ON_POSITION_LIMIT_RT"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_STOP_ON_POSITION_LIMIT_RT_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_STOP_ON_POSITION_LIMIT_RT_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_STOP_ON_POSITION_LIMIT_RT_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_STOP_ON_POSITION_LIMIT_RT_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_69__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate STOP_ON_POSITION_LIMIT_PCH"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_STOP_ON_POSITION_LIMIT_PCH_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_STOP_ON_POSITION_LIMIT_PCH_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_STOP_ON_POSITION_LIMIT_PCH_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_STOP_ON_POSITION_LIMIT_PCH_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_70__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate STOP_ON_POSITION_LIMIT_ROLL"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_STOP_ON_POSITION_LIMIT_ROLL_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_STOP_ON_POSITION_LIMIT_ROLL_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_STOP_ON_POSITION_LIMIT_ROLL_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_STOP_ON_POSITION_LIMIT_ROLL_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_71__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate STOP_ON_POSITION_LIMIT_GANTRY"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_STOP_ON_POSITION_LIMIT_GANTRY_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_STOP_ON_POSITION_LIMIT_GANTRY_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_STOP_ON_POSITION_LIMIT_GANTRY_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_STOP_ON_POSITION_LIMIT_GANTRY_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_72__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate POSITIVE_EOT_NOT_REACHED_X"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_POSITIVE_EOT_NOT_REACHED_X_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_POSITIVE_EOT_NOT_REACHED_X_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_POSITIVE_EOT_NOT_REACHED_X_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_POSITIVE_EOT_NOT_REACHED_X_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_73__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate POSITIVE_EOT_NOT_REACHED_Y"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_POSITIVE_EOT_NOT_REACHED_Y_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_POSITIVE_EOT_NOT_REACHED_Y_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_POSITIVE_EOT_NOT_REACHED_Y_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_POSITIVE_EOT_NOT_REACHED_Y_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_74__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate POSITIVE_EOT_NOT_REACHED_Z"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_POSITIVE_EOT_NOT_REACHED_Z_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_POSITIVE_EOT_NOT_REACHED_Z_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_POSITIVE_EOT_NOT_REACHED_Z_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_POSITIVE_EOT_NOT_REACHED_Z_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_75__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate POSITIVE_EOT_NOT_REACHED_RT"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_POSITIVE_EOT_NOT_REACHED_RT_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_POSITIVE_EOT_NOT_REACHED_RT_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_POSITIVE_EOT_NOT_REACHED_RT_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_POSITIVE_EOT_NOT_REACHED_RT_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_76__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate POSITIVE_EOT_NOT_REACHED_PCH"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_POSITIVE_EOT_NOT_REACHED_PCH_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_POSITIVE_EOT_NOT_REACHED_PCH_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_POSITIVE_EOT_NOT_REACHED_PCH_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_POSITIVE_EOT_NOT_REACHED_PCH_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_77__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate POSITIVE_EOT_NOT_REACHED_ROLL"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_POSITIVE_EOT_NOT_REACHED_ROLL_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_POSITIVE_EOT_NOT_REACHED_ROLL_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_POSITIVE_EOT_NOT_REACHED_ROLL_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_POSITIVE_EOT_NOT_REACHED_ROLL_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_78__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate POSITIVE_EOT_NOT_REACHED_GANTRY"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_POSITIVE_EOT_NOT_REACHED_GANTRY_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_POSITIVE_EOT_NOT_REACHED_GANTRY_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_POSITIVE_EOT_NOT_REACHED_GANTRY_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_POSITIVE_EOT_NOT_REACHED_GANTRY_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_79__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate NEGATIVE_EOT_NOT_REACHED_X"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_NEGATIVE_EOT_NOT_REACHED_X_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NEGATIVE_EOT_NOT_REACHED_X_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_NEGATIVE_EOT_NOT_REACHED_X_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NEGATIVE_EOT_NOT_REACHED_X_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_80__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate NEGATIVE_EOT_NOT_REACHED_Y"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_NEGATIVE_EOT_NOT_REACHED_Y_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NEGATIVE_EOT_NOT_REACHED_Y_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_NEGATIVE_EOT_NOT_REACHED_Y_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NEGATIVE_EOT_NOT_REACHED_Y_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_81__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate NEGATIVE_EOT_NOT_REACHED_Z"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_NEGATIVE_EOT_NOT_REACHED_Z_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NEGATIVE_EOT_NOT_REACHED_Z_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_NEGATIVE_EOT_NOT_REACHED_Z_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NEGATIVE_EOT_NOT_REACHED_Z_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_82__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate NEGATIVE_EOT_NOT_REACHED_RT"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_NEGATIVE_EOT_NOT_REACHED_RT_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NEGATIVE_EOT_NOT_REACHED_RT_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_NEGATIVE_EOT_NOT_REACHED_RT_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NEGATIVE_EOT_NOT_REACHED_RT_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_83__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate NEGATIVE_EOT_NOT_REACHED_PCH"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_NEGATIVE_EOT_NOT_REACHED_PCH_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NEGATIVE_EOT_NOT_REACHED_PCH_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_NEGATIVE_EOT_NOT_REACHED_PCH_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NEGATIVE_EOT_NOT_REACHED_PCH_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_84__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate NEGATIVE_EOT_NOT_REACHED_ROLL"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_NEGATIVE_EOT_NOT_REACHED_ROLL_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NEGATIVE_EOT_NOT_REACHED_ROLL_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_NEGATIVE_EOT_NOT_REACHED_ROLL_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NEGATIVE_EOT_NOT_REACHED_ROLL_CHECK_NOT_OK,
                        ]
        self.teardown_path = []
        
class __M_T_PMS1_85__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Simulate & Validate NEGATIVE_EOT_NOT_REACHED_GANTRY"
        info_exchange = []
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ["mcr"]
        self.setup =    [
                        SET_NEGATIVE_EOT_NOT_REACHED_GANTRY_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NEGATIVE_EOT_NOT_REACHED_GANTRY_CHECK_OK,
                        THRIVER_WAIT_1_SECONDS,
                        SET_NEGATIVE_EOT_NOT_REACHED_GANTRY_CHECK_NOT_OK,
                        THRIVER_WAIT_1_SECONDS,
                        VALIDATE_NEGATIVE_EOT_NOT_REACHED_GANTRY_CHECK_NOT_OK,
                        ]
        self.teardown_path = []