from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class mainApp(App):
    def build(self):
        self.operadores = ["/", "*", "+", "-"]
        self.ultimo_operador = None
        self.ultimo_botao = None
        
        # Criação do layout principal que sera usado para adicionar os outros widget depois 
        main_layout = BoxLayout(orientation="vertical")
        
        # widget do resultado
        self.solution=TextInput(multiline=False, readonly=True, halign="right", font_size=55) 
        main_layout.add_widget(self.solution) # Adiciona esse layout ao arquivo main_layout
        
        # widget dos botoes
        botoes = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]
        for linha in botoes:
            h_layout = BoxLayout() # Criamos um BoxLayout com orientação horizontal
            for label in linha:
                botao = Button(text=label, pos_hint={"center_x":0.5, "center_y":0.5})
                botao.bind(on_press=self.on_button_press) # Vinculamos a um manipulador de eventos 
                h_layout.add_widget(botao) # e adicionamos os botões à BoxLayout horizontal
                
            main_layout.add_widget(h_layout) # Adiciona esse layout ao arquivo main_layout
        
        # widget do botão de Igual '='   
        equals_button = Button(text="=", pos_hint={"center_x":0.5, "center_y":0.5})
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button) # Adiciona esse layout ao arquivo main_layout
        
        return main_layout
    
    def on_button_press(self, instance): #Recebe o argumento instance para que possa acessar qual widget chamou a função.
        '''Evento de clique do botão'''
        
        # extraem e armazenam o valor do solution e do botão text.
        current = self.solution.text
        button_text = instance.text
        
        #Verificação de qual botão foi pressionado
        if button_text == "C":
            #Limpará o widget solution
            self.solution.text = ""
        else: 
            if current and ( # verifica se solution possui algum valor pré-existente.
                self.ultimo_operador and button_text in self.operadores): # Verificam se o último botão pressionado foi um botão do operador.
                return
            elif current == "" and button_text in self.operadores: # Verificam se o primeiro caractere é um operador.
                # Primeiro caractere não pode ser um operador
                return
            else:
                new_text = current + button_text 
                self.solution.text = new_text
        
        self.ultimo_botao = button_text # Atribui a último_botão o ultimo botão pressionado
        self.ultimo_operador = self.ultimo_botao in self.operadores # é definida ultimo_operador como True ou False dependendo se era ou não um caractere de operador.
        

    def on_solution(self, instance):
        '''Transforma o texto e calcula com a função built-in eval()'''
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution # Define o resultado como o novo valor para o widget solution
        
            
if __name__ == '__main__': 
    app = mainApp()
    app.run()
            
            