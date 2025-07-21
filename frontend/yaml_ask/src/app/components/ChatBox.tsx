import { useState } from "react";

export default function ChatBox({ onResponse }: { onResponse: (res: any) => void }) {
  const [input, setInput] = useState("");

  const handleSend = async () => {
    const res = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: input }),
    });
    const data = await res.json();
    onResponse(data);
  };

  return (
    <div className="mt-4">
      <textarea
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Chat with your config..."
        className="bg-white shadow w-full p-2 border rounded"
        rows={3}
      />
      <button onClick={handleSend} className="mt-2 px-4 py-2 bg-purple-400 text-white rounded">
        Send
      </button>
    </div>
  );
}
