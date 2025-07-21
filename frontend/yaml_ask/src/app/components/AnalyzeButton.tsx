export default function AnalyzeButton({ onAnalyzed }: { onAnalyzed: (res: any) => void }) {
  const handleAnalyze = async () => {
    const res = await fetch("/api/analyze", { method: "POST" });
    const data = await res.json();
    onAnalyzed(data);
  };

  return (
    <button
      onClick={handleAnalyze}
      className="px-4 py-2 bg-purple-400 text-white rounded mt-4"
    >
      Analyze Config
    </button>
  );
}
