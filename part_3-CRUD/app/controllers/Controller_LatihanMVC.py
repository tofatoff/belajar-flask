from flask_restful import Resource
from flask import render_template, make_response, request

class Controller_LatihanMVC_1(Resource):
    def get(self):
        x = request.args.get('x')
        y = request.args.get('y')

        if not x or not y: # Pengecekan kondisi apabila nama kosong, maka digantikan dengan default name yaitu Hudya
            view = render_template('view_latihanMVC_1_false.html')
        else:
            view = render_template('view_latihanMVC_1_true.html', x=x, y=y)

        
        return make_response(view)

class Controller_LatihanMVC_2(Resource):
    def get(self):
        method = request.args.get('method')
        first = request.args.get('first')
        second = request.args.get('second')

        if not method or not first or not second: # Pengecekan kondisi apabila nama kosong, maka digantikan dengan default name yaitu Hudya
            view = render_template('view_latihanMVC_1_false.html')
        else:
            first = float(first)
            second = float(second)
            if method == "sum":
                result = first + second
                method = "penjumlahan"
            elif method == "divide":
                result = first / second
                method = "pembagian"
            elif method == "sub":
                result = first - second
                method = "pengurangan"
            elif method == "multiply":
                result = first * second
                method = "perkalian"

            view = render_template('view_latihanMVC_2_success.html', method=method, result=result)

        
        return make_response(view)