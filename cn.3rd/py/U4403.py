from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U4403   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U4403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60221",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '鬼炎',                                 # 9
        '鬼炎',                                 # 10
        '鬼炎',                                 # 11
        '鬼炎',                                 # 12
        '',                                     # 13
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


    AddCharChip(
        'ED6_DT29/CH14790 ._CH',             # 00
        'ED6_DT27/CH03084 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT29/CH14790P._CP',             # 00
        'ED6_DT27/CH03084P._CP',             # 01
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -100,
        TriggerZ            = 0,
        TriggerY            = 7900,
        TriggerRange        = 1000,
        ActorX              = -100,
        ActorZ              = 300,
        ActorY              = 7900,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_15E",          # 00, 0
        "Function_1_174",          # 01, 1
        "Function_2_1EE",          # 02, 2
        "Function_3_8F7",          # 03, 3
        "Function_4_94D",          # 04, 4
        "Function_5_9A3",          # 05, 5
        "Function_6_9F9",          # 06, 6
        "Function_7_A4F",          # 07, 7
    )


    def Function_0_15E(): pass

    label("Function_0_15E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_173")
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_173")

    Return()

    # Function_0_15E end

    def Function_1_174(): pass

    label("Function_1_174")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E4, 1)), scpexpr(EXPR_END)), "loc_187")
    OP_B1("U4403_y")
    Jump("loc_190")

    label("loc_187")

    OP_B1("U4403_n")

    label("loc_190")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 4)), scpexpr(EXPR_END)), "loc_19E")
    OP_64(0x0, 0x1)
    Jump("loc_1ED")

    label("loc_19E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 3)), scpexpr(EXPR_END)), "loc_1ED")
    LoadEffect(0x0, "map\\mp257_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -100, 300, 7900, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    label("loc_1ED")

    Return()

    # Function_1_174 end

    def Function_2_1EE(): pass

    label("Function_2_1EE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(238, 0x42, 0x2)
    OP_E0(239, 0x43, 0x2)
    OP_E0(240, 0x44, 0x2)
    OP_E0(241, 0x45, 0x2)
    SetChrPos(0x109, 90, 0, 2660, 0)
    SetChrPos(0x10F, -1450, 0, 2730, 0)
    SetChrPos(0xF0, 410, 0, 1110, 0)
    SetChrPos(0xF1, -1480, 0, 1320, 0)
    OP_6D(-890, 2950, 16120, 0)
    OP_67(0, 5620, -10000, 0)
    OP_6B(3020, 0)
    OP_6C(315000, 0)
    OP_6E(355, 0)

    def lambda_295():
        OP_6D(-1730, 0, 3570, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_295)

    def lambda_2AD():
        OP_67(0, 6240, -10000, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_2AD)

    def lambda_2C5():
        OP_6B(2300, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_2C5)

    def lambda_2D5():
        OP_6E(334, 5000)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_2D5)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    ChrTalk(    #0
        0x109,
        (
            "#1079F#6P这里……\x01",
            "是那个战车隐藏过的仓库吧。\x02\x03",

            "唔，\x01",
            "里面已经变成这个样子了啊。\x02",
        )
    )

    Jump("loc_359")

    label("loc_359")

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_409")

    ChrTalk(    #1
        0x10E,
        (
            "#176F#6P现在这边的仓库\x01",
            "由其他人在使用。\x02\x03",

            "#170F当然，\x01",
            "他们的身份都进行了严格的检查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x109,
        (
            "#1060F#5P原来如此。\x01",
            "嗯，这也是理所当然的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B7")

    label("loc_409")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B7")

    ChrTalk(    #3
        0x107,
        (
            "#063F#6P那东西还真能\x01",
            "一直藏在这里面啊。\x02\x03",

            "我觉得光是维护\x01",
            "就很辛苦了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x109,
        (
            "#1066F#5P不过，\x01",
            "包括那个女军官在内，\x01",
            "都是些顽固的家伙呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B7")

    OP_20(0x7D0)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 3)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #5
        0x10F,
        "#1441F#5P凯文……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x109,
        "#1063F#6P呜！\x02",
    )

    CloseMessageWindow()
    OP_1D(0x97)

    def lambda_534():
        OP_6D(-2100, 0, 7530, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_534)

    def lambda_54C():
        OP_67(0, 5110, -10000, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_54C)

    def lambda_564():
        OP_6B(2670, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_564)

    def lambda_574():
        OP_6E(364, 1500)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_574)
    WaitChrThread(0xEE, 0x0)
    OP_22(0x32E, 0x0, 0x64)
    OP_43(0x10, 0x0, 0x0, 0x3)
    Sleep(100)
    OP_43(0x11, 0x0, 0x0, 0x4)
    Sleep(100)
    OP_43(0x12, 0x0, 0x0, 0x5)
    Sleep(100)
    OP_43(0x13, 0x0, 0x0, 0x6)
    WaitChrThread(0x13, 0x0)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 2)
    SetChrSubChip(0x109, 0)
    Sleep(100)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 4)
    SetChrSubChip(0xF0, 0)
    Sleep(100)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 5)
    SetChrSubChip(0xF1, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #7
        0x109,
        (
            "#1069F#6P嘁……\x01",
            "是实体化的亡灵！？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_65B")

    ChrTalk(    #8
        0x10D,
        "#271F#6P要来了……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_68A")

    label("loc_65B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_68A")

    ChrTalk(    #9
        0x107,
        "#065F#6P啊哇哇……！\x02",
    )

    CloseMessageWindow()

    label("loc_68A")

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)

    def lambda_69E():
        OP_6D(-1970, 0, 5880, 300)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_69E)

    def lambda_6B6():
        OP_67(0, 4830, -10000, 300)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_6B6)

    def lambda_6CE():
        OP_6B(2130, 300)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_6CE)

    def lambda_6DE():
        OP_6E(329, 300)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_6DE)

    def lambda_6EE():

        label("loc_6EE")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_6EE")

    QueueWorkItem2(0x10, 3, lambda_6EE)

    def lambda_701():
        OP_8F(0xFE, 0xFFFFFC54, 0x1F4, 0xDE8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_701)
    Sleep(20)

    def lambda_721():

        label("loc_721")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_721")

    QueueWorkItem2(0x11, 3, lambda_721)

    def lambda_734():
        OP_8F(0xFE, 0xFFFFFFB0, 0x1F4, 0xECE, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_734)
    Sleep(10)

    def lambda_754():

        label("loc_754")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_754")

    QueueWorkItem2(0x12, 3, lambda_754)

    def lambda_767():
        OP_8F(0xFE, 0xFFFFF916, 0x1F4, 0x1220, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_767)
    Sleep(20)

    def lambda_787():

        label("loc_787")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_787")

    QueueWorkItem2(0x13, 3, lambda_787)

    def lambda_79A():
        OP_8F(0xFE, 0x78, 0x1F4, 0x1022, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_79A)
    WaitChrThread(0xEE, 0x0)
    Battle(0xF2, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-1700, 0, 7510, 0)
    OP_67(0, 6130, -10000, 0)
    OP_6B(2400, 0)
    OP_6C(315000, 0)
    OP_6E(340, 0)
    OP_44(0x10, 0x1)
    OP_44(0x11, 0x1)
    OP_44(0x12, 0x1)
    OP_44(0x13, 0x1)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrPos(0x109, -90, 0, 5130, 0)
    SetChrPos(0x10F, -1410, 0, 5000, 0)
    SetChrPos(0xF0, 470, 0, 3450, 0)
    SetChrPos(0xF1, -1320, 0, 3450, 0)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    LoadEffect(0x0, "map\\mp257_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -100, 300, 7900, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_A2(0x270B)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    EventEnd(0x0)
    Return()

    # Function_2_1EE end

    def Function_3_8F7(): pass

    label("Function_3_8F7")

    SetChrPos(0xFE, -1180, 500, 8070, 180)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_91E():

        label("loc_91E")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_91E")

    QueueWorkItem2(0xFE, 3, lambda_91E)
    OP_22(0x99, 0x0, 0x64)
    Sleep(200)

    def lambda_93B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_93B)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_3_8F7 end

    def Function_4_94D(): pass

    label("Function_4_94D")

    SetChrPos(0xFE, 500, 500, 8430, 180)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_974():

        label("loc_974")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_974")

    QueueWorkItem2(0xFE, 3, lambda_974)
    OP_22(0x99, 0x0, 0x64)
    Sleep(200)

    def lambda_991():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_991)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_4_94D end

    def Function_5_9A3(): pass

    label("Function_5_9A3")

    SetChrPos(0xFE, -2980, 500, 9390, 180)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_9CA():

        label("loc_9CA")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_9CA")

    QueueWorkItem2(0xFE, 3, lambda_9CA)
    OP_22(0x99, 0x0, 0x64)
    Sleep(200)

    def lambda_9E7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9E7)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_5_9A3 end

    def Function_6_9F9(): pass

    label("Function_6_9F9")

    SetChrPos(0xFE, 1240, 500, 9950, 180)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_A20():

        label("loc_A20")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_A20")

    QueueWorkItem2(0xFE, 3, lambda_A20)
    OP_22(0x99, 0x0, 0x64)
    Sleep(200)

    def lambda_A3D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A3D)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_6_9F9 end

    def Function_7_A4F(): pass

    label("Function_7_A4F")

    EventBegin(0x0)
    Fade(500)
    SetChrPos(0x109, -340, 0, 6840, 0)
    SetChrPos(0x10F, -600, 0, 5420, 0)
    SetChrPos(0xF0, -1040, 0, 3950, 0)
    SetChrPos(0xF1, 380, 0, 4010, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_6D(-1260, 0, 8050, 0)
    OP_67(0, 5800, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(315000, 0)
    OP_6E(322, 0)
    OP_0D()
    Sleep(500)
    OP_8E(0x109, 0xFFFFFEE8, 0x0, 0x1BF8, 0x1F4, 0x0)
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x109, 1)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)
    OP_82(0x0, 0x2)
    Sleep(500)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x00得到了\x1F\x29\x03\x07\x00。\x02",
    )

    Jump("loc_B6C")

    label("loc_B6C")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x329, 1)
    Sleep(500)

    ChrTalk(    #11
        0x10F,
        (
            "#1444F#6P这是……\x01",
            "刚才的那架飞艇的？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)

    def lambda_BDC():
        OP_6D(-1440, 0, 6750, 1200)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_BDC)
    OP_8C(0x109, 180, 400)
    WaitChrThread(0xEE, 0x0)

    ChrTalk(    #12
        0x109,
        (
            "#1065F#2P看起来好像是……\x02\x03",

            "#1063F可是，\x01",
            "为什么会落在这个地方呢？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CF2")

    ChrTalk(    #13
        0x10E,
        (
            "#176F#6P到处都是无法理解的事情呢……\x02\x03",

            "#170F不过这样我们就能\x01",
            "进到那架飞艇里面了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x109,
        (
            "#1060F#2P嗯……\x01",
            "我们这就去看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D95")

    label("loc_CF2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D95")

    ChrTalk(    #15
        0x107,
        (
            "#560F#6P到、到处都是\x01",
            "无法理解的事情……\x02\x03",

            "不过，现在应该\x01",
            "可以进到那架飞艇里面了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x109,
        (
            "#1060F#2P是啊。\x01",
            "我们这就去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D95")

    OP_A2(0x270C)
    OP_28(0x2C, 0x1, 0x10)
    OP_64(0x0, 0x1)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_7_A4F end

    SaveToFile()

Try(main)
