import readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";
const rl = readline.createInterface({ input, output });

let base = parseFloat(rl.question("Digite a base:"));
let altura = parseFloat(rl.question("Digite a base:"));
let retangulo = base * altura;

console.log('A área do retângulo é: ' + retangulo)
