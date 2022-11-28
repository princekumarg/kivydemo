from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import StringProperty, BooleanProperty,Clock
from kivy.uix.gridlayout  import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.pagelayout import PageLayout
from kivy.metrics import dp
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line
from kivy.graphics.vertex_instructions import Rectangle,Ellipse
from kivy.uix.button import Button
from kivy.uix.widget import Widget
class CanvasExample(Widget):
    pass
class CanvasExample1(Widget):
    pass
class CanvasExample3(Widget):
    pass
class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100,100,400,500),width=2)
            Color(0,1,0)
            Line(circle=(400,200,80),width=2)
            Line(rectangle=(700,500,150,100),width=2)
            self.r=Rectangle(pos=(700,200),size=(150,100))
    def on_button_a_click(self):
        x,y=self.r.pos
        x+=dp(10)
        self.r.pos=(x,y)
class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size=dp(50)
        self.vx=dp(3)
        self.vy=dp(3)
        with self.canvas:
            self.ball=Ellipse(pos=self.center,size=(self.ball_size,self.ball_size))
        Clock.schedule_interval(self.update,0.2)
    def on_size(self,*args):
        self.ball.pos=(self.center_x-self.ball_size/2,self.center_y-self.ball_size/2)
    def update(self,dt):
        #print("update")
        x,y=self.ball.pos
        x+=self.vx
        y+=self.vy
        self.ball.pos=(x,y)
        if y+self.ball_size>self.height:
            y=self.height-self.ball_size
            self.vy=-self.vy
        if x+self.ball_size>self.width:
            x=self.width-self.ball_size
            self.vx=-self.vx
        if y<0:
            y=0
            self.vy=-self.vy
        if x<0:
            x=0
            self.vx=-self.vx
class CanvasExample6(Widget):
    pass
class WidgetsExample(GridLayout):
    count=1
    count_enabled=BooleanProperty(False)
    my_text=StringProperty("1")
    slider_value_txt=StringProperty("Value")
    text_input_str=StringProperty("Prince")
    def on_button_click(self):
        print("Button clicked")
        if self.count_enabled:
            self.count+=1
            self.my_text=str(self.count)
    def on_toggle_button_state(self,widget):
        print("toggle state:"+ widget.state)
        if widget.state=="normal":
            widget.text="OFF"
            self.count_enabled=False
        else:
            widget.text="ON"
            self.count_enabled=True
    def on_switch_active(self,widget):
        print("Switch" + str(widget.active))
    #def on_slider_value(self,widget):
        #print("Slider:"+ str(int(widget.value)))
        #self.slider_value_txt=str(int(widget.value))
    def on_text_validate(self,widget):
        self.text_input_str=widget.text
class ScrLayout(ScrollView):
    pass
class PgLayout(PageLayout):
    pass
class StckLayout(StackLayout):
   def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b=Button(text="Z",size_hint=(.5,.5))
        self.add_widget(b)
class GrdLayout(GridLayout):
    pass
class AnrLayout(AnchorLayout):
    pass
class BxLayout(BoxLayout):
    pass
class mainwidget(Widget):
    pass
class princeapp(App):
    pass
princeapp().run()