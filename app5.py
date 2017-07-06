

import os
from flask import Flask, render_template, redirect, url_for, escape, request
from datetime import datetime
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def new():
   return render_template('home.html')


@app.route('/enternew')
def new_entry():
   return render_template('entry.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      
         item = request.form['item']
         quant = request.form['quant']
      
         
         with sql.connect("mydatabase.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO grp (item,quant)VALUES (?,?)",(item,quant))
          
            con.commit()
            msg = "Record successfully added"
      
      
      
         return render_template("result.html",msg = msg)
         con.close()

@app.route('/list')
def list():
   con = sql.connect("mydatabase.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from grp")
   
   rows = cur.fetchall();
   return render_template("list.html",rows = rows)

   
if __name__ == "__main__":
   app.run(debug=True,host='0.0.0.0', port=1000)

    
