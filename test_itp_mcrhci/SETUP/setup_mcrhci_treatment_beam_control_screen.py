
"""
File:
======================================

This module implements set up path for tcrtrmgr test

Copyright (c) MGH 2023

Test for setup ClinicalIntegrationTestProcedure

"""



from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.infoset.tcsobject.dba_objects import *

class SETUP_VALIDATE_BEAM_CONTROl_SCREEN(ClinicalIntegrationTestProcedure):
    # default variable values
    name="validate default value"
    mcr1_rejecttr1btn_visibility_expected = "13"
    mcr1_accepttr1btn_visibility_expected = "13"
    tr2_allocation_status_init_1 = 0
    mcr1_beamrequest_tr2_background_color_expected = "0"
    mcr1_rejecttr2btn_visibility_expected = "1"
    mcr1_accepttr2btn_visibility_expected = "1"
    tr2_accept_led_init_1 = 12
    mcr1_accepttr2_led_background_color_expected = "12"
    tr3_allocation_status_init_1 = 0
    mcr1_beamrequest_tr3_background_color_expected = "0"
    mcr1_rejecttr3btn_visibility_expected = "1"
    mcr1_accepttr3btn_visibility_expected = "1"
    tr3_accept_led_init_1 = 12
    mcr1_accepttr3_led_background_color_expected = "12"
    tr3_reject_led_init_1 = 12
    mcr1_rejecttr3_led_background_color_expected = "12"
    tr4_allocation_status_init_1 = 0
    mcr1_beamrequest_tr3b_background_color_expected = "0"
    mcr1_releasetr3bbtn_visibility_expected = "1"
    mcr1_allocatetr3bbtn_visibility_expected = "1"
    tr4_accept_led_init_1 = 12
    mcr1_releasetr3b_led_background_color_expected = "12"
    tr4_reject_led_init_1 = 12
    mcr1_allocatetr3b_led_background_color_expected = "12"
    tr5_allocation_status_init_1 = 0
    mcr1_beamrequest_tr3c_background_color_expected = "0"
    mcr1_releasemcrbtn_visibility_expected = "1"
    mcr1_allocatemcrbtn_visibility_expected = "1"
    tr5_accept_led_init_1 = 12
    mcr1_releasemcr_led_background_color_expected = "12"
    tr5_reject_led_init_1 = 12
    mcr1_allocatemcr_led_background_color_expected = "12"
    mcr_allocation_status_init_1 = 0
    mcr1_beamrequest_mcr_background_color_expected = "0"
    mcr1_releasetr3bbtn_visibility_expected = "1"
    mcr1_allocatetr3bbtn_visibility_expected = "1"
    mcr_reject_led_init_1 = 12
    mcr1_releasetr3b_led_background_color_expected = "12"
    mcr_accept_led_init_1 = 12
    mcr_allocatetr3b_led_background_color_expected = "12"
    mcr_abo_sw_progress_init_1 = 0
    mcr1_progress2_led_background_color_expected = "0"
    mcr_abo_sw_progress_init_2 = 0
    mcr1_progress3_led_background_color_expected = "0"
    mcr_abo_sw_progress_init_3 = 0
    mcr1_progress4_led_background_color_expected = "0"
    mcr_abo_sw_progress_init_4 = 0
    mcr1_progress5_led_background_color_expected = "0"
    mcr_abo_sw_progress_init_5 = 0
    mcr1_progress6_led_background_color_expected = "0"
    mcr_abo_sw_progress_init_6 = 0
    mcr1_progress7_led_background_color_expected = "0"
    mcr_abo_sw_progress_init_7 = 0
    mcr1_progress8_led_background_color_expected = "0"
    mcr_beammgr_sw_beamallocatedtotr_init_1 = 0
    mcr1_beamon_tr1_background_color_expected = "0"
    mcr_beammgr_sw_beamallocatedtotr_init_2 = 0
    mcr1_beamon_tr2_background_color_expected = "0"
    mcr_beammgr_sw_beamallocatedtotr_init_3 = 0
    mcr1_beamon_tr3a_background_color_expected = "0"
    mcr_beammgr_sw_beamallocatedtotr_init_4 = 0
    mcr1_beamon_tr3b_background_color_expected = "0"
    mcr1_beamprepdonebtn_visibility_expected = "1"
    mcr_bc_beamprep_done_led_init_1 = 12
    mcr1_beamprepdone_led_background_color_expected = "12"
    mcr1_beamprepabortbtn_visibility_expected = "1"
    mcr_bc_beamprep_abort_led_init_1 = 12
    mcr1_beamprepabort_led_background_color_expected = "12"
    allocatedRoomId_init_1 = "Room Allocated"
    Room_Allocated_text_expected = "Room Allocated"
    allocationPriority_init_1 = "Priority"
    Priority_text_expected = "Priority"
    pending1_roomId_init_1 = 13
    roomId_background_color_expected = "12"
    pending1_wait_init_1 = "Room Allocated"
    duration_text_expected = "Room Allocated"
    pending1_priority_init_1 = "Priority"
    priority_text_expected = "Priority"
    pending1_status_init_1 = 14
    pendingAllocated_background_color_expected = "12"
    pending2_roomId_init_1 = "Room Allocated"
    roomId_text_expected = "Room Allocated"
    pending2_wait_init_1 = "Priority"
    duration_text_expected = "Priority"
    pending2_priority_init_1 = 15
    priority_background_color_expected = "12"
    pending2_status_init_1 = "Room Allocated"
    pendingAllocated_text_expected = "Room Allocated"
    pending3_roomId_init_1 = "Priority"
    roomId_text_expected = "Priority"
    pending3_wait_init_1 = 16
    duration_background_color_expected = "12"
    pending3_priority_init_1 = "Room Allocated"
    priority_text_expected = "Room Allocated"
    pending3_status_init_1 = "Priority"
    pendingAllocated_text_expected = "Priority"
    pending4_roomId_init_1 = 17
    roomId_background_color_expected = "12"
    pending4_wait_init_1 = "Room Allocated"
    duration_text_expected = "Room Allocated"
    pending4_priority_init_1 = "Priority"
    priority_text_expected = "Priority"
    pending4_status_init_1 = 18
    pendingAllocated_background_color_expected = "12"
    pending5_roomId_init_1 = "Room Allocated"
    roomId_text_expected = "Room Allocated"
    pending5_wait_init_1 = "Priority"
    duration_text_expected = "Priority"
    pending5_priority_init_1 = 19
    priority_background_color_expected = "12"
    pending5_status_init_1 = "Room Allocated"
    pendingAllocated_text_expected = "Room Allocated"

    def __init__(self, test):
        cls = type(self)
        name = cls.name
        mcr1_rejecttr1btn_visibility_expected = cls.mcr1_rejecttr1btn_visibility_expected
        mcr1_accepttr1btn_visibility_expected = cls.mcr1_accepttr1btn_visibility_expected
        tr2_allocation_status_init_1 = cls.tr2_allocation_status_init_1
        mcr1_beamrequest_tr2_background_color_expected = cls.mcr1_beamrequest_tr2_background_color_expected
        mcr1_rejecttr2btn_visibility_expected = cls.mcr1_rejecttr2btn_visibility_expected
        mcr1_accepttr2btn_visibility_expected = cls.mcr1_accepttr2btn_visibility_expected
        tr2_accept_led_init_1 = cls.tr2_accept_led_init_1
        mcr1_accepttr2_led_background_color_expected = cls.mcr1_accepttr2_led_background_color_expected
        tr3_allocation_status_init_1 = cls.tr3_allocation_status_init_1
        mcr1_beamrequest_tr3_background_color_expected = cls.mcr1_beamrequest_tr3_background_color_expected
        mcr1_rejecttr3btn_visibility_expected = cls.mcr1_rejecttr3btn_visibility_expected
        mcr1_accepttr3btn_visibility_expected = cls.mcr1_accepttr3btn_visibility_expected
        tr3_accept_led_init_1 = cls.tr3_accept_led_init_1
        mcr1_accepttr3_led_background_color_expected = cls.mcr1_accepttr3_led_background_color_expected
        tr3_reject_led_init_1 = cls.tr3_reject_led_init_1
        mcr1_rejecttr3_led_background_color_expected = cls.mcr1_rejecttr3_led_background_color_expected
        tr4_allocation_status_init_1 = cls.tr4_allocation_status_init_1
        mcr1_beamrequest_tr3b_background_color_expected = cls.mcr1_beamrequest_tr3b_background_color_expected
        mcr1_releasetr3bbtn_visibility_expected = cls.mcr1_releasetr3bbtn_visibility_expected
        mcr1_allocatetr3bbtn_visibility_expected = cls.mcr1_allocatetr3bbtn_visibility_expected
        tr4_accept_led_init_1 = cls.tr4_accept_led_init_1
        mcr1_releasetr3b_led_background_color_expected = cls.mcr1_releasetr3b_led_background_color_expected
        tr4_reject_led_init_1 = cls.tr4_reject_led_init_1
        mcr1_allocatetr3b_led_background_color_expected = cls.mcr1_allocatetr3b_led_background_color_expected
        tr5_allocation_status_init_1 = cls.tr5_allocation_status_init_1
        mcr1_beamrequest_tr3c_background_color_expected = cls.mcr1_beamrequest_tr3c_background_color_expected
        mcr1_releasemcrbtn_visibility_expected = cls.mcr1_releasemcrbtn_visibility_expected
        mcr1_allocatemcrbtn_visibility_expected = cls.mcr1_allocatemcrbtn_visibility_expected
        tr5_accept_led_init_1 = cls.tr5_accept_led_init_1
        mcr1_releasemcr_led_background_color_expected = cls.mcr1_releasemcr_led_background_color_expected
        tr5_reject_led_init_1 = cls.tr5_reject_led_init_1
        mcr1_allocatemcr_led_background_color_expected = cls.mcr1_allocatemcr_led_background_color_expected
        mcr_allocation_status_init_1 = cls.mcr_allocation_status_init_1
        mcr1_beamrequest_mcr_background_color_expected = cls.mcr1_beamrequest_mcr_background_color_expected
        mcr1_releasetr3bbtn_visibility_expected = cls.mcr1_releasetr3bbtn_visibility_expected
        mcr1_allocatetr3bbtn_visibility_expected = cls.mcr1_allocatetr3bbtn_visibility_expected
        mcr_reject_led_init_1 = cls.mcr_reject_led_init_1
        mcr1_releasetr3b_led_background_color_expected = cls.mcr1_releasetr3b_led_background_color_expected
        mcr_accept_led_init_1 = cls.mcr_accept_led_init_1
        mcr_allocatetr3b_led_background_color_expected = cls.mcr_allocatetr3b_led_background_color_expected
        mcr_abo_sw_progress_init_1 = cls.mcr_abo_sw_progress_init_1
        mcr1_progress2_led_background_color_expected = cls.mcr1_progress2_led_background_color_expected
        mcr_abo_sw_progress_init_2 = cls.mcr_abo_sw_progress_init_2
        mcr1_progress3_led_background_color_expected = cls.mcr1_progress3_led_background_color_expected
        mcr_abo_sw_progress_init_3 = cls.mcr_abo_sw_progress_init_3
        mcr1_progress4_led_background_color_expected = cls.mcr1_progress4_led_background_color_expected
        mcr_abo_sw_progress_init_4 = cls.mcr_abo_sw_progress_init_4
        mcr1_progress5_led_background_color_expected = cls.mcr1_progress5_led_background_color_expected
        mcr_abo_sw_progress_init_5 = cls.mcr_abo_sw_progress_init_5
        mcr1_progress6_led_background_color_expected = cls.mcr1_progress6_led_background_color_expected
        mcr_abo_sw_progress_init_6 = cls.mcr_abo_sw_progress_init_6
        mcr1_progress7_led_background_color_expected = cls.mcr1_progress7_led_background_color_expected
        mcr_abo_sw_progress_init_7 = cls.mcr_abo_sw_progress_init_7
        mcr1_progress8_led_background_color_expected = cls.mcr1_progress8_led_background_color_expected
        mcr_beammgr_sw_beamallocatedtotr_init_1 = cls.mcr_beammgr_sw_beamallocatedtotr_init_1
        mcr1_beamon_tr1_background_color_expected = cls.mcr1_beamon_tr1_background_color_expected
        mcr_beammgr_sw_beamallocatedtotr_init_2 = cls.mcr_beammgr_sw_beamallocatedtotr_init_2
        mcr1_beamon_tr2_background_color_expected = cls.mcr1_beamon_tr2_background_color_expected
        mcr_beammgr_sw_beamallocatedtotr_init_3 = cls.mcr_beammgr_sw_beamallocatedtotr_init_3
        mcr1_beamon_tr3a_background_color_expected = cls.mcr1_beamon_tr3a_background_color_expected
        mcr_beammgr_sw_beamallocatedtotr_init_4 = cls.mcr_beammgr_sw_beamallocatedtotr_init_4
        mcr1_beamon_tr3b_background_color_expected = cls.mcr1_beamon_tr3b_background_color_expected
        mcr1_beamprepdonebtn_visibility_expected = cls.mcr1_beamprepdonebtn_visibility_expected
        mcr_bc_beamprep_done_led_init_1 = cls.mcr_bc_beamprep_done_led_init_1
        mcr1_beamprepdone_led_background_color_expected = cls.mcr1_beamprepdone_led_background_color_expected
        mcr1_beamprepabortbtn_visibility_expected = cls.mcr1_beamprepabortbtn_visibility_expected
        mcr_bc_beamprep_abort_led_init_1 = cls.mcr_bc_beamprep_abort_led_init_1
        mcr1_beamprepabort_led_background_color_expected = cls.mcr1_beamprepabort_led_background_color_expected
        allocatedRoomId_init_1 = cls.allocatedRoomId_init_1
        Room_Allocated_text_expected = cls.Room_Allocated_text_expected
        allocationPriority_init_1 = cls.allocationPriority_init_1
        Priority_text_expected = cls.Priority_text_expected
        pending1_roomId_init_1 = cls.pending1_roomId_init_1
        roomId_background_color_expected = cls.roomId_background_color_expected
        pending1_wait_init_1 = cls.pending1_wait_init_1
        duration_text_expected = cls.duration_text_expected
        pending1_priority_init_1 = cls.pending1_priority_init_1
        priority_text_expected = cls.priority_text_expected
        pending1_status_init_1 = cls.pending1_status_init_1
        pendingAllocated_background_color_expected = cls.pendingAllocated_background_color_expected
        pending2_roomId_init_1 = cls.pending2_roomId_init_1
        roomId_text_expected = cls.roomId_text_expected
        pending2_wait_init_1 = cls.pending2_wait_init_1
        duration_text_expected = cls.duration_text_expected
        pending2_priority_init_1 = cls.pending2_priority_init_1
        priority_background_color_expected = cls.priority_background_color_expected
        pending2_status_init_1 = cls.pending2_status_init_1
        pendingAllocated_text_expected = cls.pendingAllocated_text_expected
        pending3_roomId_init_1 = cls.pending3_roomId_init_1
        roomId_text_expected = cls.roomId_text_expected
        pending3_wait_init_1 = cls.pending3_wait_init_1
        duration_background_color_expected = cls.duration_background_color_expected
        pending3_priority_init_1 = cls.pending3_priority_init_1
        priority_text_expected = cls.priority_text_expected
        pending3_status_init_1 = cls.pending3_status_init_1
        pendingAllocated_text_expected = cls.pendingAllocated_text_expected
        pending4_roomId_init_1 = cls.pending4_roomId_init_1
        roomId_background_color_expected = cls.roomId_background_color_expected
        pending4_wait_init_1 = cls.pending4_wait_init_1
        duration_text_expected = cls.duration_text_expected
        pending4_priority_init_1 = cls.pending4_priority_init_1
        priority_text_expected = cls.priority_text_expected
        pending4_status_init_1 = cls.pending4_status_init_1
        pendingAllocated_background_color_expected = cls.pendingAllocated_background_color_expected
        pending5_roomId_init_1 = cls.pending5_roomId_init_1
        roomId_text_expected = cls.roomId_text_expected
        pending5_wait_init_1 = cls.pending5_wait_init_1
        duration_text_expected = cls.duration_text_expected
        pending5_priority_init_1 = cls.pending5_priority_init_1
        priority_background_color_expected = cls.priority_background_color_expected
        pending5_status_init_1 = cls.pending5_status_init_1
        pendingAllocated_text_expected = cls.pendingAllocated_text_expected

        #set initial values
        set_tr2_allocation_status_1 = MsgTypeNumeric("tr2_allocation_status", tr2_allocation_status_init_1)
        set_tr2_accept_led_1 = MsgTypeNumeric("tr2_accept_led", tr2_accept_led_init_1)
        set_tr3_allocation_status_1 = MsgTypeNumeric("tr3_allocation_status", tr3_allocation_status_init_1)
        set_tr3_accept_led_1 = MsgTypeNumeric("tr3_accept_led", tr3_accept_led_init_1)
        set_tr3_reject_led_1 = MsgTypeNumeric("tr3_reject_led", tr3_reject_led_init_1)
        set_tr4_allocation_status_1 = MsgTypeNumeric("tr4_allocation_status", tr4_allocation_status_init_1)
        set_tr4_accept_led_1 = MsgTypeNumeric("tr4_accept_led", tr4_accept_led_init_1)
        set_tr4_reject_led_1 = MsgTypeNumeric("tr4_reject_led", tr4_reject_led_init_1)
        set_tr5_allocation_status_1 = MsgTypeNumeric("tr5_allocation_status", tr5_allocation_status_init_1)
        set_tr5_accept_led_1 = MsgTypeNumeric("tr5_accept_led", tr5_accept_led_init_1)
        set_tr5_reject_led_1 = MsgTypeNumeric("tr5_reject_led", tr5_reject_led_init_1)
        set_mcr_allocation_status_1 = MsgTypeNumeric("mcr_allocation_status", mcr_allocation_status_init_1)
        set_mcr_reject_led_1 = MsgTypeNumeric("mcr_reject_led", mcr_reject_led_init_1)
        set_mcr_accept_led_1 = MsgTypeNumeric("mcr_accept_led", mcr_accept_led_init_1)
        set_mcr_abo_sw_progress_1 = MsgTypeNumeric("mcr_abo_sw_progress", mcr_abo_sw_progress_init_1)
        set_mcr_abo_sw_progress_2 = MsgTypeNumeric("mcr_abo_sw_progress", mcr_abo_sw_progress_init_2)
        set_mcr_abo_sw_progress_3 = MsgTypeNumeric("mcr_abo_sw_progress", mcr_abo_sw_progress_init_3)
        set_mcr_abo_sw_progress_4 = MsgTypeNumeric("mcr_abo_sw_progress", mcr_abo_sw_progress_init_4)
        set_mcr_abo_sw_progress_5 = MsgTypeNumeric("mcr_abo_sw_progress", mcr_abo_sw_progress_init_5)
        set_mcr_abo_sw_progress_6 = MsgTypeNumeric("mcr_abo_sw_progress", mcr_abo_sw_progress_init_6)
        set_mcr_abo_sw_progress_7 = MsgTypeNumeric("mcr_abo_sw_progress", mcr_abo_sw_progress_init_7)
        set_mcr_beammgr_sw_beamallocatedtotr_1 = MsgTypeNumeric("mcr_beammgr_sw_beamallocatedtotr", mcr_beammgr_sw_beamallocatedtotr_init_1)
        set_mcr_beammgr_sw_beamallocatedtotr_2 = MsgTypeNumeric("mcr_beammgr_sw_beamallocatedtotr", mcr_beammgr_sw_beamallocatedtotr_init_2)
        set_mcr_beammgr_sw_beamallocatedtotr_3 = MsgTypeNumeric("mcr_beammgr_sw_beamallocatedtotr", mcr_beammgr_sw_beamallocatedtotr_init_3)
        set_mcr_beammgr_sw_beamallocatedtotr_4 = MsgTypeNumeric("mcr_beammgr_sw_beamallocatedtotr", mcr_beammgr_sw_beamallocatedtotr_init_4)
        set_mcr_bc_beamprep_done_led_1 = MsgTypeNumeric("mcr_bc_beamprep_done_led", mcr_bc_beamprep_done_led_init_1)
        set_mcr_bc_beamprep_abort_led_1 = MsgTypeNumeric("mcr_bc_beamprep_abort_led", mcr_bc_beamprep_abort_led_init_1)
        set_allocatedRoomId_1 = MsgTypeString("allocatedRoomId", allocatedRoomId_init_1)
        set_allocationPriority_1 = MsgTypeString("allocationPriority", allocationPriority_init_1)
        set_pending1_roomId_1 = MsgTypeNumeric("pending1_roomId", pending1_roomId_init_1)
        set_pending1_wait_1 = MsgTypeString("pending1_wait", pending1_wait_init_1)
        set_pending1_priority_1 = MsgTypeString("pending1_priority", pending1_priority_init_1)
        set_pending1_status_1 = MsgTypeNumeric("pending1_status", pending1_status_init_1)
        set_pending2_roomId_1 = MsgTypeString("pending2_roomId", pending2_roomId_init_1)
        set_pending2_wait_1 = MsgTypeString("pending2_wait", pending2_wait_init_1)
        set_pending2_priority_1 = MsgTypeNumeric("pending2_priority", pending2_priority_init_1)
        set_pending2_status_1 = MsgTypeString("pending2_status", pending2_status_init_1)
        set_pending3_roomId_1 = MsgTypeString("pending3_roomId", pending3_roomId_init_1)
        set_pending3_wait_1 = MsgTypeNumeric("pending3_wait", pending3_wait_init_1)
        set_pending3_priority_1 = MsgTypeString("pending3_priority", pending3_priority_init_1)
        set_pending3_status_1 = MsgTypeString("pending3_status", pending3_status_init_1)
        set_pending4_roomId_1 = MsgTypeNumeric("pending4_roomId", pending4_roomId_init_1)
        set_pending4_wait_1 = MsgTypeString("pending4_wait", pending4_wait_init_1)
        set_pending4_priority_1 = MsgTypeString("pending4_priority", pending4_priority_init_1)
        set_pending4_status_1 = MsgTypeNumeric("pending4_status", pending4_status_init_1)
        set_pending5_roomId_1 = MsgTypeString("pending5_roomId", pending5_roomId_init_1)
        set_pending5_wait_1 = MsgTypeString("pending5_wait", pending5_wait_init_1)
        set_pending5_priority_1 = MsgTypeNumeric("pending5_priority", pending5_priority_init_1)
        set_pending5_status_1 = MsgTypeString("pending5_status", pending5_status_init_1)

        #get values
        get_mcr1_rejecttr1btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr1_rejecttr1btn")
        get_mcr1_accepttr1btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr1_accepttr1btn")
        get_mcr1_beamrequest_tr2_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr1_beamrequest_tr2")
        get_mcr1_rejecttr2btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr1_rejecttr2btn")
        get_mcr1_accepttr2btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr1_accepttr2btn")
        get_mcr1_accepttr2_led_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr1_accepttr2_led")
        get_mcr1_beamrequest_tr3_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr1_beamrequest_tr3")
        get_mcr1_rejecttr3btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr1_rejecttr3btn")
        get_mcr1_accepttr3btn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr1_accepttr3btn")
        get_mcr1_accepttr3_led_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr1_accepttr3_led")
        get_mcr1_rejecttr3_led_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr1_rejecttr3_led")
        get_mcr1_beamrequest_tr3b_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr1_beamrequest_tr3b")
        get_mcr1_releasetr3bbtn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr1_releasetr3bbtn")
        get_mcr1_allocatetr3bbtn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr1_allocatetr3bbtn")
        get_mcr1_releasetr3b_led_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr1_releasetr3b_led")
        get_mcr1_allocatetr3b_led_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr1_allocatetr3b_led")
        get_mcr1_beamrequest_tr3c_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr1_beamrequest_tr3c")
        get_mcr1_releasemcrbtn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr1_releasemcrbtn")
        get_mcr1_allocatemcrbtn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr1_allocatemcrbtn")
        get_mcr1_releasemcr_led_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr1_releasemcr_led")
        get_mcr1_allocatemcr_led_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr1_allocatemcr_led")
        get_mcr1_beamrequest_mcr_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr1_beamrequest_mcr")
        get_mcr1_releasetr3bbtn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr1_releasetr3bbtn")
        get_mcr1_allocatetr3bbtn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr1_allocatetr3bbtn")
        get_mcr1_releasetr3b_led_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr1_releasetr3b_led")
        get_mcr_allocatetr3b_led_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr_allocatetr3b_led")
        get_mcr1_progress2_led_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr1_progress2_led")
        get_mcr1_progress3_led_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr1_progress3_led")
        get_mcr1_progress4_led_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr1_progress4_led")
        get_mcr1_progress5_led_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr1_progress5_led")
        get_mcr1_progress6_led_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr1_progress6_led")
        get_mcr1_progress7_led_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr1_progress7_led")
        get_mcr1_progress8_led_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr1_progress8_led")
        get_mcr1_beamon_tr1_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr1_beamon_tr1")
        get_mcr1_beamon_tr2_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr1_beamon_tr2")
        get_mcr1_beamon_tr3a_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr1_beamon_tr3a")
        get_mcr1_beamon_tr3b_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr1_beamon_tr3b")
        get_mcr1_beamprepdonebtn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr1_beamprepdonebtn")
        get_mcr1_beamprepdone_led_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr1_beamprepdone_led")
        get_mcr1_beamprepabortbtn_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr1_beamprepabortbtn")
        get_mcr1_beamprepabort_led_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "mcr1_beamprepabort_led")
        get_Room_Allocated_text = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_TEXT_FIELD, variable_in = "Room Allocated")
        get_Priority_text = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_TEXT_FIELD, variable_in = "Priority")
        get_roomId_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "roomId")
        get_duration_text = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_TEXT_FIELD, variable_in = "duration")
        get_priority_text = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_TEXT_FIELD, variable_in = "priority")
        get_pendingAllocated_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "pendingAllocated")
        get_roomId_text = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_TEXT_FIELD, variable_in = "roomId")
        get_duration_text = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_TEXT_FIELD, variable_in = "duration")
        get_priority_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "priority")
        get_pendingAllocated_text = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_TEXT_FIELD, variable_in = "pendingAllocated")
        get_roomId_text = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_TEXT_FIELD, variable_in = "roomId")
        get_duration_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "duration")
        get_priority_text = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_TEXT_FIELD, variable_in = "priority")
        get_pendingAllocated_text = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_TEXT_FIELD, variable_in = "pendingAllocated")
        get_roomId_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "roomId")
        get_duration_text = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_TEXT_FIELD, variable_in = "duration")
        get_priority_text = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_TEXT_FIELD, variable_in = "priority")
        get_pendingAllocated_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "pendingAllocated")
        get_roomId_text = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_TEXT_FIELD, variable_in = "roomId")
        get_duration_text = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_TEXT_FIELD, variable_in = "duration")
        get_priority_background_color = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = "priority")
        get_pendingAllocated_text = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_TEXT_FIELD, variable_in = "pendingAllocated")

        #validate
        validate_mcr1_rejecttr1btn_visibility = MsgTypeString("mcr1_rejecttr1btn:TMMI_MCR_IS_VISIBLE", value=mcr1_rejecttr1btn_visibility_expected)
        validate_mcr1_accepttr1btn_visibility = MsgTypeString("mcr1_accepttr1btn:TMMI_MCR_IS_VISIBLE", value=mcr1_accepttr1btn_visibility_expected)
        validate_mcr1_beamrequest_tr2_background_color = MsgTypeString("mcr1_beamrequest_tr2:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr1_beamrequest_tr2_background_color_expected)
        validate_mcr1_rejecttr2btn_visibility = MsgTypeString("mcr1_rejecttr2btn:TMMI_MCR_IS_VISIBLE", value=mcr1_rejecttr2btn_visibility_expected)
        validate_mcr1_accepttr2btn_visibility = MsgTypeString("mcr1_accepttr2btn:TMMI_MCR_IS_VISIBLE", value=mcr1_accepttr2btn_visibility_expected)
        validate_mcr1_accepttr2_led_background_color = MsgTypeString("mcr1_accepttr2_led:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr1_accepttr2_led_background_color_expected)
        validate_mcr1_beamrequest_tr3_background_color = MsgTypeString("mcr1_beamrequest_tr3:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr1_beamrequest_tr3_background_color_expected)
        validate_mcr1_rejecttr3btn_visibility = MsgTypeString("mcr1_releasetr3atn:TMMI_MCR_IS_VISIBLE", value=mcr1_rejecttr3btn_visibility_expected)
        validate_mcr1_accepttr3btn_visibility = MsgTypeString("mcr1_allocatetr3abtn:TMMI_MCR_IS_VISIBLE", value=mcr1_accepttr3btn_visibility_expected)
        validate_mcr1_accepttr3_led_background_color = MsgTypeString("mcr1_accepttr3_led:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr1_accepttr3_led_background_color_expected)
        validate_mcr1_rejecttr3_led_background_color = MsgTypeString("mcr1_rejecttr3_led:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr1_rejecttr3_led_background_color_expected)
        validate_mcr1_beamrequest_tr3b_background_color = MsgTypeString("mcr1_beamrequest_tr3b:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr1_beamrequest_tr3b_background_color_expected)
        validate_mcr1_releasetr3bbtn_visibility = MsgTypeString("mcr1_releasetr3bbtn:TMMI_MCR_IS_VISIBLE", value=mcr1_releasetr3bbtn_visibility_expected)
        validate_mcr1_allocatetr3bbtn_visibility = MsgTypeString("mcr1_allocatetr3bbtn:TMMI_MCR_IS_VISIBLE", value=mcr1_allocatetr3bbtn_visibility_expected)
        validate_mcr1_releasetr3b_led_background_color = MsgTypeString("mcr1_releasetr3b_led:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr1_releasetr3b_led_background_color_expected)
        validate_mcr1_allocatetr3b_led_background_color = MsgTypeString("mcr1_allocatetr3b_led:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr1_allocatetr3b_led_background_color_expected)
        validate_mcr1_beamrequest_tr3c_background_color = MsgTypeString("mcr1_beamrequest_tr3c:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr1_beamrequest_tr3c_background_color_expected)
        validate_mcr1_releasemcrbtn_visibility = MsgTypeString("mcr1_releasemcrbtn:TMMI_MCR_IS_VISIBLE", value=mcr1_releasemcrbtn_visibility_expected)
        validate_mcr1_allocatemcrbtn_visibility = MsgTypeString("mcr1_allocatemcrbtn:TMMI_MCR_IS_VISIBLE", value=mcr1_allocatemcrbtn_visibility_expected)
        validate_mcr1_releasemcr_led_background_color = MsgTypeString("mcr1_releasemcr_led:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr1_releasemcr_led_background_color_expected)
        validate_mcr1_allocatemcr_led_background_color = MsgTypeString("mcr1_allocatemcr_led:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr1_allocatemcr_led_background_color_expected)
        validate_mcr1_beamrequest_mcr_background_color = MsgTypeString("mcr1_beamrequest_mcr:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr1_beamrequest_mcr_background_color_expected)
        validate_mcr1_releasetr3bbtn_visibility = MsgTypeString("mcr1_releasetr3bbtn:TMMI_MCR_IS_VISIBLE", value=mcr1_releasetr3bbtn_visibility_expected)
        validate_mcr1_allocatetr3bbtn_visibility = MsgTypeString("mcr1_allocatetr3bbtn:TMMI_MCR_IS_VISIBLE", value=mcr1_allocatetr3bbtn_visibility_expected)
        validate_mcr1_releasetr3b_led_background_color = MsgTypeString("mcr1_releasetr3b_led:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr1_releasetr3b_led_background_color_expected)
        validate_mcr_allocatetr3b_led_background_color = MsgTypeString("mcr_allocatetr3b_led:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr_allocatetr3b_led_background_color_expected)
        validate_mcr1_progress2_led_background_color = MsgTypeString("mcr1_progress2_led:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr1_progress2_led_background_color_expected)
        validate_mcr1_progress3_led_background_color = MsgTypeString("mcr1_progress3_led:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr1_progress3_led_background_color_expected)
        validate_mcr1_progress4_led_background_color = MsgTypeString("mcr1_progress4_led:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr1_progress4_led_background_color_expected)
        validate_mcr1_progress5_led_background_color = MsgTypeString("mcr1_progress5_led:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr1_progress5_led_background_color_expected)
        validate_mcr1_progress6_led_background_color = MsgTypeString("mcr1_progress6_led:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr1_progress6_led_background_color_expected)
        validate_mcr1_progress7_led_background_color = MsgTypeString("mcr1_progress7_led:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr1_progress7_led_background_color_expected)
        validate_mcr1_progress8_led_background_color = MsgTypeString("mcr1_progress8_led:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr1_progress8_led_background_color_expected)
        validate_mcr1_beamon_tr1_background_color = MsgTypeString("mcr1_beamon_tr1:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr1_beamon_tr1_background_color_expected)
        validate_mcr1_beamon_tr2_background_color = MsgTypeString("mcr1_beamon_tr2:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr1_beamon_tr2_background_color_expected)
        validate_mcr1_beamon_tr3a_background_color = MsgTypeString("mcr1_beamon_tr3a:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr1_beamon_tr3a_background_color_expected)
        validate_mcr1_beamon_tr3b_background_color = MsgTypeString("mcr1_beamon_tr3b:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr1_beamon_tr3b_background_color_expected)
        validate_mcr1_beamprepdonebtn_visibility = MsgTypeString("mcr1_beamprepdonebtn:TMMI_MCR_IS_VISIBLE", value=mcr1_beamprepdonebtn_visibility_expected)
        validate_mcr1_beamprepdone_led_background_color = MsgTypeString("mcr1_beamprepdone_led:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr1_beamprepdone_led_background_color_expected)
        validate_mcr1_beamprepabortbtn_visibility = MsgTypeString("mcr1_beamprepabortbtn:TMMI_MCR_IS_VISIBLE", value=mcr1_beamprepabortbtn_visibility_expected)
        validate_mcr1_beamprepabort_led_background_color = MsgTypeString("mcr1_beamprepabort_led:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=mcr1_beamprepabort_led_background_color_expected)
        validate_Room_Allocated_text = MsgTypeString("Room Allocated:TMMI_MCR_TEXT_FIELD", value=Room_Allocated_text_expected)
        validate_Priority_text = MsgTypeString("Priority:TMMI_MCR_TEXT_FIELD", value=Priority_text_expected)
        validate_roomId_background_color = MsgTypeString("roomId:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=roomId_background_color_expected)
        validate_duration_text = MsgTypeString("duration:TMMI_MCR_TEXT_FIELD", value=duration_text_expected)
        validate_priority_text = MsgTypeString("priority:TMMI_MCR_TEXT_FIELD", value=priority_text_expected)
        validate_pendingAllocated_background_color = MsgTypeString("pendingAllocated:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=pendingAllocated_background_color_expected)
        validate_roomId_text = MsgTypeString("roomId:TMMI_MCR_TEXT_FIELD", value=roomId_text_expected)
        validate_duration_text = MsgTypeString("duration:TMMI_MCR_TEXT_FIELD", value=duration_text_expected)
        validate_priority_background_color = MsgTypeString("priority:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=priority_background_color_expected)
        validate_pendingAllocated_text = MsgTypeString("pendingAllocated:TMMI_MCR_TEXT_FIELD", value=pendingAllocated_text_expected)
        validate_roomId_text = MsgTypeString("roomId:TMMI_MCR_TEXT_FIELD", value=roomId_text_expected)
        validate_duration_background_color = MsgTypeString("duration:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=duration_background_color_expected)
        validate_priority_text = MsgTypeString("priority:TMMI_MCR_TEXT_FIELD", value=priority_text_expected)
        validate_pendingAllocated_text = MsgTypeString("pendingAllocated:TMMI_MCR_TEXT_FIELD", value=pendingAllocated_text_expected)
        validate_roomId_background_color = MsgTypeString("roomId:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=roomId_background_color_expected)
        validate_duration_text = MsgTypeString("duration:TMMI_MCR_TEXT_FIELD", value=duration_text_expected)
        validate_priority_text = MsgTypeString("priority:TMMI_MCR_TEXT_FIELD", value=priority_text_expected)
        validate_pendingAllocated_background_color = MsgTypeString("pendingAllocated:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=pendingAllocated_background_color_expected)
        validate_roomId_text = MsgTypeString("roomId:TMMI_MCR_TEXT_FIELD", value=roomId_text_expected)
        validate_duration_text = MsgTypeString("duration:TMMI_MCR_TEXT_FIELD", value=duration_text_expected)
        validate_priority_background_color = MsgTypeString("priority:TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR", value=priority_background_color_expected)
        validate_pendingAllocated_text = MsgTypeString("pendingAllocated:TMMI_MCR_TEXT_FIELD", value=pendingAllocated_text_expected)

        info_exchange = [
                        InformationSet("get mcr1_rejecttr1btn visibility", "thriver", "mcrhci", get_mcr1_rejecttr1btn_visibility),
                        #InformationSet("validate mcr1_rejecttr1btn visibility = " + str(mcr1_rejecttr1btn_visibility_expected), "mcrhci", "hcitracer", validate_mcr1_rejecttr1btn_visibility),
                         InformationSet("get mcr1_accepttr1btn visibility", "thriver", "mcrhci", get_mcr1_accepttr1btn_visibility),
                        # InformationSet("validate mcr1_accepttr1btn visibility = " + str(mcr1_accepttr1btn_visibility_expected), "mcrhci", "hcitracer", validate_mcr1_accepttr1btn_visibility),
                        # InformationSet("set tr2_allocation_status = "+ str(tr2_allocation_status_init_1), "thriver", "mcrhci", set_tr2_allocation_status_1),
                        # #InformationSet("get mcr1_beamrequest_tr2 background_color", "thriver", "mcrhci", get_mcr1_beamrequest_tr2_background_color),
                        # #InformationSet("validate mcr1_beamrequest_tr2 background_color = " + str(mcr1_beamrequest_tr2_background_color_expected), "mcrhci", "hcitracer", validate_mcr1_beamrequest_tr2_background_color),
                         InformationSet("get mcr1_rejecttr2btn visibility", "thriver", "mcrhci", get_mcr1_rejecttr2btn_visibility),
                        # InformationSet("validate mcr1_rejecttr2btn visibility = " + str(mcr1_rejecttr2btn_visibility_expected), "mcrhci", "hcitracer", validate_mcr1_rejecttr2btn_visibility),
                         InformationSet("get mcr1_accepttr2btn visibility", "thriver", "mcrhci", get_mcr1_accepttr2btn_visibility),
                        # InformationSet("validate mcr1_accepttr2btn visibility = " + str(mcr1_accepttr2btn_visibility_expected), "mcrhci", "hcitracer", validate_mcr1_accepttr2btn_visibility),
                        # InformationSet("set tr2_accept_led = "+ str(tr2_accept_led_init_1), "thriver", "mcrhci", set_tr2_accept_led_1),
                        # #InformationSet("get mcr1_accepttr2_led background_color", "thriver", "mcrhci", get_mcr1_accepttr2_led_background_color),
                        # #InformationSet("validate mcr1_accepttr2_led background_color = " + str(mcr1_accepttr2_led_background_color_expected), "mcrhci", "hcitracer", validate_mcr1_accepttr2_led_background_color),
                        # InformationSet("set tr3_allocation_status = "+ str(tr3_allocation_status_init_1), "thriver", "mcrhci", set_tr3_allocation_status_1),
                        # #InformationSet("get mcr1_beamrequest_tr3 background_color", "thriver", "mcrhci", get_mcr1_beamrequest_tr3_background_color),
                        # #InformationSet("validate mcr1_beamrequest_tr3 background_color = " + str(mcr1_beamrequest_tr3_background_color_expected), "mcrhci", "hcitracer", validate_mcr1_beamrequest_tr3_background_color),
                         InformationSet("get mcr1_rejecttr3btn visibility", "thriver", "mcrhci", get_mcr1_rejecttr3btn_visibility),
                        # InformationSet("validate mcr1_rejecttr3btn visibility = " + str(mcr1_rejecttr3btn_visibility_expected), "mcrhci", "hcitracer", validate_mcr1_rejecttr3btn_visibility),
                         InformationSet("get mcr1_accepttr3btn visibility", "thriver", "mcrhci", get_mcr1_accepttr3btn_visibility),
                        # InformationSet("validate mcr1_accepttr3btn visibility = " + str(mcr1_accepttr3btn_visibility_expected), "mcrhci", "hcitracer", validate_mcr1_accepttr3btn_visibility),
                        # InformationSet("set tr3_accept_led = "+ str(tr3_accept_led_init_1), "thriver", "mcrhci", set_tr3_accept_led_1),
                        # #InformationSet("get mcr1_accepttr3_led background_color", "thriver", "mcrhci", get_mcr1_accepttr3_led_background_color),
                        # #InformationSet("validate mcr1_accepttr3_led background_color = " + str(mcr1_accepttr3_led_background_color_expected), "mcrhci", "hcitracer", validate_mcr1_accepttr3_led_background_color),
                        # InformationSet("set tr3_reject_led = "+ str(tr3_reject_led_init_1), "thriver", "mcrhci", set_tr3_reject_led_1),
                        # #InformationSet("get mcr1_rejecttr3_led background_color", "thriver", "mcrhci", get_mcr1_rejecttr3_led_background_color),
                        # #InformationSet("validate mcr1_rejecttr3_led background_color = " + str(mcr1_rejecttr3_led_background_color_expected), "mcrhci", "hcitracer", validate_mcr1_rejecttr3_led_background_color),
                        # InformationSet("set tr4_allocation_status = "+ str(tr4_allocation_status_init_1), "thriver", "mcrhci", set_tr4_allocation_status_1),
                        # #InformationSet("get mcr1_beamrequest_tr3b background_color", "thriver", "mcrhci", get_mcr1_beamrequest_tr3b_background_color),
                        # #InformationSet("validate mcr1_beamrequest_tr3b background_color = " + str(mcr1_beamrequest_tr3b_background_color_expected), "mcrhci", "hcitracer", validate_mcr1_beamrequest_tr3b_background_color),
                         InformationSet("get mcr1_releasetr3bbtn visibility", "thriver", "mcrhci", get_mcr1_releasetr3bbtn_visibility),
                        # InformationSet("validate mcr1_releasetr3bbtn visibility = " + str(mcr1_releasetr3bbtn_visibility_expected), "mcrhci", "hcitracer", validate_mcr1_releasetr3bbtn_visibility),
                         InformationSet("get mcr1_allocatetr3bbtn visibility", "thriver", "mcrhci", get_mcr1_allocatetr3bbtn_visibility),
                        # InformationSet("validate mcr1_allocatetr3bbtn visibility = " + str(mcr1_allocatetr3bbtn_visibility_expected), "mcrhci", "hcitracer", validate_mcr1_allocatetr3bbtn_visibility),
                        # InformationSet("set tr4_accept_led = "+ str(tr4_accept_led_init_1), "thriver", "mcrhci", set_tr4_accept_led_1),
                        # #InformationSet("get mcr1_releasetr3b_led background_color", "thriver", "mcrhci", get_mcr1_releasetr3b_led_background_color),
                        # #InformationSet("validate mcr1_releasetr3b_led background_color = " + str(mcr1_releasetr3b_led_background_color_expected), "mcrhci", "hcitracer", validate_mcr1_releasetr3b_led_background_color),
                        # InformationSet("set tr4_reject_led = "+ str(tr4_reject_led_init_1), "thriver", "mcrhci", set_tr4_reject_led_1),
                        # #InformationSet("get mcr1_allocatetr3b_led background_color", "thriver", "mcrhci", get_mcr1_allocatetr3b_led_background_color),
                        # #InformationSet("validate mcr1_allocatetr3b_led background_color = " + str(mcr1_allocatetr3b_led_background_color_expected), "mcrhci", "hcitracer", validate_mcr1_allocatetr3b_led_background_color),
                        # InformationSet("set tr5_allocation_status = "+ str(tr5_allocation_status_init_1), "thriver", "mcrhci", set_tr5_allocation_status_1),
                        # #InformationSet("get mcr1_beamrequest_tr3c background_color", "thriver", "mcrhci", get_mcr1_beamrequest_tr3c_background_color),
                        # #InformationSet("validate mcr1_beamrequest_tr3c background_color = " + str(mcr1_beamrequest_tr3c_background_color_expected), "mcrhci", "hcitracer", validate_mcr1_beamrequest_tr3c_background_color),
                         InformationSet("get mcr1_releasemcrbtn visibility", "thriver", "mcrhci", get_mcr1_releasemcrbtn_visibility),
                        # InformationSet("validate mcr1_releasemcrbtn visibility = " + str(mcr1_releasemcrbtn_visibility_expected), "mcrhci", "hcitracer", validate_mcr1_releasemcrbtn_visibility),
                         InformationSet("get mcr1_allocatemcrbtn visibility", "thriver", "mcrhci", get_mcr1_allocatemcrbtn_visibility),
                        # InformationSet("validate mcr1_allocatemcrbtn visibility = " + str(mcr1_allocatemcrbtn_visibility_expected), "mcrhci", "hcitracer", validate_mcr1_allocatemcrbtn_visibility),
                        # InformationSet("set tr5_accept_led = "+ str(tr5_accept_led_init_1), "thriver", "mcrhci", set_tr5_accept_led_1),
                        # #InformationSet("get mcr1_releasemcr_led background_color", "thriver", "mcrhci", get_mcr1_releasemcr_led_background_color),
                        # #InformationSet("validate mcr1_releasemcr_led background_color = " + str(mcr1_releasemcr_led_background_color_expected), "mcrhci", "hcitracer", validate_mcr1_releasemcr_led_background_color),
                        # InformationSet("set tr5_reject_led = "+ str(tr5_reject_led_init_1), "thriver", "mcrhci", set_tr5_reject_led_1),
                        # #InformationSet("get mcr1_allocatemcr_led background_color", "thriver", "mcrhci", get_mcr1_allocatemcr_led_background_color),
                        # #InformationSet("validate mcr1_allocatemcr_led background_color = " + str(mcr1_allocatemcr_led_background_color_expected), "mcrhci", "hcitracer", validate_mcr1_allocatemcr_led_background_color),
                        # InformationSet("set mcr_allocation_status = "+ str(mcr_allocation_status_init_1), "thriver", "mcrhci", set_mcr_allocation_status_1),
                        # #InformationSet("get mcr1_beamrequest_mcr background_color", "thriver", "mcrhci", get_mcr1_beamrequest_mcr_background_color),
                        # #InformationSet("validate mcr1_beamrequest_mcr background_color = " + str(mcr1_beamrequest_mcr_background_color_expected), "mcrhci", "hcitracer", validate_mcr1_beamrequest_mcr_background_color),
                         InformationSet("get mcr1_releasetr3bbtn visibility", "thriver", "mcrhci", get_mcr1_releasetr3bbtn_visibility),
                        # InformationSet("validate mcr1_releasetr3bbtn visibility = " + str(mcr1_releasetr3bbtn_visibility_expected), "mcrhci", "hcitracer", validate_mcr1_releasetr3bbtn_visibility),
                         InformationSet("get mcr1_allocatetr3bbtn visibility", "thriver", "mcrhci", get_mcr1_allocatetr3bbtn_visibility),
                        # InformationSet("validate mcr1_allocatetr3bbtn visibility = " + str(mcr1_allocatetr3bbtn_visibility_expected), "mcrhci", "hcitracer", validate_mcr1_allocatetr3bbtn_visibility),
                        # InformationSet("set mcr_reject_led = "+ str(mcr_reject_led_init_1), "thriver", "mcrhci", set_mcr_reject_led_1),
                        # #InformationSet("get mcr1_releasetr3b_led background_color", "thriver", "mcrhci", get_mcr1_releasetr3b_led_background_color),
                        # #InformationSet("validate mcr1_releasetr3b_led background_color = " + str(mcr1_releasetr3b_led_background_color_expected), "mcrhci", "hcitracer", validate_mcr1_releasetr3b_led_background_color),
                        # InformationSet("set mcr_accept_led = "+ str(mcr_accept_led_init_1), "thriver", "mcrhci", set_mcr_accept_led_1),
                        # #InformationSet("get mcr_allocatetr3b_led background_color", "thriver", "mcrhci", get_mcr_allocatetr3b_led_background_color),
                        # #InformationSet("validate mcr_allocatetr3b_led background_color = " + str(mcr_allocatetr3b_led_background_color_expected), "mcrhci", "hcitracer", validate_mcr_allocatetr3b_led_background_color),
                        # InformationSet("set mcr_abo_sw_progress = "+ str(mcr_abo_sw_progress_init_1), "thriver", "mcrhci", set_mcr_abo_sw_progress_1),
                        # #InformationSet("get mcr1_progress2_led background_color", "thriver", "mcrhci", get_mcr1_progress2_led_background_color),
                        # #InformationSet("validate mcr1_progress2_led background_color = " + str(mcr1_progress2_led_background_color_expected), "mcrhci", "hcitracer", validate_mcr1_progress2_led_background_color),
                        # InformationSet("set mcr_abo_sw_progress = "+ str(mcr_abo_sw_progress_init_2), "thriver", "mcrhci", set_mcr_abo_sw_progress_2),
                        # #InformationSet("get mcr1_progress3_led background_color", "thriver", "mcrhci", get_mcr1_progress3_led_background_color),
                        # #InformationSet("validate mcr1_progress3_led background_color = " + str(mcr1_progress3_led_background_color_expected), "mcrhci", "hcitracer", validate_mcr1_progress3_led_background_color),
                        # InformationSet("set mcr_abo_sw_progress = "+ str(mcr_abo_sw_progress_init_3), "thriver", "mcrhci", set_mcr_abo_sw_progress_3),
                        # #InformationSet("get mcr1_progress4_led background_color", "thriver", "mcrhci", get_mcr1_progress4_led_background_color),
                        # #InformationSet("validate mcr1_progress4_led background_color = " + str(mcr1_progress4_led_background_color_expected), "mcrhci", "hcitracer", validate_mcr1_progress4_led_background_color),
                        # InformationSet("set mcr_abo_sw_progress = "+ str(mcr_abo_sw_progress_init_4), "thriver", "mcrhci", set_mcr_abo_sw_progress_4),
                        # #InformationSet("get mcr1_progress5_led background_color", "thriver", "mcrhci", get_mcr1_progress5_led_background_color),
                        # #InformationSet("validate mcr1_progress5_led background_color = " + str(mcr1_progress5_led_background_color_expected), "mcrhci", "hcitracer", validate_mcr1_progress5_led_background_color),
                        # InformationSet("set mcr_abo_sw_progress = "+ str(mcr_abo_sw_progress_init_5), "thriver", "mcrhci", set_mcr_abo_sw_progress_5),
                        # #InformationSet("get mcr1_progress6_led background_color", "thriver", "mcrhci", get_mcr1_progress6_led_background_color),
                        # #InformationSet("validate mcr1_progress6_led background_color = " + str(mcr1_progress6_led_background_color_expected), "mcrhci", "hcitracer", validate_mcr1_progress6_led_background_color),
                        # InformationSet("set mcr_abo_sw_progress = "+ str(mcr_abo_sw_progress_init_6), "thriver", "mcrhci", set_mcr_abo_sw_progress_6),
                        # #InformationSet("get mcr1_progress7_led background_color", "thriver", "mcrhci", get_mcr1_progress7_led_background_color),
                        # #InformationSet("validate mcr1_progress7_led background_color = " + str(mcr1_progress7_led_background_color_expected), "mcrhci", "hcitracer", validate_mcr1_progress7_led_background_color),
                        # InformationSet("set mcr_abo_sw_progress = "+ str(mcr_abo_sw_progress_init_7), "thriver", "mcrhci", set_mcr_abo_sw_progress_7),
                        # #InformationSet("get mcr1_progress8_led background_color", "thriver", "mcrhci", get_mcr1_progress8_led_background_color),
                        # #InformationSet("validate mcr1_progress8_led background_color = " + str(mcr1_progress8_led_background_color_expected), "mcrhci", "hcitracer", validate_mcr1_progress8_led_background_color),
                        # InformationSet("set mcr_beammgr_sw_beamallocatedtotr = "+ str(mcr_beammgr_sw_beamallocatedtotr_init_1), "thriver", "mcrhci", set_mcr_beammgr_sw_beamallocatedtotr_1),
                        # #InformationSet("get mcr1_beamon_tr1 background_color", "thriver", "mcrhci", get_mcr1_beamon_tr1_background_color),
                        # #InformationSet("validate mcr1_beamon_tr1 background_color = " + str(mcr1_beamon_tr1_background_color_expected), "mcrhci", "hcitracer", validate_mcr1_beamon_tr1_background_color),
                        # InformationSet("set mcr_beammgr_sw_beamallocatedtotr = "+ str(mcr_beammgr_sw_beamallocatedtotr_init_2), "thriver", "mcrhci", set_mcr_beammgr_sw_beamallocatedtotr_2),
                        # #InformationSet("get mcr1_beamon_tr2 background_color", "thriver", "mcrhci", get_mcr1_beamon_tr2_background_color),
                        # #InformationSet("validate mcr1_beamon_tr2 background_color = " + str(mcr1_beamon_tr2_background_color_expected), "mcrhci", "hcitracer", validate_mcr1_beamon_tr2_background_color),
                        # InformationSet("set mcr_beammgr_sw_beamallocatedtotr = "+ str(mcr_beammgr_sw_beamallocatedtotr_init_3), "thriver", "mcrhci", set_mcr_beammgr_sw_beamallocatedtotr_3),
                        # #InformationSet("get mcr1_beamon_tr3a background_color", "thriver", "mcrhci", get_mcr1_beamon_tr3a_background_color),
                        # #InformationSet("validate mcr1_beamon_tr3a background_color = " + str(mcr1_beamon_tr3a_background_color_expected), "mcrhci", "hcitracer", validate_mcr1_beamon_tr3a_background_color),
                        # InformationSet("set mcr_beammgr_sw_beamallocatedtotr = "+ str(mcr_beammgr_sw_beamallocatedtotr_init_4), "thriver", "mcrhci", set_mcr_beammgr_sw_beamallocatedtotr_4),
                        # #InformationSet("get mcr1_beamon_tr3b background_color", "thriver", "mcrhci", get_mcr1_beamon_tr3b_background_color),
                        # #InformationSet("validate mcr1_beamon_tr3b background_color = " + str(mcr1_beamon_tr3b_background_color_expected), "mcrhci", "hcitracer", validate_mcr1_beamon_tr3b_background_color),
                         InformationSet("get mcr1_beamprepdonebtn visibility", "thriver", "mcrhci", get_mcr1_beamprepdonebtn_visibility),
                        # InformationSet("validate mcr1_beamprepdonebtn visibility = " + str(mcr1_beamprepdonebtn_visibility_expected), "mcrhci", "hcitracer", validate_mcr1_beamprepdonebtn_visibility),
                        # InformationSet("set mcr_bc_beamprep_done_led = "+ str(mcr_bc_beamprep_done_led_init_1), "thriver", "mcrhci", set_mcr_bc_beamprep_done_led_1),
                        # #InformationSet("get mcr1_beamprepdone_led background_color", "thriver", "mcrhci", get_mcr1_beamprepdone_led_background_color),
                        # #InformationSet("validate mcr1_beamprepdone_led background_color = " + str(mcr1_beamprepdone_led_background_color_expected), "mcrhci", "hcitracer", validate_mcr1_beamprepdone_led_background_color),
                         InformationSet("get mcr1_beamprepabortbtn visibility", "thriver", "mcrhci", get_mcr1_beamprepabortbtn_visibility),
                        # InformationSet("validate mcr1_beamprepabortbtn visibility = " + str(mcr1_beamprepabortbtn_visibility_expected), "mcrhci", "hcitracer", validate_mcr1_beamprepabortbtn_visibility),
                        # InformationSet("set mcr_bc_beamprep_abort_led = "+ str(mcr_bc_beamprep_abort_led_init_1), "thriver", "mcrhci", set_mcr_bc_beamprep_abort_led_1),
                        # #InformationSet("get mcr1_beamprepabort_led background_color", "thriver", "mcrhci", get_mcr1_beamprepabort_led_background_color),
                        # #InformationSet("validate mcr1_beamprepabort_led background_color = " + str(mcr1_beamprepabort_led_background_color_expected), "mcrhci", "hcitracer", validate_mcr1_beamprepabort_led_background_color),
                        # InformationSet("set allocatedRoomId = "+ str(allocatedRoomId_init_1), "thriver", "mcrhci", set_allocatedRoomId_1),
                        # InformationSet("get Room Allocated text", "thriver", "mcrhci", get_Room_Allocated_text),
                        # InformationSet("validate Room Allocated text = " + str(Room_Allocated_text_expected), "mcrhci", "hcitracer", validate_Room_Allocated_text),
                        # InformationSet("set allocationPriority = "+ str(allocationPriority_init_1), "thriver", "mcrhci", set_allocationPriority_1),
                        # InformationSet("get Priority text", "thriver", "mcrhci", get_Priority_text),
                        # InformationSet("validate Priority text = " + str(Priority_text_expected), "mcrhci", "hcitracer", validate_Priority_text),
                        # InformationSet("set pending1_roomId = "+ str(pending1_roomId_init_1), "thriver", "mcrhci", set_pending1_roomId_1),
                        # #InformationSet("get roomId background_color", "thriver", "mcrhci", get_roomId_background_color),
                        # #InformationSet("validate roomId background_color = " + str(roomId_background_color_expected), "mcrhci", "hcitracer", validate_roomId_background_color),
                        # InformationSet("set pending1_wait = "+ str(pending1_wait_init_1), "thriver", "mcrhci", set_pending1_wait_1),
                        # InformationSet("get duration text", "thriver", "mcrhci", get_duration_text),
                        # InformationSet("validate duration text = " + str(duration_text_expected), "mcrhci", "hcitracer", validate_duration_text),
                        # InformationSet("set pending1_priority = "+ str(pending1_priority_init_1), "thriver", "mcrhci", set_pending1_priority_1),
                        # InformationSet("get priority text", "thriver", "mcrhci", get_priority_text),
                        # InformationSet("validate priority text = " + str(priority_text_expected), "mcrhci", "hcitracer", validate_priority_text),
                        # InformationSet("set pending1_status = "+ str(pending1_status_init_1), "thriver", "mcrhci", set_pending1_status_1),
                        # #InformationSet("get pendingAllocated background_color", "thriver", "mcrhci", get_pendingAllocated_background_color),
                        # #InformationSet("validate pendingAllocated background_color = " + str(pendingAllocated_background_color_expected), "mcrhci", "hcitracer", validate_pendingAllocated_background_color),
                        # InformationSet("set pending2_roomId = "+ str(pending2_roomId_init_1), "thriver", "mcrhci", set_pending2_roomId_1),
                        # InformationSet("get roomId text", "thriver", "mcrhci", get_roomId_text),
                        # InformationSet("validate roomId text = " + str(roomId_text_expected), "mcrhci", "hcitracer", validate_roomId_text),
                        # InformationSet("set pending2_wait = "+ str(pending2_wait_init_1), "thriver", "mcrhci", set_pending2_wait_1),
                        # InformationSet("get duration text", "thriver", "mcrhci", get_duration_text),
                        # InformationSet("validate duration text = " + str(duration_text_expected), "mcrhci", "hcitracer", validate_duration_text),
                        # InformationSet("set pending2_priority = "+ str(pending2_priority_init_1), "thriver", "mcrhci", set_pending2_priority_1),
                        # #InformationSet("get priority background_color", "thriver", "mcrhci", get_priority_background_color),
                        # #InformationSet("validate priority background_color = " + str(priority_background_color_expected), "mcrhci", "hcitracer", validate_priority_background_color),
                        # InformationSet("set pending2_status = "+ str(pending2_status_init_1), "thriver", "mcrhci", set_pending2_status_1),
                        # InformationSet("get pendingAllocated text", "thriver", "mcrhci", get_pendingAllocated_text),
                        # InformationSet("validate pendingAllocated text = " + str(pendingAllocated_text_expected), "mcrhci", "hcitracer", validate_pendingAllocated_text),
                        # InformationSet("set pending3_roomId = "+ str(pending3_roomId_init_1), "thriver", "mcrhci", set_pending3_roomId_1),
                        # InformationSet("get roomId text", "thriver", "mcrhci", get_roomId_text),
                        # InformationSet("validate roomId text = " + str(roomId_text_expected), "mcrhci", "hcitracer", validate_roomId_text),
                        # InformationSet("set pending3_wait = "+ str(pending3_wait_init_1), "thriver", "mcrhci", set_pending3_wait_1),
                        # #InformationSet("get duration background_color", "thriver", "mcrhci", get_duration_background_color),
                        # #InformationSet("validate duration background_color = " + str(duration_background_color_expected), "mcrhci", "hcitracer", validate_duration_background_color),
                        # InformationSet("set pending3_priority = "+ str(pending3_priority_init_1), "thriver", "mcrhci", set_pending3_priority_1),
                        # InformationSet("get priority text", "thriver", "mcrhci", get_priority_text),
                        # InformationSet("validate priority text = " + str(priority_text_expected), "mcrhci", "hcitracer", validate_priority_text),
                        # InformationSet("set pending3_status = "+ str(pending3_status_init_1), "thriver", "mcrhci", set_pending3_status_1),
                        # InformationSet("get pendingAllocated text", "thriver", "mcrhci", get_pendingAllocated_text),
                        # InformationSet("validate pendingAllocated text = " + str(pendingAllocated_text_expected), "mcrhci", "hcitracer", validate_pendingAllocated_text),
                        # InformationSet("set pending4_roomId = "+ str(pending4_roomId_init_1), "thriver", "mcrhci", set_pending4_roomId_1),
                        # #InformationSet("get roomId background_color", "thriver", "mcrhci", get_roomId_background_color),
                        # #InformationSet("validate roomId background_color = " + str(roomId_background_color_expected), "mcrhci", "hcitracer", validate_roomId_background_color),
                        # InformationSet("set pending4_wait = "+ str(pending4_wait_init_1), "thriver", "mcrhci", set_pending4_wait_1),
                        # InformationSet("get duration text", "thriver", "mcrhci", get_duration_text),
                        # InformationSet("validate duration text = " + str(duration_text_expected), "mcrhci", "hcitracer", validate_duration_text),
                        # InformationSet("set pending4_priority = "+ str(pending4_priority_init_1), "thriver", "mcrhci", set_pending4_priority_1),
                        # InformationSet("get priority text", "thriver", "mcrhci", get_priority_text),
                        # InformationSet("validate priority text = " + str(priority_text_expected), "mcrhci", "hcitracer", validate_priority_text),
                        # InformationSet("set pending4_status = "+ str(pending4_status_init_1), "thriver", "mcrhci", set_pending4_status_1),
                        # #InformationSet("get pendingAllocated background_color", "thriver", "mcrhci", get_pendingAllocated_background_color),
                        # #InformationSet("validate pendingAllocated background_color = " + str(pendingAllocated_background_color_expected), "mcrhci", "hcitracer", validate_pendingAllocated_background_color),
                        # InformationSet("set pending5_roomId = "+ str(pending5_roomId_init_1), "thriver", "mcrhci", set_pending5_roomId_1),
                        # InformationSet("get roomId text", "thriver", "mcrhci", get_roomId_text),
                        # InformationSet("validate roomId text = " + str(roomId_text_expected), "mcrhci", "hcitracer", validate_roomId_text),
                        # InformationSet("set pending5_wait = "+ str(pending5_wait_init_1), "thriver", "mcrhci", set_pending5_wait_1),
                        # InformationSet("get duration text", "thriver", "mcrhci", get_duration_text),
                        # InformationSet("validate duration text = " + str(duration_text_expected), "mcrhci", "hcitracer", validate_duration_text),
                        # InformationSet("set pending5_priority = "+ str(pending5_priority_init_1), "thriver", "mcrhci", set_pending5_priority_1),
                        # #InformationSet("get priority background_color", "thriver", "mcrhci", get_priority_background_color),
                        # #InformationSet("validate priority background_color = " + str(priority_background_color_expected), "mcrhci", "hcitracer", validate_priority_background_color),
                        # InformationSet("set pending5_status = "+ str(pending5_status_init_1), "thriver", "mcrhci", set_pending5_status_1),
                        # InformationSet("get pendingAllocated text", "thriver", "mcrhci", get_pendingAllocated_text),
                        # InformationSet("validate pendingAllocated text = " + str(pendingAllocated_text_expected), "mcrhci", "hcitracer", validate_pendingAllocated_text),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_CLICK_BEAM_CONTROL(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Click on Beam control"
        # Point to Treatment Beam Control screen location
        msg_location_Treatment_Beam_Control_View = MsgHciButtonPositionEvent(9, [[100, 520]])
        #Declare list of Informationset using above tcsobject
        info_exchange = [                      
                        InformationSet("Load screen Treatment_Beam_Control", "thriver", "mcrhci", msg_location_Treatment_Beam_Control_View),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []       