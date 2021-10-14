import random

# library code here

class Allele:
    """This class represents a single allele object that can be shared by multiple individuals
    """
    
    def __init__(self, name, fitness):
        
        if not 0 <= fitness <= 1:
            raise ValueError('fitness score must be between 0 and 1 inclusive')
        
        self.name = name
        self.fitness = fitness
        
    def __repr__(self):
        return f"{self.name} (fitness {self.fitness})"
        
class Individual:
    
    def __init__(self, alleles):
        self.alleles = alleles
        
    def __getitem__(self, index):
        return self.alleles[index]
    
    def get_genotype(self):
        result = ""
        for allele in self.alleles:
            result = result + allele.name
        return result
    
    def get_fitness(self):
        result = 1
        for allele in self.alleles:
            result = result * allele.fitness
        return result
        
def get_allele_frequency(allele, population):
    if len(population) == 0:
        raise ValueError('Population must contain at least one individual')
    
    return len([i for i in population if allele in i.alleles]) / len(population)

def create_random_individual():
    random_alleles = [
        random.choice(locus_one),
        random.choice(locus_two),
        random.choice(locus_three),
    ]    

    random_individual = Individual(random_alleles)
    return random_individual

def death(population):
    for ind in population:
        if random.random() > ind.get_fitness():
            population.remove(ind)

            
def birth(population):
    for _ in range(100 - len(population)):
        chosen = random.choice(population)
        new_individual = Individual(chosen.alleles)
        population.append(new_individual)  

