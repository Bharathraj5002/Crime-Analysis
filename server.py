from flask import Flask, request, jsonify
import util
import mapp
app = Flask(__name__)

@app.route('/get_state_names')
def get_state_names():
    response = jsonify({
        'state': util.get_state_names()
        })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/get_district_names')
def get_district_names():
    response = jsonify({
        'district': util.get_district_names()
        })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/get_output', methods=['POST'])
def get_output():
    crime = (request.form['crime'])
    state = (request.form['state'])
    district = (request.form['district'])
    year = int(request.form['year'])
    graph =  request.form.get('graph')
    response = jsonify({
        'estimated_count': util.get_output(crime,state, district, year, graph)
        })
    response.headers.add('Access-Control-Allow-Origin','*')
    
    return response


@app.route('/plot_map', methods=['POST'])
def plot_map():
    crime = request.form['crime']
    year = int(request.form['year'])
    mapp.plot_map(crime, year)



if __name__ == "__main__":
    app.run()

