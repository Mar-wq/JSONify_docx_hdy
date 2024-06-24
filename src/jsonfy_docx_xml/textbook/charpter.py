from jsonfy_docx_xml.textbook.section import Section

class Charpter:
    def __init__(self, paragraphs):
        self.chapterTitle = paragraphs.pop(0);
        self.sections = Charpter.split_charpter_into_sections(paragraphs)


    def to_json(self, doc):
        charpter_json = {"charpterTitle": self.chapterTitle.text}
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