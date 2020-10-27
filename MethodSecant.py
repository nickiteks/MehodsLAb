import math


class secant:
    def work(self):
        Eps = input("Введите e")
        x1 = input("Введите x1")
        x2 = input("Введите x2")
        Xes = [float(x1), float(x2)]
        FunctionValues = []
        Fx = 1.5 - 0.4 * math.sqrt(math.pow(Xes[0], 3)) - 0.5 * math.log(Xes[0])
        FunctionValues.append(Fx)
        FunctionValues.append(1.5 - 0.4 * math.sqrt(math.pow(Xes[1], 3)) - 0.5 * math.log(Xes[1]))
        iteration = 2
        trigger = True
        while trigger:
            Xes.append(
                Xes[iteration - 1] - ((FunctionValues[iteration - 1] * (Xes[iteration - 2] - Xes[iteration - 1]))
                                      /
                                      (FunctionValues[iteration - 2] - FunctionValues[iteration - 1])))
            FunctionValues.append(1.5 - 0.4 * math.sqrt(math.pow(Xes[iteration], 3)) - 0.5 * math.log(Xes[iteration]))
            if math.fabs(Xes[iteration] - Xes[iteration - 1]) < float(Eps):
                print("___________________" + str(math.fabs(Xes[iteration] - Xes[iteration - 1])))
                trigger = False
            iteration = iteration + 1
        for i in range(len(Xes)):
            print(str(Xes[i]) + '   ' + str(FunctionValues[i]))
            print('\n')
        num = abs(Eps.find('.') - len(Eps)) - 1
        Xes[len(Xes) - 1] = round(Xes[len(Xes) - 1], num)
        print("x = " + str(Xes[len(Xes) - 1]))
