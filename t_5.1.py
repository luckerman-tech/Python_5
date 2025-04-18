import random as rand
from pathlib import Path

names = [''.join(rand.choices('abcdefghijklmnopqrstuvwxyz0123456789', k = 8)) for name in range(10)]

while True:
    directory = input("Введите имя директории, в которой будут сохранены файлы (для указания текущей директории просто нажмите Enter): ")
    if Path(directory).exists():
        break
    else:
        print("Несуществующая директория!")

for name in names:
    path = Path(f"{directory}\\{name}.txt") if directory else Path(f"{name}.txt")
    try:
        path.touch()
        print(path.absolute())
    except:
        print("Произошла ошибка при попытке создания файлов!")
        break