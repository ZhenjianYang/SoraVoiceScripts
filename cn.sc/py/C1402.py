from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        '士兵古特',                             # 10
        '士兵拉凯尔',                           # 11
        '守备队长',                             # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
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
        "Function_1_39F",          # 01, 1
        "Function_2_3D4",          # 02, 2
        "Function_3_551",          # 03, 3
        "Function_4_721",          # 04, 4
        "Function_5_84E",          # 05, 5
        "Function_6_18E7",         # 06, 6
        "Function_7_1930",         # 07, 7
        "Function_8_1965",         # 08, 8
    )


    def Function_0_31E(): pass

    label("Function_0_31E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x300, 0)), scpexpr(EXPR_END)), "loc_36D")
    OP_4A(0xA, 255)
    SetChrPos(0xA, 4880, -1940, 187950, 180)
    SetChrChipByIndex(0xA, 15)
    ClearChrFlags(0xA, 0x40)
    ClearChrFlags(0xA, 0x80)
    OP_4A(0x9, 255)
    SetChrPos(0x9, 470, -1910, 187800, 45)
    SetChrChipByIndex(0x9, 15)
    ClearChrFlags(0x9, 0x40)
    ClearChrFlags(0x9, 0x80)

    label("loc_36D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_387")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    Event(0, 4)
    Jump("loc_39E")

    label("loc_387")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_39E")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F1)
    Event(0, 5)

    label("loc_39E")

    Return()

    # Function_0_31E end

    def Function_1_39F(): pass

    label("Function_1_39F")

    OP_51(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x362, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C7")
    OP_6F(0x2, 0)
    Jump("loc_3CE")

    label("loc_3C7")

    OP_6F(0x2, 60)

    label("loc_3CE")

    OP_71(0x0, 0x4)
    Return()

    # Function_1_39F end

    def Function_2_3D4(): pass

    label("Function_2_3D4")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F9")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_53B")

    label("loc_3F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_412")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_53B")

    label("loc_412")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42B")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_53B")

    label("loc_42B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_444")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_53B")

    label("loc_444")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45D")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_53B")

    label("loc_45D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_476")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_53B")

    label("loc_476")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48F")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_53B")

    label("loc_48F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A8")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_53B")

    label("loc_4A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C1")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_53B")

    label("loc_4C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DA")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_53B")

    label("loc_4DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F3")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_53B")

    label("loc_4F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50C")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_53B")

    label("loc_50C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_525")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_53B")

    label("loc_525")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53B")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_53B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_550")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_53B")

    label("loc_550")

    Return()

    # Function_2_3D4 end

    def Function_3_551(): pass

    label("Function_3_551")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x362, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E4")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x362, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_630")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_5A3():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5A3)

    def lambda_5BE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_5BE)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #0
        "\x07\x05魔兽出现了！\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0xBA, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_60B"),
        (2, "loc_61D"),
        (1, "loc_62D"),
        (SWITCH_DEFAULT, "loc_630"),
    )


    label("loc_60B")

    OP_A2(0x1B17)
    OP_6F(0x2, 60)
    Sleep(500)
    Jump("loc_630")

    label("loc_61D")

    OP_6F(0x2, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_62D")

    OP_B4(0x0)
    Return()

    label("loc_630")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2A2, 1)"), scpexpr(EXPR_END)), "loc_67F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #1
        "\x07\x00得到了\x1F\xA2\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B16)
    Jump("loc_6E1")

    label("loc_67F")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #2
        (
            "宝箱里装有\x1F\xA2\x02\x07\x00。 \x01",
            "所持物品已经满了，\x1F\xA2\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_6E1")

    Jump("loc_713")

    label("loc_6E4")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #3
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_713")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_551 end

    def Function_4_721(): pass

    label("Function_4_721")

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

    def lambda_7C4():
        OP_6D(1860, -30, 185090, 13000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_7C4)
    Sleep(8000)

    def lambda_7E1():
        OP_67(0, 6570, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_7E1)

    def lambda_7F9():
        OP_6C(20000, 5000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_7F9)

    def lambda_809():
        OP_6E(362, 5000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_809)
    WaitChrThread(0x1, 0x2)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C1301   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_721 end

    def Function_5_84E(): pass

    label("Function_5_84E")

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
        "啊～好困。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x9,
        "交班时间快点到吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xA,
        (
            "想不到都进入第二级警戒状态了，\x01",
            "居然还是如此空闲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xA,
        (
            "刚才的小妹妹\x01",
            "能再来就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x9,
        "那个戴眼镜的女孩子？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x9,
        "你的兴趣可真古怪。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xA,
        (
            "个性确实有点独特，\x01",
            "不过也很可爱……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xA,
        "想跟她认识认识～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x9,
        (
            "哈哈，那么你就趁\x01",
            "休息时间去跟她打个招呼好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x9,
        (
            "不过……\x01",
            "不知道情报部的那些余党\x01",
            "到底在想什么呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x9,
        (
            "不管怎么看，他们似乎都\x01",
            "藏在拉文努的废坑里吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xA,
        "谁知道。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xA,
        (
            "这些原精英部队份子考虑的事情\x01",
            "我们怎么搞得清楚。\x02",
        )
    )

    CloseMessageWindow()
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xB, 2440, -2040, 192000, 177)
    ClearChrFlags(0xB, 0x80)

    ChrTalk(    #17
        0xB,
        "#6P……你们两个辛苦了。\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_BAE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_BAE)

    def lambda_BC0():
        OP_8E(0xFE, 0x988, 0xFFFFF830, 0x2E356, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_BC0)
    OP_8C(0x9, 45, 400)
    OP_8C(0xA, 315, 400)
    WaitChrThread(0xB, 0x1)

    ChrTalk(    #18
        0x9,
        "队、队长。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xA,
        "您巡视辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xB,
        "嗯，你们听着。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xB,
        (
            "情报部的余党好像\x01",
            "在格兰赛尔出现了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xB,
        (
            "以凯诺娜原上尉为首的\x01",
            "全部成员都被逮捕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x9,
        "是、是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xA,
        (
            "那么这样一来\x01",
            "警戒体制就可以结束了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xB,
        "不，那个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xB,
        (
            "听说王都出现了\x01",
            "『会飞的巨大机器人』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xB,
        "目前好像正在搜寻那个东西。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x9,
        "会、会飞的巨大机器人？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xA,
        "那是什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xB,
        "我也不清楚。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xB,
        (
            "总而言之上头指示要\x01",
            "持续警戒体制到天亮为止。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xB,
        "不好意思，麻烦你们继续辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x9,
        "呜呜……是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xA,
        "……明白了。\x02",
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
        (
            "哈……\x01",
            "真是了不得了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x9,
        (
            "『会飞的巨大机器人』\x01",
            "到底是什么啊……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x9, 400)

    ChrTalk(    #37
        0xA,
        "谁知道……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xA,
        (
            "反正，不管怎样\x01",
            "都已经没有被袭击的危险了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xA,
        (
            "接下来只要随便站到\x01",
            "交班的时间就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x9,
        "是啊……\x02",
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
        "……咦？\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 270, 400)
    Sleep(500)

    ChrTalk(    #42
        0xA,
        "什么，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x9,
        "等等，好像有什么声音……\x02",
    )

    CloseMessageWindow()

    def lambda_F42():
        OP_6D(2410, -2029, 186190, 3000)
        ExitThread()

    QueueWorkItem(0x129, 0, lambda_F42)

    def lambda_F5A():
        OP_6C(315000, 3000)
        ExitThread()

    QueueWorkItem(0x129, 1, lambda_F5A)
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

    def lambda_1037():
        OP_99(0x102, 0x1, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1037)
    Sleep(300)
    OP_22(0x8F, 0x0, 0x64)

    ChrTalk(    #44
        0xA,
        "啊……\x02",
    )

    WaitChrThread(0x102, 0x0)
    CloseMessageWindow()

    def lambda_1062():
        OP_99(0x102, 0x4, 0x6, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1062)
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

    def lambda_10F0():
        OP_96(0x102, 0xB54, 0xFFFFF7CC, 0x2CA10, 0x9C4, 0x1770)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10F0)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_1113():
        OP_8C(0x9, 0, 400)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1113)
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
        (
            "#5P喂、喂喂！\x01",
            "怎么了……\x02",
        )
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

    def lambda_11A6():
        OP_99(0x102, 0x9, 0xB, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_11A6)
    Sleep(300)
    OP_22(0x8F, 0x0, 0x64)

    ChrTalk(    #46
        0x9,
        "#5P唔……\x02",
    )

    WaitChrThread(0x102, 0x0)
    CloseMessageWindow()

    def lambda_11D4():
        OP_99(0x102, 0xC, 0xE, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_11D4)
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
        "#1033F………………………………\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x12A, 0x80)
    ClearChrFlags(0x146, 0x80)
    ClearChrFlags(0x129, 0x80)
    SetChrPos(0x12A, 3250, -2100, 176180, 0)
    SetChrPos(0x146, 2080, -2140, 176150, 0)
    SetChrPos(0x129, 2740, -2130, 175160, 0)

    NpcTalk(    #48
        0x12A,
        "男人的声音",
        "#2P嘿嘿，挺厉害的嘛。\x02",
    )

    CloseMessageWindow()

    def lambda_12C5():
        OP_6D(2100, -2040, 182000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_12C5)

    def lambda_12DD():
        OP_67(0, 6600, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_12DD)

    def lambda_12F5():
        OP_6B(3510, 3000)
        ExitThread()

    QueueWorkItem(0x12A, 3, lambda_12F5)

    def lambda_1305():
        OP_6E(242, 3000)
        ExitThread()

    QueueWorkItem(0x129, 3, lambda_1305)

    def lambda_1315():
        OP_8C(0x102, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1315)
    Sleep(500)

    def lambda_1328():
        OP_8E(0x12A, 0xD48, 0xFFFFF827, 0x2BE44, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x146, 1, lambda_1328)
    Sleep(200)

    def lambda_1348():
        OP_8E(0x146, 0x8AC, 0xFFFFF830, 0x2BEF8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12A, 1, lambda_1348)
    Sleep(200)

    def lambda_1368():
        OP_8E(0x129, 0xB40, 0xFFFFF83A, 0x2B980, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x129, 1, lambda_1368)
    Sleep(2000)
    WaitChrThread(0x12A, 0x1)
    WaitChrThread(0x102, 0x2)

    ChrTalk(    #49
        0x12A,
        (
            "#200F#6P了不起。\x01",
            "一转眼就搞定了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x146,
        (
            "#210F#5P嗯、嗯……\x01",
            "挺有一手的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x102,
        (
            "#1035F……这不算什么。\x02\x03",

            "让松懈的士兵\x01",
            "睡一觉可谓轻而易举。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x146,
        (
            "#413F#5P嗯，知道了知道了。\x02\x03",

            "是我自己太傻，\x01",
            "老是希望你的个性会可爱一点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x129,
        (
            "#197F不过『山猫号』确实\x01",
            "在这里吧？\x02\x03",

            "我还以为被运到\x01",
            "那个要塞去了呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x102,
        (
            "#1030F据我的调查是没有错的。\x02\x03",

            "而且还被作为飞行训练使用过，\x01",
            "应该已经进行了整备才对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x12A,
        (
            "#200F#6P嘿嘿，那就好。\x02\x03",

            "只不过要起动机体的话，\x01",
            "必须有『山猫号』的启动钥匙。\x02\x03",

            "可以弄得到吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x102,
        (
            "#1035F刚才那个守备队长\x01",
            "身上应该有。\x02\x03",

            "大概准备在交付帝国军飞艇时\x01",
            "一并交给对方吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x146,
        "#210F#5P也就是要强行抢回是吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x102,
        (
            "#1030F不过不可以用杀人的方式。\x02\x03",

            "没有必要的话，\x01",
            "最好不要与王国军为敌。\x02\x03",

            "也尽量不要让那些\x01",
            "巡逻的卫兵发现我们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x146,
        (
            "#413F#5P真是的……\x01",
            "好乱来的家伙。\x02\x03",

            "#210F不过我也确实\x01",
            "反对杀人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x129,
        (
            "#490F嘿嘿，当然了。\x02\x03",

            "谁让我们『卡普亚一家』\x01",
            "是禁止杀人和施暴的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x12A,
        (
            "#203F#6P唉，我们其实\x01",
            "没法彻底成为恶人……\x02\x03",

            "可能就像那个少尉说的那样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x102,
        "#1031F……呵呵。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x146,
        "#216F#5P有、有什么好笑的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x102,
        (
            "#1035F不是……\x01",
            "我们的时间不多了。\x02\x03",

            "快点开始吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x146,
        "#212F#5P嗯、嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x12A,
        "#200F#6P终于要开始了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x129,
        (
            "#196F好～……\x01",
            "加油吧！\x02",
        )
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
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_5_84E end

    def Function_6_18E7(): pass

    label("Function_6_18E7")

    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 16)
    OP_8E(0xFE, 0x9CE, 0xFFFFF844, 0x2DAA0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xB36, 0xFFFFF7E0, 0x2CD6C, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    OP_22(0xD8, 0x0, 0x46)
    SetChrChipByIndex(0xFE, 12)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_6_18E7 end

    def Function_7_1930(): pass

    label("Function_7_1930")

    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 16)
    OP_8E(0xFE, 0xE6A, 0xFFFFF844, 0x2DB86, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    OP_22(0xD8, 0x0, 0x46)
    SetChrChipByIndex(0xFE, 12)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_7_1930 end

    def Function_8_1965(): pass

    label("Function_8_1965")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x300, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x300, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19B9")
    EventBegin(0x1)

    ChrTalk(    #68
        0x102,
        (
            "#1030F（时间并不宽裕。\x01",
            "赶快进去吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_19B9")

    Return()

    # Function_8_1965 end

    SaveToFile()

Try(main)
