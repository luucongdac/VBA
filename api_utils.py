root_pwd = r'D:\02_Git\VBA'

path_workbook = r'D:\02_Git\VBA'
path_source = r'D:\02_Git\VBA\test_itp_mcrhci\SETUP'



#path_source = r'D:\02_Git\VBA\test_itp_mcrhci\SETUP'
#path_workbook = r'D:\02_Git\VBA'


import os
import re

def read_files(path):
    file_contents = {}
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    content = f.readlines()
                    file_contents[file] = content
    return file_contents

file_contents = read_files(path_source)

# # In n?i dung t? di?n
# for file, content in file_contents.items():
#     print(f"File: {file}")
#     print(f"Content:\n{content}")
#     print()  


TestCases = []
for file, content in file_contents.items():
    enable = False
    for line in content:
        line = line.replace('\n','').replace("	","    ")
        a = re.search('^class\s+(.*)\(', line)
        if(a and 'ClinicalIntegrationTestProcedure' in line):
            TestCase = []
            TestCase.append(file)
            enable = True

        if('def' in line and '__init__' in line):
            enable = False
            # print(TestCase)
            if(len(TestCase)>0):
                TestCases.append(TestCase)
        if(enable):
            if(a):
                TestCase.append(a.group(1).replace(" ","").replace("\t","").replace("\n",""))
            else:
                TestCase.append(line)

write_to_file = []
for i in TestCases:
    print("==============>")
    full = "ENTERLINE".join(i)
    file = i[0]
    name = i[1]
    overwrite = ''
    for j in i:
        # print(j)
        a = re.search('^\s{4}([\d\w_]+\s*=\s*.*)',j)
        if(a):
            if("#" in a.group(1)):
                overwrite += a.group(1).replace("    ","").split("#")[0] + 'ENTERLINE'
            else:
                overwrite += a.group(1).replace("    ","") + 'ENTERLINE'
    # print(full)
    # print("-----")
    # print(file)
    # print("-----")
    # print(name)
    # print("-----")
    # print(overwrite)
    # print("-----")
    write_to_file.append(f"{full}####{name}####{overwrite}####{file}")
# Luu n?i dung t? di?n v�o file kh�c
with open(os.path.join(path_workbook, "api_utils.txt"), "w") as f:
    # for file, content in file_contents.items():
    #     f.write(f"File: {file}\n")
    #     f.write(f"Content:\n{content}\n\n")
    for i in write_to_file:
        print(i)
        f.writelines(i+ "\n")        

# while(True):
#     None
#Not change
#path_source = r'D:\02_Git\VBA\test_itp_mcrhci\SETUP'
#path_workbook = r'D:\02_Git\VBA'
