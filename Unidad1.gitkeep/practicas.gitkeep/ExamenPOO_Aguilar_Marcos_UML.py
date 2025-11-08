class libro:
    def __init__(self, titulo, autor, año, codigo, disponible):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.codigo = codigo
        self.disponible = True

    def mostrar_info(self):
        estado = "disponible" if self.disponible else "prestado"
        print(f"\n info libro")
        print(f"titulo: {self.titulo} (codigo: {self.codigo})")
        print(f"autor: {self.autor}, anio: {self.año}")
        print(f"estado: {estado}")
        return self.disponible

    def prestamo(self):
        if self.disponible:
            self.disponible = False
            print(f" libro {self.titulo} marcado como prestado.")
            return True
        else:
            print(f" error: el libro {self.titulo} ya esta prestado.")
            return False

    def disponible(self):
        self.disponible = True
        print(f"libro {self.titulo} devuelto.")

class usuario:
    def __init__(self, nombre, id_usuario, correo):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.correo = correo
        self.prestamos_activos = []

    def mostrar_info(self):
        print(f"\n info usuario")
        print(f"nombre: {self.nombre} (id: {self.id_usuario})")
        print(f"correo: {self.correo}")
        print(f"tipo: general")

    def solicitar_prestamo(self, libro, fecha_prestamo_str):
        print(f"\n usuario {self.nombre} intenta solicitar: '{libro.titulo}'")
        if libro.disponible:
            prestamo_obj = prestamo(libro, self, fecha_prestamo_str)
            prestamo_obj.registrar_prestamo()
            self.prestamos_activos.append(prestamo_obj)
            return prestamo_obj
        else:
            print(f" error: el libro {libro.titulo} no esta disponible para su prestamo.")
            return None

class estudiante(usuario):
    def __init__(self, nombre, id_usuario, correo, carrera, semestre):
        super().__init__(nombre, id_usuario, correo)
        self.carrera = carrera
        self.semestre = semestre

    def mostrar_info(self):
        print(f"\n info. usuario (estudiante)")
        print(f"nombre: {self.nombre} (id: {self.id_usuario})")
        print(f"correo: {self.correo}")
        print(f"carrera: {self.carrera}, semestre: {self.semestre}")

class profesor(usuario):
    def __init__(self, nombre, id_usuario, correo, departamento, tipo_contrato):
        super().__init__(nombre, id_usuario, correo)
        self.departamento = departamento
        self.tipo_contrato = tipo_contrato

    def mostrar_info(self):
        print(f"\n info. usuario (profesor)")
        print(f"nombre: {self.nombre} (id: {self.id_usuario})")
        print(f"correo: {self.correo}")
        print(f"departamento: {self.departamento}, contrato: {self.tipo_contrato}")

class prestamo:
    def __init__(self, libro, usuario, fecha_prestamo_str):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo_str
        self.fecha_devolucion = None

    def registrar_prestamo(self):
        if self.libro.prestamo():  # Corrected from marcar_como_prestado
            print(f"prestamo exitoso: {self.libro.titulo} a {self.usuario.nombre}.")
        else:
            print(f" advertencia: el libro ya esta prestado, no se puede registrar.")

    def devolver_libro(self, fecha_devolucion_str):
        if not self.fecha_devolucion:
            self.fecha_devolucion = fecha_devolucion_str
            self.libro.disponible()  # Corrected from marcar_como_disponible
            if self in self.usuario.prestamos_activos:
                self.usuario.prestamos_activos.remove(self)
            print(f"devolucion de {self.libro.titulo} registrada el {self.fecha_devolucion}")
        else:
            print(f" error: este prestamo ya fue devuelto.")

    def mostrar_info(self):
        estado = "activo" if not self.fecha_devolucion else "finalizado"
        dev_info = f"devolucion: {self.fecha_devolucion}" if self.fecha_devolucion else "pendiente"
        print(f"\n info. prestamo ({estado})")
        print(f"libro: {self.libro.titulo} | usuario: {self.usuario.nombre}")
        print(f"fecha prestamo: {self.fecha_prestamo} | {dev_info}")

if __name__ == "__main__":
    libro1 = libro("Cien Años de Soledad", "Gabriel Garcia Marquez", 1967, "LIB001", True)
    libro1.mostrar_info()

    estudiante1 = estudiante("Ana Lopez", "EST001", "ana@correo.com", "Ingenieria", 5)
    estudiante1.mostrar_info()

    prestamo1 = estudiante1.solicitar_prestamo(libro1, "2025-10-07")
    prestamo1.mostrar_info()

    libro1.mostrar_info()

    prestamo1.devolver_libro
    prestamo1.mostrar_info()

    libro1.mostrar_info()
