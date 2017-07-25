#include <bits/stdc++.h>

using namespace std;

const int N = 5 * 1e6 + 1;
int a[N];
int ans[N];
int n, k, q;

int main(void){
	ios::sync_with_stdio(false);
	cin >> n >> q >> k;
	for(int i = 0; i < n; i += 1) cin >> a[i];
	deque<int> st;
	for(int i = 0; i < k-1; i += 1){
		while(!st.empty() and a[st.back()] < a[i]){
			st.pop_back();
		}
		st.push_back(i);
	}
	for(int i = k-1; i < n; i += 1){
		if(!st.empty() and i - st.front() >= k){
			st.pop_front();
		}
		while(!st.empty() and a[st.back()] <= a[i]){
			st.pop_back();
		}
		if(st.empty()){
			ans[i] = i;
		}else{
			ans[i] = st.front();
		}
		st.push_back(i);
	}
	int qi;
	for(int i= 0; i < q; i += 1){
		cin >> qi;
		cout << a[ans[qi-1]] <<endl;

	}
}
