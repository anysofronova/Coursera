# импортируем библиотеки

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sc
%matplotlib inline

# Генерируем выборку объемом 1000 из Экспоненциального-распределения с параметром lambd = 1

lambd = 0.62
ex = sc.expon(lambd)
sample = ex.rvs(1000)

x = np.linspace(0, 10, 1000)
pdf = ex.pdf(x)

plt.hist(sample, density=True, label='Гистограмма выборки')
plt.plot(x, pdf, label='Теоритическая плотность')

# подписываем оси
plt.ylabel('f(x)')
plt.xlabel('x')

plt.legend()
plt.show()

for n in [5, 10, 50]:
    
    # список из средних значений с помощью генератора списков
    means = [ex.rvs(n).mean() for i in range(1000)]
    
    # строим гистограмму
    plt.hist(means, density=True, label='Гистограмма')
    
    # вычисляем матожидание и дисперсию
    loc, scale = sc.norm.fit(means)
    
    #нормальное распределение
    norm = sc.norm(loc, scale)
    x = np.linspace(0, 5, 100)
    y = norm.pdf(x)
    
    # строим окончательный график
    plt.plot(x, y, label='Теоритическая плотность')
    plt.legend()
    plt.title("Размер выборки " + str(n))
    plt.ylabel('f(x)')
    plt.xlabel('Среднее выборки x')
    plt.show()
    
    # С ростом n точность нормальной аппроксимации увеличивается.
