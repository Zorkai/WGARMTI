# Made by Zorkai 
# https://genefit.cc

import requests

########################## CONFIG ##########################
tokens_file_name = "tokens.txt"
results_file_name = "results.txt"
reset_results_file = True  # Add/Don't add new results to old results (truncate)
save_guild_name = True  # Save/Don't save the name of the guild
save_guild_id = True  # Save/Don't save the id of the guild

########################### CODE ###########################
API_PATH = "https://discord.com/api/v9/users/@me/guilds"

tokens_file = open(tokens_file_name, "r")
tokens = tokens_file.read().splitlines()
tokens_file.close()

result_text = ""

for token in tokens:
    headers = {
      "Authorization": token,
      "Content-Type": "application/json"
    }

    response = requests.get(API_PATH, headers=headers)
    try:
        guilds = response.json()
    except:
        print(f"Unknown Error {response.text} ({token})")
        continue
    
    if "message" in guilds:
      error = guilds["message"]

      if "401" in error:
        print(f"Invalid Token! ({token})")
      else:
        print(f"Unknown Error {error} ({token})")
      
      continue


    for guild in guilds:
        guild_id, guild_name = guild["id"], guild["name"]

        if save_guild_id and not save_guild_name:
            result_text += f"{guild_id}\n"

        if not save_guild_id and save_guild_name:
            result_text += f"{guild_name}\n"

        if save_guild_id and save_guild_name:
            result_text += f"{guild_id} - {guild_name}\n"

if reset_results_file:
  results_file = open(results_file_name, "w")
else:
  results_file = open(results_file_name, "a")

results_file.write(result_text)
results_file.close()