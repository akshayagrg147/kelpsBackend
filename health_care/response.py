from rest_framework.response import Response


class JsendSuccessResponse:
    def __init__(self, status, data, pages = None, message: str = ""):
        print(type(data))
        if pages:
            self.response = {"status": status, "total_pages" : pages,  "data": data, "message" : message}
        
        else:
            self.response = {"status": status, "data": data, "message" : message}
            

    def get_response(self):
        return Response(self.response)   