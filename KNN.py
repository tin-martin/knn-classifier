import math

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
		self.model_type = model_type
	def fit(self):
		#predict a single input
		self.dist = []
		for i in range(len(self.X)):
			self.dist.append(['X', euclidian_distance(self.input,self.X[i])])
		
		for i in range(len(self.Y)):
			self.dist.append(['Y', euclidian_distance(self.input,self.Y[i])])
		self.dist.sort(key=lambda x: x[1])

	def predict(self):
		self.knn = []
		self.model_type
		#if regression, return mean of knn
		if self.model_type == 'regression':
			for i in range(n_neighbours):
				self.knn.append(self.dist[i][1])
			return sum(self.knn)/len(self.knn)
		#if classification, return mode of knn
		if self.model_type == 'classification':
			self.knn = [i[0] for i in self.dist]

			for i in range(n_neighbours):
				self.knn.append(self.dist[i][0])
			dict_items = [i[0] for i in self.knn]
			return max(set(dict_items), key = dict_items.count)
			
#defining key information
n_neighbours = 1
X = [[2,2],[2,2]]
Y = [[1,1],[1,1],[1,1]]
input = [[0,0],[0,0]]



def NearestNeighbours(n_neighbours, X, Y, input, mode_type):
	preds = []
	for i in range(len(input)):
		selected_input = input [i]
		model = KNN_model(n_neighbours,X,Y,selected_input, mode_type)
		model.fit()
		preds.append(model.predict())
	return preds

	
predictions = NearestNeighbours(n_neighbours, X, Y, input,'classification')
#print predictions
print(predictions)






