from docx.oxml.ns import qn

from jsonfy_docx_xml.elements.paragraph import paragraph
from jsonfy_docx_xml.elements.table import table


class Section:
    yieldTag = {qn("w:p"): paragraph, qn("w:tbl"): table}

    def __init__(self, paragraphs):
        self.sectionTitle = paragraphs.pop(0);
        self.elements = paragraphs

    def to_json(self, doc):
        section_json = {"sectionTitle": self.sectionTitle.text}

        content = []
        for element in self.elements:
            if element.tag in Section.yieldTag:
                content.append(Section.yieldTag[element.tag](element).to_json(doc))

        section_json["content"] = content

        return section_json