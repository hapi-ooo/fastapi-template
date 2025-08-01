from fastapi import FastAPI

from .api.v1.routes import router as v1_router
from .core.context import lifespan

app = FastAPI(
  title="FastAPI App with Poetry",
  lifespan=lifespan
  )

app.include_router(v1_router, prefix="/api/v1")
