from models import Empleado

def setup_tables(session):
    # Esto es para cumplir con un mínimo de usuarios al iniciar en caso no haya usuarios
    # Crear e insertar registros
    data_empleados = [
        Empleado(nombre='Juan Perez', edad=30, ciudad='Arequipa', salario=3000.00),
        Empleado(nombre='Maria Gomez', edad=25, ciudad='Lima', salario=3500.00),
        Empleado(nombre='Carlos Sanchez', edad=40, ciudad='Cusco', salario=4000.00),
        Empleado(nombre='Ana Torres', edad=35, ciudad='Arequipa', salario=4500.00),
        Empleado(nombre='Luis Rojas', edad=28, ciudad='Lima', salario=3200.00)
    ]

    # Buscamos si ya existen los registros en la tabla empleados
    empleados = session.query(Empleado).all()
    if len(empleados) == 0:
        session.add_all(data_empleados)
        session.commit()
        print('Registros insertados correctamente')
        for emp in data_empleados:
            print(f'Empleado: {emp.nombre} - Edad: {emp.edad} - Ciudad: {emp.ciudad} - Salario: {emp.salario}')
    else:
        print('Ya existen registros en la tabla empleados')
        for emp in empleados:
            print(f'Empleado: {emp.nombre} - Edad: {emp.edad} - Ciudad: {emp.ciudad} - Salario: {emp.salario}')
    
