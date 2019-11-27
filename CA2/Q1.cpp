// #include<bits/stdc++.h>
#include <iostream>

using namespace std;


const long long maxn = 1e3 + 3;
const long long maxk = 1e2 + 2;

long long m;
long long n;
long long coins;

long long arr[2][maxn][maxk];

long long mat[maxn][maxn];


long long findAllPaths(){
	long long row = 1, row2;
	arr[1][1][0] = 1LL;
	arr[1][1][mat[1][1]] = 1LL;


	for(long long i=1; i<=n ; ++i){
		row2 = row ^ 1;
		for (long long j=1; j<=m ; ++j){
			for(long long k=0; k <= coins; ++k){
				if (i != 1)
					arr[row][j][k] = 0LL;
				arr[row][j][k] += arr[row2][j][k] + arr[row][j-1][k];
				arr[row][j][k] %= 1000000007;
				if ((k - mat[i][j] >= 0) && (mat[i][j] !=0))
					arr[row][j][k] += arr[row2][j][k - mat[i][j]] + arr[row][j-1][k - mat[i][j]];
				arr[row][j][k] %= 1000000007;
			}
		}
		if (i != n)
			row = row ^ 1;
	}

	return arr [row][m][coins];
}

int main (){
	cin >> n >> m >> coins;
	for (long long i=1; i<=n ; i++){
		for(long long j=1 ; j<=m; j++){
			cin >> mat[i][j];
		}
	}


	cout << findAllPaths() << endl;
	return 0;
}