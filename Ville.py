class Ville :
	def __init__(self, Id, X, Y, qt, tmin, tmax, dur) :
		self._id = Id
		self._X = X
		self._Y = Y
		self._qt = qt
		self._tmin = tmin
		self._tmax = tmax
		self._dur = dur

	def __str__(self) :
		return "Ville : " + str(self._id) + " " + str(self._X) + " " + str(self._Y) + " " + str(self._qt) + " " + str(self._tmin) + " " + str(self._tmax) + " " + str(self._dur) 

	def get_id(self) :
		return self._id

	def get_X(self) :
		return self._X

	def get_Y(self) :
		return self._Y

	def get_qt(self) :
		return self._qt

	def get_tmin(self) :
		return self._tmin

	def get_tmax(self) :
		return self._tmax

	def get_dur(self) :
		return self._dur
	
	def __eq__(self, ville) :
		return self.get_id() == ville.get_id()