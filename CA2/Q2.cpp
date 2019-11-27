#include <iostream>
#include <string>

using namespace std;


long long penalties[4];

long long getCost(char s){
	if(s == 'A'){
		return penalties[0];
	}
	if(s == 'C'){
		return penalties[1];
	}
	if(s == 'G'){
		return penalties[2];
	}
	return penalties[3];
}


long long findCost(long long i, string a, string b){
	long long cost = 0;
	long long k = i;

	for(long long j=0; j<b.size(); j++){
		if(a[k] != b[j]){
			// s.insert(k,1,b[j]);
			cost += getCost(b[j]);
		}
		else{
			k++;
		}
		if (k == a.size()){
			for (int t=j+1; t<b.size(); t++){
				cost += getCost(b[t]);
			}
			break;
		}
	}
	return cost;
}

long long findAnswer(string a, string b){
	long long min;
	long long cost;


	for (long long i=0 ; i<b.size(); i++){
		min += getCost(b[i]);
	}


	for(long long i=0; i<a.size(); i++){ 
		cost = findCost(i, a, b);
		if (min > cost){ min = cost;}
	}

	return min;
}

int main(){

	string a;
	string b;

	cin >> a;
	cin >> b;

	for (long long i=0; i<4; i++){
		cin >> penalties[i];
	}

	cout << findAnswer(a, b) << endl;
	return 0;
}