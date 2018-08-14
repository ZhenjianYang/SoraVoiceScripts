from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T0400   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0400.x',
        MapIndex            = 13,
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
        '牛',                                   # 9
        '牛',                                   # 10
        '鸡',                                   # 11
        '鸡',                                   # 12
        '鸡',                                   # 13
        '鸡',                                   # 14
        '约修亚',                               # 15
        '缇欧',                                 # 16
        '伊莉莎',                               # 17
        '弗兰兹',                               # 18
        '汉娜',                                 # 19
        '小婴儿',                               # 20
        '临时',                                 # 21
        '目标用照相机',                         # 22
        '米尔西街道方向',                       # 23
        '',                                     # 24
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
        'ED6_DT07/CH01710 ._CH',             # 00
        'ED6_DT07/CH01720 ._CH',             # 01
        'ED6_DT07/CH02750 ._CH',             # 02
        'ED6_DT07/CH02740 ._CH',             # 03
        'ED6_DT07/CH02730 ._CH',             # 04
        'ED6_DT07/CH01020 ._CH',             # 05
        'ED6_DT07/CH01030 ._CH',             # 06
        'ED6_DT26/CH20790 ._CH',             # 07
        'ED6_DT26/CH20791 ._CH',             # 08
        'ED6_DT26/CH20792 ._CH',             # 09
        'ED6_DT26/CH20793 ._CH',             # 0A
        'ED6_DT26/CH20788 ._CH',             # 0B
        'ED6_DT26/CH20789 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT07/CH01710P._CP',             # 00
        'ED6_DT07/CH01720P._CP',             # 01
        'ED6_DT07/CH02750P._CP',             # 02
        'ED6_DT07/CH02740P._CP',             # 03
        'ED6_DT07/CH02730P._CP',             # 04
        'ED6_DT07/CH01020P._CP',             # 05
        'ED6_DT07/CH01030P._CP',             # 06
        'ED6_DT26/CH20790P._CP',             # 07
        'ED6_DT26/CH20791P._CP',             # 08
        'ED6_DT26/CH20792P._CP',             # 09
        'ED6_DT26/CH20793P._CP',             # 0A
        'ED6_DT26/CH20788P._CP',             # 0B
        'ED6_DT26/CH20789P._CP',             # 0C
    )

    DeclNpc(
        X                   = 39010,
        Z                   = 600,
        Y                   = 22850,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x105,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 48160,
        Z                   = 460,
        Y                   = 18800,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x105,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 0,
        Y                   = 18540,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 38780,
        Z                   = 0,
        Y                   = 19310,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 51470,
        Z                   = 0,
        Y                   = 20950,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 51470,
        Z                   = 0,
        Y                   = 20950,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 40470,
        Z                   = 0,
        Y                   = 16320,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 21900,
        Z                   = 0,
        Y                   = 25300,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 27590,
        Z                   = -60,
        Y                   = 34960,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 27590,
        Z                   = -60,
        Y                   = 34960,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 27590,
        Z                   = -60,
        Y                   = 34960,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1C4,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xCC,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 23910,
        Z                   = 30,
        Y                   = 66820,
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


    ScpFunction(
        "Function_0_2F2",          # 00, 0
        "Function_1_330",          # 01, 1
        "Function_2_34A",          # 02, 2
        "Function_3_4C7",          # 03, 3
        "Function_4_614",          # 04, 4
        "Function_5_63A",          # 05, 5
        "Function_6_654",          # 06, 6
        "Function_7_65A",          # 07, 7
        "Function_8_13DB",         # 08, 8
        "Function_9_2D00",         # 09, 9
        "Function_10_2D53",        # 0A, 10
        "Function_11_2D9C",        # 0B, 11
        "Function_12_39F7",        # 0C, 12
    )


    def Function_0_2F2(): pass

    label("Function_0_2F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_31D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xC0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 11)
    Jump("loc_32F")

    label("loc_31D")

    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 7)

    label("loc_32F")

    Return()

    # Function_0_2F2 end

    def Function_1_330(): pass

    label("Function_1_330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 0)), scpexpr(EXPR_END)), "loc_340")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_340")

    OP_B1("T0400_0")
    Return()

    # Function_1_330 end

    def Function_2_34A(): pass

    label("Function_2_34A")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36F")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_4B1")

    label("loc_36F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_388")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_4B1")

    label("loc_388")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A1")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_4B1")

    label("loc_3A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BA")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_4B1")

    label("loc_3BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D3")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_4B1")

    label("loc_3D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EC")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_4B1")

    label("loc_3EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_405")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_4B1")

    label("loc_405")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41E")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_4B1")

    label("loc_41E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_437")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_4B1")

    label("loc_437")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_450")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_4B1")

    label("loc_450")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_469")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_4B1")

    label("loc_469")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_482")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_4B1")

    label("loc_482")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49B")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_4B1")

    label("loc_49B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B1")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_4B1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4C6")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_4B1")

    label("loc_4C6")

    Return()

    # Function_2_34A end

    def Function_3_4C7(): pass

    label("Function_3_4C7")

    SetChrFlags(0xFE, 0x40)
    OP_8D(0xFE, 28710, 33610, 41830, 44000, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_613")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D8")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x7026), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_PUSH_LONG, 0x834A), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0xA366), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0xABE0), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5AD")
    SetChrFlags(0xFE, 0x20)
    TurnDirection(0xFE, 0x0, 0)
    ClearChrFlags(0xFE, 0x20)

    def lambda_59A():
        OP_94(0x0, 0xFE, 0xB4, 0x12C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_59A)
    Jump("loc_5D0")

    label("loc_5AD")


    def lambda_5B3():
        OP_8D(0xFE, 28710, 33610, 41830, 44000, 6000)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5B3)
    Sleep(200)

    label("loc_5D0")

    Sleep(30)
    Jump("loc_610")

    label("loc_5D8")

    Sleep(50)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_610")
    OP_44(0xFE, 0x2)

    def lambda_5F8():
        OP_8D(0xFE, 28710, 33610, 41830, 44000, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5F8)

    label("loc_610")

    Jump("loc_4F0")

    label("loc_613")

    Return()

    # Function_3_4C7 end

    def Function_4_614(): pass

    label("Function_4_614")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_62F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_4_614")

    label("loc_62F")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_4_614 end

    def Function_5_63A(): pass

    label("Function_5_63A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_653")
    OP_43(0xFE, 0x2, 0x0, 0x4)
    OP_22(0x191, 0x0, 0x64)

    label("loc_653")

    Return()

    # Function_5_63A end

    def Function_6_654(): pass

    label("Function_6_654")

    OP_22(0x190, 0x0, 0x64)
    Return()

    # Function_6_654 end

    def Function_7_65A(): pass

    label("Function_7_65A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    OP_6D(24110, 20, 51410, 0)
    OP_67(0, 7600, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x19, 24530, 110, 32759, 0)
    SetChrPos(0x17, 25060, 140, 34870, 180)
    SetChrPos(0x18, 23990, 130, 34570, 180)
    SetChrPos(0x101, 24480, 100, 57310, 180)
    SetChrPos(0x16, 23730, 80, 58020, 180)

    def lambda_712():
        OP_8E(0xFE, 0x5FA0, 0xA, 0x8FFC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_712)
    Sleep(50)

    def lambda_732():
        OP_8E(0xFE, 0x5C4E, 0x0, 0x92E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_732)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_757():
        OP_6D(24700, 40, 35720, 3500)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_757)

    def lambda_76F():
        OP_67(0, 6840, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_76F)

    def lambda_787():
        OP_6C(24000, 3500)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_787)
    WaitChrThread(0x1D, 0x0)
    Sleep(400)
    OP_62(0x17, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(100)
    OP_62(0x18, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(120)
    OP_62(0x19, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_7E6():
        OP_8C(0xFE, 0, 500)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_7E6)
    Sleep(50)
    OP_8C(0x18, 0, 500)

    ChrTalk(    #0
        0x18,
        (
            "啊，艾丝蒂尔～。\x01",
            "约修亚也来了～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x17,
        (
            "#2P哎呀呀，\x01",
            "看来是被硬拉来的呢。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #2
        0x101,
        (
            "#290F#5P呀嗬——！\x02\x03",

            "缇欧，叔叔，\x01",
            "我们来帮忙了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x19,
        "哦哦，来了吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x19,
        (
            "哎呀，真是不好意思，\x01",
            "汉娜生产的时候也多亏你的帮忙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        (
            "#291F#5P这点小事不值一提啦。\x02\x03",

            "交给我艾丝蒂尔大人\x01",
            "根本就是易如反掌嘛！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x19,
        "哈哈，真是可靠啊。\x02",
    )

    CloseMessageWindow()
    OP_62(0x19, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(    #7
        0x19,
        "哦，这位是……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x17,
        "#2P啊啊，是艾丝蒂尔的弟弟。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x17,
        (
            "#2P之前不是说过的吗。\x01",
            "他叫约修亚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x19,
        (
            "哦哦，\x01",
            "这么说来好像的确听说过啊……\x02\x03",

            "记得是和艾丝蒂尔\x01",
            "大吵一架的那个来着……\x02",
        )
    )

    Jump("loc_A65")

    label("loc_A65")

    CloseMessageWindow()

    ChrTalk(    #11
        0x16,
        "#1677F………………………………\x02",
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, 24530, 170, 26700, 0)
    SetChrChipByIndex(0x1A, 7)
    SetChrSubChip(0x1A, 0)
    Sleep(1000)

    def lambda_AC1():

        label("loc_AC1")

        TurnDirection(0xFE, 0x1A, 400)
        OP_48()
        Jump("loc_AC1")

    QueueWorkItem2(0x19, 2, lambda_AC1)
    Sleep(50)

    def lambda_AD7():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_AD7)
    Sleep(50)

    def lambda_AEA():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_AEA)
    Sleep(1000)

    def lambda_AFD():
        OP_8E(0xFE, 0x5FD2, 0x6E, 0x7F58, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_AFD)
    Sleep(2000)

    def lambda_B1D():
        OP_8F(0xFE, 0x6400, 0x168, 0x7F58, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_B1D)

    ChrTalk(    #12
        0x101,
        "#290F#5P啊，汉娜阿姨！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x18,
        "#5P您好～。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x1A, 0x1)
    Sleep(200)

    ChrTalk(    #14
        0x1A,
        "#6P啊，你们好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x1A,
        (
            "#6P今天真是对不住你们俩了。\x01",
            "又让你们来帮忙。\x02\x03",

            "我也想早点恢复起来\x01",
            "继续干农活呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x19,
        (
            "#11P喂、喂喂。\x01",
            "现在还不能干活哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x1A,
        (
            "#6P没什么啦，生缇欧的时候，\x01",
            "早就可以干活了呢。\x02\x03",

            "干活的时候就这样\x01",
            "把还是小婴儿的你背在背上……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x17, 500)

    ChrTalk(    #18
        0x18,
        "#3P是、是这样吗？？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x17, 0x18, 500)

    ChrTalk(    #19
        0x17,
        "#11P不知道。不记得啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x1A,
        (
            "#6P不过，\x01",
            "双胞胎的话果然还是没办法……\x02",
        )
    )

    Jump("loc_D21")

    label("loc_D21")

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x1A, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #21
        0x1A,
        "#6P哦？这个黑头发的孩子是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x19,
        (
            "#11P啊，他是约修亚哦。\x02\x03",

            "喏，就是之前缇欧说过的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x1A,
        "#6P啊，是艾丝蒂尔的弟弟吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x1A,
        (
            "#6P哎呀，\x01",
            "还真是可爱的孩子啊。\x02",
        )
    )

    Jump("loc_E0C")

    label("loc_E0C")

    CloseMessageWindow()

    ChrTalk(    #25
        0x16,
        "#1676F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x1A,
        (
            "#6P你也是来帮忙的吗？\x01",
            "真是麻烦你了……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1A, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #27
        0x1A,
        (
            "#6P啊，仔细一看，\x01",
            "怎么还裹着绷带呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_EBE():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_EBE)
    Sleep(100)

    def lambda_ED1():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_ED1)
    Sleep(120)
    OP_44(0x19, 0x2)
    OP_8C(0x19, 0, 500)

    ChrTalk(    #28
        0x19,
        (
            "哦哦，真的。\x01",
            "我都没有注意到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x16,
        (
            "#1676F………………………………\x02\x03",

            "#1671F……伤已经差不多都好了。\x01",
            "不会影响工作的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x19,
        (
            "不不，可不能勉强哦。\x01",
            "还是在哪儿休息一下……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1A, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #31
        0x1A,
        "#6P对了，我有个好主意。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x16, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    def lambda_1015():
        OP_6B(2600, 3000)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_1015)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(25360, 260, 40170, 0)
    OP_67(0, 6570, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(24000, 0)
    OP_6E(262, 0)
    SetChrPos(0x18, 25600, 270, 39300, 180)
    SetChrPos(0x17, 24710, 80, 39730, 180)
    SetChrPos(0x101, 23640, 0, 39430, 180)
    SetChrPos(0x16, 24610, 170, 41190, 180)
    SetChrChipByIndex(0x16, 8)
    SetChrSubChip(0x16, 1)
    SetChrPos(0x19, 25170, 160, 36800, 0)
    SetChrPos(0x1A, 24070, 110, 36720, 0)
    SetChrChipByIndex(0x1A, 6)
    SetChrSubChip(0x1A, 0)
    Sleep(500)
    SetMessageWindowPos(280, 250, -1, -1)
    SetChrName("弗兰兹")

    AnonymousTalk(    #32
        (
            "\x07\x00那么我来说明一下收割的安排。\x02\x03",

            "艾丝蒂尔，伊莉莎，\x01",
            "还有缇欧三个人\x01",
            "负责收割这边的田地。\x02\x03",

            "分工合作效率比较高哦。\x01",
            "最好从北边开始收割。\x02",
        )
    )

    Jump("loc_11A0")

    label("loc_11A0")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 280, -1, -1)
    SetChrName("汉娜")

    AnonymousTalk(    #33
        (
            "\x07\x00温室的蔬菜，\x01",
            "就由我和弗兰兹\x01",
            "两个人来收割。\x02\x03",

            "……还有，约修亚……\x02",
        )
    )

    Jump("loc_120B")

    label("loc_120B")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(1000)

    def lambda_1222():
        OP_6B(2700, 2500)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_1222)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x1D, 0x1)

    ChrTalk(    #34
        0x1A,
        "就拜托你照顾孩子们吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x1A,
        (
            "……男孩子叫维鲁，\x01",
            "女孩子叫查儿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x16,
        (
            "#1677F#5P………………………………\x02\x03",

            "#1671F…………明白了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x19,
        "那就开始工作吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x19,
        (
            "如果有什么不明白的，\x01",
            "可以随时来问我哦。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)

    ChrTalk(    #39
        0x17,
        "#1P好～。\x02",
    )

    Jump("loc_1348")

    label("loc_1348")

    Sleep(50)

    ChrTalk(    #40
        0x18,
        "#4P好～！\x02",
    )

    Jump("loc_1366")

    label("loc_1366")

    Sleep(50)

    ChrTalk(    #41
        0x101,
        "#3P好～！\x02",
    )

    Jump("loc_1389")

    label("loc_1389")

    OP_56(0x1)
    OP_59()

    ChrTalk(    #42
        0x16,
        "#1677F#5P…………………………\x02",
    )

    CloseMessageWindow()

    def lambda_13BC():
        OP_6B(2880, 3000)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_13BC)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    Call(0, 8)
    Return()

    # Function_7_65A end

    def Function_8_13DB(): pass

    label("Function_8_13DB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x16, 8)
    SetChrSubChip(0x16, 1)
    SetChrPos(0x16, 50120, 500, 26010, 225)
    OP_6D(50620, 0, 27300, 0)
    OP_67(0, 6380, -10000, 0)
    OP_6B(2980, 0)
    OP_6C(18000, 0)
    OP_6E(262, 0)

    def lambda_1454():
        OP_6B(2880, 3000)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_1454)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #43
        0x16,
        "#1675F………………………………\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x1D, 0x0)
    Sleep(300)
    OP_20(0xBB8)
    Fade(2500)
    SetChrPos(0x16, 80120, 500, 26010, 225)
    SetChrChipByIndex(0x16, 2)
    SetChrSubChip(0x16, 0)
    OP_6D(80620, 0, 27300, 0)
    OP_67(0, 6380, -10000, 0)
    OP_6B(2880, 0)
    OP_6C(18000, 0)
    OP_6E(262, 0)
    Sleep(3500)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(    #44
        "\x18\x07\x0C这几个星期来，都没有追兵的气息……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #45
        "\x18\x07\x0C为什么…………\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #46
        (
            "\x18\x07\x0C我身在何处，\x01",
            "他们应该早就知道了……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #47
        "\x18\x07\x0C难道已经不再关注我了吗？\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #48
        (
            "\x18\x07\x0C…………所以……\x01",
            "只消除了我的记忆，把我抛弃了……？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #49
        "\x18\x07\x0C不，但是……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #50
        "\x18\x07\x0C是什么……有什么很重要的东西……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #51
        (
            "\x18\x07\x0C…………感觉好像失去了\x01",
            "什么很重要的东西……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #52
        "\x18\x07\x0C是什么……………………\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #53
        "\x18\x07\x0C我，到底……失去了什么……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("声音")

    AnonymousTalk(    #54
        "\x07\x00#1S……约……亚……！#2S\x02",
    )

    Jump("loc_173A")

    label("loc_173A")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(    #55
        "\x18\x07\x0C……到底，是什么…………\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("活泼的声音")

    AnonymousTalk(    #56
        "\x07\x00#3S……约修亚！#2S\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("约修亚")

    ChrTalk(    #57
        0x16,
        "#5P咦………………\x02",
    )

    Jump("loc_17F4")

    label("loc_17F4")

    CloseMessageWindow()
    SetChrPos(0x101, 49080, 140, 25500, 75)
    Fade(1500)
    SetChrPos(0x16, 50120, 500, 26010, 225)
    SetChrChipByIndex(0x16, 8)
    SetChrSubChip(0x16, 1)
    OP_6D(50620, 0, 27300, 0)
    OP_67(0, 6380, -10000, 0)
    OP_6B(2880, 0)
    OP_6C(18000, 0)
    OP_6E(262, 0)
    Sleep(2000)

    NpcTalk(    #58
        0x101,
        "活泼的少女",
        "我说，约修亚！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x16,
        (
            "#1678F#11P…………………………\x02\x03",

            "………………艾丝蒂尔……？\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_1D(0xF)
    Sleep(500)

    ChrTalk(    #60
        0x101,
        "#290F#6P喏，来看这个！\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #61
        "\x07\x05艾丝蒂尔拿出一根大萝卜。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #62
        0x101,
        (
            "#291F#6P怎么样，很厉害吧。\x01",
            "这是我拔出来的哦！\x02\x03",

            "这个茄子也是……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #63
        0x101,
        "#291F#6P………新鲜水灵！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x16,
        (
            "#1671F#11P…………………………\x02\x03",

            "…………我说啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        "#290F#6P嗯？　什么？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x16,
        (
            "#1671F#11P……………………\x02\x03",

            "#1677F唉………………\x02\x03",

            "…………艾丝蒂尔，\x01",
            "你膝盖擦破了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        "#293F#6P哎…………？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x16,
        (
            "#1677F#11P你总是\x01",
            "不顾一切往前冲……\x02\x03",

            "#1689F来，膝盖给我看看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        "#290F#6P嗯、嗯……\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x16, 0x20)
    OP_8C(0x16, 150, 300)
    Sleep(500)
    OP_22(0x8F, 0x0, 0x46)
    Fade(1000)
    SetChrChipByIndex(0x16, 11)
    SetChrSubChip(0x16, 3)
    ClearChrFlags(0x16, 0x20)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, 50780, 420, 25700, 45)
    SetChrPos(0x1C, 50780, 420, 25700, 45)
    OP_0D()
    Sleep(500)
    Fade(300)
    SetChrChipByIndex(0x16, 2)
    SetChrSubChip(0x16, 0)
    OP_0D()
    TurnDirection(0x16, 0x101, 400)

    def lambda_1BBB():
        OP_8F(0xFE, 0xC256, 0x154, 0x6464, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_1BBB)
    WaitChrThread(0x16, 0x1)
    Fade(300)
    SetChrChipByIndex(0x16, 11)
    SetChrSubChip(0x16, 3)
    OP_0D()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #70
        "\x07\x05约修亚取出消毒液。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #71
        0x101,
        (
            "#297F#6P呜……！\x02\x03",

            "好、好痛……\x02",
        )
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    Sleep(600)

    def lambda_1C72():
        OP_9E(0xFE, 0xF, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1C72)
    CloseMessageWindow()

    ChrTalk(    #72
        0x16,
        (
            "#1676F#11P这点小痛，忍着点啦。\x02\x03",

            "#1675F（真是的，总是弄得满身伤痕。）\x02\x03",

            "（之前我就在想，\x01",
            "　她不会得破伤风什么的吗？）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        "#293F#6P？？？　约修亚？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x16,
        "#1677F#11P……真是的，老给人添麻烦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        (
            "#292F#6P呜～…………\x02\x03",

            "#294F我可没求你\x01",
            "给我处理伤口啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x16,
        (
            "#1670F#11P所以说你给人添麻烦啊。\x02\x03",

            "又不自己处理，\x01",
            "又不告诉别人。\x02\x03",

            "#1676F每次看着你，\x01",
            "总觉得危险重重令人担心……\x02\x03",

            "………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #77 op#A
        0x101,
        (
            "#293F#6P#25A我说，约修亚……\x01",
            "约修亚为什么……\x02\x02",
        )
    )

    Sleep(2300)
    SetChrSubChip(0x16, 2)
    Sleep(200)

    ChrTalk(    #78
        0x16,
        "#1678F#11P（啊，指甲也破了。）\x02",
    )

    OP_56(0x1)
    OP_59()
    Sleep(500)

    ChrTalk(    #79
        0x101,
        (
            "#297F#6P……哇！\x02\x03",

            "#294F消、消毒之前\x01",
            "先说一声嘛！\x02",
        )
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    Sleep(600)

    def lambda_1F57():
        OP_9E(0xFE, 0xF, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1F57)
    CloseMessageWindow()

    ChrTalk(    #80
        0x16,
        "#1679F#11P………………………………\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #81
        "\x07\x05约修亚简单处理了一下伤口。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()
    Fade(300)
    SetChrChipByIndex(0x16, 2)
    SetChrSubChip(0x16, 0)
    OP_0D()

    def lambda_1FF5():
        OP_8F(0xFE, 0xC3C8, 0x1F4, 0x659A, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_1FF5)
    WaitChrThread(0x16, 0x1)
    Sleep(300)

    ChrTalk(    #82
        0x16,
        (
            "#1676F#11P好，完成了。\x02\x03",

            "今后也要多注意点，\x01",
            "别总是把自己弄伤……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x1B,
        "呜…………\x02",
    )

    CloseMessageWindow()
    OP_43(0x1B, 0x3, 0x0, 0xA)

    ChrTalk(    #84
        0x1B,
        "哇——哇——！\x02",
    )

    OP_7C(0x0, 0x32, 0xBB8, 0x12C)
    CloseMessageWindow()
    OP_8C(0x16, 150, 500)
    OP_62(0x1B, 0x190, 800, 0x28, 0x2B, 0x64, 0x0)
    Sleep(100)
    OP_62(0x1C, 0x0, 1100, 0x28, 0x2B, 0x64, 0x0)

    ChrTalk(    #85
        0x1B,
        "#2P哇——哇——！！\x02",
    )

    OP_7C(0x0, 0x32, 0xBB8, 0x12C)
    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #86
        0x101,
        (
            "#293F#6P啊啊，哭起来了！\x02\x03",

            "#295F呃……怎么办啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x16,
        (
            "#1679F#5P…………你别管啦。\x01",
            "照顾小孩是我的工作。\x02\x03",

            "你回去做自己的事吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x101,
        "#296F#6P但、但是…………\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(300)
    SetChrChipByIndex(0x16, 11)
    SetChrSubChip(0x16, 3)
    OP_0D()
    Sleep(500)
    OP_22(0x8F, 0x0, 0x46)
    Fade(1000)
    SetChrChipByIndex(0x16, 8)
    SetChrSubChip(0x16, 1)
    SetChrPos(0x1B, 49900, 760, 25900, 225)
    SetChrPos(0x1C, 49900, 760, 25900, 225)
    SetChrFlags(0x1B, 0x8)
    OP_63(0x1B)
    OP_63(0x1C)
    OP_0D()
    SetChrFlags(0x16, 0x20)
    OP_8C(0x16, 225, 300)
    ClearChrFlags(0x16, 0x20)
    OP_62(0x1B, 0xFFFFFF38, 1200, 0x28, 0x2B, 0x64, 0x0)
    Sleep(100)
    OP_62(0x1C, 0xC8, 1000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(300)

    ChrTalk(    #89
        0x1B,
        "#4P哇——哇……\x02",
    )

    CloseMessageWindow()
    OP_44(0x1B, 0x3)

    def lambda_229F():
        OP_9E(0xFE, 0x0, 0xA, 0x3E8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x16, 3, lambda_229F)
    Sleep(1500)

    def lambda_22BE():
        OP_9E(0xFE, 0x0, 0xA, 0x3E8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x16, 3, lambda_22BE)
    Sleep(1500)
    OP_63(0x1B)
    OP_63(0x1C)
    Sleep(1000)
    OP_23(0x184)

    ChrTalk(    #90
        0x1B,
        "#4P…………呜……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #91
        0x101,
        (
            "#293F#6P不、不哭了！\x02\x03",

            "约修亚，你是妈妈吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x16,
        (
            "#1677F#11P……说什么呢。\x02\x03",

            "#1679F赶快回去工作吧，\x01",
            "不然什么时候才做得完啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        (
            "#290F#6P嗯、嗯。\x02\x03",

            "#291F……约修亚，谢谢哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 225, 500)

    def lambda_2405():
        OP_8E(0xFE, 0xA87A, 0xA, 0x4E48, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2405)
    WaitChrThread(0x101, 0x1)
    OP_62(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x16)

    ChrTalk(    #94
        0x16,
        "#1675F#11P#40W……『谢谢』吗…………\x02",
    )

    CloseMessageWindow()
    OP_62(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x16)
    OP_20(0xBB8)
    SetChrFlags(0x16, 0x20)
    OP_8C(0x16, 150, 300)
    Sleep(500)
    OP_22(0x8F, 0x0, 0x46)
    Fade(1000)
    SetChrChipByIndex(0x16, 11)
    SetChrSubChip(0x16, 3)
    ClearChrFlags(0x16, 0x20)
    ClearChrFlags(0x1B, 0x8)
    SetChrPos(0x1B, 50780, 420, 25700, 45)
    OP_0D()
    Sleep(500)
    Fade(300)
    SetChrChipByIndex(0x16, 2)
    SetChrSubChip(0x16, 0)
    OP_0D()
    OP_8C(0x16, 225, 400)
    Fade(300)
    SetChrFlags(0x16, 0x2)
    SetChrChipByIndex(0x16, 10)
    SetChrSubChip(0x16, 2)
    OP_0D()
    Fade(300)
    SetChrSubChip(0x16, 10)
    OP_0D()
    Sleep(2000)
    Fade(1000)
    OP_6B(2780, 0)
    SetChrSubChip(0x16, 7)
    OP_0D()
    Sleep(300)
    OP_43(0x16, 0x3, 0x0, 0x9)
    OP_1D(0x4A)
    Sleep(2500)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrPos(0x17, 49740, -170, 50680, 100)
    SetChrPos(0x101, 49970, -290, 40830, 110)
    SetChrPos(0x18, 42240, -200, 41770, 280)
    OP_43(0x17, 0x0, 0x0, 0x2)
    OP_43(0x101, 0x0, 0x0, 0x2)
    OP_43(0x18, 0x0, 0x0, 0x2)
    Fade(4000)
    OP_44(0x1D, 0xFF)
    OP_6D(24450, 0, 24100, 0)
    OP_67(0, 7560, -10000, 0)
    OP_6B(3620, 0)
    OP_6C(318000, 0)
    OP_6E(504, 0)

    def lambda_25D0():
        OP_6D(44250, 0, 44300, 20000)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_25D0)

    def lambda_25E8():
        OP_6C(340000, 20000)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_25E8)
    OP_77(0xFF, 0x97, 0x8A, 0x0, 0x4E20)
    WaitChrThread(0x1D, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(43260, 70, 20300, 0)
    OP_67(0, 6360, -10000, 0)
    OP_6B(2880, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 41720, 0, 18800, 45)
    SetChrPos(0x18, 41720, 0, 17800, 45)
    SetChrPos(0x17, 40720, 0, 18800, 45)
    OP_44(0x101, 0x0)
    OP_44(0x18, 0x0)
    OP_44(0x17, 0x0)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x18, 0)
    SetChrSubChip(0x17, 0)
    Sleep(2000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #95
        0x18,
        (
            "啊啊…………\x02\x03",

            "……好帅……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x17,
        (
            "#6P竟然身怀这种绝技……\x02\x03",

            "而且还背对着夕阳。\x01",
            "这简直就是犯规嘛～。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x17,
        (
            "#6P艾丝蒂尔，\x01",
            "你知道那孩子会吹口琴吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        (
            "#5P#292F唔唔唔…………\x02\x03",

            "约修亚这小子，\x01",
            "身为弟弟居然瞒着我……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #99
        0x101,
        (
            "#5P#294F#3S太小看人了！\x01",
            "约修亚大笨蛋！！#2S\x02",
        )
    )

    Sleep(150)
    OP_7C(0x0, 0x64, 0xBB8, 0x12C)
    CloseMessageWindow()
    OP_62(0x18, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x17, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #100
        0x18,
        "艾丝蒂尔真是的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x17,
        "#6P……生什么气呢……\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    SetChrPos(0x16, 50120, 500, 26010, 225)
    OP_6D(50620, 0, 27300, 0)
    OP_67(0, 6380, -10000, 0)
    OP_6B(2880, 0)
    OP_6C(18000, 0)
    OP_6E(262, 0)
    OP_0D()

    def lambda_28CD():
        OP_6B(2780, 8000)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_28CD)
    Sleep(2000)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x1B, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x1B, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x1B, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x6, 0x0, 0x64)
    Sleep(100)
    OP_20(0x0)
    FadeToDark(0, 0, -1)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("声音")

    AnonymousTalk(    #102
        "\x07\x02#40W哎呀，你好。\x02",
    )

    Jump("loc_2967")

    label("loc_2967")

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("声音")

    AnonymousTalk(    #103
        (
            "\x07\x02#40W……不用这么戒备啦。\x01",
            "我是魔法师。\x02",
        )
    )

    Jump("loc_29A7")

    label("loc_29A7")

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("声音")

    AnonymousTalk(    #104
        "\x07\x02#40W让我治愈你的心灵吧。\x02",
    )

    Jump("loc_29DA")

    label("loc_29DA")

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("声音")

    AnonymousTalk(    #105
        (
            "\x07\x02#40W只不过…………#500W\x01",
            "#40W需要付出代价哦？\x02",
        )
    )

    Jump("loc_2A21")

    label("loc_2A21")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    OP_1D(0xB2)
    Sleep(1500)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #106
        "\x18\x07\x0C#40W………………终于明白了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #107
        "\x18\x07\x0C#40W我已经付出过代价了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #108
        (
            "\x18\x07\x0C#40W重要的东西，幸福的时光……\x01",
            "以及保持自我的全部……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #109
        (
            "\x18\x07\x0C#40W我是人偶……\x01",
            "被破坏扭曲的碎片。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #110
        "\x18\x07\x0C#40W仅仅为了破坏别人最重要的东西，而存在。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #111
        "\x18\x07\x0C#40W…………我必须离开。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #112
        "\x18\x07\x0C#40W这个世界，一定会被我破坏。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #113
        (
            "\x18\x07\x0C#40W如果是最重要的东西，\x01",
            "就不能放在身边。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #114
        (
            "\x18\x07\x0C#40W必须放在我的手触碰不到的地方，\x01",
            "远远离开我才行。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #115
        (
            "\x18\x07\x0C#40W在我…………\x01",
            "在我的黑暗污染此地之前。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #116
        "\x18\x07\x0C#40W…………我必须离开。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #117
        "\x18\x07\x0C#40W在我的存在伤害她之前――\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_C4(0x1, 0x800)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(1000)
    OP_20(0x1388)
    OP_21()
    Sleep(2000)
    NewScene("ED6_DT21/T0100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_13DB end

    def Function_9_2D00(): pass

    label("Function_9_2D00")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D52")
    SetChrSubChip(0x16, 7)
    Sleep(250)
    SetChrSubChip(0x16, 15)
    Sleep(250)
    SetChrSubChip(0x16, 23)
    Sleep(250)
    SetChrSubChip(0x16, 31)
    Sleep(250)
    SetChrSubChip(0x16, 39)
    Sleep(250)
    SetChrSubChip(0x16, 47)
    Sleep(250)
    SetChrSubChip(0x16, 55)
    Sleep(250)
    Jump("Function_9_2D00")

    label("loc_2D52")

    Return()

    # Function_9_2D00 end

    def Function_10_2D53(): pass

    label("Function_10_2D53")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D9B")
    OP_22(0x184, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x184, 0x0, 0x5A)
    Sleep(1100)
    OP_22(0x184, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x184, 0x0, 0x64)
    Sleep(1200)
    OP_22(0x184, 0x0, 0x5A)
    Sleep(1000)
    OP_22(0x184, 0x0, 0x5A)
    Sleep(1300)
    Jump("Function_10_2D53")

    label("loc_2D9B")

    Return()

    # Function_10_2D53 end

    def Function_11_2D9C(): pass

    label("Function_11_2D9C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(26470, 130, 44280, 0)
    OP_67(0, 7580, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(237000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 27520, -70, 41470, 90)
    SetChrPos(0x155, 25510, 320, 53280, 180)

    def lambda_2E12():
        OP_6B(2840, 2000)
        ExitThread()

    QueueWorkItem(0x1D, 3, lambda_2E12)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #118
        0x155,
        "#291F#1P缇～欧～！！\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_43(0x155, 0x3, 0x0, 0xC)
    OP_62(0x17, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    def lambda_2E71():

        label("loc_2E71")

        TurnDirection(0xFE, 0x155, 400)
        OP_48()
        Jump("loc_2E71")

    QueueWorkItem2(0x17, 2, lambda_2E71)
    Sleep(500)

    def lambda_2E87():
        OP_6D(26910, 0, 41800, 2000)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_2E87)

    def lambda_2E9F():
        OP_67(0, 6230, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_2E9F)

    def lambda_2EB7():
        OP_6C(216000, 2000)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_2EB7)
    WaitChrThread(0x155, 0x3)
    OP_44(0x17, 0x2)
    Sleep(300)

    ChrTalk(    #119
        0x17,
        (
            "#5P咦，艾丝蒂尔。\x01",
            "怎么了？\x02",
        )
    )

    Jump("loc_2F01")

    label("loc_2F01")

    CloseMessageWindow()

    ChrTalk(    #120
        0x17,
        (
            "#5P…………看你这样子，\x01",
            "肯定又是要去抓虫吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x155,
        (
            "#290F#12P哼哼，\x01",
            "今天可是有点特别哦。\x02\x03",

            "缇欧，给我一点\x01",
            "『新鲜牛奶』和『新鲜鸡蛋』～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x17,
        "#5P怎么啦，突然要这些。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x17,
        (
            "#5P该不会是突然醒悟过来，\x01",
            "要学做料理了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x155,
        "#291F#12P嘿嘿，其实呢…………\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #125
        "\x07\x05艾丝蒂尔说明了情况。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #126
        0x17,
        "#5P传……#100W传说中的……#20W虫…………？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x155,
        (
            "#291F#12P嗯，\x01",
            "我要让约修亚大吃一惊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x17,
        (
            "#5P还、还是老样子，\x01",
            "根本就不算是说明嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x17,
        "#5P唔，据我推测……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x17,
        (
            "#5P是为了让虫靠近\x01",
            "而制作芳香剂对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x155,
        "#290F#12P嗯，大概是吧。\x02",
    )

    CloseMessageWindow()
    OP_62(0x17, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #132
        0x17,
        (
            "#5P要是做出了芳香剂，\x01",
            "可别误泼到我身上哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x155,
        "#291F#12P没～问题没～问题。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x17,
        "#5P真、真的吗……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x17, 180, 400)

    def lambda_321C():
        OP_8E(0xFE, 0x6C8E, 0xFFFFFF4C, 0x9308, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_321C)
    WaitChrThread(0x17, 0x1)

    def lambda_323C():
        OP_8E(0xFE, 0x58F2, 0x8C, 0x7846, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_323C)
    WaitChrThread(0x17, 0x1)
    Sleep(2000)

    def lambda_3261():
        OP_8E(0xFE, 0x6C8E, 0xFFFFFF4C, 0x9308, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3261)
    WaitChrThread(0x17, 0x1)

    def lambda_3281():
        OP_8E(0xFE, 0x6B80, 0xFFFFFFBA, 0xA1FE, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3281)
    WaitChrThread(0x17, 0x1)
    Sleep(300)

    ChrTalk(    #135
        0x17,
        "#5P来，你要的东西。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #136
        "\x07\x00得到了\x07\x02『新鲜牛奶』\x07\x00和\x07\x02『新鲜鸡蛋』\x07\x00。\x02",
    )

    Jump("loc_3311")

    label("loc_3311")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #137
        0x17,
        (
            "#5P对了，艾丝蒂尔。\x01",
            "我顺便说一句……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x155,
        "#290F#12P？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x17,
        (
            "#5P如果要让那孩子做你的弟弟，\x01",
            "还是逐渐把话说清楚比较好哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x17,
        "#5P那孩子的过去，还有你的过去。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x17,
        (
            "#5P……莱娜阿姨在那个家里\x01",
            "生活过的事情，\x01",
            "我想都应该让他知道。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x155,
        (
            "#296F#12P……嗯，慢慢来吧。\x02\x03",

            "#290F不过，\x01",
            "这些其实也不用特地去说。\x02\x03",

            "既然一直待在一起，\x01",
            "总会知道的嘛。\x02\x03",

            "因为，\x01",
            "约修亚已经是重要的亲人了……\x02",
        )
    )

    Jump("loc_34E1")

    label("loc_34E1")

    CloseMessageWindow()

    ChrTalk(    #143
        0x17,
        "#5P……………是吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x17,
        (
            "#5P我就喜欢\x01",
            "你这一点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x155,
        (
            "#290F#12P……嗯。\x02\x03",

            "#291F谢谢你，缇欧！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x155, 0, 500)
    OP_A2(0x2F62)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 1)), scpexpr(EXPR_END)), "loc_37C4")

    ChrTalk(    #146
        0x155,
        (
            "#292F#5P好，材料全部齐了……\x02\x03",

            "接下来只要去神秘森林\x01",
            "抓到『传说中的虫』就好了！\x02\x03",

            "#294F等着吧，约修亚！！\x01",
            "我一定要让你大吃一惊！！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3610():
        OP_6D(26810, -70, 45830, 1500)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_3610)

    def lambda_3628():
        OP_6C(226000, 1500)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_3628)

    def lambda_3638():

        label("loc_3638")

        TurnDirection(0xFE, 0x155, 400)
        OP_48()
        Jump("loc_3638")

    QueueWorkItem2(0x17, 2, lambda_3638)
    SetChrFlags(0x155, 0x40)
    SetChrFlags(0x155, 0x4)

    def lambda_3653():
        OP_8E(0xFE, 0x6B1C, 0xFFFFFFC4, 0xB2D4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_3653)
    WaitChrThread(0x155, 0x1)

    def lambda_3673():
        OP_96(0xFE, 0x6E50, 0xFFFFFFA6, 0xBEC8, 0x4B0, 0x1770)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_3673)
    WaitChrThread(0x155, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    ClearChrFlags(0x155, 0x40)
    ClearChrFlags(0x155, 0x4)

    def lambda_36A5():
        OP_8E(0xFE, 0x5ED8, 0x0, 0xBEC8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_36A5)
    WaitChrThread(0x155, 0x1)

    def lambda_36C5():
        OP_8E(0xFE, 0x5ED8, 0x0, 0xF80C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_36C5)
    WaitChrThread(0x155, 0x1)
    OP_62(0x17, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #147
        0x17,
        "#5P喂、喂喂……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x17,
        (
            "#5P神秘森林那种地方，\x01",
            "小孩子怎么能随便进去呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x17,
        (
            "#5P话说回来，\x01",
            "那个……#100W传说中的虫#30W……到底是什么！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_37A0():
        OP_6B(2740, 3000)
        ExitThread()

    QueueWorkItem(0x1D, 3, lambda_37A0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T0100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39F6")

    label("loc_37C4")


    ChrTalk(    #150
        0x155,
        "#291F#5P好了，接着是伊莉莎！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x17,
        (
            "#5P找她干什么？\x01",
            "收集芳香剂的材料？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x155, 0x17, 500)
    Sleep(300)

    ChrTalk(    #152
        0x155,
        (
            "#290F#12P嗯。\x01",
            "我去向她要『巨龙咖啡豆』！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x17,
        (
            "#5P……………是吗。\x01",
            "唉，加油吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x155, 0, 500)
    Sleep(300)

    def lambda_389C():
        OP_6D(26810, -70, 45830, 1500)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_389C)

    def lambda_38B4():
        OP_6C(226000, 1500)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_38B4)

    def lambda_38C4():

        label("loc_38C4")

        TurnDirection(0xFE, 0x155, 400)
        OP_48()
        Jump("loc_38C4")

    QueueWorkItem2(0x17, 2, lambda_38C4)
    SetChrFlags(0x155, 0x40)
    SetChrFlags(0x155, 0x4)

    def lambda_38DF():
        OP_8E(0xFE, 0x6B1C, 0xFFFFFFC4, 0xB2D4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_38DF)
    Sleep(100)

    ChrTalk(    #154 op#A
        0x155,
        "#291F#5P#15A呀嗬——！！\x02",
    )

    WaitChrThread(0x155, 0x1)

    def lambda_3928():
        OP_96(0xFE, 0x6E50, 0xFFFFFFA6, 0xBEC8, 0x4B0, 0x1770)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_3928)
    WaitChrThread(0x155, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    ClearChrFlags(0x155, 0x40)
    ClearChrFlags(0x155, 0x4)

    def lambda_395A():
        OP_8E(0xFE, 0x5ED8, 0x0, 0xBEC8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_395A)
    WaitChrThread(0x155, 0x1)

    def lambda_397A():
        OP_8E(0xFE, 0x5ED8, 0x0, 0xF80C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_397A)
    WaitChrThread(0x155, 0x1)
    OP_62(0x17, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #155
        0x17,
        "比平时更起劲呢……\x02",
    )

    CloseMessageWindow()

    def lambda_39D5():
        OP_6B(2740, 3000)
        ExitThread()

    QueueWorkItem(0x1D, 3, lambda_39D5)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T0100   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_39F6")

    Return()

    # Function_11_2D9C end

    def Function_12_39F7(): pass

    label("Function_12_39F7")

    SetChrPos(0x155, 24380, 100, 60730, 180)

    def lambda_3A0E():
        OP_8E(0xFE, 0x5F3C, 0x64, 0xB234, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_3A0E)
    WaitChrThread(0x155, 0x1)

    def lambda_3A2E():
        OP_8E(0xFE, 0x6B1C, 0xFFFFFF92, 0xA7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_3A2E)
    WaitChrThread(0x155, 0x1)
    TurnDirection(0x155, 0x17, 500)
    Return()

    # Function_12_39F7 end

    SaveToFile()

Try(main)
