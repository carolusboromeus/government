from flask import Flask, render_template, request, redirect, url_for
import pymysql.cursors, ctypes

app = Flask(__name__)

conn = cursor = None
#fungsi koneksi database
def openDb():
    global conn, cursor
    conn = pymysql.connect(host="localhost",user="root",password="",db="db_papua" )
    cursor = conn.cursor()

#fungsi untuk menutup koneksi
def closeDb():
    global conn, cursor
    cursor.close()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/maps')
def maps():
    return render_template('maps.html')

@app.route('/demography')
def demography():
    return render_template('demography.html')

@app.route('/culinary_tourism')
def culinary_tourism():
    return render_template('culinary_tourism.html')

@app.route('/historical_tourism')
def historical_tourism():
    return render_template('historical_tourism.html')

@app.route('/natural_tourism')
def natural_tourism():
    return render_template('natural_tourism.html')

@app.route('/government')
def government():
    return render_template('government.html')

@app.route('/population_service')
def population_service():
    return render_template('population_service.html')

@app.route('/healthcare_service')
def healthcare_service():
    return render_template('healthcare_service.html')

@app.route('/education_service')
def education_service():
    return render_template('education_service.html')

@app.route('/News 01')
def news01():
    return render_template('News 01.html')

@app.route('/News 02')
def news02():
    return render_template('News 02.html')

@app.route('/News 03')
def news03():
    return render_template('News 03.html')

@app.route('/form')
def form():
    return render_template('form.html')

#fungsi view tambah() untuk membuat form tambah
@app.route('/tambah', methods=['GET','POST'])
def tambah():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        openDb()
        sql = "INSERT INTO form (name, email, subject, message) VALUES (%s, %s, %s, %s)"
        val = (name, email, subject, message)
        cursor.execute(sql, val)
        conn.commit()
        closeDb()
        ctypes.windll.user32.MessageBoxW(0, "Pesan berhasil dikirim!! Kami akan hubungin secepatnya", "Berhasil!", 0)
        return redirect(url_for('form'))
    else:
        ctypes.windll.user32.MessageBoxW(0, "Pesan gagal dikirim!! Mohon di isi dengan benar!", "Gagal!", 0)
        return render_template('tambah.html')

if __name__ == '__main__':
    app.run(debug=True)