import readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";
const rl = readline.createInterface({ input, output });

let combustivel = rl.question("Digite o tipo de combustível (A-álcool, G-gasolina): ").toUpperCase();
let litros = parseFloat(rl.question("Digite a quatidade de litros: "));
let valor = 0;
let desconto = 0;

if (combustivel == "A") {
    valor = 2.9;
    if (litros <= 20) desconto = 0.03;
    else desconto = 0.05;
}
else if (combustivel == "G") {
    valor = 3.30;
    if (litros <= 20) desconto = 0.04;
    else desconto = 0.06;
}

valor = litros * valor * (1 - desconto);
console.log("O valor a ser pago é: R$ " + valor);