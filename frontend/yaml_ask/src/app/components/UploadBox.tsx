import { useDropzone } from 'react-dropzone'

export default function UploadBox({ onUpload }: { onUpload: (file: File) => void }) {
  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    accept: {
      'text/yaml': ['.yaml', '.yml'],
      'text/plain': ['.tf']
    },
    onDrop: (acceptedFiles) => {
      if (acceptedFiles.length > 0) onUpload(acceptedFiles[0])
    }
  })

  return (
    <div
      {...getRootProps()}
      className="border-2 border-dashed border-gray-300 p-6 w-full text-center bg-white rounded-lg cursor-pointer hover:bg-gray-50"
    >
      <input {...getInputProps()} />
      {isDragActive ? (
        <p>Drop the file here ...</p>
      ) : (
        <p>Drag & drop a YAML or Terraform file here, or click to select</p>
      )}
    </div>
  )
}