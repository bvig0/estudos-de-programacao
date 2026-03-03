import readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";
const rl = readline.createInterface({ input, output });

let cod = parseInt(rl.question("Código do funcionário: "));
let anoNasc = parseInt(rl.question("Digite o ano de nascimento: "));
let anoEntrada = parseInt(rl.question("Digite o ano que entrou na empresa: "));

let idade = 2025 - anoNasc;
let tempoEmpresa = 2025 - anoEntrada;

if (idade >= 65 || tempoEmpresa > 30 || idade >= 60 && tempoEmpresa > 25) {
    console.log("Requerer aposentadoria.");
}
else {
    console.log("Não requerer aposentadoria.");
}