from pydantic_settings import BaseSettings
from pydantic import validator

class Settings(BaseSettings):
    auth0_audience: str
    app_auth0_domain: str
    app_auth0_client_id: str = None
    app_auth0_callback_url: str = None
    app_api_server_url: str = None
    app_auth0_client_secret: str = None
    auth0_management_api: str = None
    reload: bool
    client_origin_url: str

    @classmethod
    @validator("client_origin_url", "auth0_audience", "auth0_domain")
    def check_not_empty(cls, v):
        assert v != "", f"{v} is not defined"
        return v

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
