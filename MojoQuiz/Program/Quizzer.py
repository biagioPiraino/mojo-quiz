from queue import Queue
from ApiRequester import ApiRequester

class Quizzer:
	def __init__(self) -> None:
		self.__questions = Queue()
		self.__cached_question: str
		self.__cached_answer: bool

	def LoadQuestions(self) -> None:
		requester = ApiRequester()
		questions = requester.RetrieveQuestions()
		for question in questions:
			self.__questions.put(question)

	def ReturnNextQuestions(self) -> str:
		self.__cache_current_question()
		return self.__cached_question

	def CheckUserAnswer(self, user_answer: bool) -> bool:
		return user_answer == self.__cached_answer

	def QuestionsStillAvailable(self) -> bool:
		return not self.__questions.empty()

	def __cache_current_question(self) -> None:
		question = self.__questions.get()
		self.__cached_question = question.GetQuestion()
		self.__cached_answer	 = question.GetAnswer()