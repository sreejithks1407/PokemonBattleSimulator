This repo contains the flask application PokemonBattleSimulator which takes two pokemon names as input from user and find the winner name based on it's different parameters from kaggle dataset pokemon.csv. As of now this project is not deployed anywhere so we need to run the application in our local machine. 

There are 4 apis created as part of this project. 

First : http://localhost:5000/api/pokemon/pagination is a pagination api which provides the details of all the pokemons.
![image](https://github.com/user-attachments/assets/3862649c-d15a-4631-8d2b-1d27aeab877b)

Second : http://localhost:5000/ will be used to get the total number of battles completed
![image](https://github.com/user-attachments/assets/6b5841d3-15d0-4eed-af5a-ef3f15a492da)

Third : http://localhost:5000/api/pokemon/battle with pokemon names as post request creates a battle and returns a battle id.
![image](https://github.com/user-attachments/assets/67fc9697-99e9-4c05-b038-a9de1b4be0b0)
Json input:
{
    "player1":"Kakuna",
    "player2":"Fearow"
}

Fourth : http://localhost:5000/api/pokemon/battle/result/<battleid> will return the result of the battle with the battle id provided.
![image](https://github.com/user-attachments/assets/0d3e18f7-7784-4a78-82e9-55103a412e7a)


