from django.core.mail import send_mail
def sendMail(username,password,email):
            send_mail(
    "Credentails",
   f"username : {username} n Password : {password} don't share it with anyone",
     from_email= "ma_missoum@esi.dz",
     recipient_list=[email],
    fail_silently=False,
)