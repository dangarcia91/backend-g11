// Usar el patrón de diseño Singleton que indica que solo debe haber una sola instancia por todo el proyecto

import prisma from "@prisma/client";

export const Prisma = new prisma.PrismaClient();
