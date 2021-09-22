import abc

class MongoAtlasInterface(metaclass=abc.ABCMeta):


    @classmethod
    def __subclasshook__(cls,subclass):

        return (
            hasattr(subclass,"GetItem") and callable(subclass,"GetItem") and
            hasattr(subclass,"GetItems") and callable(subclass,"GetItems") and
            hasattr(subclass,"UpdateItem") and callable(subclass,"UpdateItem") and
            hasattr(subclass,"DeleteItems") and callable(subclass,"DeleteItems")

        )




    @abc.abstractmethod
    def GetItem(self,table:str,id:str=None)->dict:

        raise NotImplementedError

    @abc.abstractmethod
    def GetItems(self,table)->list:

        raise NotImplementedError

    @abc.abstractmethod
    def UpdateItem(self,table,id,data)->bool:

        raise NotImplementedError

    @abc.abstractmethod
    def DeleteItem(self,table,id=None)->bool:

        raise NotImplementedError

