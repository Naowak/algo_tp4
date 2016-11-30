import Ville
import Camion
import random

class Solution :
	def __init__(self, villes) :
		if not isinstance(villes, list) :
			raise Exception("Error Solution::__init__ : Villes isn't a list\n")
		if len(villes) <= 1 :
			raise Exception("Error Solution::__init__ : Villes list not long enough\n")

		self.ville_depart = villes[0]
		villes = villes[1:]

		self._camions = list()
		self._cout = 0

		compteur = 0

		for v in villes :
			if len(self._camions) == 0 :
				self._camions.append(Camion.Camion())
				self._camions[0].add_ville(self.ville_depart, 0)
				self._camions[0].add_ville(v, 1)
				self._camions[0].add_ville(self.ville_depart, 2)
			else :
				self._camions[0].add_ville(v, random.choice(range(len(self._camions[0]))[1:-1]))
			compteur += 1

		self.cout = self._camions[0].cout()


	def move_ville(self, old_camion, old_pos, new_camion, new_pos) :
		old_camion.remove_ville(old_pos)
		new_camion.add_ville(new_pos)

	def copy(self):
		pass

	def __str__(self) :

		string = "Solution :\n"
		for c in self._camions :
			string += "0 : "
			for i in range(len(c)) :
				string += c.get_ville(i).get_id().__str__()
				string += " "
			string += "\n"
		return string
