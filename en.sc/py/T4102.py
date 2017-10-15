from ED6SCScenarioHelper import *

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
        'Private Datten',                       # 9
        'Peter',                                # 10
        'Sharnelle',                            # 11
        'Royal Army Soldier',                   # 12
        'Royal Army Soldier',                   # 13
        'Hashbrown',                            # 14
        'Coffee',                               # 15
        'Pastry',                               # 16
        'Croissant',                            # 17
        'Omelette',                             # 18
        'Golden Toast',                         # 19
        'Donut',                                # 20
        'Gus',                                  # 21
        'Tourist',                              # 22
        'Tourist',                              # 23
        'Royal Army Soldier',                   # 24
        'Grancel - North Block',                # 25
        'Grancel - South Block',                # 26
        'Grancel - N Warehouse District',       # 27
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
    )

    DeclNpc(
        X                   = -89010,
        Z                   = 250,
        Y                   = -1030,
        Direction           = 189,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -78290,
        Z                   = 0,
        Y                   = -2530,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -40940,
        Z                   = 0,
        Y                   = -5120,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = -55400,
        Z                   = 0,
        Y                   = -3050,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -78990,
        Z                   = 1250,
        Y                   = 8029,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
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
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
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
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
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
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
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
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
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
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
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
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
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
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -44500,
        Z                   = 250,
        Y                   = -19980,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = -58590,
        Z                   = -3250,
        Y                   = -22150,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = -58070,
        Z                   = -3250,
        Y                   = -23930,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = -76190,
        Z                   = -3500,
        Y                   = -32240,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
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
        Unknown_1C          = 25,
    )

    DeclEvent(
        X                   = -63390,
        Y                   = -3750,
        Z                   = -24940,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 26,
    )

    DeclEvent(
        X                   = -78840,
        Y                   = 1250,
        Z                   = 12430,
        Range               = 2000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 27,
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
        TalkFunctionIndex   = 23,
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
        TalkFunctionIndex   = 24,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3F2",          # 00, 0
        "Function_1_45D",          # 01, 1
        "Function_2_4E4",          # 02, 2
        "Function_3_508",          # 03, 3
        "Function_4_565",          # 04, 4
        "Function_5_5EA",          # 05, 5
        "Function_6_677",          # 06, 6
        "Function_7_8FE",          # 07, 7
        "Function_8_93E",          # 08, 8
        "Function_9_984",          # 09, 9
        "Function_10_9C8",         # 0A, 10
        "Function_11_A06",         # 0B, 11
        "Function_12_A55",         # 0C, 12
        "Function_13_A9D",         # 0D, 13
        "Function_14_ADC",         # 0E, 14
        "Function_15_EB1",         # 0F, 15
        "Function_16_1263",        # 10, 16
        "Function_17_1822",        # 11, 17
        "Function_18_1A82",        # 12, 18
        "Function_19_1D19",        # 13, 19
        "Function_20_1F39",        # 14, 20
        "Function_21_20BC",        # 15, 21
        "Function_22_225E",        # 16, 22
        "Function_23_254F",        # 17, 23
        "Function_24_25AE",        # 18, 24
        "Function_25_25FD",        # 19, 25
        "Function_26_2601",        # 1A, 26
        "Function_27_2605",        # 1B, 27
    )


    def Function_0_3F2(): pass

    label("Function_0_3F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_415")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    Jump("loc_45C")

    label("loc_415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_429")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_45C")

    label("loc_429")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_43D")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_45C")

    label("loc_43D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44B")
    Jump("loc_45C")

    label("loc_44B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_455")
    Jump("loc_45C")

    label("loc_455")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_45C")

    label("loc_45C")

    Return()

    # Function_0_3F2 end

    def Function_1_45D(): pass

    label("Function_1_45D")

    OP_16(0x2, 0xFA0, 0xFFFD2D58, 0xFFFE0048, 0x23005D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_48F")
    OP_B1("t4102_y")
    Jump("loc_498")

    label("loc_48F")

    OP_B1("t4102_n")

    label("loc_498")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B2")
    OP_71(0x8, 0x4)
    OP_72(0x11, 0x4)
    OP_64(0x0, 0x1)

    label("loc_4B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x300, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4DA")
    OP_10(0x2, 0x0)
    OP_72(0xF, 0x4)
    SetChrPos(0x8, -91300, 250, -3880, 90)
    Jump("loc_4DF")

    label("loc_4DA")

    OP_71(0xF, 0x4)

    label("loc_4DF")

    OP_64(0x1, 0x1)
    Return()

    # Function_1_45D end

    def Function_2_4E4(): pass

    label("Function_2_4E4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_507")
    OP_8D(0xFE, -83110, 1920, -74690, -5430, 3000)
    Jump("Function_2_4E4")

    label("loc_507")

    Return()

    # Function_2_4E4 end

    def Function_3_508(): pass

    label("Function_3_508")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_564")
    OP_8E(0xFE, 0xFFFF6014, 0x0, 0xFFFF711C, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF2C52, 0xFFFFF15A, 0xFFFF727A, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF2C0C, 0x0, 0xFFFFEC82, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF6014, 0x0, 0xFFFFEC00, 0x9C4, 0x0)
    Jump("Function_3_508")

    label("loc_564")

    Return()

    # Function_3_508 end

    def Function_4_565(): pass

    label("Function_4_565")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5E9")
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
    Jump("Function_4_565")

    label("loc_5E9")

    Return()

    # Function_4_565 end

    def Function_5_5EA(): pass

    label("Function_5_5EA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_676")
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
    Jump("Function_5_5EA")

    label("loc_676")

    Return()

    # Function_5_5EA end

    def Function_6_677(): pass

    label("Function_6_677")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x40)
    OP_8D(0xFE, -74920, -1510, -82870, 5610, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6AB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8FD")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8C6")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_77B")
    Sleep(250)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_77B")
    Sleep(500)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_77B")
    Sleep(500)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_77B")
    Sleep(500)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_77B")
    Sleep(500)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_77B")
    Sleep(500)

    label("loc_77B")

    OP_44(0xFE, 0x1)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7B6")

    def lambda_79A():

        label("loc_79A")

        OP_97(0xFE, 0xFFFECB7C, 0x3926, 0x57E40, 0x1B58, 0x1)
        OP_48()
        Jump("loc_79A")

    QueueWorkItem2(0xFE, 1, lambda_79A)
    Jump("loc_7D5")

    label("loc_7B6")


    def lambda_7BC():

        label("loc_7BC")

        OP_97(0xFE, 0xFFFECB7C, 0x3926, 0xFFFA81C0, 0x1B58, 0x1)
        OP_48()
        Jump("loc_7BC")

    QueueWorkItem2(0xFE, 1, lambda_7BC)

    label("loc_7D5")

    SetChrChipByIndex(0xFE, 3)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)

    label("loc_7E4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_81C")
    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2328), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_814")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
    Jump("loc_81C")

    label("loc_814")

    Sleep(15)
    Jump("loc_7E4")

    label("loc_81C")

    SetChrFlags(0xFE, 0x80)
    OP_44(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -78690, 0, -40, 74)

    label("loc_83B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8C3")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8BB")
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 4)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8D(0xFE, -74920, -1510, -82870, 5610, 0)
    Jump("loc_8C3")

    label("loc_8BB")

    Sleep(500)
    Jump("loc_83B")

    label("loc_8C3")

    Jump("loc_8FA")

    label("loc_8C6")

    Sleep(100)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FA")

    def lambda_8E2():
        OP_8D(0xFE, -74920, -1510, -82870, 5610, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8E2)

    label("loc_8FA")

    Jump("loc_6AB")

    label("loc_8FD")

    Return()

    # Function_6_677 end

    def Function_7_8FE(): pass

    label("Function_7_8FE")

    OP_4A(0xFE, 255)
    TalkBegin(0xFE)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(1000)

    ChrTalk(    #0
        0xFE,
        "*chirp chirp*\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    OP_4B(0xFE, 255)
    Return()

    # Function_7_8FE end

    def Function_8_93E(): pass

    label("Function_8_93E")

    OP_4A(0xFE, 255)
    TalkBegin(0xFE)
    OP_62(0xFE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(1000)

    ChrTalk(    #1
        0xFE,
        "*CHIRP CHIRP!*\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    OP_4B(0xFE, 255)
    Return()

    # Function_8_93E end

    def Function_9_984(): pass

    label("Function_9_984")

    OP_4A(0xFE, 255)
    TalkBegin(0xFE)
    OP_62(0xFE, 0x0, 1900, 0x33, 0x35, 0xC8, 0x0)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(1000)

    ChrTalk(    #2
        0xFE,
        "Nyaon? Fumyaaa...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    OP_4B(0xFE, 255)
    Return()

    # Function_9_984 end

    def Function_10_9C8(): pass

    label("Function_10_9C8")

    OP_4A(0xFE, 255)
    TalkBegin(0xFE)
    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(1000)

    ChrTalk(    #3
        0xFE,
        "*chirrr...*\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    OP_4B(0xFE, 255)
    Return()

    # Function_10_9C8 end

    def Function_11_A06(): pass

    label("Function_11_A06")

    OP_4A(0xFE, 255)
    TalkBegin(0xFE)
    OP_62(0xFE, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(1000)

    ChrTalk(    #4
        0xFE,
        "*chirp chirp... chirp?*\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    OP_4B(0xFE, 255)
    Return()

    # Function_11_A06 end

    def Function_12_A55(): pass

    label("Function_12_A55")

    OP_4A(0xFE, 255)
    TalkBegin(0xFE)
    OP_62(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(1000)
    OP_EA(0x0, 0x2, 0x0, 0x0)

    ChrTalk(    #5
        0xFE,
        "*chiiiirp?*\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    OP_4B(0xFE, 255)
    Return()

    # Function_12_A55 end

    def Function_13_A9D(): pass

    label("Function_13_A9D")

    OP_4A(0xFE, 255)
    TalkBegin(0xFE)
    OP_62(0xFE, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    OP_22(0x2F, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(1000)

    ChrTalk(    #6
        0xFE,
        "*CHIRP*\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    OP_4B(0xFE, 255)
    Return()

    # Function_13_A9D end

    def Function_14_ADC(): pass

    label("Function_14_ADC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_B67")

    ChrTalk(    #7
        0xFE,
        (
            "Apparently you can see that huge floating\x01",
            "thing from the harbor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "A number of civilians have gone off\x01",
            "to look at it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EAD")

    label("loc_B67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_C35")

    ChrTalk(    #9
        0xFE,
        (
            "Bringing an orbal tank...\x01",
            "Aidios, talk about going all out!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "Sorry, but the harbor's currently in\x01",
            "the middle of rebuilding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "It'll probably be a while before\x01",
            "we can let you in again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EAD")

    label("loc_C35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_CE4")

    ChrTalk(    #12
        0xFE,
        (
            "There are a lot more soldiers around lately.\x01",
            "It's kind of an imposing display, but I guess\x01",
            "that's the point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "The signing ceremony IS coming up,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EAD")

    label("loc_CE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D31")

    ChrTalk(    #14
        0xFE,
        (
            "Almost evening, huh?\x01",
            "Just about time to change the watch.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EAD")

    label("loc_D31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_DB1")

    ChrTalk(    #15
        0xFE,
        (
            "I see those Fisherman's Guild guys\x01",
            "going fishing at the harbor a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "I wonder what they catch around here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_EAD")

    label("loc_DB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_EAD")

    ChrTalk(    #17
        0xFE,
        (
            "Beyond this is one of the city's premiere\x01",
            "tourist spots, the harbor and warehouse\x01",
            "district.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "It was closed off during the coup\x01",
            "d'etat on orders of Colonel Richard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "If you've got the time, it might be\x01",
            "worth going and taking a look.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EAD")

    TalkEnd(0xFE)
    Return()

    # Function_14_ADC end

    def Function_15_EB1(): pass

    label("Function_15_EB1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_F3D")

    ChrTalk(    #20
        0xFE,
        "Phew! I need to get home before dark.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "The capital on dark nights is pitch black\x01",
            "and scary even when you're grown up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_125F")

    label("loc_F3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_FD0")

    ChrTalk(    #22
        0xFE,
        (
            "The entire city's talking about the\x01",
            "Intelligence Division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "I wonder if the people working at\x01",
            "the harbor facilities are okay...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_125F")

    label("loc_FD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1021")

    ChrTalk(    #24
        0xFE,
        "Have lunch yet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        "I recommend the cafe here in the west block.\x02",
    )

    CloseMessageWindow()
    Jump("loc_125F")

    label("loc_1021")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10DA")

    ChrTalk(    #26
        0xFE,
        (
            "I've been seeing a man with disheveled green\x01",
            "hair going into the cathedral a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "Is he a priest or something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "Can't say he looks particularly, uh, holy...\x02",
    )

    CloseMessageWindow()
    Jump("loc_125F")

    label("loc_10DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_11A0")

    ChrTalk(    #29
        0xFE,
        (
            "During the coup d'etat, General Morgan's\x01",
            "granddaughter, Rianne, was kidnapped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "Taking a little girl as a hostage...\x01",
            "Those Intelligence Division guys sure\x01",
            "are a bunch of cowards!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_125F")

    label("loc_11A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_125F")

    ChrTalk(    #31
        0xFE,
        "Did you visit the harbor yet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "Cargo offloading isn't as common in\x01",
            "the harbor as it used to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "Lately, the warehouse district's more\x01",
            "being used as rental storage space.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_125F")

    TalkEnd(0xFE)
    Return()

    # Function_15_EB1 end

    def Function_16_1263(): pass

    label("Function_16_1263")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_12F0")

    ChrTalk(    #34
        0xFE,
        (
            "How much longer until the orbments\x01",
            "work again?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "I didn't think life without orbments\x01",
            "like this would feel so awful...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_181E")

    label("loc_12F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1553")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_13A1")

    ChrTalk(    #36
        0xFE,
        (
            "After that incident with Captain Amalthea and\x01",
            "everything, it feels pretty dangerous here in\x01",
            "the west block.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        "Maybe I should move to the south block...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1550")

    label("loc_13A1")


    ChrTalk(    #38
        0xFE,
        "Yesterday, I heard someone arguing around here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "Though given the hour, it might've just\x01",
            "been a couple of drunks fighting...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "After that incident with Captain Amalthea and\x01",
            "everything, it feels pretty dangerous here in\x01",
            "the west block.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        "Maybe I should move to the south block...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "I'd rather be in the north block, but that's\x01",
            "premium real estate, being so close to the\x01",
            "castle and all. The rent is crazy there.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1550")

    Jump("loc_181E")

    label("loc_1553")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1609")

    ChrTalk(    #43
        0xFE,
        "There are a lot more soldiers around now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "I know the signing ceremony's close,\x01",
            "so that's just how it's got to be, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        "...it does kinda make me nervous.\x02",
    )

    CloseMessageWindow()
    Jump("loc_181E")

    label("loc_1609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1643")

    ChrTalk(    #46
        0xFE,
        "Hmm, what to do for dinner tonight...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_181E")

    label("loc_1643")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1744")

    ChrTalk(    #47
        0xFE,
        (
            "I wonder if Princess Klaudia will make an\x01",
            "appearance at the signing ceremony...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "I think it'd be far more visually pleasing than\x01",
            "having Duke Dunan there, at the very least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "I don't see Princess Klaudia at many\x01",
            "public events, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_181E")

    label("loc_1744")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_181E")

    ChrTalk(    #50
        0xFE,
        "Hello, how are you feeling?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "In this block there's the cathedral, the Liberl\x01",
            "News, and a great cafe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "If you want to have a quiet, sophisticated\x01",
            "experience, there's no block better than\x01",
            "West Block!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_181E")

    TalkEnd(0xFE)
    Return()

    # Function_16_1263 end

    def Function_17_1822(): pass

    label("Function_17_1822")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1873")

    ChrTalk(    #53
        0xFE,
        (
            "It seems Queen Alicia has some plan\x01",
            "to resolve this situation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A7E")

    label("loc_1873")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1995")

    ChrTalk(    #54
        0xFE,
        (
            "They say the Royal Army's been using\x01",
            "military ships to perform a large-scale\x01",
            "investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "They've found their target a number of times,\x01",
            "but they keep getting shaken off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "And shaking off military ships is no small\x01",
            "order. Who the heck could design such\x01",
            "a machine?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A7E")

    label("loc_1995")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1A5F")

    ChrTalk(    #57
        0xFE,
        (
            "Colonel Cid is very humble, but also\x01",
            "extremely capable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "Aside from simply being our commanding\x01",
            "officer, they say he's also a master of arts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "Pretty incredible, don't you think?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A7E")

    label("loc_1A5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A6D")
    Jump("loc_1A7E")

    label("loc_1A6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1A77")
    Jump("loc_1A7E")

    label("loc_1A77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1A7E")

    label("loc_1A7E")

    TalkEnd(0xFE)
    Return()

    # Function_17_1822 end

    def Function_18_1A82(): pass

    label("Function_18_1A82")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1B4C")

    ChrTalk(    #60
        0xFE,
        (
            "Everyone's taking the Orbal Shutdown\x01",
            "Phenomenon differently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "Well, one way or another, it doesn't change the\x01",
            "fact that it's freakin' inconvenient, so I hope\x01",
            "they fix things soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D15")

    label("loc_1B4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1BD3")

    ChrTalk(    #62
        0xFE,
        "Captain Amalthea, huh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "A pitiable end for someone who used to be\x01",
            "an elite officer of the Intelligence Division.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D15")

    label("loc_1BD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1CF6")

    ChrTalk(    #64
        0xFE,
        (
            "I've received orders from HQ to guard\x01",
            "critical points here in the west block.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "Apparently there were threatening letters\x01",
            "sent to the cathedral and to the Liberl News.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "The Liberl News is one thing, but to lob a\x01",
            "threat at the church? Pretty damned bold,\x01",
            "if you ask me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D15")

    label("loc_1CF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D04")
    Jump("loc_1D15")

    label("loc_1D04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1D0E")
    Jump("loc_1D15")

    label("loc_1D0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1D15")

    label("loc_1D15")

    TalkEnd(0xFE)
    Return()

    # Function_18_1A82 end

    def Function_19_1D19(): pass

    label("Function_19_1D19")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1D26")
    Jump("loc_1F35")

    label("loc_1D26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1D82")

    ChrTalk(    #67
        0xFE,
        (
            "I'm hearing that there was a battle over\x01",
            "near the harbor. That's just crazy!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F35")

    label("loc_1D82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1E56")

    ChrTalk(    #68
        0xFE,
        (
            "I intend to go for a walk out in the harbor\x01",
            "and warehouse district.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "...It's a bit odd having a harbor on a lake,\x01",
            "come to think of it. They usually build\x01",
            "those out on the open sea, don't they?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F35")

    label("loc_1E56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E9F")

    ChrTalk(    #70
        0xFE,
        (
            "Why does watching the sun set make\x01",
            "me all misty-eyed?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F35")

    label("loc_1E9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1EE1")

    ChrTalk(    #71
        0xFE,
        (
            "So that building is the Liberl News\x01",
            "Service, then?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F35")

    label("loc_1EE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1F35")

    ChrTalk(    #72
        0xFE,
        "You can see the whole west block from here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        "It's my favorite spot.\x02",
    )

    CloseMessageWindow()

    label("loc_1F35")

    TalkEnd(0xFE)
    Return()

    # Function_19_1D19 end

    def Function_20_1F39(): pass

    label("Function_20_1F39")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1F46")
    Jump("loc_20B8")

    label("loc_1F46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1F8F")

    ChrTalk(    #74
        0xFE,
        (
            "I thought I'd go see the sights,\x01",
            "but the harbor's closed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20B8")

    label("loc_1F8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1FC9")

    ChrTalk(    #75
        0xFE,
        "Whoa... I'm amazed you can drink it black.\x02",
    )

    CloseMessageWindow()
    Jump("loc_20B8")

    label("loc_1FC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2009")

    ChrTalk(    #76
        0xFE,
        "All we do is sit and chat wherever we visit.\x02",
    )

    CloseMessageWindow()
    Jump("loc_20B8")

    label("loc_2009")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2050")

    ChrTalk(    #77
        0xFE,
        (
            "Ahhh, isn't there some nice man out there\x01",
            "somewhere...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20B8")

    label("loc_2050")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_20B8")

    ChrTalk(    #78
        0xFE,
        (
            "A rice curry lunch for two young\x01",
            "maidens at an outdoor cafe...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        "Haha, how very like us.\x02",
    )

    CloseMessageWindow()

    label("loc_20B8")

    TalkEnd(0xFE)
    Return()

    # Function_20_1F39 end

    def Function_21_20BC(): pass

    label("Function_21_20BC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_20C9")
    Jump("loc_225A")

    label("loc_20C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_20F6")

    ChrTalk(    #80
        0xFE,
        "Indeed... This, too, is fate.\x02",
    )

    CloseMessageWindow()
    Jump("loc_225A")

    label("loc_20F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_216A")

    ChrTalk(    #81
        0xFE,
        "Coffee, like life, has a bitter taste.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "It's fruitless to try and hide\x01",
            "it behind milk and sugar.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_225A")

    label("loc_216A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21D3")

    ChrTalk(    #83
        0xFE,
        (
            "And really, as long as you're having fun,\x01",
            "what's the problem? I think it's very...us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_225A")

    label("loc_21D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2220")

    ChrTalk(    #84
        0xFE,
        "Oh, there are good men.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        "We simply aren't finding them...\x02",
    )

    CloseMessageWindow()
    Jump("loc_225A")

    label("loc_2220")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_225A")

    ChrTalk(    #86
        0xFE,
        "Calling yourself a maiden? How very like you.\x02",
    )

    CloseMessageWindow()

    label("loc_225A")

    TalkEnd(0xFE)
    Return()

    # Function_21_20BC end

    def Function_22_225E(): pass

    label("Function_22_225E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_22CB")

    ChrTalk(    #87
        0xFE,
        "You're free to enter the sewers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "However, do be sure not to cause any\x01",
            "trouble inside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_254B")

    label("loc_22CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2369")

    ChrTalk(    #89
        0xFE,
        (
            "Apparently the Intelligence Division guys\x01",
            "were hiding a tank. A whole friggin' tank!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "I'm really glad there wasn't any damage\x01",
            "to the city.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_254B")

    label("loc_2369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_23E9")

    ChrTalk(    #91
        0xFE,
        (
            "Seems like local security is\x01",
            "gonna really start stepping up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        "Even I can't help but feel more on edge now.\x02",
    )

    CloseMessageWindow()
    Jump("loc_254B")

    label("loc_23E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2444")

    ChrTalk(    #93
        0xFE,
        (
            "...Just about time for a shift change.\x01",
            "The watch here is really boring.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_254B")

    label("loc_2444")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_24D7")

    ChrTalk(    #94
        0xFE,
        (
            "Apparently some people use these sewers\x01",
            "for training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "Right now, we're only letting bracers \x01",
            "on monster hunts through, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_254B")

    label("loc_24D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_254B")

    ChrTalk(    #96
        0xFE,
        "Oh, you guys are bracers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "You're welcome to enter the sewers,\x01",
            "but it's dark inside, so be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_254B")

    TalkEnd(0xFE)
    Return()

    # Function_22_225E end

    def Function_23_254F(): pass

    label("Function_23_254F")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #98
        (
            "\x07\x05House For Sale\x01",
            "※Also Zoned For Food Service\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_23_254F end

    def Function_24_25AE(): pass

    label("Function_24_25AE")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #99
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_24_25AE end

    def Function_25_25FD(): pass

    label("Function_25_25FD")

    SetPlaceName(0xB8)
    Return()

    # Function_25_25FD end

    def Function_26_2601(): pass

    label("Function_26_2601")

    SetPlaceName(0xB7)
    Return()

    # Function_26_2601 end

    def Function_27_2605(): pass

    label("Function_27_2605")

    SetPlaceName(0xAF)
    Return()

    # Function_27_2605 end

    SaveToFile()

Try(main)
