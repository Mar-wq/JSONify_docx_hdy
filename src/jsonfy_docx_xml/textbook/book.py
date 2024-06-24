import os

from jsonfy_docx_xml.textbook.charpter import Charpter

from docx import Document


class Book:
    def __init__(self, doc):
        #self.bookTitle = os.path.splitext(os.path.basename(bookPath))[0]
        self.doc = doc
        body_element = self.doc.element.body
        paragraphs = []
        for paragraph in body_element:
            paragraphs.append(paragraph)
        self.charpters = Book.split_book_into_charpters(paragraphs)

    def to_json(self):
        book_json = {}
        charpters_json = []
        for charpter in self.charpters:
            charpters_json.append(charpter.to_json(self.doc))

        book_json["charpters"] = charpters_json

        return book_json

    def split_book_into_charpters(paragraphs):
        charpter = []
        charpters = []

        for paragraph in paragraphs:
            if hasattr(paragraph, 'style') and paragraph.style == '1':
                if charpter:
                    charpters.append(Charpter(charpter))
                    charpter = []
            charpter.append(paragraph)


        charpters.append(Charpter(charpter))

        return charpters