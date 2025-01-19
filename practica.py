def menu():
    menu_items = {
        
    menu_items = {
    

    menu_items = {

    menu_items 

    m
1: ("Pikachu Roll", 4500),
        
        

   
2: ("Otaku Roll", 5000),
        3: ("Pulpo Venenoso", 5200),
        4: ("Anguila Eléctrica Roll", 4800)
    }

    
    }

  
while True:
        pedido = {}
        
        pedido = {}
    

        pedido = {}
 

        pedido = {

        pedido

        pe

     
print("\nBienvenido a Sushi Master")
        
        
        
       

        
    

        
 

       

   
# Menú de productos
        
 
while True:
            
   
print("\nMenú de Rolls")
            
            fo

           
for opcion, (nombre, precio) in menu_items.items():
                
                pri

               

           

       
print(f"{opcion}. {nombre} - ${precio}")
            
      

  
print("5. Finalizar pedido")
            
            
           

     
try:
                opcion = 
              

          

     
int(input("Seleccione una opción: "))
                
           
if opcion == 5:
                    
                    

               

         

   
break
                
                el

           
elif opcion in menu_items:
                    pedido[opcion] = pedido.get(opcion, 
                    pedido[opcion] = pedido.get(opcio

                    pedido[opcion] = pedido.get

                    pedido[opcion] = ped

                    pedido[opcion

                    pedido[op

                    pedid

                    p

                

           

     
0) + 1
                    
                    p

                

          
print(f"{menu_items[opcion][0]} agregado al pedido.")
                
          

     
else:
                    
                    pr

                

         

 
print("Opción inválida, intenta de nuevo.")
            
            ex

       
except ValueError:
                
                pr

            

     
print("Entrada no válida, ingresa un número entre 1 y 5.")
        
        
        
      

        
if not pedido:
            print("No se ha seleccionado ningún producto. Volviendo al menú principal.")
            
         

   
continue
        
        
        
       

        

 
# Calcular subtotal
        subtotal = 
        subtotal 

        subt
sum(menu_items[opcion][1] * cantidad for opcion, cantidad in pedido.items())
        descuento = 
        de

     
0
        
        
        
  
# Código de descuento
        
        whil
while True:
            tiene_codigo = 
            tiene_codigo

            tiene_c

            t

       
input("¿Tiene un código de descuento? (si/no): ").strip().lower()
            
        

  
if tiene_codigo == "si":
                codigo = 
                codigo = inp

                codigo 

                c

          

   
input("Ingrese el código de descuento: ").strip()
                
             

    
if codigo == "otaku":
                    descuento = subtotal * 
                    descuento = subtotal 

                    descuento = subt

                    descuento =

                    descu

                  

  
0.10
                    
                    pr

                   

                

            

        

    
print("Código válido. Se aplicará un descuento del 10%.")
                    
                   

 
break
                
                el

             

       
else:
                    
                    pr

                

 
print("Código inválido, intenta de nuevo o escribe 'no' para continuar sin descuento.")
            
            

      
elif tiene_codigo == "no":
                
                br

           

   
break
            
          
else:
                
                

           

     
print("Respuesta inválida, ingresa 'si' o 'no'.")
        
        
        
      

       
# Calcular total
        total = subtotal - descuento
        
        
        total = subtotal - descuento
        
   

        total = subtotal - descuento
  

        total = subtotal - descu

        total = subtotal

        total =

     
# Mostrar detalle del pedido
        
   
print("\nDetalle del Pedido")
        
        prin

    
print("***********************************")
        total_productos = 
        total_productos = s

        total_produ

    
sum(pedido.values())
        
        prin
print(f"Total productos: {total_productos}")
        
        f
for opcion, cantidad in pedido.items():
            nombre, precio = menu_items[opcion]
            
            nombre, precio = menu_items[opcion]
            

            nombre, precio = menu_items[opcion]
     

            nombre, precio = menu_items[opcion

            nombre, precio = menu_items[

            nombre, precio = menu_

            nombre, precio 

            nombre, pr

            nombr

           

    
print(f"{nombre}: {cantidad} x ${precio} = ${cantidad * precio}")
        
        p

    
print("***********************************")
        
     

 
print(f"Subtotal: ${subtotal}")
        
       

 
print(f"Descuento: -${descuento}")
        
        

  
print(f"Total a pagar: ${total}")
        
        
      
# Preguntar si desea realizar otro pedido
        otra_vez = 
        otra_v

        

 
input("\n¿Desea realizar otro pedido? (si/no): ").strip().lower()
        
        

     

  
if otra_vez != "si":
            print("Gracias por su compra. ¡Que tenga un buen día!")
            
            b

          

       

    
break


if __name__ == "__main__":
    menu()

    menu()
``

    menu