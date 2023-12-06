#include<iostream>
#include<vector>
#include<map>
#include<iomanip>

using namespace std;

int mini(int temp1, vector <int> A){
    vector<int> pl(temp1, 0);
    for(int i = 1 ; i <temp1; i++){
        pl[i] = pl[i-1]+abs(A[i] - A[i-1]);
        if(i >= 3){
            pl[i] = min(pl[i], pl[i-3] + abs(A[i] - A[i-3]));
        }
    }
    return pl[temp1-1];
}