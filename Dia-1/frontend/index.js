const pedirAlumnos = async () => {
  const respuesta = await fetch("http://127.0.0.1:5000/alumnos", {
    method: 'GET'
  });

  const data = await respuesta.json();

  console.log(data);
};

pedirAlumnos();