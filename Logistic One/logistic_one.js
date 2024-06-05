// Función para desplegar/ocultar información de un servicio específico
function toggleInfo(serviceNumber) {
    var infoContent = document.getElementById("info_" + serviceNumber);
    infoContent.classList.toggle("active");
}


  // Función que muestra la alerta
  function mostrarAlerta() {
    alert("¡Hola! Has presionado el botón.");
}

