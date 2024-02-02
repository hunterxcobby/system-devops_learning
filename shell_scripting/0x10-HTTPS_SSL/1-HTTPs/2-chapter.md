Let's delve into how HTTPS works:

1. **SSL/TLS Protocols**:
   - HTTPS pages utilize either SSL (Secure Sockets Layer) or its successor TLS (Transport Layer Security) to encrypt communications between the web server and the browser.
   - These protocols establish a secure connection by encrypting data transmitted over the network.

2. **Asymmetric Encryption**:
   - SSL/TLS protocols employ an 'asymmetric' Public Key Infrastructure (PKI) system.
   - This system uses two keys: a 'public' key and a 'private' key.
   - Anything encrypted with the public key can only be decrypted by the corresponding private key, and vice versa.

3. **Key Management**:
   - The 'private' key is securely stored and accessible only to the owner, typically residing on the web server.
   - This private key is crucial for decrypting data encrypted with the corresponding public key.
   - Conversely, the 'public' key is distributed to anyone needing to decrypt information encrypted with the private key.
   - It's important to note that while the public key is freely distributed, the private key remains securely protected and inaccessible to unauthorized entities.

In essence, HTTPS works by encrypting data using asymmetric encryption, ensuring that sensitive information transmitted between the web server and the browser remains secure and private. The private key, held securely on the server, decrypts data encrypted with the corresponding public key, which is freely distributed for decryption purposes. This encryption scheme safeguards against eavesdropping and unauthorized access to sensitive data during transmission over the internet.