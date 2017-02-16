$	TITLE ('SUBROUTINE XMITR')
;
; "XMITR" writes a character to the USART serving as the data link transmitter.
;
; ENTRY CONDITIONS:
;
;	C	-	8-BIT CHARACTER TO BE TRANSMITTED
;
; EXIT CONDITIONS:
;
;	NONE
;
; ROUTINES CALLED:
;
;	NONE
;
; ROUTINE CALLED BY:
;
;	"ENCODE"
;
; STACK REQUIRED:
;
;	0-BYTES
;
; SYMBOLIC VARIABLE DEFINITIONS:
;
	NAME	XMITR
	PUBLIC	XMITR
;
PORTI	EQU	0A000H	;DATA LINK USART INPUT DATA PORT
PORTO	EQU	PORTI	;DATA LINK USART OUTPUT DATA PORT
PORTS	EQU	PORTI+1 ;DATA LINK USART STATUS DATA INPUT PORT
PORTC	EQU	PORTS	;DATA LINK USART CONTROL DATA OUTPUT PORT
RESET	EQU	PORTI+2 ;DATA LINK USART RESET CONTROL PORT
;
$EJECT
;
; 8251 USART STATUS BIT ASSIGNMENT
;
TXRDY	EQU	00000001B ;USART OUTPUT READY MASK
RBR	EQU	00000010B ;USART INPUT READY MASK
TBE	EQU	00000100B ;USART TRANSMITTER EMPTY MASK
RPAR	EQU	00001000B ;USART RECEIVE PARITY ERROR MASK
ROV	EQU	00010000B ;USART RECEIVE OVERRUN ERROR MASK
RFR	EQU	00100000B ;USART RECEIVE FRAMING ERROR MASK
DSR	EQU	10000000B ;USART DATA SET READY MASK
;
	CSEG
;
XMITR:			;C = CHARACTER TO BE TRANSMITTED
	;
	; WAIT FOR TRANSMITTER TO EMPTY
	;
	LDA	PORTS	;READ DATA LINK STATUS PORT
	ANI	TXRDY	;TEST IF TRANSMITTER READY FOR INPUT DATA
	JZ	XMITR	;LOOP UNTIL TRANSMITTER READY
	;
	; WRITE ACTUAL CHARACTER
	;
	MOV	A,C	;LOAD CHARACTER TO BE OUTPUT
	STA	PORTO	;WRITE TO DATA LINK USART OUTPUT PORT
	;
	RET		;EXIT XMITR
;
	END