import flet as ft 
import asyncio

num = 1

#Centros en lista 
centros1_list = ["Galletitas estilo levain ", "Galletitas de coco sin Tacc", "Galletitas de avena y pasas","Galletitas de manteca "] 
centros1 = centros1_list[0]# Inicializar
centros2_list = ["Galletitas remolino de chocolate y vainilla.","Galletitas con chips - sin TACC","Galletitas veganas de avena y cacao","Galletitas integrales de banana y cacao"]
centros2= centros2_list[0]
centros3_list = ["Galletitas con chips de chocolate","Galletitas de limón con arándanos sin gluten","Galletitas de Naranja y Chips de Chocolate","Galletitas de coco y centeno"]
centros3= centros3_list[0]

#Imagenes en lista
image1_list = ["https://img-global.cpcdn.com/recipes/76a8b342b52ec02b/680x964cq70/galletitas-estilo-levain-riquisimas-y-faciles-foto-principal.webp","https://img-global.cpcdn.com/recipes/21b4fc268df73124/640x640sq70/photo.webp","https://img-global.cpcdn.com/recipes/4cd271237d22589b/680x964cq70/galletitas-de-avena-y-pasas-vegan-foto-principal.webp","https://img-global.cpcdn.com/recipes/0819f540d8a65db8/640x640sq70/photo.webp"]
image1 = image1_list[0]
image2_list= ["https://img-global.cpcdn.com/recipes/5495c91dca61dea2/680x964cq70/galletitas-remolino-de-chocolate-y-vainilla-faciles-y-economicas-foto-principal.webp","https://img-global.cpcdn.com/recipes/295511e36179da4c/640x640sq70/photo.webp","https://img-global.cpcdn.com/recipes/8460e221b4f4728f/680x964cq70/galletitas-veganas-de-avena-y-cacao-sin-azucar-foto-principal.webp","https://img-global.cpcdn.com/recipes/e653d1085a2750e4/680x964cq70/galletitas-integrales-de-banana-y-cacao-sin-azucar-foto-principal.webp"]
image2 = image2_list[0]
image3_list = ["https://img-global.cpcdn.com/recipes/1165dd548f9dc283/680x964cq70/masa-para-galletitas-facil-economica-y-muy-rica-foto-principal.webp","https://img-global.cpcdn.com/recipes/38a55c092f986c45/640x640sq70/photo.webp","https://img-global.cpcdn.com/recipes/80c7d59dda2ad293/680x964cq70/galletitas-de-naranja-y-chips-de-chocolate-veganas-foto-principal.webp","https://img-global.cpcdn.com/recipes/99ad99c24bcb8a0b/680x964cq70/galletitas-de-coco-y-centeno-sin-azucar-apto-diabeticos-foto-principal.webp"]
image3 = image3_list[0]

# Lista de tipos de receta
tipos_receta_list = ["CLÁSICAS", "SIN TACC", "VEGANAS", "DIABÉTICAS"]
tipo_receta = tipos_receta_list[0]  # Inicializar con el primer tipo de receta

