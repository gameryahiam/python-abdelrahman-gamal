members_party = ("Alice Bob Charlie David Eve Frank Grace Heidi Ivan Judy")
print(members_party.split())

members_party2 = ("Alice_Bob_Charlie_David_Eve_Frank_Grace_Heidi_Ivan_Judy")
print(members_party2.split("_"))

members_party3 = ("Alice_Bob_Charlie_David_Eve_Frank_Grace_Heidi_Ivan_Judy")
print(members_party3.split("a"))

members_party4 = ("Alice_Bob_Charlie_David_Eve_Frank_Grace_Heidi_Ivan_Judy")
print(members_party4.split("a"))

members_party5 = ("Alice Bob Charlie David Eve Frank Grace Heidi Ivan Judy")
print(members_party5.rsplit())

members_party6 = ("Alice_Bob_Charlie_David_Eve_Frank_Grace_Heidi_Ivan_Judy")
print(members_party6.rsplit("_"))

members_party7 = ("Alice_Bob_Charlie_David_Eve_Frank_Grace_Heidi_Ivan_Judy")
print(members_party7.rsplit("a"))

members_party8 = ("Alice_Bob_Charlie_David_Eve_Frank_Grace_Heidi_Ivan_Judy")
print(members_party8.rsplit("a",3))
