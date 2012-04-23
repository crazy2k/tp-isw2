Product Backlog
---------------

== ====================================================== ===== ======
ID Item                                                   Value Effort
== ====================================================== ===== ======
1  Como usuario sin auto quiero poder registrarme para    8	5
   poder viajar al trabajo.
-- ------------------------------------------------------ ----- ------
2  Como usuario con auto quiero registrarme para dejar mi 7     3
   auto a disposición para posibles viajes.
-- ------------------------------------------------------ ----- ------
3  Como usuario registrado quiero poder pedirle al        9     8
   sistema los detalles sobre el viaje que me fue
   asignado.
-- ------------------------------------------------------ ----- ------
4  Como usuario registrado quiero recibir notificaciones  6     1
   para conocer los detalles sobre el viaje que me fue
   asignado.
== ====================================================== ===== ======

Justificación del por qué de los values
---------------------------------------

Consideramos que la decisión acerca de los valores de los ítems del 
Product Backlog es responsabidad del Product Owner.
Ante la ausencia de esta información para este trabajo elegimos valores 
que nos parecieron razonables poniéndonos en ese papel.

Justificación del por qué de los effort
---------------------------------------

Consideramos que la user story con menor esfuerzo asociado es la cuarta
dado que sólo implica notificar al cliente la información previamente 
computada.
A partir de esa user story, basamos el resto de las estimaciones en 
forma relativa, usando Fibonacci.

Con respecto a la primera y la segunda story, dado que estas son muy
similares en esfuerzo y ambas necesitan de una tarea de invertigación, 
decidimos agregar mayor esfuerzo a la que tiene mayor valor para el 
Product Owner, y estas sería la que incluye esa tarea de investigación.
Dicha tarea de investigación incluye averiguar acerca de tecnologías 
para la interfaz gráfica de la aplicación.
Además, ambas stories incluyen la registración del usuario, por lo que 
la story de mayor esfuerzo y mayor prioridad sería la encargada de 
realizar dicha tarea.

Con respecto a la tercera user story, ésta es la que incluye mayor 
desarrollo y mayores resultados. Es la que incluye el algortimo de 
matching entre pedidos y ofertas de viaje y mayor visibilidad para el 
Product Owner.

Elegimos para este sprint la primera y segunda story, no sólo por el 
valor o el esfuerzo de las mismas, sino también por un tema de 
dependecias. Es decir, la tercera story es preferente hacerla una vez que 
estén finalizadas la primera y la segunda.

Sprint Backlog
--------------

== ===================================================================
ID Criterios de aceptación                                                   
== ===================================================================
1  - El usuario puede registrarse ingresando nombre, mail y 
     contraseña.
   - El sistema rechaza el registro de usuarios si los datos 
     ingresados son inválidos.
   - El usuario puede crear un pedido de viaje ingresando lugar, día y 
     horario de salida, así como lugar, día y horario de llegada.
-- -------------------------------------------------------------------
2  - El usuario puede registrarse ingresando nombre, mail y 
     contraseña.
   - El sistema rechaza el registro de usuarios si los datos 
     ingresados son inválidos.
   - El usuario puede crear una oferta de viaje indicando que dispone 
     de auto e ingresar lugar, día y horario de salida y de llegada.
== ===================================================================
