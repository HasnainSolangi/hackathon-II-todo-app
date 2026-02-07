const fs = require("fs");
const path = require("path");
const { Client } = require("pg");

function parseEnv(filePath) {
  const text = fs.readFileSync(filePath, "utf8");
  const out = {};
  for (const line of text.split(/\r?\n/)) {
    const match = line.match(/^\s*([A-Z0-9_]+)\s*=\s*(.*)\s*$/);
    if (!match) continue;
    let value = match[2];
    if (value.startsWith("\"") && value.endsWith("\"")) {
      value = value.slice(1, -1);
    }
    out[match[1]] = value;
  }
  return out;
}

async function main() {
  const envPath = path.resolve(__dirname, "..", "..", "backend", ".env");
  if (!fs.existsSync(envPath)) {
    throw new Error(`backend .env not found at ${envPath}`);
  }
  const env = parseEnv(envPath);
  const url = env.DATABASE_URL;
  if (!url) {
    throw new Error("DATABASE_URL not found in backend/.env");
  }

  const client = new Client({ connectionString: url });
  await client.connect();
  const tableCheck = await client.query(
    "SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_name='jwks'"
  );
  if (tableCheck.rows.length === 0) {
    console.log("jwks table not found");
    await client.end();
    return;
  }
  const del = await client.query("DELETE FROM jwks");
  console.log("Deleted rows from jwks:", del.rowCount);
  await client.end();
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
