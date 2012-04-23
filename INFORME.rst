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

Justificación de los values
---------------------------

Consideramos que la decisión acerca de los valores de los ítems del
Product Backlog es responsabidad del Product Owner.
Ante la ausencia de esta información para este trabajo elegimos valores
que nos parecieron razonables poniéndonos en ese papel.

Justificación de los efforts
----------------------------

Consideramos que la user story con menor esfuerzo asociado es la #5
ya que sólo implica poder consultar los resultados de la estrategia
utilizada por el organizador de viajes; el algoritmo utilizado para la misma
está ya contemplado por el ítem #4, de mayor prioridad, por lo que no sería
necesario tenerlo en cuenta para este punto. En cuanto a la interfaz de usuario,
todos los pormenores de la misma ya estarían previamente resueltos en las
distintas stories que hacen uso de la misma.

A partir de esa user story, basamos el resto de las estimaciones en
forma relativa, usando Fibonacci.

Luego, las demás users stories que requerirían menor esfuerzo asociado son la #6
y la #3:
  La #3 sólo implicaría poder registrar un usuario, lo cual requiere
  ingresar pocos datos y realizar validaciones muy simples. 
  Esta tarea sólo conllevarían implementar la interfaz de usuario, dado que en la
  #1 se amortizó gran parte de su peso.

  La #6 sólo implicaría notificar al cliente la información previamente
  computada. La estimación asignada es algo mayor que la mínima dado que sería 
  necesario realizar un poco de investigación con respecto a las APIs de SMTP 
  disponibles o sobre el protocolo de notificación a utilizar que resulte 
  más conveniente.

La #1 y la #2 story son muy similares en esfuerzo y ambas necesitan algún tipo tarea
de investigación.
Decidimos encarar primero la que poseía mayor valor para el Product Owner,
es decir la #1, y como consecuencia de lo anterior, esta sería la que conlleve la
investigación necesaria para la interfaz gráfica requerida en ambas stories y en
otras subsiguentes. 
De modo de equiparar los efforts de ambas stories, y como ambas conllevan algo de 
trabajo para permitir que el usuario pueda hacer login, se decidió agregar esta 
tarea, a la story #2.

Dicha tarea de investigación incluye averiguar acerca de tecnologías
para la interfaz gráfica para la aplicación, sean web o para algún otro
tipo de plataforma.
Además, ambas stories necesitan del login del usuario en el sistema, por
lo que la story de mayor esfuerzo y mayor prioridad sería la encargada de
realizar dicha tarea.

Con respecto a la user story #4, ésta es una de las que comprende mayor
desarrollo y mayores resultados. Es la que incluye el algoritmo de
matching entre pedidos y ofertas de viaje y mayor visibilidad para el
Product Owner. 
Además, funcionalidades que esperamos en esta story se verán resueltas en
la story #2, dado que resolveremos el ingreso de los datos de viajes y un 
algoritmo de matching entre viajes ofertados y requeridos muy simple. Esto 
nos inclinó a reducir un poco la estimación de la misma.


Sprint Backlog
--------------

A cada story point, asociamos 4 horas de desarrollo.
Luego, las tareas asociadas a los stories #1 y #2 quedarían estimadas de la 
siguiente forma:

Story 1

Task #1
   Description: investigar tecnología conveniente para la interfaz de usuario.
   Status: Not Yet Started
   Original Estimate: 6 horas
   Remaining Estimate: 6 horas
   Time Spent: 0 horas

