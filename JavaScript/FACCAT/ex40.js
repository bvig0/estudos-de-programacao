import readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";
const rl = readline.createInterface({ input, output });

//prod -> Produto
let prodNome = rl.question("Digite o nome do produto: ");
let prodQuantidade = parseInt(rl.question("Digite a quantidade do produto: "));
let prodPreco = parseInt(rl.question("Digite o preço unitário do produto: "));
let desconto, total = 0;

if (prodQuantidade <= 5) desconto = 2 / 100;

else {
    if (prodQuantidade > 5 && prodQuantidade <= 10) {
        desconto = 3 / 100;
    }
    else {
        desconto = 5 / 100;
    }
}

total = prodQuantidade * prodPreco;
total = total - (total * desconto);
console.log("O total da compra sobre o " + prodNome + " foi de R$" + total);