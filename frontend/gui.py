import tkinter as tk
import xmlrpc.client


# Connect to XML-RPC server
proxy = xmlrpc.client.ServerProxy(
    "http://localhost:8000/"
)


window = tk.Tk()

window.title("Basic Calculator")
window.geometry("350x450")


expression = ""


display = tk.Entry(
    window,
    font=("Arial", 20),
    justify="right"
)

display.pack(
    fill="both",
    padx=10,
    pady=20
)


def click(value):
    global expression

    expression += str(value)

    display.delete(0, tk.END)
    display.insert(0, expression)



def calculate():
    global expression

    try:
        parts = expression.split()

        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])


        if operator == "+":
            result = proxy.add(num1, num2)

        elif operator == "-":
            result = proxy.sub(num1, num2)

        elif operator == "*":
            result = proxy.mul(num1, num2)

        elif operator == "/":
            result = proxy.div(num1, num2)


        display.delete(0, tk.END)
        display.insert(0, result)

        expression = str(result)


    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def clear():
    global expression

    expression = ""

    display.delete(0, tk.END)



buttons = [
    ("7",7),
    ("8",8),
    ("9",9),
    ("+", "+"),

    ("4",4),
    ("5",5),
    ("6",6),
    ("-", "-"),

    ("1",1),
    ("2",2),
    ("3",3),
    ("*", "*"),

    ("0",0),
    ("C","C"),
    ("=","="),
    ("/","/")
]


frame = tk.Frame(window)
frame.pack()


row = 0
col = 0


for text,value in buttons:

    if value == "=":
        command = calculate

    elif value == "C":
        command = clear

    else:
        command = lambda v=value: click(" " + str(v) + " ")


    button = tk.Button(
        frame,
        text=text,
        width=7,
        height=3,
        command=command
    )


    button.grid(
        row=row,
        column=col,
        padx=5,
        pady=5
    )


    col += 1

    if col == 4:
        col = 0
        row += 1



window.mainloop()