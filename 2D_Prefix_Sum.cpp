#include<iostream>
#include<vector>
using namespace std;

int main(){
    int rows, cols;
    cin>>rows>>cols;
    vector<vector<int>> matrix(rows,vector<int> (cols, 0));
    for(int row_index=0; row_index<rows; row_index++){
        for(int col_index=0; col_index<cols; col_index++){
            cin>> matrix[row_index][col_index];
        }
    }
    vector<vector<int>> cum_matrix(rows,vector<int> (cols, 0));
    
    for(int cum_row_index= 0; cum_row_index < rows; cum_row_index++){
        for(int cum_col_index=0; cum_col_index< cols; cum_col_index++){
            int sum=0;
            for(int row_index=0; row_index<=cum_row_index; row_index++){
                for(int col_index=0; col_index<=cum_col_index; col_index++){
                    sum+= matrix[row_index][col_index];
                }
            }
            cum_matrix[cum_row_index][cum_col_index]= sum;
        }
    }
    for(int cum_row_index=0; cum_row_index< rows; cum_row_index++){
        for(int cum_col_index=0; cum_col_index< cols; cum_col_index++){
            cout<< cum_matrix[cum_row_index][cum_col_index]<< " ";
        }
        cout<<endl;
    }
}