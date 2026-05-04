#include<iostream>
#include <vector>
#include <climits>
using namespace std;
void mergeSort(vector<int>& arr);
void merge(vector<int>& arr,vector<int>& leftarr,vector<int>& rightarr);

int main(){
    vector <int> arr = {4,1,2,3,7};
    mergeSort(arr);
    for (int x:arr){
        cout << x; 
    }
}
void mergeSort(vector<int>& arr){
    if (arr.size() <= 1) return;
    int n = arr.size();
    int lsize = n/2;
    int rsize = n - lsize;
    vector<int> leftArray(lsize);
    vector<int> rightArray(rsize);
    int ct = 0;
    for (int i = 0; i < n; i++){
        if (i < lsize) leftArray[i] = arr[i];
        if (i >= lsize) {
            rightArray[ct] = arr[i];
            ct++;
        }
    }    
    mergeSort(leftArray);
    mergeSort(rightArray);
    merge(arr,leftArray,rightArray);
}
void merge(vector<int>& arr,vector<int>& leftarr,vector<int>& rightarr){
    int lsize = leftarr.size();
    int rsize = rightarr.size();
    int r = 0, l = 0, i=0;
    while (r < rsize && l < lsize){
        if (leftarr[l]>=rightarr[r]){
            arr[i] = rightarr[r];
            r++;
            i++;
        }
        else if (leftarr[l]<rightarr[r]){
            arr[i] = leftarr[l];
            l++;
            i++;
        }
    }
    while (l < lsize){
            arr[i] = leftarr[l];
            l++;
            i++;

    }
    while (r < rsize){
            arr[i] = rightarr[r];
            r++;
            i++;
    }
}
