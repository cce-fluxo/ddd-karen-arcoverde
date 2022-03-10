# ddd-karen-arcoverde
DDD - Backend - Karen Arcoverde

Link: https://dashboard.heroku.com/apps/ddd-miguel-garcia
***
## Índice

- [Modelo Entidade Relacionamento](#mer)
- [Rotas](#rotas)
- [Exemplos](#exemplos)

***
## MER

![diagrama silver motors novo](https://user-images.githubusercontent.com/59583521/154323914-9eb4e9cf-ee8a-46e8-8bbf-74b820d04d83.png)


***
## Rotas
|Endpoint|Metodo|Descrição|
|-----|-----|-----|
|/login|POST|Usuario qualquer envia email e senha para fazer login|
|/send_mail/reset|POST| caso tenha esquecido a senha, token enviado por email|
|/reset/<string:token>|PATCH|Usuario registrado envia nova senha|
|/medico/create|GET|visualização de todos os médicos|
|/medico/create|POST|cadastro de novo médico|
|/medico/details/<int:id>|GET|Medico logado pode ver suas informações|
|/medico/details/<int:id>|PUT|Medico logado pode alterar todas suas informações|
|/medico/details/<int:id>|PATCH|Medico logado pode alterar alguma de suas informações|
|/medico/details/<int:id>|DELETE|Medico logado pode deletar seu perfil|
|/paciente/create|GET|visualização de todos pacientes|
|/paciente/create|POST|cadastro de novo paciente|
|/paciente/details/<int:id>|GET|paciente logado pode ver suas informações|
|/paciente/details/<int:id>|PUT|paciente logado pode alterar todas suas informações|
|/paciente/details/<int:id>|PATCH|paciente logado pode alterar alguma de suas informações|
|/paciente/details/<int:id>|DELETE|paciente logado pode deletar seu perfil|
|/files/put_url/formato|GET|para pegar o caminho do digital ocean|
|/consulta|GET|para visualizar todas as consultas do sistema|
|/consulta|POST|Criar nova consulta com a data, hora, id do medico e do paciente|

***
## Exemplos

### POST /login
```
{
    "email": "karenarcoverde@gmail.com",
    "senha": "1234"
}
```
```
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyNzY3Mzk0MiwianRpIjoiYzczYjY0MzEtMjk4Ni00YTUxLWJhNDEtOGIwZjQwY2IxMGFmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjI3NjczOTQyLCJleHAiOjE2Mjc2NzQ4NDJ9.GS16yvd8gkkWjdhV09DDMtz9Qedd0rcQwJmjC1yNLq4"
}