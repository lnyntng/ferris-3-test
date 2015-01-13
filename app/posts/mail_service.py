import ferris3
import logging
from ferris3 import mail


@ferris3.auto_service
class MailService(ferris3.Service):

    @ferris3.auto_method
    def send(self, request):
        mail.send('lnyntng@gmail.com', 'Prueba', 'Prueba contenido')
