def mostrar_descuento():
    print('PRINTAFACIL S.A de C.V')
    print('-----------------------')
    print('Nuestros Métodos de Pago:')
    print('1.Efectivo')
    print('2.Tarjeta de crédito')
    print('3.Vale de regalo')
    print('4.Salir')

def main():
    while True:
        mostrar_descuento()
        operation = (input('Ingrese método de pago por favor: '))
        precio_unitario = (80000 * 0.19) + 80000  # Este es el precio de cada impresora con IVA
        cantidad = int(input('Ingrese el número de impresoras que desea comprar:'))
        precio_neto = cantidad * precio_unitario

        match operation:
            case '1':
                operacion = 'Efectivo'
                total_a_pagar = precio_neto*0.9
                descuento = precio_neto*0.1
                print(f'El total a pagar es: ${total_a_pagar:}, el descuento es: ${descuento},'
                      f'El total sin descuento es ${precio_neto:}, y la forma de pago es {operacion} ')

            case '2':
                operacion_2 = 'Crédito'
                total_a_pagar = precio_neto * 0.95
                descuento = precio_neto * 0.05
                print(f'El total a pagar es: ${total_a_pagar:}, el descuento es: ${descuento},'
                      f'El total sin descuento es ${precio_neto:}, y la forma de pago es {operacion_2} ')

            case '3':
                operacion_3 = 'Regalo'
                total_a_pagar = precio_neto * 0.85
                descuento = precio_neto * 0.15
                print(f'El total a pagar es: ${total_a_pagar:}, el descuento es: ${descuento},'
                      f'El total sin descuento es ${precio_neto:}, y la forma de pago es {operacion_3} ')

            case '4':
                print('Saliendo...')
                break

            case other:
                raise TypeError('Ingrese una opción válida')

if __name__ == '__main__':
    main()