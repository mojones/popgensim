import pop
import pytest

def test_freq_single():
    test_allele_one = pop.Allele('A', 1)  
    
    test_population = [
        pop.Individual([test_allele_one])
    ]
    
    assert pop.get_allele_frequency(test_allele_one, test_population) == 1
    
    
def test_freq_multiple():
    test_allele_one = pop.Allele('A', 1)  
    test_allele_two = pop.Allele('a', 0.5) 
    
    test_population = [
        pop.Individual([test_allele_one]),
        pop.Individual([test_allele_two])
    ]
    
    assert pop.get_allele_frequency(test_allele_one, test_population) == 0.5
    
    
def test_individual_genotype():
    test_individual = pop.Individual([
        pop.Allele('A', 1),
        pop.Allele('f', 1),
        pop.Allele('U', 1)
    ])

    assert test_individual.get_genotype() == 'AfU'
    
    
def test_individual_fitness():
    test_individual = pop.Individual([
        pop.Allele('A', 1),
        pop.Allele('f', 0.8),
        pop.Allele('U', 0.7)
    ])

    assert test_individual.get_fitness() == pytest.approx(0.56)
    
    
def test_death():
    
    for _ in range(100):
        old_allele = pop.Allele('x', 0.9)
        new_allele = pop.Allele('X', 1)

        population = []

        for _ in range(100):
            population.append(pop.Individual([old_allele]))

        pop.death(population)

        assert len(population) <= 100