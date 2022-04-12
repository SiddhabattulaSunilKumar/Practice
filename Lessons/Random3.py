import random

rand_int = random.randint(2,7) #give random int
rand_float = random.random() #gives random float
rand_new = float(rand_int) #Converts Int to float
rand_newVal = rand_new+round(rand_float,2) # add random int and float abd rounds 2 digit

# ********* Coin tos program *********
rand_coin = random.randint(0,1)
rand_coin_OutPut = ""
if rand_coin == 0:
  rand_coin_OutPut = "Head"
else:
  rand_coin_OutPut = "Tail"
