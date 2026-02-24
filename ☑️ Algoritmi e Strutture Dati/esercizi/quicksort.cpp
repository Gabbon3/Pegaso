#include <iostream>

using namespace std;

int partition(int arr[], int low, int high, int *mosse)
{
    int pivot = arr[high];
    int j = low;

    // Iteriamo da low fino a high-1 (il pivot è in high)
    for (int i = low; i < high; i++)
    {
        // Ordine crescente elementi minori del pivot a sinistra
        if (arr[i] < pivot)
        {
            // portiamo i dietro il muro quindi dietro j
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            
            // adesso invertiamo quindi
            j++; 
            (*mosse)++;
        }
    }

    // alla fine invertiamo j (il muro che divide piccoli e grandi) con pivot (high)
    int temp = arr[j];
    arr[j] = arr[high];
    arr[high] = temp;
    (*mosse)++;

    return j;
}

void quickSort(int arr[], int low, int high, int *mosse)
{
    if (low < high)
    {
        int pivot = partition(arr, low, high, mosse);

        // Ordina i piccoli (a sinistra del pivot)
        quickSort(arr, low, pivot - 1, mosse);
        // Ordina i grandi (a destra del pivot)
        quickSort(arr, pivot + 1, high, mosse);
    }
}

int main()
{
    int len = 100;
    int arr[100] = {66, 30, 54, 18, 0, 8, 92, 77, 14, 38, 62, 1, 59, 27, 55, 93, 25, 53, 75, 47, 86, 2, 94, 87, 71, 26, 73, 61, 98, 4, 7, 56, 85, 44, 67, 33, 6, 80, 70, 5, 72, 35, 79, 57, 39, 99, 34, 68, 78, 83, 36, 43, 52, 65, 96, 82, 20, 89, 3, 81, 12, 49, 90, 9, 10, 51, 48, 91, 74, 64, 60, 76, 50, 63, 88, 17, 97, 95, 69, 11, 23, 84, 58, 22, 15, 32, 40, 16, 29, 37, 24, 46, 45, 31, 21, 13, 41, 19, 28, 42};

    int mosse = 0;
    cout << "Array originale: ";
    for (int val : arr)
        cout << val << " ";
    cout << endl;

    quickSort(arr, 0, len - 1, &mosse);

    cout << "Array ordinato:  ";
    for (int val : arr)
        cout << val << " ";
    cout << endl;
    cout << "Mosse totali: " << mosse << endl;
    return 0;
}