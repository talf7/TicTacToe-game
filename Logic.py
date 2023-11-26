import time
import tkinter as tk
from PIL import Image,ImageTk

class Main_Menu:
    def __init__(self,root):
        self.root = root
        self.root.title("TicTacToe Main Menu")
        self.root.geometry("900x500")
        self.root.resizable(False, False)


class Window:
    def __init__(self,root):
        self.root = root
        self.win_condition = False
        self.player_turn = 0
        self.check_if_all_clicked = True
        self.list_Of_Buttons = [[] * 3 for i in range(3)]
        self.root.title("TicTacToe game")
        self.root.focus()
        self.root.resizable(False,False)
        self.root.geometry("900x750")
        self.root.configure(bg="cyan")
        self.label = tk.Label(text="Tic Tac Toe", height=2, bg="cyan", fg="black", font=("Courier",44))
        self.label.pack(pady=10)
        self.label.place(x=200, y=50)
        for i in range(3):
            for j in range(3):
                self.button = XOButton(root)
                self.button.button.place(x=(j+1)*160, y=(i+1)*160)
                self.list_Of_Buttons[i].append(self.button)

        self.button1 = tk.Button(root, text="Main manu", height=1, width=10, bd='5', font=("Vladimir Script", 24), command=root.destroy)
        self.button1.pack(pady=10,padx=0)
        self.button1.place(x=800,y=160)
        self.button2 = tk.Button(root, text="Restart game", height=1, width=10, bd='5', font=("Vladimir Script", 24), command=self.restart_game)
        self.button2.pack(pady=10,padx=0)
        self.button2.place(x=800,y=260)
        self.button3 = tk.Button(root, text="Close game", height=1, width=10, bd='5', font=("Vladimir Script", 24), command=root.destroy)
        self.button3.pack(pady=10,padx=0)
        self.button3.place(x=800,y=360)

    def winner_window(self, XorO):
        output_text = ""

        if XorO == "":
            output_text = "there is a Tie!"
        else:
            output_text = "The winner is: " + XorO
        Winner_label = tk.Label(root, text=output_text, font=('Mistral 18 bold'))
        Winner_label.pack(pady=10,padx=10)
        Winner_label.place(x=330, y=650)

        for r in self.list_Of_Buttons:
            for b in r:
                b.reset_button()
            # winner.configure(text="Tie!")

            output_text = "The winner is: " + XorO
        win_message.pack(pady=10)
        # time.sleep(3)
        win_message.configure(text=output_text)
        # restart_button = tk.Button(top, text="click to restart", command=lambda: self.reset(top), height=10, width=30)
        # restart_button.pack(pady=10)

    def do_nothing(self):
        pass

    def check_Winner(self, XorO):
        rowLen = len(self.list_Of_Buttons[0])
        checkOne = True
        checkTwo = True
        shouldBreak = False

        for r in self.list_Of_Buttons:
            for b in r:
                print(b.is_clicked)
        for i in range(rowLen - 1):
            if shouldBreak:
                break
            # checking diagonal bottom right to Top left
            if self.list_Of_Buttons[rowLen - i - 2][i + 1].type == self.list_Of_Buttons[rowLen - 1][0].type and self.list_Of_Buttons[rowLen - 1][0].type != None and checkOne:
                if i + 2 == rowLen:
                    self.win_condition = True
                    break
            else:
                checkOne = False

            # checking diagonal top left to bottom right
            if self.list_Of_Buttons[i + 1][i + 1].type == self.list_Of_Buttons[0][0].type and self.list_Of_Buttons[0][0].type != None and checkTwo :
                if i + 2 == rowLen:
                    self.win_condition = True
                    break
            else:
                checkTwo = False
            checkThree = True
            checkFour = True
            for j in range(rowLen - 1):
            # checking rows
                if self.list_Of_Buttons[i][j + 1].type == self.list_Of_Buttons[i][0].type and self.list_Of_Buttons[i][0].type != None and checkThree:
                    if j + 2 == rowLen:
                        self.win_condition = True
                        shouldBreak = True
                        break
                else:
                    checkThree = False
                # checking columns
                if self.list_Of_Buttons[j + 1][i].type == self.list_Of_Buttons[0][i].type and self.list_Of_Buttons[0][i].type != None and checkFour:
                    if j + 2 == rowLen:
                        self.win_condition = True
                        shouldBreak = True
                        break
                else:
                    checkFour = False

        if self.win_condition:
            for r in self.list_Of_Buttons:
                for b in r:
                    b.button.configure(command=self.do_nothing)
            self.winner_window(XorO)
            return
        self.check_if_all_clicked = True
        for r in self.list_Of_Buttons:
            for b in r:
                if b.is_clicked == False:
                    self.check_if_all_clicked = False
        if self.check_if_all_clicked:
            self.winner_window("")


        # if True:
        #     self.label = tk.Label(text="the winner is: ", height=2, bg="cyan", fg="black", font=("Courier", 44))
        #     self.label.pack(pady=10)
        #     self.label.place(x=200, y=650)

    def restart_game(self):
        for i in range(3):
            for j in range(3):
                XOButton.reset_button(window.list_Of_Buttons[i][j])
        pass



class XOButton():
    def __init__(self, root):
        self.root = root
        self.white_img =  ImageTk.PhotoImage(Image.open('Color-white.jpeg').resize((100,100)))
        self.o_img = ImageTk.PhotoImage(Image.open('O_img.png').resize((155, 155)))
        self.x_img = ImageTk.PhotoImage(Image.open("X_img.png").resize((155, 155)))
        self.button = tk.Button(root,command=self.PlaceXO,image=self.white_img, height=155, width=155, bg="orange")
        self.button.image = self.white_img
        self.button.pack(pady=6,padx=3)
        self.is_clicked = False
        self.type = None
        #self.win_condition = False

    def reset_button(self):
        self.button.configure(command=self.PlaceXO,image=self.white_img)
        self.is_clicked = False
        self.type = None
        window.win_condition = False


    def PlaceXO(self):
        if self.is_clicked:
            return
        else:
            if window.player_turn == 0:
                self.button.configure(image=self.o_img)
                self.button.image = self.o_img
                window.player_turn = 1
                self.is_clicked = True
                self.type = "o"
                window.check_Winner("O")
            else:
                self.button.configure(image=self.x_img)
                self.button.image = self.x_img
                window.player_turn = 0
                #self.button.configure(command=)
                self.is_clicked = True
                self.type = "x"
                window.check_Winner("X")
        return


root = tk.Tk()
window = Window(root)

root.mainloop()
