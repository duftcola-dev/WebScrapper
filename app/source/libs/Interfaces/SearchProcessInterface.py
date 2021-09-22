import abc



class SearchProccessInterface(abc.ABC):

    @classmethod
    def __subclasshook__(cls,subclass):
        return(
            hasattr(subclass,"ExploreUrl") and callable(subclass,"ExploreUrl") and
            hasattr(subclass,"GetLinks") and callable(subclass,"GetLinks")
        )

    @abc.abstractmethod
    def ExploreUrl(self,url:str)->bool:
        raise NotImplementedError

    @abc.abstractmethod
    def GetLinks(self)->list:
        raise NotImplementedError

    