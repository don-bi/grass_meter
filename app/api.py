import requests
import json
import random

#PokeApi Dict Lists name/sprite link/type(s)
def random_poke():
    info = {}
    rand_index = random.randrange(900) #around the max amount of pokemon
    request_data = requests.get(f"https://pokeapi.co/api/v2/pokemon/{rand_index}")
    data = request_data.json()

    #Name
    info["name"] = data["name"]
    #Sprite Link to a PNG
    info["sprite"] = data["sprites"]["other"]["official-artwork"]["front_default"]
    #type(s)
    type1 = data["types"][0]["type"]["name"]
    type2 = ""
    try:
        type2 = data["types"][1]["type"]["name"]
    except:
        None
    info["type"] = [type1, type2]

def random_anime():
    info = {}
    rand_index = random.randrange(500)
    url = "https://api.myanimelist.net/v2/anime/ranking?ranking_type=all&limit=500" # Taking the top ranking anime and selecting a random one (500 is max)

    client_id = "" #Pulling api key
    try: #check for if text file for key exist
        with open("keys/MAL_key.txt", "r") as file:
            api_key = file.read().strip()
            client_id = api_key
    except:
        print("No API key provided.")

    data = json.loads(requests.get(url, headers={"X-MAL-CLIENT-ID": client_id}).text)

    anime_data = data["data"][rand_index]
    #Name
    info["name"] = anime_data["node"]["title"]
    #Image
    info["image"] = anime_data["node"]["main_picture"]["large"]
