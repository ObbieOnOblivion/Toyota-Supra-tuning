import random
import time
# import tkinter
import my_function_3


class ToyotaSupraInternals:

    """ anything thing that cant be tuned and the features of the car """

    DragCoefficient = .320
    CurbWeight = 3434
    """ drag Coefficient at 90 miles per hour"""
    DC90 = 66

    def __init__(self):
        self.turbo = 'PT8847'
        self.turbo_type = 'ball bearing'
        self.transmition = 'helical gear drive'  # did you mean transmission
        self.gear1_ratio = 3.55
        self.gear2_ratio = None
        self.gear3_ratio = None
        self.gear4_ratio = None
        self.gear5_ratio = None
        self.gear6_ratio = None
        self.dif_type = 'lsd'
        self.dif_ratio = 3.909
        self.engine_type = 'induction performance 2jz'
        self.tire_diameter = 20
        self.weight = 3599
        self.driver_weight = 179
        self.gutted_weight = 400

    def set_gear_ratio(self, gear, ratio):
        if gear == 1:
            self.gear1_ratio = ratio

        if gear == 2:
            self.gear2_ratio = ratio

        if gear == 3:
            self.gear3_ratio = ratio

        if gear == 4:
            self.gear4_ratio = ratio

        if gear == 5:
            self.gear5_ratio = ratio

        if gear == 6:
            self.gear6_ratio = ratio

    def gut_car(self):

        if self.weight:
            self.weight -= self.gutted_weight

    def apply_driver_weight(self):
        self.weight += self.driver_weight


Scotty = ToyotaSupraInternals()

Scotty.set_gear_ratio(1, 3.55)
Scotty.set_gear_ratio(2, 2.09)
Scotty.set_gear_ratio(3, 1.49)
Scotty.set_gear_ratio(4, 1.00)
Scotty.set_gear_ratio(5, .69)
Scotty.set_gear_ratio(6, .58)

# print(Scotty.gear1_ratio)
# print(Scotty.gear2_ratio)

""" i want to make a new class were i use ecu to add feul and increase timing"""


