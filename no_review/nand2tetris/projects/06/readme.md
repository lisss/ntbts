### Instructions
A-instruction: opcode 0 + decimal-to-binary <br/>
C-instruction: <br/>
dest = comp ; jump <br/>
111 a c1 c2 c3 c4 c5 c6 d1 d2 d3 j1 j2 j3 <br/>
e.g. `MD=D+1` -> `1110011111011000`

### Symbols
- variables (`@sum`):<br>
    - each variable is assigned a unique memory address starting with `16`
    - if you see it for the first time - assign a memory address
    - otherwise, replace symbol with its value
    - translate A-instruction
- labels (`(LOOP)`): <br>
    - translate name to memory location holding the next instruction in the program
    - replace `@LOOP` with its value (e.g. `@4`)
    - translate A-instruction
- predefined symbols (`SCREEN`, `@R1`): <br>
    - translate to decimal using table -> will receive simple A-instruction
    - translate A-instruction

### Symbol table (ST)
1. create empty table
2. populate with predefined symbols
3. **1st pass:** go though the file, keep counting lines, look for lable declarations, assign the value of counter to the label, add to the ST
4. **2nd pass:** do the same as in p. 3 for variables


### Overal logic
1. Init:
- parser
- symbol table
2. First pass: read all commands only paying attentions to labels and updating the symbol table
3. Second pass: translate commands
