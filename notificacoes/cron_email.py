# -*- coding: utf-8 -*-
#!/usr/bin/env python

from gerenciador_despesas.models import Boleto

from django_cron import CronJobBase, Schedule
from django.core.mail import send_mail

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from datetime import date


class EnviarEmail(CronJobBase):
    RUN_AT_TIMES = ['12:00']

    schedule = Schedule(run_at_times=RUN_AT_TIMES)

    code = 'notificacoes.enviar_email'

    def do(self):
        gm_connection = self.configurar_email()
        boletos = self.obter_dados()

        if boletos:
            self.enviar_email(
                self.montar_mensagem(boletos),
                gm_connection
            )

    def configurar_email(self):
        print 'Configurando...'
        gm = smtplib.SMTP("smtp.gmail.com", 587)
        gm.ehlo()
        gm.starttls()
        gm.ehlo()
        print 'Efetuando login...'
        gm.login("matheus.souza.fernandes@gmail.com", "peme1413")

        return gm

    def obter_dados(self):
        boletos = Boleto.objects.filter(
            vencimento=date.today(),
            pago=False
        )

        return boletos

    def montar_mensagem(self, boletos):

        header = """<center><p><h1>Nazário Construções</h1></p>
        <h>%s</h3></center><hr />
        """ % (date.strftime(date.today(), '%d/%m/%y'))

        introducao = """<p><h4>Boa tarde,<br>
        Os seguintes boletos vencem hoje:</h4></p><br>
        """

        mensagem = header + introducao

        for boleto in boletos:
            info_boleto = """<b>Despesa:</b> %s<br>
            <b>Valor:</b> %.2f<br>
            <b>Cod. de Barras:</b> %s<br>
            <a href="http://177.153.6.164/admin/gerenciador_despesas/boleto/%s">
            Marcar como Pago</a><br><hr/> """ % (boleto.despesa, boleto.valor, str(boleto.cod_barras), boleto.id)

            mensagem = mensagem + info_boleto

        return mensagem

    def enviar_email(self, mensagem, gm):
        mail = MIMEText(mensagem, 'html')
        mail["To"] = "matheus.souza.fernandes@gmail@gmail.com"
        mail["Subject"] = "VENCIMENTOS DE HOJE"
        # Envia o email.
        print 'Enviando email...'
        gm.sendmail("matheus.souza.fernandes@gmail.com",
                    "matheus.souza.fernandes@gmail.com", mail.as_string())
        gm.close()
