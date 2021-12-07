import pickle


def store(data, filename):
    pickle.dump(data, open(filename, 'wb')) #wb es para escribir en modo binario

def retrieve(filename):
    try:
        f_0 = open(filename, 'rb') #rb es para leer en modo binario
    except:
        print('Error al abrir el archivo', filename)
        return None #si devuelve esto es porque ha habido un error al abrir el archivo
    content = pickle.load(f_0)
    f_0.close()
    return content
