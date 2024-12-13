from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, date, timedelta
import pytz
from .controllers import Base

class Challenge(Base):
    __tablename__ = "Challenges"
    _id =  Column(Integer, primary_key=True, index=True)
    description = Column(String)
    expire_date = Column(Date = datetime.now(pytz.timezone('America/Sao_Paulo')) + timedelta(days=30))