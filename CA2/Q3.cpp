#include <iostream>

using namespace std;

long long n;

const long long maxn =  10000LL;
long long dp[2][maxn];
long long num[maxn];


long long findAnswer(){
	long long row = 1, row2,k;

	dp[1][1] = 1LL;

	for (long long i=2; i<=n ; ++i){
		for (long long j=1; j <= n; ++j){

			if(j==1){
				dp[i][j] = 1;
				continue;
			}

			dp[i][j] = (((dp[i-1][j] * (j)) % 1000007) + dp[i-1][j-1]) % 1000007;

			cout << i << " " << j << " " << dp[i][j] << endl;
		}
	}
	cout << "---" << endl;
	long long result = 1;
	for (int i=2; i<=n; ++i){
		k = num[i] - 1;
		while(k > 0){
			result += dp[i][k] % 1000007;
			k = k -1;
			cout << dp[i][k] << endl;
		}

	}
	return result + 1; 

}

int main()
{	
	cin >> n;
	for (long long i =0; i<n; i++){
		cin >> num[i];
	}

	cout << findAnswer() << endl;
	return 0;
}