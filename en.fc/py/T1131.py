from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1131   ._SN',
        MapName             = 'Bose',
        Location            = 'T1131.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T1131   ._SN',
            'ED6_DT01/T1131_1 ._SN',
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
        'Mayor Maybelle',                       # 9
        'Warner',                               # 10
        'Platina',                              # 11
        'Cornelius',                            # 12
        'Lyndon',                               # 13
        'Simon',                                # 14
        'Nial',                                 # 15
        'Manager Lechter',                      # 16
        'Head Chef Ross',                       # 17
        'Gwen',                                 # 18
        'Citron',                               # 19
        'Lenore',                               # 20
        'Marian',                               # 21
        'Norche',                               # 22
        'Horrace',                              # 23
        'Alta',                                 # 24
        'Caron',                                # 25
        'Shaque',                               # 26
        'Letta',                                # 27
        'Fannie',                               # 28
        'Dessert',                              # 29
        'Dessert',                              # 30
        'Soup Bowl',                            # 31
        'Spoon',                                # 32
        'Fork',                                 # 33
        'Fork',                                 # 34
        'Knife',                                # 35
        'Knife',                                # 36
        'Food',                                 # 37
        'Wine',                                 # 38
        'Teapot',                               # 39
        'Teapot',                               # 40
        'Teapot',                               # 41
        'Bottle',                               # 42
        'Wine Glass',                           # 43
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
        'ED6_DT07/CH02363 ._CH',             # 00
        'ED6_DT07/CH01270 ._CH',             # 01
        'ED6_DT07/CH01050 ._CH',             # 02
        'ED6_DT07/CH01043 ._CH',             # 03
        'ED6_DT07/CH01660 ._CH',             # 04
        'ED6_DT07/CH01143 ._CH',             # 05
        'ED6_DT06/CH20086 ._CH',             # 06
        'ED6_DT07/CH01560 ._CH',             # 07
        'ED6_DT07/CH01280 ._CH',             # 08
        'ED6_DT07/CH02480 ._CH',             # 09
        'ED6_DT07/CH01570 ._CH',             # 0A
        'ED6_DT07/CH02540 ._CH',             # 0B
        'ED6_DT07/CH01213 ._CH',             # 0C
        'ED6_DT07/CH01233 ._CH',             # 0D
        'ED6_DT07/CH01003 ._CH',             # 0E
        'ED6_DT07/CH01183 ._CH',             # 0F
        'ED6_DT07/CH01023 ._CH',             # 10
        'ED6_DT07/CH01123 ._CH',             # 11
        'ED6_DT07/CH01043 ._CH',             # 12
        'ED6_DT07/CH01053 ._CH',             # 13
        'ED6_DT07/CH00003 ._CH',             # 14
        'ED6_DT07/CH00013 ._CH',             # 15
        'ED6_DT07/CH00023 ._CH',             # 16
        'ED6_DT07/CH02060 ._CH',             # 17
        'ED6_DT06/CH20021 ._CH',             # 18
        'ED6_DT06/CH20020 ._CH',             # 19
    )

    AddCharChipPat(
        'ED6_DT07/CH02363P._CP',             # 00
        'ED6_DT07/CH01270P._CP',             # 01
        'ED6_DT07/CH01050P._CP',             # 02
        'ED6_DT07/CH01043P._CP',             # 03
        'ED6_DT07/CH01660P._CP',             # 04
        'ED6_DT07/CH01143P._CP',             # 05
        'ED6_DT06/CH20086P._CP',             # 06
        'ED6_DT07/CH01560P._CP',             # 07
        'ED6_DT07/CH01280P._CP',             # 08
        'ED6_DT07/CH02480P._CP',             # 09
        'ED6_DT07/CH01570P._CP',             # 0A
        'ED6_DT07/CH02540P._CP',             # 0B
        'ED6_DT07/CH01213P._CP',             # 0C
        'ED6_DT07/CH01233P._CP',             # 0D
        'ED6_DT07/CH01003P._CP',             # 0E
        'ED6_DT07/CH01183P._CP',             # 0F
        'ED6_DT07/CH01023P._CP',             # 10
        'ED6_DT07/CH01123P._CP',             # 11
        'ED6_DT07/CH01043P._CP',             # 12
        'ED6_DT07/CH01053P._CP',             # 13
        'ED6_DT07/CH00003P._CP',             # 14
        'ED6_DT07/CH00013P._CP',             # 15
        'ED6_DT07/CH00023P._CP',             # 16
        'ED6_DT07/CH02060P._CP',             # 17
        'ED6_DT06/CH20021P._CP',             # 18
        'ED6_DT06/CH20020P._CP',             # 19
    )

    DeclNpc(
        X                   = -620,
        Z                   = -1000,
        Y                   = -3500,
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
        X                   = 2970,
        Z                   = 0,
        Y                   = 3650,
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
        X                   = 1400,
        Z                   = 0,
        Y                   = 1500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -6030,
        Z                   = 3350,
        Y                   = 5100,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 5480,
        Z                   = 0,
        Y                   = 1480,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -1450,
        Z                   = 3250,
        Y                   = 3420,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -7300,
        Z                   = 1400,
        Y                   = -4100,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 196614,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -42600,
        Z                   = 0,
        Y                   = 1700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -35500,
        Z                   = 0,
        Y                   = 46700,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -47450,
        Z                   = 0,
        Y                   = 44160,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = -38500,
        Z                   = 1500,
        Y                   = 14200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -53300,
        Z                   = 1500,
        Y                   = 200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = -52950,
        Z                   = 1600,
        Y                   = 11400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x154,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = -52950,
        Z                   = 1600,
        Y                   = 8600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x154,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = -45600,
        Z                   = 1600,
        Y                   = 11000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x154,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = -36400,
        Z                   = 1600,
        Y                   = -1000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x154,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = -39120,
        Z                   = 1600,
        Y                   = 7410,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x154,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = -39130,
        Z                   = 1600,
        Y                   = 4590,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x154,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = -42400,
        Z                   = 1600,
        Y                   = 11000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x154,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = -39600,
        Z                   = 1600,
        Y                   = 11000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x154,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = -52960,
        Z                   = 2230,
        Y                   = 9560,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 589849,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -52940,
        Z                   = 2230,
        Y                   = 10400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 589849,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -35500,
        Z                   = 2150,
        Y                   = -1060,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 196633,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -35750,
        Z                   = 2150,
        Y                   = -1000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1114137,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -35670,
        Z                   = 2150,
        Y                   = -950,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1376281,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -35670,
        Z                   = 2150,
        Y                   = -830,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1376281,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -35550,
        Z                   = 2150,
        Y                   = -1350,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1441817,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -35550,
        Z                   = 2150,
        Y                   = -1490,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1441817,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -46510,
        Z                   = 2230,
        Y                   = 10750,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 393241,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -46750,
        Z                   = 2230,
        Y                   = 11300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327704,
        ChipIndex           = 0x18,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -39030,
        Z                   = 2200,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1703961,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -39030,
        Z                   = 2200,
        Y                   = 6500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638425,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -39030,
        Z                   = 2200,
        Y                   = 5300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638425,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -6490,
        Z                   = 2100,
        Y                   = -3560,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835033,
        ChipIndex           = 0x19,
        NpcIndex            = 0x1C6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -6360,
        Z                   = 2100,
        Y                   = -4420,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65560,
        ChipIndex           = 0x18,
        NpcIndex            = 0x1C6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 3050,
        TriggerZ            = 0,
        TriggerY            = 1520,
        TriggerRange        = 400,
        ActorX              = 2970,
        ActorZ              = 1500,
        ActorY              = 3650,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_5FE",          # 00, 0
        "Function_1_6DB",          # 01, 1
        "Function_2_6DC",          # 02, 2
        "Function_3_6F2",          # 03, 3
        "Function_4_716",          # 04, 4
        "Function_5_C53",          # 05, 5
        "Function_6_C77",          # 06, 6
        "Function_7_EFC",          # 07, 7
        "Function_8_F01",          # 08, 8
        "Function_9_1880",         # 09, 9
        "Function_10_21FC",        # 0A, 10
        "Function_11_2B90",        # 0B, 11
        "Function_12_3A9F",        # 0C, 12
        "Function_13_3F96",        # 0D, 13
        "Function_14_6A5A",        # 0E, 14
        "Function_15_7B66",        # 0F, 15
        "Function_16_8415",        # 10, 16
        "Function_17_8DC2",        # 11, 17
        "Function_18_9658",        # 12, 18
        "Function_19_9E29",        # 13, 19
        "Function_20_A6FE",        # 14, 20
        "Function_21_B06E",        # 15, 21
        "Function_22_BCB7",        # 16, 22
        "Function_23_C372",        # 17, 23
        "Function_24_C75B",        # 18, 24
        "Function_25_CD70",        # 19, 25
        "Function_26_CFE0",        # 1A, 26
        "Function_27_D339",        # 1B, 27
        "Function_28_E4C8",        # 1C, 28
    )


    def Function_0_5FE(): pass

    label("Function_0_5FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_60C")
    OP_A3(0x3FA)
    Event(0, 27)

    label("loc_60C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_62F")
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8)
    SetChrFlags(0xB, 0x80)
    Jump("loc_6DA")

    label("loc_62F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_64D")
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8)
    Jump("loc_6DA")

    label("loc_64D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_66B")
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8)
    Jump("loc_6DA")

    label("loc_66B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_675")
    Jump("loc_6DA")

    label("loc_675")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_697")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    Jump("loc_6DA")

    label("loc_697")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 6)), scpexpr(EXPR_END)), "loc_6AB")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_6DA")

    label("loc_6AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_6BA")
    ClearChrFlags(0xD, 0x80)
    Jump("loc_6DA")

    label("loc_6BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_6C9")
    ClearChrFlags(0xD, 0x80)
    Jump("loc_6DA")

    label("loc_6C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_6DA")
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xB, 0x10)

    label("loc_6DA")

    Return()

    # Function_0_5FE end

    def Function_1_6DB(): pass

    label("Function_1_6DB")

    Return()

    # Function_1_6DB end

    def Function_2_6DC(): pass

    label("Function_2_6DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6F1")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_6DC")

    label("loc_6F1")

    Return()

    # Function_2_6DC end

    def Function_3_6F2(): pass

    label("Function_3_6F2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_715")
    OP_8D(0xFE, 1450, 3690, 4800, 3990, 1000)
    Jump("Function_3_6F2")

    label("loc_715")

    Return()

    # Function_3_6F2 end

    def Function_4_716(): pass

    label("Function_4_716")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_855")

    label("loc_721")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_852")
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFF7CC, 0x0, 0xFFFFFB50, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFEFFC, 0x5DC, 0xFFFFFBB4, 0x3E8, 0x0)
    OP_8E(0xFE, 0xFFFFE890, 0x5DC, 0xFFFFF574, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFFE37C, 0x5DC, 0xFFFFFF9C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFE37C, 0xCB2, 0x834, 0x3E8, 0x0)
    OP_8E(0xFE, 0xFFFFEC78, 0xCB2, 0x1004, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFFE638, 0xCB2, 0x898, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFE638, 0x5DC, 0x0, 0x3E8, 0x0)
    OP_8E(0xFE, 0xFFFFE890, 0x5DC, 0xFFFFF574, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFFEFFC, 0x5DC, 0xFFFFFBB4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF7CC, 0x0, 0xFFFFFB50, 0x3E8, 0x0)
    OP_8E(0xFE, 0x578, 0x0, 0x5DC, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 200)
    Sleep(5000)
    Jump("loc_721")

    label("loc_852")

    Jump("loc_C52")

    label("loc_855")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_944")

    label("loc_860")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_941")
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFFA88, 0x0, 0x4B0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFA88, 0x0, 0xDAC, 0x7D0, 0x0)
    OP_8E(0xFE, 0x15E, 0x0, 0x1130, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 200)
    Sleep(5000)
    OP_8E(0xFE, 0x44C, 0x0, 0x1130, 0x7D0, 0x0)
    OP_8C(0xFE, 45, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFFFBB4, 0x0, 0x1130, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFFFA88, 0x0, 0xDAC, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFA88, 0x0, 0x4B0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x578, 0x0, 0x5DC, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 200)
    Sleep(5000)
    Jump("loc_860")

    label("loc_941")

    Jump("loc_C52")

    label("loc_944")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_A7F")

    label("loc_94B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A7C")
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFF7CC, 0x0, 0xFFFFFB50, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFEFFC, 0x5DC, 0xFFFFFBB4, 0x3E8, 0x0)
    OP_8E(0xFE, 0xFFFFE890, 0x5DC, 0xFFFFF574, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFFE37C, 0x5DC, 0xFFFFFF9C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFE37C, 0xCB2, 0x834, 0x3E8, 0x0)
    OP_8E(0xFE, 0xFFFFEC78, 0xCB2, 0x1004, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFFE638, 0xCB2, 0x898, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFE638, 0x5DC, 0x0, 0x3E8, 0x0)
    OP_8E(0xFE, 0xFFFFE890, 0x5DC, 0xFFFFF574, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFFEFFC, 0x5DC, 0xFFFFFBB4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF7CC, 0x0, 0xFFFFFB50, 0x3E8, 0x0)
    OP_8E(0xFE, 0x578, 0x0, 0x5DC, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 200)
    Sleep(5000)
    Jump("loc_94B")

    label("loc_A7C")

    Jump("loc_C52")

    label("loc_A7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_B6A")

    label("loc_A86")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B67")
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFFA88, 0x0, 0x4B0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFA88, 0x0, 0xDAC, 0x7D0, 0x0)
    OP_8E(0xFE, 0x15E, 0x0, 0x1130, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 200)
    Sleep(5000)
    OP_8E(0xFE, 0x44C, 0x0, 0x1130, 0x7D0, 0x0)
    OP_8C(0xFE, 45, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFFFBB4, 0x0, 0x1130, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFFFA88, 0x0, 0xDAC, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFA88, 0x0, 0x4B0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x578, 0x0, 0x5DC, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 200)
    Sleep(5000)
    Jump("loc_A86")

    label("loc_B67")

    Jump("loc_C52")

    label("loc_B6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_C52")

    label("loc_B71")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C52")
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFFA88, 0x0, 0x4B0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFA88, 0x0, 0xDAC, 0x7D0, 0x0)
    OP_8E(0xFE, 0x15E, 0x0, 0x1130, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 200)
    Sleep(5000)
    OP_8E(0xFE, 0x44C, 0x0, 0x1130, 0x7D0, 0x0)
    OP_8C(0xFE, 45, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFFFBB4, 0x0, 0x1130, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFFFA88, 0x0, 0xDAC, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFA88, 0x0, 0x4B0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x578, 0x0, 0x5DC, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 200)
    Sleep(5000)
    Jump("loc_B71")

    label("loc_C52")

    Return()

    # Function_4_716 end

    def Function_5_C53(): pass

    label("Function_5_C53")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C76")
    OP_8D(0xFE, -48200, 42570, -46450, 46500, 1000)
    Jump("Function_5_C53")

    label("loc_C76")

    Return()

    # Function_5_C53 end

    def Function_6_C77(): pass

    label("Function_6_C77")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EFB")
    OP_8E(0xFE, 0xFFFF360C, 0x5DC, 0xCE4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF360C, 0x5DC, 0xFA0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF360C, 0x5DC, 0x21FC, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFF5358, 0x5DC, 0x2580, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF5358, 0x5DC, 0x2EE0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF4D18, 0x5DC, 0x2EE0, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFF4D7C, 0x5DC, 0x319C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF5FD8, 0x5DC, 0x319C, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFF77AC, 0x5DC, 0x30D4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF77AC, 0x5DC, 0x2E7C, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFF77AC, 0x5DC, 0x30D4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF80A8, 0x5DC, 0x30D4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF80A8, 0x5DC, 0x1F40, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF6EB0, 0x5DC, 0xFA0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF6DE8, 0x5DC, 0xFFFFFB50, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF7040, 0x5DC, 0xFFFFF6A0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF72FC, 0x5DC, 0xFFFFF6A0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF748C, 0x5DC, 0xFFFFF7CC, 0x7D0, 0x0)
    OP_8C(0xFE, 45, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFF7428, 0x5DC, 0xFFFFF6A0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF81D5, 0x5DC, 0xFFFFF6A0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF81D5, 0x5DC, 0x190, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF7748, 0x5DC, 0x190, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF7040, 0x5DC, 0x960, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF7040, 0x5DC, 0x2198, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF3990, 0x5DC, 0x2198, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF360C, 0x5DC, 0x1CE8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF360C, 0x5DC, 0x9C4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF2FCC, 0x5DC, 0xC8, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 200)
    Sleep(5000)
    Jump("Function_6_C77")

    label("loc_EFB")

    Return()

    # Function_6_C77 end

    def Function_7_EFC(): pass

    label("Function_7_EFC")

    Call(0, 8)
    Return()

    # Function_7_EFC end

    def Function_8_F01(): pass

    label("Function_8_F01")

    TalkBegin(0x9)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                             # 0
            "Shop\x01",                             # 1
            "[Cheese Risotto] - 300 mira\x01",      # 2
            "Leave\x01",                            # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F7D")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x1D)
    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_F7D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10B1")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x12C), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1077")
    SubMira(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #0
        "\x06\x07\x00Ate \x07\x02Cheese Risotto\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFC, 0x0)
    OP_31(0x1, 0xFC, 0x0)
    OP_31(0x2, 0xFC, 0x0)
    OP_31(0x3, 0xFC, 0x0)
    OP_31(0x4, 0xFC, 0x0)
    OP_31(0x5, 0xFC, 0x0)
    OP_31(0x6, 0xFC, 0x0)
    OP_31(0x7, 0xFC, 0x0)
    OP_31(0x0, 0xFD, 0x96)
    OP_31(0x1, 0xFD, 0x96)
    OP_31(0x2, 0xFD, 0x96)
    OP_31(0x3, 0xFD, 0x96)
    OP_31(0x4, 0xFD, 0x96)
    OP_31(0x5, 0xFD, 0x96)
    OP_31(0x6, 0xFD, 0x96)
    OP_31(0x7, 0xFD, 0x96)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1069")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x5)"), scpexpr(EXPR_END)), "loc_1039")
    Jump("loc_1069")

    label("loc_1039")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #1
        "\x06\x07\x00Learned '\x07\x02Cheese Risotto\x07\x00' recipe.\x02",
    )

    CloseMessageWindow()

    label("loc_1069")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_109F")

    label("loc_1077")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #2
        "Insufficient mira.\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_109F")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x9)
    Return()

    label("loc_10B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10CB")
    FadeToBright(300, 0)
    TalkEnd(0x9)
    Return()

    label("loc_10CB")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_12BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1202")
    OP_A2(0x1)

    ChrTalk(    #3
        0x9,
        (
            "They say the sky bandits were responsible\x01",
            "for all those burglaries...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x9,
        (
            "And what's more, I hear they were\x01",
            "arrested en masse by a Royal Army\x01",
            "division led by General Morgan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x9,
        (
            "Haven't had a story take my breath\x01",
            "away like that for quite some time.\x01",
            "Seriously, what a scoop!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12BB")

    label("loc_1202")


    ChrTalk(    #6
        0x9,
        (
            "Is it true that the Royal Army\x01",
            "arrested the sky bandits?\x01",
            "Like, ALL of them...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x9,
        (
            "Haven't had a story take my breath\x01",
            "away like that for quite some time.\x01",
            "Seriously, what a scoop!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12BB")

    Jump("loc_187C")

    label("loc_12BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_1372")

    ChrTalk(    #8
        0x9,
        (
            "We live in lawless times, it seems.\x01",
            "The violent incidents just keep on\x01",
            "coming, one right after the other!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x9,
        (
            "I wish it'd all just stop and let\x01",
            "me live in peace...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_187C")

    label("loc_1372")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_1431")

    ChrTalk(    #10
        0x9,
        (
            "I hear the southern shopping district\x01",
            "got trashed by bandits...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x9,
        (
            "It's all because Bose is rich. You\x01",
            "get money, you get robbed. Been that\x01",
            "way for as long as I can remember.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_187C")

    label("loc_1431")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_14EF")

    ChrTalk(    #12
        0x9,
        (
            "This bar was originally founded more\x01",
            "on a whim than anything else...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x9,
        (
            "I wish I could take it easy and didn't\x01",
            "have to worry so much about criminals\x01",
            "and profits and such...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_187C")

    label("loc_14EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_166D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1603")
    OP_A2(0x1)

    ChrTalk(    #14
        0x9,
        (
            "The Anterose doesn't feel like a place\x01",
            "where you can just sit back and relax,\x01",
            "you know? You always feel rushed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x9,
        (
            "That's why I make such a point of trying to\x01",
            "give my establishment a comfortable, homey\x01",
            "feel, so people know they can take it easy!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_166A")

    label("loc_1603")


    ChrTalk(    #16
        0x9,
        (
            "It's a place where everybody knows\x01",
            "your name...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x9,
        (
            "All right. Best of luck on the\x01",
            "keyword hunt!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_166A")

    Jump("loc_187C")

    label("loc_166D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_1809")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17B5")
    OP_A2(0x1)

    ChrTalk(    #18
        0x9,
        "People often compare us to Anterose.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x9,
        "But it's like apples and oranges!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x9,
        (
            "You like good, cheap grub,\x01",
            "you come here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x9,
        (
            "You want for hoity-toity delicacies and\x01",
            "excessive formality, you go there!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x9,
        (
            "I don't feel the slightest shred of\x01",
            "competition. We appeal to completely\x01",
            "different customers!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1806")

    label("loc_17B5")


    ChrTalk(    #23
        0x9,
        "People often compare us to Anterose.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x9,
        "But it's like apples and oranges!\x02",
    )

    CloseMessageWindow()

    label("loc_1806")

    Jump("loc_187C")

    label("loc_1809")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_187C")

    ChrTalk(    #25
        0x9,
        "Welcome, welcome! Order up!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x9,
        (
            "We've got good, cheap food that'll\x01",
            "make your belly sing with delight!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_187C")

    TalkEnd(0x9)
    Return()

    # Function_8_F01 end

    def Function_9_1880(): pass

    label("Function_9_1880")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1929")

    ChrTalk(    #27
        0xFE,
        "Okay, let's get to work!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "Gotta get all this crap in order a.s.a.p.\x01",
            "so I can kick back with a drink! Sometimes\x01",
            "I wanna be a customer too, ya know!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21F8")

    label("loc_1929")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_1B52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A75")
    OP_A2(0x2)

    ChrTalk(    #29
        0xFE,
        (
            "I know there's still some serious stuff\x01",
            "going down outside, but everything seems\x01",
            "fine and dandy in here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "It's all thanks to the manager's\x01",
            "policy: Take it easy, 'cause this\x01",
            "here is a place to unwind!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "Things get a little boring sometimes\x01",
            "as a result, but hey, I'd rather be\x01",
            "in here than out there!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B4F")

    label("loc_1A75")


    ChrTalk(    #32
        0xFE,
        (
            "I know there's still some serious stuff\x01",
            "going down outside, but everything seems\x01",
            "fine and dandy in here, ya know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "It's all thanks to the manager's\x01",
            "policy: Take it easy, 'cause this\x01",
            "here is a place to unwind!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B4F")

    Jump("loc_21F8")

    label("loc_1B52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_1DF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CF4")
    OP_A2(0x2)

    ChrTalk(    #34
        0xFE,
        (
            "Looks like the bandits had enough sense\x01",
            "to know we'd be a lousy target. Do more\x01",
            "harm than good to attack us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "There are a lot of larger shops and shopkeepers\x01",
            "in the south district, but once the sun goes down,\x01",
            "the roads are practically deserted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "If we got raided, all they'd find\x01",
            "are a bunch'a leftover ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "And I think only a mouse would\x01",
            "be happy with a haul like that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DF5")

    label("loc_1CF4")


    ChrTalk(    #38
        0xFE,
        (
            "Looks like the bandits had enough sense\x01",
            "to know we'd be a lousy target. Do more\x01",
            "harm than good to attack us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "If we got raided, all they'd find\x01",
            "are a bunch'a leftover ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "And I think only a mouse would\x01",
            "be happy with a haul like that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DF5")

    Jump("loc_21F8")

    label("loc_1DF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_1F0E")

    ChrTalk(    #41
        0xFE,
        (
            "The manager always says he runs this\x01",
            "place as a hobby, and he acts like that's\x01",
            "why it's such a great establishment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "Rumor has it the owner of Anterose\x01",
            "says the exact same thing, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "But I think their obsessions are\x01",
            "on two different levels entirely.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21F8")

    label("loc_1F0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_20EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_205A")
    OP_A2(0x2)

    ChrTalk(    #44
        0xFE,
        (
            "Our boss, now HE takes pride in the fact\x01",
            "that people tend to stick around for a\x01",
            "long time when they come here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "I'm guessing it's probably because\x01",
            "a lot of people use this place for\x01",
            "business meetings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "Or maybe it's just because it's such\x01",
            "a half-assed business, people feel\x01",
            "right at home. I dunno!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20EC")

    label("loc_205A")


    ChrTalk(    #47
        0xFE,
        (
            "What I do know is that we get a lot of weirdos\x01",
            "in here, and people who blather on endlessly\x01",
            "about their troubles. It's what we're known for!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20EC")

    Jump("loc_21F8")

    label("loc_20EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_21C3")

    ChrTalk(    #48
        0xFE,
        (
            "A lot of people compare us to\x01",
            "Anterose, actually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "But there's really no comparison.\x01",
            "None whatsoever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "Anterose is where you go if you've\x01",
            "got money...and this is where you\x01",
            "go if you don't.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21F8")

    label("loc_21C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_21F8")

    ChrTalk(    #51
        0xFE,
        "Hey, welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        "Sit wherever ya like.\x02",
    )

    CloseMessageWindow()

    label("loc_21F8")

    TalkEnd(0xA)
    Return()

    # Function_9_1880 end

    def Function_10_21FC(): pass

    label("Function_10_21FC")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_231A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22E0")
    OP_A2(0x3)

    ChrTalk(    #53
        0xB,
        (
            "That Nigel fellow's been taken to\x01",
            "the Haken Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xB,
        (
            "Seems he got himself into some\x01",
            "pretty hot water.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xB,
        (
            "Hope it comes out that I was tricked\x01",
            "by him. Might help get me back on my\x01",
            "feet, you know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2317")

    label("loc_22E0")


    ChrTalk(    #56
        0xB,
        (
            "That Nigel fellow's been taken to\x01",
            "the Haken Gate.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2317")

    Jump("loc_2B8C")

    label("loc_231A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_245C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23DB")
    OP_A2(0x3)

    ChrTalk(    #57
        0xFE,
        (
            "They actually sent someone to\x01",
            "question me about it a little\x01",
            "while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "He asked all about my workshop's\x01",
            "finances...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "Guess ol' Nigel was cooking the\x01",
            "books...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2459")

    label("loc_23DB")


    ChrTalk(    #60
        0xFE,
        (
            "They actually sent someone to\x01",
            "question me about it a little\x01",
            "while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "He asked all about my workshop's\x01",
            "finances...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2459")

    Jump("loc_2B8C")

    label("loc_245C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_25B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2521")
    OP_A2(0x3)

    ChrTalk(    #62
        0xFE,
        (
            "Seems my workshop was attacked\x01",
            "by the bandits as well. Have they\x01",
            "no shame?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "I'm a bit worried about one of my\x01",
            "workers. A man named Nigel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        "Sure hope he's okay...\x02",
    )

    CloseMessageWindow()
    Jump("loc_25B5")

    label("loc_2521")


    ChrTalk(    #65
        0xFE,
        (
            "Seems my workshop was attacked\x01",
            "by the bandits as well. Have they\x01",
            "no shame?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "I'm a bit worried about one of my\x01",
            "workers. A man named Nigel.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25B5")

    Jump("loc_2B8C")

    label("loc_25B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_2776")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26BD")
    OP_A2(0x3)

    ChrTalk(    #67
        0xFE,
        (
            "Won't do me any good to just\x01",
            "keep crying about this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "It's my own fault the workshop got\x01",
            "attacked. I should've been more\x01",
            "careful!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "Well, no sense in giving up! That's\x01",
            "not the Bose way. Time to roll up\x01",
            "my sleeves and try again!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2773")

    label("loc_26BD")


    ChrTalk(    #70
        0xFE,
        (
            "It's my own fault the workshop got\x01",
            "attacked. I should've been more\x01",
            "careful!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "Well, no sense in giving up! That's\x01",
            "not the Bose way. Time to roll up\x01",
            "my sleeves and try again!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2773")

    Jump("loc_2B8C")

    label("loc_2776")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_2922")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28EC")
    OP_A2(0x3)

    ChrTalk(    #72
        0xFE,
        "Damn that Nigel...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "We always came in together and\x01",
            "worked side-by-side. Can't believe\x01",
            "he'd betray me like that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "He's the one who signed the papers to\x01",
            "give me a loan when I first started up\x01",
            "this business, for goodness' sakes!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "And then he cheated his way up to\x01",
            "the top...and now this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "What the hell, Nigel...\x01",
            "What the hell, I say!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_291F")

    label("loc_28EC")


    ChrTalk(    #77
        0xFE,
        (
            "What the hell, Nigel...\x01",
            "What the hell, I say!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_291F")

    Jump("loc_2B8C")

    label("loc_2922")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_2B06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A70")
    OP_A2(0x3)

    ChrTalk(    #78
        0xFE,
        (
            "I used to manage an orbment\x01",
            "workshop...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "Then one day, I took out a rather\x01",
            "large loan and found myself in\x01",
            "way over my head...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "...So the workshop got handed over\x01",
            "to my debtor. I lost it all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "I worked my way up from the market\x01",
            "and really thought I was on the way\x01",
            "to making my dreams come true...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B03")

    label("loc_2A70")


    ChrTalk(    #82
        0xFE,
        (
            "I worked my way up from the market\x01",
            "and really thought I was on the way\x01",
            "to making my dreams come true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        "Now, my future is looking bleak...\x02",
    )

    CloseMessageWindow()

    label("loc_2B03")

    Jump("loc_2B8C")

    label("loc_2B06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_2B8C")

    ChrTalk(    #84
        0xFE,
        "Ohhh...woe is me...*hic*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        "How did things get like this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "I gave up my whole life for that\x01",
            "damned workshop...*hic*\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B8C")

    TalkEnd(0xB)
    Return()

    # Function_10_21FC end

    def Function_11_2B90(): pass

    label("Function_11_2B90")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_2D73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CDA")
    OP_A2(0x4)

    ChrTalk(    #87
        0xFE,
        (
            "Just as I'd hoped... There really ARE\x01",
            "reports in this land from people who\x01",
            "claim to have seen an ancient dragon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "Yes... Ohhh, YES...\x01",
            "My excitement is paramount!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "I must know why they no longer show themselves...\x01",
            "I must know where they have gone...\x01",
            "And I believe the time for answers is nigh!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D70")

    label("loc_2CDA")


    ChrTalk(    #90
        0xFE,
        (
            "There really ARE reports in this\x01",
            "land from people who claim to have\x01",
            "seen an ancient dragon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "Yes... Ohhh, YES...\x01",
            "My excitement is paramount!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D70")

    Jump("loc_3A9B")

    label("loc_2D73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_2F1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E60")
    OP_A2(0x4)

    ChrTalk(    #92
        0xFE,
        (
            "The last man to have ever seen an\x01",
            "ancient dragon is from Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        "That is why I've come.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "I suppose the first order of business--\x01",
            "as always--is to speak with the locals,\x01",
            "and see what answers can be found.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F1C")

    label("loc_2E60")


    ChrTalk(    #95
        0xFE,
        (
            "The last man to have ever seen an\x01",
            "ancient dragon is from Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "I suppose the first order of business--\x01",
            "as always--is to speak with the locals,\x01",
            "and see what answers can be found.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F1C")

    Jump("loc_3A9B")

    label("loc_2F1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_2FC3")

    ChrTalk(    #97
        0xFE,
        (
            "The ancient dragons that lived\x01",
            "before the Great Collapse...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "It almost seems as if they removed\x01",
            "themselves from this land of their\x01",
            "own volition!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A9B")

    label("loc_2FC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_342B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3399")
    OP_A2(0x4)

    ChrTalk(    #99
        0xFE,
        (
            "I study creatures that lived in the old\x01",
            "world, before the Great Collapse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "Beings that surpassed mankind's potential,\x01",
            "and indeed, were almost god-like...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        "Indeed...I speak of the ancient dragons.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        (
            "#000FOh, hey! I remember hearing about\x01",
            "them in Sunday School!\x02\x03",

            "They were around in Liberl, too, up\x01",
            "until just a few decades ago, right?\x02\x03",

            "But they stopped showing up around\x01",
            "the time orbment technology was\x01",
            "first discovered.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #103
        0x102,
        "#014F...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #104
        0x101,
        (
            "#501FJoshua? You've got a real dumb\x01",
            "look on your face. Something\x01",
            "the matter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x102,
        (
            "#010FNo, nothing. I'm just surprised that\x01",
            "you actually remember something you\x01",
            "learned in school. Shocked, really.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        (
            "#009FHow rude!\x02\x03",

            "#000FOf course I paid attention. Huge,\x01",
            "cool things with wings like that?\x01",
            "I totally want to see one myself!\x02\x03",

            "#001FJust thinking about them gets me\x01",
            "all worked up!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 400)
    TurnDirection(0x102, 0xFE, 400)

    ChrTalk(    #107
        0xFE,
        (
            "Ha ha, I can relate! That's why I've\x01",
            "been journeying to exotic lands in\x01",
            "search of information.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3428")

    label("loc_3399")


    ChrTalk(    #108
        0xFE,
        (
            "Indeed, the subjects of my research are\x01",
            "the wise ones who lived in the old world,\x01",
            "before the Great Collapse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        "...The ancient dragons.\x02",
    )

    CloseMessageWindow()

    label("loc_3428")

    Jump("loc_3A9B")

    label("loc_342B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_35BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_351D")
    OP_A2(0x4)

    ChrTalk(    #110
        0xFE,
        (
            "It seems the development of orbal\x01",
            "arts was far superior before the\x01",
            "Great Collapse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "We're still discovering orbal relics\x01",
            "from that era!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "That's what people mean when they\x01",
            "say they've unearthed an 'artifact.'\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35BB")

    label("loc_351D")


    ChrTalk(    #113
        0xFE,
        (
            "We're still discovering orbal\x01",
            "relics from the era before the\x01",
            "Great Collapse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "That's what people mean when they\x01",
            "say they've unearthed an 'artifact.'\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35BB")

    Jump("loc_3A9B")

    label("loc_35BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_37A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36D1")
    OP_A2(0x4)

    ChrTalk(    #115
        0xFE,
        (
            "Are you familiar with the\x01",
            "'Great Collapse'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "Long ago, there existed a prosperous\x01",
            "society on this continent, contentedly\x01",
            "thriving on high-grade orbal arts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "Yet one day, all of that was\x01",
            "destroyed by a cataclysm we\x01",
            "call the 'Great Collapse.'\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_379E")

    label("loc_36D1")


    ChrTalk(    #118
        0xFE,
        (
            "Long ago, there existed a prosperous\x01",
            "society on this continent, contentedly\x01",
            "thriving on high-grade orbal arts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "Yet one day, all of that was\x01",
            "destroyed by a cataclysm we\x01",
            "call the 'Great Collapse'.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_379E")

    Jump("loc_3A9B")

    label("loc_37A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_3A9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_398F")
    OP_A2(0x4)

    ChrTalk(    #120
        0xFE,
        (
            "I'm a scholar specializing in\x01",
            "living beings from days long\x01",
            "past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "And on the subject of peculiar living beings, I\x01",
            "encountered the most uniquely swift monster I've\x01",
            "ever seen during a recent geological survey.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "That was...along the road in\x01",
            "West Bose, if I'm not mistaken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "Having never seen such a creature before,\x01",
            "I thought to capture it, but it was far\x01",
            "too quick for these legs of mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "I'd best get some more exercise\x01",
            "in my daily regimen, I surmise!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A9B")

    label("loc_398F")


    ChrTalk(    #125
        0xFE,
        (
            "And on the subject of peculiar living beings, I\x01",
            "encountered the most uniquely swift monster I've\x01",
            "ever seen during a recent geological survey.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "Having never seen such a creature before,\x01",
            "I thought to capture it, but it was far\x01",
            "too quick for these legs of mine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A9B")

    TalkEnd(0xC)
    Return()

    # Function_11_2B90 end

    def Function_12_3A9F(): pass

    label("Function_12_3A9F")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_3C4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BA3")
    OP_A2(0x5)

    ChrTalk(    #127
        0xFE,
        (
            "Mirano, of the Trino household, is kinda\x01",
            "like the vice mayor, 'cept she also kinda\x01",
            "runs the place all by herself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "The Borden household is pretty influential\x01",
            "too, sure...but Ms. Mirano's the real shadow\x01",
            "mayor here, hands down.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C4A")

    label("loc_3BA3")


    ChrTalk(    #129
        0xFE,
        (
            "No clue what's gonna happen to\x01",
            "me now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "Helping out Ms. Mirano ain't so bad, but I\x01",
            "can't help feeling like there's something\x01",
            "better for me out there, y'know?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C4A")

    Jump("loc_3F92")

    label("loc_3C4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_3ED4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DF8")
    OP_A2(0x5)

    ChrTalk(    #131
        0xFE,
        (
            "Ms. Mirano suddenly gave me the day off.\x01",
            "No rhyme or reason, far's I can tell!\x01",
            "What the heck is she up to...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "With the airships grounded, maybe\x01",
            "she just feels like we ain't gonna\x01",
            "get any work done anyway...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "When we get busy like this,\x01",
            "I always feel like I should be\x01",
            "doing a million things at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "Well, if I'm to take a holiday\x01",
            "today, then so be it. I'll get\x01",
            "nothing done and like it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3ED1")

    label("loc_3DF8")


    ChrTalk(    #135
        0xFE,
        (
            "Ms. Mirano suddenly gave me the day off.\x01",
            "No rhyme or reason, far's I can tell!\x01",
            "What the heck is she up to...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "With the airships grounded, maybe\x01",
            "she just feels like we ain't gonna\x01",
            "get any work done anyway...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ED1")

    Jump("loc_3F92")

    label("loc_3ED4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_3F92")

    ChrTalk(    #137
        0xFE,
        (
            "*sigh* ...Being Ms. Mirano's attendant\x01",
            "is exhausting work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "But it's precisely because of the power\x01",
            "she wields that she's earned the dubious\x01",
            "role of shadow mayor, I suppose!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F92")

    TalkEnd(0xD)
    Return()

    # Function_12_3A9F end

    def Function_13_3F96(): pass

    label("Function_13_3F96")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6793")
    ClearMapFlags(0x1)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -7020, 1500, -2310, 180)
    SetChrPos(0x102, -5070, 1500, -2700, 225)
    SetChrPos(0x103, -6250, 1500, -1960, 180)
    OP_6D(-7050, 1500, -2350, 0)
    OP_0D()
    OP_A2(0x318)
    OP_28(0x36, 0x4, 0x2)
    OP_28(0x36, 0x4, 0x4)
    OP_28(0x36, 0x1, 0x1)
    OP_28(0xE, 0x4, 0x40)
    OP_28(0x15, 0x4, 0x40)

    ChrTalk(    #139
        0xE,
        (
            "#145FOooooh...\x01",
            "Goddamn it...\x02\x03",

            "...This ain't a joke, you know!\x02\x03",

            "Uggh... *hic*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x101,
        (
            "#002F#4PWell, we found him...but he's\x01",
            "drunk off his ass.\x02\x03",

            "Was having his article rejected\x01",
            "really THAT MUCH of a shock to\x01",
            "his system?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x103,
        (
            "#027FHe's just acting like the man he is.\x01",
            "Men ARE pigs, after all...\x02\x03",

            "Though he seems to have forgotten that\x01",
            "alcohol is a drink to be consumed, not\x01",
            "a drink to be consumed BY.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 270, 0)
    OP_8C(0x101, 90, 400)

    ChrTalk(    #142
        0x101,
        (
            "#007FYou're one to talk! Don't they sometimes\x01",
            "call you 'Bottomless Schera'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x103,
        (
            "#020FOh, please. 'Bottomless' is much more\x01",
            "suitable for a woman like Aina.\x02\x03",

            "I, on the other hand, can HOLD my liquor.\x01",
            "No matter how much I may drink, my face\x01",
            "and my disposition remain unreddened.\x02\x03",

            "So don't you dare group a fun-loving\x01",
            "drinker like myself in the same category\x01",
            "as this clumsy lush!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x101,
        (
            "#009FOh, come now!\x02\x03",

            "When you get drunk, you lose it completely\x01",
            "and everyone around you gets a heck of a\x01",
            "show! Admit it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x102,
        (
            "#019F#4PIt's certainly true that Aina is like\x01",
            "a bucket to Schera's sieve.\x02\x03",

            "But no matter how you look at it,\x01",
            "they're both pretty bottomless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x103,
        "#022FI'm sensing disrespect, children...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xE,
        "#145F...Ooooh...\x02",
    )

    CloseMessageWindow()

    def lambda_4487():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4487)

    def lambda_4495():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4495)
    OP_6D(-7050, 1500, -2800, 1000)
    OP_62(0xE, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(300)
    SetChrSubChip(0xE, 0)
    Sleep(900)

    ChrTalk(    #148
        0xE,
        "#142FWh-Where am I...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x102,
        (
            "#010F#4PGood. You're awake...sort of.\x01",
            "Drinking so much is NOT good\x01",
            "for your health, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xE,
        "#145FOooogh, my head...\x02",
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    SetChrSubChip(0xE, 1)
    Sleep(500)

    ChrTalk(    #151
        0xE,
        (
            "#143F...Wh-What the...? You're that\x01",
            "bracer trainee, aren't you?\x02\x03",

            "Oh, my Goddess...what the hell\x01",
            "am I doing in Rolent?!\x02\x03",

            "Thought I'd made my way\x01",
            "to Bose...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x101,
        (
            "#006FWhat are you mumbling about,\x01",
            "you sponge? You ARE in Bose!\x01",
            "And so are we!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xE,
        (
            "#145FOh... Well, damn, don't scare\x01",
            "me like that!\x02\x03",

            "#141F...Oooooh, and I see you've got\x01",
            "a lovely lass with you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x103,
        (
            "#020FName's Scherazard Harvey. The\x01",
            "pleasure's all yours, I'm sure.\x02\x03",

            "I'm the mentor of these two.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xE,
        (
            "#143FScherazard...\x02\x03",

            "Are you the infamous 'Silver Streak,'\x01",
            "by any chance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x103,
        (
            "#021FOh? You humble me, sir.\x01",
            "I take it you've heard of\x01",
            "me, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xE,
        (
            "#141FOnly rumors, I'm afraid.\x01",
            "But yes, I know your name.\x02\x03",

            "You're one of the top young\x01",
            "bracers, if I'm not mistaken.\x02\x03",

            "...Which means you three are here\x01",
            "to investigate the incident as well,\x01",
            "I suppose?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x103,
        (
            "#027FOh, so you DO have some brains\x01",
            "left in there after all that booze.\x01",
            "I'm impressed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x101,
        (
            "#000FYou find anything out?\x02\x03",

            "We saw you by the mayor's house.\x01",
            "You seemed pretty troubled...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xE,
        (
            "#145F(Damn! They saw that?!)\x02\x03",

            "#144FUh, yeah! I was looking for clues\x01",
            "and couldn't find any!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x101,
        "#008FThat's what I figured.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xE,
        (
            "#142FDamned army's regulations on the spread\x01",
            "of information really restrict what I'm\x01",
            "able to learn, anyway.\x02\x03",

            "And if I try to consult General Morgan at\x01",
            "the Haken Gate directly, I'll be held up\x01",
            "for inspection for who knows how long!\x02\x03",

            "So I figured I'd at least try to score an\x01",
            "interview with the legendarily voluptuous\x01",
            "mayor, but a maid turned me away outright!\x02\x03",

            "And to top it all off, that useless girl\x01",
            "kept screwing everything up. Everything!\x02\x03",

            "#145FOh, great Aidios! Tell me, what\x01",
            "did I do to deserve this shabby\x01",
            "life?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x101,
        (
            "#501FWell, you did try to do an exclusive\x01",
            "on the mayor's chest...\x02\x03",

            "But if you want information that\x01",
            "badly, we might share some of\x01",
            "ours with you.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #164
        0xE,
        "#143FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x101,
        (
            "#006FWe're actually investigating the\x01",
            "incident on Mayor Maybelle's\x01",
            "behalf right now.\x02\x03",

            "So naturally, we've met with the\x01",
            "mayor and General Morgan, too,\x01",
            "for that matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xE,
        "#143F...Holy crap. You serious?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x101,
        "#502FYep. Totally.\x02",
    )

    CloseMessageWindow()
    OP_62(0xE, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(    #168
        0xE,
        (
            "#147F...Scoooore! And the Goddess gets\x01",
            "a point! Blessed be the bounty of\x01",
            "Aidios!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE)
    Sleep(500)

    ChrTalk(    #169
        0xE,
        (
            "#144FPlease, I beg of you...tell me\x01",
            "everything! Every last detail!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x102,
        (
            "#015F#4PWe'll be glad to. However...\x02\x03",

            "#010F...Aren't you forgetting something,\x01",
            "Nial?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xE,
        "#143F#3PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x103,
        (
            "#027FHeh...information ain't free, you know.\x02\x03",

            "We'll scratch your back, but you need to scratch\x01",
            "ours first. And get that look off your face...\x01",
            "I totally do NOT mean that literally.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #173
        0xE,
        (
            "#142F#3PY-You want mira or something?\x02\x03",

            "My research funds are long-exhausted\x01",
            "at this point, I'm sorry to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x102,
        (
            "#010F#4PWe're not interested in your money.\x02\x03",

            "We just find it fascinating that\x01",
            "you made your way to Bose RIGHT\x01",
            "AFTER this incident occurred.\x02\x03",

            "Seems like you might have heard\x01",
            "some interesting things yourself.\x01",
            "That being the case...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xE,
        (
            "#145F#3PUgh. And here I thought you were\x01",
            "a nice kid. Turns out you're just\x01",
            "a slimy little leech like me!\x02\x03",

            "I'll tell you what I know, but\x01",
            "rest assured, it's not big news\x01",
            "by any stretch of the imagination.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x102,
        (
            "#010F#4PAs long as it's related to the\x01",
            "incident, no matter how trivial\x01",
            "it may seem, I'll take it.\x02\x03",

            "#019FJust...don't be stingy. Give it\x01",
            "to us straight, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xE,
        (
            "#144F#3PFine, fine! I'll tell you everything,\x01",
            "on my honor as a newsman!\x02\x03",

            "I've got two clues to share, so if\x01",
            "you're taking notes, I suggest you\x01",
            "get out your pen and paper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x102,
        "#011F#4PWe're ready whenever you are.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 400)

    ChrTalk(    #179
        0x101,
        (
            "#006F#6P(Man, way to go, Joshua!\x01",
            "You're on a roll!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x103,
        (
            "#021F(Heh. Well, if he ever gets tired of being a\x01",
            "bracer, we know he'll have a bright future\x01",
            "in racketeering with those skills!)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(3330, 0, -1410, 0)
    SetChrSubChip(0xE, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0xE, 0x4)
    SetChrPos(0x101, 5100, 200, -1040, 270)
    SetChrPos(0x102, 5100, 200, -2450, 270)
    SetChrPos(0x103, 2950, 200, -2590, 90)
    SetChrPos(0xE, 2950, 0, -1070, 90)
    SetChrChipByIndex(0x101, 20)
    SetChrChipByIndex(0x102, 21)
    SetChrChipByIndex(0x103, 22)
    SetChrSubChip(0x102, 2)
    SetChrSubChip(0x103, 1)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #181
        0xE,
        (
            "#140FThe first clue is in the form of\x01",
            "an eyewitness report from the\x01",
            "village of Ravennue, to the west.\x02\x03",

            "I talked to a villager who'd just\x01",
            "come to Bose for a visit, and she\x01",
            "told me something very interesting.\x02\x03",

            "Apparently, she knows a kid who\x01",
            "saw a huge shadow flying overhead\x01",
            "on the night of the incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x101,
        "#004FA huge shadow flying overhead...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xE,
        (
            "#142FYep. Airship, I told 'em.\x01",
            "Maybe even that missing one!\x02\x03",

            "#145FBut the army checked it out\x01",
            "and found absolutely nothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x101,
        (
            "#007FAww, you meanie. You raised our\x01",
            "hopes, only to dash 'em straight\x01",
            "away!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x103,
        (
            "#020FSo you're saying somebody saw\x01",
            "something, but it was probably\x01",
            "unrelated to anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xE,
        (
            "#144FThat's what I'm saying! I warned\x01",
            "you it wasn't big news!\x02\x03",

            "And I went to a lot of trouble to get\x01",
            "this sad morsel, too, what with that\x01",
            "information embargo in place and all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x102,
        (
            "#010F#6PWell done. Now, let's hear\x01",
            "that second clue of yours.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 2)
    Sleep(300)

    ChrTalk(    #188
        0xE,
        (
            "#142FUgh...fine.\x02\x03",

            "The other thing I learned is that the\x01",
            "military's Intelligence Division is\x01",
            "on the move.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x101,
        "#004FIntelligence Division?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x103,
        (
            "#020FI've heard rumors about them.\x02\x03",

            "It's a new royally-sanctioned branch\x01",
            "of the army in charge of intelligence\x01",
            "gathering and dissemination.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xE,
        (
            "#140FThat's the one, yeah. Supposedly, they're\x01",
            "so elite they can even stand toe-to-toe\x01",
            "with the royal bodyguards.\x02\x03",

            "The man they put in charge, Colonel\x01",
            "Richard, is apparently quite the whiz kid.\x02\x03",

            "With him on the case, they say this\x01",
            "incident is as good as solved already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x101,
        (
            "#501FHmmm...\x02\x03",

            "Doesn't seem like your information\x01",
            "will be of much use to us in our\x01",
            "investigation.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0)
    Sleep(300)

    ChrTalk(    #193
        0xE,
        (
            "#144FYeah, well, can't say I didn't warn you!\x01",
            "Sorry I couldn't help much on your end.\x02\x03",

            "But a promise is a promise! I\x01",
            "scratched. Now it's your turn!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x102,
        (
            "#019F#6POf course. A deal IS a deal,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #195
        (
            "\x07\x05Joshua told Nial all about the incident in Rolent, as well as the information\x01",
            "received from General Morgan.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #196
        0xE,
        (
            "#143FThe Capuas? Sky bandits? A ransom\x01",
            "demand to the royal house and the\x01",
            "airship corporations?!\x02\x03",

            "#147FGood Goddess, that's exactly what\x01",
            "I needed! That's the missing link\x01",
            "I've been killing myself to find!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x102,
        "#010F#6PCaught your fancy, did it?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 2)
    Sleep(300)

    ChrTalk(    #198
        0xE,
        (
            "#141FAbsolutely! I can definitely write\x01",
            "my article now!\x02\x03",

            "I can't be wasting my time getting\x01",
            "drunk here...I have to find Dorothy,\x01",
            "post haste!\x02\x03",

            "#144FSee you later, you wonderful\x01",
            "people, you!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xE, 0, 0)
    SetChrChipByIndex(0xE, 23)
    OP_96(0xE, 0xBAE, 0x0, 0xFFFFFF88, 0x258, 0x1F40)
    OP_43(0x101, 0x2, 0x0, 0x1C)

    def lambda_5E4D():
        OP_6D(2130, 0, -2640, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5E4D)
    OP_8E(0xE, 0x5D2, 0x0, 0xFFFFFE8E, 0x1770, 0x1)
    OP_8E(0xE, 0x6E, 0xC8, 0xFFFFE9B2, 0x1770, 0x1)

    def lambda_5E8D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5E8D)
    OP_8E(0xE, 0x32, 0xC8, 0xFFFFE0C0, 0xBB8, 0x0)
    SetChrFlags(0xE, 0x80)
    WaitChrThread(0x101, 0x3)
    OP_62(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #199
        0x101,
        (
            "#004FWow. His spirits certainly lifted\x01",
            "fast!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5F0B():
        OP_6D(3330, 0, -1410, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5F0B)
    Sleep(500)
    SetChrSubChip(0x102, 0)
    Sleep(100)
    SetChrSubChip(0x102, 2)
    Sleep(100)
    SetChrSubChip(0x103, 0)
    Sleep(300)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #200
        0x102,
        (
            "#010F#6PWell, he was chasing a big story\x01",
            "pretty unsuccessfully until we\x01",
            "came along. It's only natural.\x02\x03",

            "I'm glad we could help him out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x101,
        (
            "#006F#4PWell, look at you. From Mr.\x01",
            "I'll-Break-Your-Kneecaps-If-You-Don't-Talk\x01",
            "to Mr. Nice Guy in under a minute!\x02\x03",

            "Talk about a split personality!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x102,
        (
            "#019F#6PStop thinking weird things about\x01",
            "me.\x02\x03",

            "I was just negotiating. A little\x01",
            "give-and-take, nothing more!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x103,
        (
            "#020FHee hee. A bad boy exterior with a good\x01",
            "boy inside, or is it the other way 'round?\x01",
            "Either way, I'm sure the girls love it.\x02\x03",

            "But anyway, I guess we've only really\x01",
            "dealt with scrupulous people thus far.\x01",
            "We're pretty lucky, in that regard.\x02\x03",

            "Start dealing with weirdos, and that's\x01",
            "when you'll need to bust out some REALLY\x01",
            "questionable negotiation techniques.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #204
        0x101,
        (
            "#007F#4P...Why were you looking at ME when\x01",
            "you said that...?\x02\x03",

            "#006FAnyway, that aside...\x02\x03",

            "...Was anyone else a little bothered\x01",
            "when Nial talked about that huge,\x01",
            "flying shadow thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x102,
        (
            "#014F#6PThat eyewitness report from\x01",
            "Ravennue?\x02\x03",

            "I'd say there's a strong chance\x01",
            "there was nothing to it, if the\x01",
            "army already checked it out...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x101,
        (
            "#006F#4PYeah, but I mean, it's not like\x01",
            "the army is totally infallible.\x01",
            "They could've missed something!\x02\x03",

            "It wasn't General Morgan himself, after\x01",
            "all, but one of his men. And some of\x01",
            "those guys are pretty thick-headed!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x102,
        (
            "#015F#6PThat is true...\x02\x03",

            "#010FProbably worth looking into.\x01",
            "Certainly can't hurt, at any\x01",
            "rate.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 2)), scpexpr(EXPR_END)), "loc_6591")

    ChrTalk(    #208
        0x103,
        (
            "#021FHeh. You two are starting to get\x01",
            "the hang of this, I see.\x02\x03",

            "#020FI think this is a splendid idea.\x01",
            "Let's head to Ravennue, then,\x01",
            "shall we?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66DB")

    label("loc_6591")


    ChrTalk(    #209
        0x103,
        (
            "#021FHeh. You two are starting to get\x01",
            "the hang of this, I see.\x02\x03",

            "#020FRavennue is a small village in\x01",
            "the west. It thrives on fruit\x01",
            "cultivation and exporting.\x02\x03",

            "Best way to get there is to head out\x01",
            "onto the West Bose roads for a bit,\x01",
            "then turn north onto the mountain trail.\x02\x03",

            "At which point, we'll be just a\x01",
            "stone's throw away!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66DB")


    ChrTalk(    #210
        0x101,
        "#006F#4PGot it!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0xE, 0x4)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrPos(0x101, 1150, 0, -2300, 180)
    SetChrPos(0x103, 1150, 0, -2300, 180)
    SetChrPos(0x102, 1150, 0, -2300, 180)
    OP_69(0x101, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Jump("loc_6A56")

    label("loc_6793")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_68D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6870")
    OP_A2(0x6)

    ChrTalk(    #211
        0xE,
        "#146F*hic*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x101,
        (
            "#000FUh, hello? Nial?\x01",
            "You in there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xE,
        (
            "#146F...\x02\x03",

            "Gonna...have to...just...\x01",
            "make something up...\x01",
            "Nobody'll know...the difference...\x02\x03",

            "*hic*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x102,
        "#017FIt's no use. He's out of it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_68D3")

    label("loc_6870")


    ChrTalk(    #215
        0xE,
        (
            "#146F*hic*\x02\x03",

            "Gonna...have to...just...\x01",
            "make something up...\x01",
            "Nobody'll know...the difference...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68D3")

    Jump("loc_6A56")

    label("loc_68D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_6A56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A09")
    OP_A2(0x6)

    ChrTalk(    #216
        0x102,
        "#010FUhh...Nial?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xE,
        (
            "#146FHoooooo... *hic*\x02\x03",

            "...'n after I came all this way\x01",
            "from...Rolent...\x02\x03",

            "Gllllllggghh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x101,
        "#501FHe's pretty gloriously drunk.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x103,
        (
            "#020FI dunno. They say you're not drunk if\x01",
            "you can lie on the floor without holding\x01",
            "on, and he's not even off the chair yet.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A56")

    label("loc_6A09")


    ChrTalk(    #220
        0xE,
        (
            "#146FHoooooo... *hic*\x02\x03",

            "...'n after I came all this way\x01",
            "from...Rolent...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A56")

    TalkEnd(0xE)
    Return()

    # Function_13_3F96 end

    def Function_14_6A5A(): pass

    label("Function_14_6A5A")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_6B0E")

    ChrTalk(    #221
        0xFE,
        (
            "Don't know if it's because the crime\x01",
            "wave's been stopped or what, but man\x01",
            "do our customers seem happy lately!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        (
            "Peace is the best, for sure.\x01",
            "Nothing beats it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B62")

    label("loc_6B0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_6C5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BE7")
    OP_A2(0x7)

    ChrTalk(    #223
        0xFE,
        "Lots of bad tidings these days.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        (
            "Wonder if we should hire\x01",
            "some protection for around\x01",
            "the restaurant...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        (
            "If anything should happen to one\x01",
            "of our customers, we'd be in\x01",
            "serious trouble!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C57")

    label("loc_6BE7")


    ChrTalk(    #226
        0xFE,
        "Lots of bad tidings these days.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        (
            "Wonder if we should hire\x01",
            "some protection for around\x01",
            "the restaurant...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C57")

    Jump("loc_7B62")

    label("loc_6C5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_704B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x71, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FDF")
    OP_A2(0x38D)
    TurnDirection(0xFE, 0x104, 0)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0xFE, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    Sleep(400)

    ChrTalk(    #228
        0xFE,
        "Wh-Whoa, a-aren't you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        (
            "No, I'm sure of it, you're...\x01",
            "that guy...from before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x104,
        (
            "#030FWhat's up, my good managerial sir?\x01",
            "Thanks for the meal last time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        (
            "Oh, oh my... Didn't I have you\x01",
            "arrested already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        (
            "I-I guess I'm going to have to\x01",
            "report you again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x104,
        (
            "#035FNow, now, let's not do anything\x01",
            "brash, my friend...\x02\x03",

            "#030FYou guys are actually quite\x01",
            "blessed!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #234
        0x104,
        (
            "#035FTo have an owner with the eyes to recognize\x01",
            "the value of an artful man such as myself is\x01",
            "quite wondrous, truly!\x02\x03",

            "And she is an exquisite beauty, is\x01",
            "she not? Like a flower in bloom!\x02\x03",

            "#030FThe future of Anterose is as bright\x01",
            "as a field bathed eternally in the\x01",
            "noontime glow of a crisp, spring day!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x102,
        (
            "#018FI can't believe you'd defy the\x01",
            "owner like that. What kind of\x01",
            "manager ARE you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x101,
        "#007FTsk tsk.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7048")

    label("loc_6FDF")


    ChrTalk(    #237
        0xFE,
        (
            "Dear me... Consider this a managerial\x01",
            "failure on my part.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xFE,
        (
            "My sincerest apologies to the\x01",
            "owner.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7048")

    Jump("loc_7B62")

    label("loc_704B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_714A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_711A")
    OP_A2(0x7)

    ChrTalk(    #239
        0xFE,
        "So, uh...welcome, I guess!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x101,
        (
            "#002F(What's up with him? He seems\x01",
            "pretty depressed...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x102,
        (
            "#014F(Yeah, his shoulders are drooping\x01",
            "off the charts. Wonder if something\x01",
            "happened...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7147")

    label("loc_711A")


    ChrTalk(    #242
        0xFE,
        (
            "Ohh, what ever shall I tell the\x01",
            "owner?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7147")

    Jump("loc_7B62")

    label("loc_714A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_73BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72C3")
    OP_A2(0x7)

    ChrTalk(    #243
        0xFE,
        (
            "We're currently looking for an\x01",
            "in-house pianist...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0xFE,
        (
            "...But there seems to be no one\x01",
            "with the necessary skills anywhere\x01",
            "in this whole land!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        (
            "I shall speak with the owner and see\x01",
            "about summoning an imperial pianist\x01",
            "for the restaurant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x103,
        "#023FHmmm...pianist, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x101,
        (
            "#007FMan, when they say this is a high-\x01",
            "class joint, they're not kidding!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73B9")

    label("loc_72C3")


    ChrTalk(    #248
        0xFE,
        (
            "We're currently looking for an\x01",
            "in-house pianist...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        (
            "...But there seems to be no one\x01",
            "with the necessary skills anywhere\x01",
            "in this whole land!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xFE,
        (
            "I shall speak with the owner and see\x01",
            "about summoning an imperial pianist\x01",
            "for the restaurant.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73B9")

    Jump("loc_7B62")

    label("loc_73BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_75D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7571")
    OP_A2(0x7)

    ChrTalk(    #251
        0xFE,
        (
            "Thank you for your continued\x01",
            "patronage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xFE,
        (
            "I shall be anxiously awaiting\x01",
            "your next visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x101,
        (
            "#000FHmph. We were treated by the mayor\x01",
            "last time, and...how much did it\x01",
            "come out to be?\x02\x03",

            "#009FDon't think we'll ever be able\x01",
            "to come here again...not on our\x01",
            "salaries anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x102,
        (
            "#010FTrue...but you have to admit,\x01",
            "the food was worth the price.\x02\x03",

            "As expected, the food made by\x01",
            "professional chefs is something\x01",
            "else.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_75D2")

    label("loc_7571")


    ChrTalk(    #255
        0xFE,
        (
            "Thank you for your continued\x01",
            "patronage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        (
            "I shall be anxiously awaiting\x01",
            "your next visit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_75D2")

    Jump("loc_7B62")

    label("loc_75D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_7B62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x71, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A80")
    OP_A2(0x38C)

    ChrTalk(    #257
        0xFE,
        (
            "Good day to you, and welcome\x01",
            "to Anterose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xFE,
        "Do you have a reservation?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x101,
        (
            "#000FUm...nope!\x02\x03",

            "Is this a restaurant, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0xFE,
        "Tis as you say, yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        (
            "I am the manager, Lechter. I tend\x01",
            "to the restaurant's needs while\x01",
            "the owner is away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0xFE,
        (
            "Herein, the best-quality ingredients\x01",
            "and servers await you, amounting to the\x01",
            "greatest dining experience of your life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xFE,
        (
            "I personally guarantee that if you\x01",
            "partake of our delicacies, you will\x01",
            "emerge full and satisfied.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0xFE,
        (
            "Please, come this way. I will\x01",
            "gladly show you to a table.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x102,
        (
            "#010FWow, this guy's got a LOT of confidence\x01",
            "in his restaurant. And I must admit, it\x01",
            "certainly does look like a nice place...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x101,
        (
            "#501FYeah, but he's a bit pushy, don't you\x01",
            "think? I mean, when I see this place,\x01",
            "my first thought is, CHA-CHING.\x02\x03",

            "We'd go broke if we ate here!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 0)

    ChrTalk(    #267
        0x103,
        (
            "#020FHa ha. It's not cheap, that's\x01",
            "for certain.\x02\x03",

            "If one wished to stay for a full\x01",
            "course dinner...let's see...\x02\x03",

            "...It would require the bounty from\x01",
            "30 large monsters, at minimum, to\x01",
            "gather enough mira.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 0)

    ChrTalk(    #268
        0x101,
        (
            "#007FYeow. Yeah, not for me, thanks! At that price\x01",
            "I'll gladly go street vendor. Deep fried Pom,\x01",
            "Pom-on-a-stick, Poms-in-a-blanket...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B62")

    label("loc_7A80")


    ChrTalk(    #269
        0xFE,
        (
            "Herein, the best-quality ingredients\x01",
            "and servers await you, amounting to the\x01",
            "greatest dining experience of your life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0xFE,
        (
            "I personally guarantee that if you\x01",
            "partake of our delicacies, you will\x01",
            "emerge full and satisfied.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B62")

    TalkEnd(0xF)
    Return()

    # Function_14_6A5A end

    def Function_15_7B66(): pass

    label("Function_15_7B66")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_7C04")

    ChrTalk(    #271
        0xFE,
        (
            "Finally, we can stock up on\x01",
            "ingredients fairly and honestly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0xFE,
        (
            "Now I'll be able to work on\x01",
            "those new menu items I've\x01",
            "been dreaming up...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8411")

    label("loc_7C04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_7C9E")

    ChrTalk(    #273
        0xFE,
        "Gwen's got high hopes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xFE,
        (
            "She may yet carve a true niche\x01",
            "for herself here at Anterose...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0xFE,
        (
            "That's the impression I'm\x01",
            "getting, anyway.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8411")

    label("loc_7C9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_7E57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DC6")
    OP_A2(0x8)

    ChrTalk(    #276
        0xFE,
        (
            "I heard a shrill scream from the\x01",
            "manager the other day. The stuff\x01",
            "nightmares are made of, that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0xFE,
        (
            "I wonder what happened this\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xFE,
        (
            "I often hear that subdued shriek from him\x01",
            "when new staff members arrive, actually.\x01",
            "So I suppose there's nothing to worry about.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E54")

    label("loc_7DC6")


    ChrTalk(    #279
        0xFE,
        (
            "I heard a shrill scream from the\x01",
            "manager the other day. The stuff\x01",
            "nightmares are made of, that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0xFE,
        (
            "I wonder what happened this\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E54")

    Jump("loc_8411")

    label("loc_7E57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_8058")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FC5")
    OP_A2(0x8)

    ChrTalk(    #281
        0xFE,
        (
            "The previous owner would never,\x01",
            "ever listen to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xFE,
        (
            "But the current owner listens\x01",
            "to even the most minuscule of\x01",
            "nitpicks I may have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0xFE,
        (
            "I'm very grateful to her for\x01",
            "that. Very grateful indeed!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xFE,
        (
            "I mean, she DID make me chef without having\x01",
            "ever met me or seen my face, so I'm a LITTLE\x01",
            "worried about her mental stability. But still!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8055")

    label("loc_7FC5")


    ChrTalk(    #285
        0xFE,
        (
            "The current owner listens to\x01",
            "even the most minuscule of\x01",
            "nitpicks I may have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xFE,
        (
            "I'm very grateful to her for\x01",
            "that. Very grateful indeed!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8055")

    Jump("loc_8411")

    label("loc_8058")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_80EC")

    ChrTalk(    #287
        0xFE,
        "Cooking is an art and a culture.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xFE,
        (
            "It requires as much creativity as\x01",
            "anything and, of course, is just\x01",
            "as resistant to compromise.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8411")

    label("loc_80EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_8150")

    ChrTalk(    #289
        0xFE,
        (
            "Were you able to have as much\x01",
            "fun cooking as I do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0xFE,
        "Please, come again any time!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8411")

    label("loc_8150")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_8411")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_833A")
    OP_A2(0x8)

    ChrTalk(    #291
        0xFE,
        (
            "To a chef, each and every day is lived in pursuit\x01",
            "of flavor. When the flavor stops, it's time to put\x01",
            "the kitchen knife down once and for all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xFE,
        (
            "One must never be satisfied.\x01",
            "Recipes must never stop evolving!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0xFE,
        (
            "Complacency disqualifies you as\x01",
            "a chef. A complacent chef is no\x01",
            "chef at all, far as I'm concerned!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x101,
        (
            "#000FTh-This guy's pretty intense.\x01",
            "It's kinda scaring me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0x102,
        (
            "#010FYeah. He has the eyes of a pro.\x01",
            "A really skilled, really psycho\x01",
            "sort of pro.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8411")

    label("loc_833A")


    ChrTalk(    #296
        0xFE,
        (
            "To a chef, each and every day is lived in pursuit\x01",
            "of flavor. When the flavor stops, it's time to put\x01",
            "the kitchen knife down once and for all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0xFE,
        (
            "One must never be satisfied.\x01",
            "Recipes must never stop evolving!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8411")

    TalkEnd(0x10)
    Return()

    # Function_15_7B66 end

    def Function_16_8415(): pass

    label("Function_16_8415")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_8480")

    ChrTalk(    #298
        0xFE,
        "Thanks again for your help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xFE,
        (
            "You should drop by from time\x01",
            "to time for a bite to eat.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8DBE")

    label("loc_8480")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_8579")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_853C")
    OP_A2(0x9)

    ChrTalk(    #300
        0xFE,
        "Hey, listen to this!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0xFE,
        (
            "The head chef actually told ME\x01",
            "to make today's soup!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0xFE,
        (
            "Looks like all my late nights\x01",
            "of practicing soup-making are\x01",
            "about to pay off!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8576")

    label("loc_853C")


    ChrTalk(    #303
        0xFE,
        (
            "The head chef actually told ME\x01",
            "to make today's soup!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8576")

    Jump("loc_8DBE")

    label("loc_8579")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_86B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8649")
    OP_A2(0x9)

    ChrTalk(    #304
        0xFE,
        (
            "The head chef actually let me\x01",
            "make the soup recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0xFE,
        "First time since I came here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0xFE,
        (
            "I kept making and re-making it\x01",
            "over and over...and all that\x01",
            "time, he stayed by my side.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_86B3")

    label("loc_8649")


    ChrTalk(    #307
        0xFE,
        (
            "I am soooo psyched! I've gotta practice\x01",
            "even harder from now on! For good soup\x01",
            "...and great justice!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86B3")

    Jump("loc_8DBE")

    label("loc_86B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_8948")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_887B")
    OP_A2(0x9)

    ChrTalk(    #308
        0xFE,
        (
            "Our prized 'Grand Chardonnay' was drunk,\x01",
            "in full, free of charge. And the owner\x01",
            "seemed not to care at all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0xFE,
        (
            "She's about my age...so how can\x01",
            "she have her head so high in the\x01",
            "clouds about this?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0xFE,
        (
            "The manager, by contrast, practically\x01",
            "swallowed his tongue. I've never seen\x01",
            "anyone turn such an unholy shade of red!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0xFE,
        (
            "Well, I guess such an unnatural color\x01",
            "is a pretty natural reaction, all things\x01",
            "considered. Poor guy...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8945")

    label("loc_887B")


    ChrTalk(    #312
        0xFE,
        (
            "Our prized 'Grand Chardonnay' was drunk,\x01",
            "in full, free of charge. And the owner\x01",
            "seemed not to care at all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0xFE,
        (
            "She's about my age...so how can\x01",
            "she have her head so high in the\x01",
            "clouds about this?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8945")

    Jump("loc_8DBE")

    label("loc_8948")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x3A7)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "OP_29(0x12, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x12, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_896C")
    Call(1, 0)
    Jump("loc_8DBE")

    label("loc_896C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_8AA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A31")
    OP_A2(0x9)

    ChrTalk(    #314
        0xFE,
        (
            "I used to work as a cook at a bar in Ruan,\x01",
            "but the owner here asked for me by name.\x01",
            "And how could I say no to that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0xFE,
        (
            "Apparently, she took a real\x01",
            "shine to my desserts.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A9E")

    label("loc_8A31")


    ChrTalk(    #316
        0xFE,
        (
            "I'm still learning the ropes here,\x01",
            "but I'm giving it everything I've\x01",
            "got. I mustn't let the owner down!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A9E")

    Jump("loc_8DBE")

    label("loc_8AA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_8C10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B99")
    OP_A2(0x9)

    ChrTalk(    #317
        0xFE,
        (
            "The head chef here is extremely strict.\x01",
            "He's a real kitchen nightmare!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0xFE,
        (
            "But he is known as the preeminent\x01",
            "chef in all of Liberl, and it's\x01",
            "not a title earned lightly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0xFE,
        (
            "His techniques and flavors are\x01",
            "second to none.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C0D")

    label("loc_8B99")


    ChrTalk(    #320
        0xFE,
        (
            "The head chef here is extremely strict.\x01",
            "But he can afford to be. His technique\x01",
            "and flavors are second to none.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C0D")

    Jump("loc_8DBE")

    label("loc_8C10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_8CB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C94")
    OP_A2(0x9)

    ChrTalk(    #321
        0xFE,
        (
            "Once these potatoes are peeled,\x01",
            "it's on to the carrots...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0xFE,
        (
            "I MUST PEEL AS I HAVE NEVER\x01",
            "PEELED BEFORE!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8CAD")

    label("loc_8C94")


    ChrTalk(    #323
        0xFE,
        "Busy, busy, busy...\x02",
    )

    CloseMessageWindow()

    label("loc_8CAD")

    Jump("loc_8DBE")

    label("loc_8CB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_8DBE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D7A")
    OP_A2(0x9)

    ChrTalk(    #324
        0xFE,
        (
            "It's amazing how tenacious the\x01",
            "head chef is about his flavors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0xFE,
        (
            "I'm trying to work on my flavors, too!\x01",
            "I even stayed in the kitchen all night\x01",
            "to perfect a new soup recipe!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8DBE")

    label("loc_8D7A")


    ChrTalk(    #326
        0xFE,
        (
            "It's amazing how tenacious the\x01",
            "head chef is about his flavors.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8DBE")

    TalkEnd(0x11)
    Return()

    # Function_16_8415 end

    def Function_17_8DC2(): pass

    label("Function_17_8DC2")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_8F27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E8C")
    OP_A2(0xB)

    ChrTalk(    #327
        0xFE,
        (
            "The wine I ordered finally\x01",
            "arrived on the last airship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0xFE,
        (
            "Our stock was beginning to dwindle\x01",
            "to a most worrisome level.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0xFE,
        (
            "We were in danger of running\x01",
            "out altogether.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F24")

    label("loc_8E8C")


    ChrTalk(    #330
        0xFE,
        (
            "The wine I ordered finally\x01",
            "arrived on the last airship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0xFE,
        (
            "It was quite a relief, as our\x01",
            "stock was dangerously low--\x01",
            "we almost ran out, in fact!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F24")

    Jump("loc_9654")

    label("loc_8F27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_9011")

    ChrTalk(    #332
        0xFE,
        (
            "Now that the airships are running\x01",
            "again, I'll finally be able to get\x01",
            "my wine shipments delivered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0xFE,
        (
            "The items were on the order list, yet\x01",
            "due to the embargo, we've run out here\x01",
            "at Anterose. And that simply won't do!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9654")

    label("loc_9011")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_9179")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_90FE")
    OP_A2(0xB)

    ChrTalk(    #334
        0xFE,
        "I'm not sure what to do now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0xFE,
        (
            "My lovely 'Grand Chardonnay' was\x01",
            "downed completely while I was\x01",
            "out on break...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0xFE,
        (
            "The owner simply laughed it off,\x01",
            "but I do feel responsible for\x01",
            "not safeguarding it better.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9176")

    label("loc_90FE")


    ChrTalk(    #337
        0xFE,
        "I'm not sure what to do now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0xFE,
        (
            "My lovely 'Grand Chardonnay' was\x01",
            "downed completely while I was\x01",
            "out on break...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9176")

    Jump("loc_9654")

    label("loc_9179")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_93BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9324")
    OP_A2(0xB)

    ChrTalk(    #339
        0xFE,
        "I am originally from the Empire.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0xFE,
        (
            "One day, the owner of this restaurant\x01",
            "came to the establishment where I\x01",
            "worked, as an ordinary customer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0xFE,
        (
            "She loved the wine I picked for her\x01",
            "during her meal so much that shortly\x01",
            "afterward, I received a letter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0xFE,
        (
            "A letter inviting me to work\x01",
            "here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0xFE,
        (
            "I decided to at least come to Liberl\x01",
            "to see this restaurant and fell in\x01",
            "love with it at first sight.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_93B7")

    label("loc_9324")


    ChrTalk(    #344
        0xFE,
        (
            "Though admittedly, when I was\x01",
            "invited by the owner to work\x01",
            "here, I had my concerns.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0xFE,
        (
            "But she has...a certain charm\x01",
            "to her. So, here I am!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_93B7")

    Jump("loc_9654")

    label("loc_93BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_9558")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94E7")
    OP_A2(0xB)

    ChrTalk(    #346
        0xFE,
        "Dear me, dear me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0xFE,
        (
            "With the airships grounded,\x01",
            "I'm finding it impossible to\x01",
            "get my wine shipments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0xFE,
        (
            "For the moment, I suppose we can make\x01",
            "do with what's in the wine cellar...\x01",
            "but our stock will not last forever!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0xFE,
        (
            "I hope the airships begin running\x01",
            "again soon...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9555")

    label("loc_94E7")


    ChrTalk(    #350
        0xFE,
        "Dear me, dear me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0xFE,
        (
            "With the airships grounded,\x01",
            "I'm finding it impossible to\x01",
            "get my wine shipments.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9555")

    Jump("loc_9654")

    label("loc_9558")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_95C1")

    ChrTalk(    #352
        0xFE,
        "Thank you so very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0xFE,
        (
            "I look forward to your next visit\x01",
            "to our fine establishment.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9654")

    label("loc_95C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_9654")

    ChrTalk(    #354
        0xFE,
        "I am the sommelier here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0xFE,
        (
            "If you have any questions or concerns\x01",
            "regarding wine, I will be more than\x01",
            "happy to address them for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9654")

    TalkEnd(0x12)
    Return()

    # Function_17_8DC2 end

    def Function_18_9658(): pass

    label("Function_18_9658")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_9716")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_96CD")
    OP_A2(0xC)

    ChrTalk(    #356
        0xFE,
        "Welcome, welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0xFE,
        (
            "Here for a good meal? If so,\x01",
            "please, let me show you to a\x01",
            "table!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9713")

    label("loc_96CD")


    ChrTalk(    #358
        0xFE,
        (
            "Here for a good meal? If so,\x01",
            "please, let me show you to a\x01",
            "table!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9713")

    Jump("loc_9E25")

    label("loc_9716")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_97B0")

    ChrTalk(    #359
        0xFE,
        (
            "I've been commissioned by the\x01",
            "head chef...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0xFE,
        (
            "I'm to go to Bose Market after\x01",
            "closing to purchase the necessary\x01",
            "ingredients for tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E25")

    label("loc_97B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_9A1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9934")
    OP_A2(0xC)

    ChrTalk(    #361
        0xFE,
        (
            "Not long ago, a very important, very VALUABLE\x01",
            "bottle of wine was completely downed by a\x01",
            "customer. A NON-paying customer, mind you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0xFE,
        (
            "That was the first time in a while that I've\x01",
            "heard the manager let out his, um, special\x01",
            "cry of dismay. It's a shriek, really.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0xFE,
        (
            "It sounds just like a little girl...or someone\x01",
            "who's been kicked very smartly in the\x01",
            "bagpipes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A1B")

    label("loc_9934")


    ChrTalk(    #364
        0xFE,
        (
            "That was the first time in a while that I've\x01",
            "heard the manager let out his, um, special\x01",
            "cry of dismay. It's a shriek, really.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0xFE,
        (
            "It sounds just like a little girl...or someone\x01",
            "who's been kicked very smartly in the\x01",
            "bagpipes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A1B")

    Jump("loc_9E25")

    label("loc_9A1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_9BFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B6C")
    OP_A2(0xC)

    ChrTalk(    #366
        0xFE,
        (
            "I previously worked as a waitress\x01",
            "at a restaurant in Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0xFE,
        (
            "The owner of this establishment\x01",
            "happened by on business, and we\x01",
            "got to talking shop, so to speak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #368
        0xFE,
        (
            "The wages seemed much better\x01",
            "here than there, so I jokingly\x01",
            "said to her, give me a job!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0xFE,
        (
            "And that's when she told me\x01",
            "she was the owner.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9BF9")

    label("loc_9B6C")


    ChrTalk(    #370
        0xFE,
        (
            "And let me tell you, our owner\x01",
            "is a strong-willed lady who\x01",
            "always gets what she wants!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0xFE,
        (
            "The polar opposite of our\x01",
            "*sigh* manager...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9BF9")

    Jump("loc_9E25")

    label("loc_9BFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_9D6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D0D")
    OP_A2(0xC)

    ChrTalk(    #372
        0xFE,
        (
            "This restaurant's become more and\x01",
            "more popular each day since the\x01",
            "current owner took over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #373
        0xFE,
        (
            "And just about every member of\x01",
            "the staff here was hand-picked\x01",
            "specifically by her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0xFE,
        (
            "Though I'm the exception, I guess.\x01",
            "I came because I wanted to.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D67")

    label("loc_9D0D")


    ChrTalk(    #375
        0xFE,
        (
            "Just about every member of the\x01",
            "staff here was hand-picked\x01",
            "specifically by the owner.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D67")

    Jump("loc_9E25")

    label("loc_9D6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_9DC1")

    ChrTalk(    #376
        0xFE,
        (
            "Oh, hey, you were in here\x01",
            "before, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #377
        0xFE,
        "Did you forget something?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9E25")

    label("loc_9DC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_9E25")

    ChrTalk(    #378
        0xFE,
        "Welcome, welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #379
        0xFE,
        (
            "Here for a good meal? If so,\x01",
            "please, let me show you to a\x01",
            "table!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9E25")

    TalkEnd(0x13)
    Return()

    # Function_18_9658 end

    def Function_19_9E29(): pass

    label("Function_19_9E29")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_9F2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9ECD")
    OP_A2(0xD)

    ChrTalk(    #380
        0xFE,
        (
            "The airships are in service\x01",
            "again...finally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0xFE,
        (
            "I feel like I've done all I\x01",
            "can in Bose. I'm thinking of\x01",
            "returning to the capital...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F27")

    label("loc_9ECD")


    ChrTalk(    #382
        0xFE,
        (
            "I feel like I've done all I\x01",
            "can in Bose. I'm thinking of\x01",
            "returning to the capital...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F27")

    Jump("loc_A6FA")

    label("loc_9F2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_A0CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A031")
    OP_A2(0xD)

    ChrTalk(    #383
        0xFE,
        (
            "When I first came here from the\x01",
            "capital, I traversed Valleria\x01",
            "Lake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #384
        0xFE,
        (
            "During that voyage, I saw a quaint,\x01",
            "charming-looking inn along its banks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0xFE,
        (
            "Ever since, I've wanted to spend\x01",
            "a night there. If only I could\x01",
            "remember its name...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A0C9")

    label("loc_A031")


    ChrTalk(    #386
        0xFE,
        (
            "When I first came here from the\x01",
            "capital, I traversed Valleria\x01",
            "Lake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #387
        0xFE,
        (
            "During that voyage, I saw a quaint,\x01",
            "charming-looking inn along its banks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A0C9")

    Jump("loc_A6FA")

    label("loc_A0CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_A20B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A1B5")
    OP_A2(0xD)

    ChrTalk(    #388
        0xFE,
        "I don't care much for soldiers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #389
        0xFE,
        (
            "They tend to be boorish and\x01",
            "overbearing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #390
        0xFE,
        (
            "Why must they behave so?\x01",
            "Why can't they just act\x01",
            "their ages?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #391
        0xFE,
        (
            "Of course, I know they're not\x01",
            "ALL like that, but still...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A208")

    label("loc_A1B5")


    ChrTalk(    #392
        0xFE,
        "I don't care much for soldiers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #393
        0xFE,
        (
            "They tend to be boorish and\x01",
            "overbearing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A208")

    Jump("loc_A6FA")

    label("loc_A20B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_A375")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A2F5")
    OP_A2(0xD)

    ChrTalk(    #394
        0xFE,
        (
            "There is a town to the northwest\x01",
            "of here where the most delicious\x01",
            "fruits are grown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #395
        0xFE,
        (
            "Sadly, it lies partway up a mountain,\x01",
            "making it an impossible destination\x01",
            "for one such as myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #396
        0xFE,
        "Such a shame...\x02",
    )

    CloseMessageWindow()
    Jump("loc_A372")

    label("loc_A2F5")


    ChrTalk(    #397
        0xFE,
        (
            "Hmm...I suppose some of their\x01",
            "delicious fruits may be sold at\x01",
            "the market here, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #398
        0xFE,
        "I shall have to go take a look!\x02",
    )

    CloseMessageWindow()

    label("loc_A372")

    Jump("loc_A6FA")

    label("loc_A375")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_A54D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A4C2")
    OP_A2(0xD)

    ChrTalk(    #399
        0xFE,
        (
            "Is it true that all operation of\x01",
            "airships has been halted?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #400
        0xFE,
        (
            "I suppose I have no choice but to\x01",
            "prolong my vacation here, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #401
        0xFE,
        (
            "And since there's nothing I can\x01",
            "do about it, why worry? I might\x01",
            "as well enjoy it while I can!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #402
        0xFE,
        (
            "I can shop and eat as I wish.\x01",
            "I can spread my capitalist\x01",
            "wings and fly!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A54A")

    label("loc_A4C2")


    ChrTalk(    #403
        0xFE,
        (
            "Is it true that all operation\x01",
            "of airships has been halted?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #404
        0xFE,
        (
            "I suppose I have no choice but to\x01",
            "prolong my vacation here, then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A54A")

    Jump("loc_A6FA")

    label("loc_A54D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_A65F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A5E9")
    OP_A2(0xD)

    ChrTalk(    #405
        0xFE,
        (
            "This restaurant has a great\x01",
            "reputation even in Grancel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #406
        0xFE,
        (
            "I actually came from the capital\x01",
            "just to eat the food here, in fact.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A65C")

    label("loc_A5E9")


    ChrTalk(    #407
        0xFE,
        (
            "And indeed, it is flavorful\x01",
            "beyond compare.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #408
        0xFE,
        (
            "This is the first time I've ever\x01",
            "had such delectable dishes!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A65C")

    Jump("loc_A6FA")

    label("loc_A65F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_A6FA")

    ChrTalk(    #409
        0xFE,
        (
            "We've come from the capital\x01",
            "for food and shopping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #410
        0xFE,
        (
            "The capital is quite lively,\x01",
            "but I must admit, this town\x01",
            "gives it a run for its money!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A6FA")

    TalkEnd(0x14)
    Return()

    # Function_19_9E29 end

    def Function_20_A6FE(): pass

    label("Function_20_A6FE")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_A8B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A80C")
    OP_A2(0xE)

    ChrTalk(    #411
        0xFE,
        (
            "I think I'll vacation in the\x01",
            "Erebonian Empire next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #412
        0xFE,
        (
            "It's a fairly historic place with\x01",
            "a lot of great sights to see,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #413
        0xFE,
        (
            "Admittedly, though, it seems a\x01",
            "frightening prospect when I think\x01",
            "back to the events of ten years ago...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A8B2")

    label("loc_A80C")


    ChrTalk(    #414
        0xFE,
        (
            "I think I'll vacation in the\x01",
            "Erebonian Empire next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #415
        0xFE,
        (
            "Admittedly, though, it seems a\x01",
            "frightening prospect when I think\x01",
            "back to the events of ten years ago...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A8B2")

    Jump("loc_B06A")

    label("loc_A8B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_A966")

    ChrTalk(    #416
        0xFE,
        (
            "My stay here has been unexpectedly\x01",
            "prolonged by delays from the airship\x01",
            "incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #417
        0xFE,
        (
            "But, when in Romn, right?\x01",
            "I fully intend to enjoy my\x01",
            "forced vacation time!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B06A")

    label("loc_A966")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_AB0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA73")
    OP_A2(0xE)

    ChrTalk(    #418
        0xFE,
        (
            "I do understand where Marian is\x01",
            "coming from, but I find it hard\x01",
            "to agree with her assessment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #419
        0xFE,
        (
            "Although they're just soldiers like anyone else,\x01",
            "I find the members of Her Royal Highness' personal\x01",
            "guards to be most polite and understanding.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB08")

    label("loc_AA73")


    ChrTalk(    #420
        0xFE,
        (
            "Although they're just soldiers like anyone else,\x01",
            "I find the members of Her Royal Highness' personal\x01",
            "guards to be most polite and understanding.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB08")

    Jump("loc_B06A")

    label("loc_AB0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_ACC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC21")
    OP_A2(0xE)

    ChrTalk(    #421
        0xFE,
        (
            "So...Marian sure does like to\x01",
            "eat, no? It's amazing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #422
        0xFE,
        (
            "If I tell her there's delicious food\x01",
            "to be had, she's packed and ready to\x01",
            "go in a heartbeat!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #423
        0xFE,
        (
            "But, as such, I must admit that\x01",
            "I am never bored thanks to her\x01",
            "unbridled enthusiasm for viands.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ACBD")

    label("loc_AC21")


    ChrTalk(    #424
        0xFE,
        (
            "So...Marian sure does like to\x01",
            "eat, no? It's amazing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #425
        0xFE,
        (
            "If I tell her there's delicious food\x01",
            "to be had, she's packed and ready to\x01",
            "go in a heartbeat!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ACBD")

    Jump("loc_B06A")

    label("loc_ACC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_AE39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD91")
    OP_A2(0xE)

    ChrTalk(    #426
        0xFE,
        (
            "It's not just the food here that's\x01",
            "top-quality, but the wait staff\x01",
            "and service, as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #427
        0xFE,
        "Just look around!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #428
        0xFE,
        (
            "You can see signs of the owner's\x01",
            "dedication in every last detail.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE36")

    label("loc_AD91")


    ChrTalk(    #429
        0xFE,
        (
            "It's not just the food here that's\x01",
            "top-quality, but the wait staff\x01",
            "and service, as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #430
        0xFE,
        (
            "You can see signs of the owner's\x01",
            "dedication in every last detail.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE36")

    Jump("loc_B06A")

    label("loc_AE39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_AF67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF0A")
    OP_A2(0xE)

    ChrTalk(    #431
        0xFE,
        (
            "How absolutely scrumptious! The\x01",
            "things they can do with monster\x01",
            "eyes here is simply amazing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #432
        0xFE,
        (
            "I'm not sure if there's a single\x01",
            "restaurant in all of Grancel that\x01",
            "can even compare!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF64")

    label("loc_AF0A")


    ChrTalk(    #433
        0xFE,
        (
            "I'm not sure if there's a single\x01",
            "restaurant in all of Grancel that\x01",
            "can even compare!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AF64")

    Jump("loc_B06A")

    label("loc_AF67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_B06A")

    ChrTalk(    #434
        0xFE,
        (
            "I often vacation with Marian. We have\x01",
            "similar interests and obnoxious amounts\x01",
            "of money to spend on them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #435
        0xFE,
        (
            "Though my goal this time was more shopping than\x01",
            "food. One can never have too many Dinedile\x01",
            "wallets or Rhinocider salad bowls, after all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B06A")

    TalkEnd(0x15)
    Return()

    # Function_20_A6FE end

    def Function_21_B06E(): pass

    label("Function_21_B06E")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_B132")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B0F7")
    OP_A2(0xF)

    ChrTalk(    #436
        0xFE,
        (
            "At last, my very favorite wine\x01",
            "has been delivered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #437
        0xFE,
        (
            "I can't tell you how long I've\x01",
            "been waiting for it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B12F")

    label("loc_B0F7")


    ChrTalk(    #438
        0xFE,
        (
            "At last, my very favorite wine\x01",
            "has been delivered.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B12F")

    Jump("loc_BCB3")

    label("loc_B132")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_B2EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B23C")
    OP_A2(0xF)

    ChrTalk(    #439
        0xFE,
        (
            "I always think of days long past\x01",
            "whenever I visit the Bose Market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #440
        0xFE,
        (
            "Every time I go, it seems like another son\x01",
            "or daughter has inherited the family business.\x01",
            "The shopkeepers just keep getting younger!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #441
        0xFE,
        "It's quite heartening to see.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B2E9")

    label("loc_B23C")


    ChrTalk(    #442
        0xFE,
        (
            "Every time I go, it seems like another son\x01",
            "or daughter has inherited the family business.\x01",
            "The shopkeepers just keep getting younger!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #443
        0xFE,
        "It's quite heartening to see.\x02",
    )

    CloseMessageWindow()

    label("loc_B2E9")

    Jump("loc_BCB3")

    label("loc_B2EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_B5A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B4DF")
    OP_A2(0xF)

    ChrTalk(    #444
        0xFE,
        (
            "Like anywhere else, this place was reduced to\x01",
            "rubble during the Hundred Days War...but it was\x01",
            "also the quickest to rebuild when it was over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #445
        0xFE,
        (
            "Of course, there's a reason\x01",
            "for that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #446
        0xFE,
        (
            "The merchants all got together\x01",
            "and pooled their profits to\x01",
            "fund the revival effort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #447
        0xFE,
        (
            "Oh, sure, Bose merchants all love the freedom to\x01",
            "earn and spend at will...but when push comes to\x01",
            "shove, we'll band together every time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #448
        0xFE,
        (
            "I'm proud to have lived my\x01",
            "life as a Bose merchant.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B5A5")

    label("loc_B4DF")


    ChrTalk(    #449
        0xFE,
        (
            "Oh, sure, Bose merchants all love the freedom to\x01",
            "earn and spend at will...but when push comes to\x01",
            "shove, we'll band together every time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #450
        0xFE,
        (
            "I'm proud to have lived my\x01",
            "life as a Bose merchant.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B5A5")

    Jump("loc_BCB3")

    label("loc_B5A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_B816")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B738")
    OP_A2(0xF)

    ChrTalk(    #451
        0xFE,
        (
            "The market became great around\x01",
            "the time when that little lady's\x01",
            "pappy served as our mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #452
        0xFE,
        (
            "He was a real pioneer, pushing forward\x01",
            "all kinds of measures to promote commerce.\x01",
            "And clearly, it worked wonderfully!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #453
        0xFE,
        (
            "The current mayor then inherited\x01",
            "all of that from her pappy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #454
        0xFE,
        (
            "At first I didn't think much\x01",
            "of her, but she's really proven\x01",
            "herself a worthy successor.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B813")

    label("loc_B738")


    ChrTalk(    #455
        0xFE,
        (
            "The market became great around\x01",
            "the time when that little lady's\x01",
            "pappy served as our mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #456
        0xFE,
        (
            "He was a real pioneer, pushing forward\x01",
            "all kinds of measures to promote commerce.\x01",
            "And clearly, it worked wonderfully!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B813")

    Jump("loc_BCB3")

    label("loc_B816")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_BAA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B9CC")
    OP_A2(0xF)

    ChrTalk(    #457
        0xFE,
        (
            "The old market here was quite bare-\x01",
            "bones. Just some stalls lined up in\x01",
            "a vacant field--a common flea market!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #458
        0xFE,
        (
            "But the merchants back then were\x01",
            "made of even tougher stuff than\x01",
            "they are today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #459
        0xFE,
        (
            "There was the mayor's family, influential\x01",
            "as anything...and all the traders of the\x01",
            "Trino and Borden households...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #460
        0xFE,
        (
            "They all started in that common\x01",
            "flea market and worked their\x01",
            "way up to what they are today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BAA4")

    label("loc_B9CC")


    ChrTalk(    #461
        0xFE,
        (
            "There was the mayor's family, influential\x01",
            "as anything...and all the traders of the\x01",
            "Trino and Borden households...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #462
        0xFE,
        (
            "They all started in that common\x01",
            "flea market and worked their\x01",
            "way up to what they are today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BAA4")

    Jump("loc_BCB3")

    label("loc_BAA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_BB17")

    ChrTalk(    #463
        0xFE,
        (
            "I was a merchant in the Bose Market\x01",
            "back in the day, myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #464
        0xFE,
        "Though I'm quite retired, now.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BCB3")

    label("loc_BB17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_BCB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC2B")
    OP_A2(0xF)

    ChrTalk(    #465
        0xFE,
        (
            "Hot-hot-hot-HOT! Ahhhhh... Spicy food is JUST\x01",
            "the thing for an old man like myself. Brings\x01",
            "back the ol' appetite something fierce!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #466
        0xFE,
        (
            "I must say, this coriander-infused duck\x01",
            "dish really does the trick. I bet I could\x01",
            "eat another two of these, easy!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BCB3")

    label("loc_BC2B")


    ChrTalk(    #467
        0xFE,
        (
            "Hot-hot-hot-HOT! Ahhhhh... Spicy food is JUST\x01",
            "the thing for an old man like myself. Brings\x01",
            "back the ol' appetite something fierce!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BCB3")

    TalkEnd(0x16)
    Return()

    # Function_21_B06E end

    def Function_22_BCB7(): pass

    label("Function_22_BCB7")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_BDF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD99")
    OP_A2(0x10)

    ChrTalk(    #468
        0xFE,
        (
            "The soup today tastes\x01",
            "different than usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #469
        0xFE,
        (
            "It's a bit rough, but the ingredients\x01",
            "blend well to create a rather bold,\x01",
            "interesting flavor. I like it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #470
        0xFE,
        "Did they get a new chef or something?\x02",
    )

    CloseMessageWindow()
    Jump("loc_BDF5")

    label("loc_BD99")


    ChrTalk(    #471
        0xFE,
        (
            "The soup today tastes\x01",
            "different than usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #472
        0xFE,
        "Did they get a new chef or something?\x02",
    )

    CloseMessageWindow()

    label("loc_BDF5")

    Jump("loc_C36E")

    label("loc_BDF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_BE86")

    ChrTalk(    #473
        0xFE,
        (
            "So, here I am again, eating at\x01",
            "this restaurant like always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #474
        0xFE,
        (
            "I feel like that man on the other\x01",
            "end is making eyes at me...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C36E")

    label("loc_BE86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_BF0E")

    ChrTalk(    #475
        0xFE,
        (
            "My stars, whenever a man in uniform\x01",
            "shows up, I can't help but think of\x01",
            "the past...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #476
        0xFE,
        "It's been a long road for us...\x02",
    )

    CloseMessageWindow()
    Jump("loc_C36E")

    label("loc_BF0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_BFCE")

    ChrTalk(    #477
        0xFE,
        (
            "During the war, we weren't the only ones to\x01",
            "take heavy damage. Poor Ravennue Village\x01",
            "suffered the same fate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #478
        0xFE,
        (
            "So there are quite a lot of us\x01",
            "who share these awful memories.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C36E")

    label("loc_BFCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_C172")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C0FB")
    OP_A2(0x10)

    ChrTalk(    #479
        0xFE,
        (
            "Times certainly have changed, though.\x01",
            "Now, tourists from the empire come\x01",
            "here to Bose to buy our goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #480
        0xFE,
        (
            "I'm just not sure how I feel\x01",
            "about that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #481
        0xFE,
        (
            "I just keep thinking about all the men\x01",
            "and women who were lost to us during the\x01",
            "war. People who will never come back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C16F")

    label("loc_C0FB")


    ChrTalk(    #482
        0xFE,
        (
            "And now, Imperialists come here\x01",
            "all the time to buy our goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #483
        0xFE,
        (
            "I'm just not sure how I feel\x01",
            "about that...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C16F")

    Jump("loc_C36E")

    label("loc_C172")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_C1E7")

    ChrTalk(    #484
        0xFE,
        (
            "I came here often with my ol'\x01",
            "grandaddy way back when.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #485
        0xFE,
        (
            "Why, that must've been ten\x01",
            "years ago now!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C36E")

    label("loc_C1E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_C36E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C2E2")
    OP_A2(0x10)

    ChrTalk(    #486
        0xFE,
        (
            "And this flavor hasn't changed\x01",
            "one bit. It's as good as ever!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #487
        0xFE,
        (
            "I hear the owner of this place changed\x01",
            "a few years back, but the quality\x01",
            "certainly hasn't dropped any.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #488
        0xFE,
        (
            "If anything, the food's gotten\x01",
            "better since then!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C36E")

    label("loc_C2E2")


    ChrTalk(    #489
        0xFE,
        (
            "This restaurant is the best,\x01",
            "hands down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #490
        0xFE,
        (
            "The flavor of this food has\x01",
            "gotten better and better ever\x01",
            "since the new owner took over.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C36E")

    TalkEnd(0x17)
    Return()

    # Function_22_BCB7 end

    def Function_23_C372(): pass

    label("Function_23_C372")

    TalkBegin(0x18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_C3F9")

    ChrTalk(    #491
        0xFE,
        (
            "*sigh* Another day, another\x01",
            "failure of a business meeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #492
        0xFE,
        (
            "I just plain suck at making\x01",
            "successful transactions.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C757")

    label("loc_C3F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_C463")

    ChrTalk(    #493
        0xFE,
        (
            "Guess it's just not my nature.\x01",
            "Well, fine, then...how about\x01",
            "at THIS price? Is that better?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C757")

    label("loc_C463")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_C504")

    ChrTalk(    #494
        0xFE,
        (
            "*sigh* I just can't make a\x01",
            "deal here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #495
        0xFE,
        (
            "Why can't I close a deal to save my life?!\x01",
            "Is it my haircut? Bad body odor?\x01",
            "Great Aidios, do I smell?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C757")

    label("loc_C504")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_C5B9")

    ChrTalk(    #496
        0xFE,
        (
            "No, no, no...I absolutely MUST\x01",
            "get it for this price, right\x01",
            "here. I won't accept any less!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #497
        0xFE,
        (
            "To say something like that\x01",
            "at the very start...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #498
        0xFE,
        "Come on, please!\x02",
    )

    CloseMessageWindow()
    Jump("loc_C757")

    label("loc_C5B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_C628")

    ChrTalk(    #499
        0xFE,
        (
            "No, no...I understand your feelings.\x01",
            "So much that it hurts!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #500
        0xFE,
        "But we have a quota to meet...\x02",
    )

    CloseMessageWindow()
    Jump("loc_C757")

    label("loc_C628")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_C67F")

    ChrTalk(    #501
        0xFE,
        (
            "No, we're under strict regulations.\x01",
            "This price would never be accepted!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C757")

    label("loc_C67F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_C757")

    ChrTalk(    #502
        0xFE,
        (
            "Army regulations, along with the grounding\x01",
            "of the airships, have a definite effect on\x01",
            "business that cannot be ignored.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #503
        0xFE,
        (
            "I need to reopen negotiations\x01",
            "and get things squared away,\x01",
            "as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C757")

    TalkEnd(0x18)
    Return()

    # Function_23_C372 end

    def Function_24_C75B(): pass

    label("Function_24_C75B")

    TalkBegin(0x19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_C92C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C8A6")
    OP_A2(0x12)

    ChrTalk(    #504
        0xFE,
        (
            "We've been discussing the effect\x01",
            "this blockade will have on our\x01",
            "local economy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #505
        0xFE,
        (
            "I suspect the blockade will be\x01",
            "lifted soon enough, though,\x01",
            "making it all a moot point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #506
        0xFE,
        (
            "Keep your eyes on the prize...\x01",
            "That's my motto.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #507
        0xFE,
        (
            "I seem to have gotten myself wrapped\x01",
            "up in business discussions, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C929")

    label("loc_C8A6")


    ChrTalk(    #508
        0xFE,
        (
            "Keep your eyes on the prize...\x01",
            "That's my motto.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #509
        0xFE,
        (
            "I seem to have gotten myself wrapped\x01",
            "up in business discussions, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C929")

    Jump("loc_CD6C")

    label("loc_C92C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_C969")

    ChrTalk(    #510
        0xFE,
        "Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #511
        0xFE,
        "That's not a BAD price, per se...\x02",
    )

    CloseMessageWindow()
    Jump("loc_CD6C")

    label("loc_C969")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_CA2A")

    ChrTalk(    #512
        0xFE,
        (
            "Just pushing your goods on me without\x01",
            "ever sweetening the pot does NOT make\x01",
            "for successful negotiation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #513
        0xFE,
        (
            "Given the circumstances, I think\x01",
            "a discount is entirely appropriate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD6C")

    label("loc_CA2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_CAF9")

    ChrTalk(    #514
        0xFE,
        (
            "No, no, NO! If I take it for\x01",
            "that much money, I'm SURE to\x01",
            "suffer losses!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #515
        0xFE,
        (
            "I realize it's just words, but please,\x01",
            "listen to me. I'm trying to help here!\x01",
            "This is simply no way to negotiate!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD6C")

    label("loc_CAF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_CC08")

    ChrTalk(    #516
        0xFE,
        (
            "No, no, I've had my eye on this for a long,\x01",
            "long time now, and you're simply not giving\x01",
            "my offer the consideration you should!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #517
        0xFE,
        (
            "Try to look at the broader picture here.\x01",
            "This is a great price to offer for AFTER\x01",
            "the airships are running again, isn't it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD6C")

    label("loc_CC08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_CCB4")

    ChrTalk(    #518
        0xFE,
        (
            "You are so going to drive us out\x01",
            "of business if THAT'S the best\x01",
            "you can do...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #519
        0xFE,
        (
            "We're having a good discussion\x01",
            "here, aren't we? I bet you're\x01",
            "loving this!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD6C")

    label("loc_CCB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_CD6C")

    ChrTalk(    #520
        0xFE,
        (
            "We've begun running out of certain\x01",
            "goods here in Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #521
        0xFE,
        (
            "And while we have no means of eliminating\x01",
            "the problem, we can at least try to make\x01",
            "it better, if only slightly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CD6C")

    TalkEnd(0x19)
    Return()

    # Function_24_C75B end

    def Function_25_CD70(): pass

    label("Function_25_CD70")

    TalkBegin(0x1A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_CE1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CDDF")
    OP_A2(0x13)

    ChrTalk(    #522
        0xFE,
        (
            "I'm so nervous, I can't even\x01",
            "taste this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #523
        0xFE,
        "Heh. Seems almost like sacrilege.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CE1B")

    label("loc_CDDF")


    ChrTalk(    #524
        0xFE,
        (
            "I hope I'll be able to savor\x01",
            "my food next time I come.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CE1B")

    Jump("loc_CFDC")

    label("loc_CE1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_CF28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CEC5")
    OP_A2(0x13)

    ChrTalk(    #525
        0xFE,
        (
            "I wore my best outfit to come\x01",
            "here, but...I hope I don't seem\x01",
            "overdressed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #526
        0xFE,
        (
            "I'll need to be careful not to\x01",
            "drop any of my tableware...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF25")

    label("loc_CEC5")


    ChrTalk(    #527
        0xFE,
        (
            "I just get this sinking feeling\x01",
            "that I'm really out of my element\x01",
            "here. Pitiful, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF25")

    Jump("loc_CFDC")

    label("loc_CF28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_CFA0")

    ChrTalk(    #528
        0xFE,
        (
            "This is actually my first time\x01",
            "eating at a place this fancy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #529
        0xFE,
        (
            "I'm so afraid I'll embarrass\x01",
            "myself...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CFDC")

    label("loc_CFA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_CFDC")

    ChrTalk(    #530
        0xFE,
        (
            "Ah, well...wh-what should I\x01",
            "order, I wonder...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CFDC")

    TalkEnd(0x1A)
    Return()

    # Function_25_CD70 end

    def Function_26_CFE0(): pass

    label("Function_26_CFE0")

    TalkBegin(0x1B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_D15B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D0D9")
    OP_A2(0x14)

    ChrTalk(    #531
        0xFE,
        "Wowwee, that was delicious!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #532
        0xFE,
        (
            "Easy to see why this is Liberl's\x01",
            "most highly-rated restaurant,\x01",
            "that's for sure!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #533
        0xFE,
        (
            "It was definitely worth the\x01",
            "trip! ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #534
        0xFE,
        (
            "A little luxury makes for a nice\x01",
            "break every now and again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D158")

    label("loc_D0D9")


    ChrTalk(    #535
        0xFE,
        (
            "Easy to see why this is Liberl's\x01",
            "most highly-rated restaurant,\x01",
            "that's for sure!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #536
        0xFE,
        (
            "It was definitely worth the\x01",
            "trip! ㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D158")

    Jump("loc_D335")

    label("loc_D15B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_D225")

    ChrTalk(    #537
        0xFE,
        (
            "The two of us have been wanting\x01",
            "to come here forEVER now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #538
        0xFE,
        (
            "We worked our little tushes off, pardon\x01",
            "my Erebonian, to save up enough money to\x01",
            "afford a meal here. But it was worth it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D335")

    label("loc_D225")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_D292")

    ChrTalk(    #539
        0xFE,
        (
            "Oh, come now, what's with that\x01",
            "hunched posture? Sit up straight!\x01",
            "This is a fancy-pants place!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D335")

    label("loc_D292")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_D335")

    ChrTalk(    #540
        0xFE,
        (
            "My goodness, what a restaurant!\x01",
            "It's just as glorious as I'd\x01",
            "always hoped it would be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #541
        0xFE,
        (
            "But up until now, we've just\x01",
            "been admiring it from afar...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D335")

    TalkEnd(0x1B)
    Return()

    # Function_26_CFE0 end

    def Function_27_D339(): pass

    label("Function_27_D339")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-35680, 1500, 4059, 0)
    OP_67(0, 7500, -10000, 0)
    ClearChrFlags(0x8, 0x80)
    OP_44(0x8, 0xFF)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x134, 0x4)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x101, -53630, 1700, 4200, 270)
    SetChrPos(0x102, -54880, 1700, 2840, 0)
    SetChrPos(0x103, -54970, 1700, 5580, 180)
    SetChrPos(0x8, -56300, 1700, 4200, 90)
    SetChrPos(0x134, -56990, 1500, 5470, 135)
    SetChrChipByIndex(0x101, 20)
    SetChrChipByIndex(0x102, 21)
    SetChrChipByIndex(0x103, 22)
    FadeToBright(2000, 0)
    OP_6D(-55280, 1700, 4240, 6000)

    ChrTalk(    #542
        0x101,
        (
            "#004FTh-This restaurant looks super\x01",
            "expensive... Are we really going\x01",
            "to have a meeting here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #543
        0x8,
        (
            "#610FI often use this place for business\x01",
            "meetings. The food is quite good,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #544
        0x103,
        (
            "#020FI tell you what though, I had heard\x01",
            "the mayor of Bose was a woman...\x02\x03",

            "But I never imagined you would\x01",
            "be this young.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #545
        0x101,
        (
            "#000FBased on looks alone, I would\x01",
            "guess that you're only four or\x01",
            "five years older than me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #546
        0x8,
        (
            "#611FActually, I still feel like I'm\x01",
            "nothing more than an unworthy\x01",
            "successor to my father.\x02\x03",

            "My late father was the previous mayor, and all I\x01",
            "did was inherit the rights to the Bose Market and\x01",
            "the political foundation which he set up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #547
        0x102,
        (
            "#010F#3PThat's a...rather unvarnished self-\x01",
            "evaluation if I've ever heard one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #548
        0x8,
        (
            "#610FAfter all, I'm just the daughter of a\x01",
            "businessman, so there's no sense\x01",
            "in getting high hat about that.\x02\x03",

            "But anyway, would it be all right\x01",
            "to go over the details of my\x01",
            "request with you again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #549
        0x101,
        "#006FSure, that'd be fine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #550
        0x8,
        (
            "#612FWell, what I would like to ask that you do is\x01",
            "investigate the disappearance of the missing\x01",
            "airship and bring closure to the incident.\x02\x03",

            "I am of the opinion that bracers would bring about\x01",
            "much more desirable results concerning this\x01",
            "incident than the army is currently producing.\x02\x03",

            "The reason being: we're not fighting a war.\x01",
            "We're trying to find answers and solve a mystery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #551
        0x103,
        (
            "#027FWell I, for one, would be honored.\x01",
            "But don't you think that you're\x01",
            "overrating us just a bit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #552
        0x8,
        (
            "#611FEhh, just call it...a businesswoman's\x01",
            "prerogative.\x02\x03",

            "#615FThe fact of the matter is, an influential\x01",
            "businessman was aboard the airliner\x01",
            "that disappeared.\x02\x03",

            "In addition, if the Royal Army continues\x01",
            "to keep the Bose airspace as a no-fly\x01",
            "zone, business is going to suffer.\x02\x03",

            "And just when business had been\x01",
            "booming prior to the queen's birthday\x01",
            "celebration, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #553
        0x102,
        (
            "#012F#3PI see. So this is an economic\x01",
            "appeal, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #554
        0x8,
        (
            "#612FYes, and it's something which\x01",
            "I can't trust to be left up to\x01",
            "the army alone.\x02\x03",

            "So what do you think? Will you\x01",
            "accept my request for your help\x01",
            "in the matter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #555
        0x103,
        (
            "#025FWell, we have our own reasons for wanting\x01",
            "to investigate the incident, and we'd like\x01",
            "to accept the job, but...\x02\x03",

            "The army has actively been trying to\x01",
            "exclude bracers from anything having\x01",
            "to do with the incident.\x02\x03",

            "#020FSo, uh...I don't suppose you could pull\x01",
            "the mayor card for us, could you? Maybe\x01",
            "show the army who's running this show?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #556
        0x8,
        (
            "#612FExcluding bracers, huh...?\x01",
            "This must have something to\x01",
            "do with General Morgan, then.\x02\x03",

            "That man has disliked bracers from\x01",
            "the beginning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #557
        0x101,
        (
            "#004FSo you know who the general is,\x01",
            "Mayor Maybelle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #558
        0x8,
        (
            "#610FHe was a friend of my late father's. Tentatively\x01",
            "speaking, we have a passing acquaintance with\x01",
            "one another.\x02\x03",

            "So...I may just be able to do something for\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #559
        0x102,
        "#014F#3PMeaning...?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 1)
    Sleep(500)

    ChrTalk(    #560
        0x8,
        "#610FLila.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #561
        0x134,
        "#620FYes, madam.\x02",
    )

    CloseMessageWindow()
    OP_8E(0x134, 0xFFFF24D2, 0x5DC, 0x1374, 0x7D0, 0x0)
    TurnDirection(0x134, 0x8, 400)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #562
        (
            "\x07\x05Lila produced a sheet of letter paper and a fountain pen from her pocket\x01",
            "and handed them to Mayor Maybelle.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetChrSubChip(0x8, 0)
    Sleep(200)
    OP_8C(0x134, 315, 400)
    OP_8F(0x134, 0xFFFF2162, 0x5DC, 0x155E, 0x7D0, 0x0)
    OP_8C(0x134, 135, 400)

    ChrTalk(    #563
        0x8,
        (
            "#612F...\x02\x03",

            "...\x02\x03",

            "#615FI guess this should be sufficient.\x02\x03",

            "#610FHere, please take this with you.\x02",
        )
    )

    CloseMessageWindow()
    OP_3E(0x32D, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #564
        "\x07\x00Received \x07\x02Mayor Maybelle's Letter\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #565
        0x101,
        "#000FWhat's this letter for?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #566
        0x8,
        (
            "#610FIt's a letter of request to General\x01",
            "Morgan.\x02\x03",

            "It is to inform him of my request for\x01",
            "information about the incident as the\x01",
            "official responsible for the region.\x02\x03",

            "I think this should be enough to get\x01",
            "some information out of the army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #567
        0x101,
        (
            "#002FI see...\x02\x03",

            "But I wonder if that bracer-hating\x01",
            "general will even meet with us at\x01",
            "all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #568
        0x8,
        (
            "#610FI think it would be a pretty safe bet\x01",
            "as long as you hide your identities.\x02\x03",

            "You would probably be best served\x01",
            "by saying that you are messengers\x01",
            "for the mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #569
        0x101,
        (
            "#003FI don't know if I like the sound of\x01",
            "that. It feels like we're lying or\x01",
            "something...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #570
        0x102,
        (
            "#010F#3PIt's not lying. We'd just not be\x01",
            "telling him everything.\x02\x03",

            "Since this is a time-sensitive situation,\x01",
            "I think we should be practical about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #571
        0x101,
        (
            "#007F...I guess you're right, Joshua.\x02\x03",

            "#000FBy the way, where do we need to\x01",
            "go to meet General Morgan?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #572
        0x8,
        (
            "#610FThere's a fort called the Haken\x01",
            "Gate on the international border\x01",
            "to the north of Bose.\x02\x03",

            "You should be able to find the\x01",
            "general there.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0x33, 0xFF)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T1101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_27_D339 end

    def Function_28_E4C8(): pass

    label("Function_28_E4C8")

    Sleep(500)
    SetChrSubChip(0x102, 0)
    Sleep(200)
    SetChrSubChip(0x103, 0)
    Sleep(200)
    SetChrSubChip(0x101, 1)
    Sleep(200)
    SetChrSubChip(0x102, 1)
    Sleep(200)
    SetChrSubChip(0x103, 2)
    Return()

    # Function_28_E4C8 end

    SaveToFile()

Try(main)
