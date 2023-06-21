## Basketball API
This is an API for a simple basketball app. It persists data in memory. If you should down and restart the application the data will be reset.
The API supports both RESTful and graphql interfaces.

## Set Up
1. install [python](https://www.python.org/downloads/) 
   1. Choose the default options and to install pip
2. clone this repository
3. in the directory with the main.py run `pip install -r requirements.txt`
4. run `pip install "uvicorn[standard]"`
5. in the directory with the main.py run the application with `uvicorn main:app`
   1. *all data is persisted in memory*
   2. *restarting/stopping the application will erase data*
6. The applicaiton will run on port `http://localhost:8000`
   1. ***You can access interactable documentation of endpoints at `http://localhost:8000/docs`***

#### Graph QL Practice questions
1. Write a query that returns all the data on all the players
1. Write a query that returns all players with just fname and last name
2. Write a query that returns all players with their lname and all their stats
3. Write a query that returns returns all players with the last name Swoop
4. Write a query that returns returns all players with the last name as a variable
5. Write a query that returns only all players height and weight
6. Write a query that use a fragment called stats that returns all the players stats. Use this fragment to query all players and return their playerId and stats.
7. Write a mutation to add a new player
8. Write a mutation to add a new player and that checks to see what the return of the query is `... on` keyword.
9. Write a mutation that uses aliasas to add two players at once
10. write a mutation that adds 10 rebounds to a player of your choice
11. write a mutation that adds 10 assists, 10 blocks and 10 rebounds to a player of your choice
