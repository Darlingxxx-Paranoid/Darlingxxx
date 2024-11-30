import ast
import json
class GetStructure():

    def __init__(self):

        self.result = {
            'class' : {},
            'function' : {},
            'variables' : {}
        }

        #self.model = [{'<type>' : '<probability>'}, {'<type>' : '<probability>'}, {'<type>' : '<probability>'}]

    def format_annotation(self, annotation):
        if annotation is None:
            return None
        # 获取源代码中的类型标注
        source_code = ast.unparse(annotation)
        # 去除字符串两侧的引号
        source_code = source_code.strip('"')
        # 去除 typing. 前缀
        source_code = source_code.replace('typing.', '')
        return source_code
    
    def get_variable_types(self, node):

        variables = {}
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    variables[target.id] = None
        elif isinstance(node, ast.AnnAssign):
            if isinstance(node.target, ast.Name):
                variables[node.target.id] = self.format_annotation(node.annotation)
        return variables


    def extract_function_data(self, func_node):

        function_data = {
            "name": func_node.name,
            "param": {},
            "variables": {}
        }

        # 获取参数类型
        for arg in func_node.args.args:
            # 获取函数参数的类型标注
            #function_data["param"][arg.arg] = 
            if arg.annotation:
                function_data["param"][arg.arg] = self.format_annotation(arg.annotation)
            else:
                function_data["param"][arg.arg] = None

        # 获取局部变量
        # function_data["variables"] = self.get_variable_types(func_node)
        for item in func_node.body:
            if isinstance(item, ast.Assign) or isinstance(item, ast.AnnAssign):
                function_data['variables'].update(self.get_variable_types(item))

        return function_data


    def extract_class_data(self, class_node):

        class_data = {
            "name": class_node.name,
            "functions": {},
            "variables": {}
        }

        # 提取类的函数和变量
        for item in class_node.body:
            if isinstance(item, ast.FunctionDef):
                class_data["functions"][item.name] = self.extract_function_data(item)
            elif isinstance(item, ast.Assign) or isinstance(item, ast.AnnAssign):
                class_data["variables"].update(self.get_variable_types(item))

        return class_data


    def extract_variables_and_functions(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            tree = ast.parse(file.read())

        data = {
            "variables": {},
            "functions": {},
            "classes": {}
        }

        # 提取全局变量和函数以及类
        for node in tree.body:
            if isinstance(node, ast.Assign) or isinstance(node, ast.AnnAssign):
                data["variables"].update(self.get_variable_types(node))
            elif isinstance(node, ast.FunctionDef):
                f = self.extract_function_data(node)
                data["functions"][f['name']] = f
            elif isinstance(node, ast.ClassDef):
                c = self.extract_class_data(node)
                data["classes"][c['name']] = c

        return data


    def write_to_json(self, file_path, data):
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)

    def get(self, filepath):
        data = self.extract_variables_and_functions(filepath)
        return data

    def save(self, srcpath, outputpath):
        data = self.extract_variables_and_functions(srcpath)
        self.write_to_json(outputpath, data)
        
if __name__ == '__main__':
    gs = GetStructure()
    gs.save('./sample/test.py', './sample/structure_test.json')