import random

class Comentario:

  def __init__(self, idPost, contenido, nombreUsuario, fecha):
    self.id = str(random.randint(0,9))
    self.idPost = idPost
    self.contenido = contenido
    self.nombreUsuario = nombreUsuario
    self.fecha = fecha
    self.esSpam = False

  def marcarSpam(self): 
    self.esSpam = True

  def imprimirComentario(self):
    print("id:",self.id, "idPost:",self.idPost, "contenido:", self.contenido, "usuario:", self.nombreUsuario, "fecha:", self.fecha, "spam:", self.esSpam)