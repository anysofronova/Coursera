# Задача 3. Минимизация негладкой функции

# Теперь рассмотрим функцию h(x) = int(f(x)) на том же отрезке [1, 30], т.е. теперь каждое значение f(x) приводится к типу int и функция принимает только целые значения.
# Такая функция будет негладкой и даже разрывной, а ее график будет иметь ступенчатый вид. Убедитесь в этом, построив график h(x) с помощью matplotlib.
# Попробуйте найти минимум функции h(x) с помощью BFGS, взяв в качестве начального приближения x=30. Получившееся значение функции – ваш первый ответ в этой задаче.
# Теперь попробуйте найти минимум h(x) на отрезке [1, 30] с помощью дифференциальной эволюции. Значение функции h(x) в точке минимума – это ваш второй ответ в этом задании. Запишите его через пробел после предыдущего.
# Обратите внимание на то, что полученные ответы различаются. Это ожидаемый результат, ведь BFGS использует градиент (в одномерном случае – производную) и явно не пригоден для минимизации рассмотренной нами разрывной функции. Попробуйте понять, почему минимум, найденный BFGS, именно такой (возможно в этом вам поможет выбор разных начальных приближений).
# Выполнив это задание, вы увидели на практике, чем поиск минимума функции отличается от глобальной оптимизации, и когда может быть полезно применить вместо градиентного метода оптимизации метод, не использующий градиент. Кроме того, вы попрактиковались в использовании библиотеки SciPy для решения оптимизационных задач, и теперь знаете, насколько это просто и удобно.

import matplotlib.pyplot as plt
def f(x):
    return int(np.sin(x/5.) * np.exp(x/10.) + 5. * np.exp(-x/2.))
x = np.arange(1, 30, 0.1)
y = [f(e) for e in x]
plt.plot (x, y)
plt.show

fun1 = lambda x: int(np.sin(x/5.) * np.exp(x/10.) + 5. * np.exp(-x/2.))
print(minimize(fun1, 30, method='BFGS'))
print()
print(differential_evolution(fun1, [(1,30)]))

#       fun: -5
#  hess_inv: array([[1]])
#       jac: array([0.])
#   message: 'Optimization terminated successfully.'
#      nfev: 3
#       nit: 0
#      njev: 1
#    status: 0
#   success: True
#         x: array([30.])

#      fun: -11.0
#  message: 'Optimization terminated successfully.'
#     nfev: 122
#      nit: 7
#  success: True
#        x: array([24.04459104])

# -5 -11
