from concurrent import futures
import grpc
import word_parser_pb2
import word_parser_pb2_grpc
from docx import Document
import json
import io

from jsonfy_docx_xml import jsonfy_book


class WordParserServicer(word_parser_pb2_grpc.WordParserServicer):
    def ParseWord(self, request, context):
        file_content = request.file_content
        document = Document(io.BytesIO(file_content))
        json_content = self.parse_document(document)
        return word_parser_pb2.WordResponse(json_content = json.dumps(json_content, ensure_ascii=False, indent=4))

    def parse_document(self, document):
        book_json = jsonfy_book(document)
        return book_json

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    word_parser_pb2_grpc.add_WordParserServicer_to_server(WordParserServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
