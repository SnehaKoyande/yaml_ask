'use client';

import { useState } from "react";
import FileUploader from "./components/FileUploader";
import IndexButton from "./components/IndexButton";
import QueryBox from "./components/QueryBox";
import ChatBox from "./components/ChatBox";
import AnalyzeButton from "./components/AnalyzeButton";

export default function Home() {
  const [parsed, setParsed] = useState(null);
  const [queryResult, setQueryResult] = useState(null);
  const [chatResponse, setChatResponse] = useState(null);
  const [analysis, setAnalysis] = useState(null);
  const [indexed, setIndexed] = useState(null);

  return (
    <main className="min-h-screen bg-gray-50 p-6 text-gray-800">
      <h1 className="text-3xl font-bold mb-6">yaml_ask Dashboard</h1>

      <div className="space-y-6">
        {/* Upload and parse */}
        <FileUploader onUpload={(data) => setParsed(data)} />
        {parsed && (
          <div className="bg-purple-200 p-4 rounded shadow text-sm overflow-auto">
            <h2 className="font-semibold">Parsed Output</h2>
            <pre>{JSON.stringify(parsed, null, 2)}</pre>
          </div>
        )}

        {/* Index button */}
        <IndexButton onIndexed={(res) => setIndexed(res)} />
        {indexed && (
          <div className="text-green-700 text-sm">
            ✅ Indexed: {JSON.stringify(indexed)}
          </div>
        )}

        {/* Query UI */}
        <QueryBox onResult={(res) => setQueryResult(res)} />
        {queryResult && (
          <div className="bg-white p-4 rounded shadow text-sm overflow-auto">
            <h2 className="font-semibold">Query Result</h2>
            <pre>{JSON.stringify(queryResult, null, 2)}</pre>
          </div>
        )}

        {/* Chat UI */}
        <ChatBox onResponse={(res) => setChatResponse(res)} />
        {chatResponse && (
          <div className="bg-white p-4 rounded shadow text-sm overflow-auto">
            <h2 className="font-semibold">Chat Response</h2>
            <pre>{JSON.stringify(chatResponse, null, 2)}</pre>
          </div>
        )}

        {/* Analyze */}
        <AnalyzeButton onAnalyzed={(res) => setAnalysis(res)} />
        {analysis && (
          <div className="bg-white p-4 rounded shadow text-sm overflow-auto">
            <h2 className="font-semibold">Config Analysis</h2>
            <pre>{JSON.stringify(analysis, null, 2)}</pre>
          </div>
        )}
      </div>
    </main>
  );
}
