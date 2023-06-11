from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import *

class SETUP_VALIDATE_OPEN_LOADCELL_GRAPH_1(ClinicalIntegrationTestProcedure):
    name = "Validate open Loadcell Graph 1 screen"
    visible = "1"
    invisible = "0"

    pcu_room1_lc_menuvar1_visible_expected = visible
    pcu_room1_lc_menuvar2_visible_expected = visible
    pcu_room1_lc_menuvar3_visible_expected = visible
    pcu_room1_lc_menuvar4_visible_expected = visible
    pcu_room1_lc_menuvar5_visible_expected = visible
    pcu_room1_lc_menuvar6_visible_expected = visible
    pcu10_printbtn_visible_expected        = visible
    pcu10_setDSbtn_visible_expected        = visible

    def __init__(self, test):
        cls = type(self)

        name = cls.name
        pcu_room1_lc_menuvar1_visible_expected = cls.pcu_room1_lc_menuvar1_visible_expected
        pcu_room1_lc_menuvar2_visible_expected = cls.pcu_room1_lc_menuvar2_visible_expected
        pcu_room1_lc_menuvar3_visible_expected = cls.pcu_room1_lc_menuvar3_visible_expected
        pcu_room1_lc_menuvar4_visible_expected = cls.pcu_room1_lc_menuvar4_visible_expected
        pcu_room1_lc_menuvar5_visible_expected = cls.pcu_room1_lc_menuvar5_visible_expected
        pcu_room1_lc_menuvar6_visible_expected = cls.pcu_room1_lc_menuvar6_visible_expected
        pcu10_printbtn_visible_expected        = cls.pcu10_printbtn_visible_expected
        pcu10_setDSbtn_visible_expected        = cls.pcu10_setDSbtn_visible_expected

        get_pcu_room1_lc_menuvar1_visible = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "pcu_room1_lc_menuvar1")
        get_pcu_room1_lc_menuvar2_visible = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "pcu_room1_lc_menuvar2")
        get_pcu_room1_lc_menuvar3_visible = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "pcu_room1_lc_menuvar3")
        get_pcu_room1_lc_menuvar4_visible = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "pcu_room1_lc_menuvar4")
        get_pcu_room1_lc_menuvar5_visible = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "pcu_room1_lc_menuvar5")
        get_pcu_room1_lc_menuvar6_visible = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "pcu_room1_lc_menuvar6")
        get_pcu10_printbtn_visible        = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "pcu10_printbtn")
        get_pcu10_setDSbtn_visible        = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "pcu10_setDSbtn")

        validate_pcu_room1_lc_menuvar1_visible = MsgTypeString("pcu_room1_lc_menuvar1:TMMI_MCR_IS_VISIBLE", value=pcu_room1_lc_menuvar1_visible_expected)
        validate_pcu_room1_lc_menuvar2_visible = MsgTypeString("pcu_room1_lc_menuvar2:TMMI_MCR_IS_VISIBLE", value=pcu_room1_lc_menuvar2_visible_expected)
        validate_pcu_room1_lc_menuvar3_visible = MsgTypeString("pcu_room1_lc_menuvar3:TMMI_MCR_IS_VISIBLE", value=pcu_room1_lc_menuvar3_visible_expected)
        validate_pcu_room1_lc_menuvar4_visible = MsgTypeString("pcu_room1_lc_menuvar4:TMMI_MCR_IS_VISIBLE", value=pcu_room1_lc_menuvar4_visible_expected)
        validate_pcu_room1_lc_menuvar5_visible = MsgTypeString("pcu_room1_lc_menuvar5:TMMI_MCR_IS_VISIBLE", value=pcu_room1_lc_menuvar5_visible_expected)
        validate_pcu_room1_lc_menuvar6_visible = MsgTypeString("pcu_room1_lc_menuvar6:TMMI_MCR_IS_VISIBLE", value=pcu_room1_lc_menuvar6_visible_expected)
        validate_pcu10_printbtn_visible        = MsgTypeString("pcu10_printbtn:TMMI_MCR_IS_VISIBLE",        value=pcu10_printbtn_visible_expected)
        validate_pcu10_setDSbtn_visible        = MsgTypeString("pcu10_setDSbtn:TMMI_MCR_IS_VISIBLE",        value=pcu10_setDSbtn_visible_expected)

        info_exchange = [
                        InformationSet("get_pcu_room1_lc_menuvar1_visible", "thriver", "mcrhci", get_pcu_room1_lc_menuvar1_visible),
                        InformationSet("validate_pcu_room1_lc_menuvar1_visible", "mcrhci", "hcitracer", validate_pcu_room1_lc_menuvar1_visible),

                        InformationSet("get_pcu_room1_lc_menuvar2_visible", "thriver", "mcrhci", get_pcu_room1_lc_menuvar2_visible),
                        InformationSet("validate_pcu_room1_lc_menuvar2_visible", "mcrhci", "hcitracer", validate_pcu_room1_lc_menuvar2_visible),

                        InformationSet("get_pcu_room1_lc_menuvar3_visible", "thriver", "mcrhci", get_pcu_room1_lc_menuvar3_visible),
                        InformationSet("validate_pcu_room1_lc_menuvar3_visible", "mcrhci", "hcitracer", validate_pcu_room1_lc_menuvar3_visible),

                        InformationSet("get_pcu_room1_lc_menuvar4_visible", "thriver", "mcrhci", get_pcu_room1_lc_menuvar4_visible),
                        InformationSet("validate_pcu_room1_lc_menuvar4_visible", "mcrhci", "hcitracer", validate_pcu_room1_lc_menuvar4_visible),

                        InformationSet("get_pcu_room1_lc_menuvar5_visible", "thriver", "mcrhci", get_pcu_room1_lc_menuvar5_visible),
                        InformationSet("validate_pcu_room1_lc_menuvar5_visible", "mcrhci", "hcitracer", validate_pcu_room1_lc_menuvar5_visible),

                        InformationSet("get_pcu_room1_lc_menuvar6_visible", "thriver", "mcrhci", get_pcu_room1_lc_menuvar6_visible),
                        InformationSet("validate_pcu_room1_lc_menuvar6_visible", "mcrhci", "hcitracer", validate_pcu_room1_lc_menuvar6_visible),

                        InformationSet("get_pcu10_printbtn_visible", "thriver", "mcrhci", get_pcu10_printbtn_visible),
                        InformationSet("validate_pcu10_printbtn_visible", "mcrhci", "hcitracer", validate_pcu10_printbtn_visible),

                        InformationSet("get_pcu10_setDSbtn_visible", "thriver", "mcrhci", get_pcu10_setDSbtn_visible),
                        InformationSet("validate_pcu10_setDSbtn_visible", "mcrhci", "hcitracer", validate_pcu10_setDSbtn_visible),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [  
                        ]
        self.teardown_path = []

class SETUP_CLICK_LOADCELL_FORCE_X_LOADCELL_GRAPH_1(SETUP_CLICK_BUTTON_BY_NAME):
    name = "Click Loadcell Force X checkbox in Loadcell Graph 1 screen according to its name"
    button_name = "mcr_treatment_pps_loadcell_graph1:pcu_room1_lc_menuvar1"

class SETUP_CLICK_LOADCELL_FORCE_Z_LOADCELL_GRAPH_1(SETUP_CLICK_BUTTON_BY_NAME):
    name = "Click Loadcell Force Z checkbox in Loadcell Graph 1 screen according to its name"
    button_name = "mcr_treatment_pps_loadcell_graph1:pcu_room1_lc_menuvar3"

class SETUP_CLICK_LOADCELL_TORQUE_X_LOADCELL_GRAPH_1(SETUP_CLICK_BUTTON_BY_NAME):
    name = "Click Loadcell Torque X checkbox in Loadcell Graph 1 screen according to its name"
    button_name = "mcr_treatment_pps_loadcell_graph1:pcu_room1_lc_menuvar4"

class SETUP_CLICK_LOADCELL_TORQUE_Y_LOADCELL_GRAPH_1(SETUP_CLICK_BUTTON_BY_NAME):
    name = "Click Loadcell Torque Y checkbox in Loadcell Graph 1 screen according to its name"
    button_name = "mcr_treatment_pps_loadcell_graph1:pcu_room1_lc_menuvar5"

class SETUP_CLICK_LOADCELL_TORQUE_Z_LOADCELL_GRAPH_1(SETUP_CLICK_BUTTON_BY_NAME):
    name = "Click Loadcell Torque Z checkbox in Loadcell Graph 1 screen according to its name"
    button_name = "mcr_treatment_pps_loadcell_graph1:pcu_room1_lc_menuvar6"

class SETUP_CLICK_PRINT_BUTTON_LOADCELL_GRAPH_1(SETUP_CLICK_BUTTON_BY_NAME):
    name = "Click Print button in Loadcell Graph 1 screen according to its name"
    button_name = "mcr_treatment_pps_loadcell_graph1:pcu10_printbtn"

class SETUP_CLICK_CANCEL_BUTTON_LOADCELL_GRAPH_1(SETUP_CLICK_BUTTON_BY_NAME):
    name = "Click Cancel button in Loadcell Graph 1 screen according to its name"
    button_name = "mcr_treatment_pps_loadcell_graph1:pcu10_setDSbtn"

class SETUP_UNCHECK_ALL_CHECKBOX_WHEN_INIT_LOADCELL_GRAPH_1(ClinicalIntegrationTestProcedure):
    name = "Uncheck all checkbox when init Loadcell Graph 1 screen"

    def __init__(self, test):
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonNameEvent(0,[["mcr_treatment_pps_loadcell_graph1:pcu_room1_lc_menuvar1"]])
        sms_2 = MsgHciButtonNameEvent(0,[["mcr_treatment_pps_loadcell_graph1:pcu_room1_lc_menuvar3"]])
        sms_3 = MsgHciButtonNameEvent(0,[["mcr_treatment_pps_loadcell_graph1:pcu_room1_lc_menuvar4"]])
        sms_4 = MsgHciButtonNameEvent(0,[["mcr_treatment_pps_loadcell_graph1:pcu_room1_lc_menuvar5"]])
        sms_5 = MsgHciButtonNameEvent(0,[["mcr_treatment_pps_loadcell_graph1:pcu_room1_lc_menuvar6"]])

        info_exchange = [ 
                        InformationSet("Click on Loadcell Force X checkbox", "thriver", "mcrhci", sms_1),
                        InformationSet("Click on Loadcell Force Z checkbox", "thriver", "mcrhci", sms_2),
                        InformationSet("Click on Loadcell Torque X checkbox", "thriver", "mcrhci", sms_3),
                        InformationSet("Click on Loadcell Torque X checkbox", "thriver", "mcrhci", sms_4),
                        InformationSet("Click on Loadcell Torque X checkbox", "thriver", "mcrhci", sms_5),
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []
