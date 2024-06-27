from docx import Document
from docx.oxml.ns import qn

input_path = r'./docs/input2.docx'
document = Document(input_path)
tag = qn("w:commentRangeStart")
comments = document.comments
print()