def square(number:int) ->int:
    """
    Calcule le carré d'un nombre.

    Parameters
    ----------
    nombres : int
        Nombres à mettre au carré


    Returns
    -------
    int
        Nombres au carré.

    Examples
    --------
    >>> square(2)
    4

    """
    return number**2

def product(a, b):
    return a*b



def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division par 0 interdite !")

    return a/b


if __name__ == '__main__':
    print(__name__)