
file_name = "recipes.txt"

def file_worker(file_name: str):
    with open(file_name, encoding="utf-8") as file:
        for line in file:
            print(line.strip())

result = file_worker(file_name)
