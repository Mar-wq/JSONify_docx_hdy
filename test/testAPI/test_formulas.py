from docx import Document
from docx.oxml.ns import qn

from jsonfy_docx_xml.elements.paragraph import paragraph
from jsonfy_docx_xml.elements.run import run
from jsonfy_docx_xml.iterators.generic import build_iterators

input_path = r'./docs/input_formulas.docx'
document = Document(input_path)
temp = qn("m:oMath")
paragraph_2 =  document.paragraphs[2]
paragraph_element = paragraph(paragraph_2._element)
build_iterators()
formula_json =  paragraph_element.to_json(document)
print()