from battle_rounds import Batterounds
from battle_methods import Battlemethods

class Fight:
    
    def fight(self, input1, input2, pokemon_df):
        
        battle_rounds = Batterounds()
        battle_methods = Battlemethods()
        #Choosing the players
        players = battle_methods.choose_player(input1, input2, pokemon_df)
        player_1 = players[0]
        player_2 = players[1]

        #First round battle ready
        first_round = battle_rounds.battle_round_1(player_1, player_2, pokemon_df)
        attack_a = first_round[0]
        against_type1_b = first_round[1]
        against_type2_b = first_round[2]

        #Second round battle ready
        second_round = battle_rounds.battle_round_2(player_1, player_2, pokemon_df)
        attack_b = second_round[0]
        against_type1_a = second_round[1]
        against_type2_a = second_round[2]

        #Battle damage result
        ans_1 = battle_methods.damage_a_b(attack_a, against_type1_b, against_type2_b)
        ans_2 = battle_methods.damage_b_a(attack_b, against_type1_a, against_type2_a)

        if ans_1 > ans_2:
            winner = player_1
            won_by_margin = ans_1 - ans_2
        elif ans_2 > ans_1:
            winner = player_2
            won_by_margin = ans_2 - ans_1
        else:
            winner = 'Draw'
            won_by_margin = 0

        return winner, won_by_margin 
