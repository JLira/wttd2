# Eventex

Sistema de Eventos encomendado pela Morena.

## Como desenvolver?

1. Clone o repositório
2. Crie um virtualenv com Python 3.10
3. Ative o virtualenv
4. Instale as dependências
5. Execute os testes

```console
git clone git@github.com:jlira/wttd2.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?
1. Crie uma instância no seu provedor
2. Envie as configurações para o provedor
3. Defina uma SECRET_KEY segura para a instância
4. Defina DEBUG=False
5. Configure o serviço de email
6. Envie o código para o provedor

```console 
Instalaçao exemplo no heroku

heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configuro o email
git push heroku master --force
```
proximo video #99