A. Cheap Travel

Ann has recently started commuting by subway. We know that a one ride subway ticket costs a rubles. Besides, Ann found out that she can buy a special ticket for m rides (she can buy it several times). It costs b rubles. Ann did the math; she will need to use subway n times. Help Ann, tell her what is the minimum sum of money she will have to spend to make n rides?

Input
The single line contains four space-separated integers n, m, a, b (1 ≤ n, m, a, b ≤ 1000) — the number of rides Ann has planned, the number of rides covered by the m ride ticket, the price of a one ride ticket and the price of an m ride ticket.

Output
Print a single integer — the minimum sum in rubles that Ann will need to spend.


#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int n, m, a, b;
    cin >> n >> m >> a >> b;

    // Calculate the cost for individual tickets
    int individualCost = n * a;

    // Calculate the cost for m-ride tickets
    int mRideCost = (n / m) * b + min((n % m) * a, b);

    // Choose the minimum cost
    int minCost = min(individualCost, mRideCost);

    cout << minCost << endl;

    return 0;
}
