# Jurnal Proses — Tugas 4

## Jalur yang dipilih
- [RPC / MQ / keduanya], alasan: 
    - RPC (Jalur A) Farisa
    Alasan milih RPC: Operasi `cek_saldo` dan `proses_pembayaran` butuh respon seketika (sinkron). Modul Pesanan harus mengetahui apakah saldo cukup dan pembayaran sukses/gagal sebelum lanjut ke tahap selanjutnya. Pola RPC cocok karena client benar-benar nunggu balasan dari server.

## Kendala teknis
- Error saat setup (mis. koneksi RabbitMQ ditolak, port bentrok):
    - RPC :
        - Saat pertama kali running `client.py`, muncul error `ConnectionRefusedError: [WinError 10061]`. Ternyata server.py belum dijalankan. Solusinya: running server.py dulu di terminal terpisah sebelum running client.
        - Saat uji blocking, saya menambahkan `time.sleep(3)` di server.py. Client beneran nunggu 3 detik sebelum menerima balasan, membuktikan RPC bersifat blocking/sinkron.
        - Saat server dimatikan (Ctrl + C) dan client running, langsung muncul error koneksi. Ini membuktikan client sangat bergantung pada server yang hidup.


## Uji "pesan tidak hilang" (khusus Jalur B)
- Langkah uji: matikan consumer → jalankan publisher → nyalakan consumer
- Hasil yang diamati: ...

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 10/10/2026 | ChatGPT | Langkah-langkah pengerjaan Jalur A RPC dari nol | Urutan: edit server.py, client.py, jalankan 2 terminal, ss, uji blocking dengan `time.sleep`, dan uji server mati | Saya ketik sendiri kode TODO, AI hanya kasih urutan langkah dan outline jurnal |
| ... | ... | ... | ... | ... |