Product Backlog
===============

== ====================================================== ======= ===== ======
ID Item                                                   Prority Value Effort
== ====================================================== ======= ===== ======
1  Como usuario con auto quiero ingresar datos para       1       50    8
   ofrecer posibles viajes que realizaré con él.
-- ------------------------------------------------------ ------- ----- ------
2  Como usuario sin auto quiero ingresar datos para       2       40    8
   conocer qué ofertas de viaje safisfacen mis
   requisitos.
-- ------------------------------------------------------ ------- ----- ------
3  Como usuario quiero poder dar de alta mi cuenta en el  3       35    3
   sistema para luego poder ingresar los datos de mis
   viajes.
-- ------------------------------------------------------ ------- ----- ------
4  Como usuario sin auto quiero que al ingresar mis datos 4       30    8
   estos queden registrados para que se me asigne
   semanalmente el viaje óptimo de forma automática.
-- ------------------------------------------------------ ------- ----- ------
5  Como usuario registrado quiero poder consultar en el   5       20    1
   sistema los detalles sobre el viaje que me fue
   asignado.
-- ------------------------------------------------------ ------- ----- ------
6  Como usuario registrado quiero recibir notificaciones  6       10    3
   para conocer los detalles sobre el viaje que me fue
   asignado.
== ====================================================== ======= ===== ======

Justificación de los *values*
=============================

Consideramos que la decisión acerca de los *values* de los ítems del
*Product Backlog* es responsabidad del *Product Owner*. Ante la ausencia de
esta información para este trabajo, elegimos valores que nos parecieron
razonables poniéndonos en ese papel.

Justificación de los *efforts*
==============================

Consideramos que la *user story* con menor esfuerzo asociado es la #5,
ya que sólo implica poder consultar los resultados de la estrategia
utilizada por el organizador de viajes; el algoritmo utilizado para la misma
está ya contemplado por el ítem #4, de mayor prioridad, por lo que no sería
necesario tenerlo en cuenta para este punto. En cuanto a la interfaz de
usuario, todos los pormenores de la misma ya estarían previamente
resueltos en las distintas stories que hacen uso de ella. A partir de
esa user story, puntuamos el resto de las estimaciones en forma
relativa, usando la secuencia de Fibonacci.

Las siguientes user stories, en orden de esfuerzo creciente, son la #6
y la #3:

- La #3 sólo implica poder registrar un usuario, lo cual abarca el
  ingreso de pocos datos y validaciones muy simples de estos. Lo
  referido a la interfaz gráfica, para la parte de registro,
  tampoco requeriría mucho esfuerzo, dado que stories más prioritarias,
  como la #1, ya implican buena parte del trabajo.

- La #6 sólo conlleva la notificación al cliente de información
  previamente computada. La estimación asignada es algo mayor que la
  mínima dado que sería necesario realizar un poco de investigación con
  respecto a las APIs de SMTP disponibles o sobre el protocolo de
  notificación a utilizar que resulte más conveniente.

Las stories #1 y #2 son similares en esfuerzo. La primera implica la
programación del mecanismo de autenticación de usuarios y el ingreso de
datos de las ofertas de viaje, así como la creación de las entidades
pertinentes en el sistema. Además, esta story conlleva el trabajo de
investigar sobre la tecnología a utilizar para el sitio web, y también
la creación de los elementos de la interfaz gráfica.

La story #2 también implica la autenticación de usuarios y el trabajo
en la interfaz gráfica. Esta story podría aprovechar lo realizado en la
story #1, disminuyendo el esfuerzo requerido para realizar algunas de
sus tareas. Sin embargo, esta story implica el desarrollo de un
algoritmo de *matching* primitivo que permita al usuario encontrar
ofertas de viaje de su interés. La programación de este algoritmo,
aunque este sea básico, podría requerir, además, un tiempo dedicado a
investigación.

La story #4 implica la registración de los datos de un usuario sin
auto y el desarrollo de un algoritmo de matching algo más elaborado
entre pedidos y ofertas de viaje. El mayor esfuerzo en esta story se lo
lleva el desarrollo del algoritmo de matching, y la investigación
que esto requiera. En un principio, habíamos asignado a esta story una
estimación de esfuerzo mayor, pero, luego de realizar la subdivisión de
algunas de las stories, se logró amortizar el esfuerzo requerido para
esta: El trabajo sobre la interfaz gráfica y la persistencia de datos,
así como el desarrollo de un primer algoritmo de matching naive en
stories de mayor prioridad, hacen que esta story se vuelva más pequeña,
lo cual es deseable porque reduce la incertidumbre y la vuelve más
fácil de planificar.

