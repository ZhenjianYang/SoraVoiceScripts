from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C1402   ._SN',
        MapName             = 'Bose',
        Location            = 'C1402.x',
        MapIndex            = 60,
        MapDefaultBGM       = "ed60089",
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
        '',                                     # 9
        'Private Gutte',                        # 10
        'Private Rakel',                        # 11
        'Guard Captain',                        # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
        '',                                     # 18
        '',                                     # 19
        '',                                     # 20
        '',                                     # 21
        '',                                     # 22
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
        'ED6_DT09/CH11170 ._CH',             # 00
        'ED6_DT09/CH11171 ._CH',             # 01
        'ED6_DT09/CH11180 ._CH',             # 02
        'ED6_DT09/CH11181 ._CH',             # 03
        'ED6_DT09/CH11190 ._CH',             # 04
        'ED6_DT09/CH11191 ._CH',             # 05
        'ED6_DT09/CH10170 ._CH',             # 06
        'ED6_DT09/CH10171 ._CH',             # 07
        'ED6_DT09/CH10840 ._CH',             # 08
        'ED6_DT09/CH10841 ._CH',             # 09
        'ED6_DT07/CH01640 ._CH',             # 0A
        'ED6_DT07/CH01600 ._CH',             # 0B
        'ED6_DT07/CH00322 ._CH',             # 0C
        'ED6_DT07/CH00324 ._CH',             # 0D
        'ED6_DT27/CH03010 ._CH',             # 0E
        'ED6_DT06/CH20043 ._CH',             # 0F
        'ED6_DT07/CH01640 ._CH',             # 10
        'ED6_DT26/CH20327 ._CH',             # 11
        'ED6_DT26/CH20310 ._CH',             # 12
    )

    AddCharChipPat(
        'ED6_DT09/CH11170P._CP',             # 00
        'ED6_DT09/CH11171P._CP',             # 01
        'ED6_DT09/CH11180P._CP',             # 02
        'ED6_DT09/CH11181P._CP',             # 03
        'ED6_DT09/CH11190P._CP',             # 04
        'ED6_DT09/CH11191P._CP',             # 05
        'ED6_DT09/CH10170P._CP',             # 06
        'ED6_DT09/CH10171P._CP',             # 07
        'ED6_DT09/CH10840P._CP',             # 08
        'ED6_DT09/CH10841P._CP',             # 09
        'ED6_DT07/CH01640P._CP',             # 0A
        'ED6_DT07/CH01600P._CP',             # 0B
        'ED6_DT07/CH00322P._CP',             # 0C
        'ED6_DT07/CH00324P._CP',             # 0D
        'ED6_DT27/CH03010P._CP',             # 0E
        'ED6_DT06/CH20043P._CP',             # 0F
        'ED6_DT07/CH01640P._CP',             # 10
        'ED6_DT26/CH20327P._CP',             # 11
        'ED6_DT26/CH20310P._CP',             # 12
    )

    DeclNpc(
        X                   = 19810,
        Z                   = 0,
        Y                   = 166800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -31230,
        Z                   = -30,
        Y                   = 76720,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -22600,
        Z                   = 0,
        Y                   = 45730,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -1980,
        Z                   = 40,
        Y                   = 82660,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 8330,
        Z                   = -1840,
        Y                   = 91320,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 2350,
        Z                   = -1960,
        Y                   = 58080,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -31080,
        Z                   = -1990,
        Y                   = 103160,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 5530,
        Z                   = -1920,
        Y                   = 140390,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 10740,
        Z                   = -2009,
        Y                   = 162000,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 10420,
        Z                   = -1910,
        Y                   = 77510,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -21780,
        Z                   = -2050,
        Y                   = 78280,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 30,
        Y                   = -2100,
        Z                   = 179370,
        Range               = 4750,
        Unknown_10          = 0xFFFFFBB4,
        Unknown_14          = 0x2C31C,
        Unknown_18          = 0x0,
        Unknown_1C          = 8,
    )


    DeclActor(
        TriggerX            = 19360,
        TriggerZ            = -1990,
        TriggerY            = 166110,
        TriggerRange        = 1000,
        ActorX              = 19810,
        ActorZ              = -490,
        ActorY              = 166800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_31E",          # 00, 0
        "Function_1_3BB",          # 01, 1
        "Function_2_405",          # 02, 2
        "Function_3_582",          # 03, 3
        "Function_4_7D9",          # 04, 4
        "Function_5_916",          # 05, 5
        "Function_6_1E4A",         # 06, 6
        "Function_7_1E93",         # 07, 7
        "Function_8_1EC8",         # 08, 8
    )


    def Function_0_31E(): pass

    label("Function_0_31E")

    OP_11(0x30, 0x78, 0xC8, 0x61A8, 0x109A0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x300, 0)), scpexpr(EXPR_END)), "loc_387")
    OP_4A(0xA, 255)
    SetChrPos(0xA, 4880, -1940, 187950, 180)
    SetChrChipByIndex(0xA, 15)
    ClearChrFlags(0xA, 0x40)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x1)
    OP_4A(0x9, 255)
    SetChrPos(0x9, 470, -1910, 187800, 45)
    SetChrChipByIndex(0x9, 15)
    ClearChrFlags(0x9, 0x1)
    ClearChrFlags(0x9, 0x40)
    ClearChrFlags(0x9, 0x80)

    label("loc_387")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_3A3")
    OP_20(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 4)
    Jump("loc_3BA")

    label("loc_3A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_3BA")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F1)
    Event(0, 5)

    label("loc_3BA")

    Return()

    # Function_0_31E end

    def Function_1_3BB(): pass

    label("Function_1_3BB")

    OP_51(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x362, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E3")
    OP_6F(0x2, 0)
    Jump("loc_3EA")

    label("loc_3E3")

    OP_6F(0x2, 60)

    label("loc_3EA")

    OP_71(0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_404")
    OP_20(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_404")

    Return()

    # Function_1_3BB end

    def Function_2_405(): pass

    label("Function_2_405")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42A")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_56C")

    label("loc_42A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_443")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_56C")

    label("loc_443")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45C")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_56C")

    label("loc_45C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_475")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_56C")

    label("loc_475")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48E")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_56C")

    label("loc_48E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A7")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_56C")

    label("loc_4A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C0")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_56C")

    label("loc_4C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D9")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_56C")

    label("loc_4D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F2")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_56C")

    label("loc_4F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50B")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_56C")

    label("loc_50B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_524")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_56C")

    label("loc_524")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53D")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_56C")

    label("loc_53D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_556")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_56C")

    label("loc_556")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56C")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_56C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_581")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_56C")

    label("loc_581")

    Return()

    # Function_2_405 end

    def Function_3_582(): pass

    label("Function_3_582")

    OP_EA(0x2, 0x2, 0x2, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x362, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x362, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66C")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_5D9():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5D9)

    def lambda_5F4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_5F4)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #0
        "\x07\x05Monsters appeared!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0xBA, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_647"),
        (2, "loc_659"),
        (1, "loc_669"),
        (SWITCH_DEFAULT, "loc_66C"),
    )


    label("loc_647")

    OP_A2(0x1B17)
    OP_6F(0x2, 60)
    Sleep(500)
    Jump("loc_66C")

    label("loc_659")

    OP_6F(0x2, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_669")

    OP_B4(0x0)
    Return()

    label("loc_66C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2A2, 1)"), scpexpr(EXPR_END)), "loc_6B8")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #1
        "Found \x1F\xA2\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B16)
    Jump("loc_71A")

    label("loc_6B8")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #2
        (
            "Found \x1F\xA2\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xA2\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_71A")

    Jump("loc_7CB")

    label("loc_71D")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #3
        (
            "\x07\x05You open the chest and see riches beyond your\x01",
            "wildest imagination. As you take your first step\x01",
            "in your victory dance, you awaken. It was a dream.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7CB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_582 end

    def Function_4_7D9(): pass

    label("Function_4_7D9")

    EventBegin(0x0)
    SetChrPos(0x9, 780, -1950, 187800, 177)
    SetChrPos(0xA, 4330, -1940, 187800, 177)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-9890, 2120, 60910, 0)
    OP_67(0, 9310, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(36000, 0)
    OP_6E(564, 0)
    OP_C8(0x200, 0x46, "C_PLAC13._CH", 0x1, 0x3E8)
    FadeToBright(1000, 0)

    def lambda_87C():
        OP_6D(1860, -30, 185090, 13000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_87C)
    Sleep(2000)
    Sleep(2000)
    Sleep(2000)
    Sleep(2000)

    def lambda_8A8():
        OP_67(0, 6570, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_8A8)

    def lambda_8C0():
        OP_6C(20000, 5000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_8C0)

    def lambda_8D0():
        OP_6E(362, 5000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_8D0)
    WaitChrThread(0x1, 0x2)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    OP_DC()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C1301   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_7D9 end

    def Function_5_916(): pass

    label("Function_5_916")

    EventBegin(0x0)
    ClearParty()
    OP_BB(0x1, 0x1, 0x1)
    AddParty(0x1, 0xF6, 0xFF)
    AddParty(0x45, 0xF7, 0xFF)
    AddParty(0x29, 0xF8, 0xFF)
    AddParty(0x28, 0xF9, 0xFF)
    OP_31(0x1, 0x0, 0x48)
    OP_31(0x1, 0xFE, 0x0)
    OP_41(0x1, 0x2C, 0xFF)
    OP_41(0x1, 0x101, 0xFF)
    OP_41(0x1, 0x122, 0xFF)
    OP_35(0x1, 0x0)
    OP_37(0x1, 0x7F, 0x2)
    OP_41(0x1, 0x2A6, 0x0)
    OP_41(0x1, 0x2A2, 0x1)
    OP_41(0x1, 0x2CB, 0x2)
    OP_41(0x1, 0x2C7, 0x3)
    OP_41(0x1, 0x25D, 0x4)
    OP_41(0x1, 0x266, 0x5)
    OP_41(0x1, 0x291, 0x6)
    OP_BB(0x1, 0x6, 0xEE)
    OP_D6(0x0)
    OP_3E(0x1F5, 5)
    OP_3E(0x1F6, 2)
    OP_3E(0x1F8, 2)
    OP_3E(0x1FB, 1)
    OP_3E(0x1FC, 2)
    OP_3E(0x1FE, 1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrPos(0x9, 780, -1950, 187800, 177)
    SetChrPos(0xA, 4330, -1940, 187800, 177)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    OP_6D(2490, -1980, 188410, 0)
    OP_67(0, 5880, -10000, 0)
    OP_6B(3540, 0)
    OP_6C(0, 0)
    OP_6E(263, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #4
        0x9,
        "*sigh* Man, I'm tired...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x9,
        (
            "Isn't it time to change\x01",
            "watch YET?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xA,
        (
            "Who the hell'd think a level two alert\x01",
            "would be this boring, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xA,
        (
            "Wish that girl would come back this way,\x01",
            "at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x9,
        "What, that chick with the glasses?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x9,
        "You got weird tastes, man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xA,
        (
            "Heeey, she's, uh, unique, sure.\x01",
            "But did you see her?\x01",
            "She's got that 'cute nerd' thing goin' on!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xA,
        (
            "I'm just sayin', I wouldn't mind gettin'\x01",
            "to know her, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x9,
        (
            "Hah, well, go indulge her camera fetish\x01",
            "once you're on break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x9,
        (
            "Still...what the hell are those Intel\x01",
            "leftovers even thinking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x9,
        (
            "Hiding out in the Ravennue mine like a\x01",
            "bunch'a monsters? The hell, man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xA,
        "Who knows, with those guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xA,
        (
            "The minds of crazy 'elites' like them?\x01",
            "Ain't like yours or mine, my friend.\x02",
        )
    )

    CloseMessageWindow()
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xB, 2440, -2040, 192000, 177)
    ClearChrFlags(0xB, 0x80)

    ChrTalk(    #17
        0xB,
        "#6PGood work, you two.\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_D9F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_D9F)

    def lambda_DB1():
        OP_8E(0xFE, 0x988, 0xFFFFF830, 0x2E356, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_DB1)
    OP_8C(0x9, 45, 400)
    OP_8C(0xA, 315, 400)
    WaitChrThread(0xB, 0x1)

    ChrTalk(    #18
        0x9,
        "Ah! Captain, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xA,
        "Captain! All's clear, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xB,
        "Right, good. Listen up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xB,
        (
            "The remnants of the Intelligence Division\x01",
            "showed up in Grancel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xB,
        (
            "All members, including former Captain\x01",
            "Amalthea, are in custody.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x9,
        "For serious, sir?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xA,
        "We're standing down from alert, then, sir?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xB,
        "About that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xB,
        (
            "What they're calling a...'giant flying\x01",
            "orbal puppet' showed up in the\x01",
            "capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xB,
        (
            "We're currently searching for its\x01",
            "whereabouts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x9,
        "A...flying...puppet? Like a doll?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xA,
        (
            "You sure HQ isn't...um...pulling\x01",
            "your leg, sir?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xB,
        "Hell if I know, private.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xB,
        (
            "Regardless, we're to maintain alert\x01",
            "status until dawn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xB,
        (
            "Sorry, gentlemen, but I need you to\x01",
            "remain at your posts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x9,
        "Ugh... Yes, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xA,
        "Understood, sir.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 0, 400)
    OP_8E(0xB, 0x988, 0xFFFFF808, 0x2EE00, 0x7D0, 0x0)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    SetChrFlags(0xB, 0x80)
    Sleep(1000)
    TurnDirection(0x9, 0xA, 400)

    ChrTalk(    #35
        0x9,
        "Pfuh. You gotta be kidding.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x9,
        (
            "A 'giant flying puppet'?\x01",
            "What, someone launch a huge toy\x01",
            "out of a cannon or something?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x9, 400)

    ChrTalk(    #37
        0xA,
        "Ah, who knows.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xA,
        (
            "You heard the captain, though.\x01",
            "Intel guys are done and dusted.\x01",
            "We aren't gonna get attacked out here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xA,
        (
            "All we gotta do is stand around until we\x01",
            "get relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x9,
        "Yeah.\x02",
    )

    CloseMessageWindow()
    OP_22(0xF8, 0x0, 0x32)
    Sleep(800)
    OP_62(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x9, 180, 400)

    ChrTalk(    #41
        0x9,
        "Huh?\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 270, 400)
    Sleep(500)

    ChrTalk(    #42
        0xA,
        "What's up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x9,
        "Thought I heard...\x02",
    )

    CloseMessageWindow()

    def lambda_12AB():
        OP_6D(2410, -2029, 186190, 3000)
        ExitThread()

    QueueWorkItem(0x129, 0, lambda_12AB)

    def lambda_12C3():
        OP_6C(315000, 3000)
        ExitThread()

    QueueWorkItem(0x129, 1, lambda_12C3)
    OP_43(0x9, 0x0, 0x0, 0x6)
    Sleep(300)
    OP_8C(0xA, 225, 400)
    Sleep(2000)
    OP_43(0xA, 0x0, 0x0, 0x7)
    WaitChrThread(0x9, 0x0)
    WaitChrThread(0xA, 0x0)
    OP_20(0xBB8)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    WaitChrThread(0x129, 0x0)
    WaitChrThread(0x129, 0x1)
    ClearChrFlags(0x102, 0x80)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x102, 3800, 10000, 187900, 180)
    SetChrChipByIndex(0x102, 17)
    SetChrSubChip(0x102, 0)
    OP_7D(0x0, 0x102, 0x32, 0x1F4)
    OP_96(0x102, 0xED8, 0xFFFFF844, 0x2DDFC, 0x64, 0x5DC)
    OP_7D(0x1, 0x102, 0x0, 0x0)
    OP_22(0xA4, 0x0, 0x32)
    ClearChrFlags(0x102, 0x4)
    SetChrSubChip(0x102, 1)
    Sleep(800)
    Fade(250)
    SetChrPos(0x102, 3720, -1980, 187090, 180)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 18)
    SetChrSubChip(0x102, 0)
    OP_0D()

    def lambda_13A0():
        OP_99(0x102, 0x1, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_13A0)
    Sleep(300)
    OP_22(0x8F, 0x0, 0x64)

    ChrTalk(    #44
        0xA,
        "Ah!\x02",
    )

    WaitChrThread(0x102, 0x0)
    CloseMessageWindow()

    def lambda_13C8():
        OP_99(0x102, 0x4, 0x6, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_13C8)
    WaitChrThread(0x102, 0x0)
    Fade(250)
    OP_22(0x20C, 0x0, 0x64)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 15)
    SetChrPos(0xA, 4000, -1980, 185970, 180)
    ClearChrFlags(0x102, 0x2)
    SetChrPos(0x102, 3800, -1980, 187600, 180)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    OP_0D()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrFlags(0x102, 0x40)
    OP_7D(0x0, 0x102, 0x32, 0x1F4)
    SetChrChipByIndex(0x102, 17)
    SetChrSubChip(0x102, 0)

    def lambda_1456():
        OP_96(0x102, 0xB54, 0xFFFFF7CC, 0x2CA10, 0x9C4, 0x1770)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1456)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_1479():
        OP_8C(0x9, 0, 400)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1479)
    Sleep(300)
    OP_22(0xA4, 0x0, 0x64)
    OP_8C(0x102, 0, 0)
    Sleep(300)
    WaitChrThread(0x102, 0x1)
    SetChrSubChip(0x102, 1)
    ClearChrFlags(0x102, 0x40)
    OP_7D(0x1, 0x102, 0x0, 0x0)

    ChrTalk(    #45
        0x9,
        "#5PH-Hey! What's wr--\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(250)
    SetChrPos(0x102, 2920, -2100, 183720, 0)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x102, 0x2)
    SetChrFlags(0x102, 0x800)
    SetChrChipByIndex(0x102, 18)
    SetChrSubChip(0x102, 8)
    OP_0D()
    Sleep(300)

    def lambda_1509():
        OP_99(0x102, 0x9, 0xB, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1509)
    Sleep(300)
    OP_22(0x8F, 0x0, 0x64)

    ChrTalk(    #46
        0x9,
        "#5PUrgh...!\x02",
    )

    WaitChrThread(0x102, 0x0)
    CloseMessageWindow()

    def lambda_1539():
        OP_99(0x102, 0xC, 0xE, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1539)
    WaitChrThread(0x102, 0x0)
    Fade(250)
    OP_22(0x20C, 0x0, 0x64)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 15)
    SetChrPos(0x9, 3280, -2080, 183670, 0)
    ClearChrFlags(0x102, 0x2)
    ClearChrFlags(0x102, 0x800)
    SetChrPos(0x102, 2880, -2100, 183230, 0)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #47
        0x102,
        "#1033F...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x12A, 0x80)
    ClearChrFlags(0x146, 0x80)
    ClearChrFlags(0x129, 0x80)
    OP_9F(0x12A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x146, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x129, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x12A, 3250, -2100, 176180, 0)
    SetChrPos(0x146, 2080, -2140, 176150, 0)
    SetChrPos(0x129, 2740, -2130, 175160, 0)

    NpcTalk(    #48
        0x12A,
        "Man's Voice",
        "#2PHeh, not bad, Joshua.\x02",
    )

    CloseMessageWindow()
    OP_9F(0x12A, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    OP_9F(0x146, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    OP_9F(0x129, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)

    def lambda_165B():
        OP_6D(2100, -2040, 182000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_165B)

    def lambda_1673():
        OP_67(0, 6600, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1673)

    def lambda_168B():
        OP_6B(3510, 3000)
        ExitThread()

    QueueWorkItem(0x12A, 3, lambda_168B)

    def lambda_169B():
        OP_6E(242, 3000)
        ExitThread()

    QueueWorkItem(0x129, 3, lambda_169B)

    def lambda_16AB():
        OP_8C(0x102, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_16AB)
    Sleep(500)

    def lambda_16BE():
        OP_8E(0x12A, 0xD48, 0xFFFFF827, 0x2BE44, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x146, 1, lambda_16BE)
    Sleep(200)

    def lambda_16DE():
        OP_8E(0x146, 0x8AC, 0xFFFFF830, 0x2BEF8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12A, 1, lambda_16DE)
    Sleep(200)

    def lambda_16FE():
        OP_8E(0x129, 0xB40, 0xFFFFF83A, 0x2B980, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x129, 1, lambda_16FE)
    Sleep(2000)
    WaitChrThread(0x12A, 0x1)
    WaitChrThread(0x102, 0x2)

    ChrTalk(    #49
        0x12A,
        (
            "#200F#5PImpressive. That was, what?\x01",
            "Half an instant?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x146,
        "#210F#1PYeah, that was...kinda cool!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x102,
        (
            "#1035FIt was nothing.\x02\x03",

            "Knocking out inattentive guards\x01",
            "like this is trivial.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x146,
        (
            "#413F#1PAh, yeah, I bet.\x02\x03",

            "Geez! Can't you take a compliment\x01",
            "at least once?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x129,
        (
            "#1P#197FAre you sure the Bobcat's here,\x01",
            "though?\x02\x03",

            "I would've thought they'd move it to\x01",
            "that fort across the lake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x102,
        (
            "#1030FAll the information I have says it's here.\x02\x03",

            "They're even using it for flight training,\x01",
            "so it should be in working order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x12A,
        (
            "#200F#5PHeh, well, that suits us just fine.\x02\x03",

            "We'll need the Bobcat's ignition key to\x01",
            "start it up, though.\x02\x03",

            "Got a plan for getting that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x102,
        (
            "#1035FI suspect the guard captain we saw has it.\x02\x03",

            "They're probably keeping it until they\x01",
            "hand it over to the Imperial Army along\x01",
            "with the ship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x146,
        (
            "#210F#1PIn other words, we need to crack some\x01",
            "skulls to get it back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x102,
        (
            "#1030FLet's avoid killing anyone if we can.\x02\x03",

            "I'd rather not make more of an enemy out\x01",
            "of the Royal Army than absolutely necessary.\x02\x03",

            "We should hide and avoid confrontation\x01",
            "with any patrolling guards.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x146,
        (
            "#413F#1PBoy, you sure make it sound simple.\x02\x03",

            "#210FNot that I'll complain about not\x01",
            "killing anyone, though!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x129,
        (
            "#1P#490FHahah. Naturally.\x02\x03",

            "The Capua family will never resort\x01",
            "to murder on my watch!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x12A,
        (
            "#203F#5PTrue, but...so much for our great run\x01",
            "of villainy, huh?\x02\x03",

            "Maybe that guy was right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x102,
        "#1031F...Heh-heh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x146,
        "#216F#1PHey, what's so funny?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x102,
        (
            "#1035FIt's nothing... We've no time.\x02\x03",

            "Let's begin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x146,
        "#212F#1PO-Okay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x12A,
        "#200F#5PFinally.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x129,
        "#1P#196FAll right. Let's do this!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_1D(0x59)
    Sleep(100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(2830, -1970, 185370, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_4A(0xA, 255)
    SetChrPos(0xA, 4880, -1940, 188000, 180)
    SetChrChipByIndex(0xA, 15)
    ClearChrFlags(0xA, 0x40)
    ClearChrFlags(0xA, 0x80)
    OP_4A(0x9, 255)
    SetChrPos(0x9, 470, -1910, 187870, 45)
    SetChrChipByIndex(0x9, 15)
    ClearChrFlags(0x9, 0x40)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x0, 2830, -1970, 185370, 0)
    SetChrPos(0x1, 2830, -1970, 185370, 0)
    SetChrPos(0x2, 2830, -1970, 185370, 0)
    SetChrPos(0x3, 2830, -1970, 185370, 0)
    OP_69(0x0, 0x0)
    OP_A2(0x1800)
    OP_3E(0x20F, 1)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_5_916 end

    def Function_6_1E4A(): pass

    label("Function_6_1E4A")

    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 16)
    OP_8E(0xFE, 0x9CE, 0xFFFFF844, 0x2DAA0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xB36, 0xFFFFF7E0, 0x2CD6C, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    OP_22(0xD8, 0x0, 0x46)
    SetChrChipByIndex(0xFE, 12)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_6_1E4A end

    def Function_7_1E93(): pass

    label("Function_7_1E93")

    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 16)
    OP_8E(0xFE, 0xE6A, 0xFFFFF844, 0x2DB86, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    OP_22(0xD8, 0x0, 0x46)
    SetChrChipByIndex(0xFE, 12)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_7_1E93 end

    def Function_8_1EC8(): pass

    label("Function_8_1EC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x300, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x300, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F26")
    EventBegin(0x1)

    ChrTalk(    #68
        0x102,
        "#1030F(We've no time to waste. Let's hurry on.)\x02",
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_1F26")

    Return()

    # Function_8_1EC8 end

    SaveToFile()

Try(main)
