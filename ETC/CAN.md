# CAN



## CAN(Control Area Network) DATA FRAME 구조

| 12bit |            | 6bit | 10~64bit | 16bit | 2bit | 7bit |
| ----- | ---------- | ---- | -------- | ----- | ---- | ---- |
| SoF   | Identifier | DLC  | Data     | CRC   | ACK  | EoF  |

dominant

recessive



## 프로토콜

* 다중 마스터 구조
* CSMA(Carrier Sense Multiple Access)
* CD-CR(Collision Detection with Collision Resoultion)
* 전송되는 메시지 그 자체가 우선 순위를 가지는 Data
* Bit Stuffing



