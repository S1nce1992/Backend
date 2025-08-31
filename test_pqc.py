# save this as test_pqc.py and run: python test_pqc.py
from Shared.pqc_lib import kem, sign

print("=== Testing KEM ===")
handshake = kem.init_handshake()
print("Handshake result:")
for k, v in handshake.items():
    if isinstance(v, dict):
        print(f"  {k}: {v}")
    else:
        print(f"  {k}: {v[:50]}{'...' if len(v) > 50 else ''}")

print("\n=== Testing SIGN ===")
message = b"post-quantum crypto test"
sig_result = sign.sign(message)
print("Signature result:")
for k, v in sig_result.items():
    print(f"  {k}: {v[:50]}{'...' if len(v) > 50 else ''}")

verify_result = sign.verify(
    message,
    sig_result["signature"],
    sig_result["public_key"]
)
print("Verification result:", verify_result)
