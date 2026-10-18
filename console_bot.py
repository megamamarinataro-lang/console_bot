import sqlite3
import random  # Используем для генерации случайных для user_id

# 1. Создание базы данных и таблицы
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER,
            name TEXT NOT NULL,
            email TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

# 2. Добавление пользователя
def add_user(telegram_id, name, email):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO users (telegram_id, name, email)
        VALUES (?, ?, ?)
    """, (telegram_id, name, email))
    conn.commit()
    conn.close()
    print("✅ Данные сохранены!")

# 3. Просмотр всех пользователей
def show_all_users():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email, created_at FROM users")
    users = cursor.fetchall()
    conn.close()
    
    if not users:
        print("Нет пользователей.")
        return
    
    print("\n📋 Список пользователей:")
    for user in users:
        print(f"{user[0]}. {user[1]} ({user[2]}) - зарегистрирован {user[3]}")

# === 4. Основная программа ===
def main():
    init_db()
    
    print("Добро пожаловать!")
    
    # задания №3: Добавление в цикле
    while True:
        name = input("\nВведите ваше имя.").strip()
        
        # Условие прерывания бесконечного цикла регистрации
        if name.lower() == "выход":
            print("Регистрация завершена.")
            break
            
        if not name:
            print("Имя не может быть пустым. Попробуйте еще раз.")
            continue

        # задания №2: Цикл валидации Email
        while True:
            email = input("Введите ваш email: ").strip()
            
            # Проверка: если в строке нет символа '@', просим ввести заново
            if "@" in email:
                break  # Почта корректна, выходим из цикла проверки
            else:
                print("❌ Ошибка: Email должен содержать символ '@'. Попробуйте еще раз.")

        # Генерируем случайный шестизначный ID
        telegram_id = random.randint(100000, 999999)
        
        
        add_user(telegram_id, name, email)
        show_all_users()


if __name__ == "__main__":
    main()
