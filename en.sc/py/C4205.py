from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'C4205   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4205.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60031",
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
        'Black Sheep',                          # 10
        'Black Sheep',                          # 11
        'Black Sheep',                          # 12
        'Black Sheep',                          # 13
        'Black Sheep',                          # 14
        'Black Sheep',                          # 15
        'Black Sheep',                          # 16
        'Pink Sheep',                           # 17
        '',                                     # 18
        '',                                     # 19
        '',                                     # 20
        '',                                     # 21
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
        'ED6_DT09/CH10490 ._CH',             # 00
        'ED6_DT09/CH10491 ._CH',             # 01
        'ED6_DT09/CH10500 ._CH',             # 02
        'ED6_DT09/CH10501 ._CH',             # 03
        'ED6_DT09/CH10510 ._CH',             # 04
        'ED6_DT09/CH10511 ._CH',             # 05
        'ED6_DT09/CH11110 ._CH',             # 06
        'ED6_DT09/CH11111 ._CH',             # 07
        'ED6_DT09/CH11120 ._CH',             # 08
        'ED6_DT09/CH11121 ._CH',             # 09
        'ED6_DT09/CH11130 ._CH',             # 0A
        'ED6_DT09/CH11131 ._CH',             # 0B
        'ED6_DT09/CH11140 ._CH',             # 0C
        'ED6_DT09/CH11141 ._CH',             # 0D
        'ED6_DT09/CH11150 ._CH',             # 0E
        'ED6_DT09/CH11151 ._CH',             # 0F
        'ED6_DT27/CH04000 ._CH',             # 10
        'ED6_DT27/CH04010 ._CH',             # 11
        'ED6_DT07/CH00120 ._CH',             # 12
        'ED6_DT07/CH00130 ._CH',             # 13
        'ED6_DT07/CH00140 ._CH',             # 14
        'ED6_DT07/CH00150 ._CH',             # 15
        'ED6_DT07/CH00160 ._CH',             # 16
        'ED6_DT07/CH00170 ._CH',             # 17
        'ED6_DT29/CH12070 ._CH',             # 18
        'ED6_DT29/CH12071 ._CH',             # 19
    )

    AddCharChipPat(
        'ED6_DT09/CH10490P._CP',             # 00
        'ED6_DT09/CH10491P._CP',             # 01
        'ED6_DT09/CH10500P._CP',             # 02
        'ED6_DT09/CH10501P._CP',             # 03
        'ED6_DT09/CH10510P._CP',             # 04
        'ED6_DT09/CH10511P._CP',             # 05
        'ED6_DT09/CH11110P._CP',             # 06
        'ED6_DT09/CH11111P._CP',             # 07
        'ED6_DT09/CH11120P._CP',             # 08
        'ED6_DT09/CH11121P._CP',             # 09
        'ED6_DT09/CH11130P._CP',             # 0A
        'ED6_DT09/CH11131P._CP',             # 0B
        'ED6_DT09/CH11140P._CP',             # 0C
        'ED6_DT09/CH11141P._CP',             # 0D
        'ED6_DT09/CH11150P._CP',             # 0E
        'ED6_DT09/CH11151P._CP',             # 0F
        'ED6_DT27/CH04000P._CP',             # 10
        'ED6_DT27/CH04010P._CP',             # 11
        'ED6_DT07/CH00120P._CP',             # 12
        'ED6_DT07/CH00130P._CP',             # 13
        'ED6_DT07/CH00140P._CP',             # 14
        'ED6_DT07/CH00150P._CP',             # 15
        'ED6_DT07/CH00160P._CP',             # 16
        'ED6_DT07/CH00170P._CP',             # 17
        'ED6_DT29/CH12070P._CP',             # 18
        'ED6_DT29/CH12071P._CP',             # 19
    )

    DeclNpc(
        X                   = 58000,
        Z                   = 1500,
        Y                   = 52910,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 54070,
        Z                   = 450,
        Y                   = 101970,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1E1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 54070,
        Z                   = 450,
        Y                   = 101970,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1E1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 54070,
        Z                   = 450,
        Y                   = 101970,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1E1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 54070,
        Z                   = 450,
        Y                   = 101970,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1E1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 54070,
        Z                   = 450,
        Y                   = 101970,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1E1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 54070,
        Z                   = 450,
        Y                   = 101970,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1E1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 54070,
        Z                   = 450,
        Y                   = 101970,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1E1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 54070,
        Z                   = 450,
        Y                   = 101970,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x1E1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -5110,
        Z                   = 0,
        Y                   = 48870,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x274,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 32880,
        Z                   = 0,
        Y                   = 53420,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x26D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -29030,
        Z                   = 0,
        Y                   = 93770,
        Unknown_0C          = 180,
        Unknown_0E          = 14,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x275,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -11760,
        Z                   = 0,
        Y                   = 93750,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x271,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -20280,
        Z                   = 0,
        Y                   = 93650,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x273,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -31370,
        Z                   = 1000,
        Y                   = 112540,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x26D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 49300,
        Y                   = 0,
        Z                   = 103300,
        Range               = 52050,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x187D6,
        Unknown_18          = 0x0,
        Unknown_1C          = 4,
    )


    DeclActor(
        TriggerX            = 57390,
        TriggerZ            = 0,
        TriggerY            = 52780,
        TriggerRange        = 1000,
        ActorX              = 58000,
        ActorZ              = 1500,
        ActorY              = 52910,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -30130,
        TriggerZ            = 0,
        TriggerY            = 114540,
        TriggerRange        = 1000,
        ActorX              = -29940,
        ActorZ              = 0,
        ActorY              = 115160,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3AA",          # 00, 0
        "Function_1_3C9",          # 01, 1
        "Function_2_417",          # 02, 2
        "Function_3_594",          # 03, 3
        "Function_4_616",          # 04, 4
        "Function_5_A78",          # 05, 5
        "Function_6_B8E",          # 06, 6
        "Function_7_CAD",          # 07, 7
        "Function_8_EC0",          # 08, 8
    )


    def Function_0_3AA(): pass

    label("Function_0_3AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2DF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C8")
    SetChrPos(0x9, 76660, 0, 102000, 270)
    ClearChrFlags(0x9, 0x80)

    label("loc_3C8")

    Return()

    # Function_0_3AA end

    def Function_1_3C9(): pass

    label("Function_1_3C9")

    OP_1B(0xD, 0x0, 0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E0")
    OP_6F(0x0, 0)
    Jump("loc_3E7")

    label("loc_3E0")

    OP_6F(0x0, 60)

    label("loc_3E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F9")
    OP_6F(0x1, 0)
    Jump("loc_400")

    label("loc_3F9")

    OP_6F(0x1, 60)

    label("loc_400")

    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_3C9 end

    def Function_2_417(): pass

    label("Function_2_417")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43C")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_57E")

    label("loc_43C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_455")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_57E")

    label("loc_455")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46E")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_57E")

    label("loc_46E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_487")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_57E")

    label("loc_487")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A0")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_57E")

    label("loc_4A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B9")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_57E")

    label("loc_4B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D2")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_57E")

    label("loc_4D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4EB")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_57E")

    label("loc_4EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_504")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_57E")

    label("loc_504")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51D")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_57E")

    label("loc_51D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_536")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_57E")

    label("loc_536")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54F")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_57E")

    label("loc_54F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_568")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_57E")

    label("loc_568")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57E")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_57E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_593")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_57E")

    label("loc_593")

    Return()

    # Function_2_417 end

    def Function_3_594(): pass

    label("Function_3_594")

    EventBegin(0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05The hidden door is completely blocked and impassable.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_90(0x0, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_3_594 end

    def Function_4_616(): pass

    label("Function_4_616")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2DF, 7)), scpexpr(EXPR_END)), "loc_61E")
    Return()

    label("loc_61E")

    EventBegin(0x0)
    OP_8C(0x0, 90, 0)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrPos(0x9, 76660, 0, 102000, 270)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 15)
    SetChrSubChip(0x9, 0)

    def lambda_669():
        OP_91(0xFE, 0xFFFFA1A0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_669)
    SetChrPos(0xA, 78660, 0, 102500, 270)
    SetChrPos(0xB, 78660, 0, 101500, 270)
    SetChrPos(0xC, 80660, 0, 102000, 270)
    SetChrPos(0xD, 82660, 0, 102500, 270)
    SetChrPos(0xE, 82660, 0, 101500, 270)
    SetChrPos(0xF, 84660, 0, 102000, 270)
    SetChrPos(0x10, 86660, 0, 102000, 270)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0xA, 15)
    SetChrSubChip(0xA, 0)
    SetChrChipByIndex(0xB, 15)
    SetChrSubChip(0xB, 0)
    SetChrChipByIndex(0xC, 15)
    SetChrSubChip(0xC, 0)
    SetChrChipByIndex(0xD, 15)
    SetChrSubChip(0xD, 0)
    SetChrChipByIndex(0xE, 15)
    SetChrSubChip(0xE, 0)
    SetChrChipByIndex(0xF, 15)
    SetChrSubChip(0xF, 0)
    SetChrChipByIndex(0x10, 25)
    SetChrSubChip(0x10, 0)
    OP_43(0x9, 0x0, 0x0, 0x2)
    OP_43(0xA, 0x0, 0x0, 0x2)
    OP_43(0xB, 0x0, 0x0, 0x2)
    OP_43(0xC, 0x0, 0x0, 0x2)
    OP_43(0xD, 0x0, 0x0, 0x2)
    OP_43(0xE, 0x0, 0x0, 0x2)
    OP_43(0xF, 0x0, 0x0, 0x2)
    OP_43(0x10, 0x0, 0x0, 0x2)

    def lambda_7A1():
        OP_91(0xFE, 0xFFFFA1A0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7A1)

    def lambda_7BC():
        OP_91(0xFE, 0xFFFFA1A0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_7BC)

    def lambda_7D7():
        OP_91(0xFE, 0xFFFFA1A0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_7D7)

    def lambda_7F2():
        OP_91(0xFE, 0xFFFFA1A0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_7F2)

    def lambda_80D():
        OP_91(0xFE, 0xFFFFA1A0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_80D)

    def lambda_828():
        OP_91(0xFE, 0xFFFFA1A0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_828)

    def lambda_843():
        OP_91(0xFE, 0xFFFFA1A0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_843)

    def lambda_85E():
        OP_6D(60800, 120, 102000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_85E)

    def lambda_876():
        OP_67(0, 5150, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_876)

    def lambda_88E():
        OP_6B(2800, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_88E)

    def lambda_89E():
        OP_6C(90000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_89E)
    WaitChrThread(0x0, 0x0)
    SetChrFlags(0xF7, 0x40)
    SetChrFlags(0xF8, 0x40)
    SetChrPos(0x101, 49500, 450, 102000, 90)
    SetChrPos(0xF7, 48200, 300, 102600, 90)
    SetChrPos(0xF8, 48200, 300, 101400, 90)
    SetChrPos(0xF9, 46950, 0, 102000, 90)
    SetChrChipByIndex(0x101, 16)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_END)),
        (1, "loc_925"),
        (2, "loc_92D"),
        (3, "loc_935"),
        (4, "loc_93D"),
        (5, "loc_945"),
        (6, "loc_94D"),
        (7, "loc_955"),
        (SWITCH_DEFAULT, "loc_95D"),
    )


    label("loc_925")

    SetChrChipByIndex(0xF7, 17)
    Jump("loc_95D")

    label("loc_92D")

    SetChrChipByIndex(0xF7, 18)
    Jump("loc_95D")

    label("loc_935")

    SetChrChipByIndex(0xF7, 19)
    Jump("loc_95D")

    label("loc_93D")

    SetChrChipByIndex(0xF7, 20)
    Jump("loc_95D")

    label("loc_945")

    SetChrChipByIndex(0xF7, 21)
    Jump("loc_95D")

    label("loc_94D")

    SetChrChipByIndex(0xF7, 22)
    Jump("loc_95D")

    label("loc_955")

    SetChrChipByIndex(0xF7, 23)
    Jump("loc_95D")

    label("loc_95D")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (1, "loc_982"),
        (2, "loc_98A"),
        (3, "loc_992"),
        (4, "loc_99A"),
        (5, "loc_9A2"),
        (6, "loc_9AA"),
        (7, "loc_9B2"),
        (SWITCH_DEFAULT, "loc_9BA"),
    )


    label("loc_982")

    SetChrChipByIndex(0xF8, 17)
    Jump("loc_9BA")

    label("loc_98A")

    SetChrChipByIndex(0xF8, 18)
    Jump("loc_9BA")

    label("loc_992")

    SetChrChipByIndex(0xF8, 19)
    Jump("loc_9BA")

    label("loc_99A")

    SetChrChipByIndex(0xF8, 20)
    Jump("loc_9BA")

    label("loc_9A2")

    SetChrChipByIndex(0xF8, 21)
    Jump("loc_9BA")

    label("loc_9AA")

    SetChrChipByIndex(0xF8, 22)
    Jump("loc_9BA")

    label("loc_9B2")

    SetChrChipByIndex(0xF8, 23)
    Jump("loc_9BA")

    label("loc_9BA")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (1, "loc_9DF"),
        (2, "loc_9E7"),
        (3, "loc_9EF"),
        (4, "loc_9F7"),
        (5, "loc_9FF"),
        (6, "loc_A07"),
        (7, "loc_A0F"),
        (SWITCH_DEFAULT, "loc_A17"),
    )


    label("loc_9DF")

    SetChrChipByIndex(0xF9, 17)
    Jump("loc_A17")

    label("loc_9E7")

    SetChrChipByIndex(0xF9, 18)
    Jump("loc_A17")

    label("loc_9EF")

    SetChrChipByIndex(0xF9, 19)
    Jump("loc_A17")

    label("loc_9F7")

    SetChrChipByIndex(0xF9, 20)
    Jump("loc_A17")

    label("loc_9FF")

    SetChrChipByIndex(0xF9, 21)
    Jump("loc_A17")

    label("loc_A07")

    SetChrChipByIndex(0xF9, 22)
    Jump("loc_A17")

    label("loc_A0F")

    SetChrChipByIndex(0xF9, 23)
    Jump("loc_A17")

    label("loc_A17")

    Sleep(2000)

    def lambda_A22():
        OP_6D(51900, 450, 102000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_A22)
    WaitChrThread(0x9, 0x1)
    Battle(0x277, 0x0, 0x0, 0x0, 0xFF)
    ClearChrFlags(0xF7, 0x40)
    ClearChrFlags(0xF8, 0x40)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_A64"),
        (0, "loc_A69"),
        (2, "loc_A70"),
        (SWITCH_DEFAULT, "loc_A77"),
    )


    label("loc_A64")

    OP_B4(0x0)
    Jump("loc_A77")

    label("loc_A69")

    Call(0, 5)
    Jump("loc_A77")

    label("loc_A70")

    Call(0, 6)
    Jump("loc_A77")

    label("loc_A77")

    Return()

    # Function_4_616 end

    def Function_5_A78(): pass

    label("Function_5_A78")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x9, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xC, 0x1)
    OP_44(0xD, 0x1)
    OP_44(0xE, 0x1)
    OP_44(0xF, 0x1)
    OP_44(0x10, 0x1)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    OP_6D(50000, 450, 101960, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 50000, 450, 101960, 90)
    SetChrPos(0x1, 50000, 450, 101960, 90)
    SetChrPos(0x2, 50000, 450, 101960, 90)
    SetChrPos(0x3, 50000, 450, 101960, 90)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0xF7, 65535)
    SetChrSubChip(0xF7, 0)
    SetChrChipByIndex(0xF8, 65535)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0xF9, 0)
    OP_A2(0x16FF)
    OP_B2(0x0, 0x0, 0x80)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_5_A78 end

    def Function_6_B8E(): pass

    label("Function_6_B8E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x9, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xC, 0x1)
    OP_44(0xD, 0x1)
    OP_44(0xE, 0x1)
    OP_44(0xF, 0x1)
    OP_44(0x10, 0x1)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrPos(0x9, 76660, 0, 102000, 270)
    ClearChrFlags(0x9, 0x80)
    OP_6D(45980, 0, 101860, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 45980, 0, 101860, 270)
    SetChrPos(0x1, 45980, 0, 101860, 270)
    SetChrPos(0x2, 45980, 0, 101860, 270)
    SetChrPos(0x3, 45980, 0, 101860, 270)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0xF7, 65535)
    SetChrSubChip(0xF7, 0)
    SetChrChipByIndex(0xF8, 65535)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0xF9, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_6_B8E end

    def Function_7_CAD(): pass

    label("Function_7_CAD")

    OP_EA(0x2, 0x9, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E48")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D97")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_D04():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_D04)

    def lambda_D1F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_D1F)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #1
        "\x07\x05Monsters appeared!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x276, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_D72"),
        (2, "loc_D84"),
        (1, "loc_D94"),
        (SWITCH_DEFAULT, "loc_D97"),
    )


    label("loc_D72")

    OP_A2(0x1723)
    OP_6F(0x0, 60)
    Sleep(500)
    Jump("loc_D97")

    label("loc_D84")

    OP_6F(0x0, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_D94")

    OP_B4(0x0)
    Return()

    label("loc_D97")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x16A, 1)"), scpexpr(EXPR_END)), "loc_DE3")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #2
        "Found \x1F\x6A\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1722)
    Jump("loc_E45")

    label("loc_DE3")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #3
        (
            "Found \x1F\x6A\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x6A\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_E45")

    Jump("loc_EB2")

    label("loc_E48")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #4
        (
            "\x07\x05Wow... You're the first human to ever take\x01",
            "something from me! I'm so excited!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_EB2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_CAD end

    def Function_8_EC0(): pass

    label("Function_8_EC0")

    OP_EA(0x2, 0xA, 0x1, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FB6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x1E)
    OP_73(0x1)
    OP_6F(0x1, 30)
    AddSepith(0x0, 0x19)
    AddSepith(0x1, 0x19)
    AddSepith(0x2, 0x19)
    AddSepith(0x3, 0x19)
    AddSepith(0x4, 0x19)
    AddSepith(0x5, 0x19)
    AddSepith(0x6, 0x19)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #5
        (
            "Found\x01",
            "#2C#56IEarth Sepith\x01",
            "#57IWater Sepith\x01",
            "#58IFire Sepith\x01",
            "#59IWind Sepith\x01",
            "#62ITime Sepith\x01",
            "#60ISpace Sepith\x01",
            "#61IMirage Sepith x25#0C.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1724)
    Jump("loc_100F")

    label("loc_FB6")


    AnonymousTalk(    #6
        (
            "\x07\x05The chest is empty. Why don't you fill it with\x01",
            "something? C'mon. Come right in...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_100F")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_EC0 end

    SaveToFile()

Try(main)
