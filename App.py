from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivymd.theming import ThemeManager
from kivy.uix.screenmanager import Screen, ScreenManager

Window.size = (412, 767)

class ImageButton(ButtonBehavior, Image):
    pass

class HomeScreen(Screen):
    pass
class MenuScreen(Screen):
    pass
class DeskripsiScreen(Screen):
    pass
class CalculateScreen(Screen):
    pass
class ResultScreen(Screen):
    pass

class MainApp(MDApp):

    def build(self):
        theme_cls = ThemeManager()
        
        self.theme_cls.primary_palette = "LightGreen"
        self.theme_cls.accent_pallete = "LightGreen"
        self.theme_cls.theme_style = "Light"
        
        switch = ScreenManager()
        switch.add_widget(HomeScreen(name='home'))
        switch.add_widget(MenuScreen(name='menu'))
        switch.add_widget(MenuScreen(name='deskripsi'))
        switch.add_widget(MenuScreen(name='calculate'))
        switch.add_widget(MenuScreen(name='result'))
        return Builder.load_file('App.kv')
    
    def opsi(self, jumlahharta, anaklk, anakpr, varayah, varibu, varsuami, varistri, varcucu, varsla, varsli, varspa, varspi):
        harta = jumlahharta
        lk = anaklk
        pr = anakpr
        ayah = varayah
        ibu = varibu
        suami = varsuami
        istri = varistri
        cucu = varcucu
        sLa = varsla
        sLi = varsli
        spa = varspa
        spi = varspi    

    
MainApp().run()