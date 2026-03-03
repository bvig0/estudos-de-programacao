import readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";
const rl = readline.createInterface({ input, output });

let x = parseInt(rl.question("Digite o valor de x:"));
let y = parseInt(rl.question("Digite o valor de y:"));
let z = (x * y) + 5;
let resposta = "";

if (z <= 0) resposta = "A";
else if (z <= 100) resposta = "B";
else resposta = "C";
console.log(resposta + " - " + z);