# Tugas 1 — Analisis Pitfall FoodGo

**Kelompok:** [swk]

| Nama | NIM | Kontribusi |
|---|---|---|
| [Refito Rahmat Firmansyah] | [103072430002] | [pitfall 1] |
| [Gerald Farellino Henuk] | [103072400116] | [Pitfall 2] |
| [farisa] | [103072400051] | [pitfall/bagian yang dikerjakan] |

## Pitfall 1: [Fallacy — "The Network is Reliable"] — ditulis oleh [refito]

**Bukti di skenario:** Tim engineering menemukan kode yang memiliki asumsi seperti *“network is always reliable, no need for retry”*.

**Kenapa ini keliru:** Jaringan di dunia nyata tidak pernah 100% stabil. Menunggu tanpa timeout membuat sistem menggantung saat koneksi terganggu atau lambat.

**Dampak ke FoodGo:** Thread server menumpuk karena terus menunggu respons pembayaran. Saat trafik naik di jam makan siang, resource server habis dan backend crash total.

**Solusi desain awal:** Menambahkan timeout dan retry mechanism pada pemanggilan antar service. Bisa juga dipasang circuit breaker untuk memutus pemanggilan jika service pembayaran bermasalah.

**Trade-off:** Retry yang terlalu banyak saat jaringan terganggu justru bisa memperberat beban server dan memperparah kemacetan lalu lintas data.

---

## Pitfall 2: [Single Point of Failure] — ditulis oleh [Gerald Farellino Henuk]

**Bukti di skenario:** Disebutkan bahwa backend kadang crash total dan membutuhkan restart manual, sementara seluruh modul berjalan pada satu proses dan satu server.

**Kenapa ini keliru:** Jika hanya ada satu server yang menangani seluruh sistem, server tersebut menjadi single point of failure. Artinya, ketika server tersebut mati, tidak ada sistem lain yang langsung mengambil alih.

**Dampak ke FoodGo:** Saat server crash, pengguna bisa tidak dapat membuat pesanan, pembayaran bisa terganggu, dan kurir juga tidak mendapatkan informasi pesanan tepat waktu. Karena recovery masih membutuhkan restart manual, downtime bisa menjadi lebih lama.

**Solusi desain awal:** Menjalankan beberapa server dari service penting dan menggunakan load balancer di depannya. Selain itu, sistem perlu memiliki health check dan mekanisme otomatis untuk mengganti server yang gagal.

**Trade-Off:** Solusi dengan menggunakan beberapa instance server dan sistem failover memang dapat mengurangi risiko seluruh aplikasi mati ketika satu server mengalami crash. Namun, trade-off-nya adalah sistem menjadi lebih kompleks dan biaya operasional menjadi lebih besar.

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
