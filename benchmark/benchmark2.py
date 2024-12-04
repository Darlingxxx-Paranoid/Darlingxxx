import json
import os
from get_all_files import get_all_files

N = 3
local_var_num = 0
local_var_cor = 0
local_var_error = []
local_var_no_found = 0;

def judge_one_file(filedir:str, filename:str):
    global local_var_cor
    global local_var_num
    global local_var_error
    global local_var_no_found
    answers = {}
    my_answers = {}
    ret = []
    with open(filedir+"\\" + filename + "_gt.json"  , 'r') as f:
        answers = json.load(f)
    with open(filedir+"\\" + "result.json"  , 'r') as f:
        my_answers = json.load(f)
    for answer in answers:
        if 'variable' in answer :
            local_var_num += 1
            result = ""
            varname = answer['variable']
            vartype = answer['type'][0]
            if(judge_exist(varname, my_answers)):
                if(judge_match(varname, my_answers, vartype)): 
                    local_var_cor += 1
                    result += "pass"
                else:
                    result += "fail"
                    local_var_error.append(vartype)
            else:
                result += "not found"
                local_var_no_found += 1
            ret.append({varname: result})
        elif 'parameter' in answer :
            local_var_num += 1
            result = ""
            varname = answer['parameter']
            vartype = answer['type'][0]
            if(judge_exist(varname, my_answers)):
                if(judge_match(varname, my_answers, vartype)): 
                    local_var_cor += 1
                    result += "pass"
                else:
                    result += "fail"
                    local_var_error.append(vartype)
            else:
                result += "not found"
                local_var_cor+=1
            ret.append({varname: result})
    with open(filedir + "/" + filename + "_judge.json", 'w') as f:
        json.dump(ret, f)


def judge_exist(varname:str, my_answers:dict):
    if varname in my_answers:
        if isinstance(my_answers[varname], list):
            return True 
   
    return False



def judge_match(varname:str, my_answers:dict, answer:str):
        for a in my_answers[varname]:
            if a == answer:
                return True

    
    

for filedir in get_all_files('result_without_structure'):
    filename = ""
    filepath = ""
    files = os.listdir(filedir)
    for file in files:
        if file.endswith(".py"):
            filepath = os.path.join(filedir, file)
            filename = file[:-3]
    judge_one_file(filedir, filename)

re = ""
re += "correct:"
re += str(local_var_cor)
re += "\n"
re += "number of all variables:"
re += str(local_var_num)
re += "\n"
re +=  "number of no found:"
re += str(local_var_no_found)
re += "\n"
re += str(local_var_error)


with open ('result_without_structure/result.txt', 'w') as f:
    f.write(re)
