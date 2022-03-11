# ddd-karen-arcoverde
DDD - Backend - Karen Arcoverde

Link: https://silver-motors-karen.herokuapp.com/
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
|Endpoint|Método|Descrição|
|-----|-----|-----|
|/login|POST|Usuario qualquer envia email e senha para fazer login e recebe seu token|
|/usuarios|GET|visualização de todos os usuários|
|/usuarios|POST|cadastro de novo usuário|
|/usuarios/<int:id>|GET|usuario logado pode ver suas informações, usando seu token|
|/files/put_url/formato|GET|para pegar o caminho do digital ocean|

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