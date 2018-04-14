from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2402   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2402.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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
        '特蕾莎院长',                           # 9
        '克拉姆',                               # 10
        '波利',                                 # 11
        '玛丽',                                 # 12
        '达尼艾尔',                             # 13
        '鸡',                                   # 14
        '鸡',                                   # 15
        '鸡',                                   # 16
        '目标用照相机',                         # 17
        '梅威海道方向',                         # 18
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
        'ED6_DT07/CH02570 ._CH',             # 00
        'ED6_DT07/CH02590 ._CH',             # 01
        'ED6_DT07/CH02500 ._CH',             # 02
        'ED6_DT07/CH02630 ._CH',             # 03
        'ED6_DT07/CH02640 ._CH',             # 04
        'ED6_DT07/CH01720 ._CH',             # 05
        'ED6_DT26/CH20237 ._CH',             # 06
        'ED6_DT26/CH20272 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH02570P._CP',             # 00
        'ED6_DT07/CH02590P._CP',             # 01
        'ED6_DT07/CH02500P._CP',             # 02
        'ED6_DT07/CH02630P._CP',             # 03
        'ED6_DT07/CH02640P._CP',             # 04
        'ED6_DT07/CH01720P._CP',             # 05
        'ED6_DT26/CH20237P._CP',             # 06
        'ED6_DT26/CH20272P._CP',             # 07
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1060,
        Z                   = 0,
        Y                   = -23220,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -1820,
        Y                   = 0,
        Z                   = 2670,
        Range               = 2120,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x157C,
        Unknown_18          = 0x0,
        Unknown_1C          = 13,
    )


    DeclActor(
        TriggerX            = -186,
        TriggerZ            = 0,
        TriggerY            = 32147,
        TriggerRange        = 400,
        ActorX              = -186,
        ActorZ              = 1250,
        ActorY              = 32147,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_26E",          # 00, 0
        "Function_1_3C2",          # 01, 1
        "Function_2_403",          # 02, 2
        "Function_3_580",          # 03, 3
        "Function_4_664",          # 04, 4
        "Function_5_688",          # 05, 5
        "Function_6_7DB",          # 06, 6
        "Function_7_821",          # 07, 7
        "Function_8_C04",          # 08, 8
        "Function_9_FEC",          # 09, 9
        "Function_10_10D4",        # 0A, 10
        "Function_11_17E6",        # 0B, 11
        "Function_12_186A",        # 0C, 12
        "Function_13_1890",        # 0D, 13
        "Function_14_24F5",        # 0E, 14
        "Function_15_27E8",        # 0F, 15
    )


    def Function_0_26E(): pass

    label("Function_0_26E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2CE")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -3270, 0, 9200, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x416, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_298")
    SetChrFlags(0x9, 0x10)

    label("loc_298")

    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 2970, 0, 27510, 45)
    OP_43(0xA, 0x0, 0x0, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 13060, 0, 20500, 90)
    Jump("loc_3AE")

    label("loc_2CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_2D8")
    Jump("loc_3AE")

    label("loc_2D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_348")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 8320, -170, 15270, 270)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -6449, -198, 20931, 90)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 7012, 0, 23975, 180)
    TurnDirection(0xA, 0x9, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 4690, 0, 26500, 220)
    OP_43(0xB, 0x0, 0x0, 0x3)
    Jump("loc_3AE")

    label("loc_348")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_3AE")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -9630, 40, 16570, 270)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 9460, 10, 19760, 270)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 2970, 0, 27510, 47)
    OP_43(0xA, 0x0, 0x0, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 5190, 0, 29630, 225)

    label("loc_3AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_3C1")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 14)

    label("loc_3C1")

    Return()

    # Function_0_26E end

    def Function_1_3C2(): pass

    label("Function_1_3C2")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE5A20, 0x230067)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3E6")
    OP_10(0x0, 0x0)
    OP_10(0x2, 0x1)

    label("loc_3E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3FE")
    OP_72(0x0, 0x10)
    OP_65(0x0, 0x1)
    Jump("loc_402")

    label("loc_3FE")

    OP_64(0x0, 0x1)

    label("loc_402")

    Return()

    # Function_1_3C2 end

    def Function_2_403(): pass

    label("Function_2_403")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_428")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_56A")

    label("loc_428")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_441")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_56A")

    label("loc_441")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45A")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_56A")

    label("loc_45A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_473")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_56A")

    label("loc_473")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48C")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_56A")

    label("loc_48C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A5")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_56A")

    label("loc_4A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BE")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_56A")

    label("loc_4BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D7")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_56A")

    label("loc_4D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F0")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_56A")

    label("loc_4F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_509")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_56A")

    label("loc_509")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_522")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_56A")

    label("loc_522")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53B")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_56A")

    label("loc_53B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_554")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_56A")

    label("loc_554")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56A")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_56A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_57F")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_56A")

    label("loc_57F")

    Return()

    # Function_2_403 end

    def Function_3_580(): pass

    label("Function_3_580")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_663")
    OP_8E(0xFE, 0x1365, 0x25, 0x5C94, 0x7D0, 0x0)
    Sleep(1000)
    OP_8B(0xFE, 0x416, 0x65E7, 0x190)
    Sleep(200)
    OP_8E(0xFE, 0x416, 0x0, 0x65E7, 0x7D0, 0x0)
    Sleep(1000)
    OP_8B(0xFE, 0x2D3, 0x5565, 0x190)
    Sleep(200)
    OP_8E(0xFE, 0x2D3, 0x1A, 0x5565, 0x7D0, 0x0)
    Sleep(1000)
    OP_8B(0xFE, 0x10BE, 0x6B64, 0x190)
    Sleep(200)
    OP_8E(0xFE, 0x10BE, 0x0, 0x6B64, 0x7D0, 0x0)
    Sleep(1000)
    OP_8B(0xFE, 0xFFFFF991, 0x4BAE, 0x190)
    Sleep(200)
    OP_8E(0xFE, 0xFFFFF991, 0xBD, 0x4BAE, 0x7D0, 0x0)
    Sleep(1000)
    OP_8B(0xFE, 0x1365, 0x5C94, 0x190)
    Sleep(200)
    Jump("Function_3_580")

    label("loc_663")

    Return()

    # Function_3_580 end

    def Function_4_664(): pass

    label("Function_4_664")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_687")
    OP_8D(0xFE, 1350, 26320, 3220, 28450, 2000)
    Jump("Function_4_664")

    label("loc_687")

    Return()

    # Function_4_664 end

    def Function_5_688(): pass

    label("Function_5_688")

    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x4)
    OP_8D(0xFE, -8760, 13210, 8700, 24630, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6B6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7DA")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_79F")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x2238), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_PUSH_LONG, 0x339A), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0x21FC), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0x6036), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_774")
    SetChrFlags(0xFE, 0x20)
    TurnDirection(0xFE, 0x0, 0)
    ClearChrFlags(0xFE, 0x20)

    def lambda_761():
        OP_94(0x0, 0xFE, 0xB4, 0x12C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_761)
    Jump("loc_797")

    label("loc_774")


    def lambda_77A():
        OP_8D(0xFE, -8760, 13210, 8700, 24630, 6000)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_77A)
    Sleep(200)

    label("loc_797")

    Sleep(30)
    Jump("loc_7D7")

    label("loc_79F")

    Sleep(50)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D7")
    OP_44(0xFE, 0x2)

    def lambda_7BF():
        OP_8D(0xFE, -8760, 13210, 8700, 24630, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7BF)

    label("loc_7D7")

    Jump("loc_6B6")

    label("loc_7DA")

    Return()

    # Function_5_688 end

    def Function_6_7DB(): pass

    label("Function_6_7DB")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #0
        "\x07\x05门上着锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_6_7DB end

    def Function_7_821(): pass

    label("Function_7_821")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_AF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_984")
    OP_8C(0xFE, 90, 0)
    OP_62(0xFE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #1
        0xFE,
        "啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "嗯……那个……\x01",
            "是约修亚……对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x102,
        (
            "#1054F嗯……\x01",
            "玛丽，好久不见。\x02\x03",

            "穿着奇怪的衣服\x01",
            "没吓到你吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #4
        0xFE,
        "没、没有那种事！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "怎么说呢……\x01",
            "好帅哦，那衣服！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x102,
        "#1049F哈哈……谢谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "啊，老师在里面\x01",
            "你去见她吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "嘿嘿……她一定会很高兴的。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    OP_A2(0x20EB)
    Jump("loc_AED")

    label("loc_984")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_A30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_9D9")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #9
        0xFE,
        (
            "老师在里面\x01",
            "你去见她吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "嘿嘿……她一定会很高兴的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A2D")

    label("loc_9D9")


    ChrTalk(    #11
        0xFE,
        (
            "自从那个奇怪的贝壳出现以后\x01",
            "信也没法送到……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "在王都的科洛丝姐姐\x01",
            "不要紧吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A2D")

    Jump("loc_AED")

    label("loc_A30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_A7E")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #13
        0xFE,
        (
            "老师在里面\x01",
            "你去见她吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "嘿嘿……她一定会很高兴的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_AED")

    label("loc_A7E")


    ChrTalk(    #15
        0xFE,
        (
            "没有导力器\x01",
            "大家也都不在乎。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "蛋和蔬菜都有，\x01",
            "有柴的话还能用火……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "就算吸尘器不能用\x01",
            "有扫帚就行了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AED")

    Jump("loc_C00")

    label("loc_AF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_B8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_B4E")

    ChrTalk(    #18
        0xFE,
        (
            "我们这里的鸡生的蛋\x01",
            "很好吃的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        "是不是因为让它们悠闲长大的关系呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_B8A")

    label("loc_B4E")

    OP_A2(0x3)

    ChrTalk(    #20
        0xFE,
        "要赶快把蛋收走才行。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "再不赶快\x01",
            "会被大家踩烂的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B8A")

    Jump("loc_C00")

    label("loc_B8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_C00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_BBB")

    ChrTalk(    #22
        0xFE,
        (
            "波利真是\x01",
            "天真烂漫啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C00")

    label("loc_BBB")

    OP_A2(0x3)

    ChrTalk(    #23
        0xFE,
        (
            "居然说还想见见\x01",
            "那个白衣男人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "波利真是\x01",
            "天真烂漫啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C00")

    TalkEnd(0xFE)
    Return()

    # Function_7_821 end

    def Function_8_C04(): pass

    label("Function_8_C04")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_DF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CAF")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #25
        0x102,
        "#1040F波利，好久不见呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "咦～\x01",
            "是约修亚啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "但是，好像\x01",
            "感觉不一样～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "不过，还是\x01",
            "很帅就行了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x102,
        "#1054F哈哈……谢了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    OP_A2(0x20EC)
    Jump("loc_DF6")

    label("loc_CAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_D6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_D05")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #30
        0xFE,
        (
            "约修亚，好像\x01",
            "感觉不一样～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "不过，这个\x01",
            "也很帅就是了～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D67")

    label("loc_D05")


    ChrTalk(    #32
        0xFE,
        (
            "外面的士兵，\x01",
            "总觉得有些慌张呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "波利从后面跟他搭话，\x01",
            "竟然一下子跳起来了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "真好玩～\x02",
    )

    CloseMessageWindow()

    label("loc_D67")

    Jump("loc_DF6")

    label("loc_D6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_DB9")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #35
        0xFE,
        (
            "约修亚，好像\x01",
            "感觉不一样～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "不过，这个\x01",
            "也很帅就是了～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF6")

    label("loc_DB9")


    ChrTalk(    #37
        0xFE,
        (
            "飞船\x01",
            "就是在天上飞的船吧～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        "为什么海边会有那个～？\x02",
    )

    CloseMessageWindow()

    label("loc_DF6")

    Jump("loc_FE8")

    label("loc_DF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_E87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_E33")

    ChrTalk(    #39
        0xFE,
        (
            "最近的克拉姆，\x01",
            "很努力的帮忙干活哦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E84")

    label("loc_E33")

    OP_A2(0x2)

    ChrTalk(    #40
        0xFE,
        (
            "最近的克拉姆，\x01",
            "很努力的帮忙干活哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "不过嘛～恶作剧\x01",
            "也很努力就是了～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E84")

    Jump("loc_FE8")

    label("loc_E87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_FE8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_EC0")

    ChrTalk(    #42
        0xFE,
        (
            "白衣叔叔，\x01",
            "还没来吗～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F9D")

    label("loc_EC0")

    TurnDirection(0xFE, 0x109, 0)
    OP_A2(0x2)

    ChrTalk(    #43
        0xFE,
        "啊，是凯文老师～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "对了，老师……\x01",
            "还能再碰到白衣叔叔吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x109,
        (
            "#1064F咦……！？\x02\x03",

            "#1068F嗯、嗯～不知道啊。\x02\x03",

            "凯文老师\x01",
            "也不知道叔叔的行程表啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        "咦～好想见啊～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "因为他滴溜溜地转\x01",
            "好像很开心的样子哦～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F9D")

    Jump("loc_FE8")

    label("loc_FA0")


    ChrTalk(    #48
        0xFE,
        (
            "真想再见到\x01",
            "白衣叔叔啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "因为他滴溜溜地转\x01",
            "好像很开心的样子哦～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FE8")

    TalkEnd(0xFE)
    Return()

    # Function_8_C04 end

    def Function_9_FEC(): pass

    label("Function_9_FEC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1063")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_101F")

    ChrTalk(    #50
        0xFE,
        (
            "科洛丝姐姐，\x01",
            "还不来玩吗～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1060")

    label("loc_101F")

    OP_A2(0x1)

    ChrTalk(    #51
        0xFE,
        (
            "科洛丝姐姐，\x01",
            "还不来玩吗～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "想请她烤馅饼\x01",
            "吃得饱饱的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1060")

    Jump("loc_10D0")

    label("loc_1063")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_10D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1091")

    ChrTalk(    #53
        0xFE,
        (
            "嗯～那个白影\x01",
            "是什么呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10D0")

    label("loc_1091")

    OP_A2(0x1)

    ChrTalk(    #54
        0xFE,
        (
            "嗯～那个白影\x01",
            "是什么呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "要是幽灵\x01",
            "应该会更可怕吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10D0")

    TalkEnd(0xFE)
    Return()

    # Function_9_FEC end

    def Function_10_10D4(): pass

    label("Function_10_10D4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1591")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x416, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_140E")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(-2350, 0, 9510, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2560, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x102, -2300, 0, 8780, 270)
    SetChrPos(0x101, -2260, 0, 9660, 270)
    SetChrPos(0xF8, -1470, 0, 8720, 270)
    SetChrPos(0xF9, -1410, 0, 9580, 270)
    OP_8C(0xFE, 270, 0)
    OP_4A(0xFE, 255)
    OP_0D()
    OP_62(0x9, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #56
        0x9,
        (
            "#773F#5P呜～劈柴\x01",
            "果然好辛苦哦。\x02\x03",

            "但是，要是我不做的话\x01",
            "老师会为难的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x102,
        (
            "#1040F#2P呀，克拉姆。\x01",
            "看起来似乎很有精神啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x9, 90, 600)
    Sleep(500)

    ChrTalk(    #58
        0x9,
        (
            "#774F#6P#3S啊啊啊啊！#2S\x02\x03",

            "#3S约、约修亚哥哥！！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #59
        0x102,
        (
            "#1049F#2P好久不见了，克拉姆。\x02\x03",

            "#1040F听说你在努力帮忙干活，\x01",
            "艾丝蒂尔都告诉我了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x9,
        (
            "#770F#6P当、当然了！\x02\x03",

            "#770F除草和喂鸡\x01",
            "都没偷懒哦。\x02\x03",

            "为了老师和大家\x01",
            "我非努力不可啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x102,
        (
            "#1053F#2P嗯，就是这股志气。\x02\x03",

            "#1054F虽然现在许多事都很麻烦，\x01",
            "但还是希望你能多帮助大家。\x02\x03",

            "为了让状况尽快转好\x01",
            "我们也在拼命努力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x9,
        (
            "#771F#6P嘿嘿，明白了！\x02\x03",

            "#770F我也不能输给哥哥你们，\x01",
            "要努力才行！\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    OP_A2(0x0)
    OP_A2(0x20B2)
    EventEnd(0x0)
    OP_4B(0xFE, 255)
    Jump("loc_158E")

    label("loc_140E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_14CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1471")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #63
        0x9,
        (
            "#770F不能输给哥哥你们，\x01",
            "要努力才行！\x02\x03",

            "老师和孤儿院的大家\x01",
            "由我来守护！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14C9")

    label("loc_1471")


    ChrTalk(    #64
        0x9,
        (
            "#770F老师说了……\x01",
            "科洛丝姐姐返回王都后\x01",
            "还是在不断努力。\x02\x03",

            "#771F好～我也不能输给她！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14C9")

    Jump("loc_158E")

    label("loc_14CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1528")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #65
        0x9,
        (
            "#770F不能输给哥哥你们，\x01",
            "要努力才行！\x02\x03",

            "老师和孤儿院的大家\x01",
            "由我来守护！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_158E")

    label("loc_1528")


    ChrTalk(    #66
        0x9,
        (
            "#772F附近的海岸好像\x01",
            "停着飞船。\x02\x03",

            "我真是超级想去看，\x01",
            "但是还有活没干完……\x02\x03",

            "#773F呜～先忍耐一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_158E")

    Jump("loc_17E2")

    label("loc_1591")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x245, 7)), scpexpr(EXPR_END)), "loc_168D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_15D9")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #67
        0x9,
        (
            "#770F跟哥哥问声好哦。\x02\x03",

            "那么，赶快\x01",
            "除草吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_168A")

    label("loc_15D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1626")

    ChrTalk(    #68
        0x9,
        (
            "#770F这田里的苗\x01",
            "才刚刚种下呢。\x02\x03",

            "还很幼小柔弱\x01",
            "所以要细心除草。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_168A")

    label("loc_1626")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_168A")

    ChrTalk(    #69
        0x9,
        (
            "#770F杂草如果不连根拔起\x01",
            "很快就会再长出来的。\x02\x03",

            "看着吧，杂草们。\x01",
            "见识见识克拉姆的力量吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_168A")

    Jump("loc_17E2")

    label("loc_168D")

    TurnDirection(0xFE, 0x101, 0)
    OP_A2(0x122F)
    OP_A2(0x0)

    ChrTalk(    #70
        0x9,
        (
            "#773F呜～约修亚哥哥\x01",
            "不在一起真可惜。\x02\x03",

            "我这么努力，\x01",
            "真想让他看看……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        (
            "#1003F…………………………\x01",
            "…………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x9,
        (
            "#772F对了，艾丝蒂尔姐姐。\x02\x03",

            "如果见到哥哥，\x01",
            "一定要跟他说哦。\x02\x03",

            "我和大家一起\x01",
            "在这里努力呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#1025F克拉姆……………………\x02\x03",

            "#1006F…………嗯，明白了。\x02\x03",

            "我一定转达给约修亚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x9,
        "#770F嗯，约定了哦！\x02",
    )

    CloseMessageWindow()

    label("loc_17E2")

    TalkEnd(0xFE)
    Return()

    # Function_10_10D4 end

    def Function_11_17E6(): pass

    label("Function_11_17E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1869")
    OP_43(0xFE, 0x2, 0x0, 0xC)
    OP_22(0x191, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1869")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x38B, 1)"), scpexpr(EXPR_END)), "loc_1869")
    TalkBegin(0xFE)
    OP_A2(0x4)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #75
        "\x07\x00得到了\x1F\x8B\x03\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFE)

    label("loc_1869")

    Return()

    # Function_11_17E6 end

    def Function_12_186A(): pass

    label("Function_12_186A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1885")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_12_186A")

    label("loc_1885")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_12_186A end

    def Function_13_1890(): pass

    label("Function_13_1890")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18A9")
    Call(0, 15)

    label("loc_18A9")

    EventBegin(0x0)
    Fade(1000)
    ClearMapFlags(0x10)
    SetMapFlags(0x10000000)
    ClearMapFlags(0x1)
    SetChrFlags(0x109, 0x40)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrPos(0x101, -390, 0, 3340, 0)
    SetChrPos(0xF7, 450, 0, 2620, 0)
    OP_6D(170, 0, 3940, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(359000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #76
        0x101,
        "#1004F#5P啊啊……\x02",
    )

    CloseMessageWindow()
    OP_C8(0x200, 0x46, "C_PLAC05._CH", 0x1, 0x7D0)

    def lambda_198B():
        OP_6D(320, 0, 32530, 6000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_198B)

    def lambda_19A3():
        OP_67(0, 9500, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_19A3)

    def lambda_19BB():
        OP_6B(4210, 6000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_19BB)

    def lambda_19CB():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_19CB)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x8, 0x2)
    WaitChrThread(0x8, 0x3)
    SetChrPos(0x101, -620, 0, 17860, 0)
    SetChrPos(0xF7, 680, 70, 17860, 0)

    def lambda_1A11():
        OP_8E(0xFE, 0xFFFFFF56, 0xA, 0x69A0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1A11)
    Sleep(300)

    def lambda_1A31():
        OP_8E(0xFE, 0x438, 0x0, 0x6860, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_1A31)
    Sleep(2000)
    Fade(500)
    OP_6D(510, 0, 28590, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xF7, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 6540, 0, 33360, 230)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1AF1")

    ChrTalk(    #77
        0x106,
        (
            "#052F哦，这可真令人吃惊。\x02\x03",

            "烧成那样，\x01",
            "居然还能复原。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B32")

    label("loc_1AF1")


    ChrTalk(    #78
        0x103,
        (
            "#020F呼～听说\x01",
            "发生了纵火事件……\x02\x03",

            "这样看来\x01",
            "完全感觉不到呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B32")


    ChrTalk(    #79
        0x101,
        (
            "#1008F#6P房子都变新了，\x01",
            "还和原来一样……\x02\x03",

            "……太好了……真是。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #80
        0x8,
        "女性的声音",
        "#6P艾丝蒂尔？\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_1BB6():
        OP_6D(3480, 0, 30020, 1500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1BB6)

    def lambda_1BCE():
        OP_67(0, 9500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1BCE)
    TurnDirection(0x101, 0x8, 400)
    Sleep(300)
    TurnDirection(0xF7, 0x8, 400)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x8, 0x2)

    ChrTalk(    #81
        0x101,
        "#1018F#5P特蕾莎老师！\x02",
    )

    CloseMessageWindow()

    def lambda_1C1E():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_1C1E)

    def lambda_1C2E():
        OP_8E(0xFE, 0xC6C, 0x0, 0x7396, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1C2E)
    Sleep(200)

    def lambda_1C4E():
        OP_8E(0xFE, 0xF46, 0x0, 0x7666, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1C4E)
    Sleep(500)

    def lambda_1C6E():
        OP_8E(0xFE, 0xEE2, 0x0, 0x6E6E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_1C6E)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xF7, 0x0)
    TurnDirection(0xF7, 0x8, 400)
    WaitChrThread(0x8, 0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1DC4")

    ChrTalk(    #82
        0x8,
        (
            "#751F#2P呵呵。\x01",
            "果然是你。\x02\x03",

            "欢迎。\x01",
            "终于来了呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x106, 400)
    Sleep(500)

    ChrTalk(    #83
        0x8,
        (
            "#753F#2P还有……\x01",
            "你是阿加特？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x106,
        (
            "#051F啊啊。\x01",
            "好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x8,
        (
            "#750F#2P以前因为克拉姆的事\x01",
            "承蒙你关照了。\x02\x03",

            "那之后好久不见了。\x01",
            "那时真是承蒙关照了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x106,
        (
            "#051F#6P哪里，没事。\x02\x03",

            "倒是我到现在\x01",
            "都没来打个招呼，真是抱歉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EC6")

    label("loc_1DC4")


    ChrTalk(    #87
        0x8,
        (
            "#751F#2P呵呵。\x01",
            "果然是你。\x02\x03",

            "欢迎。\x01",
            "终于来了呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x103, 400)
    Sleep(500)

    ChrTalk(    #88
        0x8,
        (
            "#753F#2P这位是……\x01",
            "初次见面吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x103,
        (
            "#020F#6P我是这孩子的前辈，\x01",
            "游击士雪拉扎德·哈维。\x02\x03",

            "#021F我听说过不少\x01",
            "院长老师的事。\x02\x03",

            "说是茶道高人，\x01",
            "也是大家的母亲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x8,
        (
            "#751F#2P哎呀……\x01",
            "真不好意思。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EC6")


    ChrTalk(    #91
        0x101,
        (
            "#1017F#6P那、那个，孤儿院重建了，\x01",
            "真是恭喜了。\x02\x03",

            "和从前一模一样我还吃了一惊呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #92
        0x8,
        (
            "#750F#2P多亏了玛诺利亚村和从业人员们的\x01",
            "一番好意，就做成了这样。\x02\x03",

            "还是觉得这个气氛\x01",
            "才是玛西亚孤儿院啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        (
            "#1016F#6P啊哈哈……\x01",
            "嗯，真的是这样呢。\x02\x03",

            "#1017F嗯……\x01",
            "那些孩子们在里面吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x8,
        (
            "#750F#2P刚刚去玛诺利亚村\x01",
            "上学去了。\x02\x03",

            "每周有一次，巡回神父\x01",
            "会来开主日学校……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        (
            "#1015F#6P这样啊……怎么办呢。\x02\x03",

            "本想打个招呼，顺便\x01",
            "问孩子们一些事情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x8,
        (
            "#753F#2P事情……\x02\x03",

            "难道是波利看到\x01",
            "『白衣叔叔』的事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        (
            "#1011F#6P啊，大概是了！\x02\x03",

            "是吗，目击者\x01",
            "是波利啊。\x02\x03",

            "确实那孩子，\x01",
            "感觉特别敏锐呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x8,
        (
            "#751F#2P孩子们回来之前\x01",
            "请到里面等吧。\x02\x03",

            "我给你们准备茶点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x101,
        (
            "#1011F#6P谢、谢谢……\x02\x03",

            "#1003F………………………………\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_21C8")
    OP_62(0x106, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x106, 315, 400)

    ChrTalk(    #100
        0x106,
        "#052F嗯，怎么了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2208")

    label("loc_21C8")

    OP_62(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x103, 315, 400)

    ChrTalk(    #101
        0x103,
        "#023F怎么了，艾丝蒂尔？\x02",
    )

    CloseMessageWindow()

    label("loc_2208")


    ChrTalk(    #102
        0x101,
        (
            "#1025F#6P特蕾莎老师……\x02\x03",

            "约修亚的事……你都没问呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x8,
        (
            "#757F#2P…………………………\x02\x03",

            "#754F……科洛丝\x01",
            "告诉我了。\x02\x03",

            "那孩子似乎非常烦恼，\x01",
            "于是来找我商量……\x02\x03",

            "#756F艾丝蒂尔……\x01",
            "你也经受了各种痛苦呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#1026F#6P……啊…………\x02\x03",

            "#1016F啊哈哈……讨厌啦。\x02\x03",

            "……要是老师\x01",
            "安慰我……我……\x02\x03",

            "#1027F会忍不住的……\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 6)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_237A")

    ChrTalk(    #105
        0x106,
        "#552F………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_2391")

    label("loc_237A")


    ChrTalk(    #106
        0x103,
        "#522F艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    label("loc_2391")


    ChrTalk(    #107
        0x8,
        (
            "#754F#2P…………………………\x02\x03",

            "#750F不需要忍耐。\x02\x03",

            "因为最重要的人\x01",
            "从自己身边消失了啊……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_23F3():
        OP_6D(3360, 0, 29840, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_23F3)
    OP_8E(0x8, 0xDAC, 0x0, 0x742C, 0x3E8, 0x0)
    SetChrChipByIndex(0x8, 7)
    SetChrSubChip(0x8, 0)
    OP_99(0x8, 0x0, 0x1, 0x3E8)
    Sleep(500)

    ChrTalk(    #108
        0x101,
        "#1027F#6P……啊………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x8,
        (
            "#754F#2P什么也不用说了……\x02\x03",

            "虽然无法\x01",
            "代替你的母亲……\x02\x03",

            "暂时就这样……\x01",
            "让我抱着你吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_24AC():
        OP_6D(-150, 0, 38820, 4000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_24AC)

    def lambda_24C4():
        OP_67(0, 9500, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_24C4)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    NewScene("ED6_DT21/T2412   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_24F4")

    Return()

    # Function_13_1890 end

    def Function_14_24F5(): pass

    label("Function_14_24F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2506")
    Call(0, 15)

    label("loc_2506")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x101, 470, 0, -2190, 0)
    SetChrPos(0xF7, -200, 0, -3480, 8)
    SetChrPos(0x109, 1300, 0, -2780, 0)
    SetChrPos(0x8, 390, 0, 480, 185)
    SetChrPos(0x9, 1160, 0, -90, 196)
    SetChrPos(0xA, -80, 0, 940, 186)
    SetChrPos(0xB, -1070, 0, 370, 193)
    SetChrPos(0xC, 2210, 0, 150, 208)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    OP_6D(1020, 0, -510, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2672")

    ChrTalk(    #110
        0x8,
        (
            "#750F艾丝蒂尔、阿加特。\x02\x03",

            "在卢安地区期间，\x01",
            "方便的话请再来吧。\x02\x03",

            "神父有课的时候\x01",
            "也请务必来走走。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26E2")

    label("loc_2672")


    ChrTalk(    #111
        0x8,
        (
            "#750F艾丝蒂尔。\x01",
            "雪拉扎德小姐。\x02\x03",

            "在卢安地区期间，\x01",
            "方便的话请再来吧。\x02\x03",

            "神父也是，授课的时候\x01",
            "也请务必来走走。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26E2")


    ChrTalk(    #112
        0x101,
        "#1017F#6P嗯，我们会的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x109,
        (
            "#1061F呀～有机会\x01",
            "我会再来拜访的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x9,
        (
            "#771F凯文哥哥，再见哦！\x02\x03",

            "#770F还有艾丝蒂尔姐姐！\x02\x03",

            "下次要把约修亚哥哥\x01",
            "一起带来哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x101,
        (
            "#1016F#6P啊，嗯……\x02\x03",

            "#1006F虽然不知道要到什么时候，\x01",
            "但一定会一起来玩的！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/R2200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_24F5 end

    def Function_15_27E8(): pass

    label("Function_15_27E8")

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
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2862"),
        (1, "loc_2868"),
        (SWITCH_DEFAULT, "loc_286E"),
    )


    label("loc_2862")

    OP_A2(0x1200)
    Jump("loc_286E")

    label("loc_2868")

    OP_A2(0x1201)
    Jump("loc_286E")

    label("loc_286E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_287C")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_2880")

    label("loc_287C")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_2880")

    Return()

    # Function_15_27E8 end

    SaveToFile()

Try(main)
