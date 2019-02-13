from datetime import datetime
timestamp = ''.join([ i for i in list(str((datetime.now()))) if i not in '- .:'])
timestamp

file_name_in = '/Users/davidrogers/documents/github/references-and-illustrations/Py_file_import_example.txt'
with open(file_name_in) as f:
	fl=f.readlines()

fl # Note the line break characters, and the use of double-single quote alternation for "here's"

def fileNameOut(	path='/Users/davidrogers/documents/github/references-and-illustrations/',
					base='example',
					timestamp=True):
	timestamp = ''.join([ i for i in list(str((datetime.now()))) if i not in '- .:'])
	file_name = path+base+'_'+timestamp+'.txt'
	return file_name


file_name_out = fileNameOut()
with open(file_name_out,'w') as fw:   
	fw.write("Hello world!")


with open(file_name_out,'w') as fw:  # Since no unique file name has been generated, this will overwrite the original file
	fw.write("Hello again world!")


