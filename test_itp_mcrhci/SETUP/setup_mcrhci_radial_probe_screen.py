
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

class SETUP_VALIDATE_RP_INIT_POSITION_FEEDBACK(ClinicalIntegrationTestProcedure):
    name = "Validate Init position feedback"
    # set variable values
    acu14_initposfeedback_value_expected = 100.0
    
    def __init__(self, test):
        cls = type(self)
        name = cls.name
        acu14_initposfeedback_value_expected = cls.acu14_initposfeedback_value_expected

        #get values
        get_acu14_initposfeedback_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "acu14_initposfeedback")

        #validate
        validate_acu14_initposfeedback_value = MsgTypeNumeric("acu14_initposfeedback:TMMI_MCR_OBJECT_GET_VALUE", value=acu14_initposfeedback_value_expected)

        info_exchange = [ 
                        InformationSet("get acu14_initposfeedback value", "thriver", "mcrhci", get_acu14_initposfeedback_value),	
                        InformationSet("validate acu14_initposfeedback value = " + str(acu14_initposfeedback_value_expected), "mcrhci", "hcitracer", validate_acu14_initposfeedback_value),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_VALIDATE_RP_SPEED_FEEDBACK(ClinicalIntegrationTestProcedure):
    name = "Validate Speed feedback"
    # set variable values
    acu14_speedfeedback_value_expected = 100.0

    def __init__(self, test):
        cls = type(self)
        name = cls.name
        acu14_speedfeedback_value_expected = cls.acu14_speedfeedback_value_expected

        #get values
        get_acu14_speedfeedback_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "acu14_speedfeedback")

        #validate
        validate_acu14_speedfeedback_value = MsgTypeNumeric("acu14_speedfeedback:TMMI_MCR_OBJECT_GET_VALUE", value=acu14_speedfeedback_value_expected)

        info_exchange = [ 
                        InformationSet("get acu14_speedfeedback value", "thriver", "mcrhci", get_acu14_speedfeedback_value),	
                        InformationSet("validate acu14_speedfeedback value = " + str(acu14_speedfeedback_value_expected), "mcrhci", "hcitracer", validate_acu14_speedfeedback_value),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_VALIDATE_RP_GAIN_STATUS(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "Validate the gain status of Radial probe label"
        # set variable values
        acu14_lowgaintxt_visibility_expected = "0"
        acu14_highgaintxt_visibility_expected = "1"

        #get values
        get_acu14_lowgaintxt_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu14_lowgaintxt")
        get_acu14_highgaintxt_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu14_highgaintxt")

        #validate
        validate_acu14_lowgaintxt_visibility = MsgTypeString("acu14_lowgaintxt:TMMI_MCR_IS_VISIBLE", value=acu14_lowgaintxt_visibility_expected)
        validate_acu14_highgaintxt_visibility = MsgTypeString("acu14_highgaintxt:TMMI_MCR_IS_VISIBLE", value=acu14_highgaintxt_visibility_expected)

        info_exchange = [                       
                        InformationSet("get acu14_lowgaintxt visibility", "thriver", "mcrhci", get_acu14_lowgaintxt_visibility),	
                        InformationSet("validate acu14_lowgaintxt visibility = " + str(acu14_lowgaintxt_visibility_expected), "mcrhci", "hcitracer", validate_acu14_lowgaintxt_visibility),
	                    InformationSet("get acu14_highgaintxt visibility", "thriver", "mcrhci", get_acu14_highgaintxt_visibility),	
                        InformationSet("validate acu14_highgaintxt visibility = " + str(acu14_highgaintxt_visibility_expected), "mcrhci", "hcitracer", validate_acu14_highgaintxt_visibility),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_VALIDATE_RP1_FULLSCALE_LABEL(ClinicalIntegrationTestProcedure):
    
    def __init__(self, test):
        name = "Validate the current full scale label of Radial probe 1"
        # set variable values
        acu14_rp1fullscaletxt_visibility_expected = "1"

        #get values
        get_acu14_rp1fullscaletxt_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu14_rp1fullscaletxt")
        #validate
        validate_acu14_rp1fullscaletxt_visibility = MsgTypeString("acu14_rp1fullscaletxt:TMMI_MCR_IS_VISIBLE", value=acu14_rp1fullscaletxt_visibility_expected)
        
        info_exchange = [                       
                        InformationSet("get acu14_rp1fullscaletxt visibility", "thriver", "mcrhci", get_acu14_rp1fullscaletxt_visibility),	
                        InformationSet("validate acu14_rp1fullscaletxt visibility = " + str(acu14_rp1fullscaletxt_visibility_expected), "mcrhci", "hcitracer", validate_acu14_rp1fullscaletxt_visibility),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_VALIDATE_RP2_FULLSCALE_LABEL(ClinicalIntegrationTestProcedure):
    
    def __init__(self, test):
        name = "Validate the current full scale label of Radial probe 2"
        # set variable values
        acu14_rp2fullscaletxt_visibility_expected = "1"

        #get values
        get_acu14_rp2fullscaletxt_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu14_rp2fullscaletxt")
        #validate
        validate_acu14_rp2fullscaletxt_visibility = MsgTypeString("acu14_rp2fullscaletxt:TMMI_MCR_IS_VISIBLE", value=acu14_rp2fullscaletxt_visibility_expected)
        
        info_exchange = [                       
                        InformationSet("get acu14_rp2fullscaletxt visibility", "thriver", "mcrhci", get_acu14_rp2fullscaletxt_visibility),	
                        InformationSet("validate acu14_rp2fullscaletxt visibility = " + str(acu14_rp2fullscaletxt_visibility_expected), "mcrhci", "hcitracer", validate_acu14_rp2fullscaletxt_visibility),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_VALIDATE_COL_FULLSCALE_LABEL(ClinicalIntegrationTestProcedure):
    
    def __init__(self, test):
        name = "Validate the current full scale label of Inside Collimator"
        # set variable values
        acu14_colfullscaletxt_visibility_expected = "1"

        #get values
        get_acu14_colfullscaletxt_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu14_colfullscaletxt")
        #validate
        validate_acu14_colfullscaletxt_visibility = MsgTypeString("acu14_colfullscaletxt:TMMI_MCR_IS_VISIBLE", value=acu14_colfullscaletxt_visibility_expected)
        
        info_exchange = [                       
                        InformationSet("get acu14_colfullscaletxt visibility", "thriver", "mcrhci", get_acu14_colfullscaletxt_visibility),	
                        InformationSet("validate acu14_colfullscaletxt visibility = " + str(acu14_colfullscaletxt_visibility_expected), "mcrhci", "hcitracer", validate_acu14_colfullscaletxt_visibility),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_VALIDATE_BS1_FULLSCALE_LABEL(ClinicalIntegrationTestProcedure):
    
    def __init__(self, test):
        name = "Validate the current label of Beam Stop Degrader"
        # set variable values
        acu14_beamdegraderfullscaletxt_visibility_expected = "1"

        #get values
        get_acu14_beamdegraderfullscaletxt_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu14_beamdegraderfullscaletxt")
        #validate
        validate_acu14_beamdegraderfullscaletxt_visibility = MsgTypeString("acu14_beamdegraderfullscaletxt:TMMI_MCR_IS_VISIBLE", value=acu14_beamdegraderfullscaletxt_visibility_expected)
        
        info_exchange = [                       
                        InformationSet("get acu14_beamdegraderfullscaletxt visibility", "thriver", "mcrhci", get_acu14_beamdegraderfullscaletxt_visibility),	
                        InformationSet("validate acu14_beamdegraderfullscaletxt visibility = " + str(acu14_beamdegraderfullscaletxt_visibility_expected), "mcrhci", "hcitracer", validate_acu14_beamdegraderfullscaletxt_visibility),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_VALIDATE_RP1_CURRENT_FEEDBACK(ClinicalIntegrationTestProcedure):
    name = "Validate the current feedback on radial probe 1"
    # set variable values
    acu14_rp1cfeedback_value_expected = 50.0
    acu14_rp1cfeedback_visibility_expected = "1"
    def __init__(self, test):
        cls = type(self)
        name = cls.name 
        acu14_rp1cfeedback_value_expected = cls.acu14_rp1cfeedback_value_expected
        acu14_rp1cfeedback_visibility_expected = cls.acu14_rp1cfeedback_visibility_expected

        #get values
        
        get_acu14_rp1cfeedback_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "acu14_rp1cfeedback")
        get_acu14_rp1cfeedback_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu14_rp1cfeedback")
        
        #validate
        
        validate_acu14_rp1cfeedback_value = MsgTypeNumeric("acu14_rp1cfeedback:TMMI_MCR_OBJECT_GET_VALUE", value=acu14_rp1cfeedback_value_expected)
        validate_acu14_rp1cfeedback_visibility = MsgTypeString("acu14_rp1cfeedback:TMMI_MCR_IS_VISIBLE", value=acu14_rp1cfeedback_visibility_expected)
        
        info_exchange = [                       
                        InformationSet("get acu14_rp1cfeedback value", "thriver", "mcrhci", get_acu14_rp1cfeedback_value),	
                        InformationSet("validate acu14_rp1cfeedback value = " + str(acu14_rp1cfeedback_value_expected), "mcrhci", "hcitracer", validate_acu14_rp1cfeedback_value),
                        InformationSet("get acu14_rp1cfeedback visibility", "thriver", "mcrhci", get_acu14_rp1cfeedback_visibility),	
                        InformationSet("validate acu14_rp1cfeedback visibility = " + str(acu14_rp1cfeedback_visibility_expected), "mcrhci", "hcitracer", validate_acu14_rp1cfeedback_visibility),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_VALIDATE_RP2_CURRENT_FEEDBACK(ClinicalIntegrationTestProcedure):
    name = "Validate the current feedback on radial probe 2"
    # set variable values     
    acu14_rp2cfeedback_value_expected = 50.0
    acu14_rp2cfeedback_visibility_expected = "1"
    def __init__(self, test):
        cls = type(self)
        name = cls.name
        acu14_rp2cfeedback_value_expected = cls.acu14_rp2cfeedback_value_expected
        acu14_rp2cfeedback_visibility_expected = cls.acu14_rp2cfeedback_visibility_expected

        #get values
        get_acu14_rp2cfeedback_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "acu14_rp2cfeedback")
        get_acu14_rp2cfeedback_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu14_rp2cfeedback")
       
        #validate
        validate_acu14_rp2cfeedback_value = MsgTypeNumeric("acu14_rp2cfeedback:TMMI_MCR_OBJECT_GET_VALUE", value=acu14_rp2cfeedback_value_expected)
        validate_acu14_rp2cfeedback_visibility = MsgTypeString("acu14_rp2cfeedback:TMMI_MCR_IS_VISIBLE", value=acu14_rp2cfeedback_visibility_expected)

        info_exchange = [                       
                        InformationSet("get acu14_rp2cfeedback value", "thriver", "mcrhci", get_acu14_rp2cfeedback_value),	
                        InformationSet("validate acu14_rp2cfeedback value = " + str(acu14_rp2cfeedback_value_expected), "mcrhci", "hcitracer", validate_acu14_rp2cfeedback_value),
                        InformationSet("get acu14_rp2cfeedback visibility", "thriver", "mcrhci", get_acu14_rp2cfeedback_visibility),	
                        InformationSet("validate acu14_rp2cfeedback visibility = " + str(acu14_rp2cfeedback_visibility_expected), "mcrhci", "hcitracer", validate_acu14_rp2cfeedback_visibility),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_VALIDATE_COL_CURRENT_FEEDBACK(ClinicalIntegrationTestProcedure):
    name = "Validate the current feedback on Inside Collimator"
    # set variable values
    acu14_colcfeedback_value_expected = 50.0
    acu14_colcfeedback_visibility_expected = "1"
    def __init__(self, test):
        cls = type(self)
        name = cls.name
        acu14_colcfeedback_value_expected = cls.acu14_colcfeedback_value_expected
        acu14_colcfeedback_visibility_expected = cls.acu14_colcfeedback_visibility_expected

        #get values
        get_acu14_colcfeedback_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "acu14_colcfeedback")
        get_acu14_colcfeedback_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu14_colcfeedback")
       
        #validate
        validate_acu14_colcfeedback_value = MsgTypeNumeric("acu14_colcfeedback:TMMI_MCR_OBJECT_GET_VALUE", value=acu14_colcfeedback_value_expected)
        validate_acu14_colcfeedback_visibility = MsgTypeString("acu14_colcfeedback:TMMI_MCR_IS_VISIBLE", value=acu14_colcfeedback_visibility_expected)

        info_exchange = [                       
                        InformationSet("get acu14_colcfeedback value", "thriver", "mcrhci", get_acu14_colcfeedback_value),	
                        InformationSet("validate acu14_colcfeedback value = " + str(acu14_colcfeedback_value_expected), "mcrhci", "hcitracer", validate_acu14_colcfeedback_value),
                        InformationSet("get acu14_colcfeedback visibility", "thriver", "mcrhci", get_acu14_colcfeedback_visibility),	
                        InformationSet("validate acu14_colcfeedback visibility = " + str(acu14_colcfeedback_visibility_expected), "mcrhci", "hcitracer", validate_acu14_colcfeedback_visibility),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_VALIDATE_BS1_CURRENT_FEEDBACK(ClinicalIntegrationTestProcedure):
    name = "Validate the current feedback on Beam Stop Degrader"
    # set variable values
    acu14_bs1cfeedback_value_expected = 50.0
    acu14_bs1cfeedback_visibility_expected = "1"
    def __init__(self, test):
        cls = type(self)
        name = cls.name
        acu14_bs1cfeedback_value_expected = cls.acu14_bs1cfeedback_value_expected
        acu14_bs1cfeedback_visibility_expected = cls.acu14_bs1cfeedback_visibility_expected

        #get values
        get_acu14_bs1cfeedback_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "acu14_bs1cfeedback")
        get_acu14_bs1cfeedback_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_IS_VISIBLE, variable_in = "acu14_bs1cfeedback")
       
        #validate
        validate_acu14_bs1cfeedback_value = MsgTypeNumeric("acu14_bs1cfeedback:TMMI_MCR_OBJECT_GET_VALUE", value=acu14_bs1cfeedback_value_expected)
        validate_acu14_bs1cfeedback_visibility = MsgTypeString("acu14_bs1cfeedback:TMMI_MCR_IS_VISIBLE", value=acu14_bs1cfeedback_visibility_expected)

        info_exchange = [                       
                        InformationSet("get acu14_bs1cfeedback value", "thriver", "mcrhci", get_acu14_bs1cfeedback_value),	
                        InformationSet("validate acu14_bs1cfeedback value = " + str(acu14_bs1cfeedback_value_expected), "mcrhci", "hcitracer", validate_acu14_bs1cfeedback_value),
                        InformationSet("get acu14_bs1cfeedback visibility", "thriver", "mcrhci", get_acu14_bs1cfeedback_visibility),	
                        InformationSet("validate acu14_bs1cfeedback visibility = " + str(acu14_bs1cfeedback_visibility_expected), "mcrhci", "hcitracer", validate_acu14_bs1cfeedback_visibility),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_VALIDATE_RP_POSITION_FEEDBACK(ClinicalIntegrationTestProcedure):
    name = "Validate position feedback of the radial probe"
    # set variable values
    acu14_positionmmfeedback_value_expected = 200.0
    
    def __init__(self, test):
        cls = type(self)
        name = cls.name
        # set variable values
        acu14_positionmmfeedback_value_expected = cls.acu14_positionmmfeedback_value_expected

        #get values
        get_acu14_positionmmfeedback_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "acu14_positionmmfeedback")

        #validate
        validate_acu14_positionmmfeedback_value = MsgTypeNumeric("acu14_positionmmfeedback:TMMI_MCR_OBJECT_GET_VALUE", value=acu14_positionmmfeedback_value_expected)

        info_exchange = [                       
                        InformationSet("get acu14_positionmmfeedback value", "thriver", "mcrhci", get_acu14_positionmmfeedback_value),	
                        InformationSet("validate acu14_positionmmfeedback value = " + str(acu14_positionmmfeedback_value_expected), "mcrhci", "hcitracer", validate_acu14_positionmmfeedback_value),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []        

class SETUP_VALIDATE_RP_ENERGY_FEEDBACK(ClinicalIntegrationTestProcedure):
    name = "Validate energy feedback of the radial probe"
    # set variable values
    acu14_energymevfeedback_value_expected = 100.0
    
    def __init__(self, test):
        cls = type(self)
        name = cls.name
        # set variable values
        acu14_energymevfeedback_value_expected = cls.acu14_energymevfeedback_value_expected

        #get values
        get_acu14_energymevfeedback_value = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = "acu14_energymevfeedback")

        #validate
        validate_acu14_energymevfeedback_value = MsgTypeNumeric("acu14_energymevfeedback:TMMI_MCR_OBJECT_GET_VALUE", value=acu14_energymevfeedback_value_expected)

        info_exchange = [                       
                        InformationSet("get acu14_energymevfeedback value", "thriver", "mcrhci", get_acu14_energymevfeedback_value),	
                        InformationSet("validate acu14_energymevfeedback value = " + str(acu14_energymevfeedback_value_expected), "mcrhci", "hcitracer", validate_acu14_energymevfeedback_value),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

