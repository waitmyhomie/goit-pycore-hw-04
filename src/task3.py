#START WITH python ./src/task3.py ../goit-pycore-hw-04/src/  
import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

def print_directory_structure(directory, indent=""):
    try:
        path = Path(directory)
        if not path.is_dir():
            print(f"{Fore.RED}Ошибка: Указанный путь не ведет к директории.")
            return

        for item in sorted(path.iterdir()):
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}{item.name}/")
                print_directory_structure(item, indent + "    ")
            else:
                # Отображаем файлы с зеленым цветом
                print(f"{indent}{Fore.GREEN}{item.name}")

    except Exception as e:
        print(f"{Fore.RED}Произошла ошибка: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Ошибка: Пожалуйста, укажите путь до директории.")
    else:
        directory_path = sys.argv[1]
        print_directory_structure(directory_path)
