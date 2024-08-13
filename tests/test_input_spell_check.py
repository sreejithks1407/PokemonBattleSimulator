from src.input_spell_check import Spellcheck
import pandas as pd


def test_check_spelling_returns_exact_same_input_if_input_correctly_spelled() -> None:
    input = 'bulbasaur'
    pokemon_list = ['bulbasaur', 'ivysaur', 'venusaur']    
    test_obj = Spellcheck()

    assert test_obj.check_spelling(input, pokemon_list) == ['bulbasaur']
    
def test_check_spelling_returns_updated_input_if_input_wrongly_spelled() -> None:
    input = 'bulbasaut'
    pokemon_list = ['bulbasaur', 'ivysaur', 'venusaur']    
    test_obj = Spellcheck()

    assert test_obj.check_spelling(input, pokemon_list) == ['bulbasaur']
    
def test_check_spelling_returns_empty_output_if_input_too_wrongly_spelled() -> None:
    input = 'bulbosauthj'
    pokemon_list = ['bulbasaur', 'ivysaur', 'venusaur']    
    test_obj = Spellcheck()

    assert test_obj.check_spelling(input, pokemon_list) == []
    
def test_pokemon_name_correction_returns_exact_same_input_if_input_correctly_spelled() -> None:
    df_dict = {"name":['bulbasaur', 'ivysaur', 'venusaur'], "speed":[45, 50, 55]}
    df = pd.DataFrame(df_dict)
    df.set_index("name", inplace=True)
    
    input_1 = 'bulbasaur'
    input_2 = 'ivysaur'   
    test_obj = Spellcheck()
    
    assert test_obj.pokemon_name_correction(input_1, input_2, df) == ['bulbasaur', 'ivysaur']
    
def test_pokemon_name_correction_returns_updated_input_if_input_wrongly_spelled() -> None:
    df_dict = {"name":['bulbasaur', 'ivysaur', 'venusaur'], "speed":[45, 50, 55]}
    df = pd.DataFrame(df_dict)
    df.set_index("name", inplace=True)
    
    input_1 = 'bulbasau'
    input_2 = 'ivysau'   
    test_obj = Spellcheck()
    
    assert test_obj.pokemon_name_correction(input_1, input_2, df) == ['bulbasaur', 'ivysaur']
    
def test_pokemon_name_correction_returns_no_output_if_input_too_wrongly_spelled() -> None:
    df_dict = {"name":['bulbasaur', 'ivysaur', 'venusaur'], "speed":[45, 50, 55]}
    df = pd.DataFrame(df_dict)
    df.set_index("name", inplace=True)
    
    input_1 = 'bulbasaulk'
    input_2 = 'ivysaupk'   
    test_obj = Spellcheck()
    
    assert test_obj.pokemon_name_correction(input_1, input_2, df) == []
    