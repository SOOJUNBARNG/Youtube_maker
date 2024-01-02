import tkinter as tk
from tkinter import scrolledtext as st

def send_message():
    return "Nyan"

def main():

    user_input = input("You: ")

    def on_send():
        user_input = user_entry.get()
        user_entry.delete(0, tk.END)

        if user_input.lower() == "quit":
            window.destroy()
            return

        conversation.insert(tk.END) 

    response = send_message()

    window = tk.Tk()
    window.title("YRC matching uranai")

    conversation = st.ScrolledText(window, wrap=tk.WORD, width=50, height=20)
    conversation.grid(row=0, column=0, padx=10,pady=10)

    user_entry=tk.Entry(window)
    user_entry.grid(row=1, column=0, padx=10,pady=10)

    send_button = tk.Button(window, text="送信", command=on_send)
    send_button.grid(row=1, column=1, padx=10,pady=10)

    window.bind('<Return>', lambda event: on_send())

    window.mainloop()


if __name__ == "__main__":
    main()