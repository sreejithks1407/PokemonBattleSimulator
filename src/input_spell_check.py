import difflib

class Spellcheck:
#Correct the user entered pokemon names by checking the spelling.
    def pokemon_name_correction(self, input1, input2, pokemon_df):

        print(f"Pokemon names before correction {input1}, {input2}")

        pokemon_names_list = pokemon_df.index.str.lower().to_list()
                            
        pokemon_1 = self.check_spelling(input1, pokemon_names_list)
        pokemon_2 = self.check_spelling(input2, pokemon_names_list)

        print(f"Pokemon names after correction {pokemon_1}, {pokemon_2}")

        return pokemon_1+pokemon_2
    

    def check_spelling(self, input:str, pokemon_list:list):
        close_matches = difflib.get_close_matches(input, pokemon_list, n=1, cutoff=0.85)
        return close_matches
