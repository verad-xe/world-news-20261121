// Entry for make.fun "news-image-20261121": sum up the world news of
// Saturday 21 November 2026 in a single image.
//
// The picture itself (entry.png, drawn by make_image.py from the day's
// reported headlines) sits beside this program; the program's whole job
// is to place those exact bytes at /output/entry.png.  It runs offline,
// with the Node 22 standard library only, and writes the same bytes on
// every run.
//
// Locally:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, statSync } from "node:fs";
import { join } from "node:path";

const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const source = new URL("./entry.png", import.meta.url);
const target = join(outputDir, "entry.png");

// The bounty caps the image at 1 MiB; fail loudly rather than hand in
// an entry the gate would refuse.
const bytes = statSync(source).size;
if (bytes > 1_048_576) {
  throw new Error(`entry.png is ${bytes} bytes, over the 1 MiB cap`);
}

copyFileSync(source, target);
console.log(`news image for 2026-11-21 written to ${target} (${bytes} bytes)`);
