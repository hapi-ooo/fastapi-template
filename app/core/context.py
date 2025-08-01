from fastapi import FastAPI
from contextlib import asynccontextmanager

from .config import settings
from .logging import init_logging


@asynccontextmanager
async def lifespan(app: FastAPI):
  logger = init_logging()
  if settings.DEBUG:
    import logging
    logger.setLevel(logging.DEBUG)
    logger.debug(f'Running {settings.PROJECT_NAME} in debug mode')
  else:
    logger.info(f'Starting {settings.PROJECT_NAME}')
  yield
  logger.info(f'Tearing down {settings.PROJECT_NAME}')