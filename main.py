import pandas as pd
from flask import Flask

app = Flask(__name__)

base = pd.read_excel("Paises.xlsx")

@app.route("/")
def principal():
    return "Esta es una API que muestra información sobre alumnos."


@app.route("/por_pais/<pais>")
def por_pais(pais):
    fila = base[base["Pais"] == pais]
    respuesta = f"El país  es {fila.loc[:, 'Pais']}"
    return respuesta



@app.route("/por_superficie/<superficie>")
def por_superficie(superficie):
    resultados = base[base["Superficie"] == superficie]
    superficie = int(superficie)
    resultados = str(resultados)
    return resultados


@app.route("/por_poblacion/<poblacion>")
def por_poblacion(poblacion):
    resultados = base[base["Población"] == poblacion]
    resultados = str(resultados)
    return resultados



if __name__ == "__main__":
    app.run()
