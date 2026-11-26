
#include <iostream>
#include<vector>
#include <algorithm>
#include <cstdlib>

using namespace std;
int partition(vector <int>& arr, int p, int r){
    int x = arr[r];
    int i = p-1;
    for (int j = p; j < r; j++){
        if (arr[j] <= x){
            i++;
            swap(arr[i],arr[j]);
        }
    } 
    swap(arr[i+1],arr[r]);
    return i+1;
}

int randomised_partition(vector<int>& arr, int p, int r){
    int i = p + rand() % (r - p + 1);
    swap(arr[i],arr[r]);
    return partition(arr,p,r);
}
int randomised_select(vector<int>& arr, int p, int r, int i) {
    if (p == r) return arr[p];
    int q = randomised_partition(arr, p, r);
    if (i == q) return arr[q];
    else if (i < q) return randomised_select(arr, p, q - 1, i);
    else return randomised_select(arr, q + 1, r, i);
}
int main(){
    vector<int> arr = {5,6,3,4,1};
    int st = 0;
    int n = arr.size()-1;
    int i;
    cout<< "enter the index: ";
    cin >> i;
    cout << randomised_select(arr,st,n,i);
}


