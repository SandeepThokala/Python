#my solution

def indexer(lst, val):
	l = []
	for i in lst:
		if i == val:
			l.append(lst.index(val))
		elif type(i) == list:
			l.append([lst.index(i), indexer(i, val)])
	return l

print(indexer([[[1,2,3,4,5,6,7,8],[3,4]], 3, 4, 5, [0,[4,0]]], 4))

#not my solution :(
def index_all(search_list, item):
	indices = list()
	for i in range(len(search_list)):
		if search_list[i] == item:
			indices.append([i])
		elif isinstance(search_list[i], list):
			for index in index_all(search_list[i], item):
				indices.append([i]+index)
	return indices