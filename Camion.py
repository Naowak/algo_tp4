import math
import Ville

def calcul_cout(ville_A, ville_B) :
	return math.sqrt(pow(ville_A.get_X() - ville_B.get_X(), 2) + pow(ville_A.get_Y() - ville_B.get_Y(), 2))


class Camion :
	def __init__(self) :
		self._villes = list()
		self._nb_villes = 0

	def cout(self) :
		ret = 0
		for i in range(self._nb_villes - 1) :
			ret += calcul_cout(self._villes[i], self._villes[i+1])
		return ret

	def add_ville(self, ville, pos) :
		if not isinstance(pos, int) :
			raise Exception("Error Camion::add_ville : pos is not an interger\n")
		self._villes.insert(pos, ville)
		self._nb_villes += 1

	def remove_ville(self, pos) :
		if not isinstance(ville, Ville.Ville) :
			raise Exception("Error Camion::remove_ville : ville is not a ville\n")
		ville = self.get_ville(pos)
		self._villes.remove(ville)
		self._nb_villes -= 1

	def get_ville(self, pos) :
		return self._villes[pos]

	def __len__(self) :
		return self._nb_villes
