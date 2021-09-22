from typing import List
import json
from pydantic import BaseModel,ListError


class TempModel():

    def __init__(self) -> None:

        self.response={
            "stored":[],
            "links":[],
            "differences":[],
            "message":""
        }

    def Json(self,response:dict):

        response_json=json.dumps(response)
        return response_json


class OutputModel(BaseModel):

    stored:List[str]=[]
    links:List[str]=[]
    differences:List[str]=[]
    message:str