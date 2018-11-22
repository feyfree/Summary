import os
import shutil

f = os.listdir()
for i in f:
	if os.path.isfile(i):
		shutil.move(i, './sort')
