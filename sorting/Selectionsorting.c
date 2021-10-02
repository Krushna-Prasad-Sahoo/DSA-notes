#include<stdio.h>
void selectionSort(int *A, int n){
    int indexOfMin, temp;
    for(int i=0; i<n-1; i++){ // loop for passes
        indexOfMin = i;
        for(int j=i+1; j<n; j++){ //loop for comparison of each element
            if(A[j]<A[indexOfMin]){
                indexOfMin = j;
            }
        }
        temp = A[i]; //swapping of each element
        A[i] = A[indexOfMin];
        A[indexOfMin] = temp;
    }
}
void printArray(int* A, int n){
    for(int i=0; i<n; i++){
        printf("%d ", A[i]);
    }
    printf("\n");
}
int main(){
    int n;
    scanf("%d", &n);
    int b[n];
    for(int i=0; i<n; i++)
        scanf("%d", &b[i]);
    int B[] = {1, 2, 3, 4, 5, 6};
    selectionSort(b, 0, 5);
    printArray(b, 6);
}
