document.addEventListener('DOMContentLoaded', () => {
    const textoEntrada = document.getElementById('textoEntrada');
    const botonAnalizar = document.getElementById('botonAnalizar');
    const resultadoTokenizacion = document.getElementById('resultadoTokenizacion');
    const resultadoLematizacion = document.getElementById('resultadoLematizacion');
    const resultadosDiv = document.getElementById('resultados');
    const mensajeError = document.getElementById('mensajeError');

    botonAnalizar.addEventListener('click', async () => {
        const texto = textoEntrada.value;

        if (!texto.trim()) {
            mensajeError.textContent = 'Por favor, ingresa un texto para analizar.';
            mensajeError.style.display = 'block';
            resultadosDiv.style.display = 'none';
            return;
        }

        mensajeError.style.display = 'none';

        try {
            const response = await fetch('/procesar_texto', { // Cambiar a una ruta relativa
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ texto: texto })
            });

            if (!response.ok) {
                const errorData = await response.json();
                mensajeError.textContent = `Error del servidor: ${errorData.error || 'Error desconocido'}`;
                mensajeError.style.display = 'block';
                resultadosDiv.style.display = 'none';
                return;
            }

            const data = await response.json();
            resultadoTokenizacion.textContent = data.tokens.join('| ');
            resultadoLematizacion.textContent = data.lemas.join('| ');
            resultadosDiv.style.display = 'block';

        } catch (error) {
            mensajeError.textContent = 'Error de conexión con el servidor.';
            mensajeError.style.display = 'block';
            resultadosDiv.style.display = 'none';
            console.error('Error:', error);
        }
    });
});