#ingredientes
ingredientes1 = [
    ["130 grs azúcar negra/ rubia","60 grs azúcar blanca","245 grs harina 0000","1 cta bicarbonato de sodio","1 cucharada sopera maizena (esencial)","115 grs manteca (pomada)","1 huevo","1 1/5 cdta esencia de vainilla","80/100 grs chocolate sólido amargo/semiamargo"],
    ["40 gramos coco rallado","150 gramos premezcla sin Tacc","40 gramos azúcar","1 huevo","1 cucharadita esencia de vainilla","1 cucharada aceite","1 cucharadita polvo de hornear",],
    ["70 g harina","50 g avena instantánea","25-30 g aceite neutro","40 g azúcar","30-40 ml agua o leche vegetal","1 cdita polvo de hornear","1 pizca sal","1 cdita vainilla","20 g pasas de uva",],
    ["25 gr manteca derretida","10 sobres hileret","1 huevo","1 cdita esencia de vainilla","1 cdita polvo de hornear","100 gr harina de avena"]
]
ingrediente1= ingredientes1[0]
ingredientes2 = [
    ["180 g Harina leudante","100 g Azúcar","30 g Manteca fría","1 Huevo","1 cdita Esencia de vainilla","25 g Cacao para chocolatada"],
    ["1 huevo","300 gr Premezcla sin TACC","150 gr Manteca","2 cditas Polvo para hornear","150 gr Azúcar","1 cdita Esencia de vainilla","150 gr chips de chocolate","1 cdita miel","1 cdita. Bicarbonato de sodio"],
    ["135 g avena instantánea","60 ml leche vegetal/agua","40 ml aceite de girasol","a gusto Maní","4 cucharadas stevia líquida","1 chorrito esencia de vainilla","20 g cacao amargo"],
    ["180 g harina integral","1 huevo","2 cucharadas aceite","2 cucharaditas polvo de hornear","Pizca sal","1 banana chica pisada","1 cucharada cacao amargo","1 chorrito esencia de vainilla","8 sobres edulcorante","Coco rallado c/n (opcional)"]
]
ingrediente2= ingredientes2[0]
ingredientes3 = [
    ["2 tazas harina leudante","2 huevos","Chips de chocolate","1 taza azúcar","1 taza manteca","1 cucharadita polvo para hornear"],
    ["50 cc aceite","50 gr azúcar","Esencia de vainilla","50 gr jugo de Limón y ralladura","1 huevo","150 gr pre mezcla sin gluten","1/4 cdita bicarbonato de sodio","1 cdita polvo de hornear","1/2 cdita goma xántica","Arándanos"],
    ["250 g harina 0000","100 g margarina pomada","50 g azúcar mascabo","50 g azúcar común","2 1/2 cdas maicena","1/4 cdta bicarbonato","1/2 cdta esencia de vainilla","jugo de naranja y ralladura","chips de chocolate o chocolate picado vegano"],
    ["2 tazas harina de centeno","1/2 taza coco rallado","2 cditas polvo leudante","1 yogurt natural (con o sin endulzante)","C/n esencia de vainilla","C/n agua fría","C/n chocolate al 70% (opcional)"]
]
ingrediente3= ingredientes3[0]

