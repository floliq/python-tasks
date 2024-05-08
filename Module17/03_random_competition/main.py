import random

fst_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
scd_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
print("Первая команда: ", fst_team)
print("Вторая команда: ", scd_team)
winners = [(fst_team[i_res]
            if fst_team[i_res] > scd_team[i_res] else scd_team[i_res])
           for i_res in range(20)]
print("Победители тура: ", winners)
