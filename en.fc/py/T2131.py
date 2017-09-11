from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2131   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2131.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T2131   ._SN',
            'ED6_DT01/T2131_1 ._SN',
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
        'Spiridon',                             # 9
        'Camera',                               # 10
        'Karl',                                 # 11
        'Duke Dunan',                           # 12
        'Butler Phillip',                       # 13
        'Nial',                                 # 14
        'Simon',                                # 15
        'Melvin',                               # 16
        'Primo',                                # 17
        'Hardt',                                # 18
        'Rutherford',                           # 19
        'Randall',                              # 20
        'Muriel',                               # 21
        'Seagaro',                              # 22
        'Edel',                                 # 23
        'Squaro',                               # 24
        'Zecalte',                              # 25
        'Pesca',                                # 26
        'Bolle',                                # 27
        'Jimmy',                                # 28
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
        'ED6_DT07/CH01270 ._CH',             # 00
        'ED6_DT07/CH01190 ._CH',             # 01
        'ED6_DT07/CH02140 ._CH',             # 02
        'ED6_DT07/CH02470 ._CH',             # 03
        'ED6_DT07/CH02060 ._CH',             # 04
        'ED6_DT07/CH01143 ._CH',             # 05
        'ED6_DT07/CH01760 ._CH',             # 06
        'ED6_DT07/CH01560 ._CH',             # 07
        'ED6_DT07/CH01570 ._CH',             # 08
        'ED6_DT07/CH01210 ._CH',             # 09
        'ED6_DT07/CH01023 ._CH',             # 0A
        'ED6_DT07/CH01123 ._CH',             # 0B
        'ED6_DT07/CH01020 ._CH',             # 0C
        'ED6_DT07/CH01000 ._CH',             # 0D
        'ED6_DT07/CH01050 ._CH',             # 0E
        'ED6_DT07/CH01043 ._CH',             # 0F
        'ED6_DT07/CH01213 ._CH',             # 10
        'ED6_DT07/CH01443 ._CH',             # 11
        'ED6_DT07/CH01460 ._CH',             # 12
        'ED6_DT07/CH01123 ._CH',             # 13
        'ED6_DT07/CH01023 ._CH',             # 14
        'ED6_DT07/CH01003 ._CH',             # 15
        'ED6_DT07/CH01053 ._CH',             # 16
    )

    AddCharChipPat(
        'ED6_DT07/CH01270P._CP',             # 00
        'ED6_DT07/CH01190P._CP',             # 01
        'ED6_DT07/CH02140P._CP',             # 02
        'ED6_DT07/CH02470P._CP',             # 03
        'ED6_DT07/CH02060P._CP',             # 04
        'ED6_DT07/CH01143P._CP',             # 05
        'ED6_DT07/CH01760P._CP',             # 06
        'ED6_DT07/CH01560P._CP',             # 07
        'ED6_DT07/CH01570P._CP',             # 08
        'ED6_DT07/CH01210P._CP',             # 09
        'ED6_DT07/CH01023P._CP',             # 0A
        'ED6_DT07/CH01123P._CP',             # 0B
        'ED6_DT07/CH01020P._CP',             # 0C
        'ED6_DT07/CH01000P._CP',             # 0D
        'ED6_DT07/CH01050P._CP',             # 0E
        'ED6_DT07/CH01043P._CP',             # 0F
        'ED6_DT07/CH01213P._CP',             # 10
        'ED6_DT07/CH01443P._CP',             # 11
        'ED6_DT07/CH01460P._CP',             # 12
        'ED6_DT07/CH01123P._CP',             # 13
        'ED6_DT07/CH01023P._CP',             # 14
        'ED6_DT07/CH01003P._CP',             # 15
        'ED6_DT07/CH01053P._CP',             # 16
    )

    DeclNpc(
        X                   = 24640,
        Z                   = 0,
        Y                   = 27000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
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
        X                   = 500,
        Z                   = 0,
        Y                   = 2200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 32400,
        Z                   = 0,
        Y                   = 28200,
        Direction           = 90,
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
        X                   = 31600,
        Z                   = 0,
        Y                   = 29700,
        Direction           = 145,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -3500,
        Z                   = 300,
        Y                   = 34200,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 7000,
        Z                   = 300,
        Y                   = 29100,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -3490,
        Z                   = 250,
        Y                   = 32049,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -5500,
        Z                   = 300,
        Y                   = 33800,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 2900,
        Z                   = 300,
        Y                   = 26900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 2900,
        Z                   = 300,
        Y                   = 29150,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 29260,
        Z                   = 400,
        Y                   = 30200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 27050,
        Z                   = 400,
        Y                   = 30200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = -6400,
        Z                   = 300,
        Y                   = 27200,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = -4000,
        Z                   = 300,
        Y                   = 27200,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = -2940,
        Z                   = 0,
        Y                   = 5590,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -21740,
        Z                   = 200,
        Y                   = 1670,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -1940,
        Z                   = 0,
        Y                   = 1220,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -17720,
        Z                   = 250,
        Y                   = -840,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 6870,
        Z                   = 250,
        Y                   = 29240,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )


    DeclActor(
        TriggerX            = 25600,
        TriggerZ            = 0,
        TriggerY            = 28000,
        TriggerRange        = 1400,
        ActorX              = 24920,
        ActorZ              = 1000,
        ActorY              = 28100,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -4000,
        TriggerZ            = 250,
        TriggerY            = 33700,
        TriggerRange        = 400,
        ActorX              = -5500,
        ActorZ              = 1800,
        ActorY              = 33800,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -23760,
        TriggerZ            = 0,
        TriggerY            = 6340,
        TriggerRange        = 1400,
        ActorX              = -23760,
        ActorZ              = 1500,
        ActorY              = 6340,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 1,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 28730,
        TriggerZ            = 0,
        TriggerY            = 37220,
        TriggerRange        = 800,
        ActorX              = 28730,
        ActorZ              = 1800,
        ActorY              = 37220,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 24,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_472",          # 00, 0
        "Function_1_62E",          # 01, 1
        "Function_2_6CF",          # 02, 2
        "Function_3_6E5",          # 03, 3
        "Function_4_182C",         # 04, 4
        "Function_5_190C",         # 05, 5
        "Function_6_1F5C",         # 06, 6
        "Function_7_24B9",         # 07, 7
        "Function_8_2AE7",         # 08, 8
        "Function_9_2B7F",         # 09, 9
        "Function_10_2C47",        # 0A, 10
        "Function_11_2D9C",        # 0B, 11
        "Function_12_2F64",        # 0C, 12
        "Function_13_31D7",        # 0D, 13
        "Function_14_3850",        # 0E, 14
        "Function_15_3855",        # 0F, 15
        "Function_16_4835",        # 10, 16
        "Function_17_51A1",        # 11, 17
        "Function_18_5454",        # 12, 18
        "Function_19_54EC",        # 13, 19
        "Function_20_550D",        # 14, 20
        "Function_21_552E",        # 15, 21
        "Function_22_5597",        # 16, 22
        "Function_23_564A",        # 17, 23
        "Function_24_5722",        # 18, 24
    )


    def Function_0_472(): pass

    label("Function_0_472")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4B9")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    SetChrPos(0x8, 29470, 0, 32220, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A7")
    Jump("loc_4B6")

    label("loc_4A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4B6")
    ClearChrFlags(0x1B, 0x80)

    label("loc_4B6")

    Jump("loc_62D")

    label("loc_4B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_500")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    SetChrPos(0x8, 29470, 0, 32220, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EE")
    Jump("loc_4FD")

    label("loc_4EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4FD")
    ClearChrFlags(0x1B, 0x80)

    label("loc_4FD")

    Jump("loc_62D")

    label("loc_500")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_54C")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    SetChrPos(0x8, 29470, 0, 32220, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53A")
    Jump("loc_549")

    label("loc_53A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_549")
    ClearChrFlags(0x1B, 0x80)

    label("loc_549")

    Jump("loc_62D")

    label("loc_54C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_574")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_571")
    ClearChrFlags(0x1B, 0x80)

    label("loc_571")

    Jump("loc_62D")

    label("loc_574")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_5A3")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x8, 29470, 0, 32220, 180)
    Jump("loc_62D")

    label("loc_5A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_5CD")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    SetChrPos(0x8, 29470, 0, 32220, 180)
    Jump("loc_62D")

    label("loc_5CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_5FC")
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x8, 29470, 0, 32220, 180)
    Jump("loc_62D")

    label("loc_5FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_610")
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    Jump("loc_62D")

    label("loc_610")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_62D")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x8, 29470, 0, 32220, 180)

    label("loc_62D")

    Return()

    # Function_0_472 end

    def Function_1_62E(): pass

    label("Function_1_62E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_64F")
    OP_B1("t2131_y")
    Jump("loc_658")

    label("loc_64F")

    OP_B1("t2131_n")

    label("loc_658")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x8)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_677")
    OP_64(0x0, 0x1)

    label("loc_677")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_681")
    Jump("loc_6CE")

    label("loc_681")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_68B")
    Jump("loc_6CE")

    label("loc_68B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_695")
    Jump("loc_6CE")

    label("loc_695")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_69F")
    Jump("loc_6CE")

    label("loc_69F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_6A9")
    Jump("loc_6CE")

    label("loc_6A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_6B3")
    Jump("loc_6CE")

    label("loc_6B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_6BD")
    Jump("loc_6CE")

    label("loc_6BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_6C7")
    Jump("loc_6CE")

    label("loc_6C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_6CE")

    label("loc_6CE")

    Return()

    # Function_1_62E end

    def Function_2_6CF(): pass

    label("Function_2_6CF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6E4")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_6CF")

    label("loc_6E4")

    Return()

    # Function_2_6CF end

    def Function_3_6E5(): pass

    label("Function_3_6E5")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x332)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x1, 0x800)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9B8")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                                 # 0
            "Shop\x01",                                 # 1
            "[Salubrious Oatmeal] - 500 mira\x01",      # 2
            "Return fishing rod\x01",                   # 3
            "Leave\x01",                                # 4
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_788")
    OP_0D()
    OP_A9(0x24)
    OP_56(0x0)
    TalkEnd(0x17)
    Return()

    label("loc_788")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89C")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_862")
    SubMira(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #0
        "\x06\x07\x00Ate \x07\x02Salubrious Oatmeal\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x2EE)
    OP_31(0x1, 0xFD, 0x2EE)
    OP_31(0x2, 0xFD, 0x2EE)
    OP_31(0x3, 0xFD, 0x2EE)
    OP_31(0x4, 0xFD, 0x2EE)
    OP_31(0x5, 0xFD, 0x2EE)
    OP_31(0x6, 0xFD, 0x2EE)
    OP_31(0x7, 0xFD, 0x2EE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_854")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x6)"), scpexpr(EXPR_END)), "loc_820")
    Jump("loc_854")

    label("loc_820")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #1
        "\x06\x07\x00Learned '\x07\x02Salubrious Oatmeal\x07\x00' recipe.\x02",
    )

    CloseMessageWindow()

    label("loc_854")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_88A")

    label("loc_862")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #2
        "Insufficient mira.\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_88A")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x17)
    Return()

    label("loc_89C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A4")
    OP_3F(0x332, 1)
    Sleep(400)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #3
        "\x07\x00Returned \x07\x02Progressive Rod\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #4
        0xFE,
        (
            "Ah, thank you. So, did the Goddess\x01",
            "smile upon your rod today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "Just let me know if you get\x01",
            "hungry. I'll cook you the\x01",
            "best meal you've ever had.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x17)
    Return()

    label("loc_9A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9B5")
    TalkEnd(0x17)
    Return()

    label("loc_9B5")

    Jump("loc_DE4")

    label("loc_9B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x332)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x1, 0x800)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C42")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                                 # 0
            "Shop\x01",                                 # 1
            "[Salubrious Oatmeal] - 500 mira\x01",      # 2
            "Borrow fishing rod\x01",                   # 3
            "Leave\x01",                                # 4
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A62")
    OP_0D()
    OP_A9(0x24)
    OP_56(0x0)
    TalkEnd(0x17)
    Return()

    label("loc_A62")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B76")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B3C")
    SubMira(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #6
        "\x06\x07\x00Ate \x07\x02Salubrious Oatmeal\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x2EE)
    OP_31(0x1, 0xFD, 0x2EE)
    OP_31(0x2, 0xFD, 0x2EE)
    OP_31(0x3, 0xFD, 0x2EE)
    OP_31(0x4, 0xFD, 0x2EE)
    OP_31(0x5, 0xFD, 0x2EE)
    OP_31(0x6, 0xFD, 0x2EE)
    OP_31(0x7, 0xFD, 0x2EE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B2E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x6)"), scpexpr(EXPR_END)), "loc_AFA")
    Jump("loc_B2E")

    label("loc_AFA")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #7
        "\x06\x07\x00Learned '\x07\x02Salubrious Oatmeal\x07\x00' recipe.\x02",
    )

    CloseMessageWindow()

    label("loc_B2E")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_B64")

    label("loc_B3C")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #8
        "Insufficient mira.\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_B64")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x17)
    Return()

    label("loc_B76")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C2E")

    ChrTalk(    #9
        0xFE,
        "Ah, going fishing are you?\x02",
    )

    CloseMessageWindow()
    OP_3E(0x332, 1)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #10
        "\x07\x00Borrowed \x07\x02Progressive Rod\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #11
        0xFE,
        (
            "Just bring it back whenever\x01",
            "you're done.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x17)
    Return()

    label("loc_C2E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C3F")
    TalkEnd(0x17)
    Return()

    label("loc_C3F")

    Jump("loc_DE4")

    label("loc_C42")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Talk\x01",                                 # 0
            "Shop\x01",                                 # 1
            "[Salubrious Oatmeal] - 500 mira\x01",      # 2
            "Leave\x01",                                # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CBF")
    OP_0D()
    OP_A9(0x24)
    OP_56(0x0)
    TalkEnd(0x17)
    Return()

    label("loc_CBF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DD3")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D99")
    SubMira(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #12
        "\x06\x07\x00Ate \x07\x02Salubrious Oatmeal\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x2EE)
    OP_31(0x1, 0xFD, 0x2EE)
    OP_31(0x2, 0xFD, 0x2EE)
    OP_31(0x3, 0xFD, 0x2EE)
    OP_31(0x4, 0xFD, 0x2EE)
    OP_31(0x5, 0xFD, 0x2EE)
    OP_31(0x6, 0xFD, 0x2EE)
    OP_31(0x7, 0xFD, 0x2EE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D8B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x6)"), scpexpr(EXPR_END)), "loc_D57")
    Jump("loc_D8B")

    label("loc_D57")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #13
        "\x06\x07\x00Learned '\x07\x02Salubrious Oatmeal\x07\x00' recipe.\x02",
    )

    CloseMessageWindow()

    label("loc_D8B")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_DC1")

    label("loc_D99")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #14
        "Insufficient mira.\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_DC1")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x17)
    Return()

    label("loc_DD3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DE4")
    TalkEnd(0x17)
    Return()

    label("loc_DE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x1, 0x1000)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x1, 0x800)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1050")
    OP_28(0x21, 0x1, 0x800)

    ChrTalk(    #15
        0xFE,
        "Hello! Welcome, welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#000FHey, we saw you had some fishing\x01",
            "rods upstairs... Would you mind\x01",
            "if we borrowed one?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        "Oh, not at all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "Just say the word, and you're\x01",
            "welcome to borrow it any time.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "[Borrow fishing rod]\x01",        # 0
            "[On second thought...]\x01",      # 1
        )
    )

    MenuEnd(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FEC")
    OP_0D()
    OP_3E(0x332, 1)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #19
        "\x07\x00Borrowed \x07\x02Progressive Rod\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #20
        0xFE,
        (
            "Just bring it back whenever\x01",
            "you're done.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x17)
    Return()

    label("loc_FEC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_104D")

    ChrTalk(    #21
        0xFE,
        "Just holler if you need me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "I'll be happy to lend you my\x01",
            "fishing rod.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x17)
    Return()

    label("loc_104D")

    Jump("loc_1828")

    label("loc_1050")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_11DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_112C")
    OP_A2(0x9)

    ChrTalk(    #23
        0xFE,
        "The mayor, arrested...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "Don't care how much money you've got\x01",
            "or who you are...if you start attacking\x01",
            "orphans, you're scum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "It's a nasty enough story to\x01",
            "shock the foulest of scoundrels.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11D9")

    label("loc_112C")


    ChrTalk(    #26
        0xFE,
        (
            "If I had my druthers, come next\x01",
            "election, I'd pick Portos as the\x01",
            "new mayor, myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "Bet your last mira that he's\x01",
            "the sort who'd always put\x01",
            "the good of Ruan first.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11D9")

    Jump("loc_1828")

    label("loc_11DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1310")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_128E")
    OP_A2(0x9)

    ChrTalk(    #28
        0xFE,
        (
            "The mayor gave the order to\x01",
            "stop all work at the port.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "If Chief Portos can't talk him\x01",
            "out of this, we're in trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "Ruan still needs a port!\x02",
    )

    CloseMessageWindow()
    Jump("loc_130D")

    label("loc_128E")


    ChrTalk(    #31
        0xFE,
        (
            "The mayor gave the order to\x01",
            "stop all work at the port.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "If Chief Portos can't talk him\x01",
            "out of this, we're in trouble.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_130D")

    Jump("loc_1828")

    label("loc_1310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_13DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13A3")
    OP_A2(0x9)

    ChrTalk(    #33
        0xFE,
        (
            "Some redheaded bracer came by\x01",
            "a while ago, looking for information...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "Hmm...you know, he looked\x01",
            "kind of familiar...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13D9")

    label("loc_13A3")


    ChrTalk(    #35
        0xFE,
        (
            "That redheaded bracer looked\x01",
            "kind of familiar...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13D9")

    Jump("loc_1828")

    label("loc_13DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1597")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1504")
    OP_A2(0x9)

    ChrTalk(    #36
        0xFE,
        (
            "The Ravens like to come to\x01",
            "this shop, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "They sure don't act all rough\x01",
            "and mean like they used to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "If they don't have any self-\x01",
            "confidence anymore, they'll\x01",
            "probably just drift apart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "Before, it was obvious how\x01",
            "nasty they were, just by the\x01",
            "looks of 'em.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1594")

    label("loc_1504")


    ChrTalk(    #40
        0xFE,
        (
            "The Ravens sure don't act\x01",
            "all rough and mean like\x01",
            "they used to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "Before, it was obvious how\x01",
            "nasty they were, just by the\x01",
            "looks of 'em.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1594")

    Jump("loc_1828")

    label("loc_1597")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_174E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_168D")
    OP_A2(0x9)

    ChrTalk(    #42
        0xFE,
        "I've always been a fisherman.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "All of the fish in my store are\x01",
            "caught fresh by me. I take a\x01",
            "boat out early in the mornings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "I'm not generally one to boast,\x01",
            "but you won't find fresher fish\x01",
            "anywhere else in Ruan.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_174B")

    label("loc_168D")


    ChrTalk(    #45
        0xFE,
        (
            "All of the fish in my store are\x01",
            "caught fresh by me. I take a\x01",
            "boat out early in the mornings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "I'm not generally one to boast,\x01",
            "but you won't find fresher fish\x01",
            "anywhere else in Ruan.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_174B")

    Jump("loc_1828")

    label("loc_174E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_1828")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17FD")
    OP_A2(0x9)

    ChrTalk(    #47
        0xFE,
        (
            "Hey there!\x01",
            "Welcome to the Aqua Rossa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "I mostly see fishermen and sailors\x01",
            "in here, but I'm always glad for new\x01",
            "customers, whoever they might be.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1828")

    label("loc_17FD")


    ChrTalk(    #49
        0xFE,
        (
            "Hey there!\x01",
            "Welcome to the Aqua Rossa.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1828")

    TalkEnd(0x17)
    Return()

    # Function_3_6E5 end

    def Function_4_182C(): pass

    label("Function_4_182C")

    TalkBegin(0xA)

    ChrTalk(    #50
        0xFE,
        (
            "Since airship transit got suspended\x01",
            "right as I was about to leave, I had\x01",
            "to walk here from Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "*sigh* Let me tell you,\x01",
            "that's no gentle massage\x01",
            "on the feet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "But, hey...it could have been\x01",
            "much worse.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Return()

    # Function_4_182C end

    def Function_5_190C(): pass

    label("Function_5_190C")

    TalkBegin(0x18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_19AD")

    ChrTalk(    #53
        0xFE,
        (
            "I'll be off at sea, so I won't get\x01",
            "a chance to vote.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "But whoever the next mayor is,\x01",
            "I hope he'll keep the dock hands\x01",
            "and sailors in mind.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F58")

    label("loc_19AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1B4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AAC")
    OP_A2(0xA)

    ChrTalk(    #55
        0xFE,
        (
            "The next voyage is supposed to\x01",
            "be a shipment of orbment goods\x01",
            "to the Erebonian Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "The port there is crowded with\x01",
            "military ships. Makes it hard\x01",
            "to concentrate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "Even now, I still get tense when\x01",
            "I have to dock there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B49")

    label("loc_1AAC")


    ChrTalk(    #58
        0xFE,
        (
            "I'm slated to deliver a bunch of\x01",
            "orbment goods to Erebonia next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "The port there is crammed to the\x01",
            "gills with battleships. Not good\x01",
            "for the nerves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B49")

    Jump("loc_1F58")

    label("loc_1B4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1C8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C1E")
    OP_A2(0xA)

    ChrTalk(    #60
        0xFE,
        (
            "Even on my days off, I'm still\x01",
            "transporting cargo back and\x01",
            "forth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "I guess it's just the sailor\x01",
            "in me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "But I have no urge to give\x01",
            "it up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        "I'm proud of the work that I do.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C8C")

    label("loc_1C1E")


    ChrTalk(    #64
        0xFE,
        (
            "Even on my days off, I'm still\x01",
            "transporting cargo back and\x01",
            "forth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        "But I have no urge to give it up.\x02",
    )

    CloseMessageWindow()

    label("loc_1C8C")

    Jump("loc_1F58")

    label("loc_1C8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1DFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D67")
    OP_A2(0xA)

    ChrTalk(    #66
        0xFE,
        (
            "I saw a little kid running in the\x01",
            "direction of the warehouse earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "I can't imagine what he'd\x01",
            "be doing here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "I hope he's not involved with\x01",
            "those little punks who hang\x01",
            "out there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DFC")

    label("loc_1D67")


    ChrTalk(    #69
        0xFE,
        (
            "I saw a little kid running in the\x01",
            "direction of the warehouse earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "I hope he's not involved with\x01",
            "those little punks who hang\x01",
            "out there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DFC")

    Jump("loc_1F58")

    label("loc_1DFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_1EA3")

    ChrTalk(    #71
        0xFE,
        (
            "I'm the navigation officer on\x01",
            "a merchant vessel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "I may be a little drunk right now,\x01",
            "but I'm at sea for months at a\x01",
            "time...I'm allowed, damn it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F58")

    label("loc_1EA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_1F58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F32")
    OP_A2(0xA)

    ChrTalk(    #73
        0xFE,
        "*hic*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "I just got back from the Calvard\x01",
            "Republic, some time ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "Ain't seen that place in a\x01",
            "loooong time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F58")

    label("loc_1F32")


    ChrTalk(    #76
        0xFE,
        "Hey, old man! Gimme another one!\x02",
    )

    CloseMessageWindow()

    label("loc_1F58")

    TalkEnd(0x18)
    Return()

    # Function_5_190C end

    def Function_6_1F5C(): pass

    label("Function_6_1F5C")

    TalkBegin(0x19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1FD5")

    ChrTalk(    #77
        0xFE,
        "Was the mayor really arrested?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "I don't know the whole story,\x01",
            "but it must've been something\x01",
            "major.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24B5")

    label("loc_1FD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_206F")

    ChrTalk(    #79
        0xFE,
        (
            "I did notice that the lighthouse\x01",
            "was lit until this morning.\x01",
            "What happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "I doubt that old Vogt was\x01",
            "nodding off, like I usually do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24B5")

    label("loc_206F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_20DB")

    ChrTalk(    #81
        0xFE,
        "Phew...got a nice haul, today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "The fish are always biting in\x01",
            "this one spot. It's great.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24B5")

    label("loc_20DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2207")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_219F")
    OP_A2(0xB)

    ChrTalk(    #83
        0xFE,
        (
            "I don't understand why the mayor\x01",
            "doesn't do something about those\x01",
            "delinquents in the warehouse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "Oh, well. I'm just a fisherman.\x01",
            "I don't want anything to do\x01",
            "with it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2204")

    label("loc_219F")


    ChrTalk(    #85
        0xFE,
        (
            "I don't understand why the mayor\x01",
            "doesn't do something about those\x01",
            "delinquents in the warehouse.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2204")

    Jump("loc_24B5")

    label("loc_2207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_2347")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22BF")
    OP_A2(0xB)

    ChrTalk(    #86
        0xFE,
        (
            "The seafood from Azelia Bay\x01",
            "is the best you'll ever have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        "Oh, right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "Today, I'd recommend the fish\x01",
            "that's pan-seared in wine and\x01",
            "topped with roe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2344")

    label("loc_22BF")


    ChrTalk(    #89
        0xFE,
        (
            "All the seafood from Azelia Bay\x01",
            "is delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "Today, I'd recommend the fish\x01",
            "that's pan-seared in wine and\x01",
            "topped with roe.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2344")

    Jump("loc_24B5")

    label("loc_2347")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_24B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_242C")
    OP_A2(0xB)

    ChrTalk(    #91
        0xFE,
        (
            "A lot of my fellow fishermen have\x01",
            "just given up the trade lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "Me, I don't see how I could\x01",
            "ever do anything else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "I think that as long as people\x01",
            "keep wanting to eat fish, I'll\x01",
            "keep fishing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24B5")

    label("loc_242C")


    ChrTalk(    #94
        0xFE,
        (
            "Me, I don't see how I could\x01",
            "ever do anything else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "I think that as long as people\x01",
            "keep wanting to eat fish, I'll\x01",
            "keep fishing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24B5")

    TalkEnd(0x19)
    Return()

    # Function_6_1F5C end

    def Function_7_24B9(): pass

    label("Function_7_24B9")

    TalkBegin(0x1A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2527")

    ChrTalk(    #96
        0xFE,
        (
            "The guys in the north block want\x01",
            "Norman to be the new mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        "We'd rather it be Portos.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AE3")

    label("loc_2527")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_25B2")

    ChrTalk(    #98
        0xFE,
        (
            "Way back when, the port had\x01",
            "better government funding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "It's been pretty tough lately,\x01",
            "but Chief Portos never gives up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AE3")

    label("loc_25B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_26F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26AF")
    OP_A2(0xC)

    ChrTalk(    #100
        0xFE,
        (
            "Back in the Hundred Days War,\x01",
            "Ruan was a major strategic asset.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "Break through here and\x01",
            "you'd have no opposition\x01",
            "until Valleria Lake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "But that's where Fort Leiston\x01",
            "is, and nothing's getting\x01",
            "through the defenses there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26F3")

    label("loc_26AF")


    ChrTalk(    #103
        0xFE,
        (
            "Back in the Hundred Days War\x01",
            "Ruan was a major strategic asset.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26F3")

    Jump("loc_2AE3")

    label("loc_26F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_28C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2813")
    OP_A2(0xC)

    ChrTalk(    #104
        0xFE,
        (
            "The Roubine River that runs through\x01",
            "this town leads to Valleria Lake,\x01",
            "dead center of Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "Any foreign goods that we\x01",
            "unload can be shipped\x01",
            "directly on to Grancel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "Used to be, you'd see tons of\x01",
            "people from all kinds of foreign\x01",
            "nations around here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28C2")

    label("loc_2813")


    ChrTalk(    #107
        0xFE,
        (
            "The Roubine River that runs through\x01",
            "this town leads to Valleria Lake,\x01",
            "dead center of Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "Any foreign goods that we\x01",
            "unload can be shipped\x01",
            "directly on to Grancel.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28C2")

    Jump("loc_2AE3")

    label("loc_28C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_2985")

    ChrTalk(    #109
        0xFE,
        (
            "If you're looking to make money,\x01",
            "the tourism industry is a safer\x01",
            "bet than fishing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "But the folks on this side o' the\x01",
            "river? We'd never be able to handle\x01",
            "that line o' work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AE3")

    label("loc_2985")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_2AE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A5D")
    OP_A2(0xC)

    ChrTalk(    #111
        0xFE,
        (
            "Ahh, there's nothing like a\x01",
            "drink after you've set off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "This town used to be full\x01",
            "of nothing but sailors\x01",
            "and fishermen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "Nowadays, though, it's more\x01",
            "landlubbers than anything else.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AE3")

    label("loc_2A5D")


    ChrTalk(    #114
        0xFE,
        (
            "This town used to be full\x01",
            "of nothing but sailors\x01",
            "and fishermen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "Nowadays, though, it's more\x01",
            "landlubbers than anything else.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AE3")

    TalkEnd(0x1A)
    Return()

    # Function_7_24B9 end

    def Function_8_2AE7(): pass

    label("Function_8_2AE7")

    TalkBegin(0xB)

    ChrTalk(    #116
        0xFE,
        (
            "#226FHow shameful it is that the future\x01",
            "king should fall prey to a mere\x01",
            "commoner...and a WOMAN besides!\x02\x03",

            "#224FEnough of this! One more try!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Return()

    # Function_8_2AE7 end

    def Function_9_2B7F(): pass

    label("Function_9_2B7F")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BFE")
    OP_A2(0x2)

    ChrTalk(    #117
        0xFE,
        (
            "#720FBut, Your Grace...\x02\x03",

            "The evening deepens...perhaps\x01",
            "we should retire to the inn for\x01",
            "the night...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x10)
    Jump("loc_2C43")

    label("loc_2BFE")


    ChrTalk(    #118
        0xFE,
        (
            "#722F*sigh* I know that talking to\x01",
            "him does no good, and yet...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C43")

    TalkEnd(0xC)
    Return()

    # Function_9_2B7F end

    def Function_10_2C47(): pass

    label("Function_10_2C47")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_2D28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CF2")
    OP_A2(0x3)

    ChrTalk(    #119
        0xFE,
        (
            "#141FHeh heh...and this means I've\x01",
            "got all the info I need.\x02\x03",

            "This could be the scoop of\x01",
            "a lifetime.\x02\x03",

            "#142FNow I just need to get\x01",
            "solid proof.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D25")

    label("loc_2CF2")


    ChrTalk(    #120
        0xFE,
        (
            "#141FThis could be the scoop of\x01",
            "a lifetime...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D25")

    Jump("loc_2D98")

    label("loc_2D28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2D98")

    ChrTalk(    #121
        0xFE,
        (
            "#141FHey there, bracers.\x02\x03",

            "If you turn up anything interesting,\x01",
            "you be sure to tell me all about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D98")

    TalkEnd(0xD)
    Return()

    # Function_10_2C47 end

    def Function_11_2D9C(): pass

    label("Function_11_2D9C")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_2E62")

    ChrTalk(    #122
        0xFE,
        (
            "The strategy behind gambling\x01",
            "is a lot like dealing with\x01",
            "business transactions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "If it's just for fun, there's no\x01",
            "pressure and you run into the\x01",
            "possibility of getting addicted.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F60")

    label("loc_2E62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2F60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F10")
    OP_A2(0x4)

    ChrTalk(    #124
        0xFE,
        (
            "Whew...okay, now that the\x01",
            "negotiations are behind me,\x01",
            "I can breathe again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "Ms. Mirano is off on a business\x01",
            "trip, and there's a lot to be done.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F60")

    label("loc_2F10")


    ChrTalk(    #126
        0xFE,
        (
            "Whew...okay, now that the\x01",
            "negotiations are behind me,\x01",
            "I can breathe again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F60")

    TalkEnd(0xE)
    Return()

    # Function_11_2D9C end

    def Function_12_2F64(): pass

    label("Function_12_2F64")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_3013")

    ChrTalk(    #127
        0xFE,
        (
            "Agate is just incredible...\x01",
            "What do you think his secret is?\x01",
            "The sword? The hair? The bandanna?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "But it looks like Liberl has\x01",
            "even more amazing people.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31D3")

    label("loc_3013")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_3118")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30B1")
    OP_A2(0x5)

    ChrTalk(    #129
        0xFE,
        "Hah...AHHHH...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        "HAH-CHOOOOOO!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        "Brrrrr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "I was always taught that you're\x01",
            "supposed to eat a lot when\x01",
            "you've got a cold.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3115")

    label("loc_30B1")


    ChrTalk(    #133
        0xFE,
        "Ah-CHOOO!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "Gotta eat and keep up my\x01",
            "strength to work as a bracer,\x01",
            "in case of an emergency!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3115")

    Jump("loc_31D3")

    label("loc_3118")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_31D3")

    ChrTalk(    #135
        0xFE,
        (
            "Not too long ago, I ran into\x01",
            "this really fast monster on\x01",
            "the beach!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "When I tried to kill it, I actually\x01",
            "broke my sword on its hide!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        "It may be small, but it's tough!\x02",
    )

    CloseMessageWindow()

    label("loc_31D3")

    TalkEnd(0xF)
    Return()

    # Function_12_2F64 end

    def Function_13_31D7(): pass

    label("Function_13_31D7")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_329F")

    ChrTalk(    #138
        0xFE,
        (
            "Hard to believe that the mayor's\x01",
            "been arrested...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "I suppose that means we'll\x01",
            "be electing a new mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "I'll be extremely interested in\x01",
            "seeing who decides to run\x01",
            "for office.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_384C")

    label("loc_329F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_3379")

    ChrTalk(    #141
        0x8,
        (
            "The mayor's helped out the\x01",
            "tourism industry a lot...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x8,
        (
            "But the budget for the port\x01",
            "facilities has been gradually\x01",
            "cut every year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x8,
        (
            "The folks who aren't happy about\x01",
            "that are getting more insistent.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_384C")

    label("loc_3379")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_33D7")

    ChrTalk(    #144
        0x8,
        (
            "The renovations are gradually\x01",
            "coming along.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x8,
        "I look forward to re-opening.\x02",
    )

    CloseMessageWindow()
    Jump("loc_384C")

    label("loc_33D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_3485")

    ChrTalk(    #146
        0x8,
        (
            "The roulette wheel doesn't\x01",
            "spin as freely anymore, and\x01",
            "that simply won't do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x8,
        (
            "The most important thing is\x01",
            "making sure that the customers\x01",
            "enjoy themselves.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_384C")

    label("loc_3485")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_3508")

    ChrTalk(    #148
        0x8,
        (
            "I want to replace the roulette\x01",
            "wheel while the renovations\x01",
            "are going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x8,
        "I'm trying to draw in more customers.\x02",
    )

    CloseMessageWindow()
    Jump("loc_384C")

    label("loc_3508")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_36C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_361F")
    OP_A2(0x6)

    ChrTalk(    #150
        0x8,
        (
            "Once the tourist season starts\x01",
            "up, I want to pull in customers\x01",
            "from all walks of life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x8,
        (
            "Since tourism is getting so\x01",
            "popular, it's resulted in more\x01",
            "customers for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x8,
        (
            "I want to get the remodeling\x01",
            "done as soon as possible,\x01",
            "so we'll be busy again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36C5")

    label("loc_361F")


    ChrTalk(    #153
        0x8,
        (
            "Since tourism is getting so\x01",
            "popular, it's resulted in more\x01",
            "customers for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x8,
        (
            "I want to get the remodeling\x01",
            "done as soon as possible,\x01",
            "so we'll be busy again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36C5")

    Jump("loc_384C")

    label("loc_36C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_378E")

    ChrTalk(    #155
        0x8,
        "Life is like a roulette table.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x8,
        (
            "You might get a lucky streak\x01",
            "one day, only for it all to fall\x01",
            "apart tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x8,
        (
            "That's why you should enjoy\x01",
            "the good times while you\x01",
            "have them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_384C")

    label("loc_378E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_384C")

    ChrTalk(    #158
        0x8,
        (
            "I'm planning for the grand re-opening of\x01",
            "the Lavantar Casino & Bar to coincide\x01",
            "with the queen's birthday festivities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x8,
        (
            "Right now, the entire second\x01",
            "floor is being remodeled.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_384C")

    TalkEnd(0x8)
    Return()

    # Function_13_31D7 end

    def Function_14_3850(): pass

    label("Function_14_3850")

    Call(0, 15)
    Return()

    # Function_14_3850 end

    def Function_15_3855(): pass

    label("Function_15_3855")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40FE")
    EventBegin(0x0)
    OP_4A(0x10, 255)

    ChrTalk(    #160
        0x10,
        "Hey! Good to see you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x10,
        "...Hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x10,
        (
            "Hey, aren't you going to the\x01",
            "Varenne Lighthouse?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_394F")

    ChrTalk(    #163
        0x101,
        (
            "#000FThat's right.\x02\x03",

            "We have to deliver something to\x01",
            "Mr. Vogt, the lighthouse keeper.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 0)
    Jump("loc_3A4A")

    label("loc_394F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39C6")

    ChrTalk(    #164
        0x102,
        (
            "#010FYes, that's correct.\x02\x03",

            "We have to deliver something to\x01",
            "Mr. Vogt, the lighthouse keeper.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x102, 0)
    Jump("loc_3A4A")

    label("loc_39C6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A4A")

    ChrTalk(    #165
        0x105,
        (
            "#040FOh...yes.\x02\x03",

            "But I'm just helping out...\x02\x03",

            "We're delivering something to\x01",
            "Mr. Vogt, the lighthouse keeper.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x105, 0)

    label("loc_3A4A")


    ChrTalk(    #166
        0x10,
        (
            "Is that so? I figured as much,\x01",
            "from the look of that bag.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x10,
        (
            "The old man went to the\x01",
            "lighthouse a long time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x10,
        "I guess he's still doing okay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x101,
        (
            "#000FHe used to come in here\x01",
            "a lot, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(    #170
        0x10,
        (
            "He's a fisherman. He loves his\x01",
            "drink and he loves to gamble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x10,
        (
            "He especially loves a good\x01",
            "Azelia Rose, which is a \x01",
            "cocktail made with fruit juice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x10,
        "He's missed around this place...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x10,
        (
            "We'd love to see him again,\x01",
            "but he never comes down to\x01",
            "have a drink.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x10,
        "It's a rough job he has.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x101,
        "#003FYeah...sounds like it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x10,
        "Oh, right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x10,
        (
            "So, if it's no trouble, would you\x01",
            "mind bringing him one?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x101,
        "#004FOne what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x10,
        (
            "Why, one of those cocktails,\x01",
            "seeing as you're heading to\x01",
            "the lighthouse an' all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x10,
        (
            "I'm not making a formal request or anything.\x01",
            "If it gets to be a pain to carry, you can\x01",
            "just dump it out on the way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x101,
        (
            "#006FSo, basically just dropping off\x01",
            "supplies, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #182
        0x101,
        "#006FWould you mind, Joshua?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #183
        0x102,
        "#010FNo, I don't see it being an issue.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_3E90")
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #184
        0x101,
        "#505FYou're such a gentleman.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #185
        0x105,
        "#041FHa ha...indeed, he is.\x02",
    )

    CloseMessageWindow()

    label("loc_3E90")


    ChrTalk(    #186
        0x10,
        (
            "Great! Just take it to the\x01",
            "old man.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3EBF():
        TurnDirection(0x101, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3EBF)

    def lambda_3ECD():
        TurnDirection(0x102, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3ECD)

    def lambda_3EDB():
        TurnDirection(0x105, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3EDB)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0x105, 0x1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #187
        "\x07\x00Received '\x07\x02Azelia Rose\x07\x00'.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x1D, 0x1, 0x4)
    OP_3E(0x19A, 1)

    ChrTalk(    #188
        0x10,
        (
            "It could really use something salty\x01",
            "to go with it, but I don't have\x01",
            "anything like that right now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x10,
        (
            "This season's great for Manoria's\x01",
            "specialty, salted anchovies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x10,
        (
            "Ah, well. Guess it's just the\x01",
            "drink, for right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x10,
        (
            "See you later, then.\x01",
            "Good luck.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4076")

    ChrTalk(    #192
        0x101,
        "#000FThanks.\x02",
    )

    CloseMessageWindow()
    Jump("loc_40F5")

    label("loc_4076")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40B7")

    ChrTalk(    #193
        0x102,
        "#010FPardon us, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x101,
        "#000FBye, mister.\x02",
    )

    CloseMessageWindow()
    Jump("loc_40F5")

    label("loc_40B7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40F5")

    ChrTalk(    #195
        0x105,
        "#040FPardon us, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x101,
        "#000FBye, mister.\x02",
    )

    CloseMessageWindow()

    label("loc_40F5")

    EventEnd(0x1)
    OP_4B(0x10, 255)
    Jump("loc_4831")

    label("loc_40FE")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_415B")
    OP_0D()
    OP_A9(0x23)
    OP_56(0x0)
    TalkEnd(0x10)
    Return()

    label("loc_415B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_416C")
    TalkEnd(0x10)
    Return()

    label("loc_416C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_42A9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_41EC")

    ChrTalk(    #197
        0x10,
        (
            "All I care about is that the\x01",
            "old man is doing okay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x10,
        (
            "I really appreciate it.\x01",
            "Good luck out there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42A6")

    label("loc_41EC")


    ChrTalk(    #199
        0x10,
        (
            "Don't worry about bringing\x01",
            "him the drink.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x10,
        "It was a silly request on my part.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x10,
        (
            "Maybe I'll get another chance\x01",
            "to ship him something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x10,
        "If I do, I might call on you again.\x02",
    )

    CloseMessageWindow()

    label("loc_42A6")

    Jump("loc_4831")

    label("loc_42A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_42BB")
    Call(0, 16)
    Jump("loc_4831")

    label("loc_42BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x40)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4541")
    OP_A2(0xD)
    OP_28(0x1D, 0x1, 0x2000)

    ChrTalk(    #203
        0x10,
        (
            "Hey, were you able to deliver\x01",
            "the stuff all right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(    #204
        0x101,
        (
            "#003FSorry...\x02\x03",

            "By the time everything was done,\x01",
            "we just didn't have the chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x102,
        (
            "#017FI apologize.\x02\x03",

            "I know that you made that\x01",
            "cocktail especially for him...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x102, 400)

    ChrTalk(    #206
        0x10,
        "Ah, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x10,
        (
            "Well, don't worry about it. It was\x01",
            "a silly request on my part.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x10,
        (
            "I told you from the start that\x01",
            "if it was too much trouble,\x01",
            "you could just dump it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x101,
        "#007FI'm really sorry...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(    #210
        0x10,
        (
            "Maybe I'll get another chance\x01",
            "to ship him something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x10,
        "If I do, I might call on you again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x102,
        "#010FThat would be fine.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x102, 400)

    ChrTalk(    #213
        0x10,
        "Okay, see you later.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4831")

    label("loc_4541")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_46D8")
    OP_28(0x1D, 0x1, 0x2000)
    OP_A2(0xD)

    ChrTalk(    #214
        0x10,
        (
            "Hey, there. Looks like you got\x01",
            "the whole Maintenance Kit thing\x01",
            "sorted out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x10,
        "How's the old salt doing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x101,
        (
            "#001FHe seemed to be just fine.\x01",
            "He sends his regards.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(    #217
        0x10,
        "Does he, now? Good, good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x10,
        (
            "Age eventually gets the best\x01",
            "of us all. Sounds like he's\x01",
            "still hanging in there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x10,
        (
            "I really appreciate it.\x01",
            "Good luck out there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x101,
        "#000FThanks. See you later.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4831")

    label("loc_46D8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_482D")

    ChrTalk(    #221
        0x10,
        "Say hello to the old man for me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x10,
        (
            "To be honest, it could really use something\x01",
            "salty to go with it, but I don't have\x01",
            "anything like that right now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x10,
        (
            "This season's great for Manoria's\x01",
            "specialty, salted anchovies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x10,
        (
            "Ah, well. Guess it's just the\x01",
            "drink, for right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x10,
        (
            "See you later, then.\x01",
            "Good luck.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4831")

    label("loc_482D")

    Call(0, 16)

    label("loc_4831")

    TalkEnd(0x10)
    Return()

    # Function_15_3855 end

    def Function_16_4835(): pass

    label("Function_16_4835")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_49CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4952")
    OP_A2(0x7)

    ChrTalk(    #226
        0x10,
        (
            "The Ravens must have been\x01",
            "hypnotized by the mayor to\x01",
            "help him, or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x10,
        (
            "To tell the truth, my little\x01",
            "brother is one of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x10,
        (
            "He doesn't always do the right\x01",
            "thing, but he's not a bad person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x10,
        (
            "Idiots...I guess now it's time\x01",
            "to pay the piper.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49C8")

    label("loc_4952")


    ChrTalk(    #230
        0x10,
        (
            "To tell the truth, my little\x01",
            "brother is one of the Ravens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x10,
        (
            "Idiots...I guess now it's time\x01",
            "to pay the piper.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49C8")

    Jump("loc_519D")

    label("loc_49CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_4ABA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A69")
    OP_A2(0x7)

    ChrTalk(    #232
        0x10,
        (
            "My little brother didn't come\x01",
            "home last night...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x10,
        (
            "Maybe he's just wandering\x01",
            "around somewhere...oh well.\x01",
            "I'm sure he'll turn up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AB7")

    label("loc_4A69")


    ChrTalk(    #234
        0x10,
        (
            "...I swear, he's been making\x01",
            "me worry about him ever\x01",
            "since we were kids.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AB7")

    Jump("loc_519D")

    label("loc_4ABA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_4BA1")

    ChrTalk(    #235
        0x10,
        (
            "When is the remodeling upstairs\x01",
            "going to be done already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x10,
        (
            "A lot of travelers come here,\x01",
            "specifically for the purpose\x01",
            "of going to the casino.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x10,
        (
            "If we don't reopen soon,\x01",
            "that sign outside is going\x01",
            "to be a lie.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_519D")

    label("loc_4BA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_4D54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C6C")
    OP_A2(0x7)

    ChrTalk(    #238
        0x10,
        (
            "*sigh* Looks like my brother\x01",
            "and his crew owe the bracers\x01",
            "big time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x10,
        "I hope they realize it, someday.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x10,
        (
            "Here's hoping those idiots take\x01",
            "the chance to soak their heads.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D51")

    label("loc_4C6C")


    ChrTalk(    #241
        0x10,
        (
            "*sigh* Looks like my brother\x01",
            "and his crew owe the bracers\x01",
            "big time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x10,
        (
            "I guess my brother and his\x01",
            "friends are indebted to the\x01",
            "Bracer Guild, this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x10,
        (
            "Here's hoping those idiots take\x01",
            "the chance to soak their heads.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D51")

    Jump("loc_519D")

    label("loc_4D54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_4D8E")

    ChrTalk(    #244
        0x10,
        (
            "What's wrong? Are you looking\x01",
            "for someone?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_519D")

    label("loc_4D8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_4ECB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E79")
    OP_A2(0x7)

    ChrTalk(    #245
        0x10,
        (
            "Rumor has it that my brother's\x01",
            "little crew got caught up with\x01",
            "the mayor yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x10,
        (
            "I'd bet money they only act\x01",
            "out like this because they're\x01",
            "insecure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x10,
        (
            "When you think about it,\x01",
            "it's kind of pathetic.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EC8")

    label("loc_4E79")


    ChrTalk(    #248
        0x10,
        (
            "Let's see now...time to start\x01",
            "another day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x10,
        "Best make the most of it.\x02",
    )

    CloseMessageWindow()

    label("loc_4EC8")

    Jump("loc_519D")

    label("loc_4ECB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_5052")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FBF")
    OP_A2(0x7)

    ChrTalk(    #250
        0x10,
        (
            "My kid brother is hanging\x01",
            "out with some thugs called\x01",
            "the Ravens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x10,
        (
            "He won't get a job, and now\x01",
            "he's just causing trouble\x01",
            "for other people...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x10,
        (
            "It's so damned embarrassing.\x01",
            "Makes me ashamed to say\x01",
            "we're family...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_504F")

    label("loc_4FBF")


    ChrTalk(    #253
        0x10,
        (
            "My kid brother is hanging\x01",
            "out with some thugs called\x01",
            "the Ravens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x10,
        (
            "It's so damned embarrassing.\x01",
            "Makes me ashamed to say\x01",
            "we're family...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_504F")

    Jump("loc_519D")

    label("loc_5052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_519D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5126")
    OP_A2(0x7)

    ChrTalk(    #255
        0x10,
        "Hey, what do we have here...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x10,
        "Are you folks travelers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x10,
        (
            "Word to the wise, stay away\x01",
            "from the warehouse district.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x10,
        (
            "We've got some real unsavory\x01",
            "types hanging out down there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_519D")

    label("loc_5126")


    ChrTalk(    #259
        0x10,
        (
            "You should stay away from\x01",
            "the warehouse district.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x10,
        (
            "We've got some real unsavory\x01",
            "types hanging out down there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_519D")

    TalkEnd(0x10)
    Return()

    # Function_16_4835 end

    def Function_17_51A1(): pass

    label("Function_17_51A1")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_52C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5255")
    OP_A2(0x8)

    ChrTalk(    #261
        0xFE,
        "See the guy in that chair, there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0xFE,
        (
            "I think it's Simon, from\x01",
            "Ms. Mirano's place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xFE,
        (
            "The Trinos are the most renowned\x01",
            "of Bose's merchant families.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52C6")

    label("loc_5255")


    ChrTalk(    #264
        0xFE,
        (
            "So, Simon from Mirano's\x01",
            "place is here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xFE,
        (
            "The Trinos are the most renowned\x01",
            "of Bose's merchant families.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52C6")

    Jump("loc_5450")

    label("loc_52C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_53D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5374")
    OP_A2(0x8)

    ChrTalk(    #266
        0xFE,
        (
            "I played a game or two with\x01",
            "that guy at the card table.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0xFE,
        "I'd be thrilled to beat him...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0xFE,
        (
            "...but he honestly kind\x01",
            "of gives me the creeps.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53CD")

    label("loc_5374")


    ChrTalk(    #269
        0xFE,
        "I'd be thrilled to beat him...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0xFE,
        (
            "...but he honestly kind\x01",
            "of gives me the creeps.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53CD")

    Jump("loc_5450")

    label("loc_53D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_5450")

    ChrTalk(    #271
        0xFE,
        (
            "Phew...I thought the airship\x01",
            "trouble was going to ruin the\x01",
            "business meeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0xFE,
        "I'm glad I rushed here from Bose.\x02",
    )

    CloseMessageWindow()

    label("loc_5450")

    TalkEnd(0x11)
    Return()

    # Function_17_51A1 end

    def Function_18_5454(): pass

    label("Function_18_5454")

    TalkBegin(0x12)
    OP_62(0x12, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #273
        0xFE,
        (
            "Ahhh...it's good to have some\x01",
            "alone time every now and then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xFE,
        (
            "My father and daughter are\x01",
            "upstairs, playing.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x12)
    Return()

    # Function_18_5454 end

    def Function_19_54EC(): pass

    label("Function_19_54EC")

    TalkBegin(0x13)

    ChrTalk(    #275
        0xFE,
        "Grrrr...one more go!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x13)
    Return()

    # Function_19_54EC end

    def Function_20_550D(): pass

    label("Function_20_550D")

    TalkBegin(0x14)

    ChrTalk(    #276
        0xFE,
        "Woohoo! I win again!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x14)
    Return()

    # Function_20_550D end

    def Function_21_552E(): pass

    label("Function_21_552E")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_555A")

    ChrTalk(    #277
        0xFE,
        "Okay, I'm here! I'm here!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5593")

    label("loc_555A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_5593")

    ChrTalk(    #278
        0xFE,
        (
            "I'm a little late, but I came\x01",
            "for breakfast.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5593")

    TalkEnd(0x15)
    Return()

    # Function_21_552E end

    def Function_22_5597(): pass

    label("Function_22_5597")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_55C3")

    ChrTalk(    #279
        0xFE,
        "*sigh* Losing is not fun.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5646")

    label("loc_55C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_5646")

    ChrTalk(    #280
        0xFE,
        (
            "I figured this place would be noisy,\x01",
            "being right below a casino.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0xFE,
        (
            "Instead...it's actually very quiet\x01",
            "and peaceful!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5646")

    TalkEnd(0x16)
    Return()

    # Function_22_5597 end

    def Function_23_564A(): pass

    label("Function_23_564A")

    TalkBegin(0x1B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_56C5")

    ChrTalk(    #282
        0xFE,
        (
            "Ha ha ha...I did it! I figured\x01",
            "out the map.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0xFE,
        (
            "Okay, this time I'm going to\x01",
            "find that pirate treasure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_571E")

    label("loc_56C5")


    ChrTalk(    #284
        0xFE,
        "Hmm...ah, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0xFE,
        (
            "Ha ha ha...I finally figured out\x01",
            "the significance of the map!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_571E")

    TalkEnd(0x1B)
    Return()

    # Function_23_564A end

    def Function_24_5722(): pass

    label("Function_24_5722")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #286
        (
            "\x07\x05       Lavantar Casino & Bar\x01",
            "Newly remodeled casino to reopen just in\x01",
            "time for the Queen's Birthday Celebration!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_24_5722 end

    SaveToFile()

Try(main)
