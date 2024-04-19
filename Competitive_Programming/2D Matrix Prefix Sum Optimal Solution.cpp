##Time Complexity:- O(m x n) where m= no of rows, n= no of columns


#include<iostream>
#include<vector>

using namespace std;

int main(){
    int row, col;
    cin>>row>>col;
    
    vector<vector<int>> matrix(row, vector<int> (col, 0));
    for(int i=0;i<row;i++){
        for(int j=0;j<col;j++){
            cin>>matrix[i][j];
        }
    }
    vector<vector<int>> cum_sum(row, vector<int> (col, 0));
    cum_sum[0][0]= matrix[0][0];
    
    for(int i=1; i< col; i++){
        cum_sum[0][i]= cum_sum[0][i-1] + matrix[0][i];
    }
    for(int j=1; j<row; j++){
        cum_sum[j][0]= cum_sum[j-1][0] + matrix[j][0];
    }
    for(int i=1; i<row; i++){
        for(int j=1; j<col; j++){
            cum_sum[i][j]= cum_sum[i-1][j] + cum_sum[i][j-1] - cum_sum[i-1][j-1] + matrix[i][j];
        }
    }
    for(int i=0; i<row; i++){
        for(int j=0; j<col; j++){
            cout<<cum_sum[i][j]<<" ";
        }
        cout<<endl;
    }
    return 0;
    
    
}
