from tkinter import *

class Bank:
    def __init__(self):
        self.Amount = 0
        self.showing_balance = False

    # Deposit Section
    def deposit(self):
        deposit_window = Toplevel(root)
        deposit_window.title("Deposit")
        deposit_window.geometry("300x200")
        deposit_window.resizable(False, False)
        deposit_window.configure(bg="black")

        deposit_label = Label(deposit_window, text="Enter deposit amount:")
        deposit_label.pack()

        self.deposit_entry = Entry(deposit_window)
        self.deposit_entry.pack()

        deposit_button = Button(deposit_window, text="Deposit", command=self.deposit_money)
        deposit_button.pack()

        self.result_label1 = Label(deposit_window, text="", bg="DarkViolet")
        self.result_label1.pack()

    def deposit_money(self):
        try:
            deposit_amount = int(self.deposit_entry.get())
            if deposit_amount > 0:
                self.Amount += deposit_amount
                self.result_label1.config(text="Deposit Successful")
                self.deposit_entry.delete(0, END)  # Clear the input field after deposit
            else:
                self.result_label1.config(text="Deposit Amount Must be Greater than 0.")
        except ValueError:
            self.result_label1.config(text="Enter a Valid Amount")

    # Withdraw section
    def Withdraw(self):
        withdraw_window = Toplevel(root)
        withdraw_window.title("Withdraw")
        withdraw_window.geometry("300x200")
        withdraw_window.resizable(False, False)
        withdraw_window.configure(bg="#DEB887")

        withdraw_label = Label(withdraw_window, text="Enter Withdraw amount:")
        withdraw_label.pack()

        self.withdraw_entry = Entry(withdraw_window)
        self.withdraw_entry.pack()

        withdraw_button = Button(withdraw_window, text="Withdraw", command=self.withdraw_money)
        withdraw_button.pack()

        self.result_label2 = Label(withdraw_window, text="", bg="#DEB887")
        self.result_label2.pack()

    def withdraw_money(self):
        try:
            # Convert the input to an integer
            Amt = int(self.withdraw_entry.get())
            if Amt > 0 and self.Amount >= Amt:
                # If the amount is positive and there are sufficient funds, withdraw it
                self.Amount -= Amt
                self.result_label2.config(text="Withdraw Successful")
                self.withdraw_entry.delete(0, END)
            elif Amt <= 0:
                # If the amount is not positive, return an error message
                self.result_label2.config(text="Withdraw Amount Must be Greater than 0.")
            else:
                # If there are insufficient funds, return an error message
                self.result_label2.config(text="Insufficient Funds")
        except ValueError:
            # If the input cannot be converted to an integer, return an error message
            self.result_label2.config(text="Enter a Valid Amount")

    # Balance Enquiry Section
    def balance_enquiry(self):
        if self.showing_balance:
            self.Show.place_forget()
            self.showing_balance = False
        else:
            self.Show.config(text="Balance: ₹" + str(self.Amount),bg="White")
            self.Show.place(x=620, y=300)
            self.showing_balance = True


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank Transaction")
        self.root.geometry("800x600")
        self.root.configure(bg="#008B8B")
        self.root.iconbitmap("Bank.ico")
        self.root.resizable(False, False)

        Head = Label(self.root, text="Bank Transaction", font=("Arial", 22), bg="Gold")
        Head.place(x=300, y=40)

        self.B = Bank()

        # Deposit
        D = Button(self.root, text="Deposit", font=("Arial", 16), command=self.B.deposit, bg="DarkViolet", fg="white")
        D.place(x=20, y=250)

        # Withdraw
        W = Button(self.root, text="Withdraw", font=("Arial", 16), command=self.B.Withdraw, bg="#DEB887", fg="white")
        W.place(x=320, y=250)

        # Balance
        B_E = Button(self.root, text="Balance Enquiry", font=("Arial", 16), command=self.B.balance_enquiry, bg="#A52A2A", fg="white")
        B_E.place(x=620, y=250)

        # Show label
        self.B.Show = Label(self.root, text="", font=("Arial", 12),bg="#008B8B")
        self.B.Show.place(x=620, y=300)

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
