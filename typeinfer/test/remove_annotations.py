import ast
import astor
import re

class GetStructure():
    def remove_annotations(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            tree = ast.parse(file.read())

        # 使用ASTVisitor来遍历和修改节点（更推荐的方式）
        class AnnotationRemover(ast.NodeTransformer):
            def visit_AnnAssign(self, node):
                # 直接移除AnnAssign节点中的annotation和冒号（通过转换回Assign）
                if isinstance(node.target, ast.Name):
                    return ast.Assign(targets=[node.target], value=node.value)
                return node

            def visit_FunctionDef(self, node):
                # 复制args对象，避免直接修改原始对象
                #new_args = node.args.copy()
                new_args = ast.arguments(
                    args=[ast.copy_location(ast.arg(arg.arg, arg.annotation), arg) for arg in node.args.args],
                    vararg=node.args.vararg and ast.copy_location(ast.arg(node.args.vararg.arg, None), node.args.vararg),
                    kwonlyargs=[ast.copy_location(ast.arg(arg.arg, arg.annotation), arg) for arg in node.args.kwonlyargs],
                    kwarg=node.args.kwarg and ast.copy_location(ast.arg(node.args.kwarg.arg, None), node.args.kwarg),
                    defaults=[None if default is None else ast.copy_location(default, default) for default in node.args.defaults],
                    kw_defaults=[None if kw_default is None else ast.copy_location(kw_default, kw_default) for kw_default in node.args.kw_defaults]
                )
                # 移除函数参数的类型标注，但保留参数本身（通过将annotation设置为None）
                for arg in new_args.args + new_args.kwonlyargs:
                    arg.annotation = None
 
                # 更新函数定义中的args
                node.args = new_args
                return self.generic_visit(node)

            def visit_arg(self, node):
                # 移除参数的类型标注
                node.annotation = None
                return node

        transformer = AnnotationRemover()
        new_tree = transformer.visit(tree)

        return new_tree

    def save(self, file_path, output_path):
        tree = self.remove_annotations(file_path)
        new_code = astor.to_source(tree)
        '''
        # 使用正则表达式清理可能的遗留冒号和空格
        new_code = re.sub(r':\s*=\s*', '=', new_code)  # 清理变量声明后的冒号和空格
        new_code = re.sub(r':\s*\n', '\n', new_code)  # 清理行尾的冒号和空格
        '''
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(new_code)

if __name__ == '__main__':
    gs = GetStructure()
    gs.save('./sample/test.py', './sample/remove_annotations_test.py')