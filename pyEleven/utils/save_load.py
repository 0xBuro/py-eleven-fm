import os
import json

def save_state(path, manager_dict):
    '''
    Speichert Spielstand als JSON.
    
    Args:
        path (str): Pfad für JSON-Datei.
        manager_dict (dict): Dictionary mit Game State Daten.
    '''
    with open(path, 'w') as file:
        json.dump(manager_dict, file)

def load_state(path):
    '''
    Lädt den Spielstand aus JSON.
    
    Args:
        path (str): Pfad zur JSON-Datei.
    
    Returns:
        dict: lädt Game State als Dictionary.
        None: Falls Datei nicht existiert.
    '''
    if os.path.exists(path):
        with open(path, 'r') as file:
            game_state = json.load(file)
        return game_state   
    else:
        return None 

