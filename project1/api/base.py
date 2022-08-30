from fastapi import APIRouter
from api.version1 import route_general_pagese
from api.version1 import route_users


api_router = APIRouter()
api_router.include_router(route_general_pagese.core_routes,prefix="",tags=["general_pages"])
api_router.include_router(route_users.router,prefix="/users",tags=['users'])

