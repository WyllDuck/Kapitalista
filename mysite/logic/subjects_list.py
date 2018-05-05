subjects = [[240011, "Àlgebra Lineal"],
	[240012, "Càlcul I"],
	[240013, "Mecànica Fonamental"],
	[240014, "Química I"],
	[240015, "Fonaments d'Informàtica"],
	[240021, "Geometria"],
	[240022, "Càlcul II"],
	[240023, "Termodinàmica Fonamental"],
	[240024, "Química II"],
	[240025, "Expressió Gràfica"],
	[240031, "Electromagnetisme"],
	[240032, "Mètodes Numèrics"],
	[240033, "Materials"],
	[240131, "Equacions Diferencials"],
	[240132, "Informàtica"],
	[240133, "Mecànica"],
	[240041, "Economia i Empresa"],
	[240042, "Estadística"],
	[240043, "Dinàmica de Sistemes"],
	[240044, "Projecte I"],
	[240141, "Teoria de Màquines i Mecanismes"],
	[240401, "Ampliació de Mecànica"],
	[240402, "Comunicació d'Informació Tècnica"],
	[240403, "Debats Sobre Tecnologia i Societat"],
	[240404, "Els Orígens de l'Enginyeria Moderna"],
	[240405, "Jocs per a Computadors. Estructura i Desenvolupament"],
	[240406, "Taller Elèctric"],
	[240407, "Tecnologia de la Llum"]]

# Verify that the code given is correct 
def verify_code (code):
	try:
		for item in subjects:
			if item[0] == int(code):
				break
		else:
			return False

		return True

	except:
		return False

# Get <option> tag for HTML without the code subject selected
def get_input_var (code):
	return ['{}: {}'.format(item[0], item[1]) for item in subjects if item[0] != int(code)]

# Get <option> tag for HTML with all subjects
def get_input_var_defaut ():
	return ['{}: {}'.format(item[0], item[1]) for item in subjects]	

# Get <option> tag for HTML a subject given
def get_current_subject (code):
	for subject in subjects:
		if subject[0] == int(code):
			return '{}: {}'.format(subject[0], subject[1])
