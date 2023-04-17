import express from "express";
//import prisma from "@prisma/client";
//import { categoriaRouter } from "./routes/categorias.routes.js";
import * as rutas from './routes/index.js';
import cors from 'cors';
// const Prisma = new prisma.PrismaClient()

const servidor = express();
servidor.use(express.json());
servidor.use(
  cors({
    origin: ['http://127.0.0.1:5555'],
    methods: ['GET', 'POST', 'PUT', 'PATCH', 'DELETE'],
    allowedHeaders: ["Content-Type", "Authorization"],
  })
);
const PORT = 3000;

//servidor.route("/categoria").post();
servidor.use(rutas.categoriaRouter);
servidor.use(rutas.productoRouter);

servidor.listen(PORT, () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`);
});