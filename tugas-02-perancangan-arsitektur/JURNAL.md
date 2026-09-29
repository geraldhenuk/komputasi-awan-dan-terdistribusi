# Jurnal Proses — Tugas 2

## [Tanggal]
- Opsi arsitektur yang dipertimbangkan: ...
- Kenapa akhirnya pilih [SOA/Pub-Sub]: ...
- Revisi diagram (versi 1 → versi 2, apa yang berubah dan kenapa): ...

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 29 September 2026 | Gemini | Apa yang dimaksud dengan jenis komunikasi sinkron dan asinkron (request response) | Menjelaskan apa itu sinkron dan asinkron | Saya tinggal membedakan saja |

## Jawaban

3. Alur Skenario
Nomor 1 Checkout
- Aktor & Komponen: Aplikasi User -> API Gateway -> Order
- Jenis Komunikasi: Sinkron
- Eksekusi: User tekan tombol Checkout. Order memvalidasi stok/harga, menyimpan data ke databasenya sendiri dengan status PENDING_PAYMENT, lalu langsung memberikan respons + Order ID ke aplikasi user.
- Penanganan Masalah: Dipasang strict timeout (misal max 2 detik). Jika Order Service lambat, request diputus daripada menggantung.

Nomor 2 Pembayaran
- Aktor & Komponen: Aplikasi User -> API Gateway → Payment -> Payment Gateway (Bank/E-Wallet)
- Jenis Komunikasi: Sinkron
- Eksekusi: User mengonfirmasi pembayaran dari aplikasi. Payment meneruskan request ini ke API pihak ketiga (Bank/E-Wallet).
- Penanganan Masalah: Dipasang pola Circuit Breaker dan timeout. Jika API bank lemot, Payment langsung melempar respons error ke user tanpa membuat server habis karena menunggu koneksi gantung.