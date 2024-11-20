# README

##### llamaInfer.py

示例使用：

```python
llamaInfer('example.py', 'output.json')
```

用 llama3.1 推理 example.py 类型，写入 output.json，函数返回一个 dict

示例结果：

```json
{
    "k": "int",
    "a": "int",
    "m": "int",
    "c": "int",
    "b": "int"
}
```



##### GetStructure.py

示例使用：

```python
GetStructure().get("example.py", "OutoutStructure.json")
```

函数返回一个 dict

类成员 model 是一个变量的模板推理结果：

```python
[{'type': "probability"}, {'type2': "probability"}]
```

使用时记得改成 空list

示例结果：

```json
{
    "variables": {
        "b": [
            {
                "type": "probability"
            },
            {
                "type2": "probability"
            }
        ]
    },
    "functions": [
        {
            "name": "Two",
            "param": {},
            "variables": {
                "c": [
                    {
                        "type": "probability"
                    },
                    {
                        "type2": "probability"
                    }
                ]
            }
        }
    ],
    "classes": [
        {
            "name": "A",
            "functions": {
                "__init__": {
                    "name": "__init__",
                    "param": {
                        "self": [
                            {
                                "type": "probability"
                            },
                            {
                                "type2": "probability"
                            }
                        ]
                    },
                    "variables": {}
                },
                "One": {
                    "name": "One",
                    "param": {},
                    "variables": {
                        "m": [
                            {
                                "type": "probability"
                            },
                            {
                                "type2": "probability"
                            }
                        ]
                    }
                }
            },
            "variables": {
                "k": [
                    {
                        "type": "probability"
                    },
                    {
                        "type2": "probability"
                    }
                ]
            }
        }
    ]
}
```

