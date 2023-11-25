import time
import tkinter as tk
from PIL import Image,ImageTk

class Window:
    def __init__(self,root):
        self.root = root
        self.win_condition = False
        self.player_turn = 0
        self.check_if_all_clicked = True
        self.list_Of_Buttons = [[] * 3 for i in range(3)]
        self.root.title("TicTacToe game")
        self.root.geometry("1000x1000")
        self.root.configure(bg="cyan")
        self.label = tk.Label(text="Tic Tac Toe", height=2, bg="cyan", fg="black", font=("Courier",44))
        self.label.pack(pady=10)
        self.label.place(x=200, y=50)
        for i in range(3):
            for j in range(3):
                self.button = Button(root)
                self.button.button.place(x=(j+1)*160, y=(i+1)*160)
                self.list_Of_Buttons[i].append(self.button)


    def reset(self, top):
        for b in self.list_Of_Buttons:
            b.button.reset_button()
        top.destroy()


    def winner_window(self, XorO, list_of_Buttons):
        top = tk.Toplevel(self.root)
        top.geometry("750x250")
        top.title("Child Window")
        win_message = tk.Label(top, text="", font=('Mistral 18 bold'))
        win_message.place(x=150, y=80)
        output_text = ""

        if XorO == "":
            output_text = "there is a Tie!"
        else:
            tk.Label(top, text="The winner is: " + XorO, font=('Mistral 18 bold')).place(x=150, y=80)
        for b in self.list_Of_Buttons:
            b.reset_button()
            # winner.configure(text="Tie!")

            output_text = "The winner is: " + XorO
        win_message.pack(pady=10)
        # time.sleep(3)
        win_message.configure(text=output_text)
        restart_button = tk.Button(top, text="click to restart", command=lambda: self.reset(top), height=10, width=30)
        restart_button.pack(pady=10)

    def do_nothing(self):
        return

    def check_Winner(self, XorO):
        rowLen = len(self.list_Of_Buttons[0])
        for i in range(rowLen):
            # checking diagonal bottom right to Top left
            if self.list_Of_Buttons[rowLen - i - 2][i + 1] == self.list_Of_Buttons[rowLen - 1][0].type and self.list_Of_Buttons[rowLen - 1][0].type != None:
                if i + 2 == rowLen:
                    self.win_condition = True
                    return
            else:
                break
            # checking diagonal top left to bottom right
            if self.list_Of_Buttons[i + 1][i + 1].type == self.list_Of_Buttons[0][0] and self.list_Of_Buttons[0][0] != None :
                if i + 2 == rowLen:
                    self.win_condition = True
                    return
            else:
                break
            for j in range(rowLen):
                # checking rows
                if self.list_Of_Buttons[i][j + 1].type == self.list_Of_Buttons[i][0].type and self.list_Of_Buttons[i][0].type != None:
                    if j + 2 == rowLen:
                        self.win_condition = True
                        return
                else:
                    break
                # checking columns
                if self.list_Of_Buttons[j + 1][i].type == self.list_Of_Buttons[0][i].type and self.list_Of_Buttons[0][i].type != None:
                    if j + 2 == rowLen:
                        self.win_condition = True
                    return
                else:
                    break


        if (self.win_condition):
            for b in self.list_Of_Buttons:
                b.button.configure(command=self.do_nothing)
            self.winner_window(XorO)
            return


        for i in range(len(self.list_Of_Buttons)):
            for j in range(len(self.list_Of_Buttons)):
                if self.list_Of_Buttons[i][j].is_clicked == False:
                    self.check_if_all_clicked = False
        if self.check_if_all_clicked:
            self.winner_window("")


        # if True:
        #     self.label = tk.Label(text="the winner is: ", height=2, bg="cyan", fg="black", font=("Courier", 44))
        #     self.label.pack(pady=10)
        #     self.label.place(x=200, y=650)

    def restart_game(self):
        for b in self.list_Of_Buttons:
            b.reset_button()
        pass


class Button():
    def __init__(self,root):
        self.root = root
        self.white_img =  ImageTk.PhotoImage(Image.open('Color-white.jpeg').resize((100,100)))
        self.o_img = ImageTk.PhotoImage(Image.open('O_img.png').resize((155, 155)))
        self.x_img = ImageTk.PhotoImage(Image.open("X_img.png").resize((155, 155)))
        self.button = tk.Button(root,command=self.PlaceXO,image=self.white_img, height=155, width=155, bg="orange")
        self.button.image = self.white_img
        self.button.pack(pady=6,padx=3)
        self.is_clicked = False
        self.type = None

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
