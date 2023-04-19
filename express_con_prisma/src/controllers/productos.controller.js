import { Prisma } from "../prisma.js";

export const crearProducto = async (req, res) => {
  const data = req.body;
  // SELECT if FROm categoria WHERE id = ...;

  //TODO: validar si la categoria en la cual se quiere crear el producto no este deshabilitado
  const categoria = await Prisma.categoria.findFirst({
    where: {id: data.categoriaId},
    select: { id: true},
  });

  if (!categoria) {
    return res.status(400).json({
      message: "Categoria no existe",
    });
  }
  try {
    const nuevoProducto = await Prisma.producto.create({ 
      data:{
      ...data,
      fechaVencimiento: new Date(data.fechaVencimiento),
      },
    });

    return res.status(201).json({
      message: "producto creado exitosamente",
      content: nuevoProducto,
    });
  } catch(error){
    return res.status(400).json({
      message: "Error al crear el producto",
      content: error.message,
    });
  }
};

export const listarProductos = async (req, res) => {
  //TODO
  const producto = await Prisma.producto.findMany()
  res.status(200).json({
    content: producto,
  });
};

export const devolverProducto = async (req, res) => {
  const { id } = req.params;

  const productoEncontrado = await Prisma.producto.findFirst({
    where: { id: +id },
    include: { categoria: true},

  });

  if (!productoEncontrado) {
    return res.status(400).json({
      message: "El producto no existe",
    });
  }

  return res.json({
    content: productoEncontrado,
  });
};

export const actualizarProducto = async (req, res) => {
  //TODO
  const data = req.body;
  const { id } = req.params;

  const producto = await Prisma.producto.findFirst({
    where: { id: +id },
    select: { id: true},
  });

  if (!producto) {
    return res.status(400).json({
      message: "El producto no existe",
    });
  }

  const productoActualizado = await Prisma.producto.update({
    where: { id: producto.id},
    data: data,
  })

  return res.json({
    message: "Producto actualizado correctamente",
    content: productoActualizado,
  });
};