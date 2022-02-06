class TowerOfHanoi:
	def __init__(self, height = 3):
		self.height = height
		self.state = {"L":[i for i in range(self.height, 0, -1)], "C":[], "R":[]}
		
	def get_state_string(self):
		result = ""
		for key in self.state:
			result += f"{key}|{self.state[key]}\n"
		return result
	
	def __str__(self):
		result = self.get_state_string()
		return result
	
	def __repr__(self):
		return self.__str__(self)
	
	def __or__(self, operation):
		return self.execute(operation)
	
	def execute(self,operation):
		source = operation[0]
		destoperation[-1]
		return self.move(source, destination)
		
	def move(self, source, destination):
		if source == destination:
			return None
			
		if len(self.state[source]) == 0:
			return None
		
		peeked_source_value = self.state[source][-1]
		if len(self.state[destination]) > 0 and self.state[destination][-1] < peeked_source_value:
			return None
		
		popped_source_value = self.state[source].pop()
		self.state[destination].append(popped_source_value)
		return self
	
	def solved(self):
		return sum(self.state["R"]) == (self.height * (self.height + 1))/2
			