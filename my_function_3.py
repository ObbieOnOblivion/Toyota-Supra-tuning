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

        number = ((v3.OBBIE.boost_level * (v3.OBBIE.boost_level * .7)) * .63) * (v3.OBBIE.duty_cycle // 100)

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
            time101 = time101 * v3.OBBIE.tsd1.get(v3.OBBIE.two_step_RPM)['1']

        if 22 < v3.OBBIE.tyre_pressure <= 25:
            time101 = time101 * v3.OBBIE.tsd1.get(v3.OBBIE.two_step_RPM)['2']

        if 19 < v3.OBBIE.tyre_pressure <= 22:
            time101 = time101 * v3.OBBIE.tsd1.get(v3.OBBIE.two_step_RPM)['3']

        if 17 < v3.OBBIE.tyre_pressure <= 19:
            time101 = time101 * v3.OBBIE.tsd1.get(v3.OBBIE.two_step_RPM)['4']

        if v3.OBBIE.tyre_pressure == 17:
            time101 = time101 * v3.OBBIE.tsd1.get(v3.OBBIE.two_step_RPM)['5']

        if 15 <= v3.OBBIE.tyre_pressure < 17:
            time101 = time101 * v3.OBBIE.tsd1.get(v3.OBBIE.two_step_RPM)['6']

        if 12 <= v3.OBBIE.tyre_pressure < 15:
            time101 = time101 * v3.OBBIE.tsd1.get(v3.OBBIE.two_step_RPM)['7']

        if v3.OBBIE.tyre_pressure < 12:
            time101 = time101 * v3.OBBIE.tsd1.get(v3.OBBIE.two_step_RPM)['8']

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

        if v3.OBBIE.wheel_diameter > 28:
            time2 = time2 * 1.09

        if 25 < v3.OBBIE.wheel_diameter <= 28:
            time2 = time2 * 1.07

        if 22 < v3.OBBIE.wheel_diameter <= 25:
            time2 = time2 * 1.04

        if 20 < v3.OBBIE.wheel_diameter <= 22:
            time2 = time2 * .97

        if v3.OBBIE.wheel_diameter == 20:
            time2 = time2 * 1.03

        if 18 <= v3.OBBIE.wheel_diameter < 20:
            time2 = time2 * 1.04

        if 15 <= v3.OBBIE.wheel_diameter < 18:
            time2 = time2 * 1.09

        if v3.OBBIE.wheel_diameter < 15:
            time2 = time2 * 1.11

        return time2

    @staticmethod
    def get_eighth_time():
        number1 = float(HP.get_q_time())
        number2 = (number1 * 0.623816674) + .188614263

        v3.OBBIE.tsd_set1()

        if v3.OBBIE.tyre_pressure > 25:
            number2 = number2 * v3.OBBIE.tsd1.get(v3.OBBIE.two_step_RPM)['1']

        if 22 < v3.OBBIE.tyre_pressure <= 25:
            number2 = number2 * v3.OBBIE.tsd1.get(v3.OBBIE.two_step_RPM)['2']

        if 19 < v3.OBBIE.tyre_pressure <= 22:
            number2 = number2 * v3.OBBIE.tsd1.get(v3.OBBIE.two_step_RPM)['3']

        if 17 < v3.OBBIE.tyre_pressure <= 19:
            number2 = number2 * v3.OBBIE.tsd1.get(v3.OBBIE.two_step_RPM)['4']

        if v3.OBBIE.tyre_pressure == 17:
            number2 = number2 * v3.OBBIE.tsd1.get(v3.OBBIE.two_step_RPM)['5']

        if 15 <= v3.OBBIE.tyre_pressure < 17:
            number2 = number2 * v3.OBBIE.tsd1.get(v3.OBBIE.two_step_RPM)['6']

        if 12 <= v3.OBBIE.tyre_pressure < 15:
            number2 = number2 * v3.OBBIE.tsd1.get(v3.OBBIE.two_step_RPM)['7']

        if v3.OBBIE.tyre_pressure < 12:
            number2 = number2 * v3.OBBIE.tsd1.get(v3.OBBIE.two_step_RPM)['8']

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
        main.destroy()

    import tkinter as tk
    main = tk.Tk()
    main.geometry('250x100-170-50')
    main.title('spring pressure')

    text1 = tk.Text(main)
    text1.delete(0.0, 6.6)
    text1.insert(0.0, f'{v3.OBBIE.spring_pressure} pounds of boost')
    text1.configure(background='yellow', fg='green')

    text1.grid(column=0, row=0)

    button101 = tk.Button(main, text='terminate', command=close_click)
    button101.grid(column=0, row=1)

    main.columnconfigure(0, weight=6)
    main.columnconfigure(1, weight=6)

    main.rowconfigure(0, weight=6)

    main.mainloop()


def click_1():
    import tkinter as tk

    def close_click():
        main.destroy()

    main = tk.Tk()
    main.geometry('250x100-170-50')
    main.title('tyre type')

    text1 = tk.Text(main)
    text1.delete(0.0, 6.6)  # maybe don't delete and add
    text1.insert(0.0, f'{v3.OBBIE.tyre_type}')
    text1.configure(background='yellow', fg='green')

    text1.grid(column=0, row=0)

    button101 = tk.Button(main, text='terminate', command=close_click)
    button101.grid(column=0, row=1)

    main.columnconfigure(0, weight=6)
    main.columnconfigure(1, weight=6)

    main.rowconfigure(0, weight=6)

    main.mainloop()


def click_2():
    # make sure to enter a count so they know how much psi they have in their tires
    # maybe a text field to tell the count
    import tkinter as tk

    def close_click():
        main.destroy()

    main = tk.Tk()
    main.geometry('450x500-170-50')
    main.title('tyre pressure')
    main.configure(background='yellow', relief='groove', borderwidth=4)

    text1 = tk.Text(main, width=30)
    text1.delete(0.0, 6.6)
    text1.insert(0.0, f'your tyre pressures are {v3.OBBIE.tyre_pressure} psi')
    text1.insert(0.0, time.strftime("%Y-%b-%d (%A) \nTime: [%H:%M:%S]\n"))
    text1.insert(0.0, "As of : ")
    text1.configure(background='yellow', fg='green', relief='sunken', borderwidth=6)

    text1.grid(column=0, row=0)

    button101 = tk.Button(main, text='terminate', command=close_click)
    button101.grid(column=0, row=1)

    bell1 = tk.Label(main, text='increments by\n 1 psi\n|\n|\n|\n|\n|\n|\n \/ ')
    bell1.grid(column=1, row=0)

    main.columnconfigure(0, weight=16)
    main.columnconfigure(1, weight=16)

    main.rowconfigure(0, weight=16)
    main.rowconfigure(1, weight=16)
    main.rowconfigure(2, weight=16)

    def james():  # help needed here
        # ToyotaSupra.tyre_pressure = entry1
        # print(ToyotaSupra.tyre_pressure)
        if 10 <= v3.OBBIE.tyre_pressure <= 35:
            v3.OBBIE.tyre_pressure += 1

        else:
            v3.OBBIE.tyre_pressure = 10

    but1 = tk.Button(main, text='apply new pressure', command=james)
    but1.grid(column=1, row=1)

    main.mainloop()


def click_3():
    import tkinter as tk
    import time

    def close_click():
        main.destroy()

    main = tk.Tk()
    main.geometry('550x300-170-50')
    main.title('max boost')

    text1 = tk.Text(main)
    text1.delete(0.0, 6.6)
    text1.insert(0.0, f'your max boost is {v3.OBBIE.max_boost} psi')
    text1.insert(0.0, time.strftime("%Y-%b-%d (%A) \nTime: [%H:%M:%S]\n"))
    text1.insert(0.0, "As of : ")
    text1.configure(background='yellow', fg='green')

    text1.grid(column=0, row=0)

    button101 = tk.Button(main, text='terminate', command=close_click)
    button101.grid(column=0, row=1)

    main.columnconfigure(0, weight=99)

    main.rowconfigure(0, weight=6)
    main.rowconfigure(0, weight=6)

    main.mainloop()


def click_4():
    import tkinter as tk

    def close_click():
        main.destroy()

    main = tk.Tk()
    main.geometry('450x500-170-50')
    main.title('boost pressure')
    main.configure(background='yellow', relief='groove', borderwidth=4)

    text1 = tk.Text(main, width=35)
    text1.delete(0.0, 6.6)
    text1.insert(0.0, f'your boost pressures are {v3.OBBIE.boost_level} psi')
    text1.insert(0.0, time.strftime("%Y-%b-%d (%A) \nTime: [%H:%M:%S]\n"))
    text1.insert(0.0, "As of : ")
    text1.configure(background='yellow', fg='green', relief='sunken', borderwidth=6)

    text1.grid(column=0, row=0)

    button101 = tk.Button(main, text='terminate', command=close_click)
    button101.grid(column=0, row=1)

    bell1 = tk.Label(main, text='increments by\n 1 psi\n|\n|\n|\n|\n|\n|\n \/ ')
    bell1.grid(column=1, row=0)

    main.columnconfigure(0, weight=16)
    main.columnconfigure(1, weight=16)

    main.rowconfigure(0, weight=16)
    main.rowconfigure(1, weight=16)
    main.rowconfigure(2, weight=16)

    def james():  # help needed here
        v3.OBBIE.inc_boost(1)

    but1 = tk.Button(main, text='apply new pressure', command=james)
    but1.grid(column=1, row=1)

    main.mainloop()


def click_5():
    import tkinter as tk

    main = tk.Tk()
    main.geometry('450x500-170-50')
    main.title(' car image ')
    main.configure(background='yellow', relief='groove', borderwidth=4)

    # c = tk.PhotoImage(file='/Users/abdurahmanomoruyi/Downloads/1444829005_tumblr_lzf57inObn1qkhqozo1_500.gif')
    #
    bell1 = tk.Label(main, text="ERROR\nCAN'T FIND IMAGE")
    bell1.grid(column=0, row=0)

    main.columnconfigure(0, weight=16)

    main.rowconfigure(0, weight=16)


def click_6():
    import tkinter as tk

    def close_click():
        main.destroy()

    main = tk.Tk()
    main.geometry('250x100-170-50')
    main.title('duty cycle')

    text1 = tk.Text(main)
    text1.delete(0.0, 6.6)  # maybe dont delete and add
    text1.insert(0.0, f'{v3.OBBIE.duty_cycle}%')
    text1.configure(background='yellow', fg='green')

    text1.grid(column=0, row=0)

    button101 = tk.Button(main, text='terminate', command=close_click)
    button101.grid(column=0, row=1)

    main.columnconfigure(0, weight=6)
    main.columnconfigure(1, weight=6)

    main.rowconfigure(0, weight=6)

    main.mainloop()


def click_7():
    import time
    import tkinter as tk

    def close_click():
        main.destroy()

    main = tk.Tk()
    main.geometry('450x500-170-50')
    main.title('two-step RPM')
    main.configure(background='yellow', relief='groove', borderwidth=4)

    text1 = tk.Text(main, width=35)
    text1.delete(0.0, 6.6)
    text1.insert(0.0, f'two-step rpm set at {v3.OBBIE.two_step_RPM} rpm\'s')
    text1.insert(0.0, time.strftime("%Y-%b-%d (%A) \nTime: [%H:%M:%S]\n"))
    text1.insert(0.0, "As of : ")
    text1.configure(background='yellow', fg='green', relief='sunken', borderwidth=6)

    text1.grid(column=0, row=0)

    button101 = tk.Button(main, text='terminate', command=close_click)
    button101.grid(column=0, row=1)

    bell1 = tk.Label(main, text='increments by\n 100\n|\n|\n|\n|\n|\n|\n \/ ')
    bell1.grid(column=1, row=0)

    main.columnconfigure(0, weight=16)
    main.columnconfigure(1, weight=16)

    main.rowconfigure(0, weight=16)
    main.rowconfigure(1, weight=16)
    main.rowconfigure(2, weight=16)

    def james():  # help needed here
        # ToyotaSupra.tyre_pressure = entry1
        # print(ToyotaSupra.tyre_pressure)
        if 3500 <= v3.OBBIE.twosteprpm <= 4500:
            v3.OBBIE.twosteprpm += 100

        else:
            v3.OBBIE.twosteprpm = 3500

    but1 = tk.Button(main, text='apply new two-step RPM', command=james)
    but1.grid(column=1, row=1)

    main.mainloop()


def click_8():  # more advanced fuel set up
    def close_click():
        main.destroy()

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

    main = tk.Tk()
    main.geometry('350x200-170-50')
    main.title('Fuel Information')

    label1 = tk.Label(main, text='your fuel pressures:', fg='teal')  # i spelled fuel wrong
    label1.grid(column=0, row=0, sticky='sew')

    label2 = tk.Label(main, text=f'{v3.OBBIE.fuel_pressure} PSI', fg='teal')
    label2.grid(column=0, row=1, sticky='new')

    label3 = tk.Label(main, text='fuel types')
    label3.grid(column=1, row=0, sticky='new')

    frame = tk.Frame(main)
    frame.grid(column=1, row=0, rowspan=2)

    button1 = tk.Button(frame, text='93 Octane', fg='crimson', command=octane93)
    button2 = tk.Button(frame, text='118 Octane', fg='crimson', command=octane118)
    button3 = tk.Button(frame, text='c16', fg='crimson', command=c16)
    button4 = tk.Button(frame, text='ignite red', fg='crimson', command=ignite_red)
    button5 = tk.Button(frame, text='89 Octane', fg='crimson', command=octane89)
    button6 = tk.Button(main, text='Kill', fg='aqua', command=close_click)

    button1.grid(column=0, row=1)
    button2.grid(column=0, row=2)
    button3.grid(column=0, row=3)
    button4.grid(column=0, row=4)
    button5.grid(column=0, row=5)
    button6.grid(column=0, row=2)

    main.columnconfigure(0, weight=6)
    main.columnconfigure(1, weight=6)

    main.rowconfigure(0, weight=6)
    main.rowconfigure(1, weight=6)
    main.rowconfigure(2, weight=6)

    main.mainloop()


def click_9():
    # if type(MANE) == int():
    #     MANE = str(MANE)

    def close_click():
        main.destroy()

    import tkinter as tk
    main = tk.Tk()
    main.geometry('250x100-170-50')
    main.title("gear 1 ratio")

    text1 = tk.Text(main)
    text1.delete(0.0, 6.6)
    text1.insert(0.0, f'gear 1 ratio is [{v3.Scotty.gear1_ratio}]')
    text1.configure(background='yellow', fg='green')

    text1.grid(column=0, row=0)

    button101 = tk.Button(main, text='terminate', command=close_click)
    button101.grid(column=0, row=1)

    main.columnconfigure(0, weight=6)
    main.columnconfigure(1, weight=6)

    main.rowconfigure(0, weight=6)

    main.mainloop()


def click_10():
    # if type(MANE) == int():
    #     MANE = str(MANE)

    def close_click():
        main.destroy()

    import tkinter as tk
    main = tk.Tk()
    main.geometry('250x100-170-50')
    main.title("gear 2 ratio")

    text1 = tk.Text(main)
    text1.delete(0.0, 6.6)
    text1.insert(0.0, f'gear 2 ratio is [{v3.Scotty.gear2_ratio}]')
    text1.configure(background='yellow', fg='green')

    text1.grid(column=0, row=0)

    button101 = tk.Button(main, text='terminate', command=close_click)
    button101.grid(column=0, row=1)

    main.columnconfigure(0, weight=6)
    main.columnconfigure(1, weight=6)

    main.rowconfigure(0, weight=6)

    main.mainloop()


def click_11():

    def close_click():
        main.destroy()

    import tkinter as tk
    main = tk.Tk()
    main.geometry('250x100-170-50')
    main.title("gear 3 ratio")

    text1 = tk.Text(main)
    text1.delete(0.0, 6.6)
    text1.insert(0.0, f'gear 3 ratio is [{v3.Scotty.gear3_ratio}]')
    text1.configure(background='yellow', fg='green')

    text1.grid(column=0, row=0)

    button101 = tk.Button(main, text='terminate', command=close_click)
    button101.grid(column=0, row=1)

    main.columnconfigure(0, weight=6)
    main.columnconfigure(1, weight=6)

    main.rowconfigure(0, weight=6)

    main.mainloop()


def click_12():

    def close_click():
        main.destroy()

    import tkinter as tk
    main = tk.Tk()
    main.geometry('250x100-170-50')
    main.title("gear 4 ratio")

    text1 = tk.Text(main)
    text1.delete(0.0, 6.6)
    text1.insert(0.0, f'gear 4 ratio is [{v3.Scotty.gear4_ratio}]')
    text1.configure(background='yellow', fg='green')

    text1.grid(column=0, row=0)

    button101 = tk.Button(main, text='terminate', command=close_click)
    button101.grid(column=0, row=1)

    main.columnconfigure(0, weight=6)
    main.columnconfigure(1, weight=6)

    main.rowconfigure(0, weight=6)

    main.mainloop()


def click_13():

    def close_click():
        main.destroy()

    import tkinter as tk
    main = tk.Tk()
    main.geometry('250x100-170-50')
    main.title("gear 5 ratio")

    text1 = tk.Text(main)
    text1.delete(0.0, 6.6)
    text1.insert(0.0, f'gear 5 ratio is [{v3.Scotty.gear5_ratio}]')
    text1.configure(background='yellow', fg='green')

    text1.grid(column=0, row=0)

    button101 = tk.Button(main, text='terminate', command=close_click)
    button101.grid(column=0, row=1)

    main.columnconfigure(0, weight=6)
    main.columnconfigure(1, weight=6)

    main.rowconfigure(0, weight=6)

    main.mainloop()


def click_14():
    def close_click():
        main.destroy()

    import tkinter as tk
    main = tk.Tk()
    main.geometry('250x100-170-50')
    main.title("gear 6 ratio")

    text1 = tk.Text(main)
    text1.delete(0.0, 6.6)
    text1.insert(0.0, f'gear 6 ratio is [{v3.Scotty.gear6_ratio}]')
    text1.configure(background='yellow', fg='green')

    text1.grid(column=0, row=0)

    button101 = tk.Button(main, text='terminate', command=close_click)
    button101.grid(column=0, row=1)

    main.columnconfigure(0, weight=6)
    main.columnconfigure(1, weight=6)

    main.rowconfigure(0, weight=6)

    main.mainloop()


def click_15():

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
        main.destroy()

    import tkinter as tk
    main = tk.Tk()
    main.geometry('250x100-170-50')
    main.title("engine")

    text1 = tk.Text(main)
    text1.delete(0.0, 6.6)
    text1.insert(0.0, f'engine type: \n[{v3.Scotty.engine_type}]')
    text1.configure(background='yellow', fg='green')

    text1.grid(column=0, row=0)

    button101 = tk.Button(main, text='terminate', command=close_click)
    button101.grid(column=0, row=1)

    main.columnconfigure(0, weight=6)
    main.columnconfigure(1, weight=6)

    main.rowconfigure(0, weight=6)

    main.mainloop()


def click_17():
    import tkinter

    main = tkinter.Tk()
    main.geometry('300x200-20-100')
    main.title('Dyno Sheet')

    lab1 = tkinter.Label(main, text='horse power numbers')
    lab1.grid(column=0, row=0)

    lab2 = tkinter.Label(main, text='torque numbers')
    lab2.grid(column=1, row=0)

    lab3 = tkinter.Label(main, text=f'{HP.get_number2()}')
    lab3.grid(column=0, row=1)

    lab4 = tkinter.Label(main, text=HP.get_torque_numbers())
    lab4.grid(column=1, row=1)

    main.rowconfigure(0)
    main.rowconfigure(1)

    main.columnconfigure(0)
    main.columnconfigure(1)

    main.mainloop()


def click_18():
    import tkinter
    main = tkinter.Tk()
    main.geometry("650x150-10-100")
    main.title('Times')

    label5 = tkinter.Label(main, text='eighth mile time')
    label5.grid(column=0, row=0, sticky='ews')

    label6 = tkinter.Label(main, text=HP.get_eighth_time())
    label6.grid(column=0, row=1, sticky='new')

    label1 = tkinter.Label(main, text='Quarter Mile Time')
    label1.grid(column=1, row=0, sticky='ews')

    label2 = tkinter.Label(main, text=HP.get_q_time())
    label2.grid(column=1, row=1, sticky='new')

    label3 = tkinter.Label(main, text='Half Mile Time')
    label3.grid(column=2, row=0, sticky='ews')

    label4 = tkinter.Label(main, text=HP.get_half_time())
    label4.grid(column=2, row=1, sticky='new')

    main.columnconfigure(0, weight=5)
    main.columnconfigure(1, weight=5)
    main.columnconfigure(2, weight=5)

    main.rowconfigure(0, weight=5)
    main.rowconfigure(1, weight=5)


def click_19():
    import tkinter
    main = tkinter.Tk()
    main.geometry('800x300-26-100')
    main.title('Extra info')

    def return_if_timing():
        """this function looks to see if the car has advanced timing or retarded timing """
        if 11 < v3.OBBIE.timing_degrees < 16:
            return "Advanced timing"
        if v3.OBBIE.timing_degrees <= 10:
            return "retarded timing"
        else:
            return "None"

    label1 = tkinter.Label(main, text='cars weight')
    label2 = tkinter.Label(main, text='tyre diameter')
    label3 = tkinter.Label(main, text='gutted weight')
    label4 = tkinter.Label(main, text='turbo information')
    label5 = tkinter.Label(main, text=f'{v3.Scotty.weight}')
    label6 = tkinter.Label(main, text=f'{v3.Scotty.wheel_diameter}')
    label7 = tkinter.Label(main, text=f'{v3.Scotty.gutted_weight}')
    label8 = tkinter.Label(main, text=f'{v3.Scotty.turbo}')
    label9 = tkinter.Label(main, text=f'Type:\n{v3.Scotty.turbo_type}')
    label10 = tkinter.Label(main, text='timing degrees')
    label11 = tkinter.Label(main, text=f'{return_if_timing()}')

    label1.grid(column=0, row=0)
    label2.grid(column=1, row=0)
    label3.grid(column=2, row=0)
    label4.grid(column=3, row=0)
    label5.grid(column=0, row=1)
    label6.grid(column=1, row=1)
    label7.grid(column=2, row=1)
    label8.grid(column=3, row=1)
    label9.grid(column=3, row=2)
    label10.grid(column=4, row=0)
    label11.grid(column=4, row=1)

    main.rowconfigure(0, weight=10)
    main.rowconfigure(1, weight=10)
    main.rowconfigure(2, weight=10)

    main.columnconfigure(0, weight=10)
    main.columnconfigure(1, weight=10)
    main.columnconfigure(2, weight=10)
    main.columnconfigure(3, weight=10)
    main.columnconfigure(4, weight=10)

    main.mainloop()


def click_20():
    import tkinter
    main = tkinter.Tk()
    main.title("gutting car ")
    main.geometry("200x200-100-100")

    button1 = tkinter.Button(main, text="gut car")
    button2 = tkinter.Button(main, text='original car weight')

    button1.grid(column=0, row=0, sticky='news')
    button2.grid(column=0, row=1, sticky='news')

    label1 = tkinter.Label(main, text="cars weight")
    label1.grid(column=0, row=2, sticky='news')

    label2 = tkinter.Label(main, text=f'{v3.Scotty.weight}')
    label2.grid(column=0, row=3, sticky='news')

    button1.configure(command=v3.Scotty.gut_car)
    button2.configure(command=v3.Scotty.apply_interior)

    main.rowconfigure(0, weight=10)
    main.rowconfigure(1, weight=10)
    main.rowconfigure(2, weight=10)
    main.rowconfigure(3, weight=10)

    main.mainloop()