#Paso a paso
paso_a_paso1=[
    ["Romper el huevo en un recipiente y mezclar hasta formar del huevo una mezcla homogénea. Incorporar la cdta y media de esencia de vainilla.",
     "Agregar a la preparación la manteca pomada cortada en trozos (En el caso de no haberla dejado previamente a temperatura ambiente, es conveniente dar un corto golpe de calor hasta llegar a la consistencia deseada. ES IMPORTANTE QUE NO SE DERRITA).",
     "Por otro lado, unir a la mezcla todos los ingredientes secos",
     "Luego de formar una masa homogénea, picar aprox 50 gr de chocolate amargo/ semiamargo (A mí me gusta con mucho chocolate, se puede usar menos) e incluir a la mezcla sin que el chocolate se derrita.",
     "Hacer un bollo con la masa obtenida y colocar en un bowl tapado (puede ser con film o un trapo), dejar reposar por 30/40 minutos en la heladera.",
     "15 minutos antes de sacar la preparación, recomiendo encender el horno a 160° para obtener el calor deseado a la hora de colocar las galletitas.",
     "Enmantecar una placa, realizar pequeños/medianos bollos con la preparación y colocarlos por encima de la placa. (En el caso de que la mezcla este pegajosa mojar las manos con agua para facilitar el proceso)",
     "Terminar de picar el resto de chocolate y colocar por encima. (ESTE PASO NO DEBE SER OMITIDO)",
     "Colocar la placa en el horno por aproximadamente 15/20 minutos y ya están listas!!!!"],
    ["La premezcla sin Tacc, lleva misma cantidad de leche en polvo, harina de arroz y maicena. ",
     "Lo segundo es mezclar en un bowl huevo, aceite, azúcar, la esencia. Mezclar bien.",
     "Después de mezclar todo, armar bollitos, si les queda la masa poquito líquida agregan más coco rallado. Armar en una placa y poner a horno suave de 160° por 10 minutos."],
    ["Mezclar los secos (harina, avena, polvo de hornear y sal)",
     "En un bowl aparte mezclar aceite, agua o leche y azúcar. Batir hasta que se disuelva el azúcar. Agregar la esencia de vainilla.",
     "Incorporar los líquidos al bowl de los secos. Agregar las pasas de uva.",
     "Formar 12 poriones con la mezcla y aplastarlas. Colocar en una placa para horno con papel manteca o silpat (plancha de silicona)",
     "Cocinar 20-25 min en horno precalentado a 180°C"],
    ["Empezamos mezclando la manteca con el hileret. Después añadimos el huevo con la esencia de vainilla y mezclamos.",
     "Agregamos el polvo de hornear y la harina de avena. Mezclamos todo hasta que se forme una masa.",
     "Una vez lista la masa, cortamos las galletitas, las llevamos a una placa enmantecada y las mandamos al horno medio por 10-15 minutos hasta que se doren. Después sácalas y listas para comer!"]
]
pasoapaso1= paso_a_paso1[0]
paso_a_paso2=[
    ["En un bowl colocamos la harina y el azúcar. Mezclamos y sumamos la manteca fría cortada en cubitos. Con la punta de los dedos formamos un arenado. Añadimos el huevo y la esencia de vainilla. Integramos desde el centro con una cuchara y terminamos de formar la masa sin amasar.La masa obtenida debe ser tierna pero no debe pegarse en las manos. En tal caso agregar un poco de harina. Caso contrario (ej: si el huevo usado es pequeño) que cueste formar la masa agregar apenas una cucharadita de leche.",
     "Dividimos el bollo en dos, a una parte la rompemos en trocitos y le sumamos el cacao. Unimos y rompemos hasta que quede una masa homogénea."
     ,"Cada sabor lo dividimos en pelotitas pequeñas.Colocamos enfrentadas dos pelotitas de vainilla y dos de chocolate tratando que queden unidas.",
     "Ponemos la mano ahuecada sobre esta y con movimientos circulares hacemos girar la masa. No como para formar una pelotita sino más bien como un trompito, manteniendo la unión de las masas siempre en el centro de la mano que va girando en un solo sentido y de manera circular. Chequear cómo se va formando el remolino. Al principio quizás cuesta un poco que tome forma de remolino pero es cuestión de practicar hasta tomarle la mano.",
     "Colocamos las galletas formadas en una placa con papel manteca enmantecado y aplanamos ligeramente.Cocinamos en horno precalentado a 180°C por 10 minutos o hasta que estén doradas."],
    ["Primero mezclar manteca pomada y azúcar",
     "Luego agregar el huevo, la esencia de vainilla y la miel",
     "Agregar la premezcla",
     "Por último los chips.",
     "Al horno pre-calentado 180°, por 15 min"],
    ["Mezclar la avena con el cacao.",
     "Añadir los líquidos e integrar. Si queremos le agregamos maní a nuestra preparación.",
     "En una placa con un poco de manteca le damos forma a nuestras galletitas, podemos hacerlo con una cuchara o mojándonos un poco las manos para que no se pegue la mezcla. Yo le agregue más maní por encima.",
     "Cocinar apróximadamente 25 minutos a 180° grados o hasta que estén cocidas."],
    ["En un bol ponemos los ingredientes húmedos: puré de banana, huevo, aceite y mezclamos bien. De a poco incorporamos todos los secos, aplastando con las manos, pero sin amasar, hasta unificar.",
     "Precalentar el horno. Tomamos porciones del tamaño deseado y hacemos bolitas. Yo hice unas 14. Las colocamos en una placa con rocío vegetal, esparcimos un poco de coco rallado y aplastamos un poquito con un tenedor.",
     "Llevamos al horno a temperatura media, entre 10 y 15 minutos, dependiendo del horno. Cuando la base de las galletitas esté dorada estarán listas."]
]
pasoapaso2= paso_a_paso2[0]
paso_a_paso3=[
    ["Agregamos la manteca en cubitos y desmenuzamos junto a la taza de azúcar. Agregamos los dos huevos e incorporamos todo.","Agregamos las dos tazas de harina, debe ser tamizada, junto al polvo de hornear y los chips de chocolate (o lo que quieras ponerle). La masa debe descansar 20 minutos en la heladera.","Una vez que la masa descansó, hacemos bolitas con ésta y las ponemos en una placa aceitada y enharinada, dejando espacio entre ellas. Van al horno a 180° por 20 minutos o menos, hay que revisar.","Y listo! Ya tenés tus galletitas."],
    ["En un bowl mezclar todos los secos.",
     "Por otro lado colocar el aceite, huevo, esencias azúcar, ralladura y jugo de limón. Mezclar bien.",
     "A la mezcla líquida ir añadiendo la pre mezcla hasta formar un bollo.",
     "Darle forma redonda aplanada y llevar a placa con rocio vegetal. Colocar los arándanos aplastando un poco.",
     "Llevar a horno 180 grados 15’"],
    ["Batir a mano un poco la margarina, agregar las dos azúcar, la esencia, la ralladura batir con energía para que se integren bien, con consistencia cremosa. Agregar la harina, el almidón, bicarbonato todo tamizado, unir, ir incorporando de a poco el jugo hasta que se forme el bollo, acá se le puede agregar el chocolate (yo lo puse encima ya estirada asi se ven mejor). Envolver en film y llevar al frío un par de horas.",
     "Se retira del frío, estirar con palote más o menos con un espesor de 2 a 3 mm. Cortar de la forma que gustes, yo las hice con cortante redondo de 5 cm de diámetro.",
     "Colocar en una placa untada con margarina (las podés llevar un rato a enfriar, esto ayuda a que no se deformen). Llevar a horno precalentado a 170º por 10/12 minutos(no pasarse de este tiempo). Se retiran y se dejan enfriar en la placa. No tratar de despegarlas, cuando estén frías se despegan solas."],
    ["Formar una corona con todos los ingredientes secos. Luego agregar el yogurt y la esencia. Amasar."
     ,"Formar un bollo en la mesada y estirar la masa de forma pareja. Elegir un cortante lindo. Luego pasar a una placa enmantecada y hornear unos 15 minutos con horno precalentado.",
     "Retirar de la placa y dejar enfriar. Quedan de color jaspeado y el sabor del coco y el centeno complementan muy bien. El siguiente paso es opcional: derretir chocolate y cubrir un solo extremo de las galletitas."]
]
pasoapaso3= paso_a_paso3[0]


