Hướng dẫn cài SMS Gateway trong Ubuntu Server 12.04
=============================

**Table of Contents**  *generated with [DocToc](http://doctoc.herokuapp.com/)*

[Hướng dẫn cài SMS Gateway trong Ubuntu Server 12.04](#user-content-h%C6%B0%E1%BB%9Bng-d%E1%BA%ABn-c%C3%A0i-sms-gateway-trong-ubuntu-server-1204)

[Giới thiệu](#user-content-gi%E1%BB%9Bi-thi%E1%BB%87u)

[1. Các bước chuẩn bị](#user-content-1-c%C3%A1c-b%C6%B0%E1%BB%9Bc-chu%E1%BA%A9n-b%E1%BB%8B)

[2. Các bước thực hiện](#user-content-2-c%C3%A1c-b%C6%B0%E1%BB%9Bc-th%E1%BB%B1c-hi%E1%BB%87n)

[2.1. Chuẩn bị máy và kết nối với USB sau khi cắm](#user-content-21-chu%E1%BA%A9n-b%E1%BB%8B-m%C3%A1y-v%C3%A0-k%E1%BA%BFt-n%E1%BB%91i-v%E1%BB%9Bi-usb-sau-khi-c%E1%BA%AFm)

[2.2 Thực hiện cài các gói cần thiết](#user-content-22-th%E1%BB%B1c-hi%E1%BB%87n-c%C3%A0i-c%C3%A1c-g%C3%B3i-c%E1%BA%A7n-thi%E1%BA%BFt)

[2.3. Thử gửi tin nhắn bằng dòng lệnh](#user-content-23-th%E1%BB%AD-g%E1%BB%ADi-tin-nh%E1%BA%AFn-b%E1%BA%B1ng-d%C3%B2ng-l%E1%BB%87nh)

[2.4. Mở rộng của SMS Gateway để kết hợp với các ứng dụng khác](#user-content-24-m%E1%BB%9F-r%E1%BB%99ng-c%E1%BB%A7a-sms-gateway-%C4%91%E1%BB%83-k%E1%BA%BFt-h%E1%BB%A3p-v%E1%BB%9Bi-c%C3%A1c-%E1%BB%A9ng-d%E1%BB%A5ng-kh%C3%A1c)

 [3. Liên hệ](#user-content-3-li%C3%AAn-h%E1%BB%87)

 [4. Cám ơn](#user-content-4-c%C3%A1m-%C6%A1n)

[5. Tham khảo](#user-content-5-tham-kh%E1%BA%A3o)


### Giới thiệu

Một chiều thứ 7 cuối thu - lang thang và mải mê tìm kiếm thông tin để phục vụ nhu cầu gửi SMS thông qua USB 3G được kết nối với 1 máy chủ Linux.

Sau một hồi tìm kiếm mình được thầy "MạngNV" và các bạn bè gợi ý bởi nhiều phần mềm có chức năng  SMS Gateway như Gammu, Kannel ...nhưng config vất vả quá.

Cũng trong lúc "Lý Bí" mình tìm được link ở dưới giới thiệu ở dưới về "gsm-utils" và mình đã thử, kết quả là trên cả tuyệt vời, nay mình tổng hợp lại các bước làm và chú ý ở đây để cho ai đó có nhu cầu dùng lại.

### 1. Các bước chuẩn bị

>* 01 USB 3G. Các USB được hỗ trợ bởi UBUNTU có thể tham khảo ở đây 
https://wiki.ubuntu.com/NetworkManager/Hardware/3G

>* Một máy chủ cài đặt Ubuntu 12.04 Server 64 bit. Có thể là máy ảo cài trên VMware WorkStation.

### 2. Các bước thực hiện
#### 2.1. Chuẩn bị máy và kết nối với USB sau khi cắm

- Ở đây mình cài Ubuntu 12.04 lên VMware Workstations (nếu bạn cài trên máy thật thì không cần làm động tác dưới đây và chuyển sang bước 2.2 luôn)
- Tất nhiên máy ảo đã được cài đặt và USB được cắm vào máy thật và đảm bảo máy ảo được có lựa chọn kết nối USB như hình dưới.

<img src=http://i.imgur.com/GAeWEC5.png width="60%" height="60%" border="1">

- Bật máy ảo và lựa chọn cho máy ảo kết nối được với USB (cần đảm bảo nước này)

<img src=http://i.imgur.com/g6jzmiu.png width="80%" height="80%" border="1">

#### 2.2 Thực hiện cài các gói cần thiết

- Kiểm tra xem USB đã nhận hay chưa, đối với các USB mà Ubuntu hỗ trợ ở link trên thì dùng lệnh dưới để kiểm tra
```sh
lsusb
```
Kết quả như hình dưới

<img src=http://i.imgur.com/hbDBsrh.png width="80%" height="80%" border="1">

- Thực hiện cài đặt gói  usb-modeswitch gsm-utils với quyền `root`. Trong đó gói  usb-modeswitch dùng để kết nối tới USB trong Linux còn gói gms-utils dùng để thực hiện gửi SMS.
```sh
apt-get update
apt-get install usb-modeswitch gsm-utils -y
```

Kiểm tra xem USB đã được kết nối thành công hay chưa bằng cách dùng lệnh `tail` để kiểm tra log. Lúc này đối với máy ảo bạn cần thực hiện thao tác disconnect USB và kết nối lại giống hình này ở Bước 2.1 http://i.imgur.com/g6jzmiu.png 

còn đối với máy thật thì rút USB ra cắm lại

```sh
tail -f /var/log/syslog
```
- Kết quả lệnh `tail` ở máy mình nhu dưới
```sh
Nov  1 23:36:01 controller kernel: [ 1229.351198] usb 1-1: new high-speed USB device number 3 using ehci-pci
Nov  1 23:36:01 controller kernel: [ 1229.626642] usb 1-1: New USB device found, idVendor=12d1, idProduct=1506
Nov  1 23:36:01 controller kernel: [ 1229.626645] usb 1-1: New USB device strings: Mfr=2, Product=1, SerialNumber=0
Nov  1 23:36:01 controller kernel: [ 1229.626647] usb 1-1: Product: HUAWEI Mobile
Nov  1 23:36:01 controller kernel: [ 1229.626649] usb 1-1: Manufacturer: HUAWEI
Nov  1 23:36:01 controller kernel: [ 1229.633703] option 1-1:1.0: GSM modem (1-port) converter detected
Nov  1 23:36:01 controller kernel: [ 1229.634048] usb 1-1: GSM modem (1-port) converter now attached to ttyUSB0
Nov  1 23:36:01 controller kernel: [ 1229.682679] usb 1-1: MAC-Address: 58:2c:80:13:92:63
Nov  1 23:36:01 controller kernel: [ 1229.682877] cdc_ncm 1-1:1.1 wwan0: register 'cdc_ncm' at usb-0000:02:03.0-1, Mobile Broadband Network Device, 58:2c:80:13:92:63
Nov  1 23:36:01 controller kernel: [ 1229.682973] option 1-1:1.2: GSM modem (1-port) converter detected
Nov  1 23:36:01 controller kernel: [ 1229.683142] usb 1-1: GSM modem (1-port) converter now attached to ttyUSB1
Nov  1 23:36:01 controller kernel: [ 1229.683200] option 1-1:1.3: GSM modem (1-port) converter detected
Nov  1 23:36:01 controller kernel: [ 1229.683346] usb 1-1: GSM modem (1-port) converter now attached to ttyUSB2
Nov  1 23:36:01 controller kernel: [ 1229.683732] scsi35 : usb-storage 1-1:1.4
Nov  1 23:36:01 controller kernel: [ 1229.684118] scsi36 : usb-storage 1-1:1.5
Nov  1 23:36:02 controller kernel: [ 1230.685974] scsi 36:0:0:0: Direct-Access     HUAWEI   SD Storage       2.31 PQ: 0 ANSI: 2
Nov  1 23:36:02 controller kernel: [ 1230.687495] scsi 35:0:0:0: CD-ROM            HUAWEI   Mass Storage     2.31 PQ: 0 ANSI: 2
```

- Nếu trong log trên máy khi bạn thực hành xuất hiện dòng dưới thì mọi việc đã ổn, bạn có thể bắt đầu gửi SMS.

```sh
GSM modem (1-port) converter now attached to ttyUSBX

Trong đó USBX là USB0, USB1 hoặc USB2.
```

#### 2.3. Thử gửi tin nhắn bằng dòng lệnh
- Lúc này bạn đã có thể gửi tin nhắn trong CLI tới số điện thoại mà bạn muốn như sau
```sh
echo "Test chuc nang SMS" | gsmsendsms -d /dev/ttyUSB0 -b 19200 091234940

Trong đó:
Test chuc nang SMS: Nội dung gửi
0912349490: Là số điện thoại cần gửi (số mình)
```


#### 2.4. Mở rộng của SMS Gateway để kết hợp với các ứng dụng khác
```sh
Đang soạn
```

### 3. Liên hệ
- Email: tcvn1985@gmail.com
- Skype: tu0ng_c0ng

### 4. Cám ơn
Nam | Tiến

### 5. Tham khảo
http://hashtips.wordpress.com/2013/04/12/send-sms-using-a-usb-modem-and-ubuntu-12-04/
http://packages.ubuntu.com/lucid/gsm-utils
 
