def total_salary(path):
    try:
        with open(path, encoding='utf-8') as file:
            total = 0
            count = 0
            for line in file:
                try:
                    name, salary = line.strip().split(',')
                    total += float(salary)
                    count += 1
                except ValueError:
                    continue
            if count == 0:
                return 0, 0
            average = total / count
            return total, average
    except FileNotFoundError:
        return 0, 0
    except Exception as e:
        return 0, 0

path = "./salaries.txt"
total, average = total_salary(path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
