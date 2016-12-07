#!/usr/bin/python2.7

import sys
import Ville
import Camion
import Solution
import time

DEPART = time.time()
NB_VOISINS = 20
N_MAX = 20
CPT_TABOU = 50


def func_compare_sol(s1, s2) :
	return s1.compare(s2)

def is_voisin_tabou(v, tabou) :
	for t in tabou :
		if t.is_the_same(v) :
			return True
	return False


if len(sys.argv) < 2 :
	raise Exception("Usage : <nom_fichier> <timer>\n")

nom_fichier = sys.argv[1]
timer = int(sys.argv[2]) - 2
fichier = open(nom_fichier, "r")

capacite_camion = fichier.readline().split(" ")[1] 
fichier.readline() #ligne inutile dans le fichier

villes = list()

i = 0

for ligne in fichier :
	t = ligne.split("\t")
	ville = Ville.Ville(int(t[0]), float(t[1]), float(t[2]), float(t[3]), float(t[4]), float(t[5]), float(t[6]))
	villes.append(ville)
	i = i + 1


tabou = list()
history = list()
cond = True
best_solution = None
first_round = True
test_amelioration_last_turn = False
compteur_aucune_amelioration = N_MAX
compteur_tabou = CPT_TABOU
while cond :
	solution_en_traitement = Solution.Solution()
	solution_en_traitement.init_random(villes)
	if(first_round) :
		best_solution = solution_en_traitement
		first_round = False

	while True :
		if(time.time() - DEPART > timer) :
			if(solution_en_traitement.get_cout() < best_solution.get_cout() ) :
				best_solution = solution_en_traitement
			cond = False
			break
		else :
			history.append(solution_en_traitement)
			voisins = solution_en_traitement.draw_N_voisins(NB_VOISINS)

			for v in voisins :
				if(v.get_cout() < solution_en_traitement.get_cout() and not is_voisin_tabou(v, tabou)) :
					solution_en_traitement = v
					test_amelioration_last_turn = True

			if(test_amelioration_last_turn) :
				compteur_aucune_amelioration = N_MAX
				test_amelioration_last_turn = False
			else :
				compteur_aucune_amelioration -= 1
				history = history[:-1]
				if(compteur_aucune_amelioration <= 0) :
					if(solution_en_traitement.get_cout() < best_solution.get_cout() ) :
						best_solution = solution_en_traitement
					tabou.append(solution_en_traitement)
					compteur_tabou -= 1
					if(compteur_tabou <= 0) :
						compteur_tabou = CPT_TABOU
						break
					else :
						if(len(history) >= 2) :
							solution_en_traitement = history[len(history) -1]
							history = history[:-1]
						else :
							break

print("digraph {")
for c in best_solution._camions :
	for i in range(c._nb_villes - 1) :
		print("\t" + str(c.get_ville(i).get_id()) + " -> " + str(c.get_ville(i+1).get_id()) + ";")
print("}")


fichier.close()


