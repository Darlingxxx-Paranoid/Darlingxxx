from MainInfer.MainInfer import MainInfer
import sys


def Infer(filepath : str):

    return MainInfer(filepath)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python llamaInfer.py <python_file_path>")
        sys.exit(1)
    
    result = Infer(sys.argv[1])
    print(result)