class Question:
	def __init__(self, question: str, answer: bool) -> None:
		self.__question = question
		self.__answer 	= answer

	def GetQuestion(self) -> str:
		return self.__question

	def GetAnswer(self) -> bool:
		return self.__answer