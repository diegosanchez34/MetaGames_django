// Obtener elementos del DOM
const enlaceCarrito = document.querySelector('.fas.fa-shopping-cart');
const carrito = document.querySelector('.carrito');
const listaCarrito = document.querySelector('.lista-carrito');
const totalCarrito = document.querySelector('.total');
const botonVaciarCarrito = document.querySelector('.vaciar-carrito');
const botonComprar = document.querySelector('.comprar');
const modal = document.querySelector('.modal');
const botonCancelarCompra = document.querySelector('.cancelar-compra');
const botonConfirmarCompra = document.querySelector('.confirmar-compra');

// Carrito de compras
let carritoItems = [];

// Función para mostrar u ocultar el carrito
function toggleCarrito() {
  carrito.classList.toggle('visible');
}

// Función para actualizar la vista del carrito
function actualizarCarrito() {
  listaCarrito.innerHTML = '';
  totalCarrito.textContent = `Total: $${calcularTotal()}`;

  carritoItems.forEach(item => {
    const { nombre, precio, cantidad } = item;

    const li = document.createElement('li');
    li.innerHTML = `
      <span class="carrito-1">${nombre}|</span>
      <span class="carrito-text">
        Precio: $${precio} x ${cantidad}
        <button class="restar-item" data-nombre="${nombre}">-</button>
        <button class="sumar-item" data-nombre="${nombre}">+</button>
        <button class="eliminar-item" data-nombre="${nombre}">Eliminar</button>
      </span>
    `;
    listaCarrito.appendChild(li);

    // Agregar eventos a los botones de eliminar, sumar y restar
    const botonEliminar = li.querySelector('.eliminar-item');
    botonEliminar.addEventListener('click', eliminarProducto);

    const botonRestar = li.querySelector('.restar-item');
    botonRestar.addEventListener('click', restarCantidad);

    const botonSumar = li.querySelector('.sumar-item');
    botonSumar.addEventListener('click', sumarCantidad);
  });
}

// Función para agregar un producto al carrito
function agregarProducto(e) {
  const nombre = e.target.dataset.nombre;
  const precio = Number(e.target.dataset.precio);

  const productoEnCarrito = carritoItems.find(item => item.nombre === nombre);

  if (productoEnCarrito) {
    productoEnCarrito.cantidad++;
  } else {
    carritoItems.push({ nombre, precio, cantidad: 1 });
  }

  actualizarCarrito();
}

// Función para eliminar un producto del carrito
function eliminarProducto(e) {
  const nombre = e.target.dataset.nombre;

  carritoItems = carritoItems.filter(item => item.nombre !== nombre);

  actualizarCarrito();
}

// Función para restar la cantidad de un producto en el carrito
function restarCantidad(e) {
  const nombre = e.target.dataset.nombre;

  const productoEnCarrito = carritoItems.find(item => item.nombre === nombre);

  if (productoEnCarrito && productoEnCarrito.cantidad > 1) {
    productoEnCarrito.cantidad--;
  } else {
    carritoItems = carritoItems.filter(item => item.nombre !== nombre);
  }

  actualizarCarrito();
}

// Función para sumar la cantidad de un producto en el carrito
function sumarCantidad(e) {
  const nombre = e.target.dataset.nombre;

  const productoEnCarrito = carritoItems.find(item => item.nombre === nombre);

  if (productoEnCarrito) {
    productoEnCarrito.cantidad++;
  }

  actualizarCarrito();
}

// Función para vaciar el carrito
function vaciarCarrito() {
  carritoItems = [];

  actualizarCarrito();
}

// Función para calcular el total del carrito
function calcularTotal() {
  return carritoItems.reduce((total, item) => total + (item.precio * item.cantidad), 0);
}

// Función para mostrar la ventana emergente de compra
function mostrarModalCompra() {
  modal.style.display = 'flex';
}

// Función para ocultar la ventana emergente de compra
function ocultarModalCompra() {
  modal.style.display = 'none';
}

// Función para confirmar la compra
function confirmarCompra() {
  vaciarCarrito();
  ocultarModalCompra();
  alert('¡Gracias por tu compra!');
}

// Eventos
enlaceCarrito.addEventListener('click', toggleCarrito);
botonVaciarCarrito.addEventListener('click', vaciarCarrito);
botonComprar.addEventListener('click', mostrarModalCompra);
botonCancelarCompra.addEventListener('click', ocultarModalCompra);
botonConfirmarCompra.addEventListener('click', confirmarCompra);

document.addEventListener('DOMContentLoaded', () => {
  const botonesAgregarCarrito = document.querySelectorAll('.agregar-carrito');

  botonesAgregarCarrito.forEach(boton => {
    boton.addEventListener('click', agregarProducto);
  });
});
