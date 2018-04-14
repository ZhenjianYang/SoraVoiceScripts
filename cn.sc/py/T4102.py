from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        '士兵达登',                             # 9
        '比卡',                                 # 10
        '夏妮',                                 # 11
        '王国军士兵',                           # 12
        '王国军士兵',                           # 13
        '鸽子',                                 # 14
        '鸽子',                                 # 15
        '鸽子',                                 # 16
        '鸽子',                                 # 17
        '鸽子',                                 # 18
        '鸽子',                                 # 19
        '鸽子',                                 # 20
        '格斯',                                 # 21
        '游客',                                 # 22
        '游客',                                 # 23
        '王国军士兵',                           # 24
        '王都格兰赛尔·北街区',                 # 25
        '王都格兰赛尔·南街区',                 # 26
        '王都格兰赛尔·码头',                   # 27
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
        TalkScenaIndex      = 7,
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
        TalkScenaIndex      = 8,
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
        TalkScenaIndex      = 9,
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
        TalkScenaIndex      = 10,
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
        InitScenaIndex      = 6,
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
        InitScenaIndex      = 6,
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
        InitScenaIndex      = 6,
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
        InitScenaIndex      = 6,
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
        InitScenaIndex      = 6,
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
        InitScenaIndex      = 6,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        TalkScenaIndex      = 12,
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
        TalkScenaIndex      = 13,
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
        TalkScenaIndex      = 14,
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
        TalkScenaIndex      = 15,
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
        Unknown_1C          = 18,
    )

    DeclEvent(
        X                   = -63390,
        Y                   = -3750,
        Z                   = -24940,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 19,
    )

    DeclEvent(
        X                   = -78840,
        Y                   = 1250,
        Z                   = 12430,
        Range               = 2000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 20,
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
        TalkFunctionIndex   = 16,
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
        TalkFunctionIndex   = 17,
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
        "Function_7_87A",          # 07, 7
        "Function_8_ADE",          # 08, 8
        "Function_9_D2A",          # 09, 9
        "Function_10_1092",        # 0A, 10
        "Function_11_1223",        # 0B, 11
        "Function_12_13A2",        # 0C, 12
        "Function_13_14E8",        # 0D, 13
        "Function_14_1607",        # 0E, 14
        "Function_15_173B",        # 0F, 15
        "Function_16_1922",        # 10, 16
        "Function_17_1973",        # 11, 17
        "Function_18_19B9",        # 12, 18
        "Function_19_19BD",        # 13, 19
        "Function_20_19C1",        # 14, 20
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

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_879")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_842")
    OP_44(0xFE, 0x1)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_732")

    def lambda_716():

        label("loc_716")

        OP_97(0xFE, 0xFFFECB7C, 0x3926, 0x57E40, 0x1B58, 0x1)
        OP_48()
        Jump("loc_716")

    QueueWorkItem2(0xFE, 1, lambda_716)
    Jump("loc_751")

    label("loc_732")


    def lambda_738():

        label("loc_738")

        OP_97(0xFE, 0xFFFECB7C, 0x3926, 0xFFFA81C0, 0x1B58, 0x1)
        OP_48()
        Jump("loc_738")

    QueueWorkItem2(0xFE, 1, lambda_738)

    label("loc_751")

    SetChrChipByIndex(0xFE, 3)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)

    label("loc_760")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_798")
    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2328), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_790")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
    Jump("loc_798")

    label("loc_790")

    Sleep(15)
    Jump("loc_760")

    label("loc_798")

    SetChrFlags(0xFE, 0x80)
    OP_44(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -78690, 0, -40, 74)

    label("loc_7B7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_83F")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_837")
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 4)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8D(0xFE, -74920, -1510, -82870, 5610, 0)
    Jump("loc_83F")

    label("loc_837")

    Sleep(500)
    Jump("loc_7B7")

    label("loc_83F")

    Jump("loc_876")

    label("loc_842")

    Sleep(100)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_876")

    def lambda_85E():
        OP_8D(0xFE, -74920, -1510, -82870, 5610, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_85E)

    label("loc_876")

    Jump("loc_6AB")

    label("loc_879")

    Return()

    # Function_6_677 end

    def Function_7_87A(): pass

    label("Function_7_87A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_8D6")

    ChrTalk(    #0
        0xFE,
        (
            "好像在港口能看见那个\x01",
            "飘浮的像贝壳一样的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "有好几个市民去参观了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_ADA")

    label("loc_8D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_959")

    ChrTalk(    #2
        0xFE,
        (
            "……竟然搬出导力坦克，\x01",
            "搞得还真是大。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "抱歉，现在格兰赛尔港\x01",
            "正在进行修复工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "应该还要过一阵子\x01",
            "才能进去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ADA")

    label("loc_959")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_9B4")

    ChrTalk(    #5
        0xFE,
        (
            "士兵数量一下子增加了，\x01",
            "气氛好像变得很森严。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        "不过签字仪式也是快到了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_ADA")

    label("loc_9B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9E7")

    ChrTalk(    #7
        0xFE,
        (
            "已经傍晚了啊……\x01",
            "快要交接班了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ADA")

    label("loc_9E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_A3E")

    ChrTalk(    #8
        0xFE,
        (
            "经常能在港口看见\x01",
            "钓公师团的家伙们在钓鱼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "那一带究竟能钓到什么呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_ADA")

    label("loc_A3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_ADA")

    ChrTalk(    #10
        0xFE,
        (
            "前边是这个城市的旅游景点之一，\x01",
            "格兰赛尔港和仓库街哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "就是政变的时候被理查德\x01",
            "上校命令封锁的地区。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "如果有时间的话\x01",
            "你们可以去参观一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ADA")

    TalkEnd(0xFE)
    Return()

    # Function_7_87A end

    def Function_8_ADE(): pass

    label("Function_8_ADE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_B35")

    ChrTalk(    #13
        0xFE,
        (
            "呼，在天黑之前\x01",
            "必须回家。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "王都的黑夜对大人来说\x01",
            "也是暗得可怕的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D26")

    label("loc_B35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_B8C")

    ChrTalk(    #15
        0xFE,
        "情报部的事闹得全城都沸沸扬扬的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "在港口的设施工作的\x01",
            "家伙们没事吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D26")

    label("loc_B8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_BD3")

    ChrTalk(    #17
        0xFE,
        "午饭吃过了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "西街区这边的咖啡馆\x01",
            "可是很不错的哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D26")

    label("loc_BD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C4C")

    ChrTalk(    #19
        0xFE,
        (
            "最近好像有个\x01",
            "竖着绿头发的家伙\x01",
            "出入大圣堂……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "那位小兄弟\x01",
            "难道是神职人员？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "似乎有点看不出来。\x02",
    )

    CloseMessageWindow()
    Jump("loc_D26")

    label("loc_C4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_CC1")

    ChrTalk(    #22
        0xFE,
        (
            "政变时摩尔根将军的\x01",
            "孙女莉安妮好像被\x01",
            "绑架过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "竟然把年幼的女孩子当作人质，\x01",
            "情报部的作法真是卑鄙。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D26")

    label("loc_CC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_D26")

    ChrTalk(    #24
        0xFE,
        "去港口看过了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "港口的卸货频率\x01",
            "没有以前高了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "现在仓库街的作用\x01",
            "只是出租仓库。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D26")

    TalkEnd(0xFE)
    Return()

    # Function_8_ADE end

    def Function_9_D2A(): pass

    label("Function_9_D2A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_D85")

    ChrTalk(    #27
        0xFE,
        (
            "导力器能不能\x01",
            "快点恢复呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "想不到没有导力器的\x01",
            "生活竟然这么悲惨……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_108E")

    label("loc_D85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_ECF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_DE7")

    ChrTalk(    #29
        0xFE,
        (
            "又发生了凯诺娜上尉的事，\x01",
            "西街区这边真是不太平。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "要不要搬去南街区呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_ECC")

    label("loc_DE7")


    ChrTalk(    #31
        0xFE,
        (
            "昨天听到这附近\x01",
            "有人在争论的声音。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "反正那种时间也有可能\x01",
            "是醉汉们在吵架。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "又发生了凯诺娜上尉的事，\x01",
            "西街区这边真是不太平。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "要不要搬去南街区呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "其实还是北街区最好，不过那儿\x01",
            "是王城的黄金地段，房租也高。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_ECC")

    Jump("loc_108E")

    label("loc_ECF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_F46")

    ChrTalk(    #36
        0xFE,
        "士兵的数量增加了不少呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "我也知道在临近签字仪式的\x01",
            "现在这也是没办法的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        "不过总觉得有点紧张。\x02",
    )

    CloseMessageWindow()
    Jump("loc_108E")

    label("loc_F46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F70")

    ChrTalk(    #39
        0xFE,
        "今天的晚饭吃什么呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_108E")

    label("loc_F70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_FFF")

    ChrTalk(    #40
        0xFE,
        (
            "科洛蒂娅会不会\x01",
            "出席签字仪式呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "感觉比起让杜南公爵出场，\x01",
            "她要受欢迎得多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "不过科洛蒂娅公主好像\x01",
            "很少出现在正式场合。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_108E")

    label("loc_FFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_108E")

    ChrTalk(    #43
        0xFE,
        "你们好啊，最近怎么样？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "这个街区有大圣堂、利贝尔通讯社\x01",
            "和咖啡馆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "想要安静地度过属于成年人的\x01",
            "时间还是只有在西街区才行啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_108E")

    TalkEnd(0xFE)
    Return()

    # Function_9_D2A end

    def Function_10_1092(): pass

    label("Function_10_1092")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_10CF")

    ChrTalk(    #46
        0xFE,
        (
            "艾莉茜雅女王\x01",
            "应该有办法应对\x01",
            "现在的局面……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_121F")

    label("loc_10CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1170")

    ChrTalk(    #47
        0xFE,
        (
            "王国军好像用军用艇\x01",
            "进行了相当大规模的搜索。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "虽然发现了几次目标，\x01",
            "不过听说都被甩开了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "竟然能甩开那种军用艇……\x01",
            "那机器究竟是谁造的呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_121F")

    label("loc_1170")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1200")

    ChrTalk(    #50
        0xFE,
        (
            "希德中校虽然不好张扬，\x01",
            "不过似乎是个相当优秀的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "当士官的水平自不必说，\x01",
            "其实他的魔法也很厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        "是不是感觉有点意外？\x02",
    )

    CloseMessageWindow()
    Jump("loc_121F")

    label("loc_1200")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_120E")
    Jump("loc_121F")

    label("loc_120E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1218")
    Jump("loc_121F")

    label("loc_1218")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_121F")

    label("loc_121F")

    TalkEnd(0xFE)
    Return()

    # Function_10_1092 end

    def Function_11_1223(): pass

    label("Function_11_1223")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1291")

    ChrTalk(    #53
        0xFE,
        (
            "市民对导力停止的反应\x01",
            "不一而足。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "反正不管怎样，\x01",
            "感觉不方便是肯定的，\x01",
            "真希望能早点恢复。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_139E")

    label("loc_1291")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_12DC")

    ChrTalk(    #55
        0xFE,
        "凯诺娜上尉……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "当年情报部的精英士官\x01",
            "竟然落得如此下场。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_139E")

    label("loc_12DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_137F")

    ChrTalk(    #57
        0xFE,
        (
            "本部要求我们重点\x01",
            "加强西街区这边的警戒。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "因为大圣堂和利贝尔通讯社\x01",
            "收到了恐吓信。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "利贝尔通讯社姑且不论，对大圣堂\x01",
            "也寄恐吓信，真是胆大包天。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_139E")

    label("loc_137F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_138D")
    Jump("loc_139E")

    label("loc_138D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1397")
    Jump("loc_139E")

    label("loc_1397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_139E")

    label("loc_139E")

    TalkEnd(0xFE)
    Return()

    # Function_11_1223 end

    def Function_12_13A2(): pass

    label("Function_12_13A2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_13AF")
    Jump("loc_14E4")

    label("loc_13AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_13E0")

    ChrTalk(    #60
        0xFE,
        (
            "听说港口发生了战斗……\x01",
            "吓我一跳。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14E4")

    label("loc_13E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_143C")

    ChrTalk(    #61
        0xFE,
        (
            "我准备去港口的\x01",
            "仓库街散步。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "……湖上竟然有港口，\x01",
            "总觉得有点不可思议哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14E4")

    label("loc_143C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_146D")

    ChrTalk(    #63
        0xFE,
        (
            "看着晚霞为何\x01",
            "会让人想流泪呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14E4")

    label("loc_146D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_14A0")

    ChrTalk(    #64
        0xFE,
        (
            "呼，那座建筑物\x01",
            "就是利贝尔通讯社吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14E4")

    label("loc_14A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_14E4")

    ChrTalk(    #65
        0xFE,
        (
            "从这里可以对西街区\x01",
            "一览无遗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        "这是我很喜欢的地方。\x02",
    )

    CloseMessageWindow()

    label("loc_14E4")

    TalkEnd(0xFE)
    Return()

    # Function_12_13A2 end

    def Function_13_14E8(): pass

    label("Function_13_14E8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_14F5")
    Jump("loc_1603")

    label("loc_14F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1528")

    ChrTalk(    #67
        0xFE,
        (
            "我还想去参观呢，\x01",
            "可是港口被封锁了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1603")

    label("loc_1528")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_155B")

    ChrTalk(    #68
        0xFE,
        (
            "不过你这个人……\x01",
            "竟然喝得下黑咖啡。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1603")

    label("loc_155B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_158A")

    ChrTalk(    #69
        0xFE,
        (
            "我们在旅行目的地\x01",
            "尽聊天了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1603")

    label("loc_158A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_15AF")

    ChrTalk(    #70
        0xFE,
        (
            "啊～哪里有\x01",
            "好男人呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1603")

    label("loc_15AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1603")

    ChrTalk(    #71
        0xFE,
        (
            "两位少女大白天就在露天\x01",
            "咖啡馆吃咖喱饭……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        "呵呵，真像是我们的作风。\x02",
    )

    CloseMessageWindow()

    label("loc_1603")

    TalkEnd(0xFE)
    Return()

    # Function_13_14E8 end

    def Function_14_1607(): pass

    label("Function_14_1607")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1614")
    Jump("loc_1737")

    label("loc_1614")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1641")

    ChrTalk(    #73
        0xFE,
        (
            "算了，也没办法。\x01",
            "这就叫命运。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1737")

    label("loc_1641")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1693")

    ChrTalk(    #74
        0xFE,
        (
            "只有咖啡才有像\x01",
            "人生一样的苦味……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "用牛奶和糖掩盖\x01",
            "是一种浪费。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1737")

    label("loc_1693")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16CC")

    ChrTalk(    #76
        0xFE,
        (
            "只要开心不就好了。\x01",
            "真像是我们的作风。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1737")

    label("loc_16CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_170B")

    ChrTalk(    #77
        0xFE,
        "好男人当然有。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "只不过我们\x01",
            "还没遇到而已……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1737")

    label("loc_170B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1737")

    ChrTalk(    #79
        0xFE,
        (
            "把自己说成是少女\x01",
            "真像你的作风。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1737")

    TalkEnd(0xFE)
    Return()

    # Function_14_1607 end

    def Function_15_173B(): pass

    label("Function_15_173B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1785")

    ChrTalk(    #80
        0xFE,
        "下水道可以自由进入。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "不过请尽量别在\x01",
            "里面惹出麻烦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_191E")

    label("loc_1785")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_17C9")

    ChrTalk(    #82
        0xFE,
        (
            "听说情报部\x01",
            "私藏了坦克。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "城里没受害\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_191E")

    label("loc_17C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1821")

    ChrTalk(    #84
        0xFE,
        (
            "城里的警戒工作终于\x01",
            "要动真格的了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "就连我也不经意地\x01",
            "变得警惕起来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_191E")

    label("loc_1821")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1866")

    ChrTalk(    #86
        0xFE,
        (
            "……快要到交接班的时间了。\x01",
            "这里的警戒工作真无聊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_191E")

    label("loc_1866")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_18C8")

    ChrTalk(    #87
        0xFE,
        (
            "也有人把这儿的下水\x01",
            "道当作训练场。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "不过现在只有负责剿灭\x01",
            "魔兽的游击士才能进去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_191E")

    label("loc_18C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_191E")

    ChrTalk(    #89
        0xFE,
        "哎呀，你们是游击士吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "进入下水道是可以，\x01",
            "不过里面很暗，你们要小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_191E")

    TalkEnd(0xFE)
    Return()

    # Function_15_173B end

    def Function_16_1922(): pass

    label("Function_16_1922")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #91
        (
            "\x07\x05　　 待售房\x01",
            "※可用于经营饮食店\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_16_1922 end

    def Function_17_1973(): pass

    label("Function_17_1973")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #92
        "\x07\x05门上着锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_17_1973 end

    def Function_18_19B9(): pass

    label("Function_18_19B9")

    SetPlaceName(0xB8)
    Return()

    # Function_18_19B9 end

    def Function_19_19BD(): pass

    label("Function_19_19BD")

    SetPlaceName(0xB7)
    Return()

    # Function_19_19BD end

    def Function_20_19C1(): pass

    label("Function_20_19C1")

    SetPlaceName(0xAF)
    Return()

    # Function_20_19C1 end

    SaveToFile()

Try(main)
