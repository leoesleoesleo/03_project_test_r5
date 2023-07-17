#
# Test Project R5 (Backend)
Por: Leonardo Patiño Rodriguez
## &nbsp; [![pyVersion37](https://img.shields.io/badge/python-3.7.6-blue.svg)](https://www.python.org/download/releases/3.7/)

## Diseño modelado de datos
Modelo: [https://dbdiagram.io/d/6383a24fc9abfc61117575bf](https://dbdiagram.io/d/64b1946502bd1c4a5e19c082)
<p align="justify">
Se ha definido los campos correspondientes a los atributos mencionados en la prueba y establecido las relaciones apropiadas utilizando las funciones proporcionadas por Django ORM.
El campo imagen de tipo ImageField es para representar la imagen del libro, y se especifica la opción upload_to para indicar la carpeta donde se guardarán las imágenes subidas. El campo imagen es opcional (blank=True, null=True) para permitir libros sin imagen.
También se ha agregado el método __str__ en cada modelo para que se muestre una representación legible en el administrador de Django y en otros contextos.
</p>
<div align="center">
<img height="500" src="https://leoesleoesleo.github.io/imagenes/bd_r5.png" alt="Talataa">
</div>

## Flujo del proceso
<p align="justify">
Diagrama de contexto
</p>
<div align="center">
<img height="500" src="https://leoesleoesleo.github.io/imagenes/diagrama_r5.png" alt="Talataa">
</div>

## API REST con sus endpoints.

[POST] http://localhost:8000/api/token/

- Request
	```
	{
	    "username": "xxx",
	    "password": "xxx"
	}
	}
- Response
	```
	{
		"refresh":
		"access":
	}
	```

[GET] http://localhost:8000/library/books_author

- Request
	```
	{
		"author": "Marco Antonio García Juárez"
	}
	```
- Response
	```
	[
	    {
	        "source": "google_books",
	        "id_api_google": "UnKREAAAQBAJ",
	        "author_name": "Ernest Hemingway",
	        "total_books": 117,
	        "book_title": [
	            "Fiesta",
	            "El viejo y el mar",
	            "En nuestro tiempo",
	            "Muerte en la tarde",
	            "El jardín del Edén",
	            "Ernest Hemingway - Fiesta",
	            "Al otro lado del río y entre los árboles",
	            "Por quién doblan las campanas",
	            "Adiós a las armas",
	            "Adiós a las armas / A Farewell to Arms"
	        ],
	        "v_subtitle": [
	            "unknown",
	            "unknown",
	            "Prólogo de Ricardo Piglia",
	            "unknown",
	            "unknown",
	            "unknown",
	            "unknown",
	            "unknown",
	            "unknown",
	            "unknown"
	        ],
	        "v_authors": [
	            [
	                "Ernest Hemingway"
	            ],
	            [
	                "Ernest Hemingway"
	            ],
	            [
	                "Ernest Hemingway"
	            ],
	            [
	                "Ernest Hemingway"
	            ],
	            [
	                "Ernest Hemingway"
	            ],
	            [
	                "Ernest Hemingway"
	            ],
	            [
	                "Ernest Hemingway"
	            ],
	            [
	                "Ernest Hemingway"
	            ],
	            [
	                "Ernest Hemingway"
	            ],
	            [
	                "Ernest Hemingway"
	            ]
	        ],
	        "v_categories": [
	            [
	                "Fiction"
	            ],
	            [
	                "Fiction"
	            ],
	            [
	                "Fiction"
	            ],
	            [
	                "Fiction"
	            ],
	            [
	                "Fiction"
	            ],
	            "unknown",
	            [
	                "Fiction"
	            ],
	            [
	                "Fiction"
	            ],
	            [
	                "Fiction"
	            ],
	            [
	                "Fiction"
	            ]
	        ],
	        "v_publishedDate": [
	            "1944-01-01",
	            "2020-10-01",
	            "2018-11-18",
	            "2020-10-01",
	            "2020-10-01",
	            "2019-09-15",
	            "2020-10-01",
	            "2020-10-01",
	            "2020-10-01",
	            "2021-06-22"
	        ],
	        "v_description": [
	            "Después de la Primera Guerra Mundial, Jake Barnes, un periodista estadounidense que fue herido en la contienda, se reencuentra con Brett Ashley –una enfermera que también ha participado en la guerra– en París, ciudad donde empezarán a relacionarse con la comunidad norteamericana. Desde la capital francesa estos dos protagonistas se dirigen junto con Bill, Mike y Cohn a España, donde tienen previsto ir a pescar y acudir a las fiestas de San Fermín en Pamplona. Durante las celebraciones, que el autor describe con gran detalle, se suceden una serie de problemas amorosos entre Brett; su prometido Michael; Cohn –con el que ha mantenido un romance tiempo atrás– y un joven y prometedor torero llamado Pedro Romero.",
	            "Una de las historias más grandes jamás contadas. En esta nueva y magistral traducción de Miguel Temprano García, El viejo y el mar recobra todo el esplendor del clásico imperecedero que le valió el Premio Pulitzer de 1953 a Ernest Hemingway. Con un lenguaje de gran fuerza y sencillez, El viejo y el mar narra la historia de un viejo pescador cubano a quien la suerte parece haber abandonado, y del desafío mayúsculo al que se enfrenta: la batalla despiadada y sin tregua con un pez gigantesco en las aguas del golfo. Escrito en 1952, por encargo de la revista Life, este relato lo confirmó como uno de los escritores más significativos del siglo XX, obteniendo el Premio Pulitzer en 1953 y allanando su carrera hacia el Nobel de Literatura, que recibió en 1954. Reseñas: «Su mejor obra. El tiempo demostrará que es la mejor que cualquiera de nosotros haya escrito, y con eso me refiero a sus coetáneos y a los míos.» William Faulkner «El escritor estadounidense más célebre desde Mark Twain: con él la literatura yanqui entró en una nueva dimensión.» Jaime G. Mora, ABC «Su paleta era increíblemente amplia, y exquisita y violenta y brutal y fea, era todas esas cosas. Con todos sus defectos, con todas las dificultades, su vida personal o lo que sea, parecía entender al ser humano.» Michael Katakis «Cuando se logra desmontar una de Faulkner uno tiene la impresión de que le sobran resortes y tornillos y que será imposible devolverla otra vez a su estado original. Hemingway, en cambio, con menos inspiración, con menos pasión y menos locura, pero con un rigor lúcido, dejaba sus tornillos a la vista por el lado de fuera, como en los vagones de ferrocarril. Tal vez por eso Faulkner es un escritor que tuvo mucho que ver con mi alma, pero Hemingway es el que más ha tenido que ver con mi oficio.» Gabriel García Márquez «Hemingway dejaba una intensa vida de aventuras, emociones y sentimientos que supo llevar a sus relatos magistrales. [...] Literatura sencilla, cruda, hermosa y perfecta. Escribía como vivía y ello le permitió crear su propio estilo, único, inconfundible y genial. El estilo Hemingway.» Javier García Recio, La Opinión de Málaga «Pocos como Hemingway cumplen el proverbio \"el escritor muere, pero su obra permanece\".» Vanessa Jaklitsch, La Razón «Mira el mundo sin prejuicios ni preconceptos y graba con precisión y economía, y con una inmediatez casi aterradora, exactamente lo que ve.» Javier García Recio, La Opinión «Su pasión por narrar lo lleva a la selección de la realidad, a las omisiones, al lenguaje minimalista, a esa voluntad de relatar lo real que se convierte en su poética personal y su lirismo.» Ricardo Lladosa, Zenda Libros",
	            "Primera edición en español del primer libro de cuentos de Ernest Hemingway. Incluye clásicos como \"Campamento indio\" y \"El río de los dos corazones\". Una obra fundamental de uno de los escritores norteamericanos más importantes del siglo XX. Con prólogo de Ricardo Piglia. «No me había movido; no había querido levantarme para encender la lámpara porque temía quebrar el sortilegio de esa prosa. Concluí el libro en plena oscuridad. Cuando por fin me levanté y prendí la luz ya era otro.» Fragmento del prólogo de Ricardo Piglia Hemingway publicó En nuestro tiempo; su primer libro de cuentos; en 1925. Tenía 26 años y ya escribía como un veterano. Esta primera edición en español; deuda incomprensible que debía ser saldada; respeta el orden original de un libro de cuentos que; por su organicidad y consistencia interna; puede también leerse como una novela fragmentada. La guerra y el alcohol; la pesca y los toros; la soledad atormentada de Nick Adams ya están aquí; orbitando alrededor de ese núcleo emocional que Hemingway nunca nombra pero hacia el que sus relatos siempre gravitan. Ricardo Piglia tenía 18 años cuando encontró un ejemplar usado de In Our Time en una librería de Mar del Plata. Lo leyó entero esa misma tarde. Su prólogo a esta edición (que escribió poco antes de su muerte) invita a los fieles lectores de Hemingway a participar de un diálogo iluminador y es; al mismo tiempo; una inmejorable presentación para aquellos afortunados a punto de cruzar esta puerta por primera vez.",
	            "Una obra que refleja la fascinación del Premio Nobel de Literatura por las corridas de toros y una profunda reflexión sobre el sentido trágico de la vida. En 1927, Hemingway publicó Fiesta, iniciando así una serie de novelas-reportaje relacionadas con su fascinación por el mundo de los toros. A esta siguió Muerte en la tarde (1932) que es, además de una descripción técnica y minuciosa de una corrida vista desde los ojos de un profano, un ensayo profundo y sin concesiones sobre el arte del riesgo y la estrecha relación entre vida y crueldad con el que Hemingway regresa, una vez más, al tema que cohesiona su obra: el sentimiento trágico de la vida y el instinto de autodestrucción. José Luis Castillo-Puche dijo... «Solo su obsesión por la muerte nos explica su afición casi mística a lo taurino.»",
	            "Una obra póstuma, aunque terminada en vida, sobre la complejidad del amor y de la creación artística. Por el Premio Nobel de Literatura Ernest Hemingway. La concepción y redacción de El jardín del Edén se inició en 1946, contemporánea de otras novelas que vieron la luz en vida del autor, como El viejo y el mar o París era una fiesta. Pero no llegó a las imprentas hasta veinticinco años después de la muerte de Hemingway. Es, por tanto, una obra póstuma, aunque terminada en vida, que trata, con una interpretación profunda, gran imaginación y una prosa vivaz, sobre la complejidad del amor y de la creación artística a través de un atípico triángulo amoroso entre el protagonista, David Bourne, su mujer Catherine y una joven que la propia Catherine coloca en el camino de su marido. No se trata exactamente de una novela autobiográfica, aunque el protagonista sea un escritor americano al que empieza a saludar el éxito, ni de una novela sobre un atípico triángulo amoroso. Es, más bien, la revelación de la ternura y vulnerabilidad que Hemingway, como ser humano, ocultaba tras su imagen pública; la amarga explicación de las características principales del artista y del precio que ha de pagar para mantener su vocación; y el nacimiento de una de las heroínas más logradas y complejas del autor: Catherine Bourne. Reseña: «Hemingway es el Stendhal de nuestro tiempo.» Cesare Pavese",
	            "Unos j�venes norteamericanos -dos varones y una chica- que viven en Par�s deciden acercarse a Pamplona con motivo de los San Fermines y emprenden un viaje en tren. Durante el viaje las tensiones afectivas entre los tres van dando lugar a diversos episodios. al llegar a Pamplona la crisis ha estallado. La chica se siente seducida por un torero espa�ol y este hecho desencadena toda una serie de hechos violentos.Personajes desgarrados, errr�ticos y descritos con tal veracidad que acabar�n dando nombre a esa Generaci�n Perdida, terminada la Primera Guerra Mundial. Sus andanzas desde la Rive Gauche a los Sanfermines, narradas con pulso tenso, en una atm�sfera desesperadamente vital, y amenazante.",
	            "Nueva traducción de una de las últimas novelas del Premio Nobel de Literatura Ernest Hemingway. Un triste óleo de la vejez, el hastío, el amor, la vida y la muerte. El coronel Richard Cantwell, enfermo y al borde del retiro, decide pasar sus últimos días en la hermosa e invernal Venecia bajo el pretexto de cazar patos para encontrarse allí con Renata, una joven aristócrata con quien mantiene un amor prohibido. El viejo militar hallará a su lado el gozo del que se ha visto privado toda su vida. Pero también allí, paseando por calles frías y rodeado del lento e implacable devenir del agua de los canales, rememorará sus hazañas bélicas durante la Segunda Guerra Mundial, que le legaron solamente recuerdos, la amistad con el maître de un hotel y una mano izquierda atrofiada. A través de la mirada desencantada de Cantwell y de una prosa inconfundible, vívida e hiriente, Al otro lado del río y entre los árboles es una obra sobrecogedora, escrita con la sensibilidad única de un autor irrepetible. Tenesse Williams dijo... «La novela más triste del mundo en la ciudad más triste del mundo. La mejor obra de Hemingway, la más delicada y honesta.»",
	            "Por quién doblan las campanas es una de las novelas más populares del Premio Nobel de Literatura Ernest Hemingway. Ambientada en la guerra civil española, la obra es una bella historia de amor y muerte que se ha convertido en un clásico de nuestro tiempo. En los tupidos bosques de pinos de una región montañosa española, un grupo de milicianos se dispone a volar un puente esencial para la ofensiva republicana. La acción cortará las comunicaciones por carretera y evitará el contraataque de los sublevados. Robert Jordan, un joven voluntario de las Brigadas Internacionales, es el dinamitero experto que ha venido a España para llevar a cabo esta misión. En las montañas descubrirá los peligros y la intensa camaradería de la guerra. Y descubrirá también a María, una joven rescatada por los milicianos de manos de las fuerzas sublevadas de Franco, de la cual se enamorará enseguida. Reseña: «La novela quele dio a Hemingway lo mejor y lo peor que puede recibir alguien con mentalidad de atleta: un triunfo insuperable.» Juan Villoro",
	            "Una inolvidable historia de amor entre una enfermera y un joven soldado idealista en la Italia de la I Guerra Mundial. Por el Premio Nobel de Literatura Ernest Hemingway. No amaba a Catherine Barkley, ni se le ocurría que pudiera amarla. Aquello era como el bridge, un juego donde te largas a hablar en vez de manejar las cartas. Eso pensaba el teniente americano Frederic Henry, conductor de ambulancias en el frente italiano durante la Primera Guerra Mundial, al poco de conocer a esta bella enfermera británica. Lo que parecía un juego se convirtió en pasión intensa, mientras la guerra lo arrasaba todo y los hombres desfilaban bajo la lluvia, agotados y hambrientos, sin pensar más que en huir de la muerte. Inspirada en las vivencias de Hemingway, Adiós a las armas es ya un clásico de la literatura universal y uno de los mejores retratos de la voluntad humana. Reseña: «Un libro precioso, conmovedor y lleno de humanidad.» Vita Sackville-West «El escritor estadounidense más célebre desde Mark Twain: con él la literatura yanqui entró en una nueva dimensión.» Jaime G. Mora, ABC «Su paleta era increíblemente amplia, y exquisita y violenta y brutal y fea, era todas esas cosas. Con todos sus defectos, con todas las dificultades, su vida personal o lo que sea, parecía entender al ser humano.» Michael Katakis «Cuando se logra desmontar una de Faulkner uno tiene la impresión de que le sobran resortes y tornillos y que será imposible devolverla otra vez a su estado original. Hemingway, en cambio, con menos inspiración, con menos pasión y menos locura, pero con un rigor lúcido, dejaba sus tornillos a la vista por el lado de fuera, como en los vagones de ferrocarril. Tal vez por eso Faulkner es un escritor que tuvo mucho que ver con mi alma, pero Hemingway es el que más ha tenido que ver con mi oficio.» Gabriel García Márquez «Hemingway dejaba una intensa vida de aventuras, emociones y sentimientos que supo llevar a sus relatos magistrales. [...] Literatura sencilla, cruda, hermosa y perfecta. Escribía como vivía y ello le permitió crear su propio estilo, único, inconfundible y genial. El estilo Hemingway.» Javier García Recio, La Opinión de Málaga «Pocos como Hemingway cumplen el proverbio \"el escritor muere, pero su obra permanece\".» Vanessa Jaklitsch, La Razón «Mira el mundo sin prejuicios ni preconceptos y graba con precisión y economía, y con una inmediatez casi aterradora, exactamente lo que ve.» Javier García Recio, La Opinión «Su pasión por narrar lo lleva a la selección de la realidad, a las omisiones, al lenguaje minimalista, a esa voluntad de relatar lo real que se convierte en su poética personal y su lirismo.» Ricardo Lladosa, Zenda Libros",
	            "Una inolvidable historia de amor entre una enfermera y un joven soldado idealista en la Italia de la I Guerra Mundial. Por el Premio Nobel de Literatura Ernest Hemingway. No amaba a Catherine Barkley, ni se le ocurría que pudiera amarla. Aquello era como el bridge, un juego donde te largas a hablar en vez de manejar las cartas. Eso pensaba el teniente americano Frederic Henry, conductor de ambulancias en el frente italiano durante la Primera Guerra Mundial, al poco de conocer a esta bella enfermera británica. Lo que parecía un juego se convirtió en pasión intensa, mientras la guerra lo arrasaba todo y los hombres desfilaban bajo la lluvia, agotados y hambrientos, sin pensar más que en huir de la muerte. Inspirada en las vivencias de Hemingway, Adiós a las armas es ya un clásico de la literatura universal y uno de los mejores retratos de la voluntad humana. ENGLISH DESCRIPTION An unforgettable love story between a nurse and an idealistic young soldier in World War I Italy. By the Nobel Laureate Ernest Hemingway. He did not love Catherine Barkley, nor did it occur to him that he might ever love her. This was like playing bridge, a game where you talk endlessly instead of dealing with the cards. That's what Lieutenant Frederic Henry, an American ambulance driver on the Italian front during World War I, thought shortly after meeting this beautiful British nurse. What seemed like a game turned into an intense passion, as the war swept through everything and the demoralized men marched in the rain, exhausted and hungry, thinking of nothing else but escaping death. This gripping, semi-autobiographical work captures the harsh realities of war and the pain of lovers caught in its inexorable sweep. Inspired by Hemingway's experiences, Adiós a las armas / A Farewell to Arms is a classic in world literature and one of the best portraits of human willpower."
	        ],
	        "v_publisher": [
	            "Editorial Verbum",
	            "LUMEN",
	            "LUMEN",
	            "DEBOLS!LLO",
	            "DEBOLS!LLO",
	            "unknown",
	            "DEBOLS!LLO",
	            "DEBOLS!LLO",
	            "LUMEN",
	            "National Geographic Books"
	        ],
	        "v_imageLinks": [
	            {
	                "smallThumbnail": "http://books.google.com/books/content?id=8VywDwAAQBAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
	                "thumbnail": "http://books.google.com/books/content?id=8VywDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
	            },
	            {
	                "smallThumbnail": "http://books.google.com/books/content?id=5SIAEAAAQBAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
	                "thumbnail": "http://books.google.com/books/content?id=5SIAEAAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
	            },
	            {
	                "smallThumbnail": "http://books.google.com/books/content?id=CgF7DwAAQBAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
	                "thumbnail": "http://books.google.com/books/content?id=CgF7DwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
	            },
	            {
	                "smallThumbnail": "http://books.google.com/books/content?id=8yIAEAAAQBAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
	                "thumbnail": "http://books.google.com/books/content?id=8yIAEAAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
	            },
	            {
	                "smallThumbnail": "http://books.google.com/books/content?id=8SIAEAAAQBAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
	                "thumbnail": "http://books.google.com/books/content?id=8SIAEAAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
	            },
	            {
	                "smallThumbnail": "http://books.google.com/books/content?id=Z_HTyQEACAAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api",
	                "thumbnail": "http://books.google.com/books/content?id=Z_HTyQEACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
	            },
	            {
	                "smallThumbnail": "http://books.google.com/books/content?id=7yIAEAAAQBAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
	                "thumbnail": "http://books.google.com/books/content?id=7yIAEAAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
	            },
	            {
	                "smallThumbnail": "http://books.google.com/books/content?id=7SIAEAAAQBAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
	                "thumbnail": "http://books.google.com/books/content?id=7SIAEAAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
	            },
	            {
	                "smallThumbnail": "http://books.google.com/books/content?id=4SIAEAAAQBAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
	                "thumbnail": "http://books.google.com/books/content?id=4SIAEAAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
	            },
	            {
	                "smallThumbnail": "http://books.google.com/books/content?id=UnKREAAAQBAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api",
	                "thumbnail": "http://books.google.com/books/content?id=UnKREAAAQBAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
	            }
	        ]
	    },
	    {
	        "source": "open_library",
	        "author_name": "Ernest Hemingway",
	        "total_books": 1075,
	        "book_title": [
	            "A Farewell to Arms",
	            "For Whom the Bell Tolls",
	            "The Sun Also Rises",
	            "The Old Man and the Sea",
	            "To have and have not",
	            "Short stories",
	            "Green hills of Africa",
	            "Men Without Women",
	            "In our time",
	            "Death in the afternoon",
	            "A moveable feast",
	            "Across the river and into the trees",
	            "The torrents of spring",
	            "The fifth column",
	            "The snows of Kilimanjaro, and other stories",
	            "Islands in the stream",
	            "Old Man and the Sea",
	            "The garden of Eden",
	            "By-line: Ernest Hemingway",
	            "By-Line",
	            "Ernest Hemingway - Muerte en la Tarde",
	            "Ernest Hemingway - Fiesta",
	            "The snows of Kilimanjaro",
	            "The Essential Hemingway",
	            "The first forty-nine stories",
	            "Nick Adams Stories",
	            "The dangerous summer",
	            "Sun Also Rises",
	            "Winner take nothing",
	            "Sun Also Rises",
	            "Moveable Feast",
	            "Viejo y el Mar",
	            "The Hemingway reader",
	            "Men at war",
	            "Three stories & ten poems",
	            "Death in the Afternoon",
	            "Sun Also Rises",
	            "In Our Time",
	            "The collected poems of Ernest Hemingway",
	            "True at first light",
	            "Old Man and the Sea",
	            "Men Without Women",
	            "Torrents of Spring",
	            "Moveable Feast by Ernest Hemingway Illustrated",
	            "Moveable Feast",
	            "Mort dans l'après-midi",
	            "Sun Also Rises",
	            "Viejo y el Mar",
	            "Sun Also Rises",
	            "Moveable Feast",
	            "Green Hills of Africa",
	            "Across the River and into the Trees",
	            "Sun Also Rises",
	            "Sun Also Rises",
	            "The old man and the sea",
	            "Farewell to Arms",
	            "Fiesta",
	            "For Whom the Bell Tolls",
	            "Cinquante mille dollars",
	            "Ernest Hemingway on writing",
	            "Ernest Hemingway - Muerte en la Tarde",
	            "Farewell to Arms",
	            "Sun Also Rises",
	            "The Sun Also Rises",
	            "Old Man and the Sea",
	            "Sun Also Rises",
	            "Winner Take Nothing",
	            "Men Without Women",
	            "FOR WHOM THE BELL TOLLS",
	            "By-line : Ernest Hemingway",
	            "Winner Take Nothing",
	            "A Farewell to Arms",
	            "Moveable Feast",
	            "A Farewell to Arms",
	            "Men Without Women",
	            "Green Hills of Africa [Bulgarian]",
	            "Old Man and the Sea",
	            "Death in the Afternoon",
	            "In Our Time",
	            "Death in the Afternoon",
	            "Selected Letters, 1917-1961",
	            "Poems",
	            "Le soleil se lève aussi",
	            "Dateline, Toronto",
	            "Paris Era Una Fiesta / Paris Was Festive",
	            "Across the River and into the Trees",
	            "Men Without Women",
	            "Ernest Hemingway - Muerte en la Tarde",
	            "The Old Man and the Sea",
	            "Moveable Feast",
	            "In Our Time",
	            "For Whom the Bell Tolls",
	            "Green Hills of Africa",
	            "Ernest Hemingway, selected letters, 1917-1961",
	            "Sun Also Rises",
	            "Sun Also Rises",
	            "The old man and the sea.",
	            "THE SUN ALSO RISES",
	            "Green Hills of Africa",
	            "Fiesta"
	        ]
	    }
	]
	```


[POST] http://localhost:8000/library/books_author

- Request
	```
	{
	    "id": "UnKREAAAQBAJ",
	    "source": "google_books"
	}
	```
- Response
	```
	{
	    "source": "google_books",
	    "id_api_google": "UnKREAAAQBAJ",
	    "author_name": "Ernest Hemingway",
	    "total_books": 117,
	    "book_title": [
		"Fiesta",
		"El viejo y el mar",
		"En nuestro tiempo",
		"Muerte en la tarde",
		"El jardín del Edén",
		"Ernest Hemingway - Fiesta",
		"Al otro lado del río y entre los árboles",
		"Por quién doblan las campanas",
		"Adiós a las armas",
		"Adiós a las armas / A Farewell to Arms"
	    ],
	    "v_subtitle": [
		"unknown",
		"unknown",
		"Prólogo de Ricardo Piglia",
		"unknown",
		"unknown",
		"unknown",
		"unknown",
		"unknown",
		"unknown",
		"unknown"
	    ],
	    "v_authors": [
		[
		    "Ernest Hemingway"
		],
		[
		    "Ernest Hemingway"
		],
		[
		    "Ernest Hemingway"
		],
		[
		    "Ernest Hemingway"
		],
		[
		    "Ernest Hemingway"
		],
		[
		    "Ernest Hemingway"
		],
		[
		    "Ernest Hemingway"
		],
		[
		    "Ernest Hemingway"
		],
		[
		    "Ernest Hemingway"
		],
		[
		    "Ernest Hemingway"
		]
	    ],
	    "v_categories": [
		[
		    "Fiction"
		],
		[
		    "Fiction"
		],
		[
		    "Fiction"
		],
		[
		    "Fiction"
		],
		[
		    "Fiction"
		],
		"unknown",
		[
		    "Fiction"
		],
		[
		    "Fiction"
		],
		[
		    "Fiction"
		],
		[
		    "Fiction"
		]
	    ],
	    "v_publishedDate": [
		"1944-01-01",
		"2020-10-01",
		"2018-11-18",
		"2020-10-01",
		"2020-10-01",
		"2019-09-15",
		"2020-10-01",
		"2020-10-01",
		"2020-10-01",
		"2021-06-22"
	    ],
	    "v_description": [
		"Después de la Primera Guerra Mundial, Jake Barnes, un periodista estadounidense que fue herido en la contienda, se reencuentra con Brett Ashley –una enfermera que también ha participado en la guerra– en París, ciudad donde empezarán a relacionarse con la comunidad norteamericana. Desde la capital francesa estos dos protagonistas se dirigen junto con Bill, Mike y Cohn a España, donde tienen previsto ir a pescar y acudir a las fiestas de San Fermín en Pamplona. Durante las celebraciones, que el autor describe con gran detalle, se suceden una serie de problemas amorosos entre Brett; su prometido Michael; Cohn –con el que ha mantenido un romance tiempo atrás– y un joven y prometedor torero llamado Pedro Romero.",
		"Una de las historias más grandes jamás contadas. En esta nueva y magistral traducción de Miguel Temprano García, El viejo y el mar recobra todo el esplendor del clásico imperecedero que le valió el Premio Pulitzer de 1953 a Ernest Hemingway. Con un lenguaje de gran fuerza y sencillez, El viejo y el mar narra la historia de un viejo pescador cubano a quien la suerte parece haber abandonado, y del desafío mayúsculo al que se enfrenta: la batalla despiadada y sin tregua con un pez gigantesco en las aguas del golfo. Escrito en 1952, por encargo de la revista Life, este relato lo confirmó como uno de los escritores más significativos del siglo XX, obteniendo el Premio Pulitzer en 1953 y allanando su carrera hacia el Nobel de Literatura, que recibió en 1954. Reseñas: «Su mejor obra. El tiempo demostrará que es la mejor que cualquiera de nosotros haya escrito, y con eso me refiero a sus coetáneos y a los míos.» William Faulkner «El escritor estadounidense más célebre desde Mark Twain: con él la literatura yanqui entró en una nueva dimensión.» Jaime G. Mora, ABC «Su paleta era increíblemente amplia, y exquisita y violenta y brutal y fea, era todas esas cosas. Con todos sus defectos, con todas las dificultades, su vida personal o lo que sea, parecía entender al ser humano.» Michael Katakis «Cuando se logra desmontar una de Faulkner uno tiene la impresión de que le sobran resortes y tornillos y que será imposible devolverla otra vez a su estado original. Hemingway, en cambio, con menos inspiración, con menos pasión y menos locura, pero con un rigor lúcido, dejaba sus tornillos a la vista por el lado de fuera, como en los vagones de ferrocarril. Tal vez por eso Faulkner es un escritor que tuvo mucho que ver con mi alma, pero Hemingway es el que más ha tenido que ver con mi oficio.» Gabriel García Márquez «Hemingway dejaba una intensa vida de aventuras, emociones y sentimientos que supo llevar a sus relatos magistrales. [...] Literatura sencilla, cruda, hermosa y perfecta. Escribía como vivía y ello le permitió crear su propio estilo, único, inconfundible y genial. El estilo Hemingway.» Javier García Recio, La Opinión de Málaga «Pocos como Hemingway cumplen el proverbio \"el escritor muere, pero su obra permanece\".» Vanessa Jaklitsch, La Razón «Mira el mundo sin prejuicios ni preconceptos y graba con precisión y economía, y con una inmediatez casi aterradora, exactamente lo que ve.» Javier García Recio, La Opinión «Su pasión por narrar lo lleva a la selección de la realidad, a las omisiones, al lenguaje minimalista, a esa voluntad de relatar lo real que se convierte en su poética personal y su lirismo.» Ricardo Lladosa, Zenda Libros",
		"Primera edición en español del primer libro de cuentos de Ernest Hemingway. Incluye clásicos como \"Campamento indio\" y \"El río de los dos corazones\". Una obra fundamental de uno de los escritores norteamericanos más importantes del siglo XX. Con prólogo de Ricardo Piglia. «No me había movido; no había querido levantarme para encender la lámpara porque temía quebrar el sortilegio de esa prosa. Concluí el libro en plena oscuridad. Cuando por fin me levanté y prendí la luz ya era otro.» Fragmento del prólogo de Ricardo Piglia Hemingway publicó En nuestro tiempo; su primer libro de cuentos; en 1925. Tenía 26 años y ya escribía como un veterano. Esta primera edición en español; deuda incomprensible que debía ser saldada; respeta el orden original de un libro de cuentos que; por su organicidad y consistencia interna; puede también leerse como una novela fragmentada. La guerra y el alcohol; la pesca y los toros; la soledad atormentada de Nick Adams ya están aquí; orbitando alrededor de ese núcleo emocional que Hemingway nunca nombra pero hacia el que sus relatos siempre gravitan. Ricardo Piglia tenía 18 años cuando encontró un ejemplar usado de In Our Time en una librería de Mar del Plata. Lo leyó entero esa misma tarde. Su prólogo a esta edición (que escribió poco antes de su muerte) invita a los fieles lectores de Hemingway a participar de un diálogo iluminador y es; al mismo tiempo; una inmejorable presentación para aquellos afortunados a punto de cruzar esta puerta por primera vez.",
		"Una obra que refleja la fascinación del Premio Nobel de Literatura por las corridas de toros y una profunda reflexión sobre el sentido trágico de la vida. En 1927, Hemingway publicó Fiesta, iniciando así una serie de novelas-reportaje relacionadas con su fascinación por el mundo de los toros. A esta siguió Muerte en la tarde (1932) que es, además de una descripción técnica y minuciosa de una corrida vista desde los ojos de un profano, un ensayo profundo y sin concesiones sobre el arte del riesgo y la estrecha relación entre vida y crueldad con el que Hemingway regresa, una vez más, al tema que cohesiona su obra: el sentimiento trágico de la vida y el instinto de autodestrucción. José Luis Castillo-Puche dijo... «Solo su obsesión por la muerte nos explica su afición casi mística a lo taurino.»",
		"Una obra póstuma, aunque terminada en vida, sobre la complejidad del amor y de la creación artística. Por el Premio Nobel de Literatura Ernest Hemingway. La concepción y redacción de El jardín del Edén se inició en 1946, contemporánea de otras novelas que vieron la luz en vida del autor, como El viejo y el mar o París era una fiesta. Pero no llegó a las imprentas hasta veinticinco años después de la muerte de Hemingway. Es, por tanto, una obra póstuma, aunque terminada en vida, que trata, con una interpretación profunda, gran imaginación y una prosa vivaz, sobre la complejidad del amor y de la creación artística a través de un atípico triángulo amoroso entre el protagonista, David Bourne, su mujer Catherine y una joven que la propia Catherine coloca en el camino de su marido. No se trata exactamente de una novela autobiográfica, aunque el protagonista sea un escritor americano al que empieza a saludar el éxito, ni de una novela sobre un atípico triángulo amoroso. Es, más bien, la revelación de la ternura y vulnerabilidad que Hemingway, como ser humano, ocultaba tras su imagen pública; la amarga explicación de las características principales del artista y del precio que ha de pagar para mantener su vocación; y el nacimiento de una de las heroínas más logradas y complejas del autor: Catherine Bourne. Reseña: «Hemingway es el Stendhal de nuestro tiempo.» Cesare Pavese",
		"Unos j�venes norteamericanos -dos varones y una chica- que viven en Par�s deciden acercarse a Pamplona con motivo de los San Fermines y emprenden un viaje en tren. Durante el viaje las tensiones afectivas entre los tres van dando lugar a diversos episodios. al llegar a Pamplona la crisis ha estallado. La chica se siente seducida por un torero espa�ol y este hecho desencadena toda una serie de hechos violentos.Personajes desgarrados, errr�ticos y descritos con tal veracidad que acabar�n dando nombre a esa Generaci�n Perdida, terminada la Primera Guerra Mundial. Sus andanzas desde la Rive Gauche a los Sanfermines, narradas con pulso tenso, en una atm�sfera desesperadamente vital, y amenazante.",
		"Nueva traducción de una de las últimas novelas del Premio Nobel de Literatura Ernest Hemingway. Un triste óleo de la vejez, el hastío, el amor, la vida y la muerte. El coronel Richard Cantwell, enfermo y al borde del retiro, decide pasar sus últimos días en la hermosa e invernal Venecia bajo el pretexto de cazar patos para encontrarse allí con Renata, una joven aristócrata con quien mantiene un amor prohibido. El viejo militar hallará a su lado el gozo del que se ha visto privado toda su vida. Pero también allí, paseando por calles frías y rodeado del lento e implacable devenir del agua de los canales, rememorará sus hazañas bélicas durante la Segunda Guerra Mundial, que le legaron solamente recuerdos, la amistad con el maître de un hotel y una mano izquierda atrofiada. A través de la mirada desencantada de Cantwell y de una prosa inconfundible, vívida e hiriente, Al otro lado del río y entre los árboles es una obra sobrecogedora, escrita con la sensibilidad única de un autor irrepetible. Tenesse Williams dijo... «La novela más triste del mundo en la ciudad más triste del mundo. La mejor obra de Hemingway, la más delicada y honesta.»",
		"Por quién doblan las campanas es una de las novelas más populares del Premio Nobel de Literatura Ernest Hemingway. Ambientada en la guerra civil española, la obra es una bella historia de amor y muerte que se ha convertido en un clásico de nuestro tiempo. En los tupidos bosques de pinos de una región montañosa española, un grupo de milicianos se dispone a volar un puente esencial para la ofensiva republicana. La acción cortará las comunicaciones por carretera y evitará el contraataque de los sublevados. Robert Jordan, un joven voluntario de las Brigadas Internacionales, es el dinamitero experto que ha venido a España para llevar a cabo esta misión. En las montañas descubrirá los peligros y la intensa camaradería de la guerra. Y descubrirá también a María, una joven rescatada por los milicianos de manos de las fuerzas sublevadas de Franco, de la cual se enamorará enseguida. Reseña: «La novela quele dio a Hemingway lo mejor y lo peor que puede recibir alguien con mentalidad de atleta: un triunfo insuperable.» Juan Villoro",
		"Una inolvidable historia de amor entre una enfermera y un joven soldado idealista en la Italia de la I Guerra Mundial. Por el Premio Nobel de Literatura Ernest Hemingway. No amaba a Catherine Barkley, ni se le ocurría que pudiera amarla. Aquello era como el bridge, un juego donde te largas a hablar en vez de manejar las cartas. Eso pensaba el teniente americano Frederic Henry, conductor de ambulancias en el frente italiano durante la Primera Guerra Mundial, al poco de conocer a esta bella enfermera británica. Lo que parecía un juego se convirtió en pasión intensa, mientras la guerra lo arrasaba todo y los hombres desfilaban bajo la lluvia, agotados y hambrientos, sin pensar más que en huir de la muerte. Inspirada en las vivencias de Hemingway, Adiós a las armas es ya un clásico de la literatura universal y uno de los mejores retratos de la voluntad humana. Reseña: «Un libro precioso, conmovedor y lleno de humanidad.» Vita Sackville-West «El escritor estadounidense más célebre desde Mark Twain: con él la literatura yanqui entró en una nueva dimensión.» Jaime G. Mora, ABC «Su paleta era increíblemente amplia, y exquisita y violenta y brutal y fea, era todas esas cosas. Con todos sus defectos, con todas las dificultades, su vida personal o lo que sea, parecía entender al ser humano.» Michael Katakis «Cuando se logra desmontar una de Faulkner uno tiene la impresión de que le sobran resortes y tornillos y que será imposible devolverla otra vez a su estado original. Hemingway, en cambio, con menos inspiración, con menos pasión y menos locura, pero con un rigor lúcido, dejaba sus tornillos a la vista por el lado de fuera, como en los vagones de ferrocarril. Tal vez por eso Faulkner es un escritor que tuvo mucho que ver con mi alma, pero Hemingway es el que más ha tenido que ver con mi oficio.» Gabriel García Márquez «Hemingway dejaba una intensa vida de aventuras, emociones y sentimientos que supo llevar a sus relatos magistrales. [...] Literatura sencilla, cruda, hermosa y perfecta. Escribía como vivía y ello le permitió crear su propio estilo, único, inconfundible y genial. El estilo Hemingway.» Javier García Recio, La Opinión de Málaga «Pocos como Hemingway cumplen el proverbio \"el escritor muere, pero su obra permanece\".» Vanessa Jaklitsch, La Razón «Mira el mundo sin prejuicios ni preconceptos y graba con precisión y economía, y con una inmediatez casi aterradora, exactamente lo que ve.» Javier García Recio, La Opinión «Su pasión por narrar lo lleva a la selección de la realidad, a las omisiones, al lenguaje minimalista, a esa voluntad de relatar lo real que se convierte en su poética personal y su lirismo.» Ricardo Lladosa, Zenda Libros",
		"Una inolvidable historia de amor entre una enfermera y un joven soldado idealista en la Italia de la I Guerra Mundial. Por el Premio Nobel de Literatura Ernest Hemingway. No amaba a Catherine Barkley, ni se le ocurría que pudiera amarla. Aquello era como el bridge, un juego donde te largas a hablar en vez de manejar las cartas. Eso pensaba el teniente americano Frederic Henry, conductor de ambulancias en el frente italiano durante la Primera Guerra Mundial, al poco de conocer a esta bella enfermera británica. Lo que parecía un juego se convirtió en pasión intensa, mientras la guerra lo arrasaba todo y los hombres desfilaban bajo la lluvia, agotados y hambrientos, sin pensar más que en huir de la muerte. Inspirada en las vivencias de Hemingway, Adiós a las armas es ya un clásico de la literatura universal y uno de los mejores retratos de la voluntad humana. ENGLISH DESCRIPTION An unforgettable love story between a nurse and an idealistic young soldier in World War I Italy. By the Nobel Laureate Ernest Hemingway. He did not love Catherine Barkley, nor did it occur to him that he might ever love her. This was like playing bridge, a game where you talk endlessly instead of dealing with the cards. That's what Lieutenant Frederic Henry, an American ambulance driver on the Italian front during World War I, thought shortly after meeting this beautiful British nurse. What seemed like a game turned into an intense passion, as the war swept through everything and the demoralized men marched in the rain, exhausted and hungry, thinking of nothing else but escaping death. This gripping, semi-autobiographical work captures the harsh realities of war and the pain of lovers caught in its inexorable sweep. Inspired by Hemingway's experiences, Adiós a las armas / A Farewell to Arms is a classic in world literature and one of the best portraits of human willpower."
	    ],
	    "v_publisher": [
		"Editorial Verbum",
		"LUMEN",
		"LUMEN",
		"DEBOLS!LLO",
		"DEBOLS!LLO",
		"unknown",
		"DEBOLS!LLO",
		"DEBOLS!LLO",
		"LUMEN",
		"National Geographic Books"
	    ],
	    "v_imageLinks": [
		{
		    "smallThumbnail": "http://books.google.com/books/content?id=8VywDwAAQBAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
		    "thumbnail": "http://books.google.com/books/content?id=8VywDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
		},
		{
		    "smallThumbnail": "http://books.google.com/books/content?id=5SIAEAAAQBAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
		    "thumbnail": "http://books.google.com/books/content?id=5SIAEAAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
		},
		{
		    "smallThumbnail": "http://books.google.com/books/content?id=CgF7DwAAQBAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
		    "thumbnail": "http://books.google.com/books/content?id=CgF7DwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
		},
		{
		    "smallThumbnail": "http://books.google.com/books/content?id=8yIAEAAAQBAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
		    "thumbnail": "http://books.google.com/books/content?id=8yIAEAAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
		},
		{
		    "smallThumbnail": "http://books.google.com/books/content?id=8SIAEAAAQBAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
		    "thumbnail": "http://books.google.com/books/content?id=8SIAEAAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
		},
		{
		    "smallThumbnail": "http://books.google.com/books/content?id=Z_HTyQEACAAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api",
		    "thumbnail": "http://books.google.com/books/content?id=Z_HTyQEACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
		},
		{
		    "smallThumbnail": "http://books.google.com/books/content?id=7yIAEAAAQBAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
		    "thumbnail": "http://books.google.com/books/content?id=7yIAEAAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
		},
		{
		    "smallThumbnail": "http://books.google.com/books/content?id=7SIAEAAAQBAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
		    "thumbnail": "http://books.google.com/books/content?id=7SIAEAAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
		},
		{
		    "smallThumbnail": "http://books.google.com/books/content?id=4SIAEAAAQBAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
		    "thumbnail": "http://books.google.com/books/content?id=4SIAEAAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
		},
		{
		    "smallThumbnail": "http://books.google.com/books/content?id=UnKREAAAQBAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api",
		    "thumbnail": "http://books.google.com/books/content?id=UnKREAAAQBAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
		}
	    ],
	    "Response": "Datos Guardados"
	}
	```

[DELETE] http://localhost:8000/library/books_author

- Request
	```
	{
	    "id": 1
	}
	```

 - Response
	```
	{
	    "status": "Success"
	}
	```
 
## Arquitectura de aplicación en Python
<p align="justify">
<strong>Arquitectura Hexagonal</strong>
</p>
<p align="justify">
El principal motivo para separar nuestra aplicación en dos capas (customer, library, api_google_books, api_open_library) es que cuente con su propia responsabilidad. De esta manera consigue desacoplar capas de nuestra aplicación permitiendo que evolucionen de manera aislada. Además, tener el sistema separado por responsabilidades nos facilitará:
</p>

- La reutilización y mantenibilidad
- Pruebas unitarias
- Más tolerantes a cambios (Responsabilidad única)
- Desacoplamiento

## Uso de buenas prácticas.
<p align="justify">
<strong>Implementación de principios solid</strong>
</p>

- Principio de Responsabilidad Única
- Principio de Inversión de Dependencias

<p align="justify">
<strong>Flake8 - Isort</strong>
</p>

<p align="justify">
Implementación de flake8 e Isort para estandarización y limpieza de código. 
</p>

## Patrones de diseño utilizados.
<p align="justify">
<strong>Patrón de arquitectura REST</strong>
</p>
<p align="justify">
Se utiliza el patrón de serialización para convertir los modelos de Django en formatos de datos que se pueden enviar a través de una API web. DRF proporciona serializadores, que son clases que convierten los modelos de Django en formatos como JSON o XML.
</p>

<p align="justify">
<strong>Patrón de serialización</strong>
</p>
<p align="justify">
Se utiliza una estructura de URL clara y jerárquica para representar los recursos, y HTTP para definir las acciones que se realizan en esos recursos.
</p>

<p align="justify">
<strong>Patrón de controlador de vista</strong>
</p>
<p align="justify">
Se utiliza el patrón de controlador de vista, que separa la lógica de presentación de la lógica de negocio. Los controladores de vista de DRF manejan las solicitudes HTTP y la lógica de negocio asociada con ellas, como la validación de datos y la autorización.
</p>

<p align="justify">
<strong>Patròn 3 Capas</strong>
</p>
<p align="justify">
Un patrón común como la arquitectura de 3 niveles, donde la aplicación se divide en capa de presentación, capa lógica y capa de datos.
</p>

<p align="justify">
<strong>Patròn separación de intereses (SoC)</strong>
</p>
<p align="justify">
Se divide la aplicación en componentes independientes que se centran en un aspecto específico de la funcionalidad de la aplicación.es decir separar la lógica del negocio de la lógica de presentación, lo que permite que los componentes de la aplicación sean más mantenibles y escalables, en este caso, la capa services.py actúa como una capa intermedia entre las vistas (interfaz de usuario) y los modelos (lógica del negocio). 
</p>

<p align="justify">
<strong>Patròn Connector</strong>
</p>
<p align="justify">
Este patròn se divide en dos partes principales: el conector y el componente. El conector actúa como una interfaz que conecta los componentes y permite que se comuniquen entre sí. Por su parte, el componente es la unidad funcional que realiza una tarea específica dentro del sistema.
</p>


## Manual de instalación

- Clonar repositorio
	```
	git clone https://github.com/leoesleoesleo/03_project_.git
	```

- Levantar contenedor Docker
	```
	docker-compose -p project_test up --build
	```

- Entrar al contenedor en modo bash (opcional)
	```
	docker-compose -p project_test run web bash
	```

### Pasos generales

- Crear archivo de variables de entorno .env basado en .env.example

- Entrar al contenedor en modo bash y migrar la base de datos, en la altura del archivo manage.py
    ```
   python manage.py makemigrations
    ```
    ```
   python manage.py migrate
    ``` 

- Ejecutar pruebas unitarias (Opcional)
   ```
   pytest -v  
    ``` 

- Validar cobertura de la aplicación (Opcional)
    ```
   coverage run -m pytest -v -p no:cacheprovider --junitxml=junit/test-results.xml --cov=. --cov-report=xml --cov-report=html  
    ```    
    
- Crear super usuario en auth_user, en la altura del archivo manage.py
    ```
   python manage.py createsuperuser
    ```
    
- Ejecutar Fixtures, en la altura del archivo manage.py
    ```
   python3 manage.py loaddata fixtures/data_customer_customer.json
   python3 manage.py loaddata fixtures/data_library_editor.json
   python3 manage.py loaddata fixtures/data_library_category.json
   python3 manage.py loaddata fixtures/data_library_author.json
   python3 manage.py loaddata fixtures/data_library_book.json
   python3 manage.py loaddata fixtures/data_library_bookauthor.json
   python3 manage.py loaddata fixtures/data_library_bookcategory.json
    ```

- Administrar Usuarios desde el panel admin Django(Opcional)
    ```
   http://127.0.0.1:8000/admin/
    ```
