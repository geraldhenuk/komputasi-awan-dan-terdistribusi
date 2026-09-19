# Tugas 1 — Analisis Pitfall FoodGo

**Kelompok:** [swk]

| Nama | NIM | Kontribusi |
|---|---|---|
| [refito] | [nim] | [pitfall/bagian yang dikerjakan] |
| [Gerald Farellino Henuk] | [103072400116] | [Pitfall 2] |
| [farisa] | [103072400051] | [pitfall/bagian yang dikerjakan] |

## Pitfall 1: [Fallacy — "The Network is Reliable"] — ditulis oleh [refito]

**Bukti di skenario:** [Tim menemukan bahwa kode mereka menulis asumsi seperti # network is always reliable, no need for retry dan tidak ada timeout sama sekali pada pemanggilan antar service (modul pesanan memanggil modul pembayaran dan menunggu tanpa batas waktu).]

**Kenapa ini keliru:** [Di dunia nyata, jaringan komputer itu nggak pernah bisa dipastikan 100% lancar. Bisa aja tiba-tiba ada packet loss, koneksi lambat, atau API dari pihak ketiga (seperti payment gateway) lagi down. Kalau kode kita dibuat nunggu balasan tanpa batas waktu (infinite wait), kita seolah-olah menganggap jaringan bakal selalu aman dan pasti langsung membalas.]

**Dampak ke FoodGo:** [Pas modul pembayaran lagi lemot atau unresponsive, thread di modul pesanan bakal tertahan dan terus nungguin tanpa kepastian. Begitu ada lonjakan transaksi di jam makan siang, stok thread pool di web server langsung ludes. Akibatnya, pesanan baru yang masuk kena timeout, server kehabisan memori, lalu backend langsung crash total sampai harus di-restart manual.]

**Solusi desain awal:** [Atur Timeout yang jelas di tiap pemanggilan API atau jaringan, biar kalau kelamaan nggak direspon bisa langsung diputus. Dipadu dengan mekanisme Retry pakai jeda berkala (exponential backoff + jitter). Selain itu, pasang pola Circuit Breaker—jadi kalau sistem mendeteksi modul pembayaran lagi sering gagal, aliran pemanggilan bisa diputus sementara otomatis biar server nggak makin terbeban.]

**Trade-off:** [Mekanisme retry ini ibarat pisau bermata dua. Kalau jaringan lagi benar-benar tumbang lalu sistem terus-terusan kirim retry ulang secara masif (retry storm), lalu lintas jaringan malah makin penuh dan bisa bikin komponen lain ikut tumbang (cascading failure).]

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
