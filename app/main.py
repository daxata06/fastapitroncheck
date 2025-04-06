from fastapi import FastAPI, Request
from starlette.responses import Response
from starlette import status
from contextlib import asynccontextmanager
from app.routers import address_routers
from app.models.session import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


def create_application() -> FastAPI:
    app = FastAPI(lifespan=lifespan)

    app.include_router(address_routers.router)

    @app.middleware("http")
    async def set_root_path(request: Request, call_next):
        root_path = request.headers.get("x-forwarded-prefix", "")
        request.scope["root_path"] = root_path
        return await call_next(request)

    return app


app = create_application()


@app.get("/healthcheck")
async def healthcheck():
    return Response(status_code=status.HTTP_200_OK)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
