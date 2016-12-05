import sys
import Ville
import Camion
import Solution

NB_VOISINS = 50

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

S = Solution.Solution()
S.init_random(villes)
Voisins = S.draw_N_voisins(NB_VOISINS)
print(S)
for v in Voisins :
	print(v)


fichier.close()


