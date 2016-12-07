all: run_nc
run_nc: Main.py Camion.py Solution.py Ville.py
	ln -s Main.py run_nc

clean: 
	rm run_nc