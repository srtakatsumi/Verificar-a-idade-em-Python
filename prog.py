while True:#para que assim que fechar o código possa repetir o código automaticamente

    idade = int(input("Informe sua idade: ") )#variável para guardar a informação que o usuário irá inserir

        if idade => 0 && idade <= 5 : #se a idade informada pelo o usuário for menor que 5, irá aparecer a imagem você é um neném
           print("Você é um neném")
           
        elif idade => 6 && idade < = 10 :
           print("Você é uma criança")
        
         elif idade => 11 && idade <= 17  :
           print("Você é um adolecente")   
         
        elif idade => 18 :
           print("Boa sorte com os boletos")
           
        else:#caso o usuário não informe um número o programa mostrará a mensagem abaixo e fechará o programa
        
            print("Favor inserir um valor númerico")
            break #A instrução break finaliza a iteração e o Script continua a execução normalmente. O objetivo dessa instrução é fornecer a capacidade de forçar a interrupção da iteração
