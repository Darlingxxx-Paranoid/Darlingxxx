import ollama
import json
from llamaInfer import Prompt
import sys


def llamaInfer(filepath : str):

    llamaPrompt = Prompt.GetPrompt(filepath)

    response = ollama.generate(
        model = 'llama3.1',
        prompt= llamaPrompt,
        format = 'json',
        options = {'temperature':0}
    )

    # result = json.loads(response['response'])
    result = response['response']

  #   with open(outputpath, "w") as json_file:

    #    json.dump(result, json_file, indent=4)

    return result
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python llamaInfer.py <python_file_path>")
        sys.exit(1)
    
    result = llamaInfer(sys.argv[1])
    print(result)