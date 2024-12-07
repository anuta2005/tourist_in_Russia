import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter.ttk import *
from PIL import Image, ImageTk, ImageDraw
from tkinter import messagebox
from data_base_1 import show_all, delete_city, create_new_note, update_indexes, update_city


checkbox_names, city_names = [], []
combobox, combobox_add, combobox_sort = None, None, None
(city_name_1, date_1, population_1, time_1, region_1, sight_1, max_temp_1, \
 min_temp_1) = None, None, None, None, None, None, None, None
city_name_tf, date_tf, population_tf, time_tf, region_tf, sight_tf, \
    max_temp_tf, min_temp_tf = None, None, None, None, None, None, None, None
(city_name, date, population, time, region, sight, max_temp, min_temp,
 cal_btn, cal_btn_delete, cal_btn_amend) = None, None, None, None, None, None, None, None, None, None, None
number_of_city = 0
sort_values = ['Название города', 'Дата основания', 'Население', 'Часовой пояс',
               'Регион', 'Максимальная температура', 'Минимальная температура']
sort_dict = {'Название города':1, 'Дата основания':2, 'Население':3, 'Часовой пояс':4,
               'Регион':5, 'Максимальная температура':7, 'Минимальная температура':8}

def find_city(event):
    global combobox, checkbox_names
    value = event.widget.get()
    if value == '':
        combobox['values'] = checkbox_names
    else:
        data = []
        for item in checkbox_names:
            if value.lower() in item.lower():
                data.append(item)
        combobox['values'] = data
def show_city(event):
    global checkbox_names, data, combobox
    smth = combobox.get()
    canvas.delete("all")
    city_names = []
    number_of_note = 0
    checkbox_names.clear()
    for i in range(len(data)):
        if smth == data[i][1]:
            number_of_note = i
            break

    for row in data:
        checkbox_names.append(row[1])
        city_names.append([row[0], row[1]])
    create_form(number_of_note)
def sort_of_city(event):
    global checkbox_names, data, combobox_sort
    sort_tag = combobox_sort.get()
    print(sort_tag)
    data = show_all()
    index_of_sort = sort_dict[sort_tag]
    data.sort(key=lambda x:x[index_of_sort])
    checkbox_names.clear()
    for row in data:
        checkbox_names.append(row[1])
        city_names.append([row[0], row[1]])
    canvas.delete("all")
    create_form(0)

def get_combobox_names():
    global checkbox_names, city_names
    data = show_all()
    city_names = []
    checkbox_names.clear()

    for row in data:
        checkbox_names.append(row[1])
        city_names.append([row[0], row[1]])
def show_city_add(event):
    update_form_add(combobox_add.get())
def clear_addition_form():
    global city_name_tf, date_tf, population_tf, time_tf, region_tf, sight_tf, max_temp_tf, min_temp_tf
    city_name_tf.delete(0, last=END)
    date_tf.delete(0, last=END)
    population_tf.delete(0, last=END)
    time_tf.delete(0, last=END)
    region_tf.delete(0, last=END)
    sight_tf.delete(0, last=END)
    max_temp_tf.delete(0, last=END)
    min_temp_tf.delete(0, last=END)
def update_form_add(smth):
    global city_name_tf, date_tf, population_tf, time_tf, region_tf, sight_tf, max_temp_tf, min_temp_tf, number_of_city
    data = show_all()
    city_names = []
    global checkbox_names
    checkbox_names.clear()
    for row in data:
        checkbox_names.append(row[1])
        city_names.append([row[0], row[1]])

    for i in range(len(data)):
        if smth == data[i][1]:
            number_of_city = i
            break

    id, name_n, date_n, population_n, time_n, region_n, sight_n, max_temp_n, min_temp_n = data[number_of_city]

    clear_addition_form()

    city_name_tf.insert(0, name_n)
    date_tf.insert(0, date_n)
    population_tf.insert(0, population_n)
    time_tf.insert(0, time_n)
    region_tf.insert(0, region_n)
    sight_tf.insert(0, sight_n)
    max_temp_tf.insert(0, max_temp_n)
    min_temp_tf.insert(0, min_temp_n)
