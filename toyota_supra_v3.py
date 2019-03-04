import random
import time
# import tkinter
import my_function_3


class ToyotaSupraInternals:
    """ anything thing that cant be tuned and the features of the car

    Attributes:
        turbo(str): The name of the turbo
        turbo_type(str): The type of the turbo
        transmission(str): this shows the general type of the transmission not the exact make or model
        gear1_ratio(float): this is the first gear ratio, or the trans ratio
        gear2_ratio(float): this is the second gear ratio.
        gear3_ratio(float): this is the third gear ratio.
        gear4_ratio(float): this is the forth gear ratio.
        gear5_ratio(float): this is the fifth gear ratio.
        gear6_ratio(float): this is the sixth gear ratio.
        dif_type(str): this shows if the differential is either opened or closed not the percentage locked or opened
        dif_ratio(float): this is the ratio for the differential
        engine_type(str): this is the engine type, in the first case it would be an inline 6
        wheel_diameter(int): this shows the diameter of the rear tyres
        weight(int): the weight of the car with the modifications
        driver_weight(int): this is the weight of the driver
        gutted_weight(int): this is the weight that you will lose if you gut the A/C and the interior
        """

    DragCoefficient = .320
    CurbWeight = 3434
    """ drag Coefficient at 90 miles per hour"""
    DC90 = 66

    def __init__(self):
        self.turbo = 'PT8847'
        self.turbo_type = 'ball bearing'
        self.transmission = 'helical gear drive'
        self.gear1_ratio = 3.55
        self.gear2_ratio = None
        self.gear3_ratio = None
        self.gear4_ratio = None
        self.gear5_ratio = None
        self.gear6_ratio = None
        self.dif_type = 'lsd'
        self.dif_ratio = 3.909
        self.engine_type = 'induction performance 2jz'
        self.wheel_diameter = 20
        self.weight = 3599
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
        """this method removes weight from the car"""

        if self.weight:
            self.weight -= self.gutted_weight


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
    """This class will be more concerning with the cars tune not as much the hardware of the car

    Attributes:
        spring_pressure(int): This is the minimum amount of boost you could to level with your spring
        boost_level(int): This is the psi your turbo charger is running
        duty_cycle(int): This hows at what percent work is the injectors doing for what its rated for
        fuel_pressure(int): This is the pressure of the fuel injectors
        timing_degrees(int): This is the amount of timing that is iin the car
        max_boost(int): This is the most amount of boost you could give this engine before a bearing spins or rod knock
        two_step_RPM(int): This is the RPM the two-step is set at
        tyre_type(str): this is the the type of tyre used on the rear wheels
        fuel_type(str): This shows the grade and type of fuel used
        tsd1(dict): This is a dictionary is for a range of two-step RPMs
    """

    def click(self):
        """opens the spring pressure window """
        import tkinter as tk
        mane = tk.Tk()
        mane.geometry('300x300-170-50')
        mane.title('spring pressure')

        text1 = tk.Text(mane, relief='sunken')
        text1.delete(0.0, 6.6)
        text1.insert(0.0, self.spring_pressure)

        mane.mainloop()

    @staticmethod
    def what_we_do():
        """this shows a general idea of what goes on in the use_screen method"""
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
        """this is the application itself """

        def click_19():
            my_function_3.click_19()

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

        def click3():  # add another window to change the max boost setting

            my_function_3.click_3()

        def click2():
            my_function_3.click_2()

        def click1():  # we could reuse other functions to keep our code DRY and use replacement fields
            my_function_3.click_1()

        def click():
            my_function_3.click()

        def kill_switch():
            mainwindow.destroy() 

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

        button1 = tk.Button(mainwindow, text="tyre pressures", fg='purple', command=click2)
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
        button21 = tk.Button(mainwindow, text='Other Details', fg="lavender", command=click_19)

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
        button21.grid(column=0, row=6, sticky='news')

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
        self.spring_pressure = 5
        self.boost_level = int(self.spring_pressure)
        self.duty_cycle = 103
        self.fuel_pressure = 90
        self.timing_degrees = 0
        self.max_boost = 55
        self.two_step_RPM = 3900
        self.tyre_type = "Drag Radials"
        self.fuel_type = "89 Octane"
        self.tsd1 = {}

    # use these functions to help assisgt the changing a variables in the window

    def maxboost(self, set_maxboost):
        """this sets the max boost pressure"""
        if set_maxboost >= self.spring_pressure:
            self.max_boost = set_maxboost

    def inc_timing(self, degrees_of_timing):
        """this adds timing degrees to the car"""
        if degrees_of_timing >= 16:
            print('you don\'t want your valves hitting your pistons ')
        else:
            self.timing_degrees = degrees_of_timing

    def inc_boost(self, boost):
        """this increases the boost pressures"""
        if int(self.spring_pressure) <=  self.boost_level <= int(self.max_boost):
            self.boost_level += boost

        else:
            self.boost_level = int(self.spring_pressure) + 1

    def change_fuel_type(self, fuel):
        """change the fuel type and the grade of the fuel"""

        fuel = str(fuel)
        fuel = fuel.strip(' ')

        fuel_list = ['93 Octane', 'c16', 'ignite red', '118 Octane', '89 Octane']

        while fuel in fuel_list:

            for i in range(0, 5):
                if fuel in fuel_list[i]:
                    self.fuel_type = fuel
                    break
            break

    def tsd_set1(self, number=None):
        """this sets the dictionary tsd1 indexes to dictionaries"""

        for i in range(4200, 4501, 100):
            dict1 = dict()
            dict1["1"] = 1.32  # above 25
            dict1["2"] = 1.17  # 22 - 25
            dict1["3"] = 1.11  # 19 - 22
            dict1["4"] = 1.05  # 17-19
            dict1["5"] = 1.00  # 17
            dict1["6"] = .98  # 15-17
            dict1["7"] = 1.04  # 12-15
            dict1["8"] = 1.14  # bellow 12

            self.tsd1[i] = dict1

        for i in range(4000, 4200, 100):
            dict2 = dict()
            dict2["1"] = 1.27  # above 25
            dict2["2"] = 1.15  # 22 - 25
            dict2["3"] = 1.10  # 19 - 22
            dict2["4"] = 1.04  # 17-19
            dict2["5"] = 1.03  # 17
            dict2["6"] = 1.01  # 15-17
            dict2["7"] = 1.07  # 12-15
            dict2["8"] = 1.24  # bellow 12

            self.tsd1[i] = dict2

        for i in range(3700, 4000, 100):
            dict3 = dict()
            dict3["1"] = 1.17  # above 25
            dict3["2"] = 1.09  # 22 - 25
            dict3["3"] = 1.02  # 19 - 22
            dict3["4"] = 1.009  # 17-19
            dict3["5"] = 1.07  # 17
            dict3["6"] = 1.11  # 15-17
            dict3["7"] = 1.21  # 12-15
            dict3["8"] = 1.34  # bellow 12

            self.tsd1[i] = dict3

        for i in range(3500, 3700, 100):
            dict4 = dict()
            dict4["1"] = 1.21  # above 25
            dict4["2"] = 1.17  # 22 - 25
            dict4["3"] = 1.11  # 19 - 22
            dict4["4"] = 1.09  # 17-19
            dict4["5"] = 1.03  # 17
            dict4["6"] = 1.11  # 15-17
            dict4["7"] = 1.27  # 12-15
            dict4["8"] = 1.44  # bellow 12

            self.tsd1[i] = dict4
    #
    # def tsd_set2(self, number=None):
    #     # this is for the eigth mile
    #
    #     for i in range(4200, 4501, 100):
    #         dict1 = dict()
    #         dict1["1"] = 1.32  # above 25
    #         dict1["2"] = 1.17  # 22 - 25
    #         dict1["3"] = 1.11  # 19 - 22
    #         dict1["4"] = 1.05  # 17-19
    #         dict1["5"] = 1.00  # 17
    #         dict1["6"] = .98  # 15-17
    #         dict1["7"] = 1.04  # 12-15
    #         dict1["8"] = 1.14  # bellow 12
    #
    #         self.tsd2[i] = dict1
    #
    #         # each other section for each two-step range
    #         # the subsection is for tyre pressures
    #
    #     # print(self.tsd1.items())
    #
    #     for i in range(4000, 4200, 100):
    #         dict2 = dict()
    #         dict2["1"] = 1.27  # above 25
    #         dict2["2"] = 1.15  # 22 - 25
    #         dict2["3"] = 1.10  # 19 - 22
    #         dict2["4"] = 1.04  # 17-19
    #         dict2["5"] = 1.03  # 17
    #         dict2["6"] = 1.01  # 15-17
    #         dict2["7"] = 1.07  # 12-15
    #         dict2["8"] = 1.24  # bellow 12
    #
    #         self.tsd2[i] = dict2
    #
    #     # print(self.tsd2.items())
    #
    #     for i in range(3700, 4000, 100):
    #         dict3 = dict()
    #         dict3["1"] = 1.17  # above 25
    #         dict3["2"] = 1.09  # 22 - 25
    #         dict3["3"] = 1.02  # 19 - 22
    #         dict3["4"] = 1.009  # 17-19
    #         dict3["5"] = 1.07  # 17
    #         dict3["6"] = 1.11  # 15-17
    #         dict3["7"] = 1.21  # 12-15
    #         dict3["8"] = 1.34  # bellow 12
    #
    #         self.tsd2[i] = dict3
    #
    #     for i in range(3500, 3700, 100):
    #         dict4 = dict()
    #         dict4["1"] = 1.21  # above 25
    #         dict4["2"] = 1.17  # 22 - 25
    #         dict4["3"] = 1.11  # 19 - 22
    #         dict4["4"] = 1.09  # 17-19
    #         dict4["5"] = 1.03  # 17
    #         dict4["6"] = 1.11  # 15-17
    #         dict4["7"] = 1.27  # 12-15
    #         dict4["8"] = 1.44  # bellow 12
    #
    #         self.tsd2[i] = dict4
    #
    #     # print(self.tsd2.items())


OBBIE = ToyotaSupra()



