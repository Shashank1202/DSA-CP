A. Expression
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
Petya studies in a school and he adores Maths. His class has been studying arithmetic expressions. On the last class the teacher wrote three positive integers a, b, c on the blackboard. The task was to insert signs of operations '+' and '*', and probably brackets between the numbers so that the value of the resulting expression is as large as possible. Let's consider an example: assume that the teacher wrote numbers 1, 2 and 3 on the blackboard. Here are some ways of placing signs and brackets:

1+2*3=7
1*(2+3)=5
1*2*3=6
(1+2)*3=9
Note that you can insert operation signs only between a and b, and between b and c, that is, you cannot swap integers. For instance, in the given sample you cannot get expression (1+3)*2.

It's easy to see that the maximum value that you can obtain is 9.

Your task is: given a, b and c print the maximum value that you can get.

Input
The input contains three integers a, b and c, each on a single line (1 ≤ a, b, c ≤ 10).

Output
Print the maximum value of the expression that you can obtain.

/*Solution*/

#include<iostream>
#include<algorithm>

using namespace std;

int main(){
    int a, b, c;
    cin>>a>>b>>c;
    
    int res1= a+b+c;
    int res2= a*b*c;
    int res3= (a+b)*c;
    int res4=  a*(b+c);
    
    int result=max({res1, res2, res3, res4});
    
    cout<<result<<endl;
    return 0;
}