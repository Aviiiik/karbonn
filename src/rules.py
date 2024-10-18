import datetime

class FLAGS:
    GREEN = 1
    AMBER = 2
    RED = 0
    MEDIUM_RISK = 3  # display purpose only
    WHITE = 4  # data is missing for this field

# This is already written for your reference
def latest_financial_index(data: dict):
    """
    Determine the index of the latest standalone financial entry in the data.

    Parameters:
    - data (dict): A dictionary containing a list of financial entries under the "financials" key.

    Returns:
    - int: The index of the latest standalone financial entry or 0 if not found.
    """
    for index, financial in enumerate(data.get("financials")):
        if financial.get("nature") == "STANDALONE":
            return index
    return 0

def total_revenue(data: dict, financial_index: int):
    """
    Calculate the total revenue from the financial data at the given index.

    Parameters:
    - data (dict): A dictionary containing financial data.
    - financial_index (int): The index of the financial entry to be used for calculation.

    Returns:
    - float: The net revenue value from the financial data.
    """
    try:
        return data['financials'][financial_index]['pnl']['lineItems']['netRevenue']
    except (KeyError, IndexError):
        return 0.0

def total_borrowing(data: dict, financial_index: int):
    """
    Calculate the ratio of total borrowings to total revenue for the financial data at the given index.

    Parameters:
    - data (dict): A dictionary containing financial data.
    - financial_index (int): The index of the financial entry to be used for the ratio calculation.

    Returns:
    - float: The ratio of total borrowings to total revenue.
    """
    try:
        total_revenue_value = total_revenue(data, financial_index)
        total_borrowings = (
            data['financials'][financial_index]['bs']['lineItems']['longTermBorrowings'] +
            data['financials'][financial_index]['bs']['lineItems']['shortTermBorrowings']
        )
        return total_borrowings / total_revenue_value if total_revenue_value else 0
    except (KeyError, IndexError):
        return 0.0

def iscr(data: dict, financial_index: int):
    """
    Calculate the ISCR (Interest Service Coverage Ratio) value.

    Parameters:
    - data (dict): A dictionary containing financial data.
    - financial_index (int): The index of the financial entry to be used for the ratio calculation.

    Returns:
    - float: The ISCR value.
    """
    try:
        ebit = data['financials'][financial_index]['pnl']['lineItems']['ebit']
        finance_costs = data['financials'][financial_index]['pnl']['lineItems']['financeCosts']
        return ebit / finance_costs if finance_costs else 0.0
    except (KeyError, IndexError):
        return 0.0

def total_revenue_5cr_flag(data: dict, financial_index: int):
    """
    Determine the flag color based on the total revenue.

    If the total revenue is greater than or equal to 5 crore, assign a GREEN flag. Otherwise, assign a RED flag.

    Parameters:
    - data (dict): A dictionary containing financial data.
    - financial_index (int): The index of the financial entry to be used for the revenue calculation.

    Returns:
    - FLAGS.GREEN or FLAGS.RED: The flag color based on the revenue.
    """
    return FLAGS.GREEN if total_revenue(data, financial_index) >= 50000000 else FLAGS.RED

def iscr_flag(data: dict, financial_index: int):
    """
    Determine the flag color based on the ISCR value.

    If ISCR is greater than or equal to 1.5, assign a GREEN flag. Otherwise, assign a RED flag.

    Parameters:
    - data (dict): A dictionary containing financial data.
    - financial_index (int): The index of the financial entry to be used for the ISCR calculation.

    Returns:
    - FLAGS.GREEN or FLAGS.RED: The flag color based on the ISCR value.
    """
    return FLAGS.GREEN if iscr(data, financial_index) >= 1.5 else FLAGS.RED

def borrowing_to_revenue_flag(data: dict, financial_index: int):
    """
    Determine the flag color based on the ratio of total borrowings to total revenue.

    If the ratio is less than or equal to 0.25, assign a GREEN flag, otherwise, assign an AMBER flag.

    Parameters:
    - data (dict): A dictionary containing financial data.
    - financial_index (int): The index of the financial entry to be used for the ratio calculation.

    Returns:
    - FLAGS.GREEN or FLAGS.AMBER: The flag color based on the borrowing to revenue ratio.
    """
    return FLAGS.GREEN if total_borrowing(data, financial_index) <= 0.25 else FLAGS.AMBER
