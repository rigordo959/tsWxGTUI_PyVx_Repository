      PROGRAM F77TST
*
*        THIS BENCHMARK CONSISTS OF TEN MODULES, EACH OF WHICH
*        EXERCISES A GROUP OF LANGUAGE FEATURES.  EACH MODULE
*        IS PLACED IN A LOOP AND THE NUMBER OF TIMES IT IS
*        EXERCISED IS ADJUSTED TO MIMIC, AS CLOSELY AS POSSIBLE,
*        THE AVAILABLE STATISTICAL PROFILES OF LANGUAGE FEATURE
*        USAGE.  ALL THE LOOPS HAVE BEEN ARRANGED SO THAT AN
*        OPTIMIZING COMPILER CANNOT REMOVE A SIGNIFICANT AMOUNT
*        OF CODE FROM THEM.
*
*        FEATURES EXERCISED INCLUDE SIMPLE VARIABLE AND ARRAY
*        ADDRESSING, FIXED AND FLOATING POINT ARITHMETIC, SUB-
*        ROUTINE CALLS AND PARAMETER PASSING, AND STANDARD MATHE-
*        MATICAL FUNCTIONS.
*
**    DOUBLE PRECISION X1, X2, X3, X4, X, Y, Z, T, T1, T2, E1
      COMMON T, T1, T2, E1(4), J, K, L
*
      COMMON /UNITS/ CI, CO
      INTEGER CI, CO
*
***** CHANGE FOR SYSTEM COMPATIBILITY *****
*
      CI = 5
      CO = 6
*
***** OPEN ( UNIT=CI, FILE=':CI:' )
***** OPEN ( UNIT=CO, FILE=':CO:', CARRIAGE='FORTRAN' )
      OPEN ( UNIT=CI )
      OPEN ( UNIT=CO )
*
*******************************************
*
      WRITE ( UNIT=CO, FMT=905 )
905   FORMAT ( '"F77TST" FORTRAN-77 Benchmark V2.0', //,
     &         1X, 'NUMBER OF BITS/INTEGER WORD: ', $ )
*
      READ ( UNIT=CI, FMT=* ) NBITS
910   FORMAT ( I2 )
*
***** CHANGE FOR MAXIMUM ITERATION COUNT *****
      I = INT( ( 2.0**(NBITS-1) ) - 1.0 ) / 899
**********************************************
*
      I1=I/2
      I2=I
      IRUN=0
*
***** START OF THE TIMING ROUTINE *****
      CALL TIMRB
*****                             *****
* AFTER EACH TIMED LOOP, MAIN PROGRAM COMES HERE
979   T =0.499975
      T1=0.50025
      T2=2.0
      IRUN=IRUN+1
      GOTO ( 977, 978, 1000) IRUN
977   I =I1
      WRITE ( UNIT=CO, FMT=700) I
700   FORMAT ( 'FIRST RUN, I = ', I6 )
      GOTO 908
978   I = I2
      WRITE ( UNIT=CO, FMT=705 ) I
705   FORMAT ( 'SECOND RUN, I = ', I6 )
      ZAP1=DELTA
      GOTO 908
* MAIN LOOP START TIMING
908   TIME=SECNDS(0.)
*
      ISAV=I
      N1=0
      N2=12*I
      N3=14*I
      N4=345*I
      N5=0
      N6=210*I
      N7=32*I
      N8=899*I
      N9=616*I
      N10=0
      N11=93*I
      N12=0
*
      X1=1.0
      X2=-1.0
      X3=-1.0
      X4=-1.0
*
      IF ( N1 ) 19, 19, 11
11    DO 18 I=1, N1, 1
            X1=(X1+X2+X3-X4)*T
            X2=(X1+X2-X3+X4)*T
            X4=(-X1+X2+X3+X4)*T
            X3=(X1-X2+X3+X4)*T
