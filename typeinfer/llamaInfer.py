import ollama
import sys

def llamaInfer(filepath: str):
    llamaPrompt = '''
For the following Python code, infer the type of all variables, output in json format {variable name : type } \n
                  '''

    with open(filepath, 'r') as src:
        SourceCode = src.read()

    llamaPrompt += SourceCode

    response = ollama.generate(
        model='llama3.1',
        prompt=llamaPrompt,
        format='json',
        options={'temperature': 0}
    )

    return response['response']

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python llamaInfer.py <python_file_path>")
        sys.exit(1)
    
    result = llamaInfer(sys.argv[1])
    print(result)

    