from random import choice

giving_gifts = {
    "Bob": "candle",
    "Jen": "popsicles",
    "Fred": "yo-yo"
}

white_elep = {}

for person in giving_gifts:
    # new_person = 
    gifts = giving_gifts.values()
    new_gift = choice(gifts)
    
    while True:    
        if new_gift not in white_elep.values():
            white_elep[person] = new_gift
            break
        else:
            new_gift = choice(gifts)
    



    # del giving_gifts[new_gift]

print giving_gifts
print white_elep