$(document).ready(function() {
    // Variable para almacenar el subtotal y el total
    let subtotal = 0;
    let total = 0;

    // Contador de productos en el carrito
    let productCount = 0;

    // Función para actualizar el subtotal y el total
    function updateSubtotalAndTotal() {
        subtotal = 0;
        total = 0;
        $('#cartItemsList .cart-item').each(function() {
            var itemPrice = parseFloat($(this).find('.product-price').text().replace('$', ''));
            subtotal += itemPrice;
        });
        total = subtotal * 0.8; // Aplicar el descuento del 20%
        $('#subtotalValue').text('$' + subtotal.toFixed(3));
        $('#totalValue').text('$' + total.toFixed(3));
    }

    // Manejar clic en el botón "Añadir al Carrito"
    $('.add-to-cart-btn').click(function(e) {
        e.preventDefault(); // Evitar que se recargue la página al hacer clic en el botón

        // Obtener los datos del producto
        var productName = $(this).parents('.product-description').find('h2,h6').text();
        var productPrice = parseFloat($(this).parents('.product-description').find('.product-price').text().replace('$', '').replace(',', '')); // Convertir precio a número
        var productImage = $(this).parents('.product-description').prev('.product-img').find('img').attr('src');

        // Verificar si el producto ya está en el carrito
        var alreadyInCart = false;
        $('#cartItemsList .cart-item').each(function() {
            var cartItemName = $(this).find('.product-name').text();
            if (cartItemName === productName) {
                alreadyInCart = true;
                return false; // Salir del bucle each si se encuentra el producto
            }
        });

        // Si el producto no está en el carrito, agregarlo
        if (!alreadyInCart) {
            // Crear un nuevo elemento de lista con el nombre, precio, imagen y botón de eliminar del producto
            var newItem = $('<div>').addClass('cart-item').append(
                $('<h5>').addClass('product-name').text(productName),
                $('<img>').attr('src', productImage).addClass('product-image'),
                $('<p>').addClass('product-price').text('$' + productPrice.toFixed(3)),
                $('<button>').addClass('remove-from-cart-btn').text('Eliminar').attr('aria-label', 'Eliminar Producto')
            );

            // Agregar el nuevo elemento al carrito
            $('#cartItemsList').append(newItem);

            // Incrementar el contador de productos
            productCount++;
            $('#productCount').text(productCount);

            // Actualizar el subtotal y el total
            updateSubtotalAndTotal();

            // Actualizar el contador en el icono del carrito
            const cartCounter = $('#rightSideCart').find('span');
            const currentCount = parseInt(cartCounter.text());
            cartCounter.text(currentCount + 1);
        }
    });

    // Manejar clic en el botón "Eliminar" del carrito
    $('#cartItemsList').on('click', '.remove-from-cart-btn', function() {
        var productPrice = parseFloat($(this).parent().find('.product-price').text().replace('$', '')); // Obtener precio del producto a eliminar

        $(this).parent().remove(); // Eliminar el elemento del carrito

        // Decrementar el contador de productos en el carrito
        productCount--;
        $('#productCount').text(productCount);

        // Actualizar el subtotal y el total
        updateSubtotalAndTotal();
    });
});

