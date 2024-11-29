def get_cats_info(path):
    cats_info = []
    try:
        with open(path, mode='r', encoding='utf-8') as file:
            for line in file:
                line = line.strip() 
                if line:
                    cat_id, name, age = line.split(',')
                    cats_info.append({"id": cat_id, "name": name, "age": age})
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
    except IOError:
        print(f"Помилка під час читання файлу {path}.")
    except Exception as e:
        print(f"Сталася непередбачена помилка: {e}")
    
    return cats_info

# Приклад використання функції
cats_info = get_cats_info("../../cats.txt")
print(cats_info)
