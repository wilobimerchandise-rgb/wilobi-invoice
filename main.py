from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class WilobiInvoiceApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Wil-Obi Invoice'))
        layout.add_widget(Button(text='Create Invoice'))
        return layout
        
if __name__ == '__main__':
    WilobiInvoiceApp().run()
