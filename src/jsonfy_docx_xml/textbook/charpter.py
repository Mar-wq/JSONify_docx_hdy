from docx.oxml.ns import qn

from jsonfy_docx_xml.textbook.section import Section
from ..elements.paragraph import paragraph
from ..elements.table import table
from ..utils.methods import get_paragraph_format_through_styleId
class Charpter:
    yieldTag = {qn("w:p"): paragraph, qn("w:tbl"): table}
    def __init__(self, paragraphs):
        self.chapterTitle = paragraphs.pop(0);
        self.sections = Charpter.split_charpter_into_sections(paragraphs)


    def to_json(self, doc):
        temp = Charpter.yieldTag[self.chapterTitle.tag](self.chapterTitle).to_json(doc)
        charpter_json = {"charpterTitle": self.chapterTitle.text, "content": Charpter.yieldTag[self.chapterTitle.tag](self.chapterTitle).to_json(doc)}
        #charpter_json = {"charpterTitle": self.chapterTitle.text}
        charpter_json.update(get_paragraph_format_through_styleId(self.chapterTitle))

        sections_json = []
        for section in self.sections:
            sections_json.append(section.to_json(doc))

        charpter_json["sections"] = sections_json

        return charpter_json

    def split_charpter_into_sections(paragraphs):
        section = []
        sections = []

        for paragraph in paragraphs:
            if hasattr(paragraph, 'style') and paragraph.style == '2':
                if section:
                    sections.append(Section(section))
                    section = []

            section.append(paragraph)

        sections.append(Section(section))

        return sections