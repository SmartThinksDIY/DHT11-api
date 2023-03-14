from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_sqlalchemy import DBSessionMiddleware
from temperature_monitor_api import __version__
from temperature_monitor_api.settings import get_settings

settings = get_settings()
app = FastAPI(
    title='temperature-monitor-api',
    description='temperature-monitor-api',
    version=__version__,

    # Отключаем нелокальную документацию
    root_path=settings.ROOT_PATH if __version__ != 'dev' else '/',
    docs_url=None if __version__ != 'dev' else '/docs',
    redoc_url=None,
)


app.add_middleware(
    DBSessionMiddleware,
    db_url=settings.DB_DSN,
    engine_args={"pool_pre_ping": True, "isolation_level": "AUTOCOMMIT"},
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ALLOW_ORIGINS,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS,
)
