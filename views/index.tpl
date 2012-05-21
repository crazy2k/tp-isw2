%include header title="¡Viajemos Juntos!", user_status=user_status

% if not user_status["logged_in"]:

<p>¡Bienvenido! Si ya tenés un usuario, podés
<a href="/login">autenticarte</a>. Si todavía no lo tenés, podés
<a href="/register">registrarte</a>.</p>

% else:

<p>¡Bienvenido, {{user_status["email"]}}! Estas son tus opciones:</p>
<ul>
    <li><a href="/createproposalwithcar">Ofrecer viajes que realizarás con tu
        vehículo</a></li>
    <li><a href="/createproposalwithoutcar">Ofrecerte como acompañante para
    viajes</a></li>
    <li><a href="/viewnotifications">Revisar tus notificaciones para esta
    semana</a></li>
</ul>

%include footer
