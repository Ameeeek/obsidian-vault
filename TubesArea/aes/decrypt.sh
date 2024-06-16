
#!/bin/bash

# Direktori yang akan dipantau
WATCHED_DIR="/home/amek/Desktop/OkSobatMengoding/prototyping/aes/"
# Kata sandi untuk enkripsi/dekripsi
PASSWORD="000123"
# File kunci
LOCKFILE="/tmp/encrypt_decrypt.lock"

# Fungsi untuk mendekripsi file
decrypt_file() {
    local file="$1"
    local decrypted_file="${file%.enc}"

    # Pastikan file adalah file terenkripsi
    if [[ "${file##*.}" == "enc" ]]; then
        if [[ -f "$file" ]]; then # Periksa apakah file ada
            if openssl aes-256-cbc -d -in "$file" -out "$decrypted_file" -pass pass:"$PASSWORD"; then
                echo "File $file berhasil didekripsi menjadi $decrypted_file"
                rm "$file"
            else
                echo "Gagal mendekripsi $file"
            fi
        else
            echo "File $file tidak ditemukan untuk didekripsi"
        fi
    fi
}

# Memantau direktori untuk akses file
inotifywait -m -e open --format '%w%f' "$WATCHED_DIR" | while read -r file; do
    (
        echo "File diakses: $file"
        flock -n 9 || exit 1
        sleep 1 # Tambahkan penundaan untuk memastikan file selesai dibuat
        decrypt_file "$file"
    ) 9>"$LOCKFILE"
done

