import { EventoModel } from "../models/calendarios.model.js";
import { UsuarioModel } from "../models/usuarios.models.js";
import {subirImagenes} from "../utils/s3.js"

export const crearEvento = async (req, res) => {
  // TODO: ya no vamos a recibir el usuario por el body, ahora el suuario vendrá por el req.user
  const data = req.body;

  try{
    const nuevoEvento = await EventoModel.create(data);
    // TODO: reemplaza por req.user ( usando autenticación )
    // El findById ya no es necesario, porque lo estamos haciendo por el middleware
    // Deprecated
    const usuarioEncontrado = await UsuarioModel.findById(data.user);
    
    // actualizando los eventos que tiene este usuario
    await UsuarioModel.updateOne(
      // data.usuario > req.user._id
      { _id: data.usuario },
      {
        eventos: [...usuarioEncontrado.eventos, nuevoEvento._id],
      }
    );

    // Me quedé en el minuto 2:43_14
    
    return res.status(201).json({
      message: "Evento creado exitosamente",
      content: nuevoEvento,
    });
  } catch (error) {
    return res.status(400).json({
      message: "Error al crear el evento",
      content: error.message,
    });
  }
};

export const probarS3 = async (req, res) => {
  const resultado = await subirImagenes("");
  console.log(resultado);

  res.json({
    message: "Archivo subido exitosamente",
  });
};