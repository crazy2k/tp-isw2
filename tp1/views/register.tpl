%include header title="Registración", user_status=user_status

% if failed:
    <div class="failure">
    % if reason == "empty_field":
        <p>Olvidó ingresar un campo.</p>
    % elif reason == "register_error":
        <p>Error en la registración.</p>
    % end
    </div>
% end

<form method="post" action="/register">
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
    <input type="submit" value="Registrarme"/>
</form>

%include footer
