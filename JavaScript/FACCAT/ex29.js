import readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";
const rl = readline.createInterface({ input, output });

let valor1 = parseInt(rl.question("Digite o primeiro valor:"));
let valor2 = parseInt(rl.question("Digite o segundo valor:"));
let valor3 = parseInt(rl.question("Digite o terceiro valor:"));
let soma = 0;

if(valor2 > valor1 && valor3 > valor1){
    soma = valor2 + valor3;
}
else if(valor1 > valor2 && valor3 > valor2){
    soma = valor1 + valor3;
}
else{
    soma = valor1 + valor2;
}

console.log(("A soma dos maiores valores é: " + soma));