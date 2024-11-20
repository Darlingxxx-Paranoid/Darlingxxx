from GetStructure import GetStructure


def GetPrompt(filepath):

    llamaPrompt = '''
For the following Python code, infer the type of all variables \n
'''

    SourceCode = ""
    with open(filepath, 'r') as src:
        SourceCode = src.read()

    llamaPrompt += SourceCode

    llamaPrompt += '''
Then fill in all '['type':'probability']' in the following json format to show the result\n
'''
    
    structure = GetStructure()
    llamaPrompt += str(structure.get(filepath))

    return llamaPrompt