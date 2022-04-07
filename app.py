from flask import Flask, render_template
import requests
app = Flask(__name__)


breeds_list = ['corgi', 'labrador', 'husky']
capitalized_breed_list = [ item.capitalize() for item in breeds_list]


@app.route('/')
def index():
  response = requests.get('https://dog.ceo/api/breeds/image/random').json()
  url = response['message']
  return render_template('index.html',url = url)


@app.route('/main')
def main():
  return render_template('main.html', list = capitalized_breed_list)


@app.route('/breed/<breed>', methods=['GET'])
def test(breed):
  breed = breed
  response = requests.get(f'https://dog.ceo/api/breed/{breed}/images/random').json()
  url = response['message']
  return render_template('detail.html', url = url)




if __name__ == '__main__':
  app.run(debug=True)