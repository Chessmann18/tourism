

tkinter как tk
tkinter.ttk как ttk

Главное окно приложения
root = tk.Tk()
root.title("Туристическое агентство")

Создание вкладок
tab_control = ttk.Notebook(корневой)

Вкладка "О нас"
about_tab = tk.Frame(tab_control)
tab_control.add(about_tab, text="О нас")

about_text = """
Мы - туристическое агентство, специализирующееся
на продаже туров в разные страны.
У нас можно найти лучшие предложения по доступным ценам.
"""

представление информации на выбранной поездке
def show_trip_info(trip):
trip_info = trip_data[trip]
messagebox.showinfo(trip, f"Описание: {trip_info['Описание']}\nЦена: {trip_info['Цена']}")

about_label = tk.Label(about_tab, text=about_text, pady=10)
about_label.pack()

Вкладка "Тур поездки"
trip_tab = tk.Frame(tab_control)
tab_control.add(trip_tab, text="Тур поездки")

Глобальные переменные для сохранения данных о поездках
trip_data = {
"Норвегия": {"Описание": "Норвегия - великолепная страна с красивой природой.", "Цена": "$1000"},
"Ирландия": {"Описание": "Ирландия - зеленый рай.", " Цена": "800$"},
"Швеция": {"Описание": "Швеция - современная страна со скандинавским колоритом.", "Цена": "1200$"}
}

Функция обработки оформления мероприятия
def book_trip(trip, visit_date, return_date, name):
message = f"Поздравляем, {name}! Вы успешно оформили поездку в {trip}.\n"
f"Данные вылета: {departure_date}\nДата возвращения: {return_date}"
messagebox.showinfo("Поездка оформления", message)

Создание функций для каждой поездки
для поездки в trip_data:
trip_button = tk.Button(trip_tab, text=trip,
команда=lambda t=trip: show_trip_info(t))
trip_button.pack(pady=5)

Оформление поездки
booking_frame = tk.Frame(trip_tab)

доставка_label = tk.Label(booking_frame, text="Данные вылета:")
доставка_label.grid(row=0, columns=0)

отправка_entry = tk.Entry(booking_frame)
отправка_entry.grid(строка=0, столбец=1)

return_label = tk.Label(booking_frame, text="Данные возвращения:")
return_label.grid(row=1, columns=0)

return_entry = tk.Entry(booking_frame)
return_entry.grid(строка=1, столбец=1)

name_label = tk.Label(booking_frame, text="Фамилия и имя:")
name_label.grid(row=2, columns=0)

name_entry = tk.Entry(booking_frame)
name_entry.grid(строка=2, столбец=1)

book_button = tk.Button(booking_frame, text="Оформить внутри",
команда=lambda: book_trip(tab_control.tab(tab_control.select(), "text"),
доставка_entry.get(),
return_entry.get(),
name_entry. get()))
book_button.grid(row=3, columnspan=2, Pady=10)

booking_frame.pack(pady=10)

Вкладка "Отзывы"
review_tab = tk.Frame(tab_control)
tab_control.add(reviews_tab, text="Отзывы")

review_label = tk.Label(reviews_tab, text="Оставьте свой отзыв:")
review_label.pack(pady=10)

review_entry = tk.Entry(reviews_tab)
review_entry.pack(pady=5)

submit_button = tk.Button(reviews_tab, text="Отправить отзыв",
command=lambda: messagebox.showinfo("Отзыв отправлен",
"Спасибо за ваш отзыв!"))
submit_button.pack(pady=5)

Отображение приложения
корень.mainloop()