function sumar(x,y) {
  return x + y;
}

export const restar = (x,y) => {
  return x - y;
};

export const secreto = "ABC123";

module.exports = {
  sumar: sumar,
  restar,
  secreto,
}