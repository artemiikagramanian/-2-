import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize = (10, 7))
ax = fig.add_subplot()

#заполняем массив иксов
data = [i for i in range(5990, 7942)]

#это чтоб палочки были на графике, то, что закомменченно, это тупо для большого графика все палки, я думаю, разберешься
data_x_points = [5990, 7363, 7941]    #760, 2355, 2925, 3275, 4950, 5544, 5990, 7363, 7941
data_y_points = [299.2, 306.5, 305.6] #293.79, 306.18, 304.6, 297.7, 306.4, 305.4, 299.2, 306.5, 305.6

#заполняем массивы с температурами
#файы считываются в формате "калориметр комната"
with open("c:/Users/Kagra/OneDrive/Рабочий стол/2.1.4/data_allum.txt", "r") as f:
    data_calor = []
    data_room  = []

    for x in f.readlines():
        spis = list(map(float, x.split()))
        data_calor.append(spis[0])
        data_room.append (spis[1])

#рисуем кривые
#plt.plot(data, data_room , linewidth = 1)
plt.plot(data, data_calor,  linewidth = 1)

#рисуем палочки
plt.xticks(data_x_points, fontsize = 7)
plt.yticks(data_y_points, fontsize = 6)

#дальше поймешь
plt.ylabel("$T, К$")
plt.xlabel("$t, с$")

plt.title("Аллюминий")
plt.grid()

fig.savefig('plot_4.png')
plt.show()
