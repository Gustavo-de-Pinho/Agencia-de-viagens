.data
	msg: .asciiz "Insira um número: "
	par: .asciiz "O número é par"
	impar: .asciiz "O número é impar"
	
.text
	li $v0, 4 #mensagem inicial
	la $a0, msg
	syscall
	
	li $v0, 5 #lendo número inteiro
	syscall
	
	li $t0, 2 #atribuindo o n°2 a t0
	
	div $v0, $t0 #dividindo n° por 2
	mfhi $s0 #o resto é o que importa e salvamos em s0
	
	beq $s0, $zero, imprimepar #se s0 = 0, imprime par
	li $v0, 4 #aqui seguimos para o caminho dele ser impar
	la $a0, impar
	syscall
	
	li $v0, 10 #desligamos sistema na unha
	syscall
	
	imprimepar: # caso alternativo onde o n° é par
		li $v0, 4
		la $a0, par
		syscall