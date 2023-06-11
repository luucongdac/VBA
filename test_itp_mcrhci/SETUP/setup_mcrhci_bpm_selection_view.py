
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

class SETUP_SELECT_AND_VALIDATE_CHECKBOX(ClinicalIntegrationTestProcedure):
    name = "Select and Validate Checkbox"
    position_X = 0
    position_Y = 0
    variable_name = ""
    expected_value = ""

    def __init__(self, test):
        cls = type(self)
        name = cls.name
        position_X = cls.position_X
        position_Y = cls.position_Y
        variable_name = cls.variable_name
        expected_value = cls.expected_value

        select_checkbox = MsgHciButtonPositionEvent(9,[[position_X, position_Y]])
        validate_value = MsgTypeString(str(variable_name), value=expected_value)
        
        info_exchange = [
                        InformationSet("Select checkbox: ", "thriver", "mcrhci", select_checkbox),
                        InformationSet("Validate that the value of mcr_mcrhci_current_selected_bpm is " + str(expected_value) + " and it will be sent to varie.", "mcrhci", "varie", validate_value),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

 

