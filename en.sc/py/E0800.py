from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'E0800   ._SN',
        MapName             = 'Event',
        Location            = 'E0800.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60001",
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
        '紅い飛行艇',                           # 9
        'Arseille',                             # 10
        '警備艇',                               # 11
        '警備艇',                               # 12
        '警備艇',                               # 13
        '警備艇',                               # 14
        'Ancient Dragon Ragnard',               # 15
        'Targeting Camera',                     # 16
        'Targeting Camera',                     # 17
        'Target',                               # 18
        'Captain Schwarz',                      # 19
        'General Morgan',                       # 20
        'Sieg',                                 # 21
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
        'ED6_DT27/CH03580 ._CH',             # 00
        'ED6_DT07/CH02080 ._CH',             # 01
        'ED6_DT07/CH02320 ._CH',             # 02
        'ED6_DT06/CH20113 ._CH',             # 03
        'ED6_DT26/CH20254 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT27/CH03580P._CP',             # 00
        'ED6_DT07/CH02080P._CP',             # 01
        'ED6_DT07/CH02320P._CP',             # 02
        'ED6_DT06/CH20113P._CP',             # 03
        'ED6_DT26/CH20254P._CP',             # 04
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
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
        NpcIndex            = 0x185,
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
        NpcIndex            = 0x185,
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
        NpcIndex            = 0x185,
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
        NpcIndex            = 0x185,
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
        NpcIndex            = 0x185,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_272",          # 00, 0
        "Function_1_350",          # 01, 1
        "Function_2_385",          # 02, 2
        "Function_3_39B",          # 03, 3
        "Function_4_580",          # 04, 4
        "Function_5_AEA",          # 05, 5
        "Function_6_10E7",         # 06, 6
        "Function_7_112A",         # 07, 7
        "Function_8_1226",         # 08, 8
        "Function_9_1322",         # 09, 9
        "Function_10_13BE",        # 0A, 10
        "Function_11_145A",        # 0B, 11
        "Function_12_14D0",        # 0C, 12
        "Function_13_1546",        # 0D, 13
        "Function_14_17F3",        # 0E, 14
        "Function_15_1D67",        # 0F, 15
        "Function_16_1D7E",        # 10, 16
        "Function_17_1DFA",        # 11, 17
        "Function_18_1E76",        # 12, 18
        "Function_19_1F12",        # 13, 19
        "Function_20_21F9",        # 14, 20
        "Function_21_25BF",        # 15, 21
        "Function_22_25DB",        # 16, 22
        "Function_23_26C0",        # 17, 23
        "Function_24_2796",        # 18, 24
        "Function_25_286C",        # 19, 25
        "Function_26_2E4C",        # 1A, 26
        "Function_27_2F08",        # 1B, 27
        "Function_28_3265",        # 1C, 28
        "Function_29_3440",        # 1D, 29
        "Function_30_3621",        # 1E, 30
        "Function_31_365F",        # 1F, 31
        "Function_32_36FB",        # 20, 32
    )


    def Function_0_272(): pass

    label("Function_0_272")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_291")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 3)
    Jump("loc_34F")

    label("loc_291")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_2B0")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 5)
    Jump("loc_34F")

    label("loc_2B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_2CF")
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 14)
    Jump("loc_34F")

    label("loc_2CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_2EE")
    OP_A3(0x10F3)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 20)
    Jump("loc_34F")

    label("loc_2EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_END)), "loc_30D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x22), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F4)
    SetMapFlags(0x10000000)
    Event(0, 25)
    Jump("loc_34F")

    label("loc_30D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 5)), scpexpr(EXPR_END)), "loc_327")
    OP_A3(0x10F5)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 29)
    Jump("loc_34F")

    label("loc_327")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 6)), scpexpr(EXPR_END)), "loc_341")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F6)
    Event(0, 27)
    Jump("loc_34F")

    label("loc_341")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 7)), scpexpr(EXPR_END)), "loc_34F")
    OP_A3(0x10F7)
    Event(0, 32)

    label("loc_34F")

    Return()

    # Function_0_272 end

    def Function_1_350(): pass

    label("Function_1_350")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_368")
    OP_B1("E0800_2")
    Jump("loc_384")

    label("loc_368")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 5)), scpexpr(EXPR_END)), "loc_37B")
    OP_B1("E0800_1")
    Jump("loc_384")

    label("loc_37B")

    OP_B1("E0800_2")

    label("loc_384")

    Return()

    # Function_1_350 end

    def Function_2_385(): pass

    label("Function_2_385")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_39A")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_385")

    label("loc_39A")

    Return()

    # Function_2_385 end

    def Function_3_39B(): pass

    label("Function_3_39B")

    EventBegin(0x0)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-10470, 10000, -5940, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(487, 0)
    SetChrPos(0xF, -10470, 10000, -5940, 0)
    OP_6A(0xF)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_A1(0x8, 0x2)
    SetChrPos(0x8, 20000, 0, 0, 270)
    OP_6F(0x2, 800)
    OP_70(0x2, 0x384)
    OP_22(0x79, 0x1, 0x64)
    OP_22(0x1C3, 0x0, 0x64)
    FadeToBright(2000, 0)

    def lambda_459():
        OP_90(0xFE, 0xFFFC2F70, 0x0, 0x0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_459)

    def lambda_474():
        OP_90(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_474)
    OP_24(0x79, 0x50)
    Sleep(1000)
    OP_24(0x79, 0x55)
    Sleep(1000)
    OP_24(0x79, 0x5A)
    Sleep(1000)
    OP_24(0x79, 0x5F)
    Sleep(1000)
    OP_24(0x79, 0x64)

    def lambda_4B7():
        OP_6C(315000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4B7)
    Sleep(1000)

    def lambda_4CC():
        OP_90(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_4CC)
    Sleep(4000)

    def lambda_4EC():
        OP_90(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_4EC)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_24(0x79, 0x64)
    Sleep(200)
    OP_24(0x79, 0x5A)
    Sleep(200)
    OP_24(0x79, 0x50)
    Sleep(200)
    OP_24(0x79, 0x46)
    Sleep(200)
    OP_24(0x79, 0x3C)
    Sleep(200)
    OP_24(0x79, 0x32)
    Sleep(200)
    OP_24(0x79, 0x28)
    Sleep(200)
    OP_24(0x79, 0x1E)
    Sleep(200)
    OP_24(0x79, 0x14)
    Sleep(200)
    OP_24(0x79, 0xA)
    Sleep(200)
    OP_24(0x79, 0x0)
    OP_23(0x79)
    OP_0D()
    OP_DC()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/E0610   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_39B end

    def Function_4_580(): pass

    label("Function_4_580")

    EventBegin(0x0)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    OP_6D(-19120, 5000, -3020, 0)
    OP_67(0, 5210, -10000, 0)
    OP_6B(4100, 0)
    OP_6C(61000, 0)
    OP_6E(597, 0)
    SetChrPos(0x11, -12000, -2550, 20000, 0)
    SetChrPos(0xF, -19120, 5000, -3020, 0)
    OP_6A(0xF)
    OP_A1(0x9, 0x5)
    SetChrPos(0x9, 0, 0, 0, 270)
    OP_22(0x79, 0x1, 0x46)
    OP_B0(0x5, 0x1E)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 330)
    OP_70(0x5, 0x1AE)
    ClearChrFlags(0xA, 0x100)
    ClearChrFlags(0xB, 0x100)
    OP_A1(0xA, 0x1)
    OP_A1(0xB, 0x2)
    OP_D1(10, 0, 90000, 0, 0)
    OP_D1(11, 0, 90000, 0, 0)
    SetChrPos(0xA, 96000, -6550, 20000, 90)
    SetChrPos(0xB, 96000, 2550, -20000, 90)
    OP_71(0x0, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    LoadEffect(0x1, "map\\\\mp001_01.eff")

    def lambda_6A1():
        OP_90(0x101, 0xFFFB6C20, 0x0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_6A1)

    def lambda_6BC():
        OP_91(0xFE, 0xFFFB6C20, 0x0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_6BC)

    def lambda_6D7():
        OP_91(0xFE, 0xFFFB6C20, 0x0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6D7)

    def lambda_6F2():
        OP_91(0xFE, 0xFFFB6C20, 0x0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6F2)

    def lambda_70D():
        OP_91(0xFE, 0xFFFB6C20, 0x0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_70D)

    def lambda_728():
        OP_91(0xFE, 0xFFFB6C20, 0x0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_728)

    def lambda_743():
        OP_67(0, 6390, -10000, 12000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_743)

    def lambda_75B():
        OP_6B(5200, 12000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_75B)

    def lambda_76B():
        OP_6C(74000, 12000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_76B)

    def lambda_77B():
        OP_6E(616, 12000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_77B)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(3000)
    OP_B0(0x1, 0x2D)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x208)
    Sleep(100)
    OP_B0(0x2, 0x2D)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 500)
    OP_70(0x2, 0x208)

    def lambda_7CD():
        OP_91(0xFE, 0xFFFC0860, 0x0, 0x0, 0x7148, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7CD)

    def lambda_7E8():
        OP_91(0xFE, 0xFFFC0860, 0x0, 0x0, 0x7148, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_7E8)
    Sleep(5500)

    def lambda_808():
        OP_91(0xFE, 0xFFFD40E0, 0x0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_808)

    def lambda_823():
        OP_91(0xFE, 0xFFFD40E0, 0x0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_823)
    Sleep(1000)

    def lambda_843():
        OP_67(0, 4610, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_843)

    def lambda_85B():
        OP_6B(5800, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_85B)
    PlayEffect(0x1, 0x1, 0x9, -11000, 2600, 0, 0, 0, 0, 5000, 5000, 5000, 0xFF, 0, 0, 0, 0)
    Sleep(20)
    OP_82(0x1, 0x0)
    Sleep(1000)
    PlayEffect(0x2, 0x1, 0x9, -11000, 2600, 0, 0, 0, 0, 5000, 5000, 5000, 0xFF, 0, 0, 0, 0)
    Sleep(20)
    OP_82(0x1, 0x0)
    Sleep(1000)
    PlayEffect(0x1, 0x1, 0x9, -11000, 2600, 0, 0, 0, 0, 5000, 5000, 5000, 0xFF, 0, 0, 0, 0)
    Sleep(20)
    OP_82(0x1, 0x0)
    Sleep(1500)
    PlayEffect(0x1, 0x1, 0xA, -5500, 8000, 2000, 0, 0, 0, 5000, 5000, 5000, 0xFF, 0, 0, 0, 0)
    Sleep(20)
    OP_82(0x1, 0x0)
    Sleep(100)
    PlayEffect(0x2, 0x1, 0xA, -5500, 8000, 2000, 0, 0, 0, 5000, 5000, 5000, 0xFF, 0, 0, 0, 0)
    Sleep(20)
    OP_82(0x1, 0x0)
    Sleep(1000)
    PlayEffect(0x1, 0x1, 0xB, -5500, 8000, 2000, 0, 0, 0, 5000, 5000, 5000, 0xFF, 0, 0, 0, 0)
    Sleep(20)
    OP_82(0x1, 0x0)
    Sleep(100)
    PlayEffect(0x2, 0x1, 0xB, -5500, 8000, 2000, 0, 0, 0, 5000, 5000, 5000, 0xFF, 0, 0, 0, 0)
    Sleep(20)
    OP_82(0x1, 0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(2500)
    OP_43(0xA, 0x0, 0x0, 0xB)
    Sleep(500)
    OP_43(0xB, 0x0, 0x0, 0xC)
    Sleep(1000)

    def lambda_A5C():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_A5C)

    def lambda_A77():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A77)

    def lambda_A92():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A92)
    Sleep(300)

    def lambda_AB2():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_AB2)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/E0311   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_4_580 end

    def Function_5_AEA(): pass

    label("Function_5_AEA")

    EventBegin(0x0)
    OP_DB()
    LoadEffect(0x1, "map\\\\mp076_00.eff")
    LoadEffect(0x2, "map\\\\mp076_01.eff")
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-19120, 5000, -3020, 0)
    OP_67(0, 5210, -10000, 0)
    OP_6B(4100, 0)
    OP_6C(61000, 0)
    OP_6E(1065, 0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFFD, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFFD, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFF8, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x11, -12000, -2550, 20000, 0)
    SetChrPos(0xF, -119120, 5000, -3020, 0)
    OP_A1(0x9, 0x5)
    SetChrPos(0x9, 0, 0, 0, 270)
    OP_22(0x125, 0x1, 0x50)
    OP_B0(0x5, 0x1E)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 330)
    OP_70(0x5, 0x1AE)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_C2D():
        OP_6D(-12730, -2050, 11180, 8000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C2D)

    def lambda_C45():
        OP_67(0, 3710, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C45)

    def lambda_C5D():
        OP_6B(4100, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C5D)

    def lambda_C6D():
        OP_6C(26000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_C6D)

    def lambda_C7D():
        OP_6E(885, 8000)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_C7D)
    Sleep(6000)
    ClearChrFlags(0xA, 0x100)
    ClearChrFlags(0xB, 0x100)
    OP_A1(0xA, 0x1)
    OP_A1(0xB, 0x2)
    OP_D1(10, 0, 90000, 24000, 0)
    OP_D1(11, 0, 90000, 24000, 0)
    SetChrPos(0xA, 180000, 550, 40000, 90)
    SetChrPos(0xB, 173000, -8550, 20000, 90)
    OP_72(0x1, 0x4)
    OP_72(0x2, 0x4)
    OP_B0(0x1, 0x1E)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x208)
    Sleep(100)
    OP_B0(0x2, 0x1E)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 500)
    OP_70(0x2, 0x208)
    OP_22(0x79, 0x1, 0x5A)
    OP_43(0xB, 0x0, 0x0, 0x8)

    def lambda_D37():
        OP_D1(254, 0, 90000, 25000, 4000)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_D37)
    Sleep(1500)
    OP_43(0xA, 0x0, 0x0, 0x7)

    def lambda_D5D():
        OP_D1(254, 0, 90000, 25000, 4000)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_D5D)
    WaitChrThread(0xB, 0x2)

    def lambda_D7C():
        OP_D1(254, 0, 90000, 0, 2500)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_D7C)
    WaitChrThread(0xA, 0x2)

    def lambda_D9B():
        OP_D1(254, 0, 90000, 0, 2500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_D9B)
    WaitChrThread(0xA, 0x2)
    Sleep(1000)
    PlayEffect(0x1, 0xFF, 0x9, -11000, 2600, 3000, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(600)
    PlayEffect(0x1, 0xFF, 0x9, -11000, 2600, 3000, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(600)
    PlayEffect(0x1, 0xFF, 0x9, -11000, 2600, 3000, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(1600)
    PlayEffect(0x1, 0xFF, 0xA, -5500, 8000, 2000, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)
    Sleep(600)
    PlayEffect(0x1, 0xFF, 0xA, -5500, 8000, 2000, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)
    Sleep(1600)
    PlayEffect(0x1, 0xFF, 0xB, -5500, 8000, 2000, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)
    Sleep(600)
    PlayEffect(0x1, 0xFF, 0xB, -5500, 8000, 2000, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)
    Sleep(600)

    def lambda_F55():
        OP_6D(-19120, 5000, -3020, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F55)

    def lambda_F6D():
        OP_67(0, 5210, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F6D)

    def lambda_F85():
        OP_6B(4100, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F85)

    def lambda_F95():
        OP_6C(61000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_F95)

    def lambda_FA5():
        OP_6E(865, 4000)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_FA5)
    OP_43(0xA, 0x0, 0x0, 0x9)

    def lambda_FBC():
        OP_D1(254, 0, 100000, 30000, 3000)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_FBC)
    Sleep(1000)
    OP_43(0xB, 0x0, 0x0, 0xA)

    def lambda_FE2():
        OP_D1(254, 0, 90000, 30000, 3000)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_FE2)
    OP_43(0xA, 0x3, 0x0, 0x6)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0xF, 0x0)

    def lambda_101C():
        OP_67(0, 510, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_101C)

    def lambda_1034():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1034)
    Sleep(200)

    def lambda_1054():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1054)
    Sleep(200)

    def lambda_1074():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1074)
    Sleep(200)

    def lambda_1094():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1094)
    Sleep(200)

    def lambda_10B4():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_10B4)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_DC()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/E0311   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_5_AEA end

    def Function_6_10E7(): pass

    label("Function_6_10E7")

    OP_24(0x79, 0x50)
    Sleep(400)
    OP_24(0x79, 0x46)
    Sleep(400)
    OP_24(0x79, 0x3C)
    Sleep(400)
    OP_24(0x79, 0x32)
    Sleep(400)
    OP_24(0x79, 0x28)
    Sleep(400)
    OP_24(0x79, 0x1E)
    Sleep(400)
    OP_24(0x79, 0x14)
    Sleep(400)
    OP_23(0x79)
    Return()

    # Function_6_10E7 end

    def Function_7_112A(): pass

    label("Function_7_112A")


    def lambda_1130():
        OP_8F(0xFE, 0xFA0, 0x226, 0x12110, 0x7148, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1130)
    Sleep(5000)

    def lambda_1150():
        OP_8F(0xFE, 0xFA0, 0x226, 0x12110, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1150)
    Sleep(600)

    def lambda_1170():
        OP_8F(0xFE, 0xFA0, 0x226, 0x12110, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1170)
    Sleep(500)

    def lambda_1190():
        OP_8F(0xFE, 0xFA0, 0x226, 0x12110, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1190)
    Sleep(400)

    def lambda_11B0():
        OP_8F(0xFE, 0xFA0, 0x226, 0x12110, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_11B0)
    Sleep(300)

    def lambda_11D0():
        OP_8F(0xFE, 0xFA0, 0x226, 0x12110, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_11D0)
    Sleep(200)

    def lambda_11F0():
        OP_8F(0xFE, 0xFA0, 0x226, 0x12110, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_11F0)
    Sleep(100)

    def lambda_1210():
        OP_8F(0xFE, 0xFA0, 0x226, 0x12110, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1210)
    Return()

    # Function_7_112A end

    def Function_8_1226(): pass

    label("Function_8_1226")


    def lambda_122C():
        OP_8F(0xFE, 0xFFFFF448, 0xFFFFDE9A, 0xD2F0, 0x7148, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_122C)
    Sleep(5000)

    def lambda_124C():
        OP_8F(0xFE, 0xFFFFF448, 0xFFFFDE9A, 0xD2F0, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_124C)
    Sleep(600)

    def lambda_126C():
        OP_8F(0xFE, 0xFFFFF448, 0xFFFFDE9A, 0xD2F0, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_126C)
    Sleep(500)

    def lambda_128C():
        OP_8F(0xFE, 0xFFFFF448, 0xFFFFDE9A, 0xD2F0, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_128C)
    Sleep(400)

    def lambda_12AC():
        OP_8F(0xFE, 0xFFFFF448, 0xFFFFDE9A, 0xD2F0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_12AC)
    Sleep(300)

    def lambda_12CC():
        OP_8F(0xFE, 0xFFFFF448, 0xFFFFDE9A, 0xD2F0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_12CC)
    Sleep(200)

    def lambda_12EC():
        OP_8F(0xFE, 0xFFFFF448, 0xFFFFDE9A, 0xD2F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_12EC)
    Sleep(100)

    def lambda_130C():
        OP_8F(0xFE, 0xFFFFF448, 0xFFFFDE9A, 0xD2F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_130C)
    Return()

    # Function_8_1226 end

    def Function_9_1322(): pass

    label("Function_9_1322")


    def lambda_1328():
        OP_8F(0xFE, 0xFFFF9A70, 0x226, 0x1BD50, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1328)
    Sleep(500)

    def lambda_1348():
        OP_8F(0xFE, 0xFFFF9A70, 0x226, 0x1BD50, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1348)
    Sleep(500)

    def lambda_1368():
        OP_8F(0xFE, 0xFFFF9A70, 0x226, 0x1BD50, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1368)
    Sleep(500)

    def lambda_1388():
        OP_8F(0xFE, 0xFFFF9A70, 0x226, 0x1BD50, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1388)
    Sleep(500)

    def lambda_13A8():
        OP_8F(0xFE, 0xFFFF9A70, 0x226, 0x1BD50, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_13A8)
    Return()

    # Function_9_1322 end

    def Function_10_13BE(): pass

    label("Function_10_13BE")


    def lambda_13C4():
        OP_8F(0xFE, 0xFFFF7F18, 0xFFFFDE9A, 0x16F30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_13C4)
    Sleep(500)

    def lambda_13E4():
        OP_8F(0xFE, 0xFFFF7F18, 0xFFFFDE9A, 0x16F30, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_13E4)
    Sleep(500)

    def lambda_1404():
        OP_8F(0xFE, 0xFFFF7F18, 0xFFFFDE9A, 0x16F30, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1404)
    Sleep(500)

    def lambda_1424():
        OP_8F(0xFE, 0xFFFF7F18, 0xFFFFDE9A, 0x16F30, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1424)
    Sleep(500)

    def lambda_1444():
        OP_8F(0xFE, 0xFFFF7F18, 0xFFFFDE9A, 0x16F30, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1444)
    Return()

    # Function_10_13BE end

    def Function_11_145A(): pass

    label("Function_11_145A")


    def lambda_1460():
        OP_D1(10, 0, 90000, 45000, 800)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1460)

    def lambda_147A():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0x30D40, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_147A)
    Sleep(300)

    def lambda_149A():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0x30D40, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_149A)
    Sleep(300)

    def lambda_14BA():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0x30D40, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_14BA)
    Return()

    # Function_11_145A end

    def Function_12_14D0(): pass

    label("Function_12_14D0")


    def lambda_14D6():
        OP_D1(11, 0, 90000, -45000, 800)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_14D6)

    def lambda_14F0():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0xFFFCF2C0, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_14F0)
    Sleep(300)

    def lambda_1510():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0xFFFCF2C0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1510)
    Sleep(300)

    def lambda_1530():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0xFFFCF2C0, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1530)
    Return()

    # Function_12_14D0 end

    def Function_13_1546(): pass

    label("Function_13_1546")

    EventBegin(0x0)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x4, 0x80)
    OP_6D(16900, 5000, -140, 0)
    OP_67(0, 5280, -10000, 0)
    OP_6B(4910, 0)
    OP_6C(75000, 0)
    OP_6E(713, 0)
    OP_A1(0x9, 0x5)
    SetChrPos(0x9, 150000, -30000, 0, 270)
    OP_B0(0x5, 0x1E)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 330)
    OP_70(0x5, 0x1AE)
    OP_71(0x5, 0x4)
    OP_A1(0xE, 0x0)
    SetChrPos(0xE, 50000, -30000, 0, 270)
    ClearChrFlags(0xE, 0x100)
    OP_D1(14, 0, 270000, 0, 0)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_72(0x0, 0x4)

    def lambda_1632():
        OP_8F(0xFE, 0x4E20, 0x0, 0x0, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1632)
    WaitChrThread(0xE, 0x1)
    Sleep(4000)
    OP_72(0x5, 0x4)

    def lambda_165C():
        OP_8F(0xFE, 0x1D4C0, 0x0, 0x0, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_165C)

    def lambda_1677():
        OP_6D(28100, 5000, -5050, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1677)

    def lambda_168F():
        OP_67(0, 4320, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_168F)

    def lambda_16A7():
        OP_6B(6700, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_16A7)

    def lambda_16B7():
        OP_6E(669, 2000)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_16B7)
    OP_22(0x79, 0x1, 0x50)
    Sleep(500)
    OP_24(0x79, 0x55)
    Sleep(500)
    OP_24(0x79, 0x5A)
    Sleep(500)
    OP_24(0x79, 0x5F)
    Sleep(500)
    OP_24(0x79, 0x64)
    WaitChrThread(0x9, 0x1)
    Sleep(6000)
    LoadEffect(0x0, "Scraft\\\\sc003_12.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 117730, -1780, -9290, 270, 0, 0, 8000, 8000, 8000, 0xFF, 0, 0, 0, 0)
    OP_D1(14, 0, 270000, -45000, 300)
    Sleep(800)
    OP_D1(14, 0, 270000, 0, 300)
    Sleep(1000)
    PlayEffect(0x0, 0xFF, 0xFF, 117730, -1780, 9290, 270, 0, 0, 8000, 8000, 8000, 0xFF, 0, 0, 0, 0)
    OP_D1(14, 0, 270000, 45000, 300)
    Sleep(800)
    OP_D1(14, 0, 270000, 0, 300)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_DC()
    OP_A2(0x10F6)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_13_1546 end

    def Function_14_17F3(): pass

    label("Function_14_17F3")

    EventBegin(0x0)
    OP_DB()
    LoadEffect(0x0, "monster\\\\msc0331.eff")
    LoadEffect(0x1, "map\\\\mp077_00.eff")
    LoadEffect(0x2, "map\\\\mp077_01.eff")
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x4, 0x80)
    OP_6D(9310, -8300, 11010, 0)
    OP_67(0, 2200, -10000, 0)
    OP_6B(4910, 0)
    OP_6C(44000, 0)
    OP_6E(953, 0)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFF6, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFFD, 0xFFFFFFFD, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFF1, 0xFFFFFFFA, 0x0, 0x0, 0x0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_A1(0x9, 0x5)
    SetChrPos(0x9, 150000, -30000, 0, 270)
    OP_B0(0x5, 0x1E)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 330)
    OP_70(0x5, 0x1AE)
    OP_71(0x5, 0x4)
    OP_A1(0xE, 0x0)
    SetChrPos(0xE, 30000, -30000, 0, 270)
    ClearChrFlags(0xE, 0x100)
    OP_D1(14, 0, 270000, 0, 0)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_72(0x0, 0x4)
    PlayEffect(0x1, 0xFF, 0xFF, 0, 0, 0, 270, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0, 0, 15000, 270, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0, 0, -15000, 270, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_43(0xE, 0x3, 0x0, 0xF)
    Sleep(200)
    OP_43(0xE, 0x0, 0x0, 0x10)

    def lambda_1A1A():
        OP_6D(24590, -10000, 10600, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1A1A)

    def lambda_1A32():
        OP_67(0, 4490, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A32)

    def lambda_1A4A():
        OP_6C(65000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1A4A)

    def lambda_1A5A():
        OP_6B(4910, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1A5A)

    def lambda_1A6A():
        OP_6E(1230, 2000)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_1A6A)
    OP_72(0x0, 0x20)
    OP_B0(0x0, 0xD)
    OP_6F(0x0, 76)
    OP_70(0x0, 0x5F)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_B0(0x0, 0xF)
    OP_6F(0x0, 10)
    OP_70(0x0, 0x1E)
    WaitChrThread(0xE, 0x1)
    Sleep(2000)
    OP_72(0x5, 0x4)
    OP_43(0x9, 0x0, 0x0, 0x11)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0xFF, 120000, -5000, 0, 270, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_22(0x125, 0x1, 0x50)
    Sleep(500)
    OP_24(0x125, 0x55)
    Sleep(500)
    OP_24(0x125, 0x5A)
    Sleep(500)
    OP_24(0x125, 0x5F)
    Sleep(500)
    OP_24(0x125, 0x64)
    WaitChrThread(0x9, 0x1)

    def lambda_1B29():
        OP_6D(20670, -10000, 3290, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1B29)

    def lambda_1B41():
        OP_67(0, 5480, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B41)

    def lambda_1B59():
        OP_6C(80000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1B59)
    PlayEffect(0x0, 0xFF, 0x9, -2270, -1780, -9290, 0, 0, 0, 5000, 5000, 5000, 0xE, -20000, -1000, -6000, 0)

    def lambda_1B9E():
        OP_8F(0xFE, 0x0, 0x3E8, 0x1770, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1B9E)
    OP_D1(14, 0, 270000, -30000, 1000)
    WaitChrThread(0xE, 0x1)
    Sleep(400)
    OP_43(0xE, 0x0, 0x0, 0x12)
    OP_D1(14, 0, 270000, 0, 1500)
    WaitChrThread(0xE, 0x0)
    WaitChrThread(0xE, 0x1)
    PlayEffect(0x0, 0xFF, 0x9, -2270, -1780, 9290, 0, 0, 0, 5000, 5000, 5000, 0xE, -20000, -1000, 6000, 0)

    def lambda_1C2F():
        OP_8F(0xFE, 0x0, 0x3E8, 0xFFFFE890, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1C2F)
    OP_D1(14, 0, 270000, 30000, 1000)
    WaitChrThread(0xE, 0x1)
    Sleep(400)
    OP_43(0xE, 0x0, 0x0, 0x12)
    OP_D1(14, 0, 270000, 0, 1500)
    WaitChrThread(0xE, 0x0)
    WaitChrThread(0xE, 0x1)

    def lambda_1C8B():
        OP_8F(0xFE, 0xFFFE7960, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1C8B)
    Sleep(500)

    def lambda_1CAB():
        OP_8F(0xFE, 0xFFFE7960, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1CAB)
    Sleep(400)

    def lambda_1CCB():
        OP_8F(0xFE, 0xFFFE7960, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1CCB)
    Sleep(300)

    def lambda_1CEB():
        OP_8F(0xFE, 0xFFFE7960, 0x0, 0x0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1CEB)
    Sleep(200)

    def lambda_1D0B():
        OP_8F(0xFE, 0xFFFE7960, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1D0B)
    Sleep(100)

    def lambda_1D2B():
        OP_8F(0xFE, 0xFFFE7960, 0x0, 0x0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1D2B)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0xE, 0x3)
    SetMapFlags(0x2000000)
    OP_DC()
    OP_A2(0x10F6)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_14_17F3 end

    def Function_15_1D67(): pass

    label("Function_15_1D67")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1D7D")
    OP_22(0x120, 0x0, 0x64)
    Sleep(1300)
    Jump("Function_15_1D67")

    label("loc_1D7D")

    Return()

    # Function_15_1D67 end

    def Function_16_1D7E(): pass

    label("Function_16_1D7E")


    def lambda_1D84():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1D84)
    Sleep(1500)

    def lambda_1DA4():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1DA4)
    Sleep(300)

    def lambda_1DC4():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1DC4)
    Sleep(100)

    def lambda_1DE4():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1DE4)
    Return()

    # Function_16_1D7E end

    def Function_17_1DFA(): pass

    label("Function_17_1DFA")


    def lambda_1E00():
        OP_8F(0xFE, 0x1D4C0, 0x0, 0x0, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1E00)
    Sleep(1500)

    def lambda_1E20():
        OP_8F(0xFE, 0x1D4C0, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1E20)
    Sleep(300)

    def lambda_1E40():
        OP_8F(0xFE, 0x1D4C0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1E40)
    Sleep(100)

    def lambda_1E60():
        OP_8F(0xFE, 0x1D4C0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1E60)
    Return()

    # Function_17_1DFA end

    def Function_18_1E76(): pass

    label("Function_18_1E76")


    def lambda_1E7C():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1E7C)
    Sleep(100)

    def lambda_1E9C():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1E9C)
    Sleep(100)

    def lambda_1EBC():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1EBC)
    Sleep(500)

    def lambda_1EDC():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1EDC)
    Sleep(100)

    def lambda_1EFC():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1EFC)
    Return()

    # Function_18_1E76 end

    def Function_19_1F12(): pass

    label("Function_19_1F12")

    EventBegin(0x0)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x4, 0x80)
    OP_6D(138530, 2510, -4630, 0)
    OP_67(0, 4780, -10000, 0)
    OP_6B(7240, 0)
    OP_6C(295000, 0)
    OP_6E(784, 0)
    OP_A1(0x9, 0x5)
    SetChrPos(0x9, 150000, 0, 0, 270)
    ClearChrFlags(0x9, 0x100)
    OP_D1(9, 0, 270000, 0, 0)
    OP_22(0x79, 0x1, 0x46)
    OP_B0(0x5, 0x1E)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 330)
    OP_70(0x5, 0x1AE)
    OP_A1(0xE, 0x0)
    SetChrPos(0xE, 50000, 0, 0, 270)
    ClearChrFlags(0xE, 0x100)
    OP_D1(14, 0, 270000, 0, 0)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    def lambda_200C():
        OP_91(0xFE, 0x0, 0x0, 0x4E20, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_200C)

    def lambda_2027():
        OP_D1(254, 0, 270000, -30000, 300)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_2027)
    Sleep(500)

    def lambda_2046():
        OP_91(0xFE, 0x0, 0x0, 0x4E20, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2046)

    def lambda_2061():
        OP_D1(254, 0, 270000, -20000, 300)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2061)
    WaitChrThread(0xE, 0x1)

    def lambda_2080():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF63C0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2080)

    def lambda_209B():
        OP_D1(254, 0, 270000, 30000, 300)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_209B)
    WaitChrThread(0x9, 0x1)

    def lambda_20BA():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF63C0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_20BA)

    def lambda_20D5():
        OP_D1(254, 0, 270000, 20000, 300)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_20D5)
    WaitChrThread(0xE, 0x1)

    def lambda_20F4():
        OP_8F(0xFE, 0xC350, 0x0, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_20F4)

    def lambda_210F():
        OP_D1(254, 0, 270000, -30000, 300)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_210F)
    WaitChrThread(0x9, 0x1)

    def lambda_212E():
        OP_8F(0xFE, 0x249F0, 0x0, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_212E)

    def lambda_2149():
        OP_D1(254, 0, 270000, -20000, 300)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2149)
    WaitChrThread(0xE, 0x1)

    def lambda_2168():
        OP_D1(254, 0, 270000, 0, 500)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_2168)
    WaitChrThread(0x9, 0x1)

    def lambda_2187():
        OP_D1(254, 0, 270000, 0, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2187)
    Sleep(1500)

    def lambda_21A6():
        OP_91(0xFE, 0x9C40, 0xFFFF8AD0, 0x0, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_21A6)
    Sleep(1000)

    def lambda_21C6():
        OP_91(0xFE, 0x9C40, 0xFFFF8AD0, 0x0, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_21C6)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_DC()
    OP_A2(0x10F7)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_19_1F12 end

    def Function_20_21F9(): pass

    label("Function_20_21F9")

    EventBegin(0x0)
    OP_DB()
    LoadEffect(0x1, "map\\\\mp077_00.eff")
    LoadEffect(0x2, "map\\\\mp077_01.eff")
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x4, 0x80)
    OP_6D(157720, -10000, 2940, 0)
    OP_67(0, 2670, -10000, 0)
    OP_6B(7460, 0)
    OP_6C(284000, 0)
    OP_6E(828, 0)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFE2, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFE2, 0xFFFFFFFB, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFC4, 0xFFFFFFF6, 0x0, 0x0, 0x0)
    OP_22(0x12B, 0x0, 0x64)
    OP_11(0xB8, 0xD8, 0xFF, 0x4E20, 0x877F8, 0x0)
    OP_A1(0x9, 0x5)
    SetChrPos(0x9, 200000, 0, 0, 270)
    ClearChrFlags(0x9, 0x100)
    OP_D1(9, 0, 270000, 0, 0)
    OP_22(0x12A, 0x0, 0x64)
    OP_B0(0x5, 0x3C)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 1340)
    OP_70(0x5, 0x604)
    OP_A1(0xE, 0x0)
    SetChrPos(0xE, -50000, 0, 0, 270)
    ClearChrFlags(0xE, 0x100)
    OP_D1(14, 0, 270000, 0, 0)
    OP_71(0x0, 0x20)
    OP_B0(0x0, 0x19)
    OP_6F(0x0, 10)
    OP_70(0x0, 0x1E)
    OP_43(0xF, 0x3, 0x0, 0x15)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)

    def lambda_2384():

        label("loc_2384")

        OP_7C(0x64, 0x64, 0xBB8, 0x64)
        OP_48()
        Jump("loc_2384")

    QueueWorkItem2(0xF, 0, lambda_2384)
    FadeToBright(1000, 0)
    OP_0D()
    OP_43(0xE, 0x0, 0x0, 0x16)
    Sleep(4600)

    def lambda_23B5():
        OP_D1(254, 0, 276000, -20000, 4000)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_23B5)

    def lambda_23CF():
        OP_6D(157720, -8000, 2940, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_23CF)

    def lambda_23E7():
        OP_D0(15000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_23E7)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    Sleep(3000)

    def lambda_2406():
        OP_D1(254, 0, 268000, 15000, 4000)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2406)

    def lambda_2420():
        OP_6D(157720, -8000, -2940, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2420)

    def lambda_2438():
        OP_D0(-15000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2438)

    def lambda_2448():
        OP_6C(256000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2448)

    def lambda_2458():
        OP_6B(7860, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2458)
    WaitChrThread(0x101, 0x3)

    def lambda_246D():
        OP_6B(7460, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_246D)
    WaitChrThread(0xE, 0x0)
    OP_43(0xE, 0x0, 0x0, 0x17)
    Sleep(1600)
    PlayEffect(0x1, 0xFF, 0xFF, 95000, -5000, 20000, 270, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0xFF, 0xFF, 90000, -15000, 25000, 270, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xE, 0x0)
    WaitChrThread(0xE, 0x1)
    OP_44(0xF, 0x3)
    OP_71(0x0, 0x4)
    OP_72(0x0, 0x20)
    OP_73(0x0)

    def lambda_2518():
        OP_6D(166500, -10000, -19590, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2518)

    def lambda_2530():
        OP_6C(238000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2530)

    def lambda_2540():
        OP_6E(876, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2540)
    Sleep(1000)
    OP_72(0x0, 0x20)
    OP_73(0x0)
    OP_43(0x9, 0x0, 0x0, 0x18)
    Sleep(1600)
    PlayEffect(0x1, 0xFF, 0xFF, 180000, 0, 0, 270, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0xF, 0x0)
    SetMapFlags(0x2000000)
    OP_DC()
    OP_A2(0x10F7)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_20_21F9 end

    def Function_21_25BF(): pass

    label("Function_21_25BF")

    Sleep(400)

    label("loc_25C4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_25DA")
    OP_22(0x120, 0x0, 0x50)
    Sleep(800)
    Jump("loc_25C4")

    label("loc_25DA")

    Return()

    # Function_21_25BF end

    def Function_22_25DB(): pass

    label("Function_22_25DB")

    OP_94(0x1, 0xE, 0xB4, 0x7530, 0x2710, 0x0)

    def lambda_25F0():
        OP_97(0xFE, 0x30D40, 0x0, 0x1F40, 0x1388, 0x3)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_25F0)

    def lambda_260C():
        OP_D1(254, 0, 270000, -20000, 3000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_260C)
    WaitChrThread(0xE, 0x2)
    OP_44(0xE, 0x3)

    def lambda_262F():
        OP_D1(254, 0, 270000, 0, 3000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_262F)
    OP_94(0x1, 0xE, 0xB4, 0x7530, 0x2710, 0x0)

    def lambda_2658():
        OP_97(0xFE, 0x30D40, 0x0, 0xFFFFD8F0, 0x1388, 0x3)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_2658)

    def lambda_2674():
        OP_D1(254, 0, 270000, 20000, 3000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_2674)
    WaitChrThread(0xE, 0x2)
    OP_44(0xE, 0x3)

    def lambda_2697():
        OP_D1(254, 0, 270000, 0, 3000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_2697)
    OP_8F(0xE, 0x186A0, 0x0, 0x0, 0x4650, 0x0)
    Return()

    # Function_22_25DB end

    def Function_23_26C0(): pass

    label("Function_23_26C0")


    def lambda_26C6():
        OP_D1(254, 0, 270000, -20000, 2000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_26C6)

    def lambda_26E0():
        OP_8F(0xFE, 0x15F90, 0xFFFF63C0, 0x9C40, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_26E0)
    Sleep(400)

    def lambda_2700():
        OP_8F(0xFE, 0x15F90, 0xFFFF63C0, 0x9C40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2700)
    Sleep(300)

    def lambda_2720():
        OP_8F(0xFE, 0x15F90, 0xFFFF63C0, 0x9C40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2720)
    Sleep(200)

    def lambda_2740():
        OP_8F(0xFE, 0x15F90, 0xFFFF63C0, 0x9C40, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2740)
    Sleep(100)

    def lambda_2760():
        OP_8F(0xFE, 0x15F90, 0xFFFF63C0, 0x9C40, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2760)
    Sleep(100)

    def lambda_2780():
        OP_8F(0xFE, 0x15F90, 0xFFFF63C0, 0x9C40, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2780)
    Return()

    # Function_23_26C0 end

    def Function_24_2796(): pass

    label("Function_24_2796")


    def lambda_279C():
        OP_D1(254, 0, 270000, 0, 4000)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_279C)

    def lambda_27B6():
        OP_8F(0xFE, 0x222E0, 0xFFFF63C0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_27B6)
    Sleep(500)

    def lambda_27D6():
        OP_8F(0xFE, 0x222E0, 0xFFFF63C0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_27D6)
    Sleep(400)

    def lambda_27F6():
        OP_8F(0xFE, 0x222E0, 0xFFFF63C0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_27F6)
    Sleep(300)

    def lambda_2816():
        OP_8F(0xFE, 0x222E0, 0xFFFF63C0, 0x0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2816)
    Sleep(200)

    def lambda_2836():
        OP_8F(0xFE, 0x222E0, 0xFFFF63C0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2836)
    Sleep(100)

    def lambda_2856():
        OP_8F(0xFE, 0x222E0, 0xFFFF63C0, 0x0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2856)
    Return()

    # Function_24_2796 end

    def Function_25_286C(): pass

    label("Function_25_286C")

    EventBegin(0x0)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-8910, 6280, -6210, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(20340, 0)
    OP_6C(31000, 0)
    OP_6E(262, 0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_11(0xB8, 0xD8, 0xFF, 0x0, 0x9EB10, 0x0)
    OP_71(0x0, 0x4)
    OP_A1(0x9, 0x5)
    SetChrPos(0x9, 0, 0, 0, 270)
    OP_22(0x125, 0x1, 0x46)
    OP_22(0x79, 0x1, 0x46)
    OP_71(0x5, 0x20)
    OP_B0(0x5, 0x14)
    OP_6F(0x5, 330)
    OP_70(0x5, 0x1AE)
    OP_48()
    OP_A1(0xA, 0x1)
    OP_A1(0xB, 0x2)
    OP_A1(0xC, 0x3)
    OP_A1(0xD, 0x4)
    SetChrPos(0xA, 33000, 0, 32000, 90)
    SetChrPos(0xB, 29000, 0, -30000, 90)
    SetChrPos(0xC, -31000, 0, 31000, 90)
    SetChrPos(0xD, -34000, 0, -33000, 90)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x13, 0x20)
    SetChrBattleFlags(0x12, 0x20)
    OP_89(0x13, -18360, 3000, -500, 270)
    OP_89(0x12, -17700, 3000, 690, 270)

    def lambda_29A6():
        OP_67(0, 4670, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_29A6)

    def lambda_29BE():
        OP_6B(18000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_29BE)
    OP_C8(0x200, 0x46, "C_PLAC17._CH", 0x1, 0x3E8)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    Fade(1000)
    OP_11(0xB8, 0xD8, 0xFF, 0x4E20, 0x56AB8, 0x0)
    OP_6D(-18070, 3020, 390, 0)
    OP_67(0, 6660, -10000, 0)
    OP_6B(2960, 0)
    OP_6C(45000, 0)
    OP_6E(299, 0)
    OP_0D()
    Sleep(1000)
    SetChrPos(0x14, -36450, -220, 4480, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x40)
    OP_22(0x197, 0x0, 0x64)
    Sleep(500)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_DC()

    ChrTalk(    #0
        0x12,
        "#171F#4PSieg!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x13,
        "#161F#4POho, there he is!\x02",
    )

    CloseMessageWindow()
    OP_43(0x14, 0x0, 0x0, 0x2)

    def lambda_2AE1():
        OP_6D(-28310, 3530, 600, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2AE1)

    def lambda_2AF9():

        label("loc_2AF9")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_2AF9")

    QueueWorkItem2(0x13, 1, lambda_2AF9)
    WaitChrThread(0x101, 0x2)
    ClearChrFlags(0x14, 0x1)
    Sleep(500)

    def lambda_2B19():
        OP_6D(-18070, 3020, 390, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2B19)
    OP_22(0x8C, 0x0, 0x64)

    def lambda_2B36():
        OP_8E(0x14, 0xFFFFB69A, 0x1388, 0x60E, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_2B36)
    Sleep(1000)

    def lambda_2B56():
        OP_8E(0x14, 0xFFFFB69A, 0x1388, 0x60E, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_2B56)
    Sleep(500)

    def lambda_2B76():
        OP_8E(0x14, 0xFFFFB69A, 0x1388, 0x60E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_2B76)
    Sleep(500)

    def lambda_2B96():
        OP_8E(0x14, 0xFFFFB69A, 0x1388, 0x60E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_2B96)
    WaitChrThread(0x14, 0x2)
    SetChrChipByIndex(0x14, 4)
    SetChrSubChip(0x14, 0)

    def lambda_2BC0():
        OP_8C(0x14, 180, 100)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_2BC0)

    def lambda_2BCE():
        OP_8C(0x12, 270, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2BCE)
    SetChrFlags(0x12, 0x20)
    Fade(250)
    SetChrChipByIndex(0x12, 3)
    SetChrSubChip(0x12, 2)
    WaitChrThread(0x14, 0x3)
    OP_8F(0x14, 0xFFFFB960, 0xC80, 0x3A2, 0x5DC, 0x0)
    Fade(250)
    SetChrChipByIndex(0x12, 3)
    SetChrSubChip(0x12, 0)
    SetChrFlags(0x14, 0x80)
    OP_0D()
    OP_44(0x13, 0x1)

    ChrTalk(    #2
        0x14,
        "#311FScreeee!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05Julia took the message from Sieg's leg.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x12)
    Sleep(400)
    TurnDirection(0x12, 0x13, 400)
    Sleep(400)

    ChrTalk(    #4
        0x12,
        (
            "#178F#6PLet's see... Estelle's group has arrived at\x01",
            "the mountain where they believe the dragon\x01",
            "to be.\x02\x03",

            "They're going to enter and search.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x13,
        "#160F#4PI see.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x13, 270, 400)
    Sleep(500)

    ChrTalk(    #6
        0x13,
        (
            "#163F#6P...Transmit to all ships!\x02\x03",

            "Stand by at designated coordinates with\x01",
            "armor piercing rounds loaded!\x02\x03",

            "#162FIf the dragon attempts to flee...\x01",
            "do not allow it to escape!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #7
        0x12,
        "#177F#6PYes, sir!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C1600   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_25_286C end

    def Function_26_2E4C(): pass

    label("Function_26_2E4C")


    def lambda_2E52():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E52)
    Sleep(500)

    def lambda_2E72():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E72)
    Sleep(500)

    def lambda_2E92():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0x0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E92)
    Sleep(500)

    def lambda_2EB2():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2EB2)
    Sleep(500)

    def lambda_2ED2():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2ED2)
    Sleep(500)

    def lambda_2EF2():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0x0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2EF2)
    Return()

    # Function_26_2E4C end

    def Function_27_2F08(): pass

    label("Function_27_2F08")

    EventBegin(0x0)
    OP_DB()
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFFD, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFFD, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFF8, 0x0, 0x0, 0x0, 0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS244._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS245._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS244._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_C6(0x2, 0x3, -1, 0, 0)
    Sleep(2000)
    OP_C6(0x1, 0x0, -174000, -113000, 0)
    OP_C6(0x1, 0x1, 1300, 1300, 0)
    OP_C6(0x2, 0x0, -174000, -113000, 0)
    OP_C6(0x2, 0x1, 1300, 1300, 0)
    OP_C6(0x0, 0x0, -174000, -113000, 1000)
    OP_C6(0x0, 0x1, 1300, 1300, 1000)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    OP_C7(0x0, 0x0, 0x0)
    OP_C7(0x0, 0x0, 0x1)
    Sleep(1500)
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x0, 0, -66000, 1000)
    OP_C6(0x2, 0x0, 0, -66000, 1000)
    Sleep(400)
    OP_C6(0x1, 0x3, -1, 1000, 0)
    OP_C7(0x0, 0x1, 0x0)
    OP_C7(0x0, 0x1, 0x3)
    Sleep(2000)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x2, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    OP_C6(0x0, 0x6, 0, 0, 0)
    OP_C6(0x1, 0x6, 0, 0, 0)
    OP_C6(0x2, 0x6, 0, 0, 0)
    OP_6D(-19120, 5000, -3020, 0)
    OP_67(0, 5210, -10000, 0)
    OP_6B(3990, 0)
    OP_6C(61000, 0)
    OP_6E(597, 0)
    OP_22(0x1C3, 0x0, 0x64)
    SetChrPos(0x11, -12000, -2550, 20000, 0)
    SetChrPos(0xF, -19120, 5000, -3020, 0)
    OP_6A(0xF)
    OP_A1(0x9, 0x5)
    SetChrPos(0x9, 0, 0, 0, 270)
    OP_22(0x125, 0x1, 0x50)
    OP_B0(0x5, 0x1E)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 330)
    OP_70(0x5, 0x1AE)

    def lambda_31FE():
        OP_91(0xFE, 0xFFFB6C20, 0x0, 0x0, 0x7D00, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_31FE)

    def lambda_3219():
        OP_91(0xFE, 0xFFFB6C20, 0x0, 0x0, 0x7D00, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3219)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2000)
    Sleep(1500)
    Sleep(1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC()
    SetMapFlags(0x2000000)
    OP_A2(0x10FC)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_27_2F08 end

    def Function_28_3265(): pass

    label("Function_28_3265")

    EventBegin(0x0)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrPos(0x0, -119400, -10000, -115010, 0)
    OP_71(0x0, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x1, 0x20)
    OP_B0(0x1, 0xF)
    OP_6F(0x1, 400)
    OP_70(0x1, 0x1CC)
    OP_22(0x79, 0x1, 0x64)
    OP_A1(0xA, 0x1)
    SetChrPos(0xA, -99470, 15000, -91440, 270)
    ClearChrFlags(0xA, 0x100)
    OP_D1(10, 45000, 270000, 0, 0)
    OP_43(0xA, 0x1, 0x0, 0x1F)
    OP_6D(-109880, -10000, -98990, 0)
    OP_67(0, -16070, -10000, 0)
    OP_6B(6000, 0)
    OP_6C(119000, 0)
    OP_6E(699, 0)
    FadeToBright(1000, 0)

    def lambda_333E():
        OP_6D(-95610, -10000, -97790, 5000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_333E)

    def lambda_3356():
        OP_6B(2750, 5000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3356)

    def lambda_3366():
        OP_8F(0xFE, 0xFFFE507A, 0xFFFEC780, 0xFFFE9AD0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_3366)
    Sleep(1000)
    SetMessageWindowPos(350, 60, -1, -1)
    SetChrName("Josette")

    AnonymousTalk(    #8 op#5
        "\x07\x00#210FOhhhh craaaaaaaaap!\x05\x02",
    )

    Sleep(1500)
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(80, 60, -1, -1)
    SetChrName("Don")

    AnonymousTalk(    #9 op#5
        "#190FRRRRRRRAAAAAAAAAAGH!\x05\x02",
    )

    Sleep(1500)
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    WaitChrThread(0x0, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_AD(0x2400AB, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    OP_DC()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T2100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_28_3265 end

    def Function_29_3440(): pass

    label("Function_29_3440")

    EventBegin(0x0)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_71(0x0, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_72(0x1, 0x20)
    OP_72(0x1, 0x8)
    OP_6F(0x1, 360)
    OP_A1(0xA, 0x1)
    ClearChrFlags(0xA, 0x100)
    SetChrPos(0xA, 0, 40000, 0, 270)
    OP_D1(10, 45000, 270000, 0, 0)
    OP_6D(-44780, -10000, -24460, 0)
    OP_67(0, -16059, -10000, 0)
    OP_6B(6000, 0)
    OP_6C(144000, 0)
    OP_6E(700, 0)
    ClearMapFlags(0x100000)
    FadeToBright(1000, 0)

    def lambda_34FB():
        OP_6D(-53240, -10000, -30460, 3000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_34FB)
    OP_43(0x0, 0x1, 0x0, 0x1E)
    OP_43(0xA, 0x0, 0x0, 0x1F)

    def lambda_3521():
        OP_D1(254, 90000, 270000, -20000, 3000)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_3521)
    OP_0D()
    SetMessageWindowPos(350, 60, -1, -1)
    SetChrName("Josette")

    AnonymousTalk(    #10 op#5
        "\x07\x00#216F#3SOhhhh craaaaaaaaap!\x05\x02",
    )

    Sleep(2500)
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(120, 260, -1, -1)
    SetChrName("Don")

    AnonymousTalk(    #11 op#5
        "#192F#3SRRRRRRRAAAAAAAAAAGH!\x05\x02",
    )

    Sleep(2000)
    OP_56(0x0)
    FadeToDark(2000, 0, -1)
    OP_24(0x79, 0x5A)
    Sleep(100)
    OP_24(0x79, 0x50)
    Sleep(100)
    OP_24(0x79, 0x46)
    Sleep(100)
    OP_24(0x79, 0x3C)
    Sleep(100)
    OP_24(0x79, 0x32)
    OP_0D()
    OP_44(0x0, 0x2)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_23(0x79)
    Sleep(1000)
    OP_AD(0x2400AB, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    OP_20(0x7D0)
    OP_21()
    ClearMapFlags(0x2000000)
    OP_DC()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T2100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_29_3440 end

    def Function_30_3621(): pass

    label("Function_30_3621")

    OP_7C(0x320, 0xC8, 0x7D0, 0x3E8)
    Sleep(1000)
    OP_7C(0x258, 0xA0, 0x5DC, 0x3E8)
    Sleep(1000)
    OP_7C(0x190, 0x78, 0x3E8, 0x3E8)
    Return()

    # Function_30_3621 end

    def Function_31_365F(): pass

    label("Function_31_365F")


    def lambda_3665():
        OP_8F(0xFE, 0xFFFEA070, 0xFFFE7960, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3665)
    Sleep(400)

    def lambda_3685():
        OP_8F(0xFE, 0xFFFEA070, 0xFFFE7960, 0x0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3685)
    Sleep(300)

    def lambda_36A5():
        OP_8F(0xFE, 0xFFFEA070, 0xFFFE7960, 0x0, 0x7D00, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_36A5)
    Sleep(200)

    def lambda_36C5():
        OP_8F(0xFE, 0xFFFEA070, 0xFFFE7960, 0x0, 0xB3B0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_36C5)
    Sleep(100)

    def lambda_36E5():
        OP_8F(0xFE, 0xFFFEA070, 0xFFFE7960, 0x0, 0xF230, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_36E5)
    Return()

    # Function_31_365F end

    def Function_32_36FB(): pass

    label("Function_32_36FB")

    EventBegin(0x0)
    OP_DB()
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFFB, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFFE, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFFB, 0xFFFFFFFE, 0x0, 0x0, 0x0)
    OP_11(0xB8, 0xD8, 0xFF, 0x4E20, 0x877F8, 0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_6D(10490, -10000, 13050, 0)
    OP_67(0, 5750, -10000, 0)
    OP_6B(18200, 0)
    OP_6C(48000, 0)
    OP_6E(337, 0)
    OP_22(0x1C3, 0x0, 0x64)
    SetChrPos(0x0, 76380, 1000, -14320, 0)
    OP_A1(0x9, 0x5)
    ClearChrFlags(0x9, 0x100)
    OP_D1(9, 0, 270000, 0, 0)
    SetChrPos(0x9, 50000, 0, 0, 270)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 1100)
    OP_70(0x5, 0x514)
    OP_22(0x125, 0x1, 0x50)
    FadeToBright(2000, 0)

    def lambda_3828():
        OP_6D(9890, -10000, 26390, 7000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_3828)

    def lambda_3840():
        OP_67(0, 3280, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3840)

    def lambda_3858():
        OP_6C(37000, 7000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_3858)

    def lambda_3868():
        OP_6B(12900, 7000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_3868)

    def lambda_3878():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3878)
    WaitChrThread(0x9, 0x1)
    OP_72(0x5, 0x20)
    OP_73(0x5)
    OP_6F(0x5, 1300)
    OP_70(0x5, 0x53C)
    OP_22(0xDD, 0x0, 0x64)
    Sleep(240)
    OP_22(0xDD, 0x0, 0x64)
    Sleep(240)
    OP_22(0xDD, 0x0, 0x64)
    OP_73(0x5)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 1340)
    OP_70(0x5, 0x604)
    Sleep(400)

    def lambda_38E2():
        OP_6D(-209890, 1000, 280, 3000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_38E2)

    def lambda_38FA():
        OP_67(0, 720, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_38FA)

    def lambda_3912():
        OP_6C(277000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_3912)

    def lambda_3922():
        OP_D1(254, 0, 270000, -20000, 5000)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_3922)

    def lambda_393C():
        OP_8F(0xFE, 0xFFF85EE0, 0x0, 0x4E20, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_393C)
    Sleep(100)

    def lambda_395C():
        OP_8F(0xFE, 0xFFF85EE0, 0x0, 0x4E20, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_395C)
    Sleep(100)

    def lambda_397C():
        OP_8F(0xFE, 0xFFF85EE0, 0x0, 0x4E20, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_397C)
    Sleep(100)

    def lambda_399C():
        OP_8F(0xFE, 0xFFF85EE0, 0x0, 0x4E20, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_399C)
    Sleep(100)

    def lambda_39BC():
        OP_8F(0xFE, 0xFFF85EE0, 0x0, 0x4E20, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_39BC)
    Sleep(100)

    def lambda_39DC():
        OP_8F(0xFE, 0xFFF85EE0, 0x0, 0x4E20, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_39DC)
    Sleep(100)

    def lambda_39FC():
        OP_8F(0xFE, 0xFFF85EE0, 0x0, 0x4E20, 0xEA60, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_39FC)
    Sleep(100)

    def lambda_3A1C():
        OP_8F(0xFE, 0xFFF85EE0, 0x0, 0x4E20, 0x11170, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3A1C)
    Sleep(100)

    def lambda_3A3C():
        OP_8F(0xFE, 0xFFF85EE0, 0x0, 0x4E20, 0x13880, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3A3C)
    Sleep(100)

    def lambda_3A5C():
        OP_8F(0xFE, 0xFFF85EE0, 0x0, 0x4E20, 0x15F90, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3A5C)
    Sleep(100)

    def lambda_3A7C():
        OP_8F(0xFE, 0xFFF85EE0, 0x0, 0x4E20, 0x186A0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3A7C)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC()
    SetMapFlags(0x2000000)
    OP_A2(0x10FF)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_32_36FB end

    SaveToFile()

Try(main)
