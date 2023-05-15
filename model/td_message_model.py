from .base import MessageBaseModel
from .td_field_model import QryInstrument

class ReqQryInstrumentModel(MessageBaseModel):
    QryInstrument: QryInstrument
