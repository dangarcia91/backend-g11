const data = {
  nombre: 'Daniel',
  correo: 'daes_g@hotmail.com',
  nomreb: [
    {
      nombre: "Ir al estadio",
      intensidad: "Normal",
    },
    {
      nombre: "Programar",
      intensidad: "Alta",
    },
  ],
};

// Destructuración > extraer parte de una clase, función, variable, etc
// Creo una variable 'nombre' con la información que tiene la propiedad nombre del JSON data

const { nombre} = data;

const correo = "juanito_el_mas_naky@hotmail.com";
// la forma más sencilla
const correo_usuario = data.correo;

// Usando destructuración
const { correo: nuevo_correo } = data;
// ...otro > extraigo la información d ela variable y lo guardo en una nueva variable con un nuevo espacio de memoria
const {hobbies, ...otro} = data;

console.log(nombre);
console.log(correo_usuario);
console.log(nuevo_correo);
console.log(otro);