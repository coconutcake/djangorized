# This file contains interfaces
import os
from abc import ABC, abstractmethod
from typing import List


import components.additionals


class OperationsInterface(ABC):
    """
    Basic operation interface
    """
    
    def __init__(self, python: str):
        if python and python == "3":
            self.__python = "python3"
        elif python == "2" or not python:
            self.__python = "python"
        else:
            raise ValueError("Wrong python version provided. Avalable are 2,3")
            
    
    def get_python_version(self):
        """
        Returns python version
        """
        try:
            return self.__python
        except:
            raise NameError("No python definied")
    
    
    def get_abs_path(self):
        """
        Returns current folder path
        """
        path_ = os.path.dirname(__file__)
        return path_
        
    
    def log(self, msg: str) -> None:
        """
        Returns log print with current timestramp
        """
        separation = "-"*40
        
        return print(f"\n{components.additionals.get_current_datetime()}\
            \n{msg}\n{separation}")


