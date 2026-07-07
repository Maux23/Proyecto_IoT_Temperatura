aqui se vera el archivo index que se uso para ver la pagina.

<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <title>Monitor IoT</title>

    <meta http-equiv="refresh" content="5">

    <style>

        body{
            background:#111;
            color:#00ff88;
            font-family:Consolas, monospace;
            padding:30px;
        }

        .contenedor{
            width:900px;
            margin:auto;
            border:2px solid #00ff88;
            padding:25px;
        }

        h1{
            text-align:center;
            margin-bottom:30px;
        }

        .estado{
            border:1px solid #00ff88;
            padding:20px;
            font-size:22px;
        }

        .leds{

            margin-top:30px;
            display:flex;
            justify-content:space-around;

        }

        .led{

            width:80px;
            height:80px;
            border-radius:50%;
            background:#333;
            border:4px solid #555;

        }

        .verde{

            background:lime;
            box-shadow:0 0 25px lime;

        }

        .amarillo{

            background:yellow;
            box-shadow:0 0 25px yellow;

        }

        .rojo{

            background:red;
            box-shadow:0 0 25px red;

        }

        .texto{

            text-align:center;
            margin-top:10px;
            font-size:18px;

        }

        table{

            width:100%;
            margin-top:30px;
            border-collapse:collapse;

        }

        th{

            background:#00aa55;

        }

        td,th{

            border:1px solid #00ff88;
            padding:10px;
            text-align:center;

        }

    </style>

</head>

<body>

<div class="contenedor">

<h1>MONITOR IoT - ESP32 + DHT11</h1>

<div class="estado">

<p><b>Temperatura:</b> {{ dato.temperatura }} °C</p>

<p><b>Humedad:</b> {{ dato.humedad }} %</p>

<p><b>Estado:</b> {{ dato.estado }}</p>

<p><b>Fecha:</b> {{ dato.fecha }}</p>

</div>


<h2 style="text-align:center;">Indicadores LED</h2>

<div class="leds">

<div>

<div class="led {% if dato.estado == 'FRIO' %}verde{% endif %}"></div>

<div class="texto">LED VERDE</div>

</div>

<div>

<div class="led {% if dato.estado == 'NORMAL' %}amarillo{% endif %}"></div>

<div class="texto">LED AMARILLO</div>

</div>

<div>

<div class="led {% if dato.estado == 'CALOR' %}rojo{% endif %}"></div>

<div class="texto">LED ROJO</div>

</div>

</div>


<h2>Historial</h2>

<table>

<tr>

<th>Fecha</th>

<th>Temperatura</th>

<th>Humedad</th>

<th>Estado</th>

</tr>

{% for item in historial %}

<tr>

<td>{{ item.fecha }}</td>

<td>{{ item.temperatura }} °C</td>

<td>{{ item.humedad }} %</td>

<td>{{ item.estado }}</td>

</tr>

{% endfor %}

</table>

</div>

</body>
</html>
