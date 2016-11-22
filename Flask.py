from flask import Flask, jsonify, request #import objects from the Flask model
app = Flask(__name__) #define app using Flask

languages = [{'name' : 'JavaScript'}, {'name' : 'Python'}, {'name' : 'Ruby'}]

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message' : 'It works!'})

@app.route('/lang', methods=['GET'])
def returnAll():
    return jsonify({'languages' : languages})


@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
    langs = [language for language in languages if language['name'] == name]
    return jsonify({'language' : langs[0]})

@app.route('/lang', methods=['POST'])
def addOne():
	#new dictionary is created with the 'key'=name and value='langauge specified'
    language = {'name' : request.json['name']}
    languages.append(language)
    return jsonify({'languages' : languages})

## pUT request to update data in your application
# Example replace Javascript by say Java


@app.route('/lang/', methods=['PUT'])
def editOne(name):
    langs = [language for language in languages if language['name'] == name]
    langs[0]['name'] = request.json['name']
    return jsonify({'language' : langs[0]})


if __name__ == '__main__':
    app.run(debug=True, port=8080) #run app on port 8080 in debug mode