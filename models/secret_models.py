"""Module for secret's database models"""
from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped

from core.database import Base


class Secret(Base):
    """Secrets table model"""
    __tablename__ = 'secrets'
    secret_key: Mapped[str] = Column(String, primary_key=True, index=True)
    encrypted_secret: Mapped[str] = Column(Text, nullable=False)
    passphrase_hash: Mapped[str] = Column(String)
    created_at: Mapped[datetime] = Column(
        DateTime, default=datetime.now()
    )
    expires_at: Mapped[datetime] = Column(DateTime)
    is_active: Mapped[bool] = Column(Boolean, default=True)


class Log(Base):
    """Secret logs table model"""
    id: Mapped[int] = Column(Integer, primary_key=True)
    secret_key: Mapped[str] = Column(String, nullable=False)
    action: Mapped[str] = Column(String, nullable=False)
    timestamp: Mapped[datetime] = Column(
        DateTime, default=datetime.now()
    )
    ip_address = Column(String)
