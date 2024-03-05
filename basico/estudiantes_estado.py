import modulos.calculo_imc as ci

estadoEstudiantes= {
    'bajoPeso': [],
    'pesoIdeal': [],
    'tipoI': [],
    'tipoII': [],
    'tipoIII': [],
    'sobrepeso': []
}

for i in range (0, 3):
    ci.PesoImc(estadoEstudiantes)
    ci.os.system('cls')
    if estadoEstudiantes['bajoPeso']:
        print('estudiantes con bajo peso:')
        for idx, item in enumerate(estadoEstudiantes['bajoPeso']):
            print(f'{idx+1}. {item}')
    if estadoEstudiantes['pesoIdeal']:
        print('estudiantes con peso ideal:')
        for idx, item in enumerate(estadoEstudiantes['pesoIdeal']):
            print(f'{idx+1}. {item}')
    if estadoEstudiantes['tipoI']:
        print('estudiantes con obesidad tipo I:')
        for idx, item in enumerate(estadoEstudiantes['tipoI']):
            print(f'{idx+1}. {item}')
    if estadoEstudiantes['tipoII']:
        print('estudiantes con obesidad tipo II:')
        for idx, item in enumerate(estadoEstudiantes['tipoII']):
            print(f'{idx+1}. {item}')
    if estadoEstudiantes['tipoIII']:
        print('estudiantes con obesidad tipo III:')
        for idx, item in enumerate(estadoEstudiantes['tipoIII']):
            print(f'{idx+1}. {item}')
    if estadoEstudiantes['sobrepeso']:
        print('estudiantes con sobrepeso:')
        for idx, item in enumerate(estadoEstudiantes['sobrepeso']):
            print(f'{idx+1}. {item}')