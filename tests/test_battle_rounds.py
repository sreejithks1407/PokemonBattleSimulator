from src.battle_rounds import Batterounds
import pandas as pd
import pytest

def test_battle_round_1_returns_battle_round_1_values():
    
    df = pd.read_csv("tests/pokemon.csv")
    df.set_index("name", inplace=True)
    test_obj = Batterounds()
    
    result = test_obj.battle_round_1('Bulbasaur','Ivysaur', df)
    assert result == (49, 0.25, 1)
    
def test_battle_round_1_returns_battle_round_1_values_for_same_input():
    
    df = pd.read_csv("tests/pokemon.csv")
    df.set_index("name", inplace=True)
    test_obj = Batterounds()
    
    result = test_obj.battle_round_1('Bulbasaur','Bulbasaur', df)
    assert result == (49, 0.25, 1)
    
def test_battle_round_1_returns_error_for_wrong_inputs():
    
    df = pd.read_csv("tests/pokemon.csv")
    df.set_index("name", inplace=True)
    test_obj = Batterounds()
    
    with pytest.raises(KeyError):
        test_obj.battle_round_1('Bulbasau','Bulbasaur', df)

    
def test_battle_round_2_returns_battle_round_2_values():
    
    df = pd.read_csv("tests/pokemon.csv")
    df.set_index("name", inplace=True)
    test_obj = Batterounds()
    
    result = test_obj.battle_round_2('Bulbasaur','Ivysaur', df)
    assert result == (62, 0.25, 1)
    
def test_battle_round_2_returns_battle_round_2_values_for_same_input():
    
    df = pd.read_csv("tests/pokemon.csv")
    df.set_index("name", inplace=True)
    test_obj = Batterounds()
    
    result = test_obj.battle_round_2('Ivysaur','Ivysaur', df)
    assert result == (62, 0.25, 1)
    
def test_battle_round_2_returns_error_for_wrong_inputs():
    
    df = pd.read_csv("tests/pokemon.csv")
    df.set_index("name", inplace=True)
    test_obj = Batterounds()
    
    with pytest.raises(KeyError):
        test_obj.battle_round_1('Bulbasau','Ivysaur', df)