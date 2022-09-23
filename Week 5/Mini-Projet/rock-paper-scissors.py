import random


class Game:
    def __init__(self):
        self.user_action = self.get_user_item()
        self.possible_actions1 = self.get_computer_item()

    @staticmethod
    def get_user_item():
        user_action = input("Enter a choice (rock, paper, scissors): ")
        possible_actions = ["rock", "paper", "scissors"]
        print(f'From {possible_actions} you choose {user_action}')
        return user_action

    @staticmethod
    def get_computer_item():
        possible_actions1 = ["rock", "paper", "scissors"]
        computer_action = random.choice(possible_actions1)
        # print(f"\nYou chose {self.user_action}, computer chose {computer_action}.\n")
        return computer_action

    def get_game_result(self):
        if self.user_action == self.possible_actions1:
            return f"Both players selected {self.user_action}. It's a tie!"
        elif self.user_action == "rock":
            if self.possible_actions1 == "scissors":
                return "Rock smashes scissors! You win!"
            else:
                return "Paper covers rock! You lose."
        elif self.user_action == "paper":
            if self.possible_actions1 == "rock":
                return "Paper covers rock! You win!"
            else:
                return "Scissors cuts paper! You lose."
        elif self.user_action == "scissors":
            if self.possible_actions1 == "paper":
                return "Scissors cuts paper! You win!"
            else:
                return "Rock smashes scissors! You lose."


jeu = Game()
print(jeu.get_game_result())

# Il s'agit ici du jeu piere papier sciseau. Le principe est simple:
# Un utilisateur rentre une condition entre la pierre le papier et le sciseau.
# Apres, la machine elle devra choisir sa condition et allez a l'encontre de la votre.
# Si jamais une des conditions comme presentée si haut aboutissent, On a: soit un gagnant,
# soit un perdant soit une situation de match nulle.
