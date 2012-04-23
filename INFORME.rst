Product Backlog
---------------

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
   semanalmente el viaje óptimo de forma automatica.
-- ------------------------------------------------------ ------- ----- ------
5  Como usuario registrado quiero poder consultar en el   5       20    1
   sistema los detalles sobre el viaje que me fue
   asignado.
-- ------------------------------------------------------ ------- ----- ------
6  Como usuario registrado quiero recibir notificaciones  6       10    3
   para conocer los detalles sobre el viaje que me fue
   asignado.
== ====================================================== ======= ===== ======

Justificación de los values
---------------------------------------

Consideramos que la decisión acerca de los valores de los ítems del
Product Backlog es responsabidad del Product Owner.
Ante la ausencia de esta información para este trabajo elegimos valores
que nos parecieron razonables poniéndonos en ese papel.

Justificación de los efforts
---------------------------------------

Consideramos que la user story con menor esfuerzo asociado es la #5
ya que sólo implica poder consultar los resultados de la estrategia
utilizada por el organizador de viajes; el algoritmo utilizado para la misma
esta ya contemplado por el item #4, de mayor prioridad, por lo que no seria
necesario tenerlo en cuenta para este punto. En cuanto a la interfaz de usuario,
todos los pormenores de la misma ya estarían previamente resueltos en las
distintas stories que hacen uso de la misma y tienen mayor prioridad.

A partir de esa user story, basamos el resto de las estimaciones en
forma relativa, usando Fibonacci.

Las siguientes users story que requerirían menor esfuerzo asociado son la #6
y la #3.
La #3 ya que sólo implicaría poder registrar un usuario, lo cual requiere
ingresar pocos datos y realizar validaciones muy simples; y al ser una tarea
de menor prioridad las dificultades que conllevarian implementar la interfaz
grafica ya se deberian haber encarado en la primer story amortizando las demás.
La #6 dado que sólo implica notificar al cliente la información previamente
computada. La estimación asignada es algo mayor que la mínima ya que implica
algo de riesgo, dado que sería necesario realizar un poco de investigación
con respecto a las APIs de SMTP disponibles o sobre el protocolo de
notificacion a utilizar que resulte más conveniente.

