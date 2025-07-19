'use client'

import { useState } from 'react'
import FileUploader from './components/FileUploader'

export default function Home() {
  const [response, setResponse] = useState<any>(null);

  const handleUpload = async (file: File) => {
    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("http://localhost:8000/upload/", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();
    setResponse(data);
  };

  return (
    <div className="min-h-screen p-6 bg-violet-100">
      <h1 className="text-2xl font-bold mb-4 text-center text-violet-950">Yaml Ask</h1>
      <FileUploader onUpload={handleUpload} />
      {response && (
        <pre className="mt-6 p-4 bg-stone-800 rounded-md shadow">
          {JSON.stringify(response, null, 2)}
        </pre>
      )}
    </div>
  );
}
