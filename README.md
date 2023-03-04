# <h1 align="center"><strong>JUEGO EN JAVA SCRIPT Y PYTHON</strong></h1>

## <h2 align="center"><strong>EXPLICACI&Oacute;N</strong></h2>
<p align="justify">
  Este es un programa en Python que utiliza el micro:bit para crear un juego donde el usuario controla un LED móvil con los botones A y B para atrapar objetos que caen del cielo. El objetivo del juego es atrapar la mayor cantidad de objetos posible sin dejar que caigan al suelo. A continuación se detalla la explicación de cada función y variable del código:
</p>
<br><br>
<p align="center">
  <img src="https://github.com/Alvaruky/Juego-en-JS-y-PY/blob/main/assets/img/1.jpg" alt="Códidigo Python">
</p>
<br><br>
<p align="justify">
  Esta función se ejecuta cada vez que el botón A del micro:bit es presionado. Mueve un LED móvil llamado <code>LedAbajo</code> una posición hacia la izquierda (-1 en el eje x).
</p>
<br><br>
<p align="center">
  <img src="https://github.com/Alvaruky/Juego-en-JS-y-PY/blob/main/assets/img/2.jpg" alt="Códidigo Python">
</p>
<br><br>
<p align="justify">
  Esta función crea un objeto que cae del cielo y se mueve hacia abajo por la pantalla. La variable global <code>Objeto</code> se utiliza para mantener una referencia a este objeto en todo el programa. La función crea un nuevo objeto en una posición aleatoria en el eje x en la parte superior de la pantalla (en la coordenada y = 0). Luego, un bucle for repite cuatro veces, pausando durante 500 milisegundos (0,5 segundos) y moviendo el objeto hacia abajo en una posición en el eje y. La propiedad LedSpriteProperty.Y se utiliza para actualizar la posición en el eje y del objeto.
</p>
<br><br>
<p align="center">
  <img src="https://github.com/Alvaruky/Juego-en-JS-y-PY/blob/main/assets/img/3.jpg" alt="Códidigo Python">
</p>
<br><br>
<p align="justify">
  Esta función se ejecuta cada vez que el botón B del micro:bit es presionado. Mueve el LED móvil <code>LedAbajo</code> una posición hacia la derecha (1 en el eje x).
</p>
<br><br>
<p align="center">
  <img src="https://github.com/Alvaruky/Juego-en-JS-y-PY/blob/main/assets/img/4.jpg" alt="Códidigo Python">
</p>
<br><br>
<p align="justify">
  Estas líneas de código crean dos variables globales llamadas <code>Objeto</code> y <code>LedAbajo</code>. La variable <code>LedAbajo</code> se utiliza para representar el LED móvil controlado por el usuario en la parte inferior de la pantalla. Se crea un nuevo sprite de LED en la posición (2,4) en la pantalla. Luego, la función "Objeto1" se llama para crear el primer objeto que cae del cielo.
</p>
<br><br>
<p align="center">
  <img src="https://github.com/Alvaruky/Juego-en-JS-y-PY/blob/main/assets/img/5.jpg" alt="Códidigo Python">
</p>
<br><br>
<p align="justify">
  Esta función se ejecuta constantemente mientras el programa se está ejecutando. Verifica si el objeto creado en la función <code>Objeto1</code> está tocando el LED móvil <code>LedAbajo</code> controlado por el usuario. Si es así, muestra el icono de <code>sí</code> en la pantalla, elimina el objeto y llama a la función <code>Objeto1</code> para crear otro objeto. Si el objeto no está tocando el LED móvil <code>LedAbajo</code>, muestra el icono de <code>no</code> en la pantalla y termina el juego llamando a la función <code>game_over</code>.
</p>

## <h2 align="center"><strong>PLACA MICROBIT</strong></h2>
<p align="center">
  <img src="https://github.com/Alvaruky/Juego-en-JS-y-PY/blob/main/assets/img/placa_microbit.jpg" alt="Placa-Microbit">
</p>

## <h2 align="center"><strong>TABLA C&Oacute;DIGOS</strong></h2>

<table align="center">
  <tr>
    <th align="center">C&oacute;digo JavaScript</th>
    <th align="center">C&oacute;digo Python</th>
    <th align="center">Placa MicroBit</th>
  </tr>
  <tr>
    <td align="center">
      <img src="https://github.com/Alvaruky/Juego-en-JS-y-PY/blob/main/assets/img/codigo_javascript.jpg" alt="Código-JavaScript" width="300" height="300">
    </td>
    <td align="center">
      <img src="https://github.com/Alvaruky/Juego-en-JS-y-PY/blob/main/assets/img/codigo_python.jpg" alt="Código-Python" width="300" height="300">
    </td>
    <td align="center">
      <img src="https://github.com/Alvaruky/Juego-en-JS-y-PY/blob/main/assets/img/codigo_bloques.jpg" alt="Código-Bloques" width="300" height="300">
    </td>
  </tr>
</table>

## <h2 align="center"><strong>ENLACE MICROBIT</strong></h2>
<p align="center">
  <a href="https://makecode.microbit.org/_HgVWMVKyqc8J">Microsoft Make Code</a>
</p>

### <h3 align="center">👇¡These are my social networks!👇</h3>
 <p align="center">
  <a href="https://www.youtube.com/c/AlvaroFernandezFDP" target="blank" style="margin-right: 4px">
    <img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/youtube.svg" alt="Alvaro Fernandez" height="28px" width="28px">
  </a>
    <a href="https://www.instagram.com/imalvaro__/?hl=es" target="blank" style='margin-right:4px'>
     <img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.13.0/icons/instagram.svg" alt="imalvaro__" height="28px" width="28px" />
   </a>
     <a href="https://www.tiktok.com/@alvaruky.fdp" target="blank" style='margin-right:4px'>
     <img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/tiktok.svg" alt="AlvarukyFDP" height="28px" width="28px" />
   </a>
 </p>
