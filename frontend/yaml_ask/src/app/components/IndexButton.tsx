export default function IndexButton({ onIndexed }: { onIndexed: (res: any) => void }) {
  const handleIndex = async () => {
    const res = await fetch("/api/index", { method: "POST" });
    const data = await res.json();
    onIndexed(data);
  };

  return (
    <button
      onClick={handleIndex}
      className="px-4 py-2 bg-purple-400 text-white rounded-md"
    >
      Index Config
    </button>
  );
}
