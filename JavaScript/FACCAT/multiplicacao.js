import readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";
const rl = readline.createInterface({ input, output });

let valor1 = parseInt(rl.question("Digite o primeiro número:"));
let valor2 = parseInt(rl.question("Digite o segundo número:"));
let multiplicacao = valor1 * valor2;

console.log("A soma dos dois números é: " + multiplicacao);