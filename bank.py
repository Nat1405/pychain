#!/usr/bin/env python

# Basic implementation of a banking application in Python
# Copyright Nat Comeau 2017

# STDLIB

# LOCAL


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
    accounts : iterable
        list of account objects with balances
    """
    def __init__(self, name):
        self.name = name
        self.accounts = []


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
