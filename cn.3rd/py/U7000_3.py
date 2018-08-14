from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U7000_3 ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U7000.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60210",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/U7000   ._SN',
            '',
            '',
            '',
            '',
            '',
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '',                                     # 8
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_AB",           # 01, 1
        "Function_2_AC",           # 02, 2
        "Function_3_1C92",         # 03, 3
        "Function_4_1CCF",         # 04, 4
        "Function_5_1D04",         # 05, 5
        "Function_6_1D25",         # 06, 6
        "Function_7_1D52",         # 07, 7
        "Function_8_1D81",         # 08, 8
        "Function_9_1DBE",         # 09, 9
        "Function_10_4633",        # 0A, 10
        "Function_11_4C62",        # 0B, 11
        "Function_12_70A4",        # 0C, 12
        "Function_13_76E5",        # 0D, 13
        "Function_14_C29B",        # 0E, 14
        "Function_15_C2DC",        # 0F, 15
        "Function_16_C2FF",        # 10, 16
        "Function_17_C332",        # 11, 17
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Return()

    # Function_0_AA end

    def Function_1_AB(): pass

    label("Function_1_AB")

    Return()

    # Function_1_AB end

    def Function_2_AC(): pass

    label("Function_2_AC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D2(0x2600DF, 0x2600E4, 0x13)
    OP_D2(0x270009, 0x27000D, 0x14)
    OP_D2(0x2602CB, 0x2602D0, 0x15)
    OP_D2(0x270088, 0x27008C, 0x16)
    OP_D2(0x260022, 0x260027, 0x17)
    OP_D2(0x2700F8, 0x2700FC, 0x18)
    OP_D2(0x2700F9, 0x2700FD, 0x19)
    LoadEffect(0x1, "map\\mp253_00.eff")
    LoadEffect(0x2, "map\\mp253_01.eff")
    LoadEffect(0x3, "map\\mp253_02.eff")
    LoadEffect(0x4, "map\\mp253_03.eff")
    LoadEffect(0x5, "map\\mp253_05.eff")
    LoadEffect(0x6, "map\\mp253_04.eff")
    SetChrPos(0x102, -200, 4000, -2500, 0)
    SetChrPos(0x109, -4150, 4000, -1700, 45)
    ClearChrFlags(0x20, 0x80)
    SetChrPos(0x20, -3680, 4000, -2700, 45)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x11, -1610, 4000, -3410, 0)
    SetChrPos(0x12, -1720, 4000, -6550, 0)
    SetChrPos(0x13, -660, 4000, -7090, 0)
    SetChrPos(0x14, -2800, 4000, -4730, 0)
    SetChrPos(0x16, -1690, 4000, -4840, 0)
    SetChrPos(0x18, -470, 4000, -5410, 0)
    SetChrPos(0x19, 890, 4000, -6850, 0)
    SetChrPos(0x1A, -70, 4000, -3990, 0)
    SetChrPos(0x1B, 710, 4000, -5290, 0)
    SetChrPos(0x1C, -2890, 4000, -6150, 0)
    SetChrFlags(0xF0, 0x80)
    SetChrFlags(0xF1, 0x80)
    OP_6D(1220, 4000, -590, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(2270, 0)
    OP_6C(45000, 0)
    OP_6E(392, 0)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_2DB():
        OP_6D(1760, 4000, 3840, 2000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2DB)

    def lambda_2F3():
        OP_67(0, 5490, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2F3)

    def lambda_30B():
        OP_6B(2400, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_30B)

    def lambda_31B():
        OP_6E(403, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_31B)
    OP_8F(0x102, 0x0, 0xFA0, 0xFFFFFE16, 0x3E8, 0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x102, 21)
    SetChrSubChip(0x102, 0)
    OP_22(0x8F, 0x0, 0x64)
    Sleep(100)
    ClearChrFlags(0x1D, 0x80)
    OP_9F(0x1D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x1D, 19)
    SetChrSubChip(0x1D, 0)
    SetChrFlags(0x1D, 0x40)
    SetChrFlags(0x1D, 0x4)
    SetChrPos(0x1D, 100, 5300, 0, 0)
    PlayEffect(0x1, 0x0, 0x1D, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x1D, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)
    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    OP_E5(0x2, 0xFF, 0x13, 1000)
    OP_0D()
    Fade(1000)
    OP_E5(0x2, 0xFF, 0x13, 700)
    OP_0D()

    def lambda_428():
        OP_8F(0xFE, 0x64, 0x1770, 0x64, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_428)
    WaitChrThread(0x1D, 0x0)
    Sleep(300)
    Fade(1000)
    OP_6D(0, 5000, 3260, 0)
    OP_67(0, 3980, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(0, 0)
    OP_6E(363, 0)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    SetChrPos(0x1D, 0, 6000, 1000, 0)
    SetChrPos(0x11, -1010, 4000, -3410, 0)
    SetChrPos(0x12, -1120, 4000, -6550, 0)
    SetChrPos(0x13, -60, 4000, -7090, 0)
    SetChrPos(0x14, -2100, 4000, -4730, 0)
    SetChrPos(0x16, -800, 4000, -4840, 0)
    SetChrPos(0x18, 300, 4000, -5410, 0)
    SetChrPos(0x19, 1490, 4000, -6850, 0)
    SetChrPos(0x1A, 530, 4000, -3990, 0)
    SetChrPos(0x1B, 1310, 4000, -5290, 0)
    SetChrPos(0x1C, -2290, 4000, -6150, 0)

    def lambda_554():
        OP_6D(0, 7500, 3760, 3500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_554)

    def lambda_56C():
        OP_67(0, 1650, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_56C)

    def lambda_584():
        OP_6B(2700, 3500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_584)

    def lambda_594():
        OP_6E(363, 3500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_594)

    def lambda_5A4():
        OP_8F(0xFE, 0x0, 0x2134, 0xAF0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_5A4)
    WaitChrThread(0x1D, 0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    def lambda_5CE():
        OP_6B(2000, 8000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_5CE)
    OP_22(0x147, 0x0, 0x64)
    PlayEffect(0x5, 0x2, 0x1D, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    OP_23(0x147)
    Fade(500)
    OP_22(0xC, 0x0, 0x64)
    PlayEffect(0x3, 0x2, 0x1D, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x0)
    Sleep(300)
    PlayEffect(0x6, 0x3, 0x1D, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    Sleep(3000)
    Fade(500)
    OP_6D(1090, 5000, 1260, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(45000, 0)
    OP_6E(365, 0)
    SetChrPos(0x102, -400, 4000, -1200, 0)
    SetChrPos(0x1D, 390, 8000, 2150, 180)
    PlayEffect(0x6, 0x1, 0x1D, -300, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x3, 0x0)
    ClearChrFlags(0x10, 0x80)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10, -390, 3400, 1800, 180)
    SetChrPos(0x11, -1610, 4000, -3410, 0)
    SetChrPos(0x12, -2200, 4000, -6550, 0)
    SetChrPos(0x13, -1160, 4000, -7090, 0)
    SetChrPos(0x14, -2800, 4000, -4800, 0)
    SetChrPos(0x16, -1500, 4000, -4640, 0)
    SetChrPos(0x18, -650, 4000, -5410, 0)
    SetChrPos(0x19, 300, 4000, -6850, 0)
    SetChrPos(0x1A, -200, 4000, -3800, 0)
    SetChrPos(0x1B, 500, 4000, -5290, 0)
    SetChrPos(0x1C, -3300, 4000, -6150, 0)
    OP_E5(0x2, 0xFF, 0x13, 500)

    def lambda_815():
        OP_6D(620, 4000, 820, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_815)

    def lambda_82D():
        OP_67(300, 4350, -10300, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_82D)

    def lambda_845():
        OP_6B(3220, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_845)

    def lambda_855():
        OP_6E(322, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_855)

    def lambda_865():
        OP_8F(0xFE, 0xFFFFFE7A, 0xFA0, 0x866, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_865)
    WaitChrThread(0x1D, 0x0)
    SetChrSubChip(0x1D, 0)
    SetChrFlags(0x1D, 0x2)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    Fade(1000)
    PlayEffect(0x6, 0x1, 0x1D, -300, 300, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)

    def lambda_8D3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_8D3)
    OP_22(0x99, 0x0, 0x64)
    Sleep(1500)
    OP_82(0x0, 0x0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #0
        0x11,
        "#067F#6P哇……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x16,
        "#1168F#6P……艾丝蒂尔……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    PlayEffect(0x4, 0x4, 0x1D, -300, 300, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_22(0x138, 0x0, 0x64)
    OP_23(0x146)

    def lambda_97D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_97D)
    OP_82(0x2, 0x2)
    WaitChrThread(0x1D, 0x0)
    Fade(500)
    OP_82(0x1, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #2
        0x1D,
        "#1007F#5P怎、怎么了刚才……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x102,
        "#1501F#12P艾丝蒂尔……\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Sleep(150)
    Fade(250)
    SetChrSubChip(0x1D, 7)
    OP_0D()
    Sleep(300)

    ChrTalk(    #4
        0x1D,
        (
            "#1005F#5P约修亚，你没事吧！？\x02\x03",

            "刚才的光到底是──\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #5
        0x1D,
        "#1004F#5P咦……\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x1D, 15)
    SetChrSubChip(0x1D, 0)
    ClearChrFlags(0x1D, 0x2)
    OP_0D()
    Sleep(300)
    OP_62(0x1D, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)

    ChrTalk(    #6
        0x102,
        (
            "#1512F#12P嗯，那个……\x01",
            "你会感到奇怪也是理所当然的。\x02\x03",

            "#1514F不管怎么说，\x01",
            "这都是难以置信的情况呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1D)
    Sleep(500)

    ChrTalk(    #7
        0x1D,
        "#1019F#5P难、难以置信……\x02",
    )

    CloseMessageWindow()

    def lambda_B71():
        OP_6D(1190, 4000, 1200, 2500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B71)

    def lambda_B89():
        OP_67(300, 4330, -10300, 2500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B89)

    def lambda_BA1():
        OP_6B(3300, 2500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_BA1)

    def lambda_BB1():
        OP_6E(290, 2500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_BB1)
    OP_43(0x102, 0x0, 0x3, 0x7)
    Sleep(600)

    def lambda_BCD():
        OP_8F(0xFE, 0xFFFFF95C, 0xFA0, 0xFFFFFA4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_BCD)
    Sleep(50)

    def lambda_BED():
        OP_8F(0xFE, 0xFFFFFC36, 0xFA0, 0xFFFFF7EA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_BED)
    Sleep(100)

    def lambda_C0D():
        OP_8F(0xFE, 0x122, 0xFA0, 0xFFFFF8D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_C0D)
    Sleep(50)

    def lambda_C2D():
        OP_8F(0xFE, 0x3C, 0xFA0, 0xFFFFF380, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_C2D)
    Sleep(50)

    def lambda_C4D():
        OP_8F(0xFE, 0xFFFFFA06, 0xFA0, 0xFFFFF240, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_C4D)
    Sleep(50)

    def lambda_C6D():
        OP_8F(0xFE, 0xFFFFF31C, 0xFA0, 0xFFFFED04, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_C6D)
    Sleep(50)

    def lambda_C8D():
        OP_8F(0xFE, 0xFFFFF51A, 0xFA0, 0xFFFFF20E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_C8D)

    def lambda_CA8():
        OP_8F(0xFE, 0xFFFFF768, 0xFA0, 0xFFFFECDC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_CA8)
    Sleep(50)

    def lambda_CC8():
        OP_8F(0xFE, 0xFFFFFB50, 0xFA0, 0xFFFFEAF2, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_CC8)

    def lambda_CE3():
        OP_8F(0xFE, 0xFFFFFF9C, 0xFA0, 0xFFFFEDA4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_CE3)
    Sleep(1500)
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #8
        0x11,
        "#066F#6P艾丝蒂尔姐姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x16,
        "#1168F#6P……好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x1D,
        (
            "#1008F#5P提妲、科洛丝……\x02\x03",

            "#1016F啊哈哈……\x01",
            "我快感动得流泪了……\x02\x03",

            "#1017F而、而且竟然有\x01",
            "这么多令人怀念的面孔……\x02\x03",

            "#1008F哇，奥利维尔……\x01",
            "你这打扮还真像个皇子啊！？\x02\x03",

            "还、还有雪拉姐……\x01",
            "什么时候把头发剪短的！？\x02\x03",

            "还穿着这么性感的衣服……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x1B,
        "#1536F#12P呵呵，不错吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x18,
        (
            "#1541F#6P呼，我倒觉得\x01",
            "之前那身白色的外套\x01",
            "比较能让人心情舒畅呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x1D,
        (
            "#1017F#5P哎……我正想说呢，\x01",
            "不是也有些人一点也没变嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x1C,
        "#051F#6P那还真是不好意思了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x19,
        (
            "#071F#12P哈哈……\x01",
            "这可算是我的工作服了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x1A,
        (
            "#811F#6P呵呵……\x01",
            "艾丝蒂尔，好久不见！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x14,
        (
            "#413F#6P真是的，你还是和\x01",
            "以前一样没大脑呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x1D,
        (
            "#1004F#5P亚妮拉丝……\x01",
            "连乔丝特也在……\x02\x03",

            "#1022F等一下，我说你啊。\x02\x01",

            "#1019F总说没大脑、没大脑的，\x01",
            "还有完没完！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x14,
        (
            "#210F#6P哼～你就是那个样子，\x01",
            "又有什么办法。\x02\x03",

            "#211F反正还不是一直在给\x01",
            "约修亚添麻烦吗～？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1D, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #20
        0x1D,
        (
            "#1013F#5P那、那种事……\x01",
            "倒是偶尔也有吧……\x02\x03",

            "#1022F──哎呀，\x01",
            "都说不是这个问题啦！\x02\x03",

            "#1008F怎么连尤莉亚小姐\x01",
            "和穆拉先生也在呢！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x12,
        (
            "#171F#6P呵呵……\x01",
            "很久不见了，艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x13,
        "#277F#12P久疏问候。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x1D,
        "#1016F#5P哎呀，到底怎么回事……\x02",
    )

    CloseMessageWindow()
    OP_62(0x1D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1222():
        OP_6D(120, 4000, 1980, 1000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1222)

    def lambda_123A():
        OP_6C(40000, 1000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_123A)
    OP_8C(0x1D, 225, 400)
    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #24
        0x109,
        "#1066F#6P#40W哈哈……好久不见。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x1D,
        (
            "#1008F#5P凯文先生……！？\x02\x03",

            "#1004F还有……\x01",
            "那个，这位是？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x20,
        (
            "#1446F#6P……我是星杯骑士团的随从骑士，\x01",
            "我叫莉丝·亚尔珍特。\x02\x03",

            "#1448F关于你的事情，\x01",
            "我从凯文和大家那里了解过不少。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x1D,
        (
            "#1011F#5P啊，是这样啊……\x02\x01",

            "#1001F嗯，初次见面，请多关照。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x109,
        (
            "#1075F#6P#40W怎么说呢……\x01",
            "不愧是艾丝蒂尔啊……\x02\x03",

            "#1840F……你一出现……\x01",
            "气氛立刻就变得活跃起来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x1D,
        (
            "#1016F#5P是、是这样吗？\x02\x03",

            "#1015F……等一下……\x01",
            "凯文先生，你怎么了？\x02\x03",

            "脸色好像很难看……\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)

    ChrTalk(    #30
        0x20,
        "#1444F#6P咦……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x20, 0, 400)
    OP_9E(0x109, 0xF, 0x0, 0x12C, 0xBB8)

    ChrTalk(    #31
        0x109,
        "#1070F#5P#40W呜……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(-4950, 4000, -1390, 0)
    OP_67(300, 5050, -10300, 0)
    OP_6B(2900, 0)
    OP_6C(240000, 0)
    OP_6E(298, 0)

    def lambda_152F():
        OP_6B(2800, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_152F)
    SetChrPos(0x109, -4610, 4000, -450, 90)
    SetChrPos(0x20, -4230, 4000, -1620, 45)
    SetChrPos(0x102, 1770, 4000, -230, 270)
    SetChrPos(0x1D, -310, 4000, 1740, 225)
    SetChrPos(0x11, -1560, 4000, -1310, 0)
    SetChrPos(0x12, -2060, 4000, -4990, 0)
    SetChrPos(0x13, -900, 4000, -5280, 0)
    SetChrPos(0x14, -2390, 4000, -2970, 0)
    SetChrPos(0x16, -730, 4000, -1900, 0)
    SetChrPos(0x18, -1200, 4000, -3400, 0)
    SetChrPos(0x19, 600, 4000, -4410, 0)
    SetChrPos(0x1A, 410, 4000, -1930, 0)
    SetChrPos(0x1B, 220, 4000, -3230, 0)
    SetChrPos(0x1C, -3100, 4000, -4680, 0)
    SetChrChipByIndex(0x109, 22)
    SetChrSubChip(0x109, 0)
    OP_43(0x109, 0x3, 0x3, 0x8)
    OP_22(0x20C, 0x0, 0x64)

    def lambda_1643():

        label("loc_1643")

        OP_8C(0x20, 0, 600)
        OP_48()
        Jump("loc_1643")

    QueueWorkItem2(0x20, 3, lambda_1643)
    Sleep(50)

    def lambda_1659():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1659)

    def lambda_1667():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_1667)
    Sleep(50)

    def lambda_167A():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x16, 3, lambda_167A)

    def lambda_1688():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x1B, 3, lambda_1688)
    Sleep(50)

    def lambda_169B():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_169B)

    def lambda_16A9():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_16A9)
    Sleep(50)

    def lambda_16BC():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_16BC)

    def lambda_16CA():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x18, 3, lambda_16CA)
    Sleep(50)

    def lambda_16DD():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_16DD)

    def lambda_16EB():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x19, 3, lambda_16EB)
    Sleep(50)

    def lambda_16FE():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x1C, 3, lambda_16FE)

    def lambda_170C():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_170C)
    OP_0D()
    Sleep(500)

    ChrTalk(    #32
        0x20,
        "#1802F#3S#5P！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_1D(0xB0)
    Fade(250)
    SetChrChipByIndex(0x20, 25)
    SetChrSubChip(0x20, 0)
    OP_0D()
    SetChrPos(0x10, -4030, 3800, -1420, 45)
    OP_62(0x10, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1500)

    ChrTalk(    #33
        0x109,
        (
            "#1076F#12P#50W抱歉，莉丝……\x01",
            "……刚才的事只能留到下次再说了……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #34
        "\x07\x05凯文把『方石』递给了莉丝。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(500)

    NpcTalk(    #35
        0x10,
        "莉丝",
        "#1444F#5P咦……\x02",
    )

    Jump("loc_1840")

    label("loc_1840")

    CloseMessageWindow()

    ChrTalk(    #36
        0x109,
        (
            "#1076F#12P#50W暂时……就交给你了……\x02\x03",

            "总之……\x01",
            "………现在先继续前进…………\x02",
        )
    )

    Jump("loc_18AB")

    label("loc_18AB")

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrPos(0x109, -3950, 4000, -500, 90)
    SetChrChipByIndex(0x109, 23)
    SetChrSubChip(0x109, 0)
    ClearChrFlags(0x109, 0x1)
    SetChrFlags(0x109, 0x800)
    OP_44(0x109, 0x3)
    OP_22(0x20C, 0x0, 0x64)
    OP_0D()
    Sleep(300)
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x19, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #37
        0x10,
        "莉丝",
        "#1449F#3S#5P凯文……！？\x02",
    )

    Jump("loc_1A67")

    label("loc_1A67")

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #38
        0x1D,
        "#1020F#6P凯、凯文先生！？\x02",
    )

    CloseMessageWindow()

    def lambda_1AA5():
        OP_6B(2700, 10000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1AA5)
    OP_43(0x1D, 0x1, 0x3, 0x5)
    OP_43(0x102, 0x3, 0x3, 0x4)
    WaitChrThread(0x20, 0x1)
    WaitChrThread(0x1D, 0x1)
    WaitChrThread(0x102, 0x1)
    Sleep(500)

    ChrTalk(    #39
        0x102,
        (
            "#1506F#6P唔……　\x01",
            "是刚才那个的反作用吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1D, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #40
        0x1D,
        (
            "#1026F#12P咦、咦……\x01",
            "到底是怎么回事啊！？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #41
        0x10,
        "莉丝",
        (
            "#1802F#5P……凯文……！\x02\x03",

            "凯文……振作一点……！\x02",
        )
    )

    Jump("loc_1BA2")

    label("loc_1BA2")

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_44(0x20, 0x0)
    Sleep(2000)
    OP_A2(0x2910)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BCD")
    OP_A2(0x265D)

    label("loc_1BCD")

    OP_AD(0x2400F0, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_A2(0x2582)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x159), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C4(0x0, 0x10)
    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        240,
        180,
        0,
        (
            "【保存】\x01",              # 0
            "【继续下面剧情】\x01",      # 1
        )
    )

    Jump("loc_1C35")

    label("loc_1C35")

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C49")
    ShowSaveMenu()

    label("loc_1C49")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_AE(0xC8)
    Sleep(2000)
    OP_20(0xBB8)
    OP_21()
    Sleep(2000)
    OP_C4(0x1, 0x10)
    OP_A3(0x2582)
    OP_4F(0x4, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x2506)
    NewScene("ED6_DT21/U7001   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_2_AC end

    def Function_3_1C92(): pass

    label("Function_3_1C92")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1CCE")
    OP_9E(0x109, 0xF, 0x0, 0x12C, 0x7D0)
    Sleep(1000)
    OP_9E(0x109, 0xF, 0x0, 0x12C, 0x7D0)
    Sleep(1500)
    Jump("Function_3_1C92")

    label("loc_1CCE")

    Return()

    # Function_3_1C92 end

    def Function_4_1CCF(): pass

    label("Function_4_1CCF")

    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0x3F2, 0xFA0, 0xFFFFFFCE, 0x1388, 0x0)
    OP_8C(0xFE, 270, 0)
    OP_8F(0xFE, 0xFFFFFA24, 0xFA0, 0x0, 0x1388, 0x0)
    Return()

    # Function_4_1CCF end

    def Function_5_1D04(): pass

    label("Function_5_1D04")

    SetChrFlags(0xFE, 0x40)
    OP_8F(0xFE, 0xFFFFF416, 0xFA0, 0x4E2, 0x1388, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_5_1D04 end

    def Function_6_1D25(): pass

    label("Function_6_1D25")

    SetChrFlags(0x20, 0x40)
    OP_62(0x20, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Fade(250)
    SetChrChipByIndex(0x20, 24)
    SetChrSubChip(0x20, 0)
    OP_0D()
    Sleep(300)
    Return()

    # Function_6_1D25 end

    def Function_7_1D52(): pass

    label("Function_7_1D52")


    def lambda_1D58():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1D58)
    Sleep(200)
    OP_8F(0xFE, 0x514, 0xFA0, 0xFFFFFE70, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_7_1D52 end

    def Function_8_1D81(): pass

    label("Function_8_1D81")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1DBD")
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1000)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1500)
    Jump("Function_8_1D81")

    label("loc_1DBD")

    Return()

    # Function_8_1D81 end

    def Function_9_1DBE(): pass

    label("Function_9_1DBE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0xEE, 0x80)
    SetChrFlags(0xEF, 0x80)
    SetChrFlags(0xF0, 0x80)
    SetChrFlags(0xF1, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x20, 1230, 4100, -14000, 0)
    SetChrPos(0x1D, 650, 4000, 1180, 180)
    SetChrPos(0x15, -500, 4000, 1230, 135)
    SetChrPos(0x16, 150, 4000, -870, 0)
    SetChrPos(0x11, 1450, 4000, -790, 0)
    SetChrPos(0x14, -850, 4000, -1290, 0)
    SetChrPos(0x1B, 2100, 4000, -2200, 0)
    SetChrPos(0x12, -200, 4000, -2750, 0)
    SetChrPos(0x1C, 3500, 4000, -2500, 315)
    SetChrPos(0x19, -90, 4000, -4240, 0)
    SetChrPos(0x1A, 2900, 4000, -950, 315)
    SetChrPos(0x18, 700, 4000, -2200, 0)
    SetChrPos(0x13, 1560, 4000, -3920, 0)
    OP_6D(-100, 4000, 100, 0)
    OP_67(0, 6210, -10000, 0)
    OP_6B(2050, 0)
    OP_6C(315000, 0)
    OP_6E(388, 0)
    OP_E5(0x2, 0xFF, 0x13, 500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #42
        0x1D,
        (
            "#1007F#11P是吗……\x01",
            "还有这样的事啊。\x02\x03",

            "#1015F总觉得，\x01",
            "这件事越听越让人难以相信呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x15,
        (
            "#1505F#5P嗯……\x01",
            "不过，\x01",
            "我们已经分析出来的线索也有不少。\x02\x03",

            "#1503F这个地方叫做『影之国』，\x01",
            "是根据不可思议的法则\x01",
            "所构成的世界……\x02\x03",

            "#1502F而且，我们以某种理由被选中，\x01",
            "从而被吸进这样的世界。\x02",
        )
    )

    Jump("loc_208F")

    label("loc_208F")

    CloseMessageWindow()

    ChrTalk(    #44
        0x18,
        (
            "#1540F#6P并且，在这基础之上，\x01",
            "我们也可以重新整理出几点疑问了。\x02\x03",

            "#1545F疑问之一。\x01",
            "『影之王』和『黑骑士』的真实身份是？\x02\x03",

            "疑问之二。\x01",
            "『方石』和『女性幽灵』的真实身份是？\x02\x03",

            "#1540F疑问之三。\x01",
            "『影之国』的由来和事件真相是？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x11,
        "#065F#6P没、没错……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x16,
        (
            "#1162F#6P虽然有数不清的疑问……\x01",
            "但大致还是可以\x01",
            "归入这三个问题之中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x19,
        (
            "#070F#6P嗯，不合理的魔物\x01",
            "会在这里出现的理由\x01",
            "也可以算作第三个。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x1D,
        (
            "#1006F#11P原来如此，\x01",
            "这样一来就能看清一些事情了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1D, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #49
        0x1D,
        (
            "#1004F#11P咦，可是……\x02\x03",

            "这和凯文先生晕倒\x01",
            "又有什么关系呢？\x02\x03",

            "#1015F听你们所说，\x01",
            "好像是和巨大的恶魔\x01",
            "战斗时产生的影响……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23A9")

    ChrTalk(    #50
        0x1C,
        (
            "#053F#6P把束缚我们的结界\x01",
            "冲破的那股力量……\x02\x03",

            "#555F还有同时出现的\x01",
            "红色纹章造型的光……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2782")

    label("loc_23A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_242B")

    ChrTalk(    #51
        0x11,
        (
            "#561F#6P把、把关住我们的结界\x01",
            "冲破的那股力量……\x02\x03",

            "#063F还有那个时候出现的\x01",
            "红色纹章造型的光……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2782")

    label("loc_242B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24A7")

    ChrTalk(    #52
        0x16,
        (
            "#1167F#6P把束缚我们的结界\x01",
            "冲破的那股力量……\x02\x03",

            "#1163F还有同时出现的\x01",
            "红色纹章造型的光……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2782")

    label("loc_24A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2521")

    ChrTalk(    #53
        0x12,
        (
            "#176F#6P把束缚我们的结界\x01",
            "冲破的那股力量……\x02\x03",

            "#178F还有同时出现的\x01",
            "红色纹章造型的光……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2782")

    label("loc_2521")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_259B")

    ChrTalk(    #54
        0x13,
        (
            "#272F#6P把束缚我们的结界\x01",
            "冲破的那股力量……\x02\x03",

            "#270F还有同时出现的\x01",
            "红色纹章造型的光……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2782")

    label("loc_259B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2615")

    ChrTalk(    #55
        0x1A,
        (
            "#817F#6P把关住我们的结界\x01",
            "冲破的那股力量……\x02\x03",

            "#813F还有同时出现的\x01",
            "红色纹章造型的光……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2782")

    label("loc_2615")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2691")

    ChrTalk(    #56
        0x1B,
        (
            "#1526F#6P把束缚我们的结界\x01",
            "冲破的那股力量……\x02\x03",

            "#1522F还有同时出现的\x01",
            "红色纹章造型的光……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2782")

    label("loc_2691")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_270B")

    ChrTalk(    #57
        0x14,
        (
            "#416F#6P把束缚我们的结界\x01",
            "冲破的那股力量……\x02\x03",

            "#212F还有同时出现的\x01",
            "红色纹章造型的光……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2782")

    label("loc_270B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2782")

    ChrTalk(    #58
        0x19,
        (
            "#074F#6P把束缚我们的结界\x01",
            "冲破的那股力量……\x02\x03",

            "#072F还有同时出现的\x01",
            "红色纹章造型的光……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2782")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2804")

    ChrTalk(    #59
        0x18,
        (
            "#1544F#6P嗯，就算是我本人\x01",
            "也想不出怎么解释呢。\x02\x03",

            "#1542F也许是七耀教会\x01",
            "流传的法术一类的东西……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29FE")

    label("loc_2804")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2843")

    ChrTalk(    #60
        0x19,
        (
            "#072F#6P唔……\x01",
            "那个到底是什么啊？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29FE")

    label("loc_2843")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2884")

    ChrTalk(    #61
        0x14,
        (
            "#212F#6P那个……\x01",
            "到底是什么东西啊？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29FE")

    label("loc_2884")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28C2")

    ChrTalk(    #62
        0x1B,
        (
            "#1522F#6P那个……\x01",
            "到底是什么呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29FE")

    label("loc_28C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2901")

    ChrTalk(    #63
        0x1A,
        (
            "#812F#6P那个……\x01",
            "到底会是什么呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29FE")

    label("loc_2901")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_293D")

    ChrTalk(    #64
        0x13,
        "#270F#6P……那个究竟是什么呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_29FE")

    label("loc_293D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_297E")

    ChrTalk(    #65
        0x12,
        (
            "#178F#6P那个……\x01",
            "到底是什么东西啊？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29FE")

    label("loc_297E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29C0")

    ChrTalk(    #66
        0x16,
        (
            "#1163F#6P那个……\x01",
            "到底是什么东西呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29FE")

    label("loc_29C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29FE")

    ChrTalk(    #67
        0x11,
        (
            "#063F#6P那个……\x01",
            "到底是什么东西呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A7D")

    ChrTalk(    #68
        0x18,
        (
            "#1544F#6P嗯，就算是我本人\x01",
            "也想不出怎么解释呢。\x02\x03",

            "#1542F也许是七耀教会\x01",
            "流传的法术一类的东西……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A7D")


    ChrTalk(    #69
        0x15,
        "#1503F#5P……………………………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0x1D, 270, 400)
    Sleep(300)

    ChrTalk(    #70
        0x1D,
        (
            "#1004F#12P……约修亚？\x02\x03",

            "#1002F你想到什么了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x15,
        (
            "#1505F#5P嗯……有点吧。\x02\x03",

            "#1503F虽然我还无法确信……\x01",
            "但我想那个应该是『圣痕』。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x19, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #72
        0x1D,
        "#1020F#12P咦……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x14,
        (
            "#214F#6P那个……\x01",
            "是约修亚肩膀上的东西！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x15,
        (
            "#1503F#5P嗯……\x02\x03",

            "#1505F那是教授为了控制我\x01",
            "而埋在深层意识中的印象\x01",
            "在肉体上的表现。\x02\x03",

            "凯文先生的那个也是一样……\x02\x03",

            "#1502F但比起我的圣痕来，\x01",
            "那个的力量要强大得多。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #75
        0x20,
        "女孩的声音",
        "#2P……你注意到了啊。\x02",
    )

    CloseMessageWindow()
    OP_62(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x19, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2EF6():
        OP_6D(-210, 4200, -1250, 3000)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_2EF6)

    def lambda_2F0E():
        OP_67(0, 5850, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_2F0E)

    def lambda_2F26():
        OP_6B(2230, 3000)
        ExitThread()

    QueueWorkItem(0x1D, 3, lambda_2F26)

    def lambda_2F36():
        OP_6E(375, 3000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_2F36)

    def lambda_2F46():
        OP_8F(0xFE, 0x550, 0xFA0, 0xFFFFEA20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_2F46)

    def lambda_2F61():

        label("loc_2F61")

        TurnDirection(0xFE, 0x20, 400)
        OP_48()
        Jump("loc_2F61")

    QueueWorkItem2(0x1D, 1, lambda_2F61)
    Sleep(50)

    def lambda_2F77():

        label("loc_2F77")

        TurnDirection(0xFE, 0x20, 400)
        OP_48()
        Jump("loc_2F77")

    QueueWorkItem2(0x15, 1, lambda_2F77)
    Sleep(50)

    def lambda_2F8D():

        label("loc_2F8D")

        TurnDirection(0xFE, 0x20, 400)
        OP_48()
        Jump("loc_2F8D")

    QueueWorkItem2(0x11, 1, lambda_2F8D)
    Sleep(50)

    def lambda_2FA3():

        label("loc_2FA3")

        TurnDirection(0xFE, 0x20, 400)
        OP_48()
        Jump("loc_2FA3")

    QueueWorkItem2(0x19, 1, lambda_2FA3)
    Sleep(50)

    def lambda_2FB9():

        label("loc_2FB9")

        TurnDirection(0xFE, 0x20, 400)
        OP_48()
        Jump("loc_2FB9")

    QueueWorkItem2(0x12, 1, lambda_2FB9)
    Sleep(50)

    def lambda_2FCF():

        label("loc_2FCF")

        TurnDirection(0xFE, 0x20, 400)
        OP_48()
        Jump("loc_2FCF")

    QueueWorkItem2(0x16, 1, lambda_2FCF)
    Sleep(50)

    def lambda_2FE5():

        label("loc_2FE5")

        TurnDirection(0xFE, 0x20, 400)
        OP_48()
        Jump("loc_2FE5")

    QueueWorkItem2(0x13, 1, lambda_2FE5)
    Sleep(50)

    def lambda_2FFB():

        label("loc_2FFB")

        TurnDirection(0xFE, 0x20, 400)
        OP_48()
        Jump("loc_2FFB")

    QueueWorkItem2(0x18, 1, lambda_2FFB)
    Sleep(50)

    def lambda_3011():

        label("loc_3011")

        TurnDirection(0xFE, 0x20, 400)
        OP_48()
        Jump("loc_3011")

    QueueWorkItem2(0x1B, 1, lambda_3011)
    Sleep(50)

    def lambda_3027():

        label("loc_3027")

        TurnDirection(0xFE, 0x20, 400)
        OP_48()
        Jump("loc_3027")

    QueueWorkItem2(0x1A, 1, lambda_3027)
    Sleep(50)

    def lambda_303D():

        label("loc_303D")

        TurnDirection(0xFE, 0x20, 400)
        OP_48()
        Jump("loc_303D")

    QueueWorkItem2(0x14, 1, lambda_303D)
    Sleep(50)

    def lambda_3053():

        label("loc_3053")

        TurnDirection(0xFE, 0x20, 400)
        OP_48()
        Jump("loc_3053")

    QueueWorkItem2(0x1C, 1, lambda_3053)
    Sleep(1000)

    def lambda_3069():
        OP_8F(0xFE, 0xFFFFFC90, 0xFA0, 0xFFFFF254, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_3069)
    Sleep(50)

    def lambda_3089():
        OP_8F(0xFE, 0x9B0, 0xFA0, 0xFFFFF0F6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_3089)
    WaitChrThread(0x20, 0x0)
    OP_44(0x1D, 0x1)
    OP_44(0x15, 0x1)
    OP_44(0x11, 0x1)
    OP_44(0x19, 0x1)
    OP_44(0x12, 0x1)
    OP_44(0x16, 0x1)
    OP_44(0x13, 0x1)
    OP_44(0x13, 0x1)
    OP_44(0x18, 0x1)
    OP_44(0x1B, 0x1)
    OP_44(0x1A, 0x1)
    OP_44(0x14, 0x1)
    OP_44(0x1C, 0x1)
    WaitChrThread(0x1D, 0x0)
    Fade(500)
    OP_6D(-800, 4000, -3600, 0)
    OP_67(0, 5790, -10000, 0)
    OP_6B(2310, 0)
    OP_6C(222000, 0)
    OP_6E(375, 0)
    SetChrPos(0x20, 0, 4000, -5350, 0)
    SetChrPos(0x1D, 770, 4000, 1160, 180)
    SetChrPos(0x15, -500, 4000, 1000, 180)
    SetChrPos(0x16, 460, 4000, -550, 180)
    SetChrPos(0x11, 1650, 4000, -250, 180)
    SetChrPos(0x14, -820, 4000, -680, 180)
    SetChrPos(0x1B, 1400, 4000, -2300, 180)
    SetChrPos(0x12, -1000, 4000, -1980, 180)
    SetChrPos(0x1C, 3200, 4000, -2130, 225)
    SetChrPos(0x19, -1750, 4000, -3120, 135)
    SetChrPos(0x1A, 2500, 4000, -900, 225)
    SetChrPos(0x18, 300, 4000, -2150, 180)
    SetChrPos(0x13, 1900, 4000, -3200, 225)
    OP_0D()
    Sleep(300)

    ChrTalk(    #76
        0x15,
        "#1504F#12P莉丝小姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x1D,
        (
            "#1015F#6P那个……\x01",
            "凯文先生的情况如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x20,
        (
            "#1446F#5P嗯……\x01",
            "总算平静下来了。\x02\x03",

            "#1806F但由于精神上\x01",
            "承担了过度的负荷，\x01",
            "因此需要休息一段时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x1D,
        "#1025F#6P是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x1B,
        (
            "#1525F#6P哎呀哎呀……\x01",
            "真是令人担心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x15,
        (
            "#1503F#12P可是，莉丝小姐……\x02\x03",

            "#1502F『精神上的负荷』，\x01",
            "也就是说……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x20,
        (
            "#1446F#5P嗯……\x01",
            "正如你所说，是『圣痕』。\x02\x03",

            "#1443F不过……\x01",
            "和你被刻上去的那个不同，\x01",
            "他的圣痕可以说是其『原型』吧。\x02\x03",

            "据说那是只有『守护骑士』\x01",
            "才会显现的灵魂之刻印。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x1D,
        "#1004F#6P『守护骑士』……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x18,
        (
            "#1545F#6P嗯，我听说过。\x02\x03",

            "#1540F是指统帅『星杯骑士团』的\x01",
            "十二名特别的骑士。\x02\x03",

            "听说，他们每个人\x01",
            "都有令人恐惧的特异功能。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x20,
        (
            "#1446F#5P嗯，你说的没错。\x02\x03",

            "#1445F……那个特异功能\x01",
            "就是来自各人的『圣痕』的力量。\x02\x03",

            "其作为力量之源泉，\x01",
            "能够让将肉体强化到极致，\x01",
            "或者使用高强度的法术的事情成为可能。\x02\x03",

            "#1446F凯文就是拥有『圣痕』的\x01",
            "十二名『守护骑士』之一……\x02\x03",

            "#1443F排名『第五位』的人物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x1A,
        (
            "#1317F#6P怎、怎么听起来\x01",
            "像是在说另外一个人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x16,
        (
            "#1163F#12P那么，凯文先生\x01",
            "也是和约修亚一样\x01",
            "受了什么处置吗……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x20,
        (
            "#1446F#5P不，\x01",
            "原本『圣痕』并不是\x01",
            "人为埋在体内的。\x02\x03",

            "而是自然产生，\x01",
            "并显露出来的东西。\x02\x03",

            "#1440F并且，从历史上来看，\x01",
            "『守护骑士』的数量总是维持在十二名──\x02\x03",

            "据说不管在哪个时代，\x01",
            "一定会有拥有『圣痕』的人出现\x01",
            "然后成为『守护骑士』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x1D,
        (
            "#1007F#6P这、这还真是不可思议……\x02\x03",

            "#1004F那么，\x01",
            "约修亚的『圣痕』……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x15,
        (
            "#1503F#12P那个大概是……\x01",
            "根据真正的『圣痕』\x01",
            "模拟再现出来的东西吧。\x02\x03",

            "#1502F……因为怀斯曼\x01",
            "曾经是七耀教会的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x1D,
        "#1015F#6P啊，是有这么回事。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x20,
        (
            "#1446F#5P……背叛者怀斯曼\x01",
            "曾经是『星杯骑士团』的上级——\x01",
            "『封圣省』的司教。\x02\x03",

            "他在担任司教的时候\x01",
            "就开始与『噬身之蛇』串通，\x01",
            "盗取了各种各样的圣物。\x02\x03",

            "#1445F关于守护骑士『圣痕』的\x01",
            "大量文献与研究就是其中之一……\x02\x03",

            "#1443F据推测，他将其作为参考，\x01",
            "想要在结社中实现\x01",
            "制造『超人』的技术。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x15,
        "#1505F#12P果然……是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x18,
        (
            "#1544F#6P嗯，真正的『圣痕』\x01",
            "到底是什么东西，\x01",
            "我大概是明白了……\x02\x03",

            "#1542F但是，\x01",
            "为什么凯文神父会晕倒呢？\x02\x03",

            "想要发挥出\x01",
            "『圣痕』的力量\x01",
            "竟然要伴随这样的危险吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x20,
        (
            "#1802F#5P…………那个………………\x02\x03",

            "#1445F……虽然还不知道理由，\x01",
            "但凯文似乎很少解放\x01",
            "『圣痕』的力量。\x02\x03",

            "唯一会解放力量的情况，\x01",
            "就是在制裁『异端』的场合……\x02\x03",

            "#1446F那是指处分\x01",
            "『无法挽回』的重大罪人的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x11,
        "#065F#6P处、处分……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x14,
        "#212F#12P真是可怕的说法……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x1C,
        (
            "#551F#6P算了，这个暂且不提……\x02\x03",

            "#555F总之就是平时不常用的力量\x01",
            "突然被引发出来，\x01",
            "所以才晕倒的对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x20,
        (
            "#1445F#5P嗯……\x01",
            "可以这么说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x12,
        (
            "#176F#12P原来如此……\x01",
            "凯文先生的事情我们了解了。\x02\x03",

            "#178F可是，这样好吗？\x01",
            "把这些都告诉我们……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x20,
        (
            "#1447F#5P没关系……\x01",
            "凯文似乎已经打算\x01",
            "向大家说明一切。\x02\x03",

            "#1448F我也觉得这样做是必要的，\x01",
            "因为接下来的探索\x01",
            "必须取得大家的协助。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x1D,
        (
            "#1025F#6P是吗……\x02\x03",

            "#1004F哎，这么说\x01",
            "莉丝小姐你……！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x20,
        (
            "#1447F#5P是的，\x01",
            "我会临时代替凯文的角色。\x02\x03",

            "#1448F我很荣幸担任探索的记录者\x01",
            "以及各位的向导。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x19,
        "#070F#11P是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x11,
        (
            "#065F#6P可、可是这样好吗？\x02\x03",

            "莉丝姐姐，你应该是最想\x01",
            "陪在凯文哥哥身边照顾他的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x20,
        (
            "#1446F#5P……在凯文倒下之前，\x01",
            "他把『方石』托付给了我。\x02\x03",

            "#1448F那么这就是随从骑士的任务。\x02\x03",

            "请各位不用担心，\x01",
            "让我也参加探索吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x11,
        "#063F#6P莉丝姐姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x13,
        (
            "#272F#6P嗯，这样的话，\x01",
            "也没有什么理由反对了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x16,
        (
            "#1382F#12P凯文先生的情况\x01",
            "你就不必担心了。\x02\x03",

            "有这么多人留下照顾，\x01",
            "应该没问题的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x20,
        (
            "#1806F#5P是……\x01",
            "那就请大家多关照了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x1D,
        "#1015F#6P…………………………………\x02",
    )

    CloseMessageWindow()

    def lambda_4070():
        OP_6D(-800, 4000, -3000, 800)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_4070)
    OP_8C(0x15, 90, 400)
    WaitChrThread(0x1D, 0x0)
    Sleep(300)

    ChrTalk(    #112
        0x15,
        (
            "#1504F#11P……？\x01",
            "艾丝蒂尔，怎么了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x1D,
        (
            "#1007F#6P嗯……\x02\x03",

            "#1006F我说，莉丝小姐。\x01",
            "我有一个请求。\x02\x03",

            "如果要探索的话，\x01",
            "我也一起去可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x20,
        "#1444F#5P咦……\x02",
    )

    CloseMessageWindow()

    def lambda_415B():
        TurnDirection(0xFE, 0x1D, 400)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_415B)

    def lambda_4169():
        TurnDirection(0xFE, 0x1D, 400)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_4169)

    def lambda_4177():
        TurnDirection(0xFE, 0x1D, 400)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_4177)
    Sleep(50)

    def lambda_418A():
        TurnDirection(0xFE, 0x1D, 400)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_418A)

    def lambda_4198():
        TurnDirection(0xFE, 0x1D, 400)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_4198)

    def lambda_41A6():
        TurnDirection(0xFE, 0x1D, 400)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_41A6)

    def lambda_41B4():
        TurnDirection(0xFE, 0x1D, 400)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_41B4)
    Sleep(50)

    def lambda_41C7():
        TurnDirection(0xFE, 0x1D, 400)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_41C7)

    def lambda_41D5():
        TurnDirection(0xFE, 0x1D, 400)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_41D5)

    def lambda_41E3():
        TurnDirection(0xFE, 0x1D, 400)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_41E3)
    Sleep(700)

    ChrTalk(    #115
        0x15,
        "#1504F#11P艾丝蒂尔？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x1D,
        (
            "#1018F#6P那个，因为……\x01",
            "我刚刚才醒过来，\x01",
            "很想亲自了解一下情况。\x02\x03",

            "反正，我也是个游击士，\x01",
            "一定能帮上忙的。\x02\x03",

            "#1016F#6P这个……可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x20,
        (
            "#1444F#5P…………………………………\x02\x03",

            "#1447F……我知道了。\x02\x03",

            "#1806F那就拜托你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x1D,
        "#1017F#6P嘿嘿，谢谢。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x1D, 270, 400)
    Sleep(300)

    ChrTalk(    #119
        0x1D,
        (
            "#1007F#6P……约修亚。\x01",
            "我随便做了这样的决定，真抱歉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x15,
        (
            "#1504F#11P不……\x02\x01",

            "#1513F没关系，就依你的判断吧。\x02\x03",

            "#1500F你可要好好支援\x01",
            "莉丝小姐啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x1D,
        "#1006F#6P嗯，交给我吧！\x02",
    )

    CloseMessageWindow()

    def lambda_4420():
        OP_6B(3000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4420)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_A2(0x2A00)
    OP_28(0x34, 0x1, 0x40)
    OP_28(0x34, 0x1, 0x80)
    OP_28(0x34, 0x1, 0x100)
    OP_28(0x34, 0x1, 0x200)
    OP_28(0x32, 0x4, 0x10)
    OP_28(0x32, 0x4, 0x20)
    OP_28(0x33, 0x4, 0x10)
    OP_28(0x33, 0x4, 0x20)
    OP_28(0x34, 0x4, 0x10)
    OP_28(0x34, 0x4, 0x20)
    OP_28(0x35, 0x4, 0x4)
    OP_28(0x35, 0x4, 0x8)
    OP_28(0x35, 0x1, 0x1)
    OP_28(0x35, 0x1, 0x2)
    OP_3F(0x35D, 1)
    OP_DB(0x0, 0x0)
    OP_A2(0x25C6)
    Call(6, 10)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    OP_DB(0x1, 0x8)
    OP_DB(0x0, 0xE)
    ClearParty()
    AddParty(0xE, 0xEE, 0xFF)
    AddParty(0x0, 0xEF, 0xFF)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_DD(0x1, 0x0, 0x0, 16385, 0, 0, 0)
    FadeToDark(0, 0, -1)
    OP_C0(0x20, 0x1, 0x4001, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    OP_6D(390, 4000, -1290, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(450, 0)
    SetChrPos(0x0, 390, 4000, -1290, 180)
    SetChrPos(0x1, 390, 4000, -1290, 180)
    SetChrPos(0x2, 390, 4000, -1290, 180)
    SetChrPos(0x3, 390, 4000, -1290, 180)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    OP_20(0x5DC)
    OP_21()
    OP_1D(0xD2)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xD2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_9_1DBE end

    def Function_10_4633(): pass

    label("Function_10_4633")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D2(0x2602E1, 0x2602E6, 0x13)
    OP_D2(0x2602E0, 0x2602E5, 0x14)
    OP_D2(0x60034, 0x60039, 0x15)
    OP_D2(0x702D2, 0x702D9, 0x16)
    LoadEffect(0x1, "map\\mp253_00.eff")
    LoadEffect(0x2, "map\\mp253_01.eff")
    LoadEffect(0x3, "map\\mp253_02.eff")
    LoadEffect(0x4, "map\\mp253_03.eff")
    LoadEffect(0x5, "map\\mp253_05.eff")
    LoadEffect(0x6, "map\\mp253_04.eff")
    ClearChrFlags(0x10F, 0x80)
    ClearChrFlags(0x101, 0x80)
    SetChrPos(0x10F, 0, 4000, -1770, 0)
    SetChrPos(0x101, -700, 4000, -3010, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x11, 1800, 4000, -3100, 0)
    SetChrPos(0x12, 1200, 4000, -5800, 0)
    SetChrPos(0x13, -100, 4000, -6100, 0)
    SetChrPos(0x14, 3100, 4000, -5700, 0)
    SetChrPos(0x15, 600, 4000, -3400, 0)
    SetChrPos(0x16, 300, 4000, -4600, 0)
    SetChrPos(0x18, -900, 4000, -4600, 0)
    SetChrPos(0x19, -1520, 4000, -5400, 0)
    SetChrPos(0x1A, 2300, 4000, -4300, 0)
    SetChrPos(0x1B, 1900, 4000, -5200, 0)
    SetChrPos(0x1C, 3500, 4000, -4500, 0)
    SetChrFlags(0xF0, 0x80)
    SetChrFlags(0xF1, 0x80)
    OP_6D(-950, 4000, -980, 0)
    OP_67(0, 5890, -10000, 0)
    OP_6B(2200, 0)
    OP_6C(314000, 0)
    OP_6E(388, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)

    def lambda_485E():
        OP_6D(-1180, 4000, 2780, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_485E)

    def lambda_4876():
        OP_67(0, 5490, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4876)

    def lambda_488E():
        OP_6B(2400, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_488E)

    def lambda_489E():
        OP_6E(403, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_489E)
    OP_8F(0x10F, 0x0, 0xFA0, 0xFFFFFE16, 0x3E8, 0x0)
    WaitChrThread(0x101, 0x0)
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x10F, 19)
    SetChrSubChip(0x10F, 0)
    OP_22(0x8F, 0x0, 0x64)
    Sleep(100)
    ClearChrFlags(0x1E, 0x80)
    OP_9F(0x1E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x1E, 0x40)
    SetChrFlags(0x1E, 0x4)
    SetChrFlags(0x1E, 0x1)
    SetChrChipByIndex(0x1E, 20)
    SetChrSubChip(0x1E, 0)
    SetChrPos(0x1E, 0, 5100, 100, 0)
    PlayEffect(0x1, 0x0, 0x1E, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x1E, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)
    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    OP_E5(0x2, 0xFF, 0x13, 1000)
    OP_0D()
    Fade(1000)
    OP_E5(0x2, 0xFF, 0x13, 700)
    OP_0D()

    def lambda_49B0():
        OP_8F(0xFE, 0x0, 0x1770, 0x64, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_49B0)
    WaitChrThread(0x1E, 0x0)
    Sleep(300)
    Fade(1000)
    OP_6D(0, 5000, 3260, 0)
    OP_67(0, 3980, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(0, 0)
    OP_6E(363, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    SetChrPos(0x101, -900, 4000, -3010, 0)
    SetChrPos(0x11, 1400, 4000, -3100, 0)
    SetChrPos(0x12, 500, 4000, -5800, 0)
    SetChrPos(0x13, -800, 4000, -6100, 0)
    SetChrPos(0x14, 2400, 4000, -5700, 0)
    SetChrPos(0x15, 200, 4000, -3400, 0)
    SetChrPos(0x16, -200, 4000, -4600, 0)
    SetChrPos(0x18, -1300, 4000, -4600, 0)
    SetChrPos(0x19, -2000, 4000, -5400, 0)
    SetChrPos(0x1A, 2000, 4000, -4300, 0)
    SetChrPos(0x1B, 1100, 4000, -5200, 0)
    SetChrPos(0x1C, 2800, 4000, -4800, 0)
    SetChrPos(0x1E, 0, 6000, 1000, 0)

    def lambda_4AFE():
        OP_6D(0, 7500, 3760, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_4AFE)

    def lambda_4B16():
        OP_67(0, 1650, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_4B16)

    def lambda_4B2E():
        OP_6B(2700, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_4B2E)

    def lambda_4B3E():
        OP_6E(363, 3500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4B3E)

    def lambda_4B4E():
        OP_8F(0xFE, 0x0, 0x2134, 0xAF0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_4B4E)
    WaitChrThread(0x1E, 0x0)
    WaitChrThread(0x10F, 0x0)
    Sleep(500)

    def lambda_4B78():
        OP_6B(2000, 8000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_4B78)
    OP_22(0x147, 0x0, 0x64)
    PlayEffect(0x5, 0x2, 0x1E, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    OP_23(0x147)
    Fade(500)
    OP_22(0xC, 0x0, 0x64)
    PlayEffect(0x3, 0x2, 0x1E, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x0)
    Sleep(300)
    PlayEffect(0x6, 0x3, 0x1E, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_4633 end

    def Function_11_4C62(): pass

    label("Function_11_4C62")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D2(0x2602E1, 0x2602E6, 0x13)
    OP_D2(0x2602E0, 0x2602E5, 0x14)
    OP_D2(0x60034, 0x60039, 0x15)
    OP_D2(0x702D4, 0x702DB, 0x16)
    LoadEffect(0x4, "map\\mp253_03.eff")
    LoadEffect(0x5, "map\\mp253_05.eff")
    LoadEffect(0x6, "map\\mp253_04.eff")
    ClearChrFlags(0x10F, 0x80)
    ClearChrFlags(0x101, 0x80)
    SetChrPos(0x10F, 190, 4000, -1500, 0)
    SetChrPos(0x101, -850, 4000, -2790, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x11, 1800, 4000, -3050, 0)
    SetChrPos(0x12, 1200, 4000, -5800, 0)
    SetChrPos(0x13, -100, 4000, -6100, 0)
    SetChrPos(0x14, 3200, 4000, -5800, 0)
    SetChrPos(0x15, 600, 4000, -3200, 0)
    SetChrPos(0x16, 300, 4000, -4600, 0)
    SetChrPos(0x18, -900, 4000, -4600, 0)
    SetChrPos(0x19, -1520, 4000, -5400, 0)
    SetChrPos(0x1A, 2300, 4000, -4300, 0)
    SetChrPos(0x1B, 1900, 4000, -5200, 0)
    SetChrPos(0x1C, 3500, 4000, -4600, 0)
    SetChrFlags(0xF0, 0x80)
    SetChrFlags(0xF1, 0x80)
    OP_6D(-2230, 5000, 4310, 0)
    OP_67(0, 3880, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(315000, 0)
    OP_6E(365, 0)
    ClearChrFlags(0x1E, 0x80)
    OP_9F(0x1E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x1E, 0x40)
    SetChrFlags(0x1E, 0x4)
    SetChrFlags(0x1E, 0x1)
    SetChrChipByIndex(0x1E, 20)
    SetChrSubChip(0x1E, 0)
    SetChrPos(0x1E, 390, 8000, 2150, 180)
    OP_22(0x146, 0x1, 0x50)
    PlayEffect(0x6, 0x2, 0x1E, 400, 400, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_E5(0x2, 0xFF, 0x13, 500)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_4ECA():
        OP_6D(-410, 4000, 1030, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_4ECA)

    def lambda_4EE2():
        OP_67(0, 4850, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_4EE2)

    def lambda_4EFA():
        OP_6B(3200, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_4EFA)

    def lambda_4F0A():
        OP_6E(327, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_4F0A)

    def lambda_4F1A():
        OP_8F(0xFE, 0x186, 0xFA0, 0x866, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_4F1A)
    WaitChrThread(0x1E, 0x0)
    SetChrSubChip(0x1E, 0)
    WaitChrThread(0x10F, 0x0)
    Sleep(500)
    Fade(1000)
    PlayEffect(0x6, 0x1, 0x1E, 400, 300, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)

    def lambda_4F83():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_4F83)
    OP_22(0x99, 0x0, 0x64)
    OP_82(0x2, 0x0)
    OP_0D()
    Sleep(1000)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x19, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #122
        0x101,
        "#1004F#6P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x15,
        "#1504F#6P这个人是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x12,
        "#173F#6P难、难道……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x1A,
        "#1310F#6P难道是……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x1C,
        "#055F#6P喂喂，真的假的……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    PlayEffect(0x4, 0x4, 0x1E, 400, 300, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_22(0x138, 0x0, 0x64)
    OP_23(0x146)

    def lambda_51D6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_51D6)
    OP_82(0x2, 0x2)
    WaitChrThread(0x1E, 0x0)
    Fade(500)
    OP_82(0x1, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #127
        0x1E,
        "#116F#5P哼……是闪光弹吗！？\x02",
    )

    CloseMessageWindow()
    OP_9E(0x1E, 0x14, 0x0, 0x12C, 0xBB8)
    OP_22(0xA3, 0x0, 0x64)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x1E, 22)
    SetChrSubChip(0x1E, 0)

    def lambda_524E():
        OP_96(0xFE, 0x122, 0xFA0, 0xBB8, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_524E)
    WaitChrThread(0x1E, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    ClearChrFlags(0x10, 0x80)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10, 290, 3600, 2600, 180)

    ChrTalk(    #128
        0x1E,
        "#114F#11P#3S什么人──报上名来！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #129
        0x1E,
        (
            "#113F#11P怎……\x02\x03",

            "………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x101,
        (
            "#1016F#6P啊哈哈……\x01",
            "这还真是出乎意料。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x10F,
        (
            "#1440F#6P……果然，\x01",
            "还是你们认识的人吗？\x02\x03",

            "看起来像是王国军的人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x15,
        (
            "#1513F#6P嗯……\x01",
            "是我们的老熟人了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x1E,
        "#113F#11P这到底是……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x1E, 16)
    SetChrSubChip(0x1E, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #134
        0x1E,
        (
            "#112F#11P艾丝蒂尔、约修亚……\x02\x03",

            "还、还有科洛蒂娅殿下，\x01",
            "以及尤莉亚上尉……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x16,
        (
            "#1382F#6P理查德先生。\x01",
            "好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x12,
        "#179F#6P……很久不见。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x1E, 20)
    SetChrSubChip(0x1E, 1)
    OP_0D()
    Sleep(500)

    ChrTalk(    #137
        0x1E,
        (
            "#115F#11P……彼此彼此。\x01",
            "久疏问候，十分抱歉。\x02\x03",

            "#110F在下谨祝\x01",
            "王太女殿下贵安……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x16,
        (
            "#1165F#6P呵呵，请把头抬起来吧。\x02\x03",

            "#1168F您最近还好吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x1E,
        (
            "#119F#11P是，\x01",
            "多亏了女王陛下额外开恩……\x02\x03",

            "#112F可是，现在这种情况……\x01",
            "我怎么都想不通。\x02\x03",

            "如果可以的话，\x01",
            "能给我详细地说明一下吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x10F,
        (
            "#1448F#6P……关于这一点，\x01",
            "就由我来说明吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #141
        0x1E,
        "#113F#11P你是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x10F,
        (
            "#1447F#6P初次见面。\x02\x03",

            "#1448F我来自七耀教会星杯骑士团，\x01",
            "名为莉丝·亚尔珍特。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #143
        0x1E,
        (
            "#112F星杯骑士团……！\x02\x03",

            "#115F……原来如此。\x01",
            "我明白眼前的事态\x01",
            "超乎寻常了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(500)
    SetChrChipByIndex(0x1E, 16)
    SetChrSubChip(0x1E, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #144
        0x1E,
        (
            "#110F#11P……初次见面。\x02\x03",

            "#115F我的名字是亚兰·理查德。\x02\x03",

            "原本是王国军情报部上校，\x01",
            "发动了政变的叛国贼……\x02\x03",

            "#111F现在则是一家名为\x01",
            "『Ｒ＆Ａ Research』的\x01",
            "调查公司的经营者。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrPos(0x10F, 240, 4000, -2180, 0)
    SetChrPos(0x101, -750, 4000, -3200, 0)
    SetChrPos(0x11, 1900, 4000, -3290, 0)
    SetChrPos(0x12, 1300, 4000, -6500, 0)
    SetChrPos(0x13, 100, 4000, -6700, 0)
    SetChrPos(0x14, 2800, 4000, -5950, 0)
    SetChrPos(0x15, 700, 4000, -3600, 0)
    SetChrPos(0x16, -100, 4000, -4700, 0)
    SetChrPos(0x18, -1200, 4000, -4800, 0)
    SetChrPos(0x19, -1600, 4000, -5800, 0)
    SetChrPos(0x1A, 2100, 4000, -4700, 0)
    SetChrPos(0x1B, 1500, 4000, -5440, 0)
    SetChrPos(0x1C, 3600, 4000, -5000, 0)
    SetChrPos(0x1E, 80, 4000, 30, 180)
    SetChrFlags(0x10, 0x80)
    OP_6D(-360, 4000, -1540, 0)
    OP_67(0, 5670, -10000, 0)
    OP_6B(2200, 0)
    OP_6C(314000, 0)
    OP_6E(415, 0)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #145
        0x1E,
        (
            "#115F#11P原来如此。\x01",
            "我差不多明白事情的经过了。\x02\x03",

            "#116F可是……\x01",
            "该说什么好呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x101,
        (
            "#1015F#6P嗯？怎么了？\x02\x03",

            "刚才的话，\x01",
            "果然还是很难相信吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x1E,
        (
            "#110F#11P老实说，也有这样的原因。\x02\x03",

            "#115F但是除此之外……\x01",
            "我还在考虑『为什么我会被选中』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x101,
        "#1004F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x1E,
        (
            "#110F#11P从在场的各位来看，\x01",
            "集结在这里的\x01",
            "都是有着某种缘分的人。\x02\x03",

            "这是女神的指引，或者是什么人的意图……\x02\x03",

            "#119F可以说你们都是曾经\x01",
            "并肩作战的伙伴。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x101,
        "#1008F#6P说起来的确是……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x14, 315, 400)
    Sleep(300)

    ChrTalk(    #151
        0x14,
        (
            "#413F#6P我可没有想要\x01",
            "和你并肩作战。\x02\x03",

            "#210F没大脑的毛病会传染的。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 600)
    Sleep(300)

    ChrTalk(    #152
        0x101,
        "#1019F#5P你、你说什么～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x15,
        "#1512F#5P……我说你们两个。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x1E,
        "#115F#11P咳咳……\x02",
    )

    CloseMessageWindow()

    def lambda_5C8E():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_5C8E)
    Sleep(100)
    OP_8C(0x101, 0, 600)
    Sleep(300)

    ChrTalk(    #155
        0x1E,
        (
            "#112F#11P可是无论怎么想，\x01",
            "我都不是适合\x01",
            "出现在这里的人物。\x02\x03",

            "我可是曾经策划了那么大的阴谋，\x01",
            "让你们——不，是整个利贝尔\x01",
            "陷入绝境的大罪人……\x02\x03",

            "#115F这是不是什么地方搞错了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x16,
        "#1163F#6P理查德先生……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x101,
        (
            "#1002F#6P可、可是……！\x02\x03",

            "在王都遭受袭击的时候，\x01",
            "上校你不是赶过来了吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x11,
        (
            "#065F#6P是、是啊！\x02\x03",

            "和部下的人一起\x01",
            "救了城里的人们……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x1B,
        (
            "#1527F#6P呵呵……\x01",
            "那次真是帮了大忙呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x15,
        (
            "#1500F#6P而且之后还代替\x01",
            "赶往哈肯大门的我们和科洛丝，\x01",
            "担任起防守王都的任务。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x1C,
        (
            "#051F#6P从这层意义上来说，\x01",
            "不是协力者又是什么呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x1E,
        "#112F#11P可是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x18,
        (
            "#1545F#6P呵，理查德先生。\x02\x03",

            "#1540F如果这么说的话，\x01",
            "那时候站在艾丝蒂尔以及\x01",
            "整个利贝尔敌对面的恰恰是本人。\x02\x03",

            "对于如此行为的我，\x01",
            "他们也毫不在意的当作是同伴……\x02\x03",

            "#1541F考虑到这些的话，\x01",
            "你也没必要为此而感到内疚了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x13,
        (
            "#274F#6P……我觉得\x01",
            "应该感到内疚的是你才对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x1E,
        (
            "#110F#11P可是，皇子……\x02\x03",

            "你一开始就是为了阻止\x01",
            "帝国军的阴谋而行动的。\x02\x03",

            "#119F和我的立场还是不一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x14,
        (
            "#212F#6P那我呢？\x02\x03",

            "#413F我们虽然是被\x01",
            "你们情报部所利用，\x01",
            "但身为空贼所做的事依然没变。\x02\x03",

            "#210F不过，虽然发生了那么多事，\x01",
            "现在却得到了女王陛下的恩赦，\x01",
            "还开办了民间的运输公司。\x02\x03",

            "我们的立场不是很相似吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x1E,
        "#113F#11P那个是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x19,
        (
            "#573F#6P算了，重要的不是过去。\x02\x01",

            "#070F我们应该向前看才对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x1A,
        (
            "#811F#6P是啊！\x01",
            "如果有理查德先生的剑术，\x01",
            "对我们来说也是一大帮助……\x02\x03",

            "#815F请一定要协助我们！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x1E,
        "#110F#11P……亚妮拉丝。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 400)
    Sleep(300)

    ChrTalk(    #171
        0x101,
        (
            "#1011F#5P哎，亚妮拉丝。\x02\x03",

            "你怎么会认识\x01",
            "上校的呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1A, 315, 400)
    Sleep(300)

    ChrTalk(    #172
        0x1A,
        (
            "#819F#6P啊，嘿嘿……\x02\x03",

            "在之前我去见\x01",
            "卡西乌斯先生的时候认识的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x101,
        "#1004F#5P哎，和老爸吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x10F,
        (
            "#1446F#6P──事到如今，\x01",
            "您现在已经没有\x01",
            "拒绝加入大家的理由了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_63C8():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_63C8)
    Sleep(100)
    OP_8C(0x101, 0, 400)
    Sleep(400)

    ChrTalk(    #175
        0x10F,
        (
            "#1448F#6P或者说，\x01",
            "希望您务必协助我们。\x02\x03",

            "如果觉得不合适的话，\x01",
            "用协助星杯骑士团的名义也可以。\x02\x03",

            "怎么样？\x02",
        )
    )

    Jump("loc_646C")

    label("loc_646C")

    CloseMessageWindow()

    ChrTalk(    #176
        0x1E,
        (
            "#115F#11P…………………………………\x02\x03",

            "#110F……我明白了。\x01",
            "还请多多关照。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x101,
        "#1018F#6P太好了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x16,
        "#1168F#6P呵呵……真是太好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x12,
        "#171F#6P那就请您多多指教了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x1E,
        (
            "#119F#11P哈哈……\x01",
            "但愿我能够不辜负你们的期待。\x02\x03",

            "#110F这个暂且不说……\x01",
            "我想确认一件事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x10F,
        "#1444F#6P……是什么呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x1E,
        (
            "#115F#11P我们所有的人\x01",
            "几乎是在同一时刻被白光包围\x01",
            "从而来到这里的……\x02\x03",

            "#112F──那个时候大家的装扮\x01",
            "都和现在一样吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x101,
        "#1015F#6P咦……\x02",
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #184
        0x12,
        (
            "#173F#6P说起来，理查德先生……\x02\x03",

            "您应该已经退役了，\x01",
            "为什么还穿着情报部的军服？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x101,
        "#1004F#6P啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x13,
        (
            "#272F#6P唔，原来是指这个……\x02\x03",

            "#270F这么说，当被白光包围的时候，\x01",
            "你是穿着其它服装了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x1E,
        (
            "#115F#11P……没错。\x02\x03",

            "#112F现在，\x01",
            "我都是在卢安的事务所上班……\x02\x03",

            "在那里一次也没有\x01",
            "穿过以前的军服。\x02\x03",

            "被白光包围的时候\x01",
            "也只是穿着普通的\x01",
            "衬衫和裤子而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x15,
        (
            "#1503F#6P这个……\x01",
            "的确是很奇怪的事情呢。\x02\x03",

            "#1502F也许是之前\x01",
            "没有的『规则』吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x18,
        (
            "#1543F#6P哈，难道……\x02\x03",

            "#1547F那个『影之王』认为\x01",
            "『上校果然还是穿军服最棒啊』，\x01",
            "所以特地帮你换上的吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1C, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x11, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x19, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x15, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x1A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x10F, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x1E, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    def lambda_6A3D():
        OP_6D(-360, 4000, -2040, 800)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_6A3D)

    def lambda_6A55():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6A55)

    def lambda_6A63():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_6A63)
    Sleep(50)

    def lambda_6A76():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_6A76)

    def lambda_6A84():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_6A84)
    Sleep(50)

    def lambda_6A97():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_6A97)

    def lambda_6AA5():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_6AA5)
    Sleep(50)

    def lambda_6AB8():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_6AB8)

    def lambda_6AC6():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_6AC6)
    Sleep(50)

    def lambda_6AD9():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_6AD9)

    def lambda_6AE7():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_6AE7)
    Sleep(50)
    OP_8C(0x19, 90, 400)
    WaitChrThread(0x10F, 0x1)
    Sleep(300)

    ChrTalk(    #190
        0x1B,
        "#1525F#6P我、我说你啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x101,
        (
            "#1019F#11P那、那不是\x01",
            "单纯的军服控嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x1A,
        (
            "#819F#6P啊，\x01",
            "不过我有点理解这种心情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x14,
        "#415F#6P嗯，我也是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x16,
        "#1380F#6P……………………（咳咳）\x02",
    )

    CloseMessageWindow()
    OP_62(0x1E, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #195
        0x1E,
        "#115F#11P你们……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x1C,
        (
            "#551F#12P真是的。\x01",
            "最近的小丫头们啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x11,
        "#060F#12P？？？（←完全不明白）\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_6C86():
        OP_6D(-360, 4000, -1540, 1000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_6C86)

    def lambda_6C9E():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_6C9E)

    def lambda_6CAC():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6CAC)
    Sleep(50)

    def lambda_6CBF():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_6CBF)

    def lambda_6CCD():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_6CCD)
    Sleep(50)

    def lambda_6CE0():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_6CE0)

    def lambda_6CEE():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_6CEE)
    Sleep(50)

    def lambda_6D01():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_6D01)

    def lambda_6D0F():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_6D0F)
    Sleep(50)

    def lambda_6D22():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_6D22)

    def lambda_6D30():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_6D30)
    Sleep(50)
    OP_8C(0x1C, 315, 400)
    WaitChrThread(0x10F, 0x1)
    Sleep(300)

    ChrTalk(    #198
        0x19,
        (
            "#074F#6P不管怎么说，\x01",
            "这也算是新的线索吧。\x02\x03",

            "#070F我们会被送到这里的理由……\x01",
            "应该就快水落石出了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x15,
        (
            "#1505F#6P嗯，我也是这么觉得。\x02\x03",

            "#1500F还有这个\x01",
            "『影之国』的由来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x1E,
        (
            "#119F#11P是吗……\x02\x03",

            "#110F那么关于这件事情\x01",
            "我就暂时不去管它了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x10F,
        (
            "#1447F#6P……好了，做好准备之后\x01",
            "我们就继续向前探索吧。\x02\x03",

            "#1448F理查德先生被解放之后，\x01",
            "一定会有新的道路出现的。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6EEF():
        OP_6B(2800, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_6EEF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x10F, 0x0)
    OP_A2(0x2A04)
    OP_28(0x36, 0x4, 0x4)
    OP_28(0x36, 0x4, 0x8)
    OP_28(0x36, 0x1, 0x1)
    OP_3F(0x35E, 1)
    OP_DB(0x0, 0xB)
    OP_A2(0x25D1)
    Call(6, 20)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1E, 0x80)
    ClearChrFlags(0xF0, 0x80)
    ClearChrFlags(0xF1, 0x80)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_DD(0x1, 0x0, 0x0, 16385, 0, 0, 0)
    FadeToDark(0, 0, -1)
    OP_C0(0x20, 0x1, 0x4001, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_6D(390, 4000, -1290, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(450, 0)
    SetChrPos(0x0, 390, 4000, -1290, 180)
    SetChrPos(0x1, 390, 4000, -1290, 180)
    SetChrPos(0x2, 390, 4000, -1290, 180)
    SetChrPos(0x3, 390, 4000, -1290, 180)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    OP_E5(0x2, 0xFF, 0x13, 700)
    Call(0, 5)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_11_4C62 end

    def Function_12_70A4(): pass

    label("Function_12_70A4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D2(0x2602E2, 0x2602E7, 0x13)
    OP_D2(0x270245, 0x27024F, 0x14)
    LoadEffect(0x1, "map\\mp253_00.eff")
    LoadEffect(0x2, "map\\mp253_01.eff")
    LoadEffect(0x3, "map\\mp253_02.eff")
    LoadEffect(0x4, "map\\mp253_03.eff")
    LoadEffect(0x5, "map\\mp253_05.eff")
    LoadEffect(0x6, "map\\mp253_04.eff")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x10F, 0x80)
    SetChrPos(0x10F, -800, 4000, -3200, 0)
    SetChrPos(0x101, 0, 4000, -1770, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x11, 1800, 4000, -3290, 0)
    SetChrPos(0x12, 1100, 4000, -6200, 0)
    SetChrPos(0x13, 0, 4000, -6300, 0)
    SetChrPos(0x14, 3000, 4000, -5900, 0)
    SetChrPos(0x15, 800, 4000, -3600, 0)
    SetChrPos(0x16, 450, 4000, -4700, 0)
    SetChrPos(0x18, -800, 4000, -4700, 0)
    SetChrPos(0x1E, -1800, 4000, -4900, 0)
    SetChrPos(0x1A, 2100, 4000, -4650, 0)
    SetChrPos(0x1B, 1900, 4000, -5700, 0)
    SetChrPos(0x1C, 3500, 4000, -4960, 0)
    SetChrPos(0x19, -1500, 4000, -6100, 0)
    SetChrFlags(0xF0, 0x80)
    SetChrFlags(0xF1, 0x80)
    OP_6D(-950, 4000, -980, 0)
    OP_67(0, 5890, -10000, 0)
    OP_6B(2200, 0)
    OP_6C(314000, 0)
    OP_6E(388, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)

    def lambda_72D0():
        OP_6D(-1180, 4000, 2780, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_72D0)

    def lambda_72E8():
        OP_67(0, 5490, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_72E8)

    def lambda_7300():
        OP_6B(2400, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_7300)

    def lambda_7310():
        OP_6E(403, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_7310)
    OP_8F(0x101, 0x0, 0xFA0, 0xFFFFFE16, 0x3E8, 0x0)
    WaitChrThread(0x10F, 0x0)
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x101, 19)
    SetChrSubChip(0x101, 0)
    OP_22(0x8F, 0x0, 0x64)
    Sleep(100)
    ClearChrFlags(0x1F, 0x80)
    OP_9F(0x1F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x1F, 0x40)
    SetChrFlags(0x1F, 0x4)
    SetChrFlags(0x1F, 0x1)
    SetChrChipByIndex(0x1F, 20)
    SetChrSubChip(0x1F, 0)
    SetChrPos(0x1F, 0, 5100, 100, 0)
    PlayEffect(0x1, 0x0, 0x1F, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x1F, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    OP_E5(0x2, 0xFF, 0x13, 1000)
    OP_0D()
    Fade(1000)
    OP_E5(0x2, 0xFF, 0x13, 700)
    OP_0D()

    def lambda_7422():
        OP_8F(0xFE, 0x0, 0x1770, 0x64, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_7422)
    WaitChrThread(0x1F, 0x0)
    Sleep(300)
    Fade(1000)
    OP_6D(0, 5000, 3260, 0)
    OP_67(0, 3980, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(0, 0)
    OP_6E(363, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrPos(0x10F, -900, 4000, -3200, 0)
    SetChrPos(0x11, 1300, 4000, -3290, 0)
    SetChrPos(0x12, 100, 4000, -6200, 0)
    SetChrPos(0x13, -800, 4000, -6300, 0)
    SetChrPos(0x14, 2000, 4000, -5900, 0)
    SetChrPos(0x15, 300, 4000, -3600, 0)
    SetChrPos(0x16, -100, 4000, -4700, 0)
    SetChrPos(0x18, -1000, 4000, -4700, 0)
    SetChrPos(0x1E, -1800, 4000, -4900, 0)
    SetChrPos(0x1A, 1600, 4000, -4650, 0)
    SetChrPos(0x1B, 1100, 4000, -5700, 0)
    SetChrPos(0x1C, 2500, 4000, -4960, 0)
    SetChrPos(0x19, -1900, 4000, -6100, 0)
    SetChrPos(0x1F, 0, 6000, 1000, 0)

    def lambda_7581():
        OP_6D(0, 7500, 3760, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_7581)

    def lambda_7599():
        OP_67(0, 1650, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_7599)

    def lambda_75B1():
        OP_6B(2700, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_75B1)

    def lambda_75C1():
        OP_6E(363, 3500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_75C1)

    def lambda_75D1():
        OP_8F(0xFE, 0x0, 0x2134, 0xAF0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_75D1)
    WaitChrThread(0x1F, 0x0)
    WaitChrThread(0x10F, 0x0)
    Sleep(500)

    def lambda_75FB():
        OP_6B(2000, 8000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_75FB)
    OP_22(0x147, 0x0, 0x64)
    PlayEffect(0x5, 0x2, 0x1F, 0, 0, 0, 0, 180, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    OP_23(0x147)
    Fade(500)
    OP_22(0xC, 0x0, 0x64)
    PlayEffect(0x3, 0x2, 0x1F, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x0)
    Sleep(300)
    PlayEffect(0x6, 0x3, 0x1F, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7203   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_70A4 end

    def Function_13_76E5(): pass

    label("Function_13_76E5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D2(0x270009, 0x27000D, 0x13)
    OP_D2(0x2602D6, 0x2602DB, 0x14)
    OP_D2(0x60034, 0x60039, 0x15)
    OP_D2(0x27023E, 0x270248, 0x16)
    OP_D2(0x270240, 0x27024A, 0x17)
    OP_D2(0x270246, 0x270250, 0x18)
    LoadEffect(0x3, "map\\mp253_04.eff")
    LoadEffect(0x4, "map\\mp253_03.eff")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x10F, 0x80)
    SetChrPos(0x10F, -800, 4000, -3200, 0)
    SetChrPos(0x101, 190, 4000, -1500, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x11, 1800, 4000, -3290, 0)
    SetChrPos(0x12, 1100, 4000, -6200, 0)
    SetChrPos(0x13, 0, 4000, -6300, 0)
    SetChrPos(0x14, 3100, 4000, -5900, 0)
    SetChrPos(0x15, 800, 4000, -3600, 0)
    SetChrPos(0x16, 450, 4000, -4700, 0)
    SetChrPos(0x18, -800, 4000, -4700, 0)
    SetChrPos(0x1E, -1800, 4000, -4900, 0)
    SetChrPos(0x1A, 2100, 4000, -4650, 0)
    SetChrPos(0x1B, 1900, 4000, -5700, 0)
    SetChrPos(0x1C, 3500, 4000, -4960, 0)
    SetChrPos(0x19, -1600, 4000, -6200, 0)
    SetChrFlags(0xF0, 0x80)
    SetChrFlags(0xF1, 0x80)
    OP_6D(-2230, 5000, 4310, 0)
    OP_67(0, 3880, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(327000, 0)
    OP_6E(365, 0)
    ClearChrFlags(0x1F, 0x80)
    OP_9F(0x1F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x1F, 0x40)
    SetChrFlags(0x1F, 0x4)
    SetChrFlags(0x1F, 0x1)
    SetChrFlags(0x1F, 0x800)
    SetChrFlags(0x1F, 0x2)
    SetChrChipByIndex(0x1F, 20)
    SetChrSubChip(0x1F, 0)
    SetChrPos(0x1F, 300, 8000, 1700, 180)
    OP_22(0x146, 0x1, 0x50)
    PlayEffect(0x3, 0x2, 0x1F, 100, 300, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_E5(0x2, 0xFF, 0x13, 500)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_796E():
        OP_6D(-300, 4000, 760, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_796E)

    def lambda_7986():
        OP_67(0, 4850, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_7986)

    def lambda_799E():
        OP_6B(3000, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_799E)

    def lambda_79AE():
        OP_6E(327, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_79AE)

    def lambda_79BE():
        OP_6C(327000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_79BE)

    def lambda_79CE():
        OP_8F(0xFE, 0x12C, 0xFA0, 0x69A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_79CE)
    WaitChrThread(0x1F, 0x0)
    SetChrSubChip(0x1F, 0)
    WaitChrThread(0x10F, 0x0)
    Sleep(500)
    Fade(1000)
    OP_82(0x2, 0x2)
    PlayEffect(0x3, 0x1, 0x1F, 100, 300, 200, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)

    def lambda_7A3A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_7A3A)
    OP_22(0x99, 0x0, 0x64)
    OP_82(0x0, 0x0)
    OP_0D()
    Sleep(1000)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x19, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    PlayEffect(0x4, 0x4, 0x1F, 100, 300, 200, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_22(0x138, 0x0, 0x64)
    OP_23(0x146)

    def lambda_7BF7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_7BF7)
    OP_82(0x2, 0x2)
    WaitChrThread(0x1F, 0x0)
    Fade(500)
    OP_82(0x1, 0x0)
    OP_0D()
    Sleep(1000)

    NpcTalk(    #202
        0x1F,
        "『歼灭天使』玲",
        "#268F#5P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x101,
        "#1025F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x11,
        "#066F#6P玲……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x15,
        "#1500F#6P……好像正在睡觉呢。\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    Sleep(500)

    NpcTalk(    #206
        0x1F,
        "『歼灭天使』玲",
        (
            "#268F#5P#60W……爸爸……妈妈…………\x02\x03",

            "#40W………为什么……………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #207
        0x101,
        "#1003F#6P……唉………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x15,
        "#1503F#6P………玲…………\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #209
        0x1F,
        "『歼灭天使』玲",
        "#1309F#5P#60W…………？………………\x02",
    )

    CloseMessageWindow()

    def lambda_7E02():
        OP_6B(2900, 10000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_7E02)
    OP_1D(0xAD)
    Sleep(500)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x26), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(250)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x27), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x26), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_99(0x1F, 0x0, 0x6, 0x3E8)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(300)
    OP_99(0x1F, 0x6, 0xC, 0x3E8)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(140)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(140)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(140)
    Sleep(300)

    NpcTalk(    #210
        0x1F,
        "『歼灭天使』玲",
        "#1307F#5P#40W这里……是……\x02",
    )

    CloseMessageWindow()
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(180)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(180)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(180)
    Sleep(300)

    NpcTalk(    #211
        0x1F,
        "『歼灭天使』玲",
        "#1300F#5P#40W……是吗………我在做梦………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x101,
        "#1025F#6P玲……\x02",
    )

    CloseMessageWindow()
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(180)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(180)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(180)
    Sleep(300)

    NpcTalk(    #213
        0x1F,
        "『歼灭天使』玲",
        (
            "#264F#5P#40W艾丝蒂尔……\x02\x03",

            "#40W还有约修亚……\x01",
            "……连提妲也在……\x02\x03",

            "#263F#40W嘻嘻……\x01",
            "这梦境编排得还不错……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #214
        0x101,
        "#1027F#6P#4S……玲……！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_8125():
        OP_8E(0xFE, 0x1CC, 0xFA0, 0x28A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8125)
    Sleep(200)
    OP_44(0x10F, 0x2)
    Fade(500)
    OP_6D(-700, 4000, 2400, 0)
    OP_67(0, 4800, -10000, 0)
    OP_6B(2000, 0)
    OP_6C(315000, 0)
    OP_6E(420, 0)
    WaitChrThread(0x101, 0x0)
    SetChrFlags(0x101, 0x8)
    OP_99(0x1F, 0x16, 0x18, 0x5DC)
    OP_22(0x20C, 0x0, 0x64)
    OP_99(0x1F, 0x19, 0x1C, 0x5DC)
    OP_0D()
    Sleep(300)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x22), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x22), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)

    NpcTalk(    #215
        0x1F,
        "『歼灭天使』玲",
        "#264F#5P#40W啊……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #216
        0x1F,
        "『歼灭天使』玲",
        (
            "#1305F#5P#40W嘻嘻……艾丝蒂尔真是的……\x01",
            "明明是姐姐，还这么爱撒娇……\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    Sleep(300)

    NpcTalk(    #217
        0x1F,
        "『歼灭天使』玲",
        (
            "#263F#5P#40W而且……\x01",
            "……既温暖，又好闻……\x02\x03",

            "#40W简直就像真实的一样──\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1F, 0x64, 1300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(130)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x24), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(130)

    def lambda_8390():
        OP_6D(-800, 4000, 600, 1000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_8390)

    def lambda_83A8():
        OP_6B(2400, 1000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_83A8)
    OP_22(0x50, 0x0, 0x64)
    OP_22(0xA3, 0x0, 0x64)
    SetChrChipByIndex(0x1F, 17)
    SetChrSubChip(0x1F, 0)
    ClearChrFlags(0x1F, 0x800)
    ClearChrFlags(0x1F, 0x2)
    SetChrFlags(0x1F, 0x1)
    ClearChrFlags(0x1F, 0x4)
    ClearChrFlags(0x101, 0x8)

    def lambda_83E5():
        OP_96(0xFE, 0x122, 0xFA0, 0xD52, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_83E5)

    def lambda_8403():
        OP_95(0xFE, 0x3C, 0xFA0, 0xFFFFF9C0, 0x1F4, 0x1B58)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8403)

    def lambda_8421():

        label("loc_8421")

        TurnDirection(0xFE, 0x1F, 400)
        OP_48()
        Jump("loc_8421")

    QueueWorkItem2(0x11, 2, lambda_8421)

    def lambda_8432():

        label("loc_8432")

        TurnDirection(0xFE, 0x1F, 400)
        OP_48()
        Jump("loc_8432")

    QueueWorkItem2(0x1C, 2, lambda_8432)

    def lambda_8443():

        label("loc_8443")

        TurnDirection(0xFE, 0x1F, 400)
        OP_48()
        Jump("loc_8443")

    QueueWorkItem2(0x1A, 2, lambda_8443)

    def lambda_8454():

        label("loc_8454")

        TurnDirection(0xFE, 0x1F, 400)
        OP_48()
        Jump("loc_8454")

    QueueWorkItem2(0x14, 2, lambda_8454)

    def lambda_8465():

        label("loc_8465")

        TurnDirection(0xFE, 0x1F, 400)
        OP_48()
        Jump("loc_8465")

    QueueWorkItem2(0x16, 2, lambda_8465)

    def lambda_8476():

        label("loc_8476")

        TurnDirection(0xFE, 0x1F, 400)
        OP_48()
        Jump("loc_8476")

    QueueWorkItem2(0x18, 2, lambda_8476)

    def lambda_8487():

        label("loc_8487")

        TurnDirection(0xFE, 0x1F, 400)
        OP_48()
        Jump("loc_8487")

    QueueWorkItem2(0x12, 2, lambda_8487)

    def lambda_8498():

        label("loc_8498")

        TurnDirection(0xFE, 0x1F, 400)
        OP_48()
        Jump("loc_8498")

    QueueWorkItem2(0x13, 2, lambda_8498)
    WaitChrThread(0x101, 0x1)
    SetChrChipByIndex(0x101, 19)
    SetChrSubChip(0x101, 0)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0x1F, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(500)

    NpcTalk(    #218
        0x1F,
        "『歼灭天使』玲",
        (
            "#1308F怎……！？\x02\x03",

            "怎、怎么回事！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x101,
        "#1026F#6P玲……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #220
        0x1F,
        "『歼灭天使』玲",
        (
            "#1308F为、为什么\x01",
            "艾丝蒂尔会在这种地方！？\x02\x03",

            "#268F不……不对……\x02\x03",

            "#1301F为什么玲会在\x01",
            "这样的一个奇怪的地方！？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(500)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #221
        0x101,
        (
            "#1025F#6P玲……\x01",
            "你先冷静下来听我说。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_860D():
        OP_6D(-800, 4000, 900, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_860D)

    def lambda_8625():
        OP_8F(0xFE, 0x1CC, 0xFA0, 0xFFFFFF9C, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8625)
    Sleep(500)

    ChrTalk(    #222 op#A
        0x101,
        "#1025F#6P#19A这都是因为发生了很多……\x02",
    )

    Sleep(2000)

    NpcTalk(    #223
        0x1F,
        "『歼灭天使』玲",
        "#1308F#11P#3S别、别过来！#2S\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(400)

    NpcTalk(    #224
        0x1F,
        "『歼灭天使』玲",
        (
            "#1303F#11P#3S如果你再靠近的话……\x01",
            "我就把你杀掉！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #225
        0x101,
        "#1003F#6P……啊…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x15,
        (
            "#1505F#6P艾丝蒂尔……\x01",
            "你先后退一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x101,
        "#1026F#6P啊……\x02",
    )

    CloseMessageWindow()
    OP_43(0x101, 0x0, 0x3, 0xF)
    Sleep(500)

    def lambda_87A3():
        OP_6D(-800, 4000, 1200, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_87A3)

    def lambda_87BB():
        OP_8F(0xFE, 0x32A, 0xFA0, 0xFFFFF8F8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_87BB)
    WaitChrThread(0x15, 0x0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x10F, 0x0)

    ChrTalk(    #228
        0x15,
        (
            "#1505F#6P玲……\x01",
            "真是很久不见了。\x02\x03",

            "#1514F我们上次见面\x01",
            "还是在『中枢塔』上对吧？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #229
        0x1F,
        "『歼灭天使』玲",
        (
            "#1303F#11P我、我才不管呢！\x02\x03",

            "#1301F约修亚……\x01",
            "你和艾丝蒂尔都是一样的！\x02\x03",

            "一直追着玲不放，\x01",
            "把玲逼得走投无路……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x15,
        (
            "#1512F#6P你果然注意到了。\x02\x03",

            "#1500F嗯，你说的没错，\x01",
            "我们这几个月一直在找你。\x02\x03",

            "现在正好旅行到克洛斯贝尔……\x01",
            "是不是离你很近了呢？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #231
        0x1F,
        "『歼灭天使』玲",
        (
            "#1308F#11P已、已经那么近了……\x02\x03",

            "#1303F……为什么……\x01",
            "为什么不能放过我呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x15,
        (
            "#1505F#6P总而言之，\x01",
            "我们想和你再好好谈一次。\x02\x03",

            "#1502F我从秘密途径得知……\x01",
            "在那之后你并没有\x01",
            "回到『结社』去对吧？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #233
        0x1F,
        "『歼灭天使』玲",
        (
            "#1301F#11P那、那是我的自由吧！？\x02\x03",

            "#1303F我才不想和你们这些人说话，\x01",
            "连见都不想见！\x02\x03",

            "你们为什么就不能放过我呢！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x15,
        "#1503F#6P这个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x101,
        (
            "#1007F#6P对不起……玲。\x02\x03",

            "#1003F在那之后，\x01",
            "我一直担心着你的事……\x02\x03",

            "所以就让约修亚调查了一下，\x01",
            "找了很多地方……\x02\x03",

            "#1025F不过……\x01",
            "能在这种场合遇见，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #236
        0x1F,
        "『歼灭天使』玲",
        (
            "#1308F#11P好什么……一点也不好…… \x02\x03",

            "#1300F……………………………………\x02\x03",

            "#263F嘻嘻，我明白了……\x02\x03",

            "#1306F艾丝蒂尔你净说些好听的话，\x01",
            "其实是为了来抓玲的对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x101,
        "#1004F#6P哎……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #238
        0x1F,
        "『歼灭天使』玲",
        (
            "#1305F#11P话说在前面，\x01",
            "玲对『结社』所了解的程度\x01",
            "只是和约修亚不相上下。\x02\x03",

            "就算知道，\x01",
            "也没有告诉你们的打算。\x02\x03",

            "#263F嘻嘻，真是遗憾啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #239
        0x101,
        "#1020F#6P等、等一下！\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #240
        0x1F,
        "『歼灭天使』玲",
        (
            "#1306F#11P嘻嘻，虽然不知道是怎么回事，\x01",
            "不过看来有这么多似曾相识的面孔在场呢。\x02\x03",

            "#263F就算是玲，\x01",
            "一次对付这么多人也有些困难……\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x1F, 24)
    SetChrSubChip(0x1F, 14)

    def lambda_8E4E():
        OP_99(0x1F, 0xE, 0x8, 0x5DC)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_8E4E)
    WaitChrThread(0x1F, 0x1)
    Sleep(500)

    def lambda_8E68():
        OP_99(0x1F, 0x8, 0x2, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_8E68)
    Sleep(200)
    Fade(500)

    def lambda_8E82():
        OP_6B(2300, 0)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_8E82)
    OP_22(0x1F9, 0x0, 0x64)
    WaitChrThread(0x1F, 0x1)
    Sleep(500)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x19, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)

    def lambda_8FF7():
        OP_99(0x1F, 0x2, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_8FF7)
    SetChrChipByIndex(0x1F, 23)
    SetChrSubChip(0x1F, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #241
        0x1F,
        "『歼灭天使』玲",
        (
            "#1304F……不过如果你们想寻死的话，\x01",
            "就快点出手吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x101,
        "#1027F#6P啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x11,
        "#065F#6P玲……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x1C,
        "#551F#6P喂喂…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x1A,
        (
            "#1317F#6P雪拉前辈……\x01",
            "我、我们该怎么办啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x1B,
        "#1525F#6P这下麻烦了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x10F,
        "#1805F#6P……………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_D2(0x270448, 0x27044C, 0x13)
    OP_D2(0x70064, 0x7006C, 0x14)
    OP_D2(0x600DC, 0x600E1, 0x15)
    OP_D2(0x27004E, 0x27004F, 0x16)
    OP_D2(0x270240, 0x27024A, 0x17)
    OP_D2(0x70061, 0x70069, 0x18)

    def lambda_9186():
        OP_6D(-510, 4000, 2300, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9186)

    def lambda_919E():
        OP_67(0, 5020, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_919E)

    def lambda_91B6():
        OP_8F(0xFE, 0xFFFFFC9A, 0xFA0, 0xFFFFFC22, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_91B6)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #248
        0x10F,
        (
            "#1446F#6P原来如此……\x01",
            "我知道你的身份了。\x02\x03",

            "#1443F你是『结社』的执行者——\x01",
            "Ｎｏ．ⅩⅤ『歼灭天使』对吧？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #249
        0x1F,
        "『歼灭天使』玲",
        (
            "#269F#11P没错……\x01",
            "我可是头一次见到这位姐姐呢。\x02\x03",

            "是教会的骑士吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x10F,
        (
            "#1447F#6P对……我是星杯随从骑士，\x01",
            "名叫莉丝·亚尔珍特。\x02\x03",

            "#1806F虽然我不了解你们所说的事情……\x01",
            "不过你的任性也该适可而止了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1F, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #251
        0x1F,
        "『歼灭天使』玲",
        "#1308F#11P任、任性……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x10F,
        (
            "#1805F#6P……我听说你拥有\x01",
            "常人无法比拟的处理能力。\x02\x03",

            "因此被结社所发掘，\x01",
            "还在其中学习了各种各样的技术。\x02\x03",

            "#1446F那么，\x01",
            "你应该已经领会到\x01",
            "这并不是抓捕你的陷阱……\x02\x03",

            "#1806F明明知道却还无理取闹，\x01",
            "不是任性又是什么呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x16,
        "#1163F#5P莉、莉丝小姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x14,
        "#413F#5P别、别说得这么直接啊……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #255
        0x1F,
        "『歼灭天使』玲",
        (
            "#1305F#11P……真是有趣啊，这位姐姐。\x02\x03",

            "#263F虽说你是星杯骑士团的人，\x01",
            "不过也只是个小小的随从骑士，\x01",
            "竟敢这么对玲说话……\x02\x03",

            "#1304F你就这么急着想被『歼灭』吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x10F,
        (
            "#1806F#6P彼此彼此……\x02\x03",

            "#1447F虽然我并不了解前因后果，\x01",
            "不过我从来没有和『蛇』打交道的打算。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 19)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #257
        0x10F,
        (
            "#1805F#6P……如果你想打架的话，\x01",
            "我随时可以奉陪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x101,
        "#1020F#6P啊……\x02",
    )

    CloseMessageWindow()
    OP_44(0x11, 0x2)
    OP_62(0x11, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #259
        0x11,
        "#065F#6P莉、莉丝姐姐！？\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #260
        0x1F,
        "『歼灭天使』玲",
        (
            "#1306F#11P嘻嘻，原来是使法剑的啊。\x02\x03",

            "之前我也和好几个用法剑的人交过手，\x01",
            "的确有一定实力呢。\x02\x03",

            "#263F不过我早就已经看穿其招式了，\x01",
            "你根本不是我的对手……\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_22(0x1F5, 0x0, 0x64)
    SetChrChipByIndex(0x1F, 23)
    SetChrSubChip(0x1F, 0)
    OP_99(0x1F, 0x0, 0x1, 0x5DC)
    OP_0D()
    Sleep(500)

    NpcTalk(    #261
        0x1F,
        "『歼灭天使』玲",
        (
            "#1304F#11P……你们这些人，\x01",
            "就等着落个痛哭流涕\x01",
            "向玲求饶的下场吧。\x02\x03",

            "嘻嘻，我倒想听听这位姐姐\x01",
            "会发出什么样的惨叫声呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #262
        0x101,
        "#1020F#6P等、等一下……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x11,
        "#065F#6P玲……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x10F,
        (
            "#1805F#6P……废话就不用多说了。\x01",
            "你还是赶快出手吧？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #265
        0x1F,
        "『歼灭天使』玲",
        "#263F#11P嘻嘻……说得也是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x15,
        "#1502F#6P呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x101,
        (
            "#1005F#6P你、你们两个！\x01",
            "赶快──\x02",
        )
    )

    Jump("loc_9955")

    label("loc_9955")

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(2100, 4000, -2570, 0)
    OP_67(0, 5910, -10000, 0)
    OP_6B(1960, 0)
    OP_6C(134000, 0)
    OP_6E(436, 0)
    OP_44(0x11, 0x2)
    OP_44(0x1C, 0x2)
    OP_44(0x1A, 0x2)
    OP_44(0x14, 0x2)
    OP_44(0x16, 0x2)
    OP_44(0x18, 0x2)
    OP_44(0x12, 0x2)
    OP_44(0x13, 0x2)
    SetChrPos(0x1F, 280, 4000, 3410, 180)
    SetChrSubChip(0x1F, 0)
    SetChrPos(0x10F, 100, 4000, -910, 0)
    SetChrPos(0x101, 3300, 4000, -1300, 315)
    SetChrPos(0x11, 2880, 4000, -2890, 315)
    SetChrPos(0x12, 1580, 4000, -6160, 0)
    SetChrPos(0x13, 490, 4000, -6520, 0)
    SetChrPos(0x14, 3820, 4000, -5920, 315)
    SetChrPos(0x15, 680, 4000, -2370, 0)
    SetChrPos(0x16, 500, 4000, -4270, 0)
    SetChrPos(0x18, -450, 4000, -4500, 0)
    SetChrPos(0x1E, -1500, 4000, -4500, 0)
    SetChrPos(0x1A, 3210, 4000, -4460, 315)
    SetChrPos(0x1B, 2120, 4000, -5170, 0)
    SetChrPos(0x1C, 4780, 4000, -4710, 315)
    SetChrPos(0x19, -1000, 4000, -6000, 0)

    def lambda_9AC7():
        OP_6B(1860, 500)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_9AC7)
    OP_0D()
    OP_20(0x3E8)

    ChrTalk(    #268
        0x11,
        "#567F#4S#5P赶快适可而止吧！\x02",
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x12C)
    CloseMessageWindow()
    WaitChrThread(0x10F, 0x0)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1F, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #269
        0x10F,
        "#1444F#12P啊……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #270
        0x1F,
        "『歼灭天使』玲",
        "#1308F#5P咦……\x02",
    )

    CloseMessageWindow()

    def lambda_9B96():

        label("loc_9B96")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_9B96")

    QueueWorkItem2(0x101, 2, lambda_9B96)

    def lambda_9BA7():

        label("loc_9BA7")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_9BA7")

    QueueWorkItem2(0x15, 2, lambda_9BA7)

    def lambda_9BB8():

        label("loc_9BB8")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_9BB8")

    QueueWorkItem2(0x1C, 2, lambda_9BB8)

    def lambda_9BC9():

        label("loc_9BC9")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_9BC9")

    QueueWorkItem2(0x1A, 2, lambda_9BC9)

    def lambda_9BDA():

        label("loc_9BDA")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_9BDA")

    QueueWorkItem2(0x14, 2, lambda_9BDA)

    def lambda_9BEB():

        label("loc_9BEB")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_9BEB")

    QueueWorkItem2(0x16, 2, lambda_9BEB)

    def lambda_9BFC():

        label("loc_9BFC")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_9BFC")

    QueueWorkItem2(0x18, 2, lambda_9BFC)

    def lambda_9C0D():

        label("loc_9C0D")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_9C0D")

    QueueWorkItem2(0x19, 2, lambda_9C0D)

    def lambda_9C1E():

        label("loc_9C1E")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_9C1E")

    QueueWorkItem2(0x12, 2, lambda_9C1E)

    def lambda_9C2F():

        label("loc_9C2F")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_9C2F")

    QueueWorkItem2(0x13, 2, lambda_9C2F)

    def lambda_9C40():

        label("loc_9C40")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_9C40")

    QueueWorkItem2(0x1E, 2, lambda_9C40)
    Sleep(500)

    ChrTalk(    #271
        0x101,
        "#1020F#6P提、提妲……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x1C,
        "#055F#6P喂，你怎么……！？\x02",
    )

    CloseMessageWindow()
    OP_1D(0x76)

    def lambda_9CA3():
        OP_6D(1480, 4000, -140, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_9CA3)

    def lambda_9CBB():
        OP_67(0, 5400, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_9CBB)

    def lambda_9CD3():
        OP_6B(1670, 2000)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_9CD3)

    def lambda_9CE3():
        OP_6E(500, 2000)
        ExitThread()

    QueueWorkItem(0x1F, 3, lambda_9CE3)
    OP_43(0x11, 0x3, 0x3, 0xE)
    Sleep(300)

    def lambda_9CFF():
        OP_8E(0xFE, 0xDFC, 0xFA0, 0xFFFFF29A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_9CFF)
    WaitChrThread(0x1C, 0x0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x10F, 0x3)
    OP_44(0x101, 0x2)
    OP_44(0x15, 0x2)
    OP_44(0x1C, 0x2)
    OP_44(0x1A, 0x2)
    OP_44(0x14, 0x2)
    OP_44(0x16, 0x2)
    OP_44(0x18, 0x2)
    OP_44(0x19, 0x2)
    OP_44(0x12, 0x2)
    OP_44(0x13, 0x2)
    OP_44(0x1E, 0x2)
    OP_8C(0x19, 0, 0)
    OP_8C(0x1E, 0, 0)

    ChrTalk(    #273
        0x11,
        (
            "#562F#11P你们两个真是的！\x01",
            "为什么会变成这样啊！？\x02\x03",

            "#566F玲，\x01",
            "能和艾丝蒂尔姐姐他们见面，\x01",
            "你其实是最开心的不是吗！\x02",
        )
    )

    Jump("loc_9DE5")

    label("loc_9DE5")

    CloseMessageWindow()
    OP_8C(0x11, 180, 600)
    Sleep(300)

    ChrTalk(    #274
        0x11,
        (
            "#566F#6P莉丝姐姐也是，\x01",
            "明明看得出玲并不是\x01",
            "一个坏孩子，却还……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x10F,
        "#1802F#11P提妲……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #276
        0x1F,
        "『歼灭天使』玲",
        (
            "#1308F#6P你、你在说什么……\x02\x03",

            "跟艾丝蒂尔见面，\x01",
            "怎么可能会开心──\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 0, 600)
    Sleep(500)

    ChrTalk(    #277
        0x11,
        (
            "#566F#11P那为什么\x01",
            "你在被姐姐抱住的时候\x01",
            "会是那么一副幸福的表情呢！？\x02",
        )
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x78)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #278
        0x11,
        (
            "#562F#11P还说『又温暖，又好闻』……！\x02\x03",

            "但是……\x01",
            "不想说话……\x01",
            "……不想见面什么的……\x02",
        )
    )

    Jump("loc_9FA5")

    label("loc_9FA5")

    CloseMessageWindow()

    NpcTalk(    #279
        0x1F,
        "『歼灭天使』玲",
        "#1307F#6P等、等一下，提妲……\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrFlags(0x11, 0x800)
    SetChrFlags(0x11, 0x2)
    SetChrChipByIndex(0x11, 21)
    SetChrSubChip(0x11, 8)
    OP_0D()

    def lambda_A004():

        label("loc_A004")

        OP_99(0xFE, 0x7, 0xA, 0x5DC)
        OP_48()
        Jump("loc_A004")

    QueueWorkItem2(0x11, 0, lambda_A004)
    Sleep(500)

    ChrTalk(    #280
        0x11,
        "#566F#11P那些……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #281
        0x11,
        (
            "#567F#4S#11P那些绝对\x01",
            "是谎话！\x02",
        )
    )

    Jump("loc_A06E")

    label("loc_A06E")

    OP_7C(0x0, 0x1F4, 0xBB8, 0x96)
    CloseMessageWindow()
    Sleep(300)

    NpcTalk(    #282
        0x1F,
        "『歼灭天使』玲",
        "#1309F#6P……唉………\x02",
    )

    CloseMessageWindow()
    OP_44(0x11, 0x0)
    OP_99(0x11, 0x6, 0x4, 0x3E8)

    def lambda_A0C9():

        label("loc_A0C9")

        OP_99(0xFE, 0x0, 0x3, 0x3E8)
        OP_48()
        Jump("loc_A0C9")

    QueueWorkItem2(0x11, 0, lambda_A0C9)
    Sleep(500)

    ChrTalk(    #283
        0x11,
        (
            "#069F#11P#40W……呜………\x02\x03",

            "呜……呜呜………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #284
        0x101,
        "#1025F#5P提妲……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x1C,
        (
            "#551F#6P真是……\x01",
            "太乱来了……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #286
        0x1F,
        "『歼灭天使』玲",
        "#268F#6P……唉，真是的………\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x10F, 0x0)
    Sleep(300)
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x1F, 17)
    SetChrSubChip(0x1F, 0)
    Sleep(100)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(300)

    def lambda_A1DD():
        OP_6D(1480, 4000, -500, 1500)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_A1DD)

    def lambda_A1F5():
        OP_8F(0xFE, 0x96, 0xFA0, 0x9C4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_A1F5)
    WaitChrThread(0x1F, 0x0)
    WaitChrThread(0x10F, 0x3)

    NpcTalk(    #287
        0x1F,
        "『歼灭天使』玲",
        (
            "#1307F#6P提妲啊……\x01",
            "你也算是玲的一个姐姐对吧？\x02\x03",

            "#268F那你还总是这么爱哭鼻子……\x01",
            "……真是个长不大的孩子啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x11,
        (
            "#562F#11P#40W呜……那是因为……！\x02\x03",

            "#40W姐姐好不容易见到你，\x01",
            "却变成这种样子……！\x02\x03",

            "#40W这样的话……呜呜……\x01",
            "这样的话就太让人难过了……！\x02\x03",

            "#069F#40W……呜呜……………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_44(0x11, 0x0)
    OP_99(0x11, 0x14, 0x16, 0x3E8)
    Sleep(500)

    ChrTalk(    #289
        0x11,
        "#567F#4S#11P哇啊啊啊啊————！\x02",
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0x12C)
    CloseMessageWindow()
    OP_62(0x1F, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    WaitChrThread(0x10F, 0x0)

    NpcTalk(    #290
        0x1F,
        "『歼灭天使』玲",
        "#1308F#6P等、等一下……！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x1F, 22)
    SetChrSubChip(0x1F, 0)
    OP_0D()
    Sleep(300)

    NpcTalk(    #291
        0x1F,
        "『歼灭天使』玲",
        (
            "#1309F#6P#40W唉……\x01",
            "……为什么……\x02\x03",

            "#268F#40W为什么\x01",
            "……会是提妲哭呢………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x101,
        (
            "#1012F#5P呵呵……\x02\x03",

            "#1017F──之前不是说过吗，\x01",
            "原因是不言自明的。\x02\x03",

            "那是因为喜欢玲啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1F, 0x64, 1400, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0x1F, 1)
    WaitChrThread(0x10F, 0x0)
    Sleep(300)

    NpcTalk(    #293
        0x1F,
        "『歼灭天使』玲",
        "#1307F#6P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x101,
        (
            "#1006F#5P我说，玲。\x02\x03",

            "我们暂时休战吧？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #295
        0x1F,
        "『歼灭天使』玲",
        "#1307F#6P……休战？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x101,
        (
            "#1007F#5P是啊，现在我们正处于\x01",
            "一种非常困难的情况下。\x02\x03",

            "而且不知道是因为什么，\x01",
            "玲也偶然处于同样的困境……\x02\x03",

            "#1006F为了打破这一困境，\x01",
            "我们暂且把之前的事放下，\x01",
            "同心协力共渡难关好吗。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #297
        0x1F,
        "『歼灭天使』玲",
        "#264F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0x1E,
        (
            "#119F#8P的确……\x01",
            "我们现在面临的情况中\x01",
            "仍然有很多未解之谜。\x02\x03",

            "#111F如果能得到你这样聪明的人的协助，\x01",
            "也许就可以获得新的情报。\x02\x03",

            "从这层意义上来说，\x01",
            "如果你肯帮忙那真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0x101,
        (
            "#1001F#5P是啊是啊。\x01",
            "上校，你还真会说话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x1E,
        (
            "#495F#8P我都说不是上校了……\x02\x03",

            "#110F算了，进一步站在你的立场来说，\x01",
            "利用我们比自己单独行动\x01",
            "效率应该要高很多。\x02\x03",

            "不管是为了收集情报，\x01",
            "还是确保当前的安全。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #301
        0x1F,
        "『歼灭天使』玲",
        (
            "#1300F#6P…………………………………\x02\x03",

            "#268F……确实……\x01",
            "不管怎么想这都是不寻常的状况……\x02\x03",

            "玲能帮得上忙\x01",
            "也是理所当然的事情……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(500)
    SetChrChipByIndex(0x1F, 17)
    SetChrSubChip(0x1F, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #302
        0x1F,
        "『歼灭天使』玲",
        (
            "#266F#6P……看在提妲的面子上，\x01",
            "我就不跟你们计较了。\x02\x03",

            "#262F先把事情经过告诉我吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrSubChip(0x11, 20)
    OP_0D()
    Sleep(500)

    ChrTalk(    #303
        0x11,
        "#565F#11P……啊………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0x101,
        "#1008F#5P玲……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0x15,
        "#1513F#11P……谢谢你。\x02",
    )

    CloseMessageWindow()
    OP_62(0x1F, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    NpcTalk(    #306
        0x1F,
        "『歼灭天使』玲",
        (
            "#1301F#6P话、话说在前面……\x01",
            "我只是想知道事情经过哦？\x02\x03",

            "#266F等听你们说完了，\x01",
            "再决定是否帮助你们！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AAB1():
        OP_6B(2090, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_AAB1)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    OP_44(0x10F, 0x0)
    SetChrPos(0x10F, -1360, 4000, -2630, 0)
    SetChrPos(0x101, 0, 4000, -2400, 0)
    SetChrPos(0x11, 2800, 4000, -3100, 315)
    SetChrPos(0x12, 1700, 4000, -6200, 0)
    SetChrPos(0x13, 300, 4000, -5900, 0)
    SetChrPos(0x14, 3400, 4000, -6000, 0)
    SetChrPos(0x15, 1270, 4000, -2600, 0)
    SetChrPos(0x16, 1000, 4000, -4000, 0)
    SetChrPos(0x18, -150, 4000, -4300, 0)
    SetChrPos(0x1E, -1610, 4000, -4110, 0)
    SetChrPos(0x1A, 2800, 4000, -4600, 0)
    SetChrPos(0x1B, 2000, 4000, -5400, 0)
    SetChrPos(0x1C, 4200, 4000, -4960, 315)
    SetChrPos(0x19, -1450, 4000, -5700, 0)
    SetChrPos(0x1F, 180, 4000, 30, 180)
    SetChrChipByIndex(0x11, 3)
    SetChrSubChip(0x11, 0)
    ClearChrFlags(0x11, 0x800)
    ClearChrFlags(0x11, 0x2)
    OP_6D(-330, 4000, -1830, 0)
    OP_67(0, 5340, -10000, 0)
    OP_6B(2000, 0)
    OP_6C(315000, 0)
    OP_6E(420, 0)
    Sleep(2000)
    OP_1D(0xD2)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #307
        0x1F,
        "『歼灭天使』玲",
        (
            "#263F#11P……原来如此。\x01",
            "大致经过我已经明白了。\x02\x03",

            "#269F是『影之国』吗……\x01",
            "嘻嘻，还真是个好名字。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x10F,
        "#1444F#6P哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0x15,
        (
            "#1504F#6P难道……\x01",
            "你知道了些什么吗？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #310
        0x1F,
        "『歼灭天使』玲",
        (
            "#263F#11P嘻嘻，\x01",
            "虽然还称不上确信……\x02\x03",

            "#260F但是，听了上校的话之后，\x01",
            "我认识到了一件事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0x1E,
        "#113F#6P关于我的……？\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #312
        0x1F,
        "『歼灭天使』玲",
        (
            "#268F#11P嗯，我也的确是\x01",
            "被那道白光所吸进来的……\x02\x03",

            "#262F上校在那个时候\x01",
            "并没有穿现在这身黑色军服吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0x1E,
        (
            "#495F#6P（都说不是上校了……算了。）\x02\x03",

            "#110F是的，那个时候我穿的\x01",
            "只是普通的衬衫和裤子。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #314
        0x1F,
        "『歼灭天使』玲",
        (
            "#261F#11P嘻嘻，那我问你……\x02\x03",

            "#265F上校对这身军服\x01",
            "是不是有非常深厚的感情呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #315
        0x1E,
        "#113F#6P哎……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #316
        0x1F,
        "『歼灭天使』玲",
        (
            "#263F#11P嘻嘻，看来我说对了。\x02\x03",

            "#1305F虽然还有所眷恋，\x01",
            "但却不得不与之分别……\x02\x03",

            "这身军服不正是\x01",
            "你的过去的象征吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x1E,
        (
            "#116F#6P…………………………………\x02\x03",

            "#115F……是啊，你说的没错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0x16,
        "#1163F#6P理查德先生……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0x12,
        "#175F#6P…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0x13,
        "#272F#6P……那是当然的。\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #321
        0x1F,
        "『歼灭天使』玲",
        (
            "#1306F#11P然后，你在被招待到这个世界时\x01",
            "正是穿着这样一身服装。\x02\x03",

            "#261F嘻嘻，\x01",
            "这到底是什么意思呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0x1E,
        (
            "#115F#6P…………………………………\x02\x03",

            "将我的执念\x01",
            "变化成了实体……\x02\x03",

            "#112F也就是说，这个『影之国』\x01",
            "会根据人的意念而改变形态。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x19, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #323
        0x15,
        "#1504F#6P啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0x18,
        "#1541F#6P哈哈，果然是这样吗……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0x14,
        "#216F#6P怎、怎么回事！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0x101,
        "#1019F#6P说、说得再简单一点！\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #327
        0x1F,
        "『歼灭天使』玲",
        (
            "#261F#11P嘻嘻，很简单啦。\x02\x03",

            "#265F艾丝蒂尔，\x01",
            "之前露茜奥拉不是借助『福音』\x01",
            "让你们做了那样的梦吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x101,
        "#1004F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0x1B,
        "#1532F#6P人所期望的梦境世界……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #330
        0x1F,
        "『歼灭天使』玲",
        (
            "#263F#11P当然，\x01",
            "这个世界并不是梦境。\x02\x03",

            "#1305F但是，它能反应人的愿望，\x01",
            "并将其实体化……\x02\x03",

            "并且将已知的场所\x01",
            "毫无二致地进行再现……\x02\x03",

            "可以说这种过程\x01",
            "是非常相似的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0x19,
        "#074F#6P原来如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0x1A,
        (
            "#816F#6P的确这样一来\x01",
            "就能够说明那些『石碑』\x01",
            "以及『门』的原理了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0x12,
        (
            "#172F#6P可、可是……\x02\x03",

            "现在的这种状况，\x01",
            "不可能是由我们的\x01",
            "愿望引起的啊……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #334
        0x1F,
        "『歼灭天使』玲",
        (
            "#263F#11P那是当然的。\x02\x03",

            "#1306F可是……\x01",
            "如果是我们之外的人呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #335
        0x12,
        "#173F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0x16,
        (
            "#1167F#6P我们之外的某人\x01",
            "期待着这样的一个世界，\x01",
            "并且将其实现……\x02\x03",

            "#1162F你是这个意思吧。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #337
        0x1F,
        "『歼灭天使』玲",
        (
            "#263F#11P嘻嘻……\x01",
            "终于理解了呢。\x02\x03",

            "#265F原本『辉之环』\x01",
            "就是能够满足人类愿望的至宝。\x02\x03",

            "在它失去下落的现在，\x01",
            "究竟是什么造成了这种情况\x01",
            "我也无从知晓……\x02\x03",

            "#261F但那个『某人』是谁\x01",
            "应该是再明显不过的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0x10F,
        "#1443F#6P『影之王』……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #339
        0x1F,
        "『歼灭天使』玲",
        (
            "#263F#11P对，\x01",
            "而且那个人一开始并不在『影之国』。\x02\x03",

            "一开始就在这里的\x01",
            "应该是那个女性幽灵。\x02\x03",

            "#260F她一直在这个地方\x01",
            "守护着『影之国』……\x02\x03",

            "但『影之王』却前来夺走了她的力量，\x01",
            "并且开始任意妄为。\x02\x03",

            "然后『影之国』\x01",
            "就按照『影之王』的意愿\x01",
            "逐渐变成现在这个样子……\x02\x03",

            "#261F──就是这样一回事了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0x11,
        "#560F#6P玲，你太厉害了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0x101,
        (
            "#1016F#6P你啊……\x01",
            "竟然能想到这么多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0x18,
        (
            "#1545F#6P呵呵……真是服了。\x02\x03",

            "#1540F没想到靠目前这点情报\x01",
            "就可以分析出这么多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0x15,
        (
            "#1513F#6P玲……\x01",
            "你果然是个天才。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #344
        0x1F,
        "『歼灭天使』玲",
        (
            "#268F#11P真是的……\x01",
            "这点小事，\x01",
            "约修亚也应该早就看穿了啊。\x02\x03",

            "#269F难道是因为总和艾丝蒂尔在一起，\x01",
            "连迟钝都传染了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #345
        0x101,
        "#1019F#6P你、你说什么～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0x15,
        (
            "#1514F#6P哈哈……\x01",
            "我想不会吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0x11,
        "#067F#6P嘻嘻……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0x1B,
        "#1521F#6P哎呀……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #349
        0x1F,
        "『歼灭天使』玲",
        (
            "#265F#11P话说回来，看来『影之王』\x01",
            "和玲一样都很喜欢玩游戏呢。\x02\x03",

            "只靠艾丝蒂尔你们\x01",
            "实在有点不放心，\x01",
            "我就来帮你们吧。\x02\x03",

            "#261F嘻嘻，这可是特别服务哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0x101,
        (
            "#1016F#6P啊～知道了知道了。\x01",
            "你就尽管来帮忙吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0x1A,
        "#811F#6P请多关照，玲！\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #352
        0x1F,
        "『歼灭天使』玲",
        (
            "#261F#11P嘻嘻……\x01",
            "这位教会的姐姐，就是这么回事。\x02\x03",

            "我们赶快用『方石』\x01",
            "回『第五星层』继续前进吧。\x02\x03",

            "#265F因为刚才我们已经找到了答案，\x01",
            "游戏的进展一定比预想得要快……\x02\x03",

            "大概『影之王』正在\x01",
            "忙于做下一手的准备吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0x10F,
        (
            "#1806F#6P呼……真是自信满满啊。\x02\x03",

            "#1447F算了，这样也好。\x01",
            "反正也没有其它的选择。\x02\x03",

            "#1443F不过，和之前一样，\x01",
            "在各星层的最终地点\x01",
            "一定会出现『恶魔』。\x02\x03",

            "我们先做好万全的准备吧。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #354
        0x1F,
        "『歼灭天使』玲",
        (
            "#268F#11P唔～真是麻烦啊。\x02\x03",

            "#269F恶魔吗……\x01",
            "如果有的话真想亲眼看看呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1F, 135, 400)
    Sleep(500)

    NpcTalk(    #355
        0x1F,
        "『歼灭天使』玲",
        (
            "#261F#5P我说，提妲。\x01",
            "我们一起去参观一下吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #356
        0x11,
        (
            "#067F#6P那、那个不是\x01",
            "太危险了吗……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(260, 4000, -1350, 0)
    OP_67(0, 6790, -10000, 0)
    OP_6B(1800, 0)
    OP_6C(340000, 0)
    OP_6E(420, 0)
    SetChrPos(0x101, -150, 4000, -2630, 30)
    SetChrPos(0x11, 2710, 4000, -1980, 307)
    OP_8C(0x10F, 30, 0)
    OP_8C(0x19, 30, 0)
    OP_8C(0x1E, 30, 0)
    OP_8C(0x18, 30, 0)
    OP_8C(0x13, 30, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #357
        0x101,
        (
            "#1017F#6P（呵呵，虽然那么任性，\x01",
            "  不过果然还是个小孩子呢。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0x15,
        (
            "#1513F#6P（嗯，真是太好了。）\x02\x03",

            "#1503F（如果能在这段时间里\x01",
            "  和她好好谈一下就好了……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0x101,
        "#1025F#6P（嗯……是啊。）\x02",
    )

    CloseMessageWindow()

    def lambda_C0DF():
        OP_6B(2300, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_C0DF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x10F, 0x0)
    OP_A2(0x2A07)
    OP_28(0x36, 0x1, 0x10)
    OP_28(0x36, 0x1, 0x20)
    OP_28(0x36, 0x1, 0x40)
    OP_3F(0x35F, 1)
    OP_DB(0x0, 0xF)
    OP_A2(0x25D6)
    Call(6, 23)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    ClearChrFlags(0xF0, 0x80)
    ClearChrFlags(0xF1, 0x80)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_DD(0x1, 0x0, 0x0, 16385, 0, 0, 0)
    FadeToDark(0, 0, -1)
    OP_C0(0x20, 0x1, 0x4001, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_6D(390, 4000, -1290, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(450, 0)
    SetChrPos(0x0, 390, 4000, -1290, 180)
    SetChrPos(0x1, 390, 4000, -1290, 180)
    SetChrPos(0x2, 390, 4000, -1290, 180)
    SetChrPos(0x3, 390, 4000, -1290, 180)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    OP_E5(0x2, 0xFF, 0x13, 700)
    Call(0, 5)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_13_76E5 end

    def Function_14_C29B(): pass

    label("Function_14_C29B")

    SetChrChipByIndex(0x11, 24)
    SetChrSubChip(0x11, 0)
    OP_8F(0xFE, 0x15E, 0xFA0, 0x4B0, 0x1388, 0x0)
    SetChrChipByIndex(0x11, 3)
    SetChrSubChip(0x11, 0)
    OP_8C(0x11, 180, 600)
    Sleep(300)
    OP_8C(0x11, 0, 600)
    Sleep(500)
    Return()

    # Function_14_C29B end

    def Function_15_C2DC(): pass

    label("Function_15_C2DC")

    OP_8C(0xFE, 315, 400)
    OP_8F(0xFE, 0x8E8, 0xFA0, 0xFFFFF8C6, 0x5DC, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_15_C2DC end

    def Function_16_C2FF(): pass

    label("Function_16_C2FF")


    def lambda_C305():
        OP_95(0xFE, 0x1CC, 0xFA0, 0xFFFFFE0C, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C305)
    WaitChrThread(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    OP_22(0xA4, 0x0, 0x64)
    Return()

    # Function_16_C2FF end

    def Function_17_C332(): pass

    label("Function_17_C332")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D2(0x2602E1, 0x2602E6, 0x13)
    OP_D2(0x7059B, 0x70583, 0x14)
    OP_D2(0x70598, 0x7059D, 0x15)
    LoadEffect(0x0, "map\\mp259_01.eff")
    LoadEffect(0x1, "map\\mp263_00.eff")
    LoadEffect(0x2, "map\\mp263_01.eff")
    LoadEffect(0x3, "map\\mp263_02.eff")
    LoadEffect(0x4, "map\\mp263_03.eff")
    LoadEffect(0x5, "map\\mp263_06.eff")
    LoadEffect(0x6, "map\\mp263_04.eff")
    ClearChrFlags(0x10F, 0x80)
    ClearChrFlags(0x101, 0x80)
    SetChrPos(0x10F, 0, 4000, -1770, 0)
    SetChrPos(0x101, -100, 4000, -3200, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x15, -1100, 4000, -3400, 0)
    SetChrPos(0x1F, 1300, 4000, -3300, 0)
    SetChrPos(0x11, 2300, 4000, -3170, 0)
    SetChrPos(0x12, 1300, 4000, -6500, 0)
    SetChrPos(0x13, 100, 4000, -6500, 0)
    SetChrPos(0x14, 2800, 4000, -5870, 0)
    SetChrPos(0x16, 800, 4000, -4500, 0)
    SetChrPos(0x18, -500, 4000, -4820, 0)
    SetChrPos(0x1E, -1520, 4000, -5000, 0)
    SetChrPos(0x1A, 2200, 4000, -4570, 0)
    SetChrPos(0x1B, 1500, 4000, -5600, 0)
    SetChrPos(0x1C, 3300, 4000, -4960, 0)
    SetChrPos(0x19, -1400, 4000, -6200, 0)
    SetChrFlags(0xF0, 0x80)
    SetChrFlags(0xF1, 0x80)
    OP_6D(-950, 8000, -980, 0)
    OP_67(0, 5890, -10000, 0)
    OP_6B(2200, 0)
    OP_6C(314000, 0)
    OP_6E(388, 0)

    def lambda_C583():
        OP_6D(-950, 4000, -980, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_C583)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x10F, 0x0)
    Sleep(300)

    def lambda_C5AF():
        OP_6D(-1180, 4000, 1800, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C5AF)

    def lambda_C5C7():
        OP_67(0, 5690, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C5C7)

    def lambda_C5DF():
        OP_6B(2450, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C5DF)

    def lambda_C5EF():
        OP_6E(405, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_C5EF)
    OP_8F(0x10F, 0x0, 0xFA0, 0xFFFFFE16, 0x3E8, 0x0)
    WaitChrThread(0x101, 0x0)
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x10F, 19)
    SetChrSubChip(0x10F, 0)
    OP_22(0x8F, 0x0, 0x64)
    Sleep(100)
    ClearChrFlags(0x22, 0x80)
    OP_9F(0x22, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x22, 0x40)
    SetChrFlags(0x22, 0x4)
    SetChrFlags(0x22, 0x1)
    SetChrChipByIndex(0x22, 20)
    SetChrSubChip(0x22, 0)

    def lambda_C65F():

        label("loc_C65F")

        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        OP_48()
        Jump("loc_C65F")

    QueueWorkItem2(0x22, 3, lambda_C65F)
    SetChrPos(0x22, 0, 5100, 100, 0)
    PlayEffect(0x1, 0x0, 0x22, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x22, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)
    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    OP_E5(0x2, 0xFF, 0x13, 1000)
    OP_0D()
    Fade(1000)
    OP_E5(0x2, 0xFF, 0x13, 700)
    OP_0D()

    def lambda_C714():
        OP_8F(0xFE, 0x0, 0x1770, 0x64, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_C714)
    WaitChrThread(0x22, 0x0)
    Sleep(500)

    ChrTalk(    #360
        0x101,
        (
            "#1002F#6P这次发光的样子\x01",
            "和之前的完全不同呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0x15,
        (
            "#1502F#6P嗯……\x01",
            "到底会出现什么人物呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0x16,
        "#1164F#6P………………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    def lambda_C7F1():
        OP_6D(-1180, 4000, 800, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C7F1)

    def lambda_C809():
        TurnDirection(0x101, 0x16, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C809)
    Sleep(100)
    TurnDirection(0x15, 0x16, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #363
        0x101,
        "#1015F#5P科洛丝？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0x15,
        "#1504F#5P怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0x16,
        (
            "#1165F#6P嗯……\x02\x03",

            "#1382F……那道光………\x01",
            "给我一种熟悉的感觉……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0x101,
        "#1004F#5P咦……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    OP_20(0x7D0)
    SetMessageWindowPos(-1, 100, -1, -1)

    AnonymousTalk(    #367
        (
            "\x07\x0C呵呵……\x01",
            "那是当然的。\x07\x00\x02",
        )
    )

    Jump("loc_C91E")

    label("loc_C91E")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x19, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1F, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    def lambda_CAC0():
        OP_8C(0x101, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_CAC0)
    Sleep(100)
    OP_8C(0x15, 0, 400)
    Sleep(500)
    OP_1D(0xB8)
    Fade(1000)
    OP_82(0x85, 0x0)
    OP_79(0xA, 0x2)
    OP_7B()
    OP_6D(0, 6500, 3570, 0)
    OP_67(0, 3130, -10000, 0)
    OP_6B(2460, 0)
    OP_6C(0, 0)
    OP_6E(373, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    SetChrPos(0x10F, 0, 4000, -1600, 0)
    SetChrPos(0x101, -420, 4000, -4019, 0)
    SetChrPos(0x15, -1530, 4000, -4059, 0)
    SetChrPos(0x1F, 550, 4000, -4130, 0)
    SetChrPos(0x11, 1500, 4000, -4140, 0)
    SetChrPos(0x12, 100, 4000, -7500, 0)
    SetChrPos(0x13, -950, 4000, -7660, 0)
    SetChrPos(0x14, 1350, 4000, -7850, 0)
    SetChrPos(0x16, -650, 4000, -5640, 0)
    SetChrPos(0x18, -1700, 4000, -6250, 0)
    SetChrPos(0x1E, -2700, 4000, -6100, 0)
    SetChrPos(0x1A, 2350, 4000, -5100, 0)
    SetChrPos(0x1B, 900, 4000, -6200, 0)
    SetChrPos(0x1C, 2000, 4000, -7100, 0)
    SetChrPos(0x19, -2000, 4000, -8150, 0)
    SetChrPos(0x22, 0, 5500, 1000, 180)
    PlayEffect(0x1, 0x0, 0x22, 0, 600, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x22, 0, 600, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_CCAF():
        OP_6D(0, 7500, 3760, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_CCAF)

    def lambda_CCC7():
        OP_67(0, 1650, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_CCC7)

    def lambda_CCDF():
        OP_6B(2700, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_CCDF)

    def lambda_CCEF():
        OP_6E(363, 3500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CCEF)

    def lambda_CCFF():
        OP_8F(0xFE, 0x0, 0x1F40, 0x5DC, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_CCFF)
    WaitChrThread(0x22, 0x0)
    WaitChrThread(0x10F, 0x0)
    Sleep(500)

    def lambda_CD29():
        OP_6B(2000, 8000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_CD29)

    def lambda_CD39():
        OP_6D(0, 8000, 3760, 8000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_CD39)
    OP_22(0x147, 0x0, 0x64)
    PlayEffect(0x5, 0x2, 0x22, 0, 600, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    OP_23(0x147)
    Fade(500)
    OP_22(0xC, 0x0, 0x64)
    PlayEffect(0x3, 0x2, 0x22, 0, 600, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x0)
    Sleep(300)
    PlayEffect(0x6, 0x3, 0x22, 0, 700, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    Sleep(3000)
    Fade(1000)
    OP_82(0x2, 0x2)
    PlayEffect(0x6, 0x1, 0x22, 0, 700, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)

    def lambda_CE56():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x7D0)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_CE56)
    OP_22(0x99, 0x0, 0x64)
    OP_82(0x3, 0x0)
    OP_0D()
    Sleep(2000)
    PlayEffect(0x4, 0x4, 0x22, 0, 700, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_22(0x138, 0x0, 0x64)
    OP_23(0x146)

    def lambda_CEB3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_CEB3)
    OP_82(0x2, 0x2)
    WaitChrThread(0x22, 0x0)
    PlayEffect(0x0, 0x7, 0x22, 0, 800, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)
    Fade(500)
    OP_82(0x1, 0x0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #368
        0x10F,
        "#1444F#5P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0x101,
        "#1020F#5P哎！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0x15,
        "#1504F#5P这个女性是……！？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(3540, 6000, 2620, 0)
    OP_67(0, 2790, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(35000, 0)
    OP_6E(345, 0)

    def lambda_CFB7():
        OP_6D(3540, 4000, 2620, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_CFB7)

    def lambda_CFCF():
        OP_67(0, 2790, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_CFCF)

    def lambda_CFE7():
        OP_6B(2900, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_CFE7)

    def lambda_CFF7():
        OP_6E(345, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_CFF7)

    def lambda_D007():
        OP_8F(0xFE, 0x0, 0x1388, 0x5DC, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_D007)
    Sleep(1000)
    OP_82(0x2, 0x2)
    WaitChrThread(0x22, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x10F, 0x2)
    Sleep(800)

    NpcTalk(    #371
        0x22,
        "女性的灵魂",
        "\x07\x0C#5P……………………………………\x07\x00\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x22, 21)
    SetChrSubChip(0x22, 0)
    OP_0D()
    Sleep(800)

    NpcTalk(    #372
        0x22,
        "女性的灵魂",
        (
            "\x07\x0C#5P──终于可以这样\x01",
            "和别人直接对话了呢。\x02\x03",

            "呵呵……\x01",
            "已经过了好几百年了吧？\x07\x00\x02",
        )
    )

    Jump("loc_D104")

    label("loc_D104")

    CloseMessageWindow()

    ChrTalk(    #373
        0x12,
        "#173F#11P殿、殿下……不对……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0x16,
        "#1164F#6P……难道……你是………\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x200, 0x96, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x200, 0xFFFFFF, 0x1, "C_VIS439._CH")
    OP_C6(0x0, 0x0, 140000, 0, 500)
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(2000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("女性的灵魂")

    AnonymousTalk(    #375
        (
            "\x07\x0C呵呵……\x01",
            "吾之后裔啊……初次见面，请多关照。\x02\x03",

            "还有这些前来访问庭院的客人……\x01",
            "初次见面，你们好。\x02\x03",

            "──我的名字是赛雷斯托。\x02\x03",

            "赛雷斯托·Ｄ·奥赛雷丝。\x07\x00\x02",
        )
    )

    Jump("loc_D285")

    label("loc_D285")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_44(0x10F, 0x0)
    OP_A2(0x2A09)
    Sleep(2000)
    OP_AD(0x2400F1, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_A2(0x2582)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x15A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C4(0x0, 0x10)
    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        240,
        180,
        0,
        (
            "【保存】\x01",              # 0
            "【继续下面剧情】\x01",      # 1
        )
    )

    Jump("loc_D325")

    label("loc_D325")

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D339")
    ShowSaveMenu()

    label("loc_D339")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_AE(0xC8)
    Sleep(2000)
    OP_20(0x7D0)
    OP_21()
    Sleep(2000)
    OP_C4(0x1, 0x10)
    OP_A3(0x2582)
    OP_4F(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x2505)
    OP_A2(0x2509)
    NewScene("ED6_DT21/U7000   ._SN", 104, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_17_C332 end

    SaveToFile()

Try(main)
