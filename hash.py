sha3_hash = SHA3_256.new(data=b'This is a secret message.').hexdigest()
blake2_hash = BLAKE2b.new(digest_bits=256, data=b'This is a secret message.').hexdigest()

ax1 = fig.add_subplot(gs[0])
ax1.text(0.5, 0.5, f"SHA-3 Hash:\n{sha3_hash}", ha='center', va='center', fontsize=12)
ax1.set_title("SHA-3 Hashing")
ax1.axis('off')

ax2 = fig.add_subplot(gs[1])
ax2.text(0.5, 0.5, f"BLAKE2b Hash:\n{blake2_hash}", ha='center', va='center', fontsize=12)
ax2.set_title("BLAKE2b Hashing")
ax2.axis('off')
