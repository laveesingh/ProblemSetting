/*
* Solution to max-to-left problem
* Expected Time Complexity:
* 	Preprocessing: O(N)
* 	Query: O(1)
*/

#include <bits/stdc++.h>

using namespace std;

const int N = 5 * 1e6 + 1;
int n, q, a[N], ans[N];

int main(void){
    cin >> n >> q;
    for(int i = 0; i < n; i++) cin >> a[i];
    stack<int> st;
    for(int i = 0; i < n; i++){
		while(!st.empty() and st.top() < a[i])
			st.pop();
		if(st.empty()){
			ans[i] = -1;
		}else{
			ans[i] = st.top();
		}
		st.push(a[i]);
    }
	int qi;
	for(int i = 0; i < q; i++){
		cin >> qi;
		cout << ans[qi-1] << endl;
	}
}
