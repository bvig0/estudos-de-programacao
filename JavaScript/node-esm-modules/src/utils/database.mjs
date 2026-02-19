// extensão "mjs" são arquivos JavaScript que são apenas modulos, ou seja, servem apenas para exportar as coisas de dentro dele

const databaseType = {
    userType: "admin",
    type: "datalocal"
}

async function connecToDatabase(dataName) {
    // lógica de conexão
    console.log("conectando ao banco " + dataName);
}

async function disconnecDatabase() {
    console.log("desconectando ao banco}");
}

// export default connecToDatabase;
export { connecToDatabase, disconnecDatabase, databaseType };
