import math


class qiuck:
    def work(self):
        Eps = input("Введите e")
        x1 = input("Введите x1")
        x2 = input("Введите x2")
        Xes = [[float(x1)],[float(x2)]]
        alfa = 0.09
        Normas = [0]
        iteration = 1
        trigger = True
        while(trigger):
            Xes[0].append(Xes[0][iteration-1]-alfa*(2*(math.sin(Xes[0][iteration-1]-1)+Xes[1][iteration-1]-0.1)*(math.cos(Xes[0][iteration-1]-1))+2*(Xes[0][iteration-1]-math.sin(Xes[1][iteration-1]+1)-0.8)))
            Xes[1].append(Xes[1][iteration-1]-alfa*(2*(math.sin(Xes[0][iteration-1]-1)+Xes[1][iteration-1]-0.1)*1+2*(Xes[0][iteration-1]-math.sin(Xes[1][iteration-1]+1)-0.8)*(math.cos(Xes[1][iteration-1]+1))))
            #|xk - xk-1|
            raznX1 = math.fabs(Xes[0][iteration]-Xes[0][iteration-1])
            raznX2 = math.fabs(Xes[1][iteration]-Xes[1][iteration-1])
            if(raznX1>raznX2):
                Normas.append(raznX1)
            else:
                Normas.append(raznX2)
            if(Normas[len(Normas)-1] < float(Eps)):
                trigger = False

            iteration= iteration + 1

        #Вывод
        for i in range(len(Xes[0])):
            print("x1  " + str(Xes[0][i]) + "   " + "x2  " + str(Xes[1][i]) )

        num = abs(Eps.find('.') - len(Eps)) - 1
        Xes[0][len(Xes[0]) - 1] = round(Xes[0][len(Xes[0]) - 1], num)
        Xes[1][len(Xes[1]) - 1] = round(Xes[1][len(Xes[1]) - 1], num)
        print("x1 = " + str(Xes[0][len(Xes[0]) - 1]) + "   x2 = " + str(Xes[1][len(Xes[1]) - 1]))

        print(Normas[len(Normas)-1])
        print (iteration)