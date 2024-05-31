import re
#Уточнялcя синтаксис регулярных выражений

def good_num(string: str) -> None:
    num_massive = []
    while re.search("[0-9]{2,4}\\\\[0-9]{2,5}", string):
        num_ind = list(re.search("[0-9]{2,4}\\\\[0-9]{2,5}", string).span())
        if (num_ind[1] - num_ind[0]) != 10: num_massive.append(string[num_ind[0]:num_ind[1]])
        string = string.replace(string[: string.index("\\", num_ind[0]) + 1], '', 1)
    for i in range(len(num_massive)):
        slash_num = num_massive[i].index('\\')
        if slash_num == 3:
            num_massive[i] = '0' + num_massive[i]
        elif slash_num == 2:
            num_massive[i] = '00' + num_massive[i]
        if len(num_massive[i]) == 7:
            num_massive[i] = num_massive[i][:5] + '000' + num_massive[i][5:]
        elif len(num_massive[i]) == 8:
            num_massive[i] = num_massive[i][:5] + '00' + num_massive[i][5:]
        elif len(num_massive[i]) == 9:
            num_massive[i] = num_massive[i][:5] + '0' + num_massive[i][5:]
        print(num_massive[i])