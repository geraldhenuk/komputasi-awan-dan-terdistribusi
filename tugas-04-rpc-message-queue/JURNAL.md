# Jurnal Proses — Tugas 4

## Jalur yang dipilih
- [RPC / MQ / keduanya], alasan: 
    - RPC (Jalur A) Farisa
    Alasan milih RPC: Operasi `cek_saldo` dan `proses_pembayaran` butuh respon seketika (sinkron). Modul Pesanan harus mengetahui apakah saldo cukup dan pembayaran sukses/gagal sebelum lanjut ke tahap selanjutnya. Pola RPC cocok karena client benar-benar nunggu balasan dari server.
    - MQ (Jalur B) Fito 
    Memilih MQ karena notifikasi ke Modul Kurir bersifat asinkron. Modul Pembayaran bisa langsung merespons "Pembayaran Berhasil" ke sisi *user* tanpa mempedulikan status *online/offline* dari kurir. Pesan akan tetap aman dan diantrekan oleh *message broker*.

## Kendala teknis
- Error saat setup (mis. koneksi RabbitMQ ditolak, port bentrok):
    - RPC :
        - Saat pertama kali running `client.py`, muncul error `ConnectionRefusedError: [WinError 10061]`. Ternyata server.py belum dijalankan. Solusinya: running server.py dulu di terminal terpisah sebelum running client.
        - Saat uji blocking, saya menambahkan `time.sleep(3)` di server.py. Client beneran nunggu 3 detik sebelum menerima balasan, membuktikan RPC bersifat blocking/sinkron.
        - Saat server dimatikan (Ctrl + C) dan client running, langsung muncul error koneksi. Ini membuktikan client sangat bergantung pada server yang hidup.
    -  MQ : 
        - Saat mencoba menyalakan RabbitMQ melalui Docker Compose, saya mendapat sedikit *error* karena     *daemon* Docker Desktop belum sepenuhnya jalan. Solusi: Pastikan aplikasi Docker berjalan di *background*.
        - Ketika mengeksekusi `publisher.py`, saya mendapati galat `ModuleNotFoundError: No module named 'pika'`. Galat ini terjadi karena saya lupa mengaktifkan *virtual environment* (`venv`) yang berisi *library* untuk RabbitMQ. Solusi: Jalankan sintaks pengaktifan *venv*, kemudian `pip install -r requirements.txt`.


## Uji "pesan tidak hilang" (khusus Jalur B)
- Langkah uji: matikan consumer → jalankan publisher → nyalakan consumer
- Hasil yang diamati: Saat `consumer.py` sedang tidak aktif, antarmuka `publisher` seolah-olah melaporkan bahwa pesan berhasil terkirim, dan pesannya memang tidak hilang (disimpan sementara oleh antrean/Queue pada RabbitMQ). Setelah `consumer.py` dinyalakan kembali, ia langsung memproses semua pesan yang menumpuk tersebut secara berurutan. Ini adalah bukti konkrit dari prinsip *asynchronous decoupling*, di mana pesan diletakkan dalam *broker* dan diantrekan hingga *consumer* siap membacanya.
## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 10/10/2026 | ChatGPT | Langkah-langkah pengerjaan Jalur A RPC dari nol | Urutan: edit server.py, client.py, jalankan 2 terminal, ss, uji blocking dengan `time.sleep`, dan uji server mati | Saya ketik sendiri kode TODO, AI hanya kasih urutan langkah dan outline jurnal |
| ... | ... | ... | ... | ... |