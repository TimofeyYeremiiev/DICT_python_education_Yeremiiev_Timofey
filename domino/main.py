"""Main point"""
import game
import real_player
import computer

if __name__ == "__main__":
    gam = game.DominoGame()
    gam.add_player(real_player.RealPlayer(input("Ваше имя: "), gam))
    gam.add_player(computer.ComputerPlayer("Computer", gam))
    # gam.add_player(computer.ComputerPlayer("Computer 2", gam))
    gam.main_loop()
