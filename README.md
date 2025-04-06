<h2>Запуск:</h2>
<ol>
  <li>Клонировать репозиторий с Github</li>
  <li>Создать виртуальное окружение</li>
  <li>Установить зависимости: <code>pip install -r requirements.txt</code></li>
  <li>Запустить проект: <code>python -m app.main</code></li>
</ol>

<h2>Эндпоинты:</h2>
<h3>POST - отправка адреса и получение информации</h3>
<p><code>/addressdata/address</code></p>
<pre>{
  "address": "str"
}</pre>
<p>Response:</p>
<pre>{
  "address": "str",
  "balance": float,
  "energy": float,
  "bandwidth": float
}</pre>

<h3>GET - получение последних запросов</h3>
<p>Параметры: limit и offset</p>
<p>Response:</p>
<pre>[
  {
    "address": "str",
    "balance": float,
    "energy": float,
    "bandwidth": float
  },
  ...
]</pre>

<h2>Тестирование:</h2>
<p>Запуск тестов: <code>pytest -v</code></p>