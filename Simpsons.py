import tkinter as tk
from random import randint

epslist = [13, 22, 24, 22, 22,
            25, 25, 25, 25, 23,
            22, 21, 22, 22, 22,
            21, 22, 22, 20, 21,
            23, 22, 22, 22, 22,
            22, 22, 22, 21, 23,
            22, 21, 22, 22]
numseas = 34

def generate_numbers():
    sum = 0
    for i in range(0, numseas-1):
        sum += epslist[i]

    episodeno = randint(1, sum)
#    episodeno = 666

    episode = episodeno
    season = 1
    while episode > epslist[season-1]:
        episode -= epslist[season-1]
        season += 1

    label1.config(text=f"Season: {season}")
    label2.config(text=f"Episode: {episode}")
    label3.config(text=f"Episode No.: {episodeno}")


root = tk.Tk()
root.title("'The Simpsons' Episode Picker")

frame = tk.Frame(root)
frame.pack()

label1 = tk.Label(frame, text="Season: -", width=10)
label1.grid(row=1, column=0)

label2 = tk.Label(frame, text="Episode: -", width=10)
label2.grid(row=2, column=0)

label3 = tk.Label(frame, text="Episode No.: -", width=45)
label3.grid(row=0, column=0)

button = tk.Button(frame, text="Generate Episode!", command=generate_numbers)
button.grid(row=4, column=0)

root.mainloop()
