import readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";
const rl = readline.createInterface({ input, output });

let num = parseInt(rl.question("Escreva um número para ver o seu antecessor:"));
let resp = num - 1;

console.log("O número antecessor ao digitado é: " + resp);