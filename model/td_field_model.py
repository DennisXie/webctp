from typing import Optional
from openctp import thosttraderapi as tdapi
from .base import CtpFieldModel


class QryInstrument(CtpFieldModel):
    __ctp_type__ = tdapi.CThostFtdcQryInstrumentField

    ExchangeID: Optional[str]
    InstrumentID: Optional[str]
    ExchangeInstID: Optional[str]
    ProductID: Optional[str]
