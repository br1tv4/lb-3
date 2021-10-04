
from dataclasses import dataclass

@dataclass
class TypeOfMainAssets:
    code: int
    name: str
    plosha: int
    
@dataclass
class MoveOfMainAssets:
    code: int
    period: str
    obig: float
    vdoxod: float
    vobigu: float
    pributok: float
    inspributok: float
    podatok: float

type_array = [ ]
type_array.append(TypeOfMainAssets(1010, "Універмаг", 1704))
type_array.append(TypeOfMainAssets(1020, "Дружба ЛТД", 972))
type_array.append(TypeOfMainAssets(1030, "Радунь", 500))

move_array = [ ]
move_array.append(MoveOfMainAssets(1010, "базовий", 60284.0, 5365.0, 3115.0, 2250.0, 27.0, 765.0))
move_array.append(MoveOfMainAssets(1010, "базовий", 249097.3, 52086.2, 24685.6, 16041.9, 33.0, 4035.4))
move_array.append(MoveOfMainAssets(1010, "базовий", 30590.9, 4955.9, 3725.0, 403.9, 3.0, 80.7))
move_array.append(MoveOfMainAssets(1010, "попередній", 69930.0, 11389.0, 7029.0, 4360.0, 40.0, 1140.0))
move_array.append(MoveOfMainAssets(1010, "попередній", 264159.5, 55050.8, 19697.8, 23219.6, 475.5, 5653.0))
move_array.append(MoveOfMainAssets(1010, "попередній", 32795.9, 6921.9, 4893.7, 875.6, 13.9, 160.1))
move_array.append(MoveOfMainAssets(1010, "поточний", 43202.0, 6133.0, 2030.8, -1417.0, 16684.0, 918.0))
move_array.append(MoveOfMainAssets(1010, "поточний", 311814.9, 67701.0, 49298.4, 6957.0, 478.0, 5653.0))
move_array.append(MoveOfMainAssets(1010, "поточний", 70770.0, 8099.5, 5736.8, 1012.8, 4.7, 200.0))

def printMoveOfMainAssets(moveOfMainAssets):
    '''printMoveOfMainAssets function prints
    "Рух основних засобів"
    with names and values'''

    print("Код: {code}, Період: {period}, Товарообіг: {obig}, Валовий доход: {vdoxod}, Витрати обігу: {vobigu}, Прибуток від реалізації: {pributok}, Інший прибуток: {inspributok}, Податок: {podatok}"
        .format(code=moveOfMainAssets.code, period=moveOfMainAssets.period, obig=moveOfMainAssets.obig, vdoxod=moveOfMainAssets.vdoxod, vobigu=moveOfMainAssets.vobigu,
            pributok=moveOfMainAssets.pributok, inspributok=moveOfMainAssets.inspributok, podatok=moveOfMainAssets.podatok))

for data in move_array:
    printMoveOfMainAssets(data)

def printTypeOfMainAssets(typeOfMainAssets):
    '''printTypeOfMainAssets function prints
    "Вид основних засобів"
    with names and values'''
    
    print("Код: {code}, Назва: {name}, Площа: {plosha} "
        .format(code=typeOfMainAssets.code, name=typeOfMainAssets.name, plosha=typeOfMainAssets.plosha))

for data in type_array:
    printTypeOfMainAssets(data)




