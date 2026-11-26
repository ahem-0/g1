#include <vector>
#include <string>
#include <iostream>

using namespace std;

vector<int> createlps (string s){
    vector<int>  lps(s.length(),0);
    int prevlps = 0;
    int i = 1;
    while(i < s.length()){
        if (s[i] == s[prevlps]){
            prevlps++;
            lps[i] = prevlps;
            i++;
        }
        else if (prevlps == 0){
            lps[i] = 0;
            i++;
        }
        else prevlps = lps[prevlps-1];
    }
    return lps;
};
int kmpAlgo(string s,string pattern){
    int i = 0, j = 0;
    vector<int> lps = createlps(pattern);
    while(i < s.length()){
        if (s[i] == pattern[j]){
            i++;
            j++;
        }
        else if (j == 0) i++;
        else j = lps[j-1];
        if (j == pattern.length()) return (i - pattern.length());
    }
    return -1;
};

int main(){
    string p = "AAACAAA";
    string s = "AACARCXAACAAAACAAA";
    vector<int> lps = createlps(p);
    cout << "lps : ";
    for (int i : lps) cout << i << " ";
    cout << endl;
    cout << "idx : "<< kmpAlgo(s,p) << endl;
}





