'use client'

import { useState } from 'react'
import Head from 'next/head'
import UploadBox from './components/FileUploader'

export default function Home() {
  const [fileName, setFileName] = useState("")

  const handleUpload = (file: File) => {
    setFileName(file.name)
    console.log("Uploaded file:", file)
  }

  return (
    <>
      <Head>
        <title>yaml_ask | AI YAML Debugger</title>
      </Head>
      <main className="flex flex-col items-center justify-center min-h-screen p-6 bg-gray-100">
        <h1 className="text-3xl font-bold mb-4 text-gray-800">yaml_ask</h1>
        <p className="text-gray-600 mb-6">Upload a YAML or Terraform file to get help.</p>
        <UploadBox onUpload={handleUpload} />
        {fileName && (
          <p className="mt-4 text-sm text-green-600">Uploaded: {fileName}</p>
        )}
      </main>
    </>
  )
}
