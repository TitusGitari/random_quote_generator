import json  		# To read our quotes.json file
import random		# To pick a random quote
import sys 			# To read CLI arguments 

# Function to load quotes from JSON file
def load_quotes():
	with open("quotes.json", "r") as file:
		return json.load(file)

# Function to get a random quote
def get_random_quote(quotes):
	return random.choice(quotes)

# Function to disply quote in HTML
def generate_html(quote):
	html_content = f"""
	<html>
	<head><title>Random Quote</title></head>
	<body style="font-family: Arial; text-adlign:center; margin-top:20%;">
		<h2>"{quote['quote']}"</h2>
		<p>- {quote['author']}</p>
	</body>
	</html>
	"""
	with open("index.html", "w") as file:
		file.write(html_content)
	print("HTML file generated: index.html")

# Main program logic
if __name__ == "__main__":
	quotes = load_quotes()
	random_quote = get_random_quote(quotes)

	# Check if '--html' flag was passed
	if len(sys.argv) > 1 and sys.argv[1] == "--html":
		generate_html(random_quote)
	else:
		print(f"\"{random_quote['quote']}\" - {random_quote['author']}")














