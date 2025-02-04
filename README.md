# Number Classification API

This is a Python-based API that classifies a number and returns its mathematical properties, along with a fun fact.

## Features
- Classifies a number as prime, perfect, odd/even, and Armstrong.
- Calculates the sum of the number's digits.
- Fetches a fun fact about the number from the Numbers API.

## API Endpoint
- **GET** `/api/classify-number?number=<number>`
  - Example: `https://<your-vercel-url>/api/classify-number?number=371`
  - Response:
    ```json
    {
      "number": 371,
      "is_prime": false,
      "is_perfect": false,
      "properties": ["armstrong", "odd"],
      "digit_sum": 11,
      "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
    }
    ```

## Requirements
- Python 3.x
- Flask
- Requests
- Flask-CORS

## Installation
1. Clone the repository:
	```
	git clone https://github.com/temisolovn/number-classification-api.git
	```
2. Install dependencies:
	```
	pip install -r requirements.txt
	```
3. Run the application:
	```
	python app.py
	```

## Deployment
	
This API is deployed on Vercel. You can access it at:

	```
	https://number-classification-apixx.vercel.app/api/classify-number?number=371
	```
## Resources
[Numbers API](http://numbersapi.com/#42)

[Parity (Mathematics)](https://en.wikipedia.org/wiki/Parity_(mathematics))

## Author
SOWIZIE

## License
This project is licensed under the MIT License.
