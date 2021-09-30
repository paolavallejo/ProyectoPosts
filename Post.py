import random
from Comentario import Comentario

listaPosts = []

class Post:

  def __init__(self, titulo, contenido,nombreUsuario, fecha):
    self.id = str(random.randint(0,9))
    self.titulo = titulo
    self.contenido = contenido
    self.nombreUsuario = nombreUsuario
    self.fecha = fecha
    self.votos = 0
    self.comentarios = []
    listaPosts.append(self)
    
  def agregarComentarioAPost(self, idPost, comentario):
    for p in listaPosts:
      if p.getIdPost() == idPost:    
        p.comentarios.append(comentario)

  def eliminarComentarioDePost(self, idPost, comentario):
    for p in listaPosts:
      if p.getIdPost() == idPost:    
        p.comentarios.remove(comentario)

  def agregarVoto(self):
    self.votos = self.votos + 1

  def getIdPost(self):
    return self.id

  def imprimirPost(self, post):
      if post in listaPosts: 
        print("id:", post.id, "título:",post.titulo, "contenido:", post.contenido, "usuario:", post.nombreUsuario, "fecha:", post.fecha, "votos:", self.votos, "comentarios:\n")
        for c in post.comentarios:
          c.imprimirComentario()