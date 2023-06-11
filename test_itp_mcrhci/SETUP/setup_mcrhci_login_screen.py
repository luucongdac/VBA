
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

class SETUP_INPUT_USERNAME(ClinicalIntegrationTestProcedure):
    # default variable values
    name = "Enter username"
    username = "tcsadmin"

    def __init__(self, test):
        cls = type(self)
        name = cls.name
        username = cls.username

        sms_1 = MsgHciInputNameEvent(0, [["SCR_USER_LOGIN:nameTxtF", username]])

        info_exchange = [
                        InformationSet("Enter user name", "thriver", "mcrhci", sms_1),  
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_INPUT_PASSWORD(ClinicalIntegrationTestProcedure):
    # default variable values
    name = "Enter password"
    password = "patient01"

    def __init__(self, test):
        cls = type(self)
        name = cls.name
        password = cls.password

        sms_1 = MsgHciInputNameEvent(0, [["SCR_USER_LOGIN:passwdTxtF", password]])        

        info_exchange = [
                        InformationSet("Enter password", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_CLICK_OK_LOGIN_BUTTON(ClinicalIntegrationTestProcedure):
    name = "Click on OK button in login screen"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        sms_1 = MsgHciButtonNameEvent(0, [["SCR_USER_LOGIN:okBtn"]])     

        info_exchange = [
                        InformationSet("Click OK button", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []
