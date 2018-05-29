from logic.asignaturas import quatris

subjects = quatris()

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

"""
Those two function are used to in ""Graph_3"" to get the <option> tagfor the selectors
"""
# Get <option> tag for HTML without a list of subjects
def get_input_var_without_list_code (subjects_list):
	return ['{}: {}'.format(item[0], item[1]) for item in subjects if not str(item[0]) in subjects_list]

def get_input_var_for_list_code (subjects_list):
	return ['{}: {}'.format(item[0], item[1]) for item in subjects if str(item[0]) in subjects_list]
	
# Get <option> tag for HTML a subject given
def get_current_subject (code):
	for subject in subjects:
		if subject[0] == int(code):
			return '{}: {}'.format(subject[0], subject[1])

# Get name of subject
def get_name (code):
	for subject_code, subject_name in subjects:
		if int(subject_code) == int(code):
			return subject_name