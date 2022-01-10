// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

@R1 // take val from RAM[1]
D=M
@times // store RAM[1] val into var; how many times need to add RAM[0] val
M=D
@R2
M=0 // init mult res
(LOOP)
    @times // curr times; init RAM[1]
    D=M
    @END // if times === 0 > go to end
    D;JEQ
    @R1 // decrement D by 1
    D=D-1 
    @times // store new (decremented) D val into times var
    M=D
    @R2 // take RAM[2] (curr res) val into data
    D=M
    @R0 // add RAM[0] to current res
    D=D+M
    @R2 // store current res in RAM[2]
    M=D
    @LOOP // continue loop
    0;JMP
(END)
    @END // infinite loop just to stop the program
    0;JMP
