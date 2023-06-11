
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

class SETUP_CLICK_OK_BUTTON_MSG_DIALOG(ClinicalIntegrationTestProcedure):
    name = "Click OK button in the message dialog"
    def __init__(self, test):
        cls = type(self)
        name = cls.name

        msg_tmmi_1 = MsgHciButtonNameEvent(0, [["msg_dialog:OK"]])
        msgMasterKey = MsgTypeBoolean("mcr_scu.keyswitch.in", sysMgr.MASTER_KEY_SWITCH_ACTIVATED)

        info_exchange = [
                        InformationSet("Click OK button on msg dialog", "thriver", "mcrhci", msg_tmmi_1),
                        InformationSet("Enable master key", "scu", "sysmng", msgMasterKey),  
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []