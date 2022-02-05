from tkinter import Tk, Button

def enginma():
    conundrum['text'] = mystery['text']

puzzle = Tk()

conundrum = Button(puzzle, text = '???')
conundrum.pack()

mystery = Button(puzzle, text = '!!!', command = enginma) 
mystery.pack()

puzzle.mainloop()