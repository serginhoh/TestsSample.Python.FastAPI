from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI
from src.routers.v1.pessoas import pessoasrouter

app = FastAPI()
app.include_router(pessoasrouter)

app = VersionedFastAPI(app, version_format='{major}', prefix_format='/v{major}')
