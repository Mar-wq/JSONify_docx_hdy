from docx import Document



input_path = r'./docs/input2.docx'
document = Document(input_path)
styles_list = []
styles =  document.styles
for style in styles:
    styles_list.append({"Style ID": style.style_id, "Style Name": style.name})

print()