#include"headers.h"
#define PAUSE system("pause");
#define CLEAR system("cls");
int main()
{
    int T[100],N,k,choix,choice;
    do
    {
        puts("1.Remplissage");
        puts("2.Affichage");
        puts("3.Tri");
        puts("4.Decalage");
        puts("5.Somme");
        puts("6.Produit");
        puts("7.Inverse");
        puts("8.Quitter");
        do
        {
            puts("Faites un choix :");
            scanf("%d",&choix);
        }
        while(choix <1 || choix >8);
        switch(choix)
        {
        case 1:
            do
            {
                puts("donner la taille:");
                scanf("%d",&N);
            }
            while(N<=0 || N>100);
            remplissageTableau(T,N);
            PAUSE
            CLEAR
            break;
        case 2:
            affichageTableau(T,N);
            PAUSE
            CLEAR
            break;
        case 3:
            do
            {
                puts("1.croissant");
                puts("2.Decroissant");
                puts("Faites un choix :");
                scanf("%d",&choice);
            }
            while(choice !=1 && choice !=2);
            switch(choice)
            {
            case 1:
                triTableauCroissant(T,N);
                affichageTableau(T,N);
                break;
            case 2:
                triTableauDecroissant(T,N);
                affichageTableau(T,N);
                break;
            }
            PAUSE
            CLEAR
            break;

        case 4:
            do
            {
                puts("Donner le nombre de rang");
                scanf("%d",&k);
            }
            while(k<=0);
            do
            {
                puts("1.Decalage a gauche");
                puts("2.Decalage a droite");
                puts("Faites un choix");
                scanf("%d",&choice);
            }
            while(choice !=1 && choice !=2);
            switch(choice)
            {
            case 1:
                decalageGauche(T,N,k);
                affichageTableau(T,N);
                break;
            case 2:
                decalageDroite(T,N,k);
                affichageTableau(T,N);
                break;
            }
            PAUSE
            CLEAR
            break;
        case 5:
            printf("somme = %d\n",sommeTableau(T,N));
            PAUSE
            CLEAR
            break;
        case 6:
            printf("Produit = %d\n",produitTableau(T,N));
            PAUSE
            CLEAR
            break;
        case 7:
            inverseTableau(T,N);
            affichageTableau(T,N);
            PAUSE
            CLEAR
            break;
        case 8:
            puts("Bye Bye !!!!");
            return 0;
        }
    }
    while(1);


    return 0;
}
