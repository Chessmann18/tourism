import tkinter as tk

# Функция для отправки запроса на бронирование
def book_tour():
    destination = destination_entry.get()
    num_travelers = travelers_entry.get()
    date = date_entry.get()
    
    # Здесь может быть логика для бронирования тура
    
    # Выводим сообщение об успешном бронировании
    result_label.config(text="Бронирование на {} для {} человек на {}".format(destination, num_travelers, date))

# Функция для проверки авторизации пользователя
def login_user():
    username = username_entry.get()
    password = password_entry.get()
    
    # Проверяем логин и пароль
    if username == "user" and password == "password":
        login_window.destroy()
        main_window.deiconify()
    else:
        error_label.config(text="Неверный логин или пароль")  

# Создаем окно для входа
login_window = tk.Toplevel()
login_window.title("Вход")

username_label = tk.Label(login_window, text="Логин:")
username_label.pack()
username_entry = tk.Entry(login_window)
username_entry.pack()

password_label = tk.Label(login_window, text="Пароль:")
password_label.pack()
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

login_button = tk.Button(login_window, text="Войти", command=login_user)
login_button.pack()

error_label = tk.Label(login_window, text="")
error_label.pack()

# Создаем главное окно приложения
main_window = tk.Tk()
main_window.title("Турагентство")
main_window.geometry("400x400")
main_window.protocol("WM_DELETE_WINDOW", lambda: main_window.destroy)  # Закрывать только главное окно

# Создаем и размещаем виджеты на главном окне
destination_label = tk.Label(main_window, text="Место назначения:")
destination_label.pack()
destination_entry = tk.Entry(main_window)
destination_entry.pack()

travelers_label = tk.Label(main_window, text="Количество путешественников:")
travelers_label.pack()
travelers_entry = tk.Entry(main_window)
travelers_entry.pack()

date_label = tk.Label(main_window, text="Дата поездки:")
date_label.pack()
date_entry = tk.Entry(main_window)
date_entry.pack()

# Создаем случайный список туров
tours = ["Париж", "Рим", "Лондон", "Барселона", "Токио"]

# Функция для бронирования выбранного тура
def select_tour(tour_name):
    destination_entry.insert(0, tour_name)

# Создаем и размещаем кнопки для туров
tours_frame = tk.Frame(main_window)
tours_frame.pack()

for tour_name in tours:
    tour_button = tk.Button(tours_frame, text=tour_name, command=lambda name=tour_name: select_tour(name))
    tour_button.pack(side=tk.LEFT)

book_button = tk.Button(main_window, text="Забронировать", command=book_tour)
book_button.pack()

result_label = tk.Label(main_window, text="")
result_label.pack()

# Запускаем цикл обработки событий
main_window.withdraw()  # Скрываем главное окно до авторизации
login_window.mainloop()
