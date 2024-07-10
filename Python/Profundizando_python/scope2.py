def funcion_ext():
    local_var_ext = 'Variable Local externa'
    def nested_func():
        local_var_nested = 'Variable local anidada'

        nonlocal local_var_ext
        local_var_ext = 'Nuevo valor variable local externa'

    nested_func()
    print(f'Valor variable local externa: {local_var_ext}')
    # no se puede acceder a una variable más interna -> print(f'Valor variable local anidad: {local_var_nested}')
funcion_ext()