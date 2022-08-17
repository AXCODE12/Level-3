import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
    q = simpledialog.askstring('q','Ask a question')
    # Make a variable and initialize it to a random number between 0 and 3
    ran = random.randint(0,3)
    # If the random number is 0
    if ran == 0:
        # tell the user "Yes"
        messagebox.showinfo('a','Yes')
    # If the random number is 1
    elif ran == 1:
        # tell the user "No"
        messagebox.showinfo('a','No')
    # If the random number is 2
    elif ran == 2:
        # tell the user "Maybe you should ask Google?"
        messagebox.showinfo('a','Maybe you should ask Google')
    # If the random number is 3
    else:
        # write your own answer
        messagebox.showinfo('a','Bad question')