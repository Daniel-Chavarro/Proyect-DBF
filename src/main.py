"""This module is the entry point of the application.

It contains the FastAPI instance and the routers
that will be used in the application.

Author: Carlos Andres Sierra <cavirguezs@udistrital.edu.co>
"""

from fastapi import FastAPI, HTTPException

from services import (
    
)
from initialization import InitTournament

app = FastAPI(
    title="Football API",
    version="0.0.1",
    description="This is an example of a CRUD using services for a football tournament.",
)

app.include_router(users_router)
app.include_router(stadiums_router)
app.include_router(teams_router)
app.include_router(players_router)
app.include_router(matches_router)


@app.get("/")
async def root():
    """This method is used to get the root of the API."""
    return {"message": "Welcome to the Football API!"}