class ToyotaSupra(ToyotaSupraInternals):
    """would this be more apropriate for a static method"""

    @classmethod
    def reborn(cls):
        cls.RidoxKit = True

    def click(self):
        import tkinter as tk
        mane = tk.Tk()
        mane.geometry('300x300-170-50')
        mane.title('spring pressure')

        text1 = tk.Text(mane, relief='sunken')
        text1.delete(0.0, 6.6)
        text1.insert(0.0, self.spring_preasure)

        mane.mainloop()

    @staticmethod
    def what_we_do():
        import tkinter as tk
        mainwindow = tk.Tk()
        mainwindow.geometry('700x300-50-100')

        label1 = tk.Label(mainwindow, text='tyres')
        label2 = tk.Label(mainwindow, text='boost preasure')
        label3 = tk.Label(mainwindow, text='duty cycle')
        label4 = tk.Label(mainwindow, text='launch control')
        label5 = tk.Label(mainwindow, text='boost by gear')
        label6 = tk.Label(mainwindow, text='car details')

        # label1.config(relief= 'sunken')
        # label2.config(relief= 'raised')
        # label3.config(relief= 'sunken')
        # label4.config(relief= 'raised')
        # label5.config(relief= 'sunken')
        # label6.config(relief= 'raised')
        #
        label1.config(relief='groove')
        label2.config(relief='groove')
        label3.config(relief='groove')
        label4.config(relief='groove')
        label5.config(relief='groove')
        label6.config(relief='groove')

        label1.grid(column=0, row=0, sticky='nesw')
        label2.grid(column=1, row=0, sticky='nesw')
        label3.grid(column=2, row=0, sticky='nesw')
        label4.grid(column=3, row=0, sticky='nesw')
        label5.grid(column=4, row=0, sticky='nesw')
        label6.grid(column=5, row=0, sticky='nesw')

        mainwindow.columnconfigure(0, weight=4)
        mainwindow.columnconfigure(1, weight=4)
        mainwindow.columnconfigure(2, weight=4)
        mainwindow.columnconfigure(3, weight=4)
        mainwindow.columnconfigure(4, weight=4)
        mainwindow.columnconfigure(5, weight=4)

        mainwindow.rowconfigure(0, weight=4)

        mainwindow.mainloop()

    @staticmethod
    def use_screen():  # maybe add a new window for a login and that login class this class function

        def click18():
            my_function_3.click_18()

        def click17():
            my_function_3.click_17()

        def click16():
            my_function_3.click_16()

        def click15():
            my_function_3.click_15()

        def click14():
            my_function_3.click_14()

        def click13():
            my_function_3.click_13()

        def click12():
            my_function_3.click_12()

        def click11():
            my_function_3.click_11()

        def click10():
            my_function_3.click_10()

        def click9():
            my_function_3.click_9()

        def click8():
            my_function_3.click_8()

        def click7():
            my_function_3.click_7()

        def click6():
            my_function_3.click_6()

        def click5():
            my_function_3.click_5()  # having problems with the image

        def click4():
            my_function_3.click_4()

        def click3():

            my_function_3.click_3()

        def click2():
            my_function_3.click_2()

        def click1():  # we could reuse other functions to keep our code DRY and use replacement fields
            my_function_3.click_1()

        def click():
            my_function_3.click()

        def kill_switch():

            mainwindow.destroy()

        def jane():
            print(ToyotaSupraInternals.DC90)

        import tkinter as tk
        mainwindow = tk.Tk()
        mainwindow.title("Toyota Supra Tune")
        mainwindow.geometry('700x300-50-100')
        mainwindow.configure(background='plum')

        label1 = tk.Label(mainwindow, text='tyres')
        label2 = tk.Label(mainwindow, text='boost pressure')
        label3 = tk.Label(mainwindow, text='duty cycle')
        label4 = tk.Label(mainwindow, text='launch control')
        label5 = tk.Label(mainwindow, text='gear info')
        label6 = tk.Label(mainwindow, text='car details')

        label1.config(relief='groove', bg='purple')
        label2.config(relief='groove', bg='purple')
        label3.config(relief='groove', bg='purple')
        label4.config(relief='groove', bg='purple')
        label5.config(relief='groove', bg='purple')
        label6.config(relief='groove', bg='purple')

        label1.grid(column=0, row=0, sticky='nesw')
        label2.grid(column=1, row=0, sticky='nesw')
        label3.grid(column=2, row=0, sticky='nesw')
        label4.grid(column=3, row=0, sticky='nesw')
        label5.grid(column=4, row=0, sticky='nesw')
        label6.grid(column=5, row=0, sticky='nesw')

        button1 = tk.Button(mainwindow, text="tyre pressures", fg='purple', command=click2)  # add command = for
        # all of these buttons
        button2 = tk.Button(mainwindow, text="tyre type", fg='purple', command=click1)
        button3 = tk.Button(mainwindow, text="spring pressure", fg='red', command=click)
        button4 = tk.Button(mainwindow, text="boost pressure", fg='red', command=click4)
        button5 = tk.Button(mainwindow, text="max boost psi", fg='red', command=click3)
        button6 = tk.Button(mainwindow, text="duty cycle", fg='yellow', comman=click6)
        button7 = tk.Button(mainwindow, text="two-step RPM", fg='orange', command=click7)
        button8 = tk.Button(mainwindow, text="gear1", fg='turquoise', command=click9)
        button9 = tk.Button(mainwindow, text="gear2", fg='turquoise', command=click10)
        button10 = tk.Button(mainwindow, text="gear3", fg='turquoise', command=click11)
        button11 = tk.Button(mainwindow, text="gear4", fg='turquoise', command=click12)
        button12 = tk.Button(mainwindow, text="gear5", fg='turquoise', command=click13)
        button13 = tk.Button(mainwindow, text="gear6", fg='turquoise', command=click14)
        button14 = tk.Button(mainwindow, text="fuel information", fg='green', command=click8)
        button15 = tk.Button(mainwindow, text="differential", fg='green', command=click15)
        button16 = tk.Button(mainwindow, text="Engine", fg='green', command=click16)
        button17 = tk.Button(mainwindow, text='car image', fg='green', command=click5)
        button18 = tk.Button(mainwindow, text="kill", fg='blue', command=kill_switch)
        button19 = tk.Button(mainwindow, text='simulator', fg='magenta', command=click18)  # maroon aqua plum
        button20 = tk.Button(mainwindow, text='Dyno numbers', fg='crimson', command=click17)
        # crimson teal lavender magenta

        button1.grid(column=0, row=1, sticky='news')
        button2.grid(column=0, row=2, sticky='news')
        button4.grid(column=1, row=1, sticky='news')
        button3.grid(column=1, row=2, sticky='news')
        button5.grid(column=1, row=3, sticky='news')
        button6.grid(column=2, row=1, sticky='news')
        button7.grid(column=3, row=1, sticky='news')
        button8.grid(column=4, row=1, sticky='news')
        button9.grid(column=4, row=2, sticky='news')
        button10.grid(column=4, row=3, sticky='news')
        button11.grid(column=4, row=4, sticky='news')
        button12.grid(column=4, row=5, sticky='news')
        button13.grid(column=4, row=6, sticky='news')
        button14.grid(column=5, row=1, sticky='news')
        button15.grid(column=5, row=2, sticky='news')
        button16.grid(column=5, row=3, sticky='news')
        button17.grid(column=5, row=4, sticky='news')
        button18.grid(column=2, row=6, sticky='news')
        button19.grid(column=1, row=6, sticky='news')
        button20.grid(column=5, row=5, sticky='news')

        mainwindow.columnconfigure(0, weight=4)
        mainwindow.columnconfigure(1, weight=4)
        mainwindow.columnconfigure(2, weight=4)
        mainwindow.columnconfigure(3, weight=4)
        mainwindow.columnconfigure(4, weight=4)
        mainwindow.columnconfigure(5, weight=4)

        mainwindow.rowconfigure(0, weight=4)
        mainwindow.rowconfigure(1, weight=4)
        mainwindow.rowconfigure(2, weight=4)
        mainwindow.rowconfigure(3, weight=4)
        mainwindow.rowconfigure(4, weight=4)
        mainwindow.rowconfigure(5, weight=4)
        mainwindow.rowconfigure(6, weight=4)

        mainwindow.mainloop()

    tyre_pressure = 17

    def __init__(self):
        super(ToyotaSupra, self).__init__()
        # def super(ToyotaSupra, self).super()
        self.spring_preasure = 5
        self.boost_level = int(self.spring_preasure)
        self.dutycycle = 103
        self.fuel_pressure = 60
        self.timingdegrees = 0
        self.maxxboost = 55
        self.twosteprpm = 3900
        self.buust = {}
        self.tyre_type = "Drag Radials"
        self.fuel_type = "89 Octane"

    # use these functions to help assisgt the changing a variables in the window

    def maxboost(self, set_maxboost):
        if set_maxboost >= self.spring_preasure:
            self.maxxboost = set_maxboost

    def inc_timing(self, degrees_of_timing):
        if degrees_of_timing >= 16:
            print('you don\'t want your valves hitting your pistons ')
        else:
            self.timingdegrees = degrees_of_timing

    def inc_duty_cycle(self, duty):
        if 100 >= duty >= 80:
            self.dutycycle = duty

        else:
            print('duty cycle to low')

    def inc_boost(self, boost):
        if int(self.spring_preasure) <=  self.boost_level <= int(self.maxxboost):
            self.boost_level += boost

        else:
            self.boost_level = int(self.spring_preasure) + 1

    def change_fuel_type(self, fuel):

        fuel = str(fuel)
        fuel = fuel.strip(' ')

        fuel_list = ['93 Octane', 'c16', 'ignite red', '118 Octane', '89 Octane']

        while fuel in fuel_list:

            for i in range(0, 5):
                if fuel in fuel_list[i]:
                    self.fuel_type = fuel
                    break
            break


OBBIE = ToyotaSupra()

# if __name__ == '__main__':
#
#     OBBIE.use_screen()
#
#     print(OBBIE.boost_level)

