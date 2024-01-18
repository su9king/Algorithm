N = int(input())
Shortkey = [" "]
for i in range(N):

    string = input().split()
    option = 1
    index = 0

    while option != 3:

        if option == 1: #각 단어의 첫글자 확인


            if not(string[index][0].upper() in Shortkey):#단어의 첫글자로 가능하다면 단축키 바로 등록
                Shortkey.append(string[index][0].upper())
                string[index] = '[' + string[index][0:1] + ']' + string[index][1:]
                print(*string)
                option = 3

            elif index + 1 == len(string): # 모드 단어에 대해 option1 불가능 확인, 다음 옵션 ㄱ
                index = 0
                option = 2

            else: #해당 단어에 가능한 글자가 없음, 다음 단어로
                index += 1


        elif option == 2: #왼쪽에서부터 차례대로 글자 확인

            index_2 = 0
            for letter in string[index]:

                if not(letter.upper() in Shortkey): #왼쪽에서부터 차례대로 나온 단어중 가능하다면 단축키 바로 등록
                    Shortkey.append(letter.upper())
                    string[index] = string[index][0:index_2] + '[' + string[index][index_2:index_2+1] + ']' + string[index][index_2+1:]
                    print(*string)
                    option = 3
                    break

                elif index + 1 == len(string) and index_2 + 1 == len(string[index]) : #모든 단어에 대해 option 2도 불가능 확인, 그냥 출력
                    print(*string)
                    option = 3

                else: #해당 글자는 단축키 리스트에 있기에 다음 글자로
                    index_2 += 1
            #해당 단어에 가능한 글자가 없기에 다음 단어로
            index += 1











