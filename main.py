import tkinter as tk


def calculate_floor_area():
    length = float(length_entry.get())
    width = float(width_entry.get())
    area = length * width
    result_label.config(text="Площа підлоги: {:.2f} кв. м".format(area))


def calculate_wall_area(length, width, height, num_windows, window_width, window_height, num_doors, door_width, door_height, has_cabinets, cabinet_width=0, cabinet_height=0):
    wall1_area = length * height
    wall2_area = width * height
    total_wall_area = 2 * (wall1_area + wall2_area)
    window_area = num_windows * window_width * window_height
    door_area = num_doors * door_width * door_height

    if has_cabinets:
        cabinet_area = cabinet_width * cabinet_height
    else:
        cabinet_area = 0

    area_to_process = total_wall_area - window_area - door_area - cabinet_area
    return area_to_process


def calculate_room_area():
    length = float(length_entry.get())
    width = float(width_entry.get())
    height = float(height_entry.get())

    num_windows = int(num_windows_entry.get())
    window_width = float(window_width_entry.get())
    window_height = float(window_height_entry.get())

    num_doors = int(num_doors_entry.get())
    door_width = float(door_width_entry.get())
    door_height = float(door_height_entry.get())

    has_cabinets = cabinets_var.get()
    if has_cabinets:
        cabinet_width = float(cabinet_width_entry.get())
        cabinet_height = float(cabinet_height_entry.get())
    else:
        cabinet_width = 0
        cabinet_height = 0

    area_to_process = calculate_wall_area(length, width, height, num_windows, window_width, window_height,
                                          num_doors, door_width, door_height, has_cabinets, cabinet_width, cabinet_height)
    result_wall_label.config(
        text="Площа стін, що підлягає обробці: {:.2f} кв. м".format(area_to_process))


# Створення вікна
window = tk.Tk()
window.title("Калькулятор кімнати для ремонту")

# Створення елементів у вікні для підлоги
length_label = tk.Label(window, text="Довжина кімнати (м):")
length_label.grid(row=0, column=0, padx=10, pady=5)
length_entry = tk.Entry(window)
length_entry.grid(row=0, column=1, padx=10, pady=5)
length_entry.insert(0, "3.5")

width_label = tk.Label(window, text="Ширина кімнати (м):")
width_label.grid(row=1, column=0, padx=10, pady=5)
width_entry = tk.Entry(window)
width_entry.grid(row=1, column=1, padx=10, pady=5)
width_entry.insert(0, "4.2")


calculate_floor_button = tk.Button(
    window, text="Обчислити площу підлоги", command=calculate_floor_area)
calculate_floor_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

result_label = tk.Label(window, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Створення елементів у вікні для стін

height_label = tk.Label(window, text="Висота кімнати (м):")
height_label.grid(row=2, column=0, padx=10, pady=5)
height_entry = tk.Entry(window)
height_entry.grid(row=2, column=1, padx=10, pady=5)
height_entry.insert(0, "2.7")

num_windows_label = tk.Label(window, text="Кількість вікон у кімнаті:")
num_windows_label.grid(row=5, column=0, padx=10, pady=5)
num_windows_entry = tk.Entry(window)
num_windows_entry.grid(row=5, column=1, padx=10, pady=5)
num_windows_entry.insert(0, "2")

window_width_label = tk.Label(window, text="Ширина вікна (м):")
window_width_label.grid(row=6, column=0, padx=10, pady=5)
window_width_entry = tk.Entry(window)
window_width_entry.grid(row=6, column=1, padx=10, pady=5)
window_width_entry.insert(0, "1.2")

window_height_label = tk.Label(window, text="Висота вікна (м):")
window_height_label.grid(row=7, column=0, padx=10, pady=5)
window_height_entry = tk.Entry(window)
window_height_entry.grid(row=7, column=1, padx=10, pady=5)
window_height_entry.insert(0, "1.5")

num_doors_label = tk.Label(window, text="Кількість дверей у кімнаті:")
num_doors_label.grid(row=8, column=0, padx=10, pady=5)
num_doors_entry = tk.Entry(window)
num_doors_entry.grid(row=8, column=1, padx=10, pady=5)
num_doors_entry.insert(0, "1")

door_width_label = tk.Label(window, text="Ширина дверей (м):")
door_width_label.grid(row=9, column=0, padx=10, pady=5)
door_width_entry = tk.Entry(window)
door_width_entry.grid(row=9, column=1, padx=10, pady=5)
door_width_entry.insert(0, "0.8")

door_height_label = tk.Label(window, text="Висота дверей (м):")
door_height_label.grid(row=10, column=0, padx=10, pady=5)
door_height_entry = tk.Entry(window)
door_height_entry.grid(row=10, column=1, padx=10, pady=5)
door_height_entry.insert(0, "2")

cabinets_var = tk.BooleanVar()
cabinets_checkbutton = tk.Checkbutton(
    window, text="Шафи в кімнаті", variable=cabinets_var)
cabinets_checkbutton.grid(row=11, column=0, columnspan=2, padx=10, pady=5)

cabinet_width_label = tk.Label(window, text="Ширина шафи (м):")
cabinet_width_label.grid(row=12, column=0, padx=10, pady=5)
cabinet_width_entry = tk.Entry(window)
cabinet_width_entry.grid(row=12, column=1, padx=10, pady=5)

cabinet_height_label = tk.Label(window, text="Висота шафи (м):")
cabinet_height_label.grid(row=13, column=0, padx=10, pady=5)
cabinet_height_entry = tk.Entry(window)
cabinet_height_entry.grid(row=13, column=1, padx=10, pady=5)

calculate_room_button = tk.Button(
    window, text="Обчислити площу стін", command=calculate_room_area)
calculate_room_button.grid(row=14, column=0, columnspan=2, padx=10, pady=5)

result_wall_label = tk.Label(window, text="")
result_wall_label.grid(row=15, column=0, columnspan=2, padx=10, pady=5)

# Запуск циклу обробки подій
window.mainloop()
