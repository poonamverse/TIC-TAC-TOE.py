import tkinter as tk
from tkinter import messagebox

def check_winner():
    for combo in[[0,1,2] , [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8],[2,4,6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] !="":
            buttons[combo[0]].config(bg= "green")
            buttons[combo[1]].config(bg= "green")
            buttons[combo[2]].config(bg= "green")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            root.quit()

def check_tie():
    if all(button["text"] != "" for button in buttons):
        messagebox.showinfo("Tic-Tac-Toe", "It's a Tie!")
        root.quit()            

def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] =  current_player
        check_winner()
        check_tie()
        toggle_player()  #changes current player

#here we will use toggle func, which will help to change current player 

def toggle_player():
    global current_player
    current_player ="X" if current_player == "o" else"o"
    label.config(text=f"Player {current_player}'s turn")

 #now we will make root window which comes from tkinter, will nae this window tic tak tow, and call by root

root = tk.Tk()
root.title("Tic-Tac-Toe")

##python trick to make buttons in one line:

buttons = [tk.Button(root,text="", font=("normal",25), width=6,height=2,command=lambda i=i: button_click(i)) for i in range(9)]

#to arrange these buttons in grids(3x3), for this will use enumerate func:which will gve us index also along with every button
#then use grid method to arrange in rows n columns, which will calculate by button's index

for i , button in enumerate(buttons):
    button.grid(row=i //3, column=i%3)

current_player = "X"
winner = False 
label = tk.Label(root, text=f"Player{current_player}'s turn", font=("normal",25))
label.grid(row=3,column=0,columnspan=3)
root.mainloop()

     
            