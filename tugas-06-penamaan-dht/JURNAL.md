# Jurnal Proses — Tugas 6

## Implementasi find_successor (Fito)
- Kesalahan pertama yang ditemui (mis. lupa wrap-around di ring): Pas nilai hash ID kurir lebih gede dari semua ID node yang lagi aktif di ring (contoh: hash 200, padahal ID node terbesar cuma 177), fungsinya bingung dan malah ngeluarin nilai None atau error
- Cara memperbaikinya: Nambahin logika wrap-around (muter balik ke awal). Kalau gak ketemu node yang ID-nya lebih gede atau sama dengan hash kurir, sistem otomatis muter dan milih node yang ID-nya paling kecil di ring.
## Skenario join/leave
- Hasil sebelum & sesudah node baru bergabung: 
Sebelum: kurir-001 (hash=50) dipegang Node 102, terus kurir-002 (hash=28) dipegang Node 40. 

Sesudah: Pas node-medan-1 (id=123) baru masuk, data hash 50 sama 28 otomatis dipindahin ke node-medan-1 karena ID 123 jadi penanggung jawab terdekat yang paling pas. 
- Hasil sebelum & sesudah node keluar: 
Sebelum: node-jakarta-1 (id=177) masih aktif di ring dan nyimpen data mapping.

Sesudah: - Pas node-jakarta-1 (id=177) keluar, semua datanya langsung dioper ke Node 40 sebagai penerus di ring. Pas nyari IP kurir-001 sama kurir-002 lagi, nilainya tetep dapet dan gak ada data yang hilang.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 26 Oktober 2026 | ChatGPT | Membantu memahami struktur kode Chord DHT dan logika successor | Memberikan pandua kerangka logika 'find_successor' dengan *wrap-around* dan aturan *consistent hashing* | Menggunakan konsep tersebut untuk menyusun implementasi 'join', 'leave' dan 'find_successor' pada code python tugas |
| ... | ... | ... | ... | ... |