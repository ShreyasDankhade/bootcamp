# Simple Static Site on Azure Linux VM

Run a web server with just one page displaying your name and photo. In your project README.md, provide the link to the website. Describe how you set it up. No need for any fancy HTML. This serves as proof that you completed the setup tasks.

---

## Live Site

[http://4.213.224.103/](http://4.213.224.103/)

---

## How I Set It Up

1. **Created a Resource Group**
   In the Azure Portal (`portal.azure.com`) under **Resource groups → + Create**:

   * **Name:** `testWS`
   * **Region:** `Central India`

2. **Provisioned an Ubuntu VM**
   In the Portal under **Virtual machines → + Create → Azure virtual machine**:

   * **Name:** `testWebServer`
   * **Image:** `Linux (ubuntu 24.04)`
   * **Size:** `Standard D2s v3`
   * **Inbound ports:** Selected **SSH (22)** and **HTTP (80)**

4. **Connected via SSH**

   ```bash
   ssh azureuser@4.213.224.103
   ```

5. **Installed and Enabled Nginx**

   ```bash
   sudo apt update
   sudo apt install nginx -y
   sudo systemctl enable --now nginx
   ```

6. **Gave the Server Write Access**

   ```bash
   sudo chown -R azureuser:azureuser /var/www/html
   ```

7. **Deployed My Files**
   From my local project folder (containing `index.html` and `assets/photo.jpg`):

   ```bash
   scp -i ./private_key.pem index.html assets/photo.jpg azureuser@4.213.224.103:/var/www/html/
   ```

8. **Viewed the Page**
   Open a browser to `http://4.213.224.103/` and confirm my name and photo load correctly.

