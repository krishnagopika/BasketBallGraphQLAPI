from random import randint
from pydantic import BaseModel
from fastapi import HTTPException, APIRouter
from app_data import BaksetballPlayer, basketball_players, Biometric, Stats

router = APIRouter()


class BaksetBallPlayerForm(BaseModel):
    fname: str 
    lname: str 
    bioMetrics: Biometric
    careerStats: Stats


@router.get("/players")
def get_players(lname: str | None = None) -> list[BaksetballPlayer]:

    if lname:
        return [p for p in list(basketball_players.values()) if lname.lower() in p.lname.lower()]

    return list(basketball_players.values())


@router.get("/players/{id}")
def get_player_by_id(id: int) -> BaksetballPlayer:

    if player := basketball_players.get(id):
        return player
    raise HTTPException(status_code=404, detail="No player with id {id} found")


@router.post("/players")
def add_player(player_form: BaksetBallPlayerForm) -> BaksetballPlayer:

    new_player = BaksetballPlayer(playerId=randint(1000,9999), **player_form.__dict__) 
    basketball_players[new_player.playerId] = new_player
    return new_player


@router.put("/players/{id}")
def update_player(id: int, player: BaksetballPlayer) -> BaksetballPlayer:

    if basketball_players.get(id):
        basketball_players[id] = player
        return player
    
    raise HTTPException(status_code=404, detail="No player with id {id} found")


@router.delete("/players/{id}", status_code=201)
def delete_player_by_id(id: int):

    if basketball_players.get(id):
        del basketball_players[id]
        return

    raise HTTPException(status_code=404, detail="No player with id {id} found")