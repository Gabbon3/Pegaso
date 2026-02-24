#include <iostream>
#include <vector>

using namespace std;

void merge(int arr[], int left, int mid, int right, int &mosse) {
    /*
     1. PREPARAZIONE
     Calcoliamo la dimensione e creiamo l'array temporaneo.
     Indici:
     - i punta all'inizio del sotto-array di SINISTRA (da left a mid)
     - j punta all'inizio del sotto-array di DESTRA (da mid+1 a right)
     - k punta alla posizione corrente nell'array TEMP
    */
    int i = left;
    int j = mid + 1;
    int k = 0;
    
    // Usiamo un vector per evitare problemi di memoria dinamica manuale
    // Dimensione: numero totale di elementi da fondere
    vector<int> temp(right - left + 1);

    /*
     2. IL PRIMO WHILE (La Battaglia)
     Iteriamo finché ENTRAMBI i sotto-array hanno ancora elementi.
     Qui avviene il confronto vero e proprio: il minore vince ed entra nel temp.
    */
    while (i <= mid && j <= right) {
        mosse++; // Contiamo il confronto
        
        if (arr[i] <= arr[j]) {
            // Se l'elemento di sinistra è minore (o uguale -> Stabilità), lo prendiamo
            temp[k] = arr[i];
            i++; // Avanziamo col cursore sinistro
        } else {
            // Altrimenti prendiamo quello di destra
            temp[k] = arr[j];
            j++; // Avanziamo col cursore destro
        }
        k++; // In ogni caso, avanziamo nel temp
    }

    /*
     3. SECONDO WHILE (Pulizia Sinistra)
     Se il ciclo sopra è finito, uno dei due mazzi è esaurito.
     Se è rimasto qualcosa a SINISTRA, lo copiamo tutto in blocco.
     Non servono if: sappiamo che sono già ordinati e non c'è più nessuno a destra con cui confrontarsi.
    */
    while (i <= mid) {
        temp[k] = arr[i];
        i++;
        k++;
        mosse++;
    }

    /*
     4. TERZO WHILE (Pulizia Destra)
     Stessa cosa: se invece era rimasto qualcosa a DESTRA, lo copiamo.
     Nota: Solo uno di questi due while (3 o 4) verrà eseguito realmente, mai entrambi.
    */
    while (j <= right) {
        temp[k] = arr[j];
        j++;
        k++;
        mosse++;
    }

    /*
     5. COPIA FINALE
     Ricopiamo tutto dall'array temporaneo ordinato (temp) dentro l'array originale (arr)
    */
    for (int s = 0; s < temp.size(); s++) {
        arr[left + s] = temp[s];
    }
}

void mergeSort(int arr[], int left, int right, int &mosse) {
    if (left < right) {
        // Calcolo sicuro del centro per evitare overflow
        int mid = left + (right - left) / 2;
        
        // Divide (scendiamo in profondità)
        mergeSort(arr, left, mid, mosse);
        mergeSort(arr, mid + 1, right, mosse);
        
        // Impera (fondiamo risalendo)
        merge(arr, left, mid, right, mosse);
    }
}

int main() {
    int arr[100] = {66, 30, 54, 18, 0, 8, 92, 77, 14, 38, 62, 1, 59, 27, 55, 93, 25, 53, 75, 47, 86, 2, 94, 87, 71, 26, 73, 61, 98, 4, 7, 56, 85, 44, 67, 33, 6, 80, 70, 5, 72, 35, 79, 57, 39, 99, 34, 68, 78, 83, 36, 43, 52, 65, 96, 82, 20, 89, 3, 81, 12, 49, 90, 9, 10, 51, 48, 91, 74, 64, 60, 76, 50, 63, 88, 17, 97, 95, 69, 11, 23, 84, 58, 22, 15, 32, 40, 16, 29, 37, 24, 46, 45, 31, 21, 13, 41, 19, 28, 42};
    int n = sizeof(arr) / sizeof(arr[0]);
    int mosse = 0;

    cout << "Array originale: ";
    for (int i : arr) cout << i << " ";
    cout << endl;

    mergeSort(arr, 0, n - 1, mosse);

    cout << "Array ordinato:  ";
    for (int i : arr) cout << i << " ";
    cout << endl;
    cout << "Mosse (copie + confronti): " << mosse << endl;

    return 0;
}