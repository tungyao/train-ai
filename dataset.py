import json

data = [
    ("原装正品0603贴片电容25V100NF±10%X7RCL10B104KA8NNNC50只",
     [("CL10B104KA8NNNC", "Model"),
      ("0603", "Package"),
      ("贴片电容", "Type"),
      ("25V", "Voltage"),
      ("100NF", "Cap"),
      ("10%", "Precision"),
      ("", "Resistance"),
      ("", "Watt"),
      ("", "Inductance"),
      ("", "Electricity"),
      ]),
    ("原装正品0603贴片电阻1K标字1021/10W精度5%（200只）",
     [("", "Model"),
      ("0603", "Package"),
      ("贴片电阻", "Type"),
      ("", "Voltage"),
      ("", "Cap"),
      ("5%", "Precision"),
      ("1K", "Resistance"),
      ("1/10W", "Watt"),
      ("", "Inductance"),
      ("", "Electricity"),
      ]),
    ("原装正品0603贴片电阻22R22欧1/10W精度±1%（50只）",
     [("", "Model"),
      ("0603", "Package"),
      ("贴片电阻", "Type"),
      ("", "Voltage"),
      ("", "Cap"),
      ("1%", "Precision"),
      ("22R", "Resistance"),
      ("1/10W", "Watt"),
      ("", "Inductance"),
      ("", "Electricity"),

      ]),
    ("0603贴片电感2.2UH±10%EBLS1608-2R2K(50只）",
     [("EBLS1608-2R2K", "Model"),
      ("0603", "Package"),
      ("贴片电感", "Type"),
      ("", "Voltage"),
      ("", "Cap"),
      ("10%", "Precision"),
      ("", "Resistance"),
      ("", "Watt"),
      ("2.2UH", "Inductance"),
      ("", "Electricity"),

      ]),
    ("贴片AO3401SOT-23MOS管/三极管/场效应管2.8A（20只）",
     [("AO3401", "Model"),
      ("SOT-23", "Package"),
      ("MOS管", "Type"),
      ("", "Voltage"),
      ("", "Cap"),
      ("", "Precision"),
      ("", "Resistance"),
      ("", "Watt"),
      ("", "Inductance"),
      ("2.8A", "Electricity"),

      ]),
    ("原装正品SGM4056-6.8YTDE8G/TR丝印SG7TDFN8锂电池充电管理IC",
     [("SGM4056-6.8YTDE8G/TR", "Model"),
      ("TDFN8", "Package"),
      ("锂电池充电管理IC", "Type"),
      ("", "Voltage"),
      ("", "Cap"),
      ("", "Precision"),
      ("", "Resistance"),
      ("", "Watt"),
      ("", "Inductance"),
      ("", "Electricity"),

      ]),
    (
        """
        商品目录	贴片型铝电解电容	
   容值	220uF	
   精度	±20%	
   额定电压	50V	
   纹波电流	220mA@120Hz	
   等效串联电阻	-	
   电容体直径	10mm	
   电容体长度	10mm	
   工作寿命	1000hrs@105℃	
   工作温度	-55℃~+105℃
   封装：SMD,D10xL10mm
        """
        ,
        [("", "Model"),
         ("SMD,D10xL10mm", "Package"),
         ("贴片型铝电解电容", "Type"),
         ("50V", "Voltage"),
         ("220uF", "Cap"),
         ("20%", "Precision"),
         ("", "Resistance"),
         ("", "Watt"),
         ("", "Inductance"),
         ("220mA@120Hz", "Electricity")]
    ),
    ("""
商品目录	贴片型铝电解电容	
容值	220uF	
精度	±20%	
额定电压	10V	
纹波电流	90mA@120Hz	
等效串联电阻	-	
电容体直径	6.3mm	
电容体长度	5.4mm	
工作寿命	2000hrs@105℃	
工作温度	-40℃~+105℃
封装：SMD,D6.3xL5.4mm
""",
     [("", "Model"),
      ("SMD,D6.3xL5.4mm", "Package"),
      ("贴片型铝电解电容", "Type"),
      ("10V", "Voltage"),
      ("220uF", "Cap"),
      ("20%", "Precision"),
      ("", "Resistance"),
      ("", "Watt"),
      ("", "Inductance"),
      ("90mA@120Hz", "Electricity")]
     ),
    ("""
商品目录	贴片型铝电解电容	
容值	100uF	
精度	±20%	
额定电压	16V	
纹波电流	129mA@10kHz	
等效串联电阻	-	
电容体直径	-	
电容体长度	-	
工作寿命	2000hrs@85℃	
工作温度	-40℃~+85℃
封装：SMD,D6.3xL5.4mm
""",
     [("", "Model"),
      ("SMD,D6.3xL5.4mm", "Package"),
      ("贴片型铝电解电容", "Type"),
      ("16V", "Voltage"),
      ("100uF", "Cap"),
      ("20%", "Precision"),
      ("", "Resistance"),
      ("", "Watt"),
      ("", "Inductance"),
      ("129mA@10kHz", "Electricity")]
     ),

    ("""
商品目录	贴片型铝电解电容	
容值	100uF	
精度	±20%	
额定电压	50V	
纹波电流	140mA@120Hz	
等效串联电阻	-	
电容体直径	-	
电容体长度	-	
工作寿命	1000hrs@105℃	
工作温度	-55℃~+105℃
封装：SMD,D8xL10mm
""",
     [("", "Model"),
      ("SMD,D8xL10mm", "Package"),
      ("贴片型铝电解电容", "Type"),
      ("50V", "Voltage"),

      ("100uF", "Cap"),
      ("20%", "Precision"),
      ("", "Resistance"),
      ("", "Watt"),
      ("", "Inductance"),
      ("140mA@120Hz", "Electricity")]
     ),

    (
        """
        商品目录	直插铝电解电容	
      容值	220uF	
      精度	±20%	
      额定电压	35V	
      纹波电流	-	
      等效串联电阻	-	
      脚间距	3.5mm	
      电容体直径	8mm	
      电容体长度	12mm	
      工作寿命	2000hrs@105℃
      封装：插件,D8xL12mm
        """,
        [("", "Model"),
         ("插件,D8xL12mm", "Package"),
         ("直插铝电解电容", "Type"),
         ("35V", "Voltage"),

         ("220uF", "Cap"),
         ("20%", "Precision"),
         ("", "Resistance"),
         ("", "Watt"),
         ("", "Inductance"),
         ("", "Electricity")]
    ), (
        """
        商品目录	直插铝电解电容	
      容值	220uF	
      精度	±20%	
      额定电压	16V	
      纹波电流	-	
      等效串联电阻	-	
      脚间距	2.5mm	
      电容体直径	6.3mm	
      电容体长度	11mm	
      工作寿命	1000hrs@105℃
      封装：插件,D6.3xL11mm
      """,
        [("", "Model"),
         ("插件,D6.3xL11mm", "Package"),
         ("直插铝电解电容", "Type"),
         ("16V", "Voltage"),

         ("220uF", "Cap"),
         ("20%", "Precision"),
         ("", "Resistance"),
         ("", "Watt"),
         ("", "Inductance"),
         ("", "Electricity")]
    ), ("""
    商品目录	钽电容	
容值	220uF	
精度	±20%	
额定电压	6.3V	
等效串联电阻	500mΩ@100kHz	
工作温度	-55℃~+125℃
封装：CASE-B-3528-21(mm)
    """,
        [("", "Model"),
         ("CASE-B-3528-21(mm)", "Package"),
         ("钽电容", "Type"),
         ("6.3V", "Voltage"),

         ("220uF", "Cap"),
         ("20%", "Precision"),
         ("500mΩ@100kHz", "Resistance"),
         ("", "Watt"),
         ("", "Inductance"),
         ("", "Electricity"),
         ]
        ), ("""
        商品目录：钽电容
        容值：47uF
        精度：±10%
        额定电压：10V
        等效串联电阻：1Ω@100kHz
        工作温度：-55℃~+125℃
        封装：CASE-B-3528-21(mm)
        """,
            [("", "Model"),
             ("CASE-B-3528-21(mm)", "Package"),
             ("钽电容", "Type"),
             ("10V", "Voltage"),

             ("47uF", "Cap"),
             ("10%", "Precision"),
             ("1Ω@100kHz", "Resistance"),
             ("", "Watt"),
             ("", "Inductance"),
             ("", "Electricity")
             ]
            ),
    ("""
            商品目录：钽电容
容值：100uF
精度：±20%
额定电压：10V
等效串联电阻：1.4Ω@100kHz
工作温度：-55℃~+125℃
封装：CASE-B-3528-21(mm)
            """,
     [("", "Model"),
      ("CASE-B-3528-21(mm)", "Package"),
      ("钽电容", "Type"),
      ("10V", "Voltage"),

      ("100uF", "Cap"),
      ("20%", "Precision"),
      ("1.4Ω@100kHz", "Resistance"),
      ("", "Watt"),
      ("", "Inductance"),
      ("", "Electricity")]
     ),
    ("""
商品目录	固态电容	
容值	100uF	
精度	±20%	
额定电压	35V	
纹波电流	2.35A@100kHz	
等效串联电阻	50mΩ@100kHz	
类型	-	
脚间距	2.5mm	
电容体直径	6.3mm	
电容体长度	8mm	
工作寿命	2000hrs@105℃	
工作温度	-55℃~+105℃
封装：插件,D6.3xL8mm
                """,
     [("", "Model"),
      ("插件,D6.3xL8mm", "Package"),
      ("固态电容", "Type"),

      ("35V", "Voltage"),
      ("100uF", "Cap"),
      ("20%", "Precision"),
      ("50mΩ@100kHz", "Resistance"),
      ("", "Watt"),
      ("", "Inductance"),
      ("2.35A@100kHz", "Electricity"),

      ]
     ), ("""
                    商品目录	固态电容	
容值	100uF	
精度	±20%	
额定电压	50V	
纹波电流	2.1A@100kHz	
等效串联电阻	40mΩ@100kHz	
类型	-	
脚间距	3.5mm	
电容体直径	8mm	
电容体长度	9mm	
工作寿命	2000hrs@105℃	
工作温度	-55℃~+105℃
封装：插件,D8xL9mm
                    """,
         [("", "Model"),
          ("插件,D8xL9mm", "Package"),
          ("固态电容", "Type"),
          ("50V", "Voltage"),

          ("100uF", "Cap"),
          ("20%", "Precision"),
          ("40mΩ@100kHz", "Resistance"),
          ("", "Watt"),
          ("", "Inductance"),
          ("2.1A@100kHz", "Electricity"),
          ]
         ),
    ("""
商品目录	固态电容	
容值	100uF	
精度	±20%	
额定电压	35V	
纹波电流	1.516A@100kHz	
等效串联电阻	80mΩ@100kHz	
脚间距	2.5mm	
电容体直径	6.3mm	
电容体长度	7mm	
工作寿命	2000hrs@105℃	
工作温度	-55℃~+105℃
封装：SMD,D6.3xL7mm
""",
     [("", "Model"),
      ("SMD,D6.3xL7mm", "Package"),
      ("固态电容", "Type"),
      ("35V", "Voltage"),

      ("100uF", "Cap"),
      ("20%", "Precision"),
      ("80mΩ@100kHz", "Resistance"),
      ("", "Watt"),
      ("", "Inductance"),
      ("1.516A@100kHz", "Electricity"),
      ]
     ), ("""
     商品目录	固态电容	
容值	100uF	
精度	±20%	
额定电压	25V
封装：SMD,D6.3xL5.9mm
     """,
         [("", "Model"),
          ("SMD,D6.3xL5.9mm", "Package"),
          ("固态电容", "Type"),
          ("25V", "Voltage"),

          ("100uF", "Cap"),
          ("20%", "Precision"),
          ("", "Resistance"),
          ("", "Watt"),
          ("", "Inductance"),
          ("", "Electricity"),
          ]
         ), ("""
         商品目录	固态电容	
容值	470uF	
精度	±20%	
额定电压	50V	
纹波电流	-	
等效串联电阻	-	
类型	-	
脚间距	-	
电容体直径	-	
电容体长度	-	
工作寿命	-
封装：插件,D10xL18mm
         """,
             [("", "Model"),
              ("插件,D10xL18mm", "Package"),
              ("固态电容", "Type"),
              ("50V", "Voltage"),

              ("470uF", "Cap"),
              ("20%", "Precision"),
              ("", "Resistance"),
              ("", "Watt"),
              ("", "Inductance"),
              ("", "Electricity"),

              ]
             ), ("""
             商品目录	固态电容	
容值	330uF	
精度	±20%	
额定电压	16V	
纹波电流	-	
等效串联电阻	-	
类型	-	
脚间距	2.5mm	
电容体直径	6.3mm	
电容体长度	9mm	
工作寿命	2000hrs@105℃	
工作温度	-55℃~+105℃
封装：插件,D6.3xL9mm
             """,
                 [("", "Model"),
                  ("插件,D6.3xL9mm", "Package"),
                  ("固态电容", "Type"),
                  ("16V", "Voltage"),
                  ("330uF", "Cap"),
                  ("20%", "Precision"),
                  ("", "Resistance"),
                  ("", "Watt"),
                  ("", "Inductance"),
                  ("", "Electricity"),

                  ]
                 ), ("""
                 商品目录	固态电容	
容值	220uF	
精度	±20%	
额定电压	35V	
纹波电流	2.7A@100kHz	
等效串联电阻	30mΩ@100kHz	
类型	-	
脚间距	2.5mm	
电容体直径	6.3mm	
电容体长度	11mm	
工作寿命	2000hrs@105℃	
工作温度	-55℃~+105℃
封装：插件,D6.3xL11mm
                 """,
                     [("", "Model"),
                      ("插件,D6.3xL11mm", "Package"),
                      ("固态电容", "Type"),
                      ("35V", "Voltage"),

                      ("220uF", "Cap"),
                      ("20%", "Precision"),
                      ("30mΩ@100kHz", "Resistance"),
                      ("", "Watt"),
                      ("", "Inductance"),
                      ("2.7A@100kHz", "Electricity"),
                      ]
                     ), ("""
                     商品目录	固液混合铝电解电容器	
容值	100uF	
精度	±20%	
额定电压	35V	
工作寿命	4000hrs@125℃	
工作温度	-55℃~+125℃
封装：SMD,D6.3xL7.7mm
                     """,
                         [("", "Model"),
                          ("SMD,D6.3xL7.7mm", "Package"),
                          ("固液混合铝电解电容器", "Type"),
                          ("35V", "Voltage"),

                          ("100uF", "Cap"),

                          ("20%", "Precision"),
                          ("", "Resistance"),
                          ("", "Watt"),
                          ("", "Inductance"),
                          ("", "Electricity"),
                          ]
                         ), ("""
                         商品目录	固液混合铝电解电容器	
容值	33uF	
精度	±20%	
额定电压	50V	
纹波电流	1.1A@100kHz	
等效串联电阻	40mΩ@100kHz	
工作寿命	4000hrs@125℃	
工作温度	-55℃~+125℃	
脚间距	-	
电容体直径	6.3mm	
电容体长度	7.7mm
封装：SMD,D6.3xL7.7mm
                         """,
                             [("", "Model"),
                              ("SMD,D6.3xL7.7mm", "Package"),
                              ("固液混合铝电解电容器", "Type"),
                              ("50V", "Voltage"),

                              ("33uF", "Cap"),
                              ("20%", "Precision"),
                              ("40mΩ@100kHz", "Resistance"),
                              ("", "Watt"),
                              ("", "Inductance"),
                              ("1.1A@100kHz", "Electricity"),
                              ]
                             ),
    ("""
商品目录	固液混合铝电解电容器	
容值	56uF	
精度	±20%	
额定电压	63V	
纹波电流	270mA@100Hz	
等效串联电阻	30mΩ	
工作寿命	10000hrs@105℃	
工作温度	-55℃~+105℃	
脚间距	-	
电容体直径	10mm	
电容体长度	10.2mm	
封装：SMD,D10xL10.2mm

""",
     [("", "Model"),
      ("SMD,D10xL10.2mm", "Package"),
      ("固液混合铝电解电容器", "Type"),
      ("63V", "Voltage"),

      ("56uF", "Cap"),
      ("20%", "Precision"),
      ("30mΩ", "Resistance"),
      ("", "Watt"),
      ("", "Inductance"),
      ("270mA@100Hz", "Electricity")]
     ),
    ("""
商品目录	贴片电阻	
电阻类型	厚膜电阻	
阻值	10kΩ	
精度	±1%	
功率	100mW	
最大工作电压	75V	
温度系数	±100ppm/℃	
工作温度范围	-55℃~+155℃
封装：0603
""",
     [("", "Model"),
      ("0603", "Package"),
      ("贴片电阻", "Type"),
      ("75V", "Voltage"),
      ("", "Cap"),
      ("1%", "Precision"),
      ("100mW", "Watt"),
      ("10kΩ", "Resistance"),
      ("", "Inductance"),

      ("", "Electricity")]
     ),
    ("""
10kΩ±1%125mW厚膜电阻0805
""",
     [("", "Model"),
      ("0805", "Package"),
      ("厚膜电阻", "Type"),
      ("", "Voltage"),
      ("", "Cap"),
      ("1%", "Precision"),
      ("125mW", "Watt"),
      ("10kΩ", "Resistance"),
      ("", "Inductance"),
      ("", "Electricity")]
     ),
    ("""
100kΩ±1%100mW厚膜电阻  0603
""",
     [("", "Model"),
      ("0603", "Package"),
      ("厚膜电阻", "Type"),
      ("", "Voltage"),
      ("", "Cap"),
      ("1%", "Precision"),
      ("100mW", "Watt"),
      ("100kΩ", "Resistance"),
      ("", "Inductance"),
      ("", "Electricity")]
     ),
    ("""厚膜电阻100kΩ±1%100mW0603""",
     [("", "Model"),
      ("0603", "Package"),
      ("厚膜电阻", "Type"),
      ("", "Voltage"),
      ("", "Cap"),
      ("1%", "Precision"),
      ("100mW", "Watt"),
      ("100kΩ", "Resistance"),
      ("", "Inductance"),
      ("", "Electricity")]
     ),
    ("""
0402WGJ0103TCE
品牌:UNI-ROYAL(厚声)
封装:0402
电阻类型:厚膜电阻
阻值:10kΩ
精度:±5%
功率:62.5mW
类目:贴片电阻
编号:C25531
详细:数据手册
""",
     [("", "Model"),
      ("0402", "Package"),
      ("厚膜电阻", "Type"),
      ("", "Voltage"),
      ("", "Cap"),
      ("5%", "Precision"),
      ("62.5mW", "Watt"),
      ("10kΩ", "Resistance"),
      ("", "Inductance"),
      ("", "Electricity")]
     ),
    ("""
0603WAF220JT5E
品牌:UNI-ROYAL(厚声)
封装:0603
电阻类型:厚膜电阻
阻值:22Ω
精度:±1%
功率:100mW
类目:贴片电阻
编号:C23345
详细:数据手册
""",
     [("", "Model"),
      ("0603", "Package"),
      ("厚膜电阻", "Type"),
      ("", "Voltage"),
      ("", "Cap"),
      ("1%", "Precision"),
      ("100mW", "Watt"),
      ("22Ω", "Resistance"),
      ("", "Inductance"),
      ("", "Electricity")]
     ),
    ("""
商品目录	稳压二极管	
二极管配置	独立式	
稳压值(标称值)	12V	
反向电流(Ir)	100nA@9V	
稳压值(范围)	11.4V~12.7V	
功率(Pd)	500mW	
阻抗(Zzt)	35Ω	
封装：SOD-123
""",
     [("", "Model"),
      ("SOD-123", "Package"),
      ("稳压二极管", "Type"),
      ("12V", "Voltage"),
      ("", "Cap"),
      ("", "Precision"),
      ("", "Resistance"),
      ("500mW", "Watt"),
      ("", "Inductance"),
      ("100nA@9V", "Electricity"),
      ]
     ),
    ("""
BZT52C3V3
品牌:MDD(辰达半导体)
封装:SOD-123
描述:通用贴片稳压二极管，精度5%，较低的IR漏电流
二极管配置:独立式
稳压值(标称值):3.3V
反向电流(Ir):20uA@1V
稳压值(范围):3.1V~3.5V
类目:稳压二极管
编号:C173413
详细:数据手册
""",
     [("MDD", "Model"),
      ("SOD-123", "Package"),
      ("稳压二极管", "Type"),
      ("3.3V", "Voltage"),
      ("", "Cap"),
      ("", "Precision"),
      ("", "Resistance"),
      ("", "Watt"),
      ("", "Inductance"),
      ("20uA@1V", "Electricity"),
      ]
     ),
    ("""
BZT52C5V1
品牌:TWGMC(台湾迪嘉)
封装:SOD-123
描述:二极管配置：独立式稳压值(标称值)：5.1V稳压值(范围)：4.8V~5.4V功率：500mW
稳压值(标称值):5.1V
反向电流(Ir):2uA@2V
功率(Pd):500mW
类目:稳压二极管
编号:C726995
详细:数据手册
""",
     [("TWGMC", "Model"),
      ("SOD-123", "Package"),
      ("稳压二极管", "Type"),
      ("5.1V", "Voltage"),
      ("", "Cap"),
      ("", "Precision"),
      ("", "Resistance"),
      ("500mW", "Watt"),
      ("", "Inductance"),
      ("2uA@2V", "Electricity"),
      ]
     ),
    ("""
ZMM5V6
品牌:HXYMOSFET(华轩阳电子)
封装:LL-34
描述:此款LL-34封装稳压二极管，具备5.6V精准电压稳定性能（VZ），搭载超低0.1uA反向电流（IR），确保电路在微功耗状态下高效稳定运行。5mA瞬态IZT电流能力，使器件在负载变化时迅速响应并保持输出稳定。最大功率耗散0.5W，适用于各类精密稳压及电路保护应用场景，以出色的效能满足您的设计需求。
二极管配置:独立式
稳压值(标称值):5.6V
反向电流(Ir):100nA@1V
稳压值(范围):5.2V~6V
类目:稳压二极管
编号:C5345993
详细:数据手册
""",
     [("HXYMOSFET", "Model"),
      ("LL-34", "Package"),
      ("稳压二极管", "Type"),
      ("5.6V", "Voltage"),
      ("", "Cap"),
      ("", "Precision"),
      ("", "Resistance"),
      ("", "Watt"),
      ("", "Inductance"),
      ("100nA@1V", "Electricity"),
      ]
     ),
    ("""
商品目录	稳压二极管	
二极管配置	独立式	
稳压值(标称值)	16V	
反向电流(Ir)	100nA@12V	
稳压值(范围)	15.2V~16.8V	
功率(Pd)	350mW	
阻抗(Zzt)	17Ω
SOD-123
""",
     [("", "Model"),
      ("SOD-123", "Package"),
      ("稳压二极管", "Type"),
      ("16V", "Voltage"),
      ("", "Cap"),
      ("", "Precision"),
      ("", "Resistance"),
      ("350mW", "Watt"),
      ("", "Inductance"),
      ("100nA@12V", "Electricity"),
      ]
     ),
    ("""
SS34
品牌:MDD(辰达半导体)
封装:SMA(DO-214AC)
二极管配置:独立式
正向压降(Vf):550mV@3A
直流反向耐压(Vr):40V
整流电流:3A
类目:肖特基二极管
编号:C8678
详细:数据手册
""",
     [("MDD", "Model"),
      ("SMA(DO-214AC)", "Package"),
      ("肖特基二极管", "Type"),
      ("40V", "Voltage"),
      ("", "Cap"),
      ("", "Precision"),
      ("", "Resistance"),
      ("", "Watt"),
      ("", "Inductance"),
      ("3A", "Electricity"),
      ]
     ),
    ("""
商品目录	肖特基二极管	
二极管配置	独立式	
正向压降(Vf)	550mV@1A	
直流反向耐压(Vr)	40V	
整流电流	1A	
反向电流(Ir)	500uA@40V
封装：SMA(DO-214AC)
""",
     [("", "Model"),
      ("SMA(DO-214AC)", "Package"),
      ("肖特基二极管", "Type"),
      ("40V", "Voltage"),
      ("", "Cap"),
      ("", "Precision"),
      ("", "Resistance"),
      ("", "Watt"),
      ("", "Inductance"),
      ("1A", "Electricity"),
      ]
     ),
    ("""
SS210
品牌:MDD(辰达半导体)
封装:SMA(DO-214AC)
正向压降(Vf):850mV@2A
直流反向耐压(Vr):100V
整流电流:2A
类目:肖特基二极管
编号:C14996
详细:数据手册
""",
     [("MDD", "Model"),
      ("SMA(DO-214AC)", "Package"),
      ("肖特基二极管", "Type"),
      ("100V", "Voltage"),
      ("", "Cap"),
      ("", "Precision"),
      ("", "Resistance"),
      ("", "Watt"),
      ("", "Inductance"),
      ("2A", "Electricity"),
      ]
     ),
    ("""
M7
品牌:MDD(辰达半导体)
封装:SMA(DO-214AC)
描述:GPP
正向压降(Vf):1.1V@1A
直流反向耐压(Vr):1kV
整流电流:1A
反向电流(Ir):5uA@1kV
类目:通用二极管
编号:C95872
详细:数据手册
""",
     [("MDD", "Model"),
      ("SMA(DO-214AC)", "Package"),
      ("通用二极管", "Type"),
      ("1kV", "Voltage"),
      ("", "Cap"),
      ("", "Precision"),
      ("", "Resistance"),
      ("", "Watt"),
      ("", "Inductance"),
      ("1A", "Electricity"),
      ]
     ),
    ("""
M7
品牌:MSKSEMI(美森科)
封装:DO-214AC
描述:丝印M7
正向压降(Vf):1.1V@1A
直流反向耐压(Vr):1kV
整流电流:1A
反向电流(Ir):5uA@1kV
类目:通用二极管
编号:C2902910
详细:数据手册
""",
     [("MSKSEMI", "Model"),
      ("DO-214AC", "Package"),
      ("通用二极管", "Type"),
      ("1kV", "Voltage"),
      ("", "Cap"),
      ("", "Precision"),
      ("", "Resistance"),
      ("", "Watt"),
      ("", "Inductance"),
      ("1A", "Electricity"),
      ]
     ),
    ("""
商品目录	通用二极管	
二极管配置	独立式	
正向压降(Vf)	1.1V@1A	
直流反向耐压(Vr)	1kV	
整流电流	1A	
反向电流(Ir)	5uA@1kV
封装：SMA(DO-214AC)
""",
     [("", "Model"),
      ("SMA(DO-214AC)", "Package"),
      ("通用二极管", "Type"),
      ("1kV", "Voltage"),
      ("", "Cap"),
      ("", "Precision"),
      ("", "Resistance"),
      ("", "Watt"),
      ("", "Inductance"),
      ("1A", "Electricity"),
      ]
     ),
    ("""
M7
正向压降(Vf):1.1V@1A
类目:通用二极管
品牌:Slkor(萨科微)
直流反向耐压(:1kV
编号:C426571
封装:SMA(DO-214AC)
整流电流:1A
详细:数据手册
反向电流(lr):5uA@1kV
""",
     [("Slkor", "Model"),
      ("SMA(DO-214AC)", "Package"),
      ("通用二极管", "Type"),
      ("1kV", "Voltage"),
      ("", "Cap"),
      ("", "Precision"),
      ("", "Resistance"),
      ("", "Watt"),
      ("", "Inductance"),
      ("1A", "Electricity"),
      ]
     ),
    ("""
商品目录
静电和浪涌保护(TVS/ESD)
极性
双向
反向截止电压(Vrwm)
3.3V
最大钳位电压
11.5V
峰值脉冲电流(lpp)@10/1000us
2A
击穿电压
5V
通道数
单路
工作温度
-55℃~+150C@(Tj)
类型
ESD
封装：SOD-923
""",
     [("", "Model"),
      ("SOD-923", "Package"),
      ("静电和浪涌保护(TVS/ESD)", "Type"),
      ("3.3V", "Voltage"),
      ("", "Cap"),
      ("", "Precision"),
      ("", "Resistance"),
      ("", "Watt"),
      ("", "Inductance"),
      ("2A", "Electricity"),
      ]
     ),
    ("""
商品目录
静电和浪涌保护(TVS/ESD)
极性
双向
反向截止电压(Vrwm)
5V
最大钳位电压
50V
类型
ESD封装：0603
""",
     [("", "Model"),
      ("0603", "Package"),
      ("静电和浪涌保护(TVS/ESD)", "Type"),
      ("5V", "Voltage"),
      ("", "Cap"),
      ("", "Precision"),
      ("", "Resistance"),
      ("", "Watt"),
      ("", "Inductance"),
      ("", "Electricity"),
      ]
     ),
    ("""
H5VL10B
极性:双向
类目:静电和浪涌保护(TVS/ESD)
品牌:宏迦橙
反向截止电压(:5V
编号:C7420372
封装:DFN1006-2L
最大钳位电压:10V
详细:数据手册
描述:VC:10V@5A，Cj_Typ:15pF...
峰值脉冲电流(l:5A
""",
     [("宏迦橙", "Model"),
      ("DFN1006-2L", "Package"),
      ("静电和浪涌保护(TVS/ESD)", "Type"),
      ("5V", "Voltage"),
      ("", "Cap"),
      ("", "Precision"),
      ("", "Resistance"),
      ("", "Watt"),
      ("", "Inductance"),
      ("5A", "Electricity"),
      ]
     ),
    ("""
商品目录	静电和浪涌保护(TVS/ESD)	
反向截止电压(Vrwm)	5.8V	
最大钳位电压	10.5V	
峰值脉冲电流(Ipp)@10/1000us	58.1A	
峰值脉冲功率(Ppp)@10/1000us	600W	
击穿电压	6.45V	
类型	TVS
封装：SMB(DO-214AA)
""",
     [("", "Model"),
      ("SMB(DO-214AA)", "Package"),
      ("静电和浪涌保护(TVS/ESD)", "Type"),
      ("5.8V", "Voltage"),
      ("", "Cap"),
      ("", "Precision"),
      ("", "Resistance"),
      ("", "Watt"),
      ("", "Inductance"),
      ("58.1A", "Electricity"),
      ]
     ),
    ("""
2N7002
品牌:CJ(江苏长电/长晶)
封装:SOT-23
描述:N沟道,60V,0.115A,7Ω@10V
类型:1个N沟道
漏源电压(Vdss):60V
连续漏极电流(Id):115mA
功率(Pd):200mW
类目:场效应管(MOSFET)
编号:C8545
详细:数据手册
""",
     [("CJ(江苏长电/长晶)", "Model"),
      ("SOT-23", "Package"),
      ("N沟道", "Type"),
      ("60V", "Voltage"),
      ("", "Cap"),
      ("", "Precision"),
      ("", "Resistance"),
      ("200mW", "Watt"),
      ("", "Inductance"),
      ("115mA", "Electricity"),
      ]
     ),
    ("""
AO3401A
品牌:AOS
封装:SOT-23
描述:P沟道,-30V,-4A,50mΩ@-10V
类型:1个P沟道
漏源电压(Vdss):30V
连续漏极电流(Id):4A
功率(Pd):1.4W
类目:场效应管(MOSFET)
编号:C15127
详细:数据手册
""",
     [("AOS", "Model"),
      ("SOT-23", "Package"),
      ("P沟道", "Type"),
      ("30V", "Voltage"),
      ("", "Cap"),
      ("", "Precision"),
      ("", "Resistance"),
      ("1.4W", "Watt"),
      ("", "Inductance"),
      ("4A", "Electricity"),
      ]
     ),
    ("""
AO3400A
品牌:UMW(友台半导体)
封装:SOT-23
描述:-
类型:1个N沟道
漏源电压(Vdss):30V
连续漏极电流(Id):5.8A
功率(Pd):1.4W
类目:场效应管(MOSFET)
编号:C347475
详细:数据手册
""",
     [("UMW(友台半导体)", "Model"),
      ("SOT-23", "Package"),
      ("N沟道", "Type"),
      ("30V", "Voltage"),
      ("", "Cap"),
      ("", "Precision"),
      ("", "Resistance"),
      ("1.4W", "Watt"),
      ("", "Inductance"),
      ("5.8A", "Electricity"),
      ]
     ),
    ("""
商品目录	场效应管(MOSFET)	
类型	1个N沟道	
漏源电压(Vdss)	30V	
连续漏极电流(Id)	5.7A	
功率(Pd)	1.4W	
导通电阻(RDS(on)@Vgs,Id)	26.5mΩ@10V,5.7A	
阈值电压(Vgs(th)@Id)	1.5V@250uA	
栅极电荷(Qg@Vgs)	7nC@4.5V	
输入电容(Ciss@Vds)	630pF@15V	
工作温度	-55℃~+150℃@(Tj)
封装：SOT-23-3L
""",
     [("", "Model"),
      ("SOT-23-3L", "Package"),
      ("场效应管(MOSFET)", "Type"),
      ("30V", "Voltage"),
      ("", "Cap"),
      ("", "Precision"),
      ("", "Resistance"),
      ("1.4W", "Watt"),
      ("", "Inductance"),
      ("5.7A", "Electricity"),
      ]
     ),
    ("""
SI2301-ZE
类型:1个P沟道
类目:场效应管(MOSFET).
品牌:HXYMOSFET(华轩阳电子)
漏源电压(Vdss):20V
编号:C5261052
封装:SOT-23
连续漏极电流(1:2.3A
详细:数据手册
描述:这款消费级P沟道MOSFET...
功率(Pd):700mW
""",
     [("HXYMOSFET(华轩阳电子)", "Model"),
      ("SOT-23", "Package"),
      ("P沟道", "Type"),
      ("20V", "Voltage"),
      ("", "Cap"),
      ("", "Precision"),
      ("", "Resistance"),
      ("700mW", "Watt"),
      ("", "Inductance"),
      ("2.3A", "Electricity"),
      ]
     ),
    ("""
类型:1个N沟道
类目:场效应管(MOSFET)
品牌:晶扬电子
漏源电压(Vdss):60V
编号:C3038094
封装:SOT-23
连续漏极电流(l:300mA
详细:数据手册
描述:MOSFET，小信号，SOT-23
阈值电压(Vgs(t1.2V
""",
     [("晶扬电子", "Model"),
      ("SOT-23", "Package"),
      ("N沟道", "Type"),
      ("60V", "Voltage"),
      ("", "Cap"),
      ("", "Precision"),
      ("", "Resistance"),
      ("", "Watt"),
      ("", "Inductance"),
      ("300mA", "Electricity"),
      ]
     ),
    ("""
CJ3401
类型:1个P沟道
类目:场效应管(MOSFET).
品牌:CJ(江苏长电/长晶)
漏源电压(Vdss):30V
编号:C13799
封装:SOT-23
连续漏极电流(1:4.2A
详细:数据手册
描述:P沟道,-30V,-4.2A,65mΩ@...
功率(Pd):350mW
""",
     [("CJ(江苏长电/长晶)", "Model"),
      ("SOT-23", "Package"),
      ("P沟道", "Type"),
      ("30V", "Voltage"),
      ("", "Cap"),
      ("", "Precision"),
      ("", "Resistance"),
      ("350mW", "Watt"),
      ("", "Inductance"),
      ("4.2A", "Electricity"),
      ]
     ),
    ("""
AO3401
品牌:Hottech(合科泰)
封装:SOT-23
类型:1个P沟道
漏源电压(Vdss):30V
连续漏极电流(Id):4.2A
功率(Pd):350mW
类目:场效应管(MOSFET)
编号:C181091
详细:数据手册
""",
     [("Hottech(合科泰)", "Model"),
      ("SOT-23", "Package"),
      ("P沟道", "Type"),
      ("30V", "Voltage"),
      ("", "Cap"),
      ("", "Precision"),
      ("", "Resistance"),
      ("350mW", "Watt"),
      ("", "Inductance"),
      ("4.2A", "Electricity"),
      ]
     ),
    ("""
SS8050(RANGE:200-350)
品牌:CJ(江苏长电/长晶)
封装:SOT-23
描述:丝印Y1
Type:NPN
集电极电流(Ic):1.5A
集射极击穿电压(Vceo):25V
功率(Pd):300mW
类目:三极管(BJT)
编号:C2150
详细:数据手册
""",
     [("CJ(江苏长电/长晶)", "Model"),
      ("SOT-23", "Package"),
      ("NPN", "Type"),
      ("25V", "Voltage"),
      ("", "Cap"),
      ("", "Precision"),
      ("", "Resistance"),
      ("300mW", "Watt"),
      ("", "Inductance"),
      ("1.5A", "Electricity"),
      ]
     ),
    ("""
MMBT3904(RANGE:100-300)
品牌:CJ(江苏长电/长晶)
封装:SOT-23
描述:丝印1A
Type:NPN
集电极电流(Ic):200mA
集射极击穿电压(Vceo):40V
功率(Pd):200mW
类目:三极管(BJT)
编号:C20526
详细:数据手册
""",
     [("CJ(江苏长电/长晶)", "Model"),
      ("SOT-23", "Package"),
      ("NPN", "Type"),
      ("40V", "Voltage"),
      ("", "Cap"),
      ("", "Precision"),
      ("", "Resistance"),
      ("200mW", "Watt"),
      ("", "Inductance"),
      ("200mA", "Electricity"),
      ]
     ),
    ("""
MMBTA56R100001
Type:PNP
类目:三极管(BJT)
品牌:PANJIT(强茂)
集电极电流(Ic):500mA
编号:C263320
封装:SOT-23
集射极击穿电压:80V
详细:数据手册
功率(Pd):225mW
""",
     [("PANJIT(强茂)", "Model"),
      ("SOT-23", "Package"),
      ("PNP", "Type"),
      ("80V", "Voltage"),
      ("", "Cap"),
      ("", "Precision"),
      ("", "Resistance"),
      ("225mW", "Watt"),
      ("", "Inductance"),
      ("500mA", "Electricity"),
      ]
     ),
    ("""
2N3055
品牌:JSMSEMI(杰盛微)
封装:TO-3
Type:NPN
集电极电流(Ic):15A
集射极击穿电压(Vceo):60V
功率(Pd):115W
类目:三极管(BJT)
编号:C2848354
""",
     [("JSMSEMI(杰盛微)", "Model"),
      ("TO-3", "Package"),
      ("NPN", "Type"),
      ("60V", "Voltage"),
      ("", "Cap"),
      ("", "Precision"),
      ("", "Resistance"),
      ("115W", "Watt"),
      ("", "Inductance"),
      ("15A", "Electricity"),
      ]
     ),
    ("工业级插件电容器16V2200μF±5%ECA-1HM2R2100只",
     [("ECA-1HM2R2", "Model"),
      ("", "Package"),
      ("插件电容器", "Type"),
      ("16V", "Voltage"),
      ("2200μF", "Cap"),
      ("5%", "Precision"),
      ("", "Resistance"),
      ("", "Watt"),
      ("", "Inductance"),
      ("", "Electricity"),
      ]),
    ("高性能1210贴片二极管1A20V1N4148W-7-F100只",
     [("1N4148W-7-F", "Model"),
      ("1210", "Package"),
      ("贴片二极管", "Type"),
      ("20V", "Voltage"),
      ("1A", "Electricity"),
      ("", "Cap"),
      ("", "Inductance"),
      ("", "Precision"),
      ("", "Resistance"),
      ("", "Watt"),
      ]),
    ("专业级2512贴片电感10μH±5%2512L100MX-T50只",
     [("2512L100MX-T", "Model"),
      ("2512", "Package"),
      ("贴片电感", "Type"),
      ("", "Voltage"),
      ("10μH", "Inductance"),
      ("5%", "Precision"),
      ("", "Cap"),
      ("", "Resistance"),
      ("", "Watt"),
      ("", "Electricity"),
      ]),
    ("高品质104贴片电容50V1μF±20%CERAMICDISC1005X7R1M10D50只",
     [("CERAMICDISC1005X7R1M10D", "Model"),
      ("104", "Package"),
      ("贴片电容", "Type"),
      ("50V", "Voltage"),
      ("1μF", "Cap"),
      ("20%", "Precision"),
      ("", "Resistance"),
      ("", "Watt"),
      ("", "Inductance"),
      ("", "Electricity"),
      ]),
    ("原装正品0805贴片电阻1/8W1KΩ±5%0603CRD1002J1K100只",
     [("0603CRD1002J1K", "Model"),
      ("0805", "Package"),
      ("贴片电阻", "Type"),
      ("1/8W", "Watt"),
      ("1KΩ", "Resistance"),
      ("5%", "Precision"),
      ("", "Voltage"),
      ("", "Cap"),
      ("", "Inductance"),
      ("", "Electricity"),
      ]),
    ("原装正品0805贴片电容10nF标字10425V精度10%（300只）",
     [("", "Model"),
      ("0805", "Package"),
      ("贴片电容", "Type"),
      ("25V", "Voltage"),
      ("10nF", "Cap"),
      ("10%", "Precision"),
      ("", "Resistance"),
      ("", "Watt"),
      ("", "Inductance"),
      ("", "Electricity"),
      ]),
    ("原装正品1206贴片二极管20mA标字D140V精度±1%（500只）",
     [("", "Model"),
      ("1206", "Package"),
      ("贴片二极管", "Type"),
      ("40V", "Voltage"),
      ("", "Cap"),
      ("±1%", "Precision"),
      ("", "Resistance"),
      ("20mA", "Electricity"),
      ("", "Watt"),
      ("", "Inductance"),
      ]),
    ("原装正品2512贴片电感22μH标字L221A精度3%（200只）",
     [("", "Model"),
      ("2512", "Package"),
      ("贴片电感", "Type"),
      ("", "Voltage"),
      ("22μH", "Inductance"),
      ("3%", "Precision"),
      ("", "Resistance"),
      ("1A", "Electricity"),
      ("", "Watt"),
      ("", "Cap"),
      ]),
    ("原装正品0402贴片稳压二极管20V标字ZD精度±2%（100只）",
     [("", "Model"),
      ("0402", "Package"),
      ("贴片稳压二极管", "Type"),
      ("20V", "Voltage"),
      ("", "Cap"),
      ("±2%", "Precision"),
      ("", "Resistance"),
      ("", "Watt"),
      ("", "Inductance"),
      ("", "Electricity"),
      ]),
    ("原装正品1210贴片MOSFET30V标字N30精度±5%（400只）",
     [("", "Model"),
      ("1210", "Package"),
      ("贴片MOSFET", "Type"),
      ("30V", "Voltage"),
      ("", "Cap"),
      ("±5%", "Precision"),
      ("", "Resistance"),
      ("", "Watt"),
      ("", "Inductance"),
      ("", "Electricity"),
      ]),
    ("原装正品0805贴片电容47PF47皮法50V精度±5%（100只）",
     [("", "Model"),
      ("0805", "Package"),
      ("贴片电容", "Type"),
      ("50V", "Voltage"),
      ("47PF", "Cap"),
      ("5%", "Precision"),
      ("", "Resistance"),
      ("", "Watt"),
      ("", "Inductance"),
      ("", "Electricity"),
      ]),
    ("原装正品1206贴片电感100UH100微亨1A精度±2%（200只）",
     [("", "Model"),
      ("1206", "Package"),
      ("贴片电感", "Type"),
      ("", "Voltage"),
      ("100UH", "Inductance"),
      ("2%", "Precision"),
      ("", "Resistance"),
      ("1A", "Electricity"),
      ("", "Watt"),
      ("", "Cap"),
      ]),
    ("原装正品0402贴片二极管1N414820V精度±3%（300只）",
     [("1N4148", "Model"),
      ("0402", "Package"),
      ("贴片二极管", "Type"),
      ("20V", "Voltage"),
      ("", "Cap"),
      ("3%", "Precision"),
      ("", "Resistance"),
      ("", "Watt"),
      ("", "Inductance"),
      ("", "Electricity"),
      ]),
    ("原装正品1210贴片MOSFETIRFZ44N30V精度±5%（75只）",
     [("IRFZ44N", "Model"),
      ("1210", "Package"),
      ("贴片MOSFET", "Type"),
      ("30V", "Voltage"),
      ("", "Cap"),
      ("5%", "Precision"),
      ("", "Resistance"),
      ("", "Watt"),
      ("", "Inductance"),
      ("", "Electricity"),
      ])

]

