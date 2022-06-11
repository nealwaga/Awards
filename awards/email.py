from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


#Create here
def send_welcome_email(receiver, name):
    #Creating message subject & sender
    subject = 'Welcome to The Awards!'
    sender = 'neal.waga@student.moringaschool.com'

    #Passing the context variables
    html_content = render_to_string ('email.siteemail.html', {'name':name})
    text_content = render_to_string ('email.siteemail.text', {'name':name})

    msg = EmailMultiAlternatives(subject, text_content, sender, [receiver])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()