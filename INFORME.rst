Product Backlog
---------------

== ====================================================== ======= ===== ======
ID Item                                                   Prority Value Effort
== ====================================================== ======= ===== ======
1  Como usuario con auto quiero registrarme para dejar mi 1       30    8
   auto a disposición para posibles viajes.
-- ------------------------------------------------------ ------- ----- ------
2  Como usuario sin auto quiero poder registrarme para    2       20    5
   poder viajar al trabajo.
-- ------------------------------------------------------ ------- ----- ------
3  Como usuario quiero poder dar de alta mi cuenta en el  3       15    1
   sistema para luego poder registrar mis futuros viajes.
-- ------------------------------------------------------ ------- ----- ------
4  Como usuario registrado quiero poder pedirle al        4       10    13
   sistema los detalles sobre el viaje que me fue
   asignado.
-- ------------------------------------------------------ ------- ----- ------
5  Como usuario registrado quiero recibir notificaciones  5       8     3
   para conocer los detalles sobre el viaje que me fue
   asignado.
== ====================================================== ======= ===== ======

Justificación del por qué de los values
---------------------------------------

Consideramos que la decisión acerca de los valores de los ítems del 
Product Backlog es responsabidad del Product Owner.
Ante la ausencia de esta información para este trabajo elegimos valores 
que nos parecieron razonables poniéndonos en ese papel.

Justificación del por qué de los effort
---------------------------------------

Consideramos que la user story con menor esfuerzo asociado es la tercera
ya que sólo implica agregar un usuario, el cual requiere pocos datos y 
validaciones muy simples. Luego al ser una tarea de menor prioridad las 
dificultades que conllevarian implementar la interfaz grafica ya se deberian
haber encarado en la primer story amortizando las demás.

A partir de esa user story, basamos el resto de las estimaciones en 
forma relativa, usando Fibonacci.

La segunda user story que requeriría menor esfuerzo asociado es la #5
dado que sólo implica notificar al cliente la información previamente 
computada. Es algo mas costosa que la primera ya que además sería 
necesario realizar un poco de investigación con respecto a las APIs de SMTP
disponibles o sobre el protocolo de notificacion a utilizar que resulte 
más conveniente.

Con respecto a la primera y la segunda story, dado que estas son muy
similares en esfuerzo y ambas necesitan de una tarea de investigación, 
decidimos agregar mayor esfuerzo a la que tiene mayor valor para el 
Product Owner, por ende la que se encararia primero, y como consecuencia
de lo anterior, esta sería la que conlleve la investigacion necesaria.
Dicha tarea de investigación incluye averiguar acerca de tecnologías 
para la interfaz gráfica para la aplicación, sean web o para algun otro
tipo de plataforma.
Además, ambas stories incluyen el login del usuario en el sistema, por 
lo que la story de mayor esfuerzo y mayor prioridad sería la encargada de
realizar dicha tarea.

Con respecto a la user story #4, ésta es la que incluye mayor 
desarrollo y mayores resultados. Es la que incluye el algortimo de 
matching entre pedidos y ofertas de viaje y mayor visibilidad para el 
Product Owner.

Elegimos para este sprint la primera, segunda y tercer story, no sólo por el 
valor o el esfuerzo de las mismas, sino también por un tema de 
dependecias. Es decir, la tercera story es preferente hacerla una vez que 
estén finalizadas la primera y la segunda.

Sprint Backlog
--------------

== ===================================================================
ID Criterios de aceptación                                                   
== ===================================================================
1  - El usuario puede ingresar al sistema con su email y contraseña.
   - El sistema impide el ingreso al sistema al usuario cuando su
     email y contraseña no coinciden.
   - El usuario puede crear un pedido de viaje ingresando lugar, día y
     horario de salida, así como lugar, día y horario de llegada.
-- -------------------------------------------------------------------
2  - El usuario puede ingresar al sistema con su email y contraseña.
   - El sistema impide el ingreso al sistema al usuario cuando su
     email y contraseña no coinciden.
   - El usuario puede crear una oferta de viaje indicando que dispone
     de auto e ingresar lugar, día y horario de salida y de llegada.
-- -------------------------------------------------------------------
3  - El usuario puede registrarse ingresando nombre, email y
     contraseña.
   - El sistema rechaza el registro de usuarios si los datos
     ingresados son inválidos.
== ===================================================================
