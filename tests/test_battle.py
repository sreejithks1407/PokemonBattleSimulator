from src.battle import Fight
import pandas as pd
import pytest

def test_fight_returns_the_winner_and_winning_margin():
    pokemon_df = pd.read_csv("tests/pokemon.csv")
    pokemon_df.set_index("name", inplace=True)
    input1 = 'Bulbasaur'
    input2 = 'Ivysaur'
    
    test_obj = Fight()
    
    result = test_obj.fight(input1, input2, pokemon_df)
    
    assert result == ('Ivysaur', 6.5)
    
def test_fight_returns_draw_when_both_inputs_are_same():
    pokemon_df = pd.read_csv("tests/pokemon.csv")
    pokemon_df.set_index("name", inplace=True)
    input1 = 'Bulbasaur'
    input2 = 'Bulbasaur'
    
    test_obj = Fight()
    
    result = test_obj.fight(input1, input2, pokemon_df)
    
    assert result == ('Draw', 0)
    
def test_fight_returns_the_winner_and_winning_margin_when_one_input_is_slightly_mispelled():
    pokemon_df = pd.read_csv("tests/pokemon.csv")
    pokemon_df.set_index("name", inplace=True)
    input1 = 'Bulbasau'
    input2 = 'Ivysaur'
    
    test_obj = Fight()
    
    result = test_obj.fight(input1, input2, pokemon_df)
    
    assert result == ('Ivysaur', 6.5)

def test_fight_returns_the_winner_and_winning_margin_when_second_input_is_slightly_mispelled():
    pokemon_df = pd.read_csv("tests/pokemon.csv")
    pokemon_df.set_index("name", inplace=True)
    input1 = 'Bulbasaur'
    input2 = 'Ivysau'
    
    test_obj = Fight()
    
    result = test_obj.fight(input1, input2, pokemon_df)
    
    assert result == ('Ivysaur', 6.5)
    
def test_fight_returns_error_when_first_input_is_mispelled():
    pokemon_df = pd.read_csv("tests/pokemon.csv")
    pokemon_df.set_index("name", inplace=True)
    input1 = 'Bulbosour'
    input2 = 'Ivysaur'
    
    test_obj = Fight()
    
    with pytest.raises(UnboundLocalError):
        test_obj.fight(input1, input2, pokemon_df)
        
def test_fight_returns_error_when_second_input_is_mispelled():
    pokemon_df = pd.read_csv("tests/pokemon.csv")
    pokemon_df.set_index("name", inplace=True)
    input1 = 'Bulbasaur'
    input2 = 'Ivysr'
    
    test_obj = Fight()
    
    with pytest.raises(UnboundLocalError):
        test_obj.fight(input1, input2, pokemon_df)
        
def test_fight_returns_error_when_both_inputs_are_mispelled():
    pokemon_df = pd.read_csv("tests/pokemon.csv")
    pokemon_df.set_index("name", inplace=True)
    input1 = 'Bulbar'
    input2 = 'Ivysr'
    
    test_obj = Fight()
    
    with pytest.raises(UnboundLocalError):
        test_obj.fight(input1, input2, pokemon_df)
    
    
    