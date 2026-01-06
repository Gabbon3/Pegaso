#include <iostream>
using namespace std;

void heapify(int arr[], int len, int padre, int* mosse) {
    int piugrande = padre; // indice del padre
    int sinistro = 2 * padre + 1;
    int destro = 2 * padre + 2;

    if (sinistro < len && arr[sinistro] > arr[piugrande]) {
        piugrande = sinistro;
    }

    if (destro < len && arr[destro] > arr[piugrande]) {
        piugrande = destro;
    }

    if (piugrande != padre) {
        int valorePadre = arr[padre];
        arr[padre] = arr[piugrande];
        arr[piugrande] = valorePadre;
        (*mosse)++;
        heapify(arr, len, piugrande, mosse);
    }
}

void heapSort(int arr[], int len, int* mosse) {
    // allineo l array per avere una condizione valida di maxheap
    for (int i = len / 2 - 1; i >= 0; i--) {
        heapify(arr, len, i, mosse);
    }
    // itero dal fondo
    for (int i = len - 1; i > 0; i--) {
        int valoreMaggiore = arr[0];
        arr[0] = arr[i];
        arr[i] = valoreMaggiore;
        (*mosse)++;
        heapify(arr, i, 0, mosse);
    }
}

int main() {
    int len = 100;
    int arr[100] = {66, 30, 54, 18, 0, 8, 92, 77, 14, 38, 62, 1, 59, 27, 55, 93, 25, 53, 75, 47, 86, 2, 94, 87, 71, 26, 73, 61, 98, 4, 7, 56, 85, 44, 67, 33, 6, 80, 70, 5, 72, 35, 79, 57, 39, 99, 34, 68, 78, 83, 36, 43, 52, 65, 96, 82, 20, 89, 3, 81, 12, 49, 90, 9, 10, 51, 48, 91, 74, 64, 60, 76, 50, 63, 88, 17, 97, 95, 69, 11, 23, 84, 58, 22, 15, 32, 40, 16, 29, 37, 24, 46, 45, 31, 21, 13, 41, 19, 28, 42};
    int mosse = 0;
    cout << "Array originale: ";
    for (int val : arr) cout << val << " ";
    cout << endl;

    heapSort(arr, len, &mosse);

    cout << "Array ordinato:  ";
    for (int val : arr) cout << val << " ";
    cout << endl;
    cout << "Mosse totali: " << mosse << endl;
    return 0;
}
/*
            10
    6               3
9       12      1

per prima cosa dobbiamo ottenere il primo maxheap
quindi iteriamo per ogni elemento dell array, partendo dal centro a scendere
ci mettiamo nella condizione di max heap, cioe ogni padre deve essere >= del figlio quindi
- padre = (int) i - 1 / 2
pero noi iteriamo sui padri, quindi per accedere ai figli:
- figlio sinistro = (int) 2i + 1
- figlio destro = (int) 2i + 2

quindi per ogni padre, verifichiamo i figli se sono maggiori di esso, se si aggiorniamo il padre con il figlio piu grande
*/