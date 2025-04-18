import random as rand
import statistics as stat
import math

nums = [rand.randint(1, 100) for num in range(100)]
print(f"Среднее арифметическое: {stat.mean(nums)}")
print(f"Медиана: {stat.median(nums)}")
print(f"Стандартное отклонение: {round(stat.stdev(nums), 2)}")
print(f"Корень из суммы: {round(math.sqrt(sum(nums)), 2)}")