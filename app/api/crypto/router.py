import sys
from pathlib import Path

# Add the parent of Backend (~/dev) to sys.path
sys.path.append(str(Path(__file__).resolve().parents[3]))

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

# Now that sys.path is updated, import from Shared
from Shared.pqc_lib import kem, aead, sign

router = APIRouter()

# --- KEM ---
@router.post("/kem/init")
def kem_init():
    return kem.init_handshake()

class KemCompleteReq(BaseModel):
    session_id: str
    kyber_ct: str
    hqc_ct: str
    context: str | None = None

@router.post("/kem/complete")
def kem_complete(req: KemCompleteReq):
    try:
        return kem.complete_handshake(req.session_id, req.kyber_ct, req.hqc_ct, (req.context or "").encode())
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# --- AEAD ---
class EncryptReq(BaseModel):
    session_id: str
    plaintext: str
    aad: str | None = None

@router.post("/aead/encrypt")
def aead_encrypt(req: EncryptReq):
    return aead.encrypt(req.session_id, req.plaintext.encode(), (req.aad or "").encode())

class DecryptReq(BaseModel):
    session_id: str
    nonce: str
    ciphertext: str
    aad: str | None = None

@router.post("/aead/decrypt")
def aead_decrypt(req: DecryptReq):
    return aead.decrypt(req.session_id, req.nonce, req.ciphertext, (req.aad or "").encode())

# --- Sign ---
class Msg(BaseModel):
    message: str

@router.post("/sign")
def sign_message(req: Msg):
    return sign.sign(req.message.encode())

class VerifyReq(BaseModel):
    message: str
    signature: str
    public_key: str

@router.post("/verify")
def verify_message(req: VerifyReq):
    return sign.verify(req.message.encode(), req.signature, req.public_key)


