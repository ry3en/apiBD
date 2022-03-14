import requests

def show_tasks():
    try:
        response = requests.get(url)
        print(response.status_code)
        return response.json()['tasks']
    except requests.exceptions.HTTPError as err:
        print("Error...")
        raise SystemExit(err)
    except requests.exceptions.ConnectionError as err:
        print(f"----- ERROR : {err}")
    except requests.exceptions.JSONDecodeError as err:
        print(f"----- ERROR JSONDecodeError: {err}")

def create_task(task):
    try:
        response = requests.post(url, json={"name": task})
        print(response.status_code)
        return response.json()['tasks']
    except requests.exceptions.HTTPError as err:
        print("Error...")
        raise SystemExit(err)
    except requests.exceptions.ConnectionError as err:
        print(f"----- ERROR : {err}")
    except requests.exceptions.JSONDecodeError as err:
        print(f"----- ERROR JSONDecodeError: {err}")

url = 'http://127.0.0.1:5000/api/tasks'
p_salir = True


while p_salir:
    print("==== MENU DE MI API ====\n 1. Mostrar tareas\n 2. Crear tarea\n 3. Salir")
    try:
        op = int(input("Ingresa una opción:\n"))
    except ValueError as e:
        op = 0

    if op == 1:
        data = show_tasks()
        for task in data:
            print(task)
    elif op == 2:
        data = create_task(input("Ingresa la tarea:\n"))
        for task in data:
            print(task)
    elif op == 3:
        p_salir = False
        print("Adios =)")
    else:
        print("Esa opción no existe\n")