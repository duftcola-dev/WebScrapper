
from requests.models import HTTPError
from .Request import Request
from .UrlData import Data
from bs4 import BeautifulSoup



class Proccess():

    def __init__(self) -> None:

        self.iterations=0
        self.fails=0

        self.request=Request()
        self.data=Data()



    def GetLinks(self):

        if len(self.data.links) > 1:
            return self.data.links
        print("Not exploration performed yet")
        return False

    

    def ExploreUrl(self,url:str)->list:

        self.data.root=url
        self.data.links=[]
        self.data.links.append(url)
        self.data.length=len(self.data.links)
        self.iterations=0
        self.data.index=0
        print("Fetching URls ...")
        self.__Explore(self.data.links)

        print(f"Iterations : {self.iterations}")
        print(f"Fails : {self.fails}")
        print(f"Index : {self.data.index}")
        print(f"Total Urls : {len(self.data.links)}")
        
        if self.data.index==len(self.data.links):# 1)was able to run the entire list
            
            if len(self.data.links)>1:#2)there is more than one element in the list
                 
                if self.iterations != self.data.index:#3) Was able to iterate throug a tree of links
                    
                    return self.data.links 
        
        return False


    def  __Explore(self,url:str)->list:
        
        while (self.data.index < self.data.length):

            self.iterations+=1
            print(url)
            try:

                #Get link from the queue
                url=self.data.links[self.data.index]
    

                # Check the url doesnt lead ouside the site
                if self.__InsideDomain(url) ==  False:
                    
                    if self.data.index < self.data.length:
                        self.data.index+=1
                        continue               
                
                #main http request
                if self.request.Get(url) == False:

                    if self.data.index < self.data.length:
                        self.data.index+=1
                        continue

                #check the response is valid
                if self.request.GetStatusCoded == 404:

                    if self.data.index < self.data.length:
                        self.data.index+=1
                        continue
                
                # get the response body and dine all the <a> (links)
                response_content=self.request.GetResponseContent()
                items=self.__GetAllLinks(response_content)

                if items == False:#non html found

                    if self.data.index < self.data.length:
                        self.data.index+=1
                        continue

                items=self.__GetLinkUrl(items)
                
                if items == False:#non html found / non static site
                    
                    if self.data.index < self.data.length:
                        self.data.index+=1
                        continue

                self.__EliminateDuplicates(items)
                self.__UpdateQueue()
                self.data.index+=1

            except HTTPError as httperr:

                self.fails+=1
                print("no response or the return value is not HTML")
                if self.data.index < self.data.length:
                    self.__UpdateQueue()
                    self.data.index+=1
                    continue
            


            


    def __GetAllLinks(self,content:object)->list:

        try:
            parsed_content=BeautifulSoup(content,"html.parser")
            links=parsed_content.find_all("a")
            return links
        except:
            print("Non html found")
            return False


    def __GetLinkUrl(self,elements:list)->list:
        
        try:
            items=[]
            for element in elements:

                self.iterations+=1
                items.append(element["href"])
            return items
        except:
            
            return False



    def __EliminateDuplicates(self,items:list):
        
        #current urls in our list + new urls found
        for item in items:
            self.data.links.append(item)

        temp_set=set()
        temp_set.update(self.data.links)#eliminate possible duplicates from our list
        self.data.links=list(temp_set)#update our list



    def __UpdateQueue(self):

        self.data.length=len(self.data.links)



    def __InsideDomain(self,url:str):

        if url.find(self.data.root) != -1:

            return True
        
        return False


