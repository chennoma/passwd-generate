import secrets
import string

def generate_alphanumeric_password(length=32):
    """
    生成一个只包含大小写字母和数字的密码
    
    参数:
        length (int): 密码长度，默认为32位
        
    返回:
        str: 生成的字母数字密码
    """
    # 定义字符集
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    
    # 生成密码
    password = ''.join(secrets.choice(chars) for _ in range(length))
    
    return password

if __name__ == "__main__":
    # 生成一个32位的字母数字密码并打印
    password = generate_alphanumeric_password()
    print("生成的32位字母数字密码:")
    print(password)