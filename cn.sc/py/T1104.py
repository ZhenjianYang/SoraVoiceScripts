from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1104   ._SN',
        MapName             = 'Bose',
        Location            = 'T1104.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
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
        '士兵',                                 # 9
        '士兵',                                 # 10
        '士兵',                                 # 11
        '士兵',                                 # 12
        '西柏斯街道方向',                       # 13
        '东柏斯街道方向',                       # 14
        '柏斯市·南街区',                       # 15
        '柏斯国际空港',                         # 16
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
        'ED6_DT07/CH01640 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4530,
        Z                   = 0,
        Y                   = 45190,
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
        X                   = 87650,
        Z                   = 0,
        Y                   = 60410,
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
        X                   = 47990,
        Z                   = -3000,
        Y                   = 29310,
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
        X                   = 47940,
        Z                   = 0,
        Y                   = 93220,
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
        X                   = 25200,
        Y                   = 0,
        Z                   = 57940,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 4,
    )

    DeclEvent(
        X                   = 18880,
        Y                   = 0,
        Z                   = 76030,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 5,
    )

    DeclEvent(
        X                   = 36200,
        Y                   = 0,
        Z                   = 79200,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 6,
    )

    DeclEvent(
        X                   = 59000,
        Y                   = 0,
        Z                   = 79200,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 7,
    )

    DeclEvent(
        X                   = 38540,
        Y                   = 0,
        Z                   = 59990,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 8,
    )

    DeclEvent(
        X                   = 48040,
        Y                   = 100,
        Z                   = 69500,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 8,
    )

    DeclEvent(
        X                   = 57480,
        Y                   = 0,
        Z                   = 60010,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 8,
    )

    DeclEvent(
        X                   = 48010,
        Y                   = 0,
        Z                   = 50550,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 8,
    )

    DeclEvent(
        X                   = 67340,
        Y                   = -500,
        Z                   = 73070,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 9,
    )

    DeclEvent(
        X                   = 72240,
        Y                   = 0,
        Z                   = 44910,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 10,
    )

    DeclEvent(
        X                   = 47960,
        Y                   = 0,
        Z                   = 85570,
        Range               = 1000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 11,
    )


    ScpFunction(
        "Function_0_312",          # 00, 0
        "Function_1_32F",          # 01, 1
        "Function_2_388",          # 02, 2
        "Function_3_505",          # 03, 3
        "Function_4_666",          # 04, 4
        "Function_5_66A",          # 05, 5
        "Function_6_66E",          # 06, 6
        "Function_7_672",          # 07, 7
        "Function_8_676",          # 08, 8
        "Function_9_67A",          # 09, 9
        "Function_10_67E",         # 0A, 10
        "Function_11_682",         # 0B, 11
    )


    def Function_0_312(): pass

    label("Function_0_312")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_32E")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)

    label("loc_32E")

    Return()

    # Function_0_312 end

    def Function_1_32F(): pass

    label("Function_1_32F")

    OP_16(0x2, 0xFA0, 0xFFFEC780, 0xFFFEF660, 0x230041)
    OP_71(0x12, 0x4)
    OP_71(0x13, 0x4)
    OP_71(0x14, 0x4)
    OP_71(0x15, 0x4)
    OP_71(0x16, 0x4)
    OP_71(0x17, 0x4)
    OP_71(0x18, 0x4)
    OP_71(0x19, 0x4)
    OP_71(0x1A, 0x4)
    OP_71(0x1B, 0x4)
    OP_71(0x1C, 0x4)
    OP_71(0x1D, 0x4)
    OP_71(0x1E, 0x4)
    OP_71(0x20, 0x4)
    Return()

    # Function_1_32F end

    def Function_2_388(): pass

    label("Function_2_388")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AD")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_4EF")

    label("loc_3AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C6")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_4EF")

    label("loc_3C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DF")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_4EF")

    label("loc_3DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F8")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_4EF")

    label("loc_3F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_411")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_4EF")

    label("loc_411")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42A")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_4EF")

    label("loc_42A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_443")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_4EF")

    label("loc_443")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45C")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_4EF")

    label("loc_45C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_475")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_4EF")

    label("loc_475")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48E")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_4EF")

    label("loc_48E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A7")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_4EF")

    label("loc_4A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C0")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_4EF")

    label("loc_4C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D9")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_4EF")

    label("loc_4D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4EF")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_4EF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_504")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_4EF")

    label("loc_504")

    Return()

    # Function_2_388 end

    def Function_3_505(): pass

    label("Function_3_505")

    EventBegin(0x0)
    StopSound(0x9470, 0x249F0, 0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrPos(0x0, 36740, 6050, 48800, 0)
    OP_6D(50290, 6050, 61890, 0)
    OP_67(0, 16239, -10000, 0)
    OP_6B(2650, 0)
    OP_6C(215000, 0)
    OP_6E(485, 0)
    SetChrPos(0x8, 57480, 410, 60010, 90)
    SetChrPos(0x9, 38540, 410, 59990, 270)
    SetChrPos(0xA, 48010, 420, 50550, 180)
    SetChrPos(0xB, 48040, 300, 69500, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)

    def lambda_5CF():
        OP_6C(12000, 13000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5CF)
    FadeToBright(1000, 0)
    Sleep(8000)
    StopSound(0x9470, 0x1FBD0, 0x1F40)

    def lambda_5FA():
        OP_6D(58130, 6050, 76500, 8000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5FA)

    def lambda_612():
        OP_67(0, 7200, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_612)

    def lambda_62A():
        OP_6B(4410, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_62A)

    def lambda_63A():
        OP_6E(211, 8000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_63A)
    WaitChrThread(0x101, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1124   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_505 end

    def Function_4_666(): pass

    label("Function_4_666")

    SetPlaceName(0x2A)
    Return()

    # Function_4_666 end

    def Function_5_66A(): pass

    label("Function_5_66A")

    SetPlaceName(0x26)
    Return()

    # Function_5_66A end

    def Function_6_66E(): pass

    label("Function_6_66E")

    SetPlaceName(0x25)
    Return()

    # Function_6_66E end

    def Function_7_672(): pass

    label("Function_7_672")

    SetPlaceName(0x20)
    Return()

    # Function_7_672 end

    def Function_8_676(): pass

    label("Function_8_676")

    SetPlaceName(0x28)
    Return()

    # Function_8_676 end

    def Function_9_67A(): pass

    label("Function_9_67A")

    SetPlaceName(0x2B)
    Return()

    # Function_9_67A end

    def Function_10_67E(): pass

    label("Function_10_67E")

    SetPlaceName(0x21)
    Return()

    # Function_10_67E end

    def Function_11_682(): pass

    label("Function_11_682")

    SetPlaceName(0x27)
    Return()

    # Function_11_682 end

    SaveToFile()

Try(main)
