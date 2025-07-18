import { useState } from 'react';

export default function FileUploader({ onUpload }: { onUpload: (file: File) => void }) {
  const [fileName, setFileName] = useState<string | null>(null);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;
    setFileName(file.name);
    onUpload(file);
  };

  return (
    <div className="p-4 border border-dashed border-gray-400 rounded-md w-full max-w-md mx-auto">
      <input type="file" accept=".yaml,.yml,.tf,.json,.dockerfile" onChange={handleChange} />
      {fileName && <p className="mt-2 text-sm text-green-700">Uploaded: {fileName}</p>}
    </div>
  );
}
