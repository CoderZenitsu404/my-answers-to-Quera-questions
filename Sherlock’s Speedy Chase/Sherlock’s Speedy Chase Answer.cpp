#include <iostream>
#include <vector>

using namespace std;


int main() {
    int k, n; // speed (m/s), number of buildings
    cin >> k >> n; // input
    vector<int> a(n); // height of each building
    for (int i = 0; i < n; ++i) {
        cin >> a[i]; // input
    } // input

    int h = 0; // his location's height
    int total = 0; // total time

    for (int target : a) {
        int diff = abs(target - h); // distance
        int time = (diff + k - 1) / k; // time
        total += time; // add to total
        h = target; // update
    } // main loop

    total += n + (h + k - 1) / k; // add to total

    cout << total << endl; // output

    return 0;
}