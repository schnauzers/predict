# predict
This program aims to gain an NBA player's sorts of records.

**Note**: All data are from [basketball-reference.com](http://www.basketball-reference.com/leaders/), so you should input players' names exactly by this website's convention.

## Usage

### Run from binary

Please download the windows binary file from [here](https://github.com/schnauzers/predict/files/752129/nbarecord.zip), and run it in a command window:

```
nbarecord.exe "LeBron James"
```

### Run from Python

After all, You need a Python3 environment,  and install following libs:

```
pip install requests bs4 lxml colorama
```

Run script like this:

```
python getrecord.py "LeBron James"
```

## Results

After executing the program, you will get the records of the player you are in fond of:

```
Points:
1.         Kareem Abdul-Jabbar         38387
2.         Karl Malone                 36928
3.         Kobe Bryant                 33643
4.         Michael Jordan              32292
5.         Wilt Chamberlain            31419
6.         Dirk Nowitzki               29788
7.         Shaquille O'Neal            28596
8.         LeBron James                27988
-----------------Last Time------------------
8.         LeBron James                27988
--------------------------------------------
Rebounds:
64.        Chris Webber                 8124
65.        Lamar Odom                   8059
66.        Bob McAdoo                   8048
67.        Larry Foust                  8041
68.        Happy Hairston               8019
69.        John Havlicek                8007
70.        Oscar Robertson              7804
71.        Sam Perkins                  7666
72.        Caldwell Jones               7663
73.        Antonio McDyess              7638
74.        Clyde Lee                    7626
75.        Chris Bosh                   7592
76.        Wayne Embry                  7544
77.        Maurice Lucas                7520
78.        Paul Pierce                  7497
79.        Scottie Pippen               7494
80.        James Donaldson              7492
81.        Al Jefferson                 7472
82.        Juwan Howard                 7428
           LeBron James                 7428
-----------------Last Time------------------
           LeBron James                 7428
--------------------------------------------
Blocks:
112.       Roy Hinson                    882
113.       Rony Seikaly                  872
114.       Joe Smith                     868
115.       James Edwards                 867
116.       Kenyon Martin                 864
117.       Paul Millsap                  853
118.       Donyell Marshall              848
           Dave Corzine                  848
120.       Kurt Thomas                   841
121.       Joakim Noah                   840
           Danny Schayes                 840
123.       Joel Przybilla                836
124.       Alex English                  833
125.       Marvin Webster                829
126.       Joe Meriweather               810
127.       Alvan Adams                   808
128.       Tracy McGrady                 807
129.       Jerome Kersey                 799
130.       Vin Baker                     798
131.       LeBron James                  797
-----------------Last Time------------------
131.       LeBron James                  797
--------------------------------------------
Assists:
1.         John Stockton               15806
2.         Jason Kidd                  12091
3.         Steve Nash                  10335
4.         Mark Jackson                10334
5.         Magic Johnson               10141
6.         Oscar Robertson              9887
7.         Isiah Thomas                 9061
8.         Gary Payton                  8966
9.         Andre Miller                 8524
10.        Chris Paul                   8037
11.        Rod Strickland               7987
12.        Maurice Cheeks               7392
13.        Lenny Wilkens                7211
14.        LeBron James                 7200
-----------------Last Time------------------
14.        LeBron James                 7200
--------------------------------------------
Steals:
2.         Jason Kidd                   2684
3.         Michael Jordan               2514
4.         Gary Payton                  2445
5.         Maurice Cheeks               2310
6.         Scottie Pippen               2307
7.         Clyde Drexler                2207
8.         Hakeem Olajuwon              2162
9.         Alvin Robertson              2112
10.        Karl Malone                  2085
11.        Mookie Blaylock              2075
12.        Allen Iverson                1983
13.        Derek Harper                 1957
14.        Kobe Bryant                  1944
15.        Chris Paul                   1873
16.        Isiah Thomas                 1861
17.        Kevin Garnett                1859
18.        Shawn Marion                 1759
19.        Paul Pierce                  1751
20.        Magic Johnson                1724
21.        LeBron James                 1723
-----------------Last Time------------------
21.        LeBron James                 1723
--------------------------------------------
3-pt Field Goals:
8.         Kyle Korver                  1978
9.         Joe Johnson                  1886
10.        Chauncey Billups             1830
11.        Kobe Bryant                  1827
12.        Stephen Curry                1795
13.        Rashard Lewis                1787
14.        Peja Stojakovic              1760
15.        Dirk Nowitzki                1733
16.        J.R. Smith                   1729
17.        Dale Ellis                   1719
18.        Steve Nash                   1685
19.        Jason Richardson             1608
20.        Mike Miller                  1586
21.        Glen Rice                    1559
22.        Eddie Jones                  1546
23.        Tim Hardaway                 1542
24.        Nick Van Exel                1528
25.        Mike Bibby                   1517
26.        Michael Finley               1454
27.        LeBron James                 1415
-----------------Last Time------------------
27.        LeBron James                 1415
--------------------------------------------
```

The program will show you the player's achievements, together with at most 20 players before him. The **Last Time** line will show you the Result you got last time so that you can make a comparison.

## Automation

You can always combine **crontab** and **mail** with this program to automate the whole thing to inform you the fresh news, here is the instance:

Use `contab -e` to open an edit window, and input stuff like this:

```
0 20 * * * python3 /home/predict/getpage.py "LeBron James" | mail -s "Data of LeBron today" YourEmail@domain.cc
```

By doing this,  you will receive an email at 8:00 pm everyday about the player's latest records.
