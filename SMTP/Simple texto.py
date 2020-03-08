import smtplib

Usuario = input("Tu hotmail: ")
Contra = input("Tu contraseña: ")
Asunto = input("Asunto: ")
Mensaje = input("Mensaje: ")
Destinatario = input("Hotmail del destinatario: ")

Mensaje = f"Subject: {Asunto}\n\n{Mensaje}"

Server = smtplib.SMTP('smtp-mail.outlook.com', 587)
Server.starttls()
Server.login(Usuario, Contra)

Server.sendmail(Usuario, Destinatario, Mensaje)
Server.quit()