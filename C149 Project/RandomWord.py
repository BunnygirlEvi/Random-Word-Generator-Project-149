from tkinter import *
import random
root = Tk();
root.title("Random Word Generator")
root.geometry("500x500")
root.configure(bg='lightblue')

wordHolder = Label(root, text="", font=("Arial", 25))
wordHolder.place(relx=0.5, rely=0.4, anchor=CENTER)


def randomizer():
    alphaList = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    random_no1 = random.randint(1,26)
    random_no2 = random.randint(1,26)
    random_no3 = random.randint(1,26)
    random_no4 = random.randint(1,26)
    random_no5 = random.randint(1,26)
    
    random_alpha1 = alphaList[random_no1]
    random_alpha2 = alphaList[random_no2]
    random_alpha3 = alphaList[random_no3]
    random_alpha4 = alphaList[random_no4]
    random_alpha5 = alphaList[random_no5]
    
    wordHolder["text"] = random_alpha1 + random_alpha2 + random_alpha3 + random_alpha4 + random_alpha5
    print(random_alpha1 + random_alpha2 + random_alpha3 + random_alpha4 + random_alpha5)
    
    
    
randomizer_button = Button(root,text="Randomizer", command = randomizer)
randomizer_button.place(width="100px",height="30px",relx=0.5,rely=0.6,anchor=CENTER)

root.mainloop()