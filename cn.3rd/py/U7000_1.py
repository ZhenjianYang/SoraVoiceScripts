from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U7000_1 ._SN',
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
        "Function_3_9AA",          # 03, 3
        "Function_4_AC6",          # 04, 4
        "Function_5_D92",          # 05, 5
        "Function_6_EA4",          # 06, 6
        "Function_7_EC0",          # 07, 7
        "Function_8_EDC",          # 08, 8
        "Function_9_FEE",          # 09, 9
        "Function_10_100A",        # 0A, 10
        "Function_11_1026",        # 0B, 11
        "Function_12_1138",        # 0C, 12
        "Function_13_1154",        # 0D, 13
        "Function_14_1170",        # 0E, 14
        "Function_15_1EF0",        # 0F, 15
        "Function_16_24E3",        # 10, 16
        "Function_17_25EA",        # 11, 17
        "Function_18_26A7",        # 12, 18
        "Function_19_2764",        # 13, 19
        "Function_20_2821",        # 14, 20
        "Function_21_289A",        # 15, 21
        "Function_22_370F",        # 16, 22
        "Function_23_374C",        # 17, 23
        "Function_24_3789",        # 18, 24
        "Function_25_387B",        # 19, 25
        "Function_26_3970",        # 1A, 26
        "Function_27_4170",        # 1B, 27
        "Function_28_426D",        # 1C, 28
        "Function_29_4C20",        # 1D, 29
        "Function_30_62C2",        # 1E, 30
        "Function_31_633B",        # 1F, 31
        "Function_32_698D",        # 20, 32
        "Function_33_7853",        # 21, 33
        "Function_34_9840",        # 22, 34
        "Function_35_9D19",        # 23, 35
        "Function_36_C384",        # 24, 36
        "Function_37_C3EB",        # 25, 37
        "Function_38_C895",        # 26, 38
        "Function_39_D987",        # 27, 39
        "Function_40_DE58",        # 28, 40
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
    OP_D2(0x270089, 0x27008D, 0x13)
    SetChrPos(0x109, -510, 2070, -19920, 0)
    SetChrPos(0x10F, 1290, 1980, -20110, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_6D(-680, 4100, -14130, 0)
    OP_67(0, 7020, -10000, 0)
    OP_6B(1800, 0)
    OP_6C(315000, 0)
    OP_6E(490, 0)

    def lambda_13B():
        OP_8E(0xFE, 0xFFFFFDEE, 0x1004, 0xFFFFC586, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_13B)
    Sleep(500)

    def lambda_15B():
        OP_8E(0xFE, 0x2DA, 0x1004, 0xFFFFC446, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_15B)
    Sleep(300)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Sleep(300)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #0
        0x109,
        "#1079F#6P那是……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(1000)
    OP_6D(-500, 4000, -15000, 0)
    OP_67(0, 8540, -10000, 0)
    OP_6B(2100, 0)
    OP_6C(315000, 0)
    OP_6E(516, 0)

    def lambda_210():
        OP_6D(0, 5600, 5620, 5500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_210)

    def lambda_228():
        OP_67(0, 2350, -10000, 5500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_228)

    def lambda_240():
        OP_6B(1900, 5500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_240)

    def lambda_250():
        OP_6C(0, 5500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_250)

    def lambda_260():
        OP_6E(493, 5500)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_260)
    Sleep(5000)

    def lambda_275():
        OP_8E(0xFE, 0xFFFFFD9E, 0xFA0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_275)
    Sleep(400)

    def lambda_295():
        OP_8E(0xFE, 0x3E8, 0xFA0, 0xFFFFFF6A, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_295)
    Sleep(600)

    def lambda_2B5():
        OP_6D(0, 5600, 4620, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2B5)

    def lambda_2CD():
        OP_67(0, 4000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2CD)

    def lambda_2E5():
        OP_6B(2100, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2E5)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x109, 0x1)
    Fade(500)
    OP_6D(-2029, 4000, 4520, 0)
    OP_67(0, 4610, -10000, 0)
    OP_6B(2340, 0)
    OP_6C(314000, 0)
    OP_6E(492, 0)
    SetChrPos(0x109, -440, 4000, -110, 0)
    SetChrPos(0x10F, 1000, 4000, -190, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #1
        0x109,
        (
            "#1063F#6P这……\x01",
            "还真是别有一番风情啊。\x02\x03",

            "从建造风格来看，\x01",
            "好像不是塞姆里亚\x01",
            "时代的东西呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10F,
        (
            "#1440F#6P的确……\x01",
            "不像是装置，而只是个石碑。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #3
        0x10F,
        (
            "#1444F#6P……啊。\x01",
            "下面好像写着什么。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x109,
        "#1079F#6P哦，真的啊。\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_482():
        OP_6D(-410, 4200, 6220, 2500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_482)

    def lambda_49A():
        OP_67(0, 4720, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_49A)

    def lambda_4B2():
        OP_6B(2000, 2500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_4B2)

    def lambda_4C2():
        OP_8F(0xFE, 0x78, 0x1068, 0x1432, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4C2)
    Sleep(800)

    def lambda_4E2():
        OP_8F(0xFE, 0x8E8, 0xFA0, 0xFBE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_4E2)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x109, 0x1)
    Fade(250)
    SetChrChipByIndex(0x109, 19)
    SetChrSubChip(0x109, 0)
    OP_0D()
    WaitChrThread(0x10F, 0x0)

    def lambda_51C():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_51C)
    Sleep(500)

    ChrTalk(    #5
        0x109,
        "#1067F#5P我来看看……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_AD(0x240103, 0xBE, 0x82, 0x1F4)
    Sleep(1500)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 230, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "\x07\x00  The Garden of Recluse\x01",
            "      （隐者之庭院）\x18\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1500)

    ChrTalk(    #7
        0x109,
        "#1079F#5P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10F,
        "#1802F#6P……这是什么。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x109,
        (
            "#1060F#5P唔，是某种讯息，\x01",
            "还是……\x02",
        )
    )

    Jump("loc_65D")

    label("loc_65D")

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)
    TurnDirection(0x109, 0x10F, 400)

    ChrTalk(    #10
        0x109,
        (
            "#1060F#5P算了，\x01",
            "先来调查看看吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-450, 4200, 5100, 0)
    OP_67(0, 6620, -10000, 0)
    OP_6B(1950, 0)
    OP_6C(314000, 0)
    OP_6E(450, 0)
    SetChrPos(0x109, -330, 4000, 3500, 0)
    SetChrPos(0x10F, 1190, 4000, 3120, 0)
    Sleep(3000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #11
        0x10F,
        "#1802F#6P…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x109,
        (
            "#1065F#6P不行……\x01",
            "好像什么机关都没有。\x02\x03",

            "#1067F似乎是用普通的石头造的，\x01",
            "可以肯定它不是某种装置了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10F,
        (
            "#1445F#6P是啊……\x02\x03",

            "#1440F总之，\x01",
            "强行把它破坏怎么样？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x10F, 400)

    ChrTalk(    #14
        0x109,
        (
            "#1061F#5P说的也是──\x02\x01",

            "#1069F喂，怎么可以！\x02\x03",

            "#1068F就算不是什么装置，\x01",
            "谁敢保证它不会引发什么现象呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10F, 0x109, 400)
    Sleep(300)

    ChrTalk(    #15
        0x10F,
        (
            "#1447F#6P……开玩笑的。\x01",
            "只是随便说说而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x109,
        (
            "#1068F#5P（你的眼神\x01",
            "  明明是认真的……）\x02\x03",

            "#1060F总之，\x01",
            "过激的手段还是先放放。\x02\x03",

            "先不管这里了，\x01",
            "我们到别的地方去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10F,
        "#1440F#6P……我知道了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2601)
    Sleep(300)
    Fade(1000)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_2_AC end

    def Function_3_9AA(): pass

    label("Function_3_9AA")

    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xC8, 0xFA0, 0xFAA, 0x7D0, 0x0)
    OP_8E(0xFE, 0x97E, 0xFA0, 0xFBE, 0x7D0, 0x0)
    OP_8E(0xFE, 0xA8C, 0xFA0, 0x1824, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0xAF0, 0xFA0, 0x1B94, 0x7D0, 0x0)
    OP_8E(0xFE, 0x7A8, 0xFA0, 0x2008, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFF7E, 0xFA0, 0x222E, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1000)
    OP_8C(0xFE, 270, 400)
    OP_8E(0xFE, 0xFFFFFABA, 0xFA0, 0x20D0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF704, 0xFA0, 0x1E32, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 0)
    OP_8F(0xFE, 0xFFFFF68C, 0xFA0, 0xF82, 0x7D0, 0x0)
    OP_8E(0xFE, 0x32, 0xFA0, 0xF46, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_3_9AA end

    def Function_4_AC6(): pass

    label("Function_4_AC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 2)), scpexpr(EXPR_END)), "loc_ACE")
    Return()

    label("loc_ACE")

    EventBegin(0x0)
    Fade(500)
    SetChrPos(0x109, 750, 11920, 37190, 0)
    SetChrPos(0x10F, -860, 11920, 36940, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_6D(-1060, 11920, 38690, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(1930, 0)
    OP_6C(315000, 0)
    OP_6E(484, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #18
        0x10F,
        "#1444F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x109,
        "#1063F#6P这是……\x02",
    )

    CloseMessageWindow()

    def lambda_B8E():
        OP_6D(-19030, 23080, 86830, 5000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B8E)

    def lambda_BA6():
        OP_67(0, 4890, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_BA6)

    def lambda_BBE():
        OP_6B(2530, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_BBE)

    def lambda_BCE():
        OP_6C(0, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_BCE)

    def lambda_BDE():
        OP_6E(484, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_BDE)
    WaitChrThread(0x109, 0x0)
    SetMessageWindowPos(100, 350, -1, -1)
    SetChrName("莉丝")

    AnonymousTalk(    #20
        (
            "\x07\x00#1802F这里……\x01",
            "到底是什么地方？\x02",
        )
    )

    Jump("loc_C2D")

    label("loc_C2D")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(250, 350, -1, -1)
    SetChrName("凯文")

    AnonymousTalk(    #21
        (
            "\x07\x00#1067F不知道……\x02\x03",

            "#1063F只是，就算我们朝那边说话，\x01",
            "也听不到什么回音。\x02\x03",

            "所以我们现在应该是\x01",
            "处在非常广阔的空间中。\x02",
        )
    )

    Jump("loc_CCF")

    label("loc_CCF")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 350, -1, -1)
    SetChrName("莉丝")

    AnonymousTalk(    #22
        "\x07\x00#1445F……是吗。\x02",
    )

    Jump("loc_D03")

    label("loc_D03")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2602)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-130, 11920, 40940, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(450, 0)
    SetChrPos(0x109, -130, 11920, 40940, 0)
    SetChrPos(0x10F, -130, 11920, 40940, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_4_AC6 end

    def Function_5_D92(): pass

    label("Function_5_D92")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -550, 4100, -14830, 0)
    SetChrPos(0x10F, 800, 4100, -15490, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_6D(470, 4100, -14860, 0)
    OP_67(0, 11440, -10000, 0)
    OP_6B(2690, 0)
    OP_6C(314000, 0)
    OP_6E(565, 0)
    OP_43(0x109, 0x0, 0x1, 0x6)
    Sleep(200)
    OP_43(0x10F, 0x0, 0x1, 0x7)

    def lambda_E2A():
        OP_6D(-150, 4000, -5160, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_E2A)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x3)
    Sleep(1000)
    Fade(1000)
    OP_6D(-680, 4000, -2430, 0)
    OP_67(0, 6320, -10000, 0)
    OP_6B(1720, 0)
    OP_6C(315000, 0)
    OP_6E(496, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    Call(1, 14)
    EventEnd(0x0)
    Return()

    # Function_5_D92 end

    def Function_6_EA4(): pass

    label("Function_6_EA4")

    OP_8E(0xFE, 0xFFFFFBF0, 0xFA0, 0xFFFFF2C2, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_6_EA4 end

    def Function_7_EC0(): pass

    label("Function_7_EC0")

    OP_8E(0xFE, 0x352, 0xFA0, 0xFFFFF2D6, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_7_EC0 end

    def Function_8_EDC(): pass

    label("Function_8_EDC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -11540, 4100, -9000, 45)
    SetChrPos(0x10F, -11400, 4100, -10550, 45)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_6D(-10040, 4000, -7610, 0)
    OP_67(0, 10340, -10000, 0)
    OP_6B(2690, 0)
    OP_6C(282000, 0)
    OP_6E(561, 0)
    OP_43(0x109, 0x0, 0x1, 0x9)
    Sleep(100)
    OP_43(0x10F, 0x0, 0x1, 0xA)

    def lambda_F74():
        OP_6D(-3940, 4000, -3290, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_F74)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x3)
    Sleep(1000)
    Fade(1000)
    OP_6D(-680, 4000, -2430, 0)
    OP_67(0, 6320, -10000, 0)
    OP_6B(1720, 0)
    OP_6C(315000, 0)
    OP_6E(496, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    Call(1, 14)
    EventEnd(0x0)
    Return()

    # Function_8_EDC end

    def Function_9_FEE(): pass

    label("Function_9_FEE")

    OP_8E(0xFE, 0xFFFFFBF0, 0xFA0, 0xFFFFF2C2, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_9_FEE end

    def Function_10_100A(): pass

    label("Function_10_100A")

    OP_8E(0xFE, 0x352, 0xFA0, 0xFFFFF2D6, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_10_100A end

    def Function_11_1026(): pass

    label("Function_11_1026")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 11330, 4100, -9810, 270)
    SetChrPos(0x10F, 12980, 4100, -9720, 270)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_6D(11120, 4100, -10060, 0)
    OP_67(0, 13700, -10000, 0)
    OP_6B(2690, 0)
    OP_6C(359000, 0)
    OP_6E(556, 0)
    OP_43(0x109, 0x0, 0x1, 0xC)
    Sleep(400)
    OP_43(0x10F, 0x0, 0x1, 0xD)

    def lambda_10BE():
        OP_6D(1390, 4000, -3380, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_10BE)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x3)
    Sleep(1000)
    Fade(1000)
    OP_6D(-680, 4000, -2430, 0)
    OP_67(0, 6320, -10000, 0)
    OP_6B(1720, 0)
    OP_6C(315000, 0)
    OP_6E(496, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    Call(1, 14)
    EventEnd(0x0)
    Return()

    # Function_11_1026 end

    def Function_12_1138(): pass

    label("Function_12_1138")

    OP_8E(0xFE, 0xFFFFFBF0, 0xFA0, 0xFFFFF2C2, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_12_1138 end

    def Function_13_1154(): pass

    label("Function_13_1154")

    OP_8E(0xFE, 0x352, 0xFA0, 0xFFFFF2D6, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_13_1154 end

    def Function_14_1170(): pass

    label("Function_14_1170")

    Sleep(300)
    OP_D2(0x260286, 0x26028B, 0x13)
    LoadEffect(0x0, "map\\mp252_01.eff")
    LoadEffect(0x1, "magic\\mg054_3.eff")
    LoadEffect(0x2, "monster\\ms31000.eff")

    ChrTalk(    #23
        0x10F,
        (
            "#1445F#6P全部调查过一遍了……\x02\x03",

            "可是没有发现任何\x01",
            "看起来比较重要的线索……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x109,
        (
            "#1065F#5P是啊……\x02\x03",

            "#1060F不过，\x01",
            "我大概知道这里\x01",
            "是什么样的地方了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #25
        0x10F,
        "#1444F#6P什么意思……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x109,
        (
            "#1065F#5P这里既是利贝尔，\x01",
            "又是不存在于利贝尔的地方……\x02\x03",

            "#1063F应该是某种异空间吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10F,
        (
            "#1803F#6P………………………………\x02\x03",

            "#1443F……请你说得详细一些。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x109,
        (
            "#1060F#5P对了，上次与『环』有关的事件\x01",
            "就发生过这样的事情……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #29
        (
            "\x07\x05凯文向莉丝说明了\x01",
            "在『四轮之塔』中隐藏着的\x01",
            "因为『环』被封印而形成的异空间的事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #30
        0x10F,
        (
            "#1444F#6P有这样的事……\x02\x03",

            "#1802F那么，\x01",
            "这里也是和那一样的空间了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x109,
        (
            "#1060F#5P至少是一种可能性吧。\x02\x03",

            "#1065F不过就算这么假定，\x01",
            "还是有一些奇怪的地方。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #32
        0x10F,
        (
            "#1443F#6P我知道了……\x02\x03",

            "是《边走边吃王国纪行》吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x109,
        (
            "#1063F#5P没错。\x02\x03",

            "#1065F假设这里是一千二百年前\x01",
            "与『辉之环』一起封印的\x01",
            "异空间的一角的话……\x02\x03",

            "其中会存在今年刚发行的书\x01",
            "这个现象就显得很奇怪了。\x02\x03",

            "书架上的稀有书籍\x01",
            "也都是『大崩坏』之后才有的东西。\x02\x03",

            "#1067F也就是说……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10F,
        (
            "#1445F#6P有什么人最近\x01",
            "出入过这里……\x02\x03",

            "#1443F……是那个黑衣男子？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x109,
        (
            "#1063F#5P有这种可能性。\x02\x03",

            "#1068F……虽说如此，\x01",
            "我可不认为那个男人\x01",
            "会看《边走边吃王国纪行》这种书。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x10F,
        "#1446F#6P这倒是没错……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x109,
        (
            "#1063F#5P唉，不管怎么说，\x01",
            "现在的情况肯定是\x01",
            "某个人事先计划好的。\x02\x03",

            "说不定『方石』会到\x01",
            "我们手里这件事本身\x01",
            "也是经过安排的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10F,
        (
            "#1445F#6P……连这些都………\x02\x03",

            "#1802F可是，就算是这样好了，\x01",
            "我们接下来该怎么办……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x109,
        (
            "#1068F#5P唉，这就是问题所在。\x02\x03",

            "#1067F如果有终端之类的东西\x01",
            "至少还可以做一些尝试……\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_22(0x15F, 0x0, 0x64)
    Sleep(500)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #40
        0x10F,
        "#1444F#6P啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x109,
        "#1063F#5P又来了……！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(-1190, 4000, -2560, 0)
    OP_67(0, 6320, -10000, 0)
    OP_6B(1600, 0)
    OP_6C(315000, 0)
    OP_6E(496, 0)
    ClearMapFlags(0x10)
    OP_22(0x8F, 0x0, 0x64)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 19)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)
    PlayEffect(0x0, 0x0, 0x109, 270, 1250, 100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xC9, 0x0, 0x64)
    OP_0D()
    Sleep(1500)
    PlayEffect(0x1, 0xFF, 0x10F, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_19E7():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_19E7)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x109, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1A3B():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1A3B)

    ChrTalk(    #42
        0x10F,
        "#1445F#6P啊……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x109,
        "#1070F#5P呜……！？\x02",
    )

    CloseMessageWindow()
    OP_22(0x14B, 0x0, 0x50)
    Sleep(500)
    Fade(500)
    OP_82(0x0, 0x0)
    OP_23(0xC9)
    OP_0D()
    Sleep(500)

    ChrTalk(    #44
        0x10F,
        "#1802F#6P刚、刚才的是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x109,
        (
            "#1063F#5P什么东西破碎的声音……\x02\x03",

            "#1069F……难道……！？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #46
        (
            "\x07\x05凯文从怀中掏出了战术导力器。\x02\x03",

            "其中嵌入的结晶回路一个不剩地全部粉碎了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #47
        0x10F,
        "#1444F#6P！？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #48
        (
            "\x07\x05莉丝也从怀中掏出了\x01",
            "战术导力器。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_62(0x10F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x10F)
    Sleep(300)

    ChrTalk(    #49
        0x10F,
        "#1802F#6P……我的也是……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x109,
        (
            "#1067F#5P可恶，\x01",
            "备用的结晶回路也没幸免……\x02\x03",

            "这到底是怎么回事……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x11D, 0x0, 0x64)
    OP_22(0x217, 0x0, 0x64)
    Fade(500)
    PlayEffect(0x2, 0x2, 0x109, 100, 1000, 400, 0, 0, 0, 1400, 1400, 1400, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_82(0x2, 0x2)
    OP_23(0x11D)
    Sleep(500)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #51
        0x109,
        "#1079F#5P什么……！？\x02",
    )

    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)

    def lambda_1D70():
        OP_6D(0, 4000, 10440, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1D70)

    def lambda_1D88():
        OP_67(0, 3870, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1D88)

    def lambda_1DA0():
        OP_6B(2100, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1DA0)

    def lambda_1DB0():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1DB0)

    def lambda_1DC0():
        OP_6E(507, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_1DC0)
    WaitChrThread(0x109, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1D(0xB8)
    OP_22(0x15F, 0x0, 0x64)
    Fade(1000)
    OP_E5(0x0, 0xFF, 0x13, 262144)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    OP_A2(0x2605)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x10)
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/U7003   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_1170 end

    def Function_15_1EF0(): pass

    label("Function_15_1EF0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D2(0x260286, 0x26028B, 0x13)
    SetChrPos(0x109, -1040, 4000, -3390, 0)
    SetChrPos(0x10F, 850, 4000, -3370, 0)
    SetChrChipByIndex(0x109, 19)
    SetChrSubChip(0x109, 0)
    SetChrFlags(0x109, 0x20)
    OP_82(0x81, 0x0)
    OP_71(0x400, 0x0)
    ExitThread()
    OP_6D(-370, 21220, 40970, 0)
    OP_67(0, 3720, -10000, 0)
    OP_6B(2450, 0)
    OP_6C(315000, 0)
    OP_6E(438, 0)

    def lambda_1F83():
        OP_6D(-370, 11800, 40970, 5000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1F83)

    def lambda_1F9B():
        OP_67(0, 7000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1F9B)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Fade(1000)
    OP_22(0x15F, 0x0, 0x64)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Sleep(1000)

    def lambda_200C():
        OP_6D(0, 15770, 34670, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_200C)

    def lambda_2024():
        OP_67(0, 2230, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2024)

    def lambda_203C():
        OP_6B(2350, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_203C)

    def lambda_204C():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_204C)

    def lambda_205C():
        OP_6E(458, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_205C)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    Fade(1000)
    OP_22(0x117, 0x0, 0x64)
    OP_72(0x400, 0x0)
    ExitThread()
    OP_0D()
    Sleep(1000)

    def lambda_208C():
        OP_6D(-900, 4000, -2500, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_208C)

    def lambda_20A4():
        OP_67(0, 5950, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_20A4)

    def lambda_20BC():
        OP_6B(1700, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_20BC)

    def lambda_20CC():
        OP_6C(315000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_20CC)

    def lambda_20DC():
        OP_6E(496, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_20DC)
    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #52
        0x10F,
        "#1444F#6P发、发生了什么事……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x109,
        (
            "#1067F#5P……不知道………\x02\x03",

            "#1063F不过，肯定是这东西\x01",
            "对其它的物体产生了什么干涉。\x02\x03",

            "应该也包括我们的结晶回路\x01",
            "全部被破坏的现象在内。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10F,
        "#1802F#6P…………………………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10F, 270, 400)
    Sleep(300)

    ChrTalk(    #55
        0x10F,
        (
            "#1443F#6P……这东西，\x01",
            "我们不能把它放着不管吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)
    Sleep(300)

    ChrTalk(    #56
        0x109,
        (
            "#1065F#5P不，如果放着不管，\x01",
            "我们才真正无计可施了。\x02\x03",

            "#1063F总之，\x01",
            "这下应该会有什么线索出现了。\x02\x03",

            "我们把发生变化的地点\x01",
            "再彻底调查一次吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x10F,
        "#1440F#6P……我知道了。\x02",
    )

    CloseMessageWindow()
    OP_20(0xBB8)

    def lambda_230B():
        OP_6B(2100, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_230B)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    Sleep(2000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_C0(0x26, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_34(0x8, 0xFFFF)
    OP_34(0xE, 0xFFFF)
    OP_3F(0x328, 1)
    OP_3E(0x33E, 1)
    AddSepith(0x0, 0x32)
    AddSepith(0x1, 0x32)
    AddSepith(0x2, 0x32)
    AddSepith(0x3, 0x32)
    AddSepith(0x4, 0x32)
    AddSepith(0x5, 0x32)
    AddSepith(0x6, 0x32)

    AnonymousTalk(    #58
        (
            "\x07\x00得到了结晶回路\x01",
            "破损后的碎片：\x01",
            "\x07\x02#56I地之耀晶片×５０\x01",
            "\x07\x02#57I水之耀晶片×５０\x01",
            "\x07\x02#58I火之耀晶片×５０\x01",
            "\x07\x02#59I风之耀晶片×５０\x01",
            "\x07\x02#62I时之耀晶片×５０\x01",
            "\x07\x02#60I空之耀晶片×５０\x01",
            "\x07\x02#61I幻之耀晶片×５０\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_6D(240, 4000, -2570, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(450, 0)
    SetChrPos(0x109, 240, 4000, -2570, 0)
    SetChrPos(0x10F, 240, 4000, -2570, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    ClearChrFlags(0x109, 0x20)
    OP_69(0x0, 0x0)
    OP_72(0x400, 0x0)
    ExitThread()
    Sleep(500)
    OP_1D(0xD2)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_15_1EF0 end

    def Function_16_24E3(): pass

    label("Function_16_24E3")

    EventBegin(0x1)
    TurnDirection(0x10F, 0x109, 400)

    ChrTalk(    #59
        0x10F,
        (
            "#1444F……凯文。\x01",
            "你不调查那个石碑吗？\x02\x03",

            "它正发着光呢……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x10F, 400)

    ChrTalk(    #60
        0x109,
        (
            "#1063F是啊……\x01",
            "就先调查那个吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2593")
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Jump("loc_25D8")

    label("loc_2593")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25B7")
    OP_90(0x0, 0x5DC, 0x0, 0x5DC, 0xBB8, 0x0)
    Jump("loc_25D8")

    label("loc_25B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25D8")
    OP_90(0x0, 0xFFFFFA24, 0x0, 0x5DC, 0xBB8, 0x0)

    label("loc_25D8")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_16_24E3 end

    def Function_17_25EA(): pass

    label("Function_17_25EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_25F6")
    Return()

    label("loc_25F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25FF")
    Return()

    label("loc_25FF")

    EventBegin(0x1)
    TurnDirection(0x10F, 0x109, 400)

    ChrTalk(    #61
        0x10F,
        (
            "#1444F……凯文。\x01",
            "你不调查那个石碑吗？\x02\x03",

            "它正发着光呢……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x10F, 400)

    ChrTalk(    #62
        0x109,
        (
            "#1063F是啊……\x01",
            "就先调查那个吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_17_25EA end

    def Function_18_26A7(): pass

    label("Function_18_26A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26B3")
    Return()

    label("loc_26B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26BC")
    Return()

    label("loc_26BC")

    EventBegin(0x1)
    TurnDirection(0x10F, 0x109, 400)

    ChrTalk(    #63
        0x10F,
        (
            "#1444F……凯文。\x01",
            "你不调查那个石碑吗？\x02\x03",

            "它正发着光呢……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x10F, 400)

    ChrTalk(    #64
        0x109,
        (
            "#1063F是啊……\x01",
            "就先调查那个吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_90(0x0, 0x5DC, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_18_26A7 end

    def Function_19_2764(): pass

    label("Function_19_2764")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2770")
    Return()

    label("loc_2770")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2779")
    Return()

    label("loc_2779")

    EventBegin(0x1)
    TurnDirection(0x10F, 0x109, 400)

    ChrTalk(    #65
        0x10F,
        (
            "#1444F……凯文。\x01",
            "你不调查那个石碑吗？\x02\x03",

            "它正发着光呢……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x10F, 400)

    ChrTalk(    #66
        0x109,
        (
            "#1063F是啊……\x01",
            "就先调查那个吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_90(0x0, 0xFFFFFA24, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_19_2764 end

    def Function_20_2821(): pass

    label("Function_20_2821")

    TalkBegin(0xFF)

    ChrTalk(    #67
        0x10F,
        "#1802F这是什么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x109,
        (
            "#1063F好像是结界一类的东西……\x02\x03",

            "对面还有一个\x01",
            "让人在意的法阵……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_20_2821 end

    def Function_21_289A(): pass

    label("Function_21_289A")

    EventBegin(0x0)
    OP_D2(0x260286, 0x26028B, 0x13)
    LoadEffect(0x0, "map\\mp252_01.eff")
    Fade(500)
    SetChrPos(0x109, 800, 4000, 1030, 0)
    SetChrPos(0x10F, -540, 4000, 810, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_6D(-860, 4000, 2380, 0)
    OP_67(0, 5680, -10000, 0)
    OP_6B(1990, 0)
    OP_6C(315000, 0)
    OP_6E(411, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #69
        0x10F,
        (
            "#1445F#5P不是导力器，\x01",
            "也不是古代遗物，\x01",
            "单纯的石块为什么会……\x02\x03",

            "#1443F简直……\x01",
            "就像童话中的魔法一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x109,
        (
            "#1065F#6P啊～……　\x01",
            "的确有这样的感觉呢。\x02\x03",

            "#1063F反正肯定是我们的常识\x01",
            "所不能理解的构造吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 100, -1, -1)

    AnonymousTalk(    #71
        "\x07\x0C\x18#2S#80W………举起来………\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #72
        0x109,
        "#1079F#6P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x10F,
        "#1444F#5P刚、刚才是……\x02",
    )

    CloseMessageWindow()
    OP_43(0x109, 0x0, 0x1, 0x16)
    OP_43(0x10F, 0x0, 0x1, 0x17)
    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #74
        (
            "\x07\x0C\x18#2S#80W……把那个『方石』……\x01",
            "举到……石碑前面来……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_44(0x109, 0x0)
    OP_44(0x10F, 0x0)
    OP_8C(0x109, 0, 400)
    Sleep(100)

    def lambda_2B95():
        OP_8C(0x10F, 0, 400)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_2B95)

    ChrTalk(    #75
        0x109,
        (
            "#1069F#6P是谁！？\x02\x03",

            "是谁在说话！？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 100, -1, -1)

    AnonymousTalk(    #76
        "\x07\x0C\x18#2S#80W…………拜托你们…………\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 100, -1, -1)

    AnonymousTalk(    #77
        "\x07\x0C\x18#2S#80W…………………………………\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(1000)
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x10F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x109)
    OP_63(0x10F)
    OP_8C(0x10F, 90, 400)
    Sleep(300)

    ChrTalk(    #78
        0x10F,
        "#1443F#5P……怎么办？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x109,
        (
            "#1067F#6P哼……\x02\x03",

            "#1069F嘿！\x01",
            "管不了那么多了！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 19)
    SetChrSubChip(0x109, 0)
    OP_0D()
    OP_8C(0x10F, 0, 400)
    Fade(1000)
    OP_6D(0, 6900, 8770, 0)
    OP_67(0, 3810, -10000, 0)
    OP_6B(2460, 0)
    OP_6C(0, 0)
    OP_6E(433, 0)

    def lambda_2D81():
        OP_6D(0, 3950, 8770, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2D81)

    def lambda_2D99():
        OP_67(0, 3670, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2D99)

    def lambda_2DB1():
        OP_6B(2760, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2DB1)

    def lambda_2DC1():
        OP_6E(403, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2DC1)
    SetChrPos(0x109, 690, 4000, 1090, 0)
    SetChrPos(0x10F, -480, 4000, 870, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Sleep(1000)
    Fade(1000)
    OP_22(0x15F, 0x0, 0x64)
    OP_E5(0x2, 0xFF, 0x13, 1000)
    OP_0D()
    Fade(1000)
    OP_E5(0x2, 0xFF, 0x13, 700)
    OP_0D()
    WaitChrThread(0x109, 0x2)
    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 100, -1, -1)

    AnonymousTalk(    #80
        "\x07\x05#2S#40W………异邦者们啊………\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #81
        0x109,
        "#1063F#6P又来了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x10F,
        (
            "#1443F#6P不过……\x01",
            "和刚才的声音不同……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #83
        (
            "\x07\x05#2S#40W      …………欢迎到来…………\x01",
            "#800W\x01",
            "#40W   响应吾主意愿，赐予汝等力量……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)

    ChrTalk(    #84
        0x109,
        "#1079F#6P咦……？\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #85
        (
            "\x07\x05#2S#40W           付出同等代价……\x01",
            "#800W\x01",
            "#40W 如是，则按汝等所知常理赐予力量……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_62(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #86
        0x109,
        (
            "#1069F#6P等、等一下！\x02\x03",

            "同等代价……\x01",
            "我们所知道的常理……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x10F,
        (
            "#1446F#6P……………………………\x02\x03",

            "#1802F难道……\x01",
            "是用米拉买东西吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #88
        0x109,
        "#1060F#6P原来如此……！\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #89
        (
            "\x07\x05#2S#40W    …………已掌握要领…………\x01",
            "#800W\x01",
            "#40W  遵循汝等之理，进行等价交换……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Fade(1000)
    OP_22(0x161, 0x0, 0x64)
    OP_E5(0x2, 0xFF, 0x13, 1000)
    OP_0D()
    Fade(1000)
    OP_E5(0x2, 0xFF, 0x13, 700)
    OP_0D()
    Sleep(1000)
    OP_AA(0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #90
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_323C")

    label("loc_323C")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_324F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33D0")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "回复ＨＰ·ＥＰ\x01",      # 0
            "获得武具\x01",            # 1
            "合成结晶回路\x01",        # 2
            "结束\x01",                # 3
        )
    )

    Jump("loc_32A1")

    label("loc_32A1")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_32B9"),
        (1, "loc_3358"),
        (2, "loc_338C"),
        (SWITCH_DEFAULT, "loc_33C0"),
    )


    label("loc_32B9")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(3500)
    OP_1D(0xD2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #91
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_3355")

    label("loc_3355")

    Jump("loc_33CD")

    label("loc_3358")

    OP_5F(0x1)
    OP_56(0x0)
    OP_A9(0xA)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #92
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_3389")

    label("loc_3389")

    Jump("loc_33CD")

    label("loc_338C")

    OP_5F(0x1)
    OP_56(0x0)
    OP_A9(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #93
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_33BD")

    label("loc_33BD")

    Jump("loc_33CD")

    label("loc_33C0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_33CD")

    label("loc_33CD")

    Jump("loc_324F")

    label("loc_33D0")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #94
        (
            "\x07\x05#2S#40W      解放吾等眷属……\x01",
            "#800W\x01",
            "#40W如是，则赐汝等愈强力量……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x10F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Fade(500)
    OP_6D(-850, 4000, 1770, 0)
    OP_67(0, 5680, -10000, 0)
    OP_6B(1990, 0)
    OP_6C(315000, 0)
    OP_6E(411, 0)
    SetChrPos(0x109, 800, 4000, 1030, 0)
    SetChrPos(0x10F, -540, 4000, 810, 0)
    OP_0D()
    Sleep(1000)
    OP_63(0x109)
    OP_63(0x10F)
    Sleep(300)
    OP_8C(0x10F, 90, 400)
    Sleep(300)

    ChrTalk(    #95
        0x10F,
        "#1443F#5P……刚才的是什么。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x109,
        (
            "#1068F#6P别问我……\x01",
            "我也是一头雾水。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    OP_8C(0x109, 270, 400)
    Sleep(500)

    ChrTalk(    #97
        0x109,
        (
            "#1840F#6P不过，\x01",
            "看来可以通过米拉和耀晶片\x01",
            "来调整我们的战斗力了……\x02\x03",

            "只有这一点可以肯定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x10F,
        (
            "#1446F#5P………………………………\x02\x03",

            "#1448F正好有刚才损坏的结晶回路\x01",
            "留下的这些碎片……\x02\x03",

            "用它们做些准备吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x109,
        (
            "#1060F#6P啊，来试试看吧。\x02\x03",

            "不管有多么厉害的战技，\x01",
            "回复魔法之类的也还是必不可少的。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_A2(0x2606)
    EventEnd(0x0)
    Return()

    # Function_21_289A end

    def Function_22_370F(): pass

    label("Function_22_370F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_374B")
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    Sleep(500)
    OP_8C(0xFE, 45, 400)
    Sleep(500)
    OP_8C(0xFE, 135, 400)
    Sleep(500)
    Jump("Function_22_370F")

    label("loc_374B")

    Return()

    # Function_22_370F end

    def Function_23_374C(): pass

    label("Function_23_374C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3788")
    OP_8C(0xFE, 315, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    Sleep(500)
    OP_8C(0xFE, 225, 400)
    Sleep(500)
    Jump("Function_23_374C")

    label("loc_3788")

    Return()

    # Function_23_374C end

    def Function_24_3789(): pass

    label("Function_24_3789")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -13400, 3000, -12820, 45)
    SetChrPos(0x10F, -15030, 2500, -12140, 45)
    OP_6D(-11560, 4100, -9130, 0)
    OP_67(0, 5270, -10000, 0)
    OP_6B(2110, 0)
    OP_6C(359000, 0)
    OP_6E(441, 0)

    def lambda_37FA():
        OP_8E(0xFE, 0xFFFFD602, 0x1004, 0xFFFFD828, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_37FA)

    def lambda_3815():
        OP_8E(0xFE, 0xFFFFCF9A, 0x1004, 0xFFFFD9E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_3815)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Call(1, 26)
    Return()

    # Function_24_3789 end

    def Function_25_387B(): pass

    label("Function_25_387B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 14310, 3000, -11130, 315)
    SetChrPos(0x10F, 13850, 2500, -13140, 315)
    OP_6D(12100, 4100, -8940, 0)
    OP_67(0, 5440, -10000, 0)
    OP_6B(2110, 0)
    OP_6C(0, 0)
    OP_6E(439, 0)

    def lambda_38EC():
        OP_8E(0xFE, 0x2FBC, 0x1004, 0xFFFFDC38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_38EC)

    def lambda_3907():
        OP_8E(0xFE, 0x2C24, 0x1004, 0xFFFFD620, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_3907)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_A2(0x0)
    Call(1, 26)
    Return()

    # Function_25_387B end

    def Function_26_3970(): pass

    label("Function_26_3970")


    def lambda_3976():
        OP_6D(0, 15020, 35890, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3976)

    def lambda_398E():
        OP_67(0, 4640, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_398E)

    def lambda_39A6():
        OP_6B(2600, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_39A6)

    def lambda_39B6():
        OP_6C(0, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_39B6)

    def lambda_39C6():
        OP_6E(446, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_39C6)

    def lambda_39D6():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_39D6)
    Sleep(100)
    OP_8C(0x10F, 0, 400)
    WaitChrThread(0x109, 0x1)
    SetChrPos(0x109, 750, 9190, 27370, 0)
    SetChrPos(0x10F, -750, 8870, 26740, 0)
    Sleep(500)
    Fade(1000)

    def lambda_3A21():
        OP_6B(2400, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3A21)
    OP_22(0x117, 0x0, 0x64)
    OP_71(0x400, 0x0)
    ExitThread()
    OP_0D()
    Sleep(1000)
    Sleep(500)

    ChrTalk(    #100
        0x10F,
        (
            "#1444F#5P那个法阵……\x01",
            "难道是出口……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x109,
        (
            "#1065F#5P从某种意义上来说，\x01",
            "也许是『入口』才对。\x02\x03",

            "#1063F刚才的石碑也好，\x01",
            "大树也好，还有泉水……\x02\x03",

            "都像是特地为了\x01",
            "让我们做好物质和\x01",
            "精神上的准备才设置的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x10F,
        "#1445F#5P……嗯………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3BBB")
    OP_6D(6920, 4000, 320, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(1760, 0)
    OP_6C(314000, 0)
    OP_6E(450, 0)
    SetChrPos(0x109, 8130, 4000, -450, 0)
    SetChrPos(0x10F, 6770, 4000, -450, 0)
    Jump("loc_3C1A")

    label("loc_3BBB")

    OP_6D(-6080, 4000, 80, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(1760, 0)
    OP_6C(314000, 0)
    OP_6E(450, 0)
    SetChrPos(0x109, -5140, 4000, -490, 0)
    SetChrPos(0x10F, -6670, 4000, -430, 0)

    label("loc_3C1A")

    OP_0D()
    OP_8C(0x10F, 90, 400)

    ChrTalk(    #103
        0x10F,
        (
            "#1443F#5P那么我们怎么办？\x02\x03",

            "要进到里面去吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 270, 400)
    Sleep(300)

    ChrTalk(    #104
        0x109,
        (
            "#1060F#6P是啊，反正我们\x01",
            "也没有其它的道路可以选。\x02\x03",

            "#1064F啊，\x01",
            "不过莉丝你还是留在这里──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x10F,
        "#1801F#5P……………………（瞪）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x109,
        (
            "#1068F#6P──本来是想这么说的，\x01",
            "不过还是两个人一起行动吧。\x02\x03",

            "#1066F也不知道会发生什么事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x10F,
        (
            "#1446F#5P……那是当然。\x02\x03",

            "#1440F对了，凯文。\x01",
            "把这个给你。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #108
        "\x07\x00得到了\x1F\x0A\x02\x07\x00。\x02",
    )

    Jump("loc_3DEF")

    label("loc_3DEF")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x20A, 1)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #109
        0x109,
        (
            "#1064F#6P哎……\x02\x03",

            "为、为什么你\x01",
            "会有这样的东西！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x10F,
        (
            "#1448F#5P是瑟尔纳特总长\x01",
            "拜托我交给你的。\x02\x03",

            "#1447F『最近，凯文的报告\x01",
            "  有些太笼统和应付了事了。』\x02\x03",

            "『反正他也不会好好做记录，\x01",
            "  你就把这东西给他吧』。\x01",
            "她是这么交代我的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x109,
        (
            "#1063F#6P哼……被发现了吗。\x02\x03",

            "#1079F话说回来，\x01",
            "为什么莉丝你会认识总长啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x10F,
        (
            "#1442F#5P……她是教我法剑的老师。\x02\x03",

            "我非常尊敬她。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x109,
        (
            "#1068F#6P我、我完全不知道……\x02\x03",

            "#1067F（倒不如说是总长……\x01",
            "  故意向我隐瞒了这件事……）\x02\x03",

            "（……没错……如果我知道的话，\x01",
            "  怎么可能会让她当骑士……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x10F,
        "#1444F#5P凯文……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x109,
        (
            "#1065F#6P……不，没什么。\x02\x03",

            "#1063F还不知进入那个法阵之后\x01",
            "会有什么样的东西等着我们。\x02\x03",

            "一定要小心行事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x10F,
        "#1448F#5P嗯……！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x260A)
    OP_28(0x28, 0x4, 0x4)
    OP_28(0x28, 0x4, 0x8)
    OP_28(0x28, 0x1, 0x1)
    OP_28(0x28, 0x1, 0x2)
    OP_28(0x28, 0x1, 0x4)
    OP_28(0x28, 0x1, 0x8)
    OP_64(0x1, 0x1)
    OP_10(0x3, 0x1)
    OP_1B(0x3, 0x0, 0x11)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_26_3970 end

    def Function_27_4170(): pass

    label("Function_27_4170")

    EventBegin(0x0)
    Fade(500)
    SetChrPos(0x109, 770, 11920, 40820, 0)
    SetChrPos(0x10F, -500, 11920, 40650, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_6D(-530, 11920, 41530, 0)
    OP_67(0, 6540, -10000, 0)
    OP_6B(2290, 0)
    OP_6C(314000, 0)
    OP_6E(410, 0)
    OP_0D()
    Sleep(500)

    def lambda_41F6():
        OP_6B(2500, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_41F6)
    LoadEffect(0x0, "map\\mp204_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -30, 11920, 40820, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 19)
    FadeToDark(2000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/M7001   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_27_4170 end

    def Function_28_426D(): pass

    label("Function_28_426D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D2(0x260285, 0x26028A, 0x13)
    OP_D2(0x270448, 0x27044C, 0x14)
    LoadEffect(0x0, "map\\mp252_04.eff")
    LoadEffect(0x1, "map\\mp253_00.eff")
    LoadEffect(0x2, "map\\mp253_01.eff")
    LoadEffect(0x3, "map\\mp253_02.eff")
    LoadEffect(0x4, "map\\mp253_03.eff")
    LoadEffect(0x5, "map\\mp253_05.eff")
    LoadEffect(0x6, "map\\mp253_04.eff")
    SetChrPos(0x109, -160, 4000, -1160, 180)
    SetChrPos(0x10F, 1590, 4000, -1260, 180)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x10F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(2330, 12590, 1650, 0)
    OP_67(0, 6700, -10000, 0)
    OP_6B(2250, 0)
    OP_6C(314000, 0)
    OP_6E(461, 0)

    def lambda_438D():
        OP_6D(2330, 6290, 1650, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_438D)

    def lambda_43A5():
        OP_67(0, 4880, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_43A5)

    def lambda_43BD():
        OP_6B(2250, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_43BD)

    def lambda_43CD():
        OP_6C(315000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_43CD)

    def lambda_43DD():
        OP_6E(461, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_43DD)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Fade(500)
    OP_6D(-530, 4000, -50, 0)
    OP_67(0, 5950, -10000, 0)
    OP_6B(2150, 0)
    OP_6C(315000, 0)
    OP_6E(399, 0)
    OP_0D()
    PlayEffect(0x0, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x162, 0x0, 0x64)
    Sleep(2000)

    def lambda_44B3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_44B3)

    def lambda_44C5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_44C5)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    OP_83(0x0, 0x2)
    OP_83(0x1, 0x2)
    Sleep(500)

    ChrTalk(    #117
        0x10F,
        "#1444F#5P啊……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)
    Sleep(300)

    ChrTalk(    #118
        0x109,
        (
            "#1060F#5P好，进行得很顺利。\x02\x03",

            "这样一来，一旦遇到什么危险\x01",
            "就可以随时回到这里来。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 270, 400)
    Sleep(300)

    ChrTalk(    #119
        0x10F,
        (
            "#1447F#6P嗯……非常方便呢。\x02\x03",

            "#1448F不过说老实话，\x01",
            "我对那个『方石』还是不太信任。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x109,
        (
            "#1075F#5P跟之前一样，\x01",
            "使用的时候注意一下就行了。\x02\x03",

            "#1060F好了……接下来是这个吗。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x109, 19)
    SetChrSubChip(0x109, 0)
    ClearChrFlags(0x10, 0x80)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10, 400, 5330, -1380, 0)
    PlayEffect(0x1, 0x0, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #121
        0x10F,
        (
            "#1443F#6P『封印石』……\x02\x03",

            "那个声音好像是说\x01",
            "只要把它放在石碑前面\x01",
            "就可以得到解放……\x02\x03",

            "到底是解放什么呢？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #122
        0x109,
        (
            "#1065F#5P这个只有试过了\x01",
            "才会知道啊。\x02\x03",

            "#1063F我来把它举到石碑前面，\x01",
            "为保险起见你就在一边做好警戒吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x10F,
        "#1443F#6P……明白。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10F, 0, 400)
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 20)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(500)
    OP_8C(0x109, 0, 400)

    def lambda_485D():
        OP_6D(-1180, 4000, 2780, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_485D)

    def lambda_4875():
        OP_67(0, 5490, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_4875)

    def lambda_488D():
        OP_6B(2210, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_488D)

    def lambda_489D():
        OP_6E(403, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_489D)
    OP_8F(0x109, 0x0, 0xFA0, 0xFFFFFE16, 0x3E8, 0x0)
    WaitChrThread(0x10F, 0x0)
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x109, 19)
    SetChrSubChip(0x109, 0)
    OP_22(0x8F, 0x0, 0x64)
    Sleep(100)
    SetChrPos(0x10, 200, 5300, 0, 0)
    PlayEffect(0x1, 0x0, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(500)
    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    OP_E5(0x2, 0xFF, 0x13, 1000)
    OP_0D()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #124
        0x10F,
        "#1444F#6P有反应了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x109,
        (
            "#1060F#6P那么……\x01",
            "看看会是谁出来呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_E5(0x2, 0xFF, 0x13, 700)
    OP_0D()

    def lambda_4A16():
        OP_8F(0xFE, 0xC8, 0x1770, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_4A16)
    WaitChrThread(0x10, 0x0)
    Sleep(500)
    Fade(1000)
    OP_6D(0, 5000, 3260, 0)
    OP_67(0, 3980, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(0, 0)
    OP_6E(363, 0)
    SetChrPos(0x109, 0, 5000, -500, 0)
    SetChrPos(0x10F, 790, 4000, -2800, 0)
    SetChrPos(0x10, 0, 6000, 1000, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)

    def lambda_4ABA():
        OP_6D(0, 7500, 3760, 3500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4ABA)

    def lambda_4AD2():
        OP_67(0, 1650, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4AD2)

    def lambda_4AEA():
        OP_6B(2700, 3500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4AEA)

    def lambda_4AFA():
        OP_6E(363, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_4AFA)

    def lambda_4B0A():
        OP_8F(0xFE, 0x0, 0x2134, 0xAF0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_4B0A)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    def lambda_4B34():
        OP_6B(2000, 8000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4B34)
    OP_22(0x147, 0x0, 0x64)
    PlayEffect(0x5, 0x2, 0x10, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    OP_23(0x147)
    Fade(500)
    OP_22(0xC, 0x0, 0x64)
    PlayEffect(0x3, 0x2, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x0)
    Sleep(300)
    PlayEffect(0x6, 0x3, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7001   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_28_426D end

    def Function_29_4C20(): pass

    label("Function_29_4C20")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 0, 4000, -490, 0)
    SetChrPos(0x10F, 1590, 4000, -1260, 0)
    SetChrChipByIndex(0x10F, 20)
    SetChrSubChip(0x10F, 0)
    OP_D2(0x70064, 0x7006C, 0x13)
    OP_D2(0x270448, 0x27044C, 0x14)
    OP_D2(0x26028F, 0x260294, 0x15)
    LoadEffect(0x3, "map\\mp253_04.eff")
    LoadEffect(0x4, "map\\mp253_03.eff")
    OP_6D(-2230, 5000, 4310, 0)
    OP_67(0, 3880, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(315000, 0)
    OP_6E(365, 0)
    ClearChrFlags(0x11, 0x80)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x11, 390, 8000, 2150, 180)
    SetChrChipByIndex(0x11, 21)
    SetChrSubChip(0x11, 0)
    SetChrFlags(0x11, 0x4)
    PlayEffect(0x3, 0x0, 0x11, 0, 400, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    OP_E5(0x2, 0xFF, 0x13, 500)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_4D5B():
        OP_6D(-600, 4000, 1980, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4D5B)

    def lambda_4D73():
        OP_67(0, 5590, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4D73)

    def lambda_4D8B():
        OP_6B(2470, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4D8B)

    def lambda_4D9B():
        OP_6E(327, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_4D9B)

    def lambda_4DAB():
        OP_8F(0xFE, 0x186, 0xFA0, 0x866, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_4DAB)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    Fade(1000)
    OP_82(0x2, 0x2)
    PlayEffect(0x3, 0x1, 0x11, 0, 400, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)

    def lambda_4E12():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x7D0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_4E12)
    OP_22(0x99, 0x0, 0x64)
    OP_82(0x0, 0x0)
    OP_0D()
    Sleep(1000)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #126
        0x109,
        "#1069F#6P什么……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x10F,
        "#1444F#6P……女孩子……？\x02",
    )

    CloseMessageWindow()
    PlayEffect(0x4, 0x4, 0x11, 0, 400, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_22(0x138, 0x0, 0x64)
    OP_23(0x146)

    def lambda_4EEF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_4EEF)
    WaitChrThread(0x11, 0x0)
    Fade(500)
    OP_82(0x1, 0x0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #128
        0x11,
        (
            "#562F#5P呜、呜呜～……\x02\x03",

            "……刚、刚才的光是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x109,
        "#1064F#6P……………………（说不出话）\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #130
        0x10F,
        "#1444F#6P这孩子，是照片上的……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x11, 21)
    SetChrSubChip(0x11, 1)
    OP_0D()
    Sleep(300)

    ChrTalk(    #131
        0x11,
        "#063F#5P咦……？\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(500)
    SetChrChipByIndex(0x11, 3)
    SetChrSubChip(0x11, 0)
    OP_0D()
    Sleep(500)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #132
        0x11,
        (
            "#064F#11P凯、凯文大哥哥……？\x02\x03",

            "咦、咦？\x01",
            "是凯文大哥哥吧？\x02\x03",

            "为什么在这里……\x02",
        )
    )

    Jump("loc_50AA")

    label("loc_50AA")

    CloseMessageWindow()

    ChrTalk(    #133
        0x109,
        (
            "#1068F#6P啊～……\x02\x03",

            "#1066F哈哈，很久不见了，\x01",
            "小提妲。\x02\x03",

            "应该有半年了吧？\x01",
            "你好像长高了一些嘛。\x02",
        )
    )

    Jump("loc_512C")

    label("loc_512C")

    CloseMessageWindow()

    ChrTalk(    #134
        0x11,
        (
            "#067F#11P啊……\x01",
            "嘿嘿，谢谢。\x02\x03",

            "#560F对了对了，好久不见。\x01",
            "你又是到利贝尔\x01",
            "来玩的吗？\x02\x03",

            "#064F咦，那边的大姐姐是……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x11)
    OP_8C(0x11, 270, 400)
    Sleep(500)
    OP_8C(0x11, 90, 400)
    Sleep(500)
    OP_62(0x11, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #135
        0x11,
        (
            "#064F#5P咦……\x02\x03",

            "我应该是和爸爸一起\x01",
            "留在家里看门才对……\x02\x03",

            "因为阿加特大哥哥会来，\x01",
            "我正在准备晚饭，\x01",
            "突然眼前就变得一片白……\x02\x03",

            "然后……\x02",
        )
    )

    Jump("loc_52B4")

    label("loc_52B4")

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_43(0x11, 0x0, 0x1, 0x1E)

    ChrTalk(    #136
        0x11,
        (
            "#065F#5P哇哇！？\x01",
            "这、这里到底是！？\x02\x03",

            "是、是梦！？\x01",
            "这是我在做梦吗！？\x02\x03",

            "对、对了！\x01",
            "用力捏脸试试看！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #137
        0x109,
        (
            "#1840F#6P哈哈……\x01",
            "这肯定是本人没错了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x10F,
        "#1442F#6P（………真可爱……………）\x02",
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_44(0x11, 0x0)
    OP_D2(0x260286, 0x26028B, 0x13)
    SetChrPos(0x11, 390, 4000, 1500, 180)
    OP_8C(0x109, 0, 0)
    OP_8C(0x10F, 0, 0)
    OP_8C(0x11, 180, 0)
    ClearChrFlags(0x11, 0x4)
    SetChrSubChip(0x11, 0)
    SetChrChipByIndex(0x109, 19)
    SetChrSubChip(0x109, 0)
    SetChrFlags(0x109, 0x20)
    OP_6D(-600, 4000, 1800, 0)
    OP_67(0, 5350, -10000, 0)
    OP_6B(2450, 0)
    OP_6C(315000, 0)
    OP_6E(327, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #139
        0x11,
        (
            "#063F#11P是、是这样啊……\x02\x03",

            "是因为妈妈他们\x01",
            "打捞上来的那个古代遗物在作怪吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x109,
        (
            "#1065F#6P不……\x01",
            "老实说，那个是不是原因，\x01",
            "现在还无法下定论。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(300)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    ClearChrFlags(0x109, 0x20)
    OP_0D()
    Sleep(500)

    ChrTalk(    #141
        0x109,
        (
            "#1063F#6P而且，就算那是原因，\x01",
            "也想不到有什么理由\x01",
            "会把在蔡斯的提妲也卷进来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x11,
        (
            "#065F#11P的、的确……\x02\x03",

            "蔡斯和格兰赛尔\x01",
            "之间的距离很远……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x10F,
        (
            "#1446F#6P不过，被白光包围的时间\x01",
            "基本上是相同的。\x02\x03",

            "#1440F看来之间有什么关联性\x01",
            "是必然的了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x11,
        (
            "#063F#11P是、是的。\x01",
            "我也是这么想的。\x02\x03",

            "#064F啊……\x01",
            "对、对不起！\x01",
            "我还没有打招呼……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #145
        0x11,
        (
            "#560F#11P那个那个，\x01",
            "我是蔡斯中央工房的实习生，\x01",
            "名叫提妲·拉赛尔！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x10F,
        (
            "#1448F#6P我是七耀教会的修女，\x01",
            "莉丝·亚尔珍特。\x02\x03",

            "我已经从你母亲和凯文那里\x01",
            "知道了不少你的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x11,
        (
            "#064F#11P啊，莉丝姐姐\x01",
            "也和我妈妈见过面吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x10F,
        (
            "#1447F#6P嗯……\x01",
            "还让我看了照片。\x02\x03",

            "#1442F现在见到真人，\x01",
            "就理解你母亲为什么会那么自豪了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x11,
        (
            "#562F#11P唉、唉……\x01",
            "……妈妈真是的……\x02\x03",

            "#063F对了对了，\x01",
            "妈妈有没有对莉丝姐姐\x01",
            "做出什么失礼的举动呢？\x02\x03",

            "像莉丝姐姐这么可爱的人，\x01",
            "我妈妈最喜欢了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x10F,
        "#1444F#6P咦……\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #151
        0x11,
        (
            "#560F#11P对、对不起！\x01",
            "明明是姐姐，却说什么可爱……！\x02\x03",

            "#067F不过不过，该怎么说呢，\x01",
            "虽然姐姐的外表文静端庄，\x01",
            "但有一种独特的气质……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x10F,
        "#1802F#6P…………独特……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x109,
        (
            "#1061F#6P哈哈，你们母子感觉都很敏锐嘛。\x02\x03",

            "#1062F没错，说到独特，\x01",
            "没有比莉丝更适合这个词的了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x10F,
        "#1801F#6P哼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x11,
        (
            "#067F#11P那个那个……\x02\x03",

            "#560F凯文大哥哥，\x01",
            "你们接下来要怎么办呢？\x02\x03",

            "果然还是打算继续\x01",
            "寻找逃脱方法吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x109,
        (
            "#1060F#6P啊，的确是这么打算的。\x02\x03",

            "#1068F不过话说回来，\x01",
            "探索才刚刚开始，\x01",
            "基本上没什么进展呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x11,
        (
            "#060F#11P是这样啊……\x02\x03",

            "#560F……对了对了！\x01",
            "这样的话，\x01",
            "我也来帮忙吧！\x02\x03",

            "我会努力\x01",
            "不给你们添麻烦的！\x02",
        )
    )

    Jump("loc_5BC4")

    label("loc_5BC4")

    CloseMessageWindow()

    ChrTalk(    #158
        0x10F,
        "#1444F#6P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x109,
        (
            "#1065F#6P嗯，也好。\x02\x03",

            "#1840F虽然说老实话，\x01",
            "我希望提妲能够留在这里等着。\x02\x03",

            "刚才我也说了，\x01",
            "这个空间并不是用\x01",
            "我们的常理能够解释的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x11,
        (
            "#062F#11P但是但是，\x01",
            "这么说的话呆在这里也是一样的……\x02\x03",

            "如果有我能做的事情，\x01",
            "我还是希望能够帮上忙！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x109,
        (
            "#1075F#6P是吗……\x02\x03",

            "#1066F哈哈，\x01",
            "不愧是艾丝蒂尔的妹妹啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x11,
        "#067F#11P嘿嘿。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10F, 315, 400)
    Sleep(300)

    ChrTalk(    #163
        0x10F,
        "#1443F#6P凯文……你是说真的吗？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)
    Sleep(300)

    ChrTalk(    #164
        0x109,
        (
            "#1060F#5P用不着为这个孩子\x01",
            "做多余的担心。\x02\x03",

            "别看她这么小，在那次事件中\x01",
            "可是一直跟到了最后的战场。\x02\x03",

            "她比外表看起来要坚强很多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x10F,
        "#1802F#6P就算这样说……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x11,
        (
            "#063F#11P那个那个……\x01",
            "拜托你们了！\x02\x03",

            "我会注意安全，\x01",
            "不让你们两个担心的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x10F,
        "#1444F#6P…………………………………\x02",
    )

    CloseMessageWindow()

    def lambda_5EEA():
        OP_8C(0x10F, 0, 400)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_5EEA)
    Sleep(200)
    OP_8C(0x109, 0, 400)
    Sleep(300)

    ChrTalk(    #168
        0x10F,
        (
            "#1448F#6P……我明白了。\x01",
            "那就请彼此多多关照了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #169
        0x11,
        "#064F#11P是、是真的吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x10F,
        (
            "#1447F#6P看来你很明白\x01",
            "为别人担心\x01",
            "是怎样一回事。\x02\x03",

            "那么我也不会\x01",
            "再表示反对了。\x02\x03",

            "#1442F……不过，\x01",
            "请你一定要注意安全。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x11,
        "#560F#11P是、是的！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x109,
        (
            "#1068F#6P关于这一点，\x01",
            "我也要拜托你啦。\x02\x03",

            "如果小提妲有什么万一的话，\x01",
            "我一定会被\x01",
            "艾莉卡博士勒死的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #173
        0x11,
        (
            "#065F#11P是、是的！\x01",
            "我会记住的！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)
    Sleep(300)

    ChrTalk(    #174
        0x109,
        (
            "#1060F#5P好，我们重装上阵吧。\x02\x03",

            "整理好提妲的装备之后，\x01",
            "就赶快继续探索吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 315, 400)
    Sleep(300)

    ChrTalk(    #175
        0x10F,
        "#1448F#6P……明白。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x11,
        "#560F#11P是！\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_61A4():
        OP_6B(2770, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_61A4)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_A2(0x260D)
    OP_28(0x29, 0x4, 0x4)
    OP_28(0x29, 0x4, 0x8)
    OP_28(0x29, 0x1, 0x1)
    OP_28(0x29, 0x1, 0x2)
    OP_3F(0x352, 1)
    OP_DB(0x0, 0x6)
    OP_DC(0x1, 0x0, 0x6)
    AddParty(0x6, 0xF0, 0xFF)
    OP_A2(0x25CC)
    Call(6, 16)
    SetChrFlags(0x11, 0x80)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_6D(630, 4000, -1100, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(450, 0)
    SetChrPos(0x109, 630, 4000, -1100, 180)
    SetChrPos(0x10F, 630, 4000, -1100, 180)
    SetChrPos(0x107, 630, 4000, -1100, 180)
    SetChrChipByIndex(0x109, 65535)
    SetChrChipByIndex(0x10F, 65535)
    SetChrChipByIndex(0x107, 65535)
    SetChrSubChip(0x109, 0)
    SetChrSubChip(0x10F, 0)
    SetChrSubChip(0x107, 0)
    OP_69(0x0, 0x0)
    OP_E5(0x2, 0xFF, 0x13, 700)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_29_4C20 end

    def Function_30_62C2(): pass

    label("Function_30_62C2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_633A")
    OP_62(0x11, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x11, 270, 600)
    Sleep(300)
    OP_8C(0x11, 90, 600)
    Sleep(500)
    OP_8C(0x11, 180, 600)
    Sleep(300)
    OP_8C(0x11, 225, 600)
    OP_62(0x11, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    OP_8C(0x11, 135, 600)
    Sleep(300)
    OP_8C(0x11, 0, 600)
    Sleep(500)
    Jump("Function_30_62C2")

    label("loc_633A")

    Return()

    # Function_30_62C2 end

    def Function_31_633B(): pass

    label("Function_31_633B")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D2(0x260285, 0x26028A, 0x13)
    LoadEffect(0x1, "map\\mp253_00.eff")
    LoadEffect(0x2, "map\\mp253_01.eff")
    LoadEffect(0x3, "map\\mp253_02.eff")
    LoadEffect(0x4, "map\\mp253_03.eff")
    LoadEffect(0x5, "map\\mp253_05.eff")
    LoadEffect(0x6, "map\\mp253_04.eff")
    SetChrPos(0x109, 0, 4000, -1770, 0)
    SetChrPos(0x10F, -560, 4000, -3010, 0)
    SetChrPos(0x107, 1110, 4000, -3200, 0)
    OP_6D(-950, 4000, -980, 0)
    OP_67(0, 5890, -10000, 0)
    OP_6B(1990, 0)
    OP_6C(314000, 0)
    OP_6E(388, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_6444():
        OP_6D(-1180, 4000, 2780, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_6444)

    def lambda_645C():
        OP_67(0, 5490, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_645C)

    def lambda_6474():
        OP_6B(2210, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_6474)

    def lambda_6484():
        OP_6E(403, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_6484)
    OP_8F(0x109, 0x0, 0xFA0, 0xFFFFFE16, 0x3E8, 0x0)
    WaitChrThread(0x10F, 0x0)
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x109, 19)
    SetChrSubChip(0x109, 0)
    OP_22(0x8F, 0x0, 0x64)
    Sleep(100)
    SetChrPos(0x10, 200, 5300, 0, 0)
    PlayEffect(0x1, 0x0, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)
    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    OP_E5(0x2, 0xFF, 0x13, 1000)
    OP_0D()
    Fade(1000)
    OP_E5(0x2, 0xFF, 0x13, 700)
    OP_0D()
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_6589():
        OP_8F(0xFE, 0xC8, 0x1770, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_6589)
    WaitChrThread(0x10, 0x0)
    Sleep(500)

    ChrTalk(    #177
        0x107,
        (
            "#560F#5P哇啊……！\x02\x03",

            "果、果然会有\x01",
            "什么人出现吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_65F1():
        OP_6D(-1040, 4000, -40, 1200)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_65F1)
    OP_8C(0x10F, 90, 400)
    WaitChrThread(0x10F, 0x0)

    ChrTalk(    #178
        0x10F,
        (
            "#1448F#5P这个可能性很高。\x02\x03",

            "#1447F……也许，\x01",
            "会出现另一个\x01",
            "提妲也说不定呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    OP_8C(0x107, 270, 400)

    ChrTalk(    #179
        0x107,
        "#065F#6P哎、哎～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x109,
        (
            "#1068F#5P我说……\x01",
            "如果真的变成那样了\x01",
            "该怎么办啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x10F,
        (
            "#1447F#5P……没关系。\x01",
            "让我带走就可以了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x107, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #182
        0x107,
        "#067F#6P啊、啊哈……\x02",
    )

    CloseMessageWindow()

    def lambda_677D():
        OP_8C(0x10F, 0, 400)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_677D)
    Sleep(100)
    OP_8C(0x107, 0, 400)
    Fade(1000)
    OP_6D(0, 5000, 3260, 0)
    OP_67(0, 3980, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(0, 0)
    OP_6E(363, 0)
    SetChrPos(0x109, 0, 4000, -500, 0)
    SetChrPos(0x10F, -700, 4000, -3010, 0)
    SetChrPos(0x107, 900, 4000, -3200, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrPos(0x10, 0, 6000, 1000, 0)

    def lambda_6827():
        OP_6D(0, 7500, 3760, 3500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6827)

    def lambda_683F():
        OP_67(0, 1650, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_683F)

    def lambda_6857():
        OP_6B(2700, 3500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6857)

    def lambda_6867():
        OP_6E(363, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_6867)

    def lambda_6877():
        OP_8F(0xFE, 0x0, 0x2134, 0xAF0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_6877)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    def lambda_68A1():
        OP_6B(2000, 8000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_68A1)
    OP_22(0x147, 0x0, 0x64)
    PlayEffect(0x5, 0x2, 0x10, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    OP_23(0x147)
    Fade(500)
    OP_22(0xC, 0x0, 0x64)
    PlayEffect(0x3, 0x2, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x0)
    Sleep(300)
    PlayEffect(0x6, 0x3, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7002   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_31_633B end

    def Function_32_698D(): pass

    label("Function_32_698D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 560, 4000, -1440, 0)
    SetChrPos(0x10F, -120, 4000, -2690, 0)
    SetChrPos(0x107, 1630, 4000, -3030, 0)
    OP_D2(0x260287, 0x26028C, 0x13)
    OP_D2(0x270021, 0x270024, 0x14)
    LoadEffect(0x3, "map\\mp253_04.eff")
    LoadEffect(0x4, "map\\mp253_03.eff")
    OP_6D(-2230, 5000, 4310, 0)
    OP_67(0, 3880, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(315000, 0)
    OP_6E(365, 0)
    ClearChrFlags(0x12, 0x80)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x12, 390, 8000, 2150, 180)
    SetChrChipByIndex(0x12, 19)
    SetChrSubChip(0x12, 0)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x800)
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x3, 0x0, 0x12, 0, 600, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    OP_E5(0x2, 0xFF, 0x13, 500)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_6AD5():
        OP_6D(-1210, 4000, 1510, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6AD5)

    def lambda_6AED():
        OP_67(0, 4850, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6AED)

    def lambda_6B05():
        OP_6B(2850, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6B05)

    def lambda_6B15():
        OP_6E(327, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_6B15)

    def lambda_6B25():
        OP_8F(0xFE, 0x186, 0xFA0, 0x866, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_6B25)
    WaitChrThread(0x12, 0x0)
    SetChrSubChip(0x12, 0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    Fade(1000)
    OP_82(0x2, 0x2)
    PlayEffect(0x3, 0x1, 0x12, 0, 600, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)

    def lambda_6B91():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x7D0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_6B91)
    OP_22(0x99, 0x0, 0x64)
    OP_82(0x0, 0x0)
    OP_0D()
    Sleep(1000)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #183
        0x10F,
        "#1444F#6P……军服……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x107,
        "#064F#6P那、那是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x109,
        (
            "#1065F#5P果然……\x02\x03",

            "#1840F看到埃尔赛尤的时候\x01",
            "我就已经想到了……\x02",
        )
    )

    CloseMessageWindow()
    PlayEffect(0x4, 0x4, 0x12, 0, 600, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_22(0x138, 0x0, 0x64)
    OP_23(0x146)

    def lambda_6CD9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_6CD9)
    OP_82(0x2, 0x2)
    WaitChrThread(0x12, 0x0)
    Fade(500)
    OP_82(0x1, 0x0)
    OP_0D()
    Sleep(300)

    NpcTalk(    #186
        0x12,
        "尤莉亚上尉",
        "#175F#5P……唔………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xBC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x12, 20)
    SetChrSubChip(0x12, 0)
    OP_0D()
    Sleep(300)

    NpcTalk(    #187
        0x12,
        "尤莉亚上尉",
        (
            "#177F#11P艾柯！\x01",
            "到底发生什么事了！？\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x12, 0xFFFFFED4, 1400, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x12)

    NpcTalk(    #188
        0x12,
        "尤莉亚上尉",
        "#173F#11P…………哎。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x107,
        "#560F#6P那、那个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x109,
        (
            "#1066F#6P总之……\x01",
            "尤莉亚小姐，好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #191
        0x12,
        "尤莉亚上尉",
        (
            "#173F#11P凯文神父……\x01",
            "……还有提妲……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x12, 0x800)
    SetChrChipByIndex(0x12, 4)
    SetChrSubChip(0x12, 0)
    OP_0D()
    Sleep(300)
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_8C(0x12, 90, 400)
    Sleep(500)
    OP_8C(0x12, 270, 400)
    Sleep(500)
    OP_8C(0x12, 0, 400)
    Sleep(1000)
    OP_63(0x12)
    Sleep(500)

    NpcTalk(    #192
        0x12,
        "尤莉亚上尉",
        (
            "#176F#5P在打招呼之前\x01",
            "希望你们能告诉我一件事。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x12, 180, 400)
    Sleep(500)

    NpcTalk(    #193
        0x12,
        "尤莉亚上尉",
        (
            "#178F#11P──这是梦吗？\x01",
            "还是我产生了幻觉？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrPos(0x109, 270, 4000, -2029, 0)
    SetChrPos(0x10F, -670, 4000, -2950, 0)
    SetChrPos(0x107, 1130, 4000, -3670, 0)
    SetChrPos(0x12, 290, 4000, -190, 180)
    ClearChrFlags(0x12, 0x4)
    OP_6D(-1420, 4000, -120, 0)
    OP_67(0, 5400, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(315000, 0)
    OP_6E(381, 0)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #194
        0x12,
        "尤莉亚上尉",
        (
            "#176F#11P原来如此……\x02\x03",

            "#175F虽然这很难以置信，\x01",
            "但我也不得不接受了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x109,
        (
            "#1065F#6P你能理解真是太好了。\x02\x03",

            "#1063F那么，尤莉亚小姐\x01",
            "记不记得发生过什么事？\x02\x03",

            "应该也是昨天晚上\x01",
            "被白光卷入进来的吧？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #196
        0x12,
        "尤莉亚上尉",
        (
            "#176F#11P昨天晚上吗……\x01",
            "我怎么感觉是\x01",
            "刚刚发生的事情呢……\x02\x03",

            "#178F当时我正是在\x01",
            "结束了飞行演习，\x01",
            "往雷斯顿要塞的返航途中。\x02\x03",

            "我刚在栈桥的座位上坐下，\x01",
            "突然眼前就变得一片白……\x02\x03",

            "#175F……好像记忆就\x01",
            "到这里为止了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x109,
        (
            "#1065F#6P原来如此……\x01",
            "事情经过我已经大致了解了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x10F,
        (
            "#1445F#6P从时间上来说，\x01",
            "果然是和我们一致的……\x02\x03",

            "#1443F其他乘员的下落\x01",
            "你知道吗？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #199
        0x12,
        "尤莉亚上尉",
        (
            "#175F#11P不……\x01",
            "我一点头绪也没有。\x02\x03",

            "如果只有我被卷入进来的话，\x01",
            "还可以暂时安心……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x107,
        (
            "#063F#6P不过既然我们发现了埃尔赛尤，\x01",
            "那么其他乘员也应该在这里……\x02\x03",

            "……应该是这样吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x109,
        (
            "#1063F#5P嗯……\x01",
            "现在还不能下定论。\x02\x03",

            "#1065F至少在船舱内\x01",
            "没有发现任何一个人，\x02\x03",

            "只有尤莉亚小姐的封印石。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #202
        0x12,
        "尤莉亚上尉",
        (
            "#175F#11P………………………………\x02\x03",

            "#176F凯文神父。\x01",
            "还有莉丝修女。\x02\x03",

            "#178F你们已经开始\x01",
            "对这个地方进行探索了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x109,
        "#1060F#6P嗯，算是吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x10F,
        (
            "#1440F#6P……只是刚开始探索，\x01",
            "并没有什么进展。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #205
        0x12,
        "尤莉亚上尉",
        (
            "#178F#11P那么……\x01",
            "请务必让我也尽一份力量。\x02\x03",

            "我担心部下们的安危，\x01",
            "并且还想确认一下\x01",
            "埃尔赛尤号无法发动的原因。\x02\x03",

            "所以，\x01",
            "我想协助你们的探索行动\x01",
            "应该是最好的选择。\x02",
        )
    )

    Jump("loc_75B7")

    label("loc_75B7")

    CloseMessageWindow()

    ChrTalk(    #206
        0x107,
        "#560F#6P哇啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x109,
        (
            "#1078F#6P说实话，真是求之不得。\x02\x03",

            "王国军青年一代首屈一指的剑技，\x01",
            "让我们好好开开眼界吧。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #208
        0x12,
        "尤莉亚上尉",
        (
            "#179F#11P哈哈……\x01",
            "我的剑技还差的远呢。\x02\x03",

            "#170F莉丝修女，\x01",
            "还有提妲。\x02\x03",

            "本人不才，\x01",
            "还请你们多多关照。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x10F,
        "#1448F#6P……彼此彼此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x107,
        "#560F#6P请、请多关照！\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_771A():
        OP_6B(2800, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_771A)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_A2(0x261A)
    OP_28(0x2A, 0x4, 0x4)
    OP_28(0x2A, 0x4, 0x8)
    OP_28(0x2A, 0x1, 0x1)
    OP_28(0x2A, 0x1, 0x2)
    OP_3F(0x353, 1)
    OP_DB(0x0, 0xD)
    OP_DC(0x1, 0x0, 0xD)
    AddParty(0xD, 0xF1, 0xFF)
    OP_A2(0x25D4)
    Call(6, 22)
    SetChrFlags(0x12, 0x80)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_6D(390, 4000, -1290, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(450, 0)
    SetChrPos(0x109, 390, 4000, -1290, 180)
    SetChrPos(0x10F, 390, 4000, -1290, 180)
    SetChrPos(0x107, 390, 4000, -1290, 180)
    SetChrPos(0x10E, 390, 4000, -1290, 180)
    SetChrChipByIndex(0x109, 65535)
    SetChrChipByIndex(0x10F, 65535)
    SetChrChipByIndex(0x107, 65535)
    SetChrChipByIndex(0x10E, 65535)
    SetChrSubChip(0x109, 0)
    SetChrSubChip(0x10F, 0)
    SetChrSubChip(0x107, 0)
    SetChrSubChip(0x10E, 0)
    OP_69(0x0, 0x0)
    OP_E5(0x2, 0xFF, 0x13, 700)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_32_698D end

    def Function_33_7853(): pass

    label("Function_33_7853")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(1000)
    OP_1D(0xB2)
    Sleep(1500)
    SetMessageWindowPos(350, 100, -1, -1)
    SetChrName("小女孩的声音")

    AnonymousTalk(    #211
        (
            "\x07\x0C#30W……姐姐……\x02\x03",

            "姐姐……\x01",
            "……来一下……\x02",
        )
    )

    Jump("loc_78CA")

    label("loc_78CA")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 200, -1, -1)
    SetChrName("女孩的声音")

    AnonymousTalk(    #212
        (
            "\x07\x0C#30W真是的，莉丝……\x01",
            "你跑到哪儿去了？\x02\x03",

            "我一买完东西\x01",
            "就发现你不在店里……\x02\x03",

            "让我好担心啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 100, -1, -1)
    SetChrName("小女孩的声音")

    AnonymousTalk(    #213
        (
            "\x07\x0C#30W……因为对面的摊子\x01",
            "散发出来的香味太吸引人了嘛。\x02\x03",

            "对了……\x01",
            "我发现了个奇怪的人。\x02",
        )
    )

    Jump("loc_79DF")

    label("loc_79DF")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 200, -1, -1)
    SetChrName("女孩的声音")

    AnonymousTalk(    #214
        "\x07\x0C#30W奇怪的……？\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    OP_AD(0x240106, 0x0, 0x0, 0x64)
    Sleep(3000)
    SetMessageWindowPos(80, 220, -1, -1)
    SetChrName("女孩")

    AnonymousTalk(    #215
        "\x07\x0C#30W……啊………\x02",
    )

    Jump("loc_7A5E")

    label("loc_7A5E")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(250, 260, -1, -1)
    SetChrName("小女孩")

    AnonymousTalk(    #216
        (
            "\x07\x0C#30W……饿昏路旁了？\x02\x03",

            "还是吃撑了？\x02",
        )
    )

    Jump("loc_7AB0")

    label("loc_7AB0")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 220, -1, -1)
    SetChrName("女孩")

    AnonymousTalk(    #217
        (
            "\x07\x0C#30W大概，应该不是\x01",
            "吃撑了……\x02\x03",

            "话说回来，\x01",
            "你竟然知道这样的词啊。\x02\x03",

            "……哦，对了。\x02",
        )
    )

    Jump("loc_7B32")

    label("loc_7B32")

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0xC8)
    Sleep(2000)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS407._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS408._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS409._CH")
    OP_C5(0x3, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS410._CH")
    OP_C5(0x4, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS411._CH")
    OP_C5(0x5, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS412._CH")
    OP_C6(0x0, 0x3, -1, 2000, 0)
    Sleep(3000)
    SetMessageWindowPos(150, 330, -1, -1)
    SetChrName("女孩")

    AnonymousTalk(    #218
        (
            "\x07\x0C#30W……喂，我说你。\x02\x03",

            "能听见……我们的声音吗？\x02",
        )
    )

    Jump("loc_7CB1")

    label("loc_7CB1")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x3, -1, 400, 0)
    Sleep(800)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(400, 400, -1, -1)
    SetChrName("少年")

    AnonymousTalk(    #219
        "\x07\x0C#60W…………………………………\x02",
    )

    Jump("loc_7D16")

    label("loc_7D16")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 330, -1, -1)
    SetChrName("女孩")

    AnonymousTalk(    #220
        (
            "\x07\x0C#30W太好了……\x01",
            "还活得好好的。\x02\x03",

            "怎么了……？\x01",
            "为什么坐在这种地方。\x02",
        )
    )

    Jump("loc_7D81")

    label("loc_7D81")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 400, -1, -1)
    SetChrName("少年")

    AnonymousTalk(    #221
        "\x07\x0C#60W…………………………………\x02",
    )

    Jump("loc_7DC3")

    label("loc_7DC3")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(160, 330, -1, -1)
    SetChrName("女孩")

    AnonymousTalk(    #222
        "\x07\x0C#30W……那个………\x02",
    )

    Jump("loc_7DF9")

    label("loc_7DF9")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 350, -1, -1)
    SetChrName("小女孩")

    AnonymousTalk(    #223
        (
            "\x07\x0C#30W……也许是因为肚子饿了。\x02\x03",

            "如果没吃饭的话\x01",
            "就没有说话的力气……\x02",
        )
    )

    Jump("loc_7E6A")

    label("loc_7E6A")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 330, -1, -1)
    SetChrName("女孩")

    AnonymousTalk(    #224
        (
            "\x07\x0C#30W原来如此……\x01",
            "这话由莉丝来说很能让人信服呢。\x02\x03",

            "……那么，\x01",
            "我就把珍藏的东西拿出来吧。\x02",
        )
    )

    Jump("loc_7EEB")

    label("loc_7EEB")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x2, 0x3, -1, 1000, 0)
    Sleep(1500)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(60, 350, -1, -1)
    SetChrName("小女孩")

    AnonymousTalk(    #225
        (
            "\x07\x0C#30W……！\x02\x03",

            "昆西·贝尔的\x01",
            "巧克力……！？\x02",
        )
    )

    Jump("loc_7F65")

    label("loc_7F65")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 330, -1, -1)
    SetChrName("女孩")

    AnonymousTalk(    #226
        (
            "\x07\x0C#30W虽然这是刚才\x01",
            "给莉丝你买的点心……\x02\x03",

            "……可以吗？\x02",
        )
    )

    Jump("loc_7FC3")

    label("loc_7FC3")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(60, 350, -1, -1)
    SetChrName("小女孩")

    AnonymousTalk(    #227
        (
            "\x07\x0C#30W呜……\x01",
            "……我忍……\x02",
        )
    )

    Jump("loc_8003")

    label("loc_8003")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(170, 330, -1, -1)
    SetChrName("女孩")

    AnonymousTalk(    #228
        "\x07\x0C#30W呵呵，好孩子。\x02",
    )

    Jump("loc_8039")

    label("loc_8039")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x3, 0x3, -1, 400, 0)
    Sleep(800)
    OP_C6(0x2, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(150, 330, -1, -1)
    SetChrName("女孩")

    AnonymousTalk(    #229
        (
            "\x07\x0C#30W……喂。\x01",
            "你不想尝尝看吗。\x02\x03",

            "很甜很好吃的哦。\x02",
        )
    )

    Jump("loc_80B6")

    label("loc_80B6")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 400, -1, -1)
    SetChrName("少年")

    AnonymousTalk(    #230
        "\x07\x0C#60W…………………………………\x02",
    )

    Jump("loc_80F8")

    label("loc_80F8")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(40, 350, -1, -1)
    SetChrName("小女孩")

    AnonymousTalk(    #231
        (
            "\x07\x0C#30W昆西牌的是最棒的了……\x02\x03",

            "相比较而言\x01",
            "性价比是最高的……\x02",
        )
    )

    Jump("loc_8161")

    label("loc_8161")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 330, -1, -1)
    SetChrName("女孩")

    AnonymousTalk(    #232
        (
            "\x07\x0C#30W……就是这样。\x02\x03",

            "吃甜食也可以暖和身体，\x01",
            "你就别客气了。\x02",
        )
    )

    Jump("loc_81C5")

    label("loc_81C5")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 400, -1, -1)
    SetChrName("少年")

    AnonymousTalk(    #233
        "\x07\x0C#80W……烦死……了………#20W\x02",
    )

    Jump("loc_8205")

    label("loc_8205")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(210, 320, -1, -1)
    SetChrName("女孩")

    AnonymousTalk(    #234
        "\x07\x0C#30W哎……？\x02",
    )

    Jump("loc_8235")

    label("loc_8235")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x4, 0x3, -1, 400, 0)
    Sleep(800)
    OP_C6(0x3, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(220, 330, -1, -1)
    SetChrName("女孩")

    AnonymousTalk(    #235
        "\x07\x0C#30W啊……\x02",
    )

    Jump("loc_8286")

    label("loc_8286")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(60, 350, -1, -1)
    SetChrName("小女孩")

    AnonymousTalk(    #236
        "\x07\x0C#30W……哼………\x02",
    )

    Jump("loc_82BF")

    label("loc_82BF")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 400, -1, -1)
    SetChrName("少年")

    AnonymousTalk(    #237
        (
            "\x07\x0C#80W……从刚才开始………\x01",
            "就在说些……啰嗦的话………\x02\x03",

            "……赶快……消失吧………\x02\x03",

            "……求你们了………\x01",
            "不要……来管我………#20W\x02",
        )
    )

    Jump("loc_836B")

    label("loc_836B")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 330, -1, -1)
    SetChrName("女孩")

    AnonymousTalk(    #238
        "\x07\x0C#30W………………………………\x02",
    )

    Jump("loc_83AB")

    label("loc_83AB")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(60, 350, -1, -1)
    SetChrName("小女孩")

    AnonymousTalk(    #239
        "\x07\x0C#30W……姐姐………\x02",
    )

    Jump("loc_83E6")

    label("loc_83E6")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 330, -1, -1)
    SetChrName("女孩")

    AnonymousTalk(    #240
        (
            "\x07\x0C#30W嗯，是这样啊。\x02\x03",

            "你要是这样一副不理不睬的样子，\x01",
            "我可要用那一招了哦？\x02",
        )
    )

    Jump("loc_8458")

    label("loc_8458")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x5, 0x3, -1, 1000, 0)
    Sleep(1500)
    OP_C6(0x4, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(70, 350, -1, -1)
    SetChrName("小女孩")

    AnonymousTalk(    #241
        "\x07\x0C#30W哎……？\x02",
    )

    Jump("loc_84B0")

    label("loc_84B0")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 330, -1, -1)
    SetChrName("女孩")

    AnonymousTalk(    #242
        (
            "\x07\x0C#30W………………（嚼嚼）\x02\x03",

            "………唔。\x02",
        )
    )

    Jump("loc_84FF")

    label("loc_84FF")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x5, 0x3, 16777215, 1000, 0)
    Sleep(1500)
    OP_C7(0x1, 0xFF, 0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS413._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS414._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS415._CH")
    OP_C6(0x0, 0x3, -1, 2000, 0)
    Sleep(3000)
    SetMessageWindowPos(120, 320, -1, -1)
    SetChrName("少年")

    AnonymousTalk(    #243
        "\x07\x0C#60W嗯嗯……！？#20W\x02",
    )

    Jump("loc_85E7")

    label("loc_85E7")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 350, -1, -1)
    SetChrName("女孩")

    AnonymousTalk(    #244
        "\x07\x0C#40W…………嗯………………\x02",
    )

    Jump("loc_8625")

    label("loc_8625")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(120, 320, -1, -1)
    SetChrName("少年")

    AnonymousTalk(    #245
        (
            "\x07\x0C#60W！☆▲？◎￥＃＄◆？！？\x02\x03",

            "……呜………（咕咚）#20W\x02",
        )
    )

    Jump("loc_8686")

    label("loc_8686")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(220, 380, -1, -1)
    SetChrName("小女孩")

    AnonymousTalk(    #246
        "\x07\x0C#40W……哇哇……\x02",
    )

    Jump("loc_86BF")

    label("loc_86BF")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x3, -1, 1000, 0)
    Sleep(1500)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(350, 300, -1, -1)
    SetChrName("女孩")

    AnonymousTalk(    #247
        (
            "\x07\x0C#30W……呼。\x02\x03",

            "嗯，就是这样了。\x02",
        )
    )

    Jump("loc_872B")

    label("loc_872B")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 330, -1, -1)
    SetChrName("少年")

    AnonymousTalk(    #248
        "\x07\x0C#80W……呜……咳咳……\x02",
    )

    Jump("loc_8765")

    label("loc_8765")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x2, 0x3, -1, 400, 0)
    Sleep(800)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(120, 330, -1, -1)
    SetChrName("少年")

    AnonymousTalk(    #249
        "\x07\x0C#40W你、你、你……\x02",
    )

    Jump("loc_87BE")

    label("loc_87BE")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(60, 330, -1, -1)
    SetChrName("少年")

    AnonymousTalk(    #250
        "\x07\x0C#30W#4S你突然干什么啊！！\x02",
    )

    Jump("loc_8800")

    label("loc_8800")

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 300, -1, -1)
    SetChrName("女孩")

    AnonymousTalk(    #251
        (
            "\x07\x0C#30W呵呵，太好了。\x02\x03",

            "果然甜的东西\x01",
            "会让人打起精神呢。\x02",
        )
    )

    Jump("loc_886F")

    label("loc_886F")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 330, -1, -1)
    SetChrName("少年")

    AnonymousTalk(    #252
        (
            "\x07\x0C#30W才不是打起精神呢！\x01",
            "是快被你吓死了！\x02\x03",

            "突然来这么一下……\x01",
            "你是女流氓吗！？\x02",
        )
    )

    Jump("loc_88E6")

    label("loc_88E6")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 300, -1, -1)
    SetChrName("女孩")

    AnonymousTalk(    #253
        (
            "\x07\x0C#30W哎呀，和莉丝一样，\x01",
            "最近的孩子们怎么\x01",
            "知道这么多难懂的词呢。\x02\x03",

            "应该不是\x01",
            "主日学校教的吧……\x02",
        )
    )

    Jump("loc_8978")

    label("loc_8978")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(200, 360, -1, -1)
    SetChrName("小女孩")

    AnonymousTalk(    #254
        (
            "\x07\x0C#30W姐姐。\x01",
            "好像不是这个问题吧……？\x02",
        )
    )

    Jump("loc_89C4")

    label("loc_89C4")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 330, -1, -1)
    SetChrName("少年")

    AnonymousTalk(    #255
        (
            "\x07\x0C#30W没、没错！\x01",
            "才不是这个问题呢！\x02\x03",

            "……嗯………？\x02\x03",

            "你们的装扮………\x02",
        )
    )

    Jump("loc_8A39")

    label("loc_8A39")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 300, -1, -1)
    SetChrName("女孩")

    AnonymousTalk(    #256
        (
            "\x07\x0C#30W呵呵……\x01",
            "我还没做自我介绍。\x02",
        )
    )

    Jump("loc_8A7C")

    label("loc_8A7C")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x2, 0x3, 16777215, 1000, 0)
    Sleep(1500)
    OP_AD(0x240110, 0x0, 0x0, 0x64)
    Sleep(3000)
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("女孩")

    AnonymousTalk(    #257
        (
            "\x07\x0C#30W我的名字是露菲娜。#2350W \x01",
            "#30W露菲娜·亚尔珍特。\x02\x03",

            "这孩子是我妹妹莉丝。\x02\x03",

            "你能不能……\x01",
            "告诉我们你的名字呢？\x02",
        )
    )

    Jump("loc_8B41")

    label("loc_8B41")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(0, 16777215, -1)
    OP_AE(0x64)
    Sleep(3000)
    OP_20(0xBB8)
    OP_21()
    OP_C7(0x1, 0xFF, 0x0)
    OP_E5(0x2, 0xFF, 0x13, 500)
    SetChrPos(0x109, 1300, 4000, 320, 180)
    SetChrPos(0x10F, -160, 4000, 160, 90)
    SetChrPos(0x107, 2430, 4000, -1600, 315)
    SetChrPos(0x10E, 670, 4000, -1720, 0)
    OP_6D(0, 4000, 420, 0)
    OP_67(0, 5390, -10000, 0)
    OP_6B(1870, 0)
    OP_6C(314000, 0)
    OP_6E(429, 0)
    Sleep(1000)
    SetMessageWindowPos(150, 80, -1, -1)
    SetChrName("声音")

    AnonymousTalk(    #258
        (
            "\x07\x00……凯文……\x02\x03",

            "凯文……\x01",
            "……你在听吗？\x02",
        )
    )

    Jump("loc_8C52")

    label("loc_8C52")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(280, 230, -1, -1)
    SetChrName("凯文")

    AnonymousTalk(    #259
        "\x07\x00#1063F#3S！！#2S\x02",
    )

    Jump("loc_8C86")

    label("loc_8C86")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(300)
    OP_1D(0xD2)
    FadeToBright(2000, 16777215)
    OP_0D()
    Sleep(300)
    OP_8C(0x109, 270, 400)
    Sleep(300)

    ChrTalk(    #260
        0x109,
        (
            "#1079F#6P……啊………\x02\x03",

            "#1066F抱歉抱歉。\x01",
            "我稍微发了一下呆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x10F,
        "#1802F#5P………没事吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x10E,
        (
            "#176F#6P没办法……\x02\x03",

            "#178F自从来到这里，\x01",
            "实在发生了太多事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x107,
        (
            "#063F#6P要、要不要\x01",
            "稍微休息一下呢……？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 180, 400)
    Sleep(300)

    ChrTalk(    #264
        0x109,
        (
            "#1075F#11P哈哈，别担心。\x02\x03",

            "#1060F总之……\x01",
            "我们暂且把现在的\x01",
            "情报整理一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x10F,
        "#1802F#5P嗯……说得也是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x10E,
        (
            "#176F#6P那个叫做『黑骑士』的男人，\x01",
            "告诉我们的情报\x01",
            "出人意料地多呢。\x02\x03",

            "#178F首先是我们现在\x01",
            "所处的异空间的名字……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x107,
        (
            "#062F#6P『影之国』……\x02\x03",

            "那个黑衣的大哥哥\x01",
            "好像是这么说的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x109,
        (
            "#1065F#11P没错……\x01",
            "真是意味深长的名字啊。\x02\x03",

            "#1063F不过，在七耀教会的\x01",
            "传承中好像没有这样的词语呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x10F,
        (
            "#1446F#5P……嗯。\x01",
            "是从来没听说过的词。\x02\x03",

            "#1443F还有，所谓『王』的存在。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x109,
        (
            "#1063F#11P嗯，\x01",
            "看起来那家伙应该就是\x01",
            "这次事件的幕后黑手了。\x02\x03",

            "他好像对我们的事情\x01",
            "了解不少呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x10E,
        (
            "#178F#6P……说起来，那个男人\x01",
            "说的一些话让我很在意。\x02\x03",

            "好像提到了莉丝小姐的姐姐……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x10F,
        "#1445F#5P……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x109,
        "#1067F#11P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x10E,
        (
            "#173F#6P对不起，\x01",
            "我没打算追根究底的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x109,
        "#1060F#11P没关系……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10F, 135, 400)
    Sleep(300)

    ChrTalk(    #276
        0x10F,
        (
            "#1446F#5P……我的确\x01",
            "有一个姐姐。\x02\x03",

            "#1443F露菲娜·亚尔珍特。\x02\x03",

            "和我们一样……\x01",
            "她曾经也是星杯骑士团的成员。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 270, 400)
    Sleep(300)

    ChrTalk(    #277
        0x109,
        "#1063F#6P莉丝……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x10E,
        (
            "#178F#6P曾经……\x01",
            "也就是说她已经……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x10F,
        (
            "#1448F#5P嗯，\x01",
            "在某次骑士团的任务中殉职了。\x02\x03",

            "是差不多五年前的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0x109,
        "#1067F#6P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x10E,
        (
            "#176F#6P是这样啊……\x02\x03",

            "#178F可是，为什么那个男人\x01",
            "会提到露菲娜小姐的事……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0x10F,
        (
            "#1445F#5P……不知道。\x02\x03",

            "并且我也不知道姐姐\x01",
            "所从事的工作……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 90, 400)
    Sleep(300)

    ChrTalk(    #283
        0x10F,
        "#1802F#5P……凯文呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0x109,
        (
            "#1067F#6P………………………………\x02\x03",

            "#1065F……不好意思。\x01",
            "我心里也没什么底。\x02\x03",

            "#1060F不过，露菲娜姐姐\x01",
            "是位非常优秀的骑士。\x02\x03",

            "不光是武术能力……\x01",
            "凭借她高超的判断和交涉能力\x01",
            "处理过的事件也有不少。\x02\x03",

            "那个男人也许就是在某个事件中\x01",
            "和姐姐认识的也说不定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x10F,
        "#1440F#5P是啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0x10E,
        (
            "#178F#6P不管怎么说，\x01",
            "现在还完全理不出头绪吗……\x02\x03",

            "#175F……抱歉。\x01",
            "结果还是询问了你\x01",
            "那么多事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 180, 400)
    Sleep(300)

    ChrTalk(    #287
        0x109,
        (
            "#1840F#11P不，请别在意。\x02\x03",

            "#1065F……总之，\x01",
            "『敌人』好像在试探\x01",
            "我们的态度。\x02\x03",

            "#1063F接下来我们的行动\x01",
            "必须更为小心才是。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x10E,
        (
            "#179F#6P嗯……说的没错。\x02\x03",

            "#170F好，\x01",
            "那么我们就继续探索吧。\x02",
        )
    )

    Jump("loc_9639")

    label("loc_9639")

    CloseMessageWindow()

    ChrTalk(    #289
        0x107,
        (
            "#560F#6P嗯，那个……\x01",
            "是要从那个黑衣的大哥哥\x01",
            "出现的地方继续前进吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0x109,
        (
            "#1060F#11P嗯，楼梯对面\x01",
            "好像有新的传送阵。\x02\x03",

            "我们做好准备之后，\x01",
            "就用方石回到那里看看吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_96F9():
        OP_6B(2600, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_96F9)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_A2(0x2700)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_28(0x2A, 0x1, 0x10)
    OP_28(0x2A, 0x1, 0x20)
    OP_28(0x2A, 0x1, 0x40)
    OP_28(0x28, 0x4, 0x10)
    OP_28(0x28, 0x4, 0x20)
    OP_28(0x29, 0x4, 0x10)
    OP_28(0x29, 0x4, 0x20)
    OP_28(0x2A, 0x4, 0x10)
    OP_28(0x2A, 0x4, 0x20)
    OP_28(0x2B, 0x4, 0x4)
    OP_28(0x2B, 0x4, 0x8)
    OP_28(0x2B, 0x1, 0x1)
    OP_6D(390, 4000, -1290, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(450, 0)
    SetChrPos(0x109, 390, 4000, -1290, 180)
    SetChrPos(0x10F, 390, 4000, -1290, 180)
    SetChrPos(0x107, 390, 4000, -1290, 180)
    SetChrPos(0x10E, 390, 4000, -1290, 180)
    SetChrChipByIndex(0x109, 65535)
    SetChrChipByIndex(0x10F, 65535)
    SetChrChipByIndex(0x107, 65535)
    SetChrChipByIndex(0x10E, 65535)
    SetChrSubChip(0x109, 0)
    SetChrSubChip(0x10F, 0)
    SetChrSubChip(0x107, 0)
    SetChrSubChip(0x10E, 0)
    OP_69(0x0, 0x0)
    OP_E5(0x2, 0xFF, 0x13, 700)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_33_7853 end

    def Function_34_9840(): pass

    label("Function_34_9840")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D2(0x260285, 0x26028A, 0x13)
    LoadEffect(0x1, "map\\mp253_00.eff")
    LoadEffect(0x2, "map\\mp253_01.eff")
    LoadEffect(0x3, "map\\mp253_02.eff")
    LoadEffect(0x4, "map\\mp253_03.eff")
    LoadEffect(0x5, "map\\mp253_05.eff")
    LoadEffect(0x6, "map\\mp253_04.eff")
    SetChrPos(0x109, 0, 4000, -1770, 0)
    SetChrPos(0x10F, -560, 4000, -3010, 0)
    SetChrPos(0x107, 1250, 4000, -3900, 0)
    SetChrPos(0x10E, -200, 4000, -4300, 0)
    OP_6D(-950, 4000, -980, 0)
    OP_67(0, 5890, -10000, 0)
    OP_6B(1990, 0)
    OP_6C(314000, 0)
    OP_6E(388, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_995A():
        OP_6D(-1180, 4000, 2780, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_995A)

    def lambda_9972():
        OP_67(0, 5490, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_9972)

    def lambda_998A():
        OP_6B(2450, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_998A)

    def lambda_999A():
        OP_6E(403, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_999A)
    OP_8F(0x109, 0x0, 0xFA0, 0xFFFFFE16, 0x3E8, 0x0)
    WaitChrThread(0x10F, 0x0)
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x109, 19)
    SetChrSubChip(0x109, 0)
    OP_22(0x8F, 0x0, 0x64)
    Sleep(100)
    SetChrPos(0x10, 200, 5300, 0, 0)
    PlayEffect(0x1, 0x0, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)
    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    OP_E5(0x2, 0xFF, 0x13, 1000)
    OP_0D()
    Fade(1000)
    OP_E5(0x2, 0xFF, 0x13, 700)
    OP_0D()

    def lambda_9A83():
        OP_8F(0xFE, 0xC8, 0x1770, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_9A83)
    WaitChrThread(0x10, 0x0)
    Sleep(300)

    ChrTalk(    #291
        0x107,
        (
            "#067F#5P哇……\x01",
            "果然很漂亮……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x10E,
        (
            "#173F#5P原来如此……\x01",
            "是这样被解放出来的吗。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(1000)
    OP_6D(0, 5000, 3260, 0)
    OP_67(0, 3980, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(0, 0)
    OP_6E(363, 0)
    SetChrPos(0x109, 0, 4000, -500, 0)
    SetChrPos(0x10F, -700, 4000, -3010, 0)
    SetChrPos(0x107, 750, 4000, -3900, 0)
    SetChrPos(0x10E, -500, 4000, -4300, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrPos(0x10, 0, 6000, 1000, 0)

    def lambda_9BB0():
        OP_6D(0, 7500, 3760, 3500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_9BB0)

    def lambda_9BC8():
        OP_67(0, 1650, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9BC8)

    def lambda_9BE0():
        OP_6B(2700, 3500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9BE0)

    def lambda_9BF0():
        OP_6E(363, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_9BF0)

    def lambda_9C00():
        OP_8F(0xFE, 0x0, 0x2134, 0xAF0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_9C00)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    def lambda_9C2A():
        OP_6B(2000, 8000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9C2A)
    OP_22(0x147, 0x0, 0x64)
    PlayEffect(0x5, 0x2, 0x10, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    OP_23(0x147)
    Fade(500)
    OP_22(0xC, 0x0, 0x64)
    PlayEffect(0x3, 0x2, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x0)
    Sleep(300)
    PlayEffect(0x6, 0x3, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2721)
    OP_A2(0x2504)
    NewScene("ED6_DT21/U4101   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_34_9840 end

    def Function_35_9D19(): pass

    label("Function_35_9D19")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS499._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS446._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS447._CH")
    OP_C5(0x3, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x1, "C_VIS448._CH")
    OP_C6(0x0, 0x3, -1, 0, 0)
    OP_D2(0x26029B, 0x2602A0, 0x13)
    OP_D2(0x26029C, 0x2602A1, 0x14)
    OP_D2(0x260286, 0x26028B, 0x15)
    LoadEffect(0x3, "map\\mp253_04.eff")
    LoadEffect(0x4, "map\\mp253_03.eff")
    LoadEffect(0x5, "map\\mp252_01.eff")
    SetChrPos(0x109, 560, 4000, -1440, 0)
    SetChrPos(0x10F, -120, 4000, -2690, 0)
    SetChrPos(0x107, 1630, 4000, -3530, 0)
    SetChrPos(0x10E, 240, 4000, -3980, 0)
    OP_6D(-2230, 5000, 4310, 0)
    OP_67(0, 3880, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(315000, 0)
    OP_6E(365, 0)
    ClearChrFlags(0x13, 0x80)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x13, 390, 8000, 2150, 180)
    SetChrFlags(0x13, 0x800)
    SetChrChipByIndex(0x13, 19)
    SetChrSubChip(0x13, 0)
    SetChrFlags(0x13, 0x4)
    PlayEffect(0x3, 0x0, 0x13, 0, 600, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    OP_E5(0x2, 0xFF, 0x13, 500)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_9F4C():
        OP_6D(-1210, 4000, 1510, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_9F4C)

    def lambda_9F64():
        OP_67(0, 4850, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9F64)

    def lambda_9F7C():
        OP_6B(2850, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9F7C)

    def lambda_9F8C():
        OP_6E(327, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_9F8C)

    def lambda_9F9C():
        OP_8F(0xFE, 0x186, 0xFA0, 0x866, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_9F9C)
    WaitChrThread(0x13, 0x0)
    SetChrSubChip(0x13, 0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    Fade(1000)
    OP_82(0x2, 0x2)
    PlayEffect(0x3, 0x1, 0x13, 0, 600, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)

    def lambda_A008():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x7D0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_A008)
    OP_22(0x99, 0x0, 0x64)
    OP_82(0x0, 0x0)
    OP_0D()
    Sleep(1000)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #293
        0x10E,
        "#173F难道#6P……！？\x02",
    )

    CloseMessageWindow()
    PlayEffect(0x4, 0x4, 0x13, 0, 600, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_22(0x138, 0x0, 0x64)
    OP_23(0x146)

    def lambda_A0F6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_A0F6)
    OP_82(0x2, 0x2)
    WaitChrThread(0x13, 0x0)
    Fade(500)
    OP_82(0x1, 0x0)
    OP_0D()
    Sleep(300)

    NpcTalk(    #294
        0x13,
        "穆拉少校",
        "#272F#5P哼……是闪光弹！？\x02",
    )

    Jump("loc_A153")

    label("loc_A153")

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x13, 20)
    SetChrSubChip(0x13, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #295
        0x13,
        "穆拉少校",
        (
            "#271F#11P#3S奥利维尔，快后退！\x01",
            "那大概是冲着──\x02",
        )
    )

    Jump("loc_A1BE")

    label("loc_A1BE")

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x13, 0xFFFFFF38, 1500, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #296
        0x13,
        "穆拉少校",
        "#273F#11P什……！？\x02",
    )

    Jump("loc_A220")

    label("loc_A220")

    CloseMessageWindow()

    ChrTalk(    #297
        0x10E,
        "#171F#6P少校……是你啊。\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #298
        0x13,
        "穆拉少校",
        (
            "#273F#11P上尉……\x01",
            "为什么你会在这里……\x02\x03",

            "#270F#3S！？#2S\x02",
        )
    )

    Jump("loc_A2A5")

    label("loc_A2A5")

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    ClearChrFlags(0x13, 0x800)
    SetChrChipByIndex(0x13, 5)
    SetChrSubChip(0x13, 0)
    OP_0D()
    Sleep(300)
    OP_62(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_8C(0x13, 90, 400)
    Sleep(500)
    OP_8C(0x13, 270, 400)
    Sleep(500)
    OP_63(0x13)
    Sleep(1000)

    NpcTalk(    #299
        0x13,
        "穆拉少校",
        (
            "#276F#5P这里到底是……\x02\x03",

            "奥利维尔那家伙\x01",
            "消失到什么地方去了……？\x02",
        )
    )

    Jump("loc_A35E")

    label("loc_A35E")

    CloseMessageWindow()

    ChrTalk(    #300
        0x109,
        (
            "#1063F#6P……是这样啊。\x01",
            "看来奥利维特皇子\x01",
            "也和你在一起。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 180, 400)
    Sleep(400)

    ChrTalk(    #301
        0x10E,
        (
            "#179F#6P……还是由我\x01",
            "来说明一下情况吧。\x02\x03",

            "#170F如果有不明白的地方，\x01",
            "请尽管问好了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrPos(0x109, -1200, 4000, -2700, 0)
    SetChrPos(0x10F, -260, 4000, -4170, 0)
    SetChrPos(0x107, 1080, 4000, -3810, 0)
    SetChrPos(0x10E, 270, 4000, -2000, 0)
    SetChrPos(0x13, 290, 4000, -190, 180)
    ClearChrFlags(0x13, 0x4)
    OP_6D(-780, 4000, -920, 0)
    OP_67(0, 6110, -10000, 0)
    OP_6B(2170, 0)
    OP_6C(315000, 0)
    OP_6E(381, 0)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #302
        0x13,
        "穆拉少校",
        (
            "#272F#11P原来如此……\x01",
            "竟然是这样。\x02\x03",

            "#270F老实说，一切发生的太突然了，\x01",
            "我一点也不觉得这会是真的……\x02",
        )
    )

    Jump("loc_A554")

    label("loc_A554")

    CloseMessageWindow()

    ChrTalk(    #303
        0x10E,
        (
            "#170F#6P……没办法啊。\x02\x03",

            "像我这样死脑筋的人\x01",
            "到现在还是半信半疑呢。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #304
        0x13,
        "穆拉少校",
        (
            "#278F#11P没什么……\x01",
            "要说死脑筋的话我也是一样。\x02\x03",

            "#270F……可是听了你们的话，\x01",
            "我知道这不是该发呆的场合。\x02\x03",

            "我也担心着那个赖皮蛋的安危，\x01",
            "就让我也为探索行动尽一份力吧。\x02",
        )
    )

    Jump("loc_A67C")

    label("loc_A67C")

    CloseMessageWindow()

    ChrTalk(    #305
        0x109,
        (
            "#1075F#6P那真是帮了我们大忙。\x02\x03",

            "#1063F话说回来，奥利维特皇子\x01",
            "当时正和你在一起……\x02\x03",

            "当你被光包围起来的时候\x01",
            "是怎样一种状况呢？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #306
        0x13,
        "穆拉少校",
        (
            "#272F#11P嗯……\x01",
            "那时我们为了视察\x01",
            "而访问了帕尔姆镇。\x02\x03",

            "#270F晚上刚回到旅馆的房间，\x01",
            "突然周围就变得一片白。\x02\x03",

            "那家伙也在场，\x01",
            "所以说不定也被卷了进来。\x02",
        )
    )

    Jump("loc_A7D2")

    label("loc_A7D2")

    CloseMessageWindow()

    ChrTalk(    #307
        0x107,
        (
            "#060F#6P哎，帕尔姆镇……\x02\x03",

            "我记得好像是埃雷波尼亚\x01",
            "最南边的城镇吧？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #308
        0x13,
        "穆拉少校",
        (
            "#277F#11P没错，是和利贝尔国境\x01",
            "最为接近的城镇。\x02",
        )
    )

    Jump("loc_A877")

    label("loc_A877")

    CloseMessageWindow()

    ChrTalk(    #309
        0x10F,
        (
            "#1802F#6P……那个。\x02\x03",

            "刚才你们一直提到的\x01",
            "奥利维特皇子是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0x109,
        (
            "#1062F#5P啊，就是那次事件中\x01",
            "一起登上浮游都市的成员之一。\x02\x03",

            "#1066F虽说是身为皇子，\x01",
            "不过他还真是个轻松活泼的人啊。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #311
        0x13,
        "穆拉少校",
        (
            "#274F#11P……用轻松活泼来形容那家伙\x01",
            "是不是有点用词不当呢。\x02\x03",

            "他只不过是喜欢到处去凑热闹，\x01",
            "把周围的人都搅和得头疼不已罢了。\x02",
        )
    )

    Jump("loc_A9EA")

    label("loc_A9EA")

    CloseMessageWindow()

    ChrTalk(    #312
        0x10E,
        (
            "#179F#6P呵呵……这么讲太谦虚了。\x02\x03",

            "#171F皇子回国后的活跃表现，\x01",
            "我在利贝尔也有所耳闻呢。\x02\x03",

            "据说已经成为帝国\x01",
            "社交界新的宠儿了。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #313
        0x13,
        "穆拉少校",
        (
            "#277F#11P看来他装成老老实实的样子\x01",
            "还是能够有些作为的……\x02\x03",

            "一旦把本性暴露出来，\x01",
            "还不知道会产生什么样的风言风语呢。\x02",
        )
    )

    Jump("loc_AB1A")

    label("loc_AB1A")

    CloseMessageWindow()

    ChrTalk(    #314
        0x107,
        "#067F#6P嘻嘻……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x109,
        "#1840F#6P少校，你也实在很辛苦呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x10F,
        "#1440F#6P………………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x109, 135, 400)
    Sleep(300)

    ChrTalk(    #317
        0x109,
        "#1079F#5P嗯？怎么了？\x02",
    )

    CloseMessageWindow()

    def lambda_ABDF():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_ABDF)
    Sleep(100)
    OP_8C(0x10E, 180, 400)

    ChrTalk(    #318
        0x10F,
        (
            "#1447F#6P……不，没什么。\x02\x03",

            "#1443F只是觉得，\x01",
            "你们这几位\x01",
            "互相都认识……\x02\x03",

            "这说不定是\x01",
            "被白光卷进\x01",
            "这个世界来的条件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0x107,
        "#064F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0x109,
        (
            "#1063F#5P原来如此……\x01",
            "这么说的确没错。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #321
        0x13,
        "穆拉少校",
        (
            "#272F#11P说得更准确一点，\x01",
            "也就是会被封入\x01",
            "『封印石』的人选条件。\x02",
        )
    )

    Jump("loc_AD2B")

    label("loc_AD2B")

    CloseMessageWindow()

    def lambda_AD32():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AD32)
    Sleep(100)

    def lambda_AD45():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_AD45)
    Sleep(100)
    OP_8C(0x10E, 0, 400)
    Sleep(300)

    NpcTalk(    #322
        0x13,
        "穆拉少校",
        (
            "#270F#11P听你们刚才说，\x01",
            "不仅埃尔赛尤号，\x01",
            "连格兰赛尔市也变得很奇怪……\x02\x03",

            "那你们是不是还没找到\x01",
            "乘员和居民的封印石呢？\x02",
        )
    )

    Jump("loc_ADF8")

    label("loc_ADF8")

    CloseMessageWindow()

    ChrTalk(    #323
        0x10E,
        "#178F#6P嗯……你说的没错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0x107,
        (
            "#065F#6P也、也许这也是\x01",
            "『规则』的一种呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0x109,
        (
            "#1065F#6P嗯……\x02\x03",

            "#1063F……无论如何，\x01",
            "我们就这样继续探索吧。\x02\x03",

            "现在最要紧的是\x01",
            "查明王都到底发生了什么事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0x10E,
        "#176F#6P啊啊……是啊。\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #327
        0x13,
        "穆拉少校",
        (
            "#277F#11P可以的话，\x01",
            "请让我一起行动。\x02\x03",

            "我想亲身把握一下\x01",
            "当前的异常事态。\x02",
        )
    )

    Jump("loc_AF6A")

    label("loc_AF6A")

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2708)
    OP_28(0x2C, 0x4, 0x4)
    OP_28(0x2C, 0x4, 0x8)
    OP_28(0x2C, 0x1, 0x1)
    OP_28(0x2C, 0x1, 0x2)
    OP_3F(0x354, 1)
    OP_DB(0x0, 0xC)
    OP_A2(0x25D2)
    Call(6, 21)
    SetChrFlags(0x13, 0x80)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_DD(0x1, 0x0, 0x0, 16640, 0, 0, 0)
    FadeToDark(0, 0, -1)
    OP_C0(0x20, 0x1, 0x4100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x109, 1020, 4000, -2720, 0)
    SetChrPos(0x10F, -450, 4000, -2720, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B075")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 290, 4000, -190, 180)
    SetChrPos(0x10E, 1460, 4000, -4520, 0)
    SetChrPos(0x10D, -320, 4000, -4350, 0)
    Jump("loc_B104")

    label("loc_B075")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B0BE")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 290, 4000, -190, 180)
    SetChrPos(0x107, 1460, 4000, -4520, 0)
    SetChrPos(0x10D, -320, 4000, -4350, 0)
    Jump("loc_B104")

    label("loc_B0BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B104")
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 290, 4000, -190, 180)
    SetChrPos(0x107, 1460, 4000, -4520, 0)
    SetChrPos(0x10E, -320, 4000, -4350, 0)

    label("loc_B104")

    OP_6D(-1420, 4000, -120, 0)
    OP_67(0, 5400, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(315000, 0)
    OP_6E(381, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_C4(0x0, 0x200)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #328
        (
            "\x07\x05──从现在开始，\x01",
            "在庭院会显示『队伍编成按钮』。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    Sleep(500)
    OP_C6(0x1, 0x3, -1, 500, 0)
    OP_C6(0x3, 0x0, 16000, 16000, 0)
    OP_C6(0x3, 0x1, 250, 250, 0)
    OP_A3(0x1)
    OP_43(0x0, 0x0, 0x1, 0x24)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #329
        (
            "\x07\x05按下按钮后，\x01",
            "会出现和刚才一样的队伍编成界面，\x01",
            "可以选择固定成员之外的同行人员。\x02\x03",

            "另外，在据点的时候\x01",
            "也可以在Camp Menu中\x01",
            "对待机成员的装备、回路进行操作。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(300)
    OP_A2(0x1)
    Sleep(500)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    FadeToBright(300, 0)
    OP_C6(0x0, 0x3, -1, 500, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B408")

    ChrTalk(    #330
        0x11,
        (
            "#560F#11P那、那么\x01",
            "就请大家一路小心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0x109,
        "#1060F#6P啊啊，交给我吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0x10F,
        (
            "#1447F#6P……提妲，\x01",
            "就拜托你留在『庭院』看家了。\x01",
            "那么就请多关照了。\x02\x03",

            "#1448F记住，不管发生了什么\x01",
            "都不要随意行事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0x11,
        "#060F#11P我、我知道了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B60D")

    label("loc_B408")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B529")

    ChrTalk(    #334
        0x12,
        (
            "#178F#11P那么……\x01",
            "就拜托你们继续在王都调查了。\x02\x03",

            "#176F我还是在这里\x01",
            "稍微让头脑冷静一下好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0x107,
        "#063F#6P尤莉亚小姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0x109,
        (
            "#1065F#6P如果有什么进展，\x01",
            "我们会立刻和你联系。\x02\x03",

            "#1060F在这期间，\x01",
            "那就拜托了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0x12,
        "#170F#11P知道了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B60D")

    label("loc_B529")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B60D")

    ChrTalk(    #338
        0x13,
        (
            "#278F#11P那么，探索的任务\x01",
            "就拜托你们了。\x02\x03",

            "#277F我就在这里\x01",
            "给你们担任后勤。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0x109,
        (
            "#1060F#6P拜托了。\x02\x03",

            "一旦我们找到皇子的情报，\x01",
            "就会尽快回来通知你的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0x13,
        "#277F#11P嗯，拜托了。\x02",
    )

    CloseMessageWindow()

    label("loc_B60D")

    OP_22(0x15F, 0x0, 0x64)
    Sleep(500)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B677")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B6DE")

    label("loc_B677")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B69F")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B6DE")

    label("loc_B69F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B6C7")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B6DE")

    label("loc_B6C7")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_B6DE")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B70B")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B772")

    label("loc_B70B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B733")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B772")

    label("loc_B733")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B75B")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B772")

    label("loc_B75B")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_B772")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B79F")
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B7EC")

    label("loc_B79F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B7C7")
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B7EC")

    label("loc_B7C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B7EC")
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_B7EC")

    Sleep(1000)

    def lambda_B7F7():
        OP_6D(-700, 4000, -960, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_B7F7)
    OP_8C(0x10F, 90, 400)
    WaitChrThread(0xEE, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B849")

    ChrTalk(    #341
        0x10E,
        "#173F#6P刚才的是……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_B86D")

    label("loc_B849")


    ChrTalk(    #342
        0x12,
        "#173F#11P刚才的是……？\x02",
    )

    CloseMessageWindow()

    label("loc_B86D")


    ChrTalk(    #343
        0x10F,
        "#1443F#5P凯文……难道说。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0x109,
        (
            "#1065F#6P啊啊……\x01",
            "好像又出现了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 21)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)
    PlayEffect(0x5, 0x0, 0x109, 270, 1250, 100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xC9, 0x0, 0x64)
    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 100, -1, -1)

    AnonymousTalk(    #345
        "\x07\x0C\x18#2S#80W……异邦者啊……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 100, -1, -1)

    AnonymousTalk(    #346
        "\x07\x0C\x18#2S#80W手持『方石』的人啊……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B9E8")

    ChrTalk(    #347
        0x107,
        "#064F#6P女人的声音……\x02",
    )

    CloseMessageWindow()
    Jump("loc_BA0C")

    label("loc_B9E8")


    ChrTalk(    #348
        0x11,
        "#064F#11P女人的声音……\x02",
    )

    CloseMessageWindow()

    label("loc_BA0C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BA44")

    ChrTalk(    #349
        0x10D,
        "#270F#6P……到底是什么人？\x02",
    )

    CloseMessageWindow()
    Jump("loc_BA6C")

    label("loc_BA44")


    ChrTalk(    #350
        0x13,
        "#270F#11P……到底是什么人？\x02",
    )

    CloseMessageWindow()

    label("loc_BA6C")


    ChrTalk(    #351
        0x109,
        (
            "#1841F#6P关于这一点，\x01",
            "现在还完全弄不清楚。\x02\x03",

            "#1063F看起来，她好像\x01",
            "听不见我们的声音。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #352
        (
            "\x07\x0C\x18#2S#80W……你们似乎顺利地……\x01",
            "在收集着自己的力量……\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #353
        (
            "\x07\x0C\x18#2S#80W现在……\x01",
            "就来解放一下『方石』的力量吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(1000)
    OP_22(0x15F, 0x0, 0x64)
    PlayEffect(0x5, 0x1, 0x109, 270, 1250, 100, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_23(0xC9)
    OP_C6(0x2, 0x3, -1, 1000, 0)
    OP_C6(0x3, 0x0, 467000, 305000, 0)
    OP_C6(0x3, 0x1, 1200, 1200, 0)
    Sleep(1500)
    OP_A3(0x1)
    OP_43(0x0, 0x0, 0x1, 0x24)
    Sleep(2000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #354
        "\x07\x05关于『支援能力』\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)

    AnonymousTalk(    #355
        (
            "\x07\x05在方石界面中，\x01",
            "可以从待机成员中选择一名\x01",
            "作为『支援队员』。\x02\x03",

            "被选为『支援队员』的伙伴\x01",
            "能够通过『方石』给予行动中的队伍\x01",
            "各种各样的支援效果。\x02\x03",

            "支援效果根据各人的不同\x01",
            "会产生对诸如属性值、回复效果、\x01",
            "道具取得率等参数的影响。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()
    OP_A2(0x1)
    Sleep(500)
    OP_C6(0x2, 0x3, 16777215, 500, 0)
    OP_22(0xC9, 0x0, 0x64)
    Sleep(1500)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #356
        (
            "\x07\x0C\x18#2S#80W对方的力量……\x01",
            "……过于强大……\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #357
        (
            "\x07\x0C\x18#2S#80W愿你们的羁绊……\x01",
            "……成为指引前进的光芒……\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 100, -1, -1)

    AnonymousTalk(    #358
        "\x07\x0C\x18#2S#80W…………………………………\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    Fade(500)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_23(0xC9)
    OP_0D()
    Sleep(500)
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x10F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BEB4")
    OP_62(0xF0, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_BF0C")

    label("loc_BEB4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BED7")
    OP_62(0xF0, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_BF0C")

    label("loc_BED7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BEFA")
    OP_62(0xF0, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_BF0C")

    label("loc_BEFA")

    OP_62(0xF0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_BF0C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF2F")
    OP_62(0xF1, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_BF87")

    label("loc_BF2F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF52")
    OP_62(0xF1, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_BF87")

    label("loc_BF52")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF75")
    OP_62(0xF1, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_BF87")

    label("loc_BF75")

    OP_62(0xF1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_BF87")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BFAA")
    OP_62(0x11, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_BFED")

    label("loc_BFAA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BFCD")
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_BFED")

    label("loc_BFCD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BFED")
    OP_62(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_BFED")

    Sleep(2000)
    OP_63(0x109)
    OP_63(0x10F)
    OP_63(0xF0)
    OP_63(0xF1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C012")
    OP_63(0x11)
    Jump("loc_C037")

    label("loc_C012")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C026")
    OP_63(0x12)
    Jump("loc_C037")

    label("loc_C026")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C037")
    OP_63(0x13)

    label("loc_C037")

    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C0C4")

    ChrTalk(    #359
        0x10D,
        (
            "#272F#6P……看来现在的事态\x01",
            "越来越不能用常理来解释了。\x02\x03",

            "#277F不过，从刚才的声音中\x01",
            "完全感觉不到恶意。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C13C")

    label("loc_C0C4")


    ChrTalk(    #360
        0x13,
        (
            "#272F#11P……看来现在的事态\x01",
            "越来越不能用常理来解释了。\x02\x03",

            "#277F不过，从刚才的声音中\x01",
            "完全感觉不到恶意。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C13C")


    ChrTalk(    #361
        0x10F,
        (
            "#1447F#5P嗯……\x01",
            "至少不像『黑骑士』那样\x01",
            "对我们抱有敌意。\x02\x03",

            "#1443F不过，还没弄清她的身份，\x01",
            "我们也不能轻易地完全相信……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #362
        0x109,
        (
            "#1075F总之，『方石』似乎已经\x01",
            "追加了各种各样的机能。\x02\x03",

            "#1060F我们首先来试试看吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C24C():
        OP_6B(2600, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C24C)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C32B")
    SetChrFlags(0x11, 0x80)
    Jump("loc_C354")

    label("loc_C32B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C341")
    SetChrFlags(0x12, 0x80)
    Jump("loc_C354")

    label("loc_C341")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C354")
    SetChrFlags(0x13, 0x80)

    label("loc_C354")

    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C7(0x1, 0xFF, 0x0)
    OP_E5(0x2, 0xFF, 0x13, 700)
    Call(0, 5)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_35_9D19 end

    def Function_36_C384(): pass

    label("Function_36_C384")

    OP_C6(0x3, 0x3, -1, 500, 0)
    OP_C6(0x3, 0x4, 0, 0, 0)
    Sleep(500)

    label("loc_C3A7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C3EA")
    Sleep(200)
    OP_C6(0x3, 0x3, 16777215, 500, 0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_C3D3")
    Jump("loc_C3EA")

    label("loc_C3D3")

    OP_C6(0x3, 0x3, -1, 500, 0)
    Sleep(500)
    Jump("loc_C3A7")

    label("loc_C3EA")

    Return()

    # Function_36_C384 end

    def Function_37_C3EB(): pass

    label("Function_37_C3EB")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D2(0x260285, 0x26028A, 0x13)
    LoadEffect(0x1, "map\\mp253_00.eff")
    LoadEffect(0x2, "map\\mp253_01.eff")
    LoadEffect(0x3, "map\\mp253_02.eff")
    LoadEffect(0x4, "map\\mp253_03.eff")
    LoadEffect(0x5, "map\\mp253_05.eff")
    LoadEffect(0x6, "map\\mp253_04.eff")
    SetChrPos(0x109, 0, 4000, -1770, 0)
    SetChrPos(0x10F, -560, 4000, -3010, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x11, 1440, 4000, -3840, 0)
    SetChrPos(0x12, 600, 4000, -4670, 0)
    SetChrPos(0x13, -780, 4000, -4310, 0)
    SetChrFlags(0xF0, 0x80)
    SetChrFlags(0xF1, 0x80)
    OP_6D(-950, 4000, -980, 0)
    OP_67(0, 5890, -10000, 0)
    OP_6B(1990, 0)
    OP_6C(314000, 0)
    OP_6E(388, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_C52F():
        OP_6D(-1180, 4000, 2780, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_C52F)

    def lambda_C547():
        OP_67(0, 5490, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_C547)

    def lambda_C55F():
        OP_6B(2210, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_C55F)

    def lambda_C56F():
        OP_6E(403, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_C56F)
    OP_8F(0x109, 0x0, 0xFA0, 0xFFFFFE16, 0x3E8, 0x0)
    WaitChrThread(0x10F, 0x0)
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x109, 19)
    SetChrSubChip(0x109, 0)
    OP_22(0x8F, 0x0, 0x64)
    Sleep(100)
    SetChrPos(0x10, 200, 5300, 0, 0)
    PlayEffect(0x1, 0x0, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)
    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    OP_E5(0x2, 0xFF, 0x13, 1000)
    OP_0D()
    Fade(1000)
    OP_E5(0x2, 0xFF, 0x13, 700)
    OP_0D()

    def lambda_C658():
        OP_8F(0xFE, 0xC8, 0x1770, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_C658)
    WaitChrThread(0x10, 0x0)
    Sleep(300)
    Fade(1000)
    OP_6D(0, 5000, 3260, 0)
    OP_67(0, 3980, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(0, 0)
    OP_6E(363, 0)
    SetChrPos(0x109, 0, 4000, -500, 0)
    SetChrPos(0x10F, -700, 4000, -3010, 0)
    SetChrPos(0x11, 950, 4000, -3840, 0)
    SetChrPos(0x12, 100, 4000, -4500, 0)
    SetChrPos(0x13, -1280, 4000, -4810, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrPos(0x10, 0, 6000, 1000, 0)

    def lambda_C72F():
        OP_6D(0, 7500, 3760, 3500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C72F)

    def lambda_C747():
        OP_67(0, 1650, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C747)

    def lambda_C75F():
        OP_6B(2700, 3500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_C75F)

    def lambda_C76F():
        OP_6E(363, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_C76F)

    def lambda_C77F():
        OP_8F(0xFE, 0x0, 0x2134, 0xAF0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_C77F)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    def lambda_C7A9():
        OP_6B(2000, 8000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_C7A9)
    OP_22(0x147, 0x0, 0x64)
    PlayEffect(0x5, 0x2, 0x10, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    OP_23(0x147)
    Fade(500)
    OP_22(0xC, 0x0, 0x64)
    PlayEffect(0x3, 0x2, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x0)
    Sleep(300)
    PlayEffect(0x6, 0x3, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/U4102   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_37_C3EB end

    def Function_38_C895(): pass

    label("Function_38_C895")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D2(0x2700A0, 0x2700A4, 0x13)
    OP_D2(0x27055A, 0x27055E, 0x14)
    OP_D2(0x27055B, 0x27055F, 0x15)
    LoadEffect(0x3, "map\\mp253_04.eff")
    LoadEffect(0x4, "map\\mp253_03.eff")
    SetChrPos(0x109, 560, 4000, -1440, 0)
    SetChrPos(0x10F, -120, 4000, -2690, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x11, 2000, 4000, -3090, 0)
    SetChrPos(0x12, 1530, 4000, -4170, 0)
    SetChrPos(0x13, 70, 4000, -4130, 0)
    SetChrFlags(0xF0, 0x80)
    SetChrFlags(0xF1, 0x80)
    OP_6D(-2230, 5000, 4310, 0)
    OP_67(0, 3880, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(315000, 0)
    OP_6E(365, 0)
    ClearChrFlags(0x14, 0x80)
    OP_9F(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x14, 390, 8000, 2150, 180)
    SetChrFlags(0x14, 0x800)
    SetChrChipByIndex(0x14, 20)
    SetChrSubChip(0x14, 0)
    SetChrFlags(0x14, 0x4)
    PlayEffect(0x3, 0x0, 0x14, 0, 600, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    OP_E5(0x2, 0xFF, 0x13, 500)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_CA17():
        OP_6D(-1210, 4000, 1510, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_CA17)

    def lambda_CA2F():
        OP_67(0, 4850, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_CA2F)

    def lambda_CA47():
        OP_6B(2850, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_CA47)

    def lambda_CA57():
        OP_6E(327, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_CA57)

    def lambda_CA67():
        OP_8F(0xFE, 0x186, 0xFA0, 0x866, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_CA67)
    WaitChrThread(0x14, 0x0)
    SetChrSubChip(0x14, 0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    Fade(1000)
    OP_82(0x2, 0x2)
    PlayEffect(0x3, 0x1, 0x14, 0, 600, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)

    def lambda_CAD3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x7D0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_CAD3)
    OP_22(0x99, 0x0, 0x64)
    OP_82(0x0, 0x0)
    OP_0D()
    Sleep(1000)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #363
        0x13,
        "#277F#6P哼，是那个小丫头……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0x109,
        (
            "#1840F#6P她的哥哥们\x01",
            "似乎不在一起呢。\x02",
        )
    )

    CloseMessageWindow()
    PlayEffect(0x4, 0x4, 0x14, 0, 600, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_22(0x138, 0x0, 0x64)
    OP_23(0x146)

    def lambda_CC16():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_CC16)
    OP_82(0x2, 0x2)
    WaitChrThread(0x14, 0x0)
    Fade(500)
    OP_82(0x1, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #365
        0x14,
        (
            "#413F#5P唔，嗯……\x02\x03",

            "#215F吉尔哥、多伦哥……\x01",
            "……到底发生了什么啊……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x14, 21)
    SetChrSubChip(0x14, 0)
    OP_0D()
    Sleep(300)
    OP_62(0x14, 0xFFFFFF38, 1300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #366
        0x14,
        (
            "#213F#11P咦……\x02\x03",

            "………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0x13,
        "#277F#6P好久不见了，小丫头。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #368
        0x109,
        (
            "#1066F#6P哈哈，那顶帽子上\x01",
            "是运输业的商标吗？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    ClearChrFlags(0x14, 0x800)
    SetChrChipByIndex(0x14, 19)
    SetChrSubChip(0x14, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #369
        0x14,
        (
            "#213F#11P………………………………\x02\x03",

            "#413F……怎么，是做梦吗。\x02\x03",

            "#215F唉，反正是做梦，\x01",
            "要是约修亚出来就好了……\x02\x03",

            "为什么会梦到这个白痴军人\x01",
            "还有冒牌神父啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0x13,
        (
            "#278F#6P哼……\x01",
            "这小丫头嘴还真是刁啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0x109,
        "#1068F#6P而且，我也不是冒牌的……\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrPos(0x109, 270, 4000, -2029, 0)
    SetChrPos(0x13, -670, 4000, -2950, 0)
    SetChrPos(0x11, 1670, 4000, -3420, 0)
    SetChrPos(0x12, 1140, 4000, -4560, 0)
    SetChrPos(0x10F, -320, 4000, -4620, 0)
    SetChrPos(0x14, 290, 4000, -190, 180)
    SetChrChipByIndex(0x14, 19)
    SetChrSubChip(0x14, 0)
    OP_6D(-1180, 4000, -360, 0)
    OP_67(0, 5400, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(315000, 0)
    OP_6E(381, 0)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #372
        0x14,
        (
            "#416F#11P#3S──哎呀真是的！\x01",
            "这些乱七八糟的话我已经听够了！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #373
        0x14,
        (
            "#214F#11P你们倒是告诉我\x01",
            "大哥他们到底在哪儿啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0x109,
        (
            "#1068F#6P唉，所以啊，\x01",
            "刚才不是说明过很多次了吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0x13,
        (
            "#272F#6P我们现在也是一样\x01",
            "被囚禁于这个异空间中……\x02\x03",

            "#270F不可能知道\x01",
            "你的兄弟们的去向。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0x14,
        (
            "#216F#11P这、这样的说明\x01",
            "怎么能让我接受呢！\x02\x03",

            "#413F虽然，\x01",
            "我大概知道这里\x01",
            "并不是什么正常的地方……\x02\x03",

            "#212F可是，直到刚才为止，\x01",
            "我们的山猫号还在\x01",
            "克洛斯贝尔的上空飞行着啊！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #377
        0x10F,
        (
            "#1443F#6P原来如此……\x01",
            "就是在那时被白光卷了进来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #378
        0x14,
        (
            "#213F#11P是啊……\x02\x01",

            "#214F等一下，你怎么知道的！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #379
        0x12,
        (
            "#176F#6P嗯，和埃尔赛尤号的\x01",
            "情况基本一致呢。\x02\x03",

            "#178F要说有什么不一样的，\x01",
            "就是克洛斯贝尔离得远了一些……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0x11,
        (
            "#064F#6P可、可是在地图上\x01",
            "也算不上很远吧。\x02\x03",

            "嗯，我记得应该是\x01",
            "帝国和共和国之间的自治州吧……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0x109,
        (
            "#1065F#5P没错，乘坐国际定期船\x01",
            "一个小时左右就到了。\x02\x03",

            "#1067F嗯……\x01",
            "其中应该有什么关联吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #382
        0x14,
        (
            "#216F#11P所～以啊！\x01",
            "别当我不存在一样自说自话啦！\x02\x03",

            "#416F算了！\x01",
            "我回山猫号去了！\x02\x03",

            "#214F跟你们在一起\x01",
            "没什么好说的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #383
        0x11,
        "#065F#6P可、可是乔丝特姐姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #384
        0x13,
        (
            "#272F#6P……话说在前面，\x01",
            "王都已经变成了异世界。\x02\x03",

            "#270F你们的飞艇\x01",
            "也处在随时可能被\x01",
            "徘徊的魔物袭击的状况。\x02\x03",

            "这样你也要单独行动吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #385
        0x14,
        "#215F#11P那、那个嘛……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #386
        0x109,
        (
            "#1065F#6P要是你硬要这么做的话，\x01",
            "我们倒是可以带你去山猫号……\x02\x03",

            "#1060F不过在搞清楚状况之前，\x01",
            "还是最好一起行动吧。\x02\x03",

            "反正我们也不是\x01",
            "什么陌生人了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #387
        0x14,
        (
            "#215F#11P…………………………………\x02\x03",

            "#416F……我知道啦。\x02\x03",

            "#212F老实说，我现在脑子里还很混乱，\x01",
            "不知道该怎么办才好……\x02\x03",

            "在和哥哥们会合之前\x01",
            "就暂时和你们一起行动吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #388
        0x109,
        (
            "#1840F#6P是吗。\x01",
            "嗯，那就这样吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #389
        0x14,
        (
            "#214F#11P话说在前面，\x01",
            "我可不打算在这里白吃饭！\x02\x03",

            "既然要一起行动，\x01",
            "那我就会尽力帮忙，\x01",
            "你们可别客气！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #390
        0x13,
        (
            "#277F#6P哼，多亏你有这份心。\x02\x03",

            "不过，但愿你别\x01",
            "给我们扯后腿就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #391
        0x14,
        "#216F#11P不、不用你担心！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #392
        0x11,
        "#067F#6P啊、啊哈哈……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #393
        0x10F,
        (
            "#1448F#5P（……看不出来，\x01",
            "  还真是个重情义的女孩呢。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #394
        0x12,
        (
            "#170F#6P（是啊……\x01",
            "  她的本性还是很直率的。）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D7FE():
        OP_6B(2600, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_D7FE)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_A2(0x270F)
    OP_28(0x2C, 0x1, 0x40)
    OP_28(0x2C, 0x1, 0x80)
    OP_3F(0x355, 1)
    OP_DB(0x0, 0xA)
    OP_A2(0x25D0)
    Call(6, 19)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    ClearChrFlags(0xF0, 0x80)
    ClearChrFlags(0xF1, 0x80)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_DD(0x1, 0x0, 0x0, 16640, 0, 0, 0)
    FadeToDark(0, 0, -1)
    OP_C0(0x20, 0x1, 0x4100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
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

    # Function_38_C895 end

    def Function_39_D987(): pass

    label("Function_39_D987")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D2(0x260285, 0x26028A, 0x13)
    LoadEffect(0x1, "map\\mp253_00.eff")
    LoadEffect(0x2, "map\\mp253_01.eff")
    LoadEffect(0x3, "map\\mp253_02.eff")
    LoadEffect(0x4, "map\\mp253_03.eff")
    LoadEffect(0x5, "map\\mp253_05.eff")
    LoadEffect(0x6, "map\\mp253_04.eff")
    SetChrPos(0x109, 0, 4000, -1770, 0)
    SetChrPos(0x10F, -560, 4000, -3010, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x11, 1910, 4000, -3310, 0)
    SetChrPos(0x12, 1190, 4000, -4940, 0)
    SetChrPos(0x13, -240, 4000, -4660, 0)
    SetChrPos(0x14, 1030, 4000, -3700, 0)
    SetChrFlags(0xF0, 0x80)
    SetChrFlags(0xF1, 0x80)
    OP_6D(-950, 4000, -980, 0)
    OP_67(0, 5890, -10000, 0)
    OP_6B(1990, 0)
    OP_6C(314000, 0)
    OP_6E(388, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_DAE1():
        OP_6D(-1180, 4000, 2780, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_DAE1)

    def lambda_DAF9():
        OP_67(0, 5490, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_DAF9)

    def lambda_DB11():
        OP_6B(2210, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_DB11)

    def lambda_DB21():
        OP_6E(403, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_DB21)
    OP_8F(0x109, 0x0, 0xFA0, 0xFFFFFE16, 0x3E8, 0x0)
    WaitChrThread(0x10F, 0x0)
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x109, 19)
    SetChrSubChip(0x109, 0)
    OP_22(0x8F, 0x0, 0x64)
    Sleep(100)
    SetChrPos(0x10, 200, 5300, 0, 0)
    PlayEffect(0x1, 0x0, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)
    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    OP_E5(0x2, 0xFF, 0x13, 1000)
    OP_0D()
    Fade(1000)
    OP_E5(0x2, 0xFF, 0x13, 700)
    OP_0D()

    def lambda_DC0A():
        OP_8F(0xFE, 0xC8, 0x1770, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_DC0A)
    WaitChrThread(0x10, 0x0)
    Sleep(300)
    Fade(1000)
    OP_6D(0, 5000, 3260, 0)
    OP_67(0, 3980, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(0, 0)
    OP_6E(363, 0)
    SetChrPos(0x109, 0, 4000, -500, 0)
    SetChrPos(0x10F, -700, 4000, -3010, 0)
    SetChrPos(0x11, 1250, 4000, -3240, 0)
    SetChrPos(0x12, -100, 4000, -4900, 0)
    SetChrPos(0x13, -1280, 4000, -5010, 0)
    SetChrPos(0x14, 300, 4000, -3790, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrPos(0x10, 0, 6000, 1000, 0)

    def lambda_DCF2():
        OP_6D(0, 7500, 3760, 3500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_DCF2)

    def lambda_DD0A():
        OP_67(0, 1650, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DD0A)

    def lambda_DD22():
        OP_6B(2700, 3500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_DD22)

    def lambda_DD32():
        OP_6E(363, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_DD32)

    def lambda_DD42():
        OP_8F(0xFE, 0x0, 0x2134, 0xAF0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_DD42)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    def lambda_DD6C():
        OP_6B(2000, 8000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_DD6C)
    OP_22(0x147, 0x0, 0x64)
    PlayEffect(0x5, 0x2, 0x10, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    OP_23(0x147)
    Fade(500)
    OP_22(0xC, 0x0, 0x64)
    PlayEffect(0x3, 0x2, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x0)
    Sleep(300)
    PlayEffect(0x6, 0x3, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/U4203   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_39_D987 end

    def Function_40_DE58(): pass

    label("Function_40_DE58")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D2(0x27003D, 0x270042, 0x13)
    OP_D2(0x27051E, 0x27052B, 0x14)
    LoadEffect(0x3, "map\\mp253_04.eff")
    LoadEffect(0x4, "map\\mp253_03.eff")
    SetChrPos(0x109, 560, 4000, -1440, 0)
    SetChrPos(0x10F, -320, 4000, -2690, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x11, 2600, 4000, -2960, 0)
    SetChrPos(0x12, 2190, 4000, -4480, 0)
    SetChrPos(0x13, 550, 4000, -4510, 0)
    SetChrPos(0x14, 1370, 4000, -3090, 0)
    SetChrFlags(0xF0, 0x80)
    SetChrFlags(0xF1, 0x80)
    OP_6D(-2230, 5000, 4310, 0)
    OP_67(0, 3880, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(315000, 0)
    OP_6E(365, 0)
    ClearChrFlags(0x15, 0x80)
    OP_9F(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x15, 390, 8000, 2150, 180)
    SetChrFlags(0x15, 0x800)
    SetChrChipByIndex(0x15, 19)
    SetChrSubChip(0x15, 0)
    SetChrFlags(0x15, 0x4)
    PlayEffect(0x3, 0x0, 0x15, 0, 600, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    OP_E5(0x2, 0xFF, 0x13, 500)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_DFE6():
        OP_6D(-1210, 4000, 1510, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_DFE6)

    def lambda_DFFE():
        OP_67(0, 4850, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DFFE)

    def lambda_E016():
        OP_6B(3200, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_E016)

    def lambda_E026():
        OP_6E(327, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_E026)

    def lambda_E036():
        OP_8F(0xFE, 0x186, 0xFA0, 0x866, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_E036)
    WaitChrThread(0x15, 0x0)
    SetChrSubChip(0x15, 0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    Fade(1000)
    OP_82(0x2, 0x2)
    PlayEffect(0x3, 0x1, 0x15, 0, 600, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)

    def lambda_E0A2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x7D0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_E0A2)
    OP_22(0x99, 0x0, 0x64)
    OP_82(0x0, 0x0)
    OP_0D()
    Sleep(1000)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #395
        0x14,
        "#213F#6P啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #396
        0x11,
        "#560F#6P难、难道是……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #397
        0x13,
        (
            "#278F#6P嗯……\x01",
            "连他也被卷进来了吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #398
        0x12,
        (
            "#170F#6P也许该说……\x01",
            "是压轴角色登场吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #399
        0x10F,
        "#1803F#6P……果然，还是认识的人吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #400
        0x109,
        (
            "#1075F#5P哈哈，没错。\x02\x03",

            "#1840F用一个词来概括……\x01",
            "那就应该是『黑发王子』吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #401
        0x10F,
        "#1444F#6P？？？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    PlayEffect(0x4, 0x4, 0x15, 0, 600, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_22(0x138, 0x0, 0x64)
    OP_23(0x146)

    def lambda_E2ED():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_E2ED)
    OP_82(0x2, 0x2)
    WaitChrThread(0x15, 0x0)
    Fade(500)
    OP_82(0x1, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #402
        0x15,
        "#1503F#5P呜……\x02",
    )

    CloseMessageWindow()
    OP_9E(0x15, 0x14, 0x0, 0x12C, 0xBB8)

    def lambda_E344():
        OP_6D(-1210, 4000, 2510, 500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_E344)
    OP_22(0xA3, 0x0, 0x64)
    OP_22(0xD5, 0x0, 0x64)
    ClearChrFlags(0x15, 0x800)
    SetChrChipByIndex(0x15, 20)
    SetChrSubChip(0x15, 0)

    def lambda_E375():
        OP_96(0xFE, 0x186, 0xFA0, 0xD98, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_E375)
    WaitChrThread(0x15, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    ChrTalk(    #403
        0x15,
        (
            "#1506F#11P#3S艾丝蒂尔！\x01",
            "赶快卧倒──\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #404
        0x15,
        "#1504F#11P什……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #405
        0x14,
        "#415F#6P约、约修亚……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #406
        0x11,
        "#061F#6P约修亚哥哥！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #407
        0x15,
        (
            "#1504F#11P乔丝特……\x01",
            "还有提妲……\x02\x03",

            "#1503F……是做梦………\x01",
            "不，难道是带有某种攻击性的幻术……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #408
        0x109,
        (
            "#1075F#6P哈哈，能联想到这种地步，\x01",
            "不愧是约修亚啊。\x02\x03",

            "#1840F很遗憾……\x01",
            "这既不是梦也不是幻术。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #409
        0x15,
        (
            "#1504F#11P凯文先生……\x01",
            "还有尤莉亚小姐和穆拉少校……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x15, 7)
    SetChrSubChip(0x15, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #410
        0x15,
        (
            "#1502F#11P到底这是……\x01",
            "怎么一回事呢？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrPos(0x109, 270, 4000, -2029, 0)
    SetChrPos(0x10F, -870, 4000, -2950, 0)
    SetChrPos(0x11, 1900, 4000, -3200, 0)
    SetChrPos(0x12, 1410, 4000, -4720, 0)
    SetChrPos(0x13, -320, 4000, -4620, 0)
    SetChrPos(0x14, 650, 4000, -3400, 0)
    SetChrPos(0x15, 290, 4000, -190, 180)
    OP_6D(-1180, 4000, -360, 0)
    OP_67(0, 5660, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(315000, 0)
    OP_6E(381, 0)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #411
        0x15,
        "#1503F#11P……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #412
        0x109,
        (
            "#1840F#6P那个……\x02\x03",

            "果然只靠这样的说明\x01",
            "是很难接受的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #413
        0x15,
        (
            "#1505F#11P……不，正相反。\x02\x03",

            "#1500F虽然我考虑到了幻术的可能性，\x01",
            "但是那样就无法说明\x01",
            "这位小姐的存在了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #414
        0x10F,
        "#1444F#6P我……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #415
        0x15,
        (
            "#1505F#11P是的。\x02\x03",

            "#1500F请原谅我冒昧，\x01",
            "你应该是『骑士团』的人吧……？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #416
        0x10F,
        "#1440F#6P……你已经知道了吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #417
        0x15,
        (
            "#1513F#11P嗯，因为是凯文的同伴，\x01",
            "又是使用『法剑』作为武器。\x02\x03",

            "#1500F──我的名字是约修亚。\x01",
            "约修亚·布莱特。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #418
        0x10F,
        (
            "#1447F#6P……我是星杯随从骑士，\x01",
            "莉丝·亚尔珍特。\x02\x03",

            "#1448F看来你很熟悉\x01",
            "我们的世界呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #419
        0x14,
        (
            "#214F#6P等、等一下约修亚！\x02\x03",

            "为什么那个女人的存在\x01",
            "能够证明这不是幻觉呢？\x02\x03",

            "竟然置我于不顾！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #420
        0x15,
        (
            "#1504F#11P对了……\x01",
            "我还是第一次见到那个遮阳帽呢。\x02\x03",

            "#1501F看起来很适合你……\x01",
            "是之前所说的运输业的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #421
        0x14,
        (
            "#210F#6P啊，嗯，托你的福，\x01",
            "生意相当好呢。\x02\x03",

            "#413F……不对！\x02\x01",

            "#214F看到我就应该立刻明白\x01",
            "我就是本人了吧！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #422
        0x15,
        (
            "#1505F#11P如果是幻术的话，\x01",
            "登场的人物通常都是熟识的人。\x02\x03",

            "因为那是诱导和操作\x01",
            "施术对象的知识和想象的技术。\x02\x03",

            "#1500F但是，我和这位莉丝小姐\x01",
            "完全是第一次见面……\x02\x03",

            "并且她还有着\x01",
            "十分复杂的背景。\x02\x03",

            "有这样的一位人物存在，\x01",
            "我才能判断这是幻术的\x01",
            "可能性很低。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #423
        0x14,
        (
            "#413F#6P好、好像听明白了，\x01",
            "又有些听不明白……\x02\x03",

            "#212F……总之，\x01",
            "正是因为我们很熟，\x01",
            "所以反而证明不了对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #424
        0x15,
        (
            "#1504F#11P嗯，那个……\x01",
            "也可以这么说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #425
        0x14,
        "#415F#6P嘿嘿……那就好！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #426
        0x11,
        (
            "#067F#6P嘻嘻……\x02\x03",

            "#560F那个，约修亚哥哥。\x01",
            "真是很久不见了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #427
        0x15,
        (
            "#1501F#11P嗯，提妲也是，\x01",
            "身体健康比什么都好。\x02\x03",

            "大概有半年了吧……\x01",
            "好像稍微长高了点呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #428
        0x11,
        "#067F#6P嘿嘿……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #429
        0x15,
        (
            "#1512F#11P可是，\x01",
            "没想到连你也被卷了进来……\x02\x03",

            "#1514F这还真是让人大吃一惊呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #430
        0x11,
        (
            "#563F#6P啊，嗯……\x01",
            "我还是有点做梦的感觉呢。\x02\x03",

            "#064F啊，对了……\x01",
            "约修亚哥哥……\x02\x03",

            "#063F哎，那个……\x01",
            "艾丝蒂尔姐姐呢……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #431
        0x15,
        (
            "#1503F#11P……不知道。\x02\x03",

            "#1505F不过，可以肯定的是\x01",
            "她和我一起遇到了白光。\x02\x03",

            "#1502F所以被这个『影之国』\x01",
            "卷进来的可能性很高。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #432
        0x11,
        (
            "#561F#6P是、是吗……\x02\x03",

            "#064F对了，哥哥你们\x01",
            "现在旅行到什么地方了呢？\x02\x03",

            "你们最近写来的信里面说\x01",
            "正在埃雷波尼亚……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #433
        0x15,
        (
            "#1500F#11P嗯，\x01",
            "现在是在叫做克洛斯贝尔的地方。\x02\x03",

            "正好在帝国和共和国中间。\x01",
            "是个很小的自治州……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #434
        0x14,
        (
            "#213F#6P是真的吗！？\x02\x03",

            "我们的山猫号\x01",
            "当时也正好在\x01",
            "那一片空域飞行……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #435
        0x15,
        (
            "#1504F#11P真的吗？\x02\x03",

            "#1503F嗯……\x01",
            "是不是有什么关联呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #436
        0x13,
        (
            "#272F#6P唔，要勉强说的话，\x01",
            "就是与利贝尔的距离吧。\x02\x03",

            "#270F我们也是在离国境\x01",
            "最近的帕尔姆镇。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #437
        0x15,
        "#1500F#11P是这么一回事吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #438
        0x12,
        (
            "#176F#6P……凯文神父。\x02\x03",

            "#178F如果我们假设\x01",
            "这个事态是由某个\x01",
            "强大的古代遗物所引起的……\x02\x03",

            "那能不能影响到\x01",
            "如此广泛的范围呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #439
        0x109,
        (
            "#1065F#5P不……\x01",
            "我觉得那是不可能的。\x02\x03",

            "#1063F如果勉强说的话，\x01",
            "那就是『辉之环』引起的导力停止现象了。\x02\x03",

            "但那个也只影响到了\x01",
            "帝国南部而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #440
        0x12,
        (
            "#176F#6P原来如此……\x02\x03",

            "#175F这么一来，必须要有\x01",
            "与『七至宝』匹敌的力量才行。\x02\x03",

            "仔细想想，『辉之环』\x01",
            "不知道消失到哪里去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #441
        0x11,
        "#065F#6P难、难道说……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #442
        0x109,
        (
            "#1065F#5P……确实，\x01",
            "有这种可能性呢。\x02\x03",

            "#1063F但是，\x01",
            "只靠这一点，\x01",
            "无法说明的事情也太多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #443
        0x13,
        (
            "#270F#6P『敌人』……\x01",
            "还有异界化的王都吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #444
        0x10F,
        (
            "#1446F#5P……还有，恶魔的实体化\x01",
            "以及对属性影响的变化。\x02\x03",

            "#1443F在能够解释这些现象前，\x01",
            "还是不要着急下结论比较好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #445
        0x12,
        "#176F#6P嗯……的确。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #446
        0x15,
        (
            "#1505F#11P可是，这么一来……\x02\x03",

            "#1502F我们必须首先解决\x01",
            "王都异界化的谜团才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #447
        0x109,
        (
            "#1065F#6P嗯，你说的没错。\x02\x03",

            "#1063F艾丝蒂尔的事情\x01",
            "也很让人担心……\x01",
            "你也会来帮忙的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #448
        0x15,
        (
            "#1513F#11P……我一开始就是这么打算的。\x02\x03",

            "#1514F大家都被卷了进来，\x01",
            "我也不能置身事外……\x02\x03",

            "而且要找艾丝蒂尔的话，\x01",
            "和大家一起行动\x01",
            "应该是最好的选择。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #449
        0x11,
        "#560F#6P约修亚哥哥……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #450
        0x14,
        "#413F#6P呼……唉，没办法。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #451
        0x109,
        (
            "#1078F#6P好！\x01",
            "那就再次拜托了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #452
        0x10F,
        (
            "#1448F#6P……准备好了之后，\x01",
            "我们再去王都看看吧。\x02\x03",

            "约修亚被解放之后，\x01",
            "应该会发生什么变化才对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #453
        0x15,
        "#1500F#11P知道了。\x02",
    )

    CloseMessageWindow()

    def lambda_F6EE():
        OP_6B(2600, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_F6EE)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_A2(0x2714)
    OP_28(0x2D, 0x4, 0x4)
    OP_28(0x2D, 0x4, 0x8)
    OP_28(0x2D, 0x1, 0x1)
    OP_28(0x2D, 0x1, 0x2)
    OP_3F(0x356, 1)
    OP_DB(0x0, 0x1)
    OP_A2(0x25C7)
    Call(6, 11)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    ClearChrFlags(0xF0, 0x80)
    ClearChrFlags(0xF1, 0x80)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_DD(0x1, 0x0, 0x0, 16640, 0, 0, 0)
    FadeToDark(0, 0, -1)
    OP_C0(0x20, 0x1, 0x4100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
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

    # Function_40_DE58 end

    SaveToFile()

Try(main)
