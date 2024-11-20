import ollama
import json

def llamaInfer(filepath : str, outputpath : str):

    llamaPrompt = '''
For the following Python code, infer the type of all variables, output in json format {variable name : type } \n
                  '''

    SourceCode = ""
    with open(filepath, 'r') as src:
        SourceCode = src.read()

    llamaPrompt += SourceCode

    response = ollama.generate(
        model = 'llama3.1',
        prompt= llamaPrompt,
        format = 'json',
        options = {'temperature':0}
    )

    result = json.loads(response['response'])

    with open(outputpath, "w") as json_file:

        json.dump(result, json_file, indent=4)

    return result


print(llamaInfer('example.py', 'OutputOllama.json'))

    