from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Wisp',                                 # 9
        'Wisp',                                 # 10
        'Wisp',                                 # 11
        'Wisp',                                 # 12
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
        "Function_3_9D9",          # 03, 3
        "Function_4_A2F",          # 04, 4
        "Function_5_A85",          # 05, 5
        "Function_6_ADB",          # 06, 6
        "Function_7_B31",          # 07, 7
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
            "#1079F#6PIf I remember rightly, this was the warehouse\x01",
            "that tank was hidden in.\x02\x03",

            "This is my first time seeing the inside, though.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_477")

    ChrTalk(    #1
        0x10E,
        (
            "#176F#6PIt's currently being rented out by a new\x01",
            "owner, as far as I'm aware.\x02\x03",

            "#170FNaturally, they've been given a thorough\x01",
            "background checking this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x109,
        (
            "#1060F#5POh, right. Probably for the best after what\x01",
            "went down before.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A6")

    label("loc_477")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5A6")

    ChrTalk(    #3
        0x107,
        (
            "#063F#6PI'm amazed they managed to keep it hidden here\x01",
            "for so long...\x02\x03",

            "Doing maintenance on it without drawing attention\x01",
            "must've been really difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x109,
        (
            "#1066F#5PWell, the woman leading their little group and\x01",
            "her men seemed REALLY dedicated. Folks like\x01",
            "that would've found a way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A6")

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
        "#1441F#5PKevin!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x109,
        "#1063F#6P...!\x02",
    )

    CloseMessageWindow()
    OP_1D(0x97)

    def lambda_611():
        OP_6D(-2100, 0, 7530, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_611)

    def lambda_629():
        OP_67(0, 5110, -10000, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_629)

    def lambda_641():
        OP_6B(2670, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_641)

    def lambda_651():
        OP_6E(364, 1500)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_651)
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
        "#1069F#6PWhat a mess... Now we're up against GHOSTS?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_749")

    ChrTalk(    #8
        0x10D,
        "#271F#6PThey're going to attack!\x02",
    )

    CloseMessageWindow()
    Jump("loc_76C")

    label("loc_749")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_76C")

    ChrTalk(    #9
        0x107,
        "#065F#6POh, no!\x02",
    )

    CloseMessageWindow()

    label("loc_76C")

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)

    def lambda_780():
        OP_6D(-1970, 0, 5880, 300)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_780)

    def lambda_798():
        OP_67(0, 4830, -10000, 300)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_798)

    def lambda_7B0():
        OP_6B(2130, 300)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_7B0)

    def lambda_7C0():
        OP_6E(329, 300)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_7C0)

    def lambda_7D0():

        label("loc_7D0")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_7D0")

    QueueWorkItem2(0x10, 3, lambda_7D0)

    def lambda_7E3():
        OP_8F(0xFE, 0xFFFFFC54, 0x1F4, 0xDE8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7E3)
    Sleep(20)

    def lambda_803():

        label("loc_803")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_803")

    QueueWorkItem2(0x11, 3, lambda_803)

    def lambda_816():
        OP_8F(0xFE, 0xFFFFFFB0, 0x1F4, 0xECE, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_816)
    Sleep(10)

    def lambda_836():

        label("loc_836")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_836")

    QueueWorkItem2(0x12, 3, lambda_836)

    def lambda_849():
        OP_8F(0xFE, 0xFFFFF916, 0x1F4, 0x1220, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_849)
    Sleep(20)

    def lambda_869():

        label("loc_869")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_869")

    QueueWorkItem2(0x13, 3, lambda_869)

    def lambda_87C():
        OP_8F(0xFE, 0x78, 0x1F4, 0x1022, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_87C)
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

    def Function_3_9D9(): pass

    label("Function_3_9D9")

    SetChrPos(0xFE, -1180, 500, 8070, 180)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_A00():

        label("loc_A00")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_A00")

    QueueWorkItem2(0xFE, 3, lambda_A00)
    OP_22(0x99, 0x0, 0x64)
    Sleep(200)

    def lambda_A1D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A1D)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_3_9D9 end

    def Function_4_A2F(): pass

    label("Function_4_A2F")

    SetChrPos(0xFE, 500, 500, 8430, 180)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_A56():

        label("loc_A56")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_A56")

    QueueWorkItem2(0xFE, 3, lambda_A56)
    OP_22(0x99, 0x0, 0x64)
    Sleep(200)

    def lambda_A73():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A73)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_4_A2F end

    def Function_5_A85(): pass

    label("Function_5_A85")

    SetChrPos(0xFE, -2980, 500, 9390, 180)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_AAC():

        label("loc_AAC")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_AAC")

    QueueWorkItem2(0xFE, 3, lambda_AAC)
    OP_22(0x99, 0x0, 0x64)
    Sleep(200)

    def lambda_AC9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AC9)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_5_A85 end

    def Function_6_ADB(): pass

    label("Function_6_ADB")

    SetChrPos(0xFE, 1240, 500, 9950, 180)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_B02():

        label("loc_B02")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_B02")

    QueueWorkItem2(0xFE, 3, lambda_B02)
    OP_22(0x99, 0x0, 0x64)
    Sleep(200)

    def lambda_B1F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B1F)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_6_ADB end

    def Function_7_B31(): pass

    label("Function_7_B31")

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
        "\x07\x05Found \x1F\x29\x03\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x329, 1)
    Sleep(500)

    ChrTalk(    #11
        0x10F,
        "#1444F#6PCould that be the key to the airship?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)

    def lambda_CBB():
        OP_6D(-1440, 0, 6750, 1200)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_CBB)
    OP_8C(0x109, 180, 400)
    WaitChrThread(0xEE, 0x0)

    ChrTalk(    #12
        0x109,
        (
            "#1065F#2PCan't think of anything else it'd be good for.\x02\x03",

            "#1063FWhat's it doing here, though?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E0A")

    ChrTalk(    #13
        0x10E,
        (
            "#176F#6PSolve one mystery and find two more right\x01",
            "around the corner...\x02\x03",

            "#170FStill, at least now we should be able to get\x01",
            "inside that ship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x109,
        "#1060F#2PYeah. Let's make our way back.\x02",
    )

    CloseMessageWindow()
    Jump("loc_EAA")

    label("loc_E0A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EAA")

    ChrTalk(    #15
        0x107,
        (
            "#560F#6PI haven't got a clue...\x02\x03",

            "Still, at least now we should be able to get\x01",
            "inside that ship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x109,
        "#1060F#2PYeah. Let's make our way back.\x02",
    )

    CloseMessageWindow()

    label("loc_EAA")

    OP_A2(0x270C)
    OP_28(0x2C, 0x1, 0x10)
    OP_64(0x0, 0x1)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_7_B31 end

    SaveToFile()

Try(main)
