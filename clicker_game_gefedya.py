from tkinter import *
import sys

Window = Tk()

Window.title("Clicker by @gefedya  v0.0.1 beta")
Window.geometry("{}x{}".format(640, 480))

total_clicks = 0  # Total number of clicks on the counter (your score)
real_button_clicks = 0  # Number of times you've tapped on your display
# (JFY) - coming with statistics menu in later updates
multiple = 1  # Can be bought for 50, 100, 500, 1000 etc. clicks
multiple_price = 50  # Starting price for multiplier
auto_clickers_counter = 0  # + one click every 1sec
auto_clickers_price = 100  # *=4 every purchase


# 1. Status window
statusEntry = Entry(background="#3BB9FF", width=100, justify='center')
statusEntry.insert(END, "Click on the main the button to start!")
statusEntry.pack(side=TOP)


# A pretty function to refresh the window:
def refresh(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        if real_button_clicks > 0 and real_button_clicks % 50 == 0:
            statusEntry.delete(0, END)
            statusEntry.insert(0, f"You have clicked "
                                  f"{total_clicks} times!!")
        else:
            statusEntry.delete(0, END)
    return wrapper


# 2. A label + entry showing number of clicks
Label(text="Your total number of clicks:", background="#FF7F3B").pack()

numberOfClicksEntry = Entry(background="green", width=10,
                            justify='center')
numberOfClicksEntry.pack()


def on_click():
    global total_clicks
    global real_button_clicks
    global multiple
    real_button_clicks += 1
    total_clicks += multiple
    numberOfClicksEntry.delete(0, END)
    numberOfClicksEntry.insert(0, total_clicks)


def auto_click():
    global total_clicks
    global auto_clickers_counter
    total_clicks += auto_clickers_counter
    Window.after(1000, auto_click)  # 1 second


auto_click()


def show_clicks():
    global total_clicks
    numberOfClicksEntry.delete(0, END)
    numberOfClicksEntry.insert(0, total_clicks)


Window.after(10, show_clicks())


def purchase_multiple():
    global total_clicks
    global multiple
    global multiple_price

    if total_clicks < multiple_price:
        statusEntry.delete(0, END)
        statusEntry.insert(0, f"{multiple_price} clicks needed "
                              f"for purchase :(")
    else:
        total_clicks -= multiple_price
        multiple += 1
        statusEntry.delete(0, END)
        statusEntry.insert(0, f"Purchase successful! Your multiplier is "
                              f"x{multiple}")
        if str(multiple_price)[0] == '5':
            multiple_price *= 2
        else:
            multiple_price *= 5


# 3. Button for purchasing multiplier
purchaseMultipleButton = Button(Window, background="#CCFB5D",
                                text=f"Purchase x{multiple + 1} multiplier",
                                command=purchase_multiple)
purchaseMultipleButton.pack()


def purchase_auto_clicker():
    global total_clicks
    global auto_clickers_counter
    global auto_clickers_price
    if total_clicks < auto_clickers_price:
        statusEntry.delete(0, END)
        statusEntry.insert(0, f"{auto_clickers_price} clicks needed "
                              f"for purchase :(")
    else:
        statusEntry.delete(0, END)
        total_clicks -= auto_clickers_price
        auto_clickers_counter += 1
        statusEntry.insert(0, f"Purchase successful! You now get "
                              f"{auto_clickers_counter} clicks "
                              f"every second :)")

        auto_clickers_price *= 4


# Button for purchasing auto clicker
purchaseAutoClickerButton = Button(Window, background="#8C5CFA",
                                   text="Tap to buy increment Auto clicker",
                                   command=purchase_auto_clicker)
purchaseAutoClickerButton.pack()

# 4. Main button for clicking
mainClickButton = Button(Window, text="Click!", width=30,
                         height=10, padx=320, pady=50,
                         command=refresh(on_click))
mainClickButton.pack()

# 5. Quit button
quitButton = Button(Window, text="Quit", command=sys.exit)
quitButton.pack()

mainloop()
