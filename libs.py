import datetime as dt


def calculate_current_time_to_date(expiry_date) -> float:
    """
    Returns the current total time remaining until some future datetime. The remaining time is provided in fractions of
    years.

    Example usage:
        import datetime as dt

        expiry_date = dt.datetime(2022, 12, 31, 12, 0, 0)
        tte = calculate_current_time_to_date(expiry_date)

    Arguments:
        expiry_date: A dt.datetime object representing the datetime of expiry.
    """
    now = dt.datetime.now()
    return calculate_time_to_date(expiry_date, now)


def calculate_time_to_date(expiry_date, current_time) -> float:
    """
    Returns the total time remaining until some future datetime. The remaining time is provided in fractions of years.

    Example usage:
        import datetime as dt

        expiry_date = dt.datetime(2022, 12, 31, 12, 0, 0)
        now = dt.datetime.now()
        tte = calculate_time_to_date(expiry_date, now)

    Arguments:
        expiry_date: A dt.datetime object representing the datetime of expiry.
        current_time: A dt.datetime object representing the current datetime to assume.
    """

    return (expiry_date - current_time) / dt.timedelta(days=1) / 365