      program vdap
*****     & (), "TOOLS" cade-pnXXXs0.0 <870111.1115>
*
      dimension R(6),T(6),RES(6,3),RSTEP(6),Z1(3,3),Z2(3,3),Z3(3)
      dimension VTP2(3)
      REAL ICR,ILOAD
      INTEGER CRCASE
      integer ci, co
          parameter ( ci = 5 )
          parameter ( co = 6 )
      character*4 ANS,DWRGID
*     ALPHA ANS,DWRGID
*
* STATEMENT FUNCTIONS USED TO DEFINE THE VOLTAGE ACROSS THE LOAD
      G1(A1,A2,A3)=1.0/(1.0+(A1*(A2+A3)/(A2*A3)))
      G2(A1,A2,A3)=1.0/(1.0+(A2*(A1+A3)/(A1*A3)))
      E3(A1,A2,A3,E1,E2)=G1(A1,A2,A3)*E1+G2(A1,A2,A3)*E2
*
*****      call fsysu( 1,1 )
*      open ( ci, file='sys$input', status='unknown' )
*      open ( co, file='sys$output', status='unknown' )
*
      print *,'          Voltage Divider Analysis Program'
      print *,'          ================================'
      print *,' '
      print *,' '
      print *,'    Do you want a description of the program ? _'
      read ( ci, * ) ANS
      if (ANS.eq.'NO') goto 1
      print *,'   VDAP is a program for analizing voltage divider'
      print *,'networks consisting of upto:  three variable resistors,'
      print *,'two fixed resistors, an optional diode, a load resistor,'
      print *,'and two power supplies.'
      print *,' '
      print *,'   The program calculates the nominal voltage across the'
      print *,'load elements and the deviation from the nominal, due'
      print *,'to component tolerances.  Component tolerances for'
      print *,'resistors are entered during the execution of the pro-'
      print *,'gram as a percentage deviation from  the nominal value.'
      print *,'Diode characteristics are contained in a subroutine and'
      print *,'represent the 1N457 maximum and minimum voltage-current'
      print *,'characteristics. Diode may be foward or reverse biased'
      print *,'within the ratings for the device.'
      print *,' '
      print *,'   Running time is considerably lengthened when circuit'
      print *,'contains diode and especially when variable resistors do'
      print *,'also. Scores of computer CRUs are used when the circuit'
      print *,'contains only three fixed resistors and a diode.  Same'
      print *,'circuit, less the diode uses only a couple of CRUs.'
      print *,' '
      print *,'   Voltage V1 is voltage across both the diode and the'
      print *,'resistor.  Voltage V2 is printed only when diode is in'
      print *,'the circuit, and it represents voltage across the re-'
      print *,'sistor.  Maximum and minimum values of V2 do not occur'
      print *,'at maximum and minimum values of V1.  In order to per-'
      print *,'mit determination of V2 at a given value of V1, the'
      print *,'program provides V1 specification routine and suplemen-'
      print *,'tary output.'
      print *,' '
      print *,'   F1, F3 and represent wiper positions of variable'
      print *,'resistors R1, R3 and R5 respectively.'
      print *,' '
      print *,'   Drawing 372HA217 shows the circuit schematic.'
      print *,' '
      print *,'   R.S.Gordon, January 5, 1973 (Rev. 01/17/2010)'
      print *,' '
      print *,' '
1     continue
      print *,
     &    '************************************************************'
      print *,'DRAWING NUMBER ? _'
      read ( ci, * ) DWRGID
      DWRGID=' '
      print *,'ENTER SUPPLY VOLTAGES E1 AND E2 ? _'
      read ( ci, * )  E1,E2
*****      goto 33
      print *,'   ORIENTATION CODE FOR DIODE'
      print *,'     DIODE ABSENT....0'
      print *,'     FACING LEFT....-1'
      print *,'     FACING RIGHT....1'
      print *,' '
      print *,'ENTER ORIENTATION ? _'
      read ( ci, * ) ORIENT
33    ORIENT=0
      print *,' '
      DO 100 I=1,6
      print 10,I
