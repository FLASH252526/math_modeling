import math
from task_3_my_model import k
from task_3_my_model import e
from task_3_my_model import h
T = 200
a = 300

N = (2 / math.sqrt(math.pi)) * (h / ((k * T) ** (3 / 2))) * e ** (-a / (k * T)) * a ** (T / 2)
print(N)