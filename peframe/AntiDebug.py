def get(pe, strings_match):
	antidbgs = strings_match['antidbg']
	SizeOfSignature = 0
	DEI   = hasattr(pe, 'DIRECTORY_ENTRY_IMPORT')
	if DEI:
		for lib in pe.DIRECTORY_ENTRY_IMPORT:
			for imp in lib.imports:
				for antidbg in antidbgs:
					if antidbg:
						if str(imp.name).startswith(antidbg):
							SizeOfSignature = SizeOfSignature + 1	

	return SizeOfSignature
