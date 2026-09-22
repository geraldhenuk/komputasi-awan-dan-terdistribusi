# Jurnal Proses — Tugas 1

> Isi jurnal ini selama proses diskusi berlangsung, bukan ditulis ulang rapi di akhir. Tulis dengan gaya bebas — poin diskusi, kebuntuan, perubahan pikiran.

## [Sabtu, 19 September 2026]
- Peserta: Gerald, Farisa, Fito
- Poin diskusi: Membedah masing gmasing pitfall
- Perbedaan pendapat (jika ada): ...

## [Selasa, 22 September 2026]
- Peserta: Gerald, Farisa, Fito
- Poin diskusi: Mengisi Log Penggunaan Ai
- Perbedaan pendapat (jika ada): ...

## Review Silang
- Gerald mengomentari analisis Refito: saya juga setuju dengan pembahasan retry, tetapi jumlah retry perlu dibatasi supaya tidak malah menambah beban server.
- Gerald mengomentari analisis Farisa: menurut saya, penggunaan idempotency menjadi hal penting supaya masalah tersebut bisa dicegah.

- Farisa mengomentari analisis Gerald: Analisis SPOF sudah tepat. Penjelasan soal impact saat server monolitik crash sudah jelas. Tambahan poin biaya operasional di bagian trade-off juga realistis untuk startup ini.

- Farisa mengomentari analisis Refito: Identifikasinya sudah tepat dengan bukti di skenario. Usulan pakai Circuit Breaker juga sangat tepat untuk pencegahan agar server tidak crash beruntun.

- Fito mengomentari analisis Gerald: saya setuju dengan solusi load balancer, tetapi perlu dipikirkan juga biaya operasionalnya agar tidak terlalu membengkak.

- Fito mengomentari analisis Farisa: menurut saya, penambahan timeout sudah tepat, tinggal dipastikan lagi batas waktunya agar pengguna tidak menunggu terlalu lama.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 22 september 2026 | Gemini | Bantu buatkan struktur dan kerangka untuk analisis pitfall kasus FoodGo | Dikasih saran outline pembahasan kayak bukti, dampak, solusi, sama trade-off-nya | Cuma ngambil struktur dan poin-poin ide solusinya aja, sisanya ditulis ulang pakai kalimat sendiri sesuai hasil diskusi kelompok |
