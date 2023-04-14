function sumar(x, y){
  return x + y;
}

function restar(x, y){
  return x - y;
}

function operacion(funcion, parametro1, parametro2){
  // callback: ejecución de una función dentro de otra, también se llama wrap de funciones en JS
  const resultado = funcion(parametro1, parametro2);
  console.log(resultado);
}

operacion(sumar, 1, 5);
operacion(restar, 10, 5);

operacion(
  (x, y) => {
    return x * y;
  },
  5,
  6
);