from random import choice

class RockPaperScissors():
    pc_name = "RPS_Pro_3000"
    
    def __init__(self, name, standings={"Wins": 0, "Draws": 0, "Losses": 0, "Total played": 0}, win_ratio=0):
        self.name = name
        self.standings = standings
        self.ratio = win_ratio
        
    def show_standings(self):
        if self.standings["Total played"] > 0:
            print(f"\nHello {self.name},\nYour current standings are:")
            print(">", self.standings, "\n")
        else:
            print(f"\nYou haven't played any games {self.name}, play a few rounds and come back!")
        
    def show_ratio(self):
        # calculate ratio IF games have been played 
        if self.standings["Total played"] > 0:
            if self.standings["Losses"] != 0 or self.standings["Wins"] == 0:
                self.ratio = self.standings["Wins"] / self.standings["Losses"]
                print(f"\nHello {self.name},\nYour win ratio is:\n> {self.ratio} Wins per Loss")
                if self.ratio >= 1:
                    print("Keep it up!")
                    if self.ratio >= 2:
                        print("You're absolutely crushing it")
                else:
                    print("Not good. You can do better!")
            else:
                print(f"\nHello {self.name},\nYour win ratio is:\n> ∞ Wins per Loss")        
        else:
            print(f"\nYou haven't played any games {self.name}, play a few rounds and come back!")
            
    def play(self):
        print("\n<<<<<<<<<<<==========>>>>>>>>>>>")
        print("Let's play Rock, Paper, Scissors")
        print("<<<<<<====================>>>>>>\n")
        while True:
            # capture user input of hand thrown or quit request
            user_throw = input(f"Throw a hand ({self.standings['Total played']+1}):\n\t'r' - Rock\n\t'p' - Paper\n\t's' - Scissors\n\t'q' - Quit or Go back to Game Menu\n")
            self.standings["Total played"] += 1
            pc_throw = choice(["r","p","s"])
            # hands will be defined based on r, p, or s user_input and pc_choice
            pc_hand = ""
            user_hand = ""
            # label each letter (r,p,s) as rock, paper, or scissors for pc
            if pc_throw == "r":
                pc_hand = "Rock"
            elif pc_throw == "p":
                pc_hand = "Paper"
            elif pc_throw == "s":
                pc_hand = "Scissors"

            # label each letter (r,p,s) as rock, paper, or scissors for user
            if user_throw.lower() == "r":
                user_hand = "Rock"
            elif user_throw.lower() == "p":
                user_hand = "Paper"
            elif user_throw.lower() == "s":
                user_hand = "Scissors"

            # quit option decrements Total played because it was incremented wrongfully
            if user_throw.lower() == 'q':
                self.standings["Total played"] -= 1
                break
            else:
                # user threw a hand
                if user_throw.lower() == 'r' or user_throw.lower() == 'p' or user_throw.lower() == 's':

                    print(f"\n>You threw *{user_hand.upper()}*")
                    print("PC has thrown their hand...")
                    # suspense
                    checkpoint = input("Enter any key to continue: ")
                    print(f"\n>PC threw a *{pc_hand.upper()}*")

                    # win, lose, or draw
                    if user_throw.lower() == pc_throw:
                        print("\n====")
                        print("TIE!")
                        print("====\n")
                        print("**It's a Draw!**\n")
                        self.standings["Draws"] += 1

                    elif user_throw.lower() == "r" and pc_throw == "s":
                        print("\n>>>>>>>>")
                        print("YOU W0N!")
                        print(">>>>>>>>\n")
                        print("**You Rock!**\n")
                        self.standings["Wins"] += 1
                        
                    elif user_throw.lower() == "p" and pc_throw == "r":
                        print("\n>>>>>>>>")
                        print("YOU W0N!")
                        print(">>>>>>>>\n")
                        print("**You're the sheet!**\n")
                        self.standings["Wins"] += 1
                        
                    elif user_throw.lower() == "s" and pc_throw == "p":
                        print("\n>>>>>>>>")
                        print("YOU W0N!")
                        print(">>>>>>>>\n")
                        print("**Cutting Victory!**\n")
                        self.standings["Wins"] += 1
                        
                    else:
                        print("\n<<<<<<<<")
                        print("YOU LOST")
                        print("<<<<<<<<\n")
                        print("**You lost. Unlucky son!**\n")
                        self.standings["Losses"] += 1
                
                # catch all non-q and non-r/p/s inputs - repeat the loop and decrement total played as it was incremented wrongfully
                else:
                    print("Please enter valid input")
                    self.standings["Total played"] -= 1

   
    def menu(self):
        print("***************************************")
        print("Welcome to RockPaperScissors on Python!")
        print("***************************************")
        while True:
            menu = input("\nGame Menu\nChoose an option:\n\t'p' - Play Rock, Paper, Scissors\n\t's' - Show W/D/L standings\n\t'r' - Show Win ratio\n\t'q' - Quit?\n")
            if menu.lower() == 'q':
                print(self.standings)
                if self.standings["Total played"] > 0:
                    if self.standings["Losses"] != 0 or self.standings["Wins"] == 0:
                        self.ratio = self.standings["Wins"] / self.standings["Losses"]
                        print(f"Your win ratio is {self.ratio} Wins per Loss")
                        print(f"\nGoodbye {self.name},\nCome and play again soon!")
                        break
                    else:
                        print(f"Your win ratio is ∞(infinity) Wins per Loss")
                        print(f"\nGoodbye {self.name},\nCome and play again soon!")
                        break
            elif menu.lower() == 's':
                self.show_standings()
            elif menu.lower() == 'r':
                self.show_ratio()
            elif menu.lower() == 'p':
                self.play()
            else:
                print("Please enter valid input")
                        
                              
my_game = RockPaperScissors("User_name")

my_game.menu()