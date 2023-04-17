//una promesa es un objeto que representa la culminación de éxito o error de  una operación asíncrona
async function ejecucion(){
  console.log("Sumar");
  console.log("REstar");

  const promesa = new Promise((resolve, reject) => {
    setTimeout(() => {
    //  resolve("Información guardada en la base de datos");
      reject(new Error("Error al guardar el registro en la base de datos"));
    }, 5000);
  });

  //then > sirve para indicar si la promesa se ejecutó exitosamente, o sea terminó sin problemas
  // catch > Sirve para indica si falló la ejecución de la promesa
  //promesa
    //.then((respuesta) =>{
      //console.log(respuesta);
   // })
    //.catch((error)=>{
      //console.log(error);
    //});
  try{
    const respuesta = await promesa;
    console.log(respuesta);
  } catch (error){
    console.error("Error al ejecutar la promesa");
    console.error(error.message);
  }
  console.log("FINALIZADO!");
}

ejecucion();