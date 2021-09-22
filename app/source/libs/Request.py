
import requests
import validators
from requests.models import HTTPError




class Request():

    def __init__(self) -> None:
        self.__data={}

    def Ping(self,url:str):
    
        try:

            if self.__ValidateURL(url)==False:
                return False

            response=None
            response=requests.get(url)
            response.raise_for_status()
    

        except HTTPError as http_error:
            
            print(f"Http error ocurred , no response : {http_error}")
            return False
        except Exception as error:

            print(f"Unknown error : {error}")
            return False

        else:
            return True




    def Get(self,url:str)->bool:

        try:

            if url==None or url=="":
                return False

            if self.__ValidateURL(url)==False:
                return False

            response=None
            response=requests.get(url)

        except HTTPError as httperror:

            print(httperror)
            return False

        except Exception as err:
            
            print("Unknow error / invalid request")
            return False

        if response.status_code ==404:

            return False
        try:
            self.__data["status"]=response.status_code
            self.__data["header"]=response.headers
            self.__data["content"]=response.content
            self.__data["encoding"]=response.encoding
            self.__data["history"]=response.history
            self.__data["text"]=response.text
  
        except Exception as err:

            print(err)
            return False


        return True
        




    def GetResponse(self)->dict:

        return self.__data

    def GetStatusCoded(self)->int:

        return self.__data.get("status")

    def GetResponseContent(self)->bytes:

        return self.__data.get("content")

    def GetResponseHeader(self)->dict:
        
        return self.__data.get("header")

    def GetResponseEncoding(self)->str:

        return self.__data.get("encoding")

    def GetResponseHistory(self)->list:

        return self.__data.get("history")

    def GetResponseText(self)->str:

        return self.__data.get("text")



    def ParseResponseBodyToList(self,encoding:str=None)->list:

        body=None
        enc=None
        result=None

        if len(self.__data.items()) == 0:

            print("No response available, a response obj is required for this method")
            return False

        if encoding == None:

            enc=self.__data.get("encoding")

        else:

            enc = encoding

        body=self.__data.get("content")

        if type(body) is not bytes:

            print("The response body is not (type) byte, this method expects to parse bytes")
            return False

        try:

            string=body.decode(enc)
            result=self.__SearchForHtml(string)

            if len(result) == 0:

                print("The content of the response body is empty")
                return False

            
            return result

        except Exception:

            print("The content of the response body is not iterable")
            return False




    def __SearchForHtml(self,string:str)->list:

        line_start=False
        line_end=False
        temphtml=[]
        html=[]

        for char in string :

            if char =="<":

                line_end=False
                line_start=True

            if char=="/>" or char==">":

                line_end=True
                line_start=False

            if char==" '\\n'" or char=="\n" or char==" '\n'":

                continue
            
            if line_start==True:

                string=string+char

            if line_end==True:

                string=string+char
                temphtml.append(string)
                string=""

        #cleaing empty spaces
        for line in temphtml:

            if line==" " or line==' ':

                continue
            else:

                html.append(line)


        return html
                


    def __ValidateURL(self,url:str):

        result=validators.url(url) 
        return result






        

        