// function addTax(price, percent)
// {
//     var taxAmount = price * percent;
//     return price + taxAmount;
// }

// var totalPrice = addTax(20, 3);


function requiredBinSize(items, bins)
{
    const floatBinSize = items / bins;
    return Math.ceil(floatBinSize);
}

console.log(requiredBinSize(10, 0));
console.log(requiredBinSize("5", 3));