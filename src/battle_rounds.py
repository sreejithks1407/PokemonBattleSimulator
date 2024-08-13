class Batterounds:

    def battle_round_1(self, player_1, player_2, pokemon_df):

        attack = player_1
        defend = player_2

        attacker = attack
        type1 = pokemon_df.loc[attacker].type1
        type2 = pokemon_df.loc[attacker].type2
        attack = pokemon_df.loc[attacker].attack

        defender = defend
        defender_type1 = f'against_{type1}'
        defender_type2 = f'against_{type2}'

        against_type1 = pokemon_df.loc[defender][defender_type1]
        against_type2 = pokemon_df.loc[defender][defender_type2]

        return attack, against_type1, against_type2
    

    def battle_round_2(self, player_1, player_2, pokemon_df):

        attack = player_2
        defend = player_1

        attacker = attack
        type1 = pokemon_df.loc[attacker].type1
        type2 = pokemon_df.loc[attacker].type2
        attack = pokemon_df.loc[attacker].attack

        defender = defend
        defender_type1 = f'against_{type1}'
        defender_type2 = f'against_{type2}'

        against_type1 = pokemon_df.loc[defender][defender_type1]
        against_type2 = pokemon_df.loc[defender][defender_type2]

        return attack, against_type1,  against_type2
