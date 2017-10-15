from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1132   ._SN',
        MapName             = 'Bose',
        Location            = 'T1132.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
        Flags               = 1,
        EntryFunctionIndex  = 12,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T1132_1 ._SN',
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
        'Barlowe',                              # 9
        'Dina',                                 # 10
        'Ambassador Crainagh',                  # 11
        'Jerrold',                              # 12
        'Jerrold',                              # 13
        'Secretary Barkley',                    # 14
        'Buck',                                 # 15
        'Trayton',                              # 16
        'Felicia',                              # 17
        'Pomme',                                # 18
        'Spence',                               # 19
        'Minuet',                               # 20
        'Libro',                                # 21
        'Emmy',                                 # 22
        'Hardt',                                # 23
        'Lore',                                 # 24
        'Tico',                                 # 25
        'Morie',                                # 26
        'Cecilia Passenger',                    # 27
        'Cecilia Passenger',                    # 28
        'Cecilia Passenger',                    # 29
        'Cecilia Passenger',                    # 30
        'Targeting Camera',                     # 31
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
        'ED6_DT07/CH01560 ._CH',             # 00
        'ED6_DT07/CH01350 ._CH',             # 01
        'ED6_DT27/CH03710 ._CH',             # 02
        'ED6_DT07/CH01570 ._CH',             # 03
        'ED6_DT07/CH01560 ._CH',             # 04
        'ED6_DT07/CH01140 ._CH',             # 05
        'ED6_DT07/CH01040 ._CH',             # 06
        'ED6_DT07/CH01130 ._CH',             # 07
        'ED6_DT07/CH01060 ._CH',             # 08
        'ED6_DT07/CH01000 ._CH',             # 09
        'ED6_DT07/CH01010 ._CH',             # 0A
        'ED6_DT07/CH01050 ._CH',             # 0B
        'ED6_DT07/CH01120 ._CH',             # 0C
        'ED6_DT07/CH01020 ._CH',             # 0D
        'ED6_DT07/CH01170 ._CH',             # 0E
        'ED6_DT07/CH01460 ._CH',             # 0F
    )

    AddCharChipPat(
        'ED6_DT07/CH01560P._CP',             # 00
        'ED6_DT07/CH01350P._CP',             # 01
        'ED6_DT27/CH03710P._CP',             # 02
        'ED6_DT07/CH01570P._CP',             # 03
        'ED6_DT07/CH01560P._CP',             # 04
        'ED6_DT07/CH01140P._CP',             # 05
        'ED6_DT07/CH01040P._CP',             # 06
        'ED6_DT07/CH01130P._CP',             # 07
        'ED6_DT07/CH01060P._CP',             # 08
        'ED6_DT07/CH01000P._CP',             # 09
        'ED6_DT07/CH01010P._CP',             # 0A
        'ED6_DT07/CH01050P._CP',             # 0B
        'ED6_DT07/CH01120P._CP',             # 0C
        'ED6_DT07/CH01020P._CP',             # 0D
        'ED6_DT07/CH01170P._CP',             # 0E
        'ED6_DT07/CH01460P._CP',             # 0F
    )

    DeclNpc(
        X                   = 4500,
        Z                   = 0,
        Y                   = 190600,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -49910,
        Z                   = 0,
        Y                   = 118350,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -122680,
        Z                   = 0,
        Y                   = 179240,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -126260,
        Z                   = 0,
        Y                   = 138000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -127460,
        Z                   = 0,
        Y                   = 181340,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -123490,
        Z                   = 0,
        Y                   = 178400,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -85120,
        Z                   = 0,
        Y                   = 121590,
        Direction           = 130,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -86580,
        Z                   = 0,
        Y                   = 119500,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -45690,
        Z                   = 0,
        Y                   = 152320,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = -48210,
        Z                   = 0,
        Y                   = 155300,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -49050,
        Z                   = 0,
        Y                   = 120240,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = -85770,
        Z                   = 0,
        Y                   = 152520,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = -85280,
        Z                   = 0,
        Y                   = 153820,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 4530,
        Z                   = 0,
        Y                   = 182260,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 6470,
        Z                   = 0,
        Y                   = 191180,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = -45610,
        Z                   = 0,
        Y                   = 153280,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = -88500,
        Z                   = 0,
        Y                   = 122920,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = -84260,
        Z                   = 0,
        Y                   = 119710,
        Direction           = 291,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = -49680,
        Z                   = 0,
        Y                   = 119810,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = -86090,
        Z                   = 0,
        Y                   = 151630,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = -82340,
        Z                   = 0,
        Y                   = 158280,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = -47150,
        Z                   = 0,
        Y                   = 152620,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 29,
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
        X                   = -126260,
        Y                   = 0,
        Z                   = 138000,
        Range               = 1000,
        Unknown_10          = 0x514,
        Unknown_14          = 0x0,
        Unknown_18          = 0x10040,
        Unknown_1C          = 0,
    )


    DeclActor(
        TriggerX            = 6598,
        TriggerZ            = 0,
        TriggerY            = 190158,
        TriggerRange        = 700,
        ActorX              = 4500,
        ActorZ              = 1500,
        ActorY              = 190662,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3130,
        TriggerZ            = 0,
        TriggerY            = 192000,
        TriggerRange        = 800,
        ActorX              = 3130,
        ActorZ              = 1000,
        ActorY              = 192000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 30,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_472",          # 00, 0
        "Function_1_668",          # 01, 1
        "Function_2_67B",          # 02, 2
        "Function_3_69F",          # 03, 3
        "Function_4_6EC",          # 04, 4
        "Function_5_710",          # 05, 5
        "Function_6_734",          # 06, 6
        "Function_7_758",          # 07, 7
        "Function_8_75D",          # 08, 8
        "Function_9_11AC",         # 09, 9
        "Function_10_1C1E",        # 0A, 10
        "Function_11_221D",        # 0B, 11
        "Function_12_281D",        # 0C, 12
        "Function_13_2DD6",        # 0D, 13
        "Function_14_3198",        # 0E, 14
        "Function_15_319D",        # 0F, 15
        "Function_16_36B7",        # 10, 16
        "Function_17_3A9D",        # 11, 17
        "Function_18_3D6B",        # 12, 18
        "Function_19_45C0",        # 13, 19
        "Function_20_4B7B",        # 14, 20
        "Function_21_5097",        # 15, 21
        "Function_22_54BB",        # 16, 22
        "Function_23_57C5",        # 17, 23
        "Function_24_59B1",        # 18, 24
        "Function_25_5BE0",        # 19, 25
        "Function_26_5D14",        # 1A, 26
        "Function_27_5E84",        # 1B, 27
        "Function_28_5EEB",        # 1C, 28
        "Function_29_5F76",        # 1D, 29
        "Function_30_6115",        # 1E, 30
    )


    def Function_0_472(): pass

    label("Function_0_472")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_48C")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    OP_43(0xA, 0x0, 0x6, 0x2)
    Event(1, 10)

    label("loc_48C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4F0")
    OP_B2(0x0, 0x0, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrPos(0x9, -124920, 0, 178920, 0)
    OP_43(0x9, 0x0, 0x0, 0x4)
    ClearChrFlags(0x18, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D9")
    ClearChrFlags(0x19, 0x80)
    Jump("loc_4ED")

    label("loc_4D9")

    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)

    label("loc_4ED")

    Jump("loc_600")

    label("loc_4F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_51F")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrPos(0x9, -126520, 0, 181820, 90)
    Jump("loc_600")

    label("loc_51F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_578")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x9, -42800, 0, 152070, 270)
    SetChrPos(0x16, -128430, 0, 128900, 270)
    Jump("loc_600")

    label("loc_578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_5C0")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x9, -130180, 0, 130460, 270)
    Jump("loc_600")

    label("loc_5C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_600")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x9, -130180, 0, 130460, 270)

    label("loc_600")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_623")
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)

    label("loc_623")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_667")
    SetChrPos(0xA, -123450, 0, 178760, 270)
    SetChrPos(0xD, -122420, 0, 179380, 270)
    SetChrPos(0xC, -128500, 0, 178640, 90)
    OP_43(0xA, 0x0, 0x6, 0x2)

    label("loc_667")

    Return()

    # Function_0_472 end

    def Function_1_668(): pass

    label("Function_1_668")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_67A")
    OP_10(0x1, 0x0)
    OP_10(0xE, 0x1)

    label("loc_67A")

    Return()

    # Function_1_668 end

    def Function_2_67B(): pass

    label("Function_2_67B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_69E")
    OP_8D(0xFE, 3860, 184520, 5490, 181970, 1500)
    Jump("Function_2_67B")

    label("loc_69E")

    Return()

    # Function_2_67B end

    def Function_3_69F(): pass

    label("Function_3_69F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6EB")
    OP_8E(0xFE, 0xFFFE20C8, 0x0, 0x2C2B8, 0x5DC, 0x0)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xFFFE20C8, 0x0, 0x2BC28, 0x5DC, 0x0)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    Jump("Function_3_69F")

    label("loc_6EB")

    Return()

    # Function_3_69F end

    def Function_4_6EC(): pass

    label("Function_4_6EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_70F")
    OP_8D(0xFE, -127570, 177960, -122660, 179600, 1000)
    Jump("Function_4_6EC")

    label("loc_70F")

    Return()

    # Function_4_6EC end

    def Function_5_710(): pass

    label("Function_5_710")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_733")
    OP_8D(0xFE, -51430, 121490, -47820, 118410, 1500)
    Jump("Function_5_710")

    label("loc_733")

    Return()

    # Function_5_710 end

    def Function_6_734(): pass

    label("Function_6_734")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_757")
    OP_8D(0xFE, -84580, 120430, -82970, 119500, 1500)
    Jump("Function_6_734")

    label("loc_757")

    Return()

    # Function_6_734 end

    def Function_7_758(): pass

    label("Function_7_758")

    Call(0, 8)
    Return()

    # Function_7_758 end

    def Function_8_75D(): pass

    label("Function_8_75D")

    TalkBegin(0x8)
    Call(6, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77A")
    OP_A9(0x35)
    TalkEnd(0x8)
    Return()

    label("loc_77A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_78B")
    TalkEnd(0x8)
    Return()

    label("loc_78B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_906")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87C")

    ChrTalk(    #0
        0x8,
        (
            "I wonder when the scheduled\x01",
            "liners will resume service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "There are people at our hotel who have\x01",
            "been waiting for their flights for ages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "As someone related to the tourism industry,\x01",
            "it's quite the headache.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_903")

    label("loc_87C")


    ChrTalk(    #3
        0x8,
        (
            "I wonder when the scheduled\x01",
            "liners will resume service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "As someone related to the tourism industry,\x01",
            "it's quite the headache.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_903")

    Jump("loc_11A8")

    label("loc_906")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_A6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E7")

    ChrTalk(    #5
        0x8,
        "Welcome to the Frieden Hotel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "Orbal devices may not be functioning,\x01",
            "but our hotel is still open for business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "I am sure there will be some inconveniences,\x01",
            "but please, enjoy your time here.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_A69")

    label("loc_9E7")


    ChrTalk(    #8
        0x8,
        (
            "Orbal devices may not be functioning,\x01",
            "but our hotel is still open for business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        "Please do not hesitate to patronize us.\x02",
    )

    CloseMessageWindow()

    label("loc_A69")

    Jump("loc_11A8")

    label("loc_A6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_BDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B17")

    ChrTalk(    #10
        0x8,
        (
            "We apologize for any inconvenience\x01",
            "during the market reconstruction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "As of now, we are operating as normal.\x01",
            "Please, relax and enjoy yourselves.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD7")

    label("loc_B17")


    ChrTalk(    #12
        0x8,
        "Welcome to the Frieden Hotel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "We apologize for any inconvenience\x01",
            "during the market reconstruction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "As of now, we are operating as normal.\x01",
            "Please, relax and enjoy yourselves.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_BD7")

    Jump("loc_11A8")

    label("loc_BDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_D6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_C82")

    ChrTalk(    #15
        0x8,
        (
            "It seems the market reconstruction\x01",
            "is proceeding smoothly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "I suppose we will be bidding farewell\x01",
            "to this mini-department store soon, then...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D69")

    label("loc_C82")


    ChrTalk(    #17
        0x8,
        (
            "It seems the market reconstruction\x01",
            "is proceeding smoothly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "I suppose we will be bidding farewell\x01",
            "to this mini-department store soon, then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "It'll feel a little lonely without all the\x01",
            "commotion when they're gone.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_D69")

    Jump("loc_11A8")

    label("loc_D6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_F3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E66")

    ChrTalk(    #20
        0x8,
        (
            "At the moment, our hotel is open for\x01",
            "the merchants of the market to use\x01",
            "as a temporary store front.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "It is the virtue of Bose merchants to come\x01",
            "together and help each other during times\x01",
            "of crisis. I am glad to offer my aid.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F3B")

    label("loc_E66")


    ChrTalk(    #22
        0x8,
        "Welcome to the Frieden Hotel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "At the moment, our hotel is open for\x01",
            "the merchants of the market to use\x01",
            "as a temporary store front.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "Mmmm, it almost has the atmosphere\x01",
            "of a little department store.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_F3B")

    Jump("loc_11A8")

    label("loc_F3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_1052")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F77")

    ChrTalk(    #25
        0x8,
        "Something terrible has happened...\x02",
    )

    CloseMessageWindow()
    Jump("loc_104F")

    label("loc_F77")


    ChrTalk(    #26
        0x8,
        "Something terrible occurred.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "In accordance with Mayor Maybelle's request,\x01",
            "our hotel has opened its rooms to provide\x01",
            "shelter for the merchants, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        "If that monster reappeared, what could we do...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_104F")

    Jump("loc_11A8")

    label("loc_1052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_11A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_10D0")

    ChrTalk(    #29
        0x8,
        "Welcome to the Frieden Hotel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        (
            "At the moment, our hotel is playing host\x01",
            "to the Imperial ambassador.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11A8")

    label("loc_10D0")


    ChrTalk(    #31
        0x8,
        "Welcome to the Frieden Hotel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "At the moment, our hotel is playing host\x01",
            "to the Imperial ambassador.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        (
            "For reasons of security, you may experience some\x01",
            "inconvenience, but we ask for your understanding.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_11A8")

    TalkEnd(0x8)
    Return()

    # Function_8_75D end

    def Function_9_11AC(): pass

    label("Function_9_11AC")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_13C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_131F")

    ChrTalk(    #34
        0xFE,
        (
            "The guests that are here right now have\x01",
            "all been stranded since the airships are\x01",
            "grounded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        "I do feel bad for them, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "If you ask me, THEY should feel bad for me\x01",
            "because of all this extra work I have now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "And here I was thinking I'd go check out\x01",
            "the sale the market's running today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        "*sigh* This really is a disaster.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_13BF")

    label("loc_131F")


    ChrTalk(    #39
        0xFE,
        (
            "Well, I do feel bad for the stranded\x01",
            "airship passengers, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "If you ask me, THEY should feel bad for me\x01",
            "because of all this extra work I have now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13BF")

    Jump("loc_1C1A")

    label("loc_13C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1505")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_148F")

    ChrTalk(    #41
        0xFE,
        (
            "Oh, for... No matter how much time\x01",
            "I spend, this is going nowhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        "You can't clean without a vacuum cleaner.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "It'd be like trying to make an\x01",
            "omelet without a frying pan.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1502")

    label("loc_148F")


    ChrTalk(    #44
        0xFE,
        "You can't clean without a vacuum cleaner.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "The manager's all on my case about it...\x01",
            "Do it yourself, geez.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1502")

    Jump("loc_1C1A")

    label("loc_1505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1647")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1585")

    ChrTalk(    #46
        0xFE,
        "The Imperial ambassador finally went home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "He was aaaaalways acting so high and mighty.\x01",
            "What a jerk.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1644")

    label("loc_1585")


    ChrTalk(    #48
        0xFE,
        "The Imperial ambassador finally went home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "He was aaaaalways acting so high and mighty.\x01",
            "What a jerk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "It's too bad the merchants've gone back,\x01",
            "but I'm really glad he's gone.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1644")

    Jump("loc_1C1A")

    label("loc_1647")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1760")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_16CD")

    ChrTalk(    #51
        0xFE,
        (
            "This merchant sells plates\x01",
            "and other small articles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "To be able to shop while I work...\x01",
            "It's like a dream!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_175D")

    label("loc_16CD")


    ChrTalk(    #53
        0xFE,
        (
            "Hmm, so this merchant sells plates\x01",
            "and other small articles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        "I was just looking for some teacups.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "I'll have to stop by later.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_175D")

    Jump("loc_1C1A")

    label("loc_1760")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_191C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_17F6")

    ChrTalk(    #56
        0xFE,
        (
            "For a little while, the merchants will\x01",
            "be temporarily occupying our hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "If it makes my job easier,\x01",
            "then I'm all for it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1919")

    label("loc_17F6")


    ChrTalk(    #58
        0xFE,
        (
            "For a little while, the merchants will\x01",
            "be temporarily occupying our hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "So, this basically means I don't need to do my\x01",
            "job for each of the individual rooms, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "I think you could tell by looking, but most\x01",
            "of them are technically open but not actually\x01",
            "doing business.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1919")

    Jump("loc_1C1A")

    label("loc_191C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_1A90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_19CE")

    ChrTalk(    #61
        0xFE,
        (
            "Seems like the merchants are carrying\x01",
            "their goods to the individual rooms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "Maybe we're gonna get bought out\x01",
            "by Mayor Maybelle and become market No. 2.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A8D")

    label("loc_19CE")


    ChrTalk(    #63
        0xFE,
        (
            "I-It seems like the merchants are carrying\x01",
            "their goods to the individual rooms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        "...Could it be?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "Maybe we're gonna get bought out\x01",
            "by Mayor Maybelle and become market No. 2.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1A8D")

    Jump("loc_1C1A")

    label("loc_1A90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_1C1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1B48")

    ChrTalk(    #66
        0xFE,
        (
            "Apparently that's some VIP from somewhere\x01",
            "staying on the second floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "But, I dunno much else about him. He just\x01",
            "locks himself in his room most of the time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C1A")

    label("loc_1B48")


    ChrTalk(    #68
        0xFE,
        (
            "Apparently that's some VIP from somewhere\x01",
            "staying on the second floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "But, I dunno much else about him. He just\x01",
            "locks himself in his room most of the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        "I wonder what he's doing in there.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1C1A")

    TalkEnd(0x9)
    Return()

    # Function_9_11AC end

    def Function_10_1C1E(): pass

    label("Function_10_1C1E")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1CE0")

    ChrTalk(    #71
        0xA,
        (
            "#1100FFor me, it's enough just having\x01",
            "recovered my medal.\x02\x03",

            "Phantom Thief B's capture is a national\x01",
            "and guild-wide problem...\x02\x03",

            "You shouldn't let yourself be too\x01",
            "bothered by it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2219")

    label("loc_1CE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1DF3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1D6E")

    ChrTalk(    #72
        0xA,
        (
            "#1100FI'll be returning to the capital\x01",
            "on a patrol ship.\x02\x03",

            "Seems a natural consideration\x01",
            "for the Imperial ambassador.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DF0")

    label("loc_1D6E")


    ChrTalk(    #73
        0xA,
        (
            "#1100FI'm scheduled to return to the capital\x01",
            "on a patrol ship...\x02\x03",

            "Y-You have to recover my medal\x01",
            "before that no matter what!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DF0")

    Jump("loc_2219")

    label("loc_1DF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_1F5D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1E9C")

    ChrTalk(    #74
        0xA,
        (
            "#1100FAs I was to return to the capital, the\x01",
            "scheduled liners stopped, of all things...\x02\x03",

            "I-I'm the Imperial ambassador!\x01",
            "How dare they delay me!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F5A")

    label("loc_1E9C")


    ChrTalk(    #75
        0xA,
        (
            "#1100FThat medal is proof of my family's glory and was\x01",
            "bestowed on us directly from His Highness...\x02\x03",

            "However, I must return to the capital soon.\x02\x03",

            "Y-You have to get it back before then!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F5A")

    Jump("loc_2219")

    label("loc_1F5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_20C9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_201E")

    ChrTalk(    #76
        0xA,
        (
            "#1100FEven if I were to go inspect the market,\x01",
            "considering the state it's in, well...\x02\x03",

            "Perhaps I should abandon the remainder\x01",
            "of my schedule and return to the capital.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20C6")

    label("loc_201E")


    ChrTalk(    #77
        0xA,
        (
            "#1100FThat medal is proof of my family's glory and was\x01",
            "bestowed on us directly from His Highness...\x02\x03",

            "I do hope it wasn't caught up in the\x01",
            "damage to the market... \x02",
        )
    )

    CloseMessageWindow()

    label("loc_20C6")

    Jump("loc_2219")

    label("loc_20C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_2219")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2191")

    ChrTalk(    #78
        0xA,
        (
            "#1100FI intend to resume my observations\x01",
            "of the city soon.\x02\x03",

            "I hear there are many of my country's\x01",
            "merchants in the Bose Market.\x02\x03",

            "I'll need to evaluate their businesses first.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2219")

    label("loc_2191")


    ChrTalk(    #79
        0xA,
        (
            "#1100FThat medal is proof of my family's glory and was\x01",
            "bestowed on us directly from His Highness...\x02\x03",

            "I have to recover it somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2219")

    TalkEnd(0xA)
    Return()

    # Function_10_1C1E end

    def Function_11_221D(): pass

    label("Function_11_221D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_23CC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_234C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_22A1")

    ChrTalk(    #80
        0xFE,
        "Everyone, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "With the medal safely recovered, we\x01",
            "can return happily to our country.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2349")

    label("loc_22A1")


    ChrTalk(    #82
        0xFE,
        (
            "We will be returning to the capital with\x01",
            "the assistance of the Royal Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "The ambassador is most touched by the sincere\x01",
            "response on the part of the Kingdom.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2349")

    Jump("loc_23C9")

    label("loc_234C")


    ChrTalk(    #84
        0xFE,
        (
            "The Royal Army will be providing\x01",
            "an airship for the ambassador.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        "Will the medal be located before the ship arrives?\x02",
    )

    CloseMessageWindow()

    label("loc_23C9")

    Jump("loc_2819")

    label("loc_23CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_258A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2508")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_248F")

    ChrTalk(    #86
        0xFE,
        "Everyone, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "However, the market is temporarily out\x01",
            "of operation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "Hopefully we can at least perform our\x01",
            "scheduled observations somehow, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2505")

    label("loc_248F")


    ChrTalk(    #89
        0xFE,
        (
            "It seems there were no Imperial\x01",
            "citizens among those injured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        "The silver lining in all this, one might say.\x02",
    )

    CloseMessageWindow()

    label("loc_2505")

    Jump("loc_2587")

    label("loc_2508")


    ChrTalk(    #91
        0xFE,
        "Do you think you will be able to find the medal?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "Hopefully it can be located before\x01",
            "we must return to the capital...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2587")

    Jump("loc_2819")

    label("loc_258A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_26F5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_267C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_25FA")

    ChrTalk(    #93
        0xFE,
        "Everyone, thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        "Still, what damage there was to the market.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2624")

    label("loc_25FA")


    ChrTalk(    #95
        0xFE,
        "What damage there was to the market.\x02",
    )

    CloseMessageWindow()

    label("loc_2624")


    ChrTalk(    #96
        0xFE,
        (
            "In the worst case scenario, we might have\x01",
            "to suspend our observations entirely.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26F2")

    label("loc_267C")


    ChrTalk(    #97
        0xFE,
        "What damage there was to the market.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "There may even have been injuries amongst\x01",
            "the merchants of our nation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26F2")

    Jump("loc_2819")

    label("loc_26F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_2819")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_27CD")

    ChrTalk(    #99
        0xFE,
        (
            "The medal of service...\x01",
            "A gracious thanks, indeed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "That medal is a sign of a person who\x01",
            "has dedicated himself to the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "It is very rare for it to be\x01",
            "bestowed upon a foreigner.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2819")

    label("loc_27CD")


    ChrTalk(    #102
        0xFE,
        "Everyone, please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        "We can hardly resume our inspections like this.\x02",
    )

    CloseMessageWindow()

    label("loc_2819")

    TalkEnd(0xFE)
    Return()

    # Function_11_221D end

    def Function_12_281D(): pass

    label("Function_12_281D")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2962")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_28C3")

    ChrTalk(    #104
        0xFE,
        (
            "The ambassador will be returning\x01",
            "to the capital soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "Ladies and gentlemen, allow us to offer\x01",
            "our sincerest thanks for your efforts.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_295F")

    label("loc_28C3")


    ChrTalk(    #106
        0xFE,
        "What is the state of the investigation?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "The ambassador is scheduled to return\x01",
            "to the capital soon...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        "You have almost no time left to search.\x02",
    )

    CloseMessageWindow()

    label("loc_295F")

    Jump("loc_2DD2")

    label("loc_2962")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_2B21")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2A4C")

    ChrTalk(    #109
        0xFE,
        (
            "We are currently searching for\x01",
            "a way to return to the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "While we cannot use the scheduled liners in\x01",
            "accordance with the Royal Army's restrictions,\x01",
            "we have no choice but to investigate every angle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B1E")

    label("loc_2A4C")


    ChrTalk(    #111
        0xFE,
        (
            "Ladies and gentlemen, how is\x01",
            "the investigation proceeding?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "We're currently searching for\x01",
            "a way to return to the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "We cannot afford to leave the embassy\x01",
            "unattended for too long, after all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B1E")

    Jump("loc_2DD2")

    label("loc_2B21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_2CCE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2BA0")

    ChrTalk(    #114
        0xFE,
        (
            "Just as we were going to\x01",
            "resume our observations...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        "To think something like this would happen...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CCB")

    label("loc_2BA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2C35")

    ChrTalk(    #116
        0xFE,
        (
            "Just having the medal stolen is\x01",
            "quite terrible, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "To have such a disaster on top of that...\x01",
            "Truly, when it rains, it pours.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CCB")

    label("loc_2C35")


    ChrTalk(    #118
        0xFE,
        (
            "Just having the medal stolen is\x01",
            "quite terrible, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        "To have such a thing happen to the market...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        "Truly, when it rains, it pours.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2CCB")

    Jump("loc_2DD2")

    label("loc_2CCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_2DD2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2D62")

    ChrTalk(    #121
        0xFE,
        (
            "The ambassador is scheduled to\x01",
            "resume his observations soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "You have our heartfelt thanks for your\x01",
            "efforts, bracers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DD2")

    label("loc_2D62")


    ChrTalk(    #123
        0xFE,
        (
            "For the glory of our Empire, we\x01",
            "expect a good effort from you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        "Please recover the ambassador's medal.\x02",
    )

    CloseMessageWindow()

    label("loc_2DD2")

    TalkEnd(0xD)
    Return()

    # Function_12_281D end

    def Function_13_2DD6(): pass

    label("Function_13_2DD6")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_3194")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x348, 2)), scpexpr(EXPR_END)), "loc_2EC6")

    ChrTalk(    #125
        0xFE,
        (
            "I'll be putting up temporary shop here\x01",
            "to continue business for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "I admit my stock's a little low, but\x01",
            "I'll keep working as I have until now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "If there's anything you want,\x01",
            "give my partner the word.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3194")

    label("loc_2EC6")

    TurnDirection(0xFE, 0x101, 0)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #128
        0xFE,
        "Ah, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        "Thanks. You really helped out during the rescue.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x101,
        (
            "#1002FNah. It was an emergency situation.\x01",
            "It's only natural to help.\x02\x03",

            "Was everyone able to safely evacuate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        "Yeah, seems so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "At the mayor's direction, we'll be\x01",
            "temporarily operating here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "If all our shops just ceased business, it'd cause\x01",
            "problems for all the citizens, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x101,
        (
            "#1011FHuh, nice. That's Mayor Maybelle for you. She's\x01",
            "certainly fast on the response at times like this.\x02\x03",

            "#1006FI'm sure it'll be tough like this, but good luck.\x01",
            "We're cheering for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        "You bet. I'll do my best for you too, little miss.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "If there's anything you want,\x01",
            "give my partner the word.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A42)

    label("loc_3194")

    TalkEnd(0xE)
    Return()

    # Function_13_2DD6 end

    def Function_14_3198(): pass

    label("Function_14_3198")

    Call(0, 15)
    Return()

    # Function_14_3198 end

    def Function_15_319D(): pass

    label("Function_15_319D")

    TalkBegin(0xF)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31FD")
    OP_0D()
    OP_A9(0x50)
    OP_56(0x0)
    TalkEnd(0xF)
    Return()

    label("loc_31FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_320E")
    TalkEnd(0xF)
    Return()

    label("loc_320E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_3401")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_32CB")

    ChrTalk(    #137
        0xFE,
        (
            "Due to the army's restrictions, the\x01",
            "scheduled liners are still stopped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "I know there's nothing they can do about\x01",
            "it, but our stock's starting to look pretty\x01",
            "bad.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33FE")

    label("loc_32CB")


    ChrTalk(    #139
        0xFE,
        (
            "Due to the army's restrictions, the\x01",
            "scheduled liners are still stopped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "I know there's nothing they can do about\x01",
            "it, but our stock's starting to look pretty\x01",
            "bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        "Still, everyone's sharing that little problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "We'll maintain current prices even if\x01",
            "we have to completely ignore profit.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_33FE")

    Jump("loc_36B3")

    label("loc_3401")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_353B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3486")

    ChrTalk(    #143
        0xFE,
        "Market repair work began this morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "That's our Mayor Maybelle. She's a\x01",
            "genius at making things happen.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3538")

    label("loc_3486")


    ChrTalk(    #145
        0xFE,
        "Hey, welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "Market repair work began this morning,\x01",
            "apparently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        "My partner already ran out to go help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "Honestly I envy Buck's energy\x01",
            "at times like these.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_3538")

    Jump("loc_36B3")

    label("loc_353B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_36B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_35A3")

    ChrTalk(    #149
        0xFE,
        "I'm still nervous as heck.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "I wonder how the market'll turn\x01",
            "out as things go.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36B3")

    label("loc_35A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_364F")

    ChrTalk(    #151
        0xFE,
        "*siiigh* I still feel all tense.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "We've got to somehow force ourselves\x01",
            "to keep working, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "I wonder how the market'll turn\x01",
            "out as things go.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_36B3")

    label("loc_364F")


    ChrTalk(    #154
        0xFE,
        "Hey, thanks for the help back there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "The market's a mess, but\x01",
            "I'm glad Lila was saved.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_36B3")

    TalkEnd(0xF)
    Return()

    # Function_15_319D end

    def Function_16_36B7(): pass

    label("Function_16_36B7")

    TalkBegin(0x10)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3717")
    OP_0D()
    OP_A9(0x40)
    OP_56(0x0)
    TalkEnd(0x10)
    Return()

    label("loc_3717")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3728")
    TalkEnd(0x10)
    Return()

    label("loc_3728")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_38BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_37B9")

    ChrTalk(    #156
        0xFE,
        "My husband still worried about the village.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "I wish he'd spend even one minute of\x01",
            "that time worrying about his family.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38B7")

    label("loc_37B9")


    ChrTalk(    #158
        0xFE,
        "That darn husband of mine...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "After coming all the way here,\x01",
            "he's only worried about the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "The village people aren't children.\x01",
            "They can handle themselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "He can't even spare a thought for\x01",
            "his own family at a time like this.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_38B7")

    Jump("loc_3A99")

    label("loc_38BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_39F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_393B")

    ChrTalk(    #162
        0xFE,
        (
            "My husband finally returned from\x01",
            "Ravennue Village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        (
            "It's nice to have a man's help\x01",
            "at times like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39ED")

    label("loc_393B")


    ChrTalk(    #164
        0xFE,
        (
            "My husband finally returned from\x01",
            "Ravennue Village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "It's nice to have a man's help\x01",
            "at times like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        (
            "There's a lot I want to say,\x01",
            "but I'll keep it in for now.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_39ED")

    Jump("loc_3A99")

    label("loc_39F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_3A99")

    ChrTalk(    #167
        0xFE,
        "*siiigh* I still can't believe a dragon appeared.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "There were old stories about them\x01",
            "in my home village, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        "I didn't think they really existed.\x02",
    )

    CloseMessageWindow()

    label("loc_3A99")

    TalkEnd(0x10)
    Return()

    # Function_16_36B7 end

    def Function_17_3A9D(): pass

    label("Function_17_3A9D")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_3AF6")

    ChrTalk(    #170
        0xFE,
        "Mom may be complaining, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        "She really IS happy Dad came back.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D67")

    label("loc_3AF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_3C67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3B8E")

    ChrTalk(    #172
        0xFE,
        (
            "Apparently the dragon showed\x01",
            "up at Ravennue Village too. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "No one was hurt, but for the orchards\x01",
            "to be burnt to the ground...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C64")

    label("loc_3B8E")


    ChrTalk(    #174
        0xFE,
        (
            "Apparently the dragon showed\x01",
            "up at Ravennue Village too. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        (
            "No one was hurt, but for the orchards\x01",
            "to be burnt to the ground...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        (
            "Dad's safe, and I'm happy about that,\x01",
            "but...it's hard to be too happy.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_3C64")

    Jump("loc_3D67")

    label("loc_3C67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_3D67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3CDA")

    ChrTalk(    #177
        0xFE,
        (
            "The dragon flew off towards\x01",
            "the village where my dad is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        "I hope nothing happens, but...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D67")

    label("loc_3CDA")


    ChrTalk(    #179
        0xFE,
        "The dragon flew off towards the northwest.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "That's where Ravennue Village is.\x01",
            "...And my dad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        "I hope nothing happens, but...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_3D67")

    TalkEnd(0x11)
    Return()

    # Function_17_3A9D end

    def Function_18_3D6B(): pass

    label("Function_18_3D6B")

    TalkBegin(0x12)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DCB")
    OP_0D()
    OP_A9(0x3C)
    OP_56(0x0)
    TalkEnd(0x12)
    Return()

    label("loc_3DCB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DDC")
    TalkEnd(0x12)
    Return()

    label("loc_3DDC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3DE9")
    OP_A2(0xA)

    label("loc_3DE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E76")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Cleared previous chapter QST017\x01",           # 0
            "Didn't clear previous chapter QST017\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3E6A"),
        (1, "loc_3E70"),
        (SWITCH_DEFAULT, "loc_3E76"),
    )


    label("loc_3E6A")

    OP_A2(0xA)
    Jump("loc_3E76")

    label("loc_3E70")

    OP_A3(0xA)
    Jump("loc_3E76")

    label("loc_3E76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x348, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4182")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4105")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_3F05")

    ChrTalk(    #182
        0xFE,
        "The market repairs are proceeding smoothly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "I feel like it's the first good\x01",
            "news we've had in a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4102")

    label("loc_3F05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_3F85")

    ChrTalk(    #184
        0xFE,
        (
            "Apparently the market repairs have\x01",
            "already begun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "I hope they're able to put it back\x01",
            "in good order quickly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4102")

    label("loc_3F85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_4102")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_4016")

    ChrTalk(    #186
        0xFE,
        (
            "For now, though, I plan on running\x01",
            "my business right here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        (
            "After all, we don't know when\x01",
            "the market will be restored.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4102")

    label("loc_4016")


    ChrTalk(    #188
        0xFE,
        (
            "Phew! It was a struggle with these old\x01",
            "bones, but somehow I managed to get\x01",
            "all my equipment here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "For now, at least, I plan on running\x01",
            "my business right here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        (
            "After all, we don't know when\x01",
            "the market will be restored.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_4102")

    Jump("loc_417F")

    label("loc_4105")


    ChrTalk(    #191
        0xFE,
        "That medicine is my way of cheering you on.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        (
            "It's a medicine with powerful effects,\x01",
            "so I'm sure it'll be useful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_417F")

    Jump("loc_45BC")

    label("loc_4182")

    TurnDirection(0xFE, 0x101, 0)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #193
        0xFE,
        "Oh, you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        (
            "You're the bracers who got those medical\x01",
            "herbs for me a while back, aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x101,
        (
            "#1016FAhh, yeah. Now that you mention it,\x01",
            "we did.\x02\x03",

            "#1000FSir, are you doing business out of\x01",
            "here for now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xFE,
        "Yes, for the moment...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        (
            "I'm sure everyone would be troubled if the\x01",
            "pharmacy shut down at a time like this.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_43AC")

    ChrTalk(    #198
        0x101,
        (
            "#1006FYeah, we appreciate it too.\x02\x03",

            "#1015FAfter all, we're about to head\x01",
            "off on a big job now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        "A big job, you say...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        "Is it related to the dragon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x101,
        "#1011FAh, yeah, why?\x02",
    )

    CloseMessageWindow()
    Jump("loc_447B")

    label("loc_43AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_447B")

    ChrTalk(    #202
        0x101,
        (
            "#1006FWe appreciate it.\x02\x03",

            "#1015FWe're just about to head out and investigate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        "Investigate...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        "Is it anything to do with the dragon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x101,
        "#1011FYeah, an investigation into related events.\x02",
    )

    CloseMessageWindow()

    label("loc_447B")


    ChrTalk(    #206
        0xFE,
        "Well, then, allow me to offer my support.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #207
        "\x07\x00Received #517i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x205, 1)

    ChrTalk(    #208
        0xFE,
        (
            "It's a medicine with strong effects,\x01",
            "so I'm sure it'll be useful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        (
            "Well, then, good luck with the work...\x01",
            "I'll be expecting good results.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x101,
        "#1001FThanks, sir. This'll definitely help.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A40)
    OP_A2(0x8)

    label("loc_45BC")

    TalkEnd(0x12)
    Return()

    # Function_18_3D6B end

    def Function_19_45C0(): pass

    label("Function_19_45C0")

    TalkBegin(0x13)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_462C")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_4621")
    OP_A9(0x44)
    Jump("loc_4623")

    label("loc_4621")

    OP_A9(0x42)

    label("loc_4623")

    OP_56(0x0)
    TalkEnd(0x13)
    Return()

    label("loc_462C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_463D")
    TalkEnd(0x13)
    Return()

    label("loc_463D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_47BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_46E5")

    ChrTalk(    #211
        0xFE,
        (
            "The airships are stopped again due\x01",
            "to the army's flight restrictions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        (
            "My, my, my... Securing wares to sell\x01",
            "is gonna get real hard real fast.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47B8")

    label("loc_46E5")


    ChrTalk(    #213
        0xFE,
        (
            "The airships are stopped again due\x01",
            "to the army's flight restrictions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        (
            "Well, I'm sure it's necessary\x01",
            "to stop the dragon, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        (
            "If they're gonna do that much, I sure\x01",
            "hope they do the job right.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_47B8")

    Jump("loc_4B77")

    label("loc_47BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_491B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_4852")

    ChrTalk(    #216
        0xFE,
        (
            "Apparently the Royal Army's preparing\x01",
            "for a plan to capture the dragon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        (
            "It's taught that dragons\x01",
            "are holy creatures, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4918")

    label("loc_4852")


    ChrTalk(    #218
        0xFE,
        (
            "Apparently the Royal Army's preparing\x01",
            "for a plan to capture the dragon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        (
            "When I was a kid, I was taught\x01",
            "that dragons're holy, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        (
            "Won't the Goddess punish us for\x01",
            "capturing one?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_4918")

    Jump("loc_4B77")

    label("loc_491B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_4B77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_4A08")

    ChrTalk(    #221
        0xFE,
        (
            "It was just for a moment, but scenes from\x01",
            "the war flashed in front of my eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        (
            "But, our market recovered from being\x01",
            "destroyed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xFE,
        (
            "Should another dragon come, or should\x01",
            "bombs fall, it'll rise again, I'm sure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B77")

    label("loc_4A08")


    ChrTalk(    #224
        0xFE,
        (
            "When the rubble fell, it felt\x01",
            "like the war all over again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        (
            "Back then, the ceilings collapsed in and\x01",
            "everyone was so desperate to escape...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xFE,
        (
            "But, what you mustn't forget is that\x01",
            "even then we were able to rebuild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        (
            "As long as we don't give up, we can\x01",
            "bounce back from any tragedy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xFE,
        (
            "To me, the memories of the war\x01",
            "are an irreplaceable lesson.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_4B77")

    TalkEnd(0x13)
    Return()

    # Function_19_45C0 end

    def Function_20_4B7B(): pass

    label("Function_20_4B7B")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_4CE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_4C0B")

    ChrTalk(    #229
        0xFE,
        (
            "Apparently the Arseille came for the\x01",
            "Royal Army's dragon plan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0xFE,
        (
            "I hope they manage to chase off\x01",
            "the dragon, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CE1")

    label("loc_4C0B")


    ChrTalk(    #231
        0xFE,
        (
            "Apparently the Arseille came for the\x01",
            "Royal Army's dragon plan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        (
            "Seems like the Royal Army's really mobilizing.\x01",
            "Makes sense after a declaration from\x01",
            "Her Highness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        "So, ultimately, did the plan work?\x02",
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_4CE1")

    Jump("loc_5093")

    label("loc_4CE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_4F10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_4DBD")

    ChrTalk(    #234
        0xFE,
        (
            "For the moment I'll be borrowing a room\x01",
            "from the hotel to run my business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        (
            "Really, I gotta tip my hat to the spirit of\x01",
            "mutual assistance that the merchants\x01",
            "of Bose have at a time like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F0D")

    label("loc_4DBD")


    ChrTalk(    #236
        0xFE,
        (
            "Following Mayor Maybelle's plan, we'll\x01",
            "be borrowing rooms at the hotel and\x01",
            "operating out of them for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        (
            "Really, I gotta tip my hat to the spirit of\x01",
            "mutual assistance that the merchants\x01",
            "of Bose have at a time like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xFE,
        (
            "It's because we work hand in hand like this that\x01",
            "we were able to recover from the flames of war.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_4F0D")

    Jump("loc_5093")

    label("loc_4F10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_5093")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_4FBE")

    ChrTalk(    #239
        0xFE,
        (
            "I really freaked out when Old Miss Minuet\x01",
            "went back to get her goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xFE,
        (
            "She doesn't have that fearsome reputation\x01",
            "in the market for nothing, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5093")

    label("loc_4FBE")


    ChrTalk(    #241
        0xFE,
        "W-We managed to get to safety, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xFE,
        (
            "I really freaked out when Old Miss Minuet\x01",
            "went back to get her goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        (
            "The courage of the people who came through\x01",
            "the flames of war really is different, huh.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_5093")

    TalkEnd(0x14)
    Return()

    # Function_20_4B7B end

    def Function_21_5097(): pass

    label("Function_21_5097")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_51FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_5138")

    ChrTalk(    #244
        0xFE,
        (
            "Even though the scheduled flights have stopped,\x01",
            "the price of vegetables hasn't gone up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        "That's weird... I was sure it would go up.\x02",
    )

    CloseMessageWindow()
    Jump("loc_51FB")

    label("loc_5138")


    ChrTalk(    #246
        0xFE,
        "I was just peeking in on the fruit store, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xFE,
        (
            "Even though the scheduled flights have stopped,\x01",
            "the price of produce hasn't gone up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xFE,
        "That's weird... I was sure it would go up.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_51FB")

    Jump("loc_54B7")

    label("loc_51FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_5384")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_52B1")

    ChrTalk(    #249
        0xFE,
        (
            "Even if the price is a bit high, buying\x01",
            "now might be a better deal...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xFE,
        (
            "But, buying something that's not on sale\x01",
            "kind of has a sense of defeat, you know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5381")

    label("loc_52B1")


    ChrTalk(    #251
        0xFE,
        (
            "Did you hear? Apparently the scheduled\x01",
            "flights have stopped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xFE,
        (
            "In other words, the price of vegetables'll\x01",
            "start going up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xFE,
        (
            "Even if the price is a bit high, buying\x01",
            "now might be a better deal...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_5381")

    Jump("loc_54B7")

    label("loc_5384")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_54B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_5405")

    ChrTalk(    #254
        0xFE,
        (
            "The shop people are selling even from\x01",
            "where they evacuated to, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0xFE,
        "Really, I appreciate that...\x02",
    )

    CloseMessageWindow()
    Jump("loc_54B7")

    label("loc_5405")


    ChrTalk(    #256
        0xFE,
        (
            "The shop people are selling even from\x01",
            "where they evacuated to, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xFE,
        "Really, I appreciate that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xFE,
        (
            "I still haven't decided on what\x01",
            "to do for dinner tonight.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_54B7")

    TalkEnd(0x15)
    Return()

    # Function_21_5097 end

    def Function_22_54BB(): pass

    label("Function_22_54BB")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_5664")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_556F")

    ChrTalk(    #259
        0x16,
        (
            "With the scheduled liners stopped,\x01",
            "every store's business is in trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x16,
        (
            "This really still isn't the kind of atmosphere\x01",
            "to do business deals in, huh.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5661")

    label("loc_556F")


    ChrTalk(    #261
        0x16,
        (
            "With the scheduled liners stopped,\x01",
            "every store's business is in trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x16,
        (
            "This really still isn't the kind of atmosphere\x01",
            "to do business deals in, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x16,
        (
            "Guess I've got no choice but to wait\x01",
            "a while until the market's restored.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)

    label("loc_5661")

    Jump("loc_57C1")

    label("loc_5664")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_57C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_56F1")

    ChrTalk(    #264
        0x16,
        (
            "Apparently the market stores are temporarily\x01",
            "operating out of here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x16,
        "Well, then, might as well have a look around.\x02",
    )

    CloseMessageWindow()
    Jump("loc_57C1")

    label("loc_56F1")


    ChrTalk(    #266
        0x16,
        (
            "Apparently the market stores are temporarily\x01",
            "operating out of here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x16,
        "Well, then, might as well have a look around.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x16,
        (
            "Even if business isn't gonna happen,\x01",
            "I'd at least like to introduce myself.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)

    label("loc_57C1")

    TalkEnd(0x16)
    Return()

    # Function_22_54BB end

    def Function_23_57C5(): pass

    label("Function_23_57C5")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_58ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_582F")

    ChrTalk(    #269
        0xFE,
        "I'm worried about Ravennue Village.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0xFE,
        "I hope Pesca and Gray are doing okay...\x02",
    )

    CloseMessageWindow()
    Jump("loc_58EA")

    label("loc_582F")


    ChrTalk(    #271
        0xFE,
        (
            "I ran from Ravennue all the way here,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0xFE,
        "I'm still worried about the village.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0xFE,
        "I hope Pesca and Gray are doing okay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xFE,
        "After all, I'm pretty close to those two.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xF)

    label("loc_58EA")

    Jump("loc_59AD")

    label("loc_58ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_59AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_593B")

    ChrTalk(    #275
        0xFE,
        (
            "I was really relieved to see my\x01",
            "wife and son were okay.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59AD")

    label("loc_593B")


    ChrTalk(    #276
        0xFE,
        "Apparently the market got hit too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0xFE,
        (
            "Anyway, I'm really relieved to see\x01",
            "my wife and son are uninjured.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)

    label("loc_59AD")

    TalkEnd(0x17)
    Return()

    # Function_23_57C5 end

    def Function_24_59B1(): pass

    label("Function_24_59B1")

    TalkBegin(0x18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_5ABA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A6A")

    ChrTalk(    #278
        0xFE,
        "This is bad...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xFE,
        (
            "My wallet's got more air than mira\x01",
            "in it right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0xFE,
        (
            "I've got a return ticket, but if the ship\x01",
            "never comes, that doesn't mean much.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x10)
    Jump("loc_5AB7")

    label("loc_5A6A")


    ChrTalk(    #281
        0xFE,
        "This is bad...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xFE,
        (
            "My wallet's got more air than mira\x01",
            "in it right now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5AB7")

    Jump("loc_5BDC")

    label("loc_5ABA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_5BDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B6E")

    ChrTalk(    #283
        0xFE,
        "I came to Bose to see the Haken Gate, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xFE,
        "I-I didn't expect THIS to happen at my destination.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0xFE,
        "Anyway, I hope things get back to normal soon.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x10)
    Jump("loc_5BDC")

    label("loc_5B6E")


    ChrTalk(    #286
        0xFE,
        "I didn't expect THIS to happen at my destination.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0xFE,
        "I hope the scheduled flights start up again soon.\x02",
    )

    CloseMessageWindow()

    label("loc_5BDC")

    TalkEnd(0x18)
    Return()

    # Function_24_59B1 end

    def Function_25_5BE0(): pass

    label("Function_25_5BE0")

    TalkBegin(0x19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CB2")

    ChrTalk(    #288
        0xFE,
        "My orbal camera's stopped working.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0xFE,
        (
            "And here I took lots of cool shots of\x01",
            "the Haken Gate, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0xFE,
        (
            "Maaaaan, this sucks. I hope I can get them\x01",
            "printed soon. I really wanna see them!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)
    Jump("loc_5D10")

    label("loc_5CB2")


    ChrTalk(    #291
        0xFE,
        "My orbal camera's stopped working.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xFE,
        (
            "I can't get my shots printed either.\x01",
            "This sucks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D10")

    TalkEnd(0x19)
    Return()

    # Function_25_5BE0 end

    def Function_26_5D14(): pass

    label("Function_26_5D14")

    TalkBegin(0x1A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DF4")

    ChrTalk(    #293
        0xFE,
        (
            "For such a last minute booking,\x01",
            "this is a pretty decent hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0xFE,
        "Plus the room is being paid by the airline...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xFE,
        "I feel pretty lucky.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0xFE,
        (
            "...Though, this isn't the time to be rejoicing,\x01",
            "I guess.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x12)
    Jump("loc_5E80")

    label("loc_5DF4")


    ChrTalk(    #297
        0xFE,
        (
            "For such a last minute booking,\x01",
            "this is a pretty decent hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0xFE,
        (
            "I guess the airline service isn't\x01",
            "something to sneer at after all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E80")

    TalkEnd(0x1A)
    Return()

    # Function_26_5D14 end

    def Function_27_5E84(): pass

    label("Function_27_5E84")

    TalkBegin(0x1B)

    ChrTalk(    #299
        0xFE,
        "I'm glad we could get into the hotel so quickly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0xFE,
        "My daughter and I are both so tired.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x1B)
    Return()

    # Function_27_5E84 end

    def Function_28_5EEB(): pass

    label("Function_28_5EEB")

    TalkBegin(0x1C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F50")

    ChrTalk(    #301
        0xFE,
        "The baths here are great. ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0xFE,
        "They're like what a princess would bathe in!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x14)
    Jump("loc_5F72")

    label("loc_5F50")


    ChrTalk(    #303
        0xFE,
        "The baths here are great. ♪\x02",
    )

    CloseMessageWindow()

    label("loc_5F72")

    TalkEnd(0x1C)
    Return()

    # Function_28_5EEB end

    def Function_29_5F76(): pass

    label("Function_29_5F76")

    TalkBegin(0x1D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6069")

    ChrTalk(    #304
        0xFE,
        "I'm grateful they got rooms for us, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0xFE,
        (
            "This basically means there won't be\x01",
            "any scheduled flights for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0xFE,
        (
            "Well, can't do anything about it.\x01",
            "Might as well put up my feet and\x01",
            "take a hot bath or something.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x15)
    Jump("loc_6111")

    label("loc_6069")


    ChrTalk(    #307
        0xFE,
        (
            "Seems like there won't be any scheduled\x01",
            "flights for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0xFE,
        (
            "Well, can't do anything about it.\x01",
            "Might as well put up my feet and\x01",
            "take a hot bath or something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6111")

    TalkEnd(0x1D)
    Return()

    # Function_29_5F76 end

    def Function_30_6115(): pass

    label("Function_30_6115")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #309
        (
            "\x07\x05Linen Room\x01",
            "※Employees Only\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_30_6115 end

    SaveToFile()

Try(main)
