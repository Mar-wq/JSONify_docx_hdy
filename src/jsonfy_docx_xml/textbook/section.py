from docx.oxml.ns import qn

from jsonfy_docx_xml.elements.paragraph import paragraph
from jsonfy_docx_xml.elements.table import table
from jsonfy_docx_xml.utils.methods import get_paragraph_format_through_styleId


class Section:
    yieldTag = {qn("w:p"): paragraph, qn("w:tbl"): table}

    def __init__(self, paragraphs):
        self.sectionTitle = paragraphs.pop(0)
        self.elements = paragraphs

    def to_json(self, doc):
        #temp =  Section.yieldTag[self.sectionTitle.tag](self.sectionTitle).to_json(doc)
        section_json = {"sectionTitle": self.sectionTitle.text, "content":Section.yieldTag[self.sectionTitle.tag](self.sectionTitle).to_json(doc)}
        #section_json = {"sectionTitle": self.sectionTitle.text}
        section_json.update(get_paragraph_format_through_styleId(self.sectionTitle))


        content = []
        for element in self.elements:
            if element.tag in Section.yieldTag:
                content.append(Section.yieldTag[element.tag](element).to_json(doc))

        section_json["paragraphs"] = content

        return section_json