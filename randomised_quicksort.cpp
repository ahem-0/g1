
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
using namespace std;
int partition(vector<int>& arr,int st,int end,int& comp){
    int x = arr[end];
    int i = st - 1;
    for (int j = st; j < end; j++){
        comp++;
        if (arr[j] <= x){
            i++;
            swap(arr[j],arr[i]);
        }
    }
    swap(arr[i+1], arr[end]);
    return i+1;
}

int randomized_partition(vector<int>& arr,int st,int end,int& comp){
    int i = st + rand() % (end - st + 1);
    swap(arr[i],arr[end]);
    return partition(arr,st,end,comp);
}
void quicksort(vector<int>& arr,int st,int end,int& comp){
    if (st < end){
            int q = randomized_partition(arr,st,end,comp);
            quicksort(arr,st,q-1,comp);
            quicksort(arr,q+1,end,comp);
    }

}
int main(){
    srand(time(0));
    vector<int> arr = {5,6,3,4,1};
    int st = 0;
    int n = arr.size()-1;
    int c = 0;
    quicksort(arr,st,n,c);
    
    for (int i : arr){
        cout << i << " ";
    }
    cout<< endl << "no of comparisons:" << c;

}
