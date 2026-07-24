import customtkinter as ctk
import xmlrpc.client
import os


# ==============================
# APPLICATION DETAILS
# ==============================

VERSION = "1.0.0"

HISTORY_FILE = "history.txt"


# ==============================
# XML-RPC CONNECTION
# ==============================

try:
    proxy = xmlrpc.client.ServerProxy(
        "http://localhost:8000/"
    )

except Exception:
    proxy = None



# ==============================
# THEME
# ==============================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")



# ==============================
# MAIN WINDOW
# ==============================

app = ctk.CTk()

app.title(
    f"⚡ Basic Calculator v{VERSION}"
)

app.geometry(
    "400x720"
)

app.resizable(
    False,
    False
)



# ==============================
# VARIABLES
# ==============================

expression = ""

history = []



# ==============================
# HISTORY FUNCTIONS
# ==============================


def save_history(entry):

    with open(
        HISTORY_FILE,
        "a"
    ) as file:

        file.write(
            entry + "\n"
        )



def load_history():

    if os.path.exists(HISTORY_FILE):

        with open(
            HISTORY_FILE,
            "r"
        ) as file:

            records = file.readlines()


            for record in records:

                history_box.insert(
                    "end",
                    record
                )

                history.append(
                    record.strip()
                )



def clear_history():

    history.clear()

    history_box.delete(
        "1.0",
        "end"
    )


    if os.path.exists(HISTORY_FILE):

        open(
            HISTORY_FILE,
            "w"
        ).close()



# ==============================
# HEADER
# ==============================


title = ctk.CTkLabel(

    app,

    text="BASIC CALCULATOR",

    font=(
        "Arial",
        26,
        "bold"
    )
)

title.pack(
    pady=(20,5)
)



subtitle = ctk.CTkLabel(

    app,

    text="XML-RPC Client Server Edition",

    font=(
        "Arial",
        12
    )
)

subtitle.pack()



# ==============================
# DISPLAY
# ==============================


display = ctk.CTkEntry(

    app,

    width=350,

    height=60,

    font=(
        "Arial",
        28
    ),

    justify="right"
)


display.pack(
    pady=25
)



# ==============================
# HISTORY AREA
# ==============================


history_label = ctk.CTkLabel(

    app,

    text="Calculation History",

    font=(
        "Arial",
        16
    )

)

history_label.pack()



history_box = ctk.CTkTextbox(

    app,

    width=350,

    height=100,

    font=(
        "Arial",
        14
    )
)

history_box.pack(
    pady=10
)



# ==============================
# CALCULATOR FUNCTIONS
# ==============================


def click(value):

    global expression


    expression += str(value)


    display.delete(
        0,
        "end"
    )


    display.insert(
        0,
        expression
    )




def calculate():

    global expression


    try:

        parts = expression.split()


        num1 = float(parts[0])

        operator = parts[1]

        num2 = float(parts[2])



        if operator == "+":

            result = proxy.add(
                num1,
                num2
            )


        elif operator == "-":

            result = proxy.sub(
                num1,
                num2
            )


        elif operator == "*":

            result = proxy.mul(
                num1,
                num2
            )


        elif operator == "/":

            result = proxy.div(
                num1,
                num2
            )


        else:

            result = "Invalid"



        display.delete(
            0,
            "end"
        )


        display.insert(
            0,
            str(result)
        )



        history_entry = (
            f"{num1} {operator} {num2} = {result}"
        )


        history.append(
            history_entry
        )


        history_box.insert(
            "end",
            history_entry + "\n"
        )


        save_history(
            history_entry
        )


        expression = str(result)



    except Exception:


        display.delete(
            0,
            "end"
        )


        display.insert(
            0,
            "Error"
        )




def clear():

    global expression


    expression = ""


    display.delete(
        0,
        "end"
    )



# ==============================
# BUTTONS
# ==============================


frame = ctk.CTkFrame(
    app
)

frame.pack(
    pady=10
)



buttons = [

    ("7","7"),
    ("8","8"),
    ("9","9"),
    ("/","/"),

    ("4","4"),
    ("5","5"),
    ("6","6"),
    ("*","*"),

    ("1","1"),
    ("2","2"),
    ("3","3"),
    ("-","-"),

    ("C","C"),
    ("0","0"),
    ("=","="),
    ("+","+")

]



row = 0
col = 0



for text,value in buttons:


    if value == "=":

        command = calculate
        color = "#27ae60"



    elif value == "C":

        command = clear
        color = "#e74c3c"



    elif value in ["+","-","*","/"]:

        command = lambda v=value: click(
            " " + v + " "
        )

        color = "#3498db"



    else:

        command = lambda v=value: click(v)

        color = "#34495e"




    button = ctk.CTkButton(

        frame,

        text=text,

        width=70,

        height=50,

        font=(
            "Arial",
            20
        ),

        fg_color=color,

        command=command

    )


    button.grid(

        row=row,

        column=col,

        padx=8,

        pady=8

    )


    col += 1


    if col == 4:

        col = 0

        row += 1




# ==============================
# CLEAR HISTORY BUTTON
# ==============================


clear_history_btn = ctk.CTkButton(

    app,

    text="Clear History",

    width=180,

    height=40,

    fg_color="#9b59b6",

    command=clear_history

)


clear_history_btn.pack(
    pady=15
)



# Load old calculations
load_history()



# ==============================
# START APP
# ==============================

app.mainloop()