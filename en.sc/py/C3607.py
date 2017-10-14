from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3607   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3607.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60033",
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
        'Walter',                               # 9
        'Kilika',                               # 10
        'Gospel',                               # 11
        '',                                     # 12
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT27/CH03500 ._CH',             # 00
        'ED6_DT07/CH02610 ._CH',             # 01
        'ED6_DT06/CH20021 ._CH',             # 02
        'ED6_DT26/CH20242 ._CH',             # 03
        'ED6_DT26/CH20280 ._CH',             # 04
        'ED6_DT29/CH12140 ._CH',             # 05
        'ED6_DT29/CH12141 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT27/CH03500P._CP',             # 00
        'ED6_DT07/CH02610P._CP',             # 01
        'ED6_DT06/CH20021P._CP',             # 02
        'ED6_DT26/CH20242P._CP',             # 03
        'ED6_DT26/CH20280P._CP',             # 04
        'ED6_DT29/CH12140P._CP',             # 05
        'ED6_DT29/CH12141P._CP',             # 06
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 458754,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 9600,
        Z                   = 250,
        Y                   = 1400,
        Unknown_0C          = 270,
        Unknown_0E          = 5,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F5,
        Unknown_18          = 8448,
        Unknown_1A          = 0,
    )


    ScpFunction(
        "Function_0_15E",          # 00, 0
        "Function_1_195",          # 01, 1
        "Function_2_23A",          # 02, 2
        "Function_3_105B",         # 03, 3
        "Function_4_108B",         # 04, 4
        "Function_5_10BB",         # 05, 5
        "Function_6_10EB",         # 06, 6
        "Function_7_1171",         # 07, 7
    )


    def Function_0_15E(): pass

    label("Function_0_15E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16C")
    OP_B5(0x0)

    label("loc_16C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x420, 0)), scpexpr(EXPR_END)), "loc_178")
    SetChrFlags(0xB, 0x80)

    label("loc_178")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_194")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_194")

    Return()

    # Function_0_15E end

    def Function_1_195(): pass

    label("Function_1_195")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E3")
    OP_72(0x8, 0x4)
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_79(0x0, 0x2)
    OP_79(0x1, 0x2)
    OP_79(0x2, 0x2)
    OP_79(0x3, 0x2)
    OP_79(0x4, 0x2)
    OP_7B()
    Jump("loc_21D")

    label("loc_1E3")

    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_79(0x0, 0x2)
    OP_79(0x1, 0x2)
    OP_79(0x2, 0x2)
    OP_79(0x3, 0x2)
    OP_79(0x4, 0x2)
    OP_7B()

    label("loc_21D")

    OP_51(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_239")
    OP_22(0x1C3, 0x0, 0x64)

    label("loc_239")

    Return()

    # Function_1_195 end

    def Function_2_23A(): pass

    label("Function_2_23A")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_251")
    Call(0, 6)
    Call(0, 7)

    label("loc_251")

    OP_6D(34920, 250, 12030, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3960, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_22(0x1C3, 0x0, 0x64)
    SetChrPos(0x8, -2540, 250, 9040, 90)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 4)
    SetChrSubChip(0x8, 0)
    SetChrPos(0x9, 40, 0, 6000, 90)
    ClearChrFlags(0x9, 0x80)
    OP_82(0x80, 0x0)
    OP_82(0x82, 0x0)
    SetChrPos(0x108, 2730, 250, 8740, 90)
    SetChrPos(0x101, 200, 0, 2110, 90)
    SetChrPos(0x102, 1000, 0, 1470, 90)
    SetChrPos(0xF9, -800, 0, 1110, 90)
    OP_72(0x7, 0x4)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_79(0x0, 0x2)
    OP_79(0x1, 0x2)
    OP_79(0x2, 0x2)
    OP_79(0x3, 0x2)
    OP_79(0x4, 0x2)
    OP_7B()

    def lambda_34C():
        OP_6D(1840, 0, 7670, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_34C)

    def lambda_364():
        OP_67(0, 5560, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_364)

    def lambda_37C():
        OP_6B(4800, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_37C)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    WaitChrThread(0x101, 0x0)
    Sleep(500)

    ChrTalk(    #0
        0x8,
        "#252FHeh. Job's done, then.\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x20)
    TurnDirection(0x8, 0x9, 400)
    ClearChrFlags(0x8, 0x20)

    def lambda_3D7():

        label("loc_3D7")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3D7")

    QueueWorkItem2(0x9, 1, lambda_3D7)
    Sleep(50)

    def lambda_3ED():

        label("loc_3ED")

        OP_8C(0xFE, 225, 400)
        OP_48()
        Jump("loc_3ED")

    QueueWorkItem2(0x108, 1, lambda_3ED)
    Sleep(50)

    def lambda_403():

        label("loc_403")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_403")

    QueueWorkItem2(0x101, 1, lambda_403)
    Sleep(50)

    def lambda_419():

        label("loc_419")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_419")

    QueueWorkItem2(0x102, 1, lambda_419)
    Sleep(50)

    def lambda_42F():

        label("loc_42F")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_42F")

    QueueWorkItem2(0xF9, 1, lambda_42F)
    Sleep(400)
    Fade(500)
    OP_6D(210, 0, 8800, 0)
    OP_67(0, 4650, -10000, 0)
    OP_6B(2880, 0)
    OP_6C(0, 0)
    OP_6E(315, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #1
        0x8,
        (
            "#251FKilika. Despite everything, I'm glad I\x01",
            "got to see you again before the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x9,
        (
            "#794F#2PI am half glad and half despairing.\x02\x03",

            "#792FI doubt we'll ever meet again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "#257FYeah. The rest is between me and\x01",
            "the big guy right over there\x02\x03",

            "#251FYou can't even be a little sweet at a\x01",
            "time like this, though?\x02\x03",

            "Cold as ice, right up to the very end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x9,
        "#791F#2PAs I recall, that's what you fell for.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        "#253FHeh. Suppose I did.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x8, 0x4)
    OP_7D(0x0, 0x8, 0x32, 0x1F4)
    SetChrChipByIndex(0x8, 3)
    SetChrSubChip(0x8, 1)
    Sleep(300)
    OP_22(0x23B, 0x0, 0x64)
    SetChrSubChip(0x8, 2)

    def lambda_676():
        OP_96(0xFE, 0x820, 0x3B6, 0x3246, 0x5DC, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_676)
    WaitChrThread(0x8, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrSubChip(0x8, 1)
    Sleep(50)
    OP_22(0x23B, 0x0, 0x64)
    SetChrSubChip(0x8, 2)

    def lambda_6B2():
        OP_96(0xFE, 0x31B0, 0xFA, 0x334A, 0x3E8, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6B2)
    SetChrSubChip(0x8, 1)
    Fade(500)
    OP_6D(15140, 250, 15230, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(33000, 0)
    OP_6E(277, 0)
    WaitChrThread(0x8, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    WaitChrThread(0x102, 0x3)
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x8, 4)
    SetChrSubChip(0x8, 0)
    Sleep(500)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0xF9, 0x1)
    OP_44(0x108, 0x1)
    OP_44(0x9, 0x1)

    ChrTalk(    #6
        0x108,
        "#073F#2PYou two...\x02",
    )

    CloseMessageWindow()

    def lambda_773():
        OP_6D(13250, 250, 13830, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_773)

    def lambda_78B():
        OP_67(0, 6960, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_78B)
    OP_8E(0x108, 0x5E6, 0x0, 0x259E, 0x1770, 0x0)
    OP_8E(0x108, 0x2396, 0xFA, 0x3228, 0x1770, 0x0)
    TurnDirection(0x108, 0x8, 400)
    Sleep(500)
    OP_44(0x8, 0x1)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #7
        0x8,
        (
            "#250F#4PZin.\x02\x03",

            "If you want to know the reason me\x01",
            "and the old man fought to the death...\x02\x03",

            "Make me lose.\x02\x03",

            "Use that Living Fist he left you and\x01",
            "beat me.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 3)
    SetChrSubChip(0x8, 1)
    Sleep(300)
    OP_22(0x23B, 0x0, 0x64)
    SetChrSubChip(0x8, 2)
    ClearChrFlags(0x8, 0x1)

    def lambda_898():
        OP_6D(14850, 250, 15000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_898)

    def lambda_8B0():
        OP_67(0, 6450, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8B0)

    def lambda_8C8():
        OP_96(0xFE, 0x36E2, 0x514, 0x33F4, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8C8)
    SetChrSubChip(0x8, 1)
    WaitChrThread(0x8, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x8, 4)
    SetChrSubChip(0x8, 0)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x8, 270, 400)
    WaitChrThread(0x8, 0x0)
    Sleep(500)
    OP_7D(0x0, 0x8, 0x32, 0x1F4)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    SetChrChipByIndex(0x8, 3)
    SetChrSubChip(0x8, 1)
    Sleep(300)
    OP_22(0x23B, 0x0, 0x64)
    SetChrSubChip(0x8, 0)

    def lambda_949():
        OP_6B(2800, 500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_949)

    def lambda_959():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_959)

    def lambda_96B():
        OP_96(0xFE, 0x40CE, 0xFFFFEC78, 0x3700, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_96B)
    Sleep(500)
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0x8, 0x1)
    SetChrFlags(0x8, 0x80)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)

    ChrTalk(    #8
        0x108,
        "#077F#5PWha--?!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    SetMapFlags(0x10)
    OP_6D(1580, 0, 5260, 0)
    OP_67(0, 3900, -10000, 0)
    OP_6B(2670, 0)
    OP_6C(21000, 0)
    OP_6E(303, 0)
    OP_0D()

    ChrTalk(    #9
        0x101,
        "#1020F#5PWh-Whoooa!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(12720, 250, 13130, 0)
    OP_67(0, 6250, -10000, 0)
    OP_6B(3330, 0)
    OP_6C(45000, 0)
    OP_6E(301, 0)

    def lambda_A7F():
        OP_6D(15810, 250, 13140, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A7F)

    def lambda_A97():
        OP_67(0, 5700, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_A97)

    def lambda_AAF():
        OP_6B(3000, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_AAF)

    def lambda_ABF():
        OP_8E(0xFE, 0x3426, 0xFA, 0x316A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_ABF)
    OP_43(0x101, 0x1, 0x0, 0x3)
    Sleep(500)
    OP_43(0x102, 0x1, 0x0, 0x4)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0x5)
    WaitChrThread(0x108, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(500)

    ChrTalk(    #10
        0x108,
        "#572F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#1020F#5PWhoa, whoa, hang ON!\x02\x03",

            "Can an Enforcer jump from\x01",
            "this height and, like, not DIE?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x102,
        (
            "#1035F#2PNot all of them can, no.\x02\x03",

            "#1042FBut an expert like him...\x01",
            "I wouldn't be surprised if he's fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x108,
        (
            "#074F#5PHe used the wall to slow his descent.\x02\x03",

            "#072FWhat incredible strength...\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x9, 2760, 250, 10680, 90)
    OP_E5(0x9, 0x0, 0x0)

    ChrTalk(    #14
        0x9,
        "#2PHmph. Such a pest.\x02",
    )

    CloseMessageWindow()

    def lambda_C6B():
        OP_6D(13910, 250, 12760, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C6B)

    def lambda_C83():
        OP_67(0, 6000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_C83)

    def lambda_C9B():
        OP_8E(0xFE, 0x27CE, 0xFA, 0x2CA6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_C9B)

    def lambda_CB6():

        label("loc_CB6")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_CB6")

    QueueWorkItem2(0x101, 1, lambda_CB6)
    Sleep(50)

    def lambda_CCC():

        label("loc_CCC")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_CCC")

    QueueWorkItem2(0x108, 1, lambda_CCC)
    Sleep(50)

    def lambda_CE2():

        label("loc_CE2")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_CE2")

    QueueWorkItem2(0x102, 1, lambda_CE2)
    Sleep(50)

    def lambda_CF8():

        label("loc_CF8")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_CF8")

    QueueWorkItem2(0xF9, 1, lambda_CF8)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0x101, 0x2)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0x108, 0x1)
    OP_44(0xF9, 0x1)

    ChrTalk(    #15
        0x108,
        (
            "#072F#4PKilika...\x02\x03",

            "How did you know Walter\x01",
            "would be here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x9,
        (
            "#794F#5PYou thought I didn't know?\x02\x03",

            "#792FFirst Walter, then you...\x02\x03",

            "#791FTell me, why ARE men sometimes\x01",
            "so simple?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x108,
        "#075F#4PUh... Well...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #18
        0x101,
        "#1019F#6PHmmmmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x102,
        (
            "#1048F#2P...I repent all of my sins and beg\x01",
            "forgiveness. Please, just stop staring\x01",
            "at me.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E90")

    ChrTalk(    #20
        0x103,
        "#027F#5PHahaha!\x02",
    )

    CloseMessageWindow()

    label("loc_E90")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EB3")

    ChrTalk(    #21
        0x107,
        "#061F#5PHeehee!\x02",
    )

    CloseMessageWindow()

    label("loc_EB3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ED6")

    ChrTalk(    #22
        0x105,
        "#048F#5PHaha...\x02",
    )

    CloseMessageWindow()

    label("loc_ED6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F2A")

    ChrTalk(    #23
        0x106,
        (
            "#051F#5PHeh... Yeah, I think that one might\x01",
            "apply to me as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F2A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F66")

    ChrTalk(    #24
        0x109,
        "#1068F#5PWelp, she's sure got us pegged.\x02",
    )

    CloseMessageWindow()

    label("loc_F66")


    ChrTalk(    #25
        0x9,
        (
            "#792F#5PWith my personal business out\x01",
            "of the way, I will return to Zeiss.\x02\x03",

            "#791FGood luck, everyone.\x01",
            "Take care at the other towers.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FF5():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FF5)
    Sleep(300)

    ChrTalk(    #26
        0x101,
        "#1025F#4PKilika...thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x108,
        "#070F#4PYeah, we will.\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_21()
    OP_A2(0x10F3)
    NewScene("ED6_DT21/E0311   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_2_23A end

    def Function_3_105B(): pass

    label("Function_3_105B")

    OP_8E(0xFE, 0x92E, 0xFA, 0x1FC2, 0x1388, 0x0)
    OP_8E(0xFE, 0x3674, 0xFA, 0x2CCE, 0x1388, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_3_105B end

    def Function_4_108B(): pass

    label("Function_4_108B")

    OP_8E(0xFE, 0x92E, 0xFA, 0x1FC2, 0x1388, 0x0)
    OP_8E(0xFE, 0x35C0, 0xFA, 0x27E2, 0x1388, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_4_108B end

    def Function_5_10BB(): pass

    label("Function_5_10BB")

    OP_8E(0xFE, 0x92E, 0xFA, 0x1FC2, 0x1388, 0x0)
    OP_8E(0xFE, 0x3124, 0xFA, 0x2B70, 0x1388, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_5_10BB end

    def Function_6_10EB(): pass

    label("Function_6_10EB")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1164"),
        (1, "loc_116A"),
        (SWITCH_DEFAULT, "loc_1170"),
    )


    label("loc_1164")

    OP_A2(0x1200)
    Jump("loc_1170")

    label("loc_116A")

    OP_A2(0x1201)
    Jump("loc_1170")

    label("loc_1170")

    Return()

    # Function_6_10EB end

    def Function_7_1171(): pass

    label("Function_7_1171")

    FadeToDark(0, 0, -1)
    OP_6D(-66940, 250, 36210, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3700, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0x7, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_7_1171 end

    SaveToFile()

Try(main)
