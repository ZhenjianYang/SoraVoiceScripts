from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        '红色飞艇',                             # 9
        '埃尔赛尤',                             # 10
        '警备艇',                               # 11
        '警备艇',                               # 12
        '警备艇',                               # 13
        '警备艇',                               # 14
        '古代龙',                               # 15
        '目标用照相机',                         # 16
        '目标用照相机',                         # 17
        '目标',                                 # 18
        '尤莉亚上尉',                           # 19
        '摩尔根将军',                           # 20
        '基库',                                 # 21
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
        "Function_4_57E",          # 04, 4
        "Function_5_AE6",          # 05, 5
        "Function_6_10E1",         # 06, 6
        "Function_7_1124",         # 07, 7
        "Function_8_1220",         # 08, 8
        "Function_9_131C",         # 09, 9
        "Function_10_13B8",        # 0A, 10
        "Function_11_1454",        # 0B, 11
        "Function_12_14CA",        # 0C, 12
        "Function_13_1540",        # 0D, 13
        "Function_14_17EB",        # 0E, 14
        "Function_15_1D5D",        # 0F, 15
        "Function_16_1D74",        # 10, 16
        "Function_17_1DF0",        # 11, 17
        "Function_18_1E6C",        # 12, 18
        "Function_19_1F08",        # 13, 19
        "Function_20_21ED",        # 14, 20
        "Function_21_25B1",        # 15, 21
        "Function_22_25CD",        # 16, 22
        "Function_23_26B2",        # 17, 23
        "Function_24_2788",        # 18, 24
        "Function_25_285E",        # 19, 25
        "Function_26_2DC8",        # 1A, 26
        "Function_27_2E84",        # 1B, 27
        "Function_28_31A8",        # 1C, 28
        "Function_29_3376",        # 1D, 29
        "Function_30_354A",        # 1E, 30
        "Function_31_3588",        # 1F, 31
        "Function_32_3624",        # 20, 32
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

    def lambda_458():
        OP_90(0xFE, 0xFFFC2F70, 0x0, 0x0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_458)

    def lambda_473():
        OP_90(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_473)
    OP_24(0x79, 0x50)
    Sleep(1000)
    OP_24(0x79, 0x55)
    Sleep(1000)
    OP_24(0x79, 0x5A)
    Sleep(1000)
    OP_24(0x79, 0x5F)
    Sleep(1000)
    OP_24(0x79, 0x64)

    def lambda_4B6():
        OP_6C(315000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4B6)
    Sleep(1000)

    def lambda_4CB():
        OP_90(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_4CB)
    Sleep(4000)

    def lambda_4EB():
        OP_90(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_4EB)
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
    OP_A2(0x10F0)
    NewScene("ED6_DT21/E0610   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_39B end

    def Function_4_57E(): pass

    label("Function_4_57E")

    EventBegin(0x0)
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

    def lambda_69E():
        OP_90(0x101, 0xFFFB6C20, 0x0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_69E)

    def lambda_6B9():
        OP_91(0xFE, 0xFFFB6C20, 0x0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_6B9)

    def lambda_6D4():
        OP_91(0xFE, 0xFFFB6C20, 0x0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6D4)

    def lambda_6EF():
        OP_91(0xFE, 0xFFFB6C20, 0x0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6EF)

    def lambda_70A():
        OP_91(0xFE, 0xFFFB6C20, 0x0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_70A)

    def lambda_725():
        OP_91(0xFE, 0xFFFB6C20, 0x0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_725)

    def lambda_740():
        OP_67(0, 6390, -10000, 12000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_740)

    def lambda_758():
        OP_6B(5200, 12000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_758)

    def lambda_768():
        OP_6C(74000, 12000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_768)

    def lambda_778():
        OP_6E(616, 12000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_778)
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

    def lambda_7CA():
        OP_91(0xFE, 0xFFFC0860, 0x0, 0x0, 0x7148, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7CA)

    def lambda_7E5():
        OP_91(0xFE, 0xFFFC0860, 0x0, 0x0, 0x7148, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_7E5)
    Sleep(5500)

    def lambda_805():
        OP_91(0xFE, 0xFFFD40E0, 0x0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_805)

    def lambda_820():
        OP_91(0xFE, 0xFFFD40E0, 0x0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_820)
    Sleep(1000)

    def lambda_840():
        OP_67(0, 4610, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_840)

    def lambda_858():
        OP_6B(5800, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_858)
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

    def lambda_A59():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_A59)

    def lambda_A74():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A74)

    def lambda_A8F():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A8F)
    Sleep(300)

    def lambda_AAF():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_AAF)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/E0311   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_4_57E end

    def Function_5_AE6(): pass

    label("Function_5_AE6")

    EventBegin(0x0)
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

    def lambda_C28():
        OP_6D(-12730, -2050, 11180, 8000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C28)

    def lambda_C40():
        OP_67(0, 3710, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C40)

    def lambda_C58():
        OP_6B(4100, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C58)

    def lambda_C68():
        OP_6C(26000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_C68)

    def lambda_C78():
        OP_6E(885, 8000)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_C78)
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

    def lambda_D32():
        OP_D1(254, 0, 90000, 25000, 4000)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_D32)
    Sleep(1500)
    OP_43(0xA, 0x0, 0x0, 0x7)

    def lambda_D58():
        OP_D1(254, 0, 90000, 25000, 4000)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_D58)
    WaitChrThread(0xB, 0x2)

    def lambda_D77():
        OP_D1(254, 0, 90000, 0, 2500)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_D77)
    WaitChrThread(0xA, 0x2)

    def lambda_D96():
        OP_D1(254, 0, 90000, 0, 2500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_D96)
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

    def lambda_F50():
        OP_6D(-19120, 5000, -3020, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F50)

    def lambda_F68():
        OP_67(0, 5210, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F68)

    def lambda_F80():
        OP_6B(4100, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F80)

    def lambda_F90():
        OP_6C(61000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_F90)

    def lambda_FA0():
        OP_6E(865, 4000)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_FA0)
    OP_43(0xA, 0x0, 0x0, 0x9)

    def lambda_FB7():
        OP_D1(254, 0, 100000, 30000, 3000)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_FB7)
    Sleep(1000)
    OP_43(0xB, 0x0, 0x0, 0xA)

    def lambda_FDD():
        OP_D1(254, 0, 90000, 30000, 3000)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_FDD)
    OP_43(0xA, 0x3, 0x0, 0x6)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0xF, 0x0)

    def lambda_1017():
        OP_67(0, 510, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1017)

    def lambda_102F():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_102F)
    Sleep(200)

    def lambda_104F():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_104F)
    Sleep(200)

    def lambda_106F():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_106F)
    Sleep(200)

    def lambda_108F():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_108F)
    Sleep(200)

    def lambda_10AF():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_10AF)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/E0311   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_5_AE6 end

    def Function_6_10E1(): pass

    label("Function_6_10E1")

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

    # Function_6_10E1 end

    def Function_7_1124(): pass

    label("Function_7_1124")


    def lambda_112A():
        OP_8F(0xFE, 0xFA0, 0x226, 0x12110, 0x7148, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_112A)
    Sleep(5000)

    def lambda_114A():
        OP_8F(0xFE, 0xFA0, 0x226, 0x12110, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_114A)
    Sleep(600)

    def lambda_116A():
        OP_8F(0xFE, 0xFA0, 0x226, 0x12110, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_116A)
    Sleep(500)

    def lambda_118A():
        OP_8F(0xFE, 0xFA0, 0x226, 0x12110, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_118A)
    Sleep(400)

    def lambda_11AA():
        OP_8F(0xFE, 0xFA0, 0x226, 0x12110, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_11AA)
    Sleep(300)

    def lambda_11CA():
        OP_8F(0xFE, 0xFA0, 0x226, 0x12110, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_11CA)
    Sleep(200)

    def lambda_11EA():
        OP_8F(0xFE, 0xFA0, 0x226, 0x12110, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_11EA)
    Sleep(100)

    def lambda_120A():
        OP_8F(0xFE, 0xFA0, 0x226, 0x12110, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_120A)
    Return()

    # Function_7_1124 end

    def Function_8_1220(): pass

    label("Function_8_1220")


    def lambda_1226():
        OP_8F(0xFE, 0xFFFFF448, 0xFFFFDE9A, 0xD2F0, 0x7148, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1226)
    Sleep(5000)

    def lambda_1246():
        OP_8F(0xFE, 0xFFFFF448, 0xFFFFDE9A, 0xD2F0, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1246)
    Sleep(600)

    def lambda_1266():
        OP_8F(0xFE, 0xFFFFF448, 0xFFFFDE9A, 0xD2F0, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1266)
    Sleep(500)

    def lambda_1286():
        OP_8F(0xFE, 0xFFFFF448, 0xFFFFDE9A, 0xD2F0, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1286)
    Sleep(400)

    def lambda_12A6():
        OP_8F(0xFE, 0xFFFFF448, 0xFFFFDE9A, 0xD2F0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_12A6)
    Sleep(300)

    def lambda_12C6():
        OP_8F(0xFE, 0xFFFFF448, 0xFFFFDE9A, 0xD2F0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_12C6)
    Sleep(200)

    def lambda_12E6():
        OP_8F(0xFE, 0xFFFFF448, 0xFFFFDE9A, 0xD2F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_12E6)
    Sleep(100)

    def lambda_1306():
        OP_8F(0xFE, 0xFFFFF448, 0xFFFFDE9A, 0xD2F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1306)
    Return()

    # Function_8_1220 end

    def Function_9_131C(): pass

    label("Function_9_131C")


    def lambda_1322():
        OP_8F(0xFE, 0xFFFF9A70, 0x226, 0x1BD50, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1322)
    Sleep(500)

    def lambda_1342():
        OP_8F(0xFE, 0xFFFF9A70, 0x226, 0x1BD50, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1342)
    Sleep(500)

    def lambda_1362():
        OP_8F(0xFE, 0xFFFF9A70, 0x226, 0x1BD50, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1362)
    Sleep(500)

    def lambda_1382():
        OP_8F(0xFE, 0xFFFF9A70, 0x226, 0x1BD50, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1382)
    Sleep(500)

    def lambda_13A2():
        OP_8F(0xFE, 0xFFFF9A70, 0x226, 0x1BD50, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_13A2)
    Return()

    # Function_9_131C end

    def Function_10_13B8(): pass

    label("Function_10_13B8")


    def lambda_13BE():
        OP_8F(0xFE, 0xFFFF7F18, 0xFFFFDE9A, 0x16F30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_13BE)
    Sleep(500)

    def lambda_13DE():
        OP_8F(0xFE, 0xFFFF7F18, 0xFFFFDE9A, 0x16F30, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_13DE)
    Sleep(500)

    def lambda_13FE():
        OP_8F(0xFE, 0xFFFF7F18, 0xFFFFDE9A, 0x16F30, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_13FE)
    Sleep(500)

    def lambda_141E():
        OP_8F(0xFE, 0xFFFF7F18, 0xFFFFDE9A, 0x16F30, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_141E)
    Sleep(500)

    def lambda_143E():
        OP_8F(0xFE, 0xFFFF7F18, 0xFFFFDE9A, 0x16F30, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_143E)
    Return()

    # Function_10_13B8 end

    def Function_11_1454(): pass

    label("Function_11_1454")


    def lambda_145A():
        OP_D1(10, 0, 90000, 45000, 800)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_145A)

    def lambda_1474():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0x30D40, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1474)
    Sleep(300)

    def lambda_1494():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0x30D40, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1494)
    Sleep(300)

    def lambda_14B4():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0x30D40, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_14B4)
    Return()

    # Function_11_1454 end

    def Function_12_14CA(): pass

    label("Function_12_14CA")


    def lambda_14D0():
        OP_D1(11, 0, 90000, -45000, 800)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_14D0)

    def lambda_14EA():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0xFFFCF2C0, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_14EA)
    Sleep(300)

    def lambda_150A():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0xFFFCF2C0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_150A)
    Sleep(300)

    def lambda_152A():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0xFFFCF2C0, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_152A)
    Return()

    # Function_12_14CA end

    def Function_13_1540(): pass

    label("Function_13_1540")

    EventBegin(0x0)
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

    def lambda_162B():
        OP_8F(0xFE, 0x4E20, 0x0, 0x0, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_162B)
    WaitChrThread(0xE, 0x1)
    Sleep(4000)
    OP_72(0x5, 0x4)

    def lambda_1655():
        OP_8F(0xFE, 0x1D4C0, 0x0, 0x0, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1655)

    def lambda_1670():
        OP_6D(28100, 5000, -5050, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1670)

    def lambda_1688():
        OP_67(0, 4320, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1688)

    def lambda_16A0():
        OP_6B(6700, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_16A0)

    def lambda_16B0():
        OP_6E(669, 2000)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_16B0)
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
    OP_A2(0x10F6)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_13_1540 end

    def Function_14_17EB(): pass

    label("Function_14_17EB")

    EventBegin(0x0)
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

    def lambda_1A11():
        OP_6D(24590, -10000, 10600, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1A11)

    def lambda_1A29():
        OP_67(0, 4490, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A29)

    def lambda_1A41():
        OP_6C(65000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1A41)

    def lambda_1A51():
        OP_6B(4910, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1A51)

    def lambda_1A61():
        OP_6E(1230, 2000)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_1A61)
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

    def lambda_1B20():
        OP_6D(20670, -10000, 3290, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1B20)

    def lambda_1B38():
        OP_67(0, 5480, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B38)

    def lambda_1B50():
        OP_6C(80000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1B50)
    PlayEffect(0x0, 0xFF, 0x9, -2270, -1780, -9290, 0, 0, 0, 5000, 5000, 5000, 0xE, -20000, -1000, -6000, 0)

    def lambda_1B95():
        OP_8F(0xFE, 0x0, 0x3E8, 0x1770, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1B95)
    OP_D1(14, 0, 270000, -30000, 1000)
    WaitChrThread(0xE, 0x1)
    Sleep(400)
    OP_43(0xE, 0x0, 0x0, 0x12)
    OP_D1(14, 0, 270000, 0, 1500)
    WaitChrThread(0xE, 0x0)
    WaitChrThread(0xE, 0x1)
    PlayEffect(0x0, 0xFF, 0x9, -2270, -1780, 9290, 0, 0, 0, 5000, 5000, 5000, 0xE, -20000, -1000, 6000, 0)

    def lambda_1C26():
        OP_8F(0xFE, 0x0, 0x3E8, 0xFFFFE890, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1C26)
    OP_D1(14, 0, 270000, 30000, 1000)
    WaitChrThread(0xE, 0x1)
    Sleep(400)
    OP_43(0xE, 0x0, 0x0, 0x12)
    OP_D1(14, 0, 270000, 0, 1500)
    WaitChrThread(0xE, 0x0)
    WaitChrThread(0xE, 0x1)

    def lambda_1C82():
        OP_8F(0xFE, 0xFFFE7960, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1C82)
    Sleep(500)

    def lambda_1CA2():
        OP_8F(0xFE, 0xFFFE7960, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1CA2)
    Sleep(400)

    def lambda_1CC2():
        OP_8F(0xFE, 0xFFFE7960, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1CC2)
    Sleep(300)

    def lambda_1CE2():
        OP_8F(0xFE, 0xFFFE7960, 0x0, 0x0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1CE2)
    Sleep(200)

    def lambda_1D02():
        OP_8F(0xFE, 0xFFFE7960, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1D02)
    Sleep(100)

    def lambda_1D22():
        OP_8F(0xFE, 0xFFFE7960, 0x0, 0x0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1D22)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0xE, 0x3)
    SetMapFlags(0x2000000)
    OP_A2(0x10F6)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_14_17EB end

    def Function_15_1D5D(): pass

    label("Function_15_1D5D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1D73")
    OP_22(0x120, 0x0, 0x64)
    Sleep(1300)
    Jump("Function_15_1D5D")

    label("loc_1D73")

    Return()

    # Function_15_1D5D end

    def Function_16_1D74(): pass

    label("Function_16_1D74")


    def lambda_1D7A():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1D7A)
    Sleep(1500)

    def lambda_1D9A():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1D9A)
    Sleep(300)

    def lambda_1DBA():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1DBA)
    Sleep(100)

    def lambda_1DDA():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1DDA)
    Return()

    # Function_16_1D74 end

    def Function_17_1DF0(): pass

    label("Function_17_1DF0")


    def lambda_1DF6():
        OP_8F(0xFE, 0x1D4C0, 0x0, 0x0, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1DF6)
    Sleep(1500)

    def lambda_1E16():
        OP_8F(0xFE, 0x1D4C0, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1E16)
    Sleep(300)

    def lambda_1E36():
        OP_8F(0xFE, 0x1D4C0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1E36)
    Sleep(100)

    def lambda_1E56():
        OP_8F(0xFE, 0x1D4C0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1E56)
    Return()

    # Function_17_1DF0 end

    def Function_18_1E6C(): pass

    label("Function_18_1E6C")


    def lambda_1E72():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1E72)
    Sleep(100)

    def lambda_1E92():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1E92)
    Sleep(100)

    def lambda_1EB2():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1EB2)
    Sleep(500)

    def lambda_1ED2():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1ED2)
    Sleep(100)

    def lambda_1EF2():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1EF2)
    Return()

    # Function_18_1E6C end

    def Function_19_1F08(): pass

    label("Function_19_1F08")

    EventBegin(0x0)
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

    def lambda_2001():
        OP_91(0xFE, 0x0, 0x0, 0x4E20, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2001)

    def lambda_201C():
        OP_D1(254, 0, 270000, -30000, 300)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_201C)
    Sleep(500)

    def lambda_203B():
        OP_91(0xFE, 0x0, 0x0, 0x4E20, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_203B)

    def lambda_2056():
        OP_D1(254, 0, 270000, -20000, 300)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2056)
    WaitChrThread(0xE, 0x1)

    def lambda_2075():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF63C0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2075)

    def lambda_2090():
        OP_D1(254, 0, 270000, 30000, 300)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_2090)
    WaitChrThread(0x9, 0x1)

    def lambda_20AF():
        OP_91(0xFE, 0x0, 0x0, 0xFFFF63C0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_20AF)

    def lambda_20CA():
        OP_D1(254, 0, 270000, 20000, 300)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_20CA)
    WaitChrThread(0xE, 0x1)

    def lambda_20E9():
        OP_8F(0xFE, 0xC350, 0x0, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_20E9)

    def lambda_2104():
        OP_D1(254, 0, 270000, -30000, 300)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_2104)
    WaitChrThread(0x9, 0x1)

    def lambda_2123():
        OP_8F(0xFE, 0x249F0, 0x0, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2123)

    def lambda_213E():
        OP_D1(254, 0, 270000, -20000, 300)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_213E)
    WaitChrThread(0xE, 0x1)

    def lambda_215D():
        OP_D1(254, 0, 270000, 0, 500)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_215D)
    WaitChrThread(0x9, 0x1)

    def lambda_217C():
        OP_D1(254, 0, 270000, 0, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_217C)
    Sleep(1500)

    def lambda_219B():
        OP_91(0xFE, 0x9C40, 0xFFFF8AD0, 0x0, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_219B)
    Sleep(1000)

    def lambda_21BB():
        OP_91(0xFE, 0x9C40, 0xFFFF8AD0, 0x0, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_21BB)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F7)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_19_1F08 end

    def Function_20_21ED(): pass

    label("Function_20_21ED")

    EventBegin(0x0)
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

    def lambda_2377():

        label("loc_2377")

        OP_7C(0x64, 0x64, 0xBB8, 0x64)
        OP_48()
        Jump("loc_2377")

    QueueWorkItem2(0xF, 0, lambda_2377)
    FadeToBright(1000, 0)
    OP_0D()
    OP_43(0xE, 0x0, 0x0, 0x16)
    Sleep(4600)

    def lambda_23A8():
        OP_D1(254, 0, 276000, -20000, 4000)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_23A8)

    def lambda_23C2():
        OP_6D(157720, -8000, 2940, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_23C2)

    def lambda_23DA():
        OP_D0(15000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_23DA)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    Sleep(3000)

    def lambda_23F9():
        OP_D1(254, 0, 268000, 15000, 4000)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_23F9)

    def lambda_2413():
        OP_6D(157720, -8000, -2940, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2413)

    def lambda_242B():
        OP_D0(-15000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_242B)

    def lambda_243B():
        OP_6C(256000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_243B)

    def lambda_244B():
        OP_6B(7860, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_244B)
    WaitChrThread(0x101, 0x3)

    def lambda_2460():
        OP_6B(7460, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2460)
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

    def lambda_250B():
        OP_6D(166500, -10000, -19590, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_250B)

    def lambda_2523():
        OP_6C(238000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2523)

    def lambda_2533():
        OP_6E(876, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2533)
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
    OP_A2(0x10F7)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_20_21ED end

    def Function_21_25B1(): pass

    label("Function_21_25B1")

    Sleep(400)

    label("loc_25B6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_25CC")
    OP_22(0x120, 0x0, 0x50)
    Sleep(800)
    Jump("loc_25B6")

    label("loc_25CC")

    Return()

    # Function_21_25B1 end

    def Function_22_25CD(): pass

    label("Function_22_25CD")

    OP_94(0x1, 0xE, 0xB4, 0x7530, 0x2710, 0x0)

    def lambda_25E2():
        OP_97(0xFE, 0x30D40, 0x0, 0x1F40, 0x1388, 0x3)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_25E2)

    def lambda_25FE():
        OP_D1(254, 0, 270000, -20000, 3000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_25FE)
    WaitChrThread(0xE, 0x2)
    OP_44(0xE, 0x3)

    def lambda_2621():
        OP_D1(254, 0, 270000, 0, 3000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_2621)
    OP_94(0x1, 0xE, 0xB4, 0x7530, 0x2710, 0x0)

    def lambda_264A():
        OP_97(0xFE, 0x30D40, 0x0, 0xFFFFD8F0, 0x1388, 0x3)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_264A)

    def lambda_2666():
        OP_D1(254, 0, 270000, 20000, 3000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_2666)
    WaitChrThread(0xE, 0x2)
    OP_44(0xE, 0x3)

    def lambda_2689():
        OP_D1(254, 0, 270000, 0, 3000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_2689)
    OP_8F(0xE, 0x186A0, 0x0, 0x0, 0x4650, 0x0)
    Return()

    # Function_22_25CD end

    def Function_23_26B2(): pass

    label("Function_23_26B2")


    def lambda_26B8():
        OP_D1(254, 0, 270000, -20000, 2000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_26B8)

    def lambda_26D2():
        OP_8F(0xFE, 0x15F90, 0xFFFF63C0, 0x9C40, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_26D2)
    Sleep(400)

    def lambda_26F2():
        OP_8F(0xFE, 0x15F90, 0xFFFF63C0, 0x9C40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_26F2)
    Sleep(300)

    def lambda_2712():
        OP_8F(0xFE, 0x15F90, 0xFFFF63C0, 0x9C40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2712)
    Sleep(200)

    def lambda_2732():
        OP_8F(0xFE, 0x15F90, 0xFFFF63C0, 0x9C40, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2732)
    Sleep(100)

    def lambda_2752():
        OP_8F(0xFE, 0x15F90, 0xFFFF63C0, 0x9C40, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2752)
    Sleep(100)

    def lambda_2772():
        OP_8F(0xFE, 0x15F90, 0xFFFF63C0, 0x9C40, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2772)
    Return()

    # Function_23_26B2 end

    def Function_24_2788(): pass

    label("Function_24_2788")


    def lambda_278E():
        OP_D1(254, 0, 270000, 0, 4000)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_278E)

    def lambda_27A8():
        OP_8F(0xFE, 0x222E0, 0xFFFF63C0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_27A8)
    Sleep(500)

    def lambda_27C8():
        OP_8F(0xFE, 0x222E0, 0xFFFF63C0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_27C8)
    Sleep(400)

    def lambda_27E8():
        OP_8F(0xFE, 0x222E0, 0xFFFF63C0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_27E8)
    Sleep(300)

    def lambda_2808():
        OP_8F(0xFE, 0x222E0, 0xFFFF63C0, 0x0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2808)
    Sleep(200)

    def lambda_2828():
        OP_8F(0xFE, 0x222E0, 0xFFFF63C0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2828)
    Sleep(100)

    def lambda_2848():
        OP_8F(0xFE, 0x222E0, 0xFFFF63C0, 0x0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2848)
    Return()

    # Function_24_2788 end

    def Function_25_285E(): pass

    label("Function_25_285E")

    EventBegin(0x0)
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

    def lambda_2997():
        OP_67(0, 4670, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2997)

    def lambda_29AF():
        OP_6B(18000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_29AF)
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

    ChrTalk(    #0
        0x12,
        "#171F#2P基库！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x13,
        "#161F#2P哟，来了啊！\x02",
    )

    CloseMessageWindow()
    OP_43(0x14, 0x0, 0x0, 0x2)

    def lambda_2ACD():
        OP_6D(-28310, 3530, 600, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2ACD)

    def lambda_2AE5():

        label("loc_2AE5")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_2AE5")

    QueueWorkItem2(0x13, 1, lambda_2AE5)
    WaitChrThread(0x101, 0x2)
    Sleep(500)

    def lambda_2B00():
        OP_6D(-18070, 3020, 390, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2B00)
    OP_22(0x8C, 0x0, 0x64)

    def lambda_2B1D():
        OP_8E(0x14, 0xFFFFB69A, 0x1388, 0x60E, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_2B1D)
    Sleep(1000)

    def lambda_2B3D():
        OP_8E(0x14, 0xFFFFB69A, 0x1388, 0x60E, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_2B3D)
    Sleep(500)

    def lambda_2B5D():
        OP_8E(0x14, 0xFFFFB69A, 0x1388, 0x60E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_2B5D)
    Sleep(500)

    def lambda_2B7D():
        OP_8E(0x14, 0xFFFFB69A, 0x1388, 0x60E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_2B7D)
    WaitChrThread(0x14, 0x2)
    SetChrChipByIndex(0x14, 4)
    SetChrSubChip(0x14, 0)

    def lambda_2BA7():
        OP_8C(0x14, 180, 100)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_2BA7)

    def lambda_2BB5():
        OP_8C(0x12, 270, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2BB5)
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
        "#311F啾！\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05尤莉亚从基库的脚上拿起了一张纸条。\x02",
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
            "#178F#5P……艾丝蒂尔他们已经\x01",
            "平安到达了龙所在的岩山。\x02\x03",

            "接下来他们要穿过岩山内部，\x01",
            "前往龙的所在之处。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x13,
        "#160F#6P是吗……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x13, 270, 400)
    Sleep(500)

    ChrTalk(    #6
        0x13,
        (
            "#163F#5P……通告全舰艇！\x02\x03",

            "装填好穿甲弹之后，\x01",
            "在指定位置待命！\x02\x03",

            "#162F万一龙逃了出来，\x01",
            "也绝不能让它突破包围！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #7
        0x12,
        "#177F#5P是，长官！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C1600   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_25_285E end

    def Function_26_2DC8(): pass

    label("Function_26_2DC8")


    def lambda_2DCE():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2DCE)
    Sleep(500)

    def lambda_2DEE():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2DEE)
    Sleep(500)

    def lambda_2E0E():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0x0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E0E)
    Sleep(500)

    def lambda_2E2E():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E2E)
    Sleep(500)

    def lambda_2E4E():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E4E)
    Sleep(500)

    def lambda_2E6E():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0x0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E6E)
    Return()

    # Function_26_2DC8 end

    def Function_27_2E84(): pass

    label("Function_27_2E84")

    EventBegin(0x0)
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

    def lambda_314C():
        OP_91(0xFE, 0xFFFB6C20, 0x0, 0x0, 0x7D00, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_314C)

    def lambda_3167():
        OP_91(0xFE, 0xFFFB6C20, 0x0, 0x0, 0x7D00, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3167)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(5000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10FC)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_27_2E84 end

    def Function_28_31A8(): pass

    label("Function_28_31A8")

    EventBegin(0x0)
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

    def lambda_3280():
        OP_6D(-95610, -10000, -97790, 5000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_3280)

    def lambda_3298():
        OP_6B(2750, 5000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3298)

    def lambda_32A8():
        OP_8F(0xFE, 0xFFFE507A, 0xFFFEC780, 0xFFFE9AD0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_32A8)
    Sleep(1000)
    SetMessageWindowPos(350, 60, -1, -1)
    SetChrName("乔丝特")

    AnonymousTalk(    #8 op#5
        "\x07\x00#210F不是吧～～～～！\x05\x02",
    )

    Sleep(1500)
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(80, 60, -1, -1)
    SetChrName("多伦")

    AnonymousTalk(    #9 op#5
        "#190F喔喔喔喔喔！\x05\x02",
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
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T2100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_28_31A8 end

    def Function_29_3376(): pass

    label("Function_29_3376")

    EventBegin(0x0)
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

    def lambda_3430():
        OP_6D(-53240, -10000, -30460, 3000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_3430)
    OP_43(0x0, 0x1, 0x0, 0x1E)
    OP_43(0xA, 0x0, 0x0, 0x1F)

    def lambda_3456():
        OP_D1(254, 90000, 270000, -20000, 3000)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_3456)
    OP_0D()
    SetMessageWindowPos(350, 60, -1, -1)
    SetChrName("乔丝特")

    AnonymousTalk(    #10 op#5
        "\x07\x00#216F#3S不是吧～～～～！\x05\x02",
    )

    Sleep(2500)
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(120, 260, -1, -1)
    SetChrName("多伦")

    AnonymousTalk(    #11 op#5
        "#192F#3S啊啊啊啊啊！\x05\x02",
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
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T2100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_29_3376 end

    def Function_30_354A(): pass

    label("Function_30_354A")

    OP_7C(0x320, 0xC8, 0x7D0, 0x3E8)
    Sleep(1000)
    OP_7C(0x258, 0xA0, 0x5DC, 0x3E8)
    Sleep(1000)
    OP_7C(0x190, 0x78, 0x3E8, 0x3E8)
    Return()

    # Function_30_354A end

    def Function_31_3588(): pass

    label("Function_31_3588")


    def lambda_358E():
        OP_8F(0xFE, 0xFFFEA070, 0xFFFE7960, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_358E)
    Sleep(400)

    def lambda_35AE():
        OP_8F(0xFE, 0xFFFEA070, 0xFFFE7960, 0x0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_35AE)
    Sleep(300)

    def lambda_35CE():
        OP_8F(0xFE, 0xFFFEA070, 0xFFFE7960, 0x0, 0x7D00, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_35CE)
    Sleep(200)

    def lambda_35EE():
        OP_8F(0xFE, 0xFFFEA070, 0xFFFE7960, 0x0, 0xB3B0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_35EE)
    Sleep(100)

    def lambda_360E():
        OP_8F(0xFE, 0xFFFEA070, 0xFFFE7960, 0x0, 0xF230, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_360E)
    Return()

    # Function_31_3588 end

    def Function_32_3624(): pass

    label("Function_32_3624")

    EventBegin(0x0)
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

    def lambda_3750():
        OP_6D(9890, -10000, 26390, 7000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_3750)

    def lambda_3768():
        OP_67(0, 3280, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3768)

    def lambda_3780():
        OP_6C(37000, 7000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_3780)

    def lambda_3790():
        OP_6B(12900, 7000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_3790)

    def lambda_37A0():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_37A0)
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

    def lambda_380A():
        OP_6D(-209890, 1000, 280, 3000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_380A)

    def lambda_3822():
        OP_67(0, 720, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3822)

    def lambda_383A():
        OP_6C(277000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_383A)

    def lambda_384A():
        OP_D1(254, 0, 270000, -20000, 5000)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_384A)

    def lambda_3864():
        OP_8F(0xFE, 0xFFF85EE0, 0x0, 0x4E20, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3864)
    Sleep(100)

    def lambda_3884():
        OP_8F(0xFE, 0xFFF85EE0, 0x0, 0x4E20, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3884)
    Sleep(100)

    def lambda_38A4():
        OP_8F(0xFE, 0xFFF85EE0, 0x0, 0x4E20, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_38A4)
    Sleep(100)

    def lambda_38C4():
        OP_8F(0xFE, 0xFFF85EE0, 0x0, 0x4E20, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_38C4)
    Sleep(100)

    def lambda_38E4():
        OP_8F(0xFE, 0xFFF85EE0, 0x0, 0x4E20, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_38E4)
    Sleep(100)

    def lambda_3904():
        OP_8F(0xFE, 0xFFF85EE0, 0x0, 0x4E20, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3904)
    Sleep(100)

    def lambda_3924():
        OP_8F(0xFE, 0xFFF85EE0, 0x0, 0x4E20, 0xEA60, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3924)
    Sleep(100)

    def lambda_3944():
        OP_8F(0xFE, 0xFFF85EE0, 0x0, 0x4E20, 0x11170, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3944)
    Sleep(100)

    def lambda_3964():
        OP_8F(0xFE, 0xFFF85EE0, 0x0, 0x4E20, 0x13880, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3964)
    Sleep(100)

    def lambda_3984():
        OP_8F(0xFE, 0xFFF85EE0, 0x0, 0x4E20, 0x15F90, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3984)
    Sleep(100)

    def lambda_39A4():
        OP_8F(0xFE, 0xFFF85EE0, 0x0, 0x4E20, 0x186A0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_39A4)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10FF)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_32_3624 end

    SaveToFile()

Try(main)
