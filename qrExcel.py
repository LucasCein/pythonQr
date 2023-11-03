import pandas as pd
import qrcode
from barcode import EAN13
from barcode.writer import ImageWriter
from pyzbar.pyzbar import decode
from PIL import Image

# Leer el archivo Excel
def leer_excel(ruta_archivo):
    df = pd.read_excel(ruta_archivo)
    return df

# Guardar los datos en un código QR
def guardar_datos_qr(datos, nombre_archivo):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(datos)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(f'{nombre_archivo}.png')

# Opcionalmente, guardar los datos en un código de barras (suponiendo que es un número válido para EAN13)
def guardar_datos_barcode(datos, nombre_archivo):
    ean = EAN13(datos, writer=ImageWriter())
    ean.save(nombre_archivo)

# Leer y mostrar datos desde un código QR
def leer_datos_qr(nombre_archivo):
    img = Image.open(nombre_archivo)
    resultados = decode(img)
    for resultado in resultados:
        print(resultado.data.decode('utf-8'))

# Uso de las funciones
ruta_excel = "C:/Users/user/Downloads/PLANILLA RACKS.xlsx"
 # Aquí pones la ruta a tu archivo Excel
df = leer_excel(ruta_excel)

# Recorriendo fila por fila y creando un QR por cada una
for index, row in df.iterrows():
    datos = row.to_json()  # Convertir los datos de la fila a JSON
    guardar_datos_qr(datos, f'qr_{index}')
    # Si tuvieras un EAN13 válido podrías usar también:
    # guardar_datos_barcode(str(row['tu_columna_ean']), f'barcode_{index}')

# Leer un código QR
nombre_archivo_qr = 'qr_0.png'  # Poner aquí el nombre del archivo que quieres leer
leer_datos_qr(nombre_archivo_qr)