def addition():
    root = tk.Toplevel(window)
    root.title("Changing form")
    root.geometry("400x500")
    global checkbox_names, city_names, data
    global city_name, date, population, time, region, sight, max_temp, min_temp
    global city_name_tf, date_tf, population_tf, time_tf, region_tf, sight_tf, max_temp_tf, min_temp_tf, cal_btn, \
        cal_btn_delete, cal_btn_amend
    get_combobox_names()
    data = show_all()
    global combobox_add
    city_name = Label(root, text="Выберите город", foreground="#866df7")
    city_name.grid(row=0, column=0)
    combobox_add = ttk.Combobox(root, values=checkbox_names, state="readonly")
    combobox_add.grid(row=0, column=1)
    combobox_add.bind("<<ComboboxSelected>>", show_city_add)

    city_name = Label(root, text="Название города")
    city_name.grid(row=1, column=0)
    city_name_tf = Entry(root)
    city_name_tf.insert(data[0][0], data[0][1])
    city_name_tf.grid(row=1, column=1, pady=10)

    date = Label(root, text="Год основания")
    date.grid(row=2, column=0)
    date_tf = Entry(root)
    date_tf.insert(data[0][0], data[0][2])
    date_tf.grid(row=2, column=1, pady=10)

    population = Label(root, text="Население")
    population.grid(row=3, column=0)
    population_tf = Entry(root)
    population_tf.insert(data[0][0], data[0][3])
    population_tf.grid(row=3, column=1, pady=10)

    time = Label(root, text="Часовой пояс")
    time.grid(row=4, column=0)
    time_tf = Entry(root)
    time_tf.insert(data[0][0], data[0][4])
    time_tf.grid(row=4, column=1, pady=10)

    region = Label(root, text="Регион")
    region.grid(row=5, column=0)
    region_tf = Entry(root)
    region_tf.insert(data[0][0], data[0][5])
    region_tf.grid(row=5, column=1, pady=10)

    sight = Label(root, text="Достопримечательность")
    sight.grid(row=6, column=0)
    sight_tf = Entry(root)
    sight_tf.insert(data[0][0], data[0][6])
    sight_tf.grid(row=6, column=1, pady=10)

    max_temp = Label(root, text="Минимальная температура")
    max_temp.grid(row=7, column=0)
    max_temp_tf = Entry(root)
    max_temp_tf.insert(data[0][0], data[0][7])
    max_temp_tf.grid(row=7, column=1, pady=10)

    min_temp = Label(root, text="Минимальная температура")
    min_temp.grid(row=8, column=0)
    min_temp_tf = Entry(root)
    min_temp_tf.insert(data[0][0], data[0][8])
    min_temp_tf.grid(row=8, column=1, pady=10)

    def new_city():
        new_city_name = city_name_tf.get()
        new_date = date_tf.get()
        new_population = population_tf.get()
        new_time = time_tf.get()
        new_region = region_tf.get()
        new_sight = sight_tf.get()
        new_max_temp = max_temp_tf.get()
        new_min_temp = min_temp_tf.get()
        t = [new_city_name, new_date, new_population, new_time, new_region, new_sight, new_max_temp, new_min_temp]
        if new_city_name in checkbox_names:
            messagebox.showinfo('city-pythonguides', "Такой город уже существует, вы можете изменить его")
        else:
            T = True
            for val in t:
                if val == '':
                    messagebox.showinfo('city-pythonguides', "Заполните все поля")
                    T = False
                    break
            if T:
                create_new_note(new_city_name, new_date, new_population, new_time, new_region, new_sight, new_max_temp, new_min_temp)
                update_indexes()
                get_combobox_names()
                combobox_add["values"] = checkbox_names

    cal_btn_amend = Button(root, text="Изменить данные", command=update_city_func)
    cal_btn_amend.grid(row=9, column=0)

    cal_btn = Button(root, text="Добавить город", command=new_city)
    cal_btn.grid(row=9, column=1)

    cal_btn_delete = Button(root, text="Удалить город", command=delete_city_func)
    cal_btn_delete.grid(row=9, column=2)
    root.mainloop()

def delete_city_func():
    global number_of_city, checkbox_names, combobox_add
    clear_addition_form()
    delete_city(number_of_city + 1)
    get_combobox_names()
    combobox_add["values"] = checkbox_names
    update_indexes()
def update_city_func():
    global checkbox_names, number_of_city
    global city_name_tf, date_tf, population_tf, time_tf, region_tf, sight_tf, max_temp_tf, min_temp_tf
    t = [date_tf.get(), population_tf.get(), time_tf.get(), region_tf.get(), sight_tf.get(), \
                        max_temp_tf.get(), min_temp_tf.get()]
    if city_name_tf.get() in checkbox_names:
        T = True
        for val in t:
            if val == '':
                messagebox.showinfo('city-pythonguides', "Заполните все поля")
                T = False
                break
        if T:
            update_city(date_tf.get(), population_tf.get(), time_tf.get(), region_tf.get(), sight_tf.get(), \
                        max_temp_tf.get(), min_temp_tf.get(), number_of_city+1)
    else:
        messagebox.showinfo('city-pythonguides', "Такого города пока не существует, добавьте его")
