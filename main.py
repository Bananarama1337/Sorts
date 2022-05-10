import random
import time
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d

#creating list
i = 100
list_to_sort = []
while i != 0:
    list_to_sort.append(random.randint(0, 1000))
    i -= 1

print(list_to_sort)
#sort functions


def bubble_sort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list


def selection_sort(list):
    for i in range(len(list)-1):
        for j in range(i, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list


def insert_sort(list):
    for i in range(1, len(list)):
        current = list[i]
        cur_i = i
        while cur_i > 0 and list[cur_i - 1] > current:
            list[cur_i], list[cur_i - 1] = list[cur_i - 1], list[cur_i]
            cur_i -= 1
    return list


def merge_sort(list):
    #first part (dividing list on parts)
    middle = len(list) // 2
    left = list[:middle]
    right = list[middle:]
    if len(left) > 1:
        left = merge_sort(left)
    if len(right) > 1:
        right = merge_sort(right)

    #second part (sorting)
    support_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            support_list.append(left[i])
            i += 1
        else:
            support_list.append(right[j])
            j += 1
    if i < len(left):
        support_list += left[i:]
    if j < len(right):
        support_list += right[j:]
    return support_list


def quick_sort(list):
    if len(list) <= 1:
        return list
    else:
        q = random.choice(list)
        left = []
        centre = []
        right = []
        for elem in list:
            if elem < q:
                left.append(elem)
            elif elem > q:
                right.append(elem)
            else:
                centre.append(elem)

    return quick_sort(left) + centre + quick_sort(right)

def graphic(function, name, m_plot):
    sorted_time = list()
    lengh = list()
    for i in range(0, 198):
        lengh.append(i)

    for i in range(20, 2000, 10):
        list_sort = list(range(i, 0, -1))
        start_time = time.time()
        function(list_sort)
        sorted_time.append(time.time() - start_time)
    #print("Время, затрченное на сортировку:", sorted_time)
    if m_plot == 1:
        #интерполируем прямую времени по кол-ву символов
        ysmooth = gaussian_filter1d(sorted_time, sigma=10)
        #строим график
        plt.title(name)
        plt.xlabel('Кол-во элементов (n)')
        plt.ylabel('Время, с')
        plt.plot(lengh, ysmooth)
        plt.show()
    else:
        return sorted_time

def one_gpaphic(f, f1, f2, f3, f4):
    lengh = list()
    for i in range(0, 198):
        lengh.append(i)

    time1 = graphic(f, 'Bubble', 0)
    time2 = graphic(f1, "Selection", 0)
    time3 = graphic(f2, "Insert", 0)
    time4 = graphic(f3, "Merge", 0)
    time5 = graphic(f4, "Quick", 0)

    y1 = gaussian_filter1d(time1, sigma=10)
    y2 = gaussian_filter1d(time2, sigma=10)
    y3 = gaussian_filter1d(time3, sigma=10)
    y4 = gaussian_filter1d(time4, sigma=10)
    y5 = gaussian_filter1d(time5, sigma=10)
    # строим график
    plt.title("Алгортимы сортировок")
    plt.xlabel('Кол-во элементов (n)')
    plt.ylabel('Время, с')
    plt.plot(lengh, y1, label='Пузырьковая сортировка')
    plt.plot(lengh, y2, label='Сортировка выбором')
    plt.plot(lengh, y3, label='Сортировка вставками')
    plt.plot(lengh, y4, label='Сортировка слиянием')
    plt.plot(lengh, y5, label='Быстрая сортировка')
    plt.legend()
    plt.show()

repeat = 1
list1 = [9, 6, 8, 1, 2, 3, 5]
while repeat != 0:
    choice = input("Какой метод сортировки предпочитаете? Для завершения напишите 'нет'\n")
    if choice == "нет":
        repeat = 0
# Пузырьковая
    if choice == "bubble":
        print(bubble_sort(list_to_sort))
        graphic(bubble_sort, "Пузырьковая сортировка", 1)
# Выбором
    elif choice == "selection":
        print(selection_sort(list_to_sort))
        graphic(selection_sort, "Сортировка выбором", 1)
# Вставкой
    elif choice == "insert":
        print(insert_sort(list_to_sort))
        graphic(insert_sort, "Сортировка вставками", 1)
# Слиянием
    elif choice == "merge":
        print(merge_sort(list_to_sort))
        graphic(merge_sort, "Сортировка слиянием", 1)
# Быстрая
    elif choice == "quick":
        print(quick_sort(list_to_sort))
        graphic(quick_sort, "Быстрая сортировка", 1)
# График
    elif choice == "graph":
        print("Строим график")
        one_gpaphic(bubble_sort, selection_sort, insert_sort, merge_sort, quick_sort)