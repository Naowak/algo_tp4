import Ville
import Camion
import random

class Solution :
	def __init__(self) :
		self._ville_depart = None
		self._camions = list()
		self._cout = 0

	def init_random(self, villes) :
		if not isinstance(villes, list) :
			raise Exception("Error Solution::init_random : Villes isn't a list\n")
		if len(villes) <= 1 :
			raise Exception("Error Solution::init_random : Villes list not long enough\n")

		self._ville_depart = villes[0]
		villes = villes[1:]

		compteur = 0

		for v in villes :
			if len(self._camions) == 0 :
				self._camions.append(Camion.Camion())
				self._camions[0].add_ville(self._ville_depart, 0)
				self._camions[0].add_ville(v, 1)
				self._camions[0].add_ville(self._ville_depart, 2)
			else :
				self._camions[0].add_ville(v, random.choice(range(len(self._camions[0]))[1:-1]))
			compteur += 1

		self._cout = self._camions[0].cout()

	def calcul_cout(self) :
		self._cout = 0
		for c in self._camions :
			self._cout += c.cout()
		return self._cout


	def move_ville(self, old_camion, old_pos, new_camion, new_pos) :
		ville = old_camion.get_ville(old_pos)
		old_camion.remove_ville(old_pos)
		new_camion.add_ville(ville, new_pos)
		self.calcul_cout()

	def copy(self):
		new_S = Solution()
		new_S._ville_depart = self._ville_depart
		new_S._cout = self._cout

		for c in self._camions :
			new_S._camions.append(c.copy())

		return new_S

	def create_voisin(self, old_camion, old_pos, new_camion, new_pos) :
		new_S = self.copy()
		if(new_camion == len(new_S._camions)) :
			#On creer un nouveau camion pour ce voisin
			new_S._camions.append(Camion.Camion())
			new_S._camions[new_camion].add_ville(new_S._ville_depart, 0)
			new_S._camions[new_camion].add_ville(new_S._ville_depart, 1)
		new_S.move_ville(new_S._camions[old_camion], old_pos, new_S._camions[new_camion], new_pos)
		return new_S

	def all_voisins(self) :
		liste_positions_camions = list()
		for c in self._camions :
			liste_positions_camions.append(range(len(c))[1:-1])
		liste_positions_camions.append([1])

		liste_all_voisins_pos = list()
		for c_1 in range(len(liste_positions_camions) - 1) :
			for p_1 in liste_positions_camions[c_1] :
				for c_2 in range(len(liste_positions_camions)) :
					for p_2 in liste_positions_camions[c_2] :
						liste_all_voisins_pos.append((c_1, p_1, c_2, p_2))

		return liste_all_voisins_pos

	def draw_N_voisins(self, N) :
		liste_all_voisins = self.all_voisins()
		liste_voisins_to_do = list()
		for i in range(N) :
			voisin = random.choice(liste_all_voisins)
			liste_all_voisins.remove(voisin)
			liste_voisins_to_do.append(voisin)

		voisins = list()
		for v in liste_voisins_to_do :
			voisins.append(self.create_voisin(v[0], v[1], v[2], v[3]))

		return voisins



	def __str__(self) :

		string = "Solution :\n"
		cpt = 0
		for c in self._camions :
			string += str(cpt) + " : "
			for i in range(len(c)) :
				string += c.get_ville(i).get_id().__str__()
				string += " "
			string += "\n"
			cpt += 1
		string += "Cout : " + str(self._cout) + "\n"
		return string
