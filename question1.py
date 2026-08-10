hours=int(input("Enter parking hours: "))
charges=0
if hours>5:
   charges=20*hours
elif hours>2 and hours<=5:
    charges=25*hours
else:
    charges=30*hours
service_charges=0
if charges>150:
   service_charges+=20
print("Parking Charge: Rs.",charges)
print("Service Charge: Rs.",service_charges)
print("Total Charge: Rs.",charges+service_charges)

   