writeLines("--------------------------")
writeLines("Calculadora de numeros:")
writeLines("--------------------------")
band <- TRUE
while (band == TRUE){

    n1 <- readline(prompt="Ingrese el primer numero: ")
    n2 <- readline(prompt="Ingrese el segundo numero: ")
    n1 <- as.integer(n1)
    n2 <- as.integer(n2)

    writeLines("")
    writeLines("1. Suma")
    writeLines("2. Resta")
    writeLines("3. Multiplicación")
    writeLines("4. División")
    writeLines("")

    operador <- readline(prompt="Ingrese el operador a usar (1,2,3,4): ")
    operador <- as.integer(operador)
    if(operador != 1 & operador != 2 & operador != 3 & operador != 4){
        writeLines("---")
        writeLines("Operador no válido")
    }
    else if (operador == 1){
        resultado <- n1 + n2
        print(paste("Resultado:",resultado))
    }
    else if (operador == 2){
        resultado <- n1 - n2
        print(paste("Resultado:",resultado))
    }
    else if (operador == 3){
        resultado <- n1 * n2
        print(paste("Resultado:",resultado))
    }
    else if (operador == 4){
        resultado <- n1 / n2
        print(paste("Resultado:",resultado))
    }
    
    writeLines("")
    pregunta <- readline(prompt="¿Quiere realizar otra operación? (S/N): ")
    writeLines("")
    
    if (pregunta == "S" | pregunta == "s") {
       band = TRUE
    }
    else {
       band = FALSE
    }
}