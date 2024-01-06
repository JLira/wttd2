from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r
class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Jobson Lira', cpf='12345678901',
                    email='contato@dianasimoes.com.br', phone='27-99911-2412')
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]   

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@dianasimoes.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@dianasimoes.com.br', 'contato@dianasimoes.com.br']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
            contents = [
              'Jobson Lira',
              '12345678901',
              'contato@dianasimoes.com.br', 
              '27-99911-2412',
            ]

            for content in contents:
               with self.subTest():
                self.assertIn(content, self.email.body)
