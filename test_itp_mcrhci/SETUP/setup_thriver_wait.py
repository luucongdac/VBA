
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

class SETUP_THRIVER_WAIT(ClinicalIntegrationTestProcedure):
    # default variable value
    time = 1
    def __init__(self, test):
        cls = type(self)
        name = cls.__name__
        time = cls.time
        
        sms_1 = MsgTypeNumeric("thriver_wait", time)

        info_exchange = [
                        InformationSet("Thriver wait", "thriver", "mcrhci", sms_1),  
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []