import { Router } from "express";
import { 
  crearCategoria, 
  devolverCategoria, 
  listarCategoria,
  actualizarCategoria, 
  eliminarCategoria,
} from "../controllers/categorias.controllers.js";

export const categoriaRouter = Router();

categoriaRouter.route("/categorias").post(crearCategoria).get(listarCategoria);

categoriaRouter
.route("/categoria/:id")
.get(devolverCategoria)
.patch(actualizarCategoria)
.put(actualizarCategoria)
.delete(eliminarCategoria);