Task #2
   Description: verificar el correcto funcionamiento del sistema de log in (dependencia con story #2)
   Status: Not Yet Started
   Original Estimate: 2 horas
   Remaining Estimate: 2 horas
   Time Spent: 0 horas

Task #3
   Description: usuario puede ingresar los datos para ofrecer su auto para un viaje
   Status: Not Yet Started
   Original Estimate: 6 horas
   Remaining Estimate: 6 horas
   Time Spent: 0 horas
   
Task #4
   Description: el sistema valida los datos ingresados
   Status: Not Yet Started
   Original Estimate: 4 horas
   Remaining Estimate: 4 horas
   Time Spent: 0 horas

Task #5
   Description: se crean las entidades necesarias para crear una nueva oferta de viaje
   Status: Not Yet Started
   Original Estimate: 8 horas
   Remaining Estimate: 8 horas
   Time Spent: 0 horas

Task #6
   Description: preservar los datos de la oferta generada
   Status: Not Yet Started
   Original Estimate: 6 horas
   Remaining Estimate: 6 horas
   Time Spent: 0 horas
   

Story 2

Task #1
   Description: usuario puede loggearse en el sistema.
   Status: Not Yet Started
   Original Estimate: 10 horas
   Remaining Estimate: 10 horas
   Time Spent: 0 horas

Task #2
   Description: usuario puede ingresar los datos para realizar un pedido de viaje
   Status: Not Yet Started
   Original Estimate: 6 horas
   Remaining Estimate: 6 horas
   Time Spent: 0 horas
   
Task #3
   Description: verificar el correcto funcionamiento del sistema de valición de los datos ingresados
   Status: Not Yet Started
   Original Estimate: 2 horas
   Remaining Estimate: 2 horas
   Time Spent: 0 horas

Task #4
   Description: se crean las entidades necesarias para crear un nuevo pedido de viaje
   Status: Not Yet Started
   Original Estimate: 8 horas
   Remaining Estimate: 8 horas
   Time Spent: 0 horas

Task #5
   Description: preservar los datos del pedido generado
   Status: Not Yet Started
   Original Estimate: 6 horas
   Remaining Estimate: 6 horas
   Time Spent: 0 horas

   
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


El proyecto se ejecturá en 2 sprint. Para el primero, elegimos las stories #1 y #2,
indicadas en la tabla anterior, las cuales son las de mayor importancia para el
cliente. Ambas suman una cantidad de 16 story points (del total de 31).

El equipo prefirió no comprometerse e incluir ninguna story más del product
backlog, para no establecer expectativas demasiado altas en el cliente, aunque,
si el tiempo lo permite, se podría intentar el desarrollo la story #3 antes de
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

Primero, la alta de la cuenta del usuario se separó en una story propia, de forma
tal que pueda ser desarrollada más adelante en otro sprint, aligerando la estimación
de las stories incluídas. Dado este cambio, el sistema podría comenzar a funcionar,
sin esta funcionalidad, en una etapa inicial donde la participación estaría cerrada
a algunos usuario ingresados en forma masiva a una base de datos o por pedido explícito
por fuera del sistema.

Luego se planteó que podrían satisfacerse las necesidades de los usuarios si estos
pudiesen conocer cuales son las ofertas de autos disponibles que coinciden con sus
horarios y destinos; luego ellos mismos podrían elegir cual de las ofertas mostradas
les resultarían preferibles.
Se decidío que la funcionalidad anterior podría comprender una story nueva, la cual
no incluiría el requisito de registrar los datos de viaje del usuario en una base del
sistema. Además, permitiría obtener al menos las ofertas filtradas según su correspondencia 
con las necesiades del usuario. 
Además, se agregaría un requisito de investigar las estrategias posibles de matcheo entre
pedidos y ofrecimientos que amortice el costo del desarrollo. 
De esta forma, y como se aclaró antes, la story que incluye el algoritmo de matcheo, 
tendría un esfuerzo menor.
Satisfechos con esta nueva disposición de stories decidimos incluir esta nueva story
junto con la que permita registar un auto para dispoción del sistema (la de mayor
importancia), e iniciar el primer sprint.


Diseño
------

Con respecto al diseño se tomaron distintas decisiones con el fin de mantenerlo lo
más flexible que sea posible y abierto a nuevas decisiones y cambios sobre
distintos ejes.
Se consideraron distintas estrategias para representar los distintos puntos de
partida de los viajes de los usuarios, como representarlos mediantes coordenadas,
dividir todo el territorio disponible en zonas chicas e indivisibles o usar
direcciones de calles reales las cuales podrían ser ubicadas gracias a un
servicio interno. Para que ninguna de estas posibilidades quede descartada de
entrada se incluyó la clase Place, la cual responde a un protocolo que permite
conocer la distancia entre cualquier par de puntos, independientemente de la
implementación subyacete. Por ejemplo, se podría utilizar una clase Address la cual 
consulte con un servicio web externo, y la misma podría cambiarse por cualquier 
otra implementación que respete el mismo protocolo sin problemas.
Se decidió además representar el pedido de viaje (JourneyRequest) y el ofrecimiento
de auto (JourneyOffer) mediante clases diferentes ya que poseían atributos en
común pero el protocolo y comportamiento que manifestaban era más bien diferente.
En ambas hay un lugar destino, otro origen y un horario, este último se representa
con la clase Timetable.
La clase Timetimable, representa la frecuenta y las circunstancias temporales en
las que se realiza el viaje (o potencialmente algún otro evento). Como queríamos
dejar abierto que se pudiesen especificar rutinas como "todos los Lunes las 8 AM",
o "de Lunes a Jueves a las 8:30 AM y los Viernes a las 9:00 AM", esta clase permite
modelar distintas maneras de organizar los horarios de viajes, desde un horario
y día fijos, por ejemplo, como otros con frecuencia semanal.

Finalmente las otras 3 clase importantes que vale la pena aclarar son
JourneyOrganizer, junto con Journey y JourneyStop. La primera recibe como entrada
un conjunto de pedidos y ofertas para un día determinado y tiene que ser capaz de,
organizar los distintos viajes posibles de forma óptima según algún criterio
determinado. 
Los viajes producidos se reprensentan con la clase Journey, la cual
comprende una fecha específica para el viaje además de quién será el encargado de aportar
el transporte necesario para ese viaje especifico. Luego las JourneyStops,
representan los puntos intermedios del viaje donde deben subir o bajar los distintos
pasajeros, permitiendo que los viajes puedan ser diagramados con mucha flexibilidad.
