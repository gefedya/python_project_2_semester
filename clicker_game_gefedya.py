import tkinter as tk
import sys

Window = tk.Tk()

Window.title("Clicker by @gefedya  v0.0.1 beta")
Window.geometry("{}x{}".format(640, 480))

total_clicks = 0  # Total number of clicks on the counter (your score)
real_button_clicks = 0  # Number of times you've tapped on your display
multiple = 1  # Can be bought for 50, 100, 500, 1000 etc. clicks
multiple_price = 50  # Starting price for multiplier
auto_clickers_counter = 0  # + one click every 1sec
auto_clickers_price = 100  # *=2 every purchase

# Just a label at the top
tk.Label(text="YOUR STATUS", width=16,
         background="#0089fb").pack()


# 1. Status window
statusEntry = tk.Entry(background="#0089fb", width=77, justify='center')
statusEntry.insert(tk.END, "Click on the main the button to start!")
statusEntry.pack(side=tk.TOP)


# A pretty function to refresh the window:
def refresh(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        if real_button_clicks > 0 and real_button_clicks % 50 == 0:
            statusEntry.delete(0, tk.END)
            statusEntry.insert(0, f"Congrats! You have clicked "
                                  f"{total_clicks} times!!")
        else:
            statusEntry.delete(0, tk.END)

    return wrapper


# 2. A label + entry showing number of clicks
tk.Label(text="Your total number of clicks:", background="#FF7F3B").pack()

numberOfClicksEntry = tk.Entry(background="green", width=10,
                               justify='center')
numberOfClicksEntry.pack()


def auto_click():
    global total_clicks
    global auto_clickers_counter
    total_clicks += auto_clickers_counter
    numberOfClicksEntry.delete(0, tk.END)
    numberOfClicksEntry.insert(0, total_clicks)
    Window.after(1000, auto_click)  # 1 second


auto_click()


def on_click():
    global total_clicks
    global real_button_clicks
    global multiple
    real_button_clicks += 1
    total_clicks += multiple
    numberOfClicksEntry.delete(0, tk.END)
    numberOfClicksEntry.insert(0, total_clicks)


def show_clicks():
    global total_clicks
    numberOfClicksEntry.delete(0, tk.END)
    numberOfClicksEntry.insert(0, total_clicks)


Window.after(10, show_clicks())

Multiple_text = tk.StringVar()


def purchase_multiple():
    global total_clicks
    global multiple
    global multiple_price

    if total_clicks < multiple_price:
        statusEntry.delete(0, tk.END)
        statusEntry.insert(0, f"{multiple_price} clicks needed "
                              f"for purchase :(")
    else:
        total_clicks -= multiple_price
        multiple += 1
        statusEntry.delete(0, tk.END)
        statusEntry.insert(0, f"Purchase successful! Your multiplier is "
                              f"x{multiple}")
        numberOfClicksEntry.delete(0, tk.END)
        numberOfClicksEntry.insert(0, total_clicks)
        global Multiple_text
        Multiple_text.set("Purchase x{} multiplier".format(
            multiple + 1))
        multiple_price *= 2 if str(multiple_price)[0] == '5' else 5


# 3. Button for purchasing multiplier
purchaseMultipleButton = tk.Button(Window, background="#CCFB5D",
                                   textvariable=Multiple_text,
                                   command=purchase_multiple)
Multiple_text.set("Purchase x{} multiplier".format(
    multiple + 1))
purchaseMultipleButton.pack()


def purchase_auto_clicker():
    global total_clicks
    global auto_clickers_counter
    global auto_clickers_price
    if total_clicks < auto_clickers_price:
        statusEntry.delete(0, tk.END)
        statusEntry.insert(0, f"{auto_clickers_price} clicks needed "
                              f"for purchase :(")
    else:
        statusEntry.delete(0, tk.END)
        total_clicks -= auto_clickers_price
        auto_clickers_counter += 1
        numberOfClicksEntry.delete(0, tk.END)
        numberOfClicksEntry.insert(0, total_clicks)
        if auto_clickers_counter == 1:
            statusEntry.insert(0, "Purchase successful! You now get "
                                  "1 click every second :)")
        else:
            statusEntry.insert(0, "Purchase successful! You now get "
                                  "{} clicks every second :)".format(
                                    auto_clickers_counter))
        auto_clickers_price *= 2


# Button for purchasing auto clicker
purchaseAutoClickerButton = tk.Button(Window, background="#8C5CFA",
                                      text="Purchase Autoclicker = {}".format(auto_clickers_counter + 1),
                                      command=purchase_auto_clicker)
purchaseAutoClickerButton.pack()


def show_status():
    statusEntry.delete(0, tk.END)
    statusEntry.insert(0, "Price for Autoclicker: {}, "
                               "Price for Multiplier: {}, "
                               "Total button clicks: {}".format(
                                auto_clickers_price, multiple_price,
                                real_button_clicks))


showStatusButton = tk.Button(Window, background="#8dd4ff",
                                      text="Show status",
                                      command=show_status)
showStatusButton.pack()


# 4. Main button for clicking
mainClickButton = tk.Button(Window, text="Click!", width=30,
                            height=10, padx=320, pady=50,
                            command=refresh(on_click))
mainClickButton.pack()

# 5. Quit button
quitButton = tk.Button(Window, background="#908585", text="Quit",
                       command=sys.exit)
quitButton.pack()

tk.mainloop()
