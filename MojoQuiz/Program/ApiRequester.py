from DataFormatter import DataFormatter
import requests as rq

class ApiRequester:
	def __init__(self) -> None:
		pass

	def RetrieveQuestions(self) -> list:
		"""
			The following endpoint and parameters can be modified
			to obtain different results, please refer to 
			https://opentdb.com/api_config.php for details
		
			This method will return a list of Question
		"""
		api_endpoint = "https://opentdb.com/api.php"
		parameters = {
			"amount" : 10,
			"difficulty" : "medium",
			"type" : "boolean"
		}
		response = rq.get(url=api_endpoint, params=parameters)
		response.raise_for_status()
		formatter = DataFormatter()
		return formatter.FormatResults(response.json())