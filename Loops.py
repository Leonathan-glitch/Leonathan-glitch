Leon=["Computer","Robots","AI's","Smartwatches","Coding"]
print(len(Leon))
for CITE in Leon:
   print(CITE)
    
#Elements=("Oroma","Book","God'sgift","Vhizzy","Favor","David","Rex","Divine","Munachi","Praise")
#print(len(Elements))
#for Willy in Elements:
    #print(Willy)
    #for Ariana_Grande in Willy:
     #   print(Ariana_Grande)
#New codes
CW=20
C=0.165
NW=CW
for Year in range(1,6):
    NW=NW*C
    print("Year %s = %s"%(Year,NW))\

Username="Leon"
Password="L"
while True:
   user_test=input("Enter your username :")
   pasword_test=input("Enter your password :")
   if    Password == pasword_test:
      print("Pasword is correct")
   else:
      print("You've entered the wrong password")
   if Username==user_test:
      print("Username is correct")
   else:
      print("Username is not correct")



    