10    format (1X, 'FOR R(',I1, ') ENTER: RESISTANCE ? _' )
      read ( ci, * ) R(I)
      IF(R(I).gt.0.0) goto 90
      T(I)=0.0
      RSTEP(I)=1.0
      goto 95
90    print 11
11    format (1H+,15X, '% TOLERANCE ? _' )
      read ( ci, * ) T(I)
      if ((I.eq.2).or.(I.eq.4).or.(I.eq.6)) goto 95
      print 12
12    format (1H+,15X,'F STEP SIZE ? _' )
      read ( ci, * ) RSTEP(I)
95    continue
      RES(I,1)=R(I)*(1.-T(I)/100.)
      RES(I,2)=R(I)
      RES(I,3)=R(I)*(1.+T(I)/100.)
100   continue
      print *,DWRGID
      print 601
601   format (3X,2HF1,5X,2HF3,5X,2HF5,7X,2HV1,7X,6HV1 TOL,7X,2HV2
     &     ,7X,6HV2 TOL)
      print 602
602   format (1X,64(1H-))
      ISTEP=RSTEP(3)*100.+.5
      JSTEP=RSTEP(1)*100.+.5
      KSTEP=RSTEP(5)*100.+.5
         if (R(5).eq.0.0) KS=1
         if (R(5).NE.0.0) KS=101
         DO 500 K=1,KS,KSTEP
         AK=K-1
         F5=AK/100.
         if (R(1).eq.0.0) JS=1
         if (R(1).NE.0.0) JS=101
         DO 500 J=1,JS,JSTEP
         AJ=J-1
         F1=AJ/100.
         if (R(3).eq.0.0) IS=1
         if (R(3).NE.0.0) IS=101
         DO 500 I=1,IS,ISTEP
         AI=I-1
         F3=AI/100.
         DO 101 N2=1,3
         Z3(N2)=RES(6,N2)
         DO 101 N1=1,3
         Z1(N1,N2)=F1*RES(1,N1)+RES(2,N1)+F3*RES(3,N2)
         Z2(N1,N2)=(1.0-F3)*RES(3,N1)+RES(4,N2)+F5*RES(5,N2)
101      continue
         if (Z1(2,2).gt.0.0) goto 110
         E3MAX=E1
         E3MIN=E1
         goto 190
110      if (Z2(2,2).gt.0.0) goto 120
         E3MAX=E2
         E3MIN=E2
         goto 190
120      continue
         if (((R(1)*T(1)).eq.0.0).AND.((R(2)*T(2)).eq.0.0)) N1LIM=1
         if (((R(1)*T(1)).NE.0.0).or.((R(2)*T(2)).NE.0.0)) N1LIM=3
         DO 180 N1=1,N1LIM
         if ((R(3)*T(3)).eq.0.0) N2LIM=1
         if ((R(3)*T(3)).NE.0.0) N2LIM=3
         DO 180 N2=1,N2LIM
         if (((R(4)*T(4)).eq.0.0).AND.((R(5)*T(5)).eq.0.0)) N3LIM=1
         if (((R(4)*T(4)).NE.0.0).or.((R(5)*T(5)).NE.0.0)) N3LIM=3
         DO 180 N3=1,N3LIM
         if ((R(6)*T(6)).eq.0.0) N4LIM=1
         if ((R(6)*T(6)).NE.0.0) N4LIM=3
         DO 180 N4=1,N4LIM
         if (ORIENT.eq.0.0) N5LIM=1
         if (ORIENT.NE.0.0) N5LIM=3
         DO 180 N5=1,N5LIM
         CRCASE=N5
         V1=E3(Z1(N1,N2),Z2(N2,N3),Z3(N4),E1,E2)
         VNOLOAD=E3(Z1(N1,N2),Z2(N2,N3),1.0E30,E1,E2)
         if (ORIENT.eq.0.0) goto 170
         V1=(V1+VNOLOAD)/2.0
      DO 160 N=1,10
         CALL LOAD(V1,ORIENT,CRCASE,Z3(N4),Z3EQ,V2)
         V=E3(Z1(N1,N2),Z2(N2,N3),Z3EQ,E1,E2)
