
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

class SETUP_DELETE_FILE(ClinicalIntegrationTestProcedure):
    # default variable value, need to defind value at the class inheritance
    name = "Delete file and check that the file no longer exists"
    path_check = None

    def __init__(self, test):
        cls = type(self)
        name = cls.name
        path_check = self.path_check

        exist_check = False
        permission_check = None
        content_check = None

        delete_file = TcsExecuteExtCmd("rm {path_check}".format(path_check=path_check))
        validate_file_not_exist = MsgPathCheck(path_check=path_check, exist_check=exist_check, permission_check=permission_check, content_check=content_check)

        info_exchange = [
                        InformationSet("delete file :{path_check}".format(path_check=path_check), "thriver", "mcrhci", delete_file),
                        InformationSet("check file not exist", "thriver", "mcrhci", validate_file_not_exist),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_CHANGE_PERMISSION_AND_RECHECK_FILE(ClinicalIntegrationTestProcedure):
    # default variable value, need to defind value at the class inheritance
    name = "Change permission and recheck file"
    path_check = None
    permission_check = None

    #for convert "777" to "rwxrwxrwx"
    def convert_mode(self, mode):
        if not isinstance(mode, int):
            mode = int(mode, 8)
        perm_string = ''
        for i in range(9):
            if mode & (1 << i):
                if i % 3 == 0:
                    perm_string = 'x' + perm_string
                elif i % 3 == 1:
                    perm_string = 'w' + perm_string
                elif i % 3 == 2:
                    perm_string = 'r' + perm_string
            else:
                perm_string = '-' + perm_string
        return perm_string

    def __init__(self, test):
        cls = type(self)
        name = cls.name
        path_check = self.path_check
        permission_check = self.permission_check

        content_check = None
        exist_check = True
        permission_check_rwx = self.convert_mode(int(permission_check, 8))

        delete_file = TcsExecuteExtCmd("chmod {permission_check} {path_check}".format(permission_check=permission_check, path_check=path_check))
        validate_file_permission = MsgPathCheck(path_check=path_check, exist_check=exist_check, permission_check=permission_check_rwx, content_check=content_check)

        info_exchange = [
                        InformationSet("change permssion of file:{path_check} to {permission_check} = {permission_check_rwx}".format(path_check=path_check, permission_check=permission_check, permission_check_rwx=permission_check_rwx), "thriver", "mcrhci", delete_file),
                        InformationSet("check permssion of file: {permission_check} = {permission_check_rwx}".format(permission_check=permission_check, permission_check_rwx=permission_check_rwx), "thriver", "mcrhci", validate_file_permission),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_CHECK_CONTENT_FILE(ClinicalIntegrationTestProcedure):
    # default variable value, need to defind value at the class inheritance
    name = "Check content of file"
    path_check = None
    content_file = None

    def __init__(self, test):
        cls = type(self)
        name = cls.name
        path_check = self.path_check
        content_file = self.content_file

        exist_check = True
        permission_check = None

        validate_content_file = MsgPathCheck(path_check=path_check, exist_check=exist_check, permission_check=permission_check, content_check=content_file)

        info_exchange = [
                        InformationSet("check content file", "thriver", "mcrhci", validate_content_file),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []

class SETUP_CREATE_NEW_EMPTY_FILE(ClinicalIntegrationTestProcedure):
    # default variable value, need to defind value at the class inheritance
    name = "Create new empty file"
    path_file = None

    def __init__(self, test):
        cls = type(self)
        name = cls.name
        path_file = self.path_file

        exist_check = True
        permission_check = None

        create_empty_file = TcsExecuteExtCmd("rm -f {path_file} ; touch {path_file}".format(path_file=path_file))

        info_exchange = [
                        InformationSet("create new empty file: {path_file}".format(path_file=path_file), "thriver", "mcrhci", create_empty_file),
                        ]

        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup = []
        self.teardown = []