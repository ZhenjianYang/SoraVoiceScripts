from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'CWO Dale',                             # 9
        'Warrant Officer Talbot',               # 10
        'Tammy',                                # 11
        'Sanders',                              # 12
        'Talia',                                # 13
        'Private Wayne',                        # 14
        'Bishop Reval',                         # 15
        'Private Hector',                       # 16
        'Anton',                                # 17
        'Anton',                                # 18
        'Anton',                                # 19
        'Anton',                                # 20
        'Ricky',                                # 21
        'Anton',                                # 22
        'Anton',                                # 23
        'Anton',                                # 24
        'Anton',                                # 25
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
        "Function_9_162D",         # 09, 9
        "Function_10_1632",        # 0A, 10
        "Function_11_21FC",        # 0B, 11
        "Function_12_3002",        # 0C, 12
        "Function_13_3007",        # 0D, 13
        "Function_14_3B90",        # 0E, 14
        "Function_15_4520",        # 0F, 15
        "Function_16_504D",        # 10, 16
        "Function_17_56BC",        # 11, 17
        "Function_18_5980",        # 12, 18
        "Function_19_5A7F",        # 13, 19
        "Function_20_5A84",        # 14, 20
        "Function_21_5E41",        # 15, 21
        "Function_22_6190",        # 16, 22
        "Function_23_687D",        # 17, 23
        "Function_24_6E7F",        # 18, 24
        "Function_25_7890",        # 19, 25
        "Function_26_7D4C",        # 1A, 26
        "Function_27_7DB4",        # 1B, 27
        "Function_28_7E00",        # 1C, 28
        "Function_29_7E98",        # 1D, 29
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_B61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE0")

    ChrTalk(    #0
        0xC,
        (
            "To be so obsessed with evaluating\x01",
            "men at a time like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xC,
        (
            "Seems like there's more than one\x01",
            "screw loose in Tammy's head.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xC,
        "*sigh* Where did I go wrong raising her...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_B5E")

    label("loc_AE0")


    ChrTalk(    #3
        0xC,
        (
            "To be so obsessed with evaluating\x01",
            "men at a time like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xC,
        (
            "She'd better be looking at\x01",
            "getting a real great match.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B5E")

    Jump("loc_1629")

    label("loc_B61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_D78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC3")

    ChrTalk(    #5
        0xC,
        "Oh, customers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xC,
        (
            "I don't know if it's because of the state\x01",
            "of the world lately, but we've lost a lot\x01",
            "of business lately...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xC,
        (
            "We've got plenty of open beds,\x01",
            "so relax and enjoy yourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xC,
        (
            "As a special, each guest is welcome to two\x01",
            "pillows. TWO WHOLE PILLOWS. I know such luxury\x01",
            "is hard to comprehend, but there it is.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_D75")

    label("loc_CC3")


    ChrTalk(    #9
        0xC,
        (
            "I don't know if it's because of the state\x01",
            "of the world lately, but we've lost a lot\x01",
            "of business lately...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xC,
        (
            "We've got plenty of open beds,\x01",
            "so relax and enjoy yourselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D75")

    Jump("loc_1629")

    label("loc_D78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_DD7")

    ChrTalk(    #11
        0xC,
        (
            "It seems like the soldiers haven't any time\x01",
            "to rest. It must be pretty rough...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1629")

    label("loc_DD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_E3A")

    ChrTalk(    #12
        0xC,
        "Tammy's skipping work again...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xC,
        "I'd be surprised if some heads didn't fly soon.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1629")

    label("loc_E3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_EBC")

    ChrTalk(    #14
        0xC,
        "Haha, anyone staying here is lucky.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xC,
        (
            "We've just finished drying the mattresses,\x01",
            "so they're wonderfully fluffy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1629")

    label("loc_EBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_FA7")

    ChrTalk(    #16
        0xC,
        "Welcome, this is the Sanktheim Lodge.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xC,
        (
            "Lately, we've finally started to get more\x01",
            "guests heading for Elmo hot springs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xC,
        (
            "A declaration of safety was sent out,\x01",
            "and apparently the earthquakes are over.\x01",
            "Thank Aidios.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1629")

    label("loc_FA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_1108")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1055")

    ChrTalk(    #19
        0xC,
        (
            "Apparently Tammy's at Church. That happens\x01",
            "about as often as...earthquakes. Ha.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xC,
        (
            "Sounds like the priest that came today\x01",
            "is a real good-looking guy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1105")

    label("loc_1055")


    ChrTalk(    #21
        0xC,
        (
            "Apparently Tammy went to service.\x01",
            "That's a rare thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xC,
        (
            "I don't think that girl has that much faith,\x01",
            "to be honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xC,
        "I'm sure the priest must be a handsome man.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1105")

    Jump("loc_1629")

    label("loc_1108")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_12E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_11BB")

    ChrTalk(    #24
        0xC,
        (
            "To only go praying when the earthquakes\x01",
            "hit... Hmph. How rude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xC,
        (
            "If you only go when it's useful to you,\x01",
            "I should think Aidios might be a little\x01",
            "put out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12DF")

    label("loc_11BB")


    ChrTalk(    #26
        0xC,
        (
            "Now that I think about it, there's\x01",
            "a priest visiting from the cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xC,
        (
            "Given the earthquake we had,\x01",
            "maybe I'll go pray later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xC,
        (
            "But, to only go praying when the\x01",
            "earthquakes hit, how rude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xC,
        (
            "If I were the Goddess, I'd probably drop\x01",
            "some heavenly punishment on some heads.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_12DF")

    Jump("loc_1629")

    label("loc_12E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_13EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1365")

    ChrTalk(    #30
        0xC,
        (
            "Cleaning's pretty much done, so\x01",
            "it's time to open for business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xC,
        "If you'd like, rest here before you go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13EC")

    label("loc_1365")


    ChrTalk(    #32
        0xC,
        "Oh, welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xC,
        (
            "Cleaning's pretty much done, so\x01",
            "it's time to open for business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xC,
        "If you'd like, rest here before you go.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_13EC")

    Jump("loc_1629")

    label("loc_13EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_1519")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_146C")

    ChrTalk(    #35
        0xC,
        "All the stored stuff collapsed, apparently.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xC,
        (
            "That's because that stuff is never put\x01",
            "away properly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1516")

    label("loc_146C")


    ChrTalk(    #37
        0xC,
        "It was a pretty big earthquake.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xC,
        (
            "It's been quite a while since\x01",
            "we've had some serious shaking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xC,
        (
            "Anyway, one way or the other,\x01",
            "first I have to clean up...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1516")

    Jump("loc_1629")

    label("loc_1519")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_1629")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_15A8")

    ChrTalk(    #40
        0xC,
        (
            "You should go to the cafeteria\x01",
            "nearby for your meals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xC,
        (
            "They've got fair prices and good food,\x01",
            "is what everyone says.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1629")

    label("loc_15A8")


    ChrTalk(    #42
        0xC,
        "Welcome to Sanktheim Gate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xC,
        "This is a traveler lodge open to anyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xC,
        "If you want to stay here, just talk to me.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1629")

    TalkEnd(0xC)
    Return()

    # Function_8_9DB end

    def Function_9_162D(): pass

    label("Function_9_162D")

    Call(0, 10)
    Return()

    # Function_9_162D end

    def Function_10_1632(): pass

    label("Function_10_1632")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_181C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1772")

    ChrTalk(    #45
        0x8,
        (
            "The untraceable crimson soldiers and\x01",
            "those groups of machine-like monsters...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x8,
        (
            "There are hidden enemies lurking\x01",
            "within the kingdom these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x8,
        (
            "Even if the gate doesn't close, I will\x01",
            "NOT let them do as they please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "We have our own pride as the shield\x01",
            "of the kingdom, after all.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1819")

    label("loc_1772")


    ChrTalk(    #49
        0x8,
        (
            "Even if the gate doesn't close, I will NOT\x01",
            "let those conspiratorial forces do as they\x01",
            "please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        (
            "We have our own pride as the shield\x01",
            "of the kingdom, after all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1819")

    Jump("loc_21F8")

    label("loc_181C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1A34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1985")

    ChrTalk(    #51
        0x8,
        (
            "Thanks to that little invention from the\x01",
            "central factory, our phones are working\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        "Next we really need to get that gate lowered...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x8,
        (
            "Aren't those Zero Generator things being mass\x01",
            "produced?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x8,
        (
            "If we had twenty or thirty of those we could\x01",
            "completely restore the whole guard post.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        "#1007F(T-Talk about unreasonable...)\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1A31")

    label("loc_1985")


    ChrTalk(    #56
        0x8,
        (
            "Thanks to that little invention from the\x01",
            "central factory, our phones are working\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x8,
        (
            "Aren't they going to send out a few more\x01",
            "of those generators or whatever?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A31")

    Jump("loc_21F8")

    label("loc_1A34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1B1F")

    ChrTalk(    #58
        0x8,
        (
            "I've gotten word that a giant construct\x01",
            "weapon appeared in the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x8,
        (
            "That's crazy, though. There's no way\x01",
            "such a thing could exist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x8,
        (
            "I shall have to inquire with my second\x01",
            "in command about the truth of this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21F8")

    label("loc_1B1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_1BE7")

    ChrTalk(    #61
        0x8,
        (
            "So Colonel Cid is in charge\x01",
            "of headquarters, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x8,
        (
            "He's well known within the Royal Army\x01",
            "for his superior command ability.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x8,
        (
            "It's not well known to the general public,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21F8")

    label("loc_1BE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_1CDC")

    ChrTalk(    #64
        0x8,
        (
            "Should the signing ceremony be held at\x01",
            "royal villa, then security here will be\x01",
            "absolutely critical...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        (
            "Should anything go wrong, we'd be\x01",
            "the laughing stock of foreign nations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        "Our performance must be absolutely flawless.\x02",
    )

    CloseMessageWindow()
    Jump("loc_21F8")

    label("loc_1CDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1D99")

    ChrTalk(    #67
        0x8,
        (
            "There's been a declaration of safety regarding\x01",
            "those earthquakes, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x8,
        (
            "Something seems a bit off about it if you\x01",
            "ask me, but at least now we can focus on\x01",
            "security.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21F8")

    label("loc_1D99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_1EFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1E49")

    ChrTalk(    #69
        0x8,
        (
            "It seems like the earthquake issue\x01",
            "has been resolved, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x8,
        (
            "There's too much that we don't know about it all.\x01",
            "We'll need to stay alert for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EF7")

    label("loc_1E49")


    ChrTalk(    #71
        0x8,
        (
            "It seems like the earthquake issue\x01",
            "has been resolved, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x8,
        "Still, there's far too much we don't understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x8,
        "Hmph... We'll need to stay alert for a while.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1EF7")

    Jump("loc_21F8")

    label("loc_1EFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_2022")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1F74")

    ChrTalk(    #74
        0x8,
        (
            "Anyway, we will continue with guarding\x01",
            "this location.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x8,
        "There's no way to fight an earthquake...\x02",
    )

    CloseMessageWindow()
    Jump("loc_201F")

    label("loc_1F74")


    ChrTalk(    #76
        0x8,
        (
            "So this time there was an earthquake\x01",
            "at Leiston Fortress. Hmm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x8,
        (
            "All of them have struck at critical military\x01",
            "facilities. I can't believe that's a coincidence.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_201F")

    Jump("loc_21F8")

    label("loc_2022")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_20FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 4)), scpexpr(EXPR_END)), "loc_208D")

    ChrTalk(    #78
        0x8,
        "Oh, did you still need something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x8,
        (
            "I'm quite busy.\x01",
            "Don't get in the way, please.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20FB")

    label("loc_208D")


    ChrTalk(    #80
        0x8,
        (
            "You can hear an explanation of the\x01",
            "situation from Warrant Officer Talbot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x8,
        "I have urgent work to do.\x02",
    )

    CloseMessageWindow()

    label("loc_20FB")

    Jump("loc_21F8")

    label("loc_20FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_21F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2193")

    ChrTalk(    #82
        0x8,
        "I believe I said I am working.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x8,
        (
            "If you continue to make a nuisance of yourself,\x01",
            "I'll have you removed from the guard post.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21F8")

    label("loc_2193")


    ChrTalk(    #84
        0x8,
        "What do you all want?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x8,
        (
            "Sorry, but I'm very busy right now.\x01",
            "Don't get in the way, please.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_21F8")

    TalkEnd(0x8)
    Return()

    # Function_10_1632 end

    def Function_11_21FC(): pass

    label("Function_11_21FC")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_23AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_231F")

    ChrTalk(    #86
        0xFE,
        (
            "What will the enemy's next target be...\x01",
            "I can't even imagine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "Right now, the essential thing is\x01",
            "to not move for little things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "We need to solidify our defenses and\x01",
            "wait to see how the enemy moves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        "Of course, that could be the enemy's goal itself.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_23AB")

    label("loc_231F")


    ChrTalk(    #90
        0xFE,
        (
            "What will the enemy's next target be...\x01",
            "I can't even imagine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "Right now, we have no choice but to\x01",
            "solidify our defenses and wait.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23AB")

    Jump("loc_2FFE")

    label("loc_23AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_25C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2547")

    ChrTalk(    #92
        0xFE,
        (
            "Restoration of communications is our\x01",
            "first bit of good news in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "Under General Cassius' command, the army\x01",
            "all over the nation is finally acting in an\x01",
            "organized manner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "Our main equipment isn't working and we\x01",
            "have a slew of other issues right now,\x01",
            "so things are kind of bad, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "To serve your best even under trying circumstances\x01",
            "is the duty of the military.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_25C5")

    label("loc_2547")


    ChrTalk(    #96
        0xFE,
        (
            "Restoration of communications is our\x01",
            "first bit of good news in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        "Now the Royal Army can coordinate properly.\x02",
    )

    CloseMessageWindow()

    label("loc_25C5")

    Jump("loc_2FFE")

    label("loc_25C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2715")

    ChrTalk(    #98
        0xFE,
        (
            "In order to capture the remnants of the\x01",
            "Intelligence Division, our troops here\x01",
            "have been dispatched.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "Thinking about it, that may have been just\x01",
            "a diversion on their part so that they could\x01",
            "make a move on the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "To read past that and call in Captain Schwarz,\x01",
            "Colonel Cid isn't one to be underestimated.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FFE")

    label("loc_2715")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_27DE")

    ChrTalk(    #101
        0xFE,
        (
            "Apparently there was a threat\x01",
            "delivered to Leiston Fortress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "I don't know the details, but if they really\x01",
            "intend to take action, then they should do\x01",
            "it a bit less, uh, obviously...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FFE")

    label("loc_27DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_28F9")

    ChrTalk(    #103
        0xFE,
        (
            "Thanks to the signing ceremony, I've started\x01",
            "seeing foreign nationals more often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "It's about time for the energy to hit our\x01",
            "demon commander's engine, I'm thinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "I'd better put the call out for heightened\x01",
            "security before he has the chance to say\x01",
            "anything.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FFE")

    label("loc_28F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2A15")

    ChrTalk(    #106
        0xFE,
        (
            "It's just one thing after another. We're\x01",
            "certainly being kept on our toes here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "The earthquake troubles have just ended,\x01",
            "but now the signing ceremony is coming\x01",
            "up on us, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "Apparently, guard headquarters will be\x01",
            "positioned in the royal villa for now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FFE")

    label("loc_2A15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_2B74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2AAD")

    ChrTalk(    #109
        0x9,
        "The brass seem to be quite active lately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x9,
        (
            "I wonder if the remnants of the old Intelligence\x01",
            "Division finally hit the network.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B71")

    label("loc_2AAD")


    ChrTalk(    #111
        0x9,
        (
            "The central factory sent out a message\x01",
            "that the earthquakes are finished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x9,
        (
            "We've received a similar report\x01",
            "from headquarters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x9,
        (
            "It seems it really wasn't just a\x01",
            "natural phenomenon.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_2B71")

    Jump("loc_2FFE")

    label("loc_2B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_2CC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2C32")

    ChrTalk(    #114
        0x9,
        "We're having the soldiers stay on alert status.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x9,
        (
            "As for the earthquake at the fortress,\x01",
            "we'll wait to announce it until we have\x01",
            "a clear picture of the damage done.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CC1")

    label("loc_2C32")


    ChrTalk(    #116
        0x9,
        (
            "Damage to Leiston Fortress was apparently\x01",
            "kept to a minimum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x9,
        (
            "It seems they were aware of the earthquake\x01",
            "in advance. Imagine that.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_2CC1")

    Jump("loc_2FFE")

    label("loc_2CC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_2D8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2D23")

    ChrTalk(    #118
        0x9,
        "Ahhh, I'm finally done cleaning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x9,
        "That was some seriously hard work.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D87")

    label("loc_2D23")


    ChrTalk(    #120
        0x9,
        "Ahhh, finally finished cleaning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x9,
        (
            "Now, then, time go to check up\x01",
            "on the other sections.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_2D87")

    Jump("loc_2FFE")

    label("loc_2D8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_2F18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2E08")

    ChrTalk(    #122
        0x9,
        "Yeah, the chief is really busy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x9,
        (
            "If you try asking him anything,\x01",
            "I bet he'll get pissed real quick.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F15")

    label("loc_2E08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 5)), scpexpr(EXPR_END)), "loc_2E94")

    ChrTalk(    #124
        0x9,
        "Oh, bracers. How goes the investigation?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x9,
        "We should be finished cleaning soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x9,
        "I'd like to have it done by evening.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F12")

    label("loc_2E94")


    ChrTalk(    #127
        0x9,
        "Yesterday, Chesley said he saw a weird guy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x9,
        (
            "He's cleaning up on the roof, so you\x01",
            "should go ask him for the details.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F12")

    OP_A2(0x1)

    label("loc_2F15")

    Jump("loc_2FFE")

    label("loc_2F18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_2FFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2FA7")

    ChrTalk(    #129
        0x9,
        (
            "If you climb the stairs in the back, you\x01",
            "can reach the top of the Ahnenburg Wall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x9,
        "A lot of touring guests visit it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FFE")

    label("loc_2FA7")


    ChrTalk(    #131
        0x9,
        "Oh, welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x9,
        (
            "Should you need an explanation of facilities here,\x01",
            "just ask.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_2FFE")

    TalkEnd(0x9)
    Return()

    # Function_11_21FC end

    def Function_12_3002(): pass

    label("Function_12_3002")

    Call(0, 13)
    Return()

    # Function_12_3002 end

    def Function_13_3007(): pass

    label("Function_13_3007")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_3202")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_313D")

    ChrTalk(    #133
        0xD,
        "I've been having this reoccurring dream lately...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xD,
        (
            "In it, the whole world's a dead wasteland\x01",
            "except for this guard post.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xD,
        (
            "That's kind of what it was like while\x01",
            "communications were dead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xD,
        (
            "I still get scared whenever I think of how\x01",
            "there are no travelers coming through.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_31FF")

    label("loc_313D")


    ChrTalk(    #137
        0xD,
        (
            "Lately, I've been having a dream where the\x01",
            "whole world's a dead wasteland except for\x01",
            "this guard post.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xD,
        (
            "I still get scared whenever I think of how\x01",
            "there are no travelers coming through.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31FF")

    Jump("loc_3B8C")

    label("loc_3202")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3389")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_330B")

    ChrTalk(    #139
        0xD,
        (
            "We can't shut the gate at the moment,\x01",
            "so managing passage through demands\x01",
            "a lot of attention.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xD,
        "You bracers can pass freely, so don't worry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xD,
        (
            "Those are General Cassius' orders,\x01",
            "and we've received special communiques\x01",
            "to that extent.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_3386")

    label("loc_330B")


    ChrTalk(    #142
        0xD,
        "You bracers are welcome to pass freely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xD,
        (
            "We've received communiques to that extent\x01",
            "under General Cassius' orders.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3386")

    Jump("loc_3B8C")

    label("loc_3389")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_342F")

    ChrTalk(    #144
        0xD,
        (
            "There was a battle between the Royal Guard\x01",
            "and the Intelligence Division in Grancel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xD,
        (
            "So that's why our main forces were\x01",
            "focused on the capital...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B8C")

    label("loc_342F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_34C0")

    ChrTalk(    #146
        0xD,
        (
            "Colonel Cid's been in the royal villa\x01",
            "since yesterday, apparently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xD,
        (
            "Seems like he's imposing stricter\x01",
            "security than expected.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B8C")

    label("loc_34C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_3516")
    TurnDirection(0xD, 0x12F, 400)

    ChrTalk(    #148
        0xD,
        "Oh, what a cute little missy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xD,
        "Enjoy your time here.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xD, 180, 0)
    Jump("loc_3B8C")

    label("loc_3516")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_3654")

    ChrTalk(    #150
        0xD,
        (
            "Man, we got hit bad by that\x01",
            "earthquake a little while ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xD,
        (
            "I don't know if it's related to the earthquakes or\x01",
            "not, but apparently monsters around the scenic\x01",
            "route have become a lot more active. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xD,
        (
            "I've even heard reports that they've seen giant\x01",
            "monsters around the royal villa, so be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B8C")

    label("loc_3654")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_36F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_36BC")

    ChrTalk(    #153
        0xD,
        "Cleaning up after the earthquake is finally done.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xD,
        "Man, oh, man, what a mess.\x02",
    )

    CloseMessageWindow()
    Jump("loc_36F0")

    label("loc_36BC")


    ChrTalk(    #155
        0xD,
        "Hey, welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xD,
        "You can pass on through.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_36F0")

    Jump("loc_3B8C")

    label("loc_36F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_387E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3790")

    ChrTalk(    #157
        0xD,
        (
            "Going and praying on occasion\x01",
            "feels like it calms my soul.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xD,
        (
            "Maybe for my next day off, I should\x01",
            "go join services at the cathedral.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_387B")

    label("loc_3790")


    ChrTalk(    #159
        0xD,
        "I just went off to pray with the priest.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xD,
        "Going and praying really calms my soul sometimes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xD,
        (
            "We should at least pray to Aidios when\x01",
            "there are earthquakes going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xD,
        "Even that earthquake was the will of the Goddess.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_387B")

    Jump("loc_3B8C")

    label("loc_387E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_399E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3923")

    ChrTalk(    #163
        0xD,
        "The priest offered of his own accord to help out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xD,
        (
            "That's just what I'd expect from a holy man.\x01",
            "Even at his young age, he's a good person.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_399B")

    label("loc_3923")


    ChrTalk(    #165
        0xD,
        "*pheeew* FINALLY finished cleaning up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xD,
        (
            "All thanks to the priest helping out.\x01",
            "Talk about holy intervention.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_399B")

    Jump("loc_3B8C")

    label("loc_399E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_3A71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3A0F")

    ChrTalk(    #167
        0xD,
        "That earthquake gave us some serious shaking.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xD,
        "It's almost strange no one was injured.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A6E")

    label("loc_3A0F")


    ChrTalk(    #169
        0xD,
        "It's a real mess, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xD,
        (
            "That earthquake just a bit ago\x01",
            "shook us pretty powerfully.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_3A6E")

    Jump("loc_3B8C")

    label("loc_3A71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_3B8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3B06")

    ChrTalk(    #171
        0xD,
        (
            "The birthday celebrations are over, so there\x01",
            "haven't been many tourists lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xD,
        "Well, that's a boon to us soldiers, mind.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B8C")

    label("loc_3B06")


    ChrTalk(    #173
        0xD,
        "Welcome to the Sanktheim Gate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xD,
        (
            "Since you're here, why not have a good long look\x01",
            "and admire the Ahnenburg Wall as you go.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_3B8C")

    TalkEnd(0xD)
    Return()

    # Function_13_3007 end

    def Function_14_3B90(): pass

    label("Function_14_3B90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3BA1")
    Call(0, 24)
    Return()

    label("loc_3BA1")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_3D51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CB5")

    ChrTalk(    #175
        0xFE,
        (
            "A man's true value is something\x01",
            "you find out in a crisis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        (
            "Someone you can rely on in a pinch\x01",
            "is the real thing, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        (
            "Heehee, in that sense, this situation\x01",
            "is the PERFECT chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "You bet I'm gonna be evaluating me\x01",
            "some FINE men!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_3D4E")

    label("loc_3CB5")


    ChrTalk(    #179
        0xFE,
        (
            "Someone you can rely on in a pinch\x01",
            "is the real thing, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        "In that sense, this is the PERFECT chance now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        "Teehee, this should be fun.\x02",
    )

    CloseMessageWindow()

    label("loc_3D4E")

    Jump("loc_451C")

    label("loc_3D51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3E2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DC2")

    ChrTalk(    #182
        0xFE,
        "Oh, bracers. Come for a meal?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "Thank Aidios. I was so bored I thought\x01",
            "I would die.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_3E29")

    label("loc_3DC2")


    ChrTalk(    #184
        0xFE,
        "Maaan, the world seems messed up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "*siiigh* I wish I could find me\x01",
            "a reliable boyfriend soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E29")

    Jump("loc_451C")

    label("loc_3E2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_3EA1")

    ChrTalk(    #186
        0xFE,
        (
            "A soldier said a giant machine-doll-thingy\x01",
            "attacked the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        "A doll... So, like a giant toy?\x02",
    )

    CloseMessageWindow()
    Jump("loc_451C")

    label("loc_3EA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_3F09")

    ChrTalk(    #188
        0xFE,
        "All right, almost break time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "There's got to be a good man around\x01",
            "here somewhere...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_451C")

    label("loc_3F09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_3F5C")

    ChrTalk(    #190
        0xFE,
        "The soldiers finally just finished eating.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        "Ahh, I was so busy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_451C")

    label("loc_3F5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_401C")

    ChrTalk(    #192
        0xFE,
        (
            "*sigh* That hot priest's gone,\x01",
            "and now it's boring again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        (
            "I should've chased him to Grancel Cathedral,\x01",
            "maybe...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        (
            "Mmmm, I don't want to cause trouble\x01",
            "for him, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_451C")

    label("loc_401C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_410F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_40B1")

    ChrTalk(    #195
        0xA,
        "Hmm, my future spouse...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xA,
        "Maybe that hot priest or something? ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xA,
        "Aaaah, what do I do?!\x02",
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_A2(0x2)
    Jump("loc_410C")

    label("loc_40B1")


    ChrTalk(    #198
        0xA,
        "I have the WORST luck with men.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xA,
        "How do I turn this tragic fate around, I wonder.\x02",
    )

    CloseMessageWindow()

    label("loc_410C")

    Jump("loc_451C")

    label("loc_410F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_42C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_41E4")

    ChrTalk(    #200
        0xA,
        "Ahhh, his face is so perfect as he prays...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xA,
        (
            "I can feel the presence of the Goddess just\x01",
            "shining through him as he prays. I should know,\x01",
            "I stared at him for aaaages as he prayed. Teehee.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42C1")

    label("loc_41E4")


    ChrTalk(    #202
        0xA,
        (
            "I heard there was a young priest here\x01",
            "today, so I came to look, er, pray.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xA,
        (
            "And Sweet Aidios. JACKPOT. He's not just young,\x01",
            "he's also preeetty handsome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xA,
        (
            "Teehee, if he was my priest,\x01",
            "I'd pray every day. ㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_42C1")

    Jump("loc_451C")

    label("loc_42C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_43DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4352")

    ChrTalk(    #205
        0xA,
        "I may fall for guys easy, but I also give up easy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xA,
        (
            "Teehee, if I didn't, I could hardly enjoy\x01",
            "love as much as I do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43D9")

    label("loc_4352")


    ChrTalk(    #207
        0xA,
        "Hmm, such a pity. He was really cool.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xA,
        (
            "But, if he's a wanted person, oh, well.\x01",
            "Give up and find an even better man, I say!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_43D9")

    Jump("loc_451C")

    label("loc_43DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_443C")

    ChrTalk(    #209
        0xA,
        (
            "*sigh* No matter how much I clean\x01",
            "and clean, it never ends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xA,
        "Ugh, I hate it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_451C")

    label("loc_443C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_451C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_44ED")

    ChrTalk(    #211
        0xA,
        (
            "The birthday celebration's over,\x01",
            "so I have nothing to do lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xA,
        (
            "I'm sure it's hard on the management,\x01",
            "but it makes things easy for me, so\x01",
            "I'm happy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_451C")

    label("loc_44ED")


    ChrTalk(    #213
        0xA,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xA,
        "Sit wherever you'd like.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_451C")

    TalkEnd(0xA)
    Return()

    # Function_14_3B90 end

    def Function_15_4520(): pass

    label("Function_15_4520")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46E2")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                               # 0
            "Shop\x01",                               # 1
            "[Macho Meat Stew] - 1200 mira\x01",      # 2
            "Leave\x01",                              # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45AB")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0xAD)
    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_45AB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46BF")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4685")
    SubMira(1200)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #215
        "\x06Ate #2CMacho Meat Stew#0C.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4677")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x7)"), scpexpr(EXPR_END)), "loc_4646")
    Jump("loc_4677")

    label("loc_4646")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #216
        "\x06Learned [#2CMacho Meat Stew#0C] recipe.\x02",
    )

    CloseMessageWindow()

    label("loc_4677")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_46AD")

    label("loc_4685")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #217
        "Insufficient mira.\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_46AD")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xB)
    Return()

    label("loc_46BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46D9")
    FadeToBright(300, 0)
    TalkEnd(0xB)
    Return()

    label("loc_46D9")

    FadeToBright(300, 0)

    label("loc_46E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_47B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4772")

    ChrTalk(    #218
        0xFE,
        "Heeey, welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        "Since you're here, grab something to eat, yeah?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        "I'll give ya the best meal you've ever had.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_47B1")

    label("loc_4772")


    ChrTalk(    #221
        0xFE,
        "Heeey, welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        "I was so, so bored. You got no idea.\x02",
    )

    CloseMessageWindow()

    label("loc_47B1")

    Jump("loc_5049")

    label("loc_47B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_48E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4880")

    ChrTalk(    #223
        0xFE,
        (
            "Ahhh, man, this is a pain in the butt.\x01",
            "I can't even use the oven!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        (
            "Luckily, I've got a charcoal cooker,\x01",
            "so I can still whip up some food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        "Gotta treasure your old tools.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_48E3")

    label("loc_4880")


    ChrTalk(    #226
        0xFE,
        (
            "It's been a while since I've\x01",
            "done charcoal cooking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        "Takes quite a bit of work, you know.\x02",
    )

    CloseMessageWindow()

    label("loc_48E3")

    Jump("loc_5049")

    label("loc_48E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_4951")

    ChrTalk(    #228
        0xFE,
        (
            "Seems like the soldiers are all\x01",
            "worked up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        "I wonder if something else is gonna happen.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5049")

    label("loc_4951")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_4AA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4A04")

    ChrTalk(    #230
        0xFE,
        (
            "That reminds me, those earthquakes\x01",
            "have totally gone away. Phew!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        (
            "Seems like that declaration of safety from\x01",
            "the central factory was true, after all.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_4AA0")

    label("loc_4A04")


    ChrTalk(    #232
        0xFE,
        (
            "No one can say for sure that earthquakes\x01",
            "ABSOLUTELY WON'T happen, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        (
            "So, even after being told it's safe,\x01",
            "it's hard to not doubt it a little.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AA0")

    Jump("loc_5049")

    label("loc_4AA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_4ACA")

    ChrTalk(    #234
        0xFE,
        "Phew! Time for a break.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5049")

    label("loc_4ACA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_4B7B")

    ChrTalk(    #235
        0xFE,
        "That Tammy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "On top of skipping work she's sighing\x01",
            "and complaining it's boring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        (
            "Go hide out someplace I can't see and\x01",
            "hear if ya wanna talk like that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5049")

    label("loc_4B7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_4C39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4BBF")

    ChrTalk(    #238
        0xFE,
        "Really, that Tammy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xFE,
        "Come back already.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C36")

    label("loc_4BBF")


    ChrTalk(    #240
        0xFE,
        "Heeey, welcome. I'll take your orders.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xFE,
        (
            "I don't know what happened, but\x01",
            "my waitress ain't here, after all.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_4C36")

    Jump("loc_5049")

    label("loc_4C39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_4DA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4CC9")

    ChrTalk(    #242
        0xFE,
        (
            "I've been workin' here for quite a while,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        (
            "My heart still bursts with excitement\x01",
            "when a customer eats my food.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D9F")

    label("loc_4CC9")


    ChrTalk(    #244
        0xFE,
        (
            "I've been workin' here for quite a while,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        (
            "My heart still bursts with excitement\x01",
            "when a customer eats my food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0xFE,
        (
            "That's why I always work with my back to\x01",
            "everyone. My face would give me away.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_4D9F")

    Jump("loc_5049")

    label("loc_4DA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_4E06")

    ChrTalk(    #247
        0xFE,
        "Heeey, done talkin'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xFE,
        (
            "If you are, go ahead and take a break\x01",
            "here, if you'd like.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5049")

    label("loc_4E06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_4F61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 5)), scpexpr(EXPR_END)), "loc_4ED5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4E53")

    ChrTalk(    #249
        0xFE,
        (
            "Hey, welcome. We're open for business!\x01",
            "Somehow!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4ED2")

    label("loc_4E53")


    ChrTalk(    #250
        0xFE,
        (
            "Hey, welcome. We're open for business!\x01",
            "Somehow!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xFE,
        (
            "Please, go ahead and try our new menu.\x01",
            "You won't be disappointed!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_4ED2")

    Jump("loc_4F5E")

    label("loc_4ED5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4EFE")

    ChrTalk(    #252
        0xFE,
        "Ahhh, this is a disaster.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4F5E")

    label("loc_4EFE")


    ChrTalk(    #253
        0xFE,
        "Ahhh, this is a disaster.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xFE,
        (
            "No way I can keep up business\x01",
            "without a little cleaning.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_4F5E")

    Jump("loc_5049")

    label("loc_4F61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_5049")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4FFC")

    ChrTalk(    #255
        0xB,
        (
            "I never have much to do after\x01",
            "the birthday celebrations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xB,
        "I've been so bored that I developed a new recipe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xB,
        "Please, try it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5049")

    label("loc_4FFC")


    ChrTalk(    #258
        0xB,
        "Welcome, welcome to the cafeteria!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0xB,
        "Take aaaaaany seat you like.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_5049")

    TalkEnd(0xB)
    Return()

    # Function_15_4520 end

    def Function_16_504D(): pass

    label("Function_16_504D")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_527A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_50E5")

    ChrTalk(    #260
        0xFE,
        (
            "U-Umm...\x01",
            "I really ought to be getting back, so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        (
            "I'll be glad to hear your concerns another\x01",
            "day, at the cathedral, so...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5277")

    label("loc_50E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_5174")

    ChrTalk(    #262
        0xFE,
        (
            "I will be at the cathedral, so\x01",
            "feel free to come by any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xFE,
        (
            "Now, then, I'm very sorry, but\x01",
            "I'd best be returning soon...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5277")

    label("loc_5174")


    ChrTalk(    #264
        0xFE,
        "I can well understand your troubles myself.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xFE,
        (
            "However, the problem always lies\x01",
            "within the self.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0xFE,
        (
            "What's preventing you from meeting\x01",
            "your future spouse..\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0xFE,
        (
            "Could it be that the 'ideal man' that lies\x01",
            "in your heart is naught but a false image?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_5277")

    Jump("loc_56B8")

    label("loc_527A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_53E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_5334")

    ChrTalk(    #268
        0xFE,
        "I shall pray again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0xFE,
        (
            "Please, let light shine on the path\x01",
            "beneath our feet when we stray...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0xFE,
        (
            "Please, protect us from the darkness\x01",
            "that lies in the depths...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53E4")

    label("loc_5334")


    ChrTalk(    #271
        0xFE,
        "Goddess of the sky, Aidios...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0xFE,
        (
            "I ask you grant your protection\x01",
            "to those gathered here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0xFE,
        (
            "And, I ask you to watch over us to\x01",
            "the end from your grand heights...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_53E4")

    Jump("loc_56B8")

    label("loc_53E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_54E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_5457")

    ChrTalk(    #274
        0xFE,
        "We've managed to clean it all up...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0xFE,
        "Now, then, I should like to begin services soon.\x02",
    )

    CloseMessageWindow()
    Jump("loc_54E4")

    label("loc_5457")


    ChrTalk(    #276
        0xFE,
        "Seems we've managed to clean up somehow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0xFE,
        (
            "Still, I am so unbelievably hot. Apparently\x01",
            "vestments are not well suited to exercise.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_54E4")

    Jump("loc_56B8")

    label("loc_54E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_5599")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_554C")

    ChrTalk(    #278
        0xFE,
        "Still, this is a terrible mess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xFE,
        "I should see if they'll allow me to help.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5596")

    label("loc_554C")


    ChrTalk(    #280
        0xFE,
        "It seems no one is injured.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0xFE,
        "The silver lining to this cloud.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_5596")

    Jump("loc_56B8")

    label("loc_5599")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_56B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_5615")

    ChrTalk(    #282
        0xE,
        (
            "It seems the soldiers are well\x01",
            "dedicated to their tasks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0xE,
        "I will take the time to wait for a bit.\x02",
    )

    CloseMessageWindow()
    Jump("loc_56B8")

    label("loc_5615")


    ChrTalk(    #284
        0xE,
        (
            "I came from the cathedral to lead\x01",
            "the soldiers in prayer, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0xE,
        "No one has come yet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xE,
        (
            "It seems everyone is dedicating\x01",
            "themselves to their tasks.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_56B8")

    TalkEnd(0xE)
    Return()

    # Function_16_504D end

    def Function_17_56BC(): pass

    label("Function_17_56BC")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_572C")

    ChrTalk(    #287
        0xFE,
        (
            "There's more people here at service\x01",
            "than normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xFE,
        "Probably thanks to the earthquake, huh.\x02",
    )

    CloseMessageWindow()
    Jump("loc_597C")

    label("loc_572C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_586C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_57B0")

    ChrTalk(    #289
        0xFE,
        "Phew! Finally done.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0xFE,
        (
            "Since a priest's come all the way from the\x01",
            "capital, I should probably go to service.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5869")

    label("loc_57B0")


    ChrTalk(    #291
        0xFE,
        "Phew! Finally done.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xFE,
        (
            "We cleaned up faster than expected\x01",
            "since everyone helped out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0xFE,
        (
            "Since a priest's come all the way from the\x01",
            "capital, I should probably go to service.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_5869")

    Jump("loc_597C")

    label("loc_586C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_597C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_58FC")

    ChrTalk(    #294
        0xFE,
        (
            "My post's outside, but we've got a bit\x01",
            "of an unexpected situation, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xFE,
        "I'm away from post helping out inside.\x02",
    )

    CloseMessageWindow()
    Jump("loc_597C")

    label("loc_58FC")


    ChrTalk(    #296
        0xFE,
        (
            "Seems like stuff's collapsed\x01",
            "all over the guard post.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0xFE,
        (
            "It'll be hard to guard anything until\x01",
            "we clean this mess up.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_597C")

    TalkEnd(0xF)
    Return()

    # Function_17_56BC end

    def Function_18_5980(): pass

    label("Function_18_5980")

    OP_EA(0x1, 0xB, 0x0, 0x0)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_5A04")

    ChrTalk(    #298
        0xFE,
        (
            "I really don't want to throw away\x01",
            "my life in a place like this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xFE,
        "A-Anyway let's get back to the capital!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A7B")

    label("loc_5A04")


    ChrTalk(    #300
        0xFE,
        (
            "I-I don't really want to throw away\x01",
            "my life in a place like this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0xFE,
        "A-Anyway let's get back to the capital!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_5A7B")

    TalkEnd(0xFE)
    Return()

    # Function_18_5980 end

    def Function_19_5A7F(): pass

    label("Function_19_5A7F")

    Call(0, 20)
    Return()

    # Function_19_5A7F end

    def Function_20_5A84(): pass

    label("Function_20_5A84")

    OP_EA(0x1, 0xB, 0x0, 0x0)
    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_5B89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_5B0F")

    ChrTalk(    #302
        0x11,
        (
            "I really don't want to throw away\x01",
            "my life in a place like this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0x11,
        "A-Anyway let's get back to the capital!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5B86")

    label("loc_5B0F")


    ChrTalk(    #304
        0x11,
        (
            "I-I don't really want to throw away\x01",
            "my life in a place like this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0x11,
        "A-Anyway let's get back to the capital!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_5B86")

    Jump("loc_5E3D")

    label("loc_5B89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_5CCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_5C06")

    ChrTalk(    #306
        0x11,
        (
            "Lying down like this is just making\x01",
            "me irritated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0x11,
        "Do I really want to waste my days like this...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5CC9")

    label("loc_5C06")


    ChrTalk(    #308
        0x11,
        (
            "Lying down like this is just making\x01",
            "me irritated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0x11,
        "D-Do I really want to waste my days like this...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0x11,
        (
            "When I came to my senses, I was so scared.\x01",
            "I thought I was a goner for sure.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_5CC9")

    Jump("loc_5E3D")

    label("loc_5CCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_5E3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_5D2A")

    ChrTalk(    #311
        0x11,
        "Ahh, Ricky, tell me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0x11,
        "What on earth is the meaning of my existence?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5E3D")

    label("loc_5D2A")


    ChrTalk(    #313
        0x11,
        (
            "The birthday celebration comes and all I have to\x01",
            "show is a broken heart... Then an earthquake\x01",
            "comes and all I get is nearly dying...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x11,
        (
            "How pitiful...\x01",
            "I haven't even the will to stand up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x11,
        "Ahh, Ricky, tell me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x11,
        "What on earth is the meaning of my existence?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_5E3D")

    TalkEnd(0x11)
    Return()

    # Function_20_5A84 end

    def Function_21_5E41(): pass

    label("Function_21_5E41")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_5F36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_5EBF")

    ChrTalk(    #317
        0xFE,
        (
            "Calm down, Anton.\x01",
            "No point in freaking out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0xFE,
        (
            "Well, I'm just glad you've\x01",
            "gotten your energy back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F33")

    label("loc_5EBF")


    ChrTalk(    #319
        0xFE,
        (
            "Calm down, Anton.\x01",
            "No point in freaking out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0xFE,
        (
            "Well, either way, I'd planned\x01",
            "on returning to the capital.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_5F33")

    Jump("loc_618C")

    label("loc_5F36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_6035")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_5F82")

    ChrTalk(    #321
        0xFE,
        (
            "Seems like Anton's starting to get bored\x01",
            "of this too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6032")

    label("loc_5F82")


    ChrTalk(    #322
        0xFE,
        (
            "The floor here isn't real well suited\x01",
            "to sleeping on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0xFE,
        (
            "Ideally, this'd be the elevated\x01",
            "gardens in the royal castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0xFE,
        "I bet the grass there'd be perfectly soft.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_6032")

    Jump("loc_618C")

    label("loc_6035")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_618C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_611B")

    ChrTalk(    #325
        0xFE,
        (
            "Sorry. I know we're making\x01",
            "it hard to use the road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0xFE,
        (
            "To spontaneously embark on little soul-searching\x01",
            "trips is my friend's bad habit, I'm afraid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0xFE,
        (
            "Don't worry, he'll eventually get bored\x01",
            "and recover.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_618C")

    label("loc_611B")


    ChrTalk(    #328
        0xFE,
        "Anton...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0xFE,
        (
            "It's pretty clear what your raison d'etre is\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0xFE,
        "... Yes, you are a roadblock.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_618C")

    TalkEnd(0x14)
    Return()

    # Function_21_5E41 end

    def Function_22_6190(): pass

    label("Function_22_6190")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_634A")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6213")

    ChrTalk(    #331
        0x101,
        (
            "#1000FWe don't have any business on the capital side.\x01",
            "Let's hurry up and finish our questioning.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_632C")

    label("loc_6213")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_62A8")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6230")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_6237")

    label("loc_6230")

    TurnDirection(0x106, 0x0, 400)

    label("loc_6237")


    ChrTalk(    #332
        0x106,
        (
            "#050FWe don't have any business with the capital side.\x01",
            "Let's just hurry up and finish our investigation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_632C")

    label("loc_62A8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_62BE")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_62C5")

    label("loc_62BE")

    TurnDirection(0x103, 0x0, 400)

    label("loc_62C5")


    ChrTalk(    #333
        0x103,
        (
            "#027FWe don't have anything to do on the capital side.\x01",
            "Let's just quickly finish our questioning.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_632C")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_64A0")

    label("loc_634A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_64A0")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_63EC")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6375")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_637C")

    label("loc_6375")

    TurnDirection(0x106, 0x0, 400)

    label("loc_637C")


    ChrTalk(    #334
        0x106,
        (
            "#050FPast here's the Grancel region.\x02\x03",

            "We ain't got time to visit other regions.\x01",
            "Let's just turn around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6485")

    label("loc_63EC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6402")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_6409")

    label("loc_6402")

    TurnDirection(0x103, 0x0, 400)

    label("loc_6409")


    ChrTalk(    #335
        0x103,
        (
            "#020FPast this point is the Grancel region.\x02\x03",

            "We don't have time to go to the other\x01",
            "regions. Let's just return for now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6485")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_64A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_687C")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_652F")

    ChrTalk(    #336
        0x108,
        (
            "#070FAs I recall, Kilika arranged air tickets for us.\x02\x03",

            "Let's ride the airships to get to the capital.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65B8")

    label("loc_652F")


    ChrTalk(    #337
        0x108,
        (
            "#070FPast here is the capital.\x02\x03",

            "As I recall, Kilika arranged air tickets for us.\x02\x03",

            "Let's ride the airships to get to the capital.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_65B8")

    Jump("loc_6861")

    label("loc_65BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6716")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65D8")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_65DF")

    label("loc_65D8")

    TurnDirection(0x106, 0x0, 400)

    label("loc_65DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_6642")

    ChrTalk(    #338
        0x106,
        (
            "#050FKilika should have tickets ready for us.\x02\x03",

            "Let's go via airship to the capital.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6713")

    label("loc_6642")


    ChrTalk(    #339
        0x106,
        (
            "#050FI know we're most of the way there,\x01",
            "but let's go to the capital by airship.\x02\x03",

            "Kilika should have tickets ready for us,\x01",
            "if I remember rightly.\x02\x03",

            "Let's at least enjoy ourselves\x01",
            "when we're in transit.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_6713")

    Jump("loc_6861")

    label("loc_6716")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_672C")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_6733")

    label("loc_672C")

    TurnDirection(0x103, 0x0, 400)

    label("loc_6733")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_67A1")

    ChrTalk(    #340
        0x103,
        (
            "#020FKilika should have tickets already\x01",
            "prepared for us.\x02\x03",

            "Let's go via airship to the capital.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6861")

    label("loc_67A1")


    ChrTalk(    #341
        0x103,
        (
            "#020FWe came all the way here, but let's\x01",
            "take the airship the rest of the way\x01",
            "to the capital.\x02\x03",

            "Kilika should have tickets already\x01",
            "prepared for us.\x02\x03",

            "Let's just relax for this last bit.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_6861")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_687C")

    Return()

    # Function_22_6190 end

    def Function_23_687D(): pass

    label("Function_23_687D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A58")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_690F")

    ChrTalk(    #342
        0x108,
        (
            "#070FAh, past here's the Zeiss region.\x02\x03",

            "We don't have time to stop in at other\x01",
            "regions. Let's just turn around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A3D")

    label("loc_690F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_69AC")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_692C")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_6933")

    label("loc_692C")

    TurnDirection(0x106, 0x0, 400)

    label("loc_6933")


    ChrTalk(    #343
        0x106,
        (
            "#050FLooks like Zeiss is this way.\x02\x03",

            "We don't have time to hang around the\x01",
            "other regions. Let's just turn around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A3D")

    label("loc_69AC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_69C2")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_69C9")

    label("loc_69C2")

    TurnDirection(0x103, 0x0, 400)

    label("loc_69C9")


    ChrTalk(    #344
        0x103,
        (
            "#020FPast here is the Zeiss region.\x02\x03",

            "We don't have time to go to the other\x01",
            "regions. Let's just return for now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A3D")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_6A58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B40")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6ACD")

    ChrTalk(    #345
        0x101,
        (
            "#1002FWe don't have time to waste on side trips.\x01",
            "...Let's hurry back to the guild.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B25")

    label("loc_6ACD")


    ChrTalk(    #346
        0x109,
        (
            "#1063FWe don't have time to waste... We have\x01",
            "to hurry to the guild in the capital.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B25")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_6B40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6E7E")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_6BE7")

    ChrTalk(    #347
        0x108,
        (
            "#070FWalking is good training, but it's\x01",
            "also a waste of time.\x02\x03",

            "If we're going to Bose, the wise\x01",
            "choice is to use the airship.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C85")

    label("loc_6BE7")


    ChrTalk(    #348
        0x108,
        (
            "#070FThis is towards Zeiss.\x02\x03",

            "Walking is good training, but it's\x01",
            "also a waste of time.\x02\x03",

            "If we're going to Bose, the wise\x01",
            "choice is to use the airship.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_6C85")

    Jump("loc_6E63")

    label("loc_6C88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6D75")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CA5")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_6CAC")

    label("loc_6CA5")

    TurnDirection(0x106, 0x0, 400)

    label("loc_6CAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_6D1A")

    ChrTalk(    #349
        0x106,
        (
            "#053FWalking is a waste of time.\x02\x03",

            "#050FIf we're going to Bose, let's\x01",
            "head to the landing port.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D72")

    label("loc_6D1A")


    ChrTalk(    #350
        0x106,
        (
            "#050FThis way's Zeiss.\x02\x03",

            "If we're going to Bose, let's\x01",
            "head to the landing port.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_6D72")

    Jump("loc_6E63")

    label("loc_6D75")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D8B")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_6D92")

    label("loc_6D8B")

    TurnDirection(0x103, 0x0, 400)

    label("loc_6D92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_6E0A")

    ChrTalk(    #351
        0x103,
        (
            "#026FWalking is, frankly, a waste of time.\x02\x03",

            "#020FIf we're going to Bose, let's\x01",
            "head to the landing port.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E63")

    label("loc_6E0A")


    ChrTalk(    #352
        0x103,
        (
            "#020FThis way is Zeiss.\x02\x03",

            "If we're going to Bose, let's\x01",
            "head to the landing port.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_6E63")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_6E7E")

    Return()

    # Function_23_687D end

    def Function_24_6E7F(): pass

    label("Function_24_6E7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6E99")
    Call(0, 28)
    FadeToBright(0, 0)

    label("loc_6E99")

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
        "Phew! All clean again, thank the Goddess.\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0xA, 225, 400)

    ChrTalk(    #354
        0xA,
        "Huh...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6FCE")

    ChrTalk(    #355
        0x106,
        (
            "#051F#6PHey, you're Tammy, right?\x01",
            "We're from the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_700B")

    label("loc_6FCE")


    ChrTalk(    #356
        0x103,
        (
            "#020F#6PYou're Tammy, yes?\x01",
            "We're from the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_700B")


    ChrTalk(    #357
        0x101,
        (
            "#1006FYou mind if we ask you\x01",
            "a couple questions?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #358
        (
            "\x07\x05Estelle's party asked Tammy about the man in\x01",
            "sunglasses she saw.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #359
        0xA,
        "Oooh, him, yeah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0xA,
        (
            "I passed by him on the second\x01",
            "floor in the hallway yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0xA,
        "I think he was coming down from the roof.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0x104,
        (
            "#035FThat would match what our\x01",
            "soldier friend said, yes.\x02\x03",

            "#030FDid you exchange any words\x01",
            "when you passed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0xA,
        "Well, I did say hello.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0xA,
        (
            "He just...kinda grinned in\x01",
            "response and said 'yo.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0xA,
        (
            "Oooooh, just thinking about it makes me\x01",
            "all tingly again! He was sooooo...wild!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_73A3")

    ChrTalk(    #366
        0x101,
        "#1015FWild? So, what, like Agate here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0x106,
        "#552F#6PWhat's that supposed to--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #368
        0xA,
        (
            "Mmmm, this guy was a bit\x01",
            "taller than your friend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0xA,
        (
            "He had this dark suit, but opened\x01",
            "really casually at the chest, right?\x01",
            "He looked amazing in it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0xA,
        (
            "Oh, and he was wearing a\x01",
            "pair of black gloves, I think.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74B1")

    label("loc_73A3")


    ChrTalk(    #371
        0x103,
        (
            "#026F#6PHm. I think I'm starting to\x01",
            "get a picture of him...\x02\x03",

            "#020FDo you remember what he\x01",
            "was wearing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #372
        0xA,
        (
            "He had this dark suit, but opened\x01",
            "really casually at the chest, right?\x01",
            "He looked amazing in it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #373
        0xA,
        (
            "Oh, and he was wearing a pair\x01",
            "of black gloves, I think.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74B1")


    ChrTalk(    #374
        0x101,
        (
            "#1007FSo...sunglasses, a dark suit,\x01",
            "and black gloves. Riiiiight...\x02\x03",

            "#1019FThis guy might as well wear a sign on\x01",
            "his head saying 'I AM SINISTER, BE\x01",
            "SUSPICIOUS OF MY EVIL WAYS.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0xA,
        (
            "Oh, I wouldn't say suspicious!\x01",
            "He just had a scent of...danger\x01",
            "about him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0xA,
        (
            "Heehee! You know, that dangerous,\x01",
            "tough guy charm, right?\x02",
        )
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
            "#1016FUh, right... Anyway!\x02\x03",

            "#1015FSo you just passed by and said hi,\x01",
            "and didn't see him afterward, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #378
        0xA,
        "Yeah, unfortunately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #379
        0xA,
        (
            "I, um, chased after him a little bit...\x01",
            "I thought we could, um, um, get to\x01",
            "know each other, or...anyway!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0xA,
        "I lost track of him in a weird way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0x101,
        "#1004FA weird way? How so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #382
        0xA,
        (
            "Mmmmm. It'll be easier to show you.\x01",
            "Follow me.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_77CF():
        OP_6D(56990, 0, -22070, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_77CF)
    TurnDirection(0xA, 0xB, 400)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #383
        0xA,
        (
            "#4PExcuse me, Sanders, can I step\x01",
            "out for a moment?\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0xB, 255)
    TurnDirection(0xB, 0xA, 400)

    ChrTalk(    #384
        0xB,
        "#5PYeah, go ahead.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0xB,
        "#5PJust get back before the dinner rush!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_4B(0xB, 255)
    Call(0, 25)
    Return()

    # Function_24_6E7F end

    def Function_25_7890(): pass

    label("Function_25_7890")

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

    def lambda_7931():
        OP_94(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7931)
    Sleep(80)

    def lambda_794C():
        OP_94(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_794C)
    Sleep(120)

    def lambda_7967():
        OP_94(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_7967)
    Sleep(80)

    def lambda_7982():
        OP_94(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7982)
    Sleep(120)

    def lambda_799D():
        OP_94(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_799D)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xA, 0x1)
    OP_8C(0xA, 180, 400)

    ChrTalk(    #386
        0xA,
        (
            "#6PSo, this is where I passed him,\x01",
            "right here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #387
        0xA,
        "#6PHe went walking in this direction.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #388
        0xA,
        (
            "#6PI turned to follow him after a moment,\x01",
            "figuring I'd chat with him, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #389
        0x101,
        "#1002F#2POkay...\x02",
    )

    CloseMessageWindow()
    OP_43(0xA, 0x0, 0x0, 0x1A)

    def lambda_7A93():

        label("loc_7A93")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_7A93")

    QueueWorkItem2(0x101, 0, lambda_7A93)

    def lambda_7AA4():

        label("loc_7AA4")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_7AA4")

    QueueWorkItem2(0xF7, 0, lambda_7AA4)

    def lambda_7AB5():

        label("loc_7AB5")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_7AB5")

    QueueWorkItem2(0x105, 0, lambda_7AB5)

    def lambda_7AC6():

        label("loc_7AC6")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_7AC6")

    QueueWorkItem2(0x104, 0, lambda_7AC6)
    Sleep(1300)

    def lambda_7ADC():
        OP_6D(3290, 4000, 40300, 2800)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7ADC)

    def lambda_7AF4():
        OP_67(0, 8000, -10000, 2800)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7AF4)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x2)
    OP_44(0x101, 0x0)
    OP_44(0xF7, 0x0)
    OP_44(0x104, 0x0)
    OP_44(0x105, 0x0)

    def lambda_7B26():
        OP_6D(14530, 4000, 39860, 2800)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7B26)

    def lambda_7B3E():
        OP_67(0, 8000, -10000, 2800)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7B3E)
    Sleep(2500)
    SetChrPos(0xF7, 3830, 4000, 39090, 90)
    SetChrPos(0x101, 3830, 4000, 40090, 90)
    SetChrPos(0x105, 2830, 4000, 39090, 90)
    SetChrPos(0x104, 2830, 4000, 40090, 90)

    def lambda_7B9F():
        OP_90(0xFE, 0x2580, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7B9F)
    Sleep(120)

    def lambda_7BBF():
        OP_90(0xFE, 0x2580, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_7BBF)
    Sleep(80)

    def lambda_7BDF():
        OP_90(0xFE, 0x24B8, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7BDF)
    Sleep(120)

    def lambda_7BFF():
        OP_90(0xFE, 0x24B8, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7BFF)
    WaitChrThread(0x105, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #390
        0xA,
        (
            "When I turned, I saw that door,\x01",
            "over there, closing.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7C63():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_7C63)
    OP_8C(0x105, 180, 400)

    def lambda_7C78():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7C78)
    OP_8C(0x104, 180, 400)

    ChrTalk(    #391
        0xA,
        "So I thought, 'He must have stepped out!'\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #392
        0xA,
        (
            "'Here's my chance to talk to him before\x01",
            "he leaves!' So I followed him, but...\x02",
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

    # Function_25_7890 end

    def Function_26_7D4C(): pass

    label("Function_26_7D4C")


    def lambda_7D52():
        OP_8E(0xFE, 0xB68, 0xFA0, 0xC6CA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7D52)
    WaitChrThread(0xA, 0x1)

    def lambda_7D72():
        OP_8E(0xFE, 0xAFA, 0xFA0, 0x9BE6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7D72)
    WaitChrThread(0xA, 0x1)

    def lambda_7D92():
        OP_8E(0xFE, 0x3B42, 0xFA0, 0x9B3C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7D92)
    WaitChrThread(0xA, 0x1)
    OP_8C(0xA, 270, 400)
    Return()

    # Function_26_7D4C end

    def Function_27_7DB4(): pass

    label("Function_27_7DB4")


    def lambda_7DBA():
        OP_8E(0xFE, 0x3A5C, 0xFA0, 0x9696, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7DBA)
    WaitChrThread(0xFE, 0x1)

    def lambda_7DDA():
        OP_8E(0xFE, 0x3A98, 0xFA0, 0x8F98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7DDA)
    WaitChrThread(0xFE, 0x1)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    Return()

    # Function_27_7DB4 end

    def Function_28_7E00(): pass

    label("Function_28_7E00")

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
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7E79"),
        (1, "loc_7E7F"),
        (SWITCH_DEFAULT, "loc_7E85"),
    )


    label("loc_7E79")

    OP_A2(0x1200)
    Jump("loc_7E85")

    label("loc_7E7F")

    OP_A2(0x1201)
    Jump("loc_7E85")

    label("loc_7E85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_7E93")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_7E97")

    label("loc_7E93")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_7E97")

    Return()

    # Function_28_7E00 end

    def Function_29_7E98(): pass

    label("Function_29_7E98")

    TalkBegin(0xFF)
    Sleep(400)
    TalkEnd(0xFF)
    Return()

    # Function_29_7E98 end

    SaveToFile()

Try(main)
