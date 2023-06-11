
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

class SETUP_VALIDATE_SERVICE_ESS_MENU(ClinicalIntegrationTestProcedure):
    name = "Validate that MCR Service ESS Menu is showed"
    def __init__(self, test):
        cls = type(self)
        name = cls.name
        
        #get value
        get_mcr_service_essmenu_visibility= MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "mcr_service_essmenu")

        #validate
        validate_mcr_service_essmenu_visibility = MsgTypeString(variable="mcr_service_essmenu:TMMI_MCR_IS_VISIBLE", value="1")

        info_exchange = [
                        InformationSet("get mcr_service_essmenu visibility", "thriver", "mcrhci", get_mcr_service_essmenu_visibility),
                        InformationSet("validate mcr_service_essmenu visibility = 1", "mcrhci", "hcitracer", validate_mcr_service_essmenu_visibility),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_NAVIGATE_TO_PTS_LAYOUT_SCREEN_FROM_SERVICE_ESS_MENU(ClinicalIntegrationTestProcedure):
    name = "Navigate to PTS_Layout screen"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonPositionEvent(9, [[100, 160]])    

        info_exchange = [
                        InformationSet("Click to Plainview button on the menu", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_CLICK_TO_GAUSSIAN_PIT_BUTTON_ON_SERVICE_ESS_MENU(ClinicalIntegrationTestProcedure):
    name = "Click to Gaussian Pit on Ess Menu"
    def __init__(self, test):   
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonPositionEvent(9, [[100, 650]])    

        info_exchange = [
                        InformationSet("Click to Gaussian Pit on Ess Menu", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []
        
class SETUP_OPEN_BEAM_TUNING_SCREEN(ClinicalIntegrationTestProcedure):
    name = "Navigate to Beam_Tuning screen"    
    def __init__(self, test):
        cls = type(self)
        name = cls.name                
        # Point to Beam tuning screen location
        msg_location_BeamTuningView = MsgHciButtonPositionEvent(9, [[100, 670]])
        
        info_exchange = [                      
                        InformationSet("Load screen 'beam_tuning.v", "thriver", "mcrhci", msg_location_BeamTuningView),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []        
