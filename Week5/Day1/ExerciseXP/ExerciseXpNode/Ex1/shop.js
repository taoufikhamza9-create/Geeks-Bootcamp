const products = require('./products.js');
function searchProducts(productName) {
   for (let product of products) {
    if (product.name === productName) {
      return product;
    }
  }
  return null;
}

console.log(searchProducts("Product 2")); // Returns the product object for Product 2
console.log(searchProducts("Product 4")); // Returns null since Product 4 does not exist
console.log(searchProducts("Product 1")); // Returns the product object for Product 1