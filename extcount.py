import os

def extcount(path):
	exts = {}
	try:
		filenames = os.listdir(path)
		for filename in filenames: 
			ext_temp = os.path.splitext(filename)[1]
			if ext_temp in exts.keys():
				exts[ext_temp] += 1
			else:
				exts[ext_temp] = 1

		for ext in exts.keys():
			print exts[ext], " ", ext
	except:
		pass