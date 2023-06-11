
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

class SETUP_SELECT_SERVICE_SESSION(ClinicalIntegrationTestProcedure):
    name = "Click service session button"
    def __init__(self, test):
        cls = type(self)
        name = cls.name
            
        sms_1 = MsgHciButtonNameEvent(0, [["SCR_SELECT_SESSION:serviceBtn"]])
        
        info_exchange = [
                        InformationSet("Click service session button", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_SELECT_TREATMENT_SESSION(ClinicalIntegrationTestProcedure):
    name = "Click treatment session button"
    def __init__(self, test):
        cls = type(self)
        name = cls.name
            
        sms_1 = MsgHciButtonNameEvent(0, [["SCR_SELECT_SESSION:treatmentBtn"]])
        
        info_exchange = [
                        InformationSet("Click treatment session button", "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []