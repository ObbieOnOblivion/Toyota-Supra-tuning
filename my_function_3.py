import toyota_supra_v3 as v3

import time


class HP:

    @staticmethod
    def get_number():

        hpp = 0
        if 'pt8' in v3.Scotty.turbo.lower():
            hpp += 1400

        if 'pt7' in v3.Scotty.turbo.lower():
            hpp += 1200

        while True:

            for i in ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']:
                if i in v3.Scotty.turbo[3]:
                    if 0 >= int(i) <= 5:
                        hpp += 50
                        break

                    else:
                        hpp += 75
                        break
                else:
                    hpp += 20
            break

        return hpp

    @staticmethod
    def get_number2():

        horsepower = 300

        number = ((v3.OBBIE.boost_level * (v3.OBBIE.boost_level * .7)) * .63) * (v3.OBBIE.dutycycle // 100)

        if v3.OBBIE.fuel_type == '89 Octane':
            number = number * .95

        if v3.OBBIE.fuel_type == '118 Octane':
            number = number * 1.03

        if v3.OBBIE.fuel_type == "93 Octane":
            number = number * .99

        if v3.OBBIE.fuel_type == 'ignite red':
            number = number * 1.06

        if v3.OBBIE.fuel_type == 'c16':
            number = number * 1.05

        # ended up at the same spot but the line was two steep
        # 1 pound of boost added like 100 hp which is not realistic

        # number = (toyota_supra_v2.OBBIE.boost_level * toyota_supra_v2.OBBIE.boost_level) * .43

        horsepower = horsepower + number

        return horsepower

    @staticmethod
    def get_q_time():

        time101 = 1517.00
        for i in range(0, int(HP.get_number2())):
            time101 -= .47

        time101 = time101 / 100

        time101 = float(time101)

        v3.OBBIE.tsd_set1()

        if v3.OBBIE.tyre_pressure > 25:
            time101 = time101 * v3.OBBIE.tsd1.get(v3.OBBIE.twosteprpm)['1']

        if 22 < v3.OBBIE.tyre_pressure <= 25:
            time101 = time101 * v3.OBBIE.tsd1.get(v3.OBBIE.twosteprpm)['2']

        if 19 < v3.OBBIE.tyre_pressure <= 22:
            time101 = time101 * v3.OBBIE.tsd1.get(v3.OBBIE.twosteprpm)['3']

        if 17 < v3.OBBIE.tyre_pressure <= 19:
            time101 = time101 * v3.OBBIE.tsd1.get(v3.OBBIE.twosteprpm)['4']

        if v3.OBBIE.tyre_pressure == 17:
            time101 = time101 * v3.OBBIE.tsd1.get(v3.OBBIE.twosteprpm)['5']

        if 15 <= v3.OBBIE.tyre_pressure < 17:
            time101 = time101 * v3.OBBIE.tsd1.get(v3.OBBIE.twosteprpm)['6']

        if 12 <= v3.OBBIE.tyre_pressure < 15:
            time101 = time101 * v3.OBBIE.tsd1.get(v3.OBBIE.twosteprpm)['7']

        if v3.OBBIE.tyre_pressure < 12:
            time101 = time101 * v3.OBBIE.tsd1.get(v3.OBBIE.twosteprpm)['8']

        time101 = str(time101)[0:6]

        return str(time101)

        # tyme = 1000.00
        # for i in range(0, HP.get_number()):
        #     tyme -= .09
        #
        # tyme = tyme / 100
        #
        # tyme = str(tyme)[0:5]
        #
        # return tyme

    @staticmethod
    def get_half_time():

        time1 = HP.get_q_time()
        time2 = float(time1) * 1.526135063

        return time2

    @staticmethod
    def get_eighth_time():
        import math
        number1 = float(HP.get_q_time())
        number2 = (number1 * 0.623816674) + .188614263

        v3.OBBIE.tsd_set1()

        if v3.OBBIE.tyre_pressure > 25:
            number2 = number2 * v3.OBBIE.tsd1.get(v3.OBBIE.twosteprpm)['1']

        if 22 < v3.OBBIE.tyre_pressure <= 25:
            number2 = number2 * v3.OBBIE.tsd1.get(v3.OBBIE.twosteprpm)['2']

        if 19 < v3.OBBIE.tyre_pressure <= 22:
            number2 = number2 * v3.OBBIE.tsd1.get(v3.OBBIE.twosteprpm)['3']

        if 17 < v3.OBBIE.tyre_pressure <= 19:
            number2 = number2 * v3.OBBIE.tsd1.get(v3.OBBIE.twosteprpm)['4']

        if v3.OBBIE.tyre_pressure == 17:
            number2 = number2 * v3.OBBIE.tsd1.get(v3.OBBIE.twosteprpm)['5']

        if 15 <= v3.OBBIE.tyre_pressure < 17:
            number2 = number2 * v3.OBBIE.tsd1.get(v3.OBBIE.twosteprpm)['6']

        if 12 <= v3.OBBIE.tyre_pressure < 15:
            number2 = number2 * v3.OBBIE.tsd1.get(v3.OBBIE.twosteprpm)['7']

        if v3.OBBIE.tyre_pressure < 12:
            number2 = number2 * v3.OBBIE.tsd1.get(v3.OBBIE.twosteprpm)['8']


        return number2

    @staticmethod
    def get_torque_numbers():

        k = HP.get_number2() * .89

        if v3.OBBIE.fuel_type == 'c16':
            k = k * 1.09

        k = str(k)

        return k


def click():
    def close_click():
        Mane.destroy()

    import tkinter as tk
    Mane = tk.Tk()
    Mane.geometry('250x100-170-50')
    Mane.title('spring pressure')

    text1 = tk.Text(Mane)
    text1.delete(0.0, 6.6)
    text1.insert(0.0, f'{v3.OBBIE.spring_preasure} pounds of boost')
    text1.configure(background='yellow', fg='green')

    text1.grid(column=0, row=0)

    button101 = tk.Button(Mane, text='terminate', command=close_click)
    button101.grid(column=0, row=1)

    Mane.columnconfigure(0, weight=6)
    Mane.columnconfigure(1, weight=6)

    Mane.rowconfigure(0, weight=6)

    Mane.mainloop()


def click_1():
    import tkinter as tk

    def close_click():
        Mane.destroy()

    Mane = tk.Tk()
    Mane.geometry('250x100-170-50')
    Mane.title('tyre type')

    text1 = tk.Text(Mane)
    text1.delete(0.0, 6.6)  # maybe dont delete and add
    text1.insert(0.0, f'{v3.OBBIE.tyre_type}')
    text1.configure(background='yellow', fg='green')

    text1.grid(column=0, row=0)

    button101 = tk.Button(Mane, text='terminate', command=close_click)
    button101.grid(column=0, row=1)

    Mane.columnconfigure(0, weight=6)
    Mane.columnconfigure(1, weight=6)

    Mane.rowconfigure(0, weight=6)

    Mane.mainloop()


def click_2():
    # make sure to enter a count so they know how much psi they have in their tires
    # maybe a text field to tell the count
    import tkinter as tk

    def close_click():
        Mane.destroy()

    Mane = tk.Tk()
    Mane.geometry('450x500-170-50')
    Mane.title('tyre pressure')
    Mane.configure(background='yellow', relief='groove', borderwidth=4)

    text1 = tk.Text(Mane, width=30)
    text1.delete(0.0, 6.6)
    text1.insert(0.0, f'your tyre pressures are {v3.OBBIE.tyre_pressure} psi')
    text1.insert(0.0, time.strftime("%Y-%b-%d (%A) \nTime: [%H:%M:%S]\n"))
    text1.insert(0.0, "As of : ")
    text1.configure(background='yellow', fg='green', relief='sunken', borderwidth=6)

    text1.grid(column=0, row=0)

    button101 = tk.Button(Mane, text='terminate', command=close_click)
    button101.grid(column=0, row=1)

    bell1 = tk.Label(Mane, text='increments by\n 1 psi\n|\n|\n|\n|\n|\n|\n \/ ')
    bell1.grid(column=1, row=0)

    Mane.columnconfigure(0, weight=16)
    Mane.columnconfigure(1, weight=16)

    Mane.rowconfigure(0, weight=16)
    Mane.rowconfigure(1, weight=16)
    Mane.rowconfigure(2, weight=16)

    def james():  # help needed here
        # ToyotaSupra.tyre_pressure = entry1
        # print(ToyotaSupra.tyre_pressure)
        if 10 <= v3.OBBIE.tyre_pressure <= 35:
            v3.OBBIE.tyre_pressure += 1

        else:
            v3.OBBIE.tyre_pressure = 10

    but1 = tk.Button(Mane, text='apply new pressure', command=james)
    but1.grid(column=1, row=1)

    Mane.mainloop()


def click_3():
    import tkinter as tk
    import time

    def close_click():
        Mane.destroy()

    Mane = tk.Tk()
    Mane.geometry('250x100-170-50')
    Mane.title('max boost')

    text1 = tk.Text(Mane)
    text1.delete(0.0, 6.6)
    text1.insert(0.0, f'your max boost is {v3.OBBIE.maxxboost} psi')
    text1.insert(0.0, time.strftime("%Y-%b-%d (%A) \nTime: [%H:%M:%S]\n"))
    text1.insert(0.0, "As of : ")
    text1.configure(background='yellow', fg='green')

    text1.grid(column=0, row=0)

    # c = tk.Checkbutton(mane, text='Make sure setting is safe ')

    button101 = tk.Button(Mane, text='terminate', command=close_click)
    button101.grid(column=0, row=1)

    Mane.columnconfigure(0, weight=6)
    Mane.columnconfigure(1, weight=6)

    Mane.rowconfigure(0, weight=6)

    Mane.mainloop()


def click_4():
    import tkinter as tk

    def close_click():
        Mane.destroy()

    Mane = tk.Tk()
    Mane.geometry('450x500-170-50')
    Mane.title('boost pressure')
    Mane.configure(background='yellow', relief='groove', borderwidth=4)

    text1 = tk.Text(Mane, width=35)
    text1.delete(0.0, 6.6)
    text1.insert(0.0, f'your boost pressures are {v3.OBBIE.boost_level} psi')
    text1.insert(0.0, time.strftime("%Y-%b-%d (%A) \nTime: [%H:%M:%S]\n"))
    text1.insert(0.0, "As of : ")
    text1.configure(background='yellow', fg='green', relief='sunken', borderwidth=6)

    text1.grid(column=0, row=0)

    button101 = tk.Button(Mane, text='terminate', command=close_click)
    button101.grid(column=0, row=1)

    bell1 = tk.Label(Mane, text='increments by\n 1 psi\n|\n|\n|\n|\n|\n|\n \/ ')
    bell1.grid(column=1, row=0)

    Mane.columnconfigure(0, weight=16)
    Mane.columnconfigure(1, weight=16)

    Mane.rowconfigure(0, weight=16)
    Mane.rowconfigure(1, weight=16)
    Mane.rowconfigure(2, weight=16)

    def james():  # help needed here
        v3.OBBIE.inc_boost(1)

    but1 = tk.Button(Mane, text='apply new pressure', command=james)
    but1.grid(column=1, row=1)

    Mane.mainloop()


def click_5():
    # import tkinter as tk
    #
    # def close_click():
    #     Mane.destroy()
    #
    # Mane = tk.Tk()
    # Mane.geometry('450x500-170-50')
    # Mane.title(' car image ')
    # Mane.configure(background='yellow', relief='groove', borderwidth=4)
    #
    # # c = tk.PhotoImage(file='/Users/abdurahmanomoruyi/Downloads/1444829005_tumblr_lzf57inObn1qkhqozo1_500.gif')
    # #
    # # bell1 = tk.Label(Mane, image=c)
    # # bell1.grid(column=0, row=0)
    #
    # Mane.columnconfigure(0, weight=16)
    #
    # Mane.rowconfigure(0, weight=16)
    return "sweet honey barbecue "


def click_6():
    import tkinter as tk

    def close_click():
        Mane.destroy()

    Mane = tk.Tk()
    Mane.geometry('250x100-170-50')
    Mane.title('duty cycle')

    text1 = tk.Text(Mane)
    text1.delete(0.0, 6.6)  # maybe dont delete and add
    text1.insert(0.0, f'{v3.OBBIE.dutycycle}%')
    text1.configure(background='yellow', fg='green')

    text1.grid(column=0, row=0)

    button101 = tk.Button(Mane, text='terminate', command=close_click)
    button101.grid(column=0, row=1)

    Mane.columnconfigure(0, weight=6)
    Mane.columnconfigure(1, weight=6)

    Mane.rowconfigure(0, weight=6)

    Mane.mainloop()


def click_7():
    import time
    import tkinter as tk

    def close_click():
        Mane.destroy()

    Mane = tk.Tk()
    Mane.geometry('450x500-170-50')
    Mane.title('two-step RPM')
    Mane.configure(background='yellow', relief='groove', borderwidth=4)

    text1 = tk.Text(Mane, width=35)
    text1.delete(0.0, 6.6)
    text1.insert(0.0, f'two-step rpm set at {v3.OBBIE.twosteprpm} rpm\'s')
    text1.insert(0.0, time.strftime("%Y-%b-%d (%A) \nTime: [%H:%M:%S]\n"))
    text1.insert(0.0, "As of : ")
    text1.configure(background='yellow', fg='green', relief='sunken', borderwidth=6)

    text1.grid(column=0, row=0)

    button101 = tk.Button(Mane, text='terminate', command=close_click)
    button101.grid(column=0, row=1)

    bell1 = tk.Label(Mane, text='increments by\n 100\n|\n|\n|\n|\n|\n|\n \/ ')
    bell1.grid(column=1, row=0)

    Mane.columnconfigure(0, weight=16)
    Mane.columnconfigure(1, weight=16)

    Mane.rowconfigure(0, weight=16)
    Mane.rowconfigure(1, weight=16)
    Mane.rowconfigure(2, weight=16)

    def james():  # help needed here
        # ToyotaSupra.tyre_pressure = entry1
        # print(ToyotaSupra.tyre_pressure)
        if 3500 <= v3.OBBIE.twosteprpm <= 4500:
            v3.OBBIE.twosteprpm += 100

        else:
            v3.OBBIE.twosteprpm = 3500

    but1 = tk.Button(Mane, text='apply new two-step RPM', command=james)
    but1.grid(column=1, row=1)

    Mane.mainloop()


def click_8(): # more advanced fuel set up
    def close_click():
        Mane.destroy()

    import tkinter as tk

    def octane93():
        v3.OBBIE.change_fuel_type('93 Octane')

    def octane118():
        v3.OBBIE.change_fuel_type('118 Octane')

    def c16():
        v3.OBBIE.change_fuel_type('c16')

    def ignite_red():
        v3.OBBIE.change_fuel_type('ignite red')

    def octane89():
        v3.OBBIE.change_fuel_type('89 Octane')

    Mane = tk.Tk()
    Mane.geometry('350x200-170-50')
    Mane.title('Fuel Information')

    Label1 = tk.Label(Mane, text='your fuel pressures:', fg='teal')  # i spelled fuel wrong
    Label1.grid(column=0, row=0, sticky='sew')

    Label2 = tk.Label(Mane, text=f'{v3.OBBIE.fuel_pressure} PSI', fg='teal')
    Label2.grid(column=0, row=1, sticky='new')

    Label3 = tk.Label(Mane, text='fuel types')
    Label3.grid(column=1, row=0)

    Frame = tk.Frame(Mane)
    Frame.grid(column=1, row=0, rowspan=2)

    button1 = tk.Button(Frame, text='93 Octane', fg='crimson', command=octane93)
    button2 = tk.Button(Frame, text='118 Octane', fg='crimson',command=octane118)
    button3 = tk.Button(Frame, text='c16', fg='crimson',command=c16)
    button4 = tk.Button(Frame, text='ignite red', fg='crimson', command=ignite_red)
    button5 = tk.Button(Frame, text='89 Octane', fg='crimson',command=octane89)

    button1.grid(column=0, row=1)
    button2.grid(column=0, row=2)
    button3.grid(column=0, row=3)
    button4.grid(column=0, row=4)
    button5.grid(column=0, row=5)

    Mane.columnconfigure(0, weight=6)
    Mane.columnconfigure(1, weight=6)

    Mane.rowconfigure(0, weight=6)
    Mane.rowconfigure(1, weight=6)


    Mane.mainloop()


def click_9():
    # if type(MANE) == int():
    #     MANE = str(MANE)

    def close_click():
        Mane.destroy()

    import tkinter as tk
    Mane = tk.Tk()
    Mane.geometry('250x100-170-50')
    Mane.title("gear 1 ratio")

    text1 = tk.Text(Mane)
    text1.delete(0.0, 6.6)
    text1.insert(0.0, f'gear 1 ratio is [{v3.Scotty.gear1_ratio}]')
    text1.configure(background='yellow', fg='green')

    text1.grid(column=0, row=0)

    button101 = tk.Button(Mane, text='terminate', command=close_click)
    button101.grid(column=0, row=1)

    Mane.columnconfigure(0, weight=6)
    Mane.columnconfigure(1, weight=6)

    Mane.rowconfigure(0, weight=6)

    Mane.mainloop()


def click_10():
    # if type(MANE) == int():
    #     MANE = str(MANE)

    def close_click():
        Mane.destroy()

    import tkinter as tk
    Mane = tk.Tk()
    Mane.geometry('250x100-170-50')
    Mane.title("gear 2 ratio")

    text1 = tk.Text(Mane)
    text1.delete(0.0, 6.6)
    text1.insert(0.0, f'gear 2 ratio is [{v3.Scotty.gear2_ratio}]')
    text1.configure(background='yellow', fg='green')

    text1.grid(column=0, row=0)

    button101 = tk.Button(Mane, text='terminate', command=close_click)
    button101.grid(column=0, row=1)

    Mane.columnconfigure(0, weight=6)
    Mane.columnconfigure(1, weight=6)

    Mane.rowconfigure(0, weight=6)

    Mane.mainloop()


def click_11():
    # if type(MANE) == int():
    #     MANE = str(MANE)

    def close_click():
        Mane.destroy()

    import tkinter as tk
    Mane = tk.Tk()
    Mane.geometry('250x100-170-50')
    Mane.title("gear 3 ratio")

    text1 = tk.Text(Mane)
    text1.delete(0.0, 6.6)
    text1.insert(0.0, f'gear 3 ratio is [{v3.Scotty.gear3_ratio}]')
    text1.configure(background='yellow', fg='green')

    text1.grid(column=0, row=0)

    button101 = tk.Button(Mane, text='terminate', command=close_click)
    button101.grid(column=0, row=1)

    Mane.columnconfigure(0, weight=6)
    Mane.columnconfigure(1, weight=6)

    Mane.rowconfigure(0, weight=6)

    Mane.mainloop()


def click_12():
    # if type(MANE) == int():
    #     MANE = str(MANE)

    def close_click():
        Mane.destroy()

    import tkinter as tk
    Mane = tk.Tk()
    Mane.geometry('250x100-170-50')
    Mane.title("gear 4 ratio")

    text1 = tk.Text(Mane)
    text1.delete(0.0, 6.6)
    text1.insert(0.0, f'gear 4 ratio is [{v3.Scotty.gear4_ratio}]')
    text1.configure(background='yellow', fg='green')

    text1.grid(column=0, row=0)

    button101 = tk.Button(Mane, text='terminate', command=close_click)
    button101.grid(column=0, row=1)

    Mane.columnconfigure(0, weight=6)
    Mane.columnconfigure(1, weight=6)

    Mane.rowconfigure(0, weight=6)

    Mane.mainloop()


def click_13():
    # if type(MANE) == int():
    #     MANE = str(MANE)

    def close_click():
        Mane.destroy()

    import tkinter as tk
    Mane = tk.Tk()
    Mane.geometry('250x100-170-50')
    Mane.title("gear 5 ratio")

    text1 = tk.Text(Mane)
    text1.delete(0.0, 6.6)
    text1.insert(0.0, f'gear 5 ratio is [{v3.Scotty.gear5_ratio}]')
    text1.configure(background='yellow', fg='green')

    text1.grid(column=0, row=0)

    button101 = tk.Button(Mane, text='terminate', command=close_click)
    button101.grid(column=0, row=1)

    Mane.columnconfigure(0, weight=6)
    Mane.columnconfigure(1, weight=6)

    Mane.rowconfigure(0, weight=6)

    Mane.mainloop()


def click_14():
    # if type(MANE) == int():
    #     MANE = str(MANE)

    def close_click():
        Mane.destroy()

    import tkinter as tk
    Mane = tk.Tk()
    Mane.geometry('250x100-170-50')
    Mane.title("gear 6 ratio")

    text1 = tk.Text(Mane)
    text1.delete(0.0, 6.6)
    text1.insert(0.0, f'gear 6 ratio is [{v3.Scotty.gear6_ratio}]')
    text1.configure(background='yellow', fg='green')

    text1.grid(column=0, row=0)

    button101 = tk.Button(Mane, text='terminate', command=close_click)
    button101.grid(column=0, row=1)

    Mane.columnconfigure(0, weight=6)
    Mane.columnconfigure(1, weight=6)

    Mane.rowconfigure(0, weight=6)

    Mane.mainloop()


def click_15():
    # if type(MANE) == int():
    #     MANE = str(MANE)

    def close_click():
        main.destroy()

    import tkinter as tk
    main = tk.Tk()
    main.geometry('250x100-170-50')
    main.title("differential")

    text1 = tk.Text(main)
    text1.delete(0.0, 6.6)
    text1.insert(0.0, f'differential type [{v3.Scotty.dif_type}]')
    text1.insert(0.0, f'differential ratio [{v3.Scotty.dif_ratio}]\n')
    text1.configure(background='yellow', fg='green')

    text1.grid(column=0, row=0)

    button101 = tk.Button(main, text='terminate', command=close_click)
    button101.grid(column=0, row=1)

    main.columnconfigure(0, weight=6)
    main.columnconfigure(1, weight=6)

    main.rowconfigure(0, weight=6)

    main.mainloop()


def click_16():
    # if type(MANE) == int():
    #     MANE = str(MANE)

    def close_click():
        mane.destroy()

    import tkinter as tk
    mane = tk.Tk()
    mane.geometry('250x100-170-50')
    mane.title("engine")

    text1 = tk.Text(mane)
    text1.delete(0.0, 6.6)
    text1.insert(0.0, f'engine type: \n[{v3.Scotty.engine_type}]')
    text1.configure(background='yellow', fg='green')

    text1.grid(column=0, row=0)

    button101 = tk.Button(mane, text='terminate', command=close_click)
    button101.grid(column=0, row=1)

    mane.columnconfigure(0, weight=6)
    mane.columnconfigure(1, weight=6)

    mane.rowconfigure(0, weight=6)

    mane.mainloop()


def click_17():
    import tkinter

    Main = tkinter.Tk()
    Main.geometry('300x200-20-100')
    Main.title('Dyno Sheet')

    lab1 = tkinter.Label(Main, text='horse power numbers')
    lab1.grid(column=0, row=0)

    lab2 = tkinter.Label(Main, text='torque numbers')
    lab2.grid(column=1, row=0)

    # text1 = tkinter.Text(Main, width=20)
    # text1.grid(column=0, row=1, sticky='news')
    #
    # text1.insert(0.0, f'{HP.get_number()}')
    #
    # text2 = tkinter.Text(Main, width=20)
    # text2.grid(column=1, row=1)
    #
    # text2.insert(0.0, f'{int(HP.get_number()) - 200}')

    lab3 = tkinter.Label(Main, text=f'{HP.get_number2()}')
    lab3.grid(column=0, row=1)

    lab4 = tkinter.Label(Main, text=HP.get_torque_numbers())
    lab4.grid(column=1, row=1)

    Main.rowconfigure(0)
    Main.rowconfigure(1)

    Main.columnconfigure(0)
    Main.columnconfigure(1)

    Main.mainloop()


def click_18():
    import tkinter
    Main = tkinter.Tk()
    Main.geometry("650x150-10-100")
    Main.title('Times')

    label5 = tkinter.Label(Main, text='eighth mile time')
    label5.grid(column=0, row=0, sticky='ews')

    label6 = tkinter.Label(Main, text=HP.get_eighth_time())
    label6.grid(column=0, row=1, sticky='new')

    label1 = tkinter.Label(Main, text='Quarter Mile Time')
    label1.grid(column=1, row=0, sticky='ews')

    label2 = tkinter.Label(Main, text=HP.get_q_time())
    label2.grid(column=1, row=1, sticky='new')

    label3 = tkinter.Label(Main, text='Half Mile Time')
    label3.grid(column=2, row=0, sticky='ews')

    label4 = tkinter.Label(Main, text=HP.get_half_time())
    label4.grid(column=2, row=1, sticky='new')

    Main.columnconfigure(0, weight=5)
    Main.columnconfigure(1, weight=5)
    Main.columnconfigure(2, weight=5)

    Main.rowconfigure(0, weight=5)
    Main.rowconfigure(1, weight=5)





