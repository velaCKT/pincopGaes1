// Función para actualizar la cantidad de productos en el icono del carrito
 function updateCartIconCount() {
     const cartCount = Object.keys(cartItems).length;
     $('#cartItemCount').text(cartCount);
 }

 // Agregar el evento de clic a todos los botones "Añadir al carrito"
 $(document).ready(function () {
     $('.add-to-cart-btn a').click(addToCart);
 });

 // Variable para almacenar la cantidad de productos en el carrito
let cartItemCount = 0;

// Función para agregar un producto al carrito
function addToCart(productId) {
// Incrementar la cantidad de productos en el carrito
cartItemCount++;
// Actualizar la cantidad en el icono del carrito
$('#essenceCartBtn span').text(cartItemCount);
}

// Escuchar clics en los botones "Añadir al carrito"
$('.add-to-cart').on('click', function(e) {
e.preventDefault(); // Evitar que se recargue la página al hacer clic en el enlace

const productId = $(this).attr('data-id'); // Obtener el ID del producto
addToCart(productId); // Llamar a la función para agregar el producto al carrito
});



