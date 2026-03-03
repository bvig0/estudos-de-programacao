import readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";
const rl = readline.createInterface({ input, output });

let homemUm = parseInt(rl.question("Digite a idade do primeiro homem: "));
let homemDois = parseInt(rl.question("Digite a idade do segundo homem: "));
let mulherUm = parseInt(rl.question("Digite a idade da primeira mulher: "));
let mulherDois = parseInt(rl.question("Digite a idade da segunda mulher: "));
let homemMaisVelho, homemMaisNovo, mulherMaisVelha, mulherMaisNova = 0;

// Verificar qual homem é mais velho e mais novo
if (homemUm > homemDois) {
    homemMaisVelho = homemUm;
    homemMaisNovo = homemDois;
}
else {
    homemMaisVelho = homemDois;
    homemMaisNovo = homemUm;
}

// Verificar qual mulher é mais velha e mais nova
if (mulherUm > mulherDois) {
    mulherMaisVelha = mulherUm;
    mulherMaisNova = mulherDois;
}
else {
    mulherMaisVelha = mulherDois;
    mulherMaisNova = mulherUm;
}

let soma = homemMaisVelho + mulherMaisNova;
let produto = homemMaisNovo * mulherMaisVelha;

console.log("A soma do homem mais velho com a mulher mais nova: " + soma);
console.log("O produto do homem mais novo com a mulher mais velha: " + produto);