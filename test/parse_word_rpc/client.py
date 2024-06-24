import grpc
import word_parser_pb2
import word_parser_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = word_parser_pb2_grpc.WordParserStub(channel)
        with open(r'I:\devlope\pycharm\pythonProjects\docx2json_hdy\test\docs\第1章 数值分析引论20240226.docx', 'rb') as f:
            file_content = f.read()
        # 创建请求对象并调用 gRPC 服务
        request = word_parser_pb2.WordRequest(file_content=file_content)
        response = stub.ParseWord(request)
        print("Parsed JSON content:", response.json_content)

if __name__ == '__main__':
    run()
