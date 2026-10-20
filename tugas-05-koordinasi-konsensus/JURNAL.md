# Jurnal Proses — Tugas 5

## Implementasi Bully ( Gerald )
- Kendala saat mengisi TODO 1-4: 

1. Urutan penyalaan node di awal (Startup Timing): Karena ke-5 terminal dinyalakan secara berurutan (bukan tepat pada milidetik yang sama), node dengan ID lebih rendah yang menyala lebih dulu tidak mendapat balasan OK dari node ber-ID lebih tinggi yang belum aktif, sehingga sempat mendeklarasikan diri sebagai LEADER! sementara sebelum akhirnya ditimpa oleh pesan COORDINATOR dari node yang lebih tinggi.

2. Penanganan Multiple Election secara bersamaan (Cascading Election): Saat Leader (Node 5) mati, semua node yang tersisa (Node 1, 2, 3, dan 4) mendeteksi matinya leader hampir bersamaan dan saling mengirim pesan ELECTION. Setiap kali node ber-ID lebih tinggi menerima pesan ELECTION dari node di bawahnya, node tersebut membalas OK dan memicu proses election ulang, sehingga menghasilkan pengiriman pesan COORDINATOR berulang kali dari Node 4

## Skenario 1: Start normal ( Gerald )
- Leader yang terpilih: Node 5 
- Log/observasi: Saat dijalankan mulai dari Node 1 (port 5001) hingga Node 4 (port 5004), masing-masing node memulai election ke peer yang lebih tinggi (misalnya Node 1 ke [2, 3, 4, 5], Node 2 ke [3, 4, 5], Node 3 ke [4, 5], dan Node 4 ke [5]).   

## Skenario 2: Leader dimatikan ( Fito )
- Leader baru yang terpilih: Node 4
- Berapa lama waktu sampai leader baru terdeteksi: Sebentar saja, langsung ketahuan setelah batas waktu tunggu (timeout) habis. Node 1, 2, 3, dan 4 sadar hampir bebarengan kalau Node 5 sudah tidak merespons, lalu mereka langsung mulai pemilihan baru.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
|20/10/2026|Gemini|Apa saja poin-poin kendala teknis yang umum terjadi saat menjalankan simulasi Bully Algorithm menggunakan beberapa proses socket TCP lokal?|menyebutkan beberapa poin konsep seperti perbedaan waktu nyala terminal (startup timing), pemilihan ulang beruntun (cascading election), dan penentuan durasi timeout socket.|Mencocokkan poin-poin ide tersebut dengan kejadian nyata pada screenshot terminal Node 1–5, lalu menuliskannya kembali menjadi analisis di bagian kendala dan observasi Jurnal Proses|
|20/10/2026 | Gemini | Bagaimana urutan alur logika (outline) tahapan pemilihan leader pada Bully Algorithm saat node baru menyala dan saat mendeteksi leader mati? | memberikan outline tahapan pengiriman pesan ELECTION ke peer ber-ID lebih besar, mekanisme tunggu balasan OK dengan timeout, serta kondisi kapan node mem-broadcast pesan COORDINATOR. | Memahami konsep alur tersebut lalu menerjemahkannya sendiri ke dalam baris kode Python pada bagian # TODO 1-4 di file src/node.py. |
