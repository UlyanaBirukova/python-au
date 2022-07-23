from scipy import stats
import numpy
import pandas
import random
import matplotlib.pyplot as plt
%matplotlib inline

# необходимые константы
length = 100     # длина списка данных
size_population = 50  # количество таких списков в популяции :)
cross = 0.8      # вероятность скрещивания списков
mutations = 0.1   # вероятность мутации
generations = 2_000_000_000 # количество поколений
        
# функция, возвращающая значение уровня приспособленности особи к условию задачи (чем больше р-значение, тем выше уровень)
def fitness(individ):
    id = pandas.DataFrame(individ)
    return stats.kstest(id, 'poisson', (id.mean(), id.std()), N=5000)[1]
    
# класс значений уровня приспособленности
class fitness_max():
    def __init__(self):
        self.values = [0] # изначально значение инициализируется наименьшей приспособленности

# класс особей популяции
class individ(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.fitness = fitness_max() # характеристика уровня приспособленности
    
# функция, создающая особь
def borning_individ():
    return individ([random.randint(0,1000) for i in range(length)])
    
# функция, создающая поколение
def borning_population(n = 0):
    return list([borning_individ() for i in range(n)])
    
population = borning_population(n = size_population)
cnt = 0 # счётчик числа поколений

fitness_values = list(map(fitness, population)) # список значений уровня приспособленности всех особей популяции

#for individ, fitness_values in zip(population, fitness_values):
#    individ.fitness.values = fitness_values # присваиваем вычисленное значение уровня приспособленности

max_fitness_values = []    # максимальная приспособленность особей популяции
middle_fitness_values = [] #средняя приспособленность особей популяции

# функция клонированния особи
def clone(value):
    ind = borning_individ(value[:])
    ind.fitness.values[0] = value.fitness.values[0]
    return ind

# функция естественного отбора
def competition(population, population_len):
    winners = []
    for i in range(population_len):
        i1 = i2 = i3 = 0
        while i1 == i2 or i1 == i3 or i2 == i3:
            i1, i2, i3 = random.randint(0,population_len), random.randint(0,population_len), random.randint(0,population_len)
        winners.append(max([population[i1], population[i2], population[i3]], key=lambda ind: ind.fitness.values[0])) # выживает та особь, которая больше похожа на распределение Пуассона :)
    return winners
    
# функция кроссинговера
def crossing(parent1, parent2):
    x = random.randint(1, length)
    parent1[x:], parent2[x:] = parent2[x:], parent1[x:]
    
# функция мутации
def mutation(mutant, indpb = 0.01):
    for i in range(length):
        if random.random() < indpb:
            mutant[i] = random.randint(0,1000)
            
# обновлённый список значений приспособленности особей популяции
#fitness_values = [individ.fitness.values[0] for individ in population]


# сам генетический алгоритм
inf = float('inf')
individ = pandas.DataFrame({'0': [0]})
while max(fitness_values) < stats.kstest('poisson', 'poisson', (individ.mean(), individ.std()), N=5000)[1] and cnt < generations:

    cnt += 1
    winners = competition(population, len(population))
    winners = list(map(clone, winners))
    
    for parent1, parent2 in zip(winners[::2], winners[1::2]):
        if random.random() < cross:
            crossing(parent1, parent2)
            
    for mutant in winners:
        if random.random() < mutations:
            mutation(mutant, indpb=1.0/length)
            
    new_fitness_values = list(map(fitness, winners))
    for individ, fitness_values in zip(winners, new_fitness_values):
        individ.fitness.values = fitness_value
        
    population[:] = winners
    
    fitness_values = [ind.fitness.values[0] for ind in population]
    
    fitness_max = max(fitness_value)
    middle_fitness = sum(fitness_values)/len(population)
    max_fitness_values.append(fitness_max)
    middle_fitness_values.append(middle_fitness)
    
    best_index = fitness_value.index(max(fitness_values))
    print(best_index)
    
    
print("Самая приспособленная особь = ", population[fitness_values.index(max(fitness_values))], "\n")
plt.plot(range(15), stats.poisson.cdf(range(15), mu=4), c='b', linewidth=2)
plt.show()
plt.plot(population[fitness_values.index(max(fitness_values))], color='green')
plt.show()


