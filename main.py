from Usuario import Usuario 
from Post import Post 
from Comentario import Comentario

# a. Juan Pérez ingresa un post el 25 de agosto de 2021, con el título Article y el contenido “Lorem ipsum dolor …”

print("\n --- a. Juan Pérez ingresa un post el 25 de agosto de 2021, con el título Article y el contenido Lorem ipsum dolor ---\n") 

juanPerez = Usuario("Juan Perez", "juan@perez.com","jp")

nombreUsuario1 = juanPerez.getNombreUsuario()

post1 = Post("Article", "Lorem impusm dolor...",nombreUsuario1, "25/08/2021")

post1.imprimirPost(post1)


# b. Michael comenta el post de Juan Pérez  el 25 de agosto con el mensaje “I appreciate the time …”

print("\n --- b. Michael comenta el post de Juan Pérez  el 25 de agosto con el mensaje I appreciate the time … ---\n") 

michael = Usuario("Michael", "michael@apellido.com","123")

nombreUsuario2 = michael.getNombreUsuario()

idPost1 = post1.getIdPost()

nombreUsuario = juanPerez.getNombreUsuario()

comentario1Post1 = Comentario(idPost1, "I appreciate the time …", nombreUsuario2, "25/08/2021")

post1.agregarComentarioAPost(idPost1,comentario1Post1)

post1.imprimirPost(post1)


#c. Marcela Grajales agrega un voto al post de Juan Pérez.

print("\n--- c. Marcela Grajales agrega un voto al post de Juan Pérez ---\n") 

marcela = Usuario("Marcela Grajales", "marcela@grajales.com","mg")

post1.agregarVoto()

post1.imprimirPost(post1)


#d. Marcela Grajales marca el comentario de Michael como spam.

print("\n--- d. Marcela Grajales marca el comentario de Michael como spam ---\n")

comentario1Post1.marcarSpam()

post1.imprimirPost(post1)


#e. Juan Pérez elimina el comentario de Michael. 

print("\n--- e. Juan Pérez elimina el comentario de Michael ---\n") 

post1.eliminarComentarioDePost(idPost1,comentario1Post1)

post1.imprimirPost(post1) 