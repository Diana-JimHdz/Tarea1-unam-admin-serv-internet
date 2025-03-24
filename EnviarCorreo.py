import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuración del servidor SMTP
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "beca.djh@gmail.com" # Correo emisor
sender_password = "ndqv onga aewq sczp" # Contraseña del correo emisor (contraseña para app menos segura de gmail)
receiver_email = "angel.brito@fi.unam.edu" # Correo destino

# Crear el mensaje
subject = "Prueba de envío de correo"
body = "Este es un correo de prueba enviado desde Python por Diana Jiménez Hernandez ."

# Crear un objeto MIMEMultipart para el mensaje
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Adjuntar el cuerpo del mensaje como texto plano
message.attach(MIMEText(body, "plain"))

# Enviar el correo
try:
    # Conectar al servidor SMTP
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Cifrar la conexión usando TLS (obligatorio para Gmail)
    server.login(sender_email, sender_password)  # Iniciar sesión en el servidor SMTP
    server.sendmail(sender_email, receiver_email, message.as_string())  # Enviar el correo
    print("Correo enviado exitosamente.")  # Mensaje de éxito
except Exception as e:
    print(f"Error al enviar el correo: {e}")  # Manejo de errores
finally:
    server.quit()  # Cerrar la conexión con el servidor SMTP