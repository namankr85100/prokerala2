
from client import ApiClient, ValidationError, AuthenticationError
import json

def run():
	try:
		client = ApiClient('a995b0ff-2269-45bf-a96e-07233c2aa03c', 'iqxjWqVzDUObnVTMgVdUGKVPhdFhE6qCRIF6oG8u')
		result = client.get('v2/astrology/planet-position', {
			'ayanamsa': 1,
			'coordinates': '23.1765,75.7885',
			'datetime': '1975-04-25T14:10:00+00:00',
			'chart_type': 'lagna',
			'chart_style': 'north-indian'
		})
		# print json.dumps(result, indent=4)
		print(result)
	except ValidationError as e:
		for msg in e.getValidationMessages():
			print(msg['detail'])
	except AuthenticationError as e:
		print (e.message)

if __name__ == '__main__':
	run()