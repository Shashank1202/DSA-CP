#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int main(){
    int n, m;
    cin>>n>>m;
    
    vector<int> puzzle(m);
    for(int i=0;i<m;++i){
        cin>>puzzle[i];
    }
    sort(puzzle.begin(), puzzle.end());
    
    int diff=INT_MAX;
    int start=0;
    int end=0;
    
    for(int i=0; i<=m -n; ++i){
        int cur= puzzle[i+n-1]-puzzle[i];
        if(cur<diff){
            diff=cur;
            start=i;
            end=i+n-1;
        }
    }
    cout<<diff<<endl;
    return 0;
}