print("开始处理爬虫数据")

import os


def transform_data(input_data):
    # 提取Model中的信息并构造新字符串的前半部分
    model_info = input_data["Model"]
    voltage = input_data.get("Voltage", "")
    cap = input_data.get("Cap", "")
    type = input_data.get("Type", "")
    package = input_data.get("Package", "")
    precision = input_data.get("Precision", "")
    body = input_data.get("Body", "")

    # 插入到dataset中
    data.append((body+model_info, [
        (model_info, "Model"),
        (package, "Package"),
        (type, "Type"),
        (voltage, "Voltage"),
        (cap, "Cap"),
        (precision, "Precision"),
        ("", "Resistance"),
        ("", "Watt"),
        ("", "Inductance"),
        ("", "Electricity"),
    ]))


def read_files_in_directory(directory_path):
    """
    遍历指定目录下的所有文件并打印其内容。

    :param directory_path: 要遍历的目录路径
    """
    # 确保给定的路径是一个目录
    if os.path.isdir(directory_path):
        # 遍历目录下的所有文件和子目录
        for item in os.listdir(directory_path):
            item_path = os.path.join(directory_path, item)

            # 检查是否为文件，避免进入子目录循环
            if os.path.isfile(item_path):
                print(f"正在读取文件: {item_path}")
                # 以文本模式打开文件并读取内容
                with open(item_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    data2 = json.loads(content)
                    for value in data2:
                        transform_data(value)
    else:
        print(f"{directory_path} 不是一个有效的目录路径。")


# 示例用法
directory_to_read = './data'  # 替换为你要遍历的目录路径
read_files_in_directory(directory_to_read)
