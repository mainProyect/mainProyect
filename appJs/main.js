var cuboMuestra = document.getElementById("cuboMuestra")
class Persona{
    constructor(nombre,email,telefono, dni, años,fechaDeNacimiento, domicilio, localidad){
        this.nombre=nombre
        this.email=email
        this.telefono=telefono
        this.dni=dni
        this.años=años
        this.fechaDeNacimiento=fechaDeNacimiento
        this.domicilio=domicilio
        this.localidad= localidad
    }
    datosPersona (){
        return `Nombre: ${this.nombre}<br>Email: ${this.email}<br>Telefono: ${this.telefono}<br>DNI: ${this.dni}<br>Edad: ${this.años}<br>Fecha de nacimiento: ${this.fechaDeNacimiento}<br>Domicilio: ${this.domicilio}<br>Localidad: ${this.localidad}`
    }
}
var miPersona= new Persona("Miguel Angel Salas", "miguelsalas1994@outlook.com", "1123909529", "38049111", "25 años", "13/09/1994","Achupallas 55", "Temperley")
function datosPersonales(){
    cuboMuestra.innerHTML="";
    inCubo=document.createElement("li")
    inCubo.innerHTML=miPersona.datosPersona()
    cuboMuestra.appendChild(inCubo)
}






























