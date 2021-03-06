import math


class relax:
    def work(self):
        startTable = [[2.979, 0.427, 0.406, 0.348],
                      [0.273, 3.951, 0.217, 0.327],
                      [0.318, 0.197, 2.875, 0.166],
                      [0.219, 0.231, 0.187, 3.276]]
        self.solutionVector = [0.341, 0.844, 0.131, 0.381]

        listXes = []
        listRes = []
        for i in range(len(startTable)):
            de = startTable[i][i]
            for j in range(len(startTable[i])):
                startTable[i][j] = startTable[i][j] / -de
                startTable[i][j] = round(startTable[i][j], 4)
                print(startTable[i][j], end=" ")
                if j == len(startTable[i]) - 1:
                    self.solutionVector[i] = self.solutionVector[i] / -de
                    self.solutionVector[i] = round(self.solutionVector[i], 4)
                    print("| " + str(self.solutionVector[i]))
            print("\n")

        for i in range(len(startTable)):
            for j in range(len(startTable[i])):
                if startTable[i][j] == 1.0 or startTable[i][j] == -1.0:
                    startTable[i][j] = startTable[i][j] * self.solutionVector[i] * -1

        for i in range(len(startTable)):
            for j in range(len(startTable[i])):
                print(startTable[i][j], end=" ")
            print('\n')

        for i in range(len(startTable)):
            listXes.append([])
            # Начальное приближение подставленное в систему
        for i in range(len(self.solutionVector)):
            listRes.append([])
            listRes[i].append(self.solutionVector[i] * -1)
            iteration = 0
            trigger = True
        while trigger:
            max = math.fabs(listRes[0][iteration])
            maxIndex = 0
            for i in range(len(listRes)):
                if math.fabs(listRes[i][iteration]) > max:
                    max = math.fabs(listRes[i][iteration])
                    maxIndex = i

            # присваивание  иксу
            for i in range(len(listXes)):
                if i == maxIndex:
                    listXes[i].append(listRes[i][iteration])
                else:
                    listXes[i].append(0)

            for i in range(len(listRes)):
                listRes[i].append(0)

            for i in range(len(listRes)):
                if i == maxIndex:
                    listRes[i][iteration + 1] = 0
                else:
                    listRes[i][iteration + 1] = round(listRes[i][iteration] + startTable[i][maxIndex] * listXes[maxIndex][iteration], 4)

            # вывод таблиц
            for i in range(len(listXes)):
                for j in range(len(listXes[i])):
                    print('x' + str(i + 1) + '_' + str(j) + ' |\t' + str(listXes[i][j]) + ' \t||', end=" ")
                print("\n")

            for i in range(len(listRes)):
                for j in range(len(listRes[i])):
                    print('R' + str(i + 1) + '_' + str(j) + ' |\t' + str(listRes[i][j]) + ' \t||', end=" ")
                print("\n")

            check = 0
            for i in range(len(listRes)):
                if math.fabs(listRes[i][iteration]) <= 0.0001:
                    check = check + 1
            if check == len(listRes):
                maxIndex = 0
                for i in range(len(listRes)):
                    if math.fabs(listRes[i][iteration]) > max:
                        max = math.fabs(listRes[i][iteration])
                        maxIndex = i

                for i in range(len(listXes)):
                    if i == maxIndex:
                        listXes[i].append(listRes[i][iteration])
                    else:
                        listXes[i].append(0)
                trigger = False
            else:
                iteration = iteration + 1

        # вывод таблиц
        for i in range(len(listXes)):
            for j in range(len(listXes[i])):
                print('x' + str(i + 1) + '_' + str(j) + ' |\t' + str(listXes[i][j]) + ' \t||', end=" ")
            print("\n")

        for i in range(len(listRes)):
            for j in range(len(listRes[i])):
                print('R' + str(i + 1) + '_' + str(j) + ' \t|' + str(listRes[i][j]) + ' \t||', end=" ")
            print("\n")

        res = []
        for i in range(len(listXes)):
            sum = 0
            for j in range(len(listXes[i])):
                sum = sum + listXes[i][j]
                sum = round(sum,4)
            res.append(sum)

        print("\n")
        print(res)