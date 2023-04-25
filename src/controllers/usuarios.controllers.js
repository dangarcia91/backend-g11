import { UsuarioModel } from "../models/usuarios.models.js";

export const registroUsuario = async (req, res) => {
  const data = req.body;

  try {
    const nuevoUsuario = await UsuarioModel.create(data)

    return res.status(201).json({
      message: "Usuario creado exitosamente",
    });
  } catch (error) {
    return res.status(400).json({
      message: "Error al crear el usuario",
      content: error.message,
    });
  }
};