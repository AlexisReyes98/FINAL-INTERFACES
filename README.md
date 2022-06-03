# FINAL-INTERFACES

UEA: Interfaces De Usuario.

Proyecto final: Detección de movimiento y generación de sonidos.

Introducción.

En ocasiones nuestra mascota puede ser muy traviesa, invadiendo espacios que no le corresponden o haciendo destrozos, así como salirse de las habitaciones permitidas o
incluso de la casa, es por eso que se puede tener un mecanismo que nos ayude en esas situaciones.

Es por eso que los alumnos  de Ingeniería en computación  de la UAM Cuajimalpa tienen una propuesta: El proyecto que abordaremos se trata de una alarma que se activará cuando se detecta un movimiento de alguna entidad , es decir, poniendo un escenario de una habitación en donde existen mascotas y se necesita saber cuando la mascota quiere salir de la habitación, el sistema tiene ya definido un perímetro permitido en donde la mascota puede estar sin restricciones, entonces si la mascota se acerca más hacia el área donde apunta la cámara de la computadora, la cámara detectará los movimientos y así la computadora emitirá un sonido de alarma para avisar al dueño y que éste pueda tomar sus precauciones. 

En general, se pretende:

➔	Detectar movimientos mediante una cámara.

➔	Producir un sonido para alertar.

➔	Probar la interfaz en diferentes áreas.

Se piensa que este sistema pueda ser utilizado de manera general, es decir, no solamente para la detección de movimientos de mascotas, sino también para situaciones en donde personas adultas, con alguna enfermedad o limitante, o vulnerables, puedan ser también detectados sus movimientos y estar alertas para prevenir alguna situación negativa.

Sonido.

El sonido debe ser reproducido con volumen alto al detectar un movimiento de la mascota que cruce una cierta área .

Limitaciones.

Si los niveles de luz varían en el área donde la cámara se enfoca, podrían generar falsas alarmas. Se requiere una zona sin variabilidad de iluminación, por ejemplo una habitación con iluminación estable.

La distancia debe ser adecuada para detectar el movimiento.

Objetivos.

En general, el proyecto se busca que cumpla con:

1.	Tener una interfaz eficaz, es decir, ofrecer buenos resultados a todos los usuarios interesados en ella, para  tener una especie de control de su mascota en este caso.

2.	Comprobar la velocidad máxima en la que se puede detectar un movimiento y la distancia permitida en la que funcionará la interfaz.

3.	Crear un sistema confiable en donde solamente se cumpla el propósito de la misma y que todos los usuarios que la prueben, no tengan problema alguno en su uso.

4.	Tomar en cuenta las observaciones que hagan los usuarios que prueben la interfaz con el fin de mejorar el sistema.

5.	Tener un campo abierto en donde no sólo esté diseñada para un usuario en específico, es decir, que se pueda utilizar en distintas situaciones en donde sea posible o esté adaptada.

Funcionamiento del sistema.

El sistema está pensado para ser usado dentro de casa, en un lugar fijo y libre de cambios en la iluminación. Una vez que se tenga claro esto podemos probar la interfaz ya completamente desarrollada.

Ejecutamos el programa y se escucha un pequeño mensaje de bienvenida que dice: “Hola usuario gracias por utilizar el sistema MUVI, desarrollado en la UEA interfaces de usuario”, posteriormente nos muestra la ventana principal de la interfaz y es la que se ve en la siguiente imagen.. 

![image](https://user-images.githubusercontent.com/72325257/171782781-d4c8278b-e264-408d-983d-27452bbc8b8f.png)

Ahora podemos probar cada una de las opciones que muestra la interfaz, por ejemplo, comencemos probando la opción de ayuda, si le damos clic a la opción entonces nos muestra una subventana que tiene tres opciones, las cuales son: escuchar recomendaciones, ver recomendaciones y cerrar, lo descrito anteriormente se muestra en la siguiente imagen.

![image](https://user-images.githubusercontent.com/72325257/171782856-bb7010e7-832c-4f40-92a2-7bc6c92cee46.png)

Si presiona el botón ‘Escuchar recomendaciones’, se reproducirá un audio con las recomendaciones que le ayudarán al usuario a que la interfaz funcione de la mejor manera.

Ahora, al presionar el botón “Ver recomendaciones” se muestra otra subventana con las recomendaciones más importantes en un recuadro como se muestra en la siguiente imagen.

![image](https://user-images.githubusercontent.com/72325257/171782935-4eb5f6bc-3ffa-4277-a337-d439a81e8289.png)

Si presiona el botón ‘Salir’ se cierra la ventana de la interfaz y se termina la ejecución. Pasamos al punto principal que es probar el detector de movimiento, para esto, presionamos el botón “Activar” y nos sale una subventana llamada “Detector de movimiento activo”, que nos sirve para observar el área para detectar el movimiento, donde es importante mencionar que la cámara de la computadora ya no debe ser movida, ya que si lo hace es muy probable que se generen falsas alarmas. Si se desea cambiar la posición de la cámara de la computadora, entonces es recomendable desactivar el detector presionando la tecla ‘q’.

Mediante el botón ‘Activar’ se activa el detector de movimiento.
 
Subventana que muestra el área donde se va a detectar el movimiento:

![image](https://user-images.githubusercontent.com/72325257/171783068-d2e5610a-7f63-4756-afff-5ca460f52575.png)

Mientras el detector está activo y una entidad en movimiento pasa frente a la cámara, entonces se produce un sonido con una alta frecuencia y que dura alrededor de 4 segundos. Es recomendable que antes de activar el detector de movimiento suba el volumen de la computadora a un nivel en el que el sujeto considere que escuchará la alarma.
 
Las entidades en movimiento que pasen frente a la cámara de la computadora serán remarcadas en un recuadro de color verde.

![image](https://user-images.githubusercontent.com/72325257/171783120-133b230b-097a-441d-874b-d17c4921d362.png)
