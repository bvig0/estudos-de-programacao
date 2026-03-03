import readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";
const rl = readline.createInterface({ input, output });

let valor1 = parseInt(rl.question("Digite o primeiro valor:"));
let valor2 = parseInt(rl.question("Digite o segundo valor:"));
let valor3 = parseInt(rl.question("Digite o terceiro valor:"));

if (valor1 < valor2 && valor1 < valor3) {
    if (valor2 < valor3) {
        console.log("Organizado na ordem: " + valor1 + ", " + valor2 + ", " + valor3);
    }
    else {
        console.log("Organizado na ordem: " + valor1 + ", " + valor3 + ", " + valor2);
    }
}

else if (valor2 < valor1 && valor2 < valor3) {
    if (valor1 < valor3) {
        console.log("Organizado na ordem: " + valor2 + ", " + valor1 + ", " + valor3);
    }
    else {
        console.log("Organizado na ordem: " + valor2 + ", " + valor3 + ", " + valor1);
    }
}

else {
    if (valor1 < valor2) {
        console.log("Organizado na ordem: " + valor3 + ", " + valor1 + ", " + valor2);
    }
    else {
        console.log("Organizado na ordem: " + valor3 + ", " + valor2 + ", " + valor1);
    }
}