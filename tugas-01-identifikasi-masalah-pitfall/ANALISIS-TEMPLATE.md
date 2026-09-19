# Tugas 1 — Analisis Pitfall FoodGo

**Kelompok:** [swk]

| Nama | NIM | Kontribusi |
|---|---|---|
| [refito] | [nim] | [pitfall/bagian yang dikerjakan] |
| [Gerald Farellino Henuk] | [103072400116] | [Pitfall 2] |
| [farisa] | [103072400051] | [pitfall/bagian yang dikerjakan] |

## Pitfall 1: [nama pitfall] — ditulis oleh [nama]

**Bukti di skenario:** [kutip/paraphrase bagian skenario]

**Kenapa ini keliru:** []

**Dampak ke FoodGo:** [mekanisme kegagalan konkret]

**Solusi desain awal:** [usulan solusi]

**Trade-off:** [apa yang dikorbankan/risiko dari solusi ini]

---

## Pitfall 2: [Single Point of Failure] — ditulis oleh [Gerald Farellino Henuk]

**Bukti di skenario:** Disebutkan bahwa backend kadang crash total dan membutuhkan restart manual, sementara seluruh modul berjalan pada satu proses dan satu server.

**Kenapa ini keliru:** Jika hanya ada satu server yang menangani seluruh sistem, server tersebut menjadi single point of failure. Artinya, ketika server tersebut mati, tidak ada sistem lain yang langsung mengambil alih.

**Dampak ke FoodGo:** Saat server crash, pengguna bisa tidak dapat membuat pesanan, pembayaran bisa terganggu, dan kurir juga tidak mendapatkan informasi pesanan tepat waktu. Karena recovery masih membutuhkan restart manual, downtime bisa menjadi lebih lama.

**Solusi desain awal:** Menjalankan beberapa server dari service penting dan menggunakan load balancer di depannya. Selain itu, sistem perlu memiliki health check dan mekanisme otomatis untuk mengganti server yang gagal.

**Trade-Off:** Solusi dengan menggunakan beberapa instance server dan sistem failover memang dapat mengurangi risiko seluruh aplikasi mati ketika satu server mengalami crash. Namun, trade-off-nya adalah sistem menjadi lebih kompleks dan biaya operasional menjadi lebih besar.

---

## Pitfall 3: [nama pitfall] — ditulis oleh [nama]

(ulangi struktur di atas)

---

## Kesimpulan Kelompok

[Ringkasan: jika FoodGo memperbaiki ketiga pitfall ini, apa arsitektur yang disarankan secara garis besar? Kaitkan dengan Tugas 2.]
