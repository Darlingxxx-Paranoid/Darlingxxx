from GetStructure import GetStructure
from llamaInfer import llamaInfer

structure = GetStructure()
structure.save('examples/code/test1.py', 'examples/result/test1/Structure.json')
llamaInfer('examples/code/test1.py', 'examples/result/test1/Ollama.json')