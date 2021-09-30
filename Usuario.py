class Usuario:

  def __init__(self, nombre, correo, contrasena):
    self.nombre = nombre
    self.correo = correo
    self.contrasena = contrasena

  def getNombreUsuario(self):
    return self.nombre