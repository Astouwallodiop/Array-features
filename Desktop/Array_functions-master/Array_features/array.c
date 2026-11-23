#include"headers.h"
void remplissageTableau(int T[],int n)
{
    int i;
    for(i=0; i<n; i++)
    {
        printf("Donner la %de valeur\n",i+1);
        scanf("%d",&T[i]);
    }
}

//Affichage
void affichageTableau(int T[],int n)
{
    int i;
    for(i=0; i<n; i++)
    {
        printf("%d\t",T[i]);

    }
    puts("");
}

//Tri croissant
void triTableauCroissant(int T[], int n)
{
    int i,j,tmp;
    for(i=0; i<n-1; i++)
    {
        for(j=i+1; j<n; j++)
        {
            if(T[i]>T[j])
            {
                tmp = T[i];
                T[i]=T[j];
                T[j]=tmp;
            }
        }
    }
}

//Tri decroissant
void triTableauDecroissant(int T[], int n)
{
    int i,j,tmp;
    for(i=0; i<n-1; i++)
    {
        for(j=i+1; j<n; j++)
        {
            if(T[i]<T[j])
            {
                tmp = T[i];
                T[i]=T[j];
                T[j]=tmp;
            }
        }
    }
}

//Decalage a gauche
void decalageGauche(int T[], int n,int k)
{
    int i,j,svg;

    for(i=0;i<k;i++){
//principe de decalage des elements d'un vecteur d'un rang a gauche
        svg=T[0];
        for(j=0;j<n-1;j++){
            T[j]=T[j+1];
        }
        T[n-1]=svg;
    }
}

// Decalage a droite
void decalageDroite(int T[], int n,int k)
{
    int i,j,svg;

    for(i=0;i<k;i++){
//principe de decalage des elements d'un vecteur d'un rang a droite
        svg=T[n-1];
        for(j=n-1;j>0;j--){
            T[j]=T[j-1];
        }
        T[0]=svg;
    }
}

int sommeTableau(int T[], int n){
    int i,som = 0;
    for(i=0;i<n;i++){
        som +=T[i];
    }
    return som;
}

int produitTableau(int T[], int n){
    int i,prod = 1;
    for(i=0;i<n;i++){
        prod *=T[i];
    }
    return prod;
}

// Inverse du tableau
void inverseTableau(int T[], int n){
    int i,j,svg;
    i=0;
    j=n-1;

    while(i<j){
        svg=T[i];
        T[i]=T[j];
        T[j]=svg;
        i++;
        j--;
    }
}



