root_pwd = r'D:\02_Git\VBA'


import re
import os
import shutil

testCaseTemplate = \
'''
from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

ClassImport

ClassInherritance

class __TestCaseName__(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        TestCaseDescription
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [
TestSteps
                        ]
        self.teardown_path = []
'''
testSuiteTemplate = \
'''
from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

TestCaseInport

class test_TestSuiteName(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "test_TestSuiteName"
        
        treatment_test_list = [
Treatment_test_list
                            ]
        service_test_list = [
Service_test_list
                            ]
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange, List_register_v_file)
        self.applicable_rooms = ['mcr']
        self.setup =    [  
TestCaseName
                        ]
        self.teardown_path = []
'''

def convert_to_uppercase(text):
    text = str(text).replace(r"\LF", "").replace(r"\n", "").replace(r" ", "_").replace(r".", "_").replace(r",", "_").replace(r":", "_").replace(r"\t", "_")
    text = text.replace(r"'", "_").replace(r'"', "_")
    uppercase_text = text.upper()
    return uppercase_text

def validate_text(text, is_leading_degit=False):
    text = str(text).replace(r"\LF", "")
    text = re.sub(r'[^a-zA-Z0-9_]', '', text)
    text = text.replace(' ', '').replace(r'\t', '').replace('	',"")
    if not is_leading_degit and text and text[0].isdigit():
        text = text[1:]
    return text

testSuiteName = ''
Treatment_test_list = ''
Service_test_list = ''

def crab_testcases():
    global testSuiteName
    global Treatment_test_list
    global Service_test_list
    a =  open(os.path.join(root_pwd,'data.txt'), 'r')
    data = a.readlines()
    content = []

    enable = False
    for i in data:
        if 'TestSuite Name' in i:
            testSuiteName = validate_text(i.split('"$C$29":"')[1].split('"')[0]).replace('py','')
        elif 'Treatment test list' in i:
            print(i)
            a = i.split('","')
            for b in a:
                if('$C$30":"' in b):
                    c = b.replace('$C$30":"','').replace(" ","").split(',')
                    for d in c:
                        if(d != ""):
                            Treatment_test_list += f'                            "{d}",\n'
        elif 'Service test list:' in i:
            print(i)
            a = i.split('","')
            for b in a:
                if('$C$31":"' in b):
                    c = b.replace('$C$31":"','').replace(" ","").split(',')
                    for d in c:
                        if(d != ""):
                            Service_test_list += f'                            "{d}",\n'                        
        if 'Test No.' in i:
            enable = True
            continue
        if enable:
            content.append(i)

    testCase = []
    temp = []      
    enable = False 
    for i in content:
        if re.search('^\{"\$A\$\d+":' , i) and not re.search('"\$B\$\d+":""' , i):
            enable = True
            if len(temp) >0:
                testCase.append(temp)
            temp = []
            temp.append(i)
        else:
            if enable:
                temp.append(i)
    testCase.append(temp)

    testCases = []
    for i in testCase:
        temp = []
        i = str(i).replace("\n", "").replace("$", "").replace('[\'{"',"").split('","')
        for j in i:
            print(j)
            if j[0] == 'H' or j[0] == 'I' or (not re.search('^\w+\d+":""',j) and not re.search('^\w+\d+":"$',j)):
                temp.append(j)
                print(j)
        testCases.append(temp)
        temp = []
    return testCases    

testCases = crab_testcases()

count = 0
for i in testCases:
    count += 1
    # if count > 3:
    #     break    
    print("======================> ")
    for j in i:
        print(j)
# while(True):
#     None

main_folder = f"test_{testSuiteName}"
main_folder_path = os.path.join(root_pwd, main_folder)
print(os.getcwd())
if os.path.exists(main_folder_path):
    shutil.rmtree(main_folder_path)
os.mkdir(main_folder_path)
sub_folder = f"test_{testSuiteName}_test_cases"
sub_folder_path = os.path.join(main_folder_path, sub_folder)
os.mkdir(sub_folder_path)

