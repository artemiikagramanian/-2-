import matplotlib.pyplot as plt
import numpy as np

def sigma_k(data_x, data, k): #функция ищет погрешность k (неправильно)
  sum_y = 0.0
  sum_x = 0.0
  for i in range(len(data)):
    sum_y += data[i] * data[i]
    sum_x += data_x[i] * data_x[i]
  
  sigma = (((sum_y/sum_x) - k**2) / len(data))**0.5
  return sigma

def approx (data_x, data): #функция получает k и b аппроксимирующей прямой
  sum_cr = 0.0
  sum_sq = 0.0
  for i in range(len(data)):
    sum_cr += data[i]*data_x[i]
    sum_sq += data_x[i]*data_x[i]

  l = len(data)
  k = (sum_cr/l - sum(data)*sum(data_x)/(l**2))/(sum_sq/l - sum(data_x)*sum(data_x)/(l**2))
  b = (sum(data) - k*sum(data_x))/len(data)

  spis = []
  spis.append(k)
  spis.append(b)

  return spis

#задаем размеры картинки
fig = plt.figure(figsize = (10, 7))
ax = fig.add_subplot()

#массив иксов
data = [i for i in range(7363, 7942)]

#760, 2355, 2925, 3275, 4950, 5544, 5990, 7363, 7941              это я границы cool и heat отмечал
#293.79, 306.18, 304.6, 297.7, 306.4, 305.4, 299.2, 306.5, 305.6

#массив игриков
with open("c:/Users/Kagra/OneDrive/Рабочий стол/2.1.4/data_allum_ln.txt", "r") as f:
    data_ln = list(map(float, f.readlines()))

#строим график
plt.plot(data, data_ln, ".", linewidth = 1)

#считаем k и b
spis = []
spis = approx(data, data_ln)
sigma = sigma_k(data, data_ln, spis[0])

#выводим k*10^{-6}
print(spis[0]*1000000)

#рисуем прямую
x = np.arange(7363, 7941, 0.1)
y = spis[0]*x + spis[1]
plt.plot(x, y)

#называем оси
plt.ylabel("$ln((T_{cool} - T_к)/(T_0 - T_к))$")
plt.xlabel("$t, с$")

#называем график
plt.title("Аллюминий")
plt.grid()

#сохраняем
fig.savefig('ln_plot_3.png')
plt.show()