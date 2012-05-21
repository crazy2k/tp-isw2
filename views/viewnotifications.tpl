%include header title="Notificaciones", user_status=user_status

<h2>Tus ofrecimientos para viajes con tu vehículo</h2>

<ul>
% if not proposals_with_vehicule:
    <li>Ninguno</li>
% end
% for proposal in proposals_with_vehicule:
    <li>
        De <b>{{proposal["origin"]}}</b> a <b>{{proposal["destination"]}}</b>,
        los días <b>{{proposal["daysofweeknames"]}}</b> a las
        <b>{{proposal["time"]}}</b> con capacidad
        <b>{{proposal["capacity"]}}</b>
    </li>
% end
</ul>

<h2>Tus ofrecimientos de acompañante para viajes</h2>

<ul>
% if not proposals_without_vehicule:
    <li>Ninguno</li>
% end
% for proposal in proposals_without_vehicule:
    <li>
        De <b>{{proposal["origin"]}}</b> a <b>{{proposal["destination"]}}</b>,
        los días <b>{{proposal["daysofweeknames"]}}</b> a las
        <b>{{proposal["time"]}}</b>
    </li>
% end
</ul>

<h2>¡Tus viajes organizados!</h2>

<ul>
% if not organized_journeys:
    <li>Ninguno</li>
% end
% for journey in organized_journeys:
    <li>
        De <b>{{journey["starting_point"]}}</b> a
        <b>{{journey["end_point"]}}</b>, el día
        <b>{{journey["datetime"]}}</b>; conduce <b>{{journey["driver"]}}</b> y
        viajan <b>{{journey["count"]}}</b> personas en un vehículo con
        capacidad para <b>{{journey["total_seats"]}}</b>
    </li>
% end
</ul>

<h2>Tus notificaciones</h2>

<ul>
% if not notifications:
    <li>Ninguna</li>
% end
% for notification in notifications:
    <li><b>{{notification.title()}}:</b> {{notification.content()}}</li>
% end
</ul>




<hr>

<form method="post" action="/organize">
    <table>
    <tr class="odd">
        <td>Tolerancia en minutos:</td>
        <td><input type="text" name="time_tolerance" /></td>
    </tr>
    <tr>
        <td>Tolerancia de distancia:</td>
        <td><input type="text" name="distance_tolerance" /></td>
    </tr>
    </table>
    <input type="submit" value="Organizar viajes semanales" />
</form>

%include footer

