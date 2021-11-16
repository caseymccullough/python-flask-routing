from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World!'

@app.route('/dojo')
def dojo():
   return "Dojo!"

@app.route('/say/<name>')
def say_hi(name):
   name = name.capitalize()
   return "Hi " + name

@app.route('/repeat/<times>/<word>')
def repeat(times, word):
   output = ""
   times = int(times)
   for i in range (times):
      output += "<br/>" + word
   print(output) 
   return output

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
   return "ERROR!!"
#     return app.send_static_file("index.html")

if __name__ == "__main__":
   app.run(debug=True)


