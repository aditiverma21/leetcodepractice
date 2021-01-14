import flask
import logging # we can create a log file by importing the logging package
from flask import jsonify,request

nature=flask.Flask(__name__)
nature.config['DEBUG']=True

emp_list=[{"id":301, "name":"Aditi Verma"},{"id":401,"name":"Vidhya Verma"}]
matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
l=[[row[i] for row in matrix] for i in range(len(matrix[0]))]
logging.basicConfig(filename="vidhya.log", level=logging.DEBUG)

@nature.route('/api/resources/emp_list',methods=['GET'])
def function1():
    return jsonify(emp_list)
    
@nature.route('/l', methods=['GET'])    
def function2():
    return jsonify(l)

@nature.route('/api/emp_list', methods=['GET'])  
def function_id():
    
    if "id" in request.args:
        id = int(request.args["id"])
    else:
        logging.error("Id is not is provided")
        return ("Error: no id field provided.Please specify the id")
    
    result=[]    
    for emp in emp_list:
        if emp["id"]==id:
            logging.debug("Employee id %s", emp['id'])
            result.append(emp)
    
    return jsonify(result)
              
nature.run() 
