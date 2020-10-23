import numpy as np
from flask import Flask, request, jsonify, render_template, redirect, flash
from flask_ngrok import run_with_ngrok

from summarize import generate_summary
from CAtax import CanadaTax
from SGtax import SGtax
from spam_detection import train_model

#Create the flask object
app = Flask(__name__)

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
      return render_template('summarize.html', summarized_text=output, original_text=message, TextA="Your summary", TextB="Original text" )
   else:
      return render_template('summarize.html')

@app.route('/taxcalc', methods=['POST', "GET"])
def taxcalc():
   selectedCountry = str(request.form.get('country'))
   if request.method=='POST':
      income=int(request.form['income'])
      output=0
      if selectedCountry=="Canada":
         output = CanadaTax(income)
      elif selectedCountry=="Singapore":
         output = SGtax(income)
      return render_template('tax.html',taxamount="Your Total tax" +" in "+selectedCountry +" is: ${:,.0f}".format(output), salary="Based on your income: ${:,.0f}".format(income), country=selectedCountry)
   else:
      return render_template('tax.html')

@app.route('/spam_detection', methods=['POST', "GET"])
def spam_detection():
   if request.method=='POST':
      message=request.form['email']
      output= train_model(message)
      return render_template('spam_detection.html', result=output)
   else:
      return render_template('spam_detection.html')

if __name__=="__main__":
   app.run()