Sprint Backlog
==============

A cada *story point*, le asociamos 4 horas de desarrollo. Luego, las
tareas asociadas a los stories #1 y #2 quedarían estimadas como se
detalla a continuación.

Story #1
--------

Criterio de aceptación:

- El usuario puede ingresar al sistema con su email y contraseña.
- El sistema impide el ingreso al sistema al usuario cuando su
  email y contraseña no coinciden.
- El usuario puede crear una oferta de viaje indicando que dispone
  de auto e ingresar lugar, día y horario de salida y de llegada.

Task #1
```````

=================== ===================================================
Descripción         Investigar tecnología conveniente para la interfaz
                    de usuario.
------------------- ---------------------------------------------------
Status              Not Yet Started
------------------- ---------------------------------------------------
Original Estimate   8 horas
------------------- ---------------------------------------------------
Remaining Estimate  8 horas
------------------- ---------------------------------------------------
Time Spent          0 horas
=================== ===================================================

Task #2
```````

=================== ===================================================
Descripción         Crear elementos de interfaz necesarios para la
                    autenticación de usuarios.
------------------- ---------------------------------------------------
Status              Not Yet Started
------------------- ---------------------------------------------------
Original Estimate   2 horas
------------------- ---------------------------------------------------
Remaining Estimate  2 horas
------------------- ---------------------------------------------------
Time Spent          0 horas
=================== ===================================================

Task #3
```````

=================== ===================================================
Descripción         Programar validación de datos ingresados por el
                    usuario.
------------------- ---------------------------------------------------
Status              Not Yet Started
------------------- ---------------------------------------------------
Original Estimate   4 horas
------------------- ---------------------------------------------------
Remaining Estimate  4 horas
------------------- ---------------------------------------------------
Time Spent          0 horas
=================== ===================================================

Task #4
```````

=================== ===================================================
Descripción         Programar mecanismo de autenticación de usuarios.
------------------- ---------------------------------------------------
Status              Not Yet Started
------------------- ---------------------------------------------------
Original Estimate   4 horas
------------------- ---------------------------------------------------
Remaining Estimate  4 horas
------------------- ---------------------------------------------------
Time Spent          0 horas
=================== ===================================================

Task #5
```````

=================== ===================================================
Descripción         Crear elementos de interfaz necesarios para el
                    ingreso de datos para oferta de viaje.
------------------- ---------------------------------------------------
Status              Not Yet Started
------------------- ---------------------------------------------------
Original Estimate   4 horas
------------------- ---------------------------------------------------
Remaining Estimate  4 horas
------------------- ---------------------------------------------------
Time Spent          0 horas
=================== ===================================================

Task #6
```````

=================== ===================================================
Descripción         Programar ingreso de datos para oferta de viaje.
------------------- ---------------------------------------------------
Status              In Progress
------------------- ---------------------------------------------------
Original Estimate   6 horas
------------------- ---------------------------------------------------
Remaining Estimate  6 horas
------------------- ---------------------------------------------------
Time Spent          4 horas
=================== ===================================================

Task #7
```````

=================== ===================================================
Descripción         Crear las entidades necesarias para una nueva
                    oferta de viaje.
------------------- ---------------------------------------------------
Status              Not Yet Started
------------------- ---------------------------------------------------
Original Estimate   6 horas
------------------- ---------------------------------------------------
Remaining Estimate  6 horas
------------------- ---------------------------------------------------
Time Spent          0 horas
=================== ===================================================

Task #8
```````

=================== ===================================================
Descripción         Persistir los datos de la oferta generada.
------------------- ---------------------------------------------------
Status              Not Yet Started
------------------- ---------------------------------------------------
Original Estimate   4 horas
------------------- ---------------------------------------------------
Remaining Estimate  4 horas
------------------- ---------------------------------------------------
Time Spent          0 horas
=================== ===================================================

Story #2
--------

Criterio de aceptación:

- El usuario puede ingresar al sistema con su email y contraseña.
- El sistema impide el ingreso al sistema al usuario cuando su
  email y contraseña no coinciden.
