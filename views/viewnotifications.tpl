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

%include footer

