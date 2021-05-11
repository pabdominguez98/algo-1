import doctest

def es_binario(cadena):
    """
      >>> es_binario('1011011010110')
      True
      >>> es_binario('1213432243')
      False
      >>> es_binario('321321231')
      False
      >>> es_binario('0001011101011101011101')
      True
    """
    for i in range (len(cadena)):
        if cadena[i] != '1' and cadena[i] != '0':
            return False
    return True


print (doctest.testmod())





