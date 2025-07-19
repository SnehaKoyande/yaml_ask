import { useState } from "react";

export default function FileUploader({ onUpload }: { onUpload: (parsed: any) => void }) {
  const [file, setFile] = useState<File | null>(null);
  const [uploading, setUploading] = useState(false);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files) setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) return;
    setUploading(true);

    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("/api/upload", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();
    onUpload(data);
    setUploading(false);
  };

  return (
    <div className=" p-4 rounded-xl bg-white shadow text-gray-700">
      <input type="file" onChange={handleFileChange} accept=".yaml,.yml,.tf,.json" />
      <button
        onClick={handleUpload}
        disabled={uploading}
        className="px-4 py-2 bg-purple-400 text-white rounded-md"
      >
        {uploading ? "Uploading..." : "Upload & Parse"}
      </button>
    </div>
  );
}