18    CONTINUE
19    CONTINUE
      CALL POUT( N1, N1, N1, X1, X2, X3, X4 )
      E1(1)=1.0
      E1(2)=-1.0
      E1(3)=-1.0
      E1(4)=-1.0
      IF ( N2 ) 29, 29, 21
21    DO 28 I=1, N2, 1
            E1(1)=(E1(1)+E1(2)+E1(3)-E1(4))*T
            E1(2)=(E1(1)+E1(2)-E1(3)+E1(4))*T
            E1(3)=(E1(1)-E1(2)+E1(3)+E1(4))*T
            E1(4)=(-E1(1)+E1(2)+E1(3)+E1(4))*T
28    CONTINUE
29    CONTINUE
      CALL POUT( N2, N3, N2, E1(1), E1(2), E1(3), E1(4) )
*
      IF ( N3 ) 39, 39, 31
31    DO 38 I=1, N3, 1
38    CALL PA( E1 )
39    CONTINUE
      CALL POUT( N3, N2, N2, E1(1), E1(2), E1(3), E1(4) )
*
      J=1
*
      IF ( N4 ) 49, 49, 41
41    DO 48 I=1, N4, 1
            IF ( J-1 ) 43, 42, 43
42          J=2
            GOTO 44
43          J=3
44          IF ( J-2 ) 46, 46, 45
45          J=0
            GOTO 47
46          J=1
47          IF ( J-1 ) 411, 412, 412
411         J=1
            GOTO 48
412         J=0
48    CONTINUE
49    CONTINUE
      CALL POUT( N4, J, J, X1, X2, X3, X4 )
*
      J=1
      K=2
      L=3
*
      IF ( N6 ) 69, 69, 61
61    DO 68 I=1, N6, 1
            J=J*( K-J )*( L-K )
            K=L*K-( L-J )*K
            L=( L-K )*( K+J )
            E1( L-1 )=J+K+L
            E1( K-1 )=J*K*L
68    CONTINUE
69    CONTINUE
      CALL POUT( N6, J, K, E1(1), E1(2), E1(3), E1(4))
*
      X=0.5
      Y=0.5
*
      IF ( N7 ) 79, 79, 71
71    DO 78 I=1, N7, 1
*           X=T*DATAN(T2*DSIN(X)*DCOS(X)/(DCOS(X+Y)+DCOS(X-Y)-1.0D0))
            X=T*ATAN(T2*SIN(X)*COS(X)/(COS(X+Y)+COS(X-Y)-1.0))
*           Y=T*DATAN(T2*DSIN(Y)*DCOS(Y)/(DCOS(X+Y)+DCOS(X-Y)-1.0D0))
            Y=T*ATAN(T2*SIN(Y)*COS(Y)/(COS(X+Y)+COS(X-Y)-1.0))
78    CONTINUE
79    CONTINUE
      CALL POUT( N7, J, K, X, X, Y, Y )
*
      X=1.0
      Y=1.0
      X=1.0
*
      IF ( N8 ) 89, 89, 81
81    DO 88 I=1, N8, 1
88    CALL P3( X, Y, Z )
89    CONTINUE
      CALL POUT( N8, J, K, X, Y, Z, Z )
*
      J=1
      K=2
      L=3
      E1(1)=1.0
      E1(2)=2.0
      E1(3)=3.0
*
      IF ( N9 ) 99, 99, 91
91    DO 98 I=1, N9, 1
98    CALL P0
99    CONTINUE
      CALL POUT( N9, J, K, E1(1), E1(2), E1(3), E1(4) )
      J=2
      K=3
      IF ( N10 ) 109, 109, 101
101   DO 108 I=1, N10, 1
      J=J+K
      K=J+K
      J=J-K
      K=K-J-J
108   CONTINUE
109   CONTINUE
      CALL POUT( N10, J, K, X1, X2, X3, X4 )
      X=0.75
      IF ( N11 ) 119, 119, 111
