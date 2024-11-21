import ollama
import json
import Prompt

def llamaInfer(filepath : str, outputpath : str):

    llamaPrompt = Prompt.GetPrompt(filepath)

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
    