160      V1=(V+V1)/2.0
170      if ((N1*N2*N3*N4*N5).eq.1) E3MAX=V1
         if ((N1*N2*N3*N4*N5).eq.1) E3MIN=V1
         if ((N1*N2*N3*N4*N5).eq.1) V2MAX=V2
         if ((N1*N2*N3*N4*N5).eq.1) V2MIN=V2
         E3MAX=AMAX1(E3MAX,V1)
         E3MIN=AMIN1(E3MIN,V1)
         V2MAX=AMAX1(V2MAX,V2)
         V2MIN=AMIN1(V2MIN,V2)
180      continue
190      V1=0.5*(E3MAX+E3MIN)
         V1TOL=0.5*(E3MAX-E3MIN)
         V2=0.5*(V2MAX+V2MIN)
         V2TOL=0.5*(V2MAX-V2MIN)
         print 400,F1,F3,F5,V1,V1TOL
400      format (2X,3(F4.2,3X),F8.4,3X,F8.4)
         if (ORIENT.eq.0.0) goto 500
         if ((V1.NE.E1).AND.(V1.NE.E2)) goto 412
410      DO 411 N6=1,3,2
         CRCASE=N6
411      CALL LOAD(V1,ORIENT,CRCASE,Z3(N6),Z3EQ,VTP2(N6))
         V2=(VTP2(1)+VTP2(3))/2.0
         V2TOL=ABS(VTP2(1)-VTP2(3))/2.0
412      print 420,V2,V2TOL
420      format (1H+,45X,F8.4,3X,F8.4)
500      continue
      if (ORIENT.eq.0.0) goto 599
      print *,' '
      print 602
      print *,'ENTER V1 SET POINT ? _'
      read ( ci, * ) V1
      DO 550 N6=1,3,2
      CRCASE=N6
         CALL LOAD(V1,ORIENT,CRCASE,Z3(N6),Z3EQ,VLOAD)
550      VTP2(N6)=VLOAD
      V2=(VTP2(1)+VTP2(3))/2.0
      V2TOL=ABS(VTP2(1)-VTP2(3))/2.0
      print 560,V2,V2TOL
560   format (1H+,45X,F8.4,3X,F8.4)
      print *,' '
599   print 600
600   format (1H-, '*** DO YOU WISH TO RUN ANOTHER NETWORK *** ? _' )
      read ( ci, * ) ANS
      if (ANS.eq.'YES') goto 1
      STOP
      end
*
      SUBROUTINE LOAD(V1,ORIENT,CRCASE,RL,RLEQ,V2)
*          THIS ROUTINE USES THE HALF INTERVAL SEARCH
*          METHOD TO DETERMINE THE LOAD CURRENT AND
*          THE VOLTAGE DROP ACROSS THE DIODE.  A SOL-
*          UTION IS CONSIDERED SATISFACTORY if THE
*          DIODE DROP DUE TO THE ASSUMED CURRENT IS
*          WITHIN  E*(V1-V2), WHERE V2=I*R.  THE VAL-
*          UE OF E WAS SELECTED TO  USE THE LEAST NUM-
*          BER OF ITERATIONS AND PRODUCE AN ANSWER
*          WHICH IS ACCURATE TO 0.01 PERCENT OF THE
*          DIODE DROP.
*
         REAL     ICR,ILOAD,IRLIM,IFLIM
         INTEGER  CRCASE
         character*4 CRID
*        ALPHA    CRID
         F(V1,V2,VDIODE)=V1-V2-VDIODE
         E=1.0E-4
         CRID='CR1 '
         if (V1*ORIENT) 100,200,300
*        REVERSE BIASED DIODE
100      if (CRCASE.eq.1) IRLIM=3.1E-10
         if (CRCASE.eq.2) IRLIM=4.6E-10
         if (CRCASE.eq.3) IRLIM=7.5E-10
         if (ABS(V1).gt.(100.0+RL*IRLIM)) goto 800
         XLEFT=-IRLIM
         XRIGHT=0.0
         goto 400
200      V2=V1
         RLEQ=RL
         RETURN
