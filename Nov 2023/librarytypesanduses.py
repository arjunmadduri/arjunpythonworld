import random

x=random.randint(1,1000)
print(x)

#coinflip
import random

coin = ["Heads","Tails"]
heads_or_tails = random.choice(coin)
print(heads_or_tails)


#dicestuff
import random

dice = ["1","2","3","4","5","6"]
what_number = random.choice(dice)
print(what_number)

#dicestuff two, method two
dices = random.randint(1,6)
print(dices)