from tkinter import*

def press(num):

    global equation_text
    equation_text += str(num) # we have used equation_text as a variable and also within the value too
                                             # because we want to be able to write more numbers instead of just one
                                             # on the label. It's basically incrementing
    equation_label.set(equation_text)

def equals():

    global equation_text
    try:
        total = str(eval(equation_text)) # eval is for getting the total amount
        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError:
        equation_label.set("Arithmatic error")
    except SyntaxError:
        equation_label.set("Syntax error")

def backspace():
    global equation_text
    equation_text = equation_text[:-1]  # Remove the last character
    equation_label.set(equation_text)


def clear():

    global equation_text
    equation_label.set("")
    equation_text = "" # We have to keep this also empty as when we ckear the texts from the label and try to type
                       # in the label again, what we wrote previously will appear again in the label when we try to
                       # type something new

window = Tk()
window.title("Calculator")
window.geometry("500x500")

equation_text = ""

equation_label = StringVar()

writing_label = Label(window,textvariable=equation_label,font=("Arial",15),width=30,height=3,bg="#E2f5f6")
writing_label.pack()

number_frame = Frame(window)
number_frame.pack()

button_one = Button(number_frame,text=1,width=10,height=4,bg="#66b6d2",relief=RAISED,bd=4,command=lambda:press(1))
button_one.grid(row=0,column=0)

button_two = Button(number_frame,text=2,width=10,height=4,bg="#66b6d2",relief=RAISED,bd=4,command=lambda:press(2))
button_two.grid(row=0,column=1)

button_three = Button(number_frame,text=3,width=10,height=4,bg="#66b6d2",relief=RAISED,bd=4,command=lambda:press(3))
button_three.grid(row=0,column=2)

button_four = Button(number_frame,text=4,width=10,height=4,bg="#66b6d2",relief=RAISED,bd=4,command=lambda:press(4))
button_four.grid(row=1,column=0)

button_five = Button(number_frame,text=5,width=10,height=4,bg="#66b6d2",relief=RAISED,bd=4,command=lambda:press(5))
button_five.grid(row=1,column=1)

button_six = Button(number_frame,text=6,width=10,height=4,bg="#66b6d2",relief=RAISED,bd=4,command=lambda:press(6))
button_six.grid(row=1,column=2)

button_seven = Button(number_frame,text=7,width=10,height=4,bg="#66b6d2",relief=RAISED,bd=4,command=lambda:press(7))
button_seven.grid(row=2,column=0)

button_eight = Button(number_frame,text=8,width=10,height=4,bg="#66b6d2",relief=RAISED,bd=4,command=lambda:press(8))
button_eight.grid(row=2,column=1)

button_nine = Button(number_frame,text=9,width=10,height=4,bg="#66b6d2",relief=RAISED,bd=4,command=lambda:press(9))
button_nine.grid(row=2,column=2)

button_zero = Button(number_frame,text=0,width=10,height=4,bg="#66b6d2",relief=RAISED,bd=4,command=lambda:press(0))
button_zero.grid(row=3,column=0)

button_plus = Button(number_frame,text="+",width=10,height=4,bg="#F03c40",relief=RAISED,bd=4,command=lambda:press("+"))
button_plus.grid(row=0,column=3)

button_minus = Button(number_frame,text="-",width=10,height=4,bg="#F03c40",relief=RAISED,bd=4,command=lambda:press("-"))
button_minus.grid(row=1,column=3)

button_multiply = Button(number_frame,text="*",width=10,height=4,bg="#F03c40",relief=RAISED,bd=4,command=lambda:press("*"))
button_multiply.grid(row=2,column=3)

button_division = Button(number_frame,text="/",width=10,height=4,bg="#F03c40",relief=RAISED,bd=4,command=lambda:press("/"))
button_division.grid(row=3,column=3)

button_equal = Button(number_frame,text="=",width=10,height=4,bg="#F03c40",relief=RAISED,bd=4,command=equals)
button_equal.grid(row=3,column=2)

button_fullstop = Button(number_frame,text=".",width=10,height=4,bg="#F03c40",relief=RAISED,bd=4,command=lambda:press("."))
button_fullstop.grid(row=3,column=1)

button_backspace = Button(number_frame,text="backspace",width=10,bg="#F03c40",relief=RAISED,bd=4,height=4,command=backspace)
button_backspace.grid(row=4,column=2)

button_clear = Button(number_frame,text="clear",width=10,height=4,bg="#F03c40",relief=RAISED,bd=4,command=clear)
button_clear.grid(row=4,column=1)

window.mainloop()
