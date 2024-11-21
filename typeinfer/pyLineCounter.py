import sys
import json

def count_lines(filepath: str):
    stats = {
        "total_lines": 0,
        "code_lines": 0,
        "blank_lines": 0,
        "comment_lines": 0
    }
    
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                stats["total_lines"] += 1
                stripped_line = line.strip()
                
                if not stripped_line:  # 空行
                    stats["blank_lines"] += 1
                elif stripped_line.startswith('#'):  # 注释行
                    stats["comment_lines"] += 1
                else:  # 代码行
                    stats["code_lines"] += 1
                    
        return stats
        
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(json.dumps({"error": "Usage: python pyLineCounter.py <python_file_path>"}))
        sys.exit(1)
    
    result = count_lines(sys.argv[1])
    print(json.dumps(result)) 