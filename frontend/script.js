document.getElementById("btn-enviar").addEventListener("click", enviarMensaje);

async function enviarMensaje() {
  const input = document.getElementById("input");
  const chat = document.getElementById("chat");

  const pregunta = input.value.trim();
  if (!pregunta) return;

  // Mostrar mensaje del usuario
  chat.innerHTML += `<p class="user">Tú: ${pregunta}</p>`;

  try {
    const respuesta = await fetch("http://localhost:5050/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ mensaje: pregunta })
    });

    if (!respuesta.ok) {
      throw new Error("Error al comunicarse con el servidor.");
    }

    const datos = await respuesta.json();
    chat.innerHTML += `<p class="bot">LeanBot: ${datos.respuesta}</p>`;
    input.value = "";
  } catch (error) {
    chat.innerHTML += `<p class="error">Error: ${error.message}</p>`;
  }
}
