from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4100   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Aina',                                 # 9
        'Mover',                                # 10
        'Mover',                                # 11
        'Gaspard',                              # 12
        'Berden',                               # 13
        'Latanya',                              # 14
        'Tran',                                 # 15
        'Phoebe',                               # 16
        'Nana',                                 # 17
        'Uran',                                 # 18
        'Nonna',                                # 19
        'Dick',                                 # 20
        'Raleigh',                              # 21
        'Troy',                                 # 22
        'Percy',                                # 23
        'Ilene',                                # 24
        'Grancel - North Block',                # 25
        'Royal Avenue',                         # 26
        'Grancel - East Block',                 # 27
        'Grancel - West Block',                 # 28
        'Man in Black',                         # 29
        'Man in Black',                         # 30
        'Man in Black',                         # 31
        'Man in Black',                         # 32
        'Box',                                  # 33
        'Target Camera',                        # 34
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
        'ED6_DT07/CH02710 ._CH',             # 00
        'ED6_DT07/CH01450 ._CH',             # 01
        'ED6_DT07/CH01270 ._CH',             # 02
        'ED6_DT07/CH01200 ._CH',             # 03
        'ED6_DT07/CH01210 ._CH',             # 04
        'ED6_DT07/CH01100 ._CH',             # 05
        'ED6_DT07/CH02730 ._CH',             # 06
        'ED6_DT07/CH02740 ._CH',             # 07
        'ED6_DT07/CH01140 ._CH',             # 08
        'ED6_DT07/CH01050 ._CH',             # 09
        'ED6_DT07/CH01160 ._CH',             # 0A
        'ED6_DT07/CH01470 ._CH',             # 0B
        'ED6_DT07/CH01060 ._CH',             # 0C
        'ED6_DT07/CH01640 ._CH',             # 0D
        'ED6_DT07/CH01460 ._CH',             # 0E
        'ED6_DT07/CH01180 ._CH',             # 0F
        'ED6_DT27/CH03460 ._CH',             # 10
    )

    AddCharChipPat(
        'ED6_DT07/CH02710P._CP',             # 00
        'ED6_DT07/CH01450P._CP',             # 01
        'ED6_DT07/CH01270P._CP',             # 02
        'ED6_DT07/CH01200P._CP',             # 03
        'ED6_DT07/CH01210P._CP',             # 04
        'ED6_DT07/CH01100P._CP',             # 05
        'ED6_DT07/CH02730P._CP',             # 06
        'ED6_DT07/CH02740P._CP',             # 07
        'ED6_DT07/CH01140P._CP',             # 08
        'ED6_DT07/CH01050P._CP',             # 09
        'ED6_DT07/CH01160P._CP',             # 0A
        'ED6_DT07/CH01470P._CP',             # 0B
        'ED6_DT07/CH01060P._CP',             # 0C
        'ED6_DT07/CH01640P._CP',             # 0D
        'ED6_DT07/CH01460P._CP',             # 0E
        'ED6_DT07/CH01180P._CP',             # 0F
        'ED6_DT27/CH03460P._CP',             # 10
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        X                   = 7930,
        Z                   = 250,
        Y                   = -26470,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 8400,
        Z                   = 250,
        Y                   = -30150,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = -3670,
        Z                   = 0,
        Y                   = -43050,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 5760,
        Z                   = 0,
        Y                   = -46060,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -2070,
        Z                   = 0,
        Y                   = -5120,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 3520,
        Z                   = 0,
        Y                   = 10640,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 1930,
        Z                   = 0,
        Y                   = -50840,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 690,
        Z                   = 0,
        Y                   = -50920,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 5870,
        Z                   = 0,
        Y                   = -38230,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 5550,
        Z                   = 0,
        Y                   = -54380,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -840,
        Z                   = 0,
        Y                   = -50090,
        Direction           = 90,
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
        X                   = 710,
        Z                   = 0,
        Y                   = -50090,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -90,
        Z                   = 0,
        Y                   = -51500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 92000,
        Z                   = 300,
        Y                   = 61850,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 7800,
        Z                   = 0,
        Y                   = -530,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xE4,
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


    DeclEvent(
        X                   = 0,
        Y                   = 0,
        Z                   = -65600,
        Range               = 2000,
        Unknown_10          = 0x1770,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 34,
    )

    DeclEvent(
        X                   = 9240,
        Y                   = 0,
        Z                   = -25000,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 36,
    )

    DeclEvent(
        X                   = -10280,
        Y                   = 0,
        Z                   = -11040,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 37,
    )

    DeclEvent(
        X                   = -14940,
        Y                   = 0,
        Z                   = -15750,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 37,
    )

    DeclEvent(
        X                   = -10290,
        Y                   = 0,
        Z                   = -30020,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 38,
    )

    DeclEvent(
        X                   = 9240,
        Y                   = 0,
        Z                   = -13010,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 39,
    )

    DeclEvent(
        X                   = 15900,
        Y                   = 0,
        Z                   = 6330,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 40,
    )


    ScpFunction(
        "Function_0_552",          # 00, 0
        "Function_1_711",          # 01, 1
        "Function_2_7CB",          # 02, 2
        "Function_3_948",          # 03, 3
        "Function_4_96C",          # 04, 4
        "Function_5_9C9",          # 05, 5
        "Function_6_A56",          # 06, 6
        "Function_7_AC5",          # 07, 7
        "Function_8_B34",          # 08, 8
        "Function_9_B58",          # 09, 9
        "Function_10_BAA",         # 0A, 10
        "Function_11_C13",         # 0B, 11
        "Function_12_EAB",         # 0C, 12
        "Function_13_12A4",        # 0D, 13
        "Function_14_15B4",        # 0E, 14
        "Function_15_1897",        # 0F, 15
        "Function_16_1A5F",        # 10, 16
        "Function_17_1A64",        # 11, 17
        "Function_18_1DD3",        # 12, 18
        "Function_19_1EA9",        # 13, 19
        "Function_20_2188",        # 14, 20
        "Function_21_2467",        # 15, 21
        "Function_22_25DB",        # 16, 22
        "Function_23_262A",        # 17, 23
        "Function_24_26F6",        # 18, 24
        "Function_25_273C",        # 19, 25
        "Function_26_2EF1",        # 1A, 26
        "Function_27_3450",        # 1B, 27
        "Function_28_36AD",        # 1C, 28
        "Function_29_36F5",        # 1D, 29
        "Function_30_373D",        # 1E, 30
        "Function_31_3785",        # 1F, 31
        "Function_32_37CD",        # 20, 32
        "Function_33_41EE",        # 21, 33
        "Function_34_457F",        # 22, 34
        "Function_35_496C",        # 23, 35
        "Function_36_49AE",        # 24, 36
        "Function_37_49B2",        # 25, 37
        "Function_38_49B6",        # 26, 38
        "Function_39_49BA",        # 27, 39
        "Function_40_49BE",        # 28, 40
    )


    def Function_0_552(): pass

    label("Function_0_552")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A9")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x17, 0x10)
    SetChrFlags(0x18, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_59F")
    Jump("loc_6A9")

    label("loc_59F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_624")
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    SetChrPos(0x24, 960, 0, -65800, 315)
    SetChrPos(0x25, -960, 0, -65800, 45)
    SetChrPos(0x26, 960, 0, -64099, 225)
    SetChrPos(0x27, -960, 0, -64099, 135)
    OP_43(0x24, 0x0, 0x0, 0x2)
    OP_43(0x25, 0x0, 0x0, 0x2)
    OP_43(0x26, 0x0, 0x0, 0x2)
    OP_43(0x27, 0x0, 0x0, 0x2)
    OP_43(0x24, 0x3, 0x0, 0xA)
    Jump("loc_6A9")

    label("loc_624")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_62E")
    Jump("loc_6A9")

    label("loc_62E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_6A9")
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    SetChrPos(0x24, 0, 0, -64099, 180)
    SetChrPos(0x25, -1000, 0, -65800, 45)
    SetChrPos(0x26, 1000, 0, -65800, 315)
    OP_43(0x24, 0x0, 0x0, 0x2)
    OP_43(0x25, 0x0, 0x0, 0x2)
    OP_43(0x26, 0x0, 0x0, 0x2)
    OP_43(0x24, 0x3, 0x0, 0x9)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, 7140, 250, -23020, 135)

    label("loc_6A9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_6D4")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 25)
    Jump("loc_6FD")

    label("loc_6D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_6EA")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    Event(0, 26)
    Jump("loc_6FD")

    label("loc_6EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 7)), scpexpr(EXPR_END)), "loc_6FD")
    OP_A3(0x2507)
    SetMapFlags(0x10000000)
    Event(0, 27)

    label("loc_6FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_710")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 21)

    label("loc_710")

    Return()

    # Function_0_552 end

    def Function_1_711(): pass

    label("Function_1_711")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFDBDE0, 0x23005B)
    OP_B1("T4100_n")
    OP_B2(0x0, 0x0, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AE")
    OP_71(0x411, 0x0)
    ExitThread()
    OP_71(0x412, 0x0)
    ExitThread()
    OP_71(0x413, 0x0)
    ExitThread()
    OP_71(0x414, 0x0)
    ExitThread()
    OP_71(0x417, 0x0)
    ExitThread()
    OP_71(0x418, 0x0)
    ExitThread()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_76B")
    Jump("loc_7AE")

    label("loc_76B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_77F")
    OP_1B(0x9, 0x0, 0x21)
    OP_B2(0x1, 0x0, 0x80)
    Jump("loc_7AE")

    label("loc_77F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_789")
    Jump("loc_7AE")

    label("loc_789")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_7AE")
    OP_1B(0xB, 0x0, 0x1C)
    OP_1B(0xC, 0x0, 0x1D)
    OP_1B(0xD, 0x0, 0x1E)
    OP_1B(0xE, 0x0, 0x1F)
    OP_1B(0x9, 0x0, 0x21)
    OP_B2(0x1, 0x0, 0x80)

    label("loc_7AE")

    SoundDistance(0x1CB, 0x32, 0x0, 0xFFFF4BCE, 0x7D0, 0x3A98, 0x64, 0x0)
    Return()

    # Function_1_711 end

    def Function_2_7CB(): pass

    label("Function_2_7CB")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F0")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_932")

    label("loc_7F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_809")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_932")

    label("loc_809")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_822")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_932")

    label("loc_822")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83B")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_932")

    label("loc_83B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_854")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_932")

    label("loc_854")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86D")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_932")

    label("loc_86D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_886")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_932")

    label("loc_886")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89F")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_932")

    label("loc_89F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B8")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_932")

    label("loc_8B8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D1")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_932")

    label("loc_8D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8EA")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_932")

    label("loc_8EA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_903")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_932")

    label("loc_903")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_91C")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_932")

    label("loc_91C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_932")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_932")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_947")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_932")

    label("loc_947")

    Return()

    # Function_2_7CB end

    def Function_3_948(): pass

    label("Function_3_948")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_96B")
    OP_8D(0xFE, 3700, -42040, 10110, -50100, 2000)
    Jump("Function_3_948")

    label("loc_96B")

    Return()

    # Function_3_948 end

    def Function_4_96C(): pass

    label("Function_4_96C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9C8")
    OP_8E(0xFE, 0xFFFFF7EA, 0x0, 0xFFFF6E24, 0x8FC, 0x0)
    OP_8E(0xFE, 0x9CE, 0x0, 0xFFFF6E24, 0x8FC, 0x0)
    OP_8E(0xFE, 0x9CE, 0x0, 0x2166, 0x8FC, 0x0)
    OP_8E(0xFE, 0xFFFFF7EA, 0x0, 0x2166, 0x8FC, 0x0)
    Jump("Function_4_96C")

    label("loc_9C8")

    Return()

    # Function_4_96C end

    def Function_5_9C9(): pass

    label("Function_5_9C9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A55")
    OP_8E(0xFE, 0xDC0, 0x0, 0xFFFF6532, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(2000)
    OP_8C(0xFE, 225, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFF29A, 0x0, 0xFFFF6532, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(2000)
    OP_8C(0xFE, 270, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFF29A, 0x0, 0x2990, 0x7D0, 0x0)
    OP_8E(0xFE, 0xDC0, 0x0, 0x2990, 0x7D0, 0x0)
    Jump("Function_5_9C9")

    label("loc_A55")

    Return()

    # Function_5_9C9 end

    def Function_6_A56(): pass

    label("Function_6_A56")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AC4")
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
    Jump("Function_6_A56")

    label("loc_AC4")

    Return()

    # Function_6_A56 end

    def Function_7_AC5(): pass

    label("Function_7_AC5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B33")
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
    Jump("Function_7_AC5")

    label("loc_B33")

    Return()

    # Function_7_AC5 end

    def Function_8_B34(): pass

    label("Function_8_B34")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B57")
    OP_8D(0xFE, -9540, -8220, -7490, -4270, 2000)
    Jump("Function_8_B34")

    label("loc_B57")

    Return()

    # Function_8_B34 end

    def Function_9_B58(): pass

    label("Function_9_B58")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BA9")
    OP_62(0x24, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_62(0x25, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_62(0x26, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jump("Function_9_B58")

    label("loc_BA9")

    Return()

    # Function_9_B58 end

    def Function_10_BAA(): pass

    label("Function_10_BAA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C12")
    OP_62(0x24, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_62(0x26, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_62(0x25, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_62(0x27, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jump("Function_10_BAA")

    label("loc_C12")

    Return()

    # Function_10_BAA end

    def Function_11_C13(): pass

    label("Function_11_C13")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_C20")
    Jump("loc_EA7")

    label("loc_C20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_D5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_CCF")
    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(    #0
        0xFE,
        "Hmm... This is the south block...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "If I follow this road upwards, I should reach\x01",
            "the north block, then eventually the castle...\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 135, 0)
    Jump("loc_D5B")

    label("loc_CCF")


    ChrTalk(    #2
        0xFE,
        (
            "Oh, before I start looking for a job, I need to\x01",
            "go and register that I've moved at the castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "THEN the job hunting can begin!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_D5B")

    Jump("loc_EA7")

    label("loc_D5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_D68")
    Jump("loc_EA7")

    label("loc_D68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_EA7")
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_E06")

    ChrTalk(    #4
        0xFE,
        (
            "I've just arrived here from the countryside\x01",
            "in hopes of finding work here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "Time to get searching! Then time to get working!\x02",
    )

    CloseMessageWindow()
    Jump("loc_EA0")

    label("loc_E06")


    ChrTalk(    #6
        0xFE,
        (
            "I've just arrived here from the countryside,\x01",
            "and woooooow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "The capital sure is HUGE!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "I feel like I'm going to get lost at any minute!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_EA0")

    OP_8C(0xFE, 135, 0)

    label("loc_EA7")

    TalkEnd(0xFE)
    Return()

    # Function_11_C13 end

    def Function_12_EAB(): pass

    label("Function_12_EAB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_EB8")
    Jump("loc_12A0")

    label("loc_EB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_10FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_FD6")

    ChrTalk(    #9
        0xFE,
        (
            "The north block is full of upmarket mansions,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "They're not as large as some of the houses you\x01",
            "find in the suburbs, of course, but they're all\x01",
            "high-class, beautiful buildings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "Pretty much everyone in the city either lives in\x01",
            "one or wishes they could.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10FB")

    label("loc_FD6")


    ChrTalk(    #12
        0xFE,
        "This city really is massive, isn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "The south block is large enough, but then there's \x01",
            "the east block with the department store and \x01",
            "arena, the west with the cathedral and port...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "The north has Liberl's largest hotel, too, and\x01",
            "then there's the access to Grancel Castle...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_10FB")

    Jump("loc_12A0")

    label("loc_10FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_1108")
    Jump("loc_12A0")

    label("loc_1108")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_12A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_11E7")

    ChrTalk(    #15
        0xFE,
        (
            "I'm guessing she was meant to take over the\x01",
            "place all along, though, given that it was named\x01",
            "after her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "They say she's just as capable as her father!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        "That kind of stuff must run in families.\x02",
    )

    CloseMessageWindow()
    Jump("loc_12A0")

    label("loc_11E7")


    ChrTalk(    #18
        0xFE,
        (
            "Did you know the department store changed\x01",
            "owners recently?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "The previous owner's daughter has taken over\x01",
            "the reins now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "They say she's plenty capable for her age, too!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_12A0")

    TalkEnd(0xFE)
    Return()

    # Function_12_EAB end

    def Function_13_12A4(): pass

    label("Function_13_12A4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_12B1")
    Jump("loc_15B0")

    label("loc_12B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_143C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1328")

    ChrTalk(    #21
        0xFE,
        (
            "I can't even remember what kind of fish it was\x01",
            "now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        "I think it began with a...'g'? Maybe?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1439")

    label("loc_1328")


    ChrTalk(    #23
        0xFE,
        (
            "I was talking to someone carrying boxes over\x01",
            "there just before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "They said they're from some kind of guild?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "Either way, they said the Imperial ambassador's\x01",
            "face resembled some kind of fish...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "I THINK it was meant to be a compliment...\x01",
            "Somehow. Maybe.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1439")

    Jump("loc_15B0")

    label("loc_143C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_1446")
    Jump("loc_15B0")

    label("loc_1446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_15B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_14ED")

    ChrTalk(    #27
        0xFE,
        (
            "I spotted the Erebonian ambassador in the city a\x01",
            "while ago. He looked grumpy the whole time, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "I wonder if all Erebonians are like that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_15B0")

    label("loc_14ED")


    ChrTalk(    #29
        0xFE,
        (
            "I spotted the Erebonian ambassador in the city\x01",
            "a while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "After all that's happened between us and the\x01",
            "Erebonians, I wasn't quite sure how to react\x01",
            "when I saw him, to be honest...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_15B0")

    TalkEnd(0xFE)
    Return()

    # Function_13_12A4 end

    def Function_14_15B4(): pass

    label("Function_14_15B4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_15C1")
    Jump("loc_1893")

    label("loc_15C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_1759")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1692")

    ChrTalk(    #31
        0xFE,
        (
            "According to the Liberl News, the famous \x01",
            "Saul Holden has passed away...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "He was the pride of my generation, too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "News like this just serves to make me feel that\x01",
            "much older...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1756")

    label("loc_1692")


    ChrTalk(    #34
        0xFE,
        (
            "I was quite stunned when I read the Liberl News\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "To think that the famous Saul Holden would pass\x01",
            "away so suddenly...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "The news made me feel rather old myself,\x01",
            "to be honest.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_1756")

    Jump("loc_1893")

    label("loc_1759")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_1763")
    Jump("loc_1893")

    label("loc_1763")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_1893")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_181B")

    ChrTalk(    #37
        0xFE,
        (
            "The Liberl News Service has their office in the\x01",
            "west block of the city, if you didn't know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "The newspaper they publish is pretty well known\x01",
            "here in Grancel.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1893")

    label("loc_181B")


    ChrTalk(    #39
        0xFE,
        (
            "Oh, today is the day the latest Liberl News comes\x01",
            "out, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "I'd best go and purchase a copy later on.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_1893")

    TalkEnd(0xFE)
    Return()

    # Function_14_15B4 end

    def Function_15_1897(): pass

    label("Function_15_1897")

    TalkBegin(0xFE)
    OP_4A(0x17, 255)
    OP_4A(0x18, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_18AC")
    Jump("loc_1A53")

    label("loc_18AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_1937")

    ChrTalk(    #41
        0x18,
        "So, liiike...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x18,
        (
            "...don't you feel like you wanna go take\x01",
            "a look at where she works?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x17,
        "Yeah, kinda.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x17,
        "Wanna go now?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A53")

    label("loc_1937")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_1941")
    Jump("loc_1A53")

    label("loc_1941")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_1A53")

    ChrTalk(    #45
        0x17,
        (
            "My sis works in the department store over\x01",
            "in the east block, y'know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x17,
        "What's it called? Edel or some junk?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x17,
        (
            "It's all suuuper fancy. I can't even bring\x01",
            "myself to get close.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x18,
        "Oh, whoa! Can't believe she can do that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x18,
        "What if your parents find out?\x02",
    )

    CloseMessageWindow()

    label("loc_1A53")

    OP_4B(0x17, 255)
    OP_4B(0x18, 255)
    TalkEnd(0xFE)
    Return()

    # Function_15_1897 end

    def Function_16_1A5F(): pass

    label("Function_16_1A5F")

    Call(0, 15)
    Return()

    # Function_16_1A5F end

    def Function_17_1A64(): pass

    label("Function_17_1A64")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_1A71")
    Jump("loc_1DCF")

    label("loc_1A71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_1CBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_1B9E")

    ChrTalk(    #50
        0xFE,
        (
            "Maybe running out was my own fault for getting\x01",
            "all excited at the prospect of getting to take a\x01",
            "ride on an airship and using them over and over...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "Still, one of the things Liberl's most famous for\x01",
            "is the Liberl Orbalship Corporation! How could\x01",
            "anyone resist the temptation?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CB8")

    label("loc_1B9E")


    ChrTalk(    #52
        0xFE,
        (
            "I actually graduated from an arts school in \x01",
            "Calvard, then I left on a journey around the\x01",
            "continent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "I thought it would be a great way to broaden\x01",
            "my horizons...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "Unfortunately, I ended up running out of mira\x01",
            "part way through my journey, so now I'm stuck\x01",
            "in Liberl.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_1CB8")

    Jump("loc_1DCF")

    label("loc_1CBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_1CC5")
    Jump("loc_1DCF")

    label("loc_1CC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_1DCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_1D5D")

    ChrTalk(    #55
        0xFE,
        "Don't hold back! Come over and take a look!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "It'd be great if you could buy some, too!\x01",
            "Just think of it as helping a guy out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DCF")

    label("loc_1D5D")


    ChrTalk(    #57
        0xFE,
        "Hey there! Up for some delicious candy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "We've got plenty of varieties to cater to\x01",
            "everyone's tastes!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_1DCF")

    TalkEnd(0xFE)
    Return()

    # Function_17_1A64 end

    def Function_18_1DD3(): pass

    label("Function_18_1DD3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_1DE0")
    Jump("loc_1EA5")

    label("loc_1DE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_1DEA")
    Jump("loc_1EA5")

    label("loc_1DEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_1DF4")
    Jump("loc_1EA5")

    label("loc_1DF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_1EA5")
    OP_8C(0x1E, 135, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_1E5A")

    ChrTalk(    #59
        0xFE,
        "This is the Fisherman's Guild, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        "I wonder if they'd let me join?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EA5")

    label("loc_1E5A")


    ChrTalk(    #61
        0xFE,
        "Th-This is the Fisherman's Guild, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "I wonder how you join.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_1EA5")

    TalkEnd(0xFE)
    Return()

    # Function_18_1DD3 end

    def Function_19_1EA9(): pass

    label("Function_19_1EA9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_1EB6")
    Jump("loc_2184")

    label("loc_1EB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_1F77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_1F20")

    ChrTalk(    #63
        0xFE,
        (
            "Why is this one box so much heavier\x01",
            "than the others?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        "Just to cause us trouble?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F74")

    label("loc_1F20")

    OP_8C(0xFE, 180, 0)

    ChrTalk(    #65
        0xFE,
        "Heave, ho!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "M-Maaan... This box is heavy...\x01",
            "What's even in this?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_1F74")

    Jump("loc_2184")

    label("loc_1F77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_1F81")
    Jump("loc_2184")

    label("loc_1F81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_2184")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_2087")

    ChrTalk(    #67
        0xFE,
        "Carrying these things is such a pain in the ass.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "Maybe we could put in a request to the guild to\x01",
            "get someone to do this, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x103,
        (
            "#1645FOr maybe you could, you know, actually do your\x01",
            "jobs?\x02\x03",

            "#1645FStop slacking. It's painful to watch.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2184")

    label("loc_2087")


    ChrTalk(    #70
        0xFE,
        "Hey there again, Miss Bracer.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "Decided to come and give us some\x01",
            "extra muscle after all? Thanks!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x103,
        (
            "#1646FMy job was just unloading the goods,\x01",
            "which I've already finished.\x02\x03",

            "My work here is done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        "Aww... No need to be that cold with us.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_2184")

    TalkEnd(0xFE)
    Return()

    # Function_19_1EA9 end

    def Function_20_2188(): pass

    label("Function_20_2188")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_2195")
    Jump("loc_2463")

    label("loc_2195")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_230A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_221B")

    ChrTalk(    #74
        0xFE,
        "We're kinda short on manpower right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "Sure you wouldn't be interested in joining?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x103,
        "#1646FVERY sure.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2307")

    label("loc_221B")


    ChrTalk(    #77
        0xFE,
        (
            "If you ever feel like a change in careers,\x01",
            "we'll be happy to have you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "We're real short on manpower right now,\x01",
            "you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x103,
        (
            "#1646FGuess what? So are we.\x02\x03",

            "I'm not going to feel like switching\x01",
            "careers any time soon, either.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_2307")

    Jump("loc_2463")

    label("loc_230A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_2314")
    Jump("loc_2463")

    label("loc_2314")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_2463")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_23E9")

    ChrTalk(    #80
        0xFE,
        "Hey! If it ain't that young bracer!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "Thinkin' about giving this sack of bones\x01",
            "over there a pep talk? He could do with\x01",
            "half the guts you've got.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x103,
        "#1642FHow about you do that yourself?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2463")

    label("loc_23E9")


    ChrTalk(    #83
        0xFE,
        "Hey! If it ain't that young bracer!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        "You've got guts, young lady. I like that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x103,
        "#1640F...Thanks, I guess?\x02",
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_2463")

    TalkEnd(0xFE)
    Return()

    # Function_20_2188 end

    def Function_21_2467(): pass

    label("Function_21_2467")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x109, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -5720, 0, -36280, 270)
    OP_43(0x13, 0x0, 0x0, 0x2)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 5760, 0, -46060, 270)
    OP_43(0x14, 0x0, 0x0, 0x3)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -2070, 0, -5120, 180)
    OP_43(0x15, 0x0, 0x0, 0x4)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 3520, 0, 10640, 180)
    OP_43(0x16, 0x0, 0x0, 0x5)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    OP_43(0x1E, 0x0, 0x0, 0x17)
    OP_43(0x1F, 0x0, 0x0, 0x18)
    OP_6D(0, -3750, -42620, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3590, 0)
    OP_6C(0, 0)
    OP_6E(590, 0)

    def lambda_2551():
        OP_6D(0, -5750, 630, 9000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2551)

    def lambda_2569():
        OP_67(0, 10940, -10000, 9000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2569)

    def lambda_2581():
        OP_6B(3500, 9000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2581)

    def lambda_2591():
        OP_6C(0, 9000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2591)

    def lambda_25A1():
        OP_6E(590, 9000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_25A1)
    OP_43(0x1B, 0x0, 0x0, 0x16)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(6000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T4102   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_21_2467 end

    def Function_22_25DB(): pass

    label("Function_22_25DB")

    Sleep(500)
    OP_62(0x1B, 0x0, 1600, 0x26, 0x27, 0xC8, 0x0)
    Sleep(1000)
    OP_63(0x1B)
    OP_62(0x1C, 0x0, 1600, 0x18, 0x1B, 0xC8, 0x2)
    OP_62(0x1D, 0x0, 1600, 0x0, 0x1, 0xC8, 0x0)
    Sleep(2000)
    OP_63(0x1C)
    OP_63(0x1D)
    Return()

    # Function_22_25DB end

    def Function_23_262A(): pass

    label("Function_23_262A")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 11280, 750, -25090, 270)
    OP_72(0x1001, 0x0)
    ExitThread()
    OP_6F(0x6, 0)
    OP_70(0x6, 0x3B)
    OP_23(0x6)
    OP_73(0x6)
    OP_8E(0xFE, 0x1FC2, 0xFA, 0xFFFF9F0C, 0x7D0, 0x0)
    OP_6F(0x6, 59)
    OP_70(0x6, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0x2026, 0xFA, 0xFFFFCD9C, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    OP_8E(0xFE, 0x256C, 0x1F4, 0xFFFFCD88, 0x7D0, 0x0)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x3B)
    OP_73(0x1)
    OP_8E(0xFE, 0x2CD8, 0x2EE, 0xFFFFCD9C, 0x7D0, 0x0)
    OP_6F(0x1, 59)
    OP_70(0x1, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    Return()

    # Function_23_262A end

    def Function_24_26F6(): pass

    label("Function_24_26F6")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -11710, 0, -19530, 90)
    OP_8E(0xFE, 0xFFFFF2B8, 0x0, 0xFFFFB3B6, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0xFFFFF2B8, 0x0, 0x1CB6, 0x7D0, 0x0)
    Return()

    # Function_24_26F6 end

    def Function_25_273C(): pass

    label("Function_25_273C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x103, -14500, 750, -2340, 90)
    OP_9F(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #86
        "\x07\x00#40WFive years ago...#20W\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_6D(1650, 5600, -50220, 0)
    OP_67(0, 6700, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(339000, 0)
    OP_6E(511, 0)
    OP_1D(0xE)
    FadeToBright(2000, 0)
    OP_C8(0x200, 0x46, "C_PLAC04._CH", 0x0, 0x7D0)

    def lambda_280E():
        OP_6D(-9650, 4500, -5440, 10000)
        ExitThread()

    QueueWorkItem(0x29, 0, lambda_280E)

    def lambda_2826():
        OP_67(0, 6200, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_2826)

    def lambda_283E():
        OP_6B(3100, 10000)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_283E)

    def lambda_284E():
        OP_6C(311000, 10000)
        ExitThread()

    QueueWorkItem(0x29, 3, lambda_284E)

    def lambda_285E():
        OP_6E(511, 10000)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_285E)
    WaitChrThread(0x29, 0x0)
    Sleep(500)
    Fade(1000)
    OP_6D(-14800, 250, -900, 0)
    OP_67(0, 6700, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(311000, 0)
    OP_6E(262, 0)
    OP_4A(0x15, 255)
    OP_4A(0x16, 255)
    Sleep(1000)
    OP_72(0x1004, 0x0)
    ExitThread()
    OP_70(0x4, 0x3B)
    OP_73(0x4)

    def lambda_28D7():
        OP_6D(-10820, 250, -1900, 2300)
        ExitThread()

    QueueWorkItem(0x29, 0, lambda_28D7)

    def lambda_28EF():
        OP_6C(322000, 2300)
        ExitThread()

    QueueWorkItem(0x29, 3, lambda_28EF)

    def lambda_28FF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_28FF)

    def lambda_2911():
        OP_8E(0xFE, 0xFFFFD828, 0xFA, 0xFFFFF574, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2911)
    Sleep(1500)
    OP_72(0x4, 0x8)
    ExitThread()
    OP_6F(0x4, 59)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0x4, 0x0)
    WaitChrThread(0x103, 0x1)
    Sleep(300)

    ChrTalk(    #87
        0x103,
        (
            "#1645F*sigh* Making deliveries in a city this\x01",
            "big sure isn't easy.\x02\x03",

            "Okay, where's next...?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 0, 400)
    Sleep(300)
    OP_22(0x12, 0x0, 0x5A)
    Sleep(500)

    ChrTalk(    #88
        0x103,
        (
            "#1643FErbe Royal Villa?! No way... I have to go all the way\x01",
            "THERE?!\x02\x03",

            "#1645FUgh... This is why I hate cities.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 140, 500)
    Sleep(300)

    def lambda_2A48():
        OP_8E(0xFE, 0xFFFFEACA, 0x0, 0xFFFFDDA0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2A48)
    WaitChrThread(0x103, 0x1)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)
    OP_A1(0x28, 0x1F)
    SetChrPos(0x28, 7400, 250, -25740, 0)
    SetChrPos(0x16, 5860, 0, -19380, 0)
    SetChrPos(0x15, -2000, 0, -22540, 0)

    def lambda_2AA8():
        OP_8E(0xFE, 0x16BC, 0x0, 0xFFFFE250, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2AA8)
    Sleep(100)

    def lambda_2AC8():
        OP_8E(0xFE, 0xFFFFF830, 0x0, 0xFFFFCC0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2AC8)
    Fade(1000)
    OP_6D(4480, 0, -13440, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x11, 7780, 250, -24540, 180)
    SetChrPos(0x12, 8480, 250, -25940, 270)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    OP_72(0x1006, 0x0)
    ExitThread()
    OP_6F(0x6, 59)
    SetChrPos(0x103, 4480, 0, -2140, 180)

    def lambda_2B6F():
        OP_8E(0xFE, 0x1180, 0x0, 0xFFFF955C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2B6F)
    Sleep(1000)

    def lambda_2B8F():
        OP_6D(5780, 0, -25540, 4000)
        ExitThread()

    QueueWorkItem(0x29, 0, lambda_2B8F)

    def lambda_2BA7():
        OP_67(0, 6860, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_2BA7)

    def lambda_2BBF():
        OP_6B(3080, 4000)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_2BBF)

    def lambda_2BCF():
        OP_6C(30000, 4000)
        ExitThread()

    QueueWorkItem(0x29, 3, lambda_2BCF)
    Sleep(3800)

    def lambda_2BE4():

        label("loc_2BE4")

        TurnDirection(0xFE, 0x103, 0)
        OP_48()
        Jump("loc_2BE4")

    QueueWorkItem2(0x11, 2, lambda_2BE4)

    def lambda_2BF5():

        label("loc_2BF5")

        TurnDirection(0xFE, 0x103, 0)
        OP_48()
        Jump("loc_2BF5")

    QueueWorkItem2(0x12, 2, lambda_2BF5)

    ChrTalk(    #89
        0x11,
        "Hey, bracer! Out on the job again?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 0x1)
    WaitChrThread(0x29, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 2840, 0, -37340, 0)

    def lambda_2C4E():
        OP_8E(0xFE, 0xB18, 0x0, 0xFFFFBFC8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2C4E)
    Sleep(300)

    def lambda_2C6E():
        OP_6D(7780, 0, -24520, 1500)
        ExitThread()

    QueueWorkItem(0x29, 0, lambda_2C6E)

    def lambda_2C86():
        OP_67(0, 5900, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_2C86)
    TurnDirection(0x103, 0x12, 500)
    WaitChrThread(0x29, 0x0)
    OP_44(0x16, 0xFF)
    OP_44(0x15, 0xFF)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x15, 0x80)
    Sleep(300)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #90
        0x11,
        (
            "Thanks again for the help! You're a lot stronger\x01",
            "than you look, young lady!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x12,
        (
            "#2PYou wouldn't have any interest in working for us,\x01",
            "would you? You'd be more than welcome!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x103,
        (
            "#1646FSorry, but I'm not interested.\x02\x03",

            "#1642FReally got to go, too. See ya!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 180, 500)
    Sleep(200)

    def lambda_2DD8():
        OP_8E(0xFE, 0x1180, 0x0, 0xFFFF6E4C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2DD8)
    Sleep(2000)
    WaitChrThread(0x10, 0x1)
    SetChrPos(0x10, 8460, 250, -13000, 90)
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    def lambda_2E20():
        OP_6D(11060, 750, -13000, 4000)
        ExitThread()

    QueueWorkItem(0x29, 0, lambda_2E20)

    def lambda_2E38():
        OP_67(0, 6760, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_2E38)

    def lambda_2E50():
        OP_6B(3500, 4000)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_2E50)

    def lambda_2E60():
        OP_6C(90000, 4000)
        ExitThread()

    QueueWorkItem(0x29, 3, lambda_2E60)
    WaitChrThread(0x29, 0x1)
    Sleep(1000)
    OP_63(0x10)
    Sleep(500)

    def lambda_2E82():
        OP_8E(0xFE, 0x2580, 0x1F4, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2E82)
    WaitChrThread(0x10, 0x1)
    Sleep(300)
    OP_22(0x71, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #93
        0x10,
        "Woman",
        "#1650FExcuse me...\x02",
    )

    CloseMessageWindow()

    def lambda_2ECF():
        OP_6B(3400, 3000)
        ExitThread()

    QueueWorkItem(0x29, 0, lambda_2ECF)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T4121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_25_273C end

    def Function_26_2EF1(): pass

    label("Function_26_2EF1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_41(0x2, 0x0, 0xFF)
    OP_31(0x2, 0x10, 0xA)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x2, 0x5, 0x0)
    OP_35(0x2, 0xFFFF)
    OP_34(0x2, 0xFFFF)
    OP_35(0x2, 0x0)
    OP_37(0x2, 0x7F, 0x0)
    OP_37(0x2, 0x7F, 0x0)
    OP_BB(0x2, 0x6, 0x0)
    OP_41(0x2, 0x44E, 0xFF)
    OP_41(0x2, 0x63F, 0xFF)
    OP_41(0x2, 0x7F, 0xFF)
    OP_3E(0x203, 3)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4A), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F5E")
    OP_3E(0x145, 1)
    OP_3E(0x203, 2)
    OP_3E(0x13E, 1)
    Jump("loc_2F79")

    label("loc_2F5E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4A), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F79")
    OP_3E(0x145, 1)
    OP_3E(0x203, 2)
    OP_3E(0x13E, 1)

    label("loc_2F79")

    SetChrPos(0x103, 11500, 750, -13000, 270)
    OP_9F(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10, 11500, 750, -13000, 270)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x40)
    OP_4A(0x15, 255)
    OP_4A(0x16, 255)
    OP_6D(8920, 500, -12780, 0)
    OP_67(0, 8540, -10000, 0)
    OP_6B(2760, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_72(0x1, 0x8)
    ExitThread()
    OP_22(0x6, 0x0, 0x64)
    OP_70(0x1, 0x3B)
    OP_73(0x1)

    def lambda_3025():
        OP_8E(0xFE, 0x1B30, 0xFA, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3025)

    def lambda_3040():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_3040)
    Sleep(2000)

    def lambda_3057():
        OP_8E(0xFE, 0x25E4, 0x1F4, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3057)

    def lambda_3072():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3072)
    WaitChrThread(0x10, 0x1)
    OP_8C(0x10, 90, 400)
    WaitChrThread(0x103, 0x1)
    OP_8C(0x103, 90, 400)
    Sleep(500)
    OP_6F(0x1, 59)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0x1, 0x0)
    OP_73(0x1)
    Sleep(500)

    ChrTalk(    #94
        0x103,
        (
            "#1645F(What is up with today? From delivery girl\x01",
            "to playing tour guide for some snooty silver\x01",
            "spoon. It just gets worse...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x10,
        (
            "#1653FI do apologize. I really am putting you out\x01",
            "with this request, aren't I?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 270, 400)
    Sleep(300)

    def lambda_319D():
        OP_8E(0xFE, 0x2134, 0xFA, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_319D)
    WaitChrThread(0x103, 0x1)
    Sleep(300)

    ChrTalk(    #96
        0x103,
        (
            "#1646F#2PLet's just get started.\x02\x03",

            "(Ugh. That aloof manner of talking she has\x01",
            "just makes me want to smash something...)\x02\x03",

            "#1642FSo? Where do you want to go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x10,
        (
            "#1654FHmm... Let's see...\x02\x03",

            "I suppose I should go and buy a few things in\x01",
            "the Edel Department Store just in case...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x103,
        "#1643F#2PIn case? In case of what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x10,
        "#1650FIt's in the east block of the city. Don't forget.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x103,
        (
            "#1648F#2PWhy WOULD I?\x02\x03",

            "(I can feel my blood pressure rising already.)\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8)
    AddParty(0x50, 0xFF, 0xFF)
    SetChrPos(0x151, 7180, 250, -13000, 90)
    OP_6F(0x1, 0)
    OP_71(0x1, 0x8)
    ExitThread()
    OP_4B(0x15, 255)
    OP_4B(0x16, 255)
    OP_A2(0x2F4A)
    OP_1B(0xB, 0x0, 0x1C)
    OP_1B(0xC, 0x0, 0x1D)
    OP_1B(0xD, 0x0, 0x1E)
    OP_1B(0xE, 0x0, 0x1F)
    OP_1B(0x9, 0x0, 0x21)
    OP_B2(0x1, 0x0, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    SetChrPos(0x24, 0, 0, -64099, 180)
    SetChrPos(0x25, -1000, 0, -65800, 45)
    SetChrPos(0x26, 1000, 0, -65800, 315)
    OP_43(0x24, 0x0, 0x0, 0x2)
    OP_43(0x25, 0x0, 0x0, 0x2)
    OP_43(0x26, 0x0, 0x0, 0x2)
    OP_43(0x24, 0x3, 0x0, 0x9)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, 7140, 250, -23020, 135)
    EventEnd(0x0)
    Return()

    # Function_26_2EF1 end

    def Function_27_3450(): pass

    label("Function_27_3450")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x103, 11500, 750, -13000, 270)
    OP_9F(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x151, 11500, 750, -13000, 270)
    OP_9F(0x151, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x151, 0x40)
    OP_4A(0x15, 255)
    OP_4A(0x16, 255)
    OP_6D(8920, 500, -12780, 0)
    OP_67(0, 8540, -10000, 0)
    OP_6B(2760, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_72(0x1, 0x8)
    ExitThread()
    OP_22(0x6, 0x0, 0x64)
    OP_70(0x1, 0x3B)
    OP_73(0x1)

    def lambda_3503():
        OP_8E(0xFE, 0x1BBC, 0xFA, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3503)

    def lambda_351E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_351E)
    Sleep(1500)

    def lambda_3535():
        OP_8E(0xFE, 0x2134, 0xFA, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3535)

    def lambda_3550():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_3550)
    Sleep(1000)
    OP_6F(0x1, 59)
    OP_70(0x1, 0x0)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x1)
    WaitChrThread(0x103, 0x1)
    WaitChrThread(0x151, 0x1)
    Sleep(300)

    ChrTalk(    #101
        0x103,
        (
            "#1646FOookay...\x02\x03",

            "#1641FLet's get this job out of the way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x151,
        (
            "\x07\x00#1650F#2PMiss Scherazard? Who was that you\x01",
            "were talking to?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(300)

    ChrTalk(    #103
        0x103,
        (
            "#1645FMind your own business.\x02\x03",

            "We're going to the hotel. You DID want\x01",
            "to go there, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x151,
        "#1650F#2PY-Yes. I do...\x02",
    )

    CloseMessageWindow()
    OP_4B(0x15, 255)
    OP_4B(0x16, 255)
    ClearChrFlags(0x151, 0x40)
    OP_6F(0x1, 0)
    OP_71(0x1, 0x8)
    ExitThread()
    EventEnd(0x0)
    Return()

    # Function_27_3450 end

    def Function_28_36AD(): pass

    label("Function_28_36AD")

    EventBegin(0x2)
    Call(0, 32)
    OP_59()
    Fade(1000)
    SetChrPos(0x103, -8800, 250, 13160, 180)
    SetChrPos(0x151, -8800, 250, 13160, 180)
    OP_6D(-8800, 250, 9000, 0)
    OP_0D()
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_28_36AD end

    def Function_29_36F5(): pass

    label("Function_29_36F5")

    EventBegin(0x2)
    Call(0, 32)
    OP_59()
    Fade(1000)
    SetChrPos(0x103, -3600, 0, 13160, 180)
    SetChrPos(0x151, -3600, 0, 13160, 180)
    OP_6D(-3600, 0, 9000, 0)
    OP_0D()
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_29_36F5 end

    def Function_30_373D(): pass

    label("Function_30_373D")

    EventBegin(0x2)
    Call(0, 32)
    OP_59()
    Fade(1000)
    SetChrPos(0x103, 8800, 250, 13160, 180)
    SetChrPos(0x151, 8800, 250, 13160, 180)
    OP_6D(8800, 250, 9000, 0)
    OP_0D()
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_30_373D end

    def Function_31_3785(): pass

    label("Function_31_3785")

    EventBegin(0x2)
    Call(0, 32)
    OP_59()
    Fade(1000)
    SetChrPos(0x103, 3600, 0, 13160, 180)
    SetChrPos(0x151, 3600, 0, 13160, 180)
    OP_6D(3600, 0, 9000, 0)
    OP_0D()
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_31_3785 end

    def Function_32_37CD(): pass

    label("Function_32_37CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_37D7")
    Jump("loc_41ED")

    label("loc_37D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_37E1")
    Jump("loc_41ED")

    label("loc_37E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_37EB")
    Jump("loc_41ED")

    label("loc_37EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_41ED")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3A63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_392D")
    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #105
        0x151,
        (
            "#1650F#6PThere's no point in going the long way 'round.\x02\x03",

            "#1651FWe need to turn at the guild and enter the east\x01",
            "block that way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x103,
        (
            "#1646F#6P...\x02\x03",

            "(For someone who claims it's their first\x01",
            "time in Grancel, this girl sure knows a lot\x01",
            "about the place.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A60")

    label("loc_392D")

    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #107
        0x151,
        (
            "#1653F#6PMiss Scherazard, you do know the department\x01",
            "store isn't this way, right?\x02\x03",

            "We need to turn at the guild and enter the east\x01",
            "block that way.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #108
        0x103,
        "#1642F#6PIt can still be reached this way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x151,
        (
            "#1654F#6P...Maybe so.\x02\x03",

            "#1651FBut it will take us longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x103,
        "#1646F#6P...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_3A60")

    Jump("loc_41ED")

    label("loc_3A63")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_GE), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3CF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3BC1")
    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #111
        0x151,
        (
            "#1650FWe might be able to reach the department\x01",
            "store this way, but it'll take us an unnecessarily\x01",
            "long time.\x02\x03",

            "#1651FWe need to turn at the guild and enter the east\x01",
            "block that way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x103,
        (
            "#1646F#4P...\x02\x03",

            "(For someone who claims it's their first\x01",
            "time in Grancel, this girl sure knows a lot\x01",
            "about the place.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CEE")

    label("loc_3BC1")

    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #113
        0x151,
        (
            "#1653FMiss Scherazard, you do know the department\x01",
            "store isn't this way, right?\x02\x03",

            "We need to turn at the guild and enter the east\x01",
            "block that way.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #114
        0x103,
        "#1642F#4PIt can still be reached this way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x151,
        (
            "#1654F...Maybe so.\x02\x03",

            "#1651FBut it will take us longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x103,
        "#1646F#4P...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_3CEE")

    Jump("loc_41ED")

    label("loc_3CF1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_GE), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3E4F")
    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #117
        0x151,
        (
            "#1650FWe might be able to reach the department\x01",
            "store this way, but it'll take us an unnecessarily\x01",
            "long time.\x02\x03",

            "#1651FWe need to turn at the guild and enter the east\x01",
            "block that way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x103,
        (
            "#1646F#3P...\x02\x03",

            "(For someone who claims it's their first\x01",
            "time in Grancel, this girl sure knows a lot\x01",
            "about the place.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F7C")

    label("loc_3E4F")

    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #119
        0x151,
        (
            "#1653FMiss Scherazard, you do know the department\x01",
            "store isn't this way, right?\x02\x03",

            "We need to turn at the guild and enter the east\x01",
            "block that way.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #120
        0x103,
        "#1642F#3PIt can still be reached this way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x151,
        (
            "#1654F...Maybe so.\x02\x03",

            "#1651FBut it will take us longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x103,
        "#1646F#3P...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_3F7C")

    Jump("loc_41ED")

    label("loc_3F7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_40C5")
    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #123
        0x151,
        (
            "#1650FWe might be able to reach the department\x01",
            "store this way, but it'll take us an unnecessarily\x01",
            "long time.\x02\x03",

            "#1651FWe need to turn at the guild and enter the east\x01",
            "block that way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x103,
        (
            "#1646F...\x02\x03",

            "(For someone who claims it's their first\x01",
            "time in Grancel, this girl sure knows a lot\x01",
            "about the place.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41ED")

    label("loc_40C5")

    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #125
        0x151,
        (
            "#1653FMiss Scherazard, you do know the department store \x01",
            "isn't this way, right?\x02\x03",

            "We need to turn at the guild and enter the east\x01",
            "block that way.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #126
        0x103,
        "#1642FIt can still be reached this way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x151,
        (
            "#1654F...Maybe so.\x02\x03",

            "#1651FBut it will take us longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x103,
        "#1646F...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_41ED")

    Return()

    # Function_32_37CD end

    def Function_33_41EE(): pass

    label("Function_33_41EE")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_41FA")
    Jump("loc_4563")

    label("loc_41FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_43DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4329")
    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #129
        0x151,
        (
            "#1656FThis isn't the right way, Miss Scherazard.\x02\x03",

            "#1650FWe need to walk back up the road and\x01",
            "take a left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x103,
        (
            "#1648F(Ugh. Her attitude is really starting to grate\x01",
            "on me now...)\x02\x03",

            "(Will punching her in the face disqualify me\x01",
            "from getting that letter of recommendation?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43D8")

    label("loc_4329")

    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #131
        0x151,
        (
            "#1653FThis isn't the right way, Miss Scherazard.\x02\x03",

            "#1650FThe hotel is in the north block.\x02\x03",

            "We need to walk back up the road and take\x01",
            "a left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x103,
        "#1642F...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_43D8")

    Jump("loc_4563")

    label("loc_43DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_43E5")
    Jump("loc_4563")

    label("loc_43E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_4563")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_445C")
    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #133
        0x151,
        (
            "#1651FMiss Scherazard, we're going in completely the\x01",
            "wrong direction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x103,
        "#1646F...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4563")

    label("loc_445C")

    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #135
        0x151,
        (
            "#1653FMiss Scherazard, this way leads to the west\x01",
            "block.\x02\x03",

            "We need to go to the east block...\x02\x03",

            "#1651FWhich means we're heading in completely\x01",
            "the wrong direction.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #136
        0x103,
        (
            "#1646FI-I know that... I just made a simple mistake,\x01",
            "that's all.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_4563")

    OP_90(0xEE, 0x5DC, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_33_41EE end

    def Function_34_457F(): pass

    label("Function_34_457F")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_458B")
    Jump("loc_4926")

    label("loc_458B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_4723")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_46A6")
    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #137
        0x151,
        (
            "#1653FWhere are you going, Miss Scherazard?\x02\x03",

            "This way leads out of the city, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x103,
        (
            "#1646F(I get angrier with every word that comes\x01",
            "out of her mouth.)\x02\x03",

            "#1647F(It's like she can't say ANYTHING without\x01",
            "sounding like she's ordering me around!)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4720")

    label("loc_46A6")

    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #139
        0x151,
        (
            "#1653FWhere are you going, Miss Scherazard?\x02\x03",

            "This way leads out of the city, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x103,
        "#1646F...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_4720")

    Jump("loc_4926")

    label("loc_4723")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_472D")
    Jump("loc_4926")

    label("loc_472D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_4926")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4816")
    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #141
        0x151,
        (
            "#1650FThe department store is in the east block of the\x01",
            "city. We need to travel back up the road and turn\x01",
            "right after the guild.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #142
        0x103,
        "#1642FI know that! You don't need to repeat yourself!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4926")

    label("loc_4816")

    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #143
        0x151,
        (
            "#1652FUmm... Miss Scherazard...?#1300W #20W \x01",
            "#1651FYou do know this way leads out of the city,\x01",
            "right?\x02\x03",

            "The department store is in the east block of the\x01",
            "city. We need to travel back up the road and turn\x01",
            "right after the guild.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x0, 0x151, 500)
    Sleep(200)

    ChrTalk(    #144
        0x103,
        "#1642FI-I know that!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_4926")

    OP_59()
    Fade(1000)
    SetChrPos(0x103, 0, 0, -58800, 0)
    SetChrPos(0x151, 0, 0, -58800, 0)
    OP_6D(0, 0, -58800, 0)
    Sleep(1000)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_34_457F end

    def Function_35_496C(): pass

    label("Function_35_496C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #145
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    SetMapFlags(0x2000000)
    Return()

    # Function_35_496C end

    def Function_36_49AE(): pass

    label("Function_36_49AE")

    SetPlaceName(0xB9)
    Return()

    # Function_36_49AE end

    def Function_37_49B2(): pass

    label("Function_37_49B2")

    SetPlaceName(0xB0)
    Return()

    # Function_37_49B2 end

    def Function_38_49B6(): pass

    label("Function_38_49B6")

    SetPlaceName(0xB2)
    Return()

    # Function_38_49B6 end

    def Function_39_49BA(): pass

    label("Function_39_49BA")

    SetPlaceName(0xAE)
    Return()

    # Function_39_49BA end

    def Function_40_49BE(): pass

    label("Function_40_49BE")

    SetPlaceName(0xB3)
    Return()

    # Function_40_49BE end

    SaveToFile()

Try(main)
