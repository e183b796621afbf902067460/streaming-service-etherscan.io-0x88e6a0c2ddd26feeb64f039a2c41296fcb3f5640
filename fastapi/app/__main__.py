from fastapi import FastAPI

from app.settings import get_settings
from app.views.menu.view import router as menu_router


app, env = FastAPI(), get_settings()


app.include_router(router=menu_router, prefix=f'{env.API_V1}')


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app='__main__:app', host='0.0.0.0')
