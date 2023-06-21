from random import randint
import strawberry
from strawberry.fastapi import GraphQLRouter
from collections import Counter
from typing import Optional

from app_data import BaksetballPlayer, basketball_players, Stats, Biometric

@strawberry.input
class StatsInput:
    playerId: int 
    shotAttempts: int = 0
    madeBaskets: int = 0
    rebounds: int = 0
    assists: int = 0
    blocks: int = 0

@strawberry.type
class PlayerDoesNotExist:
    playerId: int 
    message: str

@strawberry.input
class NewPlayerInput:
    fname: str 
    lname: str 
    heightInches: int 
    weightLbs: int 

@strawberry.input
class UpdatePlayerInput:
    playerId:int
    fname: str 
    lname: str 
    heightInches: int 
    weightLbs: int
    shotAttempts: int
    madeBaskets: int
    rebounds: int
    assists: int
    blocks: int


def players_resolvers(lname: str | None = None) -> list[BaksetballPlayer]:

    if lname:
        return [p for p in list(basketball_players.values()) if lname.lower() in p.lname.lower()]

    return list(basketball_players.values())


Response = strawberry.union(
    "AddStatsResponse", [BaksetballPlayer, PlayerDoesNotExist]
)


def merge_stats(input: StatsInput) -> Response:  # type: ignore
    if player := basketball_players.get(input.playerId):
        updatedStats = Stats(
            shotAttempts = player.careerStats.shotAttempts + input.shotAttempts,
            madeBaskets = player.careerStats.madeBaskets + input.madeBaskets,
            assists = player.careerStats.assists + input.assists,
            blocks = player.careerStats.blocks + input.blocks,
            rebounds = player.careerStats.rebounds + input.rebounds 
        )
        player.careerStats = updatedStats
        return player

    return PlayerDoesNotExist(playerId=input.playerId, message="No player with that ID found")

def add_player(input: NewPlayerInput) -> BaksetballPlayer:
    player = BaksetballPlayer(
        playerId=randint(1000,9999), 
        fname=input.fname,
        lname=input.lname,
        careerStats=Stats(
            assists=0,
            madeBaskets=0,
            rebounds=0,
            shotAttempts=0,
            blocks=0
        ),
        bioMetrics=Biometric(
            heightInches= input.heightInches,
            weightLbs= input.weightLbs
        ))
    
    basketball_players[player.playerId] = player
    return player

def update_player(input: UpdatePlayerInput) -> BaksetballPlayer:
    player = BaksetballPlayer(
        playerId=input.playerId,
        fname=input.fname,
        lname=input.lname,
        careerStats=Stats(
            assists=input.assists,
            madeBaskets=input.madeBaskets,
            rebounds=input.rebounds,
            shotAttempts=input.shotAttempts,
            blocks=input.blocks
        ),
        bioMetrics=Biometric(
            heightInches= input.heightInches,
            weightLbs= input.weightLbs
        ))
    if input.playerId:
        p = basketball_players[input.playerId]
        print(p)
        p.fname=player.fname
        p.bioMetrics=player.bioMetrics
        p.careerStats = player.careerStats
        p.lname=player.lname
    player = basketball_players[input.playerId]
    return player


@strawberry.type
class Query:
    players: list[BaksetballPlayer] = strawberry.field(resolver=players_resolvers)


@strawberry.type
class Mutation:
    merge_stats: BaksetballPlayer | PlayerDoesNotExist = strawberry.field(resolver=merge_stats)
    add_player: BaksetballPlayer = strawberry.field(resolver=add_player)
    update_player:BaksetballPlayer = strawberry.field(resolver=update_player)

schema = strawberry.Schema(Query, Mutation)
graphql_app = GraphQLRouter(schema)