count = 0
test_case_file_created = []
for i in testCases:
    count += 1
    # if count > 3:
    #     break
    print("======================> ")
    G = []
    H = []
    class_inherritance = []
    file_import = []
    for j in i:
        if j[0] == 'A':
            testCaseName = validate_text(j.split('":"')[1])
        elif j[0] == 'B':
            testCaseNameDescription = j.split('":"')[1]
        elif j[0] == 'I':
            file_import.append(j.split('":"')[1])
        elif j[0] == 'G':
            G.append(j.split('":"')[1])       
        elif j[0] == 'H':
            H.append(j.split('":"')[1])  
    file_import = list(set(file_import))
    print(f"testCaseName: {testCaseName}")    
    print(f"testCaseNameDescription: {testCaseNameDescription}")    
    print(f"file_import: {file_import}")   
    for g in G: 
        print(f"G: {g}")
    for h in H:    
        print(f"H: {h}")                
    content = testCaseTemplate.replace("TestCaseName", f"{testCaseName}".replace("'",'"'))
    content = content.replace("TestCaseDescription", f'name = "{testCaseNameDescription}"')
    ClassImport = ""
    for i in file_import:
        if(i != ""):
            ClassImport += f"from procedures.thriver.test_itp_mcrhci.SETUP.nameTestCase import *\n".replace('nameTestCase',i.replace(".py",""))
    content = content.replace("ClassImport", f"{ClassImport}")

    ClassInherritance = ""
    TestSteps = ""
    if len(G) == len(H):
        for i in range(0, len(G)):
            a = ""
            if ("=" in H[i]):
                a = "_" + H[i].split("', '")[0].split("=")[1]
            name_class_inheritance = validate_text(G[i].replace('SETUP_',"")+ validate_text(convert_to_uppercase(a),is_leading_degit=True))
            print(f"====[name_class_inheritance]====> {name_class_inheritance}")
            if name_class_inheritance not in class_inherritance:
                class_inherritance.append(name_class_inheritance)
                if( not "=" in H[i]):
                    ClassInherritance += 'class AA(BB): pass\n'.replace("AA",name_class_inheritance).replace("BB",G[i]) 
                else:
                    ClassInherritance += 'class AA(BB):\n'.replace("AA",name_class_inheritance).replace("BB",G[i]) 
                    for a in H[i].replace("', '","").replace(r'\t',"").split(r'\n'):
                        ClassInherritance += f'    {a}\n'
            TestSteps += f"                        {name_class_inheritance},\n"
    content = content.replace("ClassInherritance", f"{ClassInherritance}")
    content = content.replace("TestSteps", f"{TestSteps}")
    
    a_file_path = os.path.join(sub_folder_path, f"{testCaseName}.py")
    # Check if file exists
    if os.path.exists(a_file_path):
        # Append prefix "_1" to the file name
        a_file_path = a_file_path.replace(".py", "_1.py")
    # Create the file
    with open(a_file_path, "w", newline="\n") as f:
        test_case_file_created.append(a_file_path.replace(".py","").split("\\")[-1])    
        f.write(content)
        pass


#for write testStuit
b_file_path = os.path.join(main_folder_path, f"test_{testSuiteName}.py")
content = testSuiteTemplate.replace('TestSuiteName',f"{testSuiteName}")
TestCaseName = ""
TestCaseInport = ""
for i in test_case_file_created:
    TestCaseName += f"                        __{i}__,\n"
    TestCaseInport += f"from procedures.thriver.test_itp_mcrhci.{main_folder}.{sub_folder}.{i} import __{i}__\n"
content = content.replace('TestCaseName',f"{TestCaseName}")  
content = content.replace('TestCaseInport',f"{TestCaseInport}")    

if(Treatment_test_list != ""):
    content = content.replace('Service_test_list',"")   
    content = content.replace('Treatment_test_list',f"{Treatment_test_list}")  
    content = content.replace('List_register_v_file',"treatment_test_list=treatment_test_list")   
else:
    content = content.replace('Treatment_test_list',"")  
    content = content.replace('Service_test_list',f"{Service_test_list}")   
    content = content.replace('List_register_v_file',"service_test_list=service_test_list")   
    
with open(b_file_path, "w", newline='\n') as f:
    f.write(content)
    pass





