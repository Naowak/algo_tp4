import sys
import Ville
import Camion
import Solution

NB_VOISINS = 200
NB_INIT_SOLUTION = 1
NB_ARRET = 30


def func_compare_sol(s1, s2) :
	return s1.compare(s2)


if len(sys.argv) < 2 :
	raise Exception("Usage : <nom_fichier>\n")

nom_fichier = sys.argv[1]
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

file_solution = list()
for i in range(NB_INIT_SOLUTION) :
	s = Solution.Solution()
	s.init_random(villes)
	file_solution.append(s)
file_solution.sort(func_compare_sol)

liste_solution_finale = list()

test_amelioration_last_turn = False
compteur_aucune_amelioration = NB_ARRET
for i in range(NB_INIT_SOLUTION) :
	solution_en_traitement = file_solution.pop(0)
	print(i)

	while(True) :
		voisins = solution_en_traitement.draw_N_voisins(NB_VOISINS)
	
		for v in voisins :
			if(v.get_cout() < solution_en_traitement.get_cout()) :
				solution_en_traitement = v
				test_amelioration_last_turn = True

		#print(str(solution_en_traitement.get_cout()) + " " + str(i))

		if(test_amelioration_last_turn) :
			compteur_aucune_amelioration = NB_ARRET
			test_amelioration_last_turn = False
		else :
			compteur_aucune_amelioration -= 1
			if(compteur_aucune_amelioration <= 0) :
				liste_solution_finale.append(solution_en_traitement)
				break


liste_solution_finale.sort(func_compare_sol)
#for l in liste_solution_finale :
#	print(l.get_cout())

print("digraph {")
for c in liste_solution_finale[0]._camions :
	for i in range(c._nb_villes - 1) :
		print("\t\t" + str(c.get_ville(i).get_id()) + " -> " + str(c.get_ville(i+1).get_id()) + ";")
print("}")



fichier.close()


