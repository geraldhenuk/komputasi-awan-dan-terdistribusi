# Tugas 1 — Analisis Pitfall FoodGo

**Kelompok:** [swk]

| Nama | NIM | Kontribusi |
|---|---|---|
| [refito] | [103072430002] | [Pitfall 1: "The Network is Reliable" (Timeout, Retry, Circuit Breaker)] |
| [gerald] | [nim] | [pitfall/bagian yang dikerjakan] |
| [farisa] | [103072400051] | [pitfall/bagian yang dikerjakan] |

## Pitfall 1: [Fallacy — "The Network is Reliable"] — ditulis oleh [refito]

**Bukti di skenario:** [Tim menemukan bahwa kode mereka menulis asumsi seperti # network is always reliable, no need for retry dan tidak ada timeout sama sekali pada pemanggilan antar service (modul pesanan memanggil modul pembayaran dan menunggu tanpa batas waktu).]

**Kenapa ini keliru:** [Jaringan antarlayanan atau third-party payment gateway bersifat nondeterministic. Gangguan seperti packet loss, penurunan bandwidth, atau unresponsive server bisa terjadi sewaktu-waktu. Menunggu tanpa batas (infinite wait) mengasumsikan jaringan pasti 100% selalu berhasil dan merespons tepat waktu.]

**Dampak ke FoodGo:** [Saat layanan pembayaran delay atau down, thread pemanggil pada modul pesanan terblokir (blocking thread) tanpa batas. Ketika lonjakan pesanan terjadi di jam makan siang, thread pool web server habis (resource exhaustion), permintaan baru langsung timeout, hingga server backend crash total dan butuh restart manual.]

**Solusi desain awal:** [Menerapkan Timeout eksplisit pada setiap pemanggilan I/O atau API eksternal, dikombinasikan dengan Retry Mechanism (menggunakan exponential backoff dan jitter). Menerapkan pola Circuit Breaker untuk memutus pemanggilan sementara jika failure rate modul pembayaran melewati batas toleransi.]

**Trade-off:** [Mekanisme retry yang tidak terkontrol saat jaringan terganggu dapat memicu retry storm, yang memperberat beban jaringan dan justru mempercepat terjadinya cascading failure.]

---

## Pitfall 2: [nama pitfall] — ditulis oleh [nama]

(ulangi struktur di atas)

---

## Pitfall 3: [Latency is Zero] — ditulis oleh [Farisa]

**Bukti di skenario:** Modul pesanan memanggil modul pembayaran dan menunggu tanpa batas waktu, karena tidak ada timeout.

**Kenapa ini keliru:** Pada sistem terdistribusi, pengiriman data lewat jaringan membutuhkan waktu (Latency), tidak sama seperti pemanggilan fungsi lokal di memori. 

**Dampak ke FoodGo:** Tanpa timeout, thread di modul pesanan akan terus menunggu respons dari modul pembayaran. Pada jam sibuk, tumpukan panggilan yang saling menunggu membuat response time melonjak tajam. Request baru yang masuk ikut antre, performa aplikasi melambat secara dratis, hingga akhirnya terkena request timeout.

**Solusi desain awal:** FoodGo harus menerapkan timeout pada komunikasi antarservice. Jika ada pembayaran belum merespons dalam kurun waktu yang ditentukan, request dianggap gagal atau diproses ulang menggunakan mekanisme retry.

**Trade-off:** Timeout dapat menyebabkan request dianggap gagal meskipun pembayaran masih memproses transaksi. Jika ditambahkan mekanisme retry, juga menyebabkan transaksi ganda. Sehingga FoodGo perlu menggunakan mekanisme idempotency mencegah pembayaran ganda.

---

## Kesimpulan Kelompok

[Ringkasan: jika FoodGo memperbaiki ketiga pitfall ini, apa arsitektur yang disarankan secara garis besar? Kaitkan dengan Tugas 2.]
