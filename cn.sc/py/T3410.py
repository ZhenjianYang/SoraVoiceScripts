from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3410   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3410.x',
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '迪尔队长',                             # 9
        '塔尔瓦托副队长',                       # 10
        '黛米',                                 # 11
        '桑吉特',                               # 12
        '塔丽娅',                               # 13
        '士兵维恩',                             # 14
        '利瓦尔牧师',                           # 15
        '士兵埃克托尔',                         # 16
        '安敦',                                 # 17
        '安敦',                                 # 18
        '安敦',                                 # 19
        '安敦',                                 # 20
        '利库斯',                               # 21
        '安敦',                                 # 22
        '安敦',                                 # 23
        '安敦',                                 # 24
        '安敦',                                 # 25
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
        'ED6_DT07/CH01310 ._CH',             # 00
        'ED6_DT07/CH01300 ._CH',             # 01
        'ED6_DT07/CH01350 ._CH',             # 02
        'ED6_DT07/CH01520 ._CH',             # 03
        'ED6_DT07/CH01180 ._CH',             # 04
        'ED6_DT07/CH01670 ._CH',             # 05
        'ED6_DT07/CH01040 ._CH',             # 06
        'ED6_DT07/CH01143 ._CH',             # 07
        'ED6_DT26/CH20255 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH01310P._CP',             # 00
        'ED6_DT07/CH01300P._CP',             # 01
        'ED6_DT07/CH01350P._CP',             # 02
        'ED6_DT07/CH01520P._CP',             # 03
        'ED6_DT07/CH01180P._CP',             # 04
        'ED6_DT07/CH01670P._CP',             # 05
        'ED6_DT07/CH01040P._CP',             # 06
        'ED6_DT07/CH01143P._CP',             # 07
        'ED6_DT26/CH20255P._CP',             # 08
    )

    DeclNpc(
        X                   = 111940,
        Z                   = 0,
        Y                   = 22150,
        Direction           = 283,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 17500,
        Z                   = 0,
        Y                   = 2380,
        Direction           = 180,
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
        X                   = 61040,
        Z                   = 0,
        Y                   = -24890,
        Direction           = 265,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 54970,
        Z                   = 0,
        Y                   = -21440,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 89560,
        Z                   = 0,
        Y                   = -22370,
        Direction           = 98,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 6790,
        Z                   = 0,
        Y                   = 2810,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 77860,
        Z                   = 0,
        Y                   = 26210,
        Direction           = 180,
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
        X                   = 2190,
        Z                   = 0,
        Y                   = 2570,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 25320,
        Z                   = 4000,
        Y                   = 85000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0xF4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 25320,
        Z                   = 4000,
        Y                   = 85000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0xF4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 25120,
        Z                   = 4000,
        Y                   = 83900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x88,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 25120,
        Z                   = 4000,
        Y                   = 84740,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x88,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 26560,
        Z                   = 4700,
        Y                   = 83080,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 22030,
        Z                   = 4000,
        Y                   = 83790,
        Direction           = 248,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 25000,
        Z                   = 4000,
        Y                   = 83850,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 25100,
        Z                   = 4000,
        Y                   = 84740,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 25000,
        Z                   = 4000,
        Y                   = 84340,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 109850,
        TriggerZ            = 0,
        TriggerY            = 21800,
        TriggerRange        = 1000,
        ActorX              = 111940,
        ActorZ              = 1500,
        ActorY              = 22150,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 91680,
        TriggerZ            = 0,
        TriggerY            = -22240,
        TriggerRange        = 1000,
        ActorX              = 89560,
        ActorZ              = 1500,
        ActorY              = -22370,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 6760,
        TriggerZ            = 0,
        TriggerY            = 900,
        TriggerRange        = 1000,
        ActorX              = 6790,
        ActorZ              = 1500,
        ActorY              = 2810,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 25170,
        TriggerZ            = 4000,
        TriggerY            = 83960,
        TriggerRange        = 1000,
        ActorX              = 25170,
        ActorZ              = 4500,
        ActorY              = 83960,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3A2",          # 00, 0
        "Function_1_812",          # 01, 1
        "Function_2_8E5",          # 02, 2
        "Function_3_909",          # 03, 3
        "Function_4_92D",          # 04, 4
        "Function_5_951",          # 05, 5
        "Function_6_975",          # 06, 6
        "Function_7_9D6",          # 07, 7
        "Function_8_9DB",          # 08, 8
        "Function_9_1157",         # 09, 9
        "Function_10_115C",        # 0A, 10
        "Function_11_18AB",        # 0B, 11
        "Function_12_214D",        # 0C, 12
        "Function_13_2152",        # 0D, 13
        "Function_14_28B8",        # 0E, 14
        "Function_15_2F6D",        # 0F, 15
        "Function_16_378E",        # 10, 16
        "Function_17_3B8C",        # 11, 17
        "Function_18_3D56",        # 12, 18
        "Function_19_3DE2",        # 13, 19
        "Function_20_3DE7",        # 14, 20
        "Function_21_4031",        # 15, 21
        "Function_22_428C",        # 16, 22
        "Function_23_47A5",        # 17, 23
        "Function_24_4C17",        # 18, 24
        "Function_25_52F9",        # 19, 25
        "Function_26_5739",        # 1A, 26
        "Function_27_57A1",        # 1B, 27
        "Function_28_57ED",        # 1C, 28
        "Function_29_5886",        # 1D, 29
    )


    def Function_0_3A2(): pass

    label("Function_0_3A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3EF")
    SetChrFlags(0xE, 0x80)
    SetChrPos(0x9, 110750, 0, 24170, 197)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DB")
    SetChrPos(0xA, 58340, 0, -22400, 90)
    Jump("loc_3EC")

    label("loc_3DB")

    SetChrPos(0xA, 94780, 0, -22050, 270)

    label("loc_3EC")

    Jump("loc_811")

    label("loc_3EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_427")
    SetChrPos(0x9, 4950, 0, -2820, 45)
    OP_43(0x9, 0x0, 0x0, 0x4)
    SetChrPos(0xA, 58340, 0, -22400, 90)
    SetChrFlags(0xE, 0x80)
    Jump("loc_811")

    label("loc_427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_45F")
    SetChrPos(0x9, 4950, 0, -2820, 45)
    OP_43(0x9, 0x0, 0x0, 0x4)
    SetChrPos(0xA, 94780, 0, -22050, 270)
    SetChrFlags(0xE, 0x80)
    Jump("loc_811")

    label("loc_45F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_49C")
    SetChrPos(0x9, 4950, 0, -2820, 45)
    OP_43(0x9, 0x0, 0x0, 0x4)
    SetChrFlags(0xD, 0x10)
    SetChrPos(0xA, 58340, 0, -22400, 90)
    SetChrFlags(0xE, 0x80)
    Jump("loc_811")

    label("loc_49C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_4D4")
    SetChrPos(0x9, 4950, 0, -2820, 45)
    OP_43(0x9, 0x0, 0x0, 0x4)
    SetChrPos(0xA, 58340, 0, -22400, 90)
    SetChrFlags(0xE, 0x80)
    Jump("loc_811")

    label("loc_4D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_533")
    SetChrPos(0x9, 4950, 0, -2820, 45)
    OP_43(0x9, 0x0, 0x0, 0x4)
    SetChrPos(0xA, 78750, 0, 26210, 270)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0xE, 77860, 0, 26210, 90)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    OP_43(0x15, 0x0, 0x0, 0x6)
    Jump("loc_811")

    label("loc_533")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_630")
    SetChrPos(0x8, 111940, 0, 22150, 0)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0x9, 111940, 0, 23370, 180)
    SetChrFlags(0x9, 0x10)
    SetChrPos(0xF, 77580, 0, 23520, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xD, 6810, 0, 2810, 180)
    SetChrPos(0xA, 79530, 0, 24930, 315)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    OP_51(0x10, 0x2A, (scpexpr(EXPR_PUSH_LONG, 0xAFC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2B, (scpexpr(EXPR_PUSH_LONG, 0x15F90), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2C, (scpexpr(EXPR_PUSH_LONG, 0xFFFEA070), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x11, 0x8)
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x11, 25120, 3500, 83900, 0)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    OP_51(0x16, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_811")

    label("loc_630")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_71B")
    SetChrPos(0x9, 52040, 0, 24880, 75)
    SetChrPos(0xF, 8700, 0, 3240, 344)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xD, 4950, 0, -2820, 45)
    OP_43(0xD, 0x0, 0x0, 0x4)
    OP_43(0xA, 0x0, 0x0, 0x2)
    SetChrPos(0xE, 15400, 0, 1400, 180)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    OP_51(0x10, 0x2A, (scpexpr(EXPR_PUSH_LONG, 0xAFC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2B, (scpexpr(EXPR_PUSH_LONG, 0x15F90), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2C, (scpexpr(EXPR_PUSH_LONG, 0xFFFEA070), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x11, 0x8)
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x11, 25120, 3500, 83900, 0)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    OP_51(0x16, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_811")

    label("loc_71B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 5)), scpexpr(EXPR_END)), "loc_77C")
    SetChrPos(0x9, 51170, 0, 28460, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xD, 4950, 0, -2820, 45)
    OP_43(0xD, 0x0, 0x0, 0x4)
    SetChrPos(0xA, 58330, 0, -22280, 90)
    SetChrPos(0xE, 15400, 0, 1400, 180)
    OP_43(0xE, 0x0, 0x0, 0x5)
    Jump("loc_811")

    label("loc_77C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_7EB")
    SetChrPos(0x9, 51170, 0, 28460, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xD, 4950, 0, -2820, 45)
    OP_43(0xD, 0x0, 0x0, 0x4)
    SetChrPos(0xC, 94890, 0, -22010, 90)
    OP_43(0xA, 0x0, 0x0, 0x2)
    OP_43(0xB, 0x0, 0x0, 0x3)
    SetChrPos(0xE, 15400, 0, 1400, 180)
    OP_43(0xE, 0x0, 0x0, 0x5)
    Jump("loc_811")

    label("loc_7EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_811")
    OP_43(0xA, 0x0, 0x0, 0x2)
    SetChrPos(0x9, 4950, 0, -2820, 45)
    OP_43(0x9, 0x0, 0x0, 0x4)

    label("loc_811")

    Return()

    # Function_0_3A2 end

    def Function_1_812(): pass

    label("Function_1_812")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82D")
    OP_72(0x5, 0x10)
    OP_6F(0x5, 100)
    Jump("loc_832")

    label("loc_82D")

    OP_1C(0x5, 0x0, 0x1D)

    label("loc_832")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_840")
    OP_64(0x3, 0x1)
    Jump("loc_88B")

    label("loc_840")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_84A")
    Jump("loc_88B")

    label("loc_84A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_858")
    OP_64(0x2, 0x1)
    Jump("loc_88B")

    label("loc_858")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 5)), scpexpr(EXPR_END)), "loc_86A")
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    Jump("loc_88B")

    label("loc_86A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_880")
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    Jump("loc_88B")

    label("loc_880")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_88B")
    OP_64(0x3, 0x1)

    label("loc_88B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_898")
    OP_10(0x13, 0x0)
    Jump("loc_8A8")

    label("loc_898")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 5)), scpexpr(EXPR_END)), "loc_8A5")
    OP_10(0x12, 0x0)
    Jump("loc_8A8")

    label("loc_8A5")

    OP_10(0x13, 0x0)

    label("loc_8A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8C2")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x22), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8D3")
    OP_1B(0x1, 0x0, 0x16)

    label("loc_8D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8E4")
    OP_1B(0x0, 0x0, 0x17)

    label("loc_8E4")

    Return()

    # Function_1_812 end

    def Function_2_8E5(): pass

    label("Function_2_8E5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_908")
    OP_8D(0xFE, 56600, -23980, 64040, -26210, 2000)
    Jump("Function_2_8E5")

    label("loc_908")

    Return()

    # Function_2_8E5 end

    def Function_3_909(): pass

    label("Function_3_909")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_92C")
    OP_8D(0xFE, 58110, -23110, 53730, -21470, 2000)
    Jump("Function_3_909")

    label("loc_92C")

    Return()

    # Function_3_909 end

    def Function_4_92D(): pass

    label("Function_4_92D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_950")
    OP_8D(0xFE, 3140, -1230, 9860, -4460, 2000)
    Jump("Function_4_92D")

    label("loc_950")

    Return()

    # Function_4_92D end

    def Function_5_951(): pass

    label("Function_5_951")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_974")
    OP_8D(0xFE, 14200, 2000, 18960, 180, 2000)
    Jump("Function_5_951")

    label("loc_974")

    Return()

    # Function_5_951 end

    def Function_6_975(): pass

    label("Function_6_975")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_97F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9D5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_8D(0xFE, 22690, 84450, 21020, 83270, 6000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D2")
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9D2")

    Jump("loc_97F")

    label("loc_9D5")

    Return()

    # Function_6_975 end

    def Function_7_9D6(): pass

    label("Function_7_9D6")

    Call(0, 8)
    Return()

    # Function_7_9D6 end

    def Function_8_9DB(): pass

    label("Function_8_9DB")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A16")
    Call(6, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A05")
    OP_A9(0xAC)
    TalkEnd(0xC)
    Return()

    label("loc_A05")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A16")
    TalkEnd(0xC)
    Return()

    label("loc_A16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_AD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A8A")

    ChrTalk(    #0
        0xC,
        (
            "在这种时候\x01",
            "竟然还要品评男人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xC,
        (
            "黛米真没\x01",
            "紧张感啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xC,
        (
            "唉，看来是\x01",
            "从小没教育好……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_AD2")

    label("loc_A8A")


    ChrTalk(    #3
        0xC,
        (
            "在这种时候\x01",
            "竟然还要品评男人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xC,
        (
            "一定是整天\x01",
            "在想着钓金龟婿吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AD2")

    Jump("loc_1153")

    label("loc_AD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_BCA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B79")

    ChrTalk(    #5
        0xC,
        "哎呀，你们是客人？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xC,
        (
            "近来或许因为世道不好，\x01",
            "客人明显少了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xC,
        (
            "床也有富裕，\x01",
            "请好好休息吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xC,
        (
            "特别优惠，\x01",
            "一个人可以使用两个枕头。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_BC7")

    label("loc_B79")


    ChrTalk(    #9
        0xC,
        (
            "近来或许因为世道不好，\x01",
            "客人明显少了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xC,
        (
            "床也有富裕，\x01",
            "请好好休息吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BC7")

    Jump("loc_1153")

    label("loc_BCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_C01")

    ChrTalk(    #11
        0xC,
        (
            "士兵们也没什么休息的\x01",
            "空暇，真不容易……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1153")

    label("loc_C01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_C46")

    ChrTalk(    #12
        0xC,
        "黛米又在偷懒了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xC,
        (
            "说不定很快\x01",
            "就要被炒鱿鱼了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1153")

    label("loc_C46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_C9A")

    ChrTalk(    #14
        0xC,
        (
            "呵呵，今天在这里\x01",
            "住宿的人运气真好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xC,
        (
            "刚刚晾了被褥，\x01",
            "非常暖和的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1153")

    label("loc_C9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_D1F")

    ChrTalk(    #16
        0xC,
        (
            "欢迎光临，\x01",
            "欢迎来到圣海姆门旅馆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xC,
        (
            "最近去亚尔摩温泉的\x01",
            "客人总算增加了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xC,
        (
            "安全宣言发出后，\x01",
            "地震好像也不发生了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1153")

    label("loc_D1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_E06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_D82")

    ChrTalk(    #19
        0xC,
        (
            "今天黛米恨难得地\x01",
            "去做礼拜了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xC,
        (
            "今天来的牧师先生\x01",
            "好像是个相当不错的男人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E03")

    label("loc_D82")


    ChrTalk(    #21
        0xC,
        (
            "今天黛米恨难得地\x01",
            "去做礼拜了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xC,
        (
            "那个女孩儿有这样的信仰心\x01",
            "我觉得我们没有休息的余地……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xC,
        "一定是因为牧师是个好男人。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_E03")

    Jump("loc_1153")

    label("loc_E06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_F15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_E65")

    ChrTalk(    #24
        0xC,
        (
            "只在地震的时候\x01",
            "去祈祷真是失礼啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xC,
        (
            "太自说自话的话\x01",
            "女神就不会生气吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F12")

    label("loc_E65")


    ChrTalk(    #26
        0xC,
        (
            "说起来从大圣堂\x01",
            "来了牧师哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xC,
        (
            "又发生了地震，\x01",
            "要不过一会去祈祷吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xC,
        (
            "不过只在地震的时候\x01",
            "去祈祷是不是太失礼了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xC,
        (
            "如果我是女神的话\x01",
            "一定会让这种人吃天罚的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_F12")

    Jump("loc_1153")

    label("loc_F15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_FE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_F77")

    ChrTalk(    #30
        0xC,
        (
            "善后也基本上弄好了，\x01",
            "我们也重新开始营业了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xC,
        "需要的话就请在这里休息吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_FDD")

    label("loc_F77")


    ChrTalk(    #32
        0xC,
        "哎呀，欢迎。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xC,
        (
            "善后也基本上弄好了，\x01",
            "我们也重新开始营业了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xC,
        "需要的话就请在这里休息吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_FDD")

    Jump("loc_1153")

    label("loc_FE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_109D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1039")

    ChrTalk(    #35
        0xC,
        (
            "堆积着的行李\x01",
            "好像都塌下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xC,
        (
            "因为平常没整理，\x01",
            "就变成这样了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_109A")

    label("loc_1039")


    ChrTalk(    #37
        0xC,
        "是场挺大的地震呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xC,
        (
            "像这种真正的震感\x01",
            "好久没碰见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xC,
        (
            "不管怎样，\x01",
            "先要收拾一下……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_109A")

    Jump("loc_1153")

    label("loc_109D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_1153")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_10F0")

    ChrTalk(    #40
        0xC,
        (
            "吃饭请去\x01",
            "旁边的食堂。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xC,
        (
            "价格公道，\x01",
            "而且味道的评价也很好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1153")

    label("loc_10F0")


    ChrTalk(    #42
        0xC,
        "欢迎来到圣海姆门。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xC,
        (
            "这里是任何人都欢迎的\x01",
            "旅客用投宿设施哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xC,
        (
            "需要的时候\x01",
            "请跟我说。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1153")

    TalkEnd(0xC)
    Return()

    # Function_8_9DB end

    def Function_9_1157(): pass

    label("Function_9_1157")

    Call(0, 10)
    Return()

    # Function_9_1157 end

    def Function_10_115C(): pass

    label("Function_10_115C")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_1275")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_121E")

    ChrTalk(    #45
        0x8,
        (
            "身份不明的红衣士兵和\x01",
            "像机械一样的魔兽群……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x8,
        (
            "现在在的王国中\x01",
            "潜伏着看不见的敌人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x8,
        (
            "就算门不能关闭\x01",
            "我们也不会让他们恣意妄为。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "因为我们是\x01",
            "光荣的王都护盾。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1272")

    label("loc_121E")


    ChrTalk(    #49
        0x8,
        (
            "就算门不能关闭\x01",
            "也绝对不会让阴谋势力恣意妄为。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        (
            "因为我们是\x01",
            "光荣的王都护盾。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1272")

    Jump("loc_18A7")

    label("loc_1275")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_13BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1360")

    ChrTalk(    #51
        0x8,
        (
            "中央工房发明的那东西\x01",
            "使通讯功能恢复了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        (
            "接下来要尽快\x01",
            "恢复门的功能……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x8,
        (
            "那个零力场发生器\x01",
            "还没批量生产吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x8,
        (
            "如果那东西有二、三十个的话\x01",
            "整个哨所的功能都能完全恢复了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        "#1007F（说、说得真轻松～）\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_13B8")

    label("loc_1360")


    ChrTalk(    #56
        0x8,
        (
            "中央工房发明的那东西\x01",
            "使通讯功能恢复了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x8,
        (
            "唔，就不能再多\x01",
            "分配几个那种发生器吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13B8")

    Jump("loc_18A7")

    label("loc_13BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1451")

    ChrTalk(    #58
        0x8,
        (
            "好像有报告说王都\x01",
            "出现了巨大的人形兵器……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x8,
        (
            "到底在开什么玩笑？\x01",
            "怎么可能有那种东西？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x8,
        "等会儿得去向副队长确认一下这事儿的真实性。\x02",
    )

    CloseMessageWindow()
    Jump("loc_18A7")

    label("loc_1451")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_14CE")

    ChrTalk(    #61
        0x8,
        "希德中校担任警备本部的负责人啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x8,
        (
            "在王国军内部\x01",
            "他那卓越的指挥能力是得到公认的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x8,
        "虽然外界不太了解。\x02",
    )

    CloseMessageWindow()
    Jump("loc_18A7")

    label("loc_14CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_1560")

    ChrTalk(    #64
        0x8,
        (
            "签字仪式的会场是艾尔贝离宫的话，\x01",
            "这里的警戒就极为重要了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        (
            "有什么闪失的话\x01",
            "就会成为外国人的笑柄了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        "所以丝毫都不能松懈。\x02",
    )

    CloseMessageWindow()
    Jump("loc_18A7")

    label("loc_1560")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_15CE")

    ChrTalk(    #67
        0x8,
        (
            "关于那场地震，\x01",
            "好像已经发出安全宣言了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x8,
        (
            "虽然还心有余悸，\x01",
            "不过这样的话就能集中精力警戒了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18A7")

    label("loc_15CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_16C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1645")

    ChrTalk(    #69
        0x8,
        (
            "看来那一连串的地震的\x01",
            "问题总算是解决了……不过\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x8,
        (
            "还有很多无法解释的地方。\x01",
            "暂时还不能放松警惕。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16C3")

    label("loc_1645")


    ChrTalk(    #71
        0x8,
        (
            "看来那一连串的地震的\x01",
            "问题总算是解决了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x8,
        (
            "不过实在是\x01",
            "还有很多无法解释的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x8,
        (
            "真是的……\x01",
            "暂时还不能放松警惕。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_16C3")

    Jump("loc_18A7")

    label("loc_16C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_177F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1719")

    ChrTalk(    #74
        0x8,
        (
            "不管怎样我们也\x01",
            "继续警戒。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x8,
        (
            "尽管面对地震\x01",
            "确实是没办法……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_177C")

    label("loc_1719")


    ChrTalk(    #76
        0x8,
        (
            "这次轮到雷斯顿要塞\x01",
            "发生地震了吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x8,
        (
            "地点都在军队的重要设施，\x01",
            "实在无法相信这是偶然的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_177C")

    Jump("loc_18A7")

    label("loc_177F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_181D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 4)), scpexpr(EXPR_END)), "loc_17D1")

    ChrTalk(    #78
        0x8,
        "什么？你们还有事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x8,
        (
            "我不是说了我有工作吗？\x01",
            "不要妨碍我。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_181A")

    label("loc_17D1")


    ChrTalk(    #80
        0x8,
        (
            "关于情况的说明\x01",
            "你们去找塔尔瓦托副队长。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x8,
        "因为我还有紧急的工作。\x02",
    )

    CloseMessageWindow()

    label("loc_181A")

    Jump("loc_18A7")

    label("loc_181D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_18A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_186B")

    ChrTalk(    #82
        0x8,
        "我都说了我在工作。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x8,
        (
            "老缠着我的话\x01",
            "就把你们赶出哨所。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18A7")

    label("loc_186B")


    ChrTalk(    #84
        0x8,
        "你们在搞什么啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x8,
        (
            "抱歉，我在工作。\x01",
            "不要妨碍我。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_18A7")

    TalkEnd(0x8)
    Return()

    # Function_10_115C end

    def Function_11_18AB(): pass

    label("Function_11_18AB")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_19B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_196B")

    ChrTalk(    #86
        0xFE,
        (
            "敌人下一步想要干什么……\x01",
            "实在无法预料。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "现在要紧的是\x01",
            "不能随便行动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "就是说要稳固好防线，\x01",
            "然后看穿敌人的意图。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "当然，敌人也有可能\x01",
            "正希望我们这么做。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_19B5")

    label("loc_196B")


    ChrTalk(    #90
        0xFE,
        (
            "敌人下一步想要干什么……\x01",
            "实在无法预料。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "现在只能先\x01",
            "稳固好防线。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19B5")

    Jump("loc_2149")

    label("loc_19B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1AFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AA6")

    ChrTalk(    #92
        0xFE,
        (
            "通讯机的修复\x01",
            "真是一个久违了的好消息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "在卡西乌斯准将的指挥下，\x01",
            "各地的王国军终于\x01",
            "有组织地开始行动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "虽然现在还处在主力装备\x01",
            "无法使用的困境之下……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "即便如此，努力做到最好也是\x01",
            "我们军人的责任和义务。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1AFA")

    label("loc_1AA6")


    ChrTalk(    #96
        0xFE,
        (
            "通讯机的修复\x01",
            "真是一个久违了的好消息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "整个王国军终于\x01",
            "有组织地开始行动了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AFA")

    Jump("loc_2149")

    label("loc_1AFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1BB0")

    ChrTalk(    #98
        0xFE,
        (
            "为了抓情报部的余党，\x01",
            "这里的部队也被借走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "现在想想，这是情报部为了\x01",
            "在王都举兵而制造的假象吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "能看穿这一点而提前把尤莉亚上尉\x01",
            "叫回来，真不愧是希德中校。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2149")

    label("loc_1BB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_1C1D")

    ChrTalk(    #101
        0xFE,
        (
            "听说雷斯顿要塞\x01",
            "收到了恐吓信。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "虽然不了解内容，\x01",
            "不过真要搞破坏的话\x01",
            "偷偷地进行不就好了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2149")

    label("loc_1C1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_1CB4")

    ChrTalk(    #103
        0xFE,
        (
            "可能是因为签字仪式的关系，\x01",
            "最近能看到很多外国人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "我们的魔鬼队长先生\x01",
            "也快要开足马力了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "在他说话之前我得\x01",
            "赶紧去宣传加强警戒。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2149")

    label("loc_1CB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1D51")

    ChrTalk(    #106
        0xFE,
        (
            "事情一件又一件的，\x01",
            "真是忙乱到极点了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "地震的骚乱刚刚平息，\x01",
            "接着就快要到签字仪式的日子了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "听说接下来要在\x01",
            "艾尔贝离宫设置警备本部了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2149")

    label("loc_1D51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_1E2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1DAA")

    ChrTalk(    #109
        0x9,
        (
            "军队的上层最近\x01",
            "活动得挺积极的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x9,
        (
            "难道是旧情报部的\x01",
            "余党落网了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E2A")

    label("loc_1DAA")


    ChrTalk(    #111
        0x9,
        (
            "似乎中央工房已经发出了\x01",
            "地震终结的宣言。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x9,
        (
            "我们军队的上层也\x01",
            "也发来了相同的通知。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x9,
        (
            "嗯，看来这不是单纯的\x01",
            "自然现象。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1E2A")

    Jump("loc_2149")

    label("loc_1E2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1F00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1EA0")

    ChrTalk(    #114
        0x9,
        (
            "我要让士兵们\x01",
            "继续保持警戒态势。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x9,
        (
            "关于要塞地震的受害情况\x01",
            "等到有明确消息了我会告知你们的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EFD")

    label("loc_1EA0")


    ChrTalk(    #116
        0x9,
        (
            "雷斯顿要塞的受害程度\x01",
            "好像被控制在最低限度了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x9,
        (
            "看来是事先觉察到\x01",
            "会有地震发生了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1EFD")

    Jump("loc_2149")

    label("loc_1F00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1F8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1F43")

    ChrTalk(    #118
        0x9,
        "呼，总算收拾整齐了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x9,
        "真是重体力劳动啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F8A")

    label("loc_1F43")


    ChrTalk(    #120
        0x9,
        (
            "呼～这边\x01",
            "总算也收拾整齐了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x9,
        (
            "那么，我得去其他\x01",
            "岗位看看了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1F8A")

    Jump("loc_2149")

    label("loc_1F8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_20B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1FEA")

    ChrTalk(    #122
        0x9,
        (
            "对了，迪尔队长\x01",
            "好像恨忙哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x9,
        (
            "就算你们问他什么，\x01",
            "也只会被骂回来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20AE")

    label("loc_1FEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 5)), scpexpr(EXPR_END)), "loc_2055")

    ChrTalk(    #124
        0x9,
        (
            "哟，各位游击士。\x01",
            "调查有进展吗？？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x9,
        (
            "我这边也\x01",
            "快要收拾好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x9,
        (
            "傍晚之前\x01",
            "应该能弄好吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20AB")

    label("loc_2055")


    ChrTalk(    #127
        0x9,
        (
            "昨天切斯利看到了\x01",
            "一个奇怪的男人哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x9,
        (
            "他在屋顶收拾，\x01",
            "详细情况你们可以去问他。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20AB")

    OP_A2(0x1)

    label("loc_20AE")

    Jump("loc_2149")

    label("loc_20B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_2149")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2111")

    ChrTalk(    #129
        0x9,
        (
            "登上里面的台阶\x01",
            "就能到达『亚宁堡』的\x01",
            "上层。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x9,
        (
            "来旅游的客人\x01",
            "经常上去的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2149")

    label("loc_2111")


    ChrTalk(    #131
        0x9,
        "哎呀，欢迎。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x9,
        (
            "如果需要设施的说明\x01",
            "请跟我说。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_2149")

    TalkEnd(0x9)
    Return()

    # Function_11_18AB end

    def Function_12_214D(): pass

    label("Function_12_214D")

    Call(0, 13)
    Return()

    # Function_12_214D end

    def Function_13_2152(): pass

    label("Function_13_2152")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_2276")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_220F")

    ChrTalk(    #133
        0xD,
        "最近我常做一个梦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xD,
        (
            "就是世界毁灭了，\x01",
            "只剩下这座哨所。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xD,
        (
            "通讯机不能用的那段时间\x01",
            "确实有那样的感觉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xD,
        (
            "现在如果没有旅客来的话，\x01",
            "想起来还是觉得很可怕。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_2273")

    label("loc_220F")


    ChrTalk(    #137
        0xD,
        (
            "最近常做世界毁灭了，\x01",
            "只剩下这座哨所的梦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xD,
        (
            "现在如果没有旅客来的话，\x01",
            "想起来还是觉得很可怕。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2273")

    Jump("loc_28B4")

    label("loc_2276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_236B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2316")

    ChrTalk(    #139
        0xD,
        (
            "因为现在门也不能锁，\x01",
            "我对通行管理特别用心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xD,
        (
            "你们游击士可以\x01",
            "随意出入，请放心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xD,
        (
            "因为有特别的通知，\x01",
            "好像是卡西乌斯准将的命令。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_2368")

    label("loc_2316")


    ChrTalk(    #142
        0xD,
        (
            "你们游击士\x01",
            "可以自由通行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xD,
        (
            "在卡西乌斯准将的命令下\x01",
            "已经发出那样的通知了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2368")

    Jump("loc_28B4")

    label("loc_236B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_23D3")

    ChrTalk(    #144
        0xD,
        (
            "格兰赛尔亲卫队\x01",
            "和情报部发生过战斗了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xD,
        (
            "原来在王都集中全部的\x01",
            "战斗力就是为了这个啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28B4")

    label("loc_23D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_2435")

    ChrTalk(    #146
        0xD,
        (
            "从昨天起希德中校\x01",
            "好像进入了艾尔贝离宫。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xD,
        (
            "好像要布置\x01",
            "比想象中更为森严的警戒啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28B4")

    label("loc_2435")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_247B")
    TurnDirection(0xD, 0x12F, 400)

    ChrTalk(    #148
        0xD,
        "哟，好可爱的小姑娘。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xD,
        "放松一点好了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xD, 180, 0)
    Jump("loc_28B4")

    label("loc_247B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2531")

    ChrTalk(    #150
        0xD,
        (
            "真是的，前几天的地震\x01",
            "可让我们吃了苦头了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xD,
        (
            "虽然不知道是不是和地震有关\x01",
            "不过周游道的魔兽变得活跃了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xD,
        (
            "有报告说在\x01",
            "艾尔贝离宫附近\x01",
            "出现了大型魔兽，你们要小心哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28B4")

    label("loc_2531")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_25CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_258A")

    ChrTalk(    #153
        0xD,
        (
            "地震的善后工作\x01",
            "也总算结束了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xD,
        (
            "哎呀呀，简直是\x01",
            "一场飞来横祸啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25C8")

    label("loc_258A")


    ChrTalk(    #155
        0xD,
        "呀，欢迎。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xD,
        (
            "现在已经和平常\x01",
            "一样在办理通行手续了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_25C8")

    Jump("loc_28B4")

    label("loc_25CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_26CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2630")

    ChrTalk(    #157
        0xD,
        (
            "唔～偶尔祈祷一次\x01",
            "灵魂得到了安宁的感觉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xD,
        (
            "下次趁休息去参加\x01",
            "大圣堂的礼拜吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26C9")

    label("loc_2630")


    ChrTalk(    #159
        0xD,
        (
            "刚才我去神父先生\x01",
            "那里祈祷了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xD,
        (
            "偶尔祈祷一次\x01",
            "灵魂得到了安宁的感觉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xD,
        (
            "至少应该在地震时\x01",
            "向女神祈祷啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xD,
        (
            "那场地震也一定是\x01",
            "女神的意志。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_26C9")

    Jump("loc_28B4")

    label("loc_26CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_2774")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2731")

    ChrTalk(    #163
        0xD,
        (
            "牧师先生是自己\x01",
            "提出要帮忙的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xD,
        (
            "不愧是牧师先生啊。\x01",
            "虽然年轻，可是很懂道理。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2771")

    label("loc_2731")


    ChrTalk(    #165
        0xD,
        "呼～终于收拾整齐了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xD,
        (
            "这也是拜牧师先生的\x01",
            "帮忙所赐。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_2771")

    Jump("loc_28B4")

    label("loc_2774")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_2808")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_27CD")

    ChrTalk(    #167
        0xD,
        (
            "刚才的地震\x01",
            "摇得挺厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xD,
        (
            "没有人受伤\x01",
            "可以说是不可思议的事了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2805")

    label("loc_27CD")


    ChrTalk(    #169
        0xD,
        "看上去很凌乱吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xD,
        (
            "刚才的地震\x01",
            "摇得挺厉害啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_2805")

    Jump("loc_28B4")

    label("loc_2808")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_28B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2863")

    ChrTalk(    #171
        0xD,
        (
            "诞辰庆典也结束了，\x01",
            "最近游客少了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xD,
        (
            "反正我们这些\x01",
            "士兵算是轻松了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28B4")

    label("loc_2863")


    ChrTalk(    #173
        0xD,
        "欢迎来到圣海姆门。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xD,
        (
            "难得来一趟，\x01",
            "请一定要欣赏一下\x01",
            "『亚宁堡』的英姿。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_28B4")

    TalkEnd(0xD)
    Return()

    # Function_13_2152 end

    def Function_14_28B8(): pass

    label("Function_14_28B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28C9")
    Call(0, 24)
    Return()

    label("loc_28C9")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_29E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2978")

    ChrTalk(    #175
        0xFE,
        (
            "男人的价值\x01",
            "要到紧急时刻才能看出来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        (
            "危难之时能够依靠的\x01",
            "才是货真价实的男人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        (
            "呵呵，这么想的话\x01",
            "现在正是绝好的机会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        "我要好好地品评～\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_29E4")

    label("loc_2978")


    ChrTalk(    #179
        0xFE,
        (
            "危难之时能够依靠的\x01",
            "才是货真价实的男人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "这么想的话\x01",
            "现在正是绝好的机会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        "呵呵，真令人期待啊。\x02",
    )

    CloseMessageWindow()

    label("loc_29E4")

    Jump("loc_2F69")

    label("loc_29E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2A9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A4A")

    ChrTalk(    #182
        0xFE,
        (
            "哎呀，游击士们。\x01",
            "你们是来吃饭的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "我正闲得发慌呢。\x01",
            "呵呵，热烈欢迎㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_2A9A")

    label("loc_2A4A")


    ChrTalk(    #184
        0xFE,
        (
            "感觉～这世道\x01",
            "真是不好混啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "唉，我也想快点\x01",
            "找到一个能依靠的男朋友啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A9A")

    Jump("loc_2F69")

    label("loc_2A9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2AEF")

    ChrTalk(    #186
        0xFE,
        (
            "士兵们说有巨大\x01",
            "人偶袭击了王都……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        (
            "人偶……\x01",
            "比如小熊小狗那种？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F69")

    label("loc_2AEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_2B2B")

    ChrTalk(    #188
        0xFE,
        "好，快要到休息时间了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        "哪儿有好男人呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F69")

    label("loc_2B2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_2B68")

    ChrTalk(    #190
        0xFE,
        (
            "士兵们终于\x01",
            "吃完饭了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        "啊，可把我忙坏了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F69")

    label("loc_2B68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2BE9")

    ChrTalk(    #192
        0xFE,
        (
            "唉，牧师先生也回去了，\x01",
            "真没劲……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        (
            "我当时应该追他到\x01",
            "王都的大圣堂的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        (
            "不过，我也绝不想给\x01",
            "对方添麻烦啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F69")

    label("loc_2BE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_2CAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2C70")

    ChrTalk(    #195
        0xA,
        "唔～我将来的伴侣……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xA,
        (
            "莫非是……\x01",
            "要是牧师先生的话㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xA,
        "哎呀，我该怎么办呢！\x02",
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_A2(0x2)
    Jump("loc_2CA8")

    label("loc_2C70")


    ChrTalk(    #198
        0xA,
        (
            "我的男人运\x01",
            "可不好哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xA,
        (
            "怎样做才能改变\x01",
            "命运呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CA8")

    Jump("loc_2F69")

    label("loc_2CAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_2DB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2D1E")

    ChrTalk(    #200
        0xA,
        (
            "啊，他热心奉献\x01",
            "祈祷的神情真是太棒了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xA,
        (
            "在牧师大人清秀的侧脸上\x01",
            "我能感觉到女神的存在啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DAE")

    label("loc_2D1E")


    ChrTalk(    #202
        0xA,
        (
            "我听说有年轻的牧师在，\x01",
            "今天就来做礼拜了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xA,
        (
            "没想到他不仅不年轻，\x01",
            "而且还相当英俊呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xA,
        (
            "呵呵，要是这种礼拜的话\x01",
            "我每天都能来参加㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_2DAE")

    Jump("loc_2F69")

    label("loc_2DB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_2E88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2E18")

    ChrTalk(    #205
        0xA,
        (
            "我是那种容易迷上别人，\x01",
            "不过不会死缠烂打的类型。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xA,
        (
            "呵呵，这样才能\x01",
            "享受恋爱啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E85")

    label("loc_2E18")


    ChrTalk(    #207
        0xA,
        (
            "唔～真可惜。\x01",
            "明明是个很帅的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xA,
        (
            "不过既然是特别人物那就算了。\x01",
            "我还是放弃他，去找其它的好男人吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_2E85")

    Jump("loc_2F69")

    label("loc_2E88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_2EC9")

    ChrTalk(    #209
        0xA,
        (
            "唉～怎么收拾也\x01",
            "收拾不完。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xA,
        "真是的，讨厌死了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F69")

    label("loc_2EC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_2F69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2F3A")

    ChrTalk(    #211
        0xA,
        (
            "诞辰庆典也结束了，\x01",
            "最近挺闲的～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xA,
        (
            "虽然经营方面出现困难，\x01",
            "不过我能轻松一些，也挺高兴的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F69")

    label("loc_2F3A")


    ChrTalk(    #213
        0xA,
        "欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xA,
        "请随意选择喜欢的座位。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_2F69")

    TalkEnd(0xA)
    Return()

    # Function_14_28B8 end

    def Function_15_2F6D(): pass

    label("Function_15_2F6D")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3130")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",                                  # 0
            "买东西\x01",                                # 1
            "招牌菜『东方火锅·力』　1200米拉\x01",      # 2
            "离开\x01",                                  # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FFC")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0xAD)
    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_2FFC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_310D")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_30D5")
    SubMira(1200)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #215
        "\x06\x07\x02东方火锅·力\x07\x00已经品尝过了。\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x708)
    OP_31(0x1, 0xFD, 0x708)
    OP_31(0x2, 0xFD, 0x708)
    OP_31(0x3, 0xFD, 0x708)
    OP_31(0x4, 0xFD, 0x708)
    OP_31(0x5, 0xFD, 0x708)
    OP_31(0x6, 0xFD, 0x708)
    OP_31(0x7, 0xFD, 0x708)
    OP_31(0x8, 0xFD, 0x708)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30C7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x7)"), scpexpr(EXPR_END)), "loc_309B")
    Jump("loc_30C7")

    label("loc_309B")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #216
        "\x06\x07\x02东方火锅·力\x07\x00的做法已经学会了。\x02",
    )

    CloseMessageWindow()

    label("loc_30C7")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_30FB")

    label("loc_30D5")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #217
        "没有足够的米拉。\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_30FB")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xB)
    Return()

    label("loc_310D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3127")
    FadeToBright(300, 0)
    TalkEnd(0xB)
    Return()

    label("loc_3127")

    FadeToBright(300, 0)

    label("loc_3130")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_31F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31B3")

    ChrTalk(    #218
        0xFE,
        (
            "哟～欢迎光临～\x01",
            "你们能～来真是太好了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        (
            "难得来一趟，\x01",
            "好好享受吧～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        (
            "我们会用 最好的\x01",
            "菜招待你们的～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_31F5")

    label("loc_31B3")


    ChrTalk(    #221
        0xFE,
        (
            "哟～欢迎光临～\x01",
            "你们能～来真是太好了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        (
            "我正闲得\x01",
            "发慌呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31F5")

    Jump("loc_378A")

    label("loc_31F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_32B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_327A")

    ChrTalk(    #223
        0xFE,
        (
            "唉～真没办法～\x01",
            "炉子也不能用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        (
            "还好有炭火式的烤炉，\x01",
            "总算能做菜～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        (
            "果然还是要珍藏\x01",
            "一些旧工具的～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_32B4")

    label("loc_327A")


    ChrTalk(    #226
        0xFE,
        (
            "好久没有用\x01",
            "炭火烹调了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        (
            "这个说不定\x01",
            "又有怪事了～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32B4")

    Jump("loc_378A")

    label("loc_32B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_32FE")

    ChrTalk(    #228
        0xFE,
        (
            "总觉得军队的人\x01",
            "突然变得很慌乱～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        "又要发生什么了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_378A")

    label("loc_32FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_33BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3364")

    ChrTalk(    #230
        0xFE,
        (
            "说起来，地震\x01",
            "已经完全歇下来了啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        (
            "看来中央工房的安全宣言\x01",
            "是有根据的呢～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_33B8")

    label("loc_3364")


    ChrTalk(    #232
        0xFE,
        (
            "谁也不能说绝对\x01",
            "不会再发生地震了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        (
            "所以他们说安全的时候\x01",
            "我也有所怀疑的～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33B8")

    Jump("loc_378A")

    label("loc_33BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_33E3")

    ChrTalk(    #234
        0xFE,
        "呼～终于可以歇口气了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_378A")

    label("loc_33E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_344F")

    ChrTalk(    #235
        0xFE,
        "黛米那家伙……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "工作偷懒，到头来还要\x01",
            "叹气抱怨说没劲～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        (
            "这种话也不能当着\x01",
            "我的面说啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_378A")

    label("loc_344F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_34DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_348E")

    ChrTalk(    #238
        0xFE,
        "真是的，黛米那家伙～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xFE,
        "也该回来了吧～\x02",
    )

    CloseMessageWindow()
    Jump("loc_34D7")

    label("loc_348E")


    ChrTalk(    #240
        0xFE,
        (
            "哟～欢迎光临～\x01",
            "要点菜找我哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xFE,
        (
            "不知道为什么\x01",
            "女服务员不～在。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_34D7")

    Jump("loc_378A")

    label("loc_34DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_35C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3542")

    ChrTalk(    #242
        0xFE,
        (
            "我在这里也\x01",
            "干了很久了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        (
            "不过现在看到顾客吃菜时,\x01",
            "一瞬间心里也还是七上八下的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35C1")

    label("loc_3542")


    ChrTalk(    #244
        0xFE,
        (
            "我在这里也\x01",
            "干了很久了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        (
            "不过现在看到顾客吃菜时,\x01",
            "一瞬间心里也还是七上八下的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0xFE,
        (
            "所以我一直是背对着\x01",
            "客人工作的～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_35C1")

    Jump("loc_378A")

    label("loc_35C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_3607")

    ChrTalk(    #247
        0xFE,
        "哟～话已经说完了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xFE,
        (
            "方便的话\x01",
            "在这儿喝杯茶吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_378A")

    label("loc_3607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_36E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 5)), scpexpr(EXPR_END)), "loc_368E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3644")

    ChrTalk(    #249
        0xFE,
        (
            "哟～欢迎光临～\x01",
            "总算恢复营业了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_368B")

    label("loc_3644")


    ChrTalk(    #250
        0xFE,
        (
            "哟～欢迎光临～\x01",
            "总算恢复营业了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xFE,
        (
            "你们可以尝尝\x01",
            "我的新菜式～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_368B")

    Jump("loc_36E1")

    label("loc_368E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_36AC")

    ChrTalk(    #252
        0xFE,
        "唉～真没办法。\x02",
    )

    CloseMessageWindow()
    Jump("loc_36E1")

    label("loc_36AC")


    ChrTalk(    #253
        0xFE,
        "唉～真没办法。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xFE,
        "不收拾一下都没法营业了～\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_36E1")

    Jump("loc_378A")

    label("loc_36E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_378A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_374C")

    ChrTalk(    #255
        0xB,
        "诞辰庆典之后真闲啊～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xB,
        (
            "因为太闲，\x01",
            "我就开发了新菜式哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xB,
        "请一～定要试试哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_378A")

    label("loc_374C")


    ChrTalk(    #258
        0xB,
        (
            "欢迎光临～\x01",
            "欢迎来到食堂。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0xB,
        "请随意选择喜欢的座位。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_378A")

    TalkEnd(0xB)
    Return()

    # Function_15_2F6D end

    def Function_16_378E(): pass

    label("Function_16_378E")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_38E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_37F0")

    ChrTalk(    #260
        0xFE,
        (
            "那、那个……\x01",
            "我也该回去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        (
            "关于你的烦恼\x01",
            "可以来大圣堂说给我听……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38E3")

    label("loc_37F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_384A")

    ChrTalk(    #262
        0xFE,
        (
            "我就在大圣堂里，\x01",
            "你随时都可以过来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xFE,
        (
            "那么，不好意思，\x01",
            "我也该回去了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38E3")

    label("loc_384A")


    ChrTalk(    #264
        0xFE,
        (
            "你的烦恼\x01",
            "我完全能理解。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xFE,
        (
            "可是，问题永远\x01",
            "是在你自己身上的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0xFE,
        (
            "阻止你和将来的伴侣\x01",
            "相遇的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0xFE,
        (
            "不正是你心中那个\x01",
            "『理想的异性』的幻影吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_38E3")

    Jump("loc_3B88")

    label("loc_38E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_39C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3965")

    ChrTalk(    #268
        0xFE,
        "我会继续为您祈祷。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0xFE,
        (
            "当我们迷失道路时，\x01",
            "请您为我们指引正确的方向……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0xFE,
        (
            "在深远的黑暗中\x01",
            "守护我们……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39C2")

    label("loc_3965")


    ChrTalk(    #271
        0xFE,
        "空之女神啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0xFE,
        (
            "请保佑聚集\x01",
            "在这里的人们……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0xFE,
        (
            "请您在天空之上\x01",
            "永远注视我们……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_39C2")

    Jump("loc_3B88")

    label("loc_39C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_3A61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3A11")

    ChrTalk(    #274
        0xFE,
        "终于收拾好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0xFE,
        (
            "那么，差不多该\x01",
            "真想快点开始礼拜。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A5E")

    label("loc_3A11")


    ChrTalk(    #276
        0xFE,
        (
            "终于收拾\x01",
            "好像结束了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0xFE,
        (
            "不过天可真热啊。\x01",
            "祭司服好像不适合运动。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_3A5E")

    Jump("loc_3B88")

    label("loc_3A61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_3AD3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3A9E")

    ChrTalk(    #278
        0xFE,
        (
            "不过都给\x01",
            "弄乱了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xFE,
        (
            "我也来\x01",
            "帮忙吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AD0")

    label("loc_3A9E")


    ChrTalk(    #280
        0xFE,
        (
            "好像没有人\x01",
            "受伤。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0xFE,
        "真是不幸中之大幸。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_3AD0")

    Jump("loc_3B88")

    label("loc_3AD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_3B88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3B22")

    ChrTalk(    #282
        0xE,
        (
            "各位士兵都在\x01",
            "努力工作呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0xE,
        (
            "我就在这里\x01",
            "再等一会儿吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B88")

    label("loc_3B22")


    ChrTalk(    #284
        0xE,
        (
            "我是从大圣堂来\x01",
            "为士兵们祈祷的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0xE,
        (
            "不过还没有\x01",
            "人过来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xE,
        (
            "嗯，看来大家\x01",
            "都在努力工作呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_3B88")

    TalkEnd(0xE)
    Return()

    # Function_16_378E end

    def Function_17_3B8C(): pass

    label("Function_17_3B8C")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_3BD2")

    ChrTalk(    #287
        0xFE,
        (
            "来礼拜的人\x01",
            "比平时多啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xFE,
        "是不是因为发生了地震？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D52")

    label("loc_3BD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_3CA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3C24")

    ChrTalk(    #289
        0xFE,
        "呼～终于结束了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0xFE,
        (
            "好，牧师先生也来了，\x01",
            "我去做个礼拜吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C9D")

    label("loc_3C24")


    ChrTalk(    #291
        0xFE,
        "呼～终于结束了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xFE,
        (
            "因为大家合力的关系，\x01",
            "善后工作比预计的早完成了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0xFE,
        (
            "好，牧师先生也来了，\x01",
            "我去做个礼拜吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_3C9D")

    Jump("loc_3D52")

    label("loc_3CA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_3D52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3D0B")

    ChrTalk(    #294
        0xFE,
        (
            "我的工作岗位是在外面，\x01",
            "不过现在是紧急情况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xFE,
        (
            "所以就离开工作岗位\x01",
            "到里面来帮忙了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D52")

    label("loc_3D0B")


    ChrTalk(    #296
        0xFE,
        (
            "哨所里到处\x01",
            "都有行李塌下来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0xFE,
        (
            "不收拾好的话\x01",
            "也没法好好警戒。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_3D52")

    TalkEnd(0xF)
    Return()

    # Function_17_3B8C end

    def Function_18_3D56(): pass

    label("Function_18_3D56")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_3DA0")

    ChrTalk(    #298
        0xFE,
        (
            "还是不能在\x01",
            "这种地方浪费人生！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xFE,
        "总、总之要回王都去！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DDE")

    label("loc_3DA0")


    ChrTalk(    #300
        0xFE,
        (
            "不、不能在\x01",
            "这种地方浪费人生！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0xFE,
        "好，赶快回王都去！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_3DDE")

    TalkEnd(0xFE)
    Return()

    # Function_18_3D56 end

    def Function_19_3DE2(): pass

    label("Function_19_3DE2")

    Call(0, 20)
    Return()

    # Function_19_3DE2 end

    def Function_20_3DE7(): pass

    label("Function_20_3DE7")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_3E79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_3E38")

    ChrTalk(    #302
        0x11,
        (
            "还是不能在\x01",
            "这种地方浪费人生！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0x11,
        "总、总之要回王都去！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E76")

    label("loc_3E38")


    ChrTalk(    #304
        0x11,
        (
            "不、不能在\x01",
            "这种地方浪费人生！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0x11,
        "好，赶快回王都去！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_3E76")

    Jump("loc_402D")

    label("loc_3E79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_3F51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_3ECE")

    ChrTalk(    #306
        0x11,
        (
            "这么躺着\x01",
            "总觉得很烦躁。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0x11,
        (
            "我怎能就这样\x01",
            "每天在这里浪费时间。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F4E")

    label("loc_3ECE")


    ChrTalk(    #308
        0x11,
        (
            "总觉得这么躺着\x01",
            "心情就会烦躁。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0x11,
        (
            "难、难道我只能这样\x01",
            "每天待在这里浪费时间吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0x11,
        (
            "不知不觉间一辈子\x01",
            "就过去了，真可怕。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_3F4E")

    Jump("loc_402D")

    label("loc_3F51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_402D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_3F9B")

    ChrTalk(    #311
        0x11,
        "啊，利库斯，告诉我！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0x11,
        (
            "我的存在意义\x01",
            "到底是什么？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_402D")

    label("loc_3F9B")


    ChrTalk(    #313
        0x11,
        (
            "诞辰庆典就失恋……\x01",
            "有地震就差点死……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x11,
        (
            "真悲惨……\x01",
            "我连爬起来的力气也没有了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x11,
        "啊，利库斯，告诉我！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x11,
        (
            "我的存在意义\x01",
            "到底是什么？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_402D")

    TalkEnd(0x11)
    Return()

    # Function_20_3DE7 end

    def Function_21_4031(): pass

    label("Function_21_4031")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_40F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_409F")

    ChrTalk(    #317
        0xFE,
        (
            "冷静一点，安敦。\x01",
            "你着急也不是办法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0xFE,
        (
            "反正不管怎样，\x01",
            "你能恢复精神，我就很高兴了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40F0")

    label("loc_409F")


    ChrTalk(    #319
        0xFE,
        (
            "冷静一点，安敦。\x01",
            "你那么着急也不是办法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0xFE,
        (
            "总之我已经准备\x01",
            "要回王都了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_40F0")

    Jump("loc_4288")

    label("loc_40F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_4190")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_412B")

    ChrTalk(    #321
        0xFE,
        (
            "安敦那家伙好像\x01",
            "也开始感到无聊了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_418D")

    label("loc_412B")


    ChrTalk(    #322
        0xFE,
        (
            "这里的地板不太\x01",
            "适合午睡。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0xFE,
        (
            "还是王城的\x01",
            "空中庭园比较理想。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0xFE,
        (
            "那里的草坪\x01",
            "看上去很软。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_418D")

    Jump("loc_4288")

    label("loc_4190")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_4288")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_4228")

    ChrTalk(    #325
        0xFE,
        (
            "抱歉啊，\x01",
            "阻碍你们走路了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0xFE,
        (
            "时不时就开始思考自我价值\x01",
            "是我的伙伴的臭毛病。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0xFE,
        (
            "不过没关系，过几天\x01",
            "他想腻之后就肯定会恢复正常。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4288")

    label("loc_4228")


    ChrTalk(    #328
        0xFE,
        "安敦…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0xFE,
        (
            "从现在的状况来看，\x01",
            "你的存在意义已经很明确了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0xFE,
        "……对，就是通行的障碍。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_4288")

    TalkEnd(0x14)
    Return()

    # Function_21_4031 end

    def Function_22_428C(): pass

    label("Function_22_428C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43B4")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42E2")

    ChrTalk(    #331
        0x101,
        (
            "#1000F现在没必要去王都啊，\x01",
            "赶快把探听的工作解决吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4396")

    label("loc_42E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4345")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42FF")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_4306")

    label("loc_42FF")

    TurnDirection(0x106, 0x0, 400)

    label("loc_4306")


    ChrTalk(    #332
        0x106,
        (
            "#050F现在没必要去王都啊。\x01",
            "还是尽快把探听的工作解决吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4396")

    label("loc_4345")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_435B")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_4362")

    label("loc_435B")

    TurnDirection(0x103, 0x0, 400)

    label("loc_4362")


    ChrTalk(    #333
        0x103,
        (
            "#027F没必要去王都哦。\x01",
            "还是赶快继续探听工作吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4396")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_44C3")

    label("loc_43B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44C3")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_443B")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43DF")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_43E6")

    label("loc_43DF")

    TurnDirection(0x106, 0x0, 400)

    label("loc_43E6")


    ChrTalk(    #334
        0x106,
        (
            "#050F前面就是格兰赛尔地区了。\x02\x03",

            "现在可没时间去别的地方。\x01",
            "现在还是乖乖回去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44A8")

    label("loc_443B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4451")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_4458")

    label("loc_4451")

    TurnDirection(0x103, 0x0, 400)

    label("loc_4458")


    ChrTalk(    #335
        0x103,
        (
            "#020F前面是格兰赛尔地区了啊。\x02\x03",

            "没时间去其它的地方了，\x01",
            "现在还是乖乖回去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44A8")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_44C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47A4")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_459B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_4531")

    ChrTalk(    #336
        0x108,
        (
            "#070F我记得雾香\x01",
            "已经为我们准备\x01",
            "好了定期船。\x02\x03",

            "我们乘定期船\x01",
            "去王都吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4598")

    label("loc_4531")


    ChrTalk(    #337
        0x108,
        (
            "#070F唔，过了这里就是王都了。\x02\x03",

            "我记得雾香\x01",
            "已经为我们准备\x01",
            "好了定期船。\x02\x03",

            "我们乘定期船\x01",
            "去王都吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_4598")

    Jump("loc_4789")

    label("loc_459B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4695")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45B8")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_45BF")

    label("loc_45B8")

    TurnDirection(0x106, 0x0, 400)

    label("loc_45BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_460D")

    ChrTalk(    #338
        0x106,
        (
            "#050F雾香应该为我们\x01",
            "准备好了船票。\x02\x03",

            "我们还是乘定期船去王都吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4692")

    label("loc_460D")


    ChrTalk(    #339
        0x106,
        (
            "#050F虽然都走到这里了，\x01",
            "不过我们还是乘定期船去王都吧。\x02\x03",

            "我记得雾香已经为\x01",
            "我们准备好了船票。\x02\x03",

            "至少在路途中\x01",
            "应该好好享受一下。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_4692")

    Jump("loc_4789")

    label("loc_4695")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46AB")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_46B2")

    label("loc_46AB")

    TurnDirection(0x103, 0x0, 400)

    label("loc_46B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_4708")

    ChrTalk(    #340
        0x103,
        (
            "#020F雾香小姐应该\x01",
            "已经为我们准备好了船票。\x02\x03",

            "我们还是乘定期船去王都吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4789")

    label("loc_4708")


    ChrTalk(    #341
        0x103,
        (
            "#020F虽然已经到了这里，\x01",
            "不过我们还是乘定期船去王都吧。\x02\x03",

            "雾香小姐特意\x01",
            "为我们准备好了船票。\x02\x03",

            "在路上的时候要\x01",
            "好好享受才对。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_4789")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_47A4")

    Return()

    # Function_22_428C end

    def Function_23_47A5(): pass

    label("Function_23_47A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_48FF")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_480A")

    ChrTalk(    #342
        0x108,
        (
            "#070F喂，前面就是蔡斯地区了。\x02\x03",

            "现在没空去其它的地方，\x01",
            "赶快回去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48E4")

    label("loc_480A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4877")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4827")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_482E")

    label("loc_4827")

    TurnDirection(0x106, 0x0, 400)

    label("loc_482E")


    ChrTalk(    #343
        0x106,
        (
            "#050F这边是蔡斯地区。\x02\x03",

            "没时间去别的地方了。\x01",
            "现在还是乖乖回去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48E4")

    label("loc_4877")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_488D")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_4894")

    label("loc_488D")

    TurnDirection(0x103, 0x0, 400)

    label("loc_4894")


    ChrTalk(    #344
        0x103,
        (
            "#020F过了这里就是蔡斯地区了。\x02\x03",

            "没时间去其它的地方了，\x01",
            "现在还是乖乖回去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48E4")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_48FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_499B")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_494F")

    ChrTalk(    #345
        0x101,
        (
            "#1002F没时间闲逛了。\x01",
            "……要赶快返回协会才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4980")

    label("loc_494F")


    ChrTalk(    #346
        0x109,
        (
            "#1063F没时间闲逛了。\x01",
            "……赶紧去王都协会吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4980")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_499B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C16")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_4A14")

    ChrTalk(    #347
        0x108,
        (
            "#070F虽说徒步移动是修行，\x01",
            "但那样太浪费时间。\x02\x03",

            "要去柏斯的话\x01",
            "还是用定期船比较好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A7E")

    label("loc_4A14")


    ChrTalk(    #348
        0x108,
        (
            "#070F这边是蔡斯地区。\x02\x03",

            "虽说徒步移动是修行，\x01",
            "但那样太浪费时间。\x02\x03",

            "要去柏斯的话\x01",
            "还是用定期船比较好。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_4A7E")

    Jump("loc_4BFB")

    label("loc_4A81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4B45")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A9E")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_4AA5")

    label("loc_4A9E")

    TurnDirection(0x106, 0x0, 400)

    label("loc_4AA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_4AFF")

    ChrTalk(    #349
        0x106,
        (
            "#053F……要走过去\x01",
            "说实话太浪费时间。\x02\x03",

            "#050F要去柏斯\x01",
            "还是去定期船飞船坪吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B42")

    label("loc_4AFF")


    ChrTalk(    #350
        0x106,
        (
            "#050F这边是蔡斯地区。\x02\x03",

            "要去柏斯的话\x01",
            "还是去定期船飞船坪吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_4B42")

    Jump("loc_4BFB")

    label("loc_4B45")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B5B")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_4B62")

    label("loc_4B5B")

    TurnDirection(0x103, 0x0, 400)

    label("loc_4B62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_4BBC")

    ChrTalk(    #351
        0x103,
        (
            "#026F……要走过去\x01",
            "说实话是浪费时间。\x02\x03",

            "#020F要去柏斯\x01",
            "还是去定期船飞船坪吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BFB")

    label("loc_4BBC")


    ChrTalk(    #352
        0x103,
        (
            "#020F这边是蔡斯地区。\x02\x03",

            "要去柏斯\x01",
            "还是去定期船飞船坪吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_4BFB")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_4C16")

    Return()

    # Function_23_47A5 end

    def Function_24_4C17(): pass

    label("Function_24_4C17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C31")
    Call(0, 28)
    FadeToBright(0, 0)

    label("loc_4C31")

    EventBegin(0x0)
    OP_4A(0xA, 255)
    Fade(1000)
    SetChrPos(0x101, 58340, 0, -23470, 0)
    SetChrPos(0xF7, 57170, 0, -23130, 45)
    SetChrPos(0x105, 57830, 0, -24520, 0)
    SetChrPos(0x104, 57040, 0, -24090, 45)
    OP_6D(58120, 0, -22770, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(36000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #353
        0xA,
        "呼～终于收拾好了。\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0xA, 225, 400)

    ChrTalk(    #354
        0xA,
        "咦……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4D3F")

    ChrTalk(    #355
        0x106,
        (
            "#051F#6P你就是黛米吧？\x01",
            "我们是游击士协会的人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D76")

    label("loc_4D3F")


    ChrTalk(    #356
        0x103,
        (
            "#020F#6P你就是黛米小姐吧？\x01",
            "我们是游击士协会的人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D76")


    ChrTalk(    #357
        0x101,
        (
            "#1006F其实，有件事\x01",
            "想要打听一下……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #358
        (
            "\x07\x05向黛米询问了\x01",
            "有关墨镜男子的事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #359
        0xA,
        "哦，是那个人啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0xA,
        (
            "昨天的休息时间\x01",
            "我在２层的走廊和他擦肩而过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0xA,
        (
            "我估计那是他从\x01",
            "屋顶回来的时候……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0x104,
        (
            "#035F和那位士兵的证词一致。\x02\x03",

            "#030F那么，你们除了擦肩而过之外\x01",
            "没有交谈吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0xA,
        "算是打了个招呼吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0xA,
        (
            "然后那个人笑了笑，\x01",
            "回了一声。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0xA,
        (
            "我可被他的\x01",
            "野性感觉给电到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4FF7")

    ChrTalk(    #366
        0x101,
        (
            "#1015F野性……\x01",
            "就是说像这个阿加特一样的感觉？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0x106,
        "#552F#6P怎么说呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #368
        0xA,
        (
            "嗯，感觉比那位\x01",
            "大哥哥还要高。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0xA,
        (
            "虽然外边套着黑色外套，\x01",
            "不过胸口敞开，里面什么也没穿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0xA,
        (
            "还有，两只手\x01",
            "都戴着黑色的手套。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_508D")

    label("loc_4FF7")


    ChrTalk(    #371
        0x103,
        (
            "#026F#6P唔……\x01",
            "人物的形象渐渐浮现出来了。\x02\x03",

            "#020F他穿着什么衣服？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #372
        0xA,
        (
            "黑色套装，\x01",
            "不过胸口敞开，什么也没穿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #373
        0xA,
        (
            "还有，两只手\x01",
            "都戴着黑色的手套。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_508D")


    ChrTalk(    #374
        0x101,
        (
            "#1007F墨镜加黑色套装。\x01",
            "还有黑色的手套？\x02\x03",

            "#1019F很可疑啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0xA,
        (
            "与其说可疑不如说是个\x01",
            "狰狞又充满危险感的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0xA,
        "呵呵，就是说『危险的魅力』？\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xF7, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #377
        0x101,
        (
            "#1016F先、先不说这些……\x02\x03",

            "#1015F擦肩而过又打了招呼，\x01",
            "后来就没见过了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #378
        0xA,
        "嗯，是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #379
        0xA,
        (
            "我追上去\x01",
            "想要套近乎……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0xA,
        "不过在古怪的地方跟丢了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0x101,
        "#1004F古怪的地方……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #382
        0xA,
        (
            "唔～\x01",
            "还是让你们看看比较方便。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_525B():
        OP_6D(56990, 0, -22070, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_525B)
    TurnDirection(0xA, 0xB, 400)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #383
        0xA,
        (
            "#2P我说，桑吉特。\x01",
            "我能出去一下吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0xB, 255)
    TurnDirection(0xB, 0xA, 400)

    ChrTalk(    #384
        0xB,
        "#5P算了～没办法。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0xB,
        "#5P在做准备之前回来啊～\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_4B(0xB, 255)
    Call(0, 25)
    Return()

    # Function_24_4C17 end

    def Function_25_52F9(): pass

    label("Function_25_52F9")

    SetChrPos(0xA, 1580, 4000, 42070, 0)
    SetChrPos(0xF7, 2080, 4000, 40570, 0)
    SetChrPos(0x101, 1080, 4000, 40570, 0)
    SetChrPos(0x105, 2080, 4000, 39570, 0)
    SetChrPos(0x104, 1080, 4000, 39570, 0)
    OP_6D(2020, 4000, 50500, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)

    def lambda_539A():
        OP_94(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_539A)
    Sleep(80)

    def lambda_53B5():
        OP_94(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_53B5)
    Sleep(120)

    def lambda_53D0():
        OP_94(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_53D0)
    Sleep(80)

    def lambda_53EB():
        OP_94(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_53EB)
    Sleep(120)

    def lambda_5406():
        OP_94(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5406)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xA, 0x1)
    OP_8C(0xA, 180, 400)

    ChrTalk(    #386
        0xA,
        (
            "#5P我是在这里和\x01",
            "那个人擦肩而过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #387
        0xA,
        (
            "#5P然后那个人就一直\x01",
            "走到了对面……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #388
        0xA,
        (
            "#5P我为了和他搭讪\x01",
            "又返回了走廊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #389
        0x101,
        "#1002F嗯嗯……\x02",
    )

    CloseMessageWindow()
    OP_43(0xA, 0x0, 0x0, 0x1A)

    def lambda_54BD():

        label("loc_54BD")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_54BD")

    QueueWorkItem2(0x101, 0, lambda_54BD)

    def lambda_54CE():

        label("loc_54CE")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_54CE")

    QueueWorkItem2(0xF7, 0, lambda_54CE)

    def lambda_54DF():

        label("loc_54DF")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_54DF")

    QueueWorkItem2(0x105, 0, lambda_54DF)

    def lambda_54F0():

        label("loc_54F0")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_54F0")

    QueueWorkItem2(0x104, 0, lambda_54F0)
    Sleep(1300)

    def lambda_5506():
        OP_6D(3290, 4000, 40300, 2800)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5506)

    def lambda_551E():
        OP_67(0, 8000, -10000, 2800)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_551E)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x2)
    OP_44(0x101, 0x0)
    OP_44(0xF7, 0x0)
    OP_44(0x104, 0x0)
    OP_44(0x105, 0x0)

    def lambda_5550():
        OP_6D(14530, 4000, 39860, 2800)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5550)

    def lambda_5568():
        OP_67(0, 8000, -10000, 2800)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5568)
    Sleep(2500)
    SetChrPos(0xF7, 3830, 4000, 39090, 90)
    SetChrPos(0x101, 3830, 4000, 40090, 90)
    SetChrPos(0x105, 2830, 4000, 39090, 90)
    SetChrPos(0x104, 2830, 4000, 40090, 90)

    def lambda_55C9():
        OP_90(0xFE, 0x2580, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_55C9)
    Sleep(120)

    def lambda_55E9():
        OP_90(0xFE, 0x2580, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_55E9)
    Sleep(80)

    def lambda_5609():
        OP_90(0xFE, 0x24B8, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5609)
    Sleep(120)

    def lambda_5629():
        OP_90(0xFE, 0x24B8, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5629)
    WaitChrThread(0x105, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #390
        0xA,
        (
            "然后拐了个弯后，\x01",
            "看见那里的门关上了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_567E():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_567E)
    OP_8C(0x105, 180, 400)

    def lambda_5693():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5693)
    OP_8C(0x104, 180, 400)

    ChrTalk(    #391
        0xA,
        (
            "所以我觉得他一定是\x01",
            "从这里出去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #392
        0xA,
        (
            "我觉得那是搭讪的好机会，\x01",
            "就追上去了……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 180, 400)
    FadeToDark(1000, 0, -1)
    OP_8E(0xA, 0x3A98, 0xFA0, 0x8F98, 0x7D0, 0x0)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0xA, 0x80)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T3400   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_25_52F9 end

    def Function_26_5739(): pass

    label("Function_26_5739")


    def lambda_573F():
        OP_8E(0xFE, 0xB68, 0xFA0, 0xC6CA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_573F)
    WaitChrThread(0xA, 0x1)

    def lambda_575F():
        OP_8E(0xFE, 0xAFA, 0xFA0, 0x9BE6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_575F)
    WaitChrThread(0xA, 0x1)

    def lambda_577F():
        OP_8E(0xFE, 0x3B42, 0xFA0, 0x9B3C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_577F)
    WaitChrThread(0xA, 0x1)
    OP_8C(0xA, 270, 400)
    Return()

    # Function_26_5739 end

    def Function_27_57A1(): pass

    label("Function_27_57A1")


    def lambda_57A7():
        OP_8E(0xFE, 0x3A5C, 0xFA0, 0x9696, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_57A7)
    WaitChrThread(0xFE, 0x1)

    def lambda_57C7():
        OP_8E(0xFE, 0x3A98, 0xFA0, 0x8F98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_57C7)
    WaitChrThread(0xFE, 0x1)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    Return()

    # Function_27_57A1 end

    def Function_28_57ED(): pass

    label("Function_28_57ED")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5867"),
        (1, "loc_586D"),
        (SWITCH_DEFAULT, "loc_5873"),
    )


    label("loc_5867")

    OP_A2(0x1200)
    Jump("loc_5873")

    label("loc_586D")

    OP_A2(0x1201)
    Jump("loc_5873")

    label("loc_5873")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_5881")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_5885")

    label("loc_5881")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_5885")

    Return()

    # Function_28_57ED end

    def Function_29_5886(): pass

    label("Function_29_5886")

    TalkBegin(0xFF)
    Sleep(400)
    TalkEnd(0xFF)
    Return()

    # Function_29_5886 end

    SaveToFile()

Try(main)
