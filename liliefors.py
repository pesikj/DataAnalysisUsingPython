import statsmodels.api as sm
data = [
9.9,
11.1,
1.4,
4.8,
18.1,
10.8,
20.9,
8.7,
3,
7.4,
6.1,
13.3,
7.9,
11.5,
7,
22.6,
21.8,
4.6,
7.8,
1.1,
17.4,
18.2,
8.6,
1.6,
11.5,
24.4,
0,
0.7,
9.3,
14.3,
0.9,
2.1,
5.7,
16.5,
21.1,
8.3,
8.4,
4.3,
16.6,
23.6,
12.6,
18,
22.2,
16.2,
19,
13.1,
5.7,
8.8,
23.8,
8.3,
20.8,
24.5,
17.7,
15.2,
15.9,
13.5,
8.5,
18.2,
10.3,
17.5,
11.5,
4.9,
20.1,
11.1,
5.3,
1.3,
9,
3.9,
13.1,
22.9,
22.8,
12.9,
20.9,
4.8,
18,
7.3,
10.2,
19.6,
9.6,
1.5,
]
result = sm.stats.diagnostic.lilliefors(data, 'norm', 'table')
print(result)