import { NextRequest, NextResponse } from "next/server";
import fs from "fs";
import os from "os";
import path from "path";
import FormData from "form-data";

// Enable streaming body parsing
export const config = {
  api: {
    bodyParser: false,
  },
};

export async function POST(req: NextRequest) {
  const formData = await req.formData();
  const file = formData.get("file");

  if (!file || typeof file === "string") {
    return NextResponse.json({ error: "Invalid file" }, { status: 400 });
  }

  // Convert Web File to buffer
  const buffer = Buffer.from(await file.arrayBuffer());
  const tempFilePath = path.join(os.tmpdir(), file.name);
  fs.writeFileSync(tempFilePath, buffer);

  // Build multipart form using Node-compatible form-data
  const form = new FormData();
  form.append("file", fs.createReadStream(tempFilePath), {
    filename: file.name,
    contentType: file.type || "application/octet-stream",
  });

  // Send to FastAPI
  const res = await fetch("http://localhost:8000/parse/", {
    method: "POST",
    body: form,
    headers: form.getHeaders(),
  });

  const data = await res.json();
  return NextResponse.json(data);
}
