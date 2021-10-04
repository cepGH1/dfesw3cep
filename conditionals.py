devs_money = 100
dev_can_play_smash = False
if devs_money > 10 and dev_can_play_smash:
    print("Dev enters a smash tournament")
elif devs_money < 10 and dev_can_play_smash:
    print("Dev is too poor to enter")
else:
    print("Dev just can't play smash")

myMark = input("please enter your mark: ")
if int(myMark) > 85:
    print("distinction")
if int(myMark) >= 65 and int(myMark) < 86:
    print("pass")
else:
    print("fail")

myMark = input("please enter your mark: ")
if int(myMark) > 85:
    print("distinction")
elif int(myMark) >= 65 :
    print("pass")
else:
    print("fail")


