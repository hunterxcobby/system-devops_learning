### Removing or Changing the Passphrase on a Private Key - A Quick Guide:

1. **Modify Passphrase:**
   - If you wish to change the passphrase on your private key:
  
     ```bash
     ssh-keygen -p
     ```

   - Enter the location of your key or press ENTER for the default.
  
   ```bash
   Enter file in which the key is (/home/demo/.ssh/id_rsa):
   ```

   - Provide the old passphrase and set a new one.

2. **Remove Passphrase:**
   - If you want to remove the passphrase:

     ```bash
     ssh-keygen -p
     ```

   - Enter the key location and the old passphrase.
   - Press ENTER when asked for the new passphrase.

3. **Note:**
   - If you forget the old passphrase, no magical spells can recover it.
   - You might need to generate a new key pair in that case.

### Displaying the SSH Key Fingerprint - Unveiling the Magic:

1. **Find the Fingerprint:**
   - Discover the unique fingerprint of your SSH key pair.

   ```bash
   ssh-keygen -l
   ```

   - Confirm the key location or provide the correct one.

   ```bash
   Enter file in which the key is (/home/demo/.ssh/id_rsa):
   ```

2. **Witness the Magic:**
   - Receive a string showcasing the key's bit-length, fingerprint, and more.

   ```bash
   4096 8e:c4:82:47:87:c2:26:4b:68:ff:96:1a:39:62:9e:4e demo@test (RSA)
   ```

Now you possess the knowledge to modify passphrases and reveal the magical fingerprints of your SSH keys. Use this wisdom wisely in your server adventures.