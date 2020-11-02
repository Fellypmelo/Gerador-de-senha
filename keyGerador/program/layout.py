import random
import string
import PySimpleGUI as sg
import os


class PassGen:
    def __init__(self):
        # Layout
        sg.theme('Black')
        layout = [
            [sg.Text('Usuário', size=(10, 1)),
             sg.Input(key='usuario', size=(20, 1))],
            [sg.Text('Quantidade de caracteres'), sg.Combo(values=list(
                range(30)), key='total_chars', default_value=1, size=(3, 1))],
            [sg.Output(size=(32, 5))],
            [sg.Button('Gerar Senha')]
        ]
        # Declarar janela
        self.janela = sg.Window('Password Generator', layout)
    def Start(self):
        while True:
            event, valores = self.janela.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == 'Gerar Senha':
                newpass = self.genpass(valores)
                print(newpass)
                self.savepass(newpass, valores)

    def genpass(self, valores):
        char_list = string.digits + string.ascii_letters +'!@#$%¨&*'
        chars = random.choices(char_list, k=int(valores['total_chars']))
        new_pass = ''.join(chars)
        return new_pass

    def savepass(self, newpass, valores):
        with open('senhas.txt', 'a', newline='') as arquivo:
            arquivo.write(
                f"usuario: {valores['usuario']} ==> nova senha:  {newpass}\n")
        print('Arquivo salvo')

        