import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# --- KONFIGURASI AWAL ---
load_dotenv()
try:
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
except Exception as e:
    st.error("API Key tidak ditemukan atau terjadi error. Pastikan file .env Anda sudah benar.")
    st.stop()

# --- FUNGSI-FUNGSI LOGIKA ---

def dapatkan_resep_by_nama(nama_masakan):
    prompt = f"""
    Langsung berikan resep masakan Nusantara yang detail dan otentik untuk: {nama_masakan}.
    Gunakan format di bawah ini dengan ketat, tanpa kalimat pembuka atau penutup tambahan.
    **Nama Masakan:** {nama_masakan}
    **Asal Daerah:** [Sebutkan asal daerah masakan ini]
    **Deskripsi Singkat:** [Berikan 1-2 kalimat deskripsi yang menarik]
    **Bahan-bahan:**
    - [Bahan 1]
    - [dst...]
    **Bumbu Halus:**
    - [Bumbu 1]
    - [dst...]
    **Langkah-langkah Pembuatan:**
    1. [Langkah pertama]
    2. [dst...]
    **Tips & Trik:** [Berikan satu tips menarik]
    """
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Terjadi error: {e}"

def buat_resep_by_bahan(daftar_bahan):
    prompt = f"""
    Anda adalah seorang Koki Nusantara yang sangat kreatif dan handal.
    Tugas Anda adalah membuat satu resep masakan yang paling lezat dan cocok dari daftar bahan-bahan yang diberikan.
    Bahan-bahan yang tersedia: {daftar_bahan}.
    Buatkan resepnya menggunakan format di bawah ini dengan ketat:
    **Nama Resep Kreasi:** [Buatkan nama yang unik dan menarik untuk resep ini]
    **Deskripsi Singkat:** [Jelaskan secara singkat mengapa resep ini cocok dengan bahan yang ada]
    **Bahan-bahan yang Dibutuhkan:**
    - [Bahan 1 dari daftar]
    - [Bahan 2 dari daftar]
    - [Tambahkan bahan umum lain jika sangat diperlukan, misal: air, garam, gula]
    **Bumbu Halus (jika ada):**
    - [Bumbu 1 dari daftar]
    - [dst...]
    **Langkah-langkah Pembuatan:**
    1. [Langkah pertama]
    2. [dst...]
    **Selamat Menikmati!**
    """
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Terjadi error: {e}"

# --- FUNGSI BARU UNTUK MENAMPILKAN RESEP DENGAN RAPI ---
def tampilkan_resep_terformat(resep_teks):
    """
    Fungsi ini mengambil teks mentah dari AI dan menampilkannya
    dengan format kolom yang rapi dan bersih dari kode markdown.
    """
    baris_resep = resep_teks.splitlines()
    
    for baris in baris_resep:
        if ":" in baris:
            parts = baris.split(":", 1)
            
            # Menghapus karakter '**' dari label dan isi
            label = parts[0].replace("**", "").strip()
            isi = parts[1].replace("**", "").strip()
            
            col1, col2 = st.columns([1, 3])
            
            with col1:
                # Kita buat tebal lagi secara manual dengan st.markdown
                st.markdown(f"**{label}:**") 
            with col2:
                st.write(isi)
        else:
            # Jika baris tidak punya titik dua, tampilkan seperti biasa
            # dan ganti strip dengan bullet point agar lebih cantik
            st.markdown(baris.replace("- ", "• "))

# --- BAGIAN UTAMA APLIKASI STREAMLIT (USER INTERFACE) ---

st.title("🍳 Juru Resep Nusantara Digital")

# --- SIDEBAR UNTUK NAVIGASI ---
st.sidebar.title("Pilih Mode")
app_mode = st.sidebar.radio(
    "Pilih fitur yang ingin Anda gunakan:",
    ["Cari Resep Klasik", "👨‍🍳 Koki Kreatif"]
)

# --- KONTEN BERDASARKAN PILIHAN DI SIDEBAR ---
if app_mode == "Cari Resep Klasik":
    st.header("Cari Resep Berdasarkan Nama")
    with st.form("search_recipe_form"):
        nama_masakan = st.text_input("Ketik nama masakan (Contoh: Rendang)")
        submitted1 = st.form_submit_button("Carikan Resep")
        if submitted1:
            if nama_masakan:
                with st.spinner(f"Mencari resep {nama_masakan}..."):
                    resep = dapatkan_resep_by_nama(nama_masakan)
                    # Panggil fungsi baru untuk menampilkan hasil
                    tampilkan_resep_terformat(resep)
            else:
                st.error("Mohon masukkan nama masakan.")

elif app_mode == "👨‍🍳 Koki Kreatif":
    st.header("Buat Resep dari Bahan yang Ada")
    st.write("Sulap bahan di kulkasmu menjadi mahakarya kuliner!")
    with st.form("create_recipe_form"):
        daftar_bahan = st.text_area("Ketik semua bahan yang Anda punya, pisahkan dengan koma (Contoh: ayam, santan, bawang merah)")
        submitted2 = st.form_submit_button("Buatkan Resep Ajaib!")
        if submitted2:
            if daftar_bahan:
                with st.spinner("Sang Koki sedang meracik resep..."):
                    resep_kreasi = buat_resep_by_bahan(daftar_bahan)
                    # Panggil fungsi baru untuk menampilkan hasil
                    tampilkan_resep_terformat(resep_kreasi)
            else:
                st.error("Mohon masukkan bahan-bahan.")