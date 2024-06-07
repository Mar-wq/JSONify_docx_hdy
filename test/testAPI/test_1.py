import docx
from jsonfy_docx import simplify

input_path = r'./docs/input.docx'
my_doc = docx.Document(input_path)

my_doc_as_json = simplify(my_doc,{"remove-leading-white-space":False})
print()