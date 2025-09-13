from flask import Flask, render_template, request, redirect
import pymysql

app = Flask(__name__)

db = pymysql.connect(
    host='localhost',
    user='root',
    password='Aditya@2003',
    database='mydb'
)

@app.route('/', methods=['GET', 'POST'])
def home():
    cursor = db.cursor()
    message = None

    # ADD new record
    if request.method == 'POST' and 'add' in request.form:
        data = (
            request.form['ID'], request.form['Name'], request.form['Age'], request.form['Gender'],
            request.form['Mobile'], request.form['Weight'], request.form['Height'],
            request.form['Disease'], request.form['Treatment'], request.form['Amount_Paid']
        )
        try:
            cursor.execute("""
                INSERT INTO patients (ID, Name, Age, Gender, Mobile, Weight, Height, Disease, Treatment, Amount_Paid)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, data)
            db.commit()
            message = "Patient added successfully."
        except pymysql.err.IntegrityError:
            message = "ID already exists."

    # UPDATE existing record
    elif request.method == 'POST' and 'update' in request.form:
        updated = (
            request.form['Name'], request.form['Age'], request.form['Gender'], request.form['Mobile'],
            request.form['Weight'], request.form['Height'], request.form['Disease'],
            request.form['Treatment'], request.form['Amount_Paid'], request.form['ID']
        )
        cursor.execute("""
            UPDATE patients SET Name=%s, Age=%s, Gender=%s, Mobile=%s, Weight=%s, Height=%s,
            Disease=%s, Treatment=%s, Amount_Paid=%s WHERE ID=%s
        """, updated)
        db.commit()
        message = "Patient updated."

    # DELETE record
    elif request.method == 'POST' and 'delete' in request.form:
        pid = request.form['ID']
        cursor.execute("DELETE FROM patients WHERE ID = %s", (pid,))
        db.commit()
        message = "Patient deleted."

    # Fetch all rows to display
    cursor.execute("SELECT * FROM patients")
    rows = cursor.fetchall()
    cursor.close()
    return render_template("crud.html", rows=rows, message=message)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
