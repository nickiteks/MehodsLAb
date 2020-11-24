class Lab5:
    def work(self):
        pass
        ListofX = [0.259, 0.841, 1.562, 2.304, 2.856]
        ListofY = [0.018, -1.259, -1.748, -0.532, 0.911]
        x0 = float(input("Введите X0 "))
        KoficOfP = []
        tableRazn = [-2.194, 1.163, 0.206, -0.238]
        KoficOfP.append((1 / ((ListofX[0] - ListofX[1]) * (ListofX[0] - ListofX[2]) * (ListofX[0] - ListofX[3]) * (
                    ListofX[0] - ListofX[4]))) * ListofY[0])
        KoficOfP.append((1 / ((ListofX[1] - ListofX[0]) * (ListofX[1] - ListofX[2]) * (ListofX[1] - ListofX[3]) * (
                    ListofX[1] - ListofX[4]))) * ListofY[1])
        KoficOfP.append((1 / ((ListofX[2] - ListofX[0]) * (ListofX[2] - ListofX[1]) * (ListofX[2] - ListofX[3]) * (
                    ListofX[2] - ListofX[4]))) * ListofY[2])
        KoficOfP.append((1 / ((ListofX[3] - ListofX[0]) * (ListofX[3] - ListofX[1]) * (ListofX[3] - ListofX[2]) * (
                    ListofX[3] - ListofX[4]))) * ListofY[3])
        KoficOfP.append((1 / ((ListofX[4] - ListofX[0]) * (ListofX[4] - ListofX[1]) * (ListofX[4] - ListofX[2]) * (
                    ListofX[4] - ListofX[3]))) * ListofY[4])

        lx = KoficOfP[0] * (x0 - ListofX[1]) * (x0 - ListofX[2]) * (x0 - ListofX[3]) * (x0 - ListofX[4]) + \
             KoficOfP[1] * (x0 - ListofX[0]) * (x0 - ListofX[2]) * (x0 - ListofX[3]) * (x0 - ListofX[4]) + \
             KoficOfP[2] * (x0 - ListofX[0]) * (x0 - ListofX[1]) * (x0 - ListofX[3]) * (x0 - ListofX[4]) + \
             KoficOfP[3] * (x0 - ListofX[0]) * (x0 - ListofX[1]) * (x0 - ListofX[2]) * (x0 - ListofX[4]) + \
             KoficOfP[4] * (x0 - ListofX[0]) * (x0 - ListofX[1]) * (x0 - ListofX[2]) * (x0 - ListofX[3])

        print("___Лагранж :" + str(lx))
        lxFormul = f"{KoficOfP[0]}*(x - {ListofX[1]})*(x - {ListofX[2]})*(x - {ListofX[3]})*(x - {ListofX[4]})" + '\n' + \
                   f"{KoficOfP[1]}*(x - {ListofX[0]})*(x - {ListofX[2]})*(x - {ListofX[3]})*(x - {ListofX[4]})" + '\n' + \
                   f"{KoficOfP[2]}*(x - {ListofX[0]})*(x - {ListofX[1]})*(x - {ListofX[3]})*(x - {ListofX[4]})" + '\n' + \
                   f"{KoficOfP[3]}*(x - {ListofX[0]})*(x - {ListofX[1]})*(x - {ListofX[2]})*(x - {ListofX[4]})" + '\n' + \
                   f"{KoficOfP[4]}*(x - {ListofX[0]})*(x - {ListofX[1]})*(x - {ListofX[2]})*(x - {ListofX[3]})" + '\n'

        print("___Формула с коефициентами___ " + "\n" + str(lxFormul))

        Nx = ListofY[0] + tableRazn[0] * (x0 - ListofX[0]) + tableRazn[1] * (x0 - ListofX[0]) * (x0 - ListofX[1]) + \
             tableRazn[2] * (x0 - ListofX[0]) * (x0 - ListofX[1]) * (x0 - ListofX[2]) + \
             tableRazn[3] * (x0 - ListofX[0]) * (x0 - ListofX[1]) * (x0 - ListofX[2]) * (x0 - ListofX[3])

        print("___Ньютон:" + str(Nx))

        NxFormul = f"{ListofY[0]} + {tableRazn[0]} *(x - {ListofX[0]}) + {tableRazn[1]} * (x - {ListofX[0]}) * (x - {ListofX[1]}) + {tableRazn[2]} * (x - {ListofX[0]}) * (x - {ListofX[1]}) * (x - {ListofX[2]}) + {tableRazn[3]} * (x - {ListofX[0]}) * (x - {ListofX[1]}) * (x - {ListofX[2]}) * (x - {ListofX[3]})"

        print("___Формула с коефициентами___ " + "\n" + str(NxFormul) + "\n")

        # a1 = (ListofY[1] - ListofY[0]) / (ListofX[1] - ListofX[0])
        # b1 = (ListofY[0] - a1 * ListofX[0])
        ListA = []
        ListB = []
        for i in range(4):
            ListA.append((ListofY[i + 1] - ListofY[i]) / (ListofX[i + 1] - ListofX[i]))
            ListB.append((ListofY[i] - ListA[i] * ListofX[i]))
        print(ListA)
        print(ListB)
        Splx = 0.00000001
        for i in range(4):
            if x0 >= ListofX[i] and x0 <= ListofX[i + 1]:
                Splx = ListA[i] * x0 + ListB[i]
        if (Splx != 0.00000001):
            print("Сплайн равен " + str(Splx))
            SplxFormul = f""" 
                                            {ListA[0]}x + {ListB[0]},  {ListofX[0]}<=x<={ListofX[1]}
                                   φ(x) =   {ListA[1]}x + {ListB[1]},  {ListofX[1]}<=x<={ListofX[2]}
                                            {ListA[2]}x + {ListB[2]},  {ListofX[2]}<=x<={ListofX[3]}  
                                            {ListA[3]}x + {ListB[3]},  {ListofX[3]}<=x<={ListofX[4]}
                        """
            print("Формула с коефициентами " + SplxFormul)
        else:
            print("X находиться за границами сплайна")

