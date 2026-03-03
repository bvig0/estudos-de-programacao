import readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";
const rl = readline.createInterface({ input, output });

let valor1 = parseInt(rl.question("Digite um valor:"));
let valor2 = parseInt(rl.question("Digite outro valor:"));

if (valor1 > valor2) console.log("Primeiro número é maior.");
else if (valor1 < valor2) console, log("Segundo número é maior.");
else console, log("Números iguais.");