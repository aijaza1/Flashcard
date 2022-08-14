from tkinter import *
from tkmacosx import Button
from random import randint

root = Tk()
root.title('Flashcard')
root.geometry("550x410")

words = [
    (("Assan"), ("Easy")),
    (("Mushkil"), ("Hard")),
    (("Bura"), ("Bad")),
    (("Nazdeek"), ("Near")),
    (("Aana"), ("Come")),
    (("Door"), ("Far")),
    (("Barha"), ("Big")),
    (("Waqt"), ("Time")),
    (("Mein"), ("I")),
    (("Tum"), ("You")),
    (("Mazaydar"), ("Delicious")),
]




# get count of list
count = len(words)


def next():
    global hinter, hintCount, randomWord

    # clear screen
    answerLabel.config(text="", bg="white")
    myEntry.delete(0, END)
    hintLabel.config(text="")
    hinter = ""
    hintCount = 0

    randomWord = randint(0, count - 1)

    # update label with urdu word
    urduWord.config(text=words[randomWord][0])


def answer():
    if myEntry.get().capitalize() == words[randomWord][1]:
        answerLabel.config(bg="green", text=f"Correct! {words[randomWord][0]} means {words[randomWord][1]}")
    else:
        answerLabel.config(bg="red", text=f"Incorrect! {words[randomWord][0]} is not {myEntry.get()}")


hintCount = 0
# keep track of hints
hinter = ""


def hint():
    global hintCount
    global hinter

    if hintCount < len(words[randomWord][1]):
        hinter = hinter + words[randomWord][1][hintCount]
        hintLabel.config(text=hinter)
        hintCount += 1


urduWord = Label(root, text="", font=("Arial", 35))
urduWord.pack(pady=50)

answerLabel = Label(root, text="")
answerLabel.pack(pady=20)

myEntry = Entry(root, font=("Arial", 15))
myEntry.pack(pady=20)

# buttons
buttonFrame = Frame(root)
buttonFrame.pack(pady=20)

answerButton = Button(buttonFrame, text="Answer", command=answer)
answerButton.grid(row=0, column=0, padx=20)

nextButton = Button(buttonFrame, text="Next", command=next)
nextButton.grid(row=0, column=1, padx=20)

hintButton = Button(buttonFrame, text="Hint", command=hint)
hintButton.grid(row=0, column=2, padx=20)

# hint label
hintLabel = Label(root, text="")
hintLabel.pack(pady=20)

# run next fun when prog starts
next()

root.mainloop()
