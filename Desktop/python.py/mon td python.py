# exo1
a=25
b=7
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
# exo2
a=18
b=5
C=24
print(a%2)
print(b%2)
print(C%2)
print(a%b)
print(C%b)
# le reste de la division de a par 2 c'est 0
# le reste de la division de b par 2 c'est 1
# le reste de la division de C par 2 c'est 0
# le reste de la division de a par b c'est 3
# le reste de la division de C par b c'est 4
# exo3
nombre=10
nombre+=5
nombre*=2
nombre-=8
nombre/=2
print(nombre)
# 1) determine la valeur de nombre apres chaque instruction:
# - Après `nombre+=5`, nombre = 10 + 5 = 15
# - Après `nombre*=2`, nombre = 15 * 2 = 30
# - Après `nombre-=8`, nombre = 30 - 8 = 22
# - Après `nombre/=2`, nombre = 22 / 2 = 11
# 2) trouver le resultat final sans executer le programme:
# Le résultat final de `nombre` après toutes les instructions est 11.
# 3)verifier avec Python
# 4)expliquer le role de chaque operateur utiliser dans le programme:
# - `+=` : ajoute la valeur à droite à la variable à gauche et affecte le résultat à la variable à gauche
# - `*=` : multiplie la variable à gauche par la valeur à droite et affecte le résultat à la variable à gauche
# - `-=` : soustrait la valeur à droite de la variable à gauche et affecte le résultat à la variable à gauche
# - `/=` : divise la variable à gauche par la valeur à droite et affecte le résultat à la variable à gauche
# exo4
age=22
note=14
moyenne=9.5
print(age==22)
print(age>18)
print(note>=10)
print(moyenne<10)
print(note!=12)
print(age<=25)
# exo5
print(10 > 5 )
print(8==10)
print(15!=12)
print(20<=20)
print(7>=9)
print(12<5)
# la premier expression est vraie, la deuxieme est fausse, la troisieme est vraie, la quatrieme est vraie, la cinquieme est fausse, la sixieme est fausse
# exo6
est_boursier=True
benefice_aide=False
verification=est_boursier and benefice_aide
print(verification) 
verification2=est_boursier or benefice_aide
print(verification2)
verification3=not est_boursier
print(verification3)
# exo7
quantité_cahier=4
quantité_stylo=3
quantité_classeur=2
prix_cahier=1000
prix_stylo=500
prix_classeur=2500
total_cahier=quantité_cahier*prix_cahier
total_stylo=quantité_stylo*prix_stylo
total_classeur=quantité_classeur*prix_classeur
montant_total=total_cahier+total_stylo+total_classeur
print("Le montant total à payer est:", montant_total, "francs CFA")
# exo8
algorithme=15
programmation=12
maths=14
anglais=16
somme_notes=algorithme+programmation+maths+anglais
moyenne_generale=somme_notes/4
est_sup_egal=(moyenne_generale >= 10)
est_sup_egal2=(moyenne_generale >= 15)
print(est_sup_egal)
print(est_sup_egal2)
# exo9
solde=150000
solde+=50000
solde-=25000
solde-=10000
print("Le solde final est:", solde, "francs CFA")
verification_solde=(solde >100000)
print("Le solde est supérieur à 100000:", verification_solde)
verification_solde2=(solde <200000)
print("Le solde est inférieur à 200000:", verification_solde2)
# exo10
inscription_validée=True
frais_payés=True
dossier_complet=False
admission_autorisée=inscription_validée and frais_payés and dossier_complet
print("Admission autorisée:", admission_autorisée)
admission_autorisée2=inscription_validée or frais_payés or dossier_complet
print("Admission autorisée (au moins une condition remplie):", admission_autorisée2)
admission_autorisée3=not inscription_validée
print("Inscription non validée:", admission_autorisée3)
# exo11
anné_naissance=2004
anné_actuelle=2026
age_approximatif=anné_actuelle-anné_naissance
print("L'âge approximatif est:", age_approximatif, "ans")
est_sup=(age_approximatif >= 18)
est_sup2=(age_approximatif >= 25)
verification_age=(age_approximatif > 18) and (age_approximatif < 25)
print("L'âge est supérieur à 18 ans:", est_sup)
print("L'âge est supérieur ou égal à 25 ans:", est_sup2)
print("L'âge est compris entre 18 et 25 ans:", verification_age)
# exo12
# ProgrameA
resultat=10+5*2
print(resultat)
# le resultat est 20 car la multiplication est prioritaire sur l'addition.
# ProgrameB
resultat=(10+5)*2
print(resultat)
# le resultat est 30 car les parenthèses changent l'ordre des opérations, donc l'addition est effectuée avant la multiplication.
# ProgrammeC
resultat=20/4+3**2
print(resultat)
# le resultat est 14.0 car la division et l'exponentiation sont prioritaires sur l'addition. Donc, 20/4=5.0 et 3**2=9, puis 5.0+9=14.0.
# 1) le programme a et b ne donne pas le le   même resultat car dans le programme a, la multiplication est effectuée avant l'addition, tandis que dans le programme b, l'addition est effectuée avant la multiplication en raison des parenthèses.
# 2) l'operation executé en premier dans le programme c est l'exponentiation (3**2), suivie de la division (20/4), puis l'addition des deux résultats.
# Le role des parenthèses dans les expressions mathématiques est de modifier l'ordre d'évaluation des opérations. Les opérations à l'intérieur des parenthèses sont effectuées en premier, ce qui peut changer le résultat final par rapport à une expression sans parenthèses.
# exo13
prix_initial=50000
taux_reduction=10
montant_reduction=(prix_initial*taux_reduction)/100
prix_apres_reduction=prix_initial-montant_reduction
print("Le prix final est de:", prix_apres_reduction, "francs CFA")
print(prix_initial)
print(taux_reduction)
# exo14
nombre_etudiants=53
taille_groupe=5
nombre_groupes=nombre_etudiants//taille_groupe
nombre_etudiants_restant=nombre_etudiants%taille_groupe
print("Nombre de groupes complets:", nombre_groupes)
print("Nombre d'étudiants restant:", nombre_etudiants_restant)
# exo15
frais_dossier=25_000
inscription=200_000
premiere_mensualité=60_000
montant_disponible=250_000
montant_total_payer=frais_dossier+inscription+premiere_mensualité
difference=montant_disponible-montant_total_payer
verification_paiement=(montant_disponible >= montant_total_payer)
verification_paiement2=(montant_disponible < montant_total_payer)
reste_a_payer=montant_total_payer-montant_disponible
print("Montant total à payer:", montant_total_payer, "francs CFA")
print("Montant disponible:", montant_disponible, "francs CFA")
print("Différence :", difference, "francs CFA")
print("paiement suffisante:", verification_paiement)
print("reste a payer", reste_a_payer, "francs CFA")