Con respecto a la primera y la segunda story, estas son muy
similares en esfuerzo y ambas necesitan algún tipo tarea de investigación.
Decidimos encarar primero la que poseía mayor valor para el Product Owner,
es decir la #1, y como consecuencia de lo anterior, esta sería la que conlleve la
investigacion necesaria para la interfaz grafica requerida en ambas stories y en
otras subsiguentes. Esta story ademas conlleva algo de trabajo aparte de la
investigación ya que requiere que el usuario pueda hacer login (en la #2 tambien),
y poder ingresar cierta cantidad de datos que luego quedan guardados en el sistema.
Para la #2, la investigacion de interfaz puede ser pasada por alto, pero requiere
tambien ingresar otros tipos de datos aparte, y que el usuario pueda visualizar
la informacion de la ofertas que le sean útiles. Esto representa en si realizar
parte de la estragia de matching entre ofertas y pedidos para lo cual cierta
investigacion es seguramente requerida, para determinar que estrategias son
convenientes para agrupar ofertas y es el punto de partida para luego completar
el algoritmo de matching optimo entre ofrecimientos y pedidos de transporte.
Según lo dicho estas 2 stories son considerablemente más dificiles de realizar que
las hasta ahora analizadas.

Dicha tarea de investigación incluye averiguar acerca de tecnologías
para la interfaz gráfica para la aplicación, sean web o para algun otro
tipo de plataforma.
Además, ambas stories incluyen el login del usuario en el sistema, por
lo que la story de mayor esfuerzo y mayor prioridad sería la encargada de
realizar dicha tarea.

Con respecto a la user story #4, ésta una de las que comprende mayor
desarrollo y mayores resultados. Es la que incluye el algortimo de
matching entre pedidos y ofertas de viaje y mayor visibilidad para el
Product Owner. Como aliciente, gran parte de lo necesario para esta story,
como ingresar los datos de los viajes del cliente y cierto primer aproach
hacia la estrageia de matching, está resuelto en la story #2, esto nos inclinó
a reducir un poco la estimacion de la misma.


Sprint Backlog
--------------

== ===================================================================
ID Criterios de aceptación
== ===================================================================
1  - El usuario puede ingresar al sistema con su email y contraseña.
   - El sistema impide el ingreso al sistema al usuario cuando su
     email y contraseña no coinciden.
   - El usuario puede crear una oferta de viaje indicando que dispone
     de auto e ingresar lugar, día y horario de salida y de llegada.
-- -------------------------------------------------------------------
2  - El usuario puede ingresar al sistema con su email y contraseña.
   - El sistema impide el ingreso al sistema al usuario cuando su
     email y contraseña no coinciden.
   - El usuario puede ingresar un horario, un lugar de salida, así
     un como lugar llegada, y obtener todas las ofertas que los
     satisfacen.
== ===================================================================

El proyecto se ejecturá en 2 sprints, para el primero, elegimos las stories #1 y #2,
indicadas en la tabla anterior, las cuales son las de mayor importancia para el
cliente. Ambas suman una cantidad de 16 story points (del total de 31).

El equipo prefirió no comprometerse e incluir ninguna story más del product
backlog, para no establecer expectativas demasiado altas en el cliente, aunque,
si el tiempo lo permite, se podria intentar el desarrollo la story #3 antes de
finalizado sprint, de forma tal de completar las primeras 3 stories durante el
mismo.

Inicialmente las stories incluidas en este sprint sólo abarcaban la
funcionalidad para crear cuentas de usuario y que los usuarios registrados
pudieran ingresar al sitio los datos necesarios para poder cumplir sus necesadades
de transporte, o incluso, poner disposicion un auto propio, pero sin contemplar
la posibilidad de organizar viajes por el sistema.
Se consideró luego, que un hipotetico P.O. se benficiaría más al poder incluir
al menos cierta funcionalidad basica de organizacion de viajes en este mismo release,
de forma tal, de obtener un producto que pudiese ser lanzado a produccion de
manera inmediata.
Adicionalmente, y teniendo en cuenta que al agregar la story que producía los viajes
óptimos para los datos ingresados por los usuarios, el sprint se volvería demasiado
abultado y dificilmente podría cumplirse en el tiempo deseado, se decidió dividir
las stories antiguas en otras algo más simples.

Primero, la alta de la cuenta del usuario se separó en una story propia, de forma
tal que pueda ser desarrollada más adelante en otro sprint. Aligerando la estimación
de las stories incluidas. Dado este cambio, el sistema podria comenzar a funcionar,
sin esta funcionalidad, en una estapa inicial donde la participacion estaria cerrada
a unos usuario ingresados en forma masiva a la DB o por pedido explicito por fuera
del sistema.

Luego se planteó que podrian satisfacerse las necesidades de los usuarios si estós
pudiesen conocer cuales son las ofertas de autos disponibles que coinciden con sus
horarios y destinos; luego ellos mismos podrían elegir cual de las ofertas mostradas
les resultarían preferibles.

Se decidío que la funcionalidad anterior podria comprender una story nueva, la cual
no incluiria el requisito de registrar los datos de viaje del usuario en la DB del
sistema (que pasaria a otra story nueva), para aligerar su peso, pero permitira
obtener al menos las ofertas filtradas segun su correspondencia con las necesiades
del usuario; esto implicaría comenzar a investigar sobre las estrategias posibles
de matcheo entre pedidos y ofrecimientos y a su vez amortizaria el costo del
desarrollo la story que incluiría algoritmo de matching entre los pedidos de viaje
y los autos puestos a disposicion para el sistema, como consecuencia la estimación
de la story que incluia el desarrollo del algoritmo de matcheo disminuyó un poco.
Satisfechos con esta nueva disposición de stories decidimos incluir esta nueva story
junto con la que permitia registar un auto para dispoción del sistema (la de mayor
importancia), e iniciar el primer sprint.
