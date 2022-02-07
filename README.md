# pyqt-password-dlg

![input password dialogue example](https://github.com/vitperov/pyqt-password-dlg/raw/main/dialogue-example.png) 

## How to use
First, just include the module:

    from AskPasswordDlg import *
    
Best prictice is to store encrypted password. Yes, even encrypted password is not safe: if you know sha256, you can brute-force find the original password string. But it much more secure, than just unencrypted password

    pwd = 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'    
    isPasswordCorrect = AskPasswordDlg.runDlg(pwd)
    
Dialogue return True or False.

## How to encrypt sha256 own passowrd
    import hashlib
    pwd = hashlib.sha256(b'123').hexdigest() # do not store unencrypted password!
    print(pwd)
