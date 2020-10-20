import numpy as np
from flask import Flask, request, jsonify, render_template, redirect, flash
from flask_ngrok import run_with_ngrok

from summarize import generate_summary
from tax import CanadaTax

#Create the flask object
app = Flask(__name__)
run_with_ngrok(app)

#create route
@app.route('/')
def home():
   return render_template('home.html')

@app.route('/summarize', methods=['POST', "GET"])
def summarize():
   selectedValue = request.form.get('numbers_of_lines')
   if request.method=='POST':
      message=request.form['message']
      output= generate_summary(message, top_n=int(selectedValue))
      # output= generate_summary(message, top_n=3)
      return render_template('index.html', summarized_text=output, original_text=message, TextA="Here's your summary", TextB="Original text" )
   else:
      return render_template('summarize.html')

@app.route('/taxcalc', methods=['POST', "GET"])
def taxcalc():
   if request.method=='POST':
      income=int(request.form['income'])
      output= CanadaTax(income)
      return render_template('tax.html',taxamount="Your Total tax is: ${:,.0f}".format(output), salary="Based on your income: ${:,.0f}".format(income))
   else:
      return render_template('tax.html')

if __name__=="__main__":
   app.run()