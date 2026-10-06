# Jurnal Proses — Tugas 3

## Percobaan tanpa Lock
- Hasil `processed_count` yang didapat: 46 dari target 100.
- Kenapa bisa meleset (jelaskan mekanisme race condition dengan kata sendiri): Ada beberapa thread yang mengakses dan mengubah variabel 'processed_count' secara bersamaan. Proses membaca nilai lama, ditambah 1, setelah itu disimpan kembali dapat saling bertabrakan. Berakibat beberapa increment hilang sehingga hasil hanya 46, bukan 100.

## Percobaan dengan Lock
- Hasil `processed_count` setelah perbaikan: 100 dari target 100.
Disini 'threading.Lock()' membuat bagian increment 'processed_count' hanya dapat dijalankan oleh satu thread saja pada satu waktu. Dengan itu increment tidak saling bertabrakan dan seluruh 100 pesanan berhasil dihitung.

## Kendala Docker
- Error yang ditemui saat `docker build`/`docker run` dan cara memperbaikinya: Tidak ada kendala yang berarti. Proses docker dibantu oleh anggota kelompok yang lebih memahami penggunaan Docker, sehingga proses build dan run container dapat berjalan dengan baik.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 6 Oktober 2026 | ChatGpt | Mengapa Docker Desktop stuck pada halaman "Starting the Docker Engine" | AI menyarankan mengunduh ubuntu, tetapi prosesnya belum selesai. | - |
