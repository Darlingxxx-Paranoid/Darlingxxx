import json
import os

N = 3
local_var_num = 0
local_var_cor = 0
local_var_error = 0

def judge_all(filedir:str):
    listdir = os.listdir(filedir)


def judge_one_file(filedir:str, filename:str):
    answers = {}
    my_answers = {}
    ret = []
    with open(filedir + filename + "_gt.json"  , 'r') as f:
        answers = json.load(f)
    with open(filedir + filename + "_infer.json"  , 'r') as f:
        my_answers = json.load(f)
    for answer in answers:
        if('variable' in answer):
            result = ""
            varname = answer['variable']
            vartype = answer['type'][0]
            if(judge_exist(varname, my_answers)):
                if(judge_match(varname, my_answers, vartype)): 
                    result += "pass"
                else:
                    result += "fail"
            else:
                result += "not found"
            ret.append({varname: result})
    with open(filedir + filename + "_judge.json", 'w') as f:
        json.dump(ret, f)


def judge_exist(varname:str, my_answers:dict):
    return 1

def judge_match(varname:str, my_answers:dict, answer:str):
    return 1