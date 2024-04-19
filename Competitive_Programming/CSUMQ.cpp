#include<iostream>
#include<vector>
using namespace std;

int main() {
	int n;
	cin >> n;

	vector<int> array(n, 0);
	for (int i = 0; i < n; i++) {
		cin >> array[i];
	}

	vector<int> cum_arr(n, 0);
	for (int i = 0; i < n; i++) {
		cum_arr[i] = cum_arr[i - 1] + array[i];
	}

	int q;
	cin >> q;
	while (q--) {
		int start, end;
		cin >> start;
		cin >> end;

		if (start == 0) {
			cout << cum_arr[end] << endl;
		}
		else {
			cout << cum_arr[end] - cum_arr[start - 1] << endl;;

		}
	}
	return 0;

}