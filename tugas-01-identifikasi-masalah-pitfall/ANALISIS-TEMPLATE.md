# Tugas 1 — Analisis Pitfall FoodGo

**Kelompok:** [swk]

| Nama | NIM | Kontribusi |
|---|---|---|
| [refito] | [103072430002] | [Pitfall 1: "The Network is Reliable" (Timeout, Retry, Circuit Breaker)] |
| [gerald] | [nim] | [pitfall/bagian yang dikerjakan] |
| [farisa] | [103072400051] | [pitfall/bagian yang dikerjakan] |

## Pitfall 1: [Fallacy — "The Network is Reliable"] — ditulis oleh [refito]

**Bukti di skenario:** [Tim engineering menemukan kode yang memiliki asumsi seperti *“network is always reliable, no need for retry”*.]

**Kenapa ini keliru:** [Jaringan di dunia nyata tidak pernah 100% stabil. Menunggu tanpa timeout membuat sistem menggantung saat koneksi terganggu atau lambat.]

**Dampak ke FoodGo:** [Thread server menumpuk karena terus menunggu respons pembayaran. Saat trafik naik di jam makan siang, resource server habis dan backend crash total.]

**Solusi desain awal:** [Menambahkan timeout dan retry mechanism pada pemanggilan antar service. Bisa juga dipasang circuit breaker untuk memutus pemanggilan jika service pembayaran bermasalah.]

**Trade-off:** [Retry yang terlalu banyak saat jaringan terganggu justru bisa memperberat beban server dan memperparah kemacetan lalu lintas data.]

---

## Pitfall 2: [nama pitfall] — ditulis oleh [nama]

(ulangi struktur di atas)

---

## Pitfall 3: [nama pitfall] — ditulis oleh [nama]

(ulangi struktur di atas)

---

## Kesimpulan Kelompok

[Ringkasan: jika FoodGo memperbaiki ketiga pitfall ini, apa arsitektur yang disarankan secara garis besar? Kaitkan dengan Tugas 2.]
