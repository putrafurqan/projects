"""
Self Replicant Virus
20 October 2017
06 : 36
"""
import os

vir_num = 0
for i in range(100):
    vir_num += 1
    os.system(cp /home/ryan/virus_domain/virus.py /home/ryan/virus_comain)
    os.system("mv /home/ryan/virus_comain/virus.py /home/ryan/virus_comain/virus{}.py".format(vir_num))
    os.system("cp /home/ryan/virus_comain/virus{}.py /home/ryan/virus".format(vir_num))
