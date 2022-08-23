import numpy as np


def probability(p: float) -> bool:
    return p > np.random.uniform(0.0, 1.0)


def create_chromosome(n: int) -> list[int]:        
    return [np.random.randint(0, 2) for _ in range(n)]


def select_features(chromosome: list[int]) -> list[int]:
    return [index for index, element in enumerate(chromosome) if element == 1]


def mutation(chromosome: list[int]) -> list[int]:
    for i in range(chromosome.__len__()):
        if probability(0.02):
            chromosome[i] = (lambda x: 1 if x == 0 else 0)(chromosome[i])
    return chromosome


def crossover(p_1, p_2):
    crossing_point: int = len(p_1) // 2
    c_1 = mutation(p_1[:crossing_point][:]) + mutation(p_2[crossing_point:][:])
    c_2 = mutation(p_2[:crossing_point][:]) + mutation(p_1[crossing_point:][:])

    return c_1, c_2
    


if __name__ == "__main__":
    p1 = create_chromosome(10)
    p2 = create_chromosome(10)

    print(p1)
    print(p2)

    print()
    
    c1, c2 = crossover(p1, p2)
    print(c1)
    print(c2)




        
    
