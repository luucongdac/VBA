
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

class SETUP_VALIDATE_POP_UP_CONTENT(ClinicalIntegrationTestProcedure):
    # default variable value
    name = "Validate the content of the popup"
    content_popup = None
    screen_popup = None
    def __init__(self, test):
        cls = type(self)
        name = cls.name
        content_popup = self.content_popup
        screen_popup = self.screen_popup
        
        sms_1 = MsgHciInfo(content_popup, 21, 31, 31, screen_popup)

        info_exchange = [
                        InformationSet("validate pop up with content: {content_popup}, at screen: {screen_popup}".format(content_popup=content_popup, screen_popup=screen_popup), "tcrtrmgr", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_CLICK_OK_POPUP(ClinicalIntegrationTestProcedure):
    # default variable value
    name = "Click OK button on the popup"
    def __init__(self, test):
        cls = type(self)
        name = cls.name
        
        # message pop up: OK button
        sms_1 = MsgHciButtonNameEvent(0, [["msg_dialog:OK"]])

        info_exchange = [
                        InformationSet("Click OK button on the Pop-Up", "thriver", "mcrhci", sms_1),  
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []        