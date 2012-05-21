%include header title="Ofrecer viajes", user_status=user_status

% if failed:
    <div class="failure">
    % if reason == "invalid_data":
        <p>Datos faltantes o inválidos.</p>
    % end
    </div>
% end

% with_or_without_vehicle = "withvehicle" if with_vehicle else "without_vehicle"

<form method="post" action="/createproposal/{{with_or_without_vehicle}}">
    <table>
    <tr class="odd">
        <td>Origen:</td>
        <td>
            % for y in range(height):
                % for x in range(width):
                <input type="radio" name="origin" value="{{x}}-{{y}}" />
                % end
                <br />
            % end
        </td>
    </tr>
    <tr>
        <td>Destination:</td>
        <td>
            % for y in range(height):
                % for x in range(width):
                <input type="radio" name="destination" value="{{x}}-{{y}}" />
                % end
                <br />
            % end
        </td>
    </tr>
    <tr class="odd">
        <td>Días de la semana:</td>
        <td>
            <input type="checkbox" name="monday" id="monday" />
            <label for="monday">Lunes</label>
            <br />
            <input type="checkbox" name="tuesday" id="tuesday"/>
            <label for="tuesday">Martes</label>
            <br />
            <input type="checkbox" name="wednesday" id="wednesday" />
            <label for="wednesday">Miércoles</label>
            <br />
            <input type="checkbox" name="thursday" id="thursday" />
            <label for="thursday">Jueves</label>
            <br />
            <input type="checkbox" name="friday" id="friday" />
            <label for="friday">Viernes</label>
            <br />
            <input type="checkbox" name="saturday" id="saturday" />
            <label for="saturday">Sábado</label>
            <br />
            <input type="checkbox" name="sunday" id="sunday" />
            <label for="sunday">Domingo</label>
            <br />
        </td>
    </tr>
    <tr>
        <td>Hora (ejemplo: 8:30):</td>
        <td><input type="text" name="time" size="10" /></td>
    </tr>

    % if with_vehicle:
    <tr class="odd">
        <td>Capacidad del vehículo:</td>
        <td><input type="text" name="capacity" size="10" /></td>
    </tr>
    % end

    </table>
    <input type="submit" value="Ofrecer"/>
</form>

%include footer
