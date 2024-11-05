from flask import Flask,request,jsonify

import  Products_dao
from sql_connection import  get_sql_connection
app=Flask(__name__)
connection=get_sql_connection()
@app.route('/getproducts',methods=['GET'])

def get_products():
    products=Products_dao.get_all_products(connection)
    response=jsonify(products)
    response.headers.add('Access-Control-Allow-Origin','*')

    return response

if __name__=="__main__":
    print("Strting python Flask Server For Grocery Store Management System")
    app.run(port=5000)