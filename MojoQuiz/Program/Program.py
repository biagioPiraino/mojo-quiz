from Quizzer import Quizzer
from UserInterface import UserInterface

class Program:
	def __init__(self) -> None:
		pass

	@classmethod
	def RunProgram(self) -> None:
		quizzer = Quizzer()
		quizzer.LoadQuestions()
		UserInterface(quizzer)
