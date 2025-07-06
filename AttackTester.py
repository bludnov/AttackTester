import requests
import random
import string
import time

title = """
░█████╗░████████╗████████╗░█████╗░░█████╗░██╗░░██╗████████╗███████╗░██████╗████████╗███████╗██████╗░
██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔══██╗██║░██╔╝╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗
███████║░░░██║░░░░░░██║░░░███████║██║░░╚═╝█████═╝░░░░██║░░░█████╗░░╚█████╗░░░░██║░░░█████╗░░██████╔╝
██╔══██║░░░██║░░░░░░██║░░░██╔══██║██║░░██╗██╔═██╗░░░░██║░░░██╔══╝░░░╚═══██╗░░░██║░░░██╔══╝░░██╔══██╗
██║░░██║░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚██╗░░░██║░░░███████╗██████╔╝░░░██║░░░███████╗██║░░██║
╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
"""
print(title)
url = input(" attackTester@sterford:~ $ Введите API для регистрации (пример: https://example.ru/api/register/): ").strip()
headers = {"Content-Type": "application/json"}

def randomik(length):
    return ''.join(random.choices(string.digits, k=length))

success_count = 0
max_success = 5

while success_count < max_success:
    username = "attack" + randomik(6)
    password = "attack" + randomik(5)

    data = {
        "login": username,
        "password": password
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=10)
        response.raise_for_status()
        success_count += 1
        print(f" attackTester@sterford:~ $Успешная регистрация! ({success_count}/{max_success})")
        print(f"   [ Юзер: {username} ]")
        print(f"   [ Пароль: {password} ]")
        print("-" * 30)
    except requests.exceptions.RequestException as e:
        print(f" attackTester@sterford:~ Ошибка при регистрации: {e}")
        print("    [Проверьте URL или попробуйте позже]")
        print("-" * 30)
    
    time.sleep(1)

if success_count == max_success:
    print("\n attackTester@sterford:~ $ Ваш сайт провалил тест!")
    print("    [Было успешно зарегистрировано 5 аккаунтов]")
    print("-" * 30)