- El usuario puede ingresar un horario, un lugar de salida, así
  un como lugar llegada, y obtener todas las ofertas que los
  satisfacen.

Task #1
```````

=================== ===================================================
Descripción         Crear elementos de interfaz necesarios para el
                    ingreso de datos para pedido de viaje.
------------------- ---------------------------------------------------
Status              Not Yet Started
------------------- ---------------------------------------------------
Original Estimate   4 horas
------------------- ---------------------------------------------------
Remaining Estimate  4 horas
------------------- ---------------------------------------------------
Time Spent          0 horas
=================== ===================================================

Task #2
```````

=================== ===================================================
Descripción         Programar validación de datos ingresados para el
                    pedido de viaje.
------------------- ---------------------------------------------------
Status              Not Yet Started
------------------- ---------------------------------------------------
Original Estimate   4 horas
------------------- ---------------------------------------------------
Remaining Estimate  4 horas
------------------- ---------------------------------------------------
Time Spent          0 horas
=================== ===================================================

Task #3
```````

=================== ===================================================
Descripción         Programar ingreso de datos para pedido de viaje.
------------------- ---------------------------------------------------
Status              In Progress
------------------- ---------------------------------------------------
Original Estimate   4 horas
------------------- ---------------------------------------------------
Remaining Estimate  2 horas
------------------- ---------------------------------------------------
Time Spent          2 horas
=================== ===================================================

Task #4
```````

=================== ===================================================
Descripción         Investigar sobre algoritmo de matching primitivo
                    que permita al usuario encontrar ofertas de viaje
                    de su interés.
------------------- ---------------------------------------------------
Status              Not Yet Started
------------------- ---------------------------------------------------
Original Estimate   4 horas
------------------- ---------------------------------------------------
Remaining Estimate  4 horas
------------------- ---------------------------------------------------
Time Spent          0 horas
=================== ===================================================

Task #5
```````

=================== ===================================================
Descripción         Programar algoritmo de matching primitivo que
                    permita al usuario encontrar ofertas de viaje de su
                    interés.
------------------- ---------------------------------------------------
Status              Not Yet Started
------------------- ---------------------------------------------------
Original Estimate   12 horas
------------------- ---------------------------------------------------
Remaining Estimate  12 horas
------------------- ---------------------------------------------------
Time Spent          0 horas
=================== ===================================================

Task #6
```````

=================== ===================================================
Descripción         Crear las entidades necesarias para un nuevo pedido
                    de viaje.
------------------- ---------------------------------------------------
Status              Not Yet Started
------------------- ---------------------------------------------------
Original Estimate   6 horas
------------------- ---------------------------------------------------
Remaining Estimate  6 horas
------------------- ---------------------------------------------------
Time Spent          0 horas
=================== ===================================================

