import json

from .libs.MongoDriver import MgDriver
from .libs.SearchProcess import Proccess
from .models.models import TempModel
from .libs.Interfaces.MongoAtlasInterface import MongoAtlasInterface
from .libs.Interfaces.SearchProcessInterface import SearchProccessInterface

class Interface(MongoAtlasInterface,SearchProccessInterface):

    def __init__(self,confile_url:str) -> None:

        file= open(confile_url,"r")
        content=json.load(file)
        file.close()
        database=content.get("database")
        self.database=database["database"]
        self.table=database["table"]

        self.__Initialize(database=self.database,table=self.table)



    def __Initialize(self,**kargs):

        self.mongoinstance=MgDriver(kargs["database"],kargs["table"])
        self.explorer_proccess=Proccess()


    def ExploreUrl(self,url:str)->list:
        
        result=self.explorer_proccess.ExploreUrl(url)
        return result



    def GetLinks(self)->list:
        
        result=self.explorer_proccess.GetLinks()
        return result



    def GetItem(self,table:str,id:str=None)->dict:
        
        if table =="":
            return False
            
        result=self.mongoinstance.GetData(table,"_id",id)
        return result



    def GetItems(self,table)->list:

        result=self.mongoinstance.GetItems(table)
        return result


    def UpdateItem(self,table,id,data)->bool:

        result=self.mongoinstance.UpdateItem(table,id,data)
        return result


    def DeleteItem(self,table,id=None)->bool:

        result=self.mongoinstance.DeleteItem(table,id)
        return result


    def MainProcess(self,target_url:str):

        model=TempModel()
        response=model.response

        previous_sample=self.GetItem(self.table,target_url)
        if type(previous_sample) != bool:

            previous_sample=previous_sample["links"]
        else:
            previous_sample=[]
            
        result=self.ExploreUrl(target_url)

        if type(result) == list:

            response["links"]=self.GetLinks()
            

            if type(previous_sample) is not bool:

                response["stored"]=previous_sample
            else:
                response["stored"]=[""]


            old_list=set()
            new_list=set()

            old_list.update(response["stored"])
            new_list.update(response["links"])

            temp=old_list.difference(new_list)
            response["differences"]=temp


            id=target_url
            data={"links":response["links"]}
            self.UpdateItem(self.table,id,data)
            response["message"]="URL fetched succesfully"

        else:

            response["links"]=[]
            response["stored"]=[]
            response["differences"]=[]
            response["message"]=f"Unalbe to fetch url . 1) Check the provided url : {target_url} is valid or exists. 2) This process only works with static html sites"

        return response