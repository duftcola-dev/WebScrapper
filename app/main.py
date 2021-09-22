
#STANDARD LIBS
from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Optional



#MAIN LIBS/MODULES
from source.Interface import Interface
from source.libs.DirectoryTreeGenerator_lite import TreeExplorer

#INITIALIZE MAIN MODULES
tree=TreeExplorer()
tree.ExploreDirectories(path="",mode="",ignore=["static","__pycache__","__init__.py","templates","test","venv"])
interface=Interface(tree.Files_Registry["config.json"])

#INNITIALIZE FASTAPI
app=FastAPI()
app.mount("/static",StaticFiles(directory="static"),name="static")
templates=Jinja2Templates(directory="templates")





@app.get("/",response_class=HTMLResponse)
async def Index(request:Request):
    
    return templates.TemplateResponse("index.html",{"request":request})



@app.get("/url/")
async def Url(target_url:str):

    print(f"Fetching : {target_url}")
    response=interface.MainProcess(target_url)
    return {"response":response}