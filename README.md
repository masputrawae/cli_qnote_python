# MD Note (Praktik Pribadi)

MD Note adalah program Python sederhana untuk membuat catatan cepat dalam format Markdown, lengkap dengan frontmatter dan backup via Git. **Catatan:** proyek ini dibuat hanya untuk praktik pribadi.

## Fitur
- Membuat catatan dengan frontmatter: title, tags, created date
- Slug otomatis dari judul catatan
- Backup catatan ke repository Git
- Restore dari repository
- Lihat daftar file dengan struktur folder (`tree`)
- Clear terminal untuk tampilan lebih bersih

## Cara Pakai
1. Clone repository:
```bash
git clone https://github.com/masputrawae/cli_qnote_python.git qnote
cd qnote
````

2. Jalankan program:

```bash
python md_note.py
```

3. Ikuti menu interaktif:

* \[1] Create Note
* \[2] Show List
* \[3] Backup
* \[4] Backup Status
* \[5] Restore
* \[6] Clear Terminal
* \[7] Exit

4. Semua catatan disimpan di folder default `./notes/inbox` atau folder yang kamu pilih. File berekstensi `.md`.

## Contoh Frontmatter Catatan

```yaml
---
title: Contoh Judul
tags: ['unorganized', 'idea']
created: 2025-09-25T14:30:00+07:00
---
```

## Catatan

* Proyek ini **untuk latihan/praktik pribadi**, tidak dimaksudkan untuk produksi.
* Gunakan sesuai kebutuhan pribadi.

## Lisensi

Bebas digunakan untuk keperluan belajar/praktik pribadi.

