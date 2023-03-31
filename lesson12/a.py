import matplotlib.pyplot as plt

y = [i for i in range(0, 10)]
# y = [i ** 2 for i in x]
plt.title('Парабола')
plt.xlabel('Количество людей')
plt.ylabel('Количество денег')
plt.plot(y, '*--g', ms=20)
plt.savefig('my_first_figure.png')
plt.show()