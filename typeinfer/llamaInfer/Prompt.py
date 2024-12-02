from Structure.GetStructure import GetStructure


def GetPrompt(filepath):

    llamaPrompt = '''
For the following Python code, infer the type of all variables \n
'''

    SourceCode = ""
    with open(filepath, 'r', encoding='utf-8') as src:
        SourceCode = src.read()

    llamaPrompt += SourceCode

    llamaPrompt += '''
Then fill in all '{'<type>':'<probability>'}'with the type of the variable and the probability of the type in the following json format.\n
'''
    
    structure = GetStructure()
    llamaPrompt += str(structure.get(filepath))

    return llamaPrompt