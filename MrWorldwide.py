import argparse
import requests
import json
import time

# Create an argument parser
parser = argparse.ArgumentParser()
# Add arguments to the parser
parser.add_argument("--sourceLang")
parser.add_argument("--targetLang")
parser.add_argument("--sourceFile")
parser.add_argument("--targetFile")

# Parse the arguments
args = parser.parse_args()

# Make sure all the arguments are there
if args.sourceLang == None:
	print("ERROR: No source language specified.")
	exit()
if args.targetLang == None:
	print("ERROR: No target language specified.")
	exit()
if args.sourceFile == None:
	print("ERROR: No source file specified.")
	exit()
if args.targetFile == None:
	print("WARNING: No target file specified. Defaulting to 'output.json'.")
	args.targetFile = "output.json"

# Read input JSON and make it usable
startReadInputTime = time.time()
with open(args.sourceFile, 'r') as f:
	data = json.load(f)
	sourceFileKeys = data.keys()
	sourceFileValues = []
	for item in data:
		sourceFileValues.append(data[item])
print("Read input file time was " + str(time.time() - startReadInputTime) + " seconds.")

# Set query headers
headers = {
	'accept': 'application/json',
	'Content-Type': 'application/x-www-form-urlencoded',
}

# Really inefficient but it works ¯\_(ツ)_/¯
startQueryTime = time.time()
responseJSON = []
for item in sourceFileValues:
	# Set query data
	data = {
		'q': '"' + item + '"',
		'source': args.sourceLang,
		'target': args.targetLang
	}
	# Send the query and get the response
	response = requests.post('https://translate.astian.org/translate', headers=headers, data=data)
	responseData = json.loads(response.content.decode(response.encoding))["translatedText"]
	responseJSON.append(str(responseData).rstrip('"').replace('\u00ab', '').lstrip('"').replace('\u00bb', ''))

print("Query time was " + str(time.time() - startQueryTime) + " seconds.")

# Save the JSON data to file
with open(args.targetFile, 'w', encoding="UTF-8") as f:
	compiledDict = dict()
	responseJSONList = list(responseJSON)
	currentIteration = 0
	for item in sourceFileKeys:
		compiledDict.update({item: str(responseJSONList[currentIteration])})
		currentIteration = currentIteration + 1
	json.dump(compiledDict, f, separators=(',', ': '), indent="	", ensure_ascii=False)