import pandas as pd
import qrcode

# Cargar datos de Excel
df = pd.read_excel("C:/Users/user/Downloads/PLANILLA RACKS.xlsx")

# Iterar a través de las filas del DataFrame
for index, row in df.iterrows():
    # Aquí deberías generar una URL única para cada fila, por ejemplo:
    data = f"http://127.0.0.1:5000/data/{index}"
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    
    # Guardar el código QR como imagen
    img.save(f'qr_{index}.png')

from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
@app.route('/')
def home():
    return 'Bienvenido a mi aplicación Flask!'
# Cargar los datos de Excel
df = pd.read_excel("C:/Users/user/Downloads/PLANILLA RACKS.xlsx")

@app.route('/data/<int:index>')
def show_data(index):
    # Obtener los datos de la fila correspondiente
    data = df.iloc[index].to_dict()
    # Renderizar una plantilla HTML pasando los datos de la fila
    return render_template('data_template.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
