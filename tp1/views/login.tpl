%include header title="Entrar", user_status=user_status

% if failed:
    <div class="failure">
    % if reason == "empty_field":
        <p>Olvidó ingresar un campo.</p>
    % elif reason == "auth_error":
        <p>Error en la autenticación.</p>
    % end
    </div>
% end



<p>Ingresá tu email y contraseña para poder entrar al sistema.</p>

<form method="post" action="/login">
    <table>
    <tr>
        <td>Email:</td>
        <td>
            <input type="text" name="email" size="10"/>
        </td>
    </tr>
    <tr>
        <td>Contraseña:</td>
        <td>
            <input type="password" name="passwd" size="10"/>
        </td>
    </tr>
    </table>
    <input type="submit" value="Entrar"/>
</form>

%include footer

