import math


class secant:
    def work(self):
        Xes = [1, 2]
        FunctionValues = []
        Fx = 1.5 - 0.4 * math.sqrt(math.pow(Xes[0], 3) - 0.5 * math.log(Xes[0]))
        FunctionValues.append(Fx)
        FunctionValues.append(1.5 - 0.4 * math.sqrt(math.pow(Xes[1], 3) - 0.5 * math.log(Xes[1])))
        iteration = 2
        trigger = True
        while trigger:
            Xes.append(
                Xes[iteration - 1] - ((FunctionValues[iteration - 1] * (Xes[iteration - 2] - Xes[iteration - 1]))
                                      /
                                      (FunctionValues[iteration - 2] - FunctionValues[iteration - 1])))
            FunctionValues.append(1.5 - 0.4 * math.sqrt(math.pow(Xes[iteration], 3) - 0.5 * math.log(Xes[iteration])))
            if math.fabs(Xes[iteration] - Xes[iteration - 1]) < 0.000001:
                trigger = False
            iteration = iteration + 1
        print(Xes[len(Xes)-1])
        for i in range(len(Xes)):
            print(str(Xes[i])+ '   ' + str(FunctionValues[i]))
            print('\n')
