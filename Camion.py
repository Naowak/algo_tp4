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
		ville = self.get_ville(pos)
		self._villes.remove(ville)
		self._nb_villes -= 1

	def get_ville(self, pos) :
		return self._villes[pos]

	def copy(self) :
		new_C = Camion()
		new_C._nb_villes = self._nb_villes
		for i in range(self._nb_villes) :
			new_C._villes.append(self._villes[i])
		return new_C

	def __len__(self) :
		return self._nb_villes

	def __eq__(self, camion) :
		if(self._nb_villes != camion._nb_villes) :
			return False
		for i in range(self._nb_villes) :
			if not self.get_ville(i) == camion.get_ville(i) :
				return False
		return True
