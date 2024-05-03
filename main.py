# -*- coding: utf-8 -*-
from flask import Flask

app=Flask(__name__)

@app.route("/")
def Hola_mundo():
  return "Hola a todos"

if __name__=="__main__":
  app.run()
