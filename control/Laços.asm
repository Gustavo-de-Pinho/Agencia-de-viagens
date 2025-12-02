.data
	msg: .asciiz "Insira um número: "
	msgfinal: .asciiz "Chegamos ao fim"
	quebra: .asciiz "\n"
.text
	li $v0, 4 #mensagem inicial
	la $a0, msg
	syscall
	
	li $v0, 5 #lendo número inteiro
	syscall #esse número vai ser o limite do contador
	
	move $t0, $v0 #salvando valor em t0
	move $t1, $zero #salvando 0 em t1,será o contador
	
	while:
		beq $t0,$t1, saida #quando t0 for igual t1, sai do loop
		
		li $v0, 1 #imprimindo int, o valor atual de t0
		move $a0, $t1 #tem que ser move, prque é de registrador pra registrador
		syscall
		
		li $v0, 4 #Quebra de linha
		la $a0, quebra
		syscall
		
		addi $t1, $t1, 1 #somando em t0
		j while #jump de volta para o ehile
	saida:
		li $v0, 1 #imprimindo o valor final
		move $a0, $t1
		syscall
		
		li $v0, 4 #Quebra de linha
		la $a0, quebra
		syscall
		
		li $v0, 4 #mensagem final
		la $a0, msgfinal
		syscall