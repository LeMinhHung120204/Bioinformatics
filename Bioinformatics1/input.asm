lable:
add $a1, $t0, $s3
andi $1, $16, 19
test:
slti $21, $fp, -19
sw $s3, -24($a0)
beq $a0, $ra, lable
jal lable
j test