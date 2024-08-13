This repo contains the flask application PokemonBattleSimulator which takes two pokemon names as input from user and find the winner name based on it's different parameters from
kaggle dataset pokemon.csv. As of now this project is not deployed anywhere so we need to run the application in our local machine. 

There are 4 apis created as part of this project. 

First : http://localhost:5000/api/pokemon/pagination is a pagination api which provides the details of all the pokemons.

Second : http://localhost:5000/ will be used to get the total number of battles completed

Third : http://localhost:5000/api/pokemon/battle with pokemon names as post request creates a battle and returns a battle id.

Fourth : http://localhost:5000/api/pokemon/battle/result/<battleid> will return the result of the battle with the battle id provided.\

