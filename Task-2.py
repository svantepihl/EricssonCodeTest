from datetime import datetime
from collections import Counter


def calculate_totals(transactions):
    """Returns the sum of all in the transactions given

    Args:
        transactions (list[Transaction]): List of transactions 

    Returns:
        [int]: Total sum of all transactions
    """
    return sum([transaction.amount for transaction in transactions])


def calculate_card_fees(transactions):
    """Calulates the card fees for a year, three or more transaction in a month and a combined values of at least 100, qualifies for a fee free month.

    Args:
        transactions (list[Transaction]): All transactions in a year

    Returns:
        [int]: Amount of card card fees due
    """
    # Get card payments:
    card_transactions = [
        transaction for transaction in transactions if transaction.type == "Card Payment"]

    # Count number of fee free months
    fee_free_months = 0

    # Count transactions per month
    transactions_per_month = Counter(
        [transaction.date.month for transaction in card_transactions])
    for month in transactions_per_month:

        if transactions_per_month[month] >= 3:
            transaction_sum_per_month = sum(
                [transaction.amount for transaction in card_transactions if transaction.date.month == month])

            if abs(transaction_sum_per_month) >= 100:
                fee_free_months += 1

    return (12 - fee_free_months) * 5


class Transaction:
    def __init__(self, amount, date):
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.amount = amount
        self.type = "Card Payment" if amount < 0 else "Incoming Transfer"


def solution(A, D):
    # Create list of transaction objects
    all_transactions = [Transaction(A[i], D[i])
                        for i in range(min(len(A), len(D)))]

    # Calculate totals
    transactions_totals = calculate_totals(all_transactions)

    # Calculate card fees
    card_fees = calculate_card_fees(all_transactions)

    return transactions_totals - card_fees


solution([180, -50, -25, -25], ['2020-01-01',
                                '2020-01-01', '2020-01-01', '2020-01-31'])
