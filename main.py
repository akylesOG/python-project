def greet(name):
    return f"Привет, {name}! Git and Python in VS code successfully initialized!!!"

if __name__ == "__main__":
    user_name = input("Введите имя: ")
    print(greet(user_name))