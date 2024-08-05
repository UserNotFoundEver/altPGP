aes_key = get_random_bytes(32)  # AES-256 key
aes_nonce = get_random_bytes(12)  # GCM nonce

cipher = AES.new(aes_key, AES.MODE_GCM, nonce=aes_nonce)
ciphertext, tag = cipher.encrypt_and_digest(b'This is a secret message.')

cipher_dec = AES.new(aes_key, AES.MODE_GCM, nonce=aes_nonce)
plaintext = cipher_dec.decrypt_and_verify(ciphertext, tag)

fig, ax3 = plt.subplots(figsize=(10, 6))
ax3.text(0.5, 0.5, f"Ciphertext:\n{ciphertext.hex()[:64]}...\nTag: {tag.hex()}\nDecrypted Message: {plaintext.decode()}", ha='center', va='center', fontsize=12)
ax3.set_title("AES-256 Encryption with GCM")
ax3.axis('off')
