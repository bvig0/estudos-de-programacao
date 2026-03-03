import readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";
const rl = readline.createInterface({ input, output });

let codUsuario = parseInt(rl.question("Digite o código do usuário:"));

if (codUsuario == 1234) {
    let senha = parseInt(rl.question("Digite a senha:"));
    if (senha == 9999) {
        console.log("Acesso permitido.");
    }
    else {
        console.log("Senha incorreta! Acesso negado.");
    }
}
else {
    console.log("Usuário inválido!");
}