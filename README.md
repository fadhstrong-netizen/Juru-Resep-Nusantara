# 🍳 Juru Resep Nusantara Digital

Sebuah chatbot cerdas berbasis AI yang berfungsi sebagai asisten masak virtual, khusus untuk masakan Indonesia. Aplikasi ini dibuat menggunakan Streamlit dan Google Gemini API.

## ✨ Fitur-fitur

* **Cari Resep Klasik:** Pengguna dapat mencari resep masakan Nusantara berdasarkan namanya.
* **Koki Kreatif:** Pengguna dapat memasukkan daftar bahan yang mereka miliki, dan AI akan membuatkan resep yang sesuai dari bahan-bahan tersebut.
* **Layout Profesional:** Aplikasi menggunakan navigasi sidebar untuk pengalaman pengguna yang lebih baik.

## 📸 Tampilan Aplikasi

*Tambahkan screenshot aplikasi Anda di sini. Anda bisa mengunggah gambar saat mengedit file ini.*


## 🚀 Cara Menjalankan

1.  **Clone repositori ini:**
    ```bash
    git clone [https://github.com/fadhstrong-netizen/Juru-Resep-Nusantara.git](https://github.com/fadhstrong-netizen/Juru-Resep-Nusantara.git)
    ```
2.  **Buat dan aktifkan environment conda:**
    ```bash
    conda create -n resep-env python=3.9
    conda activate resep-env
    ```
3.  **Install semua library yang dibutuhkan:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Buat file `.env`** dan isi dengan Google API Key Anda:
    ```
    GOOGLE_API_KEY="API_KEY_ANDA"
    ```
5.  **Jalankan aplikasi Streamlit:**
    ```bash
    streamlit run app.py
    ```
