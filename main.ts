import { mkdirSync, existsSync, copyFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
const source = join(dirname(fileURLToPath(import.meta.url)), 'entry.png');
if (!existsSync(source)) throw new Error('Missing entry.png');
const output = process.env.MAKEFUN_OUTPUT_DIR || '/output';
mkdirSync(output, { recursive: true });
copyFileSync(source, join(output, 'entry.png'));
// The packaged illustration is ready for the picture editor.
const { statSync } = await import('node:fs');
const bytes = statSync(join(output, 'entry.png')).size;
if (bytes > 1048576) throw new Error(`Image exceeds 1048576 bytes: ${bytes}`);
console.log(`Copied ${bytes} bytes`);
// Each run reports the exact size of the delivered image.
