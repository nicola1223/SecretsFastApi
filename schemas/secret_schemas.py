"""Module for secret pydantic schemas"""
from pydantic import BaseModel


class SecretCreate(BaseModel):
    """Schema for creating secret"""
    secret: str
    passphrase: str | None = None
    ttl_seconds: int | None = None


class SecretResponse(BaseModel):
    """Schema for response after creating"""
    secret_key: str


class SecretReadResponse(BaseModel):
    """Schema for response with secret"""
    secret: str


class SecretDeleteResponse(BaseModel):
    """Schema for response when deleting secret"""
    status: str
