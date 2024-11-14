# https://myaccount.google.com/u/1/lessscureapps ya no funciona desde 2025
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

plantilla = Path("modulos_nativos/plantilla.html").read_text("utf-8")
# plantilla = """
#     <b>Jelou $usuario</b>
# """
template = Template(plantilla)
# cuerpo = template.substitute({"usurio": "Caco"})
cuerpo = template.substitute(usurio="Caco")
path = Path("modulos_nativos/foto.png")
mime_image = MIMEImage(path.read_bytes())
mensaje = MIMEMultipart()
mensaje["from"] = "Hola Mundo"
mensaje["to"] = "diegoneira@gmail.com"
mensaje["subject"] = "Esta es una prueba"
cuerpo = MIMEText(cuerpo, "html")
mensaje.attach(cuerpo)
mensaje.attach(mime_image)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()

    smtp.login("diegoneira@gmail.com", "pass123")
    smtp.send_message(mensaje)
    print("mensaje enviado")
