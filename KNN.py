import math
from collections import Counter

def euclidian_distance(a, b):
	#implementation of euclidian distance formula between points a and b
	distances = []
	for i in range(len(a)):
		distances.append((a[i] - b[i])**2)
	return math.sqrt(sum(distances))

class KNN_model():
	def __init__(self,n_neighbours,X,Y,input, model_type):
		self.n_neighbours = n_neighbours
		self.X = X
		self.Y = Y
		self.input = input
	def find_neighbours(self):
		#predict a single input
		self.dist = []
		for i in range(len(self.X)):
			self.dist.append(( self.Y[i], euclidian_distance(self.input,self.X[i])))
		self.dist.sort(key=lambda tup: tup[1])
	def predict(self):https://martin-tin.medium.com/k-nearest-neighbours-knn-a9f8ba09cb8b
		self.knn = []
		for i in range(n_neighbours):
			self.knn.append(self.dist[0][i])
		#if regression, return mean of knn
		if model_type == 'regression':
			return sum(self.knn)/len(self.knn)
		#if classifcation, return mode of knn
		if model_type == 'classification':
			c = Counter(self.knn)
			dict_items = {i:self.knn[i] for i in range(len(self.knn))} 
			return [i for i in c if i == c.most_common(1)]

#defining key information
n_neighbours = 1
X = [0,1],[0,0]
Y = [1,1]
input = [0,1],[0,1]
model_type = 'regression'

preds = []
def main():
	#predicting multiple inputs	
	for i in range(len(input)):
		selected_input = input [i]
		model = KNN_model(n_neighbours,X,Y,selected_input, model_type)
		model.find_neighbours()
		preds.append(model.predict())

main()
#print predictions
print(preds)






