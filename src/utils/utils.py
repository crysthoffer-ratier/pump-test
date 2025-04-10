import datetime

def get_dates() -> datetime:
    """
    Returns the current date and the previous date in YYYY-MM-DD format.

    The function calculates the current date using the current system time and
    computes the previous date by subtracting one day from the current date.
    Both dates are returned as strings formatted as 'YYYY-MM-DD'.

    Returns:
        tuple: A tuple containing two strings:
            - The current date (today's date) in 'YYYY-MM-DD' format.
            - The previous date (yesterday's date) in 'YYYY-MM-DD' format.
    """
    current_date = datetime.now()
    previous_date = current_date - datetime.timedelta(days=1)

    return current_date.strftime("%Y-%m-%d"), previous_date.date().strftime("%Y-%m-%d")

