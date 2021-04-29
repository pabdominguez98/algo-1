def validar_contrasenia(contrasenia):
    if len(contrasenia) > 7 and len(contrasenia) < 15:

        for i in range (len(contrasenia)):
            if contrasenia[i:i+1].isupper():
                for j in range (len(contrasenia)):
                    if contrasenia[j:j+1].isnumeric():
                        for k in range (len(contrasenia)):
                            if (contrasenia[k:k+1].isalpha() == False) and (contrasenia[k:k+1].isnumeric() == False):
                                return True

    else:
        return False
    
    return False

print(validar_contrasenia("Hole22e1"))


