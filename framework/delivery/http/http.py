from usecase import Usecase
from fastapi.responses import JSONResponse
from fastapi import FastAPI
from framework.error import Error

router_group = "/api/v1/project"

class HttpDelivery:
    usecase = Usecase
    error = Error()
    def __init__(self, app:FastAPI):
        self.app = app
    def delivery_http(self):
        @self.app.get(router_group)
        def list_project():
            try:
                self.usecase = Usecase()
                response = self.usecase.get_data()
                return JSONResponse(response, status_code=response['code'])
            except Exception as e:
                return self.error.error(e)