import readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";
const rl = readline.createInterface({ input, output });

let anos = parseInt(rl.question("Digite a sua idade/anos:"));
let meses = parseInt(rl.question("Digite quantos meses você tem"));
let dias = parseInt(rl.question("Digite quantos dias você tem:"));
dias = (anos * 365) + (meses * 30) + dias;

console.log("Total de dias vividos: " + dias);