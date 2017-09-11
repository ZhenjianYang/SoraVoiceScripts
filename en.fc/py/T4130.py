from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4130   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4130.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T4130   ._SN',
            'ED6_DT01/T4130_1 ._SN',
            'ED6_DT01/T4130_2 ._SN',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Olivier',                              # 9
        'Nial',                                 # 10
        'Dorothy',                              # 11
        'Editor-in-Chief',                      # 12
        'Grant',                                # 13
        'Kurt',                                 # 14
        'Cready',                               # 15
        'Spencer',                              # 16
        'Zin',                                  # 17
        'Olivier',                              # 18
        'Miele',                                # 19
        'Godfrey',                              # 20
        'Phoebe',                               # 21
        'Nana',                                 # 22
        'Baral',                                # 23
        'Connor',                               # 24
        'Noticia',                              # 25
        'Faults',                               # 26
        'Sariah',                               # 27
        'Private Dan',                          # 28
        'Private Aluts',                        # 29
        'Agate',                                # 30
        'Tita',                                 # 31
        'Russell',                              # 32
        'Bill',                                 # 33
        'Wine Glass',                           # 34
        'Bottle',                               # 35
        'Wine Glass',                           # 36
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
        'ED6_DT07/CH00030 ._CH',             # 00
        'ED6_DT07/CH02060 ._CH',             # 01
        'ED6_DT07/CH02070 ._CH',             # 02
        'ED6_DT07/CH01023 ._CH',             # 03
        'ED6_DT07/CH01263 ._CH',             # 04
        'ED6_DT07/CH01623 ._CH',             # 05
        'ED6_DT07/CH01150 ._CH',             # 06
        'ED6_DT07/CH01143 ._CH',             # 07
        'ED6_DT07/CH00070 ._CH',             # 08
        'ED6_DT06/CH20050 ._CH',             # 09
        'ED6_DT07/CH01040 ._CH',             # 0A
        'ED6_DT07/CH01120 ._CH',             # 0B
        'ED6_DT07/CH02480 ._CH',             # 0C
        'ED6_DT07/CH02490 ._CH',             # 0D
        'ED6_DT07/CH01100 ._CH',             # 0E
        'ED6_DT07/CH01140 ._CH',             # 0F
        'ED6_DT07/CH01210 ._CH',             # 10
        'ED6_DT07/CH01143 ._CH',             # 11
        'ED6_DT07/CH01540 ._CH',             # 12
        'ED6_DT07/CH01300 ._CH',             # 13
        'ED6_DT07/CH00053 ._CH',             # 14
        'ED6_DT07/CH00063 ._CH',             # 15
        'ED6_DT07/CH02023 ._CH',             # 16
        'ED6_DT06/CH20048 ._CH',             # 17
        'ED6_DT07/CH00003 ._CH',             # 18
        'ED6_DT07/CH00013 ._CH',             # 19
        'ED6_DT07/CH00033 ._CH',             # 1A
        'ED6_DT07/CH00073 ._CH',             # 1B
        'ED6_DT06/CH20045 ._CH',             # 1C
        'ED6_DT06/CH20039 ._CH',             # 1D
        'ED6_DT07/CH01490 ._CH',             # 1E
        'ED6_DT07/CH01020 ._CH',             # 1F
        'ED6_DT07/CH01043 ._CH',             # 20
        'ED6_DT07/CH01123 ._CH',             # 21
        'ED6_DT07/CH01260 ._CH',             # 22
        'ED6_DT06/CH20063 ._CH',             # 23
        'ED6_DT06/CH20021 ._CH',             # 24
        'ED6_DT06/CH20020 ._CH',             # 25
    )

    AddCharChipPat(
        'ED6_DT07/CH00030P._CP',             # 00
        'ED6_DT07/CH02060P._CP',             # 01
        'ED6_DT07/CH02070P._CP',             # 02
        'ED6_DT07/CH01023P._CP',             # 03
        'ED6_DT07/CH01263P._CP',             # 04
        'ED6_DT07/CH01623P._CP',             # 05
        'ED6_DT07/CH01150P._CP',             # 06
        'ED6_DT07/CH01143P._CP',             # 07
        'ED6_DT07/CH00070P._CP',             # 08
        'ED6_DT06/CH20050P._CP',             # 09
        'ED6_DT07/CH01040P._CP',             # 0A
        'ED6_DT07/CH01120P._CP',             # 0B
        'ED6_DT07/CH02480P._CP',             # 0C
        'ED6_DT07/CH02490P._CP',             # 0D
        'ED6_DT07/CH01100P._CP',             # 0E
        'ED6_DT07/CH01140P._CP',             # 0F
        'ED6_DT07/CH01210P._CP',             # 10
        'ED6_DT07/CH01143P._CP',             # 11
        'ED6_DT07/CH01540P._CP',             # 12
        'ED6_DT07/CH01300P._CP',             # 13
        'ED6_DT07/CH00053P._CP',             # 14
        'ED6_DT07/CH00063P._CP',             # 15
        'ED6_DT07/CH02023P._CP',             # 16
        'ED6_DT06/CH20048P._CP',             # 17
        'ED6_DT07/CH00003P._CP',             # 18
        'ED6_DT07/CH00013P._CP',             # 19
        'ED6_DT07/CH00033P._CP',             # 1A
        'ED6_DT07/CH00073P._CP',             # 1B
        'ED6_DT06/CH20045P._CP',             # 1C
        'ED6_DT06/CH20039P._CP',             # 1D
        'ED6_DT07/CH01490P._CP',             # 1E
        'ED6_DT07/CH01020P._CP',             # 1F
        'ED6_DT07/CH01043P._CP',             # 20
        'ED6_DT07/CH01123P._CP',             # 21
        'ED6_DT07/CH01260P._CP',             # 22
        'ED6_DT06/CH20063P._CP',             # 23
        'ED6_DT06/CH20021P._CP',             # 24
        'ED6_DT06/CH20020P._CP',             # 25
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
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 21,
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
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 12,
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
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -54100,
        Z                   = 200,
        Y                   = 61000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = 5260,
        Z                   = 4130,
        Y                   = 2290,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = 4560,
        Z                   = 0,
        Y                   = 2500,
        Direction           = 186,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 4500,
        Z                   = 100,
        Y                   = -3850,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 23,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1D6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = -3600,
        Z                   = 0,
        Y                   = -2029,
        Direction           = 174,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = -3520,
        Z                   = 0,
        Y                   = -4540,
        Direction           = 6,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 58600,
        Z                   = 0,
        Y                   = -1690,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 59980,
        Z                   = 0,
        Y                   = -1800,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 61020,
        Z                   = 0,
        Y                   = 2490,
        Direction           = 197,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 65830,
        Z                   = 0,
        Y                   = -3420,
        Direction           = 92,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -57020,
        Z                   = 0,
        Y                   = 61110,
        Direction           = 327,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -59030,
        Z                   = 100,
        Y                   = 59540,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -56630,
        Z                   = 0,
        Y                   = 5500,
        Direction           = 174,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 1580,
        Z                   = 0,
        Y                   = 1800,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 2580,
        Z                   = 0,
        Y                   = 530,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = 260,
        Z                   = 4000,
        Y                   = 3770,
        Direction           = 215,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = -4200,
        Z                   = 600,
        Y                   = -3000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327716,
        ChipIndex           = 0x24,
        NpcIndex            = 0x1C6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3600,
        Z                   = 700,
        Y                   = -3350,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835045,
        ChipIndex           = 0x25,
        NpcIndex            = 0x1C6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3320,
        Z                   = 600,
        Y                   = -3880,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327716,
        ChipIndex           = 0x24,
        NpcIndex            = 0x1C6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 4530,
        TriggerZ            = 0,
        TriggerY            = 590,
        TriggerRange        = 400,
        ActorX              = 4560,
        ActorZ              = 1500,
        ActorY              = 2500,
        Flags               = 0x7E,
        TalkScenaIndex      = 2,
        TalkFunctionIndex   = 24,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 60700,
        TriggerZ            = 0,
        TriggerY            = 550,
        TriggerRange        = 400,
        ActorX              = 61020,
        ActorZ              = 1500,
        ActorY              = 2490,
        Flags               = 0x7E,
        TalkScenaIndex      = 2,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -56840,
        TriggerZ            = 0,
        TriggerY            = 3500,
        TriggerRange        = 400,
        ActorX              = -56630,
        ActorZ              = 1500,
        ActorY              = 5500,
        Flags               = 0x7E,
        TalkScenaIndex      = 2,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 57530,
        TriggerZ            = 0,
        TriggerY            = 400,
        TriggerRange        = 800,
        ActorX              = 57290,
        ActorZ              = 900,
        ActorY              = 340,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 2480,
        TriggerZ            = -250,
        TriggerY            = -3810,
        TriggerRange        = 800,
        ActorX              = 2480,
        ActorZ              = 1100,
        ActorY              = -3810,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_60E",          # 00, 0
        "Function_1_B35",          # 01, 1
        "Function_2_BB2",          # 02, 2
        "Function_3_BC8",          # 03, 3
        "Function_4_BEC",          # 04, 4
        "Function_5_C10",          # 05, 5
        "Function_6_C34",          # 06, 6
        "Function_7_1F85",         # 07, 7
        "Function_8_1FA5",         # 08, 8
        "Function_9_37E3",         # 09, 9
        "Function_10_4E18",        # 0A, 10
        "Function_11_6FE2",        # 0B, 11
        "Function_12_8B76",        # 0C, 12
        "Function_13_8DAA",        # 0D, 13
        "Function_14_8DE2",        # 0E, 14
        "Function_15_8E98",        # 0F, 15
    )


    def Function_0_60E(): pass

    label("Function_0_60E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_630")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x48), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    SoundLoad(233)
    SoundLoad(137)
    OP_A3(0x3FA)
    Event(0, 6)

    label("loc_630")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_644")
    SoundLoad(190)
    SoundLoad(137)
    OP_A3(0x3FB)
    Event(0, 8)

    label("loc_644")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_652")
    OP_A3(0x3FC)
    Event(0, 9)

    label("loc_652")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 5)), scpexpr(EXPR_END)), "loc_66E")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FD)
    Event(0, 12)

    label("loc_66E")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (105, "loc_67A"),
        (SWITCH_DEFAULT, "loc_6A3"),
    )


    label("loc_67A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_68D")
    OP_A2(0x627)
    Event(0, 10)

    label("loc_68D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A0")
    OP_A2(0x64E)
    Event(0, 11)

    label("loc_6A0")

    Jump("loc_6A3")

    label("loc_6A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6CA")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x40)
    SetChrPos(0xC, 5780, 0, 600, 0)

    label("loc_6CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_789")
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, 57680, 200, -5000, 90)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1F, 60140, 200, -4890, 270)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 5240, 4130, -410, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 27)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x10)
    SetChrPos(0x10, -3800, 200, -2180, 180)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, -3590, 200, -4680, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -55940, 0, 3500, 315)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -54920, 0, 62590, 135)
    OP_43(0x9, 0x0, 0x0, 0x2)
    Jump("loc_B34")

    label("loc_789")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_7E6")
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -54200, 0, 63010, 194)
    OP_43(0xA, 0x0, 0x0, 0x2)
    SetChrPos(0x18, -53520, 0, 123230, 98)
    OP_43(0x18, 0x0, 0x0, 0x2)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    Jump("loc_B34")

    label("loc_7E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_86C")
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -54200, 0, 63010, 194)
    OP_43(0xA, 0x0, 0x0, 0x2)
    SetChrChipByIndex(0xC, 34)
    OP_43(0xC, 0x0, 0x0, 0x2)
    SetChrPos(0x18, -59890, 0, 120300, 180)
    OP_43(0x18, 0x0, 0x0, 0x2)
    SetChrPos(0x19, -54350, 0, 1120, 265)
    SetChrChipByIndex(0x19, 15)
    OP_43(0x19, 0x0, 0x0, 0x2)
    ClearChrFlags(0x19, 0x4)
    ClearChrFlags(0x19, 0x10)
    Jump("loc_B34")

    label("loc_86C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_914")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 5860, 4100, -4760, 350)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -3400, 120, -4500, 0)
    SetChrChipByIndex(0x12, 32)
    OP_44(0x12, 0x0)
    SetChrFlags(0x12, 0x10)
    SetChrFlags(0x12, 0x4)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -3700, 150, -2180, 180)
    SetChrChipByIndex(0x13, 33)
    OP_44(0x13, 0x0)
    SetChrFlags(0x13, 0x10)
    SetChrFlags(0x13, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 62780, 0, -3550, 162)
    OP_43(0xA, 0x0, 0x0, 0x3)
    Jump("loc_B34")

    label("loc_914")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_91E")
    Jump("loc_B34")

    label("loc_91E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_9E7")
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 26)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0x8, -3590, 200, -4680, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 27)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x10)
    SetChrPos(0x10, -3800, 200, -2180, 180)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x19, -54350, 0, 1120, 265)
    SetChrChipByIndex(0x19, 15)
    OP_43(0x19, 0x0, 0x0, 0x2)
    ClearChrFlags(0x19, 0x4)
    ClearChrFlags(0x19, 0x10)
    SetChrPos(0x18, -60680, 0, 122710, 160)
    OP_43(0x18, 0x0, 0x0, 0x5)
    SetChrChipByIndex(0xB, 31)
    ClearChrFlags(0xB, 0x40)
    ClearChrFlags(0xB, 0x10)
    SetChrPos(0xB, 58490, 0, -630, 0)
    OP_43(0xB, 0x1, 0x0, 0x2)
    Jump("loc_B34")

    label("loc_9E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_9F1")
    Jump("loc_B34")

    label("loc_9F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_A71")
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 26)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0x8, -3590, 200, -4680, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 27)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x10)
    SetChrPos(0x10, -3800, 200, -2180, 180)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x18, -63230, 0, 59560, 338)
    OP_43(0x18, 0x0, 0x0, 0x2)
    SetChrFlags(0x19, 0x80)
    Jump("loc_B34")

    label("loc_A71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_A7B")
    Jump("loc_B34")

    label("loc_A7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_B15")
    ClearChrFlags(0x20, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_END)), "loc_B12")
    SetChrPos(0x8, 1490, 0, -3580, 225)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x11, 0x40)
    SetChrPos(0x11, 980, 0, -2990, 180)
    SetChrPos(0xE, 1410, -250, -4260, 8)
    SetChrFlags(0xE, 0x10)
    SetChrPos(0x20, 1620, 0, -2610, 180)
    SetChrChipByIndex(0xF, 15)
    ClearChrFlags(0xF, 0x40)
    ClearChrFlags(0xF, 0x10)
    SetChrPos(0xF, 4059, 0, -2910, 215)
    OP_43(0xF, 0x1, 0x0, 0x2)

    label("loc_B12")

    Jump("loc_B34")

    label("loc_B15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_B34")
    SetChrPos(0x18, -59890, 0, 120300, 180)
    OP_43(0x18, 0x0, 0x0, 0x2)

    label("loc_B34")

    Return()

    # Function_0_60E end

    def Function_1_B35(): pass

    label("Function_1_B35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B68")
    OP_B1("t4130_y")
    Jump("loc_B71")

    label("loc_B68")

    OP_B1("t4130_n")

    label("loc_B71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_END)), "loc_B81")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B81")

    OP_72(0x5, 0x20)
    OP_72(0x6, 0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_B95")
    Jump("loc_BB1")

    label("loc_B95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_BAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_END)), "loc_BA7")
    OP_64(0x0, 0x1)

    label("loc_BA7")

    Jump("loc_BB1")

    label("loc_BAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_BB1")

    label("loc_BB1")

    Return()

    # Function_1_B35 end

    def Function_2_BB2(): pass

    label("Function_2_BB2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BC7")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_BB2")

    label("loc_BC7")

    Return()

    # Function_2_BB2 end

    def Function_3_BC8(): pass

    label("Function_3_BC8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BEB")
    OP_8D(0xFE, 61240, -1420, 64280, -5700, 2500)
    Jump("Function_3_BC8")

    label("loc_BEB")

    Return()

    # Function_3_BC8 end

    def Function_4_BEC(): pass

    label("Function_4_BEC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C0F")
    OP_8D(0xFE, -57970, 64269, -56460, 57520, 3000)
    Jump("Function_4_BEC")

    label("loc_C0F")

    Return()

    # Function_4_BEC end

    def Function_5_C10(): pass

    label("Function_5_C10")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C33")
    OP_8D(0xFE, -62670, 124500, -59560, 120770, 3000)
    Jump("Function_5_C10")

    label("loc_C33")

    Return()

    # Function_5_C10 end

    def Function_6_C34(): pass

    label("Function_6_C34")

    ClearMapFlags(0x10000000)
    EventBegin(0x0)
    OP_6D(9550, 0, 2380, 0)
    OP_67(0, 10810, -10950, 0)
    OP_6B(3040, 0)
    OP_6C(44000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -2570, 200, 1820, 90)
    SetChrPos(0x101, 420, -250, -4920, 0)
    SetChrPos(0x102, 1640, -250, -4860, 0)
    TurnDirection(0xE, 0x8, 0)
    SetChrChipByIndex(0x8, 23)
    SetChrFlags(0x8, 0x2)
    OP_43(0x8, 0x1, 0x0, 0x7)
    OP_1F(0x64, 0x12C)
    SetChrFlags(0x8, 0x4)
    FadeToBright(1500, 0)
    OP_6D(560, 0, 1680, 5000)
    Fade(1500)
    OP_6D(1580, 3350, 420, 0)
    OP_67(0, 4250, -10000, 0)
    OP_6B(1430, 0)
    OP_6C(32000, 0)
    OP_6E(613, 0)
    OP_6D(1410, 0, 120, 3000)

    ChrTalk(    #0
        0x101,
        (
            "#007F#2P(Oh, joy. It's Olivier.)\x02\x03",

            "#006F(Still, I always figured his talk\x01",
            "of being a traveling musician\x01",
            "was a bunch of hot air...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x102,
        (
            "#019F#2P(He's actually pretty good.)\x02\x03",

            "(I guess he really wasn't\x01",
            "kidding, eh?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        "#008F#2P(Yeah... I'm kind of in shock.)\x02",
    )

    CloseMessageWindow()
    OP_6D(-140, 0, 2720, 2500)
    Sleep(2500)
    OP_20(0x7D0)
    OP_21()
    OP_A2(0x18)
    Sleep(1000)
    OP_22(0xE9, 0x0, 0x64)
    Sleep(1500)
    Fade(1000)
    SetChrFlags(0x8, 0x20)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x8, 0x1)
    SetChrChipByIndex(0x8, 26)
    ClearChrFlags(0x8, 0x2)
    TurnDirection(0x8, 0x101, 0)
    OP_0D()
    OP_1D(0xE)
    Sleep(400)

    ChrTalk(    #3
        0x8,
        (
            "#035F#6P...That was a little number\x01",
            "I call, 'Amber Amour.'\x02\x03",

            "It was, originally, a simple\x01",
            "interlude in an opera whose\x01",
            "name...doesn't matter.\x02\x03",

            "#030FI have infused it with the power\x01",
            "of love and devotion...\x02\x03",

            "...and invite you all to tip your\x01",
            "ears and drink deep of that power.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FC3():
        OP_6D(-1740, 0, 1730, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_FC3)

    def lambda_FDB():
        OP_8E(0xFE, 0xFFFFFC2C, 0x0, 0xFFFFF9DE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FDB)
    Sleep(500)

    def lambda_FFB():
        OP_8E(0xFE, 0xFFFFFA38, 0x0, 0xFFFFFF1A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FFB)
    WaitChrThread(0x101, 0x1)

    def lambda_101B():
        OP_8E(0xFE, 0xFFFFF664, 0x0, 0xFFFFFF24, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_101B)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x8, 400)
    WaitChrThread(0x102, 0x1)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(    #4
        0x101,
        (
            "#509F#4P...I take it all back.\x01",
            "He's just a weirdo.\x02\x03",

            "#007F*sigh*... Now I feel all dirty\x01",
            "for letting the song get to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x102,
        (
            "#010FNice to see you again, Olivier.\x01",
            "What brings you to the royal city?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "#031FI could little resist the pull of this place; it\x01",
            "drew me here as surely as the siren's fallen\x01",
            "tears are swept from the rivers to the sea.\x02\x03",

            "So here I stand, my raven-topped highness,\x01",
            "reunited with you at last!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x89, 0x0, 0x64)
    OP_62(0x8, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1200)
    OP_62(0x102, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #7
        0x102,
        (
            "#018F...You really haven't changed\x01",
            "at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#509F#4PThat's enough out of you. If I have\x01",
            "to be subjected to this, let's at\x01",
            "least sit down for a minute.\x02\x03",

            "Acting all smug and dandy, totally\x01",
            "oblivious to how tactless you are...\x01",
            "*grumble* *grumble*\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8)
    OP_62(0x8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #9
        0x8,
        (
            "#034FMy dear Estelle... How I've missed\x01",
            "that obstinate irritability you so\x01",
            "thoroughly embody!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x8, 0x4)
    SetChrChipByIndex(0x101, 24)
    SetChrChipByIndex(0x102, 25)
    SetChrPos(0x8, -3600, 200, -2200, 180)
    SetChrPos(0x101, -3590, 200, -4680, 0)
    SetChrPos(0x102, -4940, 200, -4690, 0)
    OP_6D(-3340, 0, -3050, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_22(0xEA, 0x0, 0x64)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #10
        0x101,
        (
            "#006FWeren't you and Schera supposed\x01",
            "to be going to Rolent?\x02\x03",

            "When did you get here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "#030FHmmm... About a month ago, I believe?\x02\x03",

            "After we parted company, Schera and\x01",
            "I spent a short, yet blissful time in Rolent.\x02\x03",

            "#034FBut alas, the overwhelming spirit of\x01",
            "wanderlust that courses through my\x01",
            "veins eventually got the better of me...\x02\x03",

            "'Twas all I could do to pull away from weeping,\x01",
            "darling Schera, to protect her from being swept\x01",
            "away to this blazing...dazzling...wonder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x102,
        (
            "#019F#2PWhat amazes me is that you\x01",
            "can actually say that with\x01",
            "a straight face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        (
            "#507FI'm betting that she drank you under the table\x01",
            "every night until you finally decided to run\x01",
            "off with your tail between your legs.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_9E(0x8, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(    #14
        0x8,
        "#033FAck...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#001FAnd then you figured you'd try your\x01",
            "luck at drinking with Aina, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)

    ChrTalk(    #16
        0x101,
        (
            "#505FAh, but you didn't know about\x01",
            "Aina, did you, Olivier? \x02\x03",

            "She's one of Schera's closest\x01",
            "friends... Works the information\x01",
            "desk at the Rolent branch.\x02\x03",

            "And as far as drinking goes,\x01",
            "she's the only person I've ever\x01",
            "seen who could outdo Schera.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8)
    Sleep(400)

    ChrTalk(    #17
        0x8,
        (
            "#031F...Ha ha ha. C-Come now,\x01",
            "dear Estelle...!\x02\x03",

            "I've never met this person\x01",
            "you speak of...this 'Aina.'\x01",
            "Absolutely not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#509FYou might want to try that again, only\x01",
            "this time without your voice cracking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x102,
        (
            "#013F#2POkay, Estelle...\x01",
            "Enough teasing.\x02\x03",

            "#015FI'm sure it was a very\x01",
            "trying time for him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "#034FAn affinity for spirits greater\x01",
            "than even Schera...\x02\x03",

            "Hateful inebriation!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #21
        0x8,
        (
            "#036F#3SWhy dost thou arm thy darkest\x01",
            "agents with smiles so alluring?\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        "#004FUh...flashback much?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x102,
        (
            "#019F#2PAnd so begins the Tale of Aina,\x01",
            "Olivier's most tragic ballad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "#034F*shudder* Indeed...\x02\x03",

            "#030FAnyway, you've come after completing\x01",
            "your tour of the surrounding regions,\x01",
            "I presume.\x02\x03",

            "Mayhap you've seen something\x01",
            "of interest?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#506FWell, we've seen a lot of stuff,\x01",
            "but it's not easy to just sum up\x01",
            "in a few words.\x02\x03",

            "#000FBesides, we're kind of looking\x01",
            "for someone, so maybe we can\x01",
            "catch up another time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "#033FOh-ho... And might I inquire as\x01",
            "to whom it is you wish to find?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x102,
        (
            "#010F#2PHis name's Zin. He's here from the\x01",
            "Calvard Republic to participate in\x01",
            "the Martial Arts Competition.\x02\x03",

            "We know he spends a good amount\x01",
            "of time in the local bars, so\x01",
            "maybe you've met him...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "#030FAhh, yes! I recall him... Large\x01",
            "as a bear, with a disposition\x01",
            "not to match, thankfully.\x02\x03",

            "I have borne witness to his countenance\x01",
            "on several occasions, but alas, today\x01",
            "has yet to bear any sign of him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        (
            "#007FSo in other words, he hasn't\x01",
            "been to the bar yet?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EF5")

    ChrTalk(    #30
        0x102,
        (
            "#010F#2POdds are, he's at the Calvardian\x01",
            "embassy, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        (
            "#035FHeh... Then shall we proceed\x01",
            "there at once?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F65")

    label("loc_1EF5")


    ChrTalk(    #32
        0x102,
        (
            "#010F#2PHe could have gone to the\x01",
            "Erbe Scenic Route.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        (
            "#035FHeh... Then shall we proceed\x01",
            "there at once?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F65")

    OP_A2(0x613)
    OP_28(0x46, 0x1, 0x4)
    FadeToBright(1000, 0)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_C34 end

    def Function_7_1F85(): pass

    label("Function_7_1F85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F9A")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    OP_48()
    Jump("Function_7_1F85")

    label("loc_1F9A")

    Sleep(50)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_7_1F85 end

    def Function_8_1FA5(): pass

    label("Function_8_1FA5")

    EventBegin(0x0)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x108, 0x4)
    SetChrPos(0x108, -3800, 0, -2180, 180)
    SetChrPos(0x101, -3590, 200, -4680, 0)
    SetChrPos(0x102, -4940, 200, -4690, 0)
    SetChrPos(0x8, -4500, 2000, 4700, 225)
    SetChrChipByIndex(0x8, 28)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0xE, 4620, 0, 2500, 180)
    OP_6D(-3340, 0, -3050, 0)
    OP_22(0xEA, 0x0, 0x64)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x108, 0x4)
    SetChrChipByIndex(0x101, 24)
    SetChrChipByIndex(0x102, 25)
    SetChrChipByIndex(0x108, 27)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #34
        0x108,
        (
            "#070FSo that's how it is, eh?\x02\x03",

            "Tell me something, though.\x01",
            "Why do you want to take part\x01",
            "in the tournament?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        (
            "#506FWell, uh... I've been kinda itching\x01",
            "to do something like this ever since\x01",
            "I caught those preliminary matches.\x02\x03",

            "You know, really throw down\x01",
            "with some tough opponents...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x102,
        (
            "#010F#2PWe're traveling all over the\x01",
            "kingdom to help prepare us to\x01",
            "become full-fledged bracers.\x02\x03",

            "This would be the perfect opportunity\x01",
            "to test ourselves and see if our\x01",
            "training has paid off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x108,
        (
            "#074FHmmmm...\x02\x03",

            "#070FAll right. Let's do it.\x02\x03",

            "We can get you registered tomorrow,\x01",
            "before the tourney begins, so no\x01",
            "worries on that score.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        (
            "#001FWoohoo! ㈱\x02\x03",

            "#004FHey... Are you sure you're okay with\x01",
            "giving us an answer so quickly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x108,
        (
            "#071FHey, it'll give me a chance to\x01",
            "see just how skilled you are.\x02\x03",

            "You just watch my back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        (
            "#008FRoger that!\x01",
            "Thank you, Zin!\x02\x03",

            "I'm gonna give it everything\x01",
            "I've got!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x102,
        "#010F#2PWe appreciate it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x108,
        (
            "#070FIt's no bother.\x02\x03",

            "#074FI had been planning to enter\x01",
            "as a solo competitor...\x02\x03",

            "...but I suppose that having\x01",
            "some help could improve my\x01",
            "chances of overall victory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        (
            "#006FNaturally! Once I'm in the ring,\x01",
            "that championship's in the bag!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x102,
        (
            "#013F#2PWe're still one person short\x01",
            "of the requirement, though...\x02\x03",

            "Since we have to face four-person\x01",
            "teams, one more would give us\x01",
            "the best possible odds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        (
            "#505FOh, right... Hmm...\x02\x03",

            "#001FHey, I'll bet we could beat\x01",
            "them without a fourth!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x108,
        (
            "#072FNo... If you really want to come out\x01",
            "on top, you have to be prepared.\x02\x03",

            "A battle is waged well before\x01",
            "the first blow is struck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#007FErr...well, yeah, I guess.\x02\x03",

            "I sure wish Schera were with us.\x01",
            "That'd keep my spirits up.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 1)

    ChrTalk(    #48
        0x101,
        (
            "#006FHey, do you suppose we could ask\x01",
            "Elnan to try getting in touch\x01",
            "with her in Rolent?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 2)

    ChrTalk(    #49
        0x102,
        (
            "#017FI think she's kind of busy\x01",
            "at the moment.\x02\x03",

            "Since Dad's not there, and we're\x01",
            "not there, that branch is pretty\x01",
            "short-handed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        (
            "#509FYeah, that's true...\x02\x03",

            "#504FGrrrr! Isn't there someone who\x01",
            "can partner up with us?\x02",
        )
    )

    CloseMessageWindow()
    OP_1F(0x46, 0x190)
    Sleep(400)
    OP_22(0xBE, 0x0, 0x64)
    Sleep(2000)

    NpcTalk(    #51
        0x8,
        "Man's Voice",
        (
            "#4PHeh... And here I was, thinking\x01",
            "you might never see your way\x01",
            "clear to asking.\x02",
        )
    )

    CloseMessageWindow()
    OP_1F(0x64, 0x190)
    OP_62(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x108, 2)
    OP_66(0x0)
    OP_6D(-2690, 0, 2590, 2500)

    ChrTalk(    #52
        0x101,
        (
            "#509FAh...\x01",
            "Enter the pervert, stage left.\x02\x03",

            "Don't tell me you were\x01",
            "hiding out upstairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x102,
        (
            "#010FWere you listening in on\x01",
            "our conversation?\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 29)
    SetChrSubChip(0x8, 0)
    OP_0D()
    OP_99(0x8, 0x0, 0x3, 0x7D0)
    Sleep(200)
    OP_99(0x8, 0x3, 0xA, 0x5DC)
    Sleep(400)

    ChrTalk(    #54
        0x8,
        (
            "#035FHeh heh heh... Indeed, I heard\x01",
            "every tragic syllable!\x02\x03",

            "Therefore, it seemed the appropriate\x01",
            "time to make an appearance.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)

    def lambda_2A57():
        OP_6D(-4170, 0, -2650, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A57)
    OP_8E(0x8, 0xFFFFED2C, 0x0, 0x3DE, 0xBB8, 0x0)
    SetChrFlags(0x8, 0x4)
    OP_8E(0x8, 0xFFFFE9BC, 0x0, 0xFFFFF92A, 0xBB8, 0x0)
    SetChrChipByIndex(0x8, 26)
    OP_96(0x8, 0xFFFFEC64, 0xC8, 0xFFFFF722, 0x258, 0x1388)
    OP_22(0xD1, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)

    ChrTalk(    #55
        0x101,
        (
            "#009FHey!\x01",
            "Who asked you to sit down?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x108,
        (
            "#073FHe was the one who was playing\x01",
            "the piano before, wasn't he?\x02\x03",

            "You know him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        (
            "#007FReplace 'know' with 'can't get rid\x01",
            "of,' and that about covers it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x102,
        (
            "#019FAnd we haven't even known\x01",
            "him for that long, either.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 1)

    ChrTalk(    #59
        0x8,
        (
            "#030FMany call me Olivier Lenheim, the\x01",
            "wandering minstrel from Erebonia.\x02\x03",

            "It was Estelle and Joshua's\x01",
            "pleasure to make my acquaintance\x01",
            "on an earlier case.\x02\x03",

            "#031FAnd ever since, we seem to keep\x01",
            "running into each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        (
            "#582FQuit trying to trick him!\x01",
            "Zin, don't listen to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x108,
        (
            "#070FHmm... I'm not entirely sure what's\x01",
            "going on, but there's no harm in\x01",
            "introductions, I suppose.\x02\x03",

            "Zin Vathek. Bracer from Calvard\x01",
            "and perpetual traveler of the\x01",
            "path of Wushu.\x02\x03",

            "I've enjoyed your piano playing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x8,
        (
            "#035FHa ha... You do me great honor,\x01",
            "good sir.\x02\x03",

            "#030FI have also heard tales of your\x01",
            "prowess in the preliminary matches.\x02\x03",

            "Tell me, did you truly defeat a\x01",
            "team of four, entirely on your own?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x108,
        (
            "#070FAll I can say is that I had\x01",
            "the good fortune of them all\x01",
            "being rank amateurs.\x02\x03",

            "So what does a wandering minstrel,\x01",
            "as you say, want with us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        "#005F#3SWait, wait! Hold it!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #65
        0x102,
        (
            "#010FOlivier, I'd like for you to\x01",
            "verify something for me...\x02\x03",

            "By any chance, do you have a lot\x01",
            "of spare time on your hands?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0)

    ChrTalk(    #66
        0x8,
        (
            "#033FAnd you say that I haven't changed,\x01",
            "good Joshua. You were ever one for\x01",
            "the pointed questions.\x02\x03",

            "#034FIt has been nearly a month since\x01",
            "I came to Grancel...\x02\x03",

            "I've traveled the length and breadth of the city,\x01",
            "enjoying all the sights...except the castle. Those\x01",
            "boorish soldiers would not allow me to pass.\x02\x03",

            "To be certain, there are other places that I'd\x01",
            "like to visit, but I could not bear to leave\x01",
            "with the birthday celebrations so close.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        "#509FIn other words, you're bored.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x8,
        (
            "#030FNow, what is this talk of being\x01",
            "a man short that I happened\x01",
            "to overhear?\x02\x03",

            "I have heard that the winner of\x01",
            "this competition will be invited\x01",
            "to an extravagant dinner party...\x02\x03",

            "#031FSurely, this can only be\x01",
            "divine providence!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        "#007F*sigh*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x102,
        (
            "#017FYeah, pretty much what we\x01",
            "figured you were thinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x8,
        (
            "#030FI had, in fact, wondered if\x01",
            "you might invite me to join\x01",
            "you in this tournament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x108,
        "#070FYou okay with that?\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #73
        0x101,
        (
            "#009FW-Wait, Zin.\x01",
            "It's not that simple...\x02\x03",

            "I mean, you don't even know if\x01",
            "he's any good in a fight...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x108,
        (
            "#070FHis specialty is orbal firearms,\x01",
            "right?\x02\x03",

            "I think the team would be pretty well\x01",
            "served by a broad range of tactics.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0x8, 1)

    ChrTalk(    #75
        0x101,
        "#004FWHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x8,
        (
            "#033FOh, my...\x01",
            "This is a surprise.\x02\x03",

            "I presume you could tell from\x01",
            "my walk and the musculature of\x01",
            "my shoulders...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x108,
        (
            "#070FThat, and the way your eyes move.\x02\x03",

            "A martial artist and swordsman\x01",
            "each have distinct ways that\x01",
            "they track their surroundings.\x02\x03",

            "You track for a specific point\x01",
            "on any possible target.\x02\x03",

            "It's characteristic of someone\x01",
            "who's familiar with small arms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        (
            "#506FWhooooaaaa...\x01",
            "That's awesome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x102,
        (
            "#014FI see...\x01",
            "It certainly makes sense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x8,
        (
            "#035FHm... I'll have to be more\x01",
            "careful in the future, then.\x02\x03",

            "#030FAnd in your eyes, do I pass\x01",
            "muster for participating in\x01",
            "the tournament with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x108,
        (
            "#071FYeah, I think so.\x01",
            "Welcome aboard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        "#505FI'm not sure I like this...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x102,
        (
            "#010FThank you for your assistance,\x01",
            "Olivier.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_21()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4150   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_1FA5 end

    def Function_9_37E3(): pass

    label("Function_9_37E3")

    EventBegin(0x0)
    OP_6D(59950, 0, -3760, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x9, 59950, 0, -5070, 270)
    SetChrPos(0x101, 58770, 0, -3810, 180)
    SetChrPos(0x102, 58750, 0, -5890, 0)
    ClearChrFlags(0x9, 0x80)

    ChrTalk(    #84
        0x101,
        (
            "#000FWhew... The food in here sure\x01",
            "is spicy. Tasty, though!\x02\x03",

            "Nothing beats ribs covered in\x01",
            "sauce with some potatoes that\x01",
            "are cooked just right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x102,
        (
            "#010FI like a good cup of coffee\x01",
            "after a meal, myself.\x02\x03",

            "I've always heard it's difficult\x01",
            "to make it well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x9,
        (
            "#140FBah... Way to eat up a man's\x01",
            "paycheck, you guys.\x02\x03",

            "I don't know how I'm supposed to\x01",
            "afford all this on a reporter's\x01",
            "salary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        (
            "#000FNow, now...\x01",
            "It was a great meal. And great\x01",
            "meals don't come cheap.\x02\x03",

            "Okay now, you were saying something\x01",
            "about an interview...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x9,
        (
            "#140FHmph. I could write a story\x01",
            "about extortion...\x02\x03",

            "Moving on. There ain't been much to confirm\x01",
            "that the queen's really taken ill after\x01",
            "the Guardsmen went all terrorist.\x02\x03",

            "What I need is some clear info\x01",
            "that HASN'T been combed over\x01",
            "and 'cleaned up' by the army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        "#000F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x102,
        "#010F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x9,
        (
            "#140FI heard a little from Dorothy\x01",
            "about the kidnapping in Zeiss...\x02\x03",

            "Look, let me get right to the point.\x02\x03",

            "I know you've got Colonel Richard by\x01",
            "the proverbial tail...I just need to\x01",
            "know how hard you're holding on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        "#000FWay to be blunt, there...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x102,
        (
            "#010FSounds like you've already figured\x01",
            "out an awful lot...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x9,
        (
            "#140FI KNEW he was crooked...\x02\x03",

            "Before that interview in our magazine\x01",
            "bumped up his popularity, he wasn't really\x01",
            "well known or worth paying attention to.\x02\x03",

            "Seems like this guy has been\x01",
            "planning his moves every step of the way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x102,
        (
            "#010FRight now, we can't say for sure\x01",
            "that he's planning some kind of\x01",
            "treason against the throne.\x02\x03",

            "But it does look like he's\x01",
            "manipulating the duke somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x9,
        (
            "#140FDuke Dunan...\x02\x03",

            "He's taking advantage of the queen's\x01",
            "poor health and acting like he owns\x01",
            "Grancel Castle, all right...\x02\x03",

            "But what I don't get is why\x01",
            "none of the military bigwigs\x01",
            "are making their move.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        (
            "#000FWell, about that...\x02\x03",

            "...What do you think, Joshua?\x01",
            "Should we tell him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x102,
        (
            "#010FWell, we could definitely use\x01",
            "some fresh intel ourselves.\x02\x03",

            "As long as he scratches our\x01",
            "backs...let's scratch his.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x9,
        (
            "#140FHey, now... You two know\x01",
            "something, don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x102,
        (
            "#010FWe would have told you sooner...\x02\x03",

            "But anything we say from here\x01",
            "on out has to be completely\x01",
            "off the record.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x101,
        "#000FI hope you're ready for this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x9,
        (
            "#140FAhh, shit. I'm really not\x01",
            "going to like this, am I?\x02\x03",

            "But fine.\x01",
            "Say what you're gonna say.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    FadeToBright(2000, 0)

    ChrTalk(    #103
        0x9,
        "#140F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#000F*sigh* You said you were\x01",
            "ready for this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x9,
        (
            "#140FThat's just...\x01",
            "No way...\x02\x03",

            "Are you really serious?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x102,
        (
            "#010FI'm afraid so.\x02\x03",

            "The Special Ops soldiers were\x01",
            "behind the sky bandit incident,\x01",
            "as well as the arson.\x02\x03",

            "Not to mention the kidnapping of the\x01",
            "kingdom's greatest scientific mind.\x02\x03",

            "General Morgan is at the top of\x01",
            "the chain of command, and even\x01",
            "he's basically under arrest.\x02\x03",

            "All of the terrorist-style activities\x01",
            "are being made out to look like the\x01",
            "Guardsmen are doing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x9,
        (
            "#140FOkay, enough!\x01",
            "You've made your point!\x02\x03",

            "Damn it all... I can't even\x01",
            "report a word of this.\x02\x03",

            "The army's censors already have their\x01",
            "stamp all over the latest issue.\x02\x03",

            "They did their work at the\x01",
            "final printing stage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        "#000FR-Really...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x9,
        (
            "#140FAnd I'm left with nothing to cover\x01",
            "except for this damn tournament.\x02\x03",

            "...Hey, wait a minute.\x02\x03",

            "You two have something up your\x01",
            "sleeves, don't you? That's why\x01",
            "you're in the tournament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x101,
        (
            "#000FYou could say that...\x02\x03",

            "We can't give you all the details\x01",
            "on our current request...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x102,
        (
            "#010FWe do, however, think that we\x01",
            "need to make a move, just to\x01",
            "break the deadlock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x9,
        (
            "#140FYou don't say...\x02\x03",

            "...\x02\x03",

            "...All right, then.\x02\x03",

            "Since I can't do anything as \x01",
            "a reporter, I might as well\x01",
            "pitch in.\x02\x03",

            "I'll see what I can dig up. I've\x01",
            "got a few...sources...with fingers\x01",
            "in places the guild would never go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        "#000FThat'll be a big help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x102,
        (
            "#010FDoing anything to oppose the\x01",
            "military's going to be a risky\x01",
            "proposition, you know.\x02\x03",

            "Are you sure you're okay\x01",
            "with this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x9,
        (
            "#140FLet me deal with that...\x02\x03",

            "Now's as good a chance as ever\x01",
            "to prove that the pen really\x01",
            "is mightier than the sword!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        "#000FNial...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x102,
        "#010FUnderstood... Thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x9,
        (
            "#140FYeah, just leave it to me.\x02\x03",

            "So, what do you want more\x01",
            "information on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x101,
        (
            "#000FInfo about the army's movements\x01",
            "would be good.\x02\x03",

            "As would knowing whether or not\x01",
            "all of the Royal Guardsmen have\x01",
            "been arrested...\x02\x03",

            "And also where General Morgan\x01",
            "is being held...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x9,
        (
            "#140FGot it. All stuff that I've\x01",
            "been thinking about, too.\x02\x03",

            "I'll check them out.\x01",
            "Anything else?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x102,
        (
            "#010FUhh...\x02\x03",

            "Maybe some background info on someone\x01",
            "in the Intelligence Division?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x101,
        "#000FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x9,
        "#140FYou mean like a profile?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x102,
        (
            "#010FOn Colonel Richard, Captain Amalthea\x01",
            "and 2nd Lieutenant Lorence.\x02\x03",

            "If we have to face any of them, the\x01",
            "more we know, the better our odds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x9,
        (
            "#140F'If you know the enemy and know\x01",
            "yourself, you need not fear the\x01",
            "result of a hundred battles.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        (
            "#000FAnd you can bet that the colonel's\x01",
            "working on the same principle.\x02\x03",

            "He'll probably be watching the\x01",
            "fights tomorrow and the next day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x102,
        (
            "#010FDo you think you can manage\x01",
            "it, Nial?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x9,
        (
            "#140FI do know a few army folks...\x02\x03",

            "I can't get you anything classified,\x01",
            "but I might be able to scare up that\x01",
            "profile info.\x02\x03",

            "Okay, then...\x01",
            "I'll see what I can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x101,
        (
            "#000FThank you!\x01",
            "You're a lifesaver!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x102,
        "#010FWe appreciate it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x9,
        (
            "#140FHey, don't sweat it.\x02\x03",

            "You can pay me back by winning that\x01",
            "championship and filling me in on\x01",
            "what you hear at that dinner party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        "#000FI figured as much...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x102,
        "#010FWe'll do everything we can.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    AnonymousTalk(    #134
        "\x07\x05Afterward, Estelle and Joshua returned to their hotel room...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #135
        (
            "\x07\x05...where they both retired early, to ease the stress and fatigue of the\x01",
            "fights.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #136
        "\x07\x05The next morning...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4132   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_37E3 end

    def Function_10_4E18(): pass

    label("Function_10_4E18")

    EventBegin(0x0)
    OP_6D(-60260, 0, 66930, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x9, -56660, 0, 64750, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x101, -61900, 0, 67420, 135)
    SetChrPos(0x102, -63460, 0, 66810, 135)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #137
        0x101,
        "#006FHeeeey! Nial!\x02",
    )

    CloseMessageWindow()

    def lambda_4EB7():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4EB7)

    ChrTalk(    #138
        0x102,
        "#010FPardon us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x9,
        (
            "#141FHey, you're here.\x02\x03",

            "Amazing. Dorothy actually got the message\x01",
            "to you guys, and didn't screw it up.\x01",
            "Will miracles never cease?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4F61():
        OP_6D(-57890, 0, 65099, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4F61)

    def lambda_4F79():
        OP_6B(2600, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_4F79)

    def lambda_4F89():

        label("loc_4F89")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_4F89")

    QueueWorkItem2(0x101, 1, lambda_4F89)

    def lambda_4F9A():
        OP_8E(0xFE, 0xFFFF18F2, 0x0, 0xFC94, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4F9A)
    OP_8E(0x102, 0xFFFF1370, 0x0, 0x1046E, 0xBB8, 0x0)

    def lambda_4FC9():
        OP_8E(0xFE, 0xFFFF1F6E, 0x0, 0xFB9A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4FC9)
    OP_8E(0x102, 0xFFFF13B6, 0x0, 0xFC30, 0xBB8, 0x0)
    OP_8E(0x102, 0xFFFF1A28, 0x0, 0xF988, 0xBB8, 0x0)
    TurnDirection(0x102, 0x9, 400)

    ChrTalk(    #140
        0x9,
        (
            "#141FSo...I hear you won your match today.\x02\x03",

            "Dorothy was in an absurdly cheerful\x01",
            "mood when she got back from it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x101,
        "#502FHa ha... Cool.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x102,
        "#6P#012FNial, about what we discussed earlier...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x9,
        (
            "#143FStraight to business, I see.\x02\x03",

            "#140FTake a look... Got some background\x01",
            "on those big shots.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #144
        "\x07\x05Nial held out a black file folder.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #145
        0x101,
        "#004FIs this from the Royal Army?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x9,
        (
            "#140FYeah... Nothing super-secret, but I\x01",
            "was able to get out some documents.\x02\x03",

            "Let's just say they're...on loan\x01",
            "from some of my army contacts. But\x01",
            "keep that under your hat, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x102,
        "#6P#012FAbsolutely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x101,
        (
            "#06FWell, let's go ahead and\x01",
            "read it here.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    OP_20(0x5DC)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #149
        "\x07\x05Estelle and Joshua opened the black folder.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_1D(0x22)
    FadeToDark(1500, 0, -56)
    OP_0D()
    Sleep(500)

    label("loc_5308")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5DA2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5390")

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Colonel Richard]\x01",             # 0
            "[Captain Amalthea]\x01",            # 1
            "[2nd Lieutenant Lorence]\x01",      # 2
            "[Close folder]\x01",                # 3
        )
    )

    Jump("loc_53D7")

    label("loc_5390")


    Menu(
        0,
        10,
        10,
        0,
        (
            "[Colonel Richard]\x01",             # 0
            "[Captain Amalthea]\x01",            # 1
            "[2nd Lieutenant Lorence]\x01",      # 2
        )
    )


    label("loc_53D7")

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5401"),
        (1, "loc_57B6"),
        (2, "loc_5A97"),
        (3, "loc_5D8F"),
        (SWITCH_DEFAULT, "loc_5D9F"),
    )


    label("loc_5401")

    OP_AD(0x40034, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #150
        "\x07\x05Colonel Alan Richard.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #151
        "\x07\x05Born 1168, in the Ruan region of Liberl.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #152
        (
            "\x07\x05Graduated head of his class from the military academy, later assigned to the\x01",
            "mobile task force led by Cassius Bright.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #153
        (
            "\x07\x051192: Recognized for distinguished service under Cassius Bright in the\x01",
            "Hundred Days War.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #154
        (
            "\x07\x05Appointed to staff of the military operations office after Colonel Bright's\x01",
            "retirement. \x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #155
        (
            "\x07\x051201: Suggested formation of Intelligence Division. Queen Alicia approves the\x01",
            "request and appoints him as the first commander of the new branch.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57A9")
    OP_A2(0x673)
    SetMessageWindowPos(75, 250, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #156
        (
            "\x07\x00#007FWow... Pretty impressive.\x02\x03",

            "Well, he IS the man in charge.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 300, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #157
        (
            "#012FHe always seemed to\x01",
            "be pretty sharp.\x02\x03",

            "Looks like Major Cid was right about\x01",
            "him serving under Dad ten years ago.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(75, 250, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #158
        (
            "#505FSo Dad really WAS a colonel...\x02\x03",

            "I wonder why he retired... I mean, he\x01",
            "had respect and fame and all that.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_57A9")

    OP_AE(0x1F4)
    Sleep(500)
    Jump("loc_5D9F")

    label("loc_57B6")

    OP_AD(0x40035, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #159
        "\x07\x05Captain Kanone Amalthea.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #160
        "\x07\x05Born 1175, in Liberl's capital city of Grancel.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #161
        (
            "\x07\x05Her excellent grades at the military academy earned her a place on the staff\x01",
            "of the military operations office shortly after graduation.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #162
        (
            "\x07\x051201: Reassigned to the newly-formed Intelligence Division on Colonel\x01",
            "Richard's recommendation.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #163
        (
            "\x07\x05Later appointed as Colonel Richard's aide-de-camp, assisting directly with\x01",
            "military operational command.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A8A")
    OP_A2(0x674)
    SetMessageWindowPos(75, 250, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #164
        (
            "\x07\x00#509F'Excellent grades' again. Another\x01",
            "intellectual big shot, looks like.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 300, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #165
        (
            "#015FThat appointment means that she's\x01",
            "been working for Colonel Richard\x01",
            "for a long time.\x02\x03",

            "No wonder she's so loyal to him...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_5A8A")

    OP_AE(0x1F4)
    Sleep(500)
    Jump("loc_5D9F")

    label("loc_5A97")

    OP_AD(0x40036, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #166
        "\x07\x052nd Lieutenant Lorence Belgar.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #167
        "\x07\x05Age and nationality unknown.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #168
        (
            "\x07\x05A member of Jester who was invited by Colonel Richard to join the\x01",
            "Intelligence Division.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #169
        "\x07\x05Previous activities unknown.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D82")
    OP_A2(0x675)
    SetMessageWindowPos(75, 250, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #170
        (
            "\x07\x00#580FHe's been in disguise all along...\x01",
            "He's not even from Liberl.\x02\x03",

            "And what's up with his old job as a\x01",
            "mercenary being one big blank spot?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 300, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #171
        (
            "#013F...I don't know.\x02\x03",

            "Jaeger corps are known as the best\x01",
            "mercenaries in the business for good\x01",
            "reason...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(75, 250, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #172
        (
            "#505FNo kidding?\x02\x03",

            "So maybe the colonel was just looking\x01",
            "for a really skilled fighter?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 300, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #173
        (
            "#015FIt's a possibility.\x02\x03",

            "And I think I've heard of this 'Jester'\x01",
            "somewhere before.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_5D82")

    OP_AE(0x1F4)
    Sleep(500)
    Jump("loc_5D9F")

    label("loc_5D8F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_5D9F")

    label("loc_5D9F")

    Jump("loc_5308")

    label("loc_5DA2")

    FadeToBright(1500, 0)
    OP_0D()

    ChrTalk(    #174
        0x101,
        (
            "#006FThanks for this, Nial. At least\x01",
            "we know a little more about\x01",
            "who we're dealing with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x9,
        (
            "#141FAs long as it's useful.\x02\x03",

            "I've learned a few juicy tidbits\x01",
            "while I was digging around, too.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 400)

    ChrTalk(    #176
        0x102,
        "#6P#014F'Juicy tidbits'...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x9,
        (
            "#141FFor example, 1st Lieutenant Julia Schwarz\x01",
            "of the Royal Guardsman, currently\x01",
            "wanted for questioning...\x02\x03",

            "...was in the academy the same\x01",
            "year as Captain Amalthea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x101,
        "#004FReally, now...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x102,
        (
            "#6P#014FThey never gave off the impression\x01",
            "that they got along all that well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x9,
        (
            "#145FMaybe because they were\x01",
            "academy rivals.\x02\x03",

            "Kanone's got the brains, and\x01",
            "Julia's got the combat skills...\x01",
            "Pretty big difference there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x102,
        "#6P#010FAhh, I see. I'd imagine so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x101,
        (
            "#006FLooks like Julia's always been the\x01",
            "super-serious knightly type, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x9,
        (
            "#140FNext up...and this has nothing to\x01",
            "do with the military, mind you...\x02\x03",

            "You kids know about\x01",
            "Princess Klaudia, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x101,
        (
            "#505FPrincess Klaudia...\x01",
            "Sounds familiar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x102,
        (
            "#6P#010FIf memory serves, she was orphaned when\x01",
            "the crown prince and his wife died.\x02\x03",

            "She's the granddaughter of Her\x01",
            "Majesty, Queen Alicia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x9,
        (
            "#140FRight. She's not well known, but\x01",
            "she is the direct descendant of\x01",
            "the queen.\x02\x03",

            "From what I could dig up, she lives\x01",
            "in the Royal Keep, and pretty much\x01",
            "stays there most of the time.\x02\x03",

            "And it seems someone's been\x01",
            "looking for prospective marriage\x01",
            "candidates for her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x101,
        (
            "#007FHuh...\x02\x03",

            "That's not super-unusual for\x01",
            "rich families, but still...\x02\x03",

            "#003FJust...gross.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x102,
        (
            "#6P#017FThat's not the point.\x02\x03",

            "#012FThe issue here is, who is\x01",
            "this 'someone'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x9,
        "#141FHa ha... Spot on, kid.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x101,
        "#004FIt could be...\x02",
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
            "[Queen Alicia]\x01",         # 0
            "[Duke Dunan]\x01",           # 1
            "[Colonel Richard]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_646E"),
        (1, "loc_6569"),
        (2, "loc_667E"),
        (SWITCH_DEFAULT, "loc_6784"),
    )


    label("loc_646E")


    ChrTalk(    #191
        0x9,
        (
            "#142FOn paper, sure.\x02\x03",

            "But it's Colonel Richard who's\x01",
            "scouring foreign countries for\x01",
            "a suitable candidate, looks like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x101,
        (
            "#004FHuh...okay.\x02\x03",

            "#505FBut isn't that kind of weird?\x02\x03",

            "Why would he even be involved in\x01",
            "setting up an arranged marriage?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6784")

    label("loc_6569")


    ChrTalk(    #193
        0x9,
        (
            "#142FClose, but no cigar, kid.\x02\x03",

            "Actually, it's Colonel Richard who's\x01",
            "been scouring foreign countries for\x01",
            "a suitable candidate, looks like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x101,
        (
            "#004FHuh...okay.\x02\x03",

            "#505FBut isn't that kind of weird?\x02\x03",

            "Why would he even be involved in\x01",
            "setting up an arranged marriage?\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x45, 0x1)
    Jump("loc_6784")

    label("loc_667E")


    ChrTalk(    #195
        0x9,
        (
            "#141FHey, not bad, kid.\x02\x03",

            "It is Colonel Richard who's been\x01",
            "scouring foreign countries for a\x01",
            "suitable candidate, looks like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x101,
        (
            "#007FI knew it...\x02\x03",

            "#505FBut isn't that kind of weird?\x02\x03",

            "Why would he even be involved in\x01",
            "setting up an arranged marriage?\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x45, 0x2)
    Jump("loc_6784")

    label("loc_6784")


    ChrTalk(    #197
        0x9,
        (
            "#141FPretty interesting, ain't it?\x02\x03",

            "And now...there's something\x01",
            "I want from you two.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x101,
        "#004FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x102,
        (
            "#6P#015FYou want us to win the tournament\x01",
            "and get you some information at the\x01",
            "dinner party...right?\x02\x03",

            "#010FIs that about the long\x01",
            "and short of it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x101,
        (
            "#509FOh, okay...\x02\x03",

            "#007FYou're not shy about asking\x01",
            "for stuff, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x9,
        (
            "#141FHey, I got you information.\x01",
            "This is called 'give and\x01",
            "take,' sweetheart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x102,
        "#6P#019FTrue, and it's been helpful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x101,
        (
            "#006FOh, all right. We'll let you\x01",
            "know if we find out anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x9,
        (
            "#147FThat's what I like to hear.\x02\x03",

            "#141FThough if all goes well today, I might not even\x01",
            "need to rely on you two.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xC3, 0x0, 0x64)
    LoadEffect(0x0, "map\\\\mp001_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -55170, 2000, 64580, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #205
        0x9,
        "#143F'Scuse me for a sec.\x02",
    )

    CloseMessageWindow()
    OP_44(0x9, 0xFF)
    OP_8C(0x9, 90, 400)

    def lambda_6AA8():
        OP_6D(-56140, 0, 65099, 1500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6AA8)
    OP_8E(0x9, 0xFFFF24D2, 0x0, 0xFA13, 0xBB8, 0x0)
    OP_8E(0x9, 0xFFFF290A, 0x0, 0xFA13, 0xBB8, 0x0)
    OP_8C(0x9, 0, 400)
    Sleep(500)
    WaitChrThread(0x9, 0x1)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x0, 0x0)
    LoadEffect(0x0, "map\\\\mp001_01.eff")
    PlayEffect(0x0, 0x1, 0xFF, -55170, 2000, 64580, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)

    ChrTalk(    #206
        0x9,
        (
            "#140FHello, Liberl News.\x02\x03",

            "#147FOh, it's you! I've been waiting\x01",
            "for you to call in.\x02\x03",

            "#143FWhat...\x01",
            "Starting now?\x02\x03",

            "#141FOkay, got it.\x01",
            "I'll meet you there.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x1, 0x0)
    Sleep(500)

    ChrTalk(    #207
        0x101,
        "#501FWhat's going on?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    def lambda_6C1B():
        OP_6D(-57890, 0, 65099, 1200)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6C1B)
    OP_8E(0x9, 0xFFFF2676, 0x0, 0xFA13, 0x7D0, 0x0)
    OP_8E(0x9, 0xFFFF1F6E, 0x0, 0xFB9A, 0x7D0, 0x0)
    TurnDirection(0x9, 0x101, 400)
    WaitChrThread(0x9, 0x1)

    ChrTalk(    #208
        0x9,
        (
            "#141FSorry to cut and run on you, but\x01",
            "I've gotta go meet someone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x102,
        (
            "#6P#014FSounds like you're in for a\x01",
            "late night. The sun's going\x01",
            "down as it is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x9,
        (
            "#145FHey, I'm a night owl, anyways.\x02\x03",

            "I'm only up during the daytime while\x01",
            "the crazy chick is being trained.\x02\x03",

            "#142FBut hey, no biggie.\x02\x03",

            "You kids can just kick back\x01",
            "and relax while I'm out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x101,
        (
            "#006FGotcha.\x02\x03",

            "Good luck with your work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x9,
        (
            "#141FYou too. Don't screw up\x01",
            "tomorrow's match!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6E26():

        label("loc_6E26")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_6E26")

    QueueWorkItem2(0x101, 1, lambda_6E26)

    def lambda_6E37():

        label("loc_6E37")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_6E37")

    QueueWorkItem2(0x102, 1, lambda_6E37)

    def lambda_6E48():
        OP_6D(-59840, 0, 65099, 2000)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6E48)
    OP_8E(0x9, 0xFFFF1B9A, 0x0, 0xFF14, 0xBB8, 0x0)
    OP_8E(0x9, 0xFFFF1564, 0x0, 0xFF14, 0xBB8, 0x0)
    OP_8E(0x9, 0xFFFF1258, 0x0, 0x1039C, 0xBB8, 0x0)
    OP_8E(0x9, 0xFFFF0736, 0x0, 0x1039C, 0xBB8, 0x0)
    OP_44(0x101, 0xFF)
    OP_8E(0x9, 0xFFFF0736, 0xFFFFF74A, 0xF406, 0xBB8, 0x0)
    SetChrFlags(0x9, 0x80)
    OP_44(0x102, 0xFF)
    WaitChrThread(0x9, 0x1)
    OP_20(0x5DC)

    def lambda_6EDB():
        OP_6D(-57890, 0, 65099, 1500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6EDB)
    WaitChrThread(0x9, 0x1)
    OP_21()
    OP_1D(0xE)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #213
        0x101,
        (
            "#006F#6PWell, then...\x01",
            "What should we do now?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #214
        0x102,
        (
            "#4P#010FHmmm... I guess we should stop\x01",
            "by the guild, then go back to\x01",
            "the hotel.\x02\x03",

            "We ought to report in the info\x01",
            "that Nial got for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x101,
        "#006F#6PFine by me.\x02",
    )

    CloseMessageWindow()
    OP_28(0x48, 0x1, 0x40)
    EventEnd(0x0)
    Return()

    # Function_10_4E18 end

    def Function_11_6FE2(): pass

    label("Function_11_6FE2")

    EventBegin(0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -56250, 0, 60940, 90)
    SetChrPos(0x101, -60190, 0, 65280, 135)
    SetChrPos(0x102, -61190, 0, 64849, 135)
    SetChrPos(0x108, -60700, 0, 66190, 135)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    OP_4A(0xA, 255)
    OP_6D(-54490, 0, 61730, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #216
        0xA,
        (
            "#152FThis is weird, Chief.\x02\x03",

            "We haven't heard anything\x01",
            "in two days...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xB,
        (
            "Hmm... Well, he does tend to get \x01",
            "completely wrapped up when he's\x01",
            "looking for the next big story...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xB,
        (
            "...but given how close we are to a state\x01",
            "of martial law, I don't much like that\x01",
            "he hasn't contacted us, either.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #219
        0xB,
        "Hmm...?\x02",
    )

    CloseMessageWindow()

    def lambda_71B2():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_71B2)
    OP_6D(-56640, 0, 63970, 1500)

    ChrTalk(    #220
        0xA,
        "#151FOh, hi, guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x101,
        "#006F#5PHello, Dorothy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x102,
        "#010F#5PPardon us...\x02",
    )

    CloseMessageWindow()

    def lambda_7220():

        label("loc_7220")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_7220")

    QueueWorkItem2(0xA, 1, lambda_7220)

    def lambda_7231():

        label("loc_7231")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_7231")

    QueueWorkItem2(0x101, 1, lambda_7231)

    def lambda_7242():

        label("loc_7242")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_7242")

    QueueWorkItem2(0x102, 1, lambda_7242)

    def lambda_7253():
        OP_6D(-55080, 0, 62180, 2000)
        ExitThread()

    QueueWorkItem(0x108, 3, lambda_7253)

    def lambda_726B():
        OP_8E(0xFE, 0xFFFF2AF4, 0x0, 0xF532, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_726B)
    Sleep(300)

    def lambda_728B():
        OP_8E(0xFE, 0xFFFF25F4, 0x0, 0xF4A6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_728B)
    Sleep(300)
    OP_8E(0x108, 0xFFFF16E0, 0x0, 0xFC57, 0xBB8, 0x0)

    def lambda_72BF():
        OP_8E(0xFE, 0xFFFF277A, 0x0, 0xF9F6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_72BF)
    WaitChrThread(0x108, 0x2)
    OP_8C(0x108, 180, 400)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74B6")
    OP_A2(0x67F)

    ChrTalk(    #223
        0xB,
        "Hey, it's the tournament champions...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xB,
        (
            "I'm the editor-in-chief of\x01",
            "the Liberl News.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xB,
        (
            "Nial and Dorothy have told me\x01",
            "quite a bit about the two of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xB,
        (
            "Estelle and Joshua, of the\x01",
            "Bracer Guild, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x101,
        "#008F#6PGood afternoon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x102,
        (
            "#010F#6PIt's a pleasure to meet you.\x02\x03",

            "I've always enjoyed your magazine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xB,
        (
            "Ha ha ha... Well, that's always\x01",
            "good to hear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0xB,
        (
            "Weren't you two doing something\x01",
            "for Nial?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x101,
        "#501FOh, uh, yes...\x02",
    )

    CloseMessageWindow()
    Jump("loc_7536")

    label("loc_74B6")


    ChrTalk(    #232
        0xB,
        (
            "Oh, it's you...\x01",
            "Perfect timing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x101,
        (
            "#006FGood afternoon...\x02\x03",

            "We're here to talk to Nial, but\x01",
            "I'm guessing he's not around?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7536")


    ChrTalk(    #234
        0xB,
        (
            "That's what we were just\x01",
            "talking about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xB,
        (
            "Actually, Nial hasn't shown up\x01",
            "here today or yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xB,
        "No word from him or anything.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x101,
        "#580FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x102,
        (
            "#012FYesterday or today...?\x02\x03",

            "We spoke with him in the\x01",
            "evening, two days ago.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xA, 0xFF)
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #239
        0xA,
        "#6P#153FR-Really...?!\x02",
    )

    CloseMessageWindow()

    def lambda_7653():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7653)
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(    #240
        0x101,
        (
            "#007FWhat do you mean 'really'?!\x01",
            "YOU gave us the message to\x01",
            "meet him, for Aidios' sake!\x02\x03",

            "#002FWe came here to talk to him\x01",
            "after the semifinals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xA,
        (
            "#6P#151FOh, right...\x01",
            "Now that you mention it...\x02\x03",

            "#154FSo, did he say anything to you?\x02\x03",

            "Like where he was going...?\x02",
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
            "[Out researching an article.]\x01",       # 0
            "[Someone had just called him.]\x01",      # 1
            "[We went out to dinner.]\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_781A"),
        (1, "loc_78D1"),
        (2, "loc_793F"),
        (SWITCH_DEFAULT, "loc_79DE"),
    )


    label("loc_781A")


    ChrTalk(    #242
        0x102,
        (
            "#012FHe might have gone to do some\x01",
            "research for an article...\x02\x03",

            "But I can say that he got a call\x01",
            "from someone, then he said he\x01",
            "had to leave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x101,
        "#505FYeah, I remember...\x02",
    )

    CloseMessageWindow()
    OP_2B(0x4B, 0x1)
    Jump("loc_79DE")

    label("loc_78D1")


    ChrTalk(    #244
        0x102,
        (
            "#012FRight. I remember what happened.\x02\x03",

            "He got a call from someone,\x01",
            "then he said he had to leave.\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x4B, 0x2)
    Jump("loc_79DE")

    label("loc_793F")


    ChrTalk(    #245
        0x102,
        (
            "#017FNo, that was three days ago.\x02\x03",

            "#012FTwo days ago, though, someone\x01",
            "called him up, and then he\x01",
            "said he had to leave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x101,
        "#505FWas that how it went?\x02",
    )

    CloseMessageWindow()
    Jump("loc_79DE")

    label("loc_79DE")


    ChrTalk(    #247
        0xB,
        "Are you serious?\x02",
    )

    CloseMessageWindow()

    def lambda_79FA():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_79FA)
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(    #248
        0x102,
        (
            "#012FYes.\x02\x03",

            "We haven't seen hide nor\x01",
            "hair of him since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xA,
        (
            "#6P#152FOh, noooo!\x01",
            "I can't believe Nial's dead!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(    #250
        0x101,
        (
            "#509FWha...\x01",
            "Who said he was dead?!\x02\x03",

            "#007FToday's when all the airliner\x01",
            "traffic gets shut down...\x02\x03",

            "#505FEverything was normal yesterday,\x01",
            "though...so maybe he went to\x01",
            "another province?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xB,
        (
            "I already inquired with the\x01",
            "landing port's passenger registry,\x01",
            "and there was no sign of him.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7BA5():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7BA5)

    def lambda_7BB3():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7BB3)

    ChrTalk(    #252
        0xB,
        (
            "So, I figure he has to still\x01",
            "be somewhere in town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x108,
        (
            "#074FHmmmm...\x02\x03",

            "#070FYou two were the last ones to\x01",
            "see this reporter fellow...\x02\x03",

            "Weren't you talking to him about\x01",
            "something for a news article?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7C8C():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7C8C)

    def lambda_7C9A():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7C9A)
    TurnDirection(0x101, 0x108, 400)

    ChrTalk(    #254
        0x101,
        "#004F#4PHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x108,
        (
            "#070FThese are the times we live in.\x02\x03",

            "Controlling the media is a big\x01",
            "deal for the military.\x02\x03",

            "What do you think, Chief?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xB,
        "I certainly can't argue with that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xB,
        (
            "Particularly in the case of the\x01",
            "Intelligence Division. They monitor\x01",
            "and censor everything we do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xB,
        (
            "You wouldn't believe how\x01",
            "frustrating it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x108,
        (
            "#074FWhich means that you can't get\x01",
            "much information for your stories.\x02\x03",

            "But it's in a reporter's nature\x01",
            "to want to get as much as possible\x01",
            "into the hands of the readers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x102,
        (
            "#010F#4PI see...\x02\x03",

            "So he went to check out a new subject\x01",
            "that the Intelligence Division hasn't\x01",
            "started censoring yet...\x02\x03",

            "What was the last thing\x01",
            "he told us about...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x101,
        "#004F#4PI think it was about...\x02",
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
            "[The tournament winners.]\x01",                         # 0
            "[An arranged marriage for Princess Klaudia.]\x01",      # 1
            "[Julia and Kanone's history.]\x01",                     # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8031"),
        (1, "loc_81FB"),
        (2, "loc_824E"),
        (SWITCH_DEFAULT, "loc_8455"),
    )


    label("loc_8031")


    ChrTalk(    #262
        0x108,
        (
            "#072FThat's the story he was working\x01",
            "on, but we talked to him the day\x01",
            "before the championship bout.\x02\x03",

            "Maybe he was short on material.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x101,
        (
            "#505F#4POh, okay...\x02\x03",

            "It looked like those Special Ops\x01",
            "guys were going to win...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x102,
        (
            "#015F#4PI think I have an idea.\x02\x03",

            "#012FNial seemed particularly interested in the\x01",
            "marriage prospect thing for the princess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x101,
        "#580F#4PHey, yeah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x108,
        (
            "#073FAnd the duke mentioned something\x01",
            "about it at the dinner party...\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x4B, 0x1)
    Jump("loc_8455")

    label("loc_81FB")


    ChrTalk(    #267
        0x108,
        (
            "#073FAnd the duke mentioned something\x01",
            "about it at the dinner party...\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x4B, 0x2)
    Jump("loc_8455")

    label("loc_824E")


    ChrTalk(    #268
        0x108,
        (
            "#073FColonel Richard's aide-de-camp\x01",
            "and a woman in the Guardsmen were\x01",
            "rivals in military academy...\x02\x03",

            "#070FWhich is interesting, but wouldn't\x01",
            "the Intelligence Division have\x01",
            "already made that connection?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x101,
        (
            "#007F#4POops, yeah... So he probably couldn't\x01",
            "print a story about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x102,
        (
            "#015F#4PI think I have an idea.\x02\x03",

            "#012FNial seemed particularly interested in the\x01",
            "marriage prospect thing for the princess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x101,
        "#580F#4PHey, yeah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x108,
        (
            "#073FAnd the duke mentioned something\x01",
            "about it at the dinner party...\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x4B, 0x1)
    Jump("loc_8455")

    label("loc_8455")


    ChrTalk(    #273
        0xB,
        "Oh, Nial told you about that too?\x02",
    )

    CloseMessageWindow()

    def lambda_8482():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8482)

    def lambda_8490():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8490)

    ChrTalk(    #274
        0xB,
        "It'd make a hell of a story if it's true.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0xB,
        (
            "He mentioned having to get some\x01",
            "evidence at any cost...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x108,
        (
            "#073FHow did a reporter like Nial even\x01",
            "learn about something like that?\x02\x03",

            "I'd have thought that something\x01",
            "like that would be known only\x01",
            "to the royal family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0xA,
        (
            "#6P#150FWell, he did say he's friends\x01",
            "with someone who works in the\x01",
            "Erbe Royal Villa...\x02\x03",

            "#151FCompletely off the record, but\x01",
            "the terrorists are supposedly\x01",
            "after the princess.\x02\x03",

            "So she's secretly staying in\x01",
            "the villa for her own safety.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_86E5():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_86E5)

    def lambda_86F3():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_86F3)

    def lambda_8701():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_8701)

    ChrTalk(    #278
        0x101,
        "#005F...I knew it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x108,
        "#070FHa...and the veil is lifted.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0x102,
        (
            "#013FMaybe the person he was talking\x01",
            "to was his friend in the villa...\x02\x03",

            "...which would mean that Nial's\x01",
            "probably there, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0xB,
        "You don't say...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xB,
        (
            "Well, if I know Nial, he probably\x01",
            "tried to worm his way in for an\x01",
            "interview with the princess...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0xB,
        (
            "And if the soldiers saw him, they'd\x01",
            "have arrested him on the spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xA,
        "#6P#152FNooooo! Nial's a goner!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x101,
        (
            "#007FWhy do you keep coming\x01",
            "back to that...?\x02\x03",

            "#002FBut if he HAS been arrested,\x01",
            "getting him out isn't going\x01",
            "to be easy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0x102,
        (
            "#012FYeah...\x02\x03",

            "I'm betting that he and Princess\x01",
            "Klaudia are pretty much in the\x01",
            "same situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0xB,
        (
            "What exactly do you\x01",
            "people know...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xB,
        (
            "Do you have inside information\x01",
            "about what's going on in this\x01",
            "city...in all of Liberl?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8A1D():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8A1D)
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(    #289
        0x101,
        (
            "#007FSorry...but we really can't\x01",
            "talk about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0x102,
        (
            "#012FJust let the Bracer Guild take\x01",
            "care of Nial.\x02\x03",

            "If he has been arrested, we'll\x01",
            "see to it that he's released.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0xB,
        "All right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xB,
        "Please do whatever you can.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0xA,
        (
            "#6P#154FPlease, you guys!\x02\x03",

            "You gotta bring Nial back!!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(    #294
        0x101,
        "#006FLeave it to us!\x02",
    )

    CloseMessageWindow()
    OP_28(0x4B, 0x1, 0x200)
    OP_43(0xA, 0x0, 0x0, 0x2)
    EventEnd(0x0)
    Return()

    # Function_11_6FE2 end

    def Function_12_8B76(): pass

    label("Function_12_8B76")

    ClearMapFlags(0x10000000)
    EventBegin(0x0)
    SetChrFlags(0x19, 0x80)
    OP_6D(-53570, 0, 62700, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(1650, 0)
    OP_6C(58000, 0)
    OP_6E(493, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -54290, 0, 62760, 109)
    SetChrPos(0xA, -60220, 0, 62930, 197)
    OP_4A(0xA, 255)
    SetChrChipByIndex(0xA, 35)
    OP_43(0x101, 0x0, 0x0, 0xD)
    Sleep(1000)

    ChrTalk(    #295
        0x9,
        (
            "#6P#142FDamn...\x01",
            "Looks like it's started!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8C39():
        OP_6D(-56060, 0, 62820, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_8C39)
    OP_8C(0x9, 289, 400)
    OP_8E(0x9, 0xFFFF2298, 0x0, 0xF5A0, 0xBB8, 0x0)
    TurnDirection(0x9, 0xA, 400)
    WaitChrThread(0x0, 0x1)

    ChrTalk(    #296
        0x9,
        (
            "#144F#4PLet's go, Dorothy!\x02\x03",

            "We've got to get a good\x01",
            "spot to watch!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0xA, 0x9, 400)

    ChrTalk(    #297
        0xA,
        (
            "#152FW-Wait!\x02\x03",

            "Let me set up the exposure quartz!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0xB,
        "Hey, what's going on?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xB,
        (
            "You haven't shown up in\x01",
            "three days, and...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 109, 600)

    ChrTalk(    #300
        0x9,
        (
            "#144FBig story!\x02\x03",

            "Biggest in the history of\x01",
            "the Liberl News!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4240   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_8B76 end

    def Function_13_8DAA(): pass

    label("Function_13_8DAA")

    OP_22(0xB5, 0x0, 0x64)
    Sleep(2500)
    OP_22(0xB5, 0x0, 0x64)
    Sleep(2500)
    OP_22(0xB5, 0x0, 0x64)
    Sleep(2500)
    OP_22(0xB5, 0x0, 0x64)
    Sleep(2500)
    OP_22(0xB5, 0x0, 0x64)
    Sleep(2500)
    OP_22(0xB5, 0x0, 0x64)
    Return()

    # Function_13_8DAA end

    def Function_14_8DE2(): pass

    label("Function_14_8DE2")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #301
        (
            "\x07\x05The Baral Coffee House's specialty!\x01",
            "[Chef's Curry] - 1000 mira\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #302
        (
            "\x07\x05Try our hot curry, cooked to perfection\x01",
            "with our secret spices!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_14_8DE2 end

    def Function_15_8E98(): pass

    label("Function_15_8E98")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #303
        (
            "\x07\x05- Menu -\x01",
            "Mixed Cocktail    750 mira\x01",
            "Refreshing Pie    450 mira\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #304
        (
            "\x07\x05- Chef's Recommendations -\x01",
            "Bouillabaisse     1000 mira\x01\x01\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_15_8E98 end

    SaveToFile()

Try(main)
