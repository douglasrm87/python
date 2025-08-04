
function limparResultado() {
    console.log("Executado em arquivo javascript independente.");
    console.log("Resultado limpo");
    //alert("Resultado limpo");

    // Esconde o resultado e a média
    const resultadoEl = document.getElementById("resultado-container");
    const mediaEl = document.getElementById("media-container");

    if (resultadoEl) resultadoEl.style.display = "none";
    if (mediaEl) mediaEl.style.display = "none";
}
