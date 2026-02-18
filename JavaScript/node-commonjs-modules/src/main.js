const products = require("./services/products");
const { getFullName, productType } = require("./services/products");
const config = require("./services/config");
const database = require("./services/database");

async function main() {
    console.log("Carrinho de compras:");
    // products.getProductLabel("RAM");

    // Mesma função, jeitos diferentes de chamar e exportar
    products.getFullName(404, "RAM");
    getFullName(1, "teclado");

    console.log(config.client);
    database.connectToDatabase("Dados");
}

main();