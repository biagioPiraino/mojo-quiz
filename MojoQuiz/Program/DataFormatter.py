from Question import Question
import html

class DataFormatter:
	def __init__(self) -> None:
		pass

	def FormatResults(self, data:dict) -> list:
		results = data["results"]
		questions = list()
		
		for result in results:
			question = html.unescape(result["question"])
			answer: bool

			if (result["correct_answer"] == "True"):
				answer = True
			else:
				answer = False

			questions.append(Question(
				question=question,
				answer=answer))

		return questions