
class Lab5 :
    def work(self):
        pass
        Xes = [0.259 ,0.841 ,1.562 ,2.304 ,2.856]
        Yes = [0.018 ,-1.259 ,-1.748 ,-0.532 ,0.911]
        x0 = float(input("Введите X0 "))
        Pkoof = []
        tableRazn = [-2.194 ,1.163 ,0.206 ,-0.238]
        # ...Лагранж
        Pkoof.append(( 1 /((Xes[0 ] -Xes[1] ) *(Xes[0 ] -Xes[2] ) *(Xes[0 ] -Xes[3] ) *(Xes[0 ] -Xes[4])) ) *Yes[0])
        Pkoof.append(( 1 /((Xes[1 ] -Xes[0] ) *(Xes[1 ] -Xes[2] ) *(Xes[1 ] -Xes[3] ) *(Xes[1 ] -Xes[4])) ) *Yes[1])
        Pkoof.append(( 1 /((Xes[2 ] -Xes[0] ) *(Xes[2 ] -Xes[1] ) *(Xes[2 ] -Xes[3] ) *(Xes[2 ] -Xes[4])) ) *Yes[2])
        Pkoof.append(( 1 /((Xes[3 ] -Xes[0] ) *(Xes[3 ] -Xes[1] ) *(Xes[3 ] -Xes[2] ) *(Xes[3 ] -Xes[4])) ) *Yes[3])
        Pkoof.append(( 1 /((Xes[4 ] -Xes[0] ) *(Xes[4 ] -Xes[1] ) *(Xes[4 ] -Xes[2] ) *(Xes[4 ] -Xes[3])) ) *Yes[4])

        lx = Pkoof[0 ] *(x0 - Xes[1] ) *(x0 - Xes[2] ) *(x0 - Xes[3] ) *(x0 - Xes[4])  +  \
             Pkoof[1 ] *(x0 - Xes[0] ) *(x0 - Xes[2] ) *(x0 - Xes[3] ) *(x0 - Xes[4])  +  \
             Pkoof[2 ] *(x0 - Xes[0] ) *(x0 - Xes[1] ) *(x0 - Xes[3] ) *(x0 - Xes[4])  +  \
             Pkoof[3 ] *(x0 - Xes[0] ) *(x0 - Xes[1] ) *(x0 - Xes[2] ) *(x0 - Xes[4])  +  \
             Pkoof[4 ] *(x0 - Xes[0] ) *(x0 - Xes[1] ) *(x0 - Xes[2] ) *(x0 - Xes[3])

        print("Полином Лагранжа равен "+ str(lx))
        lxFormul  = f"{Pkoof[0]}*(x0 - {Xes[1]})*(x0 - {Xes[2]})*(x0 - {Xes[3]})*(x0 - {Xes[4]})" + '\n' + \
                    f"{Pkoof[1]}*(x0 - {Xes[0]})*(x0 - {Xes[2]})*(x0 - {Xes[3]})*(x0 - {Xes[4]})" + '\n' + \
                    f"{Pkoof[2]}*(x0 - {Xes[0]})*(x0 - {Xes[1]})*(x0 - {Xes[3]})*(x0 - {Xes[4]})" + '\n' + \
                    f"{Pkoof[3]}*(x0 - {Xes[0]})*(x0 - {Xes[1]})*(x0 - {Xes[2]})*(x0 - {Xes[4]})" + '\n' + \
                    f"{Pkoof[4]}*(x0 - {Xes[0]})*(x0 - {Xes[1]})*(x0 - {Xes[2]})*(x0 - {Xes[3]})" + '\n'


        print("Формула с коефициентами " + "\n" + str(lxFormul))
        # ...Ньютон


        Nx = Yes[0] + tableRazn[0] *(x0 - Xes[0]) + tableRazn[1] * (x0 - Xes[0]) * (x0 - Xes[1]) + tableRazn[2] * (x0 - Xes[0]) * (x0 - Xes[1]) * (x0 - Xes[2]) + tableRazn[3] * (x0 - Xes[0]) * (x0 - Xes[1]) * (x0 - Xes[2]) * (x0 - Xes[3])

        print("Полином Ньютона равен "+ str(Nx))

        NxFormul = f"{Yes[0]} + {tableRazn[0]} *(x0 - {Xes[0]}) + {tableRazn[1]} * (x0 - {Xes[0]}) * (x0 - {Xes[1]}) + {tableRazn[2]} * (x0 - {Xes[0]}) * (x0 - {Xes[1]}) * (x0 - {Xes[2]}) + {tableRazn[3]} * (x0 - {Xes[0]}) * (x0 - {Xes[1]}) * (x0 - {Xes[2]}) * (x0 - {Xes[3]})"

        print("Формула с коефициентами " + "\n" + str(NxFormul) + "\n")

        #...Сплайн

        a1 = (Yes[1] - Yes[2])/(Xes[1]-Xes[2])
        b1 = (Yes[0] - a1 * Xes[0])
        Splx = a1 * x0 + b1

        print("Сплайн равен " + str(Splx))
        SplxFormul = f"({Yes[1]} - {Yes[2]})/({Xes[1]}-{Xes[2]}) * x0 + {Yes[0]} - ({Yes[1]} - {Yes[2]})/({Xes[1]}-{Xes[2]}) * {Xes[0]}"
        print("Формула с коефициентами " + SplxFormul)
