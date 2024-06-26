from docx import Document

from jsonfy_docx_xml import build_iterators
from jsonfy_docx_xml.elements.run import run

input_path = r'./docs/input2.docx'
build_iterators()
document = Document(input_path)
paragraphs = document.paragraphs
paragraph = paragraphs[0]
runs = paragraph.runs
run1 = runs[1]
r_element = run(run1.element)
r_json =  r_element.to_json(document)
print()
