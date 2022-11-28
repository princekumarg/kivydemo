from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line
class Mainwidget(Widget):
    x=NumericProperty(0)
    y=NumericProperty(0)
    V_NB_LINES=7
    V_LINES_SPACING=0.1
    vertical_lines=[]
    def __init__(self, **kwargs):
        super(Mainwidget,self).__init__(**kwargs)
        #print("INIT W:"+ str(self.width) + "W:" + str(self.height))
        self.init_vertical_lines()
    def on_parent(self,widget,parent):
       # print("ON PARENT W:" + str(self.width) + "W:" + str(self.height))
       pass
    def on_size(self,*args):
       # print("ON SIZE W:"+ str(self.width)+"H:"+ str(self.height))
       # self.x=self.width/2
       # self.y=self.height*0.75
       self.update_vertical_lines()
       pass
    def on_x(self,widget,value):
        # print("PX:"+ str(value))
        pass
    def on_y(self,widget,value):
        # print("PY:"+ str(value))
        pass
    def init_vertical_lines(self):
        with self.canvas:
            Color(1,1,1)
            #self.line=Line(points=[100,0,100,0])
            for i in range(0,self.V_NB_LINES):
                self.vertical_lines.append(Line())
    def update_vertical_lines(self):
        central_line_x=int(self.width/2)
        spacing=self.V_LINES_SPACING*self.width
        offset=-int(self.V_NB_LINES/2)
        for i in range(0,self.V_NB_LINES):
            line_x=int(central_line_x+offset*spacing)
            self.vertical_lines[i].points=[line_x,0,line_x,self.height]
            offset+=1
        #self.line.points=[center_x,0,center_x,100]
class GalaxyApp(App):
    pass
GalaxyApp().run()