async def carga(page: ft.Page):
    page.window_height = 700
    page.window_width = 400
    page.window_resizable = False
    page.padding = 0
    beige= '#E4C59E'
    casinegro='#322C2B'
    ImagenLogo=ft.Image(
        src="imagenes\pngwing.com.png",
        width = 60,
        height = 50,
        fit = ft.ImageFit.CONTAIN,
    )
    Carga = ft.Text(value="CARGANDO...", size=40, color=casinegro, text_align=ft.TextAlign.CENTER)
    item_inferior=[
        ft.Container(width=40, height=50),
        ft.Container(Carga,width=250, height=50),
        ft.Container(width=40, height=50)
    ]
    
    superior = ft.Container( width=350, height=180, margin=ft.margin.only(top=15))
    centro1 = ft.Container(ImagenLogo, width=350, height=150, margin=ft.margin.only(top=15))
    inferior = ft.Container(content=ft.Row(item_inferior), width=350, height=50, margin=ft.margin.only(top=10))
    
    col = ft.Column(spacing = 0,controls=[
        superior,
        centro1,
        inferior
    ])
    
    contenedor = ft.Container(col,width=400, height=700, bgcolor=beige, alignment=ft.alignment.top_center)
    
     # Añadir la pantalla de carga
    page.add(contenedor)
    
    # Esperar 5 segundos
    await asyncio.sleep(3)
    
    # Cambiar a la pantalla principal
    await main(page)

