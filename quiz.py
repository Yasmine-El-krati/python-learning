import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
from question_quiz import quiz_data

#function
current_question = 0
score = 0
def next_question ():
    global current_question
    current_question += 1
#  if condition if ther is anther quetion pass to it
    if current_question < len(quiz_data) :
        show_question()
    else:

        messagebox.showinfo("Quiz Completed", "Final score: {}/{}".format(score, len(quiz_data)) + " 🎉")
        root.destroy()



def show_question() :
    question=quiz_data[current_question]
    question_label.config(text=question["question"])

    choices=question["choices"]
    for i in range(3):
        choice_button[i].config(text=choices[i] , state="normal",bg="NavajoWhite", fg="black")
    type_of_answer_label.config(text="")
    next_button.config(state="disabled")

def check_answer(choice):

    question = quiz_data[current_question]
    selected_choice = choice_button[choice].cget("text")
    #if condition
    if selected_choice  == question["answer"]:
        global score
        score += 1
        score_label.config(text="score: {}/{}".format(score,len(quiz_data)))
        type_of_answer_label.config(text="correct! 🎉 ")
    else:
        type_of_answer_label.config(text="incorrect! 😢 ")
    next_button.config(state="normal")
    for btn in choice_button:
        btn.config(state="disabled")
def quit_button ():
    root.quit()


root=tk.Tk()


root.title("Quiz_App")
root. geometry("800x600")
style = Style()
style.configure("TLabel", font=("Helvetica", 20))
root.config(bg="SaddleBrown")

question_label=tk.Label(
    root,
    anchor="center",
    wraplength=500,
    pady=40
)
question_label.pack(pady=50)
question_label.config( bg="Peru",fg="Black")
#choice buttons
choice_button = []
for i in range(3) :
    button=tk.Button(
        root,
        command= lambda i=i : check_answer(i),

    )
    button.pack(pady=5)
    choice_button.append(button) #the button is appended to the choice_button list

#the answer is correct or incorrect
type_of_answer_label = tk.Label(
    root,
    anchor="center"
)
type_of_answer_label.pack(pady=40)

#score
score = 0
score_label=tk.Label(
    root,
    text="score:0/{}".format(len(quiz_data)),
    anchor="center",
    pady=10,
)
score_label.pack(pady=10)
score_label.config(bg="Maroon",fg="White")

#next button
next_button=tk.Button(
    root,
    text="next question ",
    command = next_question,
    state="disabled" ,  # until an answer is selected
)
next_button.pack(pady=10)
next_button.config( bg="DarkOrange",fg="Black")
#Quit
Quit_button=tk.Button(
    root,
    text="Quit",
    command=quit_button,
    state="normal" , # until an answer is selected

)
Quit_button.pack(pady=10)
Quit_button.config( bg="DarkOrange",fg="Black")
#excut question

show_question()

root.mainloop()
