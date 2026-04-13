from flask import Flask, render_template, jsonify
import sqlite3 

app = Flask(__name__)
DB = "Database/Nahrim_Database_final.db"

@app.route('/')
def home(): 
    return render_template('index.html')

@app.route('/map')
def map_page(): 
    return render_template('map.html')

@app.route('/data')
def data_page():
    return render_template('data.html')

@app.route('/hospitals')
def hostpitals():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("SELECT Hospital_Name, Address, Hospital_Type, Latitude, Longitude FROM Hospitals")
    rows = cursor.fetchall()
    conn.close()
    
    data = []
    for row in rows:
        data.append({
            'name': row[0],
            'address': row[1],
            'type': row[2],
            'lat': row[3],
            'lng': row[4]
        })
    return jsonify(data)


@app.route('/rainfall')
def rainfall():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
                   SELECT month, day, AVG(precipitation_mm)
                   FROM rainfall_Kedah_VISUALCROSSING
                   GROUP BY month, day
                   ORDER BY month, day """)
    kedah_data = cursor.fetchall()

    cursor.execute("""
                   SELECT month, day, AVG(precipitation_mm)
                   FROM rainfall_Selangor_VISUALCROSSING
                   GROUP BY month, day
                   ORDER BY month, day """)
    
    selangor_data = cursor.fetchall()
    conn.close()

    return jsonify({
        'kedah': [{'date': f"{row[0]:02d}-{row[1]:02d}", 'rainfall': row[2]} for row in kedah_data],
        'selangor': [{'date': f"{row[0]:02d}-{row[1]:02d}", 'rainfall': row[2]} for row in selangor_data]
    })    

@app.route('/rainfall/openmeteo')
def rainfall_openmeteo():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    
    cursor.execute(""" 
                    SELECT month, day, AVG(precipitation_mm)
                    FROM rainfall_Kedah_OPENMETEO
                    GROUP BY month, day 
                    ORDER BY month, day """)
    kedah_data = cursor.fetchall()

    cursor.execute("""
                SELECT month, day, AVG(precipitation_mm)
                FROM rainfall_Selangor_OPENMETEO
                GROUP BY month, day
                ORDER BY month, day """)                   
    selangor_data = cursor.fetchall()
    conn.close()

    return jsonify ({
    'kedah': [{'date': f"{row[0]:02d}-{row[1]:02d}", 'rainfall': row[2]} for row in kedah_data],
    'selangor': [{'date': f"{row[0]:02d}-{row[1]:02d}", 'rainfall': row[2]} for row in selangor_data]
    })

@app.route('/rainfall/nahrim')
def rainfall_nahrim():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    
    cursor.execute(""" 
                    SELECT Month, Day, AVG("Ave_RCP2.6"), AVG("Ave_RCP4.5"), AVG("Ave_RCP6.0"), AVG("Ave_RCP8.5")
                    FROM rainfall_Kedah_Nahrim
                    GROUP BY Month, Day 
                    ORDER BY Month, Day """)
    kedah_data = cursor.fetchall()
    cursor.execute("""
                    SELECT Month, Day, AVG("Ave_RCP2.6"), AVG("Ave_RCP4.5"), AVG("Ave_RCP6.0"), AVG("Ave_RCP8.5")
                    FROM rainfall_Selangor_Nahrim
                    GROUP BY Month, Day 
                    ORDER BY Month, Day """)                   
    selangor_data = cursor.fetchall()
    conn.close()
    return jsonify({
        'kedah': [{'date': f"{row[0]:02d}-{row[1]:02d}", 'rcp26': row[2], 'rcp45': row[3], 'rcp60':row[4], 'rcp85': row[5]} for row in kedah_data],
        'selangor': [{'date': f"{row[0]:02d}-{row[1]:02d}", 'rcp26': row[2], 'rcp45': row[3], 'rcp60':row[4], 'rcp85': row[5]} for row in selangor_data]
    })

if __name__ == '__main__':
    app.run(debug=True)