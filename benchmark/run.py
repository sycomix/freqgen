from sklearn.model_selection import ParameterSampler, ParameterGrid
from scipy.stats.distributions import uniform
from subprocess import run

param_grid = {
    "mutation_rate": uniform(),
    "crossover_rate": uniform(),
    "population_size": uniform(5, 100),
}

grid = ParameterSampler(param_grid, 5)

file_grid = {
    "target": ["banth1", "ecol", "ngon", "paer"],
    "insert": ["BoNT", "gfp", "human_HBB", "insulin", "luciferase", "oxytocin"],
}
file_grid = ParameterGrid(file_grid)

for params in grid:
    print(params)
    cmd = [
        "freqgen generate",
        f"-p {int(params['population_size'])}",
        f"-m {params['mutation_rate']}",
        "-e 15",
        f"-c {params['crossover_rate']}",
        "--log --dna ",
    ]
    for f in file_grid:
        cmd_for_file = (
            " ".join(cmd)
            + f"-s inserts/{f['insert']}.fasta "
            + f"-f targets/{f['target']}.yaml"
            + " > /dev/null"
        )
        print(cmd_for_file)
        run(cmd_for_file, shell=True)