async def main(page: ft.Page):
    
    page.clean()
    page.window_height = 700
    page.window_width = 400
    page.window_resizable = False
    page.adaptive = True
    page.padding = 0
    beige= '#E4C59E'
    claro='#fedeb7'
    masclaro='#f6e7d6'
    marron='#AF8260'
    macolorado='#803D3B'
    casinegro='#322C2B'
    
    ImagenLogo=ft.Image(
        src="imagenes\pngwing.com.png",
        width = 60,
        height = 50,
        fit = ft.ImageFit.CONTAIN,
    )
    flechaDerecha=ft.Image(
        src="imagenes/flecha.com.png",
        width=50,
        height=50,
        fit = ft.ImageFit.CONTAIN,
    )
    flechaIzquierda=ft.Image(
        src="imagenes/flechaderecha.com.png",
        width=50,
        height=50,
        fit = ft.ImageFit.CONTAIN,
    )
    # Crear un Text para mostrar el número
    num_display = ft.Text(value=str(num), size=30, color=masclaro, text_align=ft.TextAlign.CENTER)
    
    #Crear texto para mostrar el tipo de receta
    tipos_receta = ft.Text(value=tipo_receta, size=30, color=casinegro, text_align=ft.TextAlign.CENTER)
    
    #Crear una imagen
    imagen1 = ft.Image(src=f"{image1}", fit=ft.ImageFit.CONTAIN)
    imagen2 = ft.Image(src=f"{image2}", fit=ft.ImageFit.CONTAIN)
    imagen3 = ft.Image(src=f"{image3}", fit=ft.ImageFit.CONTAIN)
    
    #Crear texto para mostrar el tipo centro
    cetro1= ft.Text(value=centros3, size=20, color=casinegro, text_align=ft.TextAlign.CENTER)
    cetro2= ft.Text(value=centros3, size=20, color=casinegro, text_align=ft.TextAlign.CENTER)
    cetro3= ft.Text(value=centros3, size=20, color=casinegro, text_align=ft.TextAlign.CENTER)
    def actualizar_datos():
        global num, tipo_receta, cetros1, cetros2, cetros3
        tipo_receta = tipos_receta_list[num - 1]
        cetros1 = centros1_list[num - 1]
        cetros2 = centros2_list[num - 1]
        cetros3 = centros3_list[num - 1]
        global image1, image2, image3, ingrediente1, ingrediente2, ingrediente3
        global pasoapaso1, pasoapaso2, pasoapaso3
        image1 = image1_list[num - 1]
        image2 = image2_list[num - 1]
        image3 = image3_list[num - 1]
        ingrediente1 = ingredientes1[num - 1]
        ingrediente2 = ingredientes2[num - 1]
        ingrediente3 = ingredientes3[num - 1]
        pasoapaso1 = paso_a_paso1[num - 1]
        pasoapaso2 = paso_a_paso2[num - 1]
        pasoapaso3 = paso_a_paso3[num - 1]
    
    # Definir las funciones para abrir nuevas páginas
    async def abrir_pagina1(e):
        actualizar_datos()
        await iu(page, image1, tipo_receta, ingrediente1, pasoapaso1)

    async def abrir_pagina2(e):
        actualizar_datos()
        await iu(page, image2, tipo_receta, ingrediente2, pasoapaso2)

    async def abrir_pagina3(e):
        actualizar_datos()
        await iu(page, image3, tipo_receta, ingrediente3, pasoapaso3)
    
    # Función que se llama al hacer clic en la flecha derecha
    def on_flecha_derecha_click(e):
        global num, tipo_receta
        if num < 4:
            num = num + 1
            tipo_receta = tipos_receta_list[num - 1]
            cetros1 = centros1_list[num - 1]
            cetros2 = centros2_list[num - 1]
            cetros3 = centros3_list[num - 1]
            image1 = image1_list[num - 1]
            image2 = image2_list[num - 1]
            image3 = image3_list[num - 1]
            ingrediente1= ingredientes1[num-1]
            ingrediente2= ingredientes2[num-1]
            ingrediente3= ingredientes3[num-1]
            pasoapaso1= paso_a_paso1[num - 1]
            pasoapaso2= paso_a_paso2[num - 1]
            pasoapaso3= paso_a_paso3[num - 1]
            # Actualizar el texto con el nuevo valor de num
            num_display.value = str(num)
            tipos_receta.value = tipo_receta
            cetro1.value = cetros1
            cetro2.value = cetros2
            cetro3.value = cetros3
            imagen1.src = f"{image1}"
            imagen2.src = f"{image2}"
            imagen3.src = f"{image3}"
        else:
            num = 0
            actualizar_datos    
        page.update()  # Actualizar la página
        
    # Función que se llama al hacer clic en la flecha izquierda
    def on_flecha_izquierda_click(e):
        global num, tipo_receta
        if num > 1:
            num = num - 1
            tipo_receta = tipos_receta_list[num - 1]
            cetros1 = centros1_list[num - 1]
            cetros2 = centros2_list[num - 1]
            cetros3 = centros3_list[num - 1]
            image1 = image1_list[num - 1]
            image2 = image2_list[num - 1]
            image3 = image3_list[num - 1]
            ingrediente1= ingredientes1[num-1]
            ingrediente2= ingredientes2[num-1]
            ingrediente3= ingredientes3[num-1]
            pasoapaso1= paso_a_paso1[num - 1]
            pasoapaso2= paso_a_paso2[num - 1]
            pasoapaso3= paso_a_paso3[num - 1]
            # Actualizar el texto con el nuevo valor de num
            num_display.value = str(num)
            tipos_receta.value = tipo_receta
            cetro1.value = cetros1
            cetro2.value = cetros2
            cetro3.value = cetros3
            imagen1.src = f"{image1}"
            imagen2.src = f"{image2}"
            imagen3.src = f"{image3}"
        elif num == 1: 
            num=5
            actualizar_datos
        page.update()  # Actualizar la página
            

    # Contenedor que actúa como botón para la flecha derecha
    flecha_derecha_button = ft.Container(
        content=flechaDerecha,
        width=50,
        height=50,
        alignment=ft.alignment.center,
        on_click=on_flecha_derecha_click,  # Asignar la función al evento de clic
    )

    # Contenedor que actúa como botón para la flecha izquierda
    flecha_izquierda_button = ft.Container(
        content=flechaIzquierda,
        width=50,
        height=50,
        alignment=ft.alignment.center,
        on_click=on_flecha_izquierda_click,  # Asignar la función al evento de clic
    )
    
    item_superiores = [
        ft.Container(ImagenLogo, alignment=ft.alignment.center, expand = True, padding=0),
        ft.Container(tipos_receta,width=168,height=45, bgcolor=claro, border_radius=20, ),
        ft.Container(width=60,height=60),
    ]
    item_inferiores=[
        ft.Container(width=79, height=50),
        flecha_izquierda_button,  # Usar el contenedor como botón
        ft.Container(num_display, width=50, height=50, bgcolor=marron, border=ft.border.all(2, masclaro)),
        flecha_derecha_button,  # Usar el contenedor como botón
        ft.Container(width=79, height=50)
    ]
    item_centrales1=[
        ft.Container(width=10, height=150),
        ft.Container(imagen1, width=136, height=130, on_click=abrir_pagina1),
        ft.Container(cetro1, width=178, height=140, bgcolor=masclaro),
    ]
    item_centrales2=[
        ft.Container(width=10, height=150),
        ft.Container(imagen2, width=136, height=130, on_click=abrir_pagina2),
        ft.Container(cetro2, width=178, height=140, bgcolor=masclaro),
    ]
    item_centrales3=[
        ft.Container(width=10, height=150),
        ft.Container(imagen3, width=136, height=130, on_click=abrir_pagina3),
        ft.Container(cetro3, width=178, height=140, bgcolor=masclaro),
    ]
    
    superior = ft.Container(content=ft.Row(item_superiores), width=350, height=80, margin=ft.margin.only(top=15), bgcolor=macolorado)
    centro1 = ft.Container(content=ft.Row(item_centrales1),width=350, height=150, margin=ft.margin.only(top=15), bgcolor=claro)
    centro2 = ft.Container(content=ft.Row(item_centrales2),width=350, height=150, margin=ft.margin.only(top=5), bgcolor=claro)
    centro3 = ft.Container(content=ft.Row(item_centrales3),width=350, height=150, margin=ft.margin.only(top=5), bgcolor=claro)
    inferior = ft.Container(content=ft.Row(item_inferiores) ,width=350, height=50, margin=ft.margin.only(top=15))
    col = ft.Column(spacing = 0,controls=[
        superior,
        centro1,
        centro2,
        centro3,
        inferior
    ])
    
    contenedor = ft.Container(col,width=400, height=700, bgcolor=beige, alignment=ft.alignment.top_center)
    
    await page.add_async(contenedor)
    
