var miTexto= "DNI / CUIL: 20-38049111-8 Fecha de nac. : 13/09/1994 Edad: 30 Años Domicilio: Achupallas 55 Localidad: Temperley (1834) Estado civil: Soltero Nacionalidad: Argentina";
var miTextoEducacion="Universitario: Cursando 1er año Institución: UNAB (Universidad nacional de Almirante Brown) Carrera: Tecnicatura en programación. Localidad: Almirante Brown"
let muestraDatos=document.getElementById("muestra")
function datosPersonales() {
  let splashDatos= document.createElement("li")
  splashDatos.textContent=miTexto
  muestraDatos.appendChild(splashDatos)
  return splashDatos
}

function educacion() {
    splashDatos.textContent=miTextoEducacion
  }