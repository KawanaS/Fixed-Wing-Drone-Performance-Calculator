import kivy
from kivy.config import Config
Config.set('graphics','width','900')
Config.set('graphics','height','600')
from kivy.app import App
from kivy.uix.boxlayout import  BoxLayout
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
kivy.require('1.11.1')


class SampleBoxLayout(BoxLayout):
    pass


class CustomWidgetLayout(GridLayout):
    def calculate(self,airframe_weight,payload,battery_weight,total_voltage,efficiency,speed,lift_to_drag,S,Cdo,e,AR,density,Clmax,power_req,battery_capacity,energy_density,No_cells,No_batteries,battery_capacity_used,cell_voltage):
        total_weight=float(airframe_weight) + float(payload) + float(battery_weight)
        self.total_weight.text=str(total_weight)
        lift_coef=(9.8*total_weight)/(0.5*float(density)*(float(speed)*float(speed))*float(S))
        drag_coef=float(Cdo)+((float(lift_coef)*float(lift_coef))/(3.1415*float(e)*float(AR)))
        lift_to_drag=float(lift_coef)/float(drag_coef)
        lift_force=float(lift_coef)*(0.5)*float(density)*float(speed)*float(speed)*float(S)
        drag_force=float(drag_coef)*(0.5)*float(density)*float(speed)*float(speed)*float(S)
        stall_speed=(((2.0)/float(Clmax))**0.5)*(((float(total_weight)*9.8/float(S))/float(density))**0.5)
        max_endurance_speed=(1.333*(((float(total_weight)*9.8)/float(S))**2)*(1.0/(float(density)**2))*(1.0/float(Cdo))*(1.0/(3.1415*float(AR)*float(e))))**0.25
        max_range_speed=(4.0/(3.1415*float(AR)*float(e)*float(Cdo)))**0.25 *(((float(total_weight)*9.8)/float(S))/float(density))**0.5
        current=(((total_weight*9.8*float(speed))/float(lift_to_drag))/float(total_voltage))*(100/float(efficiency))
        flight_time=(((float(battery_capacity)/1000)*float(No_batteries)*float(battery_capacity_used)*0.01)/(float(current)+float(power_req)/float(total_voltage)))*60
        flight_range=(float(flight_time)*60.0*float(speed))/1000
        self.lift_coef.text=str(lift_coef)
        self.drag_coef.text=str(drag_coef)
        self.lift_to_drag.text=str(lift_to_drag)
        self.lift_force.text=str(lift_force)
        self.drag_force.text=str(drag_force)
        self.stall_speed.text=str(stall_speed)
        self.max_endurance_speed.text=str(max_endurance_speed)
        self.max_range_speed.text=str(max_range_speed)
        self.current.text = str(current)
        self.flight_time.text=str(flight_time)
        self.flight_range.text=str(flight_range)

class PerformanceApp(App):
    def build(self):
        Window.clearcolor=(1,1,1,1)
        return CustomWidgetLayout()

'''class PerformanceApp(App):
    def build(self):
        Window.clearcolor=(1,1,1,1)
        return SampleBoxLayout()'''

perfo_app=PerformanceApp()
perfo_app.run()
