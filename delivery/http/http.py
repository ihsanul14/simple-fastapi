import usecase
from fastapi import Response
from decouple import config
import json
from fastapi.responses import JSONResponse

router_group = "/api/v1/project"

def delivery_http(app):
    @app.get(router_group)
    def list_project():
        response = usecase.project_handler.get_data()
        print(response)
        return JSONResponse(response, status_code=response['code'])