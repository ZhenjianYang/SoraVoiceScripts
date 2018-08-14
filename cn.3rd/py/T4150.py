from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4150   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4150.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
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
        '王都格兰赛尔·北街区',                 # 9
        '庭院大道方向',                         # 10
        '王都格兰赛尔·东街区',                 # 11
        '王都格兰赛尔·西街区',                 # 12
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
        'ED6_DT07/CH02320 ._CH',             # 00
        'ED6_DT26/CH20238 ._CH',             # 01
        'ED6_DT07/CH01640 ._CH',             # 02
        'ED6_DT07/CH01020 ._CH',             # 03
        'ED6_DT07/CH01220 ._CH',             # 04
        'ED6_DT07/CH01460 ._CH',             # 05
        'ED6_DT07/CH01130 ._CH',             # 06
        'ED6_DT07/CH01680 ._CH',             # 07
        'ED6_DT07/CH01690 ._CH',             # 08
        'ED6_DT07/CH01120 ._CH',             # 09
        'ED6_DT07/CH01150 ._CH',             # 0A
        'ED6_DT26/CH20254 ._CH',             # 0B
        'ED6_DT07/CH01200 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT07/CH02320P._CP',             # 00
        'ED6_DT26/CH20238P._CP',             # 01
        'ED6_DT07/CH01640P._CP',             # 02
        'ED6_DT07/CH01020P._CP',             # 03
        'ED6_DT07/CH01220P._CP',             # 04
        'ED6_DT07/CH01460P._CP',             # 05
        'ED6_DT07/CH01130P._CP',             # 06
        'ED6_DT07/CH01680P._CP',             # 07
        'ED6_DT07/CH01690P._CP',             # 08
        'ED6_DT07/CH01120P._CP',             # 09
        'ED6_DT07/CH01150P._CP',             # 0A
        'ED6_DT26/CH20254P._CP',             # 0B
        'ED6_DT07/CH01200P._CP',             # 0C
    )

    DeclNpc(
        X                   = 10,
        Z                   = 250,
        Y                   = 36990,
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

    DeclNpc(
        X                   = -50,
        Z                   = 0,
        Y                   = -90220,
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

    DeclNpc(
        X                   = 54990,
        Z                   = 0,
        Y                   = -1130,
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

    DeclNpc(
        X                   = -44420,
        Z                   = 0,
        Y                   = -19990,
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
        X                   = 9240,
        Y                   = 0,
        Z                   = -25000,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 9,
    )

    DeclEvent(
        X                   = -10280,
        Y                   = 0,
        Z                   = -11040,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 10,
    )

    DeclEvent(
        X                   = -14940,
        Y                   = 0,
        Z                   = -15750,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 10,
    )

    DeclEvent(
        X                   = -10290,
        Y                   = 0,
        Z                   = -30020,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 11,
    )

    DeclEvent(
        X                   = 9240,
        Y                   = 0,
        Z                   = -13010,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 12,
    )

    DeclEvent(
        X                   = 15900,
        Y                   = 0,
        Z                   = 6330,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 13,
    )


    ScpFunction(
        "Function_0_252",          # 00, 0
        "Function_1_271",          # 01, 1
        "Function_2_29C",          # 02, 2
        "Function_3_419",          # 03, 3
        "Function_4_488",          # 04, 4
        "Function_5_4F7",          # 05, 5
        "Function_6_51B",          # 06, 6
        "Function_7_58A",          # 07, 7
        "Function_8_5F9",          # 08, 8
        "Function_9_715",          # 09, 9
        "Function_10_719",         # 0A, 10
        "Function_11_71D",         # 0B, 11
        "Function_12_721",         # 0C, 12
        "Function_13_725",         # 0D, 13
    )


    def Function_0_252(): pass

    label("Function_0_252")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_270")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 8)

    label("loc_270")

    Return()

    # Function_0_252 end

    def Function_1_271(): pass

    label("Function_1_271")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFDBDE0, 0x23005B)
    OP_71(0x1002, 0x0)
    ExitThread()
    OP_71(0x1000, 0x0)
    ExitThread()
    OP_71(0x1003, 0x0)
    ExitThread()
    OP_71(0x100D, 0x0)
    ExitThread()
    Return()

    # Function_1_271 end

    def Function_2_29C(): pass

    label("Function_2_29C")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C1")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_403")

    label("loc_2C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DA")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_403")

    label("loc_2DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F3")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_403")

    label("loc_2F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30C")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_403")

    label("loc_30C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_325")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_403")

    label("loc_325")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33E")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_403")

    label("loc_33E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_357")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_403")

    label("loc_357")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_370")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_403")

    label("loc_370")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_389")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_403")

    label("loc_389")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A2")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_403")

    label("loc_3A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BB")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_403")

    label("loc_3BB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D4")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_403")

    label("loc_3D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3ED")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_403")

    label("loc_3ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_403")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_403")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_418")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_403")

    label("loc_418")

    Return()

    # Function_2_29C end

    def Function_3_419(): pass

    label("Function_3_419")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_487")
    OP_8E(0xFE, 0x1298, 0x0, 0xFFFF6550, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8E(0xFE, 0x1298, 0x0, 0xFFFFFB5A, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    Jump("Function_3_419")

    label("loc_487")

    Return()

    # Function_3_419 end

    def Function_4_488(): pass

    label("Function_4_488")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4F6")
    OP_8E(0xFE, 0xFFFFEE44, 0x0, 0xFFFFAFC4, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFFEEB2, 0x0, 0xFFFF6550, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    Jump("Function_4_488")

    label("loc_4F6")

    Return()

    # Function_4_488 end

    def Function_5_4F7(): pass

    label("Function_5_4F7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_51A")
    OP_8D(0xFE, 3700, -42040, 10110, -50100, 2000)
    Jump("Function_5_4F7")

    label("loc_51A")

    Return()

    # Function_5_4F7 end

    def Function_6_51B(): pass

    label("Function_6_51B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_589")
    OP_8E(0xFE, 0x1298, 0x0, 0xFFFF6550, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8E(0xFE, 0x1298, 0x0, 0xFFFFFB5A, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    Jump("Function_6_51B")

    label("loc_589")

    Return()

    # Function_6_51B end

    def Function_7_58A(): pass

    label("Function_7_58A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5F8")
    OP_8E(0xFE, 0xFFFFEE44, 0x0, 0xFFFFAFC4, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFFEEB2, 0x0, 0xFFFF6550, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    Jump("Function_7_58A")

    label("loc_5F8")

    Return()

    # Function_7_58A end

    def Function_8_5F9(): pass

    label("Function_8_5F9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x151, 0x8)
    OP_6D(-24240, 0, -19340, 0)
    OP_67(0, 6880, -10000, 0)
    OP_6B(4900, 0)
    OP_6C(306000, 0)
    OP_6E(406, 0)

    def lambda_652():
        OP_6D(16140, 0, 0, 14000)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_652)

    def lambda_66A():
        OP_67(0, 6580, -10000, 14000)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_66A)
    FadeToBright(2000, 0)
    Sleep(1000)

    def lambda_690():
        OP_6C(50000, 13000)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_690)
    WaitChrThread(0x103, 0x0)
    Sleep(1000)
    Fade(1000)
    OP_6D(18360, -400, 10560, 0)
    OP_67(0, 5880, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(34000, 0)
    OP_6E(360, 0)

    def lambda_6EC():
        OP_6B(2700, 5000)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6EC)
    Sleep(3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    NewScene("ED6_DT21/T4142   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_5F9 end

    def Function_9_715(): pass

    label("Function_9_715")

    SetPlaceName(0xB9)
    Return()

    # Function_9_715 end

    def Function_10_719(): pass

    label("Function_10_719")

    SetPlaceName(0xB0)
    Return()

    # Function_10_719 end

    def Function_11_71D(): pass

    label("Function_11_71D")

    SetPlaceName(0xB2)
    Return()

    # Function_11_71D end

    def Function_12_721(): pass

    label("Function_12_721")

    SetPlaceName(0xAE)
    Return()

    # Function_12_721 end

    def Function_13_725(): pass

    label("Function_13_725")

    SetPlaceName(0xB3)
    Return()

    # Function_13_725 end

    SaveToFile()

Try(main)
