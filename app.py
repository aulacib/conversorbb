""import React, { useState } from "react";
import { useDropzone } from "react-dropzone";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { CloudUpload, FileText, CheckCircle, Download } from "lucide-react";

export default function Conversor() {
  const [file, setFile] = useState(null);
  const [converted, setConverted] = useState(false);

  const { getRootProps, getInputProps } = useDropzone({
    accept: { "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": [".xlsx"] },
    onDrop: (acceptedFiles) => {
      setFile(acceptedFiles[0]);
      setConverted(true);
    },
  });

  return (
    <div className="p-6 max-w-2xl mx-auto space-y-2">
      <h1 className="text-2xl font-bold">Conversor de preguntas Blackboard Ultra</h1>
      
      <p className="text-sm">Desarrollado por: Maycoll Gamarra Chura</p>
      <p className="text-sm mb-4">Última actualización: 15/03/25</p>

      <Card className="p-4 border-dashed border-2 border-gray-300" {...getRootProps()}>
        <input {...getInputProps()} />
        <div className="flex items-center space-x-2">
          <CloudUpload className="text-gray-500" />
          <p className="text-gray-500">📂 Arrastra o selecciona un archivo Excel</p>
        </div>
        <p className="text-xs text-gray-400">Límite 200MB por archivo • XLSX</p>
      </Card>

      {file && (
        <div className="mt-2 p-2 border border-green-600 bg-green-100 rounded">
          <div className="flex items-center space-x-2">
            <span className="text-green-700 font-bold">📂 Archivo cargado: {file.name}</span>
          </div>
          <p className="text-green-700 flex items-center space-x-1">
            <CheckCircle className="text-green-700" size={16} />
            <span>Archivo cargado correctamente.</span>
          </p>
        </div>
      )}

      {converted && (
        <Button className="mt-2 flex items-center space-x-2 bg-blue-600 text-white px-4 py-2 rounded">
          <Download size={16} />
          <span>Descargar archivo TXT</span>
        </Button>
      )}
    </div>
  );
}""
