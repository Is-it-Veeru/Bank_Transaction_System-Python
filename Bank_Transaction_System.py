#Bank Transaction Programme
class Bank():
    def __init__(self):
        # Initialize the account balance to 0
        self.Amount = 0

    # Deposit Section
    def Deposit(self, Amt):
        try:
            # Convert the input to an integer
            Amt = int(Amt)
            if Amt > 0:
                # If the amount is positive, add it to the balance
                self.Amount += Amt
                return "Deposit Successful"
            else:
                # If the amount is not positive, return an error message
                return "Deposit Amount Must be Greater than 0."
        except ValueError:
            # If the input cannot be converted to an integer, return an error message
            return "Enter a Valid Amount"

    # Withdraw Section
    def Withdraw(self, Amt):
        try:
            # Convert the input to an integer
            Amt = int(Amt)
            if Amt > 0 and self.Amount >= Amt:
                # If the amount is positive and there are sufficient funds, withdraw it
                self.Amount -= Amt
                return "Withdraw Successful"
    
            elif Amt <= 0:
                # If the amount is not positive, return an error message
                return "Withdraw Amount Must be Greater than 0."
            else:
                # If there are insufficient funds, return an error message
                return "Insufficient Funds"
        except ValueError:
            # If the input cannot be converted to an integer, return an error message
            return "Enter a Valid Amount"

    # Balance Enquiry Section
    def Balance_Enquiry(self):
        # Return the current account balance
        return self.Amount

# Main program
if __name__ == '__main__':
    A = Bank()
    while True:
        x = input("Please Enter the Required Field, \nDeposit-D \nWithdraw-W \nBalance_Enquiry-B \nExit-E\n")
        if x.upper() == "D":
            Amt = input("\nEnter the Deposit Amount:")
            print(A.Deposit(Amt))

        elif x.upper() == "W":
            Amt = input("\nEnter the Withdraw Amount:")
            print(A.Withdraw(Amt))

        elif x.upper() == "B":
            # Print the current account balance when "B" is selected
            print("Current Balance:", A.Balance_Enquiry())

        elif x.upper() == "E":
            # Exit the program when "E" is selected
            break

        else:
            print("Please Enter a Valid Field")  # Print an error message for invalid input
