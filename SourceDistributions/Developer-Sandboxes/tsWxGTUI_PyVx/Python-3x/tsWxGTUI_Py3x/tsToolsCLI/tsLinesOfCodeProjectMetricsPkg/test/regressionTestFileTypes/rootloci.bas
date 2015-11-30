1000 DIM G(50),H(50),C(50),M(10)
1010 PRINT"ROOTLOCI WILL CALCULATE AND/OR PLOT THE LOCUS OF ROOTS OF A" 
1015 PRINT"LINEAR CONTROL SYSTEM WITH NEGATIVE FEEDBACK.  THE OPEN LOOP"
1020 PRINT"TRANSFER FUNCTION 'GH' IS DEFINED BY A NUMERATOR POLYNOMIAL" 
1025 PRINT"AND A DENOMINATOR POLYNOMIAL.  EACH POLYNOMIAL IS ENTERED AS"
1030 PRINT"A SERIES OF POLYNOMIAL FACTORS OF THE FORM:" 
1035 PRINT  
1040 PRINT"A(0)+A(1)*S^(1)+ ... +A(N-1)*S^(N-1)+A(N)*S^(N)" 
1045 PRINT  
1050 PRINT"THE MAXIMUM DEGREE (N) OF ANY POLYNOMIAL IS 50.  THIS LIMIT" 
1055 PRINT"APPLIES IN PRACTICE TO THE POLYNOMIAL WHICH RESULTS FROM THE"
1056 PRINT"PRODUCT OF THE DENOMINATOR FACTORS." 
1060 PRINT  
1070 PRINT"THE USER MUST HAVE STORED OR ACCESS TO TWO ADDITIONAL PROGRAMS:" 
1080 PRINT"     LPLOTTER----- THE PLOTTING PROGRAM" 
1090 PRINT"     STORE-------- A STORAGE FILE"   
1100 PRINT  
1102 PRINT"FOR INFORMATION CALL: DICK GORDON,8*235-2914/ 8*235-4737"
1104 PRINT"     LARGE STEAM TURBINE DEPARTMENT" 
1106 PRINT"     BLD. 285  RM 231"   
1108 PRINT"     SCHENECTADY, NEW YORK"  
1110 PRINT  
1120 LET K=0
1130 FOR I=0 TO 9   
1140 M(I)=10.**(I/10.)  
1150 NEXT I 
1160 FILES STORE
1170 SCRATCH #1 
1180 PRINT"NUMERATOR OF GH";
1190 GOSUB 3270 
1200 LET N1=N0  
1210 FOR I=0 TO N1  
1220 LET G(I)=C(I)  
1230 NEXT I 
1240 PRINT"OPEN LOOP ZEROS" 
1250 GOSUB 1690 
1260 PRINT  
1270 PRINT"DENOMINATOR OF GH";  
1280 GOSUB 3270 
1290 LET N2=N0  
1300 FOR I=0 TO N2  
1310 LET H(I)=C(I)  
1320 NEXT I 
1330 PRINT"OPEN LOOP POLES" 
1340 GOSUB 1690 
1350 IF N1<=N2 THEN 1370
1360 LET N0=N1  
1370 PRINT  
1380 PRINT  
1390 PRINT  
1395 SCRATCH #1 
1400 PRINT"ENTER: INITIAL AND FINAL GAIN VALUES (K>0)"; 
1410 INPUT K0,K9
1420 K9=K9  
1430 PRINT"DO YOU WANT A TABULATION OF THE ROOTS";  
1440 INPUT A$   
1450 FOR D=0 TO 9   
1460 LET K=K0*M(D)  
1470 GOSUB 1580 
1480 IF K>=K9 THEN 1520 
1490 NEXT D 
1500 LET K0=10*K0   
1510 GOTO 1450  
1520 PRINT  
1530 PRINT"     ***** END OF CALCULATIONS *****"
1540 WRITE #1,1E33  
1550 CHAIN "LPLOTTER"   
1560 INPUT K0,K9
1570 GOTO 1420  
1580 FOR I=0 TO N0  
1590 LET S=0
1600 IF I>N1 THEN 1620  
1610 LET S=S+K*G(I) 
1620 IF I>N2 THEN 1640  
1630 LET S=S+H(I)   
1640 LET C(I)=S 
1650 NEXT I 
1660 IF A$="NO" THEN 1690   
1670 PRINT  
1680 PRINT"CLOSED LOOP POLES FOR K=";K;" (";20*LOG(K)/LOG(10);" DB)"
1690 LET N=N0   
1700 DIM B(50),D(50)
1710 LET N=N0   
1720 LET L1=-1  
1730 IF C(N)<>0 THEN 1760   
1740 LET N=N-1  
1750 IF N>0 THEN 1730   
1760 IF N>0 THEN 1790   
1770 PRINT"DEGREE IS ZERO, NO ROOTS"
1780 GOTO 3260  
1790 IF C(0)<>0 THEN 1880   
1800 IF A$="NO" THEN 1820   
1810 PRINT 0
1820 LET N=N-1  
1830 FOR I=0 TO N   
1840 LET C(I)=C(I+1)
1850 NEXT I 
1860 IF N>0 THEN 1790   
1870 IF N<=0 THEN 3260  
1880 IF N>1 THEN 1910   
1890 LET R=-C(1)/C(0)   
1900 GOTO 2670  
1910 IF N>2 THEN 1950   
1920 LET P=C(1)/C(0)
1930 LET Q=C(2)/C(0)
1940 GOTO 2810  
1950 LET P1=0   
1960 LET P2=0   
1970 LET Q1=0   
1980 LET Q2=0   
1990 LET X=1E-7 
2000 LET S=SQR(ABS(C(0)*C(N)))  
2010 FOR I=0 TO N   
2020 LET C(I)=C(I)/S
2030 NEXT I 
2040 IF ABS(C(1)/C(0))>=ABS(C(N-1)/C(N)) THEN 2120  
2050 LET L1=-L1 
2060 FOR I=0 TO (N-1)/2+.1  
2070 LET J=N-I  
2080 LET T=C(I) 
2090 LET C(I)=C(J)  
2100 LET C(J)=T 
2110 NEXT I 
2120 IF Q1=0 THEN 2160  
2130 LET P=P1   
2140 LET Q=Q1   
2150 GOTO 2240  
2160 LET P=C(N-2)   
2170 IF P<>0 THEN 2210  
2180 LET Q=1
2190 LET P=-2   
2200 GOTO 2230  
2210 LET Q=C(N-1)/P 
2220 LET P=Q-C(N-3)*Q/P 
2230 LET R=0
2240 FOR L2=1 TO 20 
2250 LET B(0)=C(0)  
2260 LET C1=B(0)
2270 LET D(0)=C(0)  
2280 LET B(1)=C(1)-B(0)*P   
2290 LET C2=B(1)-C1*P   
2300 LET D(1)=C(1)+R*D(0)   
2310 LET E1=D(1)+R*D(0) 
2320 FOR I=2 TO N-1 
2330 LET B(I)=C(I)-B(I-1)*P-B(I-2)*Q
2340 LET C0=C1  
2350 LET C1=C2  
2360 LET C2=B(I)-C1*P-C0*Q  
2370 LET D(I)=C(I)+R*D(I-1) 
2380 LET E0=E1  
2390 LET E1=D(I)+R*E0   
2400 NEXT I 
2410 LET T1=C(N)-P*B(N-1)-Q*B(N-2)  
2420 LET C2=-P*C1-Q*C0  
2430 LET T=C1*C1-C2*C0  
2440 LET P3=B(N-1)*C1-T1*C0 
2450 LET Q3=T1*C1-B(N-1)*C2 
2460 IF ABS(P3)>X*ABS(P*T) THEN 2480
2470 IF ABS(Q3)<=X*ABS(Q*T) THEN 2810   
2480 IF T<>0 THEN 2520  
2490 LET P=P-2  
2500 LET Q=Q*(Q+1)  
2510 GOTO 2540  
2520 LET P=P+P3/T   
2530 LET Q=Q+Q3/T   
2540 LET T=C(N)+R*D(N-1)
2550 IF ABS(T)<=X*ABS(R*E1) THEN 2670   
2560 IF E1<>0 THEN 2590 
2570 LET R=R-1  
2580 GOTO 2600  
2590 LET R=R-T/E1   
2600 NEXT L2
2610 LET P1=P2  
2620 LET Q1=Q2  
2630 LET P2=P   
2640 LET Q2=Q   
2650 LET X=10*X 
2660 GOTO 2050  
2670 IF L1>0 THEN 2690  
2680 LET R=1/R  
2690 IF A$="NO" THEN 2710   
2700 PRINT R
2710 H1=0   
2720 IF R>0 THEN 2740   
2730 H1=180 
2740 V1=ABS(R)  
2750 WRITE #1,V1,H1,20*LOG(K)/LOG(10)   
2760 LET N=N-1  
2770 FOR I=0 TO N   
2780 LET C(I)=D(I)  
2790 NEXT I 
2800 GOTO 1870  
2810 IF L1>0 THEN 2840  
2820 LET P=P/Q  
2830 LET Q=1/Q  
2840 LET T=P*P/4-Q  
2850 IF T>=0 THEN 3020  
2860 LET T1=-P/2
2870 LET T=SQR(-T)  
2880 LET S=SQR(ABS(Q))  
2890 IF A$="NO" THEN2920
2900 PRINT T1;"  + J";T;"   DAMPING FACTOR =";-T1/S 
2910 PRINT T1;"  - J";T;"    NATURAL FREQ. =";S 
2920 IF T1>0 THEN 2980  
2930 IF T1<0 THEN 2960  
2940 H1=90  
2950 GOTO 2990  
2960 H1=180-ATN(-T/T1)*180/3.14159265   
2970 GOTO 2990  
2980 H1=ATN(T/T1)*180/3.14159265
2990 V1=S   
3000 WRITE #1,V1,H1,20*LOG(K)/LOG(10)   
3010 GOTO 3210  
3020 LET T=SQR(T)+ABS(P)/2  
3030 IF P<0 THEN 3050   
3040 LET T=-T   
3050 IF A$="NO" THEN3070
3060 PRINT Q/T  
3070 IF (Q/T)<0 THEN 3100   
3080 IF (Q/T)>0 THEN 3120   
3090 GOTO 3130  
3100 WRITE #1,(-Q/T),180,20*LOG(K)/LOG(10)  
3110 GOTO 3130  
3120 WRITE #1,(Q/T),0,20*LOG(K)/LOG(10) 
3130 IF A$="NO" THEN 3150   
3140 PRINT T
3150 IF T<0 THEN 3180   
3160 IF T>0 THEN 3200   
3170 GOTO 3210  
3180 WRITE #1,-T,180,20*LOG(K)/LOG(10)  
3190 GOTO 3210  
3200 WRITE #1,T,0,20*LOG(K)/LOG(10) 
3210 LET N=N-2  
3220 FOR I=0 TO N   
3230 LET C(I)=B(I)  
3240 NEXT I 
3250 GOTO 1870  
3260 RETURN 
3270 LET N0=0   
3280 LET C(0)=1 
3290 PRINT":  HOW MANY FACTORS ARE THERE";  
3300 INPUT M
3310 FOR L=1 TO M   
3320 PRINT  
3330 PRINT"     FACTOR #";L;"IS OF WHAT DEGREE";
3340 INPUT M1   
3350 LET M2=N0+M1   
3360 FOR I=0 TO M2  
3370 LET H(I)=C(I)  
3380 LET C(I)=0 
3390 NEXT I 
3400 FOR I=0 TO M1  
3410 PRINT"          A(";I;") =";   
3420 INPUT X
3430 FOR J=0 TO N0  
3440 LET K=I+J  
3450 LET C(K)=C(K)+H(J)*X   
3460 NEXT J 
3470 NEXT I 
3480 LET N0=M2  
3490 NEXT L 
3500 PRINT"     DEGREE OF THE RESULTANT POLYNOMIAL IS:";N0  
3510 PRINT"     COEFFICIENTS OF RESULTANT POLYNOMIAL ARE (CONST. FIRST):";  
3520 FOR I=0 TO N0  
3530 PRINT C(I);
3540 NEXT I 
3550 PRINT  
3560 PRINT  
3570 RETURN 
3580 END
 
