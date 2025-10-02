# Build a calculator app.

# Bonus Challenges (Day 7):

# Build a calculator app.

# Create a random password generator.

# Scrape website titles with requests + BeautifulSoup.

# Create a student management system (OOP + files).
import tkinter as tk

def click(button_text):
    current = entry.get()
    if button_text == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Main window
root = tk.Tk()
root.title("Python Calculator")
root.geometry("320x400")
root.resizable(True, True)

#Entry widget (display)
entry = tk.Entry(root, font=("Arial", 16), borderwidth=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10, ipady=10)

# Buttons layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=("Arial", 16), width=5, height=2,
                       command=lambda t=text: click(t))
    button.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
>>>>>>> f0961ba (Finish mini projects)
