import readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";
const rl = readline.createInterface({ input, output });

let ladoA = parseInt(rl.question("Digite o primeiro valor:"))
let ladoB = parseInt(rl.question("Digite o segundo valor:"))
let ladoC = parseInt(rl.question("Digite o terceiro valor:"))

if(ladoA < ladoB + ladoC && ladoB < ladoA + ladoC && ladoC < ladoB + ladoA) console.log("Os valores formam um triângulo.");
else console.log("Os valores NÃO formam um triângulo.");