Task #7
```````

=================== ===================================================
Descripción         Crear elementos de interfaz necesarios para mostrar
                    al usuario las ofertas de viaje de su interés.
------------------- ---------------------------------------------------
Status              Not Yet Started
------------------- ---------------------------------------------------
Original Estimate   4 horas
------------------- ---------------------------------------------------
Remaining Estimate  4 horas
------------------- ---------------------------------------------------
Time Spent          0 horas
=================== ===================================================

Se puede apreciar el progreso hasta ahora alcanzado en el task burndown chart.

Sobre las stories y los sprints
===============================

El proyecto se efectuará en 2 sprints. Para el primero, elegimos las stories #1 y #2,
indicadas en la tabla anterior, las cuales son las de mayor importancia para el
cliente. Ambas suman una cantidad de 16 story points (del total de 31).

El equipo prefirió no comprometerse e incluir ninguna story más del Product
Backlog, para no establecer expectativas demasiado altas en el cliente, aunque,
si el tiempo lo permite, se podría intentar el desarrollo de la story #3 antes de
que finalice el sprint, de forma tal de completar las primeras 3 stories durante
el mismo.

Inicialmente, las stories incluidas en este sprint sólo abarcaban la
funcionalidad para crear cuentas de usuario y que los usuarios registrados
pudieran ingresar al sitio los datos necesarios para poder cumplir sus necesidades
de transporte, o incluso, poner a disposición un auto propio, pero sin contemplar
la posibilidad de organizar viajes a través del sistema.

Se consideró luego, que un hipotético P.O. se beneficiaría más al poder incluir
al menos cierta funcionalidad básica de organización de viajes en este mismo release,
de forma tal, de obtener un producto que pudiese ser lanzado a producción de
manera inmediata.

Adicionalmente, teniendo en cuenta que al agregar la story que producía los viajes
óptimos para los datos ingresados por los usuarios, el sprint se volvería demasiado
abultado y difícilmente podría cumplirse en el tiempo deseado, se decidió dividir
las stories antiguas en otras algo más simples.

Primero, el alta de la cuenta del usuario se separó en una story propia, de forma
tal que pueda ser desarrollada más adelante en otro sprint, aligerando la estimación
de las stories incluídas. Dado este cambio, el sistema podría comenzar a funcionar,
sin esta funcionalidad, en una etapa inicial donde la participación estaría cerrada
a algunos usuarios ingresados en forma masiva a una base de datos o por pedido explícito
por fuera del sistema.

Luego se planteó que podrían satisfacerse las necesidades de los usuarios si estos
pudiesen conocer cuales son las ofertas de autos disponibles que coinciden con sus
horarios y destinos; luego ellos mismos podrían elegir cuál de las ofertas mostradas
les resultarían preferibles.
Se decidíó que la funcionalidad anterior podría comprender una story nueva, la cual
no incluiría el requisito de registrar los datos de viaje del usuario en una base del
sistema. Además, permitiría obtener al menos las ofertas filtradas según su correspondencia 
con las necesidades del usuario. 
También, se agregaría un requisito de investigar las estrategias posibles de matcheo entre
pedidos y ofrecimientos que amortice el costo del desarrollo. 
De esta forma, y como se aclaró antes, la story que incluye el algoritmo de matcheo, 
tendría un esfuerzo menor.

Satisfechos con esta nueva disposición de stories, decidimos incluir esta nueva story
y la que permita registrar un auto para disposición del sistema (la de mayor
importancia), e iniciar el primer sprint.

Diseño
======

Con respecto al diseño se tomaron distintas decisiones con el fin de mantenerlo lo
más flexible que sea posible y abierto a nuevas decisiones y cambios sobre
distintos ejes.

Se consideraron varias estrategias para representar los diferentes puntos de
partida de los viajes de los usuarios, como representarlos mediantes coordenadas,
dividir todo el territorio disponible en zonas chicas e indivisibles o usar
direcciones de calles reales las cuales podrían ser ubicadas gracias a un
servicio interno. Para que ninguna de estas posibilidades quede descartada de
entrada se incluyó la clase ``Place``, la cual responde a un protocolo que permite
conocer la distancia entre cualquier par de puntos, independientemente de la
implementación subyacente. Por ejemplo, se podría utilizar una clase Address la cual 
consulte con un servicio web externo, y la misma podría cambiarse por cualquier 
otra implementación que respete el mismo protocolo sin problemas.

Se decidió además representar el pedido de viaje (``JourneyRequest``) y el ofrecimiento
de auto (``JourneyOffer``) mediante clases diferentes ya que poseían atributos en
común pero el protocolo y comportamiento que manifestaban era distinto.
En ambas hay un lugar destino, otro origen y un horario, este último se representa
con la clase ``Timetable``.

La clase ``Timetable``, representa la frecuencia y las circunstancias temporales en
las que se realiza el viaje (o potencialmente algún otro evento). Como queríamos
dejar abierto que se pudiesen especificar rutinas como "todos los lunes
a las 8 AM",
o "de lunes a jueves a las 8:30 AM y los viernes a las 9:00 AM", esta clase permite
modelar distintas maneras de organizar los horarios de viajes, desde un horario
y día fijos, por ejemplo, como otros con frecuencia semanal.

Finalmente, las otras 3 clases importantes que vale la pena aclarar son
``JourneyOrganizer``, junto con ``Journey`` y ``JourneyStop``. La primera recibe como entrada
un conjunto de pedidos y ofertas para un día determinado, y tiene que ser capaz de
organizar los distintos viajes posibles de forma óptima según algún criterio
determinado. 
Los viajes producidos se representan con la clase ``Journey``, la cual
comprende una fecha específica para el viaje además de quién será el encargado de aportar
el transporte necesario para ese viaje en particular. Luego, las
``JourneyStops``
representan los puntos intermedios del viaje donde deben subir o bajar los distintos
pasajeros, permitiendo que los viajes puedan ser diagramados con mucha flexibilidad.
