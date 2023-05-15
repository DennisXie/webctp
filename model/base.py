from pydantic import BaseModel

from utils import CTPObjectHelper


class MessageBaseModel(BaseModel):
    MsgType: str
    RequestID: int = 0


class CtpFieldModel(BaseModel):
    __ctp_type__: any

    @property
    def object(self) -> any:
        obj = self.__ctp_type__()
        CTPObjectHelper.dict_to_object(dict(self), obj)
        return obj


class LoginModel(BaseModel):
    pass
