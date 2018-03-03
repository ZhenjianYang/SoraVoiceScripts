from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        '@FileName',                            # 8
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
        "Function_3_1DF5",         # 03, 3
        "Function_4_1E32",         # 04, 4
        "Function_5_1E67",         # 05, 5
        "Function_6_1E88",         # 06, 6
        "Function_7_1EB5",         # 07, 7
        "Function_8_1EE4",         # 08, 8
        "Function_9_1F21",         # 09, 9
        "Function_10_525F",        # 0A, 10
        "Function_11_588E",        # 0B, 11
        "Function_12_8530",        # 0C, 12
        "Function_13_8B71",        # 0D, 13
        "Function_14_E1EE",        # 0E, 14
        "Function_15_E22F",        # 0F, 15
        "Function_16_E252",        # 10, 16
        "Function_17_E285",        # 11, 17
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
        "#067F#6PYaaay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x16,
        "#1168F#6PHere she comes...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    PlayEffect(0x4, 0x4, 0x1D, -300, 300, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_22(0x138, 0x0, 0x64)
    OP_23(0x146)

    def lambda_96E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_96E)
    OP_82(0x2, 0x2)
    WaitChrThread(0x1D, 0x0)
    Fade(500)
    OP_82(0x1, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #2
        0x1D,
        "#1007F#5PWh-What just happened...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x102,
        "#1501F#12PHey, Estelle...\x02",
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
            "#1005F#5PAre you okay, Joshua?!\x02\x03",

            "What was that light, anyway?!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #5
        0x1D,
        "#1004F#5P...Huh?\x02",
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
            "#1512F#12PYeah, I'm not surprised you're feeling kind of\x01",
            "bewildered right now.\x02\x03",

            "#1514FNot every day you find yourself in a situation\x01",
            "like this.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1D)
    Sleep(500)

    ChrTalk(    #7
        0x1D,
        "#1019F#5PYou can say that again...\x02",
    )

    CloseMessageWindow()

    def lambda_B7A():
        OP_6D(1190, 4000, 1200, 2500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B7A)

    def lambda_B92():
        OP_67(300, 4330, -10300, 2500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B92)

    def lambda_BAA():
        OP_6B(3300, 2500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_BAA)

    def lambda_BBA():
        OP_6E(290, 2500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_BBA)
    OP_43(0x102, 0x0, 0x3, 0x7)
    Sleep(600)

    def lambda_BD6():
        OP_8F(0xFE, 0xFFFFF95C, 0xFA0, 0xFFFFFA4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_BD6)
    Sleep(50)

    def lambda_BF6():
        OP_8F(0xFE, 0xFFFFFC36, 0xFA0, 0xFFFFF7EA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_BF6)
    Sleep(100)

    def lambda_C16():
        OP_8F(0xFE, 0x122, 0xFA0, 0xFFFFF8D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_C16)
    Sleep(50)

    def lambda_C36():
        OP_8F(0xFE, 0x3C, 0xFA0, 0xFFFFF380, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_C36)
    Sleep(50)

    def lambda_C56():
        OP_8F(0xFE, 0xFFFFFA06, 0xFA0, 0xFFFFF240, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_C56)
    Sleep(50)

    def lambda_C76():
        OP_8F(0xFE, 0xFFFFF31C, 0xFA0, 0xFFFFED04, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_C76)
    Sleep(50)

    def lambda_C96():
        OP_8F(0xFE, 0xFFFFF51A, 0xFA0, 0xFFFFF20E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_C96)

    def lambda_CB1():
        OP_8F(0xFE, 0xFFFFF768, 0xFA0, 0xFFFFECDC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_CB1)
    Sleep(50)

    def lambda_CD1():
        OP_8F(0xFE, 0xFFFFFB50, 0xFA0, 0xFFFFEAF2, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_CD1)

    def lambda_CEC():
        OP_8F(0xFE, 0xFFFFFF9C, 0xFA0, 0xFFFFEDA4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_CEC)
    Sleep(1500)
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #8
        0x11,
        "#066F#6PI've missed you, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x16,
        "#1168F#6PHeehee. Same here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x1D,
        (
            "#1008F#5PYou guys've missed ME? I've missed YOU!\x02\x03",

            "#1016FAhaha... I'm feeling all emotional all of a sudden.\x02\x03",

            "#1017FThere're so many faces I haven't seen in ages here,\x01",
            "I'm not sure where to start. And a few who've done\x01",
            "a total 180 since I've last seen them, too!\x02\x03",

            "#1008FI mean, wow, Olivier! You look all...princely all of a\x01",
            "sudden!\x02\x03",

            "And when did you cut your hair, Schera?\x02\x03",

            "And is that a new outfit? It's so...daring...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x1B,
        "#1536F#12PHaha. I've taken quite a liking to it, myself.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x18,
        (
            "#1541F#6PI have to say, I still prefer that old white coat.\x01",
            "I feel much more at home in it than this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x1D,
        "#1017F#5PEveryone else is same old, same old, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x1C,
        (
            "#051F#6PWell, sorry for not breaking the bank on\x01",
            "some new getup for you to gawk at.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x19,
        (
            "#071F#12PHaha... These clothes are practically my\x01",
            "work uniform at this point. It'd take a lot\x01",
            "to get me to change them!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x1A,
        "#811F#6PAww, man! It's so good to see you again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x14,
        (
            "#413F#6PYou don't look like you've changed at all.\x01",
            "You're still a total airhead from where I'm\x01",
            "standing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x1D,
        (
            "#1004F#5PAnelace! You're here, too!\x02\x03",

            "#1022FAnd as for YOU, Josette...\x02\x01",

            "#1019F...can you quit calling me a damn airhead?\x01",
            "In case you were raised in a barn, that's not\x01",
            "a very nice way to greet someone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x14,
        (
            "#210F#6PWhat? I was only telling the truth.\x02\x03",

            "#211FSounds like you're always a huge pain\x01",
            "in the butt for poor Joshua!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1D, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #20
        0x1D,
        (
            "#1013F#5PO-Okay, I'll give you sometimes, but always?\x02\x03",

            "#1022FActually, you know what? Scratch that!\x01",
            "It's none of your business!\x02\x03",

            "#1008FWow, though. Even the captain and major\x01",
            "are here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x12,
        "#171F#6PIt's lovely to see you, too, Estelle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x13,
        "#277F#12PIt's been quite some time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x1D,
        "#1016F#5PMan, this is the best reunion party ever...\x02",
    )

    CloseMessageWindow()
    OP_62(0x1D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1429():
        OP_6D(120, 4000, 1980, 1000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1429)

    def lambda_1441():
        OP_6C(40000, 1000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1441)
    OP_8C(0x1D, 225, 400)
    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #24
        0x109,
        "#1066F#6P#40WHaha. Don't forget about me, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x1D,
        (
            "#1008F#5PKevin?!\x02\x03",

            "#1004FI don't recognize the person with you,\x01",
            "though. Umm... Hi. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x20,
        (
            "#1446F#6PHello. I'm Ries Argent, a squire of the Gralsritter.\x02\x03",

            "#1448FKevin's told me quite a lot about you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x1D,
        (
            "#1011F#5PHe has, huh?\x02\x01",

            "#1001FIt's nice to meet you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x109,
        (
            "#1075F#6P#40WYou really are a special girl, Estelle...\x02\x03",

            "#1840FJust having you here brightens up the\x01",
            "room...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x1D,
        (
            "#1016F#5PY-You really think so?\x02\x03",

            "#1015F...Hey, are you okay?\x02\x03",

            "You look a little pale...\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)

    ChrTalk(    #30
        0x20,
        "#1444F#6P...What?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x20, 0, 400)
    OP_9E(0x109, 0xF, 0x0, 0x12C, 0xBB8)

    ChrTalk(    #31
        0x109,
        "#1070F#5P#40WGah...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(-4950, 4000, -1390, 0)
    OP_67(300, 5050, -10300, 0)
    OP_6B(2900, 0)
    OP_6C(240000, 0)
    OP_6E(298, 0)

    def lambda_16FC():
        OP_6B(2800, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_16FC)
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

    def lambda_1810():

        label("loc_1810")

        OP_8C(0x20, 0, 600)
        OP_48()
        Jump("loc_1810")

    QueueWorkItem2(0x20, 3, lambda_1810)
    Sleep(50)

    def lambda_1826():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1826)

    def lambda_1834():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_1834)
    Sleep(50)

    def lambda_1847():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x16, 3, lambda_1847)

    def lambda_1855():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x1B, 3, lambda_1855)
    Sleep(50)

    def lambda_1868():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_1868)

    def lambda_1876():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_1876)
    Sleep(50)

    def lambda_1889():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_1889)

    def lambda_1897():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x18, 3, lambda_1897)
    Sleep(50)

    def lambda_18AA():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_18AA)

    def lambda_18B8():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x19, 3, lambda_18B8)
    Sleep(50)

    def lambda_18CB():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x1C, 3, lambda_18CB)

    def lambda_18D9():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_18D9)
    OP_0D()
    Sleep(500)

    ChrTalk(    #32
        0x20,
        "#1802F#3S#5P...?!\x02",
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
            "#1076F#12P#50WSorry...Ries... Gonna have to take a\x01",
            "rain check on our talk...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #34
        "\x07\x05Kevin handed the cube to Ries.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(500)

    NpcTalk(    #35
        0x10,
        "Ries",
        "#1444F#5PWhat are you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x109,
        (
            "#1076F#12P#50WI'll leave things to you...for a while...\x02\x03",

            "Keep moving...on...\x02",
        )
    )

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
        "Ries",
        "#1449F#3S#5PKevin?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #38
        0x1D,
        "#1020F#6PK-Kevin?!\x02",
    )

    CloseMessageWindow()

    def lambda_1C38():
        OP_6B(2700, 10000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1C38)
    OP_43(0x1D, 0x1, 0x3, 0x5)
    OP_43(0x102, 0x3, 0x3, 0x4)
    WaitChrThread(0x20, 0x1)
    WaitChrThread(0x1D, 0x1)
    WaitChrThread(0x102, 0x1)
    Sleep(500)

    ChrTalk(    #39
        0x102,
        "#1506F#6PUgh... Is this because of that thing he did?!\x02",
    )

    CloseMessageWindow()
    OP_62(0x1D, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #40
        0x1D,
        "#1026F#12PWh-What thing? What's going on?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #41
        0x10,
        "Ries",
        (
            "#1802F#5PKevin!\x02\x03",

            "Wake up! Kevin!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_44(0x20, 0x0)
    Sleep(2000)
    OP_A2(0x2910)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D3B")
    OP_A2(0x265D)

    label("loc_1D3B")

    OP_AD(0x2400F0, 0x0, 0x0, 0x64)
    OP_F7(0x4, 0x0, 0x0)
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
            "[Save]\x01",              # 0
            "[Next Chapter]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DAC")
    ShowSaveMenu()

    label("loc_1DAC")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    def Function_3_1DF5(): pass

    label("Function_3_1DF5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1E31")
    OP_9E(0x109, 0xF, 0x0, 0x12C, 0x7D0)
    Sleep(1000)
    OP_9E(0x109, 0xF, 0x0, 0x12C, 0x7D0)
    Sleep(1500)
    Jump("Function_3_1DF5")

    label("loc_1E31")

    Return()

    # Function_3_1DF5 end

    def Function_4_1E32(): pass

    label("Function_4_1E32")

    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0x3F2, 0xFA0, 0xFFFFFFCE, 0x1388, 0x0)
    OP_8C(0xFE, 270, 0)
    OP_8F(0xFE, 0xFFFFFA24, 0xFA0, 0x0, 0x1388, 0x0)
    Return()

    # Function_4_1E32 end

    def Function_5_1E67(): pass

    label("Function_5_1E67")

    SetChrFlags(0xFE, 0x40)
    OP_8F(0xFE, 0xFFFFF416, 0xFA0, 0x4E2, 0x1388, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_5_1E67 end

    def Function_6_1E88(): pass

    label("Function_6_1E88")

    SetChrFlags(0x20, 0x40)
    OP_62(0x20, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Fade(250)
    SetChrChipByIndex(0x20, 24)
    SetChrSubChip(0x20, 0)
    OP_0D()
    Sleep(300)
    Return()

    # Function_6_1E88 end

    def Function_7_1EB5(): pass

    label("Function_7_1EB5")


    def lambda_1EBB():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1EBB)
    Sleep(200)
    OP_8F(0xFE, 0x514, 0xFA0, 0xFFFFFE70, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_7_1EB5 end

    def Function_8_1EE4(): pass

    label("Function_8_1EE4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F20")
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1000)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1500)
    Jump("Function_8_1EE4")

    label("loc_1F20")

    Return()

    # Function_8_1EE4 end

    def Function_9_1F21(): pass

    label("Function_9_1F21")

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
            "#1007F#11PWow... So that's what happened...\x02\x03",

            "#1015FThe more I hear, the more off the wall\x01",
            "everything happening here sounds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x15,
        (
            "#1505F#5PI'm not surprised. We're making progress on\x01",
            "working out what's going on, thankfully.\x02\x03",

            "#1503FWe know the place we're in is called Phantasma\x01",
            "and about how it has its own unique rules that\x01",
            "govern it.\x02\x03",

            "#1502FWe also know that all of us were chosen based\x01",
            "on some criteria then drawn into it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x18,
        (
            "#1540F#6PWe still have plenty of questions that need\x01",
            "answering, but they can largely be summed\x01",
            "up by the following three:\x02\x03",

            "#1545FOne: Who are the Lord of Phantasma and \x01",
            "Schwarzritter?\x02\x03",

            "Two: What is the cube and the identity of the\x01",
            "ghost who appears to be connected to it?\x02\x03",

            "#1540FThree: What is Phantasma, and how did it come\x01",
            "to exist?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x11,
        "#065F#6PThat's a pretty succinct way of putting it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x16,
        (
            "#1162F#6PThere are other questions, of course,\x01",
            "but it's true that most of those generally\x01",
            "fall under those three in some way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x19,
        (
            "#070F#6PWhy there are fiends roaming around comes\x01",
            "under number three, for example.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x1D,
        (
            "#1006F#11PDividing everything up like that does make it\x01",
            "all a heck of a lot easier to understand, yeah.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1D, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #49
        0x1D,
        (
            "#1004F#11POh, but wait...\x02\x03",

            "Where does Kevin falling unconscious come into\x01",
            "all of this?\x02\x03",

            "#1015FYou made it sound like the cause of that was him\x01",
            "fighting some giant devil.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26E4")

    ChrTalk(    #50
        0x1C,
        (
            "#053F#6PFrom what we can tell, anyway. More specifically,\x01",
            "the power he used to break the barrier surrounding\x01",
            "us seems to have been what did it.\x02\x03",

            "#555FThe one that made that red symbol show up\x01",
            "on his back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D23")

    label("loc_26E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2797")

    ChrTalk(    #51
        0x11,
        (
            "#561F#6PYeah. It seemed like the power he used to save\x01",
            "us when we were trapped in that barrier.\x02\x03",

            "#063FThe one that made that red symbol show up\x01",
            "on his back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D23")

    label("loc_2797")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2878")

    ChrTalk(    #52
        0x16,
        (
            "#1167F#6PIt certainly seems that way. More specifically,\x01",
            "the power he used to break the barrier that\x01",
            "surrounded us must have been the cause.\x02\x03",

            "#1163FThe one that made that red symbol show up\x01",
            "on his back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D23")

    label("loc_2878")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2957")

    ChrTalk(    #53
        0x12,
        (
            "#176F#6PIt certainly seems that way. More specifically,\x01",
            "the power he used to break the barrier that\x01",
            "surrounded us must have been the cause.\x02\x03",

            "#178FThe one that made that red symbol show up\x01",
            "on his back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D23")

    label("loc_2957")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A36")

    ChrTalk(    #54
        0x13,
        (
            "#272F#6PIt certainly seems that way. More specifically,\x01",
            "the power he used to break the barrier that\x01",
            "surrounded us must have been the cause.\x02\x03",

            "#270FThe one that made that red symbol show up\x01",
            "on his back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D23")

    label("loc_2A36")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AEA")

    ChrTalk(    #55
        0x1A,
        (
            "#817F#6PYeah. It's kinda like the power he used to save\x01",
            "us when we were trapped in that barrier.\x02\x03",

            "#813FThe one that made that red symbol show up\x01",
            "on his back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D23")

    label("loc_2AEA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BAF")

    ChrTalk(    #56
        0x1B,
        (
            "#1526F#6PSeems that way. Specifically, the power he used\x01",
            "to break the barrier that surrounded us is what\x01",
            "did it.\x02\x03",

            "#1522FThe one that made that red symbol show up\x01",
            "on his back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D23")

    label("loc_2BAF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C63")

    ChrTalk(    #57
        0x14,
        (
            "#416F#6PYeah. It's kinda like the power he used to save\x01",
            "us when we were trapped in that barrier.\x02\x03",

            "#212FThe one that made that red symbol show up\x01",
            "on his back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D23")

    label("loc_2C63")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D23")

    ChrTalk(    #58
        0x19,
        (
            "#074F#6PSeems that way. Specifically, the power he used\x01",
            "to break the barrier that surrounded us is what\x01",
            "did it.\x02\x03",

            "#072FThe one that made that red symbol show up\x01",
            "on his back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D23")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DE3")

    ChrTalk(    #59
        0x18,
        (
            "#1544F#6PI haven't got any idea what it was, either...\x02\x03",

            "#1542FIt's possible it may be some form of Thaumaturgy \x01",
            "passed down through the church, but I can hardly\x01",
            "be sure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FB2")

    label("loc_2DE3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E1D")

    ChrTalk(    #60
        0x19,
        "#072F#6PI wonder what it was, then?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FB2")

    label("loc_2E1D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E57")

    ChrTalk(    #61
        0x14,
        "#212F#6PI wonder what it was, then?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FB2")

    label("loc_2E57")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E92")

    ChrTalk(    #62
        0x1B,
        "#1522F#6PI wonder what it was, then?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FB2")

    label("loc_2E92")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2ECC")

    ChrTalk(    #63
        0x1A,
        "#812F#6PI wonder what it was, then?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FB2")

    label("loc_2ECC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F06")

    ChrTalk(    #64
        0x13,
        "#270F#6PI wonder what it was, then?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FB2")

    label("loc_2F06")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F40")

    ChrTalk(    #65
        0x12,
        "#178F#6PI wonder what it was, then?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FB2")

    label("loc_2F40")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F7B")

    ChrTalk(    #66
        0x16,
        "#1163F#6PI wonder what it was, then?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FB2")

    label("loc_2F7B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FB2")

    ChrTalk(    #67
        0x11,
        "#063F#6PI wonder what it was, then?\x02",
    )

    CloseMessageWindow()

    label("loc_2FB2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_307B")

    ChrTalk(    #68
        0x18,
        (
            "#1544F#6PI haven't got any idea what it could have been,\x01",
            "either...\x02\x03",

            "#1542FIt's possible it may be some form of Thaumaturgy \x01",
            "passed down through the church, but I can hardly\x01",
            "be sure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_307B")


    ChrTalk(    #69
        0x15,
        "#1503F#5P...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x1D, 270, 400)
    Sleep(300)

    ChrTalk(    #70
        0x1D,
        (
            "#1004F#12PJoshua?\x02\x03",

            "#1002FDo you think you know what it could've been?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x15,
        (
            "#1505F#5P...I think I do.\x02\x03",

            "#1503FI can't be sure, but I think it was a Stigma.\x02",
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
        "#1020F#12PSeriously?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x14,
        (
            "#214F#6PIsn't that the thing that appeared\x01",
            "on your shoulder?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x15,
        (
            "#1503F#5PYeah, it was.\x02\x03",

            "#1505FWhat you saw was a physical manifestation of an\x01",
            "image Weissmann had placed deep within my mind \x01",
            "in order to control me.\x02\x03",

            "Kevin's is likely the same, save the control factor.\x02\x03",

            "#1502FHowever, I have a feeling his is also significantly\x01",
            "more powerful than mine was.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #75
        0x20,
        "Girl's Voice",
        "#2PWell spotted, Joshua.\x02",
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

    def lambda_353C():
        OP_6D(-210, 4200, -1250, 3000)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_353C)

    def lambda_3554():
        OP_67(0, 5850, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_3554)

    def lambda_356C():
        OP_6B(2230, 3000)
        ExitThread()

    QueueWorkItem(0x1D, 3, lambda_356C)

    def lambda_357C():
        OP_6E(375, 3000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_357C)

    def lambda_358C():
        OP_8F(0xFE, 0x550, 0xFA0, 0xFFFFEA20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_358C)

    def lambda_35A7():

        label("loc_35A7")

        TurnDirection(0xFE, 0x20, 400)
        OP_48()
        Jump("loc_35A7")

    QueueWorkItem2(0x1D, 1, lambda_35A7)
    Sleep(50)

    def lambda_35BD():

        label("loc_35BD")

        TurnDirection(0xFE, 0x20, 400)
        OP_48()
        Jump("loc_35BD")

    QueueWorkItem2(0x15, 1, lambda_35BD)
    Sleep(50)

    def lambda_35D3():

        label("loc_35D3")

        TurnDirection(0xFE, 0x20, 400)
        OP_48()
        Jump("loc_35D3")

    QueueWorkItem2(0x11, 1, lambda_35D3)
    Sleep(50)

    def lambda_35E9():

        label("loc_35E9")

        TurnDirection(0xFE, 0x20, 400)
        OP_48()
        Jump("loc_35E9")

    QueueWorkItem2(0x19, 1, lambda_35E9)
    Sleep(50)

    def lambda_35FF():

        label("loc_35FF")

        TurnDirection(0xFE, 0x20, 400)
        OP_48()
        Jump("loc_35FF")

    QueueWorkItem2(0x12, 1, lambda_35FF)
    Sleep(50)

    def lambda_3615():

        label("loc_3615")

        TurnDirection(0xFE, 0x20, 400)
        OP_48()
        Jump("loc_3615")

    QueueWorkItem2(0x16, 1, lambda_3615)
    Sleep(50)

    def lambda_362B():

        label("loc_362B")

        TurnDirection(0xFE, 0x20, 400)
        OP_48()
        Jump("loc_362B")

    QueueWorkItem2(0x13, 1, lambda_362B)
    Sleep(50)

    def lambda_3641():

        label("loc_3641")

        TurnDirection(0xFE, 0x20, 400)
        OP_48()
        Jump("loc_3641")

    QueueWorkItem2(0x18, 1, lambda_3641)
    Sleep(50)

    def lambda_3657():

        label("loc_3657")

        TurnDirection(0xFE, 0x20, 400)
        OP_48()
        Jump("loc_3657")

    QueueWorkItem2(0x1B, 1, lambda_3657)
    Sleep(50)

    def lambda_366D():

        label("loc_366D")

        TurnDirection(0xFE, 0x20, 400)
        OP_48()
        Jump("loc_366D")

    QueueWorkItem2(0x1A, 1, lambda_366D)
    Sleep(50)

    def lambda_3683():

        label("loc_3683")

        TurnDirection(0xFE, 0x20, 400)
        OP_48()
        Jump("loc_3683")

    QueueWorkItem2(0x14, 1, lambda_3683)
    Sleep(50)

    def lambda_3699():

        label("loc_3699")

        TurnDirection(0xFE, 0x20, 400)
        OP_48()
        Jump("loc_3699")

    QueueWorkItem2(0x1C, 1, lambda_3699)
    Sleep(1000)

    def lambda_36AF():
        OP_8F(0xFE, 0xFFFFFC90, 0xFA0, 0xFFFFF254, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_36AF)
    Sleep(50)

    def lambda_36CF():
        OP_8F(0xFE, 0x9B0, 0xFA0, 0xFFFFF0F6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_36CF)
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
        "#1504F#12PRies?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x1D,
        "#1015F#6PSay...how's Kevin doing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x20,
        (
            "#1446F#5PHis condition seems to have marginally improved.\x02\x03",

            "#1806FBut what he did resulted in a heavy burden being\x01",
            "placed on his mind, so I think it would be best for\x01",
            "him to rest for a while longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x1D,
        "#1025F#6PThat's a relief...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x1B,
        "#1525F#6PWhew... He sure knows how to give people a fright.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x15,
        (
            "#1503F#12PDo you mind if I get clarification on something,\x01",
            "Ries?\x02\x03",

            "#1502FWas my theory correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x20,
        (
            "#1446F#5PYes, it was. He did indeed use the power\x01",
            "of his Stigma.\x02\x03",

            "#1443FHowever, the key difference between his\x01",
            "and yours is that his is one of the original\x01",
            "kind--on which yours was likely based.\x02\x03",

            "A seal carved into a person's very soul,\x01",
            "said to manifest only in the Dominions of\x01",
            "the Gralsritter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x1D,
        "#1004F#6PWhat's a Dominion?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x18,
        (
            "#1545F#6PI've heard rumors of their existence, personally.\x02\x03",

            "#1540FThe Dominions are a group of twelve knights\x01",
            "who lead the Gralsritter.\x02\x03",

            "They're supposed to possess incredible power.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x20,
        (
            "#1446F#5PThat's also correct.\x02\x03",

            "#1445FTheir Stigmas are the source of that power.\x02\x03",

            "They allow the people who possess them\x01",
            "to strengthen their body beyond what most\x01",
            "would think humanly possible...\x02\x03",

            "#1446F...as well as use high-level Thaumaturgy far\x01",
            "exceeding the capabilities of other knights.\x02\x03",

            "#1443FAs I'm sure you've pieced together, Kevin is\x01",
            "one of them. Specifically, the Fifth Dominion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x1A,
        (
            "#1317F#6PA-Are we even talking about the same Kevin\x01",
            "who's been leading us around here? It sure\x01",
            "doesn't feel like it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x16,
        (
            "#1163F#12PSorry, but I'm a bit confused. Did Kevin have his\x01",
            "Stigma implanted within him like Joshua did?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x20,
        (
            "#1446F#5PNo. Ordinarily, Stigmas aren't carved in that\x01",
            "manner. They appear on their own without\x01",
            "human intervention.\x02\x03",

            "There are twelve Dominions, and that number\x01",
            "has always been consistent throughout history.\x02\x03",

            "#1440FThere are times when spots are left unfilled\x01",
            "because a Stigma bearer to fill them has yet \x01",
            "to appear...\x02\x03",

            "...but they're always out there, whether their \x01",
            "Stigma has manifested or not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x1D,
        (
            "#1007F#6PTh-That's so weird, don't you think?\x02\x03",

            "#1004FSo does that mean the Stigma Joshua had...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x15,
        (
            "#1503F#12PMine was only a replica of the real thing.\x02\x03",

            "#1502FWeissmann was originally a clergyman, so he\x01",
            "probably had access to a way to make such a\x01",
            "thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x1D,
        "#1015F#6POh, yeah. I forgot he said that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x20,
        (
            "#1446F#5PHe used to be a bishop in the Congregation for \x01",
            "the Sacraments, which is the organization that\x01",
            "the Gralsritter answers to.\x02\x03",

            "Even back in those days, he was in contact with\x01",
            "Ouroboros and stealing numerous sacraments\x01",
            "from the church.\x02\x03",

            "#1445FThings that were stolen included a vast amount\x01",
            "of literature and research on the Stigmas of the\x01",
            "Dominions.\x02\x03",

            "#1443FWe believe he then went on to use that material\x01",
            "as a basis to realize his dream of creating some\x01",
            "sort of 'superhuman' over with the society.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x15,
        "#1505F#12PI thought so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x18,
        (
            "#1544F#6PHmm... Still, while I think I have a vague \x01",
            "understanding of just what these Stigmas\x01",
            "are now...\x02\x03",

            "#1542F...I'm still not clear how using that power led\x01",
            "Kevin to collapse.\x02\x03",

            "Does that risk naturally come with the use\x01",
            "of your Stigma's power, or is there something\x01",
            "more to it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x20,
        (
            "#1802F#5PWell...\x02\x03",

            "#1445F...I don't know exactly why, but Kevin very\x01",
            "rarely uses the power of his Stigma at all.\x02\x03",

            "I've heard that the only time he relies on it is \x01",
            "when disposing of those he brands heretics.\x02\x03",

            "#1446FIn other words, those whose sins are too great\x01",
            "for them to ever be able to walk the path of\x01",
            "righteousness ever again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x11,
        "#065F#6PD-Disposing of?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x14,
        "#212F#12PThat's so ominous...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x1C,
        (
            "#551F#6PSo let me make sure I got this straight.\x02\x03",

            "#555FHe used a superpower he barely uses outta\x01",
            "nowhere, and that caused him to black out\x01",
            "because his body wasn't ready for it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x20,
        "#1445F#5PThat's what I believe is likely the case.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x12,
        (
            "#176F#12PI see... I think I understand well enough now.\x02\x03",

            "#178FAre you sure it's fine for you to be telling us\x01",
            "this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x20,
        (
            "#1447F#5PYes. I'm almost positive Kevin was planning on\x01",
            "telling you himself before he fell unconscious.\x02\x03",

            "#1448FAnd I believe telling you all of this is necessary\x01",
            "in order to ensure your cooperation in the rest\x01",
            "of our investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x1D,
        (
            "#1025F#6PWell, if you're sure...\x02\x03",

            "#1004FWait! Does that mean...?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x20,
        (
            "#1447F#5PIf no one has any objections, I'd like to take\x01",
            "Kevin's place and lead till he wakes up again.\x02\x03",

            "#1448FIs that all right with everyone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x19,
        "#070F#11PNo problems here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x11,
        (
            "#065F#6PAre you sure you don't want to stay here, \x01",
            "though?\x02\x03",

            "I would've thought you'd want to stay and\x01",
            "look after him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x20,
        (
            "#1446F#5PBefore he collapsed, Kevin entrusted me with\x01",
            "the cube.\x02\x03",

            "#1448FAs such, I believe this is my duty as a squire in\x01",
            "his service.\x02\x03",

            "So please, don't worry about me. Right now,\x01",
            "I'd much rather be helping all of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x11,
        "#063F#6PWell, if you're sure...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x13,
        "#272F#6PI personally see no reason to say no.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x16,
        (
            "#1382F#12PThe remaining members will be sure to look\x01",
            "after Kevin.\x02\x03",

            "You won't have to worry about a thing, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x20,
        "#1806F#5PThank you... I appreciate that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x1D,
        "#1015F#6P...\x02",
    )

    CloseMessageWindow()

    def lambda_4BE5():
        OP_6D(-800, 4000, -3000, 800)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_4BE5)
    OP_8C(0x15, 90, 400)
    WaitChrThread(0x1D, 0x0)
    Sleep(300)

    ChrTalk(    #112
        0x15,
        "#1504F#11P...? What's wrong, Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x1D,
        (
            "#1007F#6PWell...\x02\x03",

            "#1006FSo...Ries? I've got a favor I want to ask,\x01",
            "if you don't mind.\x02\x03",

            "Would you mind if I came with you when\x01",
            "you head out to explore?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x20,
        "#1444F#5PHmm? Is there any specific reason?\x02",
    )

    CloseMessageWindow()

    def lambda_4D06():
        TurnDirection(0xFE, 0x1D, 400)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_4D06)

    def lambda_4D14():
        TurnDirection(0xFE, 0x1D, 400)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_4D14)

    def lambda_4D22():
        TurnDirection(0xFE, 0x1D, 400)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_4D22)
    Sleep(50)

    def lambda_4D35():
        TurnDirection(0xFE, 0x1D, 400)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_4D35)

    def lambda_4D43():
        TurnDirection(0xFE, 0x1D, 400)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_4D43)

    def lambda_4D51():
        TurnDirection(0xFE, 0x1D, 400)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_4D51)

    def lambda_4D5F():
        TurnDirection(0xFE, 0x1D, 400)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_4D5F)
    Sleep(50)

    def lambda_4D72():
        TurnDirection(0xFE, 0x1D, 400)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_4D72)

    def lambda_4D80():
        TurnDirection(0xFE, 0x1D, 400)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_4D80)

    def lambda_4D8E():
        TurnDirection(0xFE, 0x1D, 400)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_4D8E)
    Sleep(700)

    ChrTalk(    #115
        0x15,
        "#1504F#11PEstelle...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x1D,
        (
            "#1018F#6PWell, it's just...I've only just returned to the\x01",
            "world of the living, right? I feel like I want to\x01",
            "go and see what's going on for myself.\x02\x03",

            "And I mean, I am a bracer, so I doubt I'll get\x01",
            "in your way or anything...\x02\x03",

            "#1016F#6PSo...would you mind?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x20,
        (
            "#1444F#5P...\x02\x03",

            "#1447FNot in the least.\x02\x03",

            "#1806FI'd love it if you accompanied me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x1D,
        "#1017F#6PHeehee. Thanks!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x1D, 270, 400)
    Sleep(300)

    ChrTalk(    #119
        0x1D,
        (
            "#1007F#6PSorry for up and deciding that on my own,\x01",
            "Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x15,
        (
            "#1504F#11PSorry? For what?\x02\x01",

            "#1513FIf that's what you want to do, then you\x01",
            "won't hear any complaints from me.\x02\x03",

            "#1500FWe'll be counting on you to do a good\x01",
            "job backing Ries up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x1D,
        "#1006F#6PYou know it!\x02",
    )

    CloseMessageWindow()

    def lambda_504C():
        OP_6B(3000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_504C)
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

    # Function_9_1F21 end

    def Function_10_525F(): pass

    label("Function_10_525F")

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

    def lambda_548A():
        OP_6D(-1180, 4000, 2780, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_548A)

    def lambda_54A2():
        OP_67(0, 5490, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_54A2)

    def lambda_54BA():
        OP_6B(2400, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_54BA)

    def lambda_54CA():
        OP_6E(403, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_54CA)
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

    def lambda_55DC():
        OP_8F(0xFE, 0x0, 0x1770, 0x64, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_55DC)
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

    def lambda_572A():
        OP_6D(0, 7500, 3760, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_572A)

    def lambda_5742():
        OP_67(0, 1650, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_5742)

    def lambda_575A():
        OP_6B(2700, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_575A)

    def lambda_576A():
        OP_6E(363, 3500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_576A)

    def lambda_577A():
        OP_8F(0xFE, 0x0, 0x2134, 0xAF0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_577A)
    WaitChrThread(0x1E, 0x0)
    WaitChrThread(0x10F, 0x0)
    Sleep(500)

    def lambda_57A4():
        OP_6B(2000, 8000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_57A4)
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

    # Function_10_525F end

    def Function_11_588E(): pass

    label("Function_11_588E")

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

    def lambda_5AF6():
        OP_6D(-410, 4000, 1030, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_5AF6)

    def lambda_5B0E():
        OP_67(0, 4850, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_5B0E)

    def lambda_5B26():
        OP_6B(3200, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_5B26)

    def lambda_5B36():
        OP_6E(327, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_5B36)

    def lambda_5B46():
        OP_8F(0xFE, 0x186, 0xFA0, 0x866, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_5B46)
    WaitChrThread(0x1E, 0x0)
    SetChrSubChip(0x1E, 0)
    WaitChrThread(0x10F, 0x0)
    Sleep(500)
    Fade(1000)
    PlayEffect(0x6, 0x1, 0x1E, 400, 300, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)

    def lambda_5BAF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_5BAF)
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
        "#1004F#6P...What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x15,
        "#1504F#6PThat looks like...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x12,
        "#173F#6PI-It couldn't be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x1A,
        "#1310F#6PCould it?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x1C,
        "#055F#6PYou've gotta be kidding me...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    PlayEffect(0x4, 0x4, 0x1E, 400, 300, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_22(0x138, 0x0, 0x64)
    OP_23(0x146)

    def lambda_5DF7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_5DF7)
    OP_82(0x2, 0x2)
    WaitChrThread(0x1E, 0x0)
    Fade(500)
    OP_82(0x1, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #127
        0x1E,
        "#116F#5PUgh... A stun grenade?!\x02",
    )

    CloseMessageWindow()
    OP_9E(0x1E, 0x14, 0x0, 0x12C, 0xBB8)
    OP_22(0xA3, 0x0, 0x64)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x1E, 22)
    SetChrSubChip(0x1E, 0)

    def lambda_5E6B():
        OP_96(0xFE, 0x122, 0xFA0, 0xBB8, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_5E6B)
    WaitChrThread(0x1E, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    ClearChrFlags(0x10, 0x80)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10, 290, 3600, 2600, 180)

    ChrTalk(    #128
        0x1E,
        "#114F#11P#3SWho goes there?! Speak your name!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #129
        0x1E,
        (
            "#113F#11P...What?\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x101,
        "#1016F#6PAhaha... I sure didn't see THIS coming.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x10F,
        (
            "#1440F#6PI presume you're all familiar with this man?\x02\x03",

            "All I can tell by the uniform is that he's from\x01",
            "the Royal Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x15,
        "#1513F#6PYes, we certainly are.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x1E,
        "#113F#11PI-I'm not sure what is going on here...\x02",
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
            "#112F#11PEstelle? Joshua?\x02\x03",

            "...And is that you, Your Highness?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x16,
        "#1382F#6PYes, it is. It's good to see you again, Richard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x12,
        "#179F#6PI feel the same.\x02",
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
            "#115F#11PThe pleasure is all mine, Your Highness.\x02\x03",

            "#110FI'm delighted to see you well and in good health.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x16,
        (
            "#1165F#6PHeehee. There's no need to stare at the floor\x01",
            "when you're talking to me, you know.\x02\x03",

            "#1168FHow have you been?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x1E,
        (
            "#119F#11PTh-Thanks to Her Majesty's extraordinary kindness,\x01",
            "I've been doing very well.\x02\x03",

            "#112FI hope you'll forgive me for asking--I'm afraid I don't\x01",
            "quite understand the situation I've found myself in...\x02\x03",

            "Would it be any trouble to request a brief explanation\x01",
            "of where we stand?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x10F,
        "#1448F#6PIt would probably be easier if I handled that.\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #141
        0x1E,
        "#113F#11PI don't believe we've met...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x10F,
        (
            "#1447F#6PAllow me to introduce myself.\x02\x03",

            "#1448FI'm Ries Argent, a squire affiliated with the\x01",
            "Gralsritter.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #143
        0x1E,
        (
            "#112FTHE Gralsritter?!\x02\x03",

            "#115F...I see. It sounds as though the situation\x01",
            "is even more abnormal than I thought.\x02",
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
            "#110F#11PI suppose I should introduce myself as well.\x02\x03",

            "#115FMy name is Alan Richard.\x02\x03",

            "I was once a colonel in the Royal Army's \x01",
            "Intelligence Division, as well as a traitor\x01",
            "who attempted to instigate a coup d'etat.\x02\x03",

            "#111FAt present, however, I run the research\x01",
            "agency R&A Research.\x02",
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
            "#115F#11PThank you. I think I have a solid grasp now.\x02\x03",

            "#116FI wish I knew what else to say...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x101,
        (
            "#1015F#6PWhat do you mean?\x02\x03",

            "As in, like, you're having trouble believing all\x01",
            "of what we just told you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x1E,
        (
            "#110F#11PWell, part of me feels that way, yes.\x02\x03",

            "#115FBut that's not really it... The greatest\x01",
            "doubt in my mind is simply, 'Why me?'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x101,
        "#1004F#6P...Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x1E,
        (
            "#110F#11PI look at everyone here, and I see comrades\x01",
            "who know how to fight alongside one another\x01",
            "to turn even the darkest of odds in their favor.\x02\x03",

            "Whether this turn of events was the will of the\x01",
            "Goddess or someone else, I can't rightly say...\x02\x03",

            "#119F...but from where I'm standing, you've already\x01",
            "formed the perfect team for overcoming the\x01",
            "obstacles before you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x101,
        "#1008F#6PErrr... I guess so...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x14, 315, 400)
    Sleep(300)

    ChrTalk(    #151
        0x14,
        (
            "#413F#6PI sure as hell don't wanna work with her,\x01",
            "though.\x02\x03",

            "#210FI don't want her stupid rubbing off on me.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 600)
    Sleep(300)

    ChrTalk(    #152
        0x101,
        (
            "#1019F#5POh, you're gonna feel REALLY stupid after\x01",
            "I thwack your brains to mush.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x15,
        "#1512F#5PNot now, you two...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x1E,
        "#115F#11P*cough* If I may...\x02",
    )

    CloseMessageWindow()

    def lambda_6B47():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_6B47)
    Sleep(100)
    OP_8C(0x101, 0, 600)
    Sleep(300)

    ChrTalk(    #155
        0x1E,
        (
            "#112F#11PI find it hard to understand how I, of all people,\x01",
            "came to be here.\x02\x03",

            "Far from working together well with all of you,\x01",
            "I'm a criminal who threatened both your lives\x01",
            "and the safety of the nation in which we thrive.\x02\x03",

            "#115FI can't help but feel my being here is a mistake\x01",
            "of some kind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x16,
        "#1163F#6PStill...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x101,
        (
            "#1002F#6PYou have helped us before, though!\x02\x03",

            "Like during the attack on Grancel, remember?\x01",
            "You came to everyone's aid then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x11,
        (
            "#065F#6PY-Yeah!\x02\x03",

            "That could've gotten really bad if you and your\x01",
            "men hadn't showed up to help when you did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x1B,
        "#1527F#6PHaha. They're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x15,
        (
            "#1500F#6PThen there was the fact that you assumed\x01",
            "responsibility for defending the city while\x01",
            "all of us escorted Kloe to Haken Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x1C,
        (
            "#051F#6PYeah. You might've done some bad stuff in the \x01",
            "past, but you're underselling yourself by sayin'\x01",
            "you've never helped us before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x1E,
        "#112F#11PBe as that may be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x18,
        (
            "#1545F#6PMy good man, it's not as though you're the only\x01",
            "one here who's performed terrible deeds.\x02\x03",

            "#1540FTo use the occasion Joshua mentioned: while you\x01",
            "valiantly defended Grancel, I was at Haken Gate\x01",
            "threatening Liberl's safety.\x02\x03",

            "And yet here I am, fighting alongside my friends\x01",
            "without a care in the world!\x02\x03",

            "#1541FThe best thing to do here, in my personal opinion,\x01",
            "is relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x13,
        (
            "#274F#6P...I'm not sure boasting about 'not having a care\x01",
            "in the world' is something YOU should be doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x1E,
        (
            "#110F#11PI have a different perspective on those events,\x01",
            "Your Highness.\x02\x03",

            "You were only threatening Liberl on the surface.\x01",
            "You had no intention of actually doing anything.\x01",
            "On the contrary! You were trying to protect it.\x02\x03",

            "#119FThe same can't be said for me. My conspiracy was\x01",
            "of my own doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x14,
        (
            "#212F#6POkay, but what about me?\x02\x03",

            "#413FWe were being used by you guys, yeah, but that\x01",
            "doesn't change the fact we were a bunch of sky\x01",
            "bandits who even hijacked an airship.\x02\x03",

            "#210FBut Her Majesty was gracious enough to give us\x01",
            "another chance at life, and we're trying to make\x01",
            "the most of it running our new company.\x02\x03",

            "I don't think our positions are all that different,\x01",
            "honestly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x1E,
        "#113F#11PWell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x19,
        (
            "#573F#6PYou might've done things that you regret...\x02\x01",

            "#070Fbut it's not the past that determines who you are.\x01",
            "It's what you choose to do now. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x1A,
        (
            "#811F#6PExactly! And it'd be a huge help if we had\x01",
            "someone as baller as you fighting with us!\x02\x03",

            "#815FSo please? We could really use your help!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x1E,
        "#110F#11P...Are you sure, Anelace?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 400)
    Sleep(300)

    ChrTalk(    #171
        0x101,
        (
            "#1011F#5PHuh? You guys know each other?\x02\x03",

            "How did that happen?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1A, 315, 400)
    Sleep(300)

    ChrTalk(    #172
        0x1A,
        (
            "#819F#6POh... Haha...\x02\x03",

            "I went to visit your dad for something a while\x01",
            "back, so that's when we met.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x101,
        "#1004F#5PHuh. Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x10F,
        (
            "#1446F#6PAfter all we've heard, I see no reason to refuse\x01",
            "your company.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7612():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_7612)
    Sleep(100)
    OP_8C(0x101, 0, 400)
    Sleep(400)

    ChrTalk(    #175
        0x10F,
        (
            "#1448F#6PIf anything, we're eager to welcome you to our\x01",
            "group with open arms. Myself included.\x02\x03",

            "You could consider it aid given to the Gralsritter\x01",
            "if that would make you less adverse to the idea.\x02\x03",

            "What do you say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x1E,
        (
            "#115F#11P...\x02\x03",

            "#110FVery well. You have my support.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x101,
        "#1018F#6PWoohoo!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x16,
        "#1168F#6PHeehee. I'm so glad you're with us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x12,
        "#171F#6PThank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x1E,
        (
            "#119F#11PHaha... I only hope I meet your expectations.\x02\x03",

            "#110F...Incidentally, there is one thing I would like\x01",
            "to confirm first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x10F,
        "#1444F#6PWhat would that be?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x1E,
        (
            "#115F#11PYou said that you believe everyone to have been\x01",
            "surrounded by that white light and sent here at\x01",
            "roughly the same time.\x02\x03",

            "#112FWhen that happened, were you all wearing the\x01",
            "same clothes that you are now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x101,
        "#1015F#6PWhat kind of question is that?\x02",
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #184
        0x12,
        (
            "#173F#6PNow that you mention it, how come you're wearing\x01",
            "your military uniform?\x02\x03",

            "I was under the impression that you left the armed\x01",
            "forces...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x101,
        "#1004F#6PThat's right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x13,
        (
            "#272F#6PHmm... Now the question makes sense.\x02\x03",

            "#270FYou were wearing something different when\x01",
            "you were sent here, weren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x1E,
        (
            "#115F#11PI was.\x02\x03",

            "#112FCurrently, I work out of an office in Ruan City,\x01",
            "and since beginning work there, I have never once\x01",
            "willingly worn my old uniform.\x02\x03",

            "When I was surrounded by that light, I was wearing\x01",
            "a shirt and a pair of slacks as I normally do.\x02\x03",

            "And yet somehow, I find myself here in uniform.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x15,
        (
            "#1503F#6PThat's odd...\x02\x03",

            "#1502FIt's not something that's happened to anyone else,\x01",
            "either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x18,
        (
            "#1543F#6POh! I have a thought.\x02\x03",

            "#1547FPerhaps the Lord of Phantasma decided the colonel just\x01",
            "wasn't sexy enough in anything else and prepared\x01",
            "that strapping uniform for him after bringing him here?\x02",
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

    def lambda_7E31():
        OP_6D(-360, 4000, -2040, 800)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_7E31)

    def lambda_7E49():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7E49)

    def lambda_7E57():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_7E57)
    Sleep(50)

    def lambda_7E6A():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_7E6A)

    def lambda_7E78():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_7E78)
    Sleep(50)

    def lambda_7E8B():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_7E8B)

    def lambda_7E99():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_7E99)
    Sleep(50)

    def lambda_7EAC():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_7EAC)

    def lambda_7EBA():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_7EBA)
    Sleep(50)

    def lambda_7ECD():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_7ECD)

    def lambda_7EDB():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_7EDB)
    Sleep(50)
    OP_8C(0x19, 90, 400)
    WaitChrThread(0x10F, 0x1)
    Sleep(300)

    ChrTalk(    #190
        0x1B,
        "#1525F#6PYeah... I don't think so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x101,
        (
            "#1019F#11PSo in addition to the other billion ways they're a\x01",
            "weird freak, they've got a military uniform fetish,\x01",
            "too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x1A,
        "#819F#6PI couldn't entirely blame them if they did, though...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x14,
        "#415F#6PSame...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x16,
        "#1380F#6P...\x02",
    )

    CloseMessageWindow()
    OP_62(0x1E, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #195
        0x1E,
        "#115F#11PUmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x1C,
        "#551F#12PI swear.... Girls these days.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x11,
        "#060F#12P??? (<- Has no idea what's going on)\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_80A1():
        OP_6D(-360, 4000, -1540, 1000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_80A1)

    def lambda_80B9():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_80B9)

    def lambda_80C7():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_80C7)
    Sleep(50)

    def lambda_80DA():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_80DA)

    def lambda_80E8():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_80E8)
    Sleep(50)

    def lambda_80FB():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_80FB)

    def lambda_8109():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_8109)
    Sleep(50)

    def lambda_811C():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_811C)

    def lambda_812A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_812A)
    Sleep(50)

    def lambda_813D():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_813D)

    def lambda_814B():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_814B)
    Sleep(50)
    OP_8C(0x1C, 315, 400)
    WaitChrThread(0x10F, 0x1)
    Sleep(300)

    ChrTalk(    #198
        0x19,
        (
            "#074F#6PStill, there's clearly got to be something to it.\x02\x03",

            "#070FI get the feeling we're on the verge of a major\x01",
            "breakthrough in working out how we ended up\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x15,
        (
            "#1505F#6PSo do I.\x02\x03",

            "#1500FAs well as what this place really is to begin with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x1E,
        (
            "#119F#11PInteresting...\x02\x03",

            "#110FIn that case, let's put the matter aside for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x10F,
        (
            "#1447F#6PNow that that's settled, then, we should start\x01",
            "getting ready to resume our investigation.\x02\x03",

            "#1448FReleasing Richard should hopefully have opened\x01",
            "up a new path for us to follow.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_837B():
        OP_6B(2800, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_837B)
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

    # Function_11_588E end

    def Function_12_8530(): pass

    label("Function_12_8530")

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

    def lambda_875C():
        OP_6D(-1180, 4000, 2780, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_875C)

    def lambda_8774():
        OP_67(0, 5490, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_8774)

    def lambda_878C():
        OP_6B(2400, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_878C)

    def lambda_879C():
        OP_6E(403, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_879C)
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

    def lambda_88AE():
        OP_8F(0xFE, 0x0, 0x1770, 0x64, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_88AE)
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

    def lambda_8A0D():
        OP_6D(0, 7500, 3760, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_8A0D)

    def lambda_8A25():
        OP_67(0, 1650, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_8A25)

    def lambda_8A3D():
        OP_6B(2700, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_8A3D)

    def lambda_8A4D():
        OP_6E(363, 3500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8A4D)

    def lambda_8A5D():
        OP_8F(0xFE, 0x0, 0x2134, 0xAF0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_8A5D)
    WaitChrThread(0x1F, 0x0)
    WaitChrThread(0x10F, 0x0)
    Sleep(500)

    def lambda_8A87():
        OP_6B(2000, 8000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_8A87)
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

    # Function_12_8530 end

    def Function_13_8B71(): pass

    label("Function_13_8B71")

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

    def lambda_8DFA():
        OP_6D(-300, 4000, 760, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_8DFA)

    def lambda_8E12():
        OP_67(0, 4850, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_8E12)

    def lambda_8E2A():
        OP_6B(3000, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_8E2A)

    def lambda_8E3A():
        OP_6E(327, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_8E3A)

    def lambda_8E4A():
        OP_6C(327000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8E4A)

    def lambda_8E5A():
        OP_8F(0xFE, 0x12C, 0xFA0, 0x69A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_8E5A)
    WaitChrThread(0x1F, 0x0)
    SetChrSubChip(0x1F, 0)
    WaitChrThread(0x10F, 0x0)
    Sleep(500)
    Fade(1000)
    OP_82(0x2, 0x2)
    PlayEffect(0x3, 0x1, 0x1F, 100, 300, 200, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)

    def lambda_8EC6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_8EC6)
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

    def lambda_9083():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_9083)
    OP_82(0x2, 0x2)
    WaitChrThread(0x1F, 0x0)
    Fade(500)
    OP_82(0x1, 0x0)
    OP_0D()
    Sleep(1000)

    NpcTalk(    #202
        0x1F,
        "Renne",
        "#268F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x101,
        "#1025F#6PI can't believe it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x11,
        "#066F#6PIt really is Renne...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x15,
        "#1500F#6PIt looks like she's fast asleep.\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    Sleep(500)

    NpcTalk(    #206
        0x1F,
        "Renne",
        (
            "#268F#5P#60WPapa... Mama...\x02\x03",

            "#40WWhy...?\x02",
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
        "#1003F#6P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x15,
        "#1503F#6PRenne...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #209
        0x1F,
        "Renne",
        "#1309F#5P#60W...?\x02",
    )

    CloseMessageWindow()

    def lambda_9211():
        OP_6B(2900, 10000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_9211)
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
        "Renne",
        "#1307F#5P#40WWhere...am I...?\x02",
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
        "Renne",
        "#1300F#5P#40WOh... This is just a dream...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x101,
        "#1025F#6PRenne...\x02",
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
        "Renne",
        (
            "#264F#5P#40WEstelle?\x02\x03",

            "#40WJoshua and Tita, too?\x02\x03",

            "#263F#40WTeehee... What a nice dream this is.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #214
        0x101,
        "#1027F#6P#4SRenne!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_94DC():
        OP_8E(0xFE, 0x1CC, 0xFA0, 0x28A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_94DC)
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
        "Renne",
        "#264F#5P#40WOh...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #216
        0x1F,
        "Renne",
        (
            "#1305F#5P#40WOh, silly Estelle... You're supposed to be older\x01",
            "than me. You shouldn't be acting like a clingy\x01",
            "child.\x02",
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
        "Renne",
        (
            "#263F#5P#40WYou're so warm, though...and you smell so nice...\x02\x03",

            "#40WIt's almost like this isn't a dream at a--\x02",
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

    def lambda_9764():
        OP_6D(-800, 4000, 600, 1000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_9764)

    def lambda_977C():
        OP_6B(2400, 1000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_977C)
    OP_22(0x50, 0x0, 0x64)
    OP_22(0xA3, 0x0, 0x64)
    SetChrChipByIndex(0x1F, 17)
    SetChrSubChip(0x1F, 0)
    ClearChrFlags(0x1F, 0x800)
    ClearChrFlags(0x1F, 0x2)
    SetChrFlags(0x1F, 0x1)
    ClearChrFlags(0x1F, 0x4)
    ClearChrFlags(0x101, 0x8)

    def lambda_97B9():
        OP_96(0xFE, 0x122, 0xFA0, 0xD52, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_97B9)

    def lambda_97D7():
        OP_95(0xFE, 0x3C, 0xFA0, 0xFFFFF9C0, 0x1F4, 0x1B58)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_97D7)

    def lambda_97F5():

        label("loc_97F5")

        TurnDirection(0xFE, 0x1F, 400)
        OP_48()
        Jump("loc_97F5")

    QueueWorkItem2(0x11, 2, lambda_97F5)

    def lambda_9806():

        label("loc_9806")

        TurnDirection(0xFE, 0x1F, 400)
        OP_48()
        Jump("loc_9806")

    QueueWorkItem2(0x1C, 2, lambda_9806)

    def lambda_9817():

        label("loc_9817")

        TurnDirection(0xFE, 0x1F, 400)
        OP_48()
        Jump("loc_9817")

    QueueWorkItem2(0x1A, 2, lambda_9817)

    def lambda_9828():

        label("loc_9828")

        TurnDirection(0xFE, 0x1F, 400)
        OP_48()
        Jump("loc_9828")

    QueueWorkItem2(0x14, 2, lambda_9828)

    def lambda_9839():

        label("loc_9839")

        TurnDirection(0xFE, 0x1F, 400)
        OP_48()
        Jump("loc_9839")

    QueueWorkItem2(0x16, 2, lambda_9839)

    def lambda_984A():

        label("loc_984A")

        TurnDirection(0xFE, 0x1F, 400)
        OP_48()
        Jump("loc_984A")

    QueueWorkItem2(0x18, 2, lambda_984A)

    def lambda_985B():

        label("loc_985B")

        TurnDirection(0xFE, 0x1F, 400)
        OP_48()
        Jump("loc_985B")

    QueueWorkItem2(0x12, 2, lambda_985B)

    def lambda_986C():

        label("loc_986C")

        TurnDirection(0xFE, 0x1F, 400)
        OP_48()
        Jump("loc_986C")

    QueueWorkItem2(0x13, 2, lambda_986C)
    WaitChrThread(0x101, 0x1)
    SetChrChipByIndex(0x101, 19)
    SetChrSubChip(0x101, 0)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0x1F, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(500)

    NpcTalk(    #218
        0x1F,
        "Renne",
        (
            "#1308F...?!\x02\x03",

            "Wh-What's going on?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x101,
        "#1026F#6PRenne, this...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #220
        0x1F,
        "Renne",
        (
            "#1308FWhat are you doing here?!\x02\x03",

            "#268FNo. Never mind that...\x02\x03",

            "#1301FWhat am -I- doing here?!\x02",
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
            "#1025F#6PIt's okay, Renne. I'm going to explain now,\x01",
            "so try and stay calm, okay?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_99C2():
        OP_6D(-800, 4000, 900, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_99C2)

    def lambda_99DA():
        OP_8F(0xFE, 0x1CC, 0xFA0, 0xFFFFFF9C, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_99DA)
    Sleep(500)

    ChrTalk(    #222 op#A
        0x101,
        (
            "#1025F#6P#18AYou see, we're not sure how it happened,\x01",
            "either, but...\x02",
        )
    )

    Sleep(2000)

    NpcTalk(    #223
        0x1F,
        "Renne",
        "#1308F#11P#3SD-Don't come any closer!#2S\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(400)

    NpcTalk(    #224
        0x1F,
        "Renne",
        (
            "#1303F#11P#3SIf you take another step towards me, \x01",
            "I WILL kill you!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #225
        0x101,
        "#1003F#6P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x15,
        (
            "#1505F#6PI'll try and handle this, Estelle.\x01",
            "Do you mind taking a step back?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x101,
        "#1026F#6POkay...\x02",
    )

    CloseMessageWindow()
    OP_43(0x101, 0x0, 0x3, 0xF)
    Sleep(500)

    def lambda_9B78():
        OP_6D(-800, 4000, 1200, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_9B78)

    def lambda_9B90():
        OP_8F(0xFE, 0x32A, 0xFA0, 0xFFFFF8F8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_9B90)
    WaitChrThread(0x15, 0x0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x10F, 0x0)

    ChrTalk(    #228
        0x15,
        (
            "#1505F#6PI'm happy to see you again, Renne.\x02\x03",

            "#1514FHow've you been all this time?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #229
        0x1F,
        "Renne",
        (
            "#1303F#11PHow is that any of your business?!\x02\x03",

            "#1301FYou're just as bad as Estelle is, Joshua!\x02\x03",

            "Why won't you two leave me alone and\x01",
            "stop following me around?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x15,
        (
            "#1512F#6PI figured you must have noticed...\x02\x03",

            "#1500FYou're right. For the past few months,\x01",
            "we've been traveling around trying to\x01",
            "find you.\x02\x03",

            "We're in Crossbell at the moment, too.\x01",
            "Are we getting warmer?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #231
        0x1F,
        "Renne",
        (
            "#1308F#11PY-You're in Crossbell?!\x02\x03",

            "#1303FWhy? Why do you want to find me so much?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x15,
        (
            "#1505F#6PWe just want a chance to talk with you.\x02\x03",

            "#1502FWe heard from a reliable source that you\x01",
            "haven't been back to Ouroboros since we\x01",
            "last fought... Is that true?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #233
        0x1F,
        "Renne",
        (
            "#1301F#11PWhat's that got to do with either of you?!\x02\x03",

            "#1303FAll I want is to be left alone! I don't want\x01",
            "to talk to either of you. I don't even want\x01",
            "to SEE you!\x02\x03",

            "So why won't you just leave me be?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x15,
        "#1503F#6PBecause...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x101,
        (
            "#1007F#6PSorry, Renne. This one's on me.\x02\x03",

            "#1003FEver since you flew off, I haven't been able to\x01",
            "get you off my mind.\x02\x03",

            "I've been getting Joshua to look into where you\x01",
            "might be, and we've been going around chasing\x01",
            "down every possible lead.\x02\x03",

            "#1025FBut that's why I'm so happy to finally be able to\x01",
            "see you again like this.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #236
        0x1F,
        "Renne",
        (
            "#1308F#11PBut... But...\x02\x03",

            "#1300F...\x02\x03",

            "#263FHeehee. Oh, I get it now.\x02\x03",

            "#1306FYou're lying, aren't you? Really, all of that's just\x01",
            "a cover for the fact you're trying to capture me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x101,
        "#1004F#6PWha...?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #238
        0x1F,
        "Renne",
        (
            "#1305F#11PSorry to disappoint you, but I only know about as\x01",
            "much as Joshua does about Ouroboros. \x02\x03",

            "Even if you catch me, you're not going to get\x01",
            "anything useful out of me...and even if I did\x01",
            "know lots of dirty secrets, I wouldn't tell you.\x02\x03",

            "#263FI bet you feel really stupid for wasting your\x01",
            "time now.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #239
        0x101,
        "#1020F#6PW-Wait a second! That's not...!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #240
        0x1F,
        "Renne",
        (
            "#1306F#11POr are you going to try your luck anyway?\x01",
            "You've sure brought a lot of familiar faces\x01",
            "for backup.\x02\x03",

            "#263FEven I might have trouble taking on THIS \x01",
            "many people at once...\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x1F, 24)
    SetChrSubChip(0x1F, 14)

    def lambda_A3D9():
        OP_99(0x1F, 0xE, 0x8, 0x5DC)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_A3D9)
    WaitChrThread(0x1F, 0x1)
    Sleep(500)

    def lambda_A3F3():
        OP_99(0x1F, 0x8, 0x2, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_A3F3)
    Sleep(200)
    Fade(500)

    def lambda_A40D():
        OP_6B(2300, 0)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_A40D)
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

    def lambda_A582():
        OP_99(0x1F, 0x2, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_A582)
    SetChrChipByIndex(0x1F, 23)
    SetChrSubChip(0x1F, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #241
        0x1F,
        "Renne",
        (
            "#1304F...but I'm confident I'll leave at least a few\x01",
            "of you headless before I end up beaten.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x101,
        "#1027F#6P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x11,
        "#065F#6PR-Renne...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x1C,
        "#551F#6PYou've gotta be kidding me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x1A,
        "#1317F#6PWhat're we supposed to do, Schera?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x1B,
        "#1525F#6PDon't ask me... This doesn't look good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x10F,
        "#1805F#6P...\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_D2(0x270448, 0x27044C, 0x13)
    OP_D2(0x70064, 0x7006C, 0x14)
    OP_D2(0x600DC, 0x600E1, 0x15)
    OP_D2(0x27004E, 0x27004F, 0x16)
    OP_D2(0x270240, 0x27024A, 0x17)
    OP_D2(0x70061, 0x70069, 0x18)

    def lambda_A71B():
        OP_6D(-510, 4000, 2300, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A71B)

    def lambda_A733():
        OP_67(0, 5020, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A733)

    def lambda_A74B():
        OP_8F(0xFE, 0xFFFFFC9A, 0xFA0, 0xFFFFFC22, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_A74B)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #248
        0x10F,
        (
            "#1446F#6PWell, I think I know who you are now.\x02\x03",

            "#1443FOuroboros Enforcer No. XV, the Angel of Slaughter,\x01",
            "correct?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #249
        0x1F,
        "Renne",
        (
            "#269F#11PYou certainly DO know me. I don't know you,\x01",
            "though.\x02\x03",

            "Are you a knight of the church?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x10F,
        (
            "#1447F#6PYes. I'm Ries Argent, a squire.\x02\x03",

            "#1806FAnd while I may not be very familiar with\x01",
            "your circumstances, would it hurt you to\x01",
            "behave less like a self-centered child?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1F, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #251
        0x1F,
        "Renne",
        (
            "#1308F#11PE-Excuse me? Did you call me a self-centered\x01",
            "child?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x10F,
        (
            "#1805F#6PFrom what I've heard, your intelligence and\x01",
            "deductive reasoning have few peers.\x02\x03",

            "That led to you joining Ouroboros, obtaining\x01",
            "both the current rank and abilities you now\x01",
            "have.\x02\x03",

            "#1446FSo unless I'm wrong, I find it very hard to\x01",
            "believe you haven't already figured out that\x01",
            "this isn't a trap we've set to capture you.\x02\x03",

            "#1806FAnd yet you still expect us to waste our time\x01",
            "and humor your little temper tantrum?\x01",
            "So yes--I DID call you a self-centered child.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x16,
        "#1163F#5PUmm... Ries...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x14,
        "#413F#5PD-Damn. She sure doesn't mince words...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #255
        0x1F,
        "Renne",
        (
            "#1305F#11PMy... You're a brave one, aren't you, miss?\x02\x03",

            "#263FDid I hear a lowly squire like you trying to\x01",
            "provoke an Enforcer like me?\x02\x03",

            "#1304FYou must REALLY want to end up splattered\x01",
            "all over the floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x10F,
        (
            "#1806F#6PI could say the same to you.\x02\x03",

            "#1447FI have no idea why everyone else here regards you\x01",
            "favorably, but I, for one, have no interest in being\x01",
            "friends with someone from Ouroboros.\x02",
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
            "#1805F#6PSo if a battle is what you want, I will be more than\x01",
            "happy to oblige.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x101,
        "#1020F#6POh, no...\x02",
    )

    CloseMessageWindow()
    OP_44(0x11, 0x2)
    OP_62(0x11, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #259
        0x11,
        "#065F#6PR-Ries?!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #260
        0x1F,
        "Renne",
        (
            "#1306F#11PA templar sword, huh?\x02\x03",

            "Those can certainly be a rude awakening in\x01",
            "the right hands.\x02\x03",

            "#263FOf course, everyone else who's ever tried to\x01",
            "challenge me with one ended up being quite\x01",
            "predictable after a while.\x02",
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
        "Renne",
        (
            "#1304F#11PBefore long, they were all begging me for mercy\x01",
            "like pigs about to be slaughtered. It was ever so\x01",
            "pitiful.\x02\x03",

            "Teehee. I can't wait to hear you do the same.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #262
        0x101,
        "#1020F#6PR-Renne?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x11,
        "#065F#6PN-No!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x10F,
        (
            "#1805F#6PDo you actually want to fight, or do you only intend\x01",
            "to stand around trying to sound threatening?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #265
        0x1F,
        "Renne",
        "#263F#11PI suppose that IS enough talking.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x15,
        "#1502F#6PGuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x101,
        "#1005F#6PC-Come on, you tw--\x02",
    )

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

    def lambda_B213():
        OP_6B(1860, 500)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_B213)
    OP_0D()
    OP_20(0x3E8)

    ChrTalk(    #268
        0x11,
        "#567F#4S#5PBOTH OF YOU, STOP IT!\x02",
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
        "#1444F#12P...!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #270
        0x1F,
        "Renne",
        "#1308F#5PTita?\x02",
    )

    CloseMessageWindow()

    def lambda_B2C6():

        label("loc_B2C6")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_B2C6")

    QueueWorkItem2(0x101, 2, lambda_B2C6)

    def lambda_B2D7():

        label("loc_B2D7")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_B2D7")

    QueueWorkItem2(0x15, 2, lambda_B2D7)

    def lambda_B2E8():

        label("loc_B2E8")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_B2E8")

    QueueWorkItem2(0x1C, 2, lambda_B2E8)

    def lambda_B2F9():

        label("loc_B2F9")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_B2F9")

    QueueWorkItem2(0x1A, 2, lambda_B2F9)

    def lambda_B30A():

        label("loc_B30A")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_B30A")

    QueueWorkItem2(0x14, 2, lambda_B30A)

    def lambda_B31B():

        label("loc_B31B")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_B31B")

    QueueWorkItem2(0x16, 2, lambda_B31B)

    def lambda_B32C():

        label("loc_B32C")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_B32C")

    QueueWorkItem2(0x18, 2, lambda_B32C)

    def lambda_B33D():

        label("loc_B33D")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_B33D")

    QueueWorkItem2(0x19, 2, lambda_B33D)

    def lambda_B34E():

        label("loc_B34E")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_B34E")

    QueueWorkItem2(0x12, 2, lambda_B34E)

    def lambda_B35F():

        label("loc_B35F")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_B35F")

    QueueWorkItem2(0x13, 2, lambda_B35F)

    def lambda_B370():

        label("loc_B370")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_B370")

    QueueWorkItem2(0x1E, 2, lambda_B370)
    Sleep(500)

    ChrTalk(    #271
        0x101,
        "#1020F#6PH-Hey...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x1C,
        "#055F#6PW-Wait a sec!\x02",
    )

    CloseMessageWindow()
    OP_1D(0x76)

    def lambda_B3BA():
        OP_6D(1480, 4000, -140, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_B3BA)

    def lambda_B3D2():
        OP_67(0, 5400, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_B3D2)

    def lambda_B3EA():
        OP_6B(1670, 2000)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_B3EA)

    def lambda_B3FA():
        OP_6E(500, 2000)
        ExitThread()

    QueueWorkItem(0x1F, 3, lambda_B3FA)
    OP_43(0x11, 0x3, 0x3, 0xE)
    Sleep(300)

    def lambda_B416():
        OP_8E(0xFE, 0xDFC, 0xFA0, 0xFFFFF29A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_B416)
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
            "#562F#11PWhy are the two of you so desperate to try and\x01",
            "fight when you KNOW you don't really want to?\x02\x03",

            "#566FRenne! You were trying to make it sound like you\x01",
            "don't care about Estelle and Joshua, but deep down\x01",
            "you're happy to see them again, and you know it!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 180, 600)
    Sleep(300)

    ChrTalk(    #274
        0x11,
        (
            "#566F#6PAnd Ries! You've already realized that Renne's not\x01",
            "actually a bad person. It doesn't matter that she's\x01",
            "from Ouroboros!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x10F,
        "#1802F#11PWell...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #276
        0x1F,
        "Renne",
        (
            "#1308F#6PI'm happy?\x02\x03",

            "Of course I'm not. Why would I possibly b--\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 0, 600)
    Sleep(500)

    ChrTalk(    #277
        0x11,
        (
            "#566F#11PThen why did you look so happy when Estelle\x01",
            "hugged you?!\x02",
        )
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x78)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #278
        0x11,
        (
            "#562F#11PRight up until the moment you realized this\x01",
            "was all real, you were acting like it was the\x01",
            "best dream you'd ever had!\x02\x03",

            "And now you're saying you don't want to talk\x01",
            "to them? That you don't want to see them?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #279
        0x1F,
        "Renne",
        "#1307F#6PH-Hold on a minute, Tita...\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrFlags(0x11, 0x800)
    SetChrFlags(0x11, 0x2)
    SetChrChipByIndex(0x11, 21)
    SetChrSubChip(0x11, 8)
    OP_0D()

    def lambda_B806():

        label("loc_B806")

        OP_99(0xFE, 0x7, 0xA, 0x5DC)
        OP_48()
        Jump("loc_B806")

    QueueWorkItem2(0x11, 0, lambda_B806)
    Sleep(500)

    ChrTalk(    #280
        0x11,
        "#566F#11PAnd that's not true at all...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #281
        0x11,
        "#567F#4S#11PThat's not true at all, so just ADMIT IT!\x02",
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0x96)
    CloseMessageWindow()
    Sleep(300)

    NpcTalk(    #282
        0x1F,
        "Renne",
        "#1309F#6P...\x02",
    )

    CloseMessageWindow()
    OP_44(0x11, 0x0)
    OP_99(0x11, 0x6, 0x4, 0x3E8)

    def lambda_B8C5():

        label("loc_B8C5")

        OP_99(0xFE, 0x0, 0x3, 0x3E8)
        OP_48()
        Jump("loc_B8C5")

    QueueWorkItem2(0x11, 0, lambda_B8C5)
    Sleep(500)

    ChrTalk(    #283
        0x11,
        (
            "#069F#11P#40W*sniffle*...\x02\x03",

            "*sniffle*...*sniffle*...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #284
        0x101,
        "#1025F#5PSweetie...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x1C,
        (
            "#551F#6PI swear, she just cut my life short about ten\x01",
            "years. What the hell was she thinkin'?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #286
        0x1F,
        "Renne",
        "#268F#6PLook at you. Honestly...\x02",
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

    def lambda_B9FA():
        OP_6D(1480, 4000, -500, 1500)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_B9FA)

    def lambda_BA12():
        OP_8F(0xFE, 0x96, 0xFA0, 0x9C4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_BA12)
    WaitChrThread(0x1F, 0x0)
    WaitChrThread(0x10F, 0x3)

    NpcTalk(    #287
        0x1F,
        "Renne",
        (
            "#1307F#6PI thought you were a year older than me, \x01",
            "you know?\x02\x03",

            "#268FYet here you are, crying away. You're not\x01",
            "setting a very good example.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x11,
        (
            "#562F#11P#40W*hic* I can't help it!\x02\x03",

            "#40WWhat am I supposed to do when you guys\x01",
            "finally see each other again and all you do\x01",
            "is end up fighting?\x02\x03",

            "#40W*sniffle* That's just...*hic*...too sad...\x02\x03",

            "#069F#40W*sob*...\x02",
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
        "#567F#4S#11PWaaaaaaaaaaaahhh!\x02",
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0x12C)
    CloseMessageWindow()
    OP_62(0x1F, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    WaitChrThread(0x10F, 0x0)

    NpcTalk(    #290
        0x1F,
        "Renne",
        "#1308F#6PH-Hey!\x02",
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
        "Renne",
        (
            "#1309F#6P#40W*sigh* What are you...crying for...?\x02\x03",

            "#268F#40WWhy did you have to...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x101,
        (
            "#1012F#5PHeehee.\x02\x03",

            "#1017FYou know the answer to that already, Renne.\x02\x03",

            "It's because she likes you.\x02",
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
        "Renne",
        "#1307F#6PShe does...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x101,
        (
            "#1006F#5PHey, Renne?\x02\x03",

            "I know we've still got our differences, but how\x01",
            "about we put all of that aside and call a truce\x01",
            "for now?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #295
        0x1F,
        "Renne",
        "#1307F#6PA truce?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x101,
        (
            "#1007F#5PAs I'm sure you can tell, we're in the middle\x01",
            "of a really messy situation right now.\x02\x03",

            "And however you got here, you've ended up\x01",
            "being dragged right into it with us.\x02\x03",

            "#1006FI'd say it's in all our best interests to work\x01",
            "together. At least until we get out of here,\x01",
            "anyway. What do you say?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #297
        0x1F,
        "Renne",
        "#264F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0x1E,
        (
            "#119F#8PThat's certainly true. There's still plenty we don't\x01",
            "know about our predicament.\x02\x03",

            "#111FHaving someone with your intellect on our side\x01",
            "may well help us to fill in the remaining blanks.\x02\x03",

            "In fact, I would greatly welcome your assistance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0x101,
        "#1001F#5PYeah! I'm with the colonel!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x1E,
        (
            "#495F#8PI'm not a colonel, Estelle...\x02\x03",

            "#110FRegardless, I think it would be in your best\x01",
            "interests to work with us, too.\x02\x03",

            "Cooperating will allow you to gather information\x01",
            "more efficiently, as well as make it easier for you\x01",
            "to ensure your own safety.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #301
        0x1F,
        "Renne",
        (
            "#1300F#6P...\x02\x03",

            "#268FThat's true... It's obvious that wherever we\x01",
            "are, it's somewhere abnormal.\x02\x03",

            "So it goes without saying that having me\x01",
            "around would be a big help to all of you.\x02",
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
        "Renne",
        (
            "#266F#6P...All right. Out of respect for Tita's bravery, \x01",
            "I'll spare you all this time.\x02\x03",

            "#262FFill me in on exactly what's going on here.\x02",
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
        "#565F#11POh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0x101,
        "#1008F#5PHeehee.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0x15,
        "#1513F#11P...Thanks, Renne.\x02",
    )

    CloseMessageWindow()
    OP_62(0x1F, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    NpcTalk(    #306
        0x1F,
        "Renne",
        (
            "#1301F#6PJ-Just so we're clear, I haven't decided whether\x01",
            "I'm going to work with you or not yet!\x02\x03",

            "#266FAll I'm promising is to listen to your explanation\x01",
            "of what's happening. THEN I'll decide if I'll help.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C418():
        OP_6B(2090, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_C418)
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
        "Renne",
        (
            "#263F#11PI see. I think I've got a pretty good idea what's\x01",
            "going on now.\x02\x03",

            "#269FWhoever chose this place's name couldn't have\x01",
            "picked a better one, couldn't they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x10F,
        "#1444F#6PWhat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0x15,
        "#1504F#6PHave you figured something out that we hadn't?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #310
        0x1F,
        "Renne",
        (
            "#263F#11PPossibly. I'm still not completely certain yet.\x02\x03",

            "#260FBut I'm relatively confident in my theory after\x01",
            "hearing the colonel's story, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0x1E,
        "#113F#6PMe?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #312
        0x1F,
        "Renne",
        (
            "#268F#11PMm-hmm. My own experience was the same\x01",
            "as everyone else's: ending up here after being\x01",
            "surrounded by a sudden white light.\x02\x03",

            "#262FBut you say you weren't wearing your uniform\x01",
            "when it happened to you, right, Colonel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0x1E,
        (
            "#495F#6P(How many times must I...? Well, whatever.)\x02\x03",

            "#110FI wasn't. As I explained to everyone when I first\x01",
            "arrived, I was wearing a shirt and slacks, as I do\x01",
            "every other day at work.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #314
        0x1F,
        "Renne",
        (
            "#261F#11PRight. Just checking. So, then, tell me something.\x02\x03",

            "#265FWould you say you have quite a strong emotional\x01",
            "attachment to that uniform?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #315
        0x1E,
        "#113F#6P...Pardon?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #316
        0x1F,
        "Renne",
        (
            "#263F#11PTeehee. Oh, that's a definite yes.\x02\x03",

            "#1305FIt's a symbol of your past--the past you just can't\x01",
            "quite move on from, even though you need to.\x02\x03",

            "Am I right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x1E,
        (
            "#116F#6P...\x02\x03",

            "#115FYes, you are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0x16,
        "#1163F#6PRichard...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0x12,
        "#175F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0x13,
        (
            "#272F#6PIt's no surprise you feel that way from my\x01",
            "perspective.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #321
        0x1F,
        "Renne",
        (
            "#1306F#11PAnd lo and behold, the moment you appeared\x01",
            "in this world, you were wearing that very same\x01",
            "uniform again.\x02\x03",

            "#261FWhatever do you think that could mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0x1E,
        (
            "#115F#6P...\x02\x03",

            "That would mean when I arrived here,\x01",
            "my attachment to that past ended up\x01",
            "being manifested as reality...\x02\x03",

            "#112FIn other words, this world is capable of \x01",
            "changing based on people's thoughts.\x02",
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
        "#1504F#6POh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0x18,
        "#1541F#6PHaha. NOW it makes sense.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0x14,
        "#216F#6PN-Not to me, it doesn't!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0x101,
        (
            "#1019F#6PCan you explain in slightly less complicated\x01",
            "terms for the rest of us?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #327
        0x1F,
        "Renne",
        (
            "#261F#11PIt's actually a really simple thing.\x02\x03",

            "#265FYou remember how Luciola used a Gospel\x01",
            "to make you experience a dream, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x101,
        "#1004F#6PRight...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0x1B,
        (
            "#1532F#6PThe dreams we saw were different depending\x01",
            "on what we wanted to see, too.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #330
        0x1F,
        "Renne",
        (
            "#263F#11POf course, unlike that, this isn't a dream...\x01",
            "but the concept is basically the same.\x02\x03",

            "#1305FAnyway, just like in Luciola's dream worlds,\x01",
            "this world changes depending on what the\x01",
            "people inside it want.\x02\x03",

            "It also happens to recreate places that exist\x01",
            "in their memories, too.\x02\x03",

            "It all falls into place nicely once you simplify\x01",
            "it, doesn't?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0x19,
        "#074F#6PSo it does...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0x1A,
        (
            "#816F#6PIt explains the monuments we've encountered\x01",
            "and how the doors work, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0x12,
        (
            "#172F#6PS-Still, while that explanation may explain the\x01",
            "contents of this world...\x02\x03",

            "...I find it hard to believe that any of us would\x01",
            "desire the predicament we've found ourselves in.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #334
        0x1F,
        "Renne",
        (
            "#263F#11POh, I don't disagree.\x02\x03",

            "#1306FWe're not the only ones here,\x01",
            "though, are we?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #335
        0x12,
        "#173F#6POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0x16,
        (
            "#1167F#6PSo, in other words...\x02\x03",

            "#1162F...many of the contents of this world exist\x01",
            "because of us, but its overall structure is\x01",
            "the result of someone else within it?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #337
        0x1F,
        "Renne",
        (
            "#263F#11PHeehee. From what I can gather, yes.\x02\x03",

            "#265FWhat exactly is making all of this possible is the\x01",
            "part I'm still puzzling over.\x02\x03",

            "Making people's wishes reality was the purpose of\x01",
            "the Aureole, but now that's been lost, and I can't\x01",
            "think of anything else capable of doing the same.\x02\x03",

            "#261FI think it's easy for all of us to point the finger at\x01",
            "who wished for this world to behave the way it\x01",
            "does, at the very least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0x10F,
        "#1443F#6PThe Lord of Phantasma...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #339
        0x1F,
        "Renne",
        (
            "#263F#11PExactly.\x02\x03",

            "Based on everything that's been said, they weren't\x01",
            "in this world originally. That was just the ghost you\x01",
            "you've encountered.\x02\x03",

            "#260FUntil the Lord of Phantasma, she simply watched\x01",
            "over this place from this garden here...\x02\x03",

            "...but then they showed up, stole her power, and\x01",
            "started remaking the world according to their own\x01",
            "whims.\x02\x03",

            "The result is what we're stuck in right now.\x02\x03",

            "#261FWell? What do you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0x11,
        "#560F#6PW-Wow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0x101,
        (
            "#1016F#6PDamn. Feels like you just popped your head in\x01",
            "and solved all these crazy mysteries like they\x01",
            "were nothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0x18,
        (
            "#1545F#6PHaha... It's certainly impressive.\x02\x03",

            "#1540FEven I hadn't been able to deduce\x01",
            "quite that much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0x15,
        "#1513F#6PYou really are a genius, Renne.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #344
        0x1F,
        "Renne",
        (
            "#268F#11PI'm sure you could've worked this much out if\x01",
            "you'd really put your mind to it, Joshua...\x02\x03",

            "#269FUnless Estelle's stupidity IS actually contagious\x01",
            "and rubbed off on you.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #345
        0x101,
        "#1019F#6PWell, that's not very nice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0x15,
        "#1514F#6PHaha... I'm pretty sure that's not the case.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0x11,
        "#067F#6PHeehee...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0x1B,
        "#1521F#6PDeary me...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #349
        0x1F,
        "Renne",
        (
            "#265F#11PEither way, it sounds like this Lord of Phantasma\x01",
            "person likes games just as much as I do.\x02\x03",

            "And without me, I don't know if you'll be able to\x01",
            "beat them...so I suppose I'd better lend you all a\x01",
            "hand.\x02\x03",

            "#261FTeehee. I hope you're all very grateful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0x101,
        "#1016F#6PUhh... Yeah... Sure...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0x1A,
        (
            "#811F#6PIt's nice to have a cutie like you on board,\x01",
            "Renne!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #352
        0x1F,
        "Renne",
        (
            "#261F#11PWell, now that that's settled...\x02\x03",

            "...it's time to use that cube to take us back\x01",
            "to the fifth plane so we can move on.\x02\x03",

            "#265FNow that we've gotten closer to working out\x01",
            "what's going on, we should be able to move\x01",
            "on to the next part of the game board now.\x02\x03",

            "I'm guessing our opponent's ready to make\x01",
            "their next move, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0x10F,
        (
            "#1806F#6P*sigh* Someone's confident.\x02\x03",

            "#1447FStill, have it your way. It's not as though we\x01",
            "have any option other than to press on.\x02\x03",

            "#1443FI'm expecting we'll encounter a devil at the\x01",
            "end of this plane just like we have at all of\x01",
            "the others.\x02\x03",

            "We should only move on when we're sure we\x01",
            "can handle it.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #354
        0x1F,
        "Renne",
        (
            "#268F#11PAww... I could really do without the extra \x01",
            "trouble.\x02\x03",

            "#269FThen again, I am kind of curious what these\x01",
            "devils are like in reality.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1F, 135, 400)
    Sleep(500)

    NpcTalk(    #355
        0x1F,
        "Renne",
        (
            "#261F#5PWould you like to come and have a look with\x01",
            "me, Tita?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #356
        0x11,
        (
            "#067F#6PI-I'm not sure just the two of us going would be\x01",
            "such a good idea...\x02",
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
            "#1017F#6P(D'aww. She was so opposed to being with us \x01",
            "earlier, but look at her now.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0x15,
        (
            "#1513F#6P(Yeah... I'm really glad she came around.)\x02\x03",

            "#1503F(Hopefully we'll get a chance to talk to her\x01",
            "while we're in here, too.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0x101,
        "#1025F#6P(Yeah...)\x02",
    )

    CloseMessageWindow()

    def lambda_E032():
        OP_6B(2300, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_E032)
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

    # Function_13_8B71 end

    def Function_14_E1EE(): pass

    label("Function_14_E1EE")

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

    # Function_14_E1EE end

    def Function_15_E22F(): pass

    label("Function_15_E22F")

    OP_8C(0xFE, 315, 400)
    OP_8F(0xFE, 0x8E8, 0xFA0, 0xFFFFF8C6, 0x5DC, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_15_E22F end

    def Function_16_E252(): pass

    label("Function_16_E252")


    def lambda_E258():
        OP_95(0xFE, 0x1CC, 0xFA0, 0xFFFFFE0C, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E258)
    WaitChrThread(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    OP_22(0xA4, 0x0, 0x64)
    Return()

    # Function_16_E252 end

    def Function_17_E285(): pass

    label("Function_17_E285")

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

    def lambda_E4D6():
        OP_6D(-950, 4000, -980, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_E4D6)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x10F, 0x0)
    Sleep(300)

    def lambda_E502():
        OP_6D(-1180, 4000, 1800, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E502)

    def lambda_E51A():
        OP_67(0, 5690, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E51A)

    def lambda_E532():
        OP_6B(2450, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E532)

    def lambda_E542():
        OP_6E(405, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_E542)
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

    def lambda_E5B2():

        label("loc_E5B2")

        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        OP_48()
        Jump("loc_E5B2")

    QueueWorkItem2(0x22, 3, lambda_E5B2)
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

    def lambda_E667():
        OP_8F(0xFE, 0x0, 0x1770, 0x64, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_E667)
    WaitChrThread(0x22, 0x0)
    Sleep(500)

    ChrTalk(    #360
        0x101,
        (
            "#1002F#6PThe way it glows is pretty different compared\x01",
            "to all the other sealing stones.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0x15,
        (
            "#1502F#6PYou're right... I wonder who's going to appear\x01",
            "out of it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0x16,
        "#1164F#6P...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    def lambda_E75F():
        OP_6D(-1180, 4000, 800, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E75F)

    def lambda_E777():
        TurnDirection(0x101, 0x16, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E777)
    Sleep(100)
    TurnDirection(0x15, 0x16, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #363
        0x101,
        "#1015F#5PKloe?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0x15,
        "#1504F#5PIs something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0x16,
        (
            "#1165F#6PNo, it's just...\x02\x03",

            "#1382FThe light radiating from it feels somehow...\x01",
            "nostalgic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0x101,
        "#1004F#5PHuh?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    OP_20(0x7D0)
    SetMessageWindowPos(-1, 100, -1, -1)

    AnonymousTalk(    #367
        "\x07\x0CThat comes as no surprise.\x07\x00\x02",
    )

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

    def lambda_EA1D():
        OP_8C(0x101, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_EA1D)
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

    def lambda_EC0C():
        OP_6D(0, 7500, 3760, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_EC0C)

    def lambda_EC24():
        OP_67(0, 1650, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_EC24)

    def lambda_EC3C():
        OP_6B(2700, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_EC3C)

    def lambda_EC4C():
        OP_6E(363, 3500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EC4C)

    def lambda_EC5C():
        OP_8F(0xFE, 0x0, 0x1F40, 0x5DC, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_EC5C)
    WaitChrThread(0x22, 0x0)
    WaitChrThread(0x10F, 0x0)
    Sleep(500)

    def lambda_EC86():
        OP_6B(2000, 8000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_EC86)

    def lambda_EC96():
        OP_6D(0, 8000, 3760, 8000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_EC96)
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

    def lambda_EDB3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x7D0)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_EDB3)
    OP_22(0x99, 0x0, 0x64)
    OP_82(0x3, 0x0)
    OP_0D()
    Sleep(2000)
    PlayEffect(0x4, 0x4, 0x22, 0, 700, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_22(0x138, 0x0, 0x64)
    OP_23(0x146)

    def lambda_EE10():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_EE10)
    OP_82(0x2, 0x2)
    WaitChrThread(0x22, 0x0)
    PlayEffect(0x0, 0x7, 0x22, 0, 800, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)
    Fade(500)
    OP_82(0x1, 0x0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #368
        0x10F,
        "#1444F#5PIt's her...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0x101,
        "#1020F#5PWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0x15,
        "#1504F#5PShe looks like...!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(3540, 6000, 2620, 0)
    OP_67(0, 2790, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(35000, 0)
    OP_6E(345, 0)

    def lambda_EF04():
        OP_6D(3540, 4000, 2620, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_EF04)

    def lambda_EF1C():
        OP_67(0, 2790, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_EF1C)

    def lambda_EF34():
        OP_6B(2900, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_EF34)

    def lambda_EF44():
        OP_6E(345, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_EF44)

    def lambda_EF54():
        OP_8F(0xFE, 0x0, 0x1388, 0x5DC, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_EF54)
    Sleep(1000)
    OP_82(0x2, 0x2)
    WaitChrThread(0x22, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x10F, 0x2)
    Sleep(800)

    NpcTalk(    #371
        0x22,
        "Ghost",
        "\x07\x0C#5P...\x07\x00\x02",
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
        "Ghost",
        (
            "\x07\x0C#5PI'm so glad I can finally communicate with\x01",
            "you like this.\x02\x03",

            "Heehee... I wonder how many hundreds of\x01",
            "years it's been since I was last able to hold\x01",
            "a true conversation?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #373
        0x12,
        "#173F#11PY-Your Highness...? Wait...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0x16,
        "#1164F#6PY-You aren't...are you...?\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x200, 0x96, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x200, 0xFFFFFF, 0x1, "C_VIS439._CH")
    OP_C6(0x0, 0x0, 140000, 0, 500)
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(2000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("Female Ghost")

    AnonymousTalk(    #375
        (
            "\x07\x0CIt's a pleasure to have the chance to meet one of my own descendants.\x02\x03",

            "And allow me to extend a hand of welcome to all of you, visitors to my\x01",
            "garden.\x02\x03",

            "My name is Celeste.\x02\x03",

            "Celeste D. Auslese.\x07\x00\x02",
        )
    )

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
    OP_F7(0x5, 0x0, 0x0)
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
            "[Save]\x01",              # 0
            "[Next Chapter]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F29A")
    ShowSaveMenu()

    label("loc_F29A")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_17_E285 end

    SaveToFile()

Try(main)
