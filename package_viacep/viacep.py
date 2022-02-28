from __future__ import annotations
import requests
import json

__version__ = '0.0.1'

class ViaCep:
    def __init__(self) -> None:
        self.__cep = ''

    @property
    def cep(self) -> str:
        return self.__cep

    @cep.setter
    def cep(self, cep:str):
        self.__cep = self.__ValidCep(cep)

    @classmethod
    def __SearchCep(self, cep:str):
        url = f'http://www.viacep.com.br/ws/{cep}/json/'
        try:
            req = requests.get(url)
            if req.status_code == 200:
                data_json = json.loads(req.text)
                return data_json
            else:
                raise ValueError(f"Error in the request, Status code error: {req.status_code}")
        except Exception as ex:
            return ex

    @classmethod
    def GetData(self, cep:str = None):
        if cep is None and self.cep != '':
            return self.__SearchCep(self.cep)
        elif cep is None and self.cep == '':
            raise ValueError("Cep must contain 8 digits.")
        else:
            self.cep = self.__ValidCep(cep)
            return self.__SearchCep(self.cep)
    
    @classmethod
    def __ValidCep(self, cep:str) -> str:
        cep = cep.replace('.', '').replace('-', '')
        if len(cep) != 8:
            raise ValueError("Cep must contain 8 digits.")
        return cep