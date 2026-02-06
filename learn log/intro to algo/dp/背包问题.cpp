//0-1背包问题
//关键的状态转移方程——f[i][j] = max(f[i-1][j],f[i-1][j-w[i]]+v[i]) 其中f[i][j]表示前i个物品在背包容量为j的情况下所能存储的最大价值

#include<iostream>
using namespace std;

int backpack(int n,int W,int v[], int w[])
{
	int val[100][100];
	for (int i = 0; i < n; i++)
	{
		for (int j = 1; j <= W; j++)
		{
			if (i == 0)
			{
				val[i][j] = 0;
			}
			else if (w[i] > j)
			{
				val[i][j] = val[i - 1][j];
			}
			else {
				val[i][j] = max(val[i - 1][j], val[i - 1][j - w[i]] + v[i]);
			}
		}
	}
	return val[n - 1][W];

}

//尝试优化，将二维数组变为一维
//核心在于每一维的数据仅于前一维相关 因此不断替代 即可实现一维数组
int improved_backpack(int n,int W,int v[],int w[])
{
	int arr[100] = { 0 };
	for (int i = 1; i <= n; i++)
	{
		for (int j = W; j >= w[i]; j--)//这里注意应该逆序，否则会有数据上一维的数据提前被覆盖
		{
				arr[j] = max(arr[j], arr[j - w[i]] + v[i]);
		}
	}
	return arr[W];
}
/*
	i	1		2		3		4		5		6
j
1	  arr[1]   
2	  arr[2]
3	  ...		...
4	  arr[j]  max(arr[j],arr[j-w[i]]+v[i])
5	  ...		...
6			
7
*/
