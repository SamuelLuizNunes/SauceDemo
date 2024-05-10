import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'que acesso o site Sauce Demo')
def step_impl(context):
    context.driver = webdriver.Chrome()    
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get('https://www.saucedemo.com')

# Preencher com usuario e senha
@when(u'preencho os campos de login com usuario {usuario} e senha {senha}')
def step_impl(context, usuario, senha):
    context.driver.find_element(By.ID, 'user-name').send_keys(usuario)
    context.driver.find_element(By.ID, 'password').send_keys(senha)
    context.driver.find_element(By.ID, 'login-button').click()

# Preencher com usuario em branco e senha
@when(u'preencho os campos de login com usuario  e senha {senha}')
def step_impl(context, senha):
    # não preenche o usuario
    context.driver.find_element(By.ID, 'password').send_keys(senha)
    context.driver.find_element(By.ID, 'login-button').click()

# Preencher com usuario, mas deixar a senha em branco
@when(u'preencho os campos de login com usuario {usuario} e senha ')
def step_impl(context, usuario):
    context.driver.find_element(By.ID, 'user-name').send_keys(usuario)
    # não preencho a senha
    context.driver.find_element(By.ID, 'login-button').click()

# Clica no botão de login sem preencher o usuário e senha
@when(u'preencho os campos de login com usuario  e senha ')
def step_impl(context):
    # não preencho usuário
    # não preencho a senha
    context.driver.find_element(By.ID, 'login-button').click()

@then(u'sou direcionado para pagina de Produtos')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, '.title').text == 'Products'
    context.driver.quit()

@then(u'exibe a mensagem de erro no login')
def step_impl(context):
    mensagem = 'Epic sadface: Username and password do not match any user in this service'
    assert context.driver.find_element(By.CSS_SELECTOR, '[data-test=error]').text == mensagem
    context.driver.quit()

# Verifica a mensagem para o cenário Outline
@then(u'exibe a {mensagem} de erro no login')
def step_impl(context, mensagem):
    assert context.driver.find_element(By.CSS_SELECTOR, '[data-test=error]').text == mensagem
    context.driver.quit()