from PIL import Image
from secrets import token_bytes


def get_image_data(image):
    img = Image.open(image)
    data = 'img', img, img.format
    return str(data)

def dummy_key(length):
    dummy = token_bytes(length)
    return int.from_bytes(dummy, 'big')

def encrypt(data: str):
    data_bytes = data.encode('UTF-8')
    dummy = dummy_key(len(data_bytes))
    data_bytes_int = int.from_bytes(data_bytes, 'big')
    encrypted = data_bytes_int ^ dummy
    return dummy, encrypted

def decrypt(key1, key2):
    decrypted: int = key1 ^ key2
    target = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, 'big')
    return target.decode('UTF-8')

if __name__ == '__main__':
    data = get_image_data('photo.jpg')
    key1, key2 = encrypt(data)
    print(key2)
    decrypt_data  = decrypt(key1, key2)
    print(decrypt_data)
    print(data == decrypt_data)
    