import express from "express";
//import prisma from "@prisma/client";
//import { categoriaRouter } from "./routes/categorias.routes.js";
import * as rutas from './routes/index.js';

// const Prisma = new prisma.PrismaClient()

const servidor = express();
servidor.use(express.json());

const PORT = 3000;

//servidor.route("/categoria").post();
servidor.use(rutas.categoriaRouter);
servidor.use(rutas.productoRouter);

servidor.listen(PORT, () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`);
});