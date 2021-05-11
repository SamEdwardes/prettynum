def comma(number: float, digits: int=None):
    if digits is not None:
        number = round(float(number), digits)
    number_str = f"{number:,}"
    if digits is not None:
        whole, decimal = number_str.split(".")
        decimal = decimal.ljust(digits, "0")
        number_str = whole + "." + decimal
    return number_str


def dollar(number: float, digits: int=None, symbol: str="$"):
    number_str = comma(number, digits)
    number_str = symbol + number_str
    return number_str