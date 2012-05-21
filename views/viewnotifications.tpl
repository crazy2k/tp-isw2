%include header title="Notificaciones", user_status=user_status

<h2>Tus ofrecimientos para viajes con tu vehículo</h2>

<ul>
% for proposal in proposals_with_vehicule:
    <li>De <b>{{proposal["origin"]}}</b> a <b>{{proposal["destination"]}}</b>,
    los días <b>{{proposal["daysofweeknames"]}}</b> a las
    <b>{{proposal["time"]}}</b> con capacidad <b>{{proposal["capacity"]}}</b>
% end
</ul>

%include footer

