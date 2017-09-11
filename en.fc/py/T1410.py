from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1410   ._SN',
        MapName             = 'Bose',
        Location            = 'T1410.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60016",
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
        'Nolan',                                # 9
        'Amelia',                               # 10
        'Marco',                                # 11
        'Blond-Haired Man',                     # 12
        'Sentry',                               # 13
        'Royal Army Soldier',                   # 14
        'Royal Army Soldier',                   # 15
        'General Morgan',                       # 16
        'Mayor Maybelle',                       # 17
        'Sting',                                # 18
        'Royal Army Soldier',                   # 19
        'Royal Army Soldier',                   # 20
        'Royal Army Officer',                   # 21
        'Nigel',                                # 22
        'Dish',                                 # 23
        'Wine',                                 # 24
        'Coffee',                               # 25
        'Coffee',                               # 26
        'Coffee',                               # 27
        'Coffee',                               # 28
        'Royal Army Soldier',                   # 29
        'Provost Guardsman',                    # 30
        'Provost Guardsman',                    # 31
        'Target Camera',                        # 32
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
        'ED6_DT07/CH01150 ._CH',             # 01
        'ED6_DT07/CH01100 ._CH',             # 02
        'ED6_DT07/CH00030 ._CH',             # 03
        'ED6_DT07/CH01300 ._CH',             # 04
        'ED6_DT07/CH02080 ._CH',             # 05
        'ED6_DT07/CH02360 ._CH',             # 06
        'ED6_DT07/CH01620 ._CH',             # 07
        'ED6_DT07/CH01310 ._CH',             # 08
        'ED6_DT07/CH01120 ._CH',             # 09
        'ED6_DT07/CH00033 ._CH',             # 0A
        'ED6_DT06/CH20020 ._CH',             # 0B
        'ED6_DT06/CH20021 ._CH',             # 0C
        'ED6_DT07/CH01640 ._CH',             # 0D
        'ED6_DT07/CH01650 ._CH',             # 0E
        'ED6_DT07/CH00003 ._CH',             # 0F
        'ED6_DT07/CH00013 ._CH',             # 10
        'ED6_DT07/CH00023 ._CH',             # 11
        'ED6_DT06/CH20045 ._CH',             # 12
        'ED6_DT07/CH02083 ._CH',             # 13
    )

    AddCharChipPat(
        'ED6_DT07/CH01270P._CP',             # 00
        'ED6_DT07/CH01150P._CP',             # 01
        'ED6_DT07/CH01100P._CP',             # 02
        'ED6_DT07/CH00030P._CP',             # 03
        'ED6_DT07/CH01300P._CP',             # 04
        'ED6_DT07/CH02080P._CP',             # 05
        'ED6_DT07/CH02360P._CP',             # 06
        'ED6_DT07/CH01620P._CP',             # 07
        'ED6_DT07/CH01310P._CP',             # 08
        'ED6_DT07/CH01120P._CP',             # 09
        'ED6_DT07/CH00033P._CP',             # 0A
        'ED6_DT06/CH20020P._CP',             # 0B
        'ED6_DT06/CH20021P._CP',             # 0C
        'ED6_DT07/CH01640P._CP',             # 0D
        'ED6_DT07/CH01650P._CP',             # 0E
        'ED6_DT07/CH00003P._CP',             # 0F
        'ED6_DT07/CH00013P._CP',             # 10
        'ED6_DT07/CH00023P._CP',             # 11
        'ED6_DT06/CH20045P._CP',             # 12
        'ED6_DT07/CH02083P._CP',             # 13
    )

    DeclNpc(
        X                   = 18100,
        Z                   = 0,
        Y                   = 16400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 15350,
        Z                   = 0,
        Y                   = 15480,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 13100,
        Z                   = -100,
        Y                   = 17110,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1D4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 18850,
        Z                   = 200,
        Y                   = 14150,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 131075,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 19944,
        Z                   = 0,
        Y                   = 8440,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 203044,
        Z                   = 0,
        Y                   = 9046,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 203044,
        Z                   = 0,
        Y                   = 9046,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 209550,
        Z                   = 200,
        Y                   = 11820,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x154,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -60835,
        Z                   = 0,
        Y                   = 38681,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 18300,
        Z                   = 0,
        Y                   = 14300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 201700,
        Z                   = 0,
        Y                   = 109600,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 104300,
        Z                   = 0,
        Y                   = 107600,
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
        X                   = 204600,
        Z                   = 0,
        Y                   = 15300,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 110330,
        Z                   = 0,
        Y                   = -74950,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 18500,
        Z                   = 750,
        Y                   = 15400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 524299,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 19100,
        Z                   = 700,
        Y                   = 15300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327692,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 14950,
        Z                   = 700,
        Y                   = 12390,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1572875,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 15000,
        Z                   = 700,
        Y                   = 11770,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1572875,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 13190,
        Z                   = 700,
        Y                   = 12340,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1572875,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 13240,
        Z                   = 700,
        Y                   = 11670,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1572875,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 103480,
        Z                   = 0,
        Y                   = -74820,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 110330,
        Z                   = 0,
        Y                   = -77770,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 106850,
        Z                   = 0,
        Y                   = -77680,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
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


    DeclActor(
        TriggerX            = 118930,
        TriggerZ            = 0,
        TriggerY            = 14070,
        TriggerRange        = 800,
        ActorX              = 118930,
        ActorZ              = 800,
        ActorY              = 14070,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 123890,
        TriggerZ            = 0,
        TriggerY            = 11990,
        TriggerRange        = 800,
        ActorX              = 123890,
        ActorZ              = 800,
        ActorY              = 11990,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 32,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 17690,
        TriggerZ            = 0,
        TriggerY            = 14350,
        TriggerRange        = 800,
        ActorX              = 18100,
        ActorZ              = 1500,
        ActorY              = 16400,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_4B6",          # 00, 0
        "Function_1_603",          # 01, 1
        "Function_2_62F",          # 02, 2
        "Function_3_645",          # 03, 3
        "Function_4_662",          # 04, 4
        "Function_5_6D7",          # 05, 5
        "Function_6_6DC",          # 06, 6
        "Function_7_10DA",         # 07, 7
        "Function_8_18D2",         # 08, 8
        "Function_9_1C0C",         # 09, 9
        "Function_10_2EE1",        # 0A, 10
        "Function_11_3536",        # 0B, 11
        "Function_12_3825",        # 0C, 12
        "Function_13_3AA7",        # 0D, 13
        "Function_14_4175",        # 0E, 14
        "Function_15_421B",        # 0F, 15
        "Function_16_44F0",        # 10, 16
        "Function_17_4924",        # 11, 17
        "Function_18_4CE7",        # 12, 18
        "Function_19_4FBF",        # 13, 19
        "Function_20_5ACD",        # 14, 20
        "Function_21_724B",        # 15, 21
        "Function_22_72A9",        # 16, 22
        "Function_23_730C",        # 17, 23
        "Function_24_736F",        # 18, 24
        "Function_25_73BF",        # 19, 25
        "Function_26_7400",        # 1A, 26
        "Function_27_83A4",        # 1B, 27
        "Function_28_B832",        # 1C, 28
        "Function_29_B87B",        # 1D, 29
        "Function_30_B8BF",        # 1E, 30
        "Function_31_B8F4",        # 1F, 31
        "Function_32_B93D",        # 20, 32
    )


    def Function_0_4B6(): pass

    label("Function_0_4B6")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (102, "loc_4C2"),
        (SWITCH_DEFAULT, "loc_4CF"),
    )


    label("loc_4C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 6)), scpexpr(EXPR_END)), "loc_4CC")
    OP_A2(0x9)

    label("loc_4CC")

    Jump("loc_4CF")

    label("loc_4CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_503")
    SetChrPos(0x9, 16900, 0, 14300, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jump("loc_59C")

    label("loc_503")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_51E")
    SetChrPos(0x9, 16900, 0, 14300, 0)
    Jump("loc_59C")

    label("loc_51E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_539")
    SetChrPos(0x9, 16900, 0, 14300, 0)
    Jump("loc_59C")

    label("loc_539")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_559")
    SetChrPos(0x9, 21600, 0, 11200, 180)
    ClearChrFlags(0x11, 0x80)
    Jump("loc_59C")

    label("loc_559")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 7)), scpexpr(EXPR_END)), "loc_563")
    Jump("loc_59C")

    label("loc_563")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 3)), scpexpr(EXPR_END)), "loc_572")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_59C")

    label("loc_572")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_581")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_59C")

    label("loc_581")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_590")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_59C")

    label("loc_590")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 4)), scpexpr(EXPR_END)), "loc_59C")
    ClearChrFlags(0xA, 0x80)

    label("loc_59C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DD")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x16, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_5D8")
    SetChrChipByIndex(0xB, 10)
    SetChrPos(0xB, 18850, 200, 14150, 225)
    SetChrSubChip(0xB, 2)
    Jump("loc_5DD")

    label("loc_5D8")

    SetChrChipByIndex(0xB, 10)

    label("loc_5DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_5EB")
    OP_A3(0x3FA)
    Event(0, 26)

    label("loc_5EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_602")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FB)
    Event(0, 27)

    label("loc_602")

    Return()

    # Function_0_4B6 end

    def Function_1_603(): pass

    label("Function_1_603")

    OP_72(0x3, 0x10)
    OP_72(0x4, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 2)), scpexpr(EXPR_END)), "loc_617")
    Jump("loc_623")

    label("loc_617")

    OP_6F(0x2, 0)
    OP_72(0x2, 0x10)

    label("loc_623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_62E")
    OP_64(0x0, 0x1)

    label("loc_62E")

    Return()

    # Function_1_603 end

    def Function_2_62F(): pass

    label("Function_2_62F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_644")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_62F")

    label("loc_644")

    Return()

    # Function_2_62F end

    def Function_3_645(): pass

    label("Function_3_645")

    OP_A3(0xA)

    label("loc_648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_661")
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Jump("loc_648")

    label("loc_661")

    Return()

    # Function_3_645 end

    def Function_4_662(): pass

    label("Function_4_662")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6D6")
    OP_8E(0xFE, 0x4AE2, 0x0, 0x326E, 0x5DC, 0x0)
    OP_8E(0xFE, 0x57D0, 0x0, 0x2C88, 0x5DC, 0x0)
    OP_8C(0xFE, 180, 500)
    Sleep(1000)
    OP_8E(0xFE, 0x57D0, 0x0, 0x2C88, 0x5DC, 0x0)
    OP_8E(0xFE, 0x425E, 0x0, 0x3804, 0x5DC, 0x0)
    OP_8C(0xFE, 0, 500)
    Sleep(1000)
    Jump("Function_4_662")

    label("loc_6D6")

    Return()

    # Function_4_662 end

    def Function_5_6D7(): pass

    label("Function_5_6D7")

    Call(0, 6)
    Return()

    # Function_5_6D7 end

    def Function_6_6DC(): pass

    label("Function_6_6DC")

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
            "Rest\x01",       # 2
            "Leave\x01",      # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74A")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x18)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_74A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_763")
    OP_0D()
    OP_A9(0x17)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_763")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_77D")
    FadeToBright(300, 0)
    TalkEnd(0x8)
    Return()

    label("loc_77D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_821")

    ChrTalk(    #0
        0x8,
        (
            "It seems like those sky bandit criminals\x01",
            "have finally been caught.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "Now I'm sure those soldiers\x01",
            "in the border garrison can\x01",
            "finally take a break.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10D6")

    label("loc_821")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_9AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_924")
    OP_A2(0x0)

    ChrTalk(    #2
        0x8,
        (
            "Those in the military sure have\x01",
            "a tough life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "Though the captured airliner has been\x01",
            "found, nobody has a clue where the\x01",
            "criminals responsible are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "It seems that General Morgan\x01",
            "has been leading the investigation\x01",
            "on no sleep.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A9")

    label("loc_924")


    ChrTalk(    #5
        0x8,
        (
            "Those in the military sure have\x01",
            "a tough life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "It seems that General Morgan\x01",
            "has been leading the investigation\x01",
            "on no sleep.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A9")

    Jump("loc_10D6")

    label("loc_9AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_B18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A82")
    OP_A2(0x0)

    ChrTalk(    #7
        0x8,
        (
            "I thought we only had one guy in\x01",
            "the clink for that petty eat and\x01",
            "run crime...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "Now we've got the guys who attacked\x01",
            "the airliner in custody, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "What's that?\x01",
            "We don't have them?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B15")

    label("loc_A82")


    ChrTalk(    #10
        0x8,
        (
            "Those sky bandits are more slippery\x01",
            "than a greased Pom to catch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "Not to mention they've got wings.\x01",
            "And that only adds to the difficulty.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B15")

    Jump("loc_10D6")

    label("loc_B18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_CC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C1C")
    OP_A2(0x0)

    ChrTalk(    #12
        0x8,
        (
            "The border garrison seems to be\x01",
            "really busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "But moving this many troops and\x01",
            "still being unable to find an airliner\x01",
            "looks pretty bad for the military.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "Well, it looks like our men in uniform\x01",
            "have their work cut out for them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CBD")

    label("loc_C1C")


    ChrTalk(    #15
        0x8,
        (
            "The border garrison seems to be\x01",
            "really busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "But moving this many troops and\x01",
            "still being unable to find an airliner\x01",
            "looks pretty bad for the military.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CBD")

    Jump("loc_10D6")

    label("loc_CC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_E15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D7B")
    OP_A2(0x0)

    ChrTalk(    #17
        0x8,
        "Ha ha ha.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "So the general has finally let\x01",
            "his thunder fall here at the\x01",
            "Haken Gate, has he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "No doubt his troops screwed up\x01",
            "something real bad this time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E12")

    label("loc_D7B")


    ChrTalk(    #20
        0x8,
        (
            "So the general has finally let\x01",
            "his thunder fall here at the\x01",
            "Haken Gate, has he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "No doubt his troops screwed up\x01",
            "something real bad this time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E12")

    Jump("loc_10D6")

    label("loc_E15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_F8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F02")
    OP_A2(0x0)

    ChrTalk(    #22
        0x8,
        (
            "The Royal Army has blocked off\x01",
            "the Eisen Road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "And now all those from the Empire\x01",
            "wishing to leave the country are\x01",
            "stuck here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "That man over there with the blond hair\x01",
            "seems to be in the same situation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F8A")

    label("loc_F02")


    ChrTalk(    #25
        0x8,
        (
            "The Royal Army has blocked off\x01",
            "the Eisen Road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "And now all those from the Empire\x01",
            "wishing to leave the country are\x01",
            "stuck here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F8A")

    Jump("loc_10D6")

    label("loc_F8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 4)), scpexpr(EXPR_END)), "loc_10D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1064")
    OP_A2(0x0)

    ChrTalk(    #27
        0x8,
        (
            "Good day and welcome to our humble\x01",
            "establishment on the outskirts of\x01",
            "Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "Since this is a bar, we've got\x01",
            "wine to drink and food to eat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "Just don't expect anything too\x01",
            "elaborate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10D6")

    label("loc_1064")


    ChrTalk(    #30
        0x8,
        (
            "Since this is a bar, we've got\x01",
            "wine to drink and food to eat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        (
            "Just don't expect anything too\x01",
            "elaborate.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10D6")

    TalkEnd(0x8)
    Return()

    # Function_6_6DC end

    def Function_7_10DA(): pass

    label("Function_7_10DA")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1196")

    ChrTalk(    #32
        0xFE,
        (
            "The other day some soldiers arrested\x01",
            "a man who cried the whole way to his\x01",
            "cell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "From what I heard, he seems\x01",
            "to have been involved in some\x01",
            "sort of fraudulent scheme.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18CE")

    label("loc_1196")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_1331")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12A9")
    OP_A2(0x1)

    ChrTalk(    #34
        0xFE,
        (
            "Recently the army has been going in\x01",
            "and out of here even after dark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "And thanks to the noise,\x01",
            "I can hardly sleep... *yawn*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "If my skin gets wrinkly from lack of sleep,\x01",
            "I'm gonna give the soldiers who come in\x01",
            "for a drink a piece of my mind.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_132E")

    label("loc_12A9")


    ChrTalk(    #37
        0xFE,
        (
            "Recently the army has been going in\x01",
            "and out of here even after dark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "And thanks to the noise,\x01",
            "I can hardly sleep... *yawn*\x02",
        )
    )

    CloseMessageWindow()

    label("loc_132E")

    Jump("loc_18CE")

    label("loc_1331")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_1483")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1429")
    OP_A2(0x1)

    ChrTalk(    #39
        0xFE,
        (
            "The colonel, who's rumored to\x01",
            "be an elite strategist, came\x01",
            "here for a meal the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "He was a perfect gentleman,\x01",
            "unlike the rugged soldiers\x01",
            "who work here at the fort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "I think I may have just fallen\x01",
            "for him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1480")

    label("loc_1429")


    ChrTalk(    #42
        0xFE,
        (
            "It's unbelievable to think that\x01",
            "there is a such a paragon of\x01",
            "a man in this world.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1480")

    Jump("loc_18CE")

    label("loc_1483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_1620")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1596")
    OP_A2(0x1)

    ChrTalk(    #43
        0xFE,
        (
            "I happened to hear this from\x01",
            "the soldiers earlier...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "And they said that hunk of a colonel\x01",
            "is coming to visit the fort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "I just don't know what I'm going\x01",
            "to do if he speaks to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "I'd better find something nice\x01",
            "to wear before he comes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_161D")

    label("loc_1596")


    ChrTalk(    #47
        0xFE,
        (
            "And they said that hunk of a colonel\x01",
            "is coming to visit the fort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "I just don't know what I'm going\x01",
            "to do if he speaks to me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_161D")

    Jump("loc_18CE")

    label("loc_1620")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_177E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16F8")
    OP_A2(0x1)

    ChrTalk(    #49
        0xFE,
        (
            "The general's voice is as loud\x01",
            "as ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "In fact, we could hear it all the\x01",
            "way here inside the bar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "Whenever the general yells,\x01",
            "all the young recruits come\x01",
            "running in here in fear.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_177B")

    label("loc_16F8")


    ChrTalk(    #52
        0xFE,
        (
            "The general's voice is as loud\x01",
            "as ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "Whenever the general yells,\x01",
            "all the young recruits come\x01",
            "running in here in fear.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_177B")

    Jump("loc_18CE")

    label("loc_177E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_1839")

    ChrTalk(    #54
        0xFE,
        (
            "All the customers here are off-duty\x01",
            "soldiers and travelers waiting to\x01",
            "enter or leave the country.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "Most of these customers have\x01",
            "been here so long I know them\x01",
            "by sight.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18CE")

    label("loc_1839")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 4)), scpexpr(EXPR_END)), "loc_18CE")

    ChrTalk(    #56
        0xFE,
        (
            "That blond-haired man over there is\x01",
            "rather handsome and well dressed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "But after talking to him,\x01",
            "I found him to be a little...odd.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18CE")

    TalkEnd(0x9)
    Return()

    # Function_7_10DA end

    def Function_8_18D2(): pass

    label("Function_8_18D2")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_194E")

    ChrTalk(    #58
        0xFE,
        "The road has finally been reopened.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "And now that I've got my entry permit,\x01",
            "I can finally go to Bose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C08")

    label("loc_194E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_1BB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x72, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B03")
    OP_A2(0x393)

    ChrTalk(    #60
        0xFE,
        (
            "With the airliners stopped,\x01",
            "I had to travel here on foot...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "Now how long do they expect\x01",
            "to keep a merchant from the\x01",
            "Empire such as myself waiting?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "I've even finished reading the book\x01",
            "I brought to pass the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "Holding on to it is just going to\x01",
            "add to my load, so I'll gladly give\x01",
            "it to you, free of charge. Here!\x02",
        )
    )

    CloseMessageWindow()
    OP_3E(0x214, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #64
        "\x07\x00Received \x07\x02Carnelia - Chapter 3\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jump("loc_1BAF")

    label("loc_1B03")


    ChrTalk(    #65
        0xFE,
        (
            "How long do they expect to keep\x01",
            "a merchant from the empire\x01",
            "such as myself waiting?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "This is exactly the type of tactless action\x01",
            "I'd expect from a small country...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BAF")

    Jump("loc_1C08")

    label("loc_1BB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 4)), scpexpr(EXPR_END)), "loc_1C08")

    ChrTalk(    #67
        0xFE,
        (
            "I'm a merchant from the Erebonian\x01",
            "Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        "And I'm on my way to Bose.\x02",
    )

    CloseMessageWindow()

    label("loc_1C08")

    TalkEnd(0xA)
    Return()

    # Function_8_18D2 end

    def Function_9_1C0C(): pass

    label("Function_9_1C0C")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_1D04")
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1C38")
    SetChrSubChip(0xB, 1)
    Jump("loc_1C53")

    label("loc_1C38")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xFA), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C4E")
    SetChrSubChip(0xB, 2)
    Jump("loc_1C53")

    label("loc_1C4E")

    SetChrSubChip(0xB, 0)

    label("loc_1C53")

    OP_8C(0xB, 225, 0)
    SetChrFlags(0xB, 0x10)

    ChrTalk(    #69
        0xB,
        (
            "#030FSo have you changed your mind\x01",
            "about taking me with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        "#009FIn your dreams.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xB,
        (
            "#034FSuch a cold-hearted creature\x01",
            "for being one so young...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 2)
    Jump("loc_2EDD")

    label("loc_1D04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2AC5")
    EventBegin(0x0)
    OP_A2(0x310)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 17370, 0, 13720, 90)
    SetChrPos(0x102, 17820, 0, 12390, 45)
    SetChrPos(0x103, 19280, 0, 12690, 0)
    SetChrPos(0xB, 18850, 200, 14150, 225)
    SetChrSubChip(0xB, 0)
    OP_69(0xB, 0x0)
    OP_67(0, 6740, -10000, 0)
    OP_6B(1210, 0)
    OP_6C(45000, 0)
    OP_6E(660, 0)
    OP_0D()

    ChrTalk(    #72
        0xB,
        (
            "#030FGood day to you all, my fine\x01",
            "friends.\x02\x03",

            "You appear to be citizens of\x01",
            "Liberl, but may I ask you if\x01",
            "you're traveling to the Empire?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#000FNope, we're just here on an\x01",
            "errand.\x02\x03",

            "We're not traveling to the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x102,
        (
            "#010FYou appear to be a citizen\x01",
            "of Erebonia yourself.\x02\x03",

            "What about you? Are you here\x01",
            "to visit the Liberl Kingdom?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xB,
        (
            "#035FHa, I'm glad you asked. I am\x01",
            "indeed a visitor in Liberl, both\x01",
            "for work and for...pleasure...\x02\x03",

            "#035FAnd you... You say you're running\x01",
            "an errand, but I can see your true\x01",
            "colors. I know exactly who you are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        "#505FWh-Who we are?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xB,
        (
            "#030FIndeed!\x01",
            "You're bracers, no?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #78
        0x101,
        (
            "#004FH-How'd you know...? We removed\x01",
            "our bracer emblems!\x02\x03",

            "Wait...are you trying to tell us that\x01",
            "you're in the same profession?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xB,
        (
            "#035FIt's true that there are guild\x01",
            "branches in the Empire, but\x01",
            "actually I'm not a bracer.\x02\x03",

            "#030FI just know several people\x01",
            "in the guild, that's all.\x02\x03",

            "And there's...an air about you that\x01",
            "reminded me of them, so I just\x01",
            "thought I'd ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x102,
        (
            "#015FThose are some excellent deductive reasoning\x01",
            "skills you've got. I don't think an amateur\x01",
            "could've picked us out of a crowd like that.\x02\x03",

            "#012FAre you sure you're a traveler?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xB,
        (
            "#035FHa ha ha. Please don't look at me\x01",
            "with such suspicious eyes.\x02\x03",

            "Those cold flickering eyes of amber...\x01",
            "just like a glass of exquisite brandy.\x02\x03",

            "#037FYou just make me want to kiss you\x01",
            "and hold you in my arms.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_94(0x1, 0x102, 0xB4, 0x258, 0xBB8, 0x0)

    ChrTalk(    #82
        0x102,
        "#018FWha...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x103,
        "#023FYou're a bold one, aren't you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        (
            "#005FW-Wait a minute, you! Are you one of\x01",
            "those men who likes...other boys?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xB,
        (
            "#031FI just can't help myself when I see\x01",
            "something beautiful standing before my\x01",
            "eyes.\x02\x03",

            "Daughters of serenity. Sons of elegance.\x02\x03",

            "Supernal melodies and cleansing landscapes.\x01",
            "Masterpieces and stories to move the soul.\x02\x03",

            "And last but not least, the most exquisite\x01",
            "in food and drink.\x02\x03",

            "For things such as these are those which\x01",
            "pique my interest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x101,
        (
            "#509F...\x01",
            "So you're a pervert, just like I thought!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x103,
        "#027FYep. Definitely a pervert.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xB,
        (
            "#034FHow dreadful it is that genius\x01",
            "is misunderstood in every\x01",
            "generation.\x02\x03",

            "I feel as if my delicate glass\x01",
            "heart is about to be broken.\x02\x03",

            "#030FYou, with your magnificent\x01",
            "black hair...please comfort\x01",
            "me in my time of need.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x102,
        (
            "#017FI'm going to have to pass. You've\x01",
            "already scarred me for life as it\x01",
            "is.\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0x8, 255)

    ChrTalk(    #90
        0x8,
        (
            "(I've heard strange conversations in my\x01",
            "day, but this one is worth remembering.\x01",
            "The look on that kid's face! Ha!)\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xC, 20020, 0, 8730, 0)
    OP_22(0x6, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #91
        0xC,
        "#1PHey! You three!\x02",
    )

    CloseMessageWindow()
    OP_4A(0xC, 255)
    ClearChrFlags(0xC, 0x80)
    OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_27D0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_27D0)
    OP_8E(0xC, 0x4DD0, 0x0, 0x2562, 0x7D0, 0x0)
    OP_4B(0x8, 255)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1200)

    def lambda_2835():
        OP_6D(20620, 0, 12620, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2835)

    def lambda_284D():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_284D)

    def lambda_285B():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_285B)

    def lambda_2869():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2869)
    SetChrSubChip(0xB, 1)
    OP_8E(0xC, 0x5014, 0x0, 0x2B5C, 0xBB8, 0x0)
    OP_8C(0xC, 270, 400)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #92
        0x103,
        "#020F#6POh, it's the soldier from earlier.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xC,
        "#2PThe general has just returned.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xC,
        (
            "#2PI just spoke to him about the matter\x01",
            "and he said he'll meet you now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        "#501F#5PR-Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xC,
        (
            "#2PYeah, so come to the barracks\x01",
            "with me immediately.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xC, 180, 400)
    OP_8E(0xC, 0x4E2A, 0x0, 0x2832, 0xBB8, 0x0)

    def lambda_29AD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_29AD)
    OP_8E(0xC, 0x4E2A, 0x0, 0x21F2, 0x7D0, 0x0)
    WaitChrThread(0xC, 0x1)
    SetChrFlags(0xC, 0x80)
    OP_6D(18830, 0, 13990, 1200)
    TurnDirection(0x102, 0x103, 400)

    ChrTalk(    #97
        0x102,
        (
            "#010F#1PWow, that was much quicker\x01",
            "than I thought.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 400)

    ChrTalk(    #98
        0x103,
        (
            "#020F#4PYeah, now at least maybe we'll be\x01",
            "able to find out what's going on.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0)
    Sleep(400)

    ChrTalk(    #99
        0xB,
        (
            "#035FOkay, then let's be off,\x01",
            "shall we?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T1400   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2EDD")

    label("loc_2AC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E19")
    EventBegin(0x0)
    OP_A2(0x30F)

    ChrTalk(    #100
        0xB,
        (
            "#035FWhat a surprise...\x02\x03",

            "#035FThis is my first time eating\x01",
            "Liberl's cooking, but it was\x01",
            "rather delectable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x8,
        "I'm glad you liked it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x8,
        (
            "If you head to town, there's a number\x01",
            "of other places where you can eat\x01",
            "great Liberl cooking as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x8,
        "You enjoy this trip of yours, all right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xB,
        (
            "#030FThat I will do, believe me.\x02\x03",

            "#030FIf this is the kind of food I can get in a\x01",
            "border dive like this, then I truly am in\x01",
            "for a feast elsewhere in this land...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x8,
        (
            "Well, excuse me for having my bar here on\x01",
            "the outskirts of the country!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x8,
        (
            "Before you go feasting on the finer things, how\x01",
            "about a glass of wine? I know it's not high-end\x01",
            "exactly, but the the taste is worth the price.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xB,
        "#035FHmm. Well then, maybe I will.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        "#000F(Do you think this guy is...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x102,
        (
            "#010F(He looks like a traveler from\x01",
            "the Empire, if you ask me.)\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_2EDD")

    label("loc_2E19")


    ChrTalk(    #110
        0xB,
        (
            "#030FMm, this wine is quite good...\x02\x03",

            "#030FIf this is called cheap wine, then\x01",
            "Liberl must be a wonderful country\x01",
            "of tastes.\x02\x03",

            "#030FI think this only adds to Queen\x01",
            "Alicia's prestige as a ruler.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EDD")

    TalkEnd(0xB)
    Return()

    # Function_9_1C0C end

    def Function_10_2EE1(): pass

    label("Function_10_2EE1")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3259")
    OP_A2(0x35F)
    OP_A2(0x3)

    ChrTalk(    #111
        0x101,
        "#006F(Huh, who's this guy...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x102,
        (
            "#010F(Umm, he looks like a bracer if\x01",
            "you ask me.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        "#000FUm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x101,
        "#002FHello? Is anybody there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x103,
        (
            "#020FAs unfriendly as ever, aren't you,\x01",
            "Sting?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #118
        0xFE,
        (
            "Weren't you...that bracer in training\x01",
            "from some time ago?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x103,
        (
            "#020FYou got it.\x02\x03",

            "And thanks to you I can call\x01",
            "myself a senior bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "Hmm...I almost didn't recognize you.\x01",
            "Do you have some work here at the\x01",
            "Bose branch?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x103,
        "#020FAt the moment, yeah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "Right now we are dealing with a\x01",
            "number of incidents, so we're a\x01",
            "little shorthanded...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "Any help you could give us would\x01",
            "be useful.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 0)

    ChrTalk(    #124
        0x101,
        (
            "#002F(So he was one of Schera's acquaintances,\x01",
            "huh? He does seem like a bit of a scary\x01",
            "guy if you ask me.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x102,
        (
            "#010F(That may be so, but with the way he\x01",
            "carries himself...he looks pretty\x01",
            "capable as a bracer.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3532")

    label("loc_3259")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3481")
    OP_A2(0x3)

    ChrTalk(    #126
        0x103,
        "#020FSting, is that you?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(    #127
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        "Oh, Scherazard...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x103,
        (
            "#020FI've heard that everyone in the Bose\x01",
            "branch is swamped with work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        "Yeah, that's right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "I'm just on my way back from\x01",
            "escorting a traveler from the\x01",
            "Empire...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "Except I'm going to be going\x01",
            "straight to my next job without\x01",
            "dropping by the guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x103,
        (
            "#020FThings must be really busy then.\x02\x03",

            "Well, after we take care of some\x01",
            "of these jobs, how about we sit\x01",
            "down for a drink?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "I refuse.\x01",
            "I don't drink.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x103,
        "#020FReally? Since when?\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 0)
    Jump("loc_3532")

    label("loc_3481")

    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(    #137
        0xFE,
        (
            "I'm just on my way back from\x01",
            "escorting a traveler from the\x01",
            "Empire...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "Except I'm going to be going\x01",
            "straight to my next job without\x01",
            "dropping by the guild.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 0)

    label("loc_3532")

    TalkEnd(0x11)
    Return()

    # Function_10_2EE1 end

    def Function_11_3536(): pass

    label("Function_11_3536")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_36B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3634")
    OP_A2(0x4)

    ChrTalk(    #139
        0xFE,
        (
            "With the sky bandits captured,\x01",
            "I can finally get back to my\x01",
            "regular work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "Wait a minute, what am I thinking?\x01",
            "This is the border with the\x01",
            "Erebonian Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "I can't think about relaxing my\x01",
            "guard in a place like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36B5")

    label("loc_3634")


    ChrTalk(    #142
        0xFE,
        (
            "I finally returned to my regular duties,\x01",
            "but somehow I can't settle down knowing\x01",
            "we're right on the border with the Empire.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36B5")

    Jump("loc_3821")

    label("loc_36B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_3743")

    ChrTalk(    #143
        0xFE,
        (
            "Tomorrow morning we'll be\x01",
            "using patrol ships to search\x01",
            "the mountainous regions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "I'd better get some sleep while\x01",
            "I can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3821")

    label("loc_3743")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_37A0")

    ChrTalk(    #145
        0xFE,
        "Man, am I beat...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "Right now, I'd rather sleep than\x01",
            "eat or take a shower.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3821")

    label("loc_37A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_3821")

    ChrTalk(    #147
        0xFE,
        (
            "I was supposed to be off duty\x01",
            "today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "But then we received an order\x01",
            "to maintain ready status here\x01",
            "in the fort.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3821")

    TalkEnd(0x13)
    Return()

    # Function_11_3536 end

    def Function_12_3825(): pass

    label("Function_12_3825")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_390E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38F3")
    OP_A2(0x5)

    ChrTalk(    #149
        0xFE,
        (
            "Even if these sky bandits are\x01",
            "caught, it doesn't mean that\x01",
            "we're going to get a day to rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "I'm just dragging my feet\x01",
            "from all this lack of sleep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        "Man, am I tired...\x02",
    )

    CloseMessageWindow()
    Jump("loc_390B")

    label("loc_38F3")


    ChrTalk(    #152
        0xFE,
        "Man, am I tired...\x02",
    )

    CloseMessageWindow()

    label("loc_390B")

    Jump("loc_3AA3")

    label("loc_390E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_39A3")

    ChrTalk(    #153
        0xFE,
        (
            "Even though soldiers who were\x01",
            "supposed to be off duty tomorrow\x01",
            "were called up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "This is probably going to be a\x01",
            "full scale search.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AA3")

    label("loc_39A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_3A25")

    ChrTalk(    #155
        0xFE,
        (
            "After a good night's sleep I feel\x01",
            "refreshed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        (
            "I'd better hurry and grab a bite\x01",
            "to eat while I still have time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AA3")

    label("loc_3A25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_3AA3")

    ChrTalk(    #157
        0xFE,
        "*yaaaawn...*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "I was involved in the search for\x01",
            "the missing airliner until late\x01",
            "last night, so I'm dead tired.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AA3")

    TalkEnd(0x12)
    Return()

    # Function_12_3825 end

    def Function_13_3AA7(): pass

    label("Function_13_3AA7")

    TalkBegin(0xF)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3ACC")
    SetChrSubChip(0xFE, 2)
    Jump("loc_3AFD")

    label("loc_3ACC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3AE2")
    SetChrSubChip(0xFE, 1)
    Jump("loc_3AFD")

    label("loc_3AE2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3AF8")
    SetChrSubChip(0xFE, 0)
    Jump("loc_3AFD")

    label("loc_3AF8")

    SetChrSubChip(0xFE, 2)

    label("loc_3AFD")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_3C0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BC9")
    OP_A2(0x6)

    ChrTalk(    #159
        0xF,
        (
            "#160FOh, it's Cassius' kids again...\x02\x03",

            "Why are you here? We have\x01",
            "nothing further to talk about.\x02\x03",

            "I'm busy dealing with paperwork and\x01",
            "other reports after the incident.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C0C")

    label("loc_3BC9")


    ChrTalk(    #160
        0xF,
        (
            "#160FWhy are you here? We have\x01",
            "nothing further to talk about.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C0C")

    Jump("loc_416C")

    label("loc_3C0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_3F46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3C91")

    ChrTalk(    #161
        0xF,
        (
            "#163FSo I couldn't have done this without\x01",
            "the cooperation from the Intelligence\x01",
            "Division this time, huh...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F43")

    label("loc_3C91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 1)), scpexpr(EXPR_END)), "loc_3DCE")
    OP_A2(0x6)

    ChrTalk(    #162
        0xF,
        (
            "#163FIf I mobilize any more of my men from the\x01",
            "garrison here, I'm going to be shorthanded\x01",
            "on watching the Empire side.\x02\x03",

            "It would be ill advised for us to act\x01",
            "without considering all possibilities...\x02\x03",

            "I guess there's no alternative but\x01",
            "to seek the cooperation of the\x01",
            "Intelligence Division this time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F43")

    label("loc_3DCE")

    OP_A2(0x361)

    ChrTalk(    #163
        0xF,
        (
            "#160FWhat do you want?\x02\x03",

            "Are you still loitering around here?\x02\x03",

            "I'm only going to tell you this once.\x01",
            "This incident is under the jurisdiction\x01",
            "of the army.\x02\x03",

            "Interfere again and you won't find\x01",
            "any clemency here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x101,
        (
            "#002F(The general's looking rather\x01",
            "pale in the face. He must be\x01",
            "really tired.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x102,
        (
            "#012F(I guess they've been giving\x01",
            "their all in the search as well.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F43")

    Jump("loc_416C")

    label("loc_3F46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_416C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40D0")
    OP_A2(0x361)
    OP_A2(0x6)

    ChrTalk(    #166
        0xF,
        (
            "#160FWhat do you want?\x02\x03",

            "Are you still loitering around here?\x02\x03",

            "I'm only going to tell you this once.\x01",
            "This incident is under the jurisdiction\x01",
            "of the army.\x02\x03",

            "Interfere again and you won't find\x01",
            "any clemency here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x101,
        (
            "#002F(The general's looking rather\x01",
            "pale in the face. He must be\x01",
            "really tired.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x102,
        (
            "#012F(I guess they've been giving\x01",
            "their all in the search as well.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_416C")

    label("loc_40D0")


    ChrTalk(    #169
        0xF,
        (
            "#160FI'm only going to tell you this once.\x01",
            "This incident is under the jurisdiction\x01",
            "of the army.\x02\x03",

            "Interfere again and you won't find\x01",
            "any clemency here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_416C")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xF)
    Return()

    # Function_13_3AA7 end

    def Function_14_4175(): pass

    label("Function_14_4175")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_4217")

    ChrTalk(    #170
        0xFE,
        (
            "The sky bandits were transported to\x01",
            "Leiston Fortress in the Zeiss region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "I'm sure they're going to be\x01",
            "interrogated about a number\x01",
            "of things.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4217")

    TalkEnd(0x14)
    Return()

    # Function_14_4175 end

    def Function_15_421B(): pass

    label("Function_15_421B")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x14, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_43D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4358")
    OP_A2(0x8)

    ChrTalk(    #172
        0xFE,
        (
            "Th-The devil made me do it! I swear it\x01",
            "was like a sudden impulse... Yeah,\x01",
            "that's right, a sudden impulse!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "I-I won't do anything bad again.\x01",
            "I'm begging you, please forgive me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "I-I'm faint-hearted and frail to\x01",
            "begin with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        (
            "I-If you put me in prison,\x01",
            "I'll get sick and die.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43D4")

    label("loc_4358")


    ChrTalk(    #176
        0xFE,
        (
            "I-I'm faint-hearted and frail to\x01",
            "begin with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        (
            "I-I won't do anything bad again.\x01",
            "I'm begging you, please forgive me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43D4")

    Jump("loc_44EC")

    label("loc_43D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_448D")
    OP_A2(0x8)

    ChrTalk(    #178
        0xFE,
        (
            "How many times have I told\x01",
            "you to show me some proof\x01",
            "of wrongdoing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        (
            "If I'm suspected of something,\x01",
            "then prove it! But you can't,\x01",
            "can you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        "Heh heh heh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_44EC")

    label("loc_448D")


    ChrTalk(    #181
        0xFE,
        (
            "If I'm suspected of something,\x01",
            "then prove it! But you can't,\x01",
            "can you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        "Heh heh heh...\x02",
    )

    CloseMessageWindow()

    label("loc_44EC")

    TalkEnd(0x15)
    Return()

    # Function_15_421B end

    def Function_16_44F0(): pass

    label("Function_16_44F0")

    TalkBegin(0x1C)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x14, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4635")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45C0")
    OP_A2(0xF)

    ChrTalk(    #183
        0xFE,
        (
            "It turns out that that guy locked\x01",
            "up really was a bad fellow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "I know we shouldn't judge people\x01",
            "by their appearances...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "But a lot of people are just\x01",
            "like we see them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4632")

    label("loc_45C0")


    ChrTalk(    #186
        0xFE,
        (
            "I know we shouldn't judge people\x01",
            "by their appearances...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        (
            "But a lot of people are just\x01",
            "like we see them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4632")

    Jump("loc_4920")

    label("loc_4635")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x14, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_476C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46F7")
    OP_A2(0xF)

    ChrTalk(    #188
        0xFE,
        (
            "That guy locked up really seems\x01",
            "like a bad fellow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "I know we shouldn't judge people\x01",
            "by their appearances...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        (
            "But a lot of people are just\x01",
            "like we see them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4769")

    label("loc_46F7")


    ChrTalk(    #191
        0xFE,
        (
            "I know we shouldn't judge people\x01",
            "by their appearances...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        (
            "But a lot of people are just\x01",
            "like we see them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4769")

    Jump("loc_4920")

    label("loc_476C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_485E")
    OP_A2(0xF)

    ChrTalk(    #193
        0xFE,
        (
            "No matter how I look at him,\x01",
            "that guy locked up seems like\x01",
            "a bad guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        (
            "If we can't find any evidence\x01",
            "against him soon, he's going\x01",
            "to be let free.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        (
            "Although, there's something that\x01",
            "I disagree with about that policy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4920")

    label("loc_485E")


    ChrTalk(    #196
        0xFE,
        (
            "If we can't find any evidence\x01",
            "against that guy locked up,\x01",
            "he's going to be set free.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        (
            "I just can't agree with a policy that\x01",
            "lets the seemingly bad individuals\x01",
            "back out onto the street.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4920")

    TalkEnd(0x1C)
    Return()

    # Function_16_44F0 end

    def Function_17_4924(): pass

    label("Function_17_4924")

    TalkBegin(0x1D)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x14, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4A4A")

    ChrTalk(    #198
        0xFE,
        (
            "And how do you explain this black\x01",
            "book and its secret accounts?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "Go ahead and think about it,\x01",
            "and then try to explain your\x01",
            "way out of this one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        (
            "I've got plenty of time to listen to you\x01",
            "make up excuses and try to worm your\x01",
            "way out of being locked up here for good.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CE3")

    label("loc_4A4A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x14, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_4B6B")

    ChrTalk(    #201
        0xFE,
        (
            "And how do you explain this black\x01",
            "book and its secret ledgers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        (
            "Go ahead and think about it\x01",
            "and then try to explain your\x01",
            "way out of this one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        (
            "I've got plenty of time to listen to you\x01",
            "make up excuses and try to worm your\x01",
            "way out of being locked up here for good.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CE3")

    label("loc_4B6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C55")
    OP_A2(0xE)

    ChrTalk(    #204
        0xFE,
        (
            "Hey! Where did the mira disappear\x01",
            "to that was listed in this black book?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        (
            "It would be in your best interest\x01",
            "to start talking now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        (
            "Because it's only a matter of time\x01",
            "until we find some evidence against\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CE3")

    label("loc_4C55")


    ChrTalk(    #207
        0xFE,
        (
            "It would be in your best interest\x01",
            "to start talking now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        (
            "Because it's only a matter of time\x01",
            "until we find some evidence against\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CE3")

    TalkEnd(0x1D)
    Return()

    # Function_17_4924 end

    def Function_18_4CE7(): pass

    label("Function_18_4CE7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x14, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x14, 0x1, 0x8000)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x338)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D06")
    Call(0, 19)
    Jump("loc_4FBE")

    label("loc_4D06")

    TalkBegin(0x1E)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x14, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4DBD")

    ChrTalk(    #209
        0xFE,
        (
            "I think it's safe to say that this\x01",
            "is the end of Nigel's back-door\x01",
            "schemes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        (
            "I think it's about time I made\x01",
            "arrangements to send him off to\x01",
            "Leiston Fortress.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FBB")

    label("loc_4DBD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x14, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_4E94")

    ChrTalk(    #211
        0xFE,
        (
            "Nigel's black book of secret accounts\x01",
            "was found in the sky bandits' hideout.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        (
            "I'm sure that the sky bandits\x01",
            "took it with them when they\x01",
            "robbed his factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        "Bad apples go together I guess.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4FBB")

    label("loc_4E94")


    ChrTalk(    #214
        0xFE,
        (
            "This man is being held on suspicion\x01",
            "of scheming to take over a factory\x01",
            "that didn't belong to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        (
            "The only bad news is we haven't\x01",
            "been able to find any decisive\x01",
            "evidence linking him to a crime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xFE,
        (
            "We can only detain him for so\x01",
            "long and after that we're going\x01",
            "to have to release him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FBB")

    TalkEnd(0x1E)

    label("loc_4FBE")

    Return()

    # Function_18_4CE7 end

    def Function_19_4FBF(): pass

    label("Function_19_4FBF")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 106320, 0, -76490, 180)
    SetChrPos(0x102, 105450, 0, -77130, 135)
    TurnDirection(0x101, 0x1D, 0)
    TurnDirection(0x102, 0x1D, 0)
    OP_6D(109770, 0, -76050, 2000)
    OP_0D()
    OP_4A(0x15, 0)
    OP_4A(0x1D, 0)

    ChrTalk(    #217
        0x1D,
        (
            "Hey! Where did the mira disappear\x01",
            "to that was listed in this black book?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x1D,
        (
            "It would be in your best interest\x01",
            "to start talking now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x1D,
        (
            "Because it's only a matter of time\x01",
            "until we find some evidence against\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x15,
        (
            "How many times have I told\x01",
            "you to show me some proof\x01",
            "of wrongdoing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x15,
        (
            "If I'm suspected of something,\x01",
            "then prove it! But you can't,\x01",
            "can you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x15,
        "Heh heh heh...\x02",
    )

    CloseMessageWindow()
    OP_62(0x1D, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)
    OP_4B(0x15, 0)
    OP_4B(0x1D, 0)
    OP_6D(106250, 0, -77490, 1500)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(400)
    OP_8C(0x101, 180, 400)
    OP_8C(0x102, 135, 400)

    ChrTalk(    #223
        0x101,
        "#000FWhat's the matter?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x101, 400)
    OP_4A(0x1E, 0)

    ChrTalk(    #224
        0x1E,
        "Huh? Oh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x1E,
        (
            "Actually, this man is being held on\x01",
            "suspicion of scheming to take over\x01",
            "a factory that didn't belong to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x1E,
        (
            "The only bad news is we haven't\x01",
            "been able to find any decisive\x01",
            "evidence linking him to a crime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x1E,
        (
            "We can only detain him for so\x01",
            "long and after that we're going\x01",
            "to have to release him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x101,
        (
            "#501FSo you're looking for some\x01",
            "material evidence, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x102,
        (
            "#013F...\x02\x03",

            "Hey, Estelle...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #230
        0x101,
        "#000FHmm?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #231
        0x102,
        (
            "#010FDo you remember that black book we\x01",
            "found in the sky bandits' hideout?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x101,
        (
            "#505FBlack book?\x02\x03",

            "#001FOh yeah, that one...\x02\x03",

            "You mean the one that was hidden\x01",
            "inside the vacuum cleaner, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #233
        0x1E,
        "A book inside a vacuum cleaner?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x1E,
        (
            "Would you mind letting me take a\x01",
            "look at it?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5517():
        OP_8C(0x101, 180, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_5517)
    OP_8C(0x102, 135, 400)

    ChrTalk(    #235
        0x101,
        (
            "#002FNope, we don't mind at all.\x01",
            "Here you are.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #236
        "\x07\x00Handed over \x07\x02Black Notebook\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_8C(0x1E, 45, 400)
    OP_62(0x1E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    ChrTalk(    #237
        0x1E,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x1E,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x1E,
        "...\x02",
    )

    CloseMessageWindow()
    OP_63(0x1E)
    Sleep(800)
    OP_62(0x1E, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #240
        0x1E,
        "Ah HA! This is what I was looking for.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x101,
        "#501FExcuse me?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x101, 400)

    ChrTalk(    #242
        0x1E,
        "This. There is no doubt about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x1E,
        (
            "This is his secret account ledger\x01",
            "for the factory.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x15, 400)

    ChrTalk(    #244
        0x1E,
        "Hey, Nigel!\x02",
    )

    CloseMessageWindow()
    OP_51(0x1F, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1F, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1F, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_5705():
        OP_69(0x1F, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_5705)

    def lambda_5713():
        TurnDirection(0x1D, 0x1E, 400)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_5713)

    def lambda_5721():
        TurnDirection(0x1C, 0x1E, 400)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_5721)

    def lambda_572F():
        TurnDirection(0x101, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_572F)

    def lambda_573D():
        TurnDirection(0x102, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_573D)
    OP_62(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x15, 0x1E, 400)
    OP_4A(0x15, 0)
    OP_4A(0x1D, 0)
    OP_4A(0x1C, 0)
    WaitChrThread(0x1F, 0x1)

    ChrTalk(    #245
        0x1E,
        (
            "Take a look at this! Look...\x01",
            "familiar?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0x15, 0x0, 0x0, 0x0, 0x2BC, 0x1770)
    Sleep(400)

    ChrTalk(    #246
        0x15,
        "Th-This can't be happening!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x15,
        (
            "That was taken along with my\x01",
            "vacuum by the burglars...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5831():

        label("loc_5831")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_5831")

    QueueWorkItem2(0x0, 1, lambda_5831)

    def lambda_5842():

        label("loc_5842")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_5842")

    QueueWorkItem2(0x1, 1, lambda_5842)

    def lambda_5853():

        label("loc_5853")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_5853")

    QueueWorkItem2(0x15, 1, lambda_5853)
    OP_92(0x1E, 0x1D, 0x3E8, 0x7D0, 0x0)
    Sleep(2000)
    OP_44(0x15, 0x1)
    OP_8C(0x1D, 0, 400)
    OP_8C(0x15, 180, 400)

    def lambda_5889():
        OP_6D(106250, 0, -77490, 2000)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_5889)
    OP_8E(0x1E, 0x1A162, 0x0, 0xFFFED090, 0x7D0, 0x0)
    TurnDirection(0x1E, 0x101, 400)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)

    def lambda_58C4():
        OP_8C(0x101, 180, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_58C4)
    OP_8C(0x102, 135, 400)
    WaitChrThread(0x1F, 0x1)

    ChrTalk(    #248
        0x1E,
        (
            "Thank you. This has been a\x01",
            "great help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x1E,
        (
            "Any bracer who can do work\x01",
            "like this is a good bracer in\x01",
            "my opinion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x1E,
        (
            "With this notebook, we should\x01",
            "easily be able to establish his\x01",
            "guilt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x1E,
        (
            "I'll make sure we send you an official\x01",
            "payment through the Bracer Guild\x01",
            "sometime in the near future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x1E,
        "Once again, I appreciate your help.\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #253
        "\x07\x00Quest \x07\x02[Black Notebook] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_3F(0x338, 1)
    OP_28(0x14, 0x4, 0x2)
    OP_28(0x14, 0x4, 0x4)
    OP_28(0x14, 0x4, 0x10)
    OP_28(0x14, 0x1, 0x1)
    OP_28(0x14, 0x1, 0x2)
    OP_28(0x14, 0x1, 0x4)
    OP_A3(0xF)
    OP_A3(0x8)
    OP_8C(0x1E, 45, 0)
    OP_8C(0x1C, 270, 0)
    OP_4B(0x1E, 0)
    OP_4B(0x1D, 0)
    OP_4B(0x1C, 0)
    OP_4B(0x15, 0)
    EventEnd(0x0)
    Return()

    # Function_19_4FBF end

    def Function_20_5ACD(): pass

    label("Function_20_5ACD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_724A")
    EventBegin(0x0)

    ChrTalk(    #254
        0x102,
        (
            "#010FThe end of the hall on the left...\x01",
            "It looks like this is the general's\x01",
            "room.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Knock]\x01",      # 0
            "[Leave]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_5B8F"),
        (0, "loc_5B94"),
        (SWITCH_DEFAULT, "loc_724A"),
    )


    label("loc_5B8F")

    EventEnd(0x1)
    Jump("loc_724A")

    label("loc_5B94")

    Fade(1000)
    OP_6D(118940, 0, 12530, 0)
    SetChrPos(0xF, 119060, 0, 14740, 0)
    SetChrPos(0x101, 118650, 0, 13360, 0)
    SetChrPos(0x102, 119650, 0, 12540, 315)
    SetChrPos(0x103, 117980, 0, 11970, 0)
    OP_0D()
    OP_A2(0x312)

    ChrTalk(    #255
        0x101,
        "#002F#4PAll right, here goes nothing...\x02",
    )

    CloseMessageWindow()
    OP_22(0x71, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #256
        0xF,
        "Gruff Voice",
        (
            "Are you here on behalf of\x01",
            "Mayor Maybelle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x101,
        "#000F#4PThat's right.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #258
        0xF,
        "Gruff Voice",
        "Very well, come inside.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x103,
        "#020F#4PThank you for seeing us.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(206210, 0, 13220, 0)
    OP_4A(0xF, 255)
    SetChrPos(0xF, 209550, 200, 11820, 270)
    SetChrFlags(0xF, 0x4)
    OP_0D()
    Sleep(500)
    OP_22(0x6A, 0x0, 0x64)
    Sleep(500)

    def lambda_5D19():
        OP_6D(209700, 0, 13260, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D19)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x103, 0x80)
    OP_43(0x101, 0x0, 0x0, 0x15)
    OP_43(0x103, 0x0, 0x0, 0x17)
    OP_43(0x102, 0x0, 0x0, 0x16)
    WaitChrThread(0x102, 0x0)

    ChrTalk(    #260
        0xF,
        (
            "#160F#4PI'm glad that you came.\x01",
            "My name is Morgan.\x02\x03",

            "I have been tasked with guarding\x01",
            "the Haken Gate by Her Majesty,\x01",
            "Queen Alicia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x103,
        (
            "#020F#1PIt's an honor to meet you, sir.\x01",
            "We are all here on behalf of\x01",
            "Mayor Maybelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x102,
        (
            "#010FPlease pardon our intrusion\x01",
            "during such a busy time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xF,
        (
            "#163F#4PThere's no need to apologize.\x01",
            "I've known Maybelle since she\x01",
            "was but a child.\x02\x03",

            "I couldn't imagine ignoring her\x01",
            "request, much less one from the\x01",
            "mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x101,
        (
            "#002F#1PAll right then, would you\x01",
            "please read this first?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #265
        "\x07\x00Handed over \x07\x02Mayor Maybelle's Letter\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3F(0x32D, 1)

    ChrTalk(    #266
        0xF,
        (
            "#161F#4P...\x02\x03",

            "#163FHmm... So it's about the missing airliner,\x01",
            "is it?\x02\x03",

            "Under ordinary circumstances that information\x01",
            "would be strictly confidential, but considering\x01",
            "this is a request coming from her...\x02\x03",

            "#160FI'll tell you everything I know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x101,
        "#001F#1PSweet! ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0xF,
        (
            "#161F#4P...?\x02\x03",

            "Why are you happy about something\x01",
            "that doesn't concern you?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #269
        0x101,
        (
            "#003F#1P(Crap, I should have kept\x01",
            "my mouth shut...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x102,
        (
            "#015FThe mayor appears quite distraught\x01",
            "over the situation...\x02\x03",

            "And so we've wanted to do anything\x01",
            "we can to assist her...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0xF,
        (
            "#163F#4PI see. Well, I'm glad to hear that\x01",
            "she has been blessed with some\x01",
            "good people around her.\x02\x03",

            "Let me get right down to things\x01",
            "and explain the status of our\x01",
            "search efforts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x103,
        "#022F#1PPlease do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0xF,
        (
            "#160F#4PThe airliner, Linde, disappeared on\x01",
            "its way to Rolent after taking off\x01",
            "from the Bose Landing Port.\x02\x03",

            "Presently, we have units searching\x01",
            "all areas of the region, but we have\x01",
            "yet to come up with anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x102,
        (
            "#012FSo what you're saying is the possibility\x01",
            "of the incident being caused by monsters\x01",
            "or an accident is fairly slim, right?\x02\x03",

            "If an airship of that size had crashed,\x01",
            "it likely would have been discovered in\x01",
            "the initial search efforts...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0xF,
        (
            "#160F#4PYes, that's exactly right.\x02\x03",

            "In fact, the flight route between Bose\x01",
            "and Rolent goes over some plains that\x01",
            "allow a commanding view of the land.\x02\x03",

            "And of course, the probability of the\x01",
            "airliner going down in Valleria Lake\x01",
            "or the ocean is extremely low.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x101,
        (
            "#007F#1PBoy, am I relieved to hear that it's\x01",
            "probably not a worst-case scenario\x01",
            "like that.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #277
        0x103,
        (
            "#022F#1PSo if those have been ruled out, then that\x01",
            "leaves the door open to the possibility that\x01",
            "the airship could have been taken, right?\x02\x03",

            "Which makes me think that the only remaining\x01",
            "motives must be to loot the cargo or demand\x01",
            "a ransom for the hostages...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x102,
        (
            "#012FIn other words, a hijacking, right?\x02\x03",

            "#013FAlso, considering the geographical conditions,\x01",
            "it could have been a covert operation carried\x01",
            "out by the Imperial Army.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #279
        0x101,
        (
            "#505F#2PAnd that would be really big news\x01",
            "if that were the case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0xF,
        "#161F#4P...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xF, 400)
    TurnDirection(0x103, 0xF, 400)

    ChrTalk(    #281
        0x101,
        "#004F#1PWhat's the matter, General?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xF,
        (
            "#163F#4PI was just thinking that that's\x01",
            "quite an impressive assessment\x01",
            "for some civilians.\x02\x03",

            "We also considered the possibility that the\x01",
            "Imperial Army was involved, so we have enforced\x01",
            "strict regulations on the flow of information.\x02\x03",

            "An international incident, if taken lightly, could\x01",
            "result in another war.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x101,
        "#003F#1PWar...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xF,
        (
            "#160F#4PBut, thanks to the small mercies of Aidios,\x01",
            "the possibility for another conflict disappeared\x01",
            "early this morning.\x02\x03",

            "A certain organization sent a letter to the Royal\x01",
            "Family and Orbalship Co. claiming responsibility\x01",
            "and demanding a ransom for the passengers.\x02\x03",

            "This organization goes by the name of the\x01",
            "'Capua family.'\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #285
        0x101,
        (
            "#580F#1PThe Capua family?\x02\x03",

            "It-it couldn't be who I think it is,\x01",
            "could it...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0x102,
        (
            "#012FIt certainly appears to be\x01",
            "that way...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0xF,
        (
            "#160F#4PThe sky bandits who have been operating in\x01",
            "the shadows in the Bose region and are led\x01",
            "by three siblings at their head.\x02\x03",

            "I take it you've heard of them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x101,
        (
            "#009F#1PNot only have we heard of them, we just\x01",
            "had a run-in with them in Rolent!\x02\x03",

            "I just can't believe those good-for-nothing\x01",
            "thieves have managed to create such a big\x01",
            "incident here in Bose...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_6D0E():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6D0E)

    ChrTalk(    #289
        0x102,
        "#012FEstelle...!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #290
        0x101,
        "#008F#1PEh...heh... Oops?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0xF,
        (
            "#161F#4PYou had a run-in with them\x01",
            "in Rolent?\x02\x03",

            "I had heard that some of their\x01",
            "gang had shown up in the Rolent\x01",
            "region, but...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x101,
        "#007F#1PI think he's on to us...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x103,
        (
            "#025F#1PYeah, because of you and\x01",
            "your big mouth...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0xF, 400)
    Sleep(500)

    ChrTalk(    #294
        0xF,
        (
            "#163F#4PI see now...\x02\x03",

            "I thought the way you were able to\x01",
            "analyze the situation was strange\x01",
            "for mere civilians...\x02\x03",

            "#160FBut I never would have guessed that\x01",
            "a girl and a couple of kids like you\x01",
            "were bracers!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0x101,
        "#009F#1PWh-Who are you calling kids!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x102,
        (
            "#013FJust for the record, Mayor Maybelle\x01",
            "did in fact request that we come here\x01",
            "and talk to you...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_6B(3070, 0)
    OP_6B(3000, 80)

    def lambda_6FF0():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0x1F40)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6FF0)

    def lambda_700E():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0x1F40)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_700E)

    def lambda_702C():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0x1F40)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_702C)

    ChrTalk(    #297
        0xF,
        "#162F#3S#4PSilence, deceivers!\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0xF, 5)
    SetChrPos(0xF, 209430, 0, 11990, 270)
    OP_0D()
    Sleep(400)

    ChrTalk(    #298
        0xF,
        "#162F#3S#4PGet in here, men!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0x101,
        "#004F#1PHe looks pre-tty pissed...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x103,
        (
            "#023F#1PSo this is how a hard-nosed\x01",
            "military man acts, eh?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7119():
        OP_6D(206340, 0, 12850, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_7119)
    OP_43(0xD, 0x0, 0x0, 0x18)
    OP_43(0xE, 0x0, 0x0, 0x19)
    Sleep(500)

    def lambda_7144():

        label("loc_7144")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_7144")

    QueueWorkItem2(0x101, 2, lambda_7144)

    def lambda_7155():

        label("loc_7155")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_7155")

    QueueWorkItem2(0x103, 2, lambda_7155)

    def lambda_7166():

        label("loc_7166")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_7166")

    QueueWorkItem2(0x102, 2, lambda_7166)
    Sleep(1000)

    ChrTalk(    #301
        0xD,
        "#1PWhat's the matter, General?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0xE,
        (
            "Did these visitors try to pull\x01",
            "anything funny?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0xF,
        (
            "#163F#4PThese 'bracers' need to be shown\x01",
            "the door!\x02\x03",

            "#4PThrow them out immediately!!!\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x35, 0x1, 0x200)
    OP_28(0x35, 0x1, 0x400)
    SetMapFlags(0x400000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T1400   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_724A")

    label("loc_724A")

    Return()

    # Function_20_5ACD end

    def Function_21_724B(): pass

    label("Function_21_724B")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_725C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_725C)
    SetChrPos(0xFE, 202980, 0, 8390, 0)
    OP_8E(0xFE, 0x318A8, 0x0, 0x2B02, 0xBB8, 0x0)
    OP_8E(0xFE, 0x328DE, 0x0, 0x2AF8, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_21_724B end

    def Function_22_72A9(): pass

    label("Function_22_72A9")

    Sleep(1600)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_72BF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_72BF)
    SetChrPos(0xFE, 202980, 0, 8390, 0)
    OP_8E(0xFE, 0x318A8, 0x0, 0x2B02, 0xBB8, 0x0)
    OP_8E(0xFE, 0x322F8, 0x0, 0x2D1E, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_22_72A9 end

    def Function_23_730C(): pass

    label("Function_23_730C")

    Sleep(800)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_7322():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_7322)
    SetChrPos(0xFE, 202980, 0, 8390, 0)
    OP_8E(0xFE, 0x318A8, 0x0, 0x2B02, 0xBB8, 0x0)
    OP_8E(0xFE, 0x32906, 0x0, 0x3228, 0xBB8, 0x0)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_23_730C end

    def Function_24_736F(): pass

    label("Function_24_736F")

    SetChrChipByIndex(0xFE, 14)
    SetChrPos(0xFE, 202630, 0, 7280, 0)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x318A8, 0x0, 0x2B02, 0xFA0, 0x0)
    OP_8E(0xFE, 0x31B28, 0x0, 0x30F2, 0xFA0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_24_736F end

    def Function_25_73BF(): pass

    label("Function_25_73BF")

    Sleep(500)
    SetChrChipByIndex(0xFE, 14)
    SetChrPos(0xFE, 202630, 0, 7280, 0)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x318A8, 0x0, 0x2B02, 0xFA0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_25_73BF end

    def Function_26_7400(): pass

    label("Function_26_7400")

    OP_31(0x3, 0x0, 0xD)
    OP_B5(0x3, 0x0)
    OP_B5(0x3, 0x1)
    OP_B5(0x3, 0x2)
    OP_B5(0x3, 0x3)
    OP_B5(0x3, 0x4)
    OP_41(0x3, 0x5C)
    OP_41(0x3, 0xF3)
    OP_41(0x3, 0x111)
    OP_41(0x3, 0x25B, 0x0)
    OP_41(0x3, 0x26A, 0x1)
    OP_41(0x3, 0x25E, 0x2)
    OP_35(0x3, 0xB4)
    OP_36(0x3, 0xF5)
    AddParty(0x3, 0xFF)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(14980, 200, 13030, 0)
    OP_67(0, 5040, -10000, 0)
    OP_6B(1680, 0)
    OP_6C(45000, 0)
    OP_6E(484, 0)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x101, 15)
    SetChrChipByIndex(0x102, 16)
    SetChrChipByIndex(0x103, 17)
    SetChrChipByIndex(0x104, 10)
    SetChrPos(0x101, 13130, 200, 10750, 0)
    SetChrPos(0x102, 14990, 200, 10750, 0)
    SetChrPos(0x103, 13190, 200, 13350, 180)
    SetChrPos(0x104, 14980, 200, 13350, 225)
    SetChrSubChip(0x101, 2)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x103, 1)
    SetChrSubChip(0x104, 0)
    FadeToBright(2000, 0)
    OP_0D()

    NpcTalk(    #304
        0x104,
        "Blond-Haired Man",
        (
            "#030F#6PLet me try and introduce\x01",
            "myself again.\x02\x03",

            "I'm Olivier Lenheim, a wandering\x01",
            "bard and musician by trade.\x02\x03",

            "As you already know, I am an Erebonian\x01",
            "touring your fair Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0x101,
        (
            "#001F#2PI'm Estelle and...\x02\x03",

            "#005FNow wait a minute! Why do we have\x01",
            "to introduce ourselves to you?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0x102,
        (
            "#010F#4PEasy, Estelle. He did intercede\x01",
            "for us back there.\x02\x03",

            "I'm Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0x103,
        (
            "#020F#3PAnd I'm Scherazard.\x02\x03",

            "Things were getting pretty heated,\x01",
            "and I'm glad you stepped in before\x01",
            "something really bad happened.\x02\x03",

            "Let me just say thanks.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 2)
    Sleep(300)

    ChrTalk(    #308
        0x104,
        (
            "#035F#4PHa, you've got nothing to thank\x01",
            "me for.\x02\x03",

            "I only did what any person who loves\x01",
            "beauty and peace would have done.\x02\x03",

            "However, if you insist, how about\x01",
            "going out on a date with me for a\x01",
            "day?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0x103,
        (
            "#027F#3PI'm going to have to pass on that.\x01",
            "First of all, I don't have that sort\x01",
            "of free time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0x104,
        "#034F#4PThat's too bad.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0)
    Sleep(100)
    SetChrSubChip(0x104, 1)
    Sleep(300)

    ChrTalk(    #311
        0x104,
        (
            "#030F#6PAll right then. I guess I'll accept\x01",
            "Joshua as a substitute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0x102,
        (
            "#017F#4PWhat do I have to do with any\x01",
            "of this...?\x02\x03",

            "Please don't involve me in your\x01",
            "questionable humor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0x104,
        (
            "#033F#6PWell, that's odd. I didn't mean it\x01",
            "as a joke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x102,
        (
            "#018F#4PSaying that makes you even\x01",
            "more questionable.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101)

    ChrTalk(    #315
        0x101,
        (
            "#009F#2PNow just a minute! How come you\x01",
            "didn't invite me on a date?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0)
    Sleep(300)

    ChrTalk(    #316
        0x104,
        (
            "#033F#6PYou?\x02\x03",

            "Umm, I don't know how to put this,\x01",
            "but you're a bit lacking in the sexy\x01",
            "department.\x02\x03",

            "#035FYou might want to think about taking\x01",
            "a lesson or two from your friends\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #317
        0x101,
        (
            "#005F#2PWell, excuse me for not being sexy!\x02\x03",

            "And...just what do you mean by\x01",
            "saying I should take a few lessons\x01",
            "from Joshua?!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 1)
    Sleep(300)

    ChrTalk(    #318
        0x102,
        (
            "#014F#4PC-Calm down, Estelle. I think you're\x01",
            "cute enough just the way you are.\x02\x03",

            "#017FThough I guess it's true... You are a\x01",
            "bit lackluster in the sexy category.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0x101,
        "#509F#1PWh-What did you just say?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0x103,
        (
            "#026F#3POh, good grief...\x02\x03",

            "#020FAnyway, like I said before,\x01",
            "we're busy.\x02\x03",

            "I'm sorry there's not a better way\x01",
            "to thank you, but we've got to get\x01",
            "going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x104,
        (
            "#030F#6PThen how about...\x02\x03",

            "You take me along with you\x01",
            "to the city of Bose?\x02\x03",

            "This is my first time in Liberl,\x01",
            "after all, and I'd like to request\x01",
            "a guide.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0x103,
        (
            "#020F#3PWell, if that's all that you want,\x01",
            "then I don't mind...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1200)
    SetChrSubChip(0x101, 0)

    ChrTalk(    #323
        0x101,
        "#009F#2PSchera! Now just a second!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0)
    Sleep(300)

    ChrTalk(    #324
        0x103,
        (
            "#020F#3PIt's the least we can do, and\x01",
            "we're headed to the same\x01",
            "place anyway.\x02\x03",

            "Plus, acting as a guide is one\x01",
            "of a bracer's many duties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0x101,
        (
            "#007F#2POh, all right. I guess we're stuck\x01",
            "with him until then.\x02\x03",

            "#003FB-But what if he tries to sink his poisonous\x01",
            "fangs of lust into Joshua...?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #326
        0x102,
        "#014F#4PUh, Estelle?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 2)
    Sleep(300)

    ChrTalk(    #327
        0x101,
        (
            "#002F#1PDon't you worry, Joshua!\x02\x03",

            "I'll save you from his perverted\x01",
            "attentions if he tries anything\x01",
            "funny!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x102,
        (
            "#018F#4PWhat is it exactly that you\x01",
            "think he'll try...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0x104,
        (
            "#033F#6PPlease don't refer to me like I'm\x01",
            "some sort of ferocious beast.\x02\x03",

            "#035FI'd rather that you call me a\x01",
            "'hunter of love.'\x02\x03",

            "Even 'love stealer' wouldn't be\x01",
            "that bad of a title, either.\x01",
            "Heh heh heh...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 2)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x103, 1)
    OP_62(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x103, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #330
        0x101,
        "#509F#2PAre you right in the head?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0x104,
        (
            "#031F#6PSo how about it, everyone?\x01",
            "Shall we leave for Bose?\x02\x03",

            "I'm counting on you all to\x01",
            "get me there safely.\x01",
            "Now let us be off!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0x101,
        (
            "#007F#2PWho died and made you leader...?\x02\x03",

            "#005FHey, wait a minute, you! I'm not done warning\x01",
            "you about the grisly fate that awaits you if\x01",
            "you sully Joshua's innocence!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(18700, 0, 12270, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 18700, 0, 12267, 180)
    SetChrPos(0x102, 18700, 0, 12267, 180)
    SetChrPos(0x103, 18700, 0, 12267, 180)
    SetChrPos(0x104, 18700, 0, 12267, 180)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0x104, 65535)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x103, 0)
    SetChrSubChip(0x104, 0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    OP_0D()
    Return()

    # Function_26_7400 end

    def Function_27_83A4(): pass

    label("Function_27_83A4")

    OP_78(0x64, 0x78, 0x82)
    OP_72(0x5, 0x4)
    OP_72(0x6, 0x4)
    OP_72(0x7, 0x4)
    OP_3F(0x32E, 1)
    OP_A2(0x32A)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_31(0x3, 0x0, 0xF)
    AddParty(0x3, 0xFF)
    OP_41(0x3, 0x5C)
    OP_41(0x3, 0xF3)
    OP_41(0x3, 0x111)
    OP_41(0x3, 0x25B, 0x0)
    OP_41(0x3, 0x26A, 0x1)
    OP_41(0x3, 0x25E, 0x2)
    SetChrPos(0x101, 109190, 0, -72940, 180)
    SetChrPos(0x102, 110080, 0, -71930, 180)
    SetChrPos(0x103, 108560, 0, -71890, 180)
    SetChrPos(0x104, 113220, 0, -74620, 225)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    OP_4A(0xD, 255)
    OP_4A(0xE, 255)
    SetChrPos(0xD, 108515, 0, -76468, 0)
    SetChrPos(0xE, 109535, 0, -76968, 0)
    SetChrChipByIndex(0xD, 13)
    SetChrChipByIndex(0xE, 13)
    OP_6D(102920, 0, -73120, 0)
    OP_67(0, 10460, -10000, 0)
    OP_6B(2240, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeToBright(2000, 0)
    OP_6D(109920, 0, -73120, 3000)
    OP_0D()

    ChrTalk(    #333
        0xD,
        (
            "#2PThe general will be questioning\x01",
            "you himself on the morrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0xD,
        (
            "#2PIf your innocence is proven, then\x01",
            "you will be released in two or\x01",
            "three days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0xE,
        (
            "#2PSo for the time being, this cell\x01",
            "will give you a place to cool\x01",
            "your heels.\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0xD, 0x1, 0x0, 0x1C)
    Sleep(500)
    OP_43(0xE, 0x1, 0x0, 0x1C)
    Sleep(1000)

    def lambda_85CC():
        OP_69(0x102, 0x7D0)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_85CC)
    Sleep(500)
    OP_8C(0x102, 225, 400)
    OP_8C(0x103, 135, 400)
    OP_8C(0x101, 0, 400)
    WaitChrThread(0x0, 0x3)

    ChrTalk(    #336
        0x101,
        (
            "#007F#2P*sigh* This is not even funny...\x02\x03",

            "Tossing us in a place like this\x01",
            "without even listening to a word\x01",
            "we have to say...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0x102,
        (
            "#013F#4PIf the army managed to arrest\x01",
            "the sky bandits, then I'm sure\x01",
            "we'd have our names cleared...\x02\x03",

            "But with the way things are at\x01",
            "the moment, that may not be\x01",
            "possible...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0x101,
        "#004F#2PHuh? Why not?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0x102,
        (
            "#012F#4PYou remember what the sky bandit\x01",
            "leader we fought in the old mine\x01",
            "said, right?\x02\x03",

            "He said, 'This can't be right! You're\x01",
            "not supposed to be here this early!'\x01",
            "if I remember correctly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0x101,
        (
            "#505F#2PNow that you mention it, he did\x01",
            "say that, didn't he?\x02\x03",

            "#580FYou're not trying to tell me that\x01",
            "he meant the army by that, are\x01",
            "you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0x102,
        (
            "#012F#4PI don't know for sure, but I would\x01",
            "bet that's what he meant.\x02\x03",

            "Which means that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0x103,
        (
            "#026F#1PThe sky bandits have a mole in\x01",
            "the army.\x02\x03",

            "Or a collaborator who is leaking\x01",
            "information.\x02\x03",

            "#022FThat's what you wanted to say,\x01",
            "isn't it, Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0x102,
        "#012F#4PYeah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0x101,
        (
            "#009F#2PW-Well, if that's the case, they'll\x01",
            "never get caught!\x02\x03",

            "Which means we were the only ones\x01",
            "that stood a chance of nabbing\x01",
            "them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0x103,
        (
            "#522F#1PBut now we're stuck in here.\x02\x03",

            "I wonder how your father would\x01",
            "get around this little setback...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #346
        0x104,
        "Man's Voice",
        (
            "#3PMy, my, my...\x02\x03",

            "Well, don't you all seem to be\x01",
            "in a bit of a fix?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #347
        0x101,
        (
            "#505F#2PHuh...? Did you just say something,\x01",
            "Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0x102,
        "#014F#4PNo, I didn't say anything...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0x103,
        (
            "#023F#1PIt came from the cell next door.\x02\x03",

            "It almost sounds familiar...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #350
        0x104,
        "Man's Voice",
        (
            "#3POh, how could you say something\x01",
            "so heartless?\x02\x03",

            "My lustrous voice should be\x01",
            "recognizable to anyone...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #351
        0x101,
        (
            "#509F#1PC-Could this unfounded self-\x01",
            "confidence...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 400)

    ChrTalk(    #352
        0x102,
        (
            "#017F#3PAnd tone of absurd narcissism\x01",
            "belong to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0x103,
        "#023F#1PIt's you, isn't it, Olivier?\x02",
    )

    CloseMessageWindow()
    OP_22(0xA6, 0x0, 0x64)

    NpcTalk(    #354
        0x104,
        "Man's Voice",
        (
            "#3PYou DO remember my\x01",
            "dulcet cords!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8D90():
        OP_6D(111710, 0, -72760, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_8D90)

    def lambda_8DA8():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_8DA8)

    def lambda_8DB8():
        OP_67(0, 6000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_8DB8)

    def lambda_8DD0():
        OP_6B(3000, 3000)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_8DD0)
    Sleep(1000)

    def lambda_8DE5():
        OP_8E(0xFE, 0x1ACFC, 0x0, 0xFFFEDC8E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8DE5)
    Sleep(500)

    def lambda_8E05():
        OP_8E(0xFE, 0x1A9E6, 0x0, 0xFFFEDE3C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8E05)
    Sleep(500)

    def lambda_8E25():
        OP_8E(0xFE, 0x1AE46, 0x0, 0xFFFEE058, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8E25)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 135, 0)
    WaitChrThread(0x103, 0x1)
    OP_8C(0x103, 135, 0)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 135, 0)
    WaitChrThread(0x0, 0x2)

    ChrTalk(    #355
        0x104,
        (
            "#031F#2PTo think that we'd meet again\x01",
            "in a place like this...\x02\x03",

            "It seems that we are bound\x01",
            "by destiny.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0x101,
        (
            "#005FWh-Why are you here...?\x02\x03",

            "I thought we took you to Bose!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0x103,
        (
            "#023FAnd now you're locked up in a\x01",
            "place like this...?\x02\x03",

            "What the heck did you do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0x104,
        (
            "#035F#2PCome now, let's not worry about\x01",
            "all the little details, shall we?\x02\x03",

            "I have my reasons, which are deeper\x01",
            "than the deepest ocean and higher\x01",
            "than the highest peak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0x101,
        (
            "#509FI'm definitely not asking now.\x02\x03",

            "I'm sure we'd just get tired while\x01",
            "you talked our ears off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0x102,
        (
            "#017FWhat a coincidence, Estelle...\x01",
            "I was just thinking the same thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0x103,
        (
            "#027FSo there you have it.\x01",
            "We don't really care to know.\x02\x03",

            "You talk so much that I'd probably be an\x01",
            "old woman by the time you were done,\x01",
            "and I'm not ready for wrinkles yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0x104,
        (
            "#031F#2PHa ha ha. Come on now,\x01",
            "let's not be like that.\x02\x03",

            "#030FI'll fill you in on all the details\x01",
            "of the tragic incident which\x01",
            "befell me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0x101,
        (
            "#007F(Didn't you listen, dummy? We\x01",
            "don't want to hear about it...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0x104,
        (
            "#035F#2PIt all began after we parted ways...\x02\x03",

            "I did some window shopping in the\x01",
            "Bose Market and then moved on to\x01",
            "the Anterose restaurant.\x02\x03",

            "You see, once I had eaten to my heart's\x01",
            "content, I began to play the grand piano\x01",
            "to then feed my artistic soul.\x02\x03",

            "And upon doing so, the restaurant\x01",
            "manager was overcome by my skill...\x02\x03",

            "So I was asked to stay and work\x01",
            "as the professional pianist for the\x01",
            "restaurant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0x101,
        (
            "#509FThat's great and all...but I thought\x01",
            "you were supposed to be a lutist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0x104,
        (
            "#035F#2PHa, a musical genius is not limited\x01",
            "to just one instrument.\x02\x03",

            "#030FAnyway, back to my story...\x01",
            "After negotiating a few of my own\x01",
            "conditions, I accepted the job offer.\x02\x03",

            "Those conditions were, of course,\x01",
            "food and wine for free every day\x01",
            "instead of mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0x102,
        (
            "#010FI don't know how to put it...\x01",
            "but that's very you, Olivier.\x02\x03",

            "Yet, I'm not sure how that has\x01",
            "anything to do with you getting\x01",
            "thrown in jail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #368
        0x104,
        (
            "#034F#2POh, well this is where the real\x01",
            "sob story begins.\x02\x03",

            "That night, I had been enjoying\x01",
            "a plate of sauteed duck I'd had\x01",
            "the chef prepare...\x02\x03",

            "But the blood-sauce which had been\x01",
            "used was a little too overbearing\x01",
            "for my palate.\x02\x03",

            "Consequently, I began to feel that\x01",
            "normal red wine was not satisfying\x01",
            "enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0x101,
        (
            "#509FThe more you talk, the more\x01",
            "I want to hit you...\x02\x03",

            "But go on. I'm curious, in spite\x01",
            "of knowing better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0x104,
        (
            "#030F#2PWell, so I borrowed a bottle of wine\x01",
            "which seemed good from the cellar.\x02\x03",

            "Something called 'Grand Chardonnay'\x01",
            "from the year 1183.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #371
        0x103,
        (
            "#024FGrand Chardonnay...from the year 1183?!\x02\x03",

            "That's the legendary vintage wine that\x01",
            "was auctioned off in the Royal City!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #372
        0x104,
        (
            "#033F#2POh, aren't you well informed?\x02\x03",

            "#033FI heard a rumor about it too,\x01",
            "so of course I was interested\x01",
            "in having a drink for myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #373
        0x101,
        (
            "#008FA-Auctioned off... How much\x01",
            "are we talking about here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0x103,
        (
            "#022FFrom what I heard...it went for\x01",
            "somewhere in the neighborhood\x01",
            "of five-hundred thousand mira.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #375
        0x101,
        (
            "#005FF-Five-hundred thousand mira?!\x02\x03",

            "For just one bottle?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0x102,
        (
            "#017FThat's out of this world...\x02\x03",

            "#018FAnd you didn't, did you, Olivier...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #377
        0x104,
        (
            "#031F#2PHa, such a needless question.\x01",
            "Of course I opened the bottle\x01",
            "and had a sip.\x02\x03",

            "Its sweet-smelling fragrance\x01",
            "tickled my nostrils...\x02\x03",

            "Its luxurious, mellow taste\x01",
            "caressed my throat...\x02\x03",

            "And can you believe what else?\x02\x03",

            "A rose-tinted vignette of time\x01",
            "and space existed within that\x01",
            "very bottle...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #378
        0x101,
        (
            "#007FI don't think I can listen to this\x01",
            "any longer...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #379
        0x102,
        (
            "#017FYeah, my ears are bleeding from\x01",
            "listening to such stupidity...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0x103,
        "#025FI'm completely dumbfounded...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0x104,
        (
            "#035F#2PThe sad thing is, that after taking a\x01",
            "sip of such excellent wine, I began\x01",
            "to feel the food was lacking.\x02\x03",

            "And as I was having the chef cook me\x01",
            "up something else to match the wine,\x01",
            "the restaurant manager returned.\x02\x03",

            "Since I'm not a stingy fellow,\x01",
            "I cordially invited him to join\x01",
            "me for a drink.\x02\x03",

            "But for some odd reason, he got rather\x01",
            "upset. In fact, he got so steaming mad\x01",
            "that his face looked like a ripe tomato.\x02\x03",

            "And before I could say another word,\x01",
            "a group of soldiers came filing in...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, 100)

    ChrTalk(    #382
        0x104,
        "#035F#2PAnd...well...\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -56)

    ChrTalk(    #383
        0x104,
        "#035F#2POne thing led to another and...\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(2000)

    ChrTalk(    #384
        0x104,
        (
            "#030F#2PI can't say another word about this\x01",
            "tragedy of being dragged all the way\x01",
            "here without coming to tears.\x02\x03",

            "#031FSo let us all weep together as you\x01",
            "sympathize with my dilemma.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0x101,
        "#500FZzz...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #386
        0x102,
        "#015F...Zzzz...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #387
        0x103,
        "#025FZzz... Idiot...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #388
        0x104,
        (
            "#033F#2PPardon...?\x02\x03",

            "#033F#2PBut do my ears deceive me...?\x02\x03",

            "I could have sworn I heard a 'zzz'\x01",
            "and 'zzzz' and even an assuredly\x01",
            "misheard 'idiot' coming from your cell.\x02\x03",

            "#035FAre you listening? This is where the\x01",
            "story gets really interesting.\x02\x03",

            "You see, several further trials\x01",
            "awaited me after I was brought here...\x02\x03",

            "#036FHello? Are you listening?\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    Sleep(2000)
    OP_22(0xD, 0x0, 0x64)
    Sleep(5000)
    SetChrPos(0x101, 109190, 0, -72940, 180)
    SetChrPos(0x102, 110080, 0, -71930, 180)
    SetChrPos(0x103, 108560, 0, -71890, 180)
    SetChrPos(0x104, 113180, 0, -74620, 225)
    OP_4A(0xD, 255)
    OP_4A(0xE, 255)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 109535, 0, -76170, 0)
    SetChrChipByIndex(0xD, 13)
    SetChrChipByIndex(0xE, 13)
    OP_6D(109920, 0, -73120, 0)
    OP_67(0, 10460, -10000, 0)
    OP_6B(2240, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)

    ChrTalk(    #389
        0xE,
        "#4PHey! You three, get up!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #390
        0x101,
        (
            "#007F#1PNnnnngggg... *yawn...*\x02\x03",

            "Mmm, I'm tired...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #391
        0x102,
        "#017F#1PWhat's wrong...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #392
        0x103,
        (
            "#025F#1PWhat...are you trying to tell us\x01",
            "we're being interrogated this\x01",
            "early in the morning?\x02\x03",

            "That's a little early even for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #393
        0xE,
        "#4PNo, it's just the opposite.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #394
        0xE,
        "#4PYou're being released.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #395
        0x101,
        "#004F#1PHuh...?!\x02",
    )

    CloseMessageWindow()
    OP_1D(0x10)
    FadeToBright(2000, 0)
    OP_0D()
    OP_8E(0xE, 0x1A0D8, 0x0, 0xFFFED694, 0x7D0, 0x0)
    OP_8C(0xE, 0, 400)
    Sleep(500)
    OP_22(0x6E, 0x0, 0x64)
    OP_72(0x3, 0x800)
    OP_70(0x3, 0x50)
    OP_73(0x3)
    OP_8E(0xE, 0x1A70C, 0x0, 0xFFFED676, 0x7D0, 0x0)
    OP_8C(0xE, 271, 400)

    ChrTalk(    #396
        0x101,
        "#004FWh-Why all of a sudden...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #397
        0x102,
        "#014FIs there a reason for this?\x02",
    )

    CloseMessageWindow()
    OP_4A(0x10, 255)
    OP_4A(0xF, 255)
    SetChrChipByIndex(0xF, 5)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x10, 102150, 0, -78020, 0)
    SetChrPos(0xF, 102150, 0, -76690, 0)
    SetChrFlags(0xF, 0x1)

    NpcTalk(    #398
        0x10,
        "Woman's Voice",
        (
            "#2PYes, I'd like to consider myself\x01",
            "that reason.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A456():
        OP_6D(108420, 0, -75290, 1500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A456)
    OP_8C(0x101, 225, 400)
    OP_8C(0x102, 225, 400)
    OP_8C(0x103, 225, 400)

    def lambda_A483():
        OP_8E(0xFE, 0x19A8C, 0x0, 0xFFFECF3C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_A483)
    Sleep(600)

    def lambda_A4A3():
        OP_8E(0xFE, 0x1980C, 0x0, 0xFFFED46E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_A4A3)
    WaitChrThread(0x10, 0x0)
    OP_8C(0x10, 45, 400)
    WaitChrThread(0xF, 0x0)
    OP_8C(0xF, 90, 400)
    WaitChrThread(0x104, 0x1)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #399
        0x101,
        "#004FM-Mayor Maybelle?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #400
        0x103,
        (
            "#023FWell, what an unusual place\x01",
            "to be meeting you.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A57B():
        OP_6D(106510, 0, -76720, 1500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A57B)
    OP_43(0x101, 0x1, 0x0, 0x1D)
    OP_43(0x102, 0x1, 0x0, 0x1E)
    OP_43(0x103, 0x1, 0x0, 0x1F)
    WaitChrThread(0x104, 0x1)
    WaitChrThread(0x102, 0x1)

    ChrTalk(    #401
        0x10,
        (
            "#611F#6PI'm really sorry about everything\x01",
            "that's happened to you.\x02\x03",

            "But, don't worry. Your names have\x01",
            "been cleared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #402
        0xF,
        (
            "#163FHmph. I don't completely agree\x01",
            "with everything, but...\x02\x03",

            "This is a request coming from\x01",
            "Maybelle herself. You'd better\x01",
            "remember to thank her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #403
        0x101,
        (
            "#501F#6PSo you mean...\x02\x03",

            "Mayor Maybelle stood up on\x01",
            "our behalf?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #404
        0x10,
        (
            "#610F#6PNo, that's not exactly it.\x02\x03",

            "I just explained your situation\x01",
            "to General Morgan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #405
        0x101,
        "#505F#6POur situation...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #406
        0xF,
        (
            "#160FYes... I have one question for\x01",
            "the both of you.\x02\x03",

            "Are you really the children of\x01",
            "Cassius Bright?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0xF, 400)
    TurnDirection(0x102, 0xF, 400)
    TurnDirection(0x103, 0xF, 400)

    ChrTalk(    #407
        0x101,
        "#004F#4PUm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #408
        0x102,
        (
            "#015F#4PYes, that's right.\x02\x03",

            "#010FThis is Estelle Bright...\x02\x03",

            "And I'm his adopted son, Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #409
        0xF,
        (
            "#160FI see...\x02\x03",

            "Now that you mention it, the girl\x01",
            "does slightly resemble Lena.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #410
        0x101,
        (
            "#004F#4P!!!\x02\x03",

            "You knew my mother?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #411
        0xF,
        (
            "#160FYes, I enjoyed your mother's cooking\x01",
            "on several occasions when I visited\x01",
            "your home in Rolent.\x02\x03",

            "#163FWhy, in fact, we even met once\x01",
            "when you were just a baby.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #412
        0x101,
        (
            "#580F#4PN-Now wait just a minute...\x02\x03",

            "You're a personal acquaintance of\x01",
            "my dad's?\x02\x03",

            "I knew that he was in the military\x01",
            "before, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #413
        0xF,
        (
            "#160FHmph... I don't know 'Cassius Bright,\x01",
            "the bracer'.\x02\x03",

            "The only Cassius I know is the\x01",
            "one from the service.\x02\x03",

            "He was a rare strategist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #414
        0x101,
        "#505F#4PStrategist? Dad?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #415
        0xF,
        (
            "#163FI just can't imagine what he saw\x01",
            "in the Bracer Guild...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #416
        0xF,
        (
            "#162FIt makes me angry just thinking\x01",
            "about it!\x02\x03",

            "You'll have to excuse me!\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xF, 0xFF)

    def lambda_ABB3():

        label("loc_ABB3")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_ABB3")

    QueueWorkItem2(0x10, 1, lambda_ABB3)

    def lambda_ABC4():

        label("loc_ABC4")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_ABC4")

    QueueWorkItem2(0x101, 1, lambda_ABC4)

    def lambda_ABD5():

        label("loc_ABD5")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_ABD5")

    QueueWorkItem2(0x102, 1, lambda_ABD5)

    def lambda_ABE6():

        label("loc_ABE6")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_ABE6")

    QueueWorkItem2(0x103, 1, lambda_ABE6)
    OP_43(0xF, 0x1, 0x0, 0x1C)
    Sleep(500)
    OP_8E(0xE, 0x1A61C, 0x0, 0xFFFECFAA, 0xBB8, 0x0)
    OP_43(0xE, 0x1, 0x0, 0x1C)
    Sleep(2000)
    OP_44(0x10, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0x103, 0x1)

    ChrTalk(    #417
        0x101,
        "#007F#4PWh-What's wrong with him?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 45, 400)

    ChrTalk(    #418
        0x10,
        (
            "#611F#6PHa ha...\x02\x03",

            "It seems like your father was a\x01",
            "brilliant officer in the military.\x02\x03",

            "I've heard from the general that he tried\x01",
            "several times to get your father to change\x01",
            "his mind about retiring.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10, 400)
    TurnDirection(0x103, 0x10, 0)
    TurnDirection(0x102, 0x10, 0)

    ChrTalk(    #419
        0x101,
        (
            "#008F#6PI-I didn't know that...\x02\x03",

            "Somehow, it feels hard to believe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #420
        0x103,
        (
            "#020FHowever, if that's the case...\x02\x03",

            "The general's hatred for bracers\x01",
            "may stem from Cassius leaving\x01",
            "the army.\x02\x03",

            "From the vexation of being left by\x01",
            "one of his most promising men.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #421
        0x102,
        "#019FI get the same impression.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #422
        0x101,
        (
            "#509F#6PSo what you're saying is...our\x01",
            "lives are such a pain because\x01",
            "of Dad?\x02\x03",

            "#582FTh-That dirty rotten scoundrel!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #423
        0x10,
        (
            "#611F#6PHa ha ha...\x02\x03",

            "#610FHow about we return to Bose now?\x02\x03",

            "With the airliner being found,\x01",
            "the situation has taken a new\x01",
            "turn.\x02\x03",

            "So there are a number of things\x01",
            "I'd like to discuss with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #424
        0x101,
        (
            "#501F#6POh, sure...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #425
        0x10,
        "#613F#6PIs something the matter?\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #426
        0x101,
        (
            "#505F#6PI'm definitely ready to get out\x01",
            "of here, but it feels like we're\x01",
            "forgetting something...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #427
        0x102,
        "#014F#6PNow that you mention it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #428
        0x103,
        "#023FWhat could it be...?\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    Sleep(400)
    OP_22(0xBE, 0x0, 0x64)
    Sleep(3000)
    OP_1D(0x49)

    NpcTalk(    #429
        0x104,
        "Man's Voice",
        (
            "#3POh...how callous people can be\x01",
            "at times.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1200)
    OP_1F(0x64, 0x190)
    SetChrChipByIndex(0x104, 18)
    SetChrPos(0x104, 113250, 0, -74620, 180)

    def lambda_B164():
        OP_6D(109470, 0, -72760, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_B164)

    def lambda_B17C():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_B17C)

    def lambda_B18C():
        OP_67(0, 6000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_B18C)

    def lambda_B1A4():
        OP_6B(3000, 3000)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_B1A4)

    def lambda_B1B4():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B1B4)

    def lambda_B1C2():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B1C2)

    def lambda_B1D0():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B1D0)

    def lambda_B1DE():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_B1DE)
    Sleep(3000)

    ChrTalk(    #430
        0x104,
        (
            "#034F#2PHow could you forget about a\x01",
            "companion who spent the night\x01",
            "with you in a cold, hard cell...?\x02\x03",

            "How lamentable...\x01",
            "How pitiful...\x02\x03",

            "Fine, be that way. I shall wither\x01",
            "away friendless and hungry,\x01",
            "alone in this dark purgatory...\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x104, 0x0, 0x0, 0x3)
    Sleep(2000)

    ChrTalk(    #431
        0x101,
        "#509F#1PIs he still here...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #432
        0x103,
        (
            "#021F#1PYeah...I completely forgot\x01",
            "about him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #433
        0x102,
        (
            "#010F#1PI'm sorry to say this, but there's\x01",
            "not much we can do for you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #434
        0x10,
        (
            "#612F#1PIs he...the musician I heard about?\x02\x03",

            "The one who chugged that bottle\x01",
            "of Grand Chardonnay without a\x01",
            "second thought?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    OP_20(0x5DC)
    OP_21()
    OP_1D(0x10)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x104, 65535)
    OP_0D()
    Sleep(500)
    OP_8C(0x104, 225, 400)

    ChrTalk(    #435
        0x104,
        (
            "#031F#2PHa, indeed that is I...\x02\x03",

            "Yet, my fair lass, I would be heartbroken\x01",
            "if you took my intentions the wrong way.\x02\x03",

            "For you see, I perceived it as an advance\x01",
            "payment for the exquisite services that\x01",
            "I was about to render.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #436
        0x10,
        (
            "#611F#1PHa ha ha. You're quite the\x01",
            "interesting character.\x02\x03",

            "All right, I'll see what I can do to\x01",
            "bargain with the general for your\x01",
            "release.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #437
        0x104,
        (
            "#033F#2PReally...? Truly...? You would do\x01",
            "such a kind service for a man\x01",
            "such as myself?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B602():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B602)
    Sleep(100)

    def lambda_B615():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B615)
    Sleep(100)

    def lambda_B628():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B628)
    WaitChrThread(0x102, 0x1)

    ChrTalk(    #438
        0x101,
        (
            "#506F#2PI-I think that may be asking\x01",
            "a bit much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #439
        0x103,
        (
            "#023F#2PIf the restaurant takes this to trial,\x01",
            "there's going to at least be a lawsuit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #440
        0x10,
        (
            "#610F#1PHa ha ha...well, there's no need to\x01",
            "worry about that.\x02\x03",

            "You see, the owner of the restaurant\x01",
            "is me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #441
        0x101,
        "#004F#2PHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #442
        0x10,
        (
            "#611F#1PAnd that Grand Chardonnay\x01",
            "was the very one I bid on.\x02\x03",

            "That being the case, I'm fairly\x01",
            "confident there won't be any\x01",
            "other problems over the matter.\x02",
        )
    )

    CloseMessageWindow()
    FadeToBright(1500, 0)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    ClearMapFlags(0x2000000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T1111   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_27_83A4 end

    def Function_28_B832(): pass

    label("Function_28_B832")

    OP_8C(0xFE, 270, 400)
    OP_8E(0xFE, 0x192A3, 0x0, 0xFFFED3F8, 0xBB8, 0x0)
    OP_8E(0xFE, 0x191CF, 0x0, 0xFFFEEEAB, 0xBB8, 0x0)
    OP_8E(0xFE, 0x18300, 0x7D0, 0xFFFEEDE9, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_28_B832 end

    def Function_29_B87B(): pass

    label("Function_29_B87B")

    OP_8E(0xFE, 0x1A216, 0x0, 0xFFFEE06C, 0xBB8, 0x0)
    OP_8E(0xFE, 0x1A1B2, 0x0, 0xFFFED68A, 0xBB8, 0x0)
    OP_8E(0xFE, 0x19DB6, 0x0, 0xFFFED432, 0xBB8, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_29_B87B end

    def Function_30_B8BF(): pass

    label("Function_30_B8BF")

    Sleep(1000)
    OP_8E(0xFE, 0x1A216, 0x0, 0xFFFEE06C, 0xBB8, 0x0)
    OP_8E(0xFE, 0x1A1B2, 0x0, 0xFFFED68A, 0xBB8, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_30_B8BF end

    def Function_31_B8F4(): pass

    label("Function_31_B8F4")

    Sleep(500)
    OP_8E(0xFE, 0x1A216, 0x0, 0xFFFEE06C, 0xBB8, 0x0)
    OP_8E(0xFE, 0x1A1B2, 0x0, 0xFFFED68A, 0xBB8, 0x0)
    OP_8E(0xFE, 0x1A20C, 0x0, 0xFFFED306, 0xBB8, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_31_B8F4 end

    def Function_32_B93D(): pass

    label("Function_32_B93D")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #443
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_32_B93D end

    SaveToFile()

Try(main)
