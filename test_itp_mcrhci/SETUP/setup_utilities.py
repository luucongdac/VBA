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

class SETUP_CLICK_BUTTON_BY_NAME(ClinicalIntegrationTestProcedure):
    name = ""           #Overwrite: Optional (If a different format name is needed, this filed should be overwritten)
    button_name = ""    #Overwrite: Compulsory
    def __init__(self, test):
        cls = type(self)
        button_name = cls.button_name
        if cls.name != "":
            name = cls.name
        else:
            name = "Click on {button_name}".format(button_name=button_name)
        sms_1 = MsgHciButtonNameEvent(0,[[button_name]])
        info_exchange = [ 
                        InformationSet(name, "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_CLICK_BUTTON_BY_POSITION(ClinicalIntegrationTestProcedure):
    name = ""           #Overwrite: Optional (If a different format name is needed, this filed should be overwritten)
    button_pos_x = 0    #Overwrite: Compulsory
    button_pos_y = 0    #Overwrite: Compulsory
    def __init__(self, test):
        cls = type(self)
        button_pos_x = cls.button_pos_x
        button_pos_y = cls.button_pos_y
        if cls.name != "":
            name = cls.name
        else:
            name = "Click on an object/button at position [{x}, {y}]".format(x=str(button_pos_x), y=str(button_pos_y))
            
        sms_1 = MsgHciButtonPositionEvent(9,[[button_pos_x, button_pos_y]])
        info_exchange = [ 
                        InformationSet(name, "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []     

class SETUP_INPUT_TEXTBOX_BY_NAME(ClinicalIntegrationTestProcedure):
    name = ""            #Overwrite: Optional (If a different format name is needed, this field should be overwritten)
    textbox_name = ""    #Overwrite: Compulsory
    content = ""         #Overwrite: Compulsory
    extension_key = ""   #Overwrite: NEWLINE_CHAR, CARRIAGE_RETURN_CHAR, ESCAPE_CHAR
    def __init__(self, test):
        cls = type(self)
        textbox_name = cls.textbox_name
        content = cls.content
        extension_key = cls.extension_key
        if cls.name != "":
            name = cls.name
        else:
            name = "Enter text = {content} on {textbox_name} with extension key = {extension_key}".format(content = content, textbox_name=textbox_name, extension_key=extension_key)
        sms_1 = MsgHciInputNameEvent(0, [[textbox_name, content]], extension_key)
        info_exchange = [ 
                        InformationSet(name, "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_INPUT_TEXTBOX_BY_POSITION(ClinicalIntegrationTestProcedure):
    name = ""            #Overwrite: Optional (If a different format name is needed, this field should be overwritten)
    textbox_pos_x = 0    #Overwrite: Compulsory
    textbox_pos_y = 0    #Overwrite: Compulsory
    content = ""         #Overwrite: Compulsory
    extension_key = ""   #Overwrite: NEWLINE_CHAR, CARRIAGE_RETURN_CHAR, ESCAPE_CHAR    
    def __init__(self, test):
        cls = type(self)
        textbox_pos_x = cls.textbox_pos_x
        textbox_pos_y = cls.textbox_pos_y
        content = cls.content
        extension_key = cls.extension_key        
        if cls.name != "":
            name = cls.name
        else:
            name = "Enter text = {content} at position [{x}, {y}] with extension key = {extension_key}".format(content=content, x=str(textbox_pos_x), y=str(textbox_pos_y), extension_key=extension_key)
            
        sms_1 = MsgHciInputPositionEvent(9, [[textbox_pos_x, textbox_pos_y, content]], extension_key)  
        info_exchange = [ 
                        InformationSet(name, "thriver", "mcrhci", sms_1),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = [] 

class SETUP_SET_VARIABLE(ClinicalIntegrationTestProcedure):
    name = ""       #Overwrite: Optional (If a different format name is needed, this filed should be overwritten)
    var_name = ""   #Overwrite: Compulsory
    value = 1       #Overwrite: Optional (Must be overwritten if the value is different than 1 )  
                        #When overwrite the value in the derived class, only set True or False if the var_name is a boolean, otherwise, use number for numeric#
    
    def __init__(self, test):
        cls = type(self)
        var_name = cls.var_name
        value = cls.value
        if var_name != "":
            if isinstance(value, bool):
                sms_1 = MsgTypeBoolean(var_name,value)
            elif isinstance(value, (float, int)):
                sms_1 = MsgTypeNumeric(var_name, value)
            elif isinstance(value,str):
                sms_1 = MsgTypeString(var_name, value)                               
            else:
                name = "Invalid data type"
                sms_1 = MsgTypeString(var_name, value)

            if cls.name != "":
                name = cls.name
            else:
                name = "Set {var_name} to {value}".format(var_name=var_name, value=value)
            info_exchange = [ 
                            InformationSet(name, "thriver", "mcrhci", sms_1),
                            ]

            ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
            self.applicable_rooms = ['mcr']
            self.setup = []
            self.teardown = []

#TODO: Separate Click action and validation into 2 classes
class SETUP_CLICK_AND_VALIDATE_SENT_VARIABLE(ClinicalIntegrationTestProcedure):
    button_name = ""            #Overwrite: Compulsory
    validate_slot_name = ""     #Overwrite: Compulsory
    value = 0                   #Overwrite: Compulsory (You can overwrite this field not only with a numeric type but also with a string type)
    destination = ""            #Overwrite: Compulsory
    origin = "mcrhci"           #Overwrite: Optional (Only overwrite if the origin is other than mcrhci)
    name = ""                   #Overwrite: Optional (If a different format name is needed, this field should be overwritten)
    forced_datagroup= ""        #Overwrite: Optional (Only overwrite if you need to validate messages sent with a specific data group)
    def __init__(self, test):
        cls = type(self)
        button_name = cls.button_name
        validate_slot_name = cls.validate_slot_name
        value = cls.value
        destination = cls.destination
        origin = cls.origin
        forced_datagroup = cls.forced_datagroup
        if cls.name != "":
            name = cls.name
        else:
            name = "Click on {button_name} and validate {validate_slot_name} sent".format(button_name=button_name,validate_slot_name=validate_slot_name)

        click_msg = MsgHciButtonNameEvent(0,[[button_name]])
        if validate_slot_name != "":
            if isinstance(value, bool):
                validate_var = MsgTypeBoolean(validate_slot_name, value)
            elif isinstance(value, (float, int)):
                validate_var = MsgTypeNumeric(validate_slot_name, value)
            elif isinstance(value,str):
                validate_var = MsgTypeString(validate_slot_name, value)
            else:
                name = "Invalid data type"
                validate_var = MsgTypeString(validate_slot_name, value)

            if forced_datagroup != "":
                info_exchange = [
                                InformationSet("Click on {button_name}".format(button_name=button_name), "thriver", "mcrhci", click_msg), 
                                InformationSet("Validate {validate_slot_name} sent through {forced_datagroup}".format(validate_slot_name=validate_slot_name, forced_datagroup=forced_datagroup), origin, destination, validate_var, forced_dg=forced_datagroup),
                                ]
            else:
                info_exchange = [
                                InformationSet("Click on {button_name}".format(button_name=button_name), "thriver", "mcrhci", click_msg), 
                                InformationSet("Validate {validate_slot_name} sent".format(validate_slot_name=validate_slot_name), origin, destination, validate_var),
                                ]

            ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
            self.applicable_rooms = ['mcr']
            self.setup = []
            self.teardown = []

class SETUP_VALIDATE_OBJECT_INFO(ClinicalIntegrationTestProcedure):
    name = ""               #Overwrite: Optional (If a different format name is needed, this field should be overwritten)
    object_name = ""        #Overwrite: Compulsory
    info_type = ""          #Overwrite: Compulsory
    expected_value = ""     #Overwrite: Compulsory (You can overwrite this field not only with a string type but also with a numeric type)
    def __init__(self, test):
        cls = type(self)
        object_name = cls.object_name
        info_type = cls.info_type
        expected_value = cls.expected_value
        unknown_type = "INVALID_TYPE"

        # Create object, validate info
        def getAttrObject(type_in):
            return {
                "TMMI_MCR_OBJECT_GET_ATTR:BACKGROUND_COLOR" : [ TMMI_MCR_OBJECT_GET_ATTR            , "background color"],
                "TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR" : [ TMMI_MCR_OBJECT_GET_ATTR            , "foreground color"],
                "TMMI_MCR_IS_VISIBLE"                       : [ TMMI_MCR_IS_VISIBLE                 , "visibility"      ],
                "TMMI_MCR_TEXT_FIELD"                       : [ TMMI_MCR_TEXT_FIELD                 , "text"            ],
                "TMMI_MCR_OBJECT_GET_VALUE"                 : [ TMMI_MCR_OBJECT_GET_VALUE           , "object value"    ],
                "TMMI_MCR_OBJECT_GET_BOOLVALUE"             : [ TMMI_MCR_OBJECT_GET_BOOLVALUE       , "bool value"      ],
                "TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME"        : [ TMMI_MCR_OBJECT_GET_SUBOBJECT_NAME  , "sub object"      ],
                "TMMI_MCR_TOGGLE_STATE"                     : [ TMMI_MCR_TOGGLE_STATE               , "toggle state"    ],
                "TMMI_MCR_TEXT_LIST"                        : [ TMMI_MCR_TEXT_LIST                  , "text list"       ],
                "TMMI_MCR_TEXT_LIST2"                       : [ TMMI_MCR_TEXT_LIST2                 , "text list 2"     ],
                "TMMI_MCR_OBJECT_GET_ATTR:FILL_AMOUNT"      : [ TMMI_MCR_OBJECT_GET_ATTR            , "fill amount"     ],
                "TMMI_MCR_OBJECT_GET_ATTR:FILL_DIRECTION"   : [ TMMI_MCR_OBJECT_GET_ATTR            , "fill direction"  ]
            }.get(type_in, [unknown_type, unknown_type])

        mcr_type, mcr_attr = getAttrObject(info_type)
        if mcr_type != unknown_type:
            get_object = MsgMCRHciDumpGuiData(type_in = mcr_type, variable_in = object_name)
            get_info_name = "Get {object_name} {mcr_attr}".format(object_name=object_name, mcr_attr=mcr_attr)
            validate_info_name = "Validate that the {object_name}'s {mcr_attr} is {expected_value}".format(object_name=object_name, mcr_attr=mcr_attr, expected_value=expected_value)
        else:
            get_info_name = "Get invalid type"
            validate_info_name = "Validate invalid type"

        if cls.name != "":
            name = cls.name
        else:
            name = validate_info_name

        # validate
        if isinstance(expected_value, bool):
            validate_object = MsgTypeBoolean(object_name + ":" + info_type, value=expected_value)
        elif isinstance(expected_value, (float, int)):
            validate_object = MsgTypeNumeric(object_name + ":" + info_type, value=expected_value)
        elif isinstance(expected_value, str):
            validate_object = MsgTypeString(object_name  + ":" + info_type, value=expected_value)
        else:
            name = "Invalid data type"
            validate_object = MsgTypeString(object_name + ":" + info_type, value=expected_value)

        info_exchange = [
                        InformationSet(get_info_name, "thriver", "mcrhci", get_object),
                        InformationSet(validate_info_name, "mcrhci", "hcitracer", validate_object)
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_VALIDATE_SUBDRAWING_OBJECT_TEXT(ClinicalIntegrationTestProcedure):
    """
    This class is used to validate the displaying text of a subdrawing object.
    Variables:
        name:                   optional  - if a different format name is needed, this field should be overwritten
        view_name:              mandatory - name of the view to be checked (e.g.: view_name = "pts_layout")
        subdrawing_object_name: mandatory - name of the subdrawing object
        expected_value:         mandatory - the expected text
    """
    name = ""
    view_name = ""
    subdrawing_object_name = ""
    expected_value = ""
    def __init__(self, test):
        cls = type(self)
        view_name = cls.view_name
        subdrawing_object_name = cls.subdrawing_object_name
        expected_value = cls.expected_value
        info_type = "TMMI_MCR_SUBDRAWING_OBJECT_GET_TEXT"

        get_object = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_SUBDRAWING_OBJECT_GET_TEXT, variable_in = "{view_name}:{subdrawing_object_name}".\
                    format(view_name=view_name, subdrawing_object_name=subdrawing_object_name))
        get_info_name = "Get {view_name}:{subdrawing_object_name}:{info_type}".\
                        format(view_name=view_name, subdrawing_object_name=subdrawing_object_name, info_type=info_type)
        validate_info_name = "Validate that the value of {view_name}:{subdrawing_object_name}:{info_type} is equal to {expected_value}".\
                                format(view_name=view_name, subdrawing_object_name=subdrawing_object_name, info_type=info_type, expected_value=expected_value)

        if cls.name != "":
            name = cls.name
        else:
            name = validate_info_name

        # validate
        validate_object = MsgTypeString("{view_name}:{subdrawing_object_name}:{info_type}".\
                                        format(view_name=view_name, subdrawing_object_name=subdrawing_object_name, info_type=info_type), value=expected_value)

        info_exchange = [
                        InformationSet(get_info_name, "thriver", "mcrhci", get_object),
                        InformationSet(validate_info_name, "mcrhci", "hcitracer", validate_object)
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_VALIDATE_SUBDRAWING_SUBOBJECT_INFO(ClinicalIntegrationTestProcedure):
    """
    This class is used to validate the information of the subobject contained by a subdrawing object.
    Variables:
        name:                   optional - if a different format name is needed, this field should be overwritten
        view_name:              mandatory - the name of the view to be checked (e.g.: view_name = "pts_layout")
        subdrawing_object_name: mandatory - name of the subdrawing object
        subobject_name:         mandatory - name of the subobject contained by the subdrawing object
        info_type:              mandatory - type of information which needs to be validate
        expected_value:         mandatory - the expected result, it can be a numeric or string value
    """
    name = ""
    view_name = ""
    subdrawing_object_name = ""
    subobject_name = ""
    info_type = ""
    expected_value = ""
    def __init__(self, test):
        cls = type(self)
        view_name = cls.view_name
        subdrawing_object_name = cls.subdrawing_object_name
        subobject_name = cls.subobject_name
        info_type = cls.info_type
        expected_value = cls.expected_value
        unknown_type = "INVALID_TYPE"

        # Create object, validate info
        def getAttrObject(type_in):
            return {
                "TMMI_MCR_SUBDRAWING_SUBOBJECT_GET_ATTR:BACKGROUND_COLOR" : TMMI_MCR_SUBDRAWING_SUBOBJECT_GET_ATTR,
                "TMMI_MCR_SUBDRAWING_SUBOBJECT_GET_ATTR:FOREGROUND_COLOR" : TMMI_MCR_SUBDRAWING_SUBOBJECT_GET_ATTR,
                "TMMI_MCR_SUBDRAWING_SUBOBJECT_GET_ATTR:FILL_AMOUNT"      : TMMI_MCR_SUBDRAWING_SUBOBJECT_GET_ATTR,
                "TMMI_MCR_SUBDRAWING_SUBOBJECT_GET_ATTR:FILL_DIRECTION"   : TMMI_MCR_SUBDRAWING_SUBOBJECT_GET_ATTR,
                "TMMI_MCR_SUBDRAWING_SUBOBJECT_GET_VISIBILITY"            : TMMI_MCR_SUBDRAWING_SUBOBJECT_GET_VISIBILITY,
                "TMMI_MCR_SUBDRAWING_SUBOBJECT_GET_TEXT"                  : TMMI_MCR_SUBDRAWING_SUBOBJECT_GET_TEXT       
            }.get(type_in, unknown_type)

        mcr_type = getAttrObject(info_type)
        if mcr_type != unknown_type:
            get_object = MsgMCRHciDumpGuiData(type_in = mcr_type, variable_in = "{view_name}:{subdrawing_object_name}#{subobject_name}".\
                        format(view_name=view_name, subdrawing_object_name=subdrawing_object_name, subobject_name=subobject_name))
            get_info_name = "Get {view_name}:{subdrawing_object_name}:{subobject_name}:{info_type}".\
                            format(view_name=view_name, subdrawing_object_name=subdrawing_object_name, subobject_name=subobject_name, info_type=info_type)
            validate_info_name = "Validate that the value of {view_name}:{subdrawing_object_name}:{subobject_name}:{info_type} is equal to {expected_value}".\
                                    format(view_name=view_name, subdrawing_object_name=subdrawing_object_name, subobject_name= subobject_name, info_type=info_type, expected_value=expected_value)
        else:
            get_info_name = "Get invalid type"
            validate_info_name = "Validate invalid type"

        if cls.name != "":
            name = cls.name
        else:
            name = validate_info_name

        # validate
        if isinstance(expected_value, bool):
            validate_object = MsgTypeBoolean("{view_name}:{subdrawing_object_name}:{subobject_name}:{info_type}".\
                                             format(view_name=view_name, subdrawing_object_name=subdrawing_object_name, subobject_name= subobject_name, info_type=info_type), value=expected_value)
        elif isinstance(expected_value, (float, int)):
            validate_object = MsgTypeNumeric("{view_name}:{subdrawing_object_name}:{subobject_name}:{info_type}".\
                                             format(view_name=view_name, subdrawing_object_name=subdrawing_object_name, subobject_name= subobject_name, info_type=info_type), value=expected_value)
        elif isinstance(expected_value, str):
            validate_object = MsgTypeString("{view_name}:{subdrawing_object_name}:{subobject_name}:{info_type}".\
                                             format(view_name=view_name, subdrawing_object_name=subdrawing_object_name, subobject_name= subobject_name, info_type=info_type), value=expected_value)
        else:
            name = "Invalid data type"
            validate_object = MsgTypeString("{view_name}:{subdrawing_object_name}:{subobject_name}:{info_type}".\
                                             format(view_name=view_name, subdrawing_object_name=subdrawing_object_name, subobject_name= subobject_name, info_type=info_type), value=expected_value)

        info_exchange = [
                        InformationSet(get_info_name, "thriver", "mcrhci", get_object),
                        InformationSet(validate_info_name, "mcrhci", "hcitracer", validate_object)
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

"""
Constant Color Id

    BLACK_1         : 0
    WHITE_1         : 1
    BLUESKY_1       : 2
    BLUE_1          : 3
    VIOLET_1        : 4
    LIGHT_PINK_1    : 5
    PINK_1          : 6
    HOT_PINK_1      : 7
    RED_1           : 8
    ORANGE_1        : 9
    TANGERINE_1     : 10
    ORANGE_YELLOW_1 : 11
    YELLOW_1        : 12
    GREEN_1         : 13
    SEAGLASS_1      : 14
    CYAN_1          : 15
    BLACK_2         : 16
    WHITE_2         : 17
    BLUESKY_2       : 18
    BLUE_2          : 19
    VIOLET_2        : 20
    LIGHT_PINK_2    : 21
    PINK_2          : 22
    HOT_PINK_2      : 23
    RED_2           : 24
    ORANGE_2        : 25
    TANGERINE_2     : 26
    ORANGE_YELLOW_2 : 27
    YELLOW_2        : 28
    GREEN_2         : 29
    SEAGLASS_2      : 30
    CYAN_2          : 31
    BLACK_3         : 32
    WHITE_3         : 33
    BLUESKY_3       : 34
    BLUE_3          : 35
    VIOLET_3        : 36
    LIGHT_PINK_3    : 37
    PINK_3          : 38
    HOT_PINK_3      : 39
    RED_3           : 40
    ORANGE_3        : 41
    TANGERINE_3     : 42
    ORANGE_YELLOW_3 : 43
    YELLOW_3        : 44
    GREEN_3         : 45
    SEAGLASS_3      : 46
    CYAN_3          : 47
    BLACK_4         : 48
    WHITE_4         : 49
    BLUESKY_4       : 50
    BLUE_4          : 51
    VIOLET_4        : 52
    LIGHT_PINK_4    : 53
    PINK_4          : 54
    HOT_PINK_4      : 55
    RED_4           : 56
    ORANGE_4        : 57
    TANGERINE_4     : 58
    ORANGE_YELLOW_4 : 59
    YELLOW_4        : 60
    GREEN_4         : 61
    SEAGLASS_4      : 62
    CYAN_4          : 63
    BLACK_5         : 64
    WHITE_5         : 65
    BLUESKY_5       : 66
    BLUE_5          : 67
    VIOLET_5        : 68
    LIGHT_PINK_5    : 69
    PINK_5          : 70
    HOT_PINK_5      : 71
    RED_5           : 72
    ORANGE_5        : 73
    TANGERINE_5     : 74
    ORANGE_YELLOW_5 : 75
    YELLOW_5        : 76
    GREEN_5         : 77
    SEAGLASS_5      : 78
    CYAN_5          : 79
    BLACK_6         : 80
    WHITE_6         : 81
    BLUESKY_6       : 82
    BLUE_6          : 83
    VIOLET_6        : 84
    LIGHT_PINK_6    : 85
    PINK_6          : 86
    HOT_PINK_6      : 87
    RED_6           : 88
    ORANGE_6        : 89
    TANGERINE_6     : 90
    ORANGE_YELLOW_6 : 91
    YELLOW_6        : 92
    GREEN_6         : 93
    SEAGLASS_6      : 94
    CYAN_6          : 95
    BLACK_7         : 96
    WHITE_7         : 97
    BLUESKY_7       : 98
    BLUE_7          : 99
    VIOLET_7        : 100
    LIGHT_PINK_7    : 101
    PINK_7          : 102
    HOT_PINK_7      : 103
    RED_7           : 104
    ORANGE_7        : 105
    TANGERINE_7     : 106
    ORANGE_YELLOW_7 : 107
    YELLOW_7        : 108
    GREEN_7         : 109
    SEAGLASS_7      : 110
    CYAN_7          : 111
    BLACK_8         : 112
    WHITE_8         : 113
    BLUESKY_8       : 114
    BLUE_8          : 115
    VIOLET_8        : 116
    LIGHT_PINK_8    : 117
    PINK_8          : 118
    HOT_PINK_8      : 119
    RED_8           : 120
    ORANGE_8        : 121
    TANGERINE_8     : 122
    ORANGE_YELLOW_8 : 123
    YELLOW_8        : 124
    GREEN_8         : 125
    SEAGLASS_8      : 126
    CYAN_8          : 127

# Usage - two ways to get color id:
   COLORS.colorDict["BLACK_4"]
   COLORS().getColorID("BLACK_4")
"""
class COLORS:
    base_colors = ["BLACK", "WHITE", "BLUESKY", "BLUE", "VIOLET", "LIGHT_PINK", "PINK", "HOT_PINK",
                    "RED", "ORANGE", "TANGERINE", "ORANGE_YELLOW", "YELLOW", "GREEN", "SEAGLASS", "CYAN"]
    color_value = 0
    colorDict = {}
    for i in range(1,9):
        for base_color in base_colors:
            color_name = "{color}_{index}".format(color=base_color, index=i)
            colorDict[color_name] = str(color_value)
            color_value += 1

    # Get Color Id
    def getColorID(self, color_name):
        if color_name in self.colorDict:
            return self.colorDict[color_name]
        else:
            return ""

# TODO: Delete this class and update code with new APIs
class SETUP_SET_VALIDATE_NUMERIC_VAR_FOREGROUND_COLOR(ClinicalIntegrationTestProcedure):    
    # default variable value
    variable_name = ""
    variable_set = 0
    object_name = ""
    color_code = "0"
    def __init__(self, test):
        cls = type(self)
        variable_name = cls.variable_name
        variable_set = cls.variable_set
        object_name = cls.object_name
        color_code = cls.color_code
        
        name = "[Set " + variable_name + " to: " + str(variable_set) + "] and [Validate the corresponding object " + object_name + "]"
        set_object = MsgTypeNumeric(variable_name, variable_set)
        get_object_var = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_VALUE, variable_in = object_name )
        get_object_att = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = object_name )
        validate_value_object = MsgTypeNumeric(object_name + ":TMMI_MCR_OBJECT_GET_VALUE", value = variable_set )
        validate_color_object = MsgTypeString(object_name + ":TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value = color_code )
        info_exchange = [
                        InformationSet("set " + variable_name + str(variable_set), "thriver", "mcrhci", set_object ),
                        InformationSet("get " + variable_name, "thriver", "mcrhci", get_object_var),
                        InformationSet("validate value of " + variable_name, "mcrhci", "hcitracer", validate_value_object),
                        InformationSet("get " + variable_name, "thriver", "mcrhci", get_object_att),
                        InformationSet("validate color of " + variable_name, "mcrhci", "hcitracer", validate_color_object),
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [  
                        ]
        self.teardown_path = []      

# TODO: Delete this class and update code with new APIs
class SETUP_SET_VALIDATE_TEXT_VAR_FOREGROUND_COLOR(ClinicalIntegrationTestProcedure):    
    # default variable value
    variable_name = ""
    variable_set = ""
    object_name = ""
    color_code = "0"
    def __init__(self, test):
        cls = type(self)
        variable_name = cls.variable_name
        variable_set = cls.variable_set
        object_name = cls.object_name
        color_code = cls.color_code
        
        name = "[Set " + variable_name + " to: " + str(variable_set) + "] and [Validate the corresponding object " + object_name + "]"
        set_object = MsgTypeString( variable_name, variable_set )
        get_object_var = MsgMCRHciDumpGuiData( type_in = TMMI_MCR_TEXT_FIELD, variable_in = object_name )
        get_object_att = MsgMCRHciDumpGuiData( type_in = TMMI_MCR_OBJECT_GET_ATTR, variable_in = object_name )
        validate_value_object = MsgTypeString( object_name + ":TMMI_MCR_TEXT_FIELD", value = variable_set )
        validate_color_object = MsgTypeString( object_name + ":TMMI_MCR_OBJECT_GET_ATTR:FOREGROUND_COLOR", value = color_code )
        info_exchange = [
                        InformationSet("set " + variable_name + str(variable_set), "thriver", "mcrhci", set_object),
                        InformationSet("get " + variable_name, "thriver", "mcrhci", get_object_var),
                        InformationSet("validate value of " + variable_name, "mcrhci", "hcitracer", validate_value_object),
                        InformationSet("get " + variable_name, "thriver", "mcrhci", get_object_att),
                        InformationSet("validate color of " + variable_name, "mcrhci", "hcitracer", validate_color_object),
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name = name, info_exchange = info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [  
                        ]
        self.teardown_path = []            

class SETUP_VIEW_DISPLAY_STATUS_CHECK(ClinicalIntegrationTestProcedure):
    """
    This class is used to check the display status of a specific view.
    Variables:
        name:            optional - if a different format name is needed, this field should be overwritten
        view_name:       the name of the view to be checked (e.g.: view_name = "pts_layout")
        expected_result: the expected display status of the view. "0" - the view is not being displayed / "1" - the view is being displayed.
    """
    name = ""
    view_name = ""
    expected_result = ""
    def __init__(self, test):
        cls = type(self)
        name = cls.name
        view_name = cls.view_name
        expected_result = cls.expected_result
        if cls.name != "":
            name = cls.name
        else:
            name = "Validate that {view_name}.v view is displayed".format(view_name=view_name)
        
        check_view_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_VIEW_IS_DISPLAYED, variable_in = "{view_name}:".format(view_name=view_name))
        validate_view_visibility = MsgTypeString("{view_name}:TMMI_MCR_VIEW_IS_DISPLAYED".format(view_name=view_name), expected_result)

        info_exchange = [ 
                        InformationSet("Check {view_name}.v view's visibility".format(view_name=view_name), "thriver", "mcrhci", check_view_visibility),
                        InformationSet("Validate {view_name}.v view's visibility".format(view_name=view_name), "mcrhci", "hcitracer", validate_view_visibility),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_VALIDATE_OBJECT_POSITION(ClinicalIntegrationTestProcedure):
    """
    This class is used to check the object's position.
    Variables:
        name:                optional - if a different format name is needed, this field should be overwritten
        view_name:           the name of the view including the object, keep empty if no need
        object_name:         the name of the object to be checked (e.g.: object_name = "rectangle_1")
        expected_position_x: the expected X position of the object.
        expected_position_y: the expected Y position of the object.
    """
    name = ""
    view_name = ""
    object_name = ""
    expected_position_x = 0
    expected_position_y = 0
    def __init__(self, test):
        cls = type(self)
        name = cls.name
        view_name = cls.view_name
        object_name = cls.object_name
        expected_position_x = cls.expected_position_x
        expected_position_y = cls.expected_position_y
        if cls.name != "":
            name = cls.name
        else:
            if view_name == "":
                name = "Validate object's position: {object_name}".format(object_name=object_name)
            else:
                name = "Validate object's position with view: {view_name}:{object_name}".format(view_name=view_name, object_name=object_name)
        
        info_exchange = []
        if view_name == "":
            get_object_position = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_POSITION, variable_in = object_name)
            validate_object_position = MsgTypeString("{object_name}:TMMI_MCR_OBJECT_GET_POSITION".format(object_name=object_name), "X={X}, Y={Y}".format(X=expected_position_x, Y=expected_position_y))
            info_exchange = [ 
                            InformationSet("Get object's position: {object_name}".format(object_name=object_name), "thriver", "mcrhci", get_object_position),
                            InformationSet("Validate object's position: {object_name}".format(object_name=object_name), "mcrhci", "hcitracer", validate_object_position),
                            ]        
        else:
            get_object_position = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_POSITION, variable_in = "{view_name}:{object_name}".format(view_name=view_name, object_name=object_name))
            validate_object_position = MsgTypeString("{view_name}:{object_name}:TMMI_MCR_OBJECT_GET_POSITION".format(view_name=view_name, object_name=object_name), "X={X}, Y={Y}".format(X=expected_position_x, Y=expected_position_y))
            info_exchange = [ 
                            InformationSet("Get object's position with view: {view_name}:{object_name}".format(view_name=view_name, object_name=object_name), "thriver", "mcrhci", get_object_position),
                            InformationSet("Validate object's position with view: {view_name}:{object_name}".format(view_name=view_name, object_name=object_name), "mcrhci", "hcitracer", validate_object_position),
                            ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []        


class SETUP_VALIDATE_VALUE_OF_SLOT(ClinicalIntegrationTestProcedure):
    """
    This class is used to check the slot's value.
    Variables:
        name:                   optional - if a different format name is needed, this field should be overwritten
        slot_name:              the name of the slot to be checked ("setslot acq_mode" - slot_name = "acq_mode")
        expected_value:         the expected numeric value of the slot including String, Boolean and Numeric type
    """
    name = ""
    slot_name = ""
    expected_value = 0
    def __init__(self, test):
        cls = type(self)
        name = cls.name
        slot_name = cls.slot_name
        expected_value = cls.expected_value
        if cls.name != "":
            name = cls.name
        else:
            if isinstance(expected_value, (float, int)):
                name = "Validate slot's numeric value: {slot_name}".format(slot_name=slot_name)
            elif isinstance(expected_value, bool):
                name = "Validate slot's boolean value: {slot_name}".format(slot_name=slot_name)
            elif isinstance(expected_value, str):
                name = "Validate slot's string value: {slot_name}".format(slot_name=slot_name)
            else:
                name = "Invalid data type, empty info_exchange"

        get_value_of_slot = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_GET_SLOT_VALUE, variable_in = slot_name)
        # validate
        if isinstance(expected_value, bool):
            validate_boolean_value_of_slot = MsgTypeString("{slot_name}:TMMI_MCR_GET_SLOT_VALUE".format(slot_name=slot_name), expected_value)
            info_exchange = [ 
                            InformationSet("Get slot's boolean value: {slot_name}".format(slot_name=slot_name), "thriver", "mcrhci", get_value_of_slot),
                            InformationSet("Validate slot's boolean value: {slot_name}".format(slot_name=slot_name), "mcrhci", "hcitracer", validate_boolean_value_of_slot),
                            ]
        elif isinstance(expected_value, (float, int)):
            validate_numeric_value_of_slot = MsgTypeNumeric("{slot_name}:TMMI_MCR_GET_SLOT_VALUE".format(slot_name=slot_name), expected_value)
            info_exchange = [ 
                            InformationSet("Get slot's numeric value: {slot_name}".format(slot_name=slot_name), "thriver", "mcrhci", get_value_of_slot),
                            InformationSet("Validate slot's numeric value: {slot_name}".format(slot_name=slot_name), "mcrhci", "hcitracer", validate_numeric_value_of_slot),
                            ]
        elif isinstance(expected_value, str):
            validate_string_value_of_slot = MsgTypeString("{slot_name}:TMMI_MCR_GET_SLOT_VALUE".format(slot_name=slot_name), expected_value)
            info_exchange = [ 
                            InformationSet("Get slot's string value: {slot_name}".format(slot_name=slot_name), "thriver", "mcrhci", get_value_of_slot),
                            InformationSet("Validate slot's string value: {slot_name}".format(slot_name=slot_name), "mcrhci", "hcitracer", validate_string_value_of_slot),
                            ]
        else:
            info_exchange = []
            
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []          

class SETUP_POPUP_VIEW_STATUS_CHECK(ClinicalIntegrationTestProcedure):
    """
    This class is used to check if the specified view is currently popped up on the specified base view.
    Variables:
        name:            optional - if a different format name is needed, this field should be overwritten
        view_name:       the name of the base view (e.g.: view_name = "mbpm")
        popup_view:      the name of the view to be checked (e.g.: popup_view = "bpm_selection")
        expected_result: the expected status of the popup view. "0" - the view is not being popped up. / "1" - the view is being popped up.
    """
    name = ""
    view_name = ""
    popup_view = ""
    expected_result = ""
    def __init__(self, test):
        cls = type(self)
        name = cls.name
        view_name = cls.view_name
        popup_view = cls.popup_view
        expected_result = cls.expected_result
        if cls.name != "":
            name = cls.name
        else:
            name = "Validate that {popup_view}.v view is popped up onto the {view_name}.v view".format(popup_view=popup_view, view_name=view_name)
        
        check_popup_view_visibility = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_VIEW_IS_POPPED_UP, variable_in = "{view_name}:{popup_view}".format(view_name=view_name, popup_view=popup_view))
        validate_popup_view_visibility = MsgTypeString("{popup_view}:TMMI_MCR_VIEW_IS_POPPED_UP".format(popup_view=popup_view), expected_result)

        info_exchange = [ 
                        InformationSet("Check {popup_view}.v popup view's visibility".format(popup_view=popup_view), "thriver", "mcrhci", check_popup_view_visibility),
                        InformationSet("Validate {popup_view}.v popup view's visibility".format(popup_view=popup_view), "mcrhci", "hcitracer", validate_popup_view_visibility),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_VALIDATE_VALUE_OF_OBJECT_SLOT(ClinicalIntegrationTestProcedure):
    """
    This class is used to check value the object's slot
    Variables:
        name:            optional - if a different format name is needed, this field should be overwritten
        object_name:            the name of a sub-drawing or a graphical object
        slot_name:              the name of the slot to be checked ("setslot acq_mode" - slot_name = "acq_mode")
        expected_value:         the expected numeric value of the slot including String, Boolean and Numeric type
    """
    name = ""
    object_name = ""
    slot_name = ""
    expected_value = 0
    def __init__(self, test):
        cls = type(self)
        name = cls.name
        object_name = cls.object_name
        slot_name = cls.slot_name
        expected_value = cls.expected_value
        if cls.name != "":
            name = cls.name
        else:
            if isinstance(expected_value, (float, int)):
                name = "Validate slot's numeric value: {object_name}#{slot_name}".format(object_name=object_name,slot_name=slot_name)
            elif isinstance(expected_value, bool):
                name = "Validate slot's boolean value: {object_name}#{slot_name}".format(object_name=object_name,slot_name=slot_name)
            elif isinstance(expected_value, str):
                name = "Validate slot's string value: {object_name}#{slot_name}".format(object_name=object_name,slot_name=slot_name)
            else:
                name = "Invalid data type, empty info_exchange"

        get_value_of_slot = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_SLOT_VALUE , variable_in = object_name+"#"+slot_name)
        # validate
        if isinstance(expected_value, bool):
            validate_boolean_value_of_slot = MsgTypeString("{object_name}#{slot_name}:TMMI_MCR_OBJECT_GET_SLOT_VALUE".format(object_name=object_name,slot_name=slot_name), expected_value)
            info_exchange = [ 
                            InformationSet("Get slot's boolean value: {slot_name}".format(slot_name=slot_name), "thriver", "mcrhci", get_value_of_slot),
                            InformationSet("Validate slot's boolean value: {slot_name}".format(slot_name=slot_name), "mcrhci", "hcitracer", validate_boolean_value_of_slot),
                            ]
        elif isinstance(expected_value, (float, int)):
            validate_numeric_value_of_slot = MsgTypeNumeric("{object_name}#{slot_name}:TMMI_MCR_OBJECT_GET_SLOT_VALUE".format(object_name=object_name,slot_name=slot_name), expected_value)
            info_exchange = [ 
                            InformationSet("Get slot's numeric value: {slot_name}".format(slot_name=slot_name), "thriver", "mcrhci", get_value_of_slot),
                            InformationSet("Validate slot's numeric value: {slot_name}".format(slot_name=slot_name), "mcrhci", "hcitracer", validate_numeric_value_of_slot),
                            ]
        elif isinstance(expected_value, str):
            validate_string_value_of_slot = MsgTypeString("{object_name}#{slot_name}:TMMI_MCR_OBJECT_GET_SLOT_VALUE".format(object_name=object_name,slot_name=slot_name), expected_value)
            info_exchange = [ 
                            InformationSet("Get slot's string value: {slot_name}".format(slot_name=slot_name), "thriver", "mcrhci", get_value_of_slot),
                            InformationSet("Validate slot's string value: {slot_name}".format(slot_name=slot_name), "mcrhci", "hcitracer", validate_string_value_of_slot),
                            ]
        else:
            info_exchange = []
            
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_VALIDATE_RPC_CALL_FUNCTION(ClinicalIntegrationTestProcedure):
    name = ""               #Overwrite: Optional (If a different format name is needed, this filed should be overwritten)
    rpc_message_name = ""   #Overwrite: Compulsory
    destination = ""        #Overwrite: Compulsory
    origin = "mcrhci"       #Overwrite: Optional (Only overwite if the origin is other than mcrhci)
    value = []              #Overwrite: Optional (Must be overwritten if the list is not empty)                          
    
    def __init__(self, test):
        cls = type(self)
        rpc_message_name = cls.rpc_message_name
        origin = cls.origin
        destination = cls.destination
        value = cls.value
        if rpc_message_name != "":
            rpc_sms = RpcCallService(rpc_message_name, value)
            if cls.name != "":
                name = cls.name
            else:
                name = "Validate {rpc_message_name} function to {value}".format(rpc_message_name=rpc_message_name, value=value)
            info_exchange = [ 
                            InformationSet(name, origin, destination, rpc_sms),
                            ]
        else:
            name = "Invalid data for RPC call validation"
            info_exchange = [
                            ]
        
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = [] 

class SETUP_VALIDATE_GRAPH_INFO(ClinicalIntegrationTestProcedure):
    """
    This class is used to get the Graph's information.
    Variables:
        name:                   #Overwrite: optional - if a different format name is needed, this field should be overwritten
        view_name:              the name of the base view (e.g.: view_name = "mcr_treatment_pps_loadcell_graph1")
        object_name:            the name of the Graph object to be checked
        variable_name:          the variable name was binded on to Graph
        info_type:              TMMI message type, i.e TMMI_MCR_GRAPH_GET_VAR_VALID/ TMMI_MCR_GRAPH_GET_VAR_VALUE/ TMMI_MCR_GRAPH_GET_VAR_COLOR
        expected_value:         the expected value of the graph including Boolean, Float type
    """
    name           = ""
    view_name      = ""
    object_name    = ""
    variable_name  = ""
    info_type      = ""
    expected_value = 0
    def __init__(self, test):
        cls = type(self)
        name           = cls.name
        view_name      = cls.view_name
        object_name    = cls.object_name
        variable_name  = cls.variable_name
        info_type      = cls.info_type
        expected_value = cls.expected_value
        unknown_type   = "INVALID_TYPE"

        # Create object, validate info
        def getAttrObject(type_in):
            return {
                "TMMI_MCR_GRAPH_GET_VAR_VALID"  : [ TMMI_MCR_GRAPH_GET_VAR_VALID  , "validity"      ],
                "TMMI_MCR_GRAPH_GET_VAR_VALUE"  : [ TMMI_MCR_GRAPH_GET_VAR_VALUE  , "value"         ],
                "TMMI_MCR_GRAPH_GET_VAR_COLOR"  : [ TMMI_MCR_GRAPH_GET_VAR_COLOR  , "color index"   ]
            }.get(type_in, [unknown_type, unknown_type])

        mcr_type, mcr_graph_info = getAttrObject(info_type)
        if mcr_type != unknown_type:
            variable_in        = "{view_name}:{object_name}#{variable_name}".format(view_name=view_name, object_name=object_name, variable_name=variable_name)
            get_object         = MsgMCRHciDumpGuiData(type_in = mcr_type, variable_in = variable_in)
            get_info_name      = "Get {object_name}'s {variable_name} {mcr_graph_info}".format(object_name=object_name, variable_name=variable_name, mcr_graph_info=mcr_graph_info)
            validate_info_name = "Validate that the {mcr_graph_info} of the variable {variable_name} in the graph {object_name} is {expected_value}".format(mcr_graph_info=mcr_graph_info, variable_name=variable_name, object_name=object_name, expected_value=expected_value)
        else:
            get_info_name      = "Get invalid type"
            validate_info_name = "Validate invalid type"

        if cls.name != "":
            name = cls.name
        else:
            name = validate_info_name
        
        # validate
        if isinstance(expected_value, bool):
            validate_object = MsgTypeBoolean("{view_name}:{object_name}#{variable_name}:{info_type}".format(view_name=view_name,object_name=object_name, variable_name=variable_name, info_type=info_type), value=expected_value)
        elif isinstance(expected_value, (float, int)):
            validate_object = MsgTypeNumeric("{view_name}:{object_name}#{variable_name}:{info_type}".format(view_name=view_name,object_name=object_name, variable_name=variable_name, info_type=info_type), value=expected_value)
        elif isinstance(expected_value, str):
            validate_object = MsgTypeString("{view_name}:{object_name}#{variable_name}:{info_type}".format(view_name=view_name,object_name=object_name, variable_name=variable_name, info_type=info_type), value=expected_value)
        else:
            name = "Invalid data type"
            validate_object = MsgTypeString("{view_name}:{object_name}#{variable_name}:{info_type}".format(view_name=view_name,object_name=object_name, variable_name=variable_name, info_type=info_type), value=expected_value)

        info_exchange = [
                        InformationSet(get_info_name, "thriver", "mcrhci", get_object),
                        InformationSet(validate_info_name, "mcrhci", "hcitracer", validate_object)
                        ]
            
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_VALIDATE_VALUE_OF_OBJECT_STRING_ATTRIBUTE(ClinicalIntegrationTestProcedure):
    """
    This class is used to get the Object's string attribute in the specific view.
    Variables:
        name:                   optional  - if a different format name is needed, this field should be overwritten
        view_name:              mandatory - the name of the view including the object (e.g.: view_name = "pts_layout")
        object_name:            mandatory - the name of the object to be checked (e.g.: object_name = "rectangle_1")
        expected_string_value:  mandatory - the expected string value (e.g: "111.11", "1234", "HelloWorld")
    """
    name = ""
    view_name = ""
    object_name = ""
    expected_string_value = ""

    def __init__(self, test):
        cls = type(self)
        name = cls.name
        view_name = cls.view_name
        object_name = cls.object_name
        expected_string_value = cls.expected_string_value
        if cls.name != "":
            name = cls.name
        else:
            name = "Validate object's string attribute with view: {view_name}:{object_name} = {expected_string_value}".format(view_name=view_name, object_name=object_name, expected_string_value=expected_string_value)
        
        get_object_string_attr = MsgMCRHciDumpGuiData(type_in = TMMI_MCR_OBJECT_GET_TEXT_ATTR, variable_in = "{view_name}:{object_name}".format(view_name=view_name, object_name=object_name))
        validate_object_string_attr = MsgTypeString("{view_name}:{object_name}:TMMI_MCR_OBJECT_GET_TEXT_ATTR".format(view_name=view_name, object_name=object_name), expected_string_value)
        info_exchange = [ 
                        InformationSet("Get object's string attribute with view: {view_name}:{object_name}".format(view_name=view_name, object_name=object_name), "thriver", "mcrhci", get_object_string_attr),
                        InformationSet("Validate object's string attribute with view: {view_name}:{object_name}".format(view_name=view_name, object_name=object_name), "mcrhci", "hcitracer", validate_object_string_attr),
                        ]
            
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = [] 
