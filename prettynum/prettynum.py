def comma(number: float, digits: int=None) -> str:
    """Format numbers with a comma.

    Parameters
    ----------
    number : float
        The number to be formatted.
    digits : int, optional
        The number of decimals to use when rounding the number. By default 
        None.

    Returns
    -------
    str
        The number formatted with a comma.
        
    Examples
    --------
    >>> from prettynum import comma
    >>> comma(1000)
    '1,000'
    >>> comma(1000, 3)
    '1,000.000'
    >>> comma(1000.89, 1)
    '1,000.9'
    """
    if digits is not None:
        number = round(float(number), digits)
    number_str = f"{number:,}"
    if digits is not None:
        whole, decimal = number_str.split(".")
        decimal = decimal.ljust(digits, "0")
        number_str = whole + "." + decimal
    return number_str


def dollar(number: float, digits: int=None, symbol: str="$") -> str:
    """Format numbers with a leading "$" and a comma.

    Parameters
    ----------
    number : float
        The number to be formatted.
    digits : int, optional
        The number of decimals to use when rounding the number. By default 
        None.
    symbol : str, optional
        [description], by default "$"

    Returns
    -------
    str
        The number formatted with a "$" and comma.
        
    Examples
    --------
    >>> from prettynum import dollar
    >>> dollar(1000)
    '$1,000'
    >>> dollar(1000, 3)
    '$1,000.000'
    >>> dollar(1000.89, 1)
    '$1,000.9'
    """
    number_str = comma(number, digits)
    number_str = symbol + number_str
    return number_str
