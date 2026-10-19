import matplotlib.pyplot as plt #импортируем модуль pyplot из библиотеки matplotlib,
                                #которая отвечает за построение графиков при помощи математических функций
import numpy as np #имопртируем библиотеку numpy для быстрой работы с математическими функциями

def graphic(min_x,max_x):
    if min_x>max_x:
        print("Ошибка,min<max")
        return -1
    if min_x + max_x == 0:
        print("Ошибка,min не должен быть отрицательной версией max")  #так как в следующей строке у нас кол-во точек напрямую зависит от min_x+max_x
        return -1
    x = np.linspace(min_x,max_x,10 * (min_x + max_x))   #размещаем на оси Ox 10*(min_x+max_x) точек,равномерно удаленных друг от друга,
                                  #в промежутке от min_x до max_x
    y = x * np.sin(x)    #ищем значение для каждого x
    plt.figure(figsize=(9, 5))  #создаем окно для вывода графика(figsize отвечает за соотношение сторон окна)
    plt.plot(x, y, label="y = x * sin(x)", color="red", linewidth=5)  #выводит все точки (x,y) на график,после чего соединяет их линиями
                                                                        #label- название, linewidth-толщина линии
    plt.title("График функции y = x * sin(x)", fontsize=12)  #делает заголовок в самом верху графика
    plt.xlabel("Ось X", fontsize=12) #fontsize-координаты на оси Ox
    plt.ylabel("Ось Y", fontsize=12) #fontsize-координаты на оси Ox
    plt.axhline(0, color='black', linewidth=1, linestyle='-')  #рисует горизонтальную линию,проходящую через 0,linestyle-тип линии(сплошной)
    plt.axvline(0, color='black', linewidth=1, linestyle='-')  #аналогично,только вертикально 
    plt.grid(True, linestyle=':', alpha=0.5)  #задает задний фон(точечный,для большей наглядности графика),alpha-прозрачность линий фона(от 0 до 1,для усредненности берем 0.5)
                                                #True активирует отображение сетки
    plt.legend(fontsize=12)   #окно в углу графика с описанием(y=x*sinx)
    plt.show()   #вывод на экран


def main():
    min_x=int(input("Введите min значение"))
    max_x=int(input("Введите max значение"))
    graphic(min_x,max_x)


main()