def roundPolygon(x, y, sharpness, **kwargs):
    global  canvas
    # The sharpness here is just how close the sub-points
    # are going to be to the vertex. The more the sharpness,
    # the more the sub-points will be closer to the vertex.
    # (This is not normalized)
    if sharpness < 2:
        sharpness = 2

    ratioMultiplier = sharpness - 1
    ratioDividend = sharpness

    # Array to store the points
    points = []

    # Iterate over the x points
    for i in range(len(x)):
        # Set vertex
        points.append(x[i])
        points.append(y[i])

        # If it's not the last point
        if i != (len(x) - 1):
            # Insert submultiples points. The more the sharpness, the more these points will be
            # closer to the vertex.
            points.append((ratioMultiplier*x[i] + x[i + 1])/ratioDividend)
            points.append((ratioMultiplier*y[i] + y[i + 1])/ratioDividend)
            points.append((ratioMultiplier*x[i + 1] + x[i])/ratioDividend)
            points.append((ratioMultiplier*y[i + 1] + y[i])/ratioDividend)
        else:
            # Insert submultiples points.
            points.append((ratioMultiplier*x[i] + x[0])/ratioDividend)
            points.append((ratioMultiplier*y[i] + y[0])/ratioDividend)
            points.append((ratioMultiplier*x[0] + x[i])/ratioDividend)
            points.append((ratioMultiplier*y[0] + y[i])/ratioDividend)
            # Close the polygon
            points.append(x[0])
            points.append(y[0])

    canvas.create_polygon(points, **kwargs, smooth=TRUE)
