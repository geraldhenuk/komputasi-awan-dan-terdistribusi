# Jurnal Proses — Tugas 7

## Diskusi pemilihan model konsistensi
- Argumen yang dipertimbangkan: Kalau pakai Eventual Consistency biasa, jeda waktu replikasi (replication lag) bikin saldo e-wallet pas di-top-up bisa kebaca 0 di server wilayah lain. Dampaknya fatal: transaksi pesan makanan user ditolak padahal saldo cukup, bikin kapok dan pindah aplikasi.
- Kesimpulan akhir & alasan: Memilih Client-Centric Consistency (Read-Your-Writes). Alasannya, user yang baru aja melakukan write (top-up) wajib langsung melihat saldo terbarunya sendiri secara akurat tanpa harus nunggu server lain selesai sinkronisasi total.

## Simulasi (jika dikerjakan)
- Hasil skenario naif vs Read-Your-Writes: 

  Naif: Server Bandung langsung baca data sebelum replikasi selesai, alhasil saldo kebaca 0.0 (gagal/bug).

  Read-Your-Writes: Dengan melacak versi data klien, server Bandung otomatis dipaksa sinkron instan sebelum ngasih data, jadi saldo langsung tampil akurat (90000.0) walau dicek sebelum jeda replikasi habis.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 17 Nov 2026 | ChatGPT | "Bagaimana cara kerja dasar konsistensi Read-Your-Writes pada sistem terdistribusi?" | Dijelaskan konsep pelacakan versi klien (*client's last write version*). | Digunakan sebagai referensi konseptual untuk menyusun argumen bisnis di README.md dan melengkapi logika versioning di skrip simulasi. |
| ... | ... | ... | ... | ... |
