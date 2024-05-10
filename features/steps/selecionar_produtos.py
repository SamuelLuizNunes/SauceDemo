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

@when(u'preencho os campos de login com usuario {usuario} e senha {senha}')
def step_impl(context, usuario, senha):
    context.driver.find_element(By.ID, 'user-name').send_keys(usuario)
    context.driver.find_element(By.ID, 'password').send_keys(senha)
    context.driver.find_element(By.ID, 'login-button').click()

@then(u'sou direcionado para pagina de Produtos')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, '.title').text == 'Products'
    context.driver.quit()

@then(u'exibe a mensagem de erro no login')
def step_impl(context):
    mensagem = 'Epic sadface: Username and password do not match any user in this service'
    assert context.driver.find_element(By.CSS_SELECTOR, '[data-test="error"]').text == mensagem