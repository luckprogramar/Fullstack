class libreria:
    libros=[]

    def agregar_libro(self, isbn, titulo, paginas, precio, imagen):
        if self.consultar_libro(isbn):
            return False
        nuevo_libro={
            "isbn":isbn,
            "titulo":titulo,
            "paginas":paginas,
            "precio":precio,
            "imagen":imagen,
        }
        self.libros.append(nuevo_libro)
        return True
    def consultar_libro(self, isbn):
        for libro in self.libros:
            if libro["isbn"]==isbn:
                return libro
        return False
    def cambiar_libro(self, isbn, ntitulo, npaginas, nprecio, nimagen):
        for libro in self.libros:
            if libro["isbn"] == isbn:
                libro["titulo"]=ntitulo
                libro["paginas"]=npaginas
                libro["precio"]=nprecio
                libro["imagen"]=nimagen
            return True
        return False    
    def eliminar_libro(self, isbn):
        for libro in self.libros:
            if libro["isbn"]==isbn:
                self.libros.remove(libro)
            return True
        return False
    def lista_delibros(self, isbn):
         print("2")


