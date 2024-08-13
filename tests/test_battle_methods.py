from src.battle_methods import Battlemethods
import pandas as pd
import pytest

def test_damage_a_b_calculate_damage_value() -> None:
    attack_a = 50
    against_type1_b = 20
    against_type2_b = 30
    test_obj = Battlemethods()
    
    result = test_obj.damage_a_b(attack_a, against_type1_b, against_type2_b)
    
    assert result == -1225
    
def test_damage_a_b_calculate_damage_value_() -> None:
    attack_a = 500
    against_type1_b = 50
    against_type2_b = 50
    test_obj = Battlemethods()
    
    result = test_obj.damage_a_b(attack_a, against_type1_b, against_type2_b)
    
    assert result == -2250
    
def test_damage_b_a_calculate_damage_value() -> None:
    attack_b = 500
    against_type1_a = 50
    against_type2_ab = 50
    test_obj = Battlemethods()
    
    result = test_obj.damage_a_b(attack_b, against_type1_a, against_type2_ab)
    
    assert result == -2250.0
    
def test_damage_b_a_calculate_damage_value_() -> None:
    attack_b = 50
    against_type1_a = 20
    against_type2_ab = 30
    test_obj = Battlemethods()
    
    result = test_obj.damage_a_b(attack_b, against_type1_a, against_type2_ab)
    
    assert result == -1225
    
def test_damage_b_a_calculate_damage_zero_when_the_inputs_are_zeros() -> None:
    attack_b = 0
    against_type1_a = 0
    against_type2_ab = 0
    test_obj = Battlemethods()
    
    result = test_obj.damage_a_b(attack_b, against_type1_a, against_type2_ab)
    
    assert result == 0

def test_damage_a_b_calculate_damage_zero_when_the_inputs_are_zeros() -> None:
    attack_a = 0
    against_type1_b = 0
    against_type2_b = 0
    test_obj = Battlemethods()
    
    result = test_obj.damage_a_b(attack_a, against_type1_b, against_type2_b)
    
    assert result == 0
    
def test_choose_player_chooses_same_input_players_when_spelling_is_correct() -> None:
    input1 = "Spearow"
    input2 = "Nidoking"
    df_dict = {"name":['Bulbasaur', 'Spearow', 'Nidoking'], "speed":[45, 50, 55]}
    df = pd.DataFrame(df_dict)
    df.set_index("name", inplace=True)
    
    test_obj = Battlemethods()
    
    result = test_obj.choose_player(input1, input2, df)
    
    assert result == ('Spearow', 'Nidoking')
    
def test_choose_player_chooses_updated_input_players_when_spelling_is_slightly_wrong() -> None:
    input1 = "Spearaw"
    input2 = "Nidokig"
    df_dict = {"name":['Bulbasaur', 'Spearow', 'Nidoking'], "speed":[45, 50, 55]}
    df = pd.DataFrame(df_dict)
    df.set_index("name", inplace=True)
    
    test_obj = Battlemethods()
    
    result = test_obj.choose_player(input1, input2, df)
    
    assert result == ('Spearow', 'Nidoking')
    
def test_choose_player_throws_exception_when_spelling_is_completely_wrong() -> None:
    input1 = "Spiaraw"
    input2 = "Nikokig"
    df_dict = {"name":['Bulbasaur', 'Spearow', 'Nidoking'], "speed":[45, 50, 55]}
    df = pd.DataFrame(df_dict)
    df.set_index("name", inplace=True)
    
    test_obj = Battlemethods()
    
    with pytest.raises(UnboundLocalError):
        test_obj.choose_player(input1, input2, df)
    
def test_choose_player_update_one_input_player_when_spelling_is_slightly_wrong() -> None:
    input1 = "Spearow"
    input2 = "Nidokig"
    df_dict = {"name":['Bulbasaur', 'Spearow', 'Nidoking'], "speed":[45, 50, 55]}
    df = pd.DataFrame(df_dict)
    df.set_index("name", inplace=True)
    
    test_obj = Battlemethods()
    
    result = test_obj.choose_player(input1, input2, df)
    
    assert result == ('Spearow', 'Nidoking')

def test_choose_player_update_one_input_player_when_spelling_is_slightly_wrong_() -> None:
    input1 = "Sparow"
    input2 = "Nidoking"
    df_dict = {"name":['Bulbasaur', 'Spearow', 'Nidoking'], "speed":[45, 50, 55]}
    df = pd.DataFrame(df_dict)
    df.set_index("name", inplace=True)
    
    test_obj = Battlemethods()
    
    result = test_obj.choose_player(input1, input2, df)
    
    assert result == ('Spearow', 'Nidoking')