*        FOWARD BIASED DIODE
300      if (CRCASE.eq.1) VFLIM=1.12
         if (CRCASE.eq.2) VFLIM=1.04
         if (CRCASE.eq.3) VFLIM=0.97
         if (ABS(V1).gt.(0.5*RL+VFLIM)) goto 800
         IFLIM=0.5
         XLEFT=0.0
         XRIGHT=IFLIM
         goto 400
400      V2LEFT=RL*XLEFT*ORIENT
         CALL CR1N457(CRID,1,CRCASE,XLEFT,VDLEFT)
         FA=F(V1,V2LEFT,VDLEFT*ORIENT)
410      X=(XLEFT+XRIGHT)/2.0
         V2=RL*X*ORIENT
         CALL CR1N457(CRID,1,CRCASE,X,VCR)
         VDIODE=VCR*ORIENT
         FX=F(V1,V2,VDIODE)
         if (FX) 500,700,500
500      if ((V1.NE.0.0).AND.(V1.eq.V2)) goto 505
         if (ABS(FX/(V1-V2)).le.E) goto 700
505      if (FA*FX) 510,700,520
510      XRIGHT=X
         goto 410
520      XLEFT=X
         FA=FX
         goto 410
700      ILOAD=V2/RL
         if (ILOAD.eq.0.0) RLEQ=1.0E30
         if (ILOAD.NE.0.0) RLEQ=V1/ILOAD
         RETURN
800      print *,'     ALARM FOR OVER VOLTAGE:  V1=',V1
         STOP
         END
*
*
         SUBROUTINE CR1N457(CRID,INDVAR,CRCASE,I,V)
         dimension VFTAB1(15),VFTAB2(15),VFTAB3(15),VFTAB(15),VRTAB(15)
         REAL I,I0,IFTAB(15),IRTAB1(15),IRTAB2(15),IRTAB3(15),IRTAB(15)
         INTEGER CRCASE
         character*4 CRID
*        ALPHA CRID
         if (VRTAB(2)/VRTAB(1).NE.2.) I0=25.E-9
         NDP=15
         NDP1=NDP-1
         goto (100,120,140),CRCASE
100      DO 110 N=1,NDP
         IRTAB(N)=IRTAB1(N)
110      VFTAB(N)=VFTAB1(N)
         goto 200
120      DO 130 N=1,NDP
         IRTAB(N)=IRTAB2(N)
130      VFTAB(N)=VFTAB2(N)
         goto 200
140      DO 150 N=1,NDP
         IRTAB(N)=IRTAB3(N)
150      VFTAB(N)=VFTAB3(N)
         goto 200
200      if (VRTAB(2)/VRTAB(1).eq.2.)
     &       I0=-(IRTAB(1)**2)/(IRTAB(2)-2.*IRTAB(1))
         goto (210,220),INDVAR
210      if (I) 300,350,400
220      if (V) 450,500,550
300      if (-I.ge.IRTAB(1)) goto 305
         V=-VRTAB(1)*ALOG(1.+I/I0)/ALOG(1.-IRTAB(1)/I0)
         RETURN
305      if (-I.gt.IRTAB(NDP)) goto 340
         DO 320 N=1,NDP1
         if ((-I.lt.IRTAB(N)).or.(-I.gt.IRTAB(N+1))) goto 320
         RSLOPE=(VRTAB(N+1)-VRTAB(N))/ALOG(IRTAB(N+1)/IRTAB(N))
         RINTCPT=VRTAB(N+1)-RSLOPE*ALOG(IRTAB(N+1))
         V=-(RSLOPE*ALOG(-I)+RINTCPT)
         RETURN
320      continue
340      print 345,CRID
345      format (6X,A4,30H-- OPERATING AT MAXIMUM RATING)
         V=-VRTAB(NDP)
         RETURN
350      V=0
         RETURN
400      if (I.ge.IFTAB(1)) goto 405
         V=VFTAB(1)*ALOG(1.+I/I0)/ALOG(1.+IFTAB(1)/I0)
         RETURN
