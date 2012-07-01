<html>
<head>
    <title>{{title}}</title>
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <link rel="stylesheet" type="text/css" href="/static/style.css" />
    <style type="text/css">
        body {
            font-family: Palatino, Georgia, serif;
            font-size: 18px;
            word-spacing: 0.1em;

            /* body is centered */
            width: 700px;
            margin-left: auto;
            margin-right: auto;

        }
        div.failure {
            color: red;
        }

        table tr.odd { background: #F0F0F0 }
        h1#logo a { 
            text-decoration: none;
            color: #202020;
        }
    </style>
</head>
<body>
<h1 id="logo"><a href="/">Viajemos Juntos</a></h1>
<div id="main">
    <div id="menu">
        <ul>
        % if not user_status["logged_in"]:
            <li><a href="/login">Entrar</a></li>
            <li><a href="/register">Registrarme</a></li>
        % else:
            <li><a href="/logout">Salir</a></li>
        % end
        </ul>
    </div>
