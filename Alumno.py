class Alumno:
    def __init__(self, nombre= '', nota= 0) -> None:
        self._nombre = nombre
        self._nota = nota
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def nota(self):
        if self._is_approved():
            print(f'Aprobado?: {self._is_approved()}')
            return self._nota
        print(f'Aprobado? {self._is_approved()}')
        return self._nota 

    @nota.setter
    def nota(self, nota):
        self._nota = nota
    
    def _is_approved(self):
        if self._nota > 70:
            return True
        else:
            return False