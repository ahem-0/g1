#include<iostream>
#include <vector>
#include <climits>
using namespace std;

void selectionsort(vector<int>& arr);
void bubblesort(vector<int>& arr);
void insertionsort(vector<int>& arr);

int main(){
    vector <int> arr = {4,1,2,3,7};
    selectionsort(arr);
    for (int x:arr){
        cout << x; 
    }
    cout << endl;
    
    arr = {4,1,2,3,7};
    insertionsort(arr);
    for (int x:arr){
        cout<< x; 
    }
    cout << endl;
/*
    arr = {4,1,2,3,7};
    buublesort(arr);
    for (int x:arr){
        cout<< x; 
    }
    cout << endl;
    
*/
}
void selectionsort(vector<int>& arr){
    int n = arr.size();
    for (int i = 0; i < n-1; i++){
        int smallestIdx = i;
        for (int j = i+1;j < n; j++){
            if(arr[smallestIdx]>arr[j])smallestIdx = j;

        }
        swap(arr[i],arr[smallestIdx]);
    }
}

void insertionsort(vector<int>& arr){
    int n = arr.size();
    int temp = 0;
    for (int i = 1; i < n; i++){
        int temp =arr[i];
        int prev = i-1;
        while (prev >= 0 && temp<arr[prev]){
            arr[prev+1] = arr[prev];
            prev--;
        }
        arr[prev+1] = temp;        
    }
}