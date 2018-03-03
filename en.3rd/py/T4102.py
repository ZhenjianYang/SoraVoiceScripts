from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4102   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4102.x',
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
        'Pigeon',                               # 9
        'Pigeon',                               # 10
        'Pigeon',                               # 11
        'Pigeon',                               # 12
        'Pigeon',                               # 13
        'Pigeon',                               # 14
        'Pigeon',                               # 15
        'Nial',                                 # 16
        'Man in Black',                         # 17
        'Man in Black',                         # 18
        'Man in Black',                         # 19
        'Lt. Col. Cid',                         # 20
        'Ghost',                                # 21
        'Tourist',                              # 22
        'Tourist',                              # 23
        'Private Datten',                       # 24
        'Peter',                                # 25
        'Connor',                               # 26
        'Noticia',                              # 27
        'Sharnelle',                            # 28
        'Target Camera',                        # 29
        'Grancel - North Block',                # 30
        'Grancel - South Block',                # 31
        'Grancel - Wharf',                      # 32
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
        'ED6_DT07/CH01680 ._CH',             # 01
        'ED6_DT07/CH01690 ._CH',             # 02
        'ED6_DT07/CH01730 ._CH',             # 03
        'ED6_DT07/CH01731 ._CH',             # 04
        'ED6_DT07/CH01020 ._CH',             # 05
        'ED6_DT07/CH01053 ._CH',             # 06
        'ED6_DT07/CH01153 ._CH',             # 07
        'ED6_DT07/CH02060 ._CH',             # 08
        'ED6_DT27/CH03460 ._CH',             # 09
        'ED6_DT27/CH03590 ._CH',             # 0A
        'ED6_DT07/CH01020 ._CH',             # 0B
        'ED6_DT07/CH01053 ._CH',             # 0C
        'ED6_DT07/CH01153 ._CH',             # 0D
        'ED6_DT07/CH01640 ._CH',             # 0E
        'ED6_DT07/CH01680 ._CH',             # 0F
        'ED6_DT07/CH01140 ._CH',             # 10
        'ED6_DT07/CH01210 ._CH',             # 11
        'ED6_DT26/CH20686 ._CH',             # 12
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01680P._CP',             # 01
        'ED6_DT07/CH01690P._CP',             # 02
        'ED6_DT07/CH01730P._CP',             # 03
        'ED6_DT07/CH01731P._CP',             # 04
        'ED6_DT07/CH01020P._CP',             # 05
        'ED6_DT07/CH01053P._CP',             # 06
        'ED6_DT07/CH01153P._CP',             # 07
        'ED6_DT07/CH02060P._CP',             # 08
        'ED6_DT27/CH03460P._CP',             # 09
        'ED6_DT27/CH03590P._CP',             # 0A
        'ED6_DT07/CH01020P._CP',             # 0B
        'ED6_DT07/CH01053P._CP',             # 0C
        'ED6_DT07/CH01153P._CP',             # 0D
        'ED6_DT07/CH01640P._CP',             # 0E
        'ED6_DT07/CH01680P._CP',             # 0F
        'ED6_DT07/CH01140P._CP',             # 10
        'ED6_DT07/CH01210P._CP',             # 11
        'ED6_DT26/CH20686P._CP',             # 12
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -44500,
        Z                   = 250,
        Y                   = -19980,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -58590,
        Z                   = -3250,
        Y                   = -22150,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -58070,
        Z                   = -3250,
        Y                   = -23930,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -89010,
        Z                   = 250,
        Y                   = -1030,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -75890,
        Z                   = 0,
        Y                   = -5330,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -54960,
        Z                   = -3750,
        Y                   = -30670,
        Direction           = 270,
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
        X                   = -63160,
        Z                   = -3000,
        Y                   = -35170,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -40940,
        Z                   = 0,
        Y                   = -5120,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
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
        X                   = -39960,
        Z                   = 0,
        Y                   = 43920,
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
        X                   = -7520,
        Z                   = 300,
        Y                   = -20000,
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
        X                   = -117000,
        Z                   = 0,
        Y                   = -4090,
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
        X                   = -63040,
        Y                   = -3750,
        Z                   = -33480,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 48,
    )

    DeclEvent(
        X                   = -63390,
        Y                   = -3750,
        Z                   = -24940,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 49,
    )

    DeclEvent(
        X                   = -78840,
        Y                   = 1250,
        Z                   = 12430,
        Range               = 2000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 50,
    )


    DeclActor(
        TriggerX            = -72220,
        TriggerZ            = -3180,
        TriggerY            = -15630,
        TriggerRange        = 800,
        ActorX              = -72220,
        ActorZ              = -2000,
        ActorY              = -15630,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 46,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -76990,
        TriggerZ            = -3500,
        TriggerY            = -30450,
        TriggerRange        = 800,
        ActorX              = -76990,
        ActorZ              = -2500,
        ActorY              = -30450,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 47,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_4EA",          # 00, 0
        "Function_1_585",          # 01, 1
        "Function_2_601",          # 02, 2
        "Function_3_686",          # 03, 3
        "Function_4_713",          # 04, 4
        "Function_5_916",          # 05, 5
        "Function_6_93A",          # 06, 6
        "Function_7_997",          # 07, 7
        "Function_8_AAB",          # 08, 8
        "Function_9_CCA",          # 09, 9
        "Function_10_E45",         # 0A, 10
        "Function_11_10BE",        # 0B, 11
        "Function_12_11E5",        # 0C, 12
        "Function_13_120E",        # 0D, 13
        "Function_14_1291",        # 0E, 14
        "Function_15_1342",        # 0F, 15
        "Function_16_136D",        # 10, 16
        "Function_17_139D",        # 11, 17
        "Function_18_1414",        # 12, 18
        "Function_19_1492",        # 13, 19
        "Function_20_14F0",        # 14, 20
        "Function_21_1553",        # 15, 21
        "Function_22_15B1",        # 16, 22
        "Function_23_160F",        # 17, 23
        "Function_24_166D",        # 18, 24
        "Function_25_16CB",        # 19, 25
        "Function_26_1729",        # 1A, 26
        "Function_27_1779",        # 1B, 27
        "Function_28_17CF",        # 1C, 28
        "Function_29_182A",        # 1D, 29
        "Function_30_1885",        # 1E, 30
        "Function_31_18DB",        # 1F, 31
        "Function_32_18F1",        # 20, 32
        "Function_33_1B34",        # 21, 33
        "Function_34_1B94",        # 22, 34
        "Function_35_1BED",        # 23, 35
        "Function_36_33DC",        # 24, 36
        "Function_37_347D",        # 25, 37
        "Function_38_34CA",        # 26, 38
        "Function_39_350B",        # 27, 39
        "Function_40_3D61",        # 28, 40
        "Function_41_3DE0",        # 29, 41
        "Function_42_3FA2",        # 2A, 42
        "Function_43_41C4",        # 2B, 43
        "Function_44_433B",        # 2C, 44
        "Function_45_44B9",        # 2D, 45
        "Function_46_44E7",        # 2E, 46
        "Function_47_4554",        # 2F, 47
        "Function_48_4722",        # 30, 48
        "Function_49_4726",        # 31, 49
        "Function_50_472A",        # 32, 50
    )


    def Function_0_4EA(): pass

    label("Function_0_4EA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51D")
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x1F, -89010, 250, -1030, 189)
    OP_43(0x20, 0x0, 0x0, 0x5)

    label("loc_51D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_571")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 7)), scpexpr(EXPR_END)), "loc_53F")
    OP_A3(0x2507)
    SetMapFlags(0x10000000)
    Event(0, 39)
    Jump("loc_571")

    label("loc_53F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_555")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    Event(0, 35)
    Jump("loc_571")

    label("loc_555")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_571")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x29), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 32)

    label("loc_571")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_584")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 10)

    label("loc_584")

    Return()

    # Function_0_4EA end

    def Function_1_585(): pass

    label("Function_1_585")

    OP_16(0x2, 0xFA0, 0xFFFD2D58, 0xFFFE0048, 0x23005D)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B8")
    OP_B1("t4102_y")
    Jump("loc_5C1")

    label("loc_5B8")

    OP_B1("t4102_n")

    label("loc_5C1")

    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_600")
    OP_71(0x408, 0x0)
    ExitThread()
    OP_71(0x40F, 0x0)
    ExitThread()
    OP_72(0x411, 0x0)
    ExitThread()
    OP_72(0x100A, 0x0)
    ExitThread()
    OP_1B(0x0, 0x0, 0x29)
    OP_1B(0x2, 0x0, 0x2A)
    OP_1B(0xB, 0x0, 0x2C)
    OP_65(0x1, 0x1)

    label("loc_600")

    Return()

    # Function_1_585 end

    def Function_2_601(): pass

    label("Function_2_601")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_685")
    OP_8E(0xFE, 0xFFFF63CA, 0x0, 0xFFFFF416, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFF291E, 0x0, 0xFFFFF416, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFF259A, 0x0, 0xFFFFF416, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    Jump("Function_2_601")

    label("loc_685")

    Return()

    # Function_2_601 end

    def Function_3_686(): pass

    label("Function_3_686")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_712")
    OP_8E(0xFE, 0xFFFED716, 0x4E2, 0x1F5D, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFECB72, 0x4E2, 0x1F5D, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFEC014, 0x4E2, 0x1F5D, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFECB72, 0x4E2, 0x1F5D, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    Jump("Function_3_686")

    label("loc_712")

    Return()

    # Function_3_686 end

    def Function_4_713(): pass

    label("Function_4_713")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x40)
    OP_8D(0xFE, -74920, -1510, -82870, 5610, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_747")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_915")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8DE")
    OP_44(0xFE, 0x1)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7CE")

    def lambda_7B2():

        label("loc_7B2")

        OP_97(0xFE, 0xFFFECB7C, 0x3926, 0x57E40, 0x1B58, 0x1)
        OP_48()
        Jump("loc_7B2")

    QueueWorkItem2(0xFE, 1, lambda_7B2)
    Jump("loc_7ED")

    label("loc_7CE")


    def lambda_7D4():

        label("loc_7D4")

        OP_97(0xFE, 0xFFFECB7C, 0x3926, 0xFFFA81C0, 0x1B58, 0x1)
        OP_48()
        Jump("loc_7D4")

    QueueWorkItem2(0xFE, 1, lambda_7D4)

    label("loc_7ED")

    SetChrChipByIndex(0xFE, 3)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)

    label("loc_7FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_834")
    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2328), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_82C")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
    Jump("loc_834")

    label("loc_82C")

    Sleep(15)
    Jump("loc_7FC")

    label("loc_834")

    SetChrFlags(0xFE, 0x80)
    OP_44(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -78690, 0, -40, 74)

    label("loc_853")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8DB")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8D3")
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 4)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8D(0xFE, -74920, -1510, -82870, 5610, 0)
    Jump("loc_8DB")

    label("loc_8D3")

    Sleep(500)
    Jump("loc_853")

    label("loc_8DB")

    Jump("loc_912")

    label("loc_8DE")

    Sleep(100)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_912")

    def lambda_8FA():
        OP_8D(0xFE, -74920, -1510, -82870, 5610, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8FA)

    label("loc_912")

    Jump("loc_747")

    label("loc_915")

    Return()

    # Function_4_713 end

    def Function_5_916(): pass

    label("Function_5_916")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_939")
    OP_8D(0xFE, -83110, 1920, -74690, -5430, 3000)
    Jump("Function_5_916")

    label("loc_939")

    Return()

    # Function_5_916 end

    def Function_6_93A(): pass

    label("Function_6_93A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_996")
    OP_8E(0xFE, 0xFFFF6014, 0x0, 0xFFFF711C, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF2C52, 0xFFFFF15A, 0xFFFF727A, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF2C0C, 0x0, 0xFFFFEC82, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF6014, 0x0, 0xFFFFEC00, 0x9C4, 0x0)
    Jump("Function_6_93A")

    label("loc_996")

    Return()

    # Function_6_93A end

    def Function_7_997(): pass

    label("Function_7_997")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_A8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_A27")

    ChrTalk(    #0
        0xFE,
        "This way leads to Grancel Port.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "You're welcome to pay it a visit, but just be\x01",
            "careful not to fall into the water.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A89")

    label("loc_A27")


    ChrTalk(    #2
        0xFE,
        "This way leads to Grancel Port.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "Are you tourists interested in taking a look around?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_A89")

    Jump("loc_AA7")

    label("loc_A8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_A96")
    Jump("loc_AA7")

    label("loc_A96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_AA0")
    Jump("loc_AA7")

    label("loc_AA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_AA7")

    label("loc_AA7")

    TalkEnd(0xFE)
    Return()

    # Function_7_997 end

    def Function_8_AAB(): pass

    label("Function_8_AAB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_CAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_BA2")

    ChrTalk(    #4
        0xFE,
        (
            "That said, there's less of them now than there\x01",
            "were because of orbal airships becoming more\x01",
            "popular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "Still, there's lots of large cargo ships still\x01",
            "coming into the port. It's hard to get bored\x01",
            "just watching them all!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA8")

    label("loc_BA2")


    ChrTalk(    #6
        0xFE,
        (
            "If you head over to the port, you can see all\x01",
            "kinds of foreign ships there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "They come here from Azelia Bay, passing through\x01",
            "the Roubine River along the way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "There's lots of large cargo ships, too. It's hard\x01",
            "to get bored just watching them all!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_CA8")

    Jump("loc_CC6")

    label("loc_CAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_CB5")
    Jump("loc_CC6")

    label("loc_CB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_CBF")
    Jump("loc_CC6")

    label("loc_CBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_CC6")

    label("loc_CC6")

    TalkEnd(0xFE)
    Return()

    # Function_8_AAB end

    def Function_9_CCA(): pass

    label("Function_9_CCA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_E26")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_DBC")

    ChrTalk(    #9
        0xFE,
        (
            "If you're up for recommendations, that coffee\x01",
            "house over there is a real swell spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "Their bitter coffee in particular's really popular!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "I'm more a fan of the atmosphere than anything\x01",
            "on their menu, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E23")

    label("loc_DBC")


    ChrTalk(    #12
        0xFE,
        "*yawn* I'm sooo tired...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "I guess I'll just scarf down some breakfast\x01",
            "in the coffee house.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_E23")

    Jump("loc_E41")

    label("loc_E26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_E30")
    Jump("loc_E41")

    label("loc_E30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_E3A")
    Jump("loc_E41")

    label("loc_E3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_E41")

    label("loc_E41")

    TalkEnd(0xFE)
    Return()

    # Function_9_CCA end

    def Function_10_E45(): pass

    label("Function_10_E45")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x109, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)
    OP_4A(0x13, 255)
    OP_4A(0x14, 255)
    OP_4A(0x15, 255)
    OP_4A(0x16, 255)
    OP_43(0x1D, 0x0, 0x0, 0xB)
    OP_43(0x1E, 0x0, 0x0, 0xB)
    OP_43(0x20, 0x0, 0x0, 0xC)
    OP_43(0x21, 0x0, 0x0, 0xD)
    OP_43(0x22, 0x0, 0x0, 0xE)
    OP_71(0x408, 0x0)
    ExitThread()
    OP_71(0x40F, 0x0)
    ExitThread()
    OP_6D(-63000, 0, -30990, 0)
    OP_67(0, 8300, -10000, 0)
    OP_6B(5010, 0)
    OP_6C(216000, 0)
    OP_6E(309, 0)

    def lambda_F25():
        OP_6D(-64690, 1150, -9120, 8000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F25)

    def lambda_F3D():
        OP_67(0, 7950, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_F3D)

    def lambda_F55():
        OP_6B(5010, 8000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_F55)

    def lambda_F65():
        OP_6C(225000, 8000)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_F65)

    def lambda_F75():
        OP_6E(309, 8000)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_F75)
    FadeToBright(2000, 0)
    OP_0D()
    OP_43(0x109, 0x0, 0x0, 0xF)
    OP_43(0x1B, 0x0, 0x0, 0x10)
    Sleep(5000)
    Fade(1000)
    OP_6D(-78370, 6150, 15020, 0)
    OP_67(0, 7610, -10000, 0)
    OP_6B(5010, 0)
    OP_6C(0, 0)
    OP_6E(317, 0)
    OP_43(0x109, 0x0, 0x0, 0x11)
    OP_43(0x1B, 0x0, 0x0, 0x12)
    OP_43(0x10, 0x3, 0x0, 0x1A)

    def lambda_FF9():
        OP_6D(-78780, 1500, 14220, 7000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_FF9)

    def lambda_1011():
        OP_67(0, 3430, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1011)

    def lambda_1029():
        OP_6B(5010, 7000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1029)

    def lambda_1039():
        OP_6C(0, 7000)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_1039)

    def lambda_1049():
        OP_6E(317, 7000)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_1049)
    OP_0D()
    WaitChrThread(0x109, 0x1)
    OP_23(0x155)
    Sleep(1000)

    def lambda_1067():
        OP_6D(-78780, 2200, 14220, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1067)

    def lambda_107F():
        OP_67(0, 2990, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_107F)

    def lambda_1097():
        OP_6B(4000, 5000)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_1097)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T4131   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_E45 end

    def Function_11_10BE(): pass

    label("Function_11_10BE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11E4")
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10FA")
    Sleep(1000)
    OP_62(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_11E1")

    label("loc_10FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1121")
    Sleep(1300)
    OP_62(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_11E1")

    label("loc_1121")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1148")
    Sleep(1600)
    OP_62(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_11E1")

    label("loc_1148")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_116F")
    Sleep(1900)
    OP_62(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_11E1")

    label("loc_116F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1196")
    Sleep(2200)
    OP_62(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_11E1")

    label("loc_1196")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11BD")
    Sleep(2500)
    OP_62(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_11E1")

    label("loc_11BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11E1")
    Sleep(2800)
    OP_62(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)

    label("loc_11E1")

    Jump("Function_11_10BE")

    label("loc_11E4")

    Return()

    # Function_11_10BE end

    def Function_12_11E5(): pass

    label("Function_12_11E5")

    OP_8E(0xFE, 0xFFFF281A, 0x0, 0xFFFFE8B8, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF29B4, 0xFFFFF15A, 0xFFFF7180, 0x9C4, 0x0)
    Return()

    # Function_12_11E5 end

    def Function_13_120E(): pass

    label("Function_13_120E")

    OP_8E(0xFE, 0xFFFF176C, 0xFFFFF15A, 0xFFFF8918, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF0BC8, 0xFFFFF254, 0xFFFF9DE0, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF0786, 0xFFFFF3B2, 0xFFFF9DEA, 0x9C4, 0x0)
    OP_72(0x1005, 0x0)
    ExitThread()
    Sleep(100)
    OP_6F(0x5, 0)
    OP_70(0x5, 0x3B)
    OP_73(0x5)
    OP_8E(0xFE, 0xFFFF0024, 0xFFFFF4AC, 0xFFFF9DAE, 0x9C4, 0x0)
    OP_6F(0x5, 59)
    OP_70(0x5, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    Return()

    # Function_13_120E end

    def Function_14_1291(): pass

    label("Function_14_1291")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sleep(1500)
    OP_72(0x1009, 0x0)
    ExitThread()
    OP_6F(0x9, 0)
    OP_70(0x9, 0x3B)
    OP_73(0x9)

    def lambda_12BE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12BE)

    def lambda_12D0():
        OP_8E(0xFE, 0xFFFF0A7E, 0xFFFFF15A, 0xFFFF83E6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_12D0)
    Sleep(200)
    OP_6F(0x9, 59)
    OP_70(0x9, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0xFE, 0x3)
    OP_8E(0xFE, 0xFFFF281A, 0xFFFFF15A, 0xFFFF83FA, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF29AA, 0xFFFFF15A, 0xFFFF70EA, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF64E2, 0x0, 0xFFFF6FD2, 0x1388, 0x0)
    Return()

    # Function_14_1291 end

    def Function_15_1342(): pass

    label("Function_15_1342")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -50890, 0, -3860, 270)
    OP_8E(0xFE, 0xFFFEDAEA, 0x0, 0xFFFFF11E, 0x7D0, 0x0)
    Return()

    # Function_15_1342 end

    def Function_16_136D(): pass

    label("Function_16_136D")

    Sleep(300)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -50220, 0, -4380, 270)
    OP_8E(0xFE, 0xFFFEE288, 0x0, 0xFFFFEF34, 0x7D0, 0x0)
    Return()

    # Function_16_136D end

    def Function_17_139D(): pass

    label("Function_17_139D")

    Sleep(2000)
    SetChrPos(0xFE, -79100, 0, 1940, 0)
    OP_8E(0xFE, 0xFFFECC6C, 0x6D6, 0x30A2, 0x7D0, 0x0)
    Sleep(200)
    OP_72(0x100C, 0x0)
    ExitThread()
    OP_6F(0xC, 0)
    OP_70(0xC, 0x3B)
    OP_73(0xC)
    Sleep(200)

    def lambda_13EE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x258)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_13EE)
    OP_8E(0xFE, 0xFFFECB5E, 0x6D6, 0x3872, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_17_139D end

    def Function_18_1414(): pass

    label("Function_18_1414")

    Sleep(2500)
    SetChrPos(0xFE, -79730, 0, 910, 0)
    OP_8E(0xFE, 0xFFFEC9BA, 0x5F0, 0x2AB2, 0x7D0, 0x0)
    Sleep(1000)

    def lambda_1449():
        OP_8E(0xFE, 0xFFFECB4A, 0x6D6, 0x3872, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1449)
    Sleep(1000)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x258)
    WaitChrThread(0xFE, 0x3)
    OP_6F(0xC, 59)
    OP_70(0xC, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0xC)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_18_1414 end

    def Function_19_1492(): pass

    label("Function_19_1492")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xFE, -95400, 18200, -10980, 90)
    SetChrChipByIndex(0xFE, 3)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)
    OP_22(0x155, 0x1, 0x46)
    OP_43(0xFE, 0x2, 0x0, 0x1F)

    def lambda_14DA():
        OP_8F(0xFE, 0xFFFEEB16, 0x5096, 0xFFFFE016, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_14DA)
    Return()

    # Function_19_1492 end

    def Function_20_14F0(): pass

    label("Function_20_14F0")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x155, 0x1, 0x32)
    SetChrPos(0xFE, -95400, 18200, -10980, 90)
    SetChrChipByIndex(0xFE, 3)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)
    OP_22(0x155, 0x1, 0x46)
    OP_43(0xFE, 0x2, 0x0, 0x1F)

    def lambda_153D():
        OP_8F(0xFE, 0xFFFEEB16, 0x5096, 0xFFFFD846, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_153D)
    Return()

    # Function_20_14F0 end

    def Function_21_1553(): pass

    label("Function_21_1553")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xFE, -95400, 18200, -10980, 90)
    SetChrChipByIndex(0xFE, 3)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)
    OP_22(0x155, 0x1, 0x46)
    OP_43(0xFE, 0x2, 0x0, 0x1F)

    def lambda_159B():
        OP_8F(0xFE, 0xFFFEEB16, 0x5096, 0xFFFFD076, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_159B)
    Return()

    # Function_21_1553 end

    def Function_22_15B1(): pass

    label("Function_22_15B1")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xFE, -95400, 18200, -10980, 90)
    SetChrChipByIndex(0xFE, 3)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)
    OP_22(0x155, 0x1, 0x46)
    OP_43(0xFE, 0x2, 0x0, 0x1F)

    def lambda_15F9():
        OP_8F(0xFE, 0xFFFEEB16, 0x5096, 0xFFFFC8A6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_15F9)
    Return()

    # Function_22_15B1 end

    def Function_23_160F(): pass

    label("Function_23_160F")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xFE, -95400, 18200, -10980, 90)
    SetChrChipByIndex(0xFE, 3)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)
    OP_22(0x155, 0x1, 0x46)
    OP_43(0xFE, 0x2, 0x0, 0x1F)

    def lambda_1657():
        OP_8F(0xFE, 0xFFFEEB16, 0x5096, 0xFFFFC0D6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_1657)
    Return()

    # Function_23_160F end

    def Function_24_166D(): pass

    label("Function_24_166D")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xFE, -95400, 18200, -10980, 90)
    SetChrChipByIndex(0xFE, 3)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)
    OP_22(0x155, 0x1, 0x46)
    OP_43(0xFE, 0x2, 0x0, 0x1F)

    def lambda_16B5():
        OP_8F(0xFE, 0xFFFEEB16, 0x5096, 0xFFFFB906, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_16B5)
    Return()

    # Function_24_166D end

    def Function_25_16CB(): pass

    label("Function_25_16CB")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xFE, -95400, 18200, -10980, 90)
    SetChrChipByIndex(0xFE, 3)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)
    OP_22(0x155, 0x1, 0x46)
    OP_43(0xFE, 0x2, 0x0, 0x1F)

    def lambda_1713():
        OP_8F(0xFE, 0xFFFEEB16, 0x5096, 0xFFFFB136, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_1713)
    Return()

    # Function_25_16CB end

    def Function_26_1729(): pass

    label("Function_26_1729")

    OP_43(0x10, 0x1, 0x0, 0x13)
    Sleep(150)
    OP_43(0x14, 0x1, 0x0, 0x17)
    Sleep(100)
    OP_43(0x12, 0x1, 0x0, 0x15)
    Sleep(150)
    OP_43(0x16, 0x1, 0x0, 0x19)
    Sleep(100)
    OP_43(0x11, 0x1, 0x0, 0x14)
    Sleep(150)
    OP_43(0x15, 0x1, 0x0, 0x18)
    Sleep(100)
    OP_43(0x13, 0x1, 0x0, 0x16)
    Return()

    # Function_26_1729 end

    def Function_27_1779(): pass

    label("Function_27_1779")

    SetChrPos(0xFE, -106330, 3290, 5750, 90)
    SetChrChipByIndex(0xFE, 3)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)
    OP_98(0x0, 0xFE)
    OP_98(0x1, 0xFFFEC6FE, 0x23AA, 0x960)
    OP_98(0x1, 0xFFFF3990, 0x50B4, 0x231E)
    OP_43(0xFE, 0x2, 0x0, 0x1F)
    OP_98(0x2, 0xFE, 0x2134, 0x2)
    Return()

    # Function_27_1779 end

    def Function_28_17CF(): pass

    label("Function_28_17CF")

    Sleep(100)
    SetChrPos(0xFE, -105330, 2290, 5750, 90)
    SetChrChipByIndex(0xFE, 3)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)
    OP_98(0x0, 0xFE)
    OP_98(0x1, 0xFFFEC6FE, 0x2792, 0x578)
    OP_98(0x1, 0xFFFF3990, 0x549C, 0x231E)
    OP_43(0xFE, 0x2, 0x0, 0x1F)
    OP_98(0x2, 0xFE, 0x2134, 0x2)
    Return()

    # Function_28_17CF end

    def Function_29_182A(): pass

    label("Function_29_182A")

    Sleep(200)
    SetChrPos(0xFE, -108330, 3290, 5750, 90)
    SetChrChipByIndex(0xFE, 3)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)
    OP_98(0x0, 0xFE)
    OP_98(0x1, 0xFFFEC6FE, 0x2B7A, 0xD48)
    OP_98(0x1, 0xFFFF2DD8, 0x5884, 0x2AEE)
    OP_43(0xFE, 0x2, 0x0, 0x1F)
    OP_98(0x2, 0xFE, 0x2134, 0x2)
    Return()

    # Function_29_182A end

    def Function_30_1885(): pass

    label("Function_30_1885")

    SetChrPos(0xFE, -107330, 2590, 6750, 90)
    SetChrChipByIndex(0xFE, 3)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)
    OP_98(0x0, 0xFE)
    OP_98(0x1, 0xFFFEC6FE, 0x2792, 0x960)
    OP_98(0x1, 0xFFFF2DD8, 0x549C, 0x2AEE)
    OP_43(0xFE, 0x2, 0x0, 0x1F)
    OP_98(0x2, 0xFE, 0x2134, 0x2)
    Return()

    # Function_30_1885 end

    def Function_31_18DB(): pass

    label("Function_31_18DB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_18F0")
    OP_99(0xFE, 0x0, 0x7, 0x1770)
    Jump("Function_31_18DB")

    label("loc_18F0")

    Return()

    # Function_31_18DB end

    def Function_32_18F1(): pass

    label("Function_32_18F1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-39800, 0, 29500, 0)
    OP_67(0, 3660, -10000, 0)
    OP_6B(3140, 0)
    OP_6C(0, 0)
    OP_6E(322, 0)
    SetChrPos(0x103, -39060, 0, 42500, 180)
    SetChrPos(0x151, -40340, 0, 41520, 180)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x18, 0x40)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x1A, 0x40)
    SetChrPos(0x18, -39080, 0, -15580, 0)
    SetChrPos(0x19, -41000, 0, -16860, 0)
    SetChrPos(0x1A, -58700, 0, -3460, 90)
    SetChrChipByIndex(0x18, 18)
    SetChrChipByIndex(0x19, 18)
    SetChrChipByIndex(0x1A, 18)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x23, 0x80)

    def lambda_19D1():
        OP_6B(3140, 2500)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_19D1)

    def lambda_19E1():
        OP_6E(322, 2500)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_19E1)

    def lambda_19F1():
        OP_67(0, 3660, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x24, 3, lambda_19F1)
    FadeToBright(2000, 0)
    Sleep(1500)
    OP_43(0x151, 0x3, 0x0, 0x21)
    OP_43(0x103, 0x3, 0x0, 0x22)
    WaitChrThread(0x24, 0x1)

    def lambda_1A2A():
        OP_6D(-39800, 0, -2300, 5000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_1A2A)
    Sleep(3500)
    Fade(1000)
    OP_67(0, 4920, -10000, 0)
    OP_6B(2620, 0)
    OP_6C(24000, 0)
    OP_6E(364, 0)
    Sleep(1500)
    Sleep(900)

    def lambda_1A82():
        OP_8E(0xFE, 0xFFFF6064, 0x0, 0xFFFFF27C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1A82)
    Sleep(1100)

    def lambda_1AA2():
        OP_8E(0xFE, 0xFFFF6758, 0x0, 0x503C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1AA2)
    Sleep(100)

    def lambda_1AC2():
        OP_8E(0xFE, 0xFFFF5FD8, 0x0, 0x5258, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1AC2)
    WaitChrThread(0x1A, 0x1)

    def lambda_1AE2():
        OP_8E(0xFE, 0xFFFF6384, 0x0, 0xFFFFF59C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1AE2)
    WaitChrThread(0x1A, 0x1)

    def lambda_1B02():
        OP_8E(0xFE, 0xFFFF6384, 0x0, 0x599C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1B02)
    Sleep(1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T4106   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_32_18F1 end

    def Function_33_1B34(): pass

    label("Function_33_1B34")


    def lambda_1B3A():
        OP_8E(0xFE, 0xFFFF626C, 0x0, 0xFFFFF470, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_1B3A)
    WaitChrThread(0x151, 0x1)
    OP_8C(0x151, 270, 500)
    Sleep(500)
    OP_8C(0x151, 180, 500)
    Sleep(500)
    OP_8C(0x151, 0, 500)
    Sleep(200)

    def lambda_1B7E():
        OP_8E(0xFE, 0xFFFF626C, 0x0, 0xA230, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_1B7E)
    Return()

    # Function_33_1B34 end

    def Function_34_1B94(): pass

    label("Function_34_1B94")


    def lambda_1B9A():
        OP_8E(0xFE, 0xFFFF676C, 0x0, 0xFFFFF088, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1B9A)
    WaitChrThread(0x103, 0x1)
    Sleep(500)
    OP_8C(0x103, 270, 500)
    Sleep(500)
    OP_8C(0x103, 0, 500)
    Sleep(300)

    def lambda_1BD7():
        OP_8E(0xFE, 0xFFFF676C, 0x0, 0xA604, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1BD7)
    Return()

    # Function_34_1B94 end

    def Function_35_1BED(): pass

    label("Function_35_1BED")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-63900, -3150, -27000, 0)
    OP_67(0, 5840, -10000, 0)
    OP_6B(4820, 0)
    OP_6C(230000, 0)
    OP_6E(368, 0)
    SetChrPos(0x103, -79300, -3250, -31120, 90)
    SetChrPos(0x151, -79300, -3250, -30060, 90)
    SetChrFlags(0x103, 0x40)
    SetChrFlags(0x151, 0x40)
    OP_9F(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x151, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x23, 0x80)

    def lambda_1C8D():
        OP_6D(-72900, -3750, -30580, 7000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_1C8D)

    def lambda_1CA5():
        OP_6C(270000, 7000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_1CA5)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(2500)
    OP_70(0xA, 0x3C)
    OP_73(0xA)

    def lambda_1CCE():
        OP_8E(0xFE, 0xFFFEE094, 0xFFFFF254, 0xFFFF8670, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1CCE)

    def lambda_1CE9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1CE9)
    Sleep(200)

    def lambda_1D00():
        OP_8E(0xFE, 0xFFFEDAF4, 0xFFFFF254, 0xFFFF8A94, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_1D00)

    def lambda_1D1B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_1D1B)
    WaitChrThread(0x24, 0x0)
    Fade(1000)
    OP_6D(-75840, -3500, -30580, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2820, 0)
    OP_6C(270000, 0)
    OP_6E(320, 0)
    Sleep(1000)
    WaitChrThread(0x103, 0x1)
    WaitChrThread(0x151, 0x1)

    ChrTalk(    #14
        0x151,
        "#1650F#2PWhew... We're finally back on the surface.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x103,
        (
            "#1646FIt's evening, too. That took longer than I thought\x01",
            "it would.\x02\x03",

            "#1642FWe should hurry.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x151, 0x103, 400)
    Sleep(300)

    ChrTalk(    #16
        0x151,
        (
            "#1652F#2POf course...\x02\x03",

            "#1652FAre you all right, though?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    TurnDirection(0x103, 0x151, 500)
    Sleep(1000)

    ChrTalk(    #17
        0x103,
        "#1643FWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x151,
        (
            "#1656F#2PYou look kind of pale...\x02\x03",

            "#1650FAre you feeling tired? Maybe we should rest\x01",
            "a little before moving on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x103,
        (
            "#1647FI-I'm fine!\x02\x03",

            "I've had enough training to handle this level of\x01",
            "physical activity, thank you very much!\x02\x03",

            "#1644FDon't underestimate the stamina of a bracer!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x151,
        "#1653F#2PI-I suppose you're right... I'm sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x103,
        (
            "#1646F...Wait. What the hell?\x02\x03",

            "(She was never more than a few steps behind\x01",
            "me at any given moment...)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x103)
    OP_8C(0x103, 135, 500)
    Sleep(300)

    ChrTalk(    #22
        0x103,
        "#1643F(How is SHE still fine?)\x02",
    )

    CloseMessageWindow()
    OP_62(0x151, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #23
        0x103,
        (
            "#1642F(She never seemed out of breath even when we\x01",
            "were being chased by those guys, come to think\x01",
            "of it...)\x02\x03",

            "#1643F(I feel like there were a few times when she was\x01",
            "even ahead of me...)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(600)

    ChrTalk(    #24
        0x151,
        "#1651F#2P#40W???\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x103,
        (
            "#1644F(What is UP with this girl? Is this, like, nothing\x01",
            "to her?!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x151,
        (
            "#1650F#2PAre you absolutely sure you don't need to rest?\x02\x03",

            "#1651FI do have a few snacks on me. Would you like\x01",
            "me to share some?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x103,
        (
            "#1646FIt's okay. I-I'm definitely fine.\x02\x03",

            "Right now, we need to focus on getting to the\x01",
            "guild so we can hide out there. Food breaks can\x01",
            "wait.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 90, 500)
    Sleep(300)

    ChrTalk(    #28
        0x103,
        (
            "#1646F(We might've run into a lot of trouble on the way,\x01",
            "but the request was to show her around the\x01",
            "capital. I've done that.)\x02\x03",

            "#1642F(Now all I need to do is get back to the guild,\x01",
            "and this request is done. I win!)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_23DF():

        label("loc_23DF")

        TurnDirection(0xFE, 0x103, 400)
        OP_48()
        Jump("loc_23DF")

    QueueWorkItem2(0x151, 3, lambda_23DF)

    def lambda_23F0():
        OP_6D(-73840, -3500, -30580, 1500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_23F0)

    def lambda_2408():
        OP_8E(0xFE, 0xFFFEE864, 0xFFFFF18C, 0xFFFF8670, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2408)
    WaitChrThread(0x103, 0x1)

    ChrTalk(    #29
        0x103,
        "#1644F...Come on! Get a move on!\x02",
    )

    CloseMessageWindow()
    OP_44(0x151, 0x3)
    OP_62(0x151, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_2464():
        OP_8E(0xFE, 0xFFFEE2C4, 0xFFFFF254, 0xFFFF8A94, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_2464)
    WaitChrThread(0x151, 0x1)
    TurnDirection(0x151, 0x103, 500)
    Sleep(100)

    ChrTalk(    #30
        0x151,
        (
            "#1653F#2PI still feel like it would be a good idea to rest\x01",
            "at least a little, though...\x02\x03",

            "Are you certain you're all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x103,
        (
            "#1647FHow many times do I need to repeat myself\x01",
            "before you get the message? \x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x17, -63000, -3000, -35500, 180)
    ClearChrFlags(0x17, 0x80)
    OP_9F(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    NpcTalk(    #32
        0x17,
        "Angry Voice",
        "#2PTo hell with it all!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0xC8)
    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(50)
    OP_62(0x151, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    def lambda_25F5():
        OP_6D(-66780, -3750, -32460, 2000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_25F5)

    def lambda_260D():
        OP_6C(224000, 2000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_260D)
    WaitChrThread(0x24, 0x0)
    OP_72(0x1009, 0x0)
    ExitThread()
    OP_70(0x9, 0x3B)
    OP_73(0x9)

    def lambda_2632():
        OP_8E(0xFE, 0xFFFF09E8, 0xFFFFF18C, 0xFFFF842C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2632)

    def lambda_264D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_264D)
    Sleep(500)

    ChrTalk(    #33
        0x103,
        "#1644F#1P(...Hide!)\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x17, 0x1)

    NpcTalk(    #34
        0x17,
        "Unkempt Man",
        (
            "#144FI was up all night working that damn story!\x01",
            "ALL! NIGHT!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_26D0():
        OP_8E(0xFE, 0xFFFF09E8, 0xFFFFF18C, 0xFFFF8C10, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_26D0)
    WaitChrThread(0x17, 0x1)
    OP_22(0x8E, 0x0, 0x64)

    def lambda_26F5():
        OP_96(0xFE, 0xFFFF09E8, 0xFFFFF18C, 0xFFFF842C, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_26F5)

    def lambda_2713():
        OP_9E(0xFE, 0xA, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_2713)
    WaitChrThread(0x17, 0x1)

    NpcTalk(    #35
        0x17,
        "Unkempt Man",
        (
            "#145FWho the hell does Noticia think she is?!\x02\x03",

            "'The better the scoop, the hotter it needs to\x01",
            "be caught'?!\x02\x03",

            "#144FDoes she think I don't KNOW that?! Arrrgh!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_27DE():
        OP_8E(0xFE, 0xFFFF09E8, 0xFFFFF18C, 0xFFFF8C10, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_27DE)
    WaitChrThread(0x17, 0x1)
    OP_22(0x8E, 0x0, 0x64)

    def lambda_2803():
        OP_96(0xFE, 0xFFFF09E8, 0xFFFFF18C, 0xFFFF842C, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2803)

    def lambda_2821():
        OP_9E(0xFE, 0xA, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_2821)
    WaitChrThread(0x17, 0x1)
    OP_59()
    Fade(1000)
    OP_6D(-74140, -3500, -28760, 0)
    OP_67(0, 3800, -10000, 0)
    OP_6B(2920, 0)
    OP_6C(280000, 0)
    OP_6E(320, 0)
    SetChrPos(0x103, -72900, -3500, -28960, 100)
    SetChrPos(0x151, -74120, -3500, -29060, 100)
    Sleep(1000)

    ChrTalk(    #36
        0x151,
        "#1652F(What do you think he's talking about?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x103,
        (
            "#1646F(I've got no more idea than you do...)\x02\x03",

            "(Maybe he's using some kind of code like those\x01",
            "men from earlier?)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #38
        0x103,
        "#1643F(...He couldn't be one of them, could he?!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x151,
        "#1653F(D-Do you think he could be?)\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #40
        0x17,
        "Angry Voice",
        "Damn it all!\x02",
    )

    CloseMessageWindow()
    OP_22(0x8E, 0x0, 0x64)

    ChrTalk(    #41
        0x103,
        (
            "#1642F(I can't be sure...)\x02\x03",

            "(Just look at his eyes, though. He doesn't look\x01",
            "like a man who makes an honest living to me.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x151,
        "#1652F(I see what you mean...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x103,
        (
            "#1646F(We've come this far. There's no way I'm letting\x01",
            "us get caught now.)\x02\x03",

            "(We need to proceed carefully and deliberately.)\x02\x03",

            "#1642F(Let's see if we can find another route...)\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 135, 500)
    Sleep(500)
    OP_8C(0x103, 0, 500)
    Sleep(500)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2B7D():
        OP_6D(-74240, -3500, -14080, 2000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_2B7D)

    def lambda_2B95():
        OP_67(0, 5960, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_2B95)

    def lambda_2BAD():
        OP_6C(310000, 2000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_2BAD)
    WaitChrThread(0x24, 0x0)
    Sleep(300)

    ChrTalk(    #44
        0x103,
        (
            "#1643F(Ah! If I remember correctly, that house over\x01",
            "there is empty!)\x02\x03",

            "#1644F(This way! Follow me!)\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    SetChrPos(0x103, -73400, -3500, -20900, 0)
    SetChrPos(0x151, -73400, -3500, -24400, 0)

    def lambda_2C52():
        OP_8E(0xFE, 0xFFFEE60C, 0xFFFFF3B2, 0xFFFFC091, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2C52)
    Sleep(50)

    def lambda_2C72():
        OP_8E(0xFE, 0xFFFEE148, 0xFFFFF254, 0xFFFFBE60, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_2C72)
    WaitChrThread(0x103, 0x1)
    Sleep(500)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x73, 0x0, 0x64)
    Sleep(1000)
    OP_70(0x11, 0x3C)
    OP_73(0x11)
    OP_8C(0x103, 180, 500)
    Sleep(100)

    def lambda_2CCB():
        OP_8F(0xFE, 0xFFFEE878, 0xFFFFF3B2, 0xFFFFC091, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2CCB)
    WaitChrThread(0x103, 0x1)

    def lambda_2CEB():
        OP_8E(0xFE, 0xFFFEE4CC, 0xFFFFF3B2, 0xFFFFC091, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_2CEB)
    WaitChrThread(0x151, 0x1)

    def lambda_2D0B():
        OP_8E(0xFE, 0xFFFEE4CC, 0xFFFFF4AC, 0xFFFFC824, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_2D0B)

    def lambda_2D26():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_2D26)
    WaitChrThread(0x151, 0x1)

    def lambda_2D3D():
        OP_8F(0xFE, 0xFFFEE60C, 0xFFFFF3B2, 0xFFFFC091, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2D3D)
    WaitChrThread(0x103, 0x1)
    OP_8C(0x103, 90, 500)
    Sleep(500)
    OP_8C(0x103, 270, 500)
    Sleep(800)
    OP_8C(0x103, 180, 500)
    Sleep(500)

    def lambda_2D81():
        OP_8F(0xFE, 0xFFFEE60C, 0xFFFFF4AC, 0xFFFFC824, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2D81)

    def lambda_2D9C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2D9C)
    WaitChrThread(0x103, 0x1)
    OP_72(0x11, 0x8)
    ExitThread()
    OP_6F(0x11, 30)
    OP_70(0x11, 0x0)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x11)

    def lambda_2DCF():
        OP_6B(2820, 3000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_2DCF)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x24, 0x1)
    SetChrPos(0x17, -54160, -3750, -21840, 0)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x18, -55880, 0, -3100, 180)
    SetChrPos(0x19, -55460, 0, -5260, 0)
    SetChrPos(0x1A, -57020, 0, -5560, 0)
    OP_6D(-54160, -3750, -21840, 0)
    OP_67(0, 6460, -10000, 0)
    OP_6B(2820, 0)
    OP_6C(45000, 0)
    OP_6E(320, 0)
    OP_6A(0x17)
    Sleep(1000)

    def lambda_2E86():
        OP_6B(2920, 3000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_2E86)
    OP_43(0x17, 0x3, 0x0, 0x24)
    FadeToBright(2000, 0)
    OP_0D()
    #Sleep(500)

    NpcTalk(    #45 op#A
        0x17,
        "Unkempt Man",
        (
            "#142F#32AFor Aidios' sake... If I could get conclusive\x01",
            "evidence to back up my story that easily...\x02",
        )
    )

    Sleep(3600)

    NpcTalk(    #46 op#A
        0x17,
        "Unkempt Man",
        "#144F#29A#3S...I would've DONE it already!\x02",
    )

    Sleep(3200)

    ChrTalk(    #47 op#A
        0x18,
        (
            "#24A#2PYou two patrol the area at the bottom of\x01",
            "the stairs. I'll take the area at the top.\x02",
        )
    )

    Sleep(2800)

    ChrTalk(    #48 op#A
        0x19,
        "#7A#4PUnderstood.\x02",
    )

    Sleep(1200)
    OP_8C(0x19, 180, 500)
    Sleep(200)

    def lambda_2FEE():
        OP_8E(0xFE, 0xFFFF270C, 0xFFFFF15A, 0xFFFFB17C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_2FEE)
    Sleep(500)
    OP_43(0x1A, 0x3, 0x0, 0x25)
    OP_8C(0x18, 270, 500)
    Sleep(200)

    def lambda_3021():
        OP_8E(0xFE, 0xFFFEFF20, 0x0, 0xFFFFF3E4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3021)
    Sleep(3000)

    NpcTalk(    #49 op#A
        0x17,
        "Unkempt Man",
        (
            "#142F#38ABah... I guess I'm gonna have to call on\x01",
            "Raymond again...\x02",
        )
    )

    Sleep(4300)
    WaitChrThread(0x17, 0x3)

    NpcTalk(    #50
        0x17,
        "Unkempt Man",
        "#145FWait. He works at the villa now, doesn't he?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x17, 180, 500)
    Sleep(300)

    NpcTalk(    #51
        0x17,
        "Unkempt Man",
        "#142FJust my luck. That's ages away!\x02",
    )

    CloseMessageWindow()

    def lambda_3123():
        OP_8E(0xFE, 0xFFFF6294, 0x0, 0xFFFFAF88, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3123)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 3)), scpexpr(EXPR_END)), "loc_31A6")
    #Sleep(2000)

    NpcTalk(    #52 op#A
        0x17,
        "Unkempt Man",
        (
            "#140F#35A...Oh, yeah. I need to go and get that damn\x01",
            "camera back later, too.\x02",
        )
    )

    Sleep(4500)

    label("loc_31A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 4)), scpexpr(EXPR_END)), "loc_322B")
    #Sleep(2000)

    NpcTalk(    #53 op#A
        0x17,
        "Unkempt Man",
        (
            "#145F#47AI can't believe I had to shell out 3,000 mira for\x01",
            "more photo-quartz 'cause of that brat...\x02",
        )
    )

    Sleep(5500)

    label("loc_322B")

    OP_6A(0xFF)
    #Sleep(2000)

    NpcTalk(    #54 op#A
        0x17,
        "Unkempt Man",
        (
            "#145F#40A#1PI swear, this job is bad for my blood pressure.\x01",
            "I need some more nicotine in me.\x02",
        )
    )

    Sleep(5000)
    Fade(1000)
    OP_6D(-74240, -3500, -14080, 0)
    OP_67(0, 5960, -10000, 0)
    OP_6B(2920, 0)
    OP_6C(310000, 0)
    OP_6E(320, 0)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x151, 0x4)
    SetChrPos(0x103, -73100, -3500, -15300, 0)
    SetChrPos(0x151, -72100, -3500, -15300, 0)
    OP_44(0x19, 0xFF)
    OP_44(0x1A, 0xFF)
    SetChrPos(0x19, -63040, -3500, -17320, 270)
    SetChrPos(0x1A, -60040, -3500, -17320, 270)
    Sleep(2000)

    def lambda_3348():
        OP_8E(0xFE, 0xFFFEDFF4, 0xFFFFF254, 0xFFFFBC58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_3348)
    Sleep(100)
    OP_43(0x1A, 0x3, 0x0, 0x26)
    Sleep(2000)
    OP_62(0x151, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    WaitChrThread(0x19, 0x1)

    def lambda_339D():
        OP_8E(0xFE, 0xFFFEDFF4, 0xFFFFF254, 0xFFFF9980, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_339D)
    WaitChrThread(0x19, 0x1)
    Sleep(1500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_21()
    Sleep(1000)
    NewScene("ED6_DT21/T4152   ._SN", 110, 0, 0)
    IdleLoop()
    Return()

    # Function_35_1BED end

    def Function_36_33DC(): pass

    label("Function_36_33DC")


    def lambda_33E2():
        OP_8E(0xFE, 0xFFFF2C70, 0x0, 0xFFFFE9BC, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_33E2)
    WaitChrThread(0x17, 0x1)

    def lambda_3402():
        OP_8E(0xFE, 0xFFFF33B4, 0x0, 0xFFFFF164, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3402)
    WaitChrThread(0x17, 0x1)

    def lambda_3422():
        OP_8E(0xFE, 0xFFFF5C18, 0x0, 0xFFFFF164, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3422)
    WaitChrThread(0x17, 0x1)

    def lambda_3442():
        OP_8E(0xFE, 0xFFFF6294, 0x0, 0xFFFFF7A4, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3442)
    WaitChrThread(0x17, 0x1)

    def lambda_3462():
        OP_8E(0xFE, 0xFFFF6294, 0x0, 0xAF0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3462)
    WaitChrThread(0x17, 0x1)
    Return()

    # Function_36_33DC end

    def Function_37_347D(): pass

    label("Function_37_347D")

    OP_8C(0x1A, 135, 500)
    Sleep(200)

    def lambda_348F():
        OP_8E(0xFE, 0xFFFF270C, 0xFFFFF15A, 0xFFFFE534, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_348F)
    WaitChrThread(0x1A, 0x1)

    def lambda_34AF():
        OP_8E(0xFE, 0xFFFF270C, 0xFFFFF15A, 0xFFFFB758, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_34AF)
    WaitChrThread(0x1A, 0x1)
    Return()

    # Function_37_347D end

    def Function_38_34CA(): pass

    label("Function_38_34CA")


    def lambda_34D0():
        OP_8E(0xFE, 0xFFFEDFF4, 0xFFFFF254, 0xFFFFBC58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_34D0)
    WaitChrThread(0x1A, 0x1)

    def lambda_34F0():
        OP_8E(0xFE, 0xFFFEDFF4, 0xFFFFF254, 0xFFFF9980, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_34F0)
    WaitChrThread(0x1A, 0x1)
    Return()

    # Function_38_34CA end

    def Function_39_350B(): pass

    label("Function_39_350B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x50, 0xFE, 0x0)
    OP_6D(-60000, -3750, -18720, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(296000, 0)
    OP_6E(338, 0)
    SetChrPos(0x103, -71720, -2900, -14320, 180)
    SetChrPos(0x151, -72680, -2900, -14320, 180)
    OP_9F(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x151, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_359C():
        OP_6D(-72640, -3500, -14280, 8000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_359C)

    def lambda_35B4():
        OP_6B(2800, 8000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_35B4)

    def lambda_35C4():
        OP_6C(335000, 8000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_35C4)

    def lambda_35D4():
        OP_6E(262, 8000)
        ExitThread()

    QueueWorkItem(0x24, 3, lambda_35D4)
    FadeToBright(2000, 0)
    OP_22(0x1C2, 0x0, 0x64)
    OP_0D()
    WaitChrThread(0x24, 0x0)
    OP_23(0x1C2)
    OP_70(0x11, 0x3C)
    OP_73(0x11)

    def lambda_3605():
        OP_8E(0xFE, 0xFFFEE7D8, 0xFFFFF4AC, 0xFFFFC220, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3605)

    def lambda_3620():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3620)
    WaitChrThread(0x103, 0x1)
    OP_8C(0x103, 90, 500)
    Sleep(1000)

    def lambda_3643():
        OP_6D(-75440, -3500, -20580, 4000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_3643)
    OP_43(0x151, 0x3, 0x0, 0x28)
    Sleep(2000)

    def lambda_3667():
        OP_8F(0xFE, 0xFFFEE7D8, 0xFFFFF254, 0xFFFFBE38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3667)
    WaitChrThread(0x103, 0x1)
    OP_72(0x11, 0x8)
    ExitThread()
    OP_6F(0x11, 30)
    OP_70(0x11, 0x0)
    OP_22(0x7, 0x0, 0x64)

    def lambda_36A0():
        OP_8E(0xFE, 0xFFFED9DC, 0xFFFFF254, 0xFFFFB168, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_36A0)
    WaitChrThread(0x103, 0x1)
    OP_8C(0x103, 60, 500)
    Sleep(300)
    WaitChrThread(0x24, 0x0)

    ChrTalk(    #55
        0x103,
        (
            "#1642FSo, where was it in Grancel Castle that we\x01",
            "need to go again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x151,
        (
            "#1652FThe administrative room.\x02\x03",

            "The deadline for submitting the paperwork\x01",
            "is noon.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)
    TurnDirection(0x103, 0x151, 500)
    Sleep(500)

    ChrTalk(    #57
        0x103,
        (
            "#1643FN-Noon?! Noon TODAY?!\x02\x03",

            "#1647FThat barely leaves us any time at all! Why are you\x01",
            "only telling me this now?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x151,
        (
            "#1654FIt has to be filed within a month of the deceased\x01",
            "passing away.\x02\x03",

            "#1652FThat's the law here in Liberl, apparently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x103,
        (
            "#1645FOh, right... I never was much good at this\x01",
            "legal stuff.\x02\x03",

            "I bet Kurt knows it all by heart, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x151,
        (
            "#1653FH-He did seem like the type who might...\x02\x03",

            "#1651FHeehee...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x103,
        (
            "#1641FAhahaha!\x02\x03",

            "#1640F...Let's get going. We don't have any time\x01",
            "to waste.\x02\x03",

            "As long as we do as we discussed earlier,\x01",
            "we should be able to handle this.\x02\x03",

            "We're getting inside the castle, and they're not\x01",
            "going to stop us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x151,
        (
            "#1650F...Miss Scherazard.\x02\x03",

            "I really am glad that you were the one who\x01",
            "undertook my request.\x02\x03",

            "The more time I spend with you, the more\x01",
            "I realize you're really someone dependable--\x01",
            "who relies on their own strength to live.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x103,
        (
            "#1646FYou're blowing my merits out of proportion,\x01",
            "I think.\x02\x03",

            "#1640FAlso, can we stop with the 'Miss Scherazard' \x01",
            "now?\x02\x03",

            "The way you say it, it just makes my name sound\x01",
            "ridiculously long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x151,
        "#1653FD-Does it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x103,
        (
            "#1640FIt does. It feels like our conversations take\x01",
            "twice as long as they should because of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x151,
        (
            "#1650F...\x02\x03",

            "#1654FWell, if you insist.\x02\x03",

            "#1652FAnd now you know all there is to know\x01",
            "about what I want to do.\x02\x03",

            "So I would like to formally request again\x01",
            "that you escort me to Grancel Castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x103,
        (
            "#1642FYou got it.\x02\x03",

            "#1640FYou'll get there. I promise you that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x151,
        "#1651FThank you.\x02",
    )

    CloseMessageWindow()
    OP_6F(0x11, 0)
    OP_71(0x11, 0x8)
    ExitThread()
    EventEnd(0x0)
    Return()

    # Function_39_350B end

    def Function_40_3D61(): pass

    label("Function_40_3D61")


    def lambda_3D67():
        OP_8E(0xFE, 0xFFFEE418, 0xFFFFF254, 0xFFFFBAA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3D67)

    def lambda_3D82():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_3D82)
    WaitChrThread(0x151, 0x1)

    def lambda_3D99():
        OP_8E(0xFE, 0xFFFED9DC, 0xFFFFF254, 0xFFFFB168, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3D99)
    WaitChrThread(0x151, 0x1)

    def lambda_3DB9():
        OP_8E(0xFE, 0xFFFED9DC, 0xFFFFF254, 0xFFFFA7E0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3DB9)
    WaitChrThread(0x151, 0x1)
    Sleep(500)
    OP_8C(0x151, 0, 500)
    Return()

    # Function_40_3D61 end

    def Function_41_3DE0(): pass

    label("Function_41_3DE0")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3E72")
    OP_8C(0x103, 270, 500)
    Sleep(500)
    OP_90(0xEE, 0xFFFFFA24, 0x0, 0x0, 0x7D0, 0x0)
    OP_8C(0x103, 0, 500)
    Sleep(200)

    ChrTalk(    #69
        0x103,
        (
            "#1640FThis way leads to the city's south block.\x02\x03",

            "Let's hurry over to Grancel Castle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F9A")

    label("loc_3E72")

    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #70
        0x151,
        "#1650FOh, are we stopping by at the guild after all?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #71
        0x103,
        (
            "#1646FNo. We don't have time for that.\x02\x03",

            "I doubt Kurt would be there even if we were to\x01",
            "call there, either, given the time of day.\x02\x03",

            "#1640FLet's just get ourselves over to Grancel Castle.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    OP_90(0xEE, 0xFFFFFA24, 0x0, 0x0, 0x7D0, 0x0)

    label("loc_3F9A")

    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_41_3DE0 end

    def Function_42_3FA2(): pass

    label("Function_42_3FA2")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4040")
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #72
        0x103,
        (
            "#1640FThis is the way to the port, not the castle.\x02\x03",

            "I'm not sure trying to approach the castle with\x01",
            "a boat would be a good idea.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41A8")

    label("loc_4040")


    ChrTalk(    #73
        0x103,
        "#1643FWait. This is the way to the port, not the castle.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #74
        0x151,
        (
            "#1656FThat's right.\x02\x03",

            "I did actually consider the possibility of using\x01",
            "a boat to reach Grancel Castle, but...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #75
        0x103,
        (
            "#1645FI'm not sure that'd be such a good idea.\x02\x03",

            "The last thing we want is to get shot by the\x01",
            "soldiers guarding it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x151,
        "#1650FTh-That's a good point...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_41A8")

    OP_90(0xEE, 0x5DC, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_42_3FA2 end

    def Function_43_41C4(): pass

    label("Function_43_41C4")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4245")
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #77
        0x103,
        (
            "#1640FThis way leads down into the sewers.\x02\x03",

            "We don't need to go through there to get\x01",
            "to the castle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_431F")

    label("loc_4245")


    ChrTalk(    #78
        0x103,
        "#1642FThis way leads down into the sewers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x151,
        "#1650FWe did unlock the door, but still...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #80
        0x103,
        (
            "#1645FWe really don't have time to be messing\x01",
            "around down there.\x02\x03",

            "#1642FLet's get over to the castle!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_431F")

    OP_90(0xEE, 0x5DC, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_43_41C4 end

    def Function_44_433B(): pass

    label("Function_44_433B")

    EventBegin(0x2)

    def lambda_4343():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_4343)
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #81
        0x103,
        "#1640FDo you want to go inside and rest a bit?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "Rest\x01",            # 0
            "Don't Rest\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_43E8"),
        (SWITCH_DEFAULT, "loc_449F"),
    )


    label("loc_43E8")

    OP_20(0xBB8)
    OP_8C(0x103, 0, 500)
    FadeToDark(1000, 0, -1)

    def lambda_4404():
        OP_90(0xFE, 0x0, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4404)
    OP_43(0x151, 0x3, 0x0, 0x2D)
    OP_0D()
    WaitChrThread(0x103, 0x1)
    OP_44(0x151, 0x3)
    SetChrPos(0x103, -72140, -2900, -14300, 180)
    SetChrPos(0x151, -72140, -2900, -14300, 180)
    OP_22(0xD, 0x0, 0x64)
    OP_31(0x2, 0xFC, 0x0)
    OP_31(0x50, 0xFC, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x50, 0xFE, 0x0)
    Sleep(1000)
    Sleep(3500)
    OP_1E()
    FadeToBright(1000, 0)

    def lambda_447F():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF6DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_447F)
    OP_0D()
    WaitChrThread(0x103, 0x1)
    EventEnd(0x2)
    Jump("loc_44B8")

    label("loc_449F")

    OP_90(0xEE, 0x0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
    EventEnd(0x2)
    Jump("loc_44B8")

    label("loc_44B8")

    Return()

    # Function_44_433B end

    def Function_45_44B9(): pass

    label("Function_45_44B9")

    Sleep(200)
    OP_8E(0x151, 0xFFFEE634, 0xFFFFF3B2, 0xFFFFC0E0, 0x3E8, 0x0)
    OP_8E(0x151, 0xFFFEE634, 0xFFFFF3B2, 0xFFFFC4C8, 0x3E8, 0x0)
    Return()

    # Function_45_44B9 end

    def Function_46_44E7(): pass

    label("Function_46_44E7")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #82
        (
            "\x07\x05           House for Sale\x01",
            "※Easy conversion to restaurant!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_46_44E7 end

    def Function_47_4554(): pass

    label("Function_47_4554")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_45E4")
    Sleep(300)
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #83
        0x103,
        (
            "#1640FThis way leads down into the sewers.\x02\x03",

            "We don't need to go through there to get\x01",
            "to the castle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46CD")

    label("loc_45E4")


    ChrTalk(    #84
        0x103,
        "#1642FThis way leads down into the sewers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x151,
        "#1650FThe door seems to be unlocked, too...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #86
        0x103,
        (
            "#1645FMaybe so, but we really don't have time to be\x01",
            "messing around down there.\x02\x03",

            "#1642FLet's get over to the castle!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_46CD")

    TalkEnd(0xFF)
    Jump("loc_4721")

    label("loc_46D3")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #87
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)

    label("loc_4721")

    Return()

    # Function_47_4554 end

    def Function_48_4722(): pass

    label("Function_48_4722")

    SetPlaceName(0xB8)
    Return()

    # Function_48_4722 end

    def Function_49_4726(): pass

    label("Function_49_4726")

    SetPlaceName(0xB7)
    Return()

    # Function_49_4726 end

    def Function_50_472A(): pass

    label("Function_50_472A")

    SetPlaceName(0xAF)
    Return()

    # Function_50_472A end

    SaveToFile()

Try(main)
