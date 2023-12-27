from tabulate import tabulate

def table_popu(list_pop, list_popAwal):
    header = ['Chromosome', 'Individu', 'Fitness', 'Relative Fitness', 'Cumulative Fitness', 'Chromosome Area']
    
    chromo = [f'k{i}' for i in range(len(list_pop))]
    individu = [''.join(map(str, data)) for data in list_popAwal]
    fitness = [sum(x) for x in list_pop]
    Selected_Prob = [round(x/sum(fitness),3) for x in fitness]
    Cumulative_Prob = [round(sum(Selected_Prob[:i+1]), 3) for i in range(len(Selected_Prob))]
    area = []
    
    for i in range(len(Cumulative_Prob)):
        if i < len(Cumulative_Prob)-1:
            if Cumulative_Prob[i] != Cumulative_Prob[i+1]:
                if i == 0:
                    area.append(f'0.0 - {Cumulative_Prob[i]}')
                else:
                    area.append(f'{Cumulative_Prob[i-1]} - {Cumulative_Prob[i]}')
            else:
                area.append(f'{Cumulative_Prob[i-1]} - {Cumulative_Prob[i]}')
        else:
            area.append(f'{Cumulative_Prob[i-1]} - {Cumulative_Prob[i]}')
    
    table = zip(chromo, individu, fitness, Selected_Prob, Cumulative_Prob, area)
    print(tabulate(table, headers = header, floatfmt = ".3f"))
    
    return Selected_Prob