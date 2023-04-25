import { JsonWebTokenError } from "jsonwebtoken";

export const validarToken = (req, res, next) => {
  // TODO. validar que hay el header de autorizathion
  // Validar que la token sea correcta
  // agregar al req.user la información del usuario de la token
};
