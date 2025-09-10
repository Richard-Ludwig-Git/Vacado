from fastapi import FastAPI
from backend import security, backend_endpoints
from frontend import frontend_routes

tags_metadata = [
    {
        "name": "frontend"
    },
{
        "name": "security"
    },
    {
        "name": "backend"
        }

]
vacado = FastAPI(title="Vacado", openapi_tags=tags_metadata)
vacado.include_router(router=security.security_router)
vacado.include_router(router=frontend_routes.routing)
vacado.include_router(router=backend_endpoints.backapp)



