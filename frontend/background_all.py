from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle

class MyApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        # Изменяем фон с помощью Canvas
        with self.layout.canvas.before:
            Color(0.2, 0.4, 0.6, 1)
            self.rect = Rectangle(size=self.layout.size, pos=self.layout.pos)

        # Обновляем фон при изменении размера окна
        self.layout.bind(size=self.update_rect, pos=self.update_rect)

        # Кнопка
        btn = Button(text="Поздороваться", size_hint=(None, None), size=(200, 100))
        self.layout.add_widget(btn)

        return self.layout

    def update_rect(self, instance, value):
        # Обновляем прямоугольник при изменении размера окна
        self.rect.size = instance.size
        self.rect.pos = instance.pos

if __name__ == "__main__":
    MyApp().run()
