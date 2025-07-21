import { useState } from "react";

export default function QueryBox({ onResult }: { onResult: (res: any) => void }) {
  const [question, setQuestion] = useState("");

  const handleQuery = async () => {
    const res = await fetch("/api/query", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query: question }),
    });
    const data = await res.json();
    onResult(data);
  };

  return (
    <div className="mt-4">
      <input
        type="text"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask about the config..."
        className="shadow p-2 rounded w-full bg-white text-gray-700"
      />
      <button onClick={handleQuery} className="mt-2 px-4 py-2 bg-purple-400 text-white rounded">
        Query
      </button>
    </div>
  );
}
