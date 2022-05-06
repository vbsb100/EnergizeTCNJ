#! /usr/bin/python3

import psycopg2
from config import config
from flask import Flask, render_template, request

# Connect to the PostgreSQL database server
def connect(query):
    conn = None
    try:
        # read connection parameters
        params = config()
 
        # connect to the PostgreSQL server
        print('Connecting to the %s database...' % (params['database']))
        conn = psycopg2.connect(**params)
        print('Connected.')
      
        # create a cursor
        cur = conn.cursor()
        
        # execute a query using fetchall()
        cur.execute(query)
        rows = cur.fetchall()

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
    # return the query result from fetchall()
    return rows
 
# app.py
app = Flask(__name__)


# serve form web page
@app.route("/")
def form():
    return render_template('index.html')

# handle venue POST and serve result web page
@app.route('/emissions', methods=['POST'])
def emissions():
    if not request.form['meter_name']:
        rows = connect('SELECT * FROM totalAvgEmissions WHERE meter_type = \'' + request.form['meterType'] + '\';')
    else:
        rows = connect('SELECT * FROM totalAvgEmissions WHERE meter_name = \'' + request.form['meter_name'] + '\';')
    heads = ['Meter Name', 'Meter Type', 'EstCO2Emission']
    return render_template('my-result.html', rows=rows, heads=heads)

@app.route('/TotalEmissions', methods=['POST'])
def TotalEmissions():
    if not request.form['meter_name']:
        rows = connect('SELECT * FROM totalEmissions WHERE units = \'' + request.form['units'] + '\';')
    else:
        rows = connect('SELECT * FROM totalEmissions WHERE meter_name = \'' + request.form['meter_name'] + '\';')
    heads = ['Meter Name', 'Total Emissions', 'Meter Type', 'Unit']
    return render_template('my-result.html', rows=rows, heads=heads)

@app.route('/TotalCost', methods=['POST'])
def TotalCost():
    if not request.form['meter_name']:
        rows = connect('SELECT * FROM totalCost ORDER BY ' + request.form['cost'] + ';')
    else:
        rows = connect('SELECT * FROM totalCost WHERE meter_name = \'' + request.form['meter_name'] + '\';')
    heads = ['Meter Name', 'Total Cost', 'Total Usage']
    return render_template('my-result.html', rows=rows, heads=heads)



if __name__ == '__main__':
    app.run(debug = True)
