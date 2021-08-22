from app import api, web
from app.controllers import MyController, MyViewController, Controller_LatihanMVC

api.add_resource(MyController.MyController, '/')
api.add_resource(Controller_LatihanMVC.Controller_LatihanMVC_1, '/dua-parameter')
api.add_resource(Controller_LatihanMVC.Controller_LatihanMVC_2, '/operasi-aritmatika')

# Tambahkan route ini
web.add_resource(MyViewController.MyViewController, '/')
web.add_resource(MyViewController.MySecondViewController, '/say-my-name')
#web.add_resource(Controller_LatihanMVC.Controller_LatihanMVC, '/latihan_mvc')