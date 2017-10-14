from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'C0412   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0412.x',
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
        'Luke',                                 # 9
        'Pat',                                  # 10
        'Monster',                              # 11
        'Monster',                              # 12
        'Monster',                              # 13
        'Monster',                              # 14
        'Monster',                              # 15
        'Monster',                              # 16
        'Cassius',                              # 17
        'Cassius',                              # 18
        'Cassius',                              # 19
        'Cassius',                              # 20
        'Cassius',                              # 21
        '',                                     # 22
        '',                                     # 23
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
        'ED6_DT07/CH01160 ._CH',             # 00
        'ED6_DT07/CH01060 ._CH',             # 01
        'ED6_DT09/CH10020 ._CH',             # 02
        'ED6_DT09/CH10021 ._CH',             # 03
        'ED6_DT07/CH02000 ._CH',             # 04
        'ED6_DT07/CH00100 ._CH',             # 05
        'ED6_DT07/CH00101 ._CH',             # 06
        'ED6_DT07/CH00110 ._CH',             # 07
        'ED6_DT07/CH00111 ._CH',             # 08
        'ED6_DT07/CH00112 ._CH',             # 09
        'ED6_DT07/CH00102 ._CH',             # 0A
        'ED6_DT09/CH10160 ._CH',             # 0B
        'ED6_DT09/CH10161 ._CH',             # 0C
        'ED6_DT06/CH20031 ._CH',             # 0D
        'ED6_DT09/CH10070 ._CH',             # 0E
        'ED6_DT09/CH10071 ._CH',             # 0F
        'ED6_DT09/CH10040 ._CH',             # 10
        'ED6_DT09/CH10041 ._CH',             # 11
        'ED6_DT09/CH10150 ._CH',             # 12
        'ED6_DT09/CH10151 ._CH',             # 13
    )

    AddCharChipPat(
        'ED6_DT07/CH01160P._CP',             # 00
        'ED6_DT07/CH01060P._CP',             # 01
        'ED6_DT09/CH10020P._CP',             # 02
        'ED6_DT09/CH10021P._CP',             # 03
        'ED6_DT07/CH02000P._CP',             # 04
        'ED6_DT07/CH00100P._CP',             # 05
        'ED6_DT07/CH00101P._CP',             # 06
        'ED6_DT07/CH00110P._CP',             # 07
        'ED6_DT07/CH00111P._CP',             # 08
        'ED6_DT07/CH00112P._CP',             # 09
        'ED6_DT07/CH00102P._CP',             # 0A
        'ED6_DT09/CH10160P._CP',             # 0B
        'ED6_DT09/CH10161P._CP',             # 0C
        'ED6_DT06/CH20031P._CP',             # 0D
        'ED6_DT09/CH10070P._CP',             # 0E
        'ED6_DT09/CH10071P._CP',             # 0F
        'ED6_DT09/CH10040P._CP',             # 10
        'ED6_DT09/CH10041P._CP',             # 11
        'ED6_DT09/CH10150P._CP',             # 12
        'ED6_DT09/CH10151P._CP',             # 13
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 19000,
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
        X                   = 3000,
        Z                   = 0,
        Y                   = 19000,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -18100,
        Z                   = 0,
        Y                   = 110,
        Unknown_0C          = 180,
        Unknown_0E          = 14,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x31,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 18020,
        Z                   = 0,
        Y                   = 10,
        Unknown_0C          = 180,
        Unknown_0E          = 14,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x32,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    ScpFunction(
        "Function_0_322",          # 00, 0
        "Function_1_341",          # 01, 1
        "Function_2_342",          # 02, 2
        "Function_3_358",          # 03, 3
        "Function_4_2D40",         # 04, 4
        "Function_5_2D76",         # 05, 5
        "Function_6_2DBE",         # 06, 6
        "Function_7_2E1D",         # 07, 7
        "Function_8_2E7C",         # 08, 8
        "Function_9_2EDB",         # 09, 9
    )


    def Function_0_322(): pass

    label("Function_0_322")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_32E"),
        (SWITCH_DEFAULT, "loc_340"),
    )


    label("loc_32E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33D")
    OP_A2(0x217)
    Event(0, 3)

    label("loc_33D")

    Jump("loc_340")

    label("loc_340")

    Return()

    # Function_0_322 end

    def Function_1_341(): pass

    label("Function_1_341")

    Return()

    # Function_1_341 end

    def Function_2_342(): pass

    label("Function_2_342")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_357")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_342")

    label("loc_357")

    Return()

    # Function_2_342 end

    def Function_3_358(): pass

    label("Function_3_358")

    EventBegin(0x0)
    AddParty(0x3F, 0xFF)
    AddParty(0x40, 0xFF)
    SetChrFlags(0x140, 0x80)
    SetChrFlags(0x141, 0x80)
    FadeToBright(2000, 0)
    OP_6D(20, 500, 21100, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(335000, 0)
    OP_6E(275, 0)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrPos(0x101, -680, 250, 20560, 180)
    SetChrPos(0x102, 630, 250, 20650, 180)
    SetChrPos(0x8, -3860, 0, -3700, 45)
    SetChrPos(0x9, -2850, 0, -4300, 45)
    SetChrPos(0xA, -2830, 0, 1630, 180)
    SetChrPos(0xB, -2120, 0, 2880, 209)
    SetChrPos(0xC, -1510, 0, -250, 192)
    SetChrPos(0xD, 840, 0, 1810, 201)
    SetChrPos(0xE, 1750, 0, -1350, 180)
    TurnDirection(0xA, 0x8, 0)
    TurnDirection(0xB, 0x8, 0)
    TurnDirection(0xC, 0x8, 0)
    TurnDirection(0xD, 0x8, 0)
    TurnDirection(0xE, 0x8, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    OP_6E(262, 2500)
    OP_0D()

    NpcTalk(    #0
        0x8,
        "Luke's Voice",
        "#1SWh-What are we going to do?!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #1
        0x9,
        "Pat's Voice",
        "#1SS-Somebody, heeeeeelp!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Run full speed in the direction of the voice]\x01",      # 0
            "[Rush in simultaneously with Joshua]\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5CC"),
        (1, "loc_105E"),
        (SWITCH_DEFAULT, "loc_1A0A"),
    )


    label("loc_5CC")

    OP_28(0x1, 0x1, 0x10)

    ChrTalk(    #2
        0x101,
        "#005FOh no!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 5)
    Sleep(500)

    def lambda_5F3():
        OP_8E(0xFE, 0xFFFFFCE0, 0x0, 0xC12, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5F3)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #3
        0x102,
        (
            "#012FEstelle!\x02\x03",

            "#012FYou idiot...\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x102, 7)
    Sleep(500)

    def lambda_65A():
        OP_8E(0xFE, 0x442, 0x0, 0x2706, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_65A)
    OP_43(0xA, 0x3, 0x0, 0x2)
    Sleep(100)
    OP_43(0xB, 0x3, 0x0, 0x2)
    Sleep(200)

    def lambda_68D():
        OP_8E(0xFE, 0x442, 0x0, 0x2706, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_68D)
    OP_43(0xC, 0x3, 0x0, 0x2)
    Sleep(100)
    OP_43(0xD, 0x3, 0x0, 0x2)
    Sleep(200)
    OP_43(0xE, 0x3, 0x0, 0x2)
    Sleep(500)

    def lambda_6CC():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_6CC)

    def lambda_6DA():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_6DA)
    SetChrFlags(0x102, 0x80)
    OP_44(0x101, 0xFF)
    Fade(1000)
    OP_6D(-1550, 0, -920, 0)
    OP_67(0, 8670, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(336000, 0)
    OP_6E(306, 0)
    SetChrPos(0x101, 1090, 0, 9990, 66)

    def lambda_744():
        OP_6D(-3060, 0, -2370, 4000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_744)

    def lambda_75C():
        OP_94(0x0, 0xFE, 0x0, 0x834, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_75C)
    Sleep(100)

    def lambda_777():
        OP_94(0x0, 0xFE, 0x0, 0x7D0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_777)
    Sleep(100)

    def lambda_792():
        OP_94(0x0, 0xFE, 0x0, 0x7D0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_792)

    def lambda_7A8():
        OP_94(0x0, 0xFE, 0x0, 0x834, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_7A8)
    Sleep(100)

    def lambda_7C3():
        OP_94(0x0, 0xFE, 0x0, 0x578, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_7C3)
    Sleep(1000)
    OP_62(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    def lambda_7F0():
        OP_8F(0xFE, 0xFFFFEE8A, 0x0, 0xFFFFEE80, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7F0)
    Sleep(500)
    OP_62(0x9, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    def lambda_822():
        OP_8F(0xFE, 0xFFFFF29A, 0x0, 0xFFFFEAFC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_822)
    Sleep(1500)

    ChrTalk(    #4
        0x8,
        "#1PY-You monsters go somewhere else!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x9,
        (
            "Noooo! Shoo! Shoo!\x01",
            "Leave us alone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6 op#A op#5
        0x101,
        "#10AChew on this!\x05\x02",
    )

    Sleep(300)

    def lambda_8B0():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_8B0)

    def lambda_8BE():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_8BE)

    def lambda_8CC():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_8CC)

    def lambda_8DA():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_8DA)

    def lambda_8E8():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_8E8)

    def lambda_8F6():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_8F6)

    def lambda_904():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_904)
    Sleep(300)

    def lambda_917():
        OP_8E(0xFE, 0xFFFFFB6E, 0x0, 0x8F2, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_917)

    def lambda_932():
        OP_6D(-2220, 0, -1110, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_932)
    WaitChrThread(0x101, 0x1)

    def lambda_94F():

        label("loc_94F")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_94F")

    QueueWorkItem2(0xA, 2, lambda_94F)

    def lambda_960():

        label("loc_960")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_960")

    QueueWorkItem2(0xB, 2, lambda_960)

    def lambda_971():

        label("loc_971")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_971")

    QueueWorkItem2(0xC, 2, lambda_971)

    def lambda_982():

        label("loc_982")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_982")

    QueueWorkItem2(0xD, 2, lambda_982)

    def lambda_993():

        label("loc_993")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_993")

    QueueWorkItem2(0xE, 2, lambda_993)

    def lambda_9A4():

        label("loc_9A4")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_9A4")

    QueueWorkItem2(0x9, 2, lambda_9A4)

    def lambda_9B5():

        label("loc_9B5")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_9B5")

    QueueWorkItem2(0x8, 2, lambda_9B5)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 10)
    SetChrFlags(0x101, 0x1000)
    OP_22(0x1F4, 0x0, 0x64)

    def lambda_9E0():
        OP_99(0xFE, 0x0, 0xC, 0x9C4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9E0)
    OP_8C(0x101, 270, 0)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0x101, 0xFFFFF827, 0x0, 0xFFFFF8A8, 0x7D0, 0x1770)
    OP_22(0xA4, 0x0, 0x64)
    PlayEffect(0x8, 0xFF, 0xFF, -2630, 500, -1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_A4D():
        OP_8F(0xFE, 0xFFFFF006, 0x0, 0xFFFFF9DE, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_A4D)

    def lambda_A68():
        OP_94(0x1, 0xFE, 0xB4, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A68)

    def lambda_A7E():
        OP_94(0x1, 0xFE, 0xB4, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_A7E)
    Sleep(150)

    def lambda_A99():
        OP_94(0x1, 0xFE, 0xB4, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_A99)
    Sleep(100)

    def lambda_AB4():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_AB4)
    Sleep(200)

    def lambda_ACF():
        OP_94(0x1, 0xFE, 0xB4, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_ACF)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 5)

    def lambda_AF5():
        OP_8C(0xFE, 19, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AF5)

    def lambda_B03():
        OP_8F(0xFE, 0xFFFFF524, 0x0, 0xFFFFF420, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B03)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #7
        0x8,
        (
            "#1PEstelle?!\x01",
            "What are you doing here?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#005FGet back, you two!\x01",
            "These monsters aren't\x01",
            "playing around!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B92():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_B92)

    def lambda_BA0():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_BA0)

    def lambda_BAE():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_BAE)

    def lambda_BBC():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_BBC)

    def lambda_BCA():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_BCA)

    def lambda_BD8():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_BD8)

    def lambda_BE6():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_BE6)
    ClearChrFlags(0x102, 0x80)
    SetChrFlags(0x102, 0x1000)
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 7)
    TurnDirection(0x102, 0x101, 0)
    OP_96(0x102, 0xFFFFFE8E, 0x0, 0x898, 0x3E8, 0x1B58)
    OP_22(0xA4, 0x0, 0x64)
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 9)
    OP_99(0x102, 0x0, 0x5, 0x9C4)
    OP_22(0x1F5, 0x0, 0x64)

    def lambda_C4F():

        label("loc_C4F")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_C4F")

    QueueWorkItem2(0xA, 2, lambda_C4F)

    def lambda_C60():

        label("loc_C60")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_C60")

    QueueWorkItem2(0xB, 2, lambda_C60)

    def lambda_C71():

        label("loc_C71")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_C71")

    QueueWorkItem2(0xC, 2, lambda_C71)

    def lambda_C82():

        label("loc_C82")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_C82")

    QueueWorkItem2(0xD, 2, lambda_C82)

    def lambda_C93():

        label("loc_C93")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_C93")

    QueueWorkItem2(0xE, 2, lambda_C93)

    def lambda_CA4():

        label("loc_CA4")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_CA4")

    QueueWorkItem2(0x9, 2, lambda_CA4)

    def lambda_CB5():

        label("loc_CB5")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_CB5")

    QueueWorkItem2(0x8, 2, lambda_CB5)

    def lambda_CC6():
        OP_99(0xFE, 0x5, 0xC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CC6)

    def lambda_CD6():
        OP_8E(0xFE, 0xFFFFFFD8, 0x0, 0xFFFFFC72, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CD6)
    Sleep(100)

    def lambda_CF6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x4B0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_CF6)
    SetChrFlags(0x102, 0x40)
    PlayEffect(0x8, 0xFF, 0xFF, -10, 500, 690, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x102, 0x2)
    OP_44(0x102, 0xFF)
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 7)

    def lambda_D5B():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D5B)
    OP_96(0x102, 0xFFFFF876, 0x0, 0xFFFFF39E, 0x1F4, 0x1B58)
    OP_22(0xA4, 0x0, 0x64)

    ChrTalk(    #9
        0x9,
        "Joshua! You're here too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x102,
        (
            "#012F#2PEstelle...quit trying to be a\x01",
            "glory hog by diving in all by\x01",
            "yourself!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#006FLecture me later!\x02\x03",

            "Right now we need to take care\x01",
            "of these things!\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    Battle(0x386, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_E66"),
        (SWITCH_DEFAULT, "loc_E6B"),
    )


    label("loc_E66")

    OP_B4(0x0)
    Jump("loc_E6B")

    label("loc_E6B")

    SetChrFlags(0x140, 0x80)
    SetChrFlags(0x141, 0x80)
    EventBegin(0x0)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    OP_6D(-3150, 0, -3290, 0)
    OP_67(0, 7450, -10000, 0)
    OP_6B(1710, 0)
    OP_6E(554, 0)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    OP_8C(0x8, 28, 0)
    OP_8C(0x9, 28, 0)
    SetChrPos(0x101, -3210, 0, -460, 291)
    SetChrPos(0x102, -50, 0, -1270, 72)

    def lambda_F04():
        OP_6E(504, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F04)
    OP_6C(225000, 3000)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 65535)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #12
        0x101,
        "#502FAnd it's as easy as that!☆\x02",
    )

    CloseMessageWindow()
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 65535)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #13
        0x102,
        (
            "#017FThere was nothing 'easy' about\x01",
            "the mess you just got us into.\x02\x03",

            "What were you thinking rushing\x01",
            "in like that without assessing\x01",
            "the situation first...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#001FOh, don't get your boxers in\x01",
            "a bunch. Everything worked\x01",
            "out just fine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A0A")

    label("loc_105E")

    OP_28(0x1, 0x1, 0x8)
    OP_2B(0x1, 0x1)

    ChrTalk(    #15
        0x101,
        "#005FLet's go, Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        "#012FRight! I've got your back!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 5)
    Sleep(250)
    SetChrChipByIndex(0x102, 7)
    Sleep(250)

    def lambda_10C4():
        OP_8E(0xFE, 0xFFFFFCE0, 0x0, 0xC12, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10C4)
    Sleep(250)

    def lambda_10E4():
        OP_8E(0xFE, 0x442, 0x0, 0x2706, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10E4)
    OP_43(0xA, 0x3, 0x0, 0x2)
    Sleep(100)
    OP_43(0xB, 0x3, 0x0, 0x2)
    Sleep(200)

    def lambda_1117():
        OP_8E(0xFE, 0x442, 0x0, 0x2706, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1117)
    OP_43(0xC, 0x3, 0x0, 0x2)
    Sleep(100)
    OP_43(0xD, 0x3, 0x0, 0x2)
    Sleep(200)
    OP_43(0xE, 0x3, 0x0, 0x2)
    Sleep(500)

    def lambda_1156():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1156)

    def lambda_1164():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1164)
    SetChrFlags(0x102, 0x80)
    OP_44(0x101, 0xFF)
    Fade(1000)
    OP_6D(-1550, 0, -920, 0)
    OP_67(0, 8670, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(336000, 0)
    OP_6E(306, 0)
    SetChrPos(0x101, 1090, 0, 9990, 66)

    def lambda_11CE():
        OP_6D(-3060, 0, -2370, 4000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_11CE)

    def lambda_11E6():
        OP_94(0x0, 0xFE, 0x0, 0x834, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_11E6)
    Sleep(100)

    def lambda_1201():
        OP_94(0x0, 0xFE, 0x0, 0x7D0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1201)
    Sleep(100)

    def lambda_121C():
        OP_94(0x0, 0xFE, 0x0, 0x7D0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_121C)

    def lambda_1232():
        OP_94(0x0, 0xFE, 0x0, 0x834, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1232)
    Sleep(100)

    def lambda_124D():
        OP_94(0x0, 0xFE, 0x0, 0x578, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_124D)
    Sleep(1000)
    OP_62(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    def lambda_127A():
        OP_8F(0xFE, 0xFFFFEE8A, 0x0, 0xFFFFEE80, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_127A)
    Sleep(500)
    OP_62(0x9, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    def lambda_12AC():
        OP_8F(0xFE, 0xFFFFF29A, 0x0, 0xFFFFEAFC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_12AC)
    Sleep(1500)

    ChrTalk(    #17
        0x8,
        "#1PY-You monsters go somewhere else!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x9,
        (
            "Noooo! Shoo! Shoo!\x01",
            "Leave us alone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19 op#A op#5
        0x101,
        "#10AChew on this!\x05\x02",
    )

    Sleep(300)

    def lambda_133A():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_133A)

    def lambda_1348():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1348)

    def lambda_1356():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1356)

    def lambda_1364():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1364)

    def lambda_1372():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_1372)

    def lambda_1380():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1380)

    def lambda_138E():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_138E)
    Sleep(300)

    def lambda_13A1():
        OP_8E(0xFE, 0xFFFFFB6E, 0x0, 0x8F2, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13A1)

    def lambda_13BC():
        OP_6D(-2220, 0, -1110, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_13BC)
    WaitChrThread(0x101, 0x1)

    def lambda_13D9():

        label("loc_13D9")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_13D9")

    QueueWorkItem2(0xA, 2, lambda_13D9)

    def lambda_13EA():

        label("loc_13EA")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_13EA")

    QueueWorkItem2(0xB, 2, lambda_13EA)

    def lambda_13FB():

        label("loc_13FB")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_13FB")

    QueueWorkItem2(0xC, 2, lambda_13FB)

    def lambda_140C():

        label("loc_140C")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_140C")

    QueueWorkItem2(0xD, 2, lambda_140C)

    def lambda_141D():

        label("loc_141D")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_141D")

    QueueWorkItem2(0xE, 2, lambda_141D)

    def lambda_142E():

        label("loc_142E")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_142E")

    QueueWorkItem2(0x9, 2, lambda_142E)

    def lambda_143F():

        label("loc_143F")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_143F")

    QueueWorkItem2(0x8, 2, lambda_143F)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 10)
    SetChrFlags(0x101, 0x1000)
    OP_22(0x1F4, 0x0, 0x64)

    def lambda_146A():
        OP_99(0xFE, 0x0, 0xC, 0x9C4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_146A)
    OP_8C(0x101, 270, 0)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0x101, 0xFFFFF827, 0x0, 0xFFFFF8A8, 0x7D0, 0x1770)
    OP_22(0xA4, 0x0, 0x64)
    PlayEffect(0x8, 0xFF, 0xFF, -2630, 500, -1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_14D7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_14D7)

    def lambda_14E9():
        OP_8F(0xFE, 0xFFFFF006, 0x0, 0xFFFFF9DE, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_14E9)

    def lambda_1504():
        OP_94(0x1, 0xFE, 0xB4, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1504)

    def lambda_151A():
        OP_94(0x1, 0xFE, 0xB4, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_151A)
    Sleep(150)

    def lambda_1535():
        OP_94(0x1, 0xFE, 0xB4, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1535)
    Sleep(100)

    def lambda_1550():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1550)
    Sleep(200)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 5)

    def lambda_157B():
        OP_8C(0xFE, 19, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_157B)

    def lambda_1589():
        OP_8F(0xFE, 0xFFFFF524, 0x0, 0xFFFFF420, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1589)

    def lambda_15A4():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_15A4)

    def lambda_15B2():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_15B2)

    def lambda_15C0():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_15C0)

    def lambda_15CE():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_15CE)

    def lambda_15DC():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_15DC)

    def lambda_15EA():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_15EA)
    ClearChrFlags(0x102, 0x80)
    SetChrFlags(0x102, 0x1000)
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 7)
    TurnDirection(0x102, 0x101, 0)
    OP_96(0x102, 0xFFFFFE8E, 0x0, 0x898, 0x3E8, 0x1B58)
    OP_22(0xA4, 0x0, 0x64)
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 9)
    OP_99(0x102, 0x0, 0x5, 0x9C4)
    OP_22(0x1F5, 0x0, 0x64)

    def lambda_1653():

        label("loc_1653")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_1653")

    QueueWorkItem2(0xA, 2, lambda_1653)

    def lambda_1664():

        label("loc_1664")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_1664")

    QueueWorkItem2(0xB, 2, lambda_1664)

    def lambda_1675():

        label("loc_1675")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_1675")

    QueueWorkItem2(0xC, 2, lambda_1675)

    def lambda_1686():

        label("loc_1686")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_1686")

    QueueWorkItem2(0xD, 2, lambda_1686)

    def lambda_1697():

        label("loc_1697")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_1697")

    QueueWorkItem2(0xE, 2, lambda_1697)

    def lambda_16A8():

        label("loc_16A8")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_16A8")

    QueueWorkItem2(0x9, 2, lambda_16A8)

    def lambda_16B9():

        label("loc_16B9")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_16B9")

    QueueWorkItem2(0x8, 2, lambda_16B9)

    def lambda_16CA():
        OP_99(0xFE, 0x5, 0xC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_16CA)

    def lambda_16DA():
        OP_8E(0xFE, 0xFFFFFFD8, 0x0, 0xFFFFFC72, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_16DA)
    Sleep(100)

    def lambda_16FA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x4B0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_16FA)
    SetChrFlags(0x102, 0x40)
    PlayEffect(0x8, 0xFF, 0xFF, -10, 500, 690, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x102, 0x2)
    OP_44(0x102, 0xFF)
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 7)

    def lambda_175F():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_175F)
    OP_96(0x102, 0xFFFFF876, 0x0, 0xFFFFF39E, 0x1F4, 0x1B58)
    OP_22(0xA4, 0x0, 0x64)

    ChrTalk(    #20
        0x8,
        (
            "#1PEstelle?!\x01",
            "What are you doing here?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x9,
        "Joshua! You're here, too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#005FGet back, you two!\x01",
            "These monsters aren't\x01",
            "playing around!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x102,
        "#012F#2PWe'll take care of them!\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    Battle(0x3B0, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_1860"),
        (SWITCH_DEFAULT, "loc_1865"),
    )


    label("loc_1860")

    OP_B4(0x0)
    Jump("loc_1865")

    label("loc_1865")

    EventBegin(0x0)
    SetChrFlags(0x140, 0x80)
    SetChrFlags(0x141, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    OP_6D(-3150, 0, -3290, 0)
    OP_67(0, 7450, -10000, 0)
    OP_6B(1710, 0)
    OP_6E(554, 0)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    OP_8C(0x8, 28, 0)
    OP_8C(0x9, 28, 0)
    SetChrPos(0x101, -3210, 0, -460, 291)
    SetChrPos(0x102, -50, 0, -1270, 72)

    def lambda_18FE():
        OP_6E(504, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18FE)
    OP_6C(225000, 3000)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 65535)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #24
        0x101,
        "#001FIt looks like that's that.\x02",
    )

    CloseMessageWindow()
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 65535)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #25
        0x102,
        (
            "#019FYeah. I'm glad everyone's\x01",
            "safe, too.\x02\x03",

            "#010FBy the way, that was great\x01",
            "timing the way you blitzed\x01",
            "those monsters, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        "#008FYou really think so?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A0A")

    label("loc_1A0A")


    ChrTalk(    #27
        0x9,
        "Is it safe now...?\x02",
    )

    CloseMessageWindow()

    def lambda_1A28():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A28)

    def lambda_1A36():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1A36)

    ChrTalk(    #28
        0x8,
        (
            "Oh man!\x01",
            "That was awesome!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1A63():

        label("loc_1A63")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_1A63")

    QueueWorkItem2(0x8, 1, lambda_1A63)

    def lambda_1A74():

        label("loc_1A74")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_1A74")

    QueueWorkItem2(0x101, 1, lambda_1A74)

    def lambda_1A85():

        label("loc_1A85")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_1A85")

    QueueWorkItem2(0x102, 1, lambda_1A85)
    OP_62(0x8, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_95(0x8, 0x0, 0x0, 0x0, 0x2BC, 0x1770)
    OP_95(0x8, 0x0, 0x0, 0x0, 0x2BC, 0x1770)
    Sleep(300)

    def lambda_1ADB():
        OP_8E(0xFE, 0xFFFFF196, 0x0, 0xFFFFF9E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1ADB)
    Sleep(300)

    def lambda_1AFB():
        OP_6D(-3440, 0, -2740, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1AFB)
    Sleep(100)

    def lambda_1B18():

        label("loc_1B18")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_1B18")

    QueueWorkItem2(0x9, 1, lambda_1B18)

    def lambda_1B29():
        OP_8E(0xFE, 0xFFFFFC04, 0x0, 0xFFFFF39E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1B29)
    WaitChrThread(0x8, 0x2)
    OP_96(0x8, 0xFFFFEE6C, 0x0, 0xFFFFFBFA, 0x320, 0x1770)
    OP_96(0x8, 0xFFFFEF66, 0x0, 0xFFFFFF42, 0x4B0, 0x1770)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #29
        0x8,
        (
            "You really showed them,\x01",
            "Estelle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        "Not bad for a girl!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #31
        0x101,
        "#5P#005FYou little twerp!\x02",
    )

    CloseMessageWindow()

    def lambda_1BF6():
        OP_6D(-4540, 0, -1610, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1BF6)
    SetChrFlags(0x101, 0x40)
    OP_92(0x101, 0x8, 0x190, 0x1770, 0x0)
    OP_22(0x7D, 0x0, 0x64)
    OP_94(0x1, 0x8, 0xB4, 0x1F4, 0x1770, 0x0)
    Sleep(500)
    OP_8F(0x8, 0xFFFFE98A, 0x0, 0x14, 0x7D0, 0x0)

    ChrTalk(    #32
        0x8,
        (
            "Ow! That hurts!\x01",
            "What are you tryin'\x01",
            "to do to me?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#009FWhat's wrong with you?! \x02\x03",

            "You even dragged poor Pat all the\x01",
            "way up here against his will...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 1700, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1300)
    OP_62(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_44(0x8, 0xFF)

    def lambda_1D1D():
        OP_8C(0xFE, 270, 800)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1D1D)

    def lambda_1D2B():
        OP_94(0x1, 0xFE, 0xB4, 0x5DC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1D2B)
    ClearChrFlags(0x101, 0x1000)
    OP_8F(0x101, 0xFFFFE5B6, 0x0, 0x10E, 0x1388, 0x0)
    SetChrFlags(0x8, 0x4)
    OP_91(0x8, 0x0, 0x64, 0x0, 0x320, 0x0)

    def lambda_1D73():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D73)
    OP_97(0x8, 0xFFFFE5B6, 0x10E, 0xFFFD40E0, 0xFA0, 0x3)

    ChrTalk(    #34
        0x101,
        (
            "#005FIt's time to think about what you\x01",
            "did today!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1DCD():
        OP_91(0xFE, 0x4B0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1DCD)
    OP_91(0x8, 0x4B0, 0x0, 0x0, 0x7D0, 0x0)
    OP_9E(0x8, 0x3C, 0x0, 0x12C, 0x1F40)
    OP_9E(0x8, 0x3C, 0x0, 0x12C, 0x1F40)

    ChrTalk(    #35
        0x8,
        "Ow! You're hurting me! Stop it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x8,
        (
            "I said stop it,\x01",
            "you violent she-devil!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        (
            "#009FSo this is the thanks I get\x01",
            "for saving your neck, huh?\x02\x03",

            "#009FLooks like it's time to give you\x01",
            "some of my SPECIAL discipline!\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x8, 0x3C, 0x0, 0x1F4, 0x1F40)

    ChrTalk(    #38
        0x8,
        "Owowowowow!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        (
            "All right, Estelle, I'm sorry!\x01",
            "Everything was all my fault!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1F5F():

        label("loc_1F5F")

        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        OP_48()
        Jump("loc_1F5F")

    QueueWorkItem2(0x8, 3, lambda_1F5F)

    ChrTalk(    #40
        0x9,
        "#1PU-Umm...Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x9,
        (
            "#1PShouldn't we forgive each other\x01",
            "like they teach at school?\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xA, 11)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -16000, 0, 0, 282)

    def lambda_1FE9():
        OP_8E(0xFE, 0xFFFFD508, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1FE9)

    ChrTalk(    #42
        0x101,
        (
            "#006FThis brat doesn't need forgiveness,\x01",
            "but a little discipline should do\x01",
            "the trick!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xA, 0x1)
    TurnDirection(0xA, 0x101, 400)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    ClearChrFlags(0x101, 0x1000)

    ChrTalk(    #43
        0x102,
        "#016FEstelle, behind you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        (
            "#004F...It's something with teeth,\x01",
            "isn't it?\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x8, 0xFF)
    OP_44(0x101, 0xFF)
    ClearChrFlags(0x8, 0x4)
    TurnDirection(0x101, 0xA, 400)
    TurnDirection(0x8, 0x101, 400)

    def lambda_20F8():
        OP_6D(-6670, 0, -1080, 2000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_20F8)

    def lambda_2110():
        OP_8E(0xFE, 0xFFFFDAE4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2110)
    Sleep(1500)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #45
        0x101,
        "#002FUh...nice monster?\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x0, "battle\\\\mgblood.eff")

    ChrTalk(    #46
        0x102,
        "#510F#1P(I'm not going to make it in time...)\x02",
    )

    CloseMessageWindow()
    OP_43(0x102, 0x0, 0x0, 0x4)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x14, 0x4)
    SetChrFlags(0x10, 0x4)
    SetChrPos(0x11, -21000, 0, 0, 0)
    SetChrPos(0x12, -21040, 0, 0, 0)
    SetChrPos(0x13, -21040, 0, 0, 0)
    SetChrPos(0x14, -21040, 0, 0, 0)
    SetChrPos(0x10, -21040, 0, 0, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x14, 0x40)
    SetChrFlags(0x10, 0x40)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0xC8, 0x0)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x96, 0x0)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x64, 0x0)
    OP_9F(0x14, 0xFF, 0xFF, 0xFF, 0x32, 0x0)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 12)

    def lambda_228F():
        OP_8E(0xA, 0xFFFFEA84, 0x0, 0x0, 0xA8C, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_228F)

    def lambda_22AA():
        OP_6D(-5130, 0, -1080, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_22AA)

    def lambda_22C2():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_22C2)

    def lambda_22D8():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_22D8)
    SetChrFlags(0x10, 0x2)
    SetChrFlags(0x11, 0x2)
    SetChrFlags(0x12, 0x2)
    SetChrFlags(0x13, 0x2)
    SetChrFlags(0x14, 0x2)
    SetChrSubChip(0x10, 0)
    SetChrSubChip(0x11, 0)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x13, 0)
    SetChrSubChip(0x14, 0)
    SetChrFlags(0x10, 0x20)
    SetChrFlags(0x11, 0x20)
    SetChrFlags(0x12, 0x20)
    SetChrFlags(0x13, 0x20)
    SetChrFlags(0x14, 0x20)
    SetChrChipByIndex(0x10, 13)
    SetChrChipByIndex(0x11, 13)
    SetChrChipByIndex(0x12, 13)
    SetChrChipByIndex(0x13, 13)
    SetChrChipByIndex(0x14, 13)

    def lambda_2352():
        OP_8E(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2352)
    Sleep(100)

    def lambda_2372():
        OP_8E(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2372)
    Sleep(100)

    def lambda_2392():
        OP_8E(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2392)
    Sleep(100)

    def lambda_23B2():
        OP_8E(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_23B2)
    Sleep(100)

    def lambda_23D2():
        OP_8E(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_23D2)
    OP_20(0x3E8)
    WaitChrThread(0x10, 0x1)
    OP_43(0x11, 0x1, 0x0, 0x6)
    OP_43(0x12, 0x1, 0x0, 0x7)
    OP_43(0x13, 0x1, 0x0, 0x8)
    OP_43(0x14, 0x1, 0x0, 0x9)
    SetChrSubChip(0x10, 1)
    OP_96(0x10, 0xFFFFE1EC, 0x0, 0x5DC, 0x4B0, 0x2710)
    OP_22(0xA4, 0x0, 0x64)
    OP_43(0x10, 0x1, 0x0, 0x5)
    WaitChrThread(0xA, 0x1)
    OP_22(0x9B, 0x0, 0x64)
    PlayEffect(0x8, 0xFF, 0xFF, -5500, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x9, 0xFF, 0xFF, -5500, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, -5500, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xA, 0x40)

    def lambda_24F3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_24F3)
    Sleep(1000)

    ChrTalk(    #47
        0x101,
        "#6P#004FHuh...?\x02",
    )

    CloseMessageWindow()
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 65535)
    TurnDirection(0x102, 0x10, 400)
    Sleep(500)

    ChrTalk(    #48
        0x102,
        "#010FDad, you came!\x02",
    )

    CloseMessageWindow()

    def lambda_2554():
        OP_6C(270000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2554)

    def lambda_2564():
        OP_6D(-5500, 0, 0, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2564)
    Sleep(1300)
    SetChrSubChip(0x10, 4)
    Sleep(1200)

    def lambda_258B():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_258B)

    def lambda_2599():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2599)

    def lambda_25A7():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_25A7)
    OP_1D(0x58)
    Sleep(500)

    ChrTalk(    #49
        0x10,
        (
            "#085FYou still lack skill and\x01",
            "understanding, Estelle.\x02\x03",

            "You must always prepare for unseen\x01",
            "danger by sharpening your senses.\x02\x03",

            "#080FThat's part of what it means\x01",
            "to be a bracer.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2670():

        label("loc_2670")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_2670")

    QueueWorkItem2(0x101, 1, lambda_2670)

    ChrTalk(    #50
        0x101,
        (
            "#004F#4PD-Dad?!\x02\x03",

            "Wh-What are you doing here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x10,
        (
            "#080FI just happened to be in town and\x01",
            "heard the whole story from Aina.\x02\x03",

            "I'll give you points for your quick\x01",
            "thinking and taking action to\x01",
            "come after the children...\x02\x03",

            "But, you failed to follow through\x01",
            "completely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        (
            "#007F#4PI really messed up,\x01",
            "didn't I?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_27B8():
        OP_6D(-6270, 0, 130, 2000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_27B8)

    def lambda_27D0():

        label("loc_27D0")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_27D0")

    QueueWorkItem2(0x8, 1, lambda_27D0)

    def lambda_27E1():
        OP_8F(0xFE, 0xFFFFEED0, 0x0, 0x5FA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_27E1)

    def lambda_27FC():

        label("loc_27FC")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_27FC")

    QueueWorkItem2(0x9, 1, lambda_27FC)

    def lambda_280D():
        OP_8F(0xFE, 0xFFFFF5E2, 0x0, 0xFFFFF9C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_280D)
    OP_8E(0x102, 0xFFFFED90, 0x0, 0xFFFFFD12, 0xBB8, 0x0)
    OP_44(0x102, 0xFF)
    OP_8C(0x102, 315, 400)
    WaitChrThread(0x8, 0x2)

    ChrTalk(    #53
        0x102,
        (
            "#013FIt's a good thing you showed up\x01",
            "when you did.\x02\x03",

            "I'm sorry. I should have been\x01",
            "watching her back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10,
        (
            "#081FThat just means that you have\x01",
            "room for improvement.\x02\x03",

            "Constantly working to overcome\x01",
            "your weak spots is the key.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x102,
        "#011FUnderstood...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x10,
        (
            "#080FSo how about we head home,\x01",
            "everyone?\x02\x03",

            "Can you boys walk?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x9,
        "I-I think so...\x02",
    )

    CloseMessageWindow()

    def lambda_29A0():
        OP_8E(0xFE, 0xFFFFE9BC, 0x0, 0xFFFFF948, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_29A0)
    Sleep(200)

    def lambda_29C0():
        OP_8E(0xFE, 0xFFFFE476, 0x0, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_29C0)

    def lambda_29DB():

        label("loc_29DB")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_29DB")

    QueueWorkItem2(0x8, 1, lambda_29DB)
    WaitChrThread(0x9, 0x1)

    def lambda_29F1():
        OP_8E(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFFBE6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_29F1)

    def lambda_2A0C():

        label("loc_2A0C")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_2A0C")

    QueueWorkItem2(0x9, 1, lambda_2A0C)
    WaitChrThread(0x9, 0x2)
    WaitChrThread(0x8, 0x2)

    ChrTalk(    #58
        0x8,
        (
            "That was...incredible,\x01",
            "Mr. Bright!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x8,
        (
            "You were like a gazillion times\x01",
            "more awesome than Estelle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x10,
        (
            "#081FHa ha ha, of course I was!\x01",
            "I'm her father!\x02\x03",

            "All right everyone,\x01",
            "let's file on out of here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x8,
        (
            "I'm with you,\x01",
            "Mr. Bright!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0)
    ClearChrFlags(0x10, 0x2)
    ClearChrFlags(0x10, 0x20)
    SetChrChipByIndex(0x10, 4)
    OP_8C(0x10, 90, 0)
    OP_8C(0x10, 270, 400)

    def lambda_2B35():
        OP_8E(0xFE, 0xFFFF6D2A, 0x0, 0xFFFFFF88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2B35)
    Sleep(300)

    def lambda_2B55():
        OP_8E(0xFE, 0xFFFF6D2A, 0x0, 0xFFFFFF88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2B55)
    Sleep(100)

    def lambda_2B75():
        OP_8E(0xFE, 0xFFFF6D2A, 0x0, 0xFFFFFF88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2B75)

    def lambda_2B90():
        OP_6E(471, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B90)

    def lambda_2BA0():
        OP_6C(224000, 3000)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2BA0)
    OP_6D(-6000, 0, 290, 2500)
    OP_63(0x101)
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #62
        0x101,
        (
            "#007F#6PWho's the glory hog now...?\x02\x03",

            "I mean, I guess I should be\x01",
            "thankful that Dad saved my\x01",
            "behind...\x02\x03",

            "But why does he have to go and\x01",
            "take all the credit like that?!\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_8C(0x101, 45, 400)
    Sleep(500)

    ChrTalk(    #63
        0x101,
        "#009F#4S#6PIt really chaps my hide!\x02",
    )

    CloseMessageWindow()
    OP_44(0x102, 0xFF)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #64
        0x102,
        (
            "#019FHa ha. That's just the way he is.\x02\x03",

            "#010FAfter all, he is Cassius Bright.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_28(0x1, 0x1, 0x20)
    RemoveParty(0x3F, 0xFF)
    RemoveParty(0x40, 0xFF)
    OP_A2(0x217)
    NewScene("ED6_DT01/T0121   ._SN", 1, 0, 0)
    IdleLoop()
    Return()

    # Function_3_358 end

    def Function_4_2D40(): pass

    label("Function_4_2D40")

    ClearChrFlags(0x102, 0x1000)
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 7)
    Sleep(500)

    def lambda_2D60():
        OP_8E(0xFE, 0xFFFFF600, 0x0, 0xFFFFFC54, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2D60)
    Return()

    # Function_4_2D40 end

    def Function_5_2D76(): pass

    label("Function_5_2D76")

    OP_96(0xFE, 0xFFFFE7C8, 0x0, 0x96, 0x3E8, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    SetChrSubChip(0xFE, 2)
    Sleep(500)
    OP_96(0xFE, 0xFFFFE1EC, 0x0, 0x0, 0x1F4, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    SetChrSubChip(0xFE, 3)
    Return()

    # Function_5_2D76 end

    def Function_6_2DBE(): pass

    label("Function_6_2DBE")

    Sleep(100)
    SetChrSubChip(0xFE, 1)
    OP_96(0xFE, 0xFFFFE1EC, 0x0, 0x5DC, 0x4B0, 0x2710)
    OP_96(0xFE, 0xFFFFE7C8, 0x0, 0x96, 0x3E8, 0x1388)
    SetChrSubChip(0xFE, 2)
    Sleep(500)
    OP_96(0xFE, 0xFFFFE1EC, 0x0, 0x0, 0x1F4, 0x1388)
    SetChrFlags(0x11, 0x80)
    Return()

    # Function_6_2DBE end

    def Function_7_2E1D(): pass

    label("Function_7_2E1D")

    Sleep(200)
    SetChrSubChip(0xFE, 1)
    OP_96(0xFE, 0xFFFFE1EC, 0x0, 0x5DC, 0x4B0, 0x2710)
    OP_96(0xFE, 0xFFFFE7C8, 0x0, 0x96, 0x3E8, 0x1388)
    SetChrSubChip(0xFE, 2)
    Sleep(500)
    OP_96(0xFE, 0xFFFFE1EC, 0x0, 0x0, 0x1F4, 0x1388)
    SetChrFlags(0x12, 0x80)
    Return()

    # Function_7_2E1D end

    def Function_8_2E7C(): pass

    label("Function_8_2E7C")

    Sleep(300)
    SetChrSubChip(0xFE, 1)
    OP_96(0xFE, 0xFFFFE1EC, 0x0, 0x5DC, 0x4B0, 0x2710)
    OP_96(0xFE, 0xFFFFE7C8, 0x0, 0x96, 0x3E8, 0x1388)
    SetChrSubChip(0xFE, 2)
    Sleep(500)
    OP_96(0xFE, 0xFFFFE1EC, 0x0, 0x0, 0x1F4, 0x1388)
    SetChrFlags(0x13, 0x80)
    Return()

    # Function_8_2E7C end

    def Function_9_2EDB(): pass

    label("Function_9_2EDB")

    Sleep(400)
    SetChrSubChip(0xFE, 1)
    OP_96(0xFE, 0xFFFFE1EC, 0x0, 0x5DC, 0x4B0, 0x2710)
    OP_96(0xFE, 0xFFFFE7C8, 0x0, 0x96, 0x3E8, 0x1388)
    SetChrSubChip(0xFE, 2)
    Sleep(500)
    OP_96(0xFE, 0xFFFFE1EC, 0x0, 0x0, 0x1F4, 0x1388)
    SetChrFlags(0x14, 0x80)
    Return()

    # Function_9_2EDB end

    SaveToFile()

Try(main)
