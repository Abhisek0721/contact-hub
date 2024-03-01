from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

async def http_error_handler(request: Request, exc: HTTPException) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )

async def unhandled_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    return JSONResponse(
        status_code=500,
        content={"message": "Internal server error"},
    )
