class Simple_list:

    def __init__(self, elementos):
        self._elementos = list(elementos)

    def add_element(self, elemento):
        self._elementos.append(elemento)

    def __getitem__(self, indice):
        return self._elementos[indice]

    def order(self):
        self._elementos.sort()

    def __len__(self):
        return len(self._elementos)

    def __repr__(self):
        return f'{self.__class__.__name__} ({self._elementos!r})'

class Order_list(Simple_list):
    def __init__(self, elementos=[]):
        super().__init__(elementos)
        self.order()

    def add_element(self, elemento):
        super().add_element(elemento)
        self.order()

class Int_list(Simple_list):
    def __init__(self, elementos=[]):
        for elemento in elementos:
            self._validar(elemento)
            super().__init__(elementos)
    def _validar(self, elemento):
        if not isinstance(elemento, int):
            raise ValueError(f'No es un valor entero: {elemento}')

    def add_element(self, elemento):
        self._validar(elemento)
        super().add_element(elemento)

class IntOrderList(Int_list, Order_list):
    pass


if __name__ == '__main__':
    lista1 = Simple_list([5, 6, 3, 8])
    print(lista1)

    lista_o1 = Order_list([4, 3, 2, 9, 10, 11])
    print(lista_o1)
    lista_o1.add_element(-14)
    print(lista_o1)
    print(f'La lista tiene un largo de {len(lista_o1)} elementos')

    list_i1 = Int_list([12, 2, 5, 7])
    print(list_i1)
    print(lista1)

    lista_o1 = Order_list([4, 3, 2, 9, 10, 11])
    print(lista_o1)
    lista_o1.add_element(-14)
    print(lista_o1)
    print(f'La lista tiene un largo de {len(lista_o1)} elementos')

    list_i1 = Int_list([12, 2, 5, 7])
    print(list_i1)

    List_IO1 = IntOrderList([-3, 12, 1, -6])
    print(List_IO1)
    List_IO1.add_element(-20)
    print(List_IO1)

    print('Est entero?', isinstance(10, int))
    print('Es cadena', isinstance('Hola', str))
    print('Es una lista ent ord?', isinstance(List_IO1, IntOrderList))