# Import der gameState Klasse aus dem gamestateobs module.
from state.gamestateobs import gameState as gs

def main():
    '''
    Main Funktion für pyEleven:
    hier wird unsere Anwendung mit einem init-State instanziiert.
    '''
    gs.update_game_state('init_game')
   
if __name__ == '__main__':
    main()