

#include <iostream>
#include <algorithm>
#include <stdio.h>


using namespace std;




int main() {
	
		
		
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++) 
	{
		int N, B;
		cin >> N >> B;
		
		int A[N];
		for (int j = 0; j < N; j++)
			cin >> A[j];
		
		int M[N+1][B+1];
		for(int i=0; i<=N; i++){
			for(int j=0;j<=B;j++){
				M[i][j] = 0;
			}
		}
		
		for (int i=1;i<=N;i++)
		{
			for(int j=0;j<=B;j++)
			{
				M[i][j] = M[i-1][j];
				if(j >= A[i-1]){
					if(M[i][j] < (M[i-1][j - A[i-1]] + 1)){
						M[i][j] = M[i-1][j - A[i-1]] + 1;
					}
				}
			}
		}

		int len = N;
		int sol=0;
		while (len >= 1){
			if (M[len][B] != M[len-1][B]){
				sol++;
				B = B - A[len-1];
			}
			len--;
		}
		cout << "Case #" << tt << ": " << sol << '\n';
	}
}
