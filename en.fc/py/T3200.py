from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3200   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3200.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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
        'Mrs. Mao',                             # 9
        'Dorothy',                              # 10
        'Gary',                                 # 11
        'Percy',                                # 12
        'Ed',                                   # 13
        'Lynn',                                 # 14
        'Recia',                                # 15
        'Cyril',                                # 16
        'Addy',                                 # 17
        'Lucky',                                # 18
        'Sima',                                 # 19
        'Quantay',                              # 20
        'Seagaro',                              # 21
        'Edel',                                 # 22
        'Eastern Man',                          # 23
        'Tratt Plains Road',                    # 24
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
        'ED6_DT07/CH02430 ._CH',             # 00
        'ED6_DT07/CH02070 ._CH',             # 01
        'ED6_DT07/CH01040 ._CH',             # 02
        'ED6_DT07/CH01460 ._CH',             # 03
        'ED6_DT07/CH01270 ._CH',             # 04
        'ED6_DT07/CH01030 ._CH',             # 05
        'ED6_DT07/CH01150 ._CH',             # 06
        'ED6_DT07/CH01120 ._CH',             # 07
        'ED6_DT07/CH01130 ._CH',             # 08
        'ED6_DT07/CH01160 ._CH',             # 09
        'ED6_DT07/CH01020 ._CH',             # 0A
        'ED6_DT07/CH01060 ._CH',             # 0B
        'ED6_DT07/CH01040 ._CH',             # 0C
        'ED6_DT07/CH01210 ._CH',             # 0D
        'ED6_DT07/CH01153 ._CH',             # 0E
        'ED6_DT07/CH00070 ._CH',             # 0F
    )

    AddCharChipPat(
        'ED6_DT07/CH02430P._CP',             # 00
        'ED6_DT07/CH02070P._CP',             # 01
        'ED6_DT07/CH01040P._CP',             # 02
        'ED6_DT07/CH01460P._CP',             # 03
        'ED6_DT07/CH01270P._CP',             # 04
        'ED6_DT07/CH01030P._CP',             # 05
        'ED6_DT07/CH01150P._CP',             # 06
        'ED6_DT07/CH01120P._CP',             # 07
        'ED6_DT07/CH01130P._CP',             # 08
        'ED6_DT07/CH01160P._CP',             # 09
        'ED6_DT07/CH01020P._CP',             # 0A
        'ED6_DT07/CH01060P._CP',             # 0B
        'ED6_DT07/CH01040P._CP',             # 0C
        'ED6_DT07/CH01210P._CP',             # 0D
        'ED6_DT07/CH01153P._CP',             # 0E
        'ED6_DT07/CH00070P._CP',             # 0F
    )

    DeclNpc(
        X                   = 2590,
        Z                   = 250,
        Y                   = 5360,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 13610,
        Z                   = 2500,
        Y                   = 16860,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = -30790,
        Z                   = -2000,
        Y                   = 15330,
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
        X                   = 4000,
        Y                   = 0,
        Z                   = 18870,
        Range               = 7100,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x2D82,
        Unknown_18          = 0x0,
        Unknown_1C          = 19,
    )

    DeclEvent(
        X                   = -13210,
        Y                   = -3000,
        Z                   = 9240,
        Range               = -19510,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x5BAE,
        Unknown_18          = 0x0,
        Unknown_1C          = 21,
    )

    DeclEvent(
        X                   = 28950,
        Y                   = 1000,
        Z                   = 4030,
        Range               = 2500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 27,
    )

    DeclEvent(
        X                   = 980,
        Y                   = -250,
        Z                   = 18420,
        Range               = 1250,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 28,
    )

    DeclEvent(
        X                   = 42330,
        Y                   = 5750,
        Z                   = 36020,
        Range               = 1250,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 29,
    )


    DeclActor(
        TriggerX            = 43290,
        TriggerZ            = 6250,
        TriggerY            = 35890,
        TriggerRange        = 800,
        ActorX              = 43290,
        ActorZ              = 6500,
        ActorY              = 35890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 40000,
        TriggerZ            = 6000,
        TriggerY            = 49730,
        TriggerRange        = 800,
        ActorX              = 40000,
        ActorZ              = 7000,
        ActorY              = 49730,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 22,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 42130,
        TriggerZ            = 0,
        TriggerY            = -860,
        TriggerRange        = 1250,
        ActorX              = 44880,
        ActorZ              = 3000,
        ActorY              = 1020,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 26,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_436",          # 00, 0
        "Function_1_71D",          # 01, 1
        "Function_2_7EB",          # 02, 2
        "Function_3_968",          # 03, 3
        "Function_4_98C",          # 04, 4
        "Function_5_CDA",          # 05, 5
        "Function_6_EC5",          # 06, 6
        "Function_7_101E",         # 07, 7
        "Function_8_1025",         # 08, 8
        "Function_9_102C",         # 09, 9
        "Function_10_14C7",        # 0A, 10
        "Function_11_14CE",        # 0B, 11
        "Function_12_14D5",        # 0C, 12
        "Function_13_199F",        # 0D, 13
        "Function_14_19A6",        # 0E, 14
        "Function_15_1D99",        # 0F, 15
        "Function_16_209A",        # 10, 16
        "Function_17_2107",        # 11, 17
        "Function_18_24EA",        # 12, 18
        "Function_19_2634",        # 13, 19
        "Function_20_2BC0",        # 14, 20
        "Function_21_33B0",        # 15, 21
        "Function_22_37C7",        # 16, 22
        "Function_23_3816",        # 17, 23
        "Function_24_3924",        # 18, 24
        "Function_25_3A0A",        # 19, 25
        "Function_26_3AE2",        # 1A, 26
        "Function_27_3B7B",        # 1B, 27
        "Function_28_3B7F",        # 1C, 28
        "Function_29_3B83",        # 1D, 29
    )


    def Function_0_436(): pass

    label("Function_0_436")

    OP_A2(0x5D2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_447")
    OP_A3(0x3FA)
    Event(0, 20)

    label("loc_447")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_453"),
        (SWITCH_DEFAULT, "loc_469"),
    )


    label("loc_453")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_466")
    OP_A2(0x51C)
    Event(0, 17)

    label("loc_466")

    Jump("loc_469")

    label("loc_469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_473")
    Jump("loc_4BE")

    label("loc_473")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_49A")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -450, 0, 12380, 180)
    OP_43(0xA, 0x0, 0x0, 0x3)
    Jump("loc_4BE")

    label("loc_49A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_4BE")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -450, 0, 12380, 180)
    OP_43(0xA, 0x0, 0x0, 0x3)

    label("loc_4BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_519")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 30590, 4500, 35260, 249)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 28630, 4000, 36530, 176)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 28800, 4000, 33220, 0)
    SetChrFlags(0x13, 0x10)
    Jump("loc_71C")

    label("loc_519")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_565")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 11420, 2000, 14520, 273)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 9750, 2000, 15450, 181)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 9820, 2000, 13580, 351)
    Jump("loc_71C")

    label("loc_565")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_5B6")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 39080, 6000, 47390, 7)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 40560, 6000, 47840, 342)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 39640, 6000, 44670, 353)
    SetChrFlags(0xE, 0x10)
    Jump("loc_71C")

    label("loc_5B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 2)), scpexpr(EXPR_END)), "loc_5C5")
    ClearChrFlags(0x16, 0x80)
    Jump("loc_71C")

    label("loc_5C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_5CF")
    Jump("loc_71C")

    label("loc_5CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_5EF")
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 49070, 2500, -2340, 12)
    Jump("loc_71C")

    label("loc_5EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_625")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 17100, 2500, 20360, 180)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 39080, 6000, 47390, 7)
    Jump("loc_71C")

    label("loc_625")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_671")
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 13770, 2500, 18660, 90)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 17040, 2500, 13580, 0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 15970, 2500, 13580, 45)
    Jump("loc_71C")

    label("loc_671")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_6D3")
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 14240, 2500, 16170, 90)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 14200, 2500, 17020, 90)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 15630, 2500, 13690, 45)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 17390, 2500, 13750, 0)
    Jump("loc_71C")

    label("loc_6D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_71C")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 12180, 2000, 15020, 270)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 9850, 2000, 13940, 45)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 10210, 2000, 16010, 135)

    label("loc_71C")

    Return()

    # Function_0_436 end

    def Function_1_71D(): pass

    label("Function_1_71D")

    OP_16(0x2, 0xFA0, 0xFFFE8130, 0xFFFE5E08, 0x30054)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_747")
    OP_B1("t3200_y")
    Jump("loc_750")

    label("loc_747")

    OP_B1("t3200_n")

    label("loc_750")

    OP_72(0xB, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_765")
    OP_72(0x3, 0x10)
    Jump("loc_769")

    label("loc_765")

    OP_64(0x0, 0x1)

    label("loc_769")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_773")
    Jump("loc_7A7")

    label("loc_773")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_782")
    OP_1B(0x0, 0x0, 0x19)
    Jump("loc_7A7")

    label("loc_782")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_796")
    OP_1B(0x0, 0x0, 0x18)
    Jump("loc_7A7")

    label("loc_796")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A7")
    OP_1B(0x0, 0x0, 0x17)

    label("loc_7A7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x11C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BB")
    OP_28(0x2A, 0x1, 0x800)

    label("loc_7BB")

    OP_64(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x2E, 0x0, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x2E, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7DB")
    OP_65(0x2, 0x1)

    label("loc_7DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7EA")
    OP_82(0x8D, 0x0)

    label("loc_7EA")

    Return()

    # Function_1_71D end

    def Function_2_7EB(): pass

    label("Function_2_7EB")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_810")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_952")

    label("loc_810")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_829")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_952")

    label("loc_829")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_842")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_952")

    label("loc_842")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_85B")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_952")

    label("loc_85B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_874")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_952")

    label("loc_874")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_88D")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_952")

    label("loc_88D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A6")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_952")

    label("loc_8A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8BF")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_952")

    label("loc_8BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D8")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_952")

    label("loc_8D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F1")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_952")

    label("loc_8F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_90A")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_952")

    label("loc_90A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_923")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_952")

    label("loc_923")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93C")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_952")

    label("loc_93C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_952")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_952")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_967")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_952")

    label("loc_967")

    Return()

    # Function_2_7EB end

    def Function_3_968(): pass

    label("Function_3_968")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_98B")
    OP_8D(0xFE, 2630, 16300, -3360, 10300, 3000)
    Jump("Function_3_968")

    label("loc_98B")

    Return()

    # Function_3_968 end

    def Function_4_98C(): pass

    label("Function_4_98C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_999")
    Jump("loc_CD6")

    label("loc_999")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_9A3")
    Jump("loc_CD6")

    label("loc_9A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_9AD")
    Jump("loc_CD6")

    label("loc_9AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_9B7")
    Jump("loc_CD6")

    label("loc_9B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_A1F")

    ChrTalk(    #0
        0xFE,
        (
            "This garden is so mysterious\x01",
            "and beautiful under the moon...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "...Don't you think so?\x02",
    )

    CloseMessageWindow()
    Jump("loc_CD6")

    label("loc_A1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_B38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_AA2")

    ChrTalk(    #2
        0xFE,
        (
            "I'd love to see the other side\x01",
            "of the mountain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "But there aren't any roads to\x01",
            "get there in the village.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B35")

    label("loc_AA2")

    OP_A2(0xB)

    ChrTalk(    #4
        0xFE,
        (
            "They say there's a giant natural\x01",
            "hot spring on the other side of\x01",
            "the mountain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "I'd to love go see, but they said\x01",
            "nobody's allowed to.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B35")

    Jump("loc_CD6")

    label("loc_B38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_B42")
    Jump("loc_CD6")

    label("loc_B42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_CCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_BE0")

    ChrTalk(    #6
        0xFE,
        (
            "Here I was hoping to have a\x01",
            "long relaxing soak, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "Oh well. I guess I'll just do\x01",
            "some shopping and then\x01",
            "have an exotic dinner.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CCC")

    label("loc_BE0")

    OP_A2(0xB)

    ChrTalk(    #8
        0xFE,
        (
            "If my husband wants to spend\x01",
            "his time training, that's his\x01",
            "choice. It sure isn't mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "Here I was hoping to have a\x01",
            "long relaxing soak, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "Oh well. I guess I'll just do\x01",
            "some shopping and then\x01",
            "have an exotic dinner.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CCC")

    Jump("loc_CD6")

    label("loc_CCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_CD6")

    label("loc_CD6")

    TalkEnd(0xFE)
    Return()

    # Function_4_98C end

    def Function_5_CDA(): pass

    label("Function_5_CDA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_CE7")
    Jump("loc_EC1")

    label("loc_CE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_CF1")
    Jump("loc_EC1")

    label("loc_CF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_CFB")
    Jump("loc_EC1")

    label("loc_CFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_D05")
    Jump("loc_EC1")

    label("loc_D05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_D0F")
    Jump("loc_EC1")

    label("loc_D0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_D19")
    Jump("loc_EC1")

    label("loc_D19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_D50")

    ChrTalk(    #11
        0xFE,
        "Hmph...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "Where did Edel get off to?\x02",
    )

    CloseMessageWindow()
    Jump("loc_EC1")

    label("loc_D50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_EBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_DE1")

    ChrTalk(    #13
        0xFE,
        (
            "I heard the pumps are broken,\x01",
            "and we can't use the baths.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "It's a shame, but then again,\x01",
            "it's also the will of Aidios.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB7")

    label("loc_DE1")

    OP_A2(0xA)

    ChrTalk(    #15
        0xFE,
        (
            "Yep...it's luke-warm. Definitely\x01",
            "nothing 'hot' about these springs\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "I heard the pumps are broken,\x01",
            "and we can't use the baths.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "It's a shame, but then again,\x01",
            "it's also the will of Aidios.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EB7")

    Jump("loc_EC1")

    label("loc_EBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_EC1")

    label("loc_EC1")

    TalkEnd(0xFE)
    Return()

    # Function_5_CDA end

    def Function_6_EC5(): pass

    label("Function_6_EC5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_ED2")
    Jump("loc_101A")

    label("loc_ED2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_EDC")
    Jump("loc_101A")

    label("loc_EDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_EE6")
    Jump("loc_101A")

    label("loc_EE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_EF0")
    Jump("loc_101A")

    label("loc_EF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_EFA")
    Jump("loc_101A")

    label("loc_EFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_FFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_F50")

    ChrTalk(    #18
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        "Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "This well would make a\x01",
            "great fishing pond.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FFC")

    label("loc_F50")

    OP_A2(0x1)

    ChrTalk(    #21
        0xFE,
        (
            "Ahh, the hot springs are\x01",
            "so refreshing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "When I breathe in these vapors,\x01",
            "I forget all about fishing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "It's like I'm completely cleansed...\x01",
            "body and soul!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FFC")

    Jump("loc_101A")

    label("loc_FFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_1009")
    Jump("loc_101A")

    label("loc_1009")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1013")
    Jump("loc_101A")

    label("loc_1013")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_101A")

    label("loc_101A")

    TalkEnd(0xFE)
    Return()

    # Function_6_EC5 end

    def Function_7_101E(): pass

    label("Function_7_101E")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_7_101E end

    def Function_8_1025(): pass

    label("Function_8_1025")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_8_1025 end

    def Function_9_102C(): pass

    label("Function_9_102C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_116D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_10B0")

    ChrTalk(    #24
        0xFE,
        "Hello, Quantay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "You were just practicing some\x01",
            "orbal arts, weren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "You should pace yourself.\x02",
    )

    CloseMessageWindow()
    Jump("loc_116A")

    label("loc_10B0")

    OP_A2(0x4)

    ChrTalk(    #27
        0xFE,
        (
            "It's like you're pretending you're\x01",
            "at the Martial Arts Competition...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "...right there in the middle of the\x01",
            "road. Don't you feel embarrassed\x01",
            "at all?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        "You're such a child.\x02",
    )

    CloseMessageWindow()

    label("loc_116A")

    Jump("loc_14C3")

    label("loc_116D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1281")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1209")

    ChrTalk(    #30
        0xFE,
        (
            "Figures the pumps here would\x01",
            "break right when some big\x01",
            "calamity hits Zeiss...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "'Elmo, the town of little rest\x01",
            "and no relaxation.'\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_127E")

    label("loc_1209")

    OP_A2(0x4)

    ChrTalk(    #32
        0xFE,
        "Some news, isn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "That big attack in Zeiss.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "It ought to make the front page\x01",
            "of the Liberl News.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_127E")

    Jump("loc_14C3")

    label("loc_1281")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1371")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_12F5")

    ChrTalk(    #35
        0xFE,
        (
            "Hey, Lucky! No going past\x01",
            "the fences!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "Mrs. Mao'll have my hide if you\x01",
            "do, you know that!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_136E")

    label("loc_12F5")

    OP_A2(0x4)

    ChrTalk(    #37
        0xFE,
        (
            "Why does everybody care so much\x01",
            "about the other side of the mountain?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "You guys act like such\x01",
            "little kids...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_136E")

    Jump("loc_14C3")

    label("loc_1371")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_137B")
    Jump("loc_14C3")

    label("loc_137B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_1385")
    Jump("loc_14C3")

    label("loc_1385")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_138F")
    Jump("loc_14C3")

    label("loc_138F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_1399")
    Jump("loc_14C3")

    label("loc_1399")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_13A3")
    Jump("loc_14C3")

    label("loc_13A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_14C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1415")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #39
        0xFE,
        "People from Zeiss are so cool.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "They're so...I don't know...\x01",
            "so...sophisticated.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14C3")

    label("loc_1415")

    OP_A2(0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_143E")

    ChrTalk(    #41
        0xFE,
        "Ooh, look at him!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1473")

    label("loc_143E")

    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #42
        0xFE,
        (
            "That boy over there is one\x01",
            "major hottie.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1473")


    ChrTalk(    #43
        0xFE,
        (
            "Hey! You guys are from Zeiss,\x01",
            "right? Right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        "What's popular there now?\x02",
    )

    CloseMessageWindow()

    label("loc_14C3")

    TalkEnd(0xFE)
    Return()

    # Function_9_102C end

    def Function_10_14C7(): pass

    label("Function_10_14C7")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_10_14C7 end

    def Function_11_14CE(): pass

    label("Function_11_14CE")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_11_14CE end

    def Function_12_14D5(): pass

    label("Function_12_14D5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_156F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_151B")

    ChrTalk(    #45
        0xFE,
        "Taste my ORBAL ARTS!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        "BOOM-SHAKKA-LAKKA!\x02",
    )

    CloseMessageWindow()
    Jump("loc_156C")

    label("loc_151B")

    OP_A2(0x7)

    ChrTalk(    #47
        0xFE,
        "See, Recia?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0xE, 400)

    ChrTalk(    #48
        0xFE,
        (
            "I'll really do it this time,\x01",
            "so watch me!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 180, 0)

    label("loc_156C")

    Jump("loc_199B")

    label("loc_156F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_160E")

    ChrTalk(    #49
        0xFE,
        (
            "Hey, did you hear? Some big\x01",
            "crazy thing happened in Zeiss!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "I heard some bracers came here\x01",
            "to investigate it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        "I wanna meet a bracer...\x02",
    )

    CloseMessageWindow()
    Jump("loc_199B")

    label("loc_160E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1719")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1674")

    ChrTalk(    #52
        0xFE,
        (
            "Man, I wanna go to the other\x01",
            "side of the mountain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "I'm BORED playing here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1716")

    label("loc_1674")

    OP_A2(0x7)

    ChrTalk(    #54
        0xFE,
        (
            "The hot spring there has got\x01",
            "to be GIGANTIC.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "It's been giving us hot water for\x01",
            "years, and it still hasn't dried up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        "I wish I could see it once.\x02",
    )

    CloseMessageWindow()

    label("loc_1716")

    Jump("loc_199B")

    label("loc_1719")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1723")
    Jump("loc_199B")

    label("loc_1723")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_172D")
    Jump("loc_199B")

    label("loc_172D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_182D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_17A9")

    ChrTalk(    #57
        0xFE,
        (
            "Man, I wanna go to the other\x01",
            "side of the mountain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "There's no place left to explore\x01",
            "around here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_182A")

    label("loc_17A9")

    OP_A2(0x7)

    ChrTalk(    #59
        0xFE,
        (
            "I heard there's a big spring over\x01",
            "on the other side of the mountain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "I wanna go see, but they said\x01",
            "I'm not allowed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_182A")

    Jump("loc_199B")

    label("loc_182D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1898")

    ChrTalk(    #61
        0xFE,
        (
            "I thought the hot water was\x01",
            "starting to get weaker...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "...but it's all stopped now.\x02",
    )

    CloseMessageWindow()
    Jump("loc_199B")

    label("loc_1898")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_199B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1932")

    ChrTalk(    #63
        0xFE,
        (
            "You guys are pretty young to\x01",
            "be visiting the hot springs. It's\x01",
            "like an old people hangout.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "You must be real tired\x01",
            "or sumthin'.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_199B")

    label("loc_1932")

    OP_A2(0x7)

    ChrTalk(    #65
        0xFE,
        "Hey, it's new people!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "Wow, they're young. Or maybe\x01",
            "they just LOOK young but are\x01",
            "REALLY old!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_199B")

    TalkEnd(0xFE)
    Return()

    # Function_12_14D5 end

    def Function_13_199F(): pass

    label("Function_13_199F")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_13_199F end

    def Function_14_19A6(): pass

    label("Function_14_19A6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1A72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_1A02")

    ChrTalk(    #67
        0xFE,
        (
            "You can't defeat me! My orbal\x01",
            "arts are TOO STRONG!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        "AAH-CHOOO!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A6F")

    label("loc_1A02")

    OP_A2(0x9)

    ChrTalk(    #69
        0xFE,
        (
            "Heh heh, the best part of the\x01",
            "birthday celebration stuff has gotta \x01",
            "be the Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A6F")

    Jump("loc_1D95")

    label("loc_1A72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1B40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_1ADD")

    ChrTalk(    #70
        0xFE,
        "That was some incident...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "But it doesn't have anything\x01",
            "to do with this village.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B3D")

    label("loc_1ADD")

    OP_A2(0x9)

    ChrTalk(    #72
        0xFE,
        (
            "You hear about that big incident\x01",
            "that happened in Zeiss?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        "Cities sure can be scary.\x02",
    )

    CloseMessageWindow()

    label("loc_1B3D")

    Jump("loc_1D95")

    label("loc_1B40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1C6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_1BB1")

    ChrTalk(    #74
        0xFE,
        "Wow, Recia sure looks bored.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "She ought to be helping out at\x01",
            "the inn, not watching us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C6A")

    label("loc_1BB1")

    OP_A2(0x9)

    ChrTalk(    #76
        0xFE,
        (
            "You know the spring on the\x01",
            "other side of the mountain?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "I've heard all about it, but I've\x01",
            "never seen it for real.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "I'd go right now if it weren't for\x01",
            "this stupid fence.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C6A")

    Jump("loc_1D95")

    label("loc_1C6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1C77")
    Jump("loc_1D95")

    label("loc_1C77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_1C81")
    Jump("loc_1D95")

    label("loc_1C81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_1C8B")
    Jump("loc_1D95")

    label("loc_1C8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1CD9")

    ChrTalk(    #79
        0xFE,
        (
            "This place sure seems lonely\x01",
            "without all the steam clouds.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D95")

    label("loc_1CD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1D95")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_1D57")

    ChrTalk(    #80
        0xFE,
        "Lucky's such a little kid.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "Doesn't he know that the best\x01",
            "place for a couple to go is a\x01",
            "hot spring?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D95")

    label("loc_1D57")

    OP_A2(0x9)

    ChrTalk(    #82
        0xFE,
        (
            "Heh. Nice. A little date vacation\x01",
            "to the hot springs?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D95")

    TalkEnd(0xFE)
    Return()

    # Function_14_19A6 end

    def Function_15_1D99(): pass

    label("Function_15_1D99")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1EE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1E24")

    ChrTalk(    #83
        0xFE,
        (
            "Oh, I'd love to see some authentic\x01",
            "Eastern culture!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "I should see if I can get a transfer\x01",
            "to the Wolf Base...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EDE")

    label("loc_1E24")

    OP_A2(0x0)

    ChrTalk(    #85
        0xFE,
        (
            "Wow, that was some crazy business\x01",
            "they had over in Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "I was thinking of traveling out to\x01",
            "the Republic...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "...but after that terrorist attack\x01",
            "I don't feel very safe.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EDE")

    Jump("loc_2096")

    label("loc_1EE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2096")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1FEF")

    ChrTalk(    #88
        0xFE,
        (
            "Speaking of which, I was on\x01",
            "the road here, right...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "And I was lost, right? And then,\x01",
            "this monster chased me all over\x01",
            "the place!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "I thought he was going to kill me,\x01",
            "but all he ended up doing was...\x01",
            "glowing at me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        "Talk about surprised.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2096")

    label("loc_1FEF")

    OP_A2(0x0)

    ChrTalk(    #92
        0xFE,
        "Wow, this is great!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "These buildings...oh, I could spend\x01",
            "FOREVER just looking around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        "So this is Eastern-style, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        "Goddess, I love this stuff!\x02",
    )

    CloseMessageWindow()

    label("loc_2096")

    TalkEnd(0xFE)
    Return()

    # Function_15_1D99 end

    def Function_16_209A(): pass

    label("Function_16_209A")

    TalkBegin(0xFE)

    ChrTalk(    #96
        0xFE,
        (
            "#070FOh, this one is nice.\x02\x03",

            "I believe I'll go soak in the bath\x01",
            "and wash the road dust right off.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_209A end

    def Function_17_2107(): pass

    label("Function_17_2107")

    EventBegin(0x0)
    OP_6D(17070, 6660, 16820, 0)
    OP_67(0, 3960, -10000, 0)
    OP_6B(4370, 0)
    OP_6C(39000, 0)
    SetChrPos(0x101, -17420, -2000, 15200, 90)
    SetChrPos(0x102, -18340, -2000, 16000, 90)
    SetChrPos(0x107, -18340, -2000, 14400, 90)
    FadeToBright(1000, 0)

    def lambda_217F():
        OP_6C(90000, 8500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_217F)
    Sleep(4000)

    def lambda_2194():
        OP_6D(-16149, -2000, 14900, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2194)

    def lambda_21AC():
        OP_67(0, 9500, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_21AC)

    def lambda_21C4():
        OP_6B(2800, 4000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_21C4)
    Sleep(4500)

    ChrTalk(    #97
        0x101,
        (
            "#501F#5PWow... So this is Elmo, huh?\x01",
            "I like it. Feels homey.\x02\x03",

            "#505FErr...what's that smell?\x01",
            "Joshua...did you...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x107,
        (
            "#560FOh, that's just the sulfur\x01",
            "in the water.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x102,
        (
            "#010FI guess that's just what happens\x01",
            "when the water pours out of\x01",
            "the hot springs, huh?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x107, 400)
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(    #100
        0x101,
        (
            "#004F#5PUgh...really? Smells like someone\x01",
            "left eggs out in the sun for a year.\x02\x03",

            "#006FWell, if I hold my breath,\x01",
            "it's not too bad, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x107,
        (
            "#067FHee hee...\x02\x03",

            "#064FIt's not as strong as usual,\x01",
            "though...\x02\x03",

            "There's hardly any steam\x01",
            "coming out...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x102,
        (
            "#010FMaybe it's tied to the pump\x01",
            "breaking down.\x02\x03",

            "Want to go ahead and see\x01",
            "about fixing it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x102, 400)

    ChrTalk(    #103
        0x107,
        (
            "#060FOh, the key to the pump\x01",
            "shed is back at the inn.\x01",
            "Mrs. Mao has it.\x02\x03",

            "We'll have to get that,\x01",
            "first...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#006F#5PNo problem.\x01",
            "To the inn we go.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x40, 0x1, 0x2)
    EventEnd(0x0)
    Return()

    # Function_17_2107 end

    def Function_18_24EA(): pass

    label("Function_18_24EA")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #105
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2630")
    EventBegin(0x0)
    OP_A2(0x51E)
    OP_28(0x40, 0x1, 0x8)

    ChrTalk(    #106
        0x101,
        "#501FSo this is the pump shed?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x107,
        (
            "#060FThat's right.\x02\x03",

            "It sends hot water to the\x01",
            "inn and to the well in the\x01",
            "town square.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x102,
        "#010FWell, let's try that key.\x02",
    )

    CloseMessageWindow()
    OP_22(0x73, 0x0, 0x64)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #109
        "\x07\x05Used Pump Shed Key.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_71(0x3, 0x10)
    OP_64(0x0, 0x1)
    EventEnd(0x1)
    Jump("loc_2633")

    label("loc_2630")

    TalkEnd(0xFF)

    label("loc_2633")

    Return()

    # Function_18_24EA end

    def Function_19_2634(): pass

    label("Function_19_2634")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2BBF")
    OP_A2(0x523)
    OP_28(0x40, 0x1, 0x200)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_8C(0x101, 90, 400)
    OP_8C(0x102, 90, 400)
    OP_8C(0x110, 90, 400)

    ChrTalk(    #110
        0x101,
        (
            "#501FOh...\x02\x03",

            "Look, there's steam coming out!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x110,
        "#153FHey, you're right!\x02",
    )

    CloseMessageWindow()

    def lambda_26B9():
        OP_6D(15680, 2830, 16620, 2600)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_26B9)

    def lambda_26D1():
        OP_6C(56000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_26D1)
    Sleep(2500)
    SetChrPos(0x101, 8210, 2000, 16740, 90)
    SetChrPos(0x102, 7680, 2000, 15580, 90)
    SetChrPos(0x110, 6840, 2000, 16430, 90)

    def lambda_2719():
        OP_8E(0xFE, 0x3520, 0x9C4, 0x424A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2719)
    Sleep(300)

    def lambda_2739():
        OP_8E(0xFE, 0x3250, 0x9C4, 0x3E62, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2739)
    Sleep(300)

    def lambda_2759():
        OP_8F(0xFE, 0x30F2, 0x8CA, 0x44DE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x110, 1, lambda_2759)
    WaitChrThread(0x110, 0x1)

    ChrTalk(    #112
        0x102,
        "#010FLooks like the repairs worked.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x110,
        (
            "#151F*whistle* Now, we can finally\x01",
            "use the spa! Yay!\x02\x03",

            "Life is good again...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x110, 400)

    ChrTalk(    #114
        0x101,
        (
            "#506F#2PKinda overstating things\x01",
            "a bit, aren't you?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x110, 400)

    ChrTalk(    #115
        0x102,
        (
            "#010F#2PDo you really like the\x01",
            "spa that much?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x110, 0x102, 400)

    ChrTalk(    #116
        0x110,
        (
            "#150FHeh heh... Well, yeah.\x02\x03",

            "There's absolutely nothing\x01",
            "finer than a tall glass of\x01",
            "fruity milk after a hot bath.\x02\x03",

            "#151FNow, I'm going to go ahead\x01",
            "and get in.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2917():
        OP_6D(16100, 2000, 12100, 3600)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2917)

    def lambda_292F():
        OP_6C(135000, 3600)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_292F)

    def lambda_293F():

        label("loc_293F")

        TurnDirection(0xFE, 0x110, 0)
        OP_48()
        Jump("loc_293F")

    QueueWorkItem2(0x101, 3, lambda_293F)

    def lambda_2950():

        label("loc_2950")

        TurnDirection(0xFE, 0x110, 0)
        OP_48()
        Jump("loc_2950")

    QueueWorkItem2(0x102, 3, lambda_2950)
    OP_8E(0x110, 0x2ABC, 0x7D0, 0x3DD6, 0xBB8, 0x0)
    OP_8E(0x110, 0x2C10, 0x7D0, 0x300C, 0xBB8, 0x0)
    OP_8E(0x110, 0x427C, 0x7D0, 0x2A26, 0xBB8, 0x0)
    OP_62(0x110, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #117
        0x110,
        "#153F#6POh, I just remembered...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x110, 0x101, 400)

    ChrTalk(    #118
        0x110,
        (
            "#151F#6PGuys...?\x02\x03",

            "Thanks for coming to help me earlier!\x01",
            "I have all my hands, and toes, and\x01",
            "bits because of you two!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2A5A():
        OP_6D(14030, 2500, 16360, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A5A)

    def lambda_2A72():
        OP_6C(90000, 2500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2A72)
    OP_8C(0x110, 90, 400)
    OP_8E(0x110, 0x5A50, 0x7D0, 0xFFA, 0xBB8, 0x0)
    SetChrFlags(0x110, 0x80)
    SetChrPos(0x110, 13600, 2500, 16970, 0)
    OP_44(0x101, 0x3)
    OP_44(0x102, 0x3)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #119
        0x101,
        (
            "#007F#3PY-You don't have to thank us\x01",
            "for having good timing...\x02\x03",

            "#008FMan, she can be such a ditz.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #120
        0x102,
        (
            "#019F#4PWell, that's Dorothy for you.\x02\x03",

            "#010FAnyway, let's get back to\x01",
            "the pump shed.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #121
        0x101,
        (
            "#006F#3POkay.\x02\x03",

            "Tita's probably still there.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    RemoveParty(0xF, 0xFF)

    label("loc_2BBF")

    Return()

    # Function_19_2634 end

    def Function_20_2BC0(): pass

    label("Function_20_2BC0")

    EventBegin(0x0)
    OP_6D(26330, 2000, 4950, 0)
    OP_6C(44000, 0)
    SetChrPos(0x101, 23790, 2000, 4370, 90)
    SetChrPos(0x102, 23900, 2000, 3160, 90)
    SetChrPos(0x107, 25060, 2000, 3830, 90)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 27590, 2000, 3840, 270)
    OP_3F(0x369, 1)
    FadeToBright(1500, 0)
    OP_0D()

    ChrTalk(    #122
        0x101,
        "#006FOkay, Mrs. Mao...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x102,
        "#010FWe really appreciate everything.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x8,
        (
            "#681FHa ha. I'm just glad you were\x01",
            "able to relax a little.\x02\x03",

            "And, Tita. You certainly seem\x01",
            "to have enjoyed yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x107,
        (
            "#067FHee hee...\x01",
            "Is it that obvious?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x8,
        (
            "#680FYou all seem closer than \x01",
            "you were yesterday. Must\x01",
            "be the magic of the springs!\x02\x03",

            "#683FBy the way... What happened to\x01",
            "that girl with the glasses?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        (
            "#505FHmmm...\x01",
            "I think she's still in bed.\x02\x03",

            "We called for her, but she\x01",
            "didn't answer, and we didn't\x01",
            "want to barge in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x102,
        (
            "#010FWhen Dorothy does wake up,\x01",
            "please give her our regards.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x8,
        (
            "#680FCertainly.\x02\x03",

            "Tita, I'd like for you to tell\x01",
            "Russell something for me, when\x01",
            "you see him next.\x02\x03",

            "Tell him that I said he needs to\x01",
            "focus on the rest of his life,\x01",
            "beyond all the 24/7 research.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x107,
        (
            "#060FHa ha... Okay, I will.\x02\x03",

            "#061FTake care of yourself, Mrs. Mao.\x01",
            "And you need to come visit, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x8,
        (
            "#681FSure thing, hon.\x02\x03",

            "#680FYou're all welcome back\x01",
            "here any time.\x02\x03",

            "The baths are always waiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        "#508FYou can count on it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x102,
        (
            "#019FAbsolutely.\x01",
            "The food was great, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)
    OP_8E(0x8, 0x73B4, 0x9C4, 0x1022, 0x7D0, 0x0)
    OP_70(0x4, 0x1D)
    OP_73(0x4)
    SetChrFlags(0x8, 0x4)
    OP_8E(0x8, 0x7C88, 0x9C4, 0xFBE, 0x7D0, 0x0)
    OP_72(0x4, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x4, 29)
    OP_70(0x4, 0x0)
    OP_73(0x4)
    OP_71(0x4, 0x800)

    def lambda_30BA():
        OP_6D(24380, 2000, 3780, 1500)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_30BA)
    OP_8C(0x107, 270, 400)
    WaitChrThread(0x107, 0x1)

    ChrTalk(    #134
        0x101,
        "#001FAhhh... I feel rejuvenated.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x102,
        (
            "#019FAnd we never would have come\x01",
            "at all, if the pump hadn't\x01",
            "needed repairing.\x02\x03",

            "So I guess we owe our\x01",
            "thanks to you, Tita.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x107,
        (
            "#067FBut...I... I didn't do anything...\x02\x03",

            "#066FI should be thanking you\x01",
            "for everything yesterday.\x02\x03",

            "It was...really fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x101,
        (
            "#008FHeh heh...\x01",
            "Glad to hear it.\x02\x03",

            "#001FI guess that means we're even!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x107,
        "#061FYep, I guess it does!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #139
        0x102,
        (
            "#010FShall we return to Zeiss,\x01",
            "then?\x02\x03",

            "The professor might be done\x01",
            "with taking apart the Black\x01",
            "Orbment by now.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #140
        0x101,
        (
            "#004FOh, yeah... We do still\x01",
            "have that to deal with.\x02\x03",

            "#506FI'd completely forgotten.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x102,
        (
            "#018F*sigh*\x01",
            "Why am I not surprised?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x107,
        "#067FHa ha...\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_44(0x101, 0xFF)
    ClearMapFlags(0x10000000)
    EventEnd(0x0)
    Return()

    # Function_20_2BC0 end

    def Function_21_33B0(): pass

    label("Function_21_33B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37C6")
    OP_A2(0x529)
    EventBegin(0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 5790, 1000, 14450, 0)

    ChrTalk(    #143
        0x9,
        "Waaaaiit!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)

    def lambda_33F6():
        OP_6C(45000, 0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_33F6)
    SetChrFlags(0xA, 0x80)
    OP_6D(-11320, -2000, 15580, 0)
    SetChrPos(0x9, -2260, 0, 14820, 270)
    SetChrPos(0x101, -11140, -2000, 15290, 90)
    SetChrPos(0x102, -12050, -2000, 16190, 90)
    SetChrPos(0x107, -12260, -2000, 14680, 90)
    OP_0D()

    def lambda_3461():
        OP_8E(0xFE, 0xFFFFD99A, 0xFFFFF830, 0x3C50, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3461)
    WaitChrThread(0x9, 0x1)

    ChrTalk(    #144
        0x101,
        (
            "#501FHi, Dorothy. Finally decided to\x01",
            "rejoin the world of the living?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x9,
        (
            "#152F*huff huff*\x01",
            "No fair, you guys!\x02\x03",

            "How come I got left behind?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x101,
        "#004FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x102,
        (
            "#014FDidn't you say that you were\x01",
            "sticking around to get some\x01",
            "more shots for a story?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x9,
        (
            "#153FOh...\x01",
            "Did I?\x02\x03",

            "#151FWhatever!\x01",
            "I just hate being left out.\x02\x03",

            "Don't you, Lil' T?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x107,
        (
            "#065FUhh...\x01",
            "Are you talking to me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x101,
        "#509FWhere'd THAT come from?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x9,
        (
            "#154FI just wanted to give you\x01",
            "a nickname.\x02\x03",

            "You don't like it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x107,
        "#067FN-No...it's all right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x9,
        "#151FAwesome! Thanks, Lil' T!♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x101,
        (
            "#007F*sigh* You really are lost\x01",
            "in your own little world...\x02\x03",

            "#006FOh, well. You can come back\x01",
            "with us to Zeiss, if you want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x9,
        "#150FHee hee, now you're talking!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x102,
        (
            "#010FOkay, then. Want to give\x01",
            "this whole 'leaving' thing\x01",
            "another shot?\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x9, 0x40)

    def lambda_37A3():
        OP_92(0xFE, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_37A3)
    EventEnd(0x0)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearMapFlags(0x10000000)
    AddParty(0xF, 0xFF)

    label("loc_37C6")

    Return()

    # Function_21_33B0 end

    def Function_22_37C7(): pass

    label("Function_22_37C7")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #157
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_22_37C7 end

    def Function_23_3816(): pass

    label("Function_23_3816")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_386F")

    ChrTalk(    #158
        0x107,
        (
            "#060F(This is the way out of town.\x01",
            "I need to go to the pump shed.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3908")

    label("loc_386F")

    TurnDirection(0x107, 0x0, 400)

    ChrTalk(    #159
        0x107,
        (
            "#060FU-Umm... This way leads out\x01",
            "onto the fields.\x02\x03",

            "The pump shed is on the\x01",
            "other side of the village.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_38E7():
        TurnDirection(0x102, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_38E7)
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(    #160
        0x101,
        "#000FGot it.\x02",
    )

    CloseMessageWindow()

    label("loc_3908")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_23_3816 end

    def Function_24_3924(): pass

    label("Function_24_3924")

    EventBegin(0x2)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #161
        0x102,
        (
            "#010FWe need to wait at the inn,\x01",
            "until the repairs are done.\x02\x03",

            "I don't think we can really\x01",
            "do anything to help.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #162
        0x101,
        (
            "#000FYeah... I guess taking it easy\x01",
            "for a little bit can't hurt.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_24_3924 end

    def Function_25_3A0A(): pass

    label("Function_25_3A0A")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A62")

    ChrTalk(    #163
        0x102,
        (
            "#010FIt's almost dusk... It's too \x01",
            "risky to go out on the plains.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AC6")

    label("loc_3A62")

    TurnDirection(0x102, 0x0, 400)

    ChrTalk(    #164
        0x102,
        (
            "#014FIt's almost dusk... It's too \x01",
            "risky to go out on the plains.\x02\x03",

            "We should turn back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AC6")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_25_3A0A end

    def Function_26_3AE2(): pass

    label("Function_26_3AE2")

    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #165
        "\x07\x00Found a package wrapped in oiled-paper.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #166
        "\x07\x00Inside was \x07\x02The Erbe Woodpecker\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x343, 1)
    OP_64(0x2, 0x1)
    OP_28(0x2E, 0x1, 0x10)
    TalkEnd(0xFF)
    Return()

    # Function_26_3AE2 end

    def Function_27_3B7B(): pass

    label("Function_27_3B7B")

    SetPlaceName(0x88)
    Return()

    # Function_27_3B7B end

    def Function_28_3B7F(): pass

    label("Function_28_3B7F")

    SetPlaceName(0x87)
    Return()

    # Function_28_3B7F end

    def Function_29_3B83(): pass

    label("Function_29_3B83")

    SetPlaceName(0x89)
    Return()

    # Function_29_3B83 end

    SaveToFile()

Try(main)
