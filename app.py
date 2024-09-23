from flask import Flask, render_template
from db import init_db
from models import Empleado
import plotly.graph_objs as go
import plotly.io as pio

app = Flask(__name__)

session = init_db()

@app.route('/')
def dashboard():
    # Obtener datos de la base de datos
    empleados = session.query(Empleado).all()

    # Preparar datos para las gráficas
    edades = [emp.edad for emp in empleados]
    salarios = [emp.salario for emp in empleados]
    ciudades = [emp.ciudad for emp in empleados]
    ciudades_unicas = list(set(ciudades))

    # Gráfico de Barras: Relación Edad-Salario
    bar_data = go.Bar(x=edades, y=salarios, name="Edad vs Salario")
    bar_layout = go.Layout(title="Relación entre Edad y Salario", xaxis=dict(title="Edad"), yaxis=dict(title="Salario"))
    bar_fig = go.Figure(data=[bar_data], layout=bar_layout)
    bar_graph = pio.to_html(bar_fig, full_html=False)

    # Gráfico Circular: Cantidad de Personas por Ciudad
    ciudad_counts = [ciudades.count(ciudad) for ciudad in ciudades_unicas]
    pie_data = go.Pie(labels=ciudades_unicas, values=ciudad_counts)
    pie_layout = go.Layout(title="Cantidad de Personas por Ciudad")
    pie_fig = go.Figure(data=[pie_data], layout=pie_layout)
    pie_chart = pio.to_html(pie_fig, full_html=False)

    # Renderizar el template
    return render_template('dashboard.html', bar_graph=bar_graph, pie_chart=pie_chart, empleados=empleados)

if __name__ == '__main__':
    app.run(debug=True)