111   DO 118 I=1, N11, 1
*118  X=DSQRT(DEXP(DLOG(X)/T1))
118   X=SQRT(EXP(ALOG(X)/T1))
119   CONTINUE
      CALL POUT( N11, J, K, X, X, X, X )
      DELTA=SECNDS( TIME )
* END MAIN TIMED LOOP
***** END OF THE TIMING ROUTINE *****
      CALL TIMRE
*****                    *****
      WRITE ( UNIT=CO, FMT=920 ) DELTA
920   FORMAT ( 'ELAPSED TIME (IN SECONDS) =', 1PE16.8 )
      GOTO 979
* FINISH UP
1000  ZAP2=DELTA
*     SPEED= 1000./(ZAP2-ZAP1)
      SPEED= 100.0*(I2-I1)/(ZAP2-ZAP1)
      WRITE ( UNIT=CO, FMT=930 ) SPEED
930   FORMAT ( 'SPEED = ', 1PE16.8 )
* F4+ STATEMENT
      CALL EXIT
      CLOSE ( UNIT=CI )
      CLOSE ( UNIT=CO )
      END
*
      SUBROUTINE POUT( N, J, K, X1, X2, X3, X4 )
*
      COMMON /UNITS/ CI, CO
      INTEGER CI, CO
*
*     DOUBLE PRECISION X1,X2,X3, X4
      WRITE ( UNIT=CO, FMT=1 ) N, J, K, X1, X2, X3, X4
1     FORMAT ( 1H , 3I7, 4E12.4 )
      RETURN
      END
*
      SUBROUTINE P0
*     DOUBLE PRECISION T, T1, T2, E1
      COMMON T, T1, T2, E1(4), J, K, L
      E1(J)=E1(K)
      E1(K)=E1(L)
      E1(L)=E1(J)
      RETURN
      END
*
      SUBROUTINE P3( X, Y, Z )
*     DOUBLE PRECISION T, T1, T2, X1, Y1, X, Y, Z
      COMMON T, T1, T2
      X1=X
      Y1=Y
      X1=T*(X1+Y1)
      Y1=T*(X1+Y1)
      Z=(X1+Y1)/T2
      RETURN
      END
*
      SUBROUTINE PA(E)
*     DOUBLE PRECISION T, T1, T2, E
      COMMON T, T1, T2
      DIMENSION E(4)
      J=0
1     E(1)=(E(1)+E(2)+E(3)-E(4))*T
      E(2)=(E(1)+E(2)-E(3)+E(4))*T
      E(3)=(E(1)-E(2)+E(3)+E(4))*T
      E(4)=(-E(1)+E(2)+E(3)+E(4))/T2
      J=J+1
      IF ( J-6 ) 1, 2, 2
2     CONTINUE
      RETURN
      END
*
**********************************************************************
 
      SUBROUTINE EXIT
*
      COMMON /UNITS/ CI, CO
      INTEGER CI, CO
*
      COMMON /CLOCK/ ON, OFF
      WRITE ( UNIT=CO, FMT=1 ) ON, OFF, OFF-ON
1     FORMAT ( 'STARTED=', F8.3,
     &         ' STOPPED=', F8.3, ' HOURS=', F8.3 )
      STOP
      END
*
      SUBROUTINE TIMRB
      COMMON /CLOCK/ ON, OFF
      ON = BCLK()
      OFF = ON
      RETURN
      END
*
      FUNCTION SECNDS( TIME )
      SECNDS = BCLK()*3600.0 - TIME
      RETURN
      END
*
      SUBROUTINE TIMRE
      COMMON /CLOCK/ ON, OFF
      OFF = BCLK()
      RETURN
      END
*
      FUNCTION BCLK()
*
******************************************************
***** DETERMINE TIME OF DAY AS MEASURED IN HOURS *****
*****     NOTE: MANUAL TIMEKEEPING HAS           *****
*****           BEEN PRESUMED FOR THIS           *****
*****           IMPLIMENTATION                   *****
******************************************************
*
      BCLK = 0.0
      RETURN
      END

