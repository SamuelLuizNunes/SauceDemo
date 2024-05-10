Feature: Selecionar Produto

    Scenario: Selecionar produto "Sauce Labs Backpack"
        Given que acesso o site Sauce Demo
        When preencho os campos de login com usuario standard_user e senha secret_sauce
        Then sou direcionado para pagina de Produtos

    Scenario: Login com a senha invalida
        Given que acesso o site Sauce Demo
        When preencho os campos de login com usuario standard_user e senha senha_invalida
        Then exibe a mensagem de erro no login

    Scenario Outline: Login Negativo
        Given que acesso o site Sauce Demo
        When preencho os campos de login com usuario <usuario> e senha <senha>
        Then exibe a <mensagem> de erro no login
        Exemples:
        | usuario       | senha          | mensagem                                                                  |
        | standard_user | senha_invalida | Epic sadface: Username and password do not match any user in this service |
        | standard_user |                | Epic sadface: Password is required                                        |
        |               | secret_sauce   | Epic sadface: Password is required                                        |
        | juca          | secret_sauce   | Epic sadface: Username and password do not match any user in this service |
        | juca          | senha_invalida | Epic sadface: Username and password do not match any user in this service |
        | juca          |                | Epic sadface: Password is required                                        |
        |               |                | Epic sadface: Password is required                                        |
        |               | senha_invalida | Epic sadface: Password is required                                        |