import numpy as np
import matplotlib.pyplot as plt

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

fig, ax = plt.subplots(ncols = 3, figsize = (15, 4))

with open("c:/Users/Kagra/OneDrive/Рабочий стол/2.5.1/data_sigma.txt", "r") as f:
    temp  = [0]*7
    sigma = [0]*7
    q  = [0]*7
    ar = [0]*7
    i = 0
    for x in f.readlines():
        temp[i], sigma[i], q[i], ar[i] = map(float, x.split())
        i += 1


ax[0].plot(temp, sigma, ".", label = "ds/dT = -0,267 Дж/(К * м^2)")
ax[1].plot(temp, q, ".", label = "q(T) = 0,27*T")
ax[2].plot(temp, ar, ".", label = "(U/F)(T) = -0.0002*T + 74.23")

spis = []
spis = approx(temp, sigma)
sigma = sigma_k(temp, sigma, spis[0])

x = np.arange(25, 60, 0.1)
y = spis[0]*x + spis[1]
ax[0].plot(x, y)

print(spis)

spis = []
spis = approx(temp, q)
sigma = sigma_k(temp, q, spis[0])

x = np.arange(25, 60, 0.1)
y = spis[0]*x + spis[1]
ax[1].plot(x, y) 

spis = []
spis = approx(temp, ar)
sigma = sigma_k(temp, ar, spis[0])

x = np.arange(25, 60, 0.1)
y = spis[0]*x + spis[1] + 0.1
ax[2].plot(x, y)


ax[0].set_ylabel("$\sigma, Н/м \cdot 10^{-3}$")
ax[0].set_xlabel("$T, К$")

ax[0].set_title("sigma")
ax[0].legend()

ax[1].set_ylabel("$q, Дж/м \cdot 10^{-3}$")
ax[1].set_xlabel("$T, К$")

ax[1].set_title("q")
ax[1].legend()

ax[2].set_ylabel("$U/F, Дж/м^2 \cdot 10^{-3}$")
ax[2].set_xlabel("$T, К$")

ax[2].set_title("U/F")
ax[2].legend()

ax[0].grid()
ax[1].grid()
ax[2].grid()
fig.savefig('c:/Users/Kagra/OneDrive/Рабочий стол/2.5.1/sigma.png')
plt.show() 
