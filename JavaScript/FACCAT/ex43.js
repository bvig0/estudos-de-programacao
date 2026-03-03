import readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";
const rl = readline.createInterface({ input, output });

let ladoA = parseFloat(rl.question("Digite o valor do 1° lado:"));
let ladoB = parseFloat(rl.question("Digite o valor do 2° lado:"));
let ladoC = parseFloat(rl.question("Digite o valor do 3° lado:"));
let mens = ""

if (ladoA < ladoB + lado3 && ladoB < ladoA + lado3 && ladoC < ladoA + ladoB) {
    if (ladoA == lado && ladoB == ladoC) {
        mens = "Triângulo Equilátero";
    }
    else if (ladoA == ladoB || ladoB == ladoC || ladoA == ladoC) {
        mens = "Triângulo Isósceles";
    }
    else {
        mens = "Triângulo Escaleno";
    }
}
else {
    mens = "Não foi possível formar um triângulo";
}
console.log(mens);