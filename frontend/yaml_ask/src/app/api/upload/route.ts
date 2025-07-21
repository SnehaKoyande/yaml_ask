import { NextRequest, NextResponse } from "next/server";
import fs from "fs";
import os from "os";
import path from "path";
import FormData from "form-data";
import { request } from "undici";

export async function POST(req: NextRequest) {
  const formData = await req.formData();
  const file = formData.get("file") as File;

  if (!file) {
    return NextResponse.json({ error: "No file provided" }, { status: 400 });
  }

  // ✅ Convert browser File to Buffer
  const buffer = Buffer.from(await file.arrayBuffer());

  // ✅ Save to temp path
  const tempPath = path.join(os.tmpdir(), file.name);
  fs.writeFileSync(tempPath, buffer);

  // ✅ Use FormData lib to send multipart/form-data
  const forwardForm = new FormData();
  forwardForm.append("file", fs.createReadStream(tempPath), {
    filename: file.name,
    contentType: file.type || "application/octet-stream"
  });

  // ✅ Send to FastAPI endpoint (e.g., /parse)
  const { statusCode, body } = await request("http://localhost:8000/parse/", {
    method: "POST",
    body: forwardForm,
    headers: forwardForm.getHeaders(),
  });

  const parsed = await streamToJson(body);
  return NextResponse.json(parsed);
}

// Helper
async function streamToJson(stream: NodeJS.ReadableStream): Promise<any> {
  const chunks: Buffer[] = [];
  for await (const chunk of stream) {
    chunks.push(Buffer.from(chunk));
  }
  const buffer = Buffer.concat(chunks);
  return JSON.parse(buffer.toString("utf-8"));
}
