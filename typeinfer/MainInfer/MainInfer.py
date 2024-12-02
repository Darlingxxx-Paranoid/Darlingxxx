from llamaInfer.llamaInfer import llamaInfer
import sys
import json

#判断结果是否符合格式
def validate_format(json_string):
    try:
        data = json.loads(json_string)
    except json.JSONDecodeError:
        return False

    if not isinstance(data, dict):
        return False

    # Check for the presence of the top-level keys
    required_keys = {"variables", "functions", "classes"}
    return required_keys.issubset(data.keys())

def MainInfer(filepath : str):
    result=""
    while not validate_format(result):
        result=llamaInfer(filepath)
    return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python llamaInfer.py <python_file_path>")
        sys.exit(1)
    
    result = MainInfer(sys.argv[1])
    print(result)