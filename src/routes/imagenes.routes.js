import {Router} from 'express';
import multer from "multer";
import * as controller from "../controllers/imagenes.controllers.js"

export const imagenRouter = Router();

//Distore > permanente; memoryStorage> temporal
const almacenamiento = multer.diskStorage({
  destination: (req, file, cb)=>{
    //donde quiero que se almacene, llamando al callback
    cb(null, "imagenes/");
  },

  filename: (req,file,cb)=>{
    //modifico nombre del archivo para que se guarde con su nombre original
    const nombre = `${Date.now()}_${file.originalname}`;
    cb(null, nombre)
  },
});

const upload = multer({
  storage: almacenamiento,
}); 

// any > acepta cualquier archivo y los almacena en req.files
// none > Acepta solamente texto osea no archivos
// fields(fields) > Podemos recibir varios archivos en diferentes llaves del form-data y se especificaran en el arreglo lo almacenara en req.files
// upload.fields([
//     { name: "imagen1", maxCount: 1 },
//     { name: "imagenes-adicionales", maxCount: 5 },
//   ])

// array > acepta un arreglo de archivos lo almacenara en req.files
// upload.array('total-imagenes',10),

// single > solamente permite subir una sola imagen y lo almacenara en req.file

imagenRouter.post(
  "/subir-imagen", 
  upload.single("imagen"),
  controller.subirImagen
  );

  imagenRouter.get('/devolver-imagen/:nombre', controller.devolverImagen);

  imagenRouter.delete('/eliminar-imagen/:nombre', controller.eliminarImagen );