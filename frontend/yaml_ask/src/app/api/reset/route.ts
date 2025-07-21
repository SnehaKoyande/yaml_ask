import { NextResponse } from "next/server";

export async function POST() {
  const res = await fetch("http://localhost:8000/rest", { method: "POST" });
  const data = await res.json();
  return NextResponse.json(data);
}
