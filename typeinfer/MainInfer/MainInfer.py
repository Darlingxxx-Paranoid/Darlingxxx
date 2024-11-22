from llamaInfer.llamaInfer import llamaInfer
import sys

def MainInfer(filepath : str):

    return llamaInfer(filepath)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python llamaInfer.py <python_file_path>")
        sys.exit(1)
    
    result = MainInfer(sys.argv[1])
    print(result)