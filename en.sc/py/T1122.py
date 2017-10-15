from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1122   ._SN',
        MapName             = 'Bose',
        Location            = 'T1122.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
        Flags               = 0,
        EntryFunctionIndex  = 37,
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
        'Buck',                                 # 9
        'Trayton',                              # 10
        'Felicia',                              # 11
        'Pomme',                                # 12
        'Spence',                               # 13
        'Katrina',                              # 14
        'Finel',                                # 15
        'Paul',                                 # 16
        'Minuet',                               # 17
        'Libro',                                # 18
        'Emmy',                                 # 19
        'Claire',                               # 20
        'Lyril',                                # 21
        'Carol',                                # 22
        'Meissen',                              # 23
        'Gantz',                                # 24
        'Lucas',                                # 25
        'Corna',                                # 26
        'Simon',                                # 27
        'Hardt',                                # 28
        'Elke',                                 # 29
        'Marco',                                # 30
        'Monte',                                # 31
        'Lore',                                 # 32
        'Mayor Maybelle',                       # 33
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
        'ED6_DT07/CH01140 ._CH',             # 00
        'ED6_DT07/CH01040 ._CH',             # 01
        'ED6_DT07/CH01130 ._CH',             # 02
        'ED6_DT07/CH01060 ._CH',             # 03
        'ED6_DT07/CH01000 ._CH',             # 04
        'ED6_DT07/CH02490 ._CH',             # 05
        'ED6_DT07/CH01220 ._CH',             # 06
        'ED6_DT07/CH01010 ._CH',             # 07
        'ED6_DT07/CH01050 ._CH',             # 08
        'ED6_DT07/CH01150 ._CH',             # 09
        'ED6_DT07/CH01070 ._CH',             # 0A
        'ED6_DT07/CH01030 ._CH',             # 0B
        'ED6_DT07/CH01200 ._CH',             # 0C
        'ED6_DT07/CH01270 ._CH',             # 0D
        'ED6_DT07/CH01180 ._CH',             # 0E
        'ED6_DT07/CH01120 ._CH',             # 0F
        'ED6_DT07/CH01480 ._CH',             # 10
        'ED6_DT07/CH01100 ._CH',             # 11
        'ED6_DT07/CH01020 ._CH',             # 12
        'ED6_DT07/CH02360 ._CH',             # 13
    )

    AddCharChipPat(
        'ED6_DT07/CH01140P._CP',             # 00
        'ED6_DT07/CH01040P._CP',             # 01
        'ED6_DT07/CH01130P._CP',             # 02
        'ED6_DT07/CH01060P._CP',             # 03
        'ED6_DT07/CH01000P._CP',             # 04
        'ED6_DT07/CH02490P._CP',             # 05
        'ED6_DT07/CH01220P._CP',             # 06
        'ED6_DT07/CH01010P._CP',             # 07
        'ED6_DT07/CH01050P._CP',             # 08
        'ED6_DT07/CH01150P._CP',             # 09
        'ED6_DT07/CH01070P._CP',             # 0A
        'ED6_DT07/CH01030P._CP',             # 0B
        'ED6_DT07/CH01200P._CP',             # 0C
        'ED6_DT07/CH01270P._CP',             # 0D
        'ED6_DT07/CH01180P._CP',             # 0E
        'ED6_DT07/CH01120P._CP',             # 0F
        'ED6_DT07/CH01480P._CP',             # 10
        'ED6_DT07/CH01100P._CP',             # 11
        'ED6_DT07/CH01020P._CP',             # 12
        'ED6_DT07/CH02360P._CP',             # 13
    )

    DeclNpc(
        X                   = 1500,
        Z                   = 0,
        Y                   = -12700,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 8500,
        Z                   = 0,
        Y                   = -8300,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 4100,
        Z                   = 0,
        Y                   = 13650,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 8250,
        Z                   = 0,
        Y                   = 13600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 9300,
        Z                   = 0,
        Y                   = 6900,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -13400,
        Z                   = 0,
        Y                   = 2500,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 2830,
        Z                   = 0,
        Y                   = 9160,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -16700,
        Z                   = 0,
        Y                   = -8600,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = -13600,
        Z                   = 0,
        Y                   = 10700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = -11100,
        Z                   = 0,
        Y                   = 10300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 5250,
        Z                   = 0,
        Y                   = -4500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = -3600,
        Z                   = 0,
        Y                   = 12500,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = -2310,
        Z                   = -1000,
        Y                   = -10530,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 2350,
        Z                   = 0,
        Y                   = -8000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 11500,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = -17180,
        Z                   = 0,
        Y                   = 5980,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = -12620,
        Z                   = 0,
        Y                   = -8490,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 29,
    )

    DeclNpc(
        X                   = -7300,
        Z                   = -1000,
        Y                   = 2510,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 30,
    )

    DeclNpc(
        X                   = -12380,
        Z                   = 0,
        Y                   = 7420,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = -16980,
        Z                   = 0,
        Y                   = -7310,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = -1200,
        Z                   = -1000,
        Y                   = 6040,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = -1200,
        Z                   = -1000,
        Y                   = 5040,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 34,
    )

    DeclNpc(
        X                   = 9730,
        Z                   = -1000,
        Y                   = 13220,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 1600,
        Z                   = -1000,
        Y                   = 150,
        Direction           = 257,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 36,
    )


    DeclActor(
        TriggerX            = 6830,
        TriggerZ            = 0,
        TriggerY            = -8820,
        TriggerRange        = 400,
        ActorX              = 8360,
        ActorZ              = 1500,
        ActorY              = -8430,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7540,
        TriggerZ            = 0,
        TriggerY            = 6450,
        TriggerRange        = 400,
        ActorX              = 9300,
        ActorZ              = 1500,
        ActorY              = 6900,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -15120,
        TriggerZ            = 0,
        TriggerY            = -8860,
        TriggerRange        = 400,
        ActorX              = -16700,
        ActorZ              = 1500,
        ActorY              = -8600,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_4D6",          # 00, 0
        "Function_1_5E9",          # 01, 1
        "Function_2_64C",          # 02, 2
        "Function_3_699",          # 03, 3
        "Function_4_6EA",          # 04, 4
        "Function_5_70E",          # 05, 5
        "Function_6_732",          # 06, 6
        "Function_7_756",          # 07, 7
        "Function_8_77A",          # 08, 8
        "Function_9_79E",          # 09, 9
        "Function_10_F97",         # 0A, 10
        "Function_11_F9C",         # 0B, 11
        "Function_12_17ED",        # 0C, 12
        "Function_13_1C93",        # 0D, 13
        "Function_14_208C",        # 0E, 14
        "Function_15_2091",        # 0F, 15
        "Function_16_33B3",        # 10, 16
        "Function_17_393D",        # 11, 17
        "Function_18_3E1F",        # 12, 18
        "Function_19_3E24",        # 13, 19
        "Function_20_468D",        # 14, 20
        "Function_21_4DC3",        # 15, 21
        "Function_22_53AA",        # 16, 22
        "Function_23_589B",        # 17, 23
        "Function_24_5C43",        # 18, 24
        "Function_25_6197",        # 19, 25
        "Function_26_6653",        # 1A, 26
        "Function_27_69E4",        # 1B, 27
        "Function_28_719B",        # 1C, 28
        "Function_29_77C7",        # 1D, 29
        "Function_30_784D",        # 1E, 30
        "Function_31_7AE6",        # 1F, 31
        "Function_32_7C5A",        # 20, 32
        "Function_33_7D1F",        # 21, 33
        "Function_34_7EBB",        # 22, 34
        "Function_35_80C3",        # 23, 35
        "Function_36_83B1",        # 24, 36
        "Function_37_8C0C",        # 25, 37
        "Function_38_8D85",        # 26, 38
        "Function_39_8EEB",        # 27, 39
        "Function_40_9017",        # 28, 40
        "Function_41_9125",        # 29, 41
    )


    def Function_0_4D6(): pass

    label("Function_0_4D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_58B")
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    OP_43(0x12, 0x0, 0x6, 0x2)
    SetChrPos(0x12, 6320, 0, -5410, 90)
    OP_43(0x15, 0x0, 0x6, 0x2)
    SetChrPos(0x15, 6690, 0, -6830, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_557")
    OP_43(0x14, 0x0, 0x6, 0x2)
    SetChrPos(0x14, -7650, -1000, 270, 90)
    OP_43(0x16, 0x0, 0x0, 0x8)
    SetChrPos(0x16, 8210, 0, 11230, 90)
    SetChrFlags(0x13, 0x80)
    Jump("loc_588")

    label("loc_557")

    SetChrFlags(0x8, 0x10)
    SetChrPos(0x14, -8720, -1000, -3130, 0)
    SetChrPos(0x18, -10900, 0, -7320, 232)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x1F, 0x80)

    label("loc_588")

    Jump("loc_5E8")

    label("loc_58B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_5E8")
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0xB, 0x10)
    SetChrPos(0x1A, 580, -1000, 5590, 270)
    SetChrPos(0x18, -8790, 0, -11320, 270)
    SetChrPos(0x14, -8720, -1000, -3130, 0)

    label("loc_5E8")

    Return()

    # Function_0_4D6 end

    def Function_1_5E9(): pass

    label("Function_1_5E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_62F")
    OP_72(0x0, 0x10)
    OP_6F(0x0, 29)
    OP_72(0x1, 0x10)
    OP_6F(0x1, 29)
    OP_75(0xFF, 0xA, 0x7)
    OP_75(0xFF, 0xC, 0x7)
    OP_75(0xFF, 0xD, 0x7)
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_82(0x84, 0x0)
    Jump("loc_64B")

    label("loc_62F")

    SoundDistance(0x1CB, 0xFFFFEF98, 0xFFFFFC18, 0x276, 0x7D0, 0x61A8, 0x64, 0x0)

    label("loc_64B")

    Return()

    # Function_1_5E9 end

    def Function_2_64C(): pass

    label("Function_2_64C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_698")
    OP_8E(0xFE, 0x1798, 0x0, 0x3520, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    OP_8E(0xFE, 0x203A, 0x0, 0x3520, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    Jump("Function_2_64C")

    label("loc_698")

    Return()

    # Function_2_64C end

    def Function_3_699(): pass

    label("Function_3_699")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_6C6")

    label("loc_6A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6C3")
    OP_8D(0xFE, -9760, 1870, -7910, -2550, 2000)
    Jump("loc_6A0")

    label("loc_6C3")

    Jump("loc_6E9")

    label("loc_6C6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6E9")
    OP_8D(0xFE, -1410, -8950, -3910, -12650, 2000)
    Jump("loc_6C6")

    label("loc_6E9")

    Return()

    # Function_3_699 end

    def Function_4_6EA(): pass

    label("Function_4_6EA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_70D")
    OP_8D(0xFE, 5660, -10000, -300, -7600, 2000)
    Jump("Function_4_6EA")

    label("loc_70D")

    Return()

    # Function_4_6EA end

    def Function_5_70E(): pass

    label("Function_5_70E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_731")
    OP_8D(0xFE, 200, 14800, -7900, 10300, 2000)
    Jump("Function_5_70E")

    label("loc_731")

    Return()

    # Function_5_70E end

    def Function_6_732(): pass

    label("Function_6_732")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_755")
    OP_8D(0xFE, 7480, 600, 4800, -5000, 2000)
    Jump("Function_6_732")

    label("loc_755")

    Return()

    # Function_6_732 end

    def Function_7_756(): pass

    label("Function_7_756")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_779")
    OP_8D(0xFE, -12100, 16600, -16600, 14400, 2000)
    Jump("Function_7_756")

    label("loc_779")

    Return()

    # Function_7_756 end

    def Function_8_77A(): pass

    label("Function_8_77A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_79D")
    OP_8D(0xFE, 9580, 12630, 5520, 9820, 2000)
    Jump("Function_8_77A")

    label("loc_79D")

    Return()

    # Function_8_77A end

    def Function_9_79E(): pass

    label("Function_9_79E")

    TalkBegin(0x8)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80B")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_800")
    OP_A9(0x3E)
    Jump("loc_802")

    label("loc_800")

    OP_A9(0x60)

    label("loc_802")

    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_80B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_81C")
    TalkEnd(0x8)
    Return()

    label("loc_81C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_A78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_932")

    ChrTalk(    #0
        0x8,
        (
            "All right, everyone, it's time for the support\x01",
            "sale you've all been waiting for!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "Remember, it's exactly during hard\x01",
            "times that we need to help each other!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "To offer thanks for your daily patronage\x01",
            "we've prepared great deals on our stock!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    OP_A2(0x0)
    Jump("loc_A75")

    label("loc_932")


    ChrTalk(    #3
        0x8,
        (
            "It's gonna be hard going, but thanks to\x01",
            "the assistance of the little lady we've\x01",
            "avoided shortages for the moment. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "Times like these, you just gotta run a sale\x01",
            "and cheer everyone up with a bang.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "To show my gratitude to our customers,\x01",
            "I gotta work my hardest, especially\x01",
            "during the tough times.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 400)
    SetChrFlags(0x8, 0x10)
    OP_A3(0x0)

    label("loc_A75")

    Jump("loc_F93")

    label("loc_A78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_BF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B95")

    ChrTalk(    #6
        0x8,
        (
            "Unbelievable. It's not just the scheduled liners,\x01",
            "but the freight trucks AND ships have stopped.\x01",
            "All distribution's totally paralyzed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        "At this rate we're gonna hit shortages real fast.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "My product's life is its freshness.\x01",
            "This's a serious problem...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_BED")

    label("loc_B95")


    ChrTalk(    #9
        0x8,
        "Oh, hell. Distribution's totally frozen.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        "This is a matter of life or death...\x02",
    )

    CloseMessageWindow()

    label("loc_BED")

    Jump("loc_F93")

    label("loc_BF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_D15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_C53")

    ChrTalk(    #11
        0x8,
        (
            "All right, everyone, we'll be having our\x01",
            "reopening memorial sale in moments!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D12")

    label("loc_C53")


    ChrTalk(    #12
        0x8,
        (
            "All right, everyone, we'll be having our\x01",
            "reopening memorial sale in moments!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "Want a deal? We got special today-only\x01",
            "stuff! You'd have to be a Mad Roper to\x01",
            "miss this opportunity!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_D12")

    Jump("loc_F93")

    label("loc_D15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_F93")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E17")

    ChrTalk(    #14
        0x8,
        (
            "We've got lots of fruit in stock from Ravennue\x01",
            "Village! These goods'll move faster than a\x01",
            "Shining Pom! Don't miss out!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "I recommend the fresh Rolent vegetables!\x01",
            "They're super fresh! Even a Gourd Boar\x01",
            "wouldn't miss out on this deal!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F93")

    label("loc_E17")


    ChrTalk(    #16
        0x8,
        "Come, take a look.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "I've got lots of fresh fruit just harvested\x01",
            "from Ravennue Village! Crop munchers\x01",
            "would kill for this stuff! Get it now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "If you're thinking over what to make for dinner,\x01",
            "then how about some vegetables from Rolent?\x01",
            "They pair well with dinedile steaks!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "We just got a fresh delivery from Perzel Farm!\x01",
            "Don't be a creepy sheep, get in on this!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_F93")

    TalkEnd(0x8)
    Return()

    # Function_9_79E end

    def Function_10_F97(): pass

    label("Function_10_F97")

    Call(0, 11)
    Return()

    # Function_10_F97 end

    def Function_11_F9C(): pass

    label("Function_11_F9C")

    TalkBegin(0x9)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1009")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FFE")
    OP_A9(0x3D)
    Jump("loc_1000")

    label("loc_FFE")

    OP_A9(0x5F)

    label("loc_1000")

    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_1009")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_101A")
    TalkEnd(0x9)
    Return()

    label("loc_101A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_118B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10FD")

    ChrTalk(    #20
        0x9,
        (
            "All stores in the market are\x01",
            "having a 'thank you' sale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x9,
        (
            "Thanks to the little lady we've got stock in,\x01",
            "so it's time to brighten the mood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x9,
        (
            "The Bose Market's always on\x01",
            "the side of the citizens.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1188")

    label("loc_10FD")


    ChrTalk(    #23
        0x9,
        (
            "All stores in the market are\x01",
            "having a 'thank you' sale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x9,
        (
            "We'll be putting out some real special stuff,\x01",
            "so be sure to take a look.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1188")

    Jump("loc_17E9")

    label("loc_118B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1424")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_130D")

    ChrTalk(    #25
        0x9,
        (
            "Wh-What should I do?\x01",
            "No goods are coming in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x9,
        (
            "Honestly, I probably ought to be considering\x01",
            "raising prices here, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x9,
        (
            "Once before, we took advantage of the\x01",
            "situation to raise prices and ended up\x01",
            "causing a lot of trouble for everyone...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x9,
        (
            "I can't really raise my prices\x01",
            "so easily these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x9,
        (
            "I need to talk to Buck and figure\x01",
            "out a good plan.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1421")

    label("loc_130D")


    ChrTalk(    #30
        0x9,
        (
            "With distribution stopped, I probably ought to\x01",
            "be considering raising prices here, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x9,
        (
            "Once before, we took advantage of the\x01",
            "situation to raise prices and ended up\x01",
            "causing a lot of trouble for everyone...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x9,
        (
            "I can't really raise my prices\x01",
            "so easily these days.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1421")

    Jump("loc_17E9")

    label("loc_1424")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1643")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_14F0")

    ChrTalk(    #33
        0x9,
        (
            "We're currently in the middle of\x01",
            "a restoration memorial sale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x9,
        (
            "After all, resuming business is a big event\x01",
            "on its own. We need to make sure we use it\x01",
            "for business, not waste it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1640")

    label("loc_14F0")


    ChrTalk(    #35
        0x9,
        (
            "Hey, welcome. We're currently in the middle\x01",
            "of a restoration memorial sale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x9,
        (
            "After all, it's the first day we're back\x01",
            "in business. No way am I not going to\x01",
            "use it to sell product.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x9,
        (
            "'Even if you fall, don't just\x01",
            "get up for nothing'...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x9,
        (
            "It's a line of Miss Minuet's, but that really\x01",
            "is what it means to be a merchant.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1640")

    Jump("loc_17E9")

    label("loc_1643")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_17E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_16DA")

    ChrTalk(    #39
        0x9,
        (
            "I've got lots of great deals,\x01",
            "so, please, take a look.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x9,
        (
            "And while you're at it, look over my\x01",
            "partner's products, next to me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17E9")

    label("loc_16DA")


    ChrTalk(    #41
        0x9,
        (
            "Lately Bose's been safe and peaceful, so getting\x01",
            "products in stock's been totally stable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x9,
        (
            "Thanks to that, our shelves are full of\x01",
            "great stuff. Please, take a peek.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x9,
        (
            "Ohh, and also check out Buck's store.\x01",
            "His is the one next to mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x9,
        "He's my partner.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_17E9")

    TalkEnd(0x9)
    Return()

    # Function_11_F9C end

    def Function_12_17ED(): pass

    label("Function_12_17ED")

    TalkBegin(0xA)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_185A")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_184F")
    OP_A9(0x40)
    Jump("loc_1851")

    label("loc_184F")

    OP_A9(0x5C)

    label("loc_1851")

    OP_56(0x0)
    TalkEnd(0xA)
    Return()

    label("loc_185A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_186B")
    TalkEnd(0xA)
    Return()

    label("loc_186B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_1A40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1989")

    ChrTalk(    #45
        0xA,
        (
            "We're in the middle of a market-wide sale,\x01",
            "so I've got some special stuff on offer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xA,
        (
            "It was the idea of the guys over at the fruit\x01",
            "store, but I think it was a really good one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xA,
        (
            "So, then, I gotta make sure I keep my\x01",
            "voice up there with everyone else's.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1A3D")

    label("loc_1989")


    ChrTalk(    #48
        0xA,
        (
            "We're in the middle of a market-wide sale,\x01",
            "so I've got some special stuff on offer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xA,
        (
            "I've got to make sure to keep my voice as\x01",
            "loud and strong as any of the other stores.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A3D")

    Jump("loc_1C8F")

    label("loc_1A40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1ADD")

    ChrTalk(    #50
        0xA,
        (
            "No one really knows why the doors or\x01",
            "the fountain have suddenly stopped\x01",
            "working, it sounds like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xA,
        "What the heck is going on in this city?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C8F")

    label("loc_1ADD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1BB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1B49")

    ChrTalk(    #52
        0xA,
        "Hey, welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xA,
        (
            "We've got lots of handy stuff practically\x01",
            "falling off the shelves!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BB0")

    label("loc_1B49")


    ChrTalk(    #54
        0xA,
        "My husband's helping out around the store today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xA,
        "Thanks to that, I can focus on business.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1BB0")

    Jump("loc_1C8F")

    label("loc_1BB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_1C8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1C04")

    ChrTalk(    #56
        0xA,
        (
            "Hey, hey, welcome! We've got lots\x01",
            "of useful general goods.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C8F")

    label("loc_1C04")


    ChrTalk(    #57
        0xA,
        (
            "Hey, hey, welcome, we've got lots\x01",
            "of useful general goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xA,
        (
            "Stuff to scratch that itch is practically\x01",
            "falling off the shelves!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1C8F")

    TalkEnd(0xA)
    Return()

    # Function_12_17ED end

    def Function_13_1C93(): pass

    label("Function_13_1C93")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_1D10")

    ChrTalk(    #59
        0xB,
        (
            "Apparently the whole market's doing\x01",
            "some kind of support sale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xB,
        "Mom's even more energetic than normal.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2088")

    label("loc_1D10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1E32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DD0")

    ChrTalk(    #61
        0xB,
        (
            "It seems like orbments have stopped\x01",
            "working all over town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xB,
        (
            "The register at our store's\x01",
            "stopped working too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xB,
        "Dad's off at the factory getting it repaired.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_1E2F")

    label("loc_1DD0")


    ChrTalk(    #64
        0xB,
        (
            "It seems like orbments have stopped\x01",
            "working all over town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xB,
        "I wonder what's going on.\x02",
    )

    CloseMessageWindow()

    label("loc_1E2F")

    Jump("loc_2088")

    label("loc_1E32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1F62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1EC2")

    ChrTalk(    #66
        0xB,
        "I'm happy he's helping, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xB,
        "Dad keeps getting where things go wrong.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xB,
        "He'd better get used to the job soon...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F5F")

    label("loc_1EC2")

    OP_62(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xB, 0x1F, 400)

    ChrTalk(    #69
        0xB,
        "Ah, Dad. That doesn't go on that shelf.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xB,
        (
            "Come on, keep it together. You made\x01",
            "the same mistake just a bit ago.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    ClearChrFlags(0xB, 0x10)

    label("loc_1F5F")

    Jump("loc_2088")

    label("loc_1F62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_2088")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1FF3")

    ChrTalk(    #71
        0xB,
        (
            "I'm part of the staff here.\x01",
            "I'm helping Mom out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xB,
        (
            "We've got lots of useful stuff.\x01",
            "Please take a look around the store.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2088")

    label("loc_1FF3")


    ChrTalk(    #73
        0xB,
        "Ah, welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xB,
        (
            "I'm part of the staff here.\x01",
            "I'm helping Mom out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xB,
        (
            "We've got lots of useful stuff.\x01",
            "Please take a look around the store.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2088")

    TalkEnd(0xB)
    Return()

    # Function_13_1C93 end

    def Function_14_208C(): pass

    label("Function_14_208C")

    Call(0, 15)
    Return()

    # Function_14_208C end

    def Function_15_2091(): pass

    label("Function_15_2091")

    TalkBegin(0xC)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20FE")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20F3")
    OP_A9(0x3C)
    Jump("loc_20F5")

    label("loc_20F3")

    OP_A9(0x5A)

    label("loc_20F5")

    OP_56(0x0)
    TalkEnd(0xC)
    Return()

    label("loc_20FE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_210F")
    TalkEnd(0xC)
    Return()

    label("loc_210F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_211C")
    OP_A2(0x6)

    label("loc_211C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21C3")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as finished QST017 in the previous game\x01",             # 0
            "Set as did not finish QST017 in the previous game.\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_21B7"),
        (1, "loc_21BD"),
        (SWITCH_DEFAULT, "loc_21C3"),
    )


    label("loc_21B7")

    OP_A2(0x6)
    Jump("loc_21C3")

    label("loc_21BD")

    OP_A3(0x6)
    Jump("loc_21C3")

    label("loc_21C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x348, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2830")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_269B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_23BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_232F")

    ChrTalk(    #76
        0xC,
        (
            "Ho ho. To plan a big sale at a time like this...\x01",
            "The young folk sure are energetic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xC,
        (
            "As a practical matter, it seems there\x01",
            "was aid from Mayor Maybelle, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xC,
        (
            "It seems the good old Bose merchant\x01",
            "spirit's still alive and well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xC,
        (
            "Of course, we're putting out some treasured\x01",
            "items as goods at this shop, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_23B9")

    label("loc_232F")


    ChrTalk(    #80
        0xC,
        (
            "Ho ho. To plan a big sale at a time like this...\x01",
            "The young folk sure are energetic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xC,
        "Of course, our store will be participating.\x02",
    )

    CloseMessageWindow()

    label("loc_23B9")

    Jump("loc_2698")

    label("loc_23BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_250B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24A2")

    ChrTalk(    #82
        0xC,
        (
            "All distribution throughout the kingdom's\x01",
            "gone kaput, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xC,
        (
            "I have enough stock for the moment,\x01",
            "but if I can't restock, then sooner or\x01",
            "later shortages will come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xC,
        "Hmm... This is quite grave.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_2508")

    label("loc_24A2")


    ChrTalk(    #85
        0xC,
        (
            "All distribution throughout the kingdom's\x01",
            "gone kaput, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xC,
        "Hmm... This is quite grave.\x02",
    )

    CloseMessageWindow()

    label("loc_2508")

    Jump("loc_2698")

    label("loc_250B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_25AC")

    ChrTalk(    #87
        0xC,
        (
            "Thanks to the authority of the queen, the\x01",
            "dragon has been driven off, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xC,
        (
            "The market's been restored,\x01",
            "so now I can return to business.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2698")

    label("loc_25AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_2698")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2629")

    ChrTalk(    #89
        0xC,
        "If you need medicine, leave it to us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xC,
        (
            "I even carry new medicines developed\x01",
            "by the Septium Church.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2698")

    label("loc_2629")


    ChrTalk(    #91
        0xC,
        "If you need medicine, leave it to us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xC,
        (
            "I've a wide selection from injury\x01",
            "medicine to restoratives.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_2698")

    Jump("loc_282D")

    label("loc_269B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2722")

    ChrTalk(    #93
        0xC,
        (
            "I've got useful medicine to help you\x01",
            "with your job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xC,
        (
            "Should you need anything, please,\x01",
            "come by the Spence Pharmacy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_282D")

    label("loc_2722")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_27A9")

    ChrTalk(    #95
        0xC,
        (
            "I've got useful medicine to help you\x01",
            "with your job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xC,
        (
            "Should you need anything, please,\x01",
            "come by the Spence Pharmacy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_282D")

    label("loc_27A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_282D")

    ChrTalk(    #97
        0xC,
        (
            "I've got useful medicine to help you\x01",
            "with your job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xC,
        (
            "Should you need anything, please,\x01",
            "come by the Spence Pharmacy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_282D")

    Jump("loc_33AF")

    label("loc_2830")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2C04")
    TurnDirection(0xC, 0x101, 0)
    OP_62(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(    #99
        0xC,
        "Oh, everyone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xC,
        (
            "You're the bracers who helped me get a\x01",
            "hold of some Bear Claw some time ago,\x01",
            "yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x101,
        "#1011FOh, yeah, now that you mention it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x102,
        (
            "#1040FHaha... It's a bit nostalgic.\x02\x03",

            "Happy to see you're still\x01",
            "in good health, sir.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x102, 400)

    ChrTalk(    #103
        0xC,
        (
            "Ho ho, health is my one strength,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xC,
        "Still, though, you were a great help back then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xC,
        (
            "Since you've come by, allow me to offer\x01",
            "you a treasured piece of medicine.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #106
        "\x07\x00Received #517i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x205, 1)

    ChrTalk(    #107
        0xC,
        "No need to hesitate, take it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xC,
        "It's my way of saying thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        (
            "#1001FWooow, thanks.\x02\x03",

            "Well, then, since you're offering,\x01",
            "we'll gladly accept it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x102,
        "#1041FThank you very much...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xC,
        (
            "I've got lots of other useful medicines\x01",
            "to help you at your job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xC,
        (
            "Should you need anything, please,\x01",
            "come by the Spence Pharmacy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        (
            "#1016FR-Right, got it.\x02\x03",

            "(W-Well, that's a merchant for you...\x01",
            "Never miss a beat on the job.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33A9")

    label("loc_2C04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_3036")
    TurnDirection(0xC, 0x101, 0)
    OP_62(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #114
        0xC,
        "Oh, everyone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xC,
        (
            "You're the bracers who helped me get a\x01",
            "hold of some Bear Claw some time ago,\x01",
            "yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        (
            "#1016FOh, yeah. Now that you mention it,\x01",
            "that did happen.\x02\x03",

            "#1000FIt's been quite a while. Things have\x01",
            "been hard lately, I'm sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xC,
        "Ho ho ho. Oh, this is nothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xC,
        (
            "Barely worth mentioning compared\x01",
            "to during the Hundred Days War.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xC,
        (
            "Now, putting that aside, since\x01",
            "you've come out to my store...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xC,
        "Let me offer you my thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x101,
        "#1011FThanks...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xC,
        (
            "Ho ho ho. Thanks for calming the dragon,\x01",
            "of course.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #123
        "\x07\x00Received #517i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x205, 1)

    ChrTalk(    #124
        0xC,
        (
            "It's a powerfully effective medicine,\x01",
            "so I'm sure it'll be helpful to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xC,
        "Please, go ahead, take it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        (
            "#1001FWooow, thanks.\x02\x03",

            "Well, then, since you're offering,\x01",
            "we'll gladly accept it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xC,
        (
            "I've got lots of other useful medicines\x01",
            "to help you at your job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xC,
        (
            "Should you need anything, please,\x01",
            "come by the Spence Pharmacy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x101,
        (
            "#1016FR-Right, got it.\x02\x03",

            "(W-Well, that's a merchant for you...\x01",
            "Never miss a beat on the job.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33A9")

    label("loc_3036")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_33A9")
    TurnDirection(0xC, 0x101, 0)
    OP_62(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #130
        0xC,
        "Oh, everyone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xC,
        (
            "You're the bracers who helped me get a\x01",
            "hold of some Bear Claw some time ago,\x01",
            "yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        (
            "#1016FOh, yeah. Now that you mention it,\x01",
            "that did happen.\x02\x03",

            "#1000FIt's been a while.\x01",
            "Have you been well, sir?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xC,
        "Yes, yes, as always.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xC,
        "Still, you really were a great help at the time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xC,
        (
            "Since you've come by, allow me to offer\x01",
            "you a treasured piece of medicine.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #136
        "\x07\x00Received #517i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x205, 1)

    ChrTalk(    #137
        0xC,
        "No need to hesitate, take it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xC,
        "It's my way of saying thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x101,
        (
            "#1001FWooow, thanks.\x02\x03",

            "Well, then, since you're offering,\x01",
            "we'll gladly accept it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xC,
        (
            "I've got lots of other useful medicines\x01",
            "to help you at your job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xC,
        (
            "Should you need anything, please,\x01",
            "come by the Spence Pharmacy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x101,
        (
            "#1016FR-Right, got it.\x02\x03",

            "(W-Well, that's a merchant for you...\x01",
            "Never miss a beat on the job.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33A9")

    OP_A2(0x1A40)
    OP_A2(0x4)

    label("loc_33AF")

    TalkEnd(0xC)
    Return()

    # Function_15_2091 end

    def Function_16_33B3(): pass

    label("Function_16_33B3")

    TalkBegin(0xD)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3420")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3415")
    OP_A9(0x3F)
    Jump("loc_3417")

    label("loc_3415")

    OP_A9(0x5E)

    label("loc_3417")

    OP_56(0x0)
    TalkEnd(0xD)
    Return()

    label("loc_3420")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3431")
    TalkEnd(0xD)
    Return()

    label("loc_3431")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_3586")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34CD")

    ChrTalk(    #143
        0xD,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xD,
        (
            "We've got castella cake made with the fluffiest\x01",
            "eggs! It's a must-try of the Bose Market!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xD,
        "Would you like one?!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_3583")

    label("loc_34CD")


    ChrTalk(    #146
        0xD,
        "I've got to try to cheer up the customers...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xD,
        "I'm joining in on the sale with everyone else.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xD,
        (
            "I'd like it if people could at least\x01",
            "be smiling while they're shopping.\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x7)

    label("loc_3583")

    Jump("loc_3939")

    label("loc_3586")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3734")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3679")

    ChrTalk(    #149
        0xD,
        (
            "Making castella cake takes fresh eggs and\x01",
            "milk. You can't skimp if you want the best!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xD,
        (
            "If I continue to be unable to get stock in,\x01",
            "I won't be able to keep this stand running.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xD,
        "*sigh* What am I supposed to do?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_3731")

    label("loc_3679")


    ChrTalk(    #152
        0xD,
        (
            "Making castella cake takes fresh eggs and\x01",
            "milk. You can't skimp if you want the best!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xD,
        (
            "If I continue to be unable to get stock in,\x01",
            "I won't be able to keep this stand running.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3731")

    Jump("loc_3939")

    label("loc_3734")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_3831")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_37BE")

    ChrTalk(    #154
        0xD,
        (
            "We've got castella cake made with the fluffiest\x01",
            "eggs! It's a must-try of the Bose Market!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xD,
        "Would you like one?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_382E")

    label("loc_37BE")


    ChrTalk(    #156
        0xD,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xD,
        (
            "We've got castella cake made with the fluffiest\x01",
            "eggs! It's a must-try of the Bose Market!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_382E")

    Jump("loc_3939")

    label("loc_3831")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_3939")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_38AF")

    ChrTalk(    #158
        0xD,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xD,
        (
            "We've got castella cake made with the fluffiest\x01",
            "eggs! It's a must-try of the Bose Market!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3939")

    label("loc_38AF")


    ChrTalk(    #160
        0xD,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xD,
        (
            "We've got castella cake made with the fluffiest\x01",
            "eggs! It's a must-try of the Bose Market!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xD,
        "Would you like one?!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_3939")

    TalkEnd(0xD)
    Return()

    # Function_16_33B3 end

    def Function_17_393D(): pass

    label("Function_17_393D")

    TalkBegin(0xE)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39AA")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_399F")
    OP_A9(0x43)
    Jump("loc_39A1")

    label("loc_399F")

    OP_A9(0x5B)

    label("loc_39A1")

    OP_56(0x0)
    TalkEnd(0xE)
    Return()

    label("loc_39AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39BB")
    TalkEnd(0xE)
    Return()

    label("loc_39BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_3B83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B2A")

    ChrTalk(    #163
        0xE,
        (
            "A market-wide sale...\x01",
            "What a thoughtful plan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xE,
        (
            "Katrina's all on board with it,\x01",
            "so I'll take part too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xE,
        (
            "Well, it's thanks to Mayor Maybelle\x01",
            "I can at all, to be honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xE,
        (
            "The mayor managed to persuade the big\x01",
            "merchants to not lock up their stock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xE,
        (
            "If that'd happened, then prices would be\x01",
            "shot through the roof right about now.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_3B80")

    label("loc_3B2A")


    ChrTalk(    #168
        0xE,
        "Hey, welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xE,
        (
            "I've got delicious ice cream,\x01",
            "even popular in the capital!\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x8)

    label("loc_3B80")

    Jump("loc_3E1B")

    label("loc_3B83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3CE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C57")

    ChrTalk(    #170
        0xE,
        "The market's really lost all its energy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xE,
        (
            "I guess everyone is really\x01",
            "worried about the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xE,
        (
            "Damn it! I really wish I could help people\x01",
            "at times like these especially, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_3CE3")

    label("loc_3C57")


    ChrTalk(    #173
        0xE,
        (
            "If even the market gets all dark,\x01",
            "it really is all over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xE,
        (
            "I really wish I could help people at\x01",
            "times like these especially, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CE3")

    Jump("loc_3E1B")

    label("loc_3CE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_3D77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_3D32")

    ChrTalk(    #175
        0xE,
        "Welcome, welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xE,
        "We've got delicious ice cream!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D74")

    label("loc_3D32")


    ChrTalk(    #177
        0xE,
        "Heeey, welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xE,
        "Delicious ice cream is finally back!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_3D74")

    Jump("loc_3E1B")

    label("loc_3D77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_3E1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_3DC3")

    ChrTalk(    #179
        0xE,
        "Welcome, welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xE,
        "We've got delicious ice cream!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E1B")

    label("loc_3DC3")


    ChrTalk(    #181
        0xE,
        "Heeey, welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xE,
        (
            "I've got delicious ice cream,\x01",
            "even popular in the capital!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_3E1B")

    TalkEnd(0xE)
    Return()

    # Function_17_393D end

    def Function_18_3E1F(): pass

    label("Function_18_3E1F")

    Call(0, 19)
    Return()

    # Function_18_3E1F end

    def Function_19_3E24(): pass

    label("Function_19_3E24")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E91")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E86")
    OP_A9(0x41)
    Jump("loc_3E88")

    label("loc_3E86")

    OP_A9(0x5D)

    label("loc_3E88")

    OP_56(0x0)
    TalkEnd(0xF)
    Return()

    label("loc_3E91")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3EA2")
    TalkEnd(0xF)
    Return()

    label("loc_3EA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_3FAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F54")

    ChrTalk(    #183
        0xF,
        "Heeey, welcome! Take a look if you'd like.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xF,
        "Haha. It's been a while since I yelled like this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xF,
        "After all, this kind of business isn't my style.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_3FA8")

    label("loc_3F54")


    ChrTalk(    #186
        0xF,
        "Heeey, welcome! Take a look if you'd like.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xF,
        "I'm sure you'll like my stuff!\x02",
    )

    CloseMessageWindow()

    label("loc_3FA8")

    Jump("loc_4689")

    label("loc_3FAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_416C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40D9")

    ChrTalk(    #188
        0xF,
        (
            "Orbments are all stopped... Man, talk\x01",
            "about one to send you into the dumps.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xF,
        (
            "All the lights at my house are out and\x01",
            "my daughter's crying her eyes out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xF,
        (
            "After all, orbments are an expected\x01",
            "part of life for her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xF,
        (
            "It was a shock when I realized\x01",
            "we couldn't use them.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_4169")

    label("loc_40D9")


    ChrTalk(    #192
        0xF,
        (
            "To my daughter's generation, orbments\x01",
            "are an expected part of life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xF,
        (
            "The shock might've been a lot bigger\x01",
            "for them than for us adults.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4169")

    Jump("loc_4689")

    label("loc_416C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_42E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_4203")

    ChrTalk(    #194
        0xF,
        (
            "I really wanted to show my daughter\x01",
            "the market now that's it's all fixed up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xF,
        "I want her to know that the city's safe again.\x02",
    )

    CloseMessageWindow()
    Jump("loc_42E0")

    label("loc_4203")


    ChrTalk(    #196
        0xF,
        (
            "I brought my daughter Elke along to\x01",
            "show her the restored market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xF,
        (
            "After all, my daughter is very\x01",
            "literally one half of my shop name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xF,
        (
            "We here at Paul & Elke's Outlet look\x01",
            "forward to your future business!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_42E0")

    Jump("loc_4689")

    label("loc_42E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_4689")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x348, 1)), scpexpr(EXPR_END)), "loc_4491")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_43A5")

    ChrTalk(    #199
        0xF,
        (
            "Man, brands from the capital really are\x01",
            "that much different than anywhere else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xF,
        (
            "I've still got a long ways to go towards\x01",
            "building up my shop's original brands.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_448E")

    label("loc_43A5")

    TurnDirection(0xF, 0x101, 0)

    ChrTalk(    #201
        0xF,
        "Those clothes of yours...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xF,
        (
            "They've got a very functional design,\x01",
            "but still compliment the loveliness of\x01",
            "a young woman...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xF,
        (
            "It's frustrating, but that's what I'd expect\x01",
            "from a first class brand from the capital.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_448E")

    Jump("loc_4689")

    label("loc_4491")


    ChrTalk(    #204
        0xF,
        "Welcome. What are you looking for today?\x02",
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xF, 0x101, 400)
    Sleep(400)

    ChrTalk(    #205
        0xF,
        (
            "Wait, those clothes...\x01",
            "Are those a capital brand?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x101,
        "#1004FHuh, wow, I'm surprised you know.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_458A")

    ChrTalk(    #207
        0x103,
        "#021FHeh. Well, that's a professional for you.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x103, 400)

    label("loc_458A")


    ChrTalk(    #208
        0xF,
        (
            "Haha, yeah, I've seen more\x01",
            "clothes than most people.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x101, 400)

    ChrTalk(    #209
        0xF,
        (
            "Still, from a first-class brand,\x01",
            "and order made at that, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xF,
        (
            "It's frustrating, but...that's an\x01",
            "incredible design.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xF,
        (
            "*sigh* I gotta keep improving if\x01",
            "I ever hope to compete.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A41)

    label("loc_4689")

    TalkEnd(0xF)
    Return()

    # Function_19_3E24 end

    def Function_20_468D(): pass

    label("Function_20_468D")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4728")
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4700")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46FB")
    OP_A9(0x4C)
    Jump("loc_46FD")

    label("loc_46FB")

    OP_A9(0x4D)

    label("loc_46FD")

    Jump("loc_471F")

    label("loc_4700")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4711")
    OP_A9(0x45)
    Jump("loc_471F")

    label("loc_4711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_471D")
    OP_A9(0x44)
    Jump("loc_471F")

    label("loc_471D")

    OP_A9(0x42)

    label("loc_471F")

    OP_56(0x0)
    TalkEnd(0x10)
    Return()

    label("loc_4728")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4739")
    TalkEnd(0x10)
    Return()

    label("loc_4739")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_4906")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x218, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_489C")

    ChrTalk(    #212
        0x10,
        (
            "Market-wide sale, hmm.\x01",
            "Nothing to do with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x10,
        "After all, my store's running sales every day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x10,
        (
            "Well, as a supporting shop I do intend to\x01",
            "at least offer some stuff at a loss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        (
            "Hey, hey, you!\x01",
            "Read this book and cheer up!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #216
        "\x07\x00Received #583i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    OP_3E(0x247, 1)
    OP_A2(0x10C2)
    OP_0D()

    ChrTalk(    #217
        0x101,
        "#1004FWow, thanks.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4903")

    label("loc_489C")


    ChrTalk(    #218
        0x10,
        (
            "Market-wide sale, hmm.\x01",
            "Nothing to do with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x10,
        "After all, my store's running sales every day.\x02",
    )

    CloseMessageWindow()

    label("loc_4903")

    Jump("loc_4DBF")

    label("loc_4906")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4ACA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A23")

    ChrTalk(    #220
        0xFE,
        (
            "I don't care if distribution's stopped or whatnot.\x01",
            "I'll be opening this shop just like always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xFE,
        (
            "It's at times like this you gotta\x01",
            "give people some courage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        (
            "...If it's come down to this, then maybe\x01",
            "I should sell that new issue I've been\x01",
            "keeping safe.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_4AC7")

    label("loc_4A23")


    ChrTalk(    #223
        0xFE,
        (
            "It's at times like this you gotta\x01",
            "give people some courage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        (
            "...If it's come down to this, then maybe\x01",
            "I should sell that new issue I've been\x01",
            "keeping safe.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AC7")

    Jump("loc_4DBF")

    label("loc_4ACA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_4C5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_4B3F")

    ChrTalk(    #225
        0x10,
        (
            "I've got top-class carpets from\x01",
            "the Republic for just 500 mira!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x10,
        "Get another one for free!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C59")

    label("loc_4B3F")


    ChrTalk(    #227
        0x10,
        "Come on by! Take a look!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x10,
        (
            "I've got top-class carpets from\x01",
            "the Republic for just 500 mira!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x10,
        "Just 500 mira!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x10,
        "And you know what else?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x10,
        "As part of our return to business campaign...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x10,
        (
            "You get another one of the same\x01",
            "#4Scarpet for freeeeee!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x10,
        "What a deal!\x02",
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_4C59")

    Jump("loc_4DBF")

    label("loc_4C5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_4DBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_4D0B")

    ChrTalk(    #234
        0x10,
        (
            "We've got old books, textiles, and daily\x01",
            "goods. You'll find everything you need\x01",
            "at Minuet's Stand!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x10,
        (
            "Take a look. We've got some new\x01",
            "magazine issues.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DBF")

    label("loc_4D0B")


    ChrTalk(    #236
        0x10,
        "Hey, welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x10,
        (
            "We've got old books, textiles, and daily\x01",
            "goods. You'll find everything you need\x01",
            "at Minuet's Stand!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x10,
        (
            "Take a look. We've got some new\x01",
            "magazine issues.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_4DBF")

    TalkEnd(0x10)
    Return()

    # Function_20_468D end

    def Function_21_4DC3(): pass

    label("Function_21_4DC3")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_4F76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ED9")

    ChrTalk(    #239
        0x11,
        (
            "The market really does brighten up\x01",
            "with a sale like this going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x11,
        (
            "It really feels like the life is back\x01",
            "into it for the first time in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x11,
        (
            "And with our lady mayor here to\x01",
            "check up on things, everyone's\x01",
            "pushing themselves even harder.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_4F73")

    label("loc_4ED9")


    ChrTalk(    #242
        0x11,
        (
            "The market really does brighten up\x01",
            "with a sale like this going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x11,
        (
            "It really feels like the life is back\x01",
            "into it for the first time in a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F73")

    Jump("loc_53A6")

    label("loc_4F76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_50CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5064")

    ChrTalk(    #244
        0x11,
        "Hey, welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x11,
        (
            "Minuet's well, but...the whole market's\x01",
            "a bit down in the dumps.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x11,
        (
            "After all, just as everyone's recovered,\x01",
            "now distribution's totally frozen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x11,
        "It's not surprising they'd get depressed.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_50C8")

    label("loc_5064")


    ChrTalk(    #248
        0x11,
        "Minuet's as energetic as always.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x11,
        (
            "That old lady's merchant spirit is\x01",
            "the toughest in Bose.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50C8")

    Jump("loc_53A6")

    label("loc_50CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_521E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_515C")

    ChrTalk(    #250
        0x11,
        (
            "With the military restrictions lifted,\x01",
            "distribution's back to normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x11,
        "New issues should start getting delivered soon.\x02",
    )

    CloseMessageWindow()
    Jump("loc_521B")

    label("loc_515C")


    ChrTalk(    #252
        0x11,
        "Hey, welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x11,
        (
            "With the military restrictions lifted,\x01",
            "distribution's back to normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x11,
        "New issues should start getting delivered soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x11,
        "If you'd like, check out the store.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_521B")

    Jump("loc_53A6")

    label("loc_521E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_53A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_52A9")

    ChrTalk(    #256
        0x11,
        (
            "As you can see, I'm a part-timer\x01",
            "here at the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x11,
        (
            "I actually got offered the job\x01",
            "because I really like books.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53A6")

    label("loc_52A9")


    ChrTalk(    #258
        0x11,
        (
            "Hey, welcome. We've got the latest\x01",
            "magazines in stock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x11,
        (
            "As you can see, I'm a part-timer\x01",
            "here at the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x11,
        (
            "I actually got offered the job\x01",
            "because I really like books.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x11,
        (
            "Didn't expect to end up working\x01",
            "at a familiar place like this.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_53A6")

    TalkEnd(0x11)
    Return()

    # Function_21_4DC3 end

    def Function_22_53AA(): pass

    label("Function_22_53AA")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_550B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_547B")

    ChrTalk(    #262
        0xFE,
        (
            "Heh heh heh. This! This is what\x01",
            "I've been waiting for!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xFE,
        (
            "Sales! Special offers! DEALS!!\x01",
            "Ahh, what a sweet sound...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0xFE,
        (
            "Just hearing the word at any\x01",
            "time makes my spirits rise!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_5508")

    label("loc_547B")


    ChrTalk(    #265
        0xFE,
        (
            "If there are gonna be special offers,\x01",
            "then I'm not leavin' till I get them all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0xFE,
        (
            "Heh heh. I'm gonna charge in the\x01",
            "second they open!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5508")

    Jump("loc_5897")

    label("loc_550B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_55C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55BE")

    ChrTalk(    #267
        0xFE,
        (
            "With scheduled flights and transport\x01",
            "stopped, things are really serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0xFE,
        (
            "Anyway, I'd better go shopping and stock\x01",
            "up while the stores still HAVE stock...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55BE")

    Jump("loc_5897")

    label("loc_55C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_5701")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_565E")

    ChrTalk(    #269
        0xFE,
        (
            "Heh heh heh. Today there's a\x01",
            "restoration memorial sale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0xFE,
        (
            "I've got the best position by lining\x01",
            "up in front of the store in advance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56FE")

    label("loc_565E")


    ChrTalk(    #271
        0xFE,
        (
            "Heh heh heh. Today there's a\x01",
            "restoration memorial sale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0xFE,
        "Ahh, the first price cut in a while...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0xFE,
        "I'm not offering this best position to ANYONE.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_56FE")

    Jump("loc_5897")

    label("loc_5701")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_5897")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_57AA")

    ChrTalk(    #274
        0xFE,
        (
            "Seems like all the special offers during\x01",
            "the morning have already ended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0xFE,
        (
            "Next chance to aim for will be timed\x01",
            "sales during the evening, then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5897")

    label("loc_57AA")


    ChrTalk(    #276
        0xFE,
        (
            "Now, then. Seems like all the special offers\x01",
            "during the morning have already ended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0xFE,
        (
            "Heh heh. Of course I've checked\x01",
            "every store in the market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xFE,
        (
            "Thanks to that I got some great meat at\x01",
            "an absolutely shockingly low price.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_5897")

    TalkEnd(0x12)
    Return()

    # Function_22_53AA end

    def Function_23_589B(): pass

    label("Function_23_589B")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_5970")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_590C")

    ChrTalk(    #279
        0xFE,
        "A sale means to offer stuff for cheap, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0xFE,
        "Heh heh. I know what that means.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xD)
    Jump("loc_596D")

    label("loc_590C")


    ChrTalk(    #281
        0xFE,
        (
            "Mom always gets really happy\x01",
            "when we buy things on sale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xFE,
        "All right, let's do our best!\x02",
    )

    CloseMessageWindow()

    label("loc_596D")

    Jump("loc_5C3F")

    label("loc_5970")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_59E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59C4")

    ChrTalk(    #283
        0xFE,
        "Even the fountain's tired...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xFE,
        "I wonder what happened.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xD)
    Jump("loc_59E6")

    label("loc_59C4")


    ChrTalk(    #285
        0xFE,
        "Even the fountain's tired...\x02",
    )

    CloseMessageWindow()

    label("loc_59E6")

    Jump("loc_5C3F")

    label("loc_59E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_5B12")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_5A5C")

    ChrTalk(    #286
        0xFE,
        "Heehee, we're gonna have some castella today!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0xFE,
        "Castella, castella, castellaaaaaaaa... ♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_5B0F")

    label("loc_5A5C")


    ChrTalk(    #288
        0xFE,
        "Teehee, today I'm not here on errands.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0xFE,
        (
            "I got my allowance, so I'm here\x01",
            "to do some shoppin' of my own. ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0xFE,
        (
            "I'm gonna eat some of the castella\x01",
            "this lady's sellin'!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_5B0F")

    Jump("loc_5C3F")

    label("loc_5B12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_5C3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_5B70")

    ChrTalk(    #291
        0xFE,
        "Cheese, apple, and po-ta-to... ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xFE,
        "Cheese, apple and po-ta-to... ♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_5C3F")

    label("loc_5B70")


    ChrTalk(    #293
        0xFE,
        (
            "I'm old enough to go shoppin' aaaaall\x01",
            "on my own now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0xFE,
        (
            "So, you know, I made a song so I'd\x01",
            "remember what I need to buy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xFE,
        "Cheese, apple, and po-ta-to, it goes... ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0xFE,
        "Heh. Pretty great, huh?\x02",
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_5C3F")

    TalkEnd(0x14)
    Return()

    # Function_23_589B end

    def Function_24_5C43(): pass

    label("Function_24_5C43")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_5D91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D03")

    ChrTalk(    #297
        0xFE,
        "Huh, a sale at a time like this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0xFE,
        "Heehee. That actually makes me really happy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xFE,
        (
            "That's Bose Market for you. They really\x01",
            "know how the citizens are feeling.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_5D8E")

    label("loc_5D03")


    ChrTalk(    #300
        0xFE,
        (
            "Well, since there's a sale going on, let's\x01",
            "make dinner a bit more extravagant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0xFE,
        (
            "All right!\x01",
            "Now, what should tonight's menu be...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D8E")

    Jump("loc_6193")

    label("loc_5D91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_5E2B")

    ChrTalk(    #302
        0xFE,
        (
            "With the orbments stopped, lights\x01",
            "and heating are all unusable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0xFE,
        (
            "Once I'm done shopping for foodstuffs,\x01",
            "I need to go look at sundries.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6193")

    label("loc_5E2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_6097")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_5F32")

    ChrTalk(    #304
        0xFE,
        (
            "It'd be nice if rather than just selling\x01",
            "ingredients, they also taught you what\x01",
            "to make.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0xFE,
        "That'd certainly be a load off a housewife's mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0xFE,
        (
            "Yeah, thinking about it, that's only reasonable.\x01",
            "I'm going to go negotiate with the store.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6094")

    label("loc_5F32")


    ChrTalk(    #307
        0xFE,
        (
            "Meat, vegetables, fish...\x01",
            "*sigh* What should I do today...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0xFE,
        (
            "It'd be nice if rather than just selling\x01",
            "ingredients they also taught you what to\x01",
            "make...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0xFE,
        (
            "...Now that I think about it, yes,\x01",
            "it really would.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0xFE,
        (
            "After all, when you buy a vacuum cleaner\x01",
            "they show you how to use it, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0xFE,
        "Why don't they do the same with meat and fish?\x02",
    )

    CloseMessageWindow()
    OP_A2(0xE)

    label("loc_6094")

    Jump("loc_6193")

    label("loc_6097")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_6193")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_6120")

    ChrTalk(    #312
        0xFE,
        "What should I make for dinner tonight...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0xFE,
        (
            "Well, maybe I should match it to whatever's\x01",
            "on special offer today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6193")

    label("loc_6120")


    ChrTalk(    #314
        0xFE,
        "What should tonight's main dish be, I wonder.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0xFE,
        (
            "I need to decide before tonight's\x01",
            "special offers start.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)

    label("loc_6193")

    TalkEnd(0x15)
    Return()

    # Function_24_5C43 end

    def Function_25_6197(): pass

    label("Function_25_6197")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_626F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_623A")

    ChrTalk(    #316
        0xFE,
        "The market's finally back to its normal feel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0xFE,
        (
            "Seems like today I'll be able to\x01",
            "focus on my appreciation of antiques.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 90, 0)
    SetChrFlags(0xFE, 0x10)
    OP_A2(0xF)
    Jump("loc_626C")

    label("loc_623A")


    ChrTalk(    #318
        0xFE,
        "Hmm... This plate is quite lovely, isn't it?\x02",
    )

    CloseMessageWindow()

    label("loc_626C")

    Jump("loc_664F")

    label("loc_626F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_63C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6335")

    ChrTalk(    #319
        0xFE,
        (
            "With orbments not working, we won't\x01",
            "be able to defend the kingdom...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0xFE,
        "I can't help but feel anxious.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0xFE,
        (
            "Hopefully the Empire keeps to\x01",
            "the non-aggression pact, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)
    Jump("loc_63C2")

    label("loc_6335")


    ChrTalk(    #322
        0xFE,
        (
            "With orbments not working, we won't\x01",
            "be able to defend the kingdom...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0xFE,
        (
            "Hopefully the empire keeps to\x01",
            "the non-aggression pact, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63C2")

    Jump("loc_664F")

    label("loc_63C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_6591")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_648F")

    ChrTalk(    #324
        0xFE,
        (
            "The other day I had the opportunity to observe\x01",
            "some antiques in the mayor's residence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0xFE,
        (
            "I feel like I had the chance to polish my eyes,\x01",
            "having seen such masterpieces up close.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_658E")

    label("loc_648F")


    ChrTalk(    #326
        0xFE,
        (
            "The other day, I ended up visiting the\x01",
            "mayoral residence by chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0xFE,
        (
            "I had the opportunity to observe a number\x01",
            "of their antiques up close.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0xFE,
        (
            "Truly, seeing the real thing up close\x01",
            "is spectacular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0xFE,
        "It was a good chance to polish my eyes.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xF)

    label("loc_658E")

    Jump("loc_664F")

    label("loc_6591")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_664F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_65CD")

    ChrTalk(    #330
        0xFE,
        "Oh, oh, this is quite the good one...\x02",
    )

    CloseMessageWindow()
    Jump("loc_664F")

    label("loc_65CD")


    ChrTalk(    #331
        0xFE,
        "Antiques are my hobby, you see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0xFE,
        (
            "It's a part of my daily routine to go look\x01",
            "for rare finds like I am now.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)
    OP_8C(0x16, 90, 0)
    SetChrFlags(0x16, 0x10)

    label("loc_664F")

    TalkEnd(0x16)
    Return()

    # Function_25_6197 end

    def Function_26_6653(): pass

    label("Function_26_6653")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_6762")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66E8")

    ChrTalk(    #333
        0xFE,
        "Ah, the market's so nice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0xFE,
        "Hearing everyone's voices fills me with energy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0xFE,
        "Heehee, I'm glad I decided to come.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x10)
    Jump("loc_675F")

    label("loc_66E8")


    ChrTalk(    #336
        0xFE,
        (
            "Hearing so many energetic voices\x01",
            "makes me feel energetic too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0xFE,
        "Heehee, now this is what the market should be.\x02",
    )

    CloseMessageWindow()

    label("loc_675F")

    Jump("loc_69E0")

    label("loc_6762")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_67C8")

    ChrTalk(    #338
        0xFE,
        "The smiles are back on everyone's faces.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0xFE,
        "The market really is the symbol of Bose.\x02",
    )

    CloseMessageWindow()
    Jump("loc_69E0")

    label("loc_67C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_69E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_689D")

    ChrTalk(    #340
        0xFE,
        (
            "Coming to the market lets you feel\x01",
            "the lives of everyone who visits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0xFE,
        (
            "I was raised in a mansion all my life,\x01",
            "so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0xFE,
        (
            "Perhaps that's why I find myself\x01",
            "attracted to such a lively world.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_69E0")

    label("loc_689D")


    ChrTalk(    #343
        0xFE,
        (
            "My parents forbade me from ever\x01",
            "coming to the market, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0xFE,
        (
            "I've been coming here to play for\x01",
            "a long time in secret.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0xFE,
        "I really do like the atmosphere of the market.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0xFE,
        (
            "It's very crowded, and it'd be a stretch\x01",
            "to say it's even clean, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0xFE,
        (
            "It's just bursting with the liveliness\x01",
            "of so many people.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x10)

    label("loc_69E0")

    TalkEnd(0x13)
    Return()

    # Function_26_6653 end

    def Function_27_69E4(): pass

    label("Function_27_69E4")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_6BC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B1C")

    ChrTalk(    #348
        0xFE,
        (
            "The lady who runs the confectionery shop's\x01",
            "got her usual cheerful smile back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0xFE,
        (
            "Maybe that fiance of hers who runs\x01",
            "the ice cream stand cheered her up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0xFE,
        (
            "If by some crazy chance he did,\x01",
            "I guess I could acknowledge him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0xFE,
        (
            "I hope he keeps looking after her\x01",
            "from here on out.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)
    Jump("loc_6BBD")

    label("loc_6B1C")


    ChrTalk(    #352
        0xFE,
        (
            "The lady who runs the confectionery shop's\x01",
            "got her usual cheerful smile back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0xFE,
        (
            "Maybe that fiance of hers who runs\x01",
            "the ice cream stand cheered her up...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BBD")

    Jump("loc_7197")

    label("loc_6BC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_6DF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D47")

    ChrTalk(    #354
        0xFE,
        (
            "The lady who runs the confectionery shop\x01",
            "doesn't seem to have her normal energy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0xFE,
        (
            "Well, given the situation we're in\x01",
            "I think that's true of everyone, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0xFE,
        (
            "But still, what's that damn fiance of\x01",
            "hers doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0xFE,
        (
            "It's the job of a spouse to support the\x01",
            "other at a time like this, aint it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0xFE,
        (
            "...Geez, maybe I should go lecture\x01",
            "him while I do my shopping.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)
    Jump("loc_6DEE")

    label("loc_6D47")


    ChrTalk(    #359
        0xFE,
        (
            "That young confectionery lady is so down\x01",
            "and depressed... Why isn't that fiance of\x01",
            "hers doing anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0xFE,
        (
            "I feel like going and giving him\x01",
            "a piece of my mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DEE")

    Jump("loc_7197")

    label("loc_6DF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_6F00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_6E74")

    ChrTalk(    #361
        0xFE,
        "Ah, a healthy smile's best on her.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0xFE,
        (
            "I'm stuffed, but I already feel like\x01",
            "I want to buy another castella.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EFD")

    label("loc_6E74")


    ChrTalk(    #363
        0xFE,
        (
            "The smile of the confectionery shop\x01",
            "owner sure does shine...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0xFE,
        (
            "It really was worth pitching in\x01",
            "to help with the construction.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)

    label("loc_6EFD")

    Jump("loc_7197")

    label("loc_6F00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_7197")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_6FFB")

    ChrTalk(    #365
        0xFE,
        (
            "The fiance of the confectionery shop's owner\x01",
            "runs the ice cream stand over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0xFE,
        (
            "Since they're engaged, you'd figure they\x01",
            "could run both in one shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0xFE,
        (
            "Well, as a fan of the little lady,\x01",
            "I'm glad they're not, but still.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7197")

    label("loc_6FFB")


    ChrTalk(    #368
        0xFE,
        (
            "Ahh, the smile of the confectionery\x01",
            "shop lady really is wonderful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0xFE,
        (
            "But, that lady has someone she's\x01",
            "promised her future to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0xFE,
        (
            "It's the young guy running the ice\x01",
            "cream stand over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0xFE,
        (
            "Apparently he's a real competitive person, so\x01",
            "he started his own shop because he didn't want\x01",
            "to play second fiddle to her in her shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #372
        0xFE,
        (
            "They're engaged, so you'd think they\x01",
            "could run a shop together.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)

    label("loc_7197")

    TalkEnd(0x17)
    Return()

    # Function_27_69E4 end

    def Function_28_719B(): pass

    label("Function_28_719B")

    TalkBegin(0x18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_7392")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72D5")

    ChrTalk(    #373
        0xFE,
        "Apparently the whole market's running a sale.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0xFE,
        (
            "T-To have a sale at a time like this...\x01",
            "That's just too incredible!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0xFE,
        (
            "That's the Bose Market for you, though.\x01",
            "They really do seem like they think about\x01",
            "the customer first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0xFE,
        (
            "I-I'd better work hard or I won't be\x01",
            "able to keep up.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x12)
    Jump("loc_738F")

    label("loc_72D5")


    ChrTalk(    #377
        0xFE,
        (
            "To have a sale like at a time like this...\x01",
            "That's the Bose Market for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #378
        0xFE,
        (
            "Th-This isn't the time for me to be losing\x01",
            "my nerve just because I'm a little late\x01",
            "opening my store.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_738F")

    Jump("loc_77C3")

    label("loc_7392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_74F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7462")

    ChrTalk(    #379
        0xFE,
        (
            "Thanks to the trouble recently,\x01",
            "my stock's not come in...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0xFE,
        (
            "My store's opening has to be\x01",
            "heavily delayed, as a result.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0xFE,
        (
            "Of course, this isn't the time\x01",
            "for excuses like those.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x12)
    Jump("loc_74EE")

    label("loc_7462")


    ChrTalk(    #382
        0xFE,
        (
            "Seems like even the market can't keep\x01",
            "up its normal energy today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #383
        0xFE,
        (
            "Everyone's filled with concern and fear.\x01",
            "I'm sure no different.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74EE")

    Jump("loc_77C3")

    label("loc_74F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_766B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_7577")

    ChrTalk(    #384
        0xFE,
        "Seems like the ancient dragon was driven away.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0xFE,
        (
            "Now I can work on getting ready\x01",
            "to re-open without concern.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7668")

    label("loc_7577")


    ChrTalk(    #386
        0xFE,
        (
            "Seems like the ancient dragon went off\x01",
            "somewhere. Thank Aidios for that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #387
        0xFE,
        (
            "Now I can work on getting ready\x01",
            "to re-open without concern.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #388
        0xFE,
        (
            "I think it'll take a bit longer, but I look\x01",
            "forward to your business when I'm open again!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x12)

    label("loc_7668")

    Jump("loc_77C3")

    label("loc_766B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_77C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_770D")

    ChrTalk(    #389
        0xFE,
        (
            "The market finally processed my request\x01",
            "for a store!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #390
        0xFE,
        (
            "My store should be around here, so when\x01",
            "we open, I look forward to your business!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77C3")

    label("loc_770D")


    ChrTalk(    #391
        0xFE,
        (
            "The market finally processed my request\x01",
            "for a store!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #392
        0xFE,
        "This is the start of my life as a merchant.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #393
        0xFE,
        (
            "I'll put forward a great shop that\x01",
            "won't lose to any of my rivals.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x12)

    label("loc_77C3")

    TalkEnd(0x18)
    Return()

    # Function_28_719B end

    def Function_29_77C7(): pass

    label("Function_29_77C7")

    TalkBegin(0x19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_7849")

    ChrTalk(    #394
        0xFE,
        (
            "*sigh* There's so many people I don't\x01",
            "even know who to ask...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #395
        0xFE,
        (
            "Ahhh, where on earth could that girl\x01",
            "be living?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7849")

    TalkEnd(0x19)
    Return()

    # Function_29_77C7 end

    def Function_30_784D(): pass

    label("Function_30_784D")

    TalkBegin(0x1A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_79C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_78EC")

    ChrTalk(    #396
        0xFE,
        (
            "I'm showing some new customers around\x01",
            "the market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #397
        0xFE,
        (
            "These two are Imperial merchants, as\x01",
            "it happens. They're fairly major clients.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_79C2")

    label("loc_78EC")


    ChrTalk(    #398
        0xFE,
        (
            "I'm showing some new customers around\x01",
            "the market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #399
        0xFE,
        (
            "These two are Imperial merchants, as\x01",
            "it happens. They're fairly major clients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #400
        0xFE,
        (
            "I suspect we'll be dealing with people\x01",
            "from the Empire more, soon.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x13)

    label("loc_79C2")

    Jump("loc_7AE2")

    label("loc_79C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_7AE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_7A61")

    ChrTalk(    #401
        0xFE,
        (
            "Wasn't it clothing goods I was supposed\x01",
            "to check on our inventory of?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #402
        0xFE,
        (
            "I-I have so much work that it all\x01",
            "kind of blends together.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AE2")

    label("loc_7A61")


    ChrTalk(    #403
        0xFE,
        (
            "Let's see, next I need to go check\x01",
            "our inventory of carpets...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #404
        0xFE,
        (
            "Really, Mirano is as much of\x01",
            "a slave driver as ever.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x13)

    label("loc_7AE2")

    TalkEnd(0x1A)
    Return()

    # Function_30_784D end

    def Function_31_7AE6(): pass

    label("Function_31_7AE6")

    TalkBegin(0x1B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_7C56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_7B6B")

    ChrTalk(    #405
        0x1B,
        (
            "I came for a business discussion,\x01",
            "but then this sale started.\x02\x03",

            "Looks like I'll have to wait here for a bit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C56")

    label("loc_7B6B")


    ChrTalk(    #406
        0x1B,
        (
            "I heard the market had re-opened and came\x01",
            "over to talk business immediately, but...\x02\x03",

            "With the worst timing possible I get here\x01",
            "just as they're starting a sale.\x02\x03",

            "Once that starts, nothing I say to\x01",
            "the old lady will get through.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x14)

    label("loc_7C56")

    TalkEnd(0x1B)
    Return()

    # Function_31_7AE6 end

    def Function_32_7C5A(): pass

    label("Function_32_7C5A")

    TalkBegin(0x1C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_7D1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_7CD8")

    ChrTalk(    #407
        0xFE,
        "I'm here to help out with Dad's store today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #408
        0xFE,
        (
            "Heehee! I'm gonna be the best helper\x01",
            "in the world!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D1B")

    label("loc_7CD8")


    ChrTalk(    #409
        0xFE,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #410
        0xFE,
        "I'm here to help out with Dad's store today.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x15)

    label("loc_7D1B")

    TalkEnd(0x1C)
    Return()

    # Function_32_7C5A end

    def Function_33_7D1F(): pass

    label("Function_33_7D1F")

    TalkBegin(0x1D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_7EB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_END)), "loc_7D9A")

    ChrTalk(    #411
        0xFE,
        "I managed to find a contract at the eleventh hour.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #412
        0xFE,
        "Phew! I somehow managed to maintain face.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7EB7")

    label("loc_7D9A")


    ChrTalk(    #413
        0xFE,
        (
            "Just when I'd practically given up,\x01",
            "a certain merchant came to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #414
        0xFE,
        "I managed to find a contract at the eleventh hour.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #415
        0xFE,
        (
            "Still, though, to proceed with business so\x01",
            "vigorously in such unknown conditions...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #416
        0xFE,
        (
            "That merchant, Mirano? She's got\x01",
            "nerves of steel, she does.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x16)

    label("loc_7EB7")

    TalkEnd(0x1D)
    Return()

    # Function_33_7D1F end

    def Function_34_7EBB(): pass

    label("Function_34_7EBB")

    TalkBegin(0x1E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_80BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_END)), "loc_7F79")

    ChrTalk(    #417
        0xFE,
        (
            "My, there's quite the crowd. It's unbelievable\x01",
            "that this is a market of a minor nation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #418
        0xFE,
        (
            "This market should be most capable\x01",
            "of serving as an export destination.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80BF")

    label("loc_7F79")


    ChrTalk(    #419
        0xFE,
        "Hmm, so this is the Bose Market.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #420
        0xFE,
        (
            "My, there's quite the crowd. It's unbelievable\x01",
            "that this is a market of a minor nation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #421
        0xFE,
        (
            "It seems even our Imperial products are\x01",
            "bought and sold quite regularly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #422
        0xFE,
        (
            "Hmm, it appears my understanding was\x01",
            "lacking. This location will be QUITE sufficient\x01",
            "as a site to export to.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x17)

    label("loc_80BF")

    TalkEnd(0x1E)
    Return()

    # Function_34_7EBB end

    def Function_35_80C3(): pass

    label("Function_35_80C3")

    TalkBegin(0x1F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_8257")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_81BA")

    ChrTalk(    #423
        0xFE,
        (
            "I went to the orbal factory to\x01",
            "get the register fixed, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #424
        0xFE,
        (
            "According to the shop owner it\x01",
            "isn't actually broken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #425
        0xFE,
        (
            "He looked pretty tired too. Apparently he's been\x01",
            "bombarded by people with similar problems.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x18)
    Jump("loc_8254")

    label("loc_81BA")


    ChrTalk(    #426
        0xFE,
        (
            "Apparently our cash register isn't\x01",
            "actually broken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #427
        0xFE,
        (
            "Hmm, if it's not working it's basically\x01",
            "the same as if it was broken, if you ask\x01",
            "me, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8254")

    Jump("loc_83AD")

    label("loc_8257")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_83AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_END)), "loc_82C9")

    ChrTalk(    #428
        0xFE,
        (
            "I'll stick around in Bose and\x01",
            "help at the store for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #429
        0xFE,
        "All right, let's do this!\x02",
    )

    CloseMessageWindow()
    Jump("loc_83AD")

    label("loc_82C9")


    ChrTalk(    #430
        0xFE,
        "Hey, welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #431
        0xFE,
        (
            "I decided to stay around in Bose and\x01",
            "help with the store for a while longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #432
        0xFE,
        (
            "After all, I've put a lot of work on\x01",
            "my wife and Pomme's shoulders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #433
        0xFE,
        "I'd like to repay the debt at least a little.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x18)

    label("loc_83AD")

    TalkEnd(0x1F)
    Return()

    # Function_35_80C3 end

    def Function_36_83B1(): pass

    label("Function_36_83B1")

    TalkBegin(0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A71")
    TurnDirection(0x20, 0x101, 400)

    ChrTalk(    #434
        0x20,
        (
            "#613FHello again, Estelle.\x01",
            "And... Oh, my, hello, Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #435
        0x101,
        "#1000FHi, Mayor Maybelle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #436
        0x102,
        "#1040F...It's been a while.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x20, 0x102, 400)

    ChrTalk(    #437
        0x20,
        (
            "#611FHeehee. It certainly has.\x02\x03",

            "You two look busy again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #438
        0x101,
        (
            "#1016FNo kidding. I heard it's been really hard\x01",
            "on you, too, though, Mayor Maybelle.\x02\x03",

            "Old man Lugran was telling us about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #439
        0x102,
        (
            "#1035FI was a little worried when I heard\x01",
            "some citizens broke in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #440
        0x20,
        (
            "#615F*sigh* Yes, I had to spend the better part of\x01",
            "the evening talking them down, and even then\x01",
            "I only barely got them to return home.\x02\x03",

            "#612FI didn't really do anything to actually\x01",
            "assuage their fears, though. I couldn't.\x01",
            "Even I'M half-scared out of my wits.\x02\x03",

            "If this keeps up, I'm afraid there will be\x01",
            "another uprising. A much more violent\x01",
            "one, next time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #441
        0x102,
        (
            "#1043FIt could happen, yes...\x02\x03",

            "So long as the real problem remains\x01",
            "unresolved, people will be on edge\x01",
            "and looking for someone to blame.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #442
        0x101,
        (
            "#1006FRight now, though, we just need to do\x01",
            "what we can.\x02\x03",

            "Staring at the floor and fretting won't\x01",
            "solve anything!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8822")

    ChrTalk(    #443
        0x106,
        (
            "#051FYou got that right.\x02\x03",

            "No matter what comes,\x01",
            "we'll do our duty as bracers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_890F")

    label("loc_8822")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8885")

    ChrTalk(    #444
        0x103,
        (
            "#020FYes, exactly.\x02\x03",

            "No matter what may come,\x01",
            "we will do our duty as bracers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_890F")

    label("loc_8885")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_890F")

    ChrTalk(    #445
        0x108,
        (
            "#070FHm. As you say.\x02\x03",

            "'Do your best, and let heaven decide\x01",
            "the rest'... All we can do is continue\x01",
            "our duty as bracers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_890F")

    TurnDirection(0x20, 0x101, 400)

    ChrTalk(    #446
        0x20,
        (
            "#610FI feel pretty much the\x01",
            "same way about being a mayor.\x02\x03",

            "No matter how dark and hopeless the\x01",
            "situation may seem, a mayor must\x01",
            "remain with her city and protect it.\x02\x03",

            "Of course, I believe you will resolve\x01",
            "things in the end, mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #447
        0x101,
        "#1008FAh...haha... Well, no pressure there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #448
        0x102,
        "#1049FWe'll take those as words of encouragement.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x19)
    OP_A2(0x2090)
    Jump("loc_8C08")

    label("loc_8A71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 1)), scpexpr(EXPR_END)), "loc_8B0E")

    ChrTalk(    #449
        0x20,
        (
            "#610FRight now, all each and every one\x01",
            "of us can do is our best.\x02\x03",

            "I believe that by combining all of our\x01",
            "efforts we can overcome this crisis.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C08")

    label("loc_8B0E")


    ChrTalk(    #450
        0x20,
        (
            "#610FIt seems the market has reclaimed its calm.\x02\x03",

            "Stabilizing the prices seems to have\x01",
            "done the trick.\x02\x03",

            "The younger merchants are adding their\x01",
            "own twist to things as well...\x02\x03",

            "#611FAt this rate, I can probably\x01",
            "relax and just step back and watch.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C08")

    TalkEnd(0x20)
    Return()

    # Function_36_83B1 end

    def Function_37_8C0C(): pass

    label("Function_37_8C0C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x381), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8C19")
    Return()

    label("loc_8C19")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8C2B")
    Return()

    label("loc_8C2B")

    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x10)"), scpexpr(EXPR_END)), "loc_8C66")
    Call(0, 38)
    Jump("loc_8D7E")

    label("loc_8C66")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xC)"), scpexpr(EXPR_END)), "loc_8C75")
    Call(0, 39)
    Jump("loc_8D7E")

    label("loc_8C75")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x9)"), scpexpr(EXPR_END)), "loc_8C84")
    Call(0, 40)
    Jump("loc_8D7E")

    label("loc_8C84")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x8)"), scpexpr(EXPR_END)), "loc_8C93")
    Call(0, 41)
    Jump("loc_8D7E")

    label("loc_8C93")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x3E8)"), scpexpr(EXPR_END)), "loc_8CA2")
    Call(0, 40)
    Jump("loc_8D7E")

    label("loc_8CA2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x3E9)"), scpexpr(EXPR_END)), "loc_8CB1")
    Call(0, 39)
    Jump("loc_8D7E")

    label("loc_8CB1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xFF)"), scpexpr(EXPR_EXEC_OP, "OP_CD(0x4E7)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8D28")
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #451
        "\x07\x05Tried showing them the photograph, but they didn't recognize her.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_8D7E")

    label("loc_8D28")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #452
        "\x07\x05There's no one to show the photograph to nearby.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_8D7E")

    OP_0D()
    ClearMapFlags(0x80)
    Return()

    # Function_37_8C0C end

    def Function_38_8D85(): pass

    label("Function_38_8D85")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_8E09")

    ChrTalk(    #453
        0x10,
        "You all, do your best to find that girl.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #454
        0x10,
        (
            "To be parted by war... Truly a sad\x01",
            "affair that should never happen.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8EE7")

    label("loc_8E09")


    ChrTalk(    #455
        0x10,
        "What, you lookin' for someone?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #456
        0x10,
        "I see. A ten-year-old story...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #457
        0x10,
        "Unfortunately, she doesn't look familiar to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #458
        0x10,
        "But, good luck.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #459
        0x10,
        (
            "To be parted by war... Truly a sad\x01",
            "affair that should never happen.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_8EE7")

    TalkEnd(0x10)
    Return()

    # Function_38_8D85 end

    def Function_39_8EEB(): pass

    label("Function_39_8EEB")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_8F4B")

    ChrTalk(    #460
        0xC,
        "Sorry. She doesn't look familiar at all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #461
        0xC,
        "Try checking with someone else.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9013")

    label("loc_8F4B")


    ChrTalk(    #462
        0xC,
        "Ohh, searching for someone?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #463
        0xC,
        "Hmm, hmm... I see, I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #464
        0xC,
        (
            "Sorry.\x01",
            "She doesn't look familiar at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #465
        0xC,
        (
            "I'm sorry I couldn't be of any help.\x01",
            "You should try checking with someone else.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_9013")

    TalkEnd(0xC)
    Return()

    # Function_39_8EEB end

    def Function_40_9017(): pass

    label("Function_40_9017")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_9072")

    ChrTalk(    #466
        0x9,
        (
            "The girl in that photo...\x01",
            "She looks kinda familiar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #467
        0x9,
        "But who was it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9121")

    label("loc_9072")


    ChrTalk(    #468
        0x9,
        (
            "Huh, the girl in that photo...\x01",
            "I feel like I've seen her somewhere...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #469
        0x9,
        (
            "Buuuut I could just be mistaking her\x01",
            "for someone else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #470
        0x9,
        "Sorry, don't let it bother you.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_9121")

    TalkEnd(0x9)
    Return()

    # Function_40_9017 end

    def Function_41_9125(): pass

    label("Function_41_9125")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_91AA")

    ChrTalk(    #471
        0x8,
        "Those green eyes are lovely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #472
        0x8,
        (
            "If there was a girl like that around here,\x01",
            "I sure wouldn't be leaving her alone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9241")

    label("loc_91AA")


    ChrTalk(    #473
        0x8,
        "Oh, that's a cute kid.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #474
        0x8,
        "Those green eyes are lovely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #475
        0x8,
        (
            "If there was a girl like that around here,\x01",
            "I sure wouldn't be leaving her alone.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_9241")

    TalkEnd(0x8)
    Return()

    # Function_41_9125 end

    SaveToFile()

Try(main)