405      if (I.gt.IFTAB(NDP)) goto 440
         DO 420 N=1,NDP1
         if ((I.lt.IFTAB(N)).or.(I.gt.IFTAB(N+1))) goto 420
         FSLOPE=(VFTAB(N+1)-VFTAB(N))/ALOG(IFTAB(N+1)/IFTAB(N))
         FINTCPT=VFTAB(N+1)-FSLOPE*ALOG(IFTAB(N+1))
         V=FSLOPE*ALOG(I)+FINTCPT
         RETURN
420      continue
440      print 345,CRID
         V=VFTAB(NDP)
         RETURN
450      if (-V.ge.VRTAB(1)) goto 455
         RSLOPE=-ALOG(1.0-IRTAB(1)/I0)/VRTAB(1)
         I=I0*(EXP(RSLOPE*V)-1.0)
         RETURN
455      if (-V.gt.VRTAB(NDP)) goto 490
         DO 470 N=1,NDP1
         if ((-V.lt.VRTAB(N)).or.(-V.gt.VRTAB(N+1))) goto 470
         RSLOPE=ALOG(IRTAB(N+1)/IRTAB(N))/(VRTAB(N+1)-VRTAB(N))
         RINTCPT=ALOG(IRTAB(N+1))-RSLOPE*VRTAB(N+1)
         I=-EXP(RSLOPE*(-V)+RINTCPT)
         RETURN
470      continue
490      print 345,CRID
         I=-IRTAB(NDP)
         RETURN
500      I=0
         RETURN
550      if (V.ge.VFTAB(1)) goto 555
         FSLOPE=ALOG(1.+IFTAB(1)/I0)/VFTAB(1)
         I=I0*(EXP(V*FSLOPE)-1.0)
         RETURN
555      if (V.gt.VFTAB(NDP)) goto 590
         DO 570 N=1,NDP1
         if ((V.lt.VFTAB(N)).or.(V.gt.VFTAB(N+1))) goto 570
         FSLOPE=ALOG(IFTAB(N+1)/IFTAB(N))/(VFTAB(N+1)-VFTAB(N))
         FINTCPT=ALOG(IFTAB(N+1))-FSLOPE*VFTAB(N+1)
         I=EXP(FSLOPE*V+FINTCPT)
         RETURN
570      continue
590      print 345,CRID
         I=IFTAB(NDP)
         RETURN
         DATA IFTAB/1.E-5,2.E-5,5.E-5,1.E-4,2.E-4,5.E-4,
     &     1.E-3,2.E-3,5.E-3,
     &     1.E-2,2.E-2,5.E-2,1.E-1,2.E-1,5.E-1/
         DATA VFTAB3/0.425,0.450,0.480,0.505,0.525,0.560,
     &     0.590,0.618,0.660,
     &     0.690,0.725,0.780,0.830,0.885,0.970/
         DATA VFTAB2/0.475,0.495,0.525,0.550,0.575,0.610,
     &     0.640,0.670,0.710,
     &     0.750,0.790,0.840,0.900,0.955,1.040/
         DATA VFTAB1/0.510,0.530,0.565,0.590,0.618,0.660,
     &     0.690,0.720,0.768,
     &     0.800,0.840,0.900,0.950,1.020,1.120/
         DATA VRTAB/5.,10.,15.,20.,25.,30.,35.,40.,45.,
     &     50.,60.,70.,80.,90.,100./
         DATA IRTAB1/7.0E-11,8.5E-11,1.0E-10,1.1E-10,1.25E-10,1.35E-10,
     &     1.45E-10,1.55E-10,1.65E-10,1.77E-10,2.0E-10,2.2E-10,2.5E-10,
     &     2.8E-10,3.1E-10/
         DATA IRTAB2/1.15E-10,1.3E-10,1.5E-10,1.7E-10,1.85E-10,2.0E-10,
     &     2.2E-10,2.4E-10,2.55E-10,2.7E-10,3.0E-10,3.4E-10,3.7E-10,
     &     4.1E-10,4.6E-10/
         DATA IRTAB3/2.0E-10,2.4E-10,2.7E-10,3.0E-10,3.3E-10,3.6E-10,
     &     3.9E-10, 4.1E-10,
     &     4.4E-10,4.6E-10,5.0E-10,5.6E-10,6.2E-10,6.8E-10,7.5E-10/
         END
