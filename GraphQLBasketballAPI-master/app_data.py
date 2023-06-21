import strawberry


@strawberry.type
class Stats:
    shotAttempts: int 
    madeBaskets: int
    rebounds: int 
    assists: int 
    blocks: int

@strawberry.type
class Biometric:
    heightInches: int
    weightLbs: int 

@strawberry.type
class BaksetballPlayer:
    playerId: int 
    fname: str 
    lname: str 
    bioMetrics: Biometric
    careerStats: Stats


basketball_players: dict[int,BaksetballPlayer] = {
    10001:BaksetballPlayer(
        playerId=10001,
        fname="Billy",
        lname="McBrickshot",
        bioMetrics= Biometric(heightInches=80, weightLbs=245),
        careerStats = Stats(
            shotAttempts = 245, 
            madeBaskets = 23, 
            rebounds = 98,
            assists = 74,
            blocks = 40)
    ),
    20002:BaksetballPlayer(
        playerId=20002,
        fname="Marcus",
        lname="Nevapass",
        bioMetrics= Biometric(heightInches=74, weightLbs=190),
        careerStats = Stats(
            shotAttempts = 224, 
            madeBaskets = 150, 
            rebounds = 24,
            assists = 0,
            blocks = 5)
    ),  
    30003:BaksetballPlayer(
        playerId=30003,
        fname="Tim",
        lname="Swoop",
        bioMetrics= Biometric(heightInches=74, weightLbs=190),
        careerStats = Stats(
            shotAttempts = 200, 
            madeBaskets = 165, 
            rebounds = 240,
            assists = 41,
            blocks = 44)
    ),  
        40004:BaksetballPlayer(
        playerId=40004,
        fname="Kevin",
        lname="Swoop",
        bioMetrics= Biometric(heightInches=74, weightLbs=185),
        careerStats = Stats(
            shotAttempts = 90, 
            madeBaskets = 71, 
            rebounds = 277,
            assists = 14,
            blocks = 32)
    ), 
}