def create_form(number_of_note):
    global data, checkbox_names, combobox, combobox_sort
    id, name_n, date_n, population_n, time_n, region_n, sight_n, max_temp_n, min_temp_n = data[number_of_note]
    font_of_main = ("Calibri", 11)
    font_of_information = ("Arial", 18, 'bold')
    colour_main = "#d7cffc"
    colour_information ="white"

    canvas.pack(anchor=CENTER, expand=1)
    n_1 = 10
    roundPolygon([-10, 410, 410, -10], [0, 0, 350, 350], 1, outline="white", fill="#866df7")
    canvas.create_text(30, 20+n_1, text=name_n, font=("Roboto", 20), anchor='nw', fill="white")
    canvas.create_text(30, 50+n_1, text=region_n, font=("Arial", 10), anchor='nw', fill="#d7cffc")

    roundPolygon([30, 170, 170, 30], [150, 150, 320, 320], 1, outline="#a496f2", fill="#a496f2")
    roundPolygon([210, 370, 370, 210], [150, 150, 320, 320], 1, outline="#a496f2", fill="#a496f2")


    if len(sight_n) < 20:
        font_size = 18
    else:
        font_size =int(300/len(sight_n)*1.4)
  #  canvas.create_text(40, 80, text="sight", font=font_of_main, anchor='nw', fill=colour_main)
    canvas.create_text(200-(len(str(sight_n))//2*font_size*0.75), 75+20, text=sight_n, font=("Arial", font_size, 'bold'), anchor='nw', fill=colour_information)

    m, n = 70, 80
    # print(70 - (len(str(date_n))//2)*10)
    canvas.create_text(100-(len(str(date_n))//2*13), 90+m, text=date_n, font=font_of_information, anchor='nw', fill=colour_information)
    canvas.create_text(100-(len("foundation date")//2*7.5), 112+m, text="foundation date", font=font_of_main, anchor='nw', fill=colour_main)
    # print(70 - (len(str(population_n)) // 2))
    canvas.create_text(100-(len(str(population_n))//2*13), 140+m, text=population_n, font=font_of_information, anchor='nw', fill=colour_information)
    canvas.create_text(100-(len("population")//2*7.5), 162+m, text="population", font=font_of_main, anchor='nw', fill=colour_main)
    # print(70 - (len(str(time_n)) // 2) * 11)
    canvas.create_text(100-(len(str(time_n))//2*13), 190+m, text=time_n, font=font_of_information, anchor='nw', fill=colour_information)
    canvas.create_text(100-(len(str("time zone"))//2*7.5), 212+m, text="time zone", font=font_of_main, anchor='nw', fill=colour_main)



    canvas.create_text(315, 98+n, text=max_temp_n, font=("Arial", 14, 'bold'), anchor='nw', fill=colour_information)


    canvas.create_oval(270, 100 + n, 270, 212 + n, width=15, outline="white")
    canvas.create_line(271, 110 + n, 310, 110 + n, fill="white", width=2)

    canvas.create_line(271, 120 + n, 285, 120 + n, fill="white", width=2)
    canvas.create_line(271, 130 + n, 285, 130 + n, fill="white", width=2)

    canvas.create_line(271, 140 + n, 290, 140 + n, fill="white", width=2)

    canvas.create_line(271, 150 + n, 285, 150 + n, fill="white", width=2)
    canvas.create_line(271, 160 + n, 285, 160 + n, fill="white", width=2)

    canvas.create_line(271, 170 + n, 290, 170 + n, fill="white", width=2)

    canvas.create_line(271, 180 + n, 285, 180 + n, fill="white", width=2)
    canvas.create_line(271, 190 + n, 285, 190 + n, fill="white", width=2)

    canvas.create_line(271, 200 + n, 310, 200 + n, fill="white", width=2)

    canvas.create_text(315, 188 + n, text=min_temp_n, font=("Arial", 14, 'bold'), anchor='nw', fill=colour_information)


    canvas.create_text(21, 355, text="city:", font=("Arial", 10, 'bold'), anchor='nw', fill="#866df7")
    combobox = ttk.Combobox(values=checkbox_names)
    canvas.create_window(20, 370, anchor=NW, window=combobox, width=180, height=20)
    combobox.bind("<<ComboboxSelected>>", show_city)
    combobox.bind("<KeyRelease>", find_city)

    canvas.create_text(201, 355, text="sort:", font=("Arial", 10, 'bold'), anchor='nw', fill="#866df7")
    combobox_sort = ttk.Combobox(values=sort_values, state="readonly")
    canvas.create_window(200, 370, anchor=NW, window=combobox_sort, width=180, height=20)
    combobox_sort.bind("<<ComboboxSelected>>", sort_of_city)


window = Tk()
width = 400
height = 450
radius = 30
window.title("Tourist_in_Russia")
window.geometry(f"{width}x{height}+100+100")
window['background']='#866df7'


style = ttk.Style()
menu_bar = Menu(window, background='#866df7', foreground='black', activebackground='white', activeforeground='black')
menu_1 = Menu(menu_bar, tearoff=0, foreground='#866df7')
menu_1.add_command(label="Change BD", command=addition)
menu_bar.add_cascade(label="Change", background="#866df7", menu=menu_1)
window.config(menu=menu_bar)


canvas = Canvas(bg="white", width=width, height=height)
data = show_all()
city_names = []
checkbox_names.clear()

for row in data:
    checkbox_names.append(row[1])
    city_names.append([row[0], row[1]])

create_form(0)

window.mainloop()

# canvas.create_text(300, 100+n, text="max_T", font=font_of_main, anchor='nw', fill=colour_main)
# canvas.create_text(300, 212 + n, text="min_T", font=font_of_main, anchor='nw', fill=colour_main)


# photo = PhotoImage(file="image/moscow.png")
# Artwork = Label(window, image=photo)
# Artwork.photo = photo
# Artwork.pack()


# addition_tab = Button(window, text="Добавить|Удалить|Изменить", style='TButton', command=addition)
# addition_tab.grid(row=0, column=0)
#
# view_tab = Button(window, text="Главный экран", command=delete_addition)
# view_tab.grid(row=0, column=1)

# frame = Frame(window, padx=5, pady=5)
# frame.pack(expand=True)

#style.configure('TButton', font=('calibri', 10, 'bold', 'underline'), foreground='red')
# style.map("TButton",
#     foreground=[('pressed', '#856ff8'), ('active', 'blue')],
#     background=[('pressed', '!disabled', 'black'), ('active', 'white')]
#     )
#combobox.grid(anchor=NW, fill=X, padx=50, pady=50)
#combobox.grid(row=1, column=0)
# city_name_1 = Label(window, text="Название города", font="Roboto")
# city_name_1.grid(row=4, column=0)

# combobox_sort = ttk.Combobox(values=sort_values)
# combobox_sort.pack(anchor=NW, fill=X, padx=50, pady=50)
# combobox_sort.bind("<<ComboboxSelected>>", sort_of_city)

# btn = ttk.Button(text="Click")
# canvas.create_window(10, 20, anchor=NW, window=btn, width=100, height=50)

# city_name_2 = Label(window, text=name_n, font=("Roboto", 14),  justify='center', background="#866df7", foreground="white", anchor='e')
# city_name_2.grid(sticky = N, row=1, column=1)
#
# canvas.create_rectangle(0, 50, 400, 400, fill="#866df7", outline="white")
# date_1 = Label(window, text="foundation date", font=font_of_main,  justify='left', background="#866df7", foreground="white", anchor='w')
# date_1.grid(sticky = W, row=5, column=0, pady=3)
# date_2 = Label(window, text=date_n, font=font_of_information,  justify='left', background="#866df7", foreground="white", anchor='nw')
# date_2.grid(sticky = W, row=5, column=1)
#
# population_1 = Label(window, text="population", font=font_of_main,  justify='left', background="#866df7", foreground="white", anchor='nw')
# population_1.grid(sticky = W, row=6, column=0, pady=3)
# population_2 = Label(window, text=population_n, font=font_of_information,  justify='left', background="#866df7", foreground="white", anchor='nw')
# population_2.grid(sticky = W, row=6, column=1)
#
# time_1 = Label(window, text="time zone", font=font_of_main,  justify='left', background="#866df7", foreground="white", anchor='nw')
# time_1.grid(sticky = W, row=7, column=0, pady=3)
# time_2 = Label(window, text=time_n, font=font_of_information,  justify='left', background="#866df7", foreground="white", anchor='w')
# time_2.grid(sticky = W, row=7, column=1)
#
# region_1 = Label(window, text="subject", font=font_of_main,  justify='left', background="#866df7", foreground="white", anchor='nw')
# region_1.grid(sticky = W, row=8, column=0, pady=3)
# region_2 = Label(window, text=region_n, font=font_of_information,  justify='left', background="#866df7", foreground="white", anchor='w')
# region_2.grid(sticky = W, row=8, column=1)
#
#
# max_temp_1 = Label(window, text="max \ntemperature", font=font_of_main,  justify='left', background="#866df7", foreground="white", anchor='nw')
# max_temp_1.grid(sticky = W, row=10, column=0, pady=3)
#
# max_temp_2 = Label(window, text=max_temp_n, font=font_of_information,  justify='left', background="#866df7", foreground="white", anchor='w')
# max_temp_2.grid(sticky = W, row=10, column=1)
#
# min_temp_1 = Label(window, text="min \ntemperature", font=font_of_main,  justify='left', background="#866df7", foreground="white", anchor='nw')
# min_temp_1.grid(sticky = W, row=11, column=0, pady=3)
# min_temp_2 = Label(window, text=min_temp_n, font=font_of_information,  justify='left', background="#866df7", foreground="white", anchor='w')
# min_temp_2.grid(sticky = W, row=11, column=1)
#
# sight_1 = Label(window, text="sight", font=font_of_main,  justify='left', background="#866df7", foreground="white", anchor='nw')
# sight_1.grid(sticky = W, row=9, column=0, pady=3)
# sight_2 = Label(window, text=sight_n, font=font_of_information,  justify='left', background="#866df7", foreground="white", anchor='w')
# sight_2.grid(sticky = W, row=9, column=1)


# def delete_addition():
#     global city_name, date, population, time, region, sight, max_temp, min_temp
#     global city_name_tf, date_tf, population_tf, time_tf, region_tf, sight_tf, max_temp_tf, min_temp_tf, \
#         cal_btn, cal_btn_amend, cal_btn_delete
#     global combobox_add
#     city_name.grid_remove()
#     date.grid_remove()
#     population.grid_remove()
#     time.grid_remove()
#     region.grid_remove()
#     sight.grid_remove()
#     max_temp.grid_remove()
#     min_temp.grid_remove()
#
#     city_name_tf.grid_remove()
#     date_tf.grid_remove()
#     population_tf.grid_remove()
#     time_tf.grid_remove()
#     region_tf.grid_remove()
#     sight_tf.grid_remove()
#     max_temp_tf.grid_remove()
#     min_temp_tf.grid_remove()
#
#     cal_btn.grid_remove()
#     cal_btn_delete.grid_remove()
#     cal_btn_amend.grid_remove()
#     combobox_add.forget()

# combobox_sort = ttk.Combobox(values=sort_values)
# combobox_sort.pack(anchor=NW, fill=X, padx=50, pady=50)
# combobox_sort.bind("<<ComboboxSelected>>", sort_of_city)

