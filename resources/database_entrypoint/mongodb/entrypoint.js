db.createCollection("productCatalog");
db.productCatalog.insertMany([
    {
        name: "Nike Court Lite 2",
        value: 17.55,
        photos: [
            "/nike-branco/pic1.jpg",
            "/nike-branco/pic2.jpg",
            "/nike-branco/pic3.jpg",
            "/nike-branco/pic4.jpg"
        ],
        size: 44,
        color: "Branco",
        brand: "Nike",
        description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    },
    {
        name: "Wilson Slice Masculino",
        value: 29.00,
        photos: [
            "/wilson/pic1.jpg",
            "/wilson/pic2.jpg",
            "/wilson/pic3.jpg",
            "/wilson/pic4.jpg"
        ],
        size: 43,
        color: "Amarelo",
        brand: "Wilson",
        description: "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo."
    },
    {
        name: "Fila Lugano 6.0",
        value: 10.13,
        photos: [
            "/fila/pic1.jpg",
            "/fila/pic2.jpg",
            "/fila/pic3.jpg",
            "/fila/pic4.jpg"
        ],
        size: 37,
        color: "Preto",
        brand: "Fila",
        description: "Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure."
    },
    {
        name: "Nike Shox Nz Se",
        value: 50.00,
        photos: [
            "/nike-shox/pic1.jpg",
            "/nike-shox/pic2.jpg",
            "/nike-shox/pic3.jpg",
            "/nike-shox/pic4.jpg"
        ],
        size: 40,
        color: "Preto com Vermelho",
        brand: "Nike",
        description: "O Tênis Nike Shox Nz Se foi desenvolvido para os homens que não dispensam conforto e nem estilo. Uma ótima pedida para compor a produção e aproveitar a casualidade do dia a dia."
    }
]);
