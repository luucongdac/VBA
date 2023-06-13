
"""
File:
======================================

This module implements set up path for mcrhci test

Copyright (c) MGH 2023

Test for setup ClinicalIntegrationTestProcedure

"""



from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.infoset.tcsobject.dba_objects import *

class SETUP_VALIDATE_SERVICE_BTS2_MENU(ClinicalIntegrationTestProcedure):
    name = "Confirm that MCR_Service_BTS2Menu (mcr_service_bts2menu.v) is displayed"
    def __init__(self, test):
        cls = type(self)
        name = cls.name
        
        #get value
        get_mcr_service_bts2menu_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_service_bts2menu")

        #validate
        validate_mcr_service_bts2menu_visibility = MsgTypeString(variable="mcr_service_bts2menu:TMMI_MCR_IS_VISIBLE", value="1")

        info_exchange = [
                        InformationSet("get mcr_service_bts2menu visibility", "thriver", "mcrhci", get_mcr_service_bts2menu_visibility),
                        InformationSet("validate mcr_service_bts2menu visibility = 1", "mcrhci", "hcitracer", validate_mcr_service_bts2menu_visibility),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_NAVIGATE_TO_PTS_LAYOUT_SCREEN_FROM_SERVICE_BTS2_MENU(ClinicalIntegrationTestProcedure):
    name = "Navigate to PTS_Layout screen"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonPositionEvent(9, [[ 99, 215 ]])    

        info_exchange = [
                        InformationSet("Click to Plainview button on the menu", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []
