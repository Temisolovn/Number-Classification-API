from flask import Flask, jsonify, request
from flask_cors import CORS

# Initialize the Flask app
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Define a route for the root URL
@app.route('/')
def home():
    return "Welcome to the Number Classification API!"

# Import the requests library to fetch fun facts
import requests

# Define the number classification endpoint
@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    # Get the 'number' parameter from the query string
    number = request.args.get('number')

    # Validate the input
    if not number:
        return jsonify({"error": "Missing 'number' parameter"}), 400

    try:
        number = int(number)
    except ValueError:
        return jsonify({"number": number, "error": True}), 400

    # Calculate mathematical properties
    is_prime = check_prime(number)
    is_perfect = check_perfect(number)
    digit_sum = sum_digits(number)
    properties = determine_properties(number)

    # Fetch a fun fact from the Numbers API
    fun_fact = get_fun_fact(number)

    # Prepare the response
    response = {
        "number": number,
        "is_prime": is_prime,
        "is_perfect": is_perfect,
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact
    }

    return jsonify(response), 200

# Helper function to check if a number is prime
def check_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Helper function to check if a number is perfect
def check_perfect(n):
    if n < 2:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

# Helper function to calculate the sum of digits
def sum_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

# Helper function to determine properties (Armstrong, odd/even)
def determine_properties(n):
    properties = []
    if is_armstrong(n):
        properties.append("armstrong")
    if n % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
    return properties

# Helper function to check if a number is an Armstrong number
def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    num_digits = len(digits)
    return sum(d**num_digits for d in digits) == n

# Helper function to fetch a fun fact from the Numbers API
def get_fun_fact(n):
    url = f"http://numbersapi.com/{n}/math"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return "No fun fact available."

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
else:
    # This is required for Vercel to recognize the app
    application = app