async def iu(page: ft.Page, image, tipo_receta, ingredientes, pasoapaso):
    page.clean()
    page.window_height = 700
    page.window_width = 400
    page.window_resizable = False
    page.padding = 0
    beige = '#E4C59E'
    claro = '#fedeb7'
    casinegro = '#322C2B'

    async def on_flecha_salida_click(e):
        await main(page)

    # Botón de salida
    ImgSalida = ft.Image(
        src="imagenes/flecaParacerrar.png",
        width=50,
        height=50,
        fit=ft.ImageFit.CONTAIN,
    )
    Salida_button = ft.Container(
        content=ImgSalida,
        width=50,
        height=50,
        alignment=ft.alignment.center,
        expand=True,
        padding=0,
        on_click=on_flecha_salida_click,  # Asignar la función al evento de clic
    )

    # Contenido superior (tipo_receta como ft.Text)
    item_superiores = [
        Salida_button,
        ft.Container(
            content=ft.Text(value=tipo_receta, size=30, color=casinegro, text_align=ft.TextAlign.CENTER),  # Mostrar el tipo de receta
            width=289,
            height=50,
            border_radius=15,
            bgcolor=claro
        )
    ]

    # Contenedor superior
    superior = ft.Container(
        content=ft.Row(item_superiores),
        width=350,
        height=50,
        margin=ft.margin.only(top=15)
    )

    # Contenedor central con imagen
    centro1 = ft.Container(
        content=ft.Image(
            src=image,  # Pasar la ruta o fuente de la imagen
            width=350,
            height=150,
            fit=ft.ImageFit.CONTAIN
        ),
        width=350,
        height=150,
        margin=ft.margin.only(top=15)
    )

    # Ingredientes con barra de desplazamiento
    centro2 = ft.Container(
        content=ft.ListView(
            controls=[
                ft.Text(value="Ingredientes:", size=20, weight="bold", color=casinegro)
            ] + [ft.Text(value=f"- {ing}", color=casinegro) for ing in ingredientes],
            expand=True,
            spacing=5,
        ),
        width=350,
        height=150,
        margin=ft.margin.only(top=15, bottom=0),
        bgcolor=claro,
        padding=ft.padding.all(10),
        border_radius=10
    )

    # Paso a paso con barra de desplazamiento
    inferior = ft.Container(
        content=ft.ListView(
            controls=[
                ft.Text(value="Paso a paso:", size=20, weight="bold", color=casinegro)
            ] + [ft.Text(value=f"{i+1}. {paso}", color=casinegro) for i, paso in enumerate(pasoapaso)],
            expand=True,
            spacing=5,
        ),
        width=350,
        height=230,
        margin=ft.margin.only(top=15),
        bgcolor=claro,
        padding=ft.padding.all(10),
        border_radius=10
    )

    # Columna con todos los elementos
    col = ft.Column(
        spacing=0,
        controls=[
            superior,
            centro1,
            centro2,
            inferior
        ]
    )

    # Contenedor principal
    contenedor = ft.Container(
        content=col,
        width=400,
        height=700,
        bgcolor=beige,
        alignment=ft.alignment.top_center
    )

    # Agregar al `page`
    await page.add_async(contenedor)



ft.app(target=carga)