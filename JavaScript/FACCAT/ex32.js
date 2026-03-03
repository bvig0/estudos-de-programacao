import readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";
const rl = readline.createInterface({ input, output });

let timeA = rl.question("Digite o primeiro time:");
let timeB = rl.question("Digite o segundo time:");
let golsA = parseInt(rl.question("Digite os gols do " + timeA + ": "));
let golsB = parseInt(rl.question("Digite os gols do " + timeB + ": "));

if (golsA > golsB) console.log(timeA + " ganhou com " + golsA + " pontos.");
else if (golsA < golsB) console.log(timeB + " ganhou com " + golsB + " pontos.");
else console.log("EMPATE.");