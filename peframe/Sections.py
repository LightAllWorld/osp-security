
from modules import pefile

def get(pe):
	NumberOfSections = 0
	for section in pe.sections:
		section.get_entropy()
		if section.SizeOfRawData == 0 or (section.get_entropy() > 0 and section.get_entropy() < 1) or section.get_entropy() > 7:
			suspicious = True
		else:
			suspicious = False

		if suspicious == True :
			NumberOfSections = NumberOfSections + 1

	return NumberOfSections
