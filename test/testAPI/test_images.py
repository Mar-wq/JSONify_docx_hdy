import base64
#  主要是测试图片本身的json化
from docx import Document
from docx.oxml.ns import qn
from jsonfy_docx_xml.elements.run import run
from jsonfy_docx_xml.iterators.generic import build_iterators
from PIL import Image
from io import BytesIO

temp =  qn("w:drawing")
input_path = r'./docs/input2.docx'
document = Document(input_path)
paragraph =  document.paragraphs[0]
run_0 = paragraph.runs[0];
build_iterators()
json_run = run(run_0._element).to_json(document)
blob =  json_run['VALUE'][0]['blob']
blob = base64.b64decode(blob)
Image.open(BytesIO(blob)).show()
print()