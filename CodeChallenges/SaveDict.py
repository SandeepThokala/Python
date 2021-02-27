#my solution :((
def save(dictionary, file_path):
	#dictionary.sort
	with open(file_path + r'\Dictionaries.txt', 'wt') as file:
		#file.write('-'*50 +'\n')
		#for i in dictionary.items():
			#file.write(f"{i[0]}: {i[1]}\n")


sample_dict = {'sandy': 1, 'deepu': 100, 'perserverance': 1000}
sample_file_path = r'C:\Users\sande\Desktop\Deepu\CodeChallenges'
saved_file_path = r'C:\Users\sande\Desktop\Deepu\CodeChallenges\Dictionaries.txt'
#save(sample_dict, sample_file_path)

def loader(file_path):
	dictionary = dict()
	with open(file_path, 'rt') as file:
		txt = file.readlines()
		#print(*(i.split(':')[1] for i in txt))
		for i in txt:
			dictionary[i.split(':')[0]] = i.split(':')[1]
	return dictionary

#not my solution :((
import pickle

def save_dict(dict_to_save, file_path):
	with open(file_path, 'wb') as file:
		pickle.dump(dict_to_save, file)

def load_dict(file_path):
	with open(file_path, 'rb') as file:
		return pickle.load(file)