from input_spell_check import Spellcheck

class Battlemethods:
    def choose_player(self, input1, input2, pokemon_df) -> tuple:

        input_1 = input1.lower() #Normalizing the input by converting it to lowercase.
        input_2 = input2.lower() 

        #Spell check function.
        try:
            spell_check = Spellcheck()
            corrected_pokemon_names = spell_check.pokemon_name_correction(input_1, input_2, pokemon_df)
            input_1 = corrected_pokemon_names[0]
            input_2 = corrected_pokemon_names[1]
            
            
            player_1 = f'{input_1[0].upper()}{input_1[1:]}'
            player_2 = f'{input_2[0].upper()}{input_2[1:]}'
        except Exception as e:
            print(f'choose player function failed due to {e}')

        return player_1, player_2
    
        
    def damage_a_b(self, attack_a, against_type1_b, against_type2_b):
        damage_a_b = (attack_a/200) * 100 - (((against_type1_b / 4) * 100) + ((against_type2_b / 4) * 100))

        return damage_a_b
    

    def damage_b_a(self, attack_b, against_type1_a, against_type2_a):
        damage_b_a = (attack_b/200) * 100 - (((against_type1_a / 4) * 100) + ((against_type2_a / 4) * 100))

        return damage_b_a
