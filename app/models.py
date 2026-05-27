from sqlalchemy import Column, Integer, String

from .database import Base

class SecurityEvent(Base):
    __tablename__ = "security_events"

    id = Column(Integer, primary_key=True, index=True)
    severity = Column(String)
    source = Column(String)
    message = Column(String)