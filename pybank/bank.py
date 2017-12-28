#!/usr/bin/env python

# Basic implementation of a banking application in Python
# Copyright Nat Comeau 2017

# STDLIB

# LOCAL

class Bank(object):
    """A bank has customers that want to do things with their money

    This is a simple bank that holds people's money and transfers it to each other.

    Parameters
    ----------
    name : str
        name of the bank


    Attributes
    ----------
    name : str
        name of bank
    customers : dict
        dictionary of customer: <customer_object> pairs

    """
    def __init__(self, name):
        self.name = name
        # Create an empty dict to hold


class Customer(object):
    """

    A customer starts with just a name. After, you must add accounts to their
    list of accounts with a starting balance.

    Parameters
    ----------
    name : str
        name of the customer

    Attributes
    ----------
    name : str
        name of the customer
    accounts : dict
        dictionary of account objects with balances

    Examples
    --------

    Create a new Customer

    >>> nat = Customer('Nathaniel C')

    Give them a student banking account and a credit account

    >>> nat.add_account('Student Banking', 10.00)
    >>> nat.add_account('Credit', 50.00)
    >>> print(nat)
    Valued Customer Name: Nathaniel C
    Account name: Student Banking Account balance: 10.0
    Account name: Credit Account balance: 50.0

    >>> nat.deposit('Student Banking', 10.0)
    >>> print(nat)
    Valued Customer Name: Nathaniel C
    Account name: Student Banking Account balance: 20.0
    Account name: Credit Account balance: 50.0

    """
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def add_account(self, name, start=0.00):
        """Add account to a customers portfolio

        Parameters
        ----------
        name : str
            The account name
        start : float, optional
            The starting value of the account
        """
        self.accounts[name] = Account(name, start)

    def withdraw(self, account, amount):
        """Withdraw from an account

        Parameters
        ----------
        account : str
            name of account to withdraw from
        amount : float
            amount of money to withdraw from account

        Returns
        -------
        withdrawn : float
            amount of money withdrawn from account
        """
        # Take the amount of money our of the account
        self.accounts[account].balance -= amount
        # Return the amount of money we withdrew
        return amount

    def deposit(self, account, amount):
        """Deposit some money in an account

        Parameters
        ----------
        account : str
            name of account to deposit in
        amount : float
            amount of money to deposit in account
        """
        self.accounts[account].balance += amount

    def transfer(self, sending, recieving, amount):
        """Transfer money between two accounts

        Parameters
        ----------
        sending : str
        recieving : str
        amount : float

        """
        pass

    def __str__(self):
        """
        """
        rep = "Valued Customer Name: {}\n".format(self.name)
        for i, account in enumerate(self.accounts):
            if i < len(self.accounts) - 1:
                rep += str(self.accounts[account]) + "\n"
            else:
                rep += str(self.accounts[account])
        return rep


class Account(object):
    """
    Parameters
    ----------
    name : str
        account name
    start : float, optional
        starting balance to begin with; default 0.00

    Attributes
    ----------
    name : str
        account name
    balance : float
        account balance


    Examples
    --------
    >>> acc = Account('Student Banking', 100.00)
    >>> print(acc)
    Account name: Student Banking Account balance: 100.0
    """
    def __init__(self, name, start=0.00):
        self.name = name
        self.balance = start

    def deposit(self, amount):
        """Add money to self

        Parameters
        ----------
        amount : float
            amount to deposit; must be positive

        Raises
        ------
        ValueError
            If the amount is not a positive number
        """
        if amount >= 0:
            self.balance += amount
        else:
            raise ValueError

    def withdraw(self, amount):
        """Remove money from self

        Parameters
        ----------
        amount : float
            amount to withdraw; must be positive

        Raises
        ------
        ValueError
            If the amount is not a positive number
        """
        if amount >= 0:
            self.balance -= amount
        else:
            raise ValueError

    def __str__(self):
        """
        """
        return "Account name: {} Account balance: {}".format(self.name, self.balance)



if __name__ == "__main__":
    # Use doctest to test new accounts
    import doctest
    doctest.testmod()
