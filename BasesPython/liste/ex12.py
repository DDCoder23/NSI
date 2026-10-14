Date= ["3/10", "5/10", "9/10", "9/10", "11/10", "15/10", "19/10", "21/10"]
Montant = [-60.00, -12.50, -27.90, -23.00, 100.00, -250.00, 23.00, 600.00]
for Date,Montant  in zip(reversed(Date), reversed(Montant)):
        if Montant <0:
             print(f"Le{Date}: retrait de {Montant} €")
        else:
             print(f"Le{Date}: versement de {Montant} €")