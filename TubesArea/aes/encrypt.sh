
#!/bin/bash

# Direktori yang akan dipantau
WATCHED_DIR="/home/amek/Desktop/OkSobatMengoding/prototyping/aes/"
# Kata sandi untuk enkripsi/dekripsi
PASSWORD="000123"
# File kunci
LOCKFILE="/tmp/encrypt_decrypt.lock"

# Fungsi untuk mengenkripsi file
encrypt_file() {
    local file="$1"
    local encrypted_file="${file}.enc"

    # Pastikan file belum terenkripsi
    if [[ "${file##*.}" != "enc" ]]; then
        if openssl aes-256-cbc -salt -in "$file" -out "$encrypted_file" -pass pass:"$PASSWORD"; then
            echo "File $file berhasil dienkripsi menjadi $encrypted_file"
            rm "$file"
        else
            echo "Gagal mengenkripsi $file"
        fi
    fi
}

# Memantau direktori untuk perubahan file
inotifywait -m -e create --format '%w%f' "$WATCHED_DIR" | while read -r file; do
    (
        echo "File baru terdeteksi: $file"
        flock -n 9 || exit 1
        sleep 1 # Tambahkan penundaan untuk memastikan file selesai dibuat
        encrypt_file "$file"
    ) 9>"$LOCKFILE"
done

