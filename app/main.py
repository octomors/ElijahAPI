import uvicorn
from fastapi import FastAPI
from config import settings
from contextlib import asynccontextmanager

from models import db_helper, Base
from api import router as api_router

from fastapi_pagination import add_pagination
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield
    # shutdown
    await db_helper.dispose()


main_app = FastAPI(
    lifespan=lifespan,
)

main_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

main_app.include_router(
    api_router,
)

# Add pagination support
add_pagination(main_app)



if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=settings.run.reload,
    )
