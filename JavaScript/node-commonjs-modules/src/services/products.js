// todas as funções que lidam com produtos
const productType = {
    version: "digital",
    tax: "x1",
};

// hidden const
const apiURL = {
    url: "www.google.com/api"
}

async function getFullName(codeID, productName) {
    console.log("produto: " + codeID + "--" + productName);
    doBreakLine();
}

// hidden function
async function doBreakLine() {
    console.log("\n");
}

async function getProductLabel(productName) {
    console.log("Product " + productName)
}

module.exports = {
    getFullName, getProductLabel, productType,
};