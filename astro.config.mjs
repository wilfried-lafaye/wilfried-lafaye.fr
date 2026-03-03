// @ts-check
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
    site: 'https://wilfried-lafaye.fr',
    outDir: './docs',
    build: {
        format: 'file'
    }
});
