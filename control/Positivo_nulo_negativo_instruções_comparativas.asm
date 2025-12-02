.data
	msg: .asciiz "Insira um número: "
	maior: .asciiz "O número é maior que 0"
	igual: .asciiz "O número é igual a 0"
	menor: .asciiz "O número é menor que 0"
	
.text
	li $v0, 4 #mensagem inicial
	la $a0, msg
	syscall
	
	li $v0, 5 #lendo número inteiro
	syscall
	
	move $t0, $v0
	
	bgt $t0, $zero, imprimemaior	#se for maior
	beq $t0, $zero, imprimeigual   #se for igual
	blt $t0, $zero, imprimemenor   #se for menor
	
	imprimemaior:
		li $v0, 4 #impimindo mensagem se o número for maior
		la $a0, maior
		syscall
		
		li $v0, 10 #desligando sistema
		syscall
		
	imprimeigual:
		li $v0, 4 # #impimindo mensagem se o número for igual
		la $a0, igual
		syscall
		
		li $v0, 10 #desligamos sistema na unha
		syscall
		
	imprimemenor:
		li $v0, 4 # #impimindo mensagem se o número for menor
		la $a0, menor
		syscall
		
		li $v0, 10 #desligamos sistema na unha
		syscall
	