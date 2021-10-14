import pop
import tqdm
import sys

if len(sys.argv) != 5:
    sys.exit("Usage: python new_mutation.py fitness popluation_size iterations output_filename")

# gather command line arguments
old_allele_fitness = float(sys.argv[1])
population_size = int(sys.argv[2])
iterations = int(sys.argv[3])
output_filename = sys.argv[4]

# do the simulations
output  = open(output_filename, 'w')
output.write('iteration,population size, generation, fitness, frequency\n')

for it in tqdm.tqdm(range(iterations)):

    old_allele = pop.Allele('x', old_allele_fitness)
    new_allele = pop.Allele('X', 1)

    population = []

    for _ in range(population_size):
        population.append(pop.Individual([old_allele]))
    population.append(pop.Individual([new_allele]))


    for generation in range(100):
        freq = pop.get_allele_frequency(new_allele, population)
        output.write(f"{it},{population_size},{generation},{old_allele_fitness},{freq}\n")
        pop.death(population)
        pop.birth(population)
    
output.close()
