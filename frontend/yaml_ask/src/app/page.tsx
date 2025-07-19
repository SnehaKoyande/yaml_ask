'use client'

import { useState } from 'react'
import FileUploader from './components/FileUploader'

export default function Home() {
  const [parsed, setParsed] = useState<any>(null);

  return (
    <div className="min-h-screen min-w-screen bg-gray-100">
      <div className="max-w-2xl mx-auto py-10 space-y-6 bg-gray">
        <h1 className="text-2xl font-bold text-purple-900 text-center">InfraBuddy: Upload Infra File</h1>
        <FileUploader onUpload={setParsed} />
        {parsed && (
          <pre className="bg-gray-100 p-4 rounded-md text-sm overflow-x-auto">
            {JSON.stringify(parsed, null, 2)}
          </pre>
        )}
      </div>
    </div>
  );
}
