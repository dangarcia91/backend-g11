import { Router } from "express";
import { 
  crearProducto,
  devolverProducto,
  listarProductos, 
  actualizarProducto,
} from "../controllers/productos.controller.js";

export const productoRouter = Router();

//productoRouter.route('/productos').post(crearProducto)
productoRouter.post("/productos", crearProducto);

productoRouter.get("/productos", listarProductos);

productoRouter.get("/producto/:id", devolverProducto);

productoRouter.put("/producto/:id", actualizarProducto);