from GetStructure import GetStructure
from llamaInfer import llamaInfer

def test(filename):
    structure = GetStructure()
    structure.save('examples/code/' + filename + '.py', 'examples/result/' + filename + '/Structure.json')
    llamaInfer('examples/code/' + filename + '.py', 'examples/result/' + filename + '/llama.json')


test('test3')