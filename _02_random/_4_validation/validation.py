import random
from tkinter import messagebox, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    random_number = random.randint(1, 5)

    print(random_number)

    # TODO 1) Use each value of random_number to give the user a random compliment

    # TODO 2) Repeat all the code above 10 times

    # TODO 3) Find someone to test out your program. They will like it :)

for i in range(10):
    random_number = random.randint(1, 5)
if random_number == 1:
    messagebox.showinfo('a','You have a nice smile!')
elif random_number == 2:
    messagebox.showinfo('a','You look strong')
elif random_number == 3:
    messagebox.showinfo('a','You look good today')
elif random_number == 4:
    messagebox.showinfo('a','You are an incredible human')
elif random_number == 5:
    messagebox.showinfo('a','You are nothing less than special')
else:
    messagebox.showinfo('a','You are always there for me')


