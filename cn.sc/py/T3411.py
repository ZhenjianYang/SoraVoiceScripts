from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3411   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3411.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
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
        '利库斯',                               # 20
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
        TalkScenaIndex      = 9,
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
        TalkScenaIndex      = 10,
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
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 54970,
        Z                   = 0,
        Y                   = -21440,
        Direction           = 4,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
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
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 27480,
        Z                   = 0,
        Y                   = 1360,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
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
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 560,
        Z                   = 0,
        Y                   = 1930,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 25320,
        Z                   = 4000,
        Y                   = 83680,
        Direction           = 0,
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
        Y                   = 84320,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        TalkScenaIndex      = 19,
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
        TalkFunctionIndex   = 8,
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
        TalkFunctionIndex   = 6,
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
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 25120,
        TriggerZ            = 4000,
        TriggerY            = 84320,
        TriggerRange        = 1000,
        ActorX              = 25120,
        ActorZ              = 4500,
        ActorY              = 84320,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 25320,
        TriggerZ            = 4000,
        TriggerY            = 83680,
        TriggerRange        = 1000,
        ActorX              = 25320,
        ActorZ              = 5500,
        ActorY              = 83680,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_31E",          # 00, 0
        "Function_1_59C",          # 01, 1
        "Function_2_66C",          # 02, 2
        "Function_3_690",          # 03, 3
        "Function_4_6B4",          # 04, 4
        "Function_5_6D8",          # 05, 5
        "Function_6_6FC",          # 06, 6
        "Function_7_701",          # 07, 7
        "Function_8_A74",          # 08, 8
        "Function_9_A79",          # 09, 9
        "Function_10_D59",         # 0A, 10
        "Function_11_1167",        # 0B, 11
        "Function_12_116C",        # 0C, 12
        "Function_13_14B4",        # 0D, 13
        "Function_14_182D",        # 0E, 14
        "Function_15_1D2D",        # 0F, 15
        "Function_16_20BF",        # 10, 16
        "Function_17_2287",        # 11, 17
        "Function_18_228C",        # 12, 18
        "Function_19_24D0",        # 13, 19
        "Function_20_2717",        # 14, 20
        "Function_21_2E70",        # 15, 21
        "Function_22_3659",        # 16, 22
        "Function_23_36F2",        # 17, 23
        "Function_24_3AC8",        # 18, 24
        "Function_25_3F3A",        # 19, 25
    )


    def Function_0_31E(): pass

    label("Function_0_31E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_37E")
    SetChrPos(0xA, 78750, 0, 26210, 270)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0xE, 77860, 0, 26210, 90)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x10, 0x40)
    ClearChrFlags(0x10, 0x20)
    ClearChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x100)
    SetChrFlags(0x10, 0x1)
    OP_43(0x10, 0x0, 0x6, 0x2)
    Jump("loc_57C")

    label("loc_37E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_426")
    SetChrPos(0x8, 111940, 0, 22150, 0)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0x9, 111940, 0, 23370, 180)
    SetChrFlags(0x9, 0x10)
    SetChrPos(0xF, 77580, 0, 23520, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xD, 76130, 0, 24430, 45)
    SetChrPos(0xA, 79530, 0, 24930, 315)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    OP_51(0x10, 0x2A, (scpexpr(EXPR_PUSH_LONG, 0xAFC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2B, (scpexpr(EXPR_PUSH_LONG, 0x15F90), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2C, (scpexpr(EXPR_PUSH_LONG, 0x15F90), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_57C")

    label("loc_426")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_4B5")
    SetChrPos(0x9, 51170, 0, 28460, 0)
    SetChrPos(0xF, 2190, 0, 2570, 180)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xD, 4950, 0, -2820, 45)
    OP_43(0xA, 0x0, 0x0, 0x2)
    SetChrPos(0xE, 15400, 0, 1400, 180)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    OP_51(0x10, 0x2A, (scpexpr(EXPR_PUSH_LONG, 0xAFC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2B, (scpexpr(EXPR_PUSH_LONG, 0x15F90), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2C, (scpexpr(EXPR_PUSH_LONG, 0x15F90), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_57C")

    label("loc_4B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 5)), scpexpr(EXPR_END)), "loc_517")
    SetChrPos(0x9, 51170, 0, 28460, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xA, 58330, 0, -22280, 90)
    SetChrPos(0xC, 94890, 0, -22010, 90)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    SetChrPos(0xE, 15400, 0, 1400, 180)
    OP_43(0xE, 0x0, 0x0, 0x5)
    Jump("loc_57C")

    label("loc_517")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_56E")
    SetChrPos(0x9, 51170, 0, 28460, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xC, 94890, 0, -22010, 90)
    OP_43(0xA, 0x0, 0x0, 0x2)
    OP_43(0xB, 0x0, 0x0, 0x3)
    SetChrPos(0xE, 15400, 0, 1400, 180)
    OP_43(0xE, 0x0, 0x0, 0x5)
    Jump("loc_57C")

    label("loc_56E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_57C")
    OP_43(0xA, 0x0, 0x0, 0x2)

    label("loc_57C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_59B")
    OP_A2(0x1413)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x22), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    OP_A3(0x10F0)
    Event(0, 20)

    label("loc_59B")

    Return()

    # Function_0_31E end

    def Function_1_59C(): pass

    label("Function_1_59C")

    OP_1C(0x5, 0x0, 0x19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_5AF")
    OP_64(0x3, 0x1)
    Jump("loc_612")

    label("loc_5AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_5C1")
    OP_64(0x2, 0x1)
    OP_64(0x4, 0x1)
    Jump("loc_612")

    label("loc_5C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_5D3")
    OP_64(0x2, 0x1)
    OP_64(0x4, 0x1)
    Jump("loc_612")

    label("loc_5D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 5)), scpexpr(EXPR_END)), "loc_5E9")
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    Jump("loc_612")

    label("loc_5E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_603")
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    Jump("loc_612")

    label("loc_603")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_612")
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)

    label("loc_612")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_61F")
    OP_10(0x11, 0x0)
    Jump("loc_62F")

    label("loc_61F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 5)), scpexpr(EXPR_END)), "loc_62C")
    OP_10(0x11, 0x0)
    Jump("loc_62F")

    label("loc_62C")

    OP_10(0x13, 0x0)

    label("loc_62F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_649")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x22), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_649")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_65A")
    OP_1B(0x1, 0x0, 0x17)

    label("loc_65A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_66B")
    OP_1B(0x0, 0x0, 0x18)

    label("loc_66B")

    Return()

    # Function_1_59C end

    def Function_2_66C(): pass

    label("Function_2_66C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_68F")
    OP_8D(0xFE, 56600, -23980, 64040, -26210, 2000)
    Jump("Function_2_66C")

    label("loc_68F")

    Return()

    # Function_2_66C end

    def Function_3_690(): pass

    label("Function_3_690")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6B3")
    OP_8D(0xFE, 58110, -23110, 53730, -21470, 2000)
    Jump("Function_3_690")

    label("loc_6B3")

    Return()

    # Function_3_690 end

    def Function_4_6B4(): pass

    label("Function_4_6B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6D7")
    OP_8D(0xFE, 3140, -1230, 9860, -4460, 2000)
    Jump("Function_4_6B4")

    label("loc_6D7")

    Return()

    # Function_4_6B4 end

    def Function_5_6D8(): pass

    label("Function_5_6D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6FB")
    OP_8D(0xFE, 14200, 2000, 18960, 180, 2000)
    Jump("Function_5_6D8")

    label("loc_6FB")

    Return()

    # Function_5_6D8 end

    def Function_6_6FC(): pass

    label("Function_6_6FC")

    Call(0, 7)
    Return()

    # Function_6_6FC end

    def Function_7_701(): pass

    label("Function_7_701")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73C")
    Call(6, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72B")
    OP_A9(0xAC)
    TalkEnd(0xC)
    Return()

    label("loc_72B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_73C")
    TalkEnd(0xC)
    Return()

    label("loc_73C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_823")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_79F")

    ChrTalk(    #0
        0xC,
        (
            "今天黛米恨难得地\x01",
            "去做礼拜了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xC,
        (
            "今天来的牧师先生\x01",
            "好像是个相当不错的男人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_820")

    label("loc_79F")


    ChrTalk(    #2
        0xC,
        (
            "今天黛米恨难得地\x01",
            "去做礼拜了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xC,
        (
            "那个女孩儿有这样的信仰心\x01",
            "我觉得我们没有休息的余地……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xC,
        "一定是因为牧师是个好男人。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_820")

    Jump("loc_A70")

    label("loc_823")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_8FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_8AF")

    ChrTalk(    #5
        0xC,
        (
            "不过因为有地震\x01",
            "才去祈祷是很失礼的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xC,
        (
            "太自说自话\x01",
            "女神就不会生气吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xC,
        (
            "如果我是女神的话\x01",
            "一定会让这种人吃天罚的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8FC")

    label("loc_8AF")


    ChrTalk(    #8
        0xC,
        (
            "说起来从大圣堂\x01",
            "来了牧师哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xC,
        (
            "又发生了地震，\x01",
            "要不过一会去祈祷吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_8FC")

    Jump("loc_A70")

    label("loc_8FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_9BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_958")

    ChrTalk(    #10
        0xC,
        (
            "堆积着的行李\x01",
            "好像都塌下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xC,
        (
            "因为平常没整理，\x01",
            "就变成这样了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9B7")

    label("loc_958")


    ChrTalk(    #12
        0xC,
        "是场挺大的地震呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xC,
        (
            "像这种真正的震感\x01",
            "好久没碰见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xC,
        (
            "无论如何\x01",
            "先要收拾一下……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_9B7")

    Jump("loc_A70")

    label("loc_9BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_A70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_A0D")

    ChrTalk(    #15
        0xC,
        (
            "吃饭请去\x01",
            "旁边的食堂。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xC,
        (
            "价格公道，\x01",
            "而且味道的评价也很好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A70")

    label("loc_A0D")


    ChrTalk(    #17
        0xC,
        "欢迎来到圣海姆门。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xC,
        (
            "这里是任何人都欢迎的\x01",
            "旅客用投宿设施哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xC,
        (
            "需要的时候\x01",
            "请跟我说。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_A70")

    TalkEnd(0xC)
    Return()

    # Function_7_701 end

    def Function_8_A74(): pass

    label("Function_8_A74")

    Call(0, 9)
    Return()

    # Function_8_A74 end

    def Function_9_A79(): pass

    label("Function_9_A79")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_B74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_AF3")

    ChrTalk(    #20
        0x8,
        (
            "看来那一连串的地震的\x01",
            "问题总算是解决了……不过\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "还有很多无法解释的地方。\x01",
            "暂时还不能放松警惕。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B71")

    label("loc_AF3")


    ChrTalk(    #22
        0x8,
        (
            "看来那一连串的地震的\x01",
            "问题总算是解决了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "不过实在是\x01",
            "还有很多无法解释的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "真是的……\x01",
            "暂时还不能放松警惕。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_B71")

    Jump("loc_D55")

    label("loc_B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_C2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_BC7")

    ChrTalk(    #25
        0x8,
        (
            "不管怎样我们也\x01",
            "继续警戒。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "尽管面对地震\x01",
            "确实是没办法……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C2A")

    label("loc_BC7")


    ChrTalk(    #27
        0x8,
        (
            "这次轮到雷斯顿要塞\x01",
            "发生地震了吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "地点都在军队的重要设施，\x01",
            "实在无法相信这是偶然的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_C2A")

    Jump("loc_D55")

    label("loc_C2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_CCB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 4)), scpexpr(EXPR_END)), "loc_C7F")

    ChrTalk(    #29
        0x8,
        "什么？你们还有事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        (
            "我不是说了我有工作吗？\x01",
            "不要妨碍我。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CC8")

    label("loc_C7F")


    ChrTalk(    #31
        0x8,
        (
            "关于情况的说明\x01",
            "你们去找塔尔瓦托副队长。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        "因为我还有紧急的工作。\x02",
    )

    CloseMessageWindow()

    label("loc_CC8")

    Jump("loc_D55")

    label("loc_CCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_D55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D19")

    ChrTalk(    #33
        0x8,
        "我都说了我在工作。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "老缠着我的话\x01",
            "就把你们赶出哨所。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D55")

    label("loc_D19")


    ChrTalk(    #35
        0x8,
        "你们在搞什么啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x8,
        (
            "抱歉，我在工作。\x01",
            "不要妨碍我。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_D55")

    TalkEnd(0x8)
    Return()

    # Function_9_A79 end

    def Function_10_D59(): pass

    label("Function_10_D59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D6A")
    Call(0, 21)
    Return()

    label("loc_D6A")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_E45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_DC6")

    ChrTalk(    #37
        0x9,
        (
            "军队的上层最近\x01",
            "活动得挺积极的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x9,
        (
            "难道是旧情报部的\x01",
            "余党落网了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E42")

    label("loc_DC6")


    ChrTalk(    #39
        0x9,
        (
            "地震结束的宣告\x01",
            "已经从中央工房发出了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x9,
        (
            "我们军队的上层也\x01",
            "也发来了相同的通知。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x9,
        (
            "嗯，看来不是单纯的\x01",
            "自然现象。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_E42")

    Jump("loc_1163")

    label("loc_E45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_F18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_EB8")

    ChrTalk(    #42
        0x9,
        (
            "我要让士兵们\x01",
            "继续保持警戒态势。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x9,
        (
            "关于要塞地震的受害情况\x01",
            "等到有明确消息了我会告知你们的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F15")

    label("loc_EB8")


    ChrTalk(    #44
        0x9,
        (
            "雷斯顿要塞的受害程度\x01",
            "好像被控制在最低限度了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x9,
        (
            "看来是事先觉察到\x01",
            "会有地震发生了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_F15")

    Jump("loc_1163")

    label("loc_F18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_FA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_F5B")

    ChrTalk(    #46
        0x9,
        "呼，总算收拾整齐了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x9,
        "真是重体力劳动啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_FA2")

    label("loc_F5B")


    ChrTalk(    #48
        0x9,
        (
            "呼～这边\x01",
            "总算也收拾整齐了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x9,
        (
            "那么，我得去其他\x01",
            "岗位看看了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_FA2")

    Jump("loc_1163")

    label("loc_FA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_10C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1002")

    ChrTalk(    #50
        0x9,
        (
            "对了，迪尔队长\x01",
            "好像恨忙哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x9,
        (
            "就算你们问他什么，\x01",
            "也只会被骂回来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10C6")

    label("loc_1002")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 5)), scpexpr(EXPR_END)), "loc_106D")

    ChrTalk(    #52
        0x9,
        (
            "哟，各位游击士。\x01",
            "调查有进展吗？？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x9,
        (
            "我这边也\x01",
            "快要收拾好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x9,
        (
            "傍晚之前\x01",
            "应该能弄好吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10C3")

    label("loc_106D")


    ChrTalk(    #55
        0x9,
        (
            "昨天切斯利看到了\x01",
            "一个奇怪的男人哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x9,
        (
            "他在屋顶收拾，\x01",
            "详细情况你们可以去问他。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10C3")

    OP_A2(0x1)

    label("loc_10C6")

    Jump("loc_1163")

    label("loc_10C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_1163")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_112B")

    ChrTalk(    #57
        0x9,
        (
            "登上里面的台阶\x01",
            "就能到达『亚宁堡』的\x01",
            "的上层。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x9,
        (
            "来旅游的客人\x01",
            "经常上去的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1163")

    label("loc_112B")


    ChrTalk(    #59
        0x9,
        "哎呀，欢迎。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x9,
        (
            "如果需要设施的说明\x01",
            "请跟我说。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1163")

    TalkEnd(0x9)
    Return()

    # Function_10_D59 end

    def Function_11_1167(): pass

    label("Function_11_1167")

    Call(0, 12)
    Return()

    # Function_11_1167 end

    def Function_12_116C(): pass

    label("Function_12_116C")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_1209")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_11C8")

    ChrTalk(    #61
        0xD,
        (
            "地震的善后工作\x01",
            "也总算结束了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xD,
        (
            "哎呀，人真是\x01",
            "真是一场大灾难啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1206")

    label("loc_11C8")


    ChrTalk(    #63
        0xD,
        "呀，欢迎。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xD,
        (
            "现在已经和平常\x01",
            "一样在办理通行手续了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1206")

    Jump("loc_14B0")

    label("loc_1209")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_12C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_126E")

    ChrTalk(    #65
        0xD,
        (
            "唔～偶尔祈祷一次\x01",
            "灵魂得到了安宁的感觉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xD,
        (
            "下次趁休息去参加\x01",
            "大圣堂的礼拜吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12C5")

    label("loc_126E")


    ChrTalk(    #67
        0xD,
        (
            "必须在地震来临的时候\x01",
            "去向女神祈祷。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xD,
        (
            "那场地震也一定是\x01",
            "因为那是女神的意志。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_12C5")

    Jump("loc_14B0")

    label("loc_12C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1370")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_132D")

    ChrTalk(    #69
        0xD,
        (
            "牧师先生是自己\x01",
            "提出要帮忙的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xD,
        (
            "不愧是牧师先生啊。\x01",
            "虽然年轻，可是很懂道理。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_136D")

    label("loc_132D")


    ChrTalk(    #71
        0xD,
        "呼～终于收拾整齐了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xD,
        (
            "这也是拜牧师先生的\x01",
            "帮忙所赐。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_136D")

    Jump("loc_14B0")

    label("loc_1370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_1404")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_13C9")

    ChrTalk(    #73
        0xD,
        (
            "刚才的地震\x01",
            "摇得挺厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xD,
        (
            "没有人受伤\x01",
            "可以说是不可思议的事了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1401")

    label("loc_13C9")


    ChrTalk(    #75
        0xD,
        "看上去很凌乱吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xD,
        (
            "刚才的地震\x01",
            "摇得挺厉害啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1401")

    Jump("loc_14B0")

    label("loc_1404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_14B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_145F")

    ChrTalk(    #77
        0xD,
        (
            "诞辰庆典也结束了，\x01",
            "最近游客少了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xD,
        (
            "反正我们这些\x01",
            "士兵算是轻松了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14B0")

    label("loc_145F")


    ChrTalk(    #79
        0xD,
        "欢迎来到圣海姆门。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xD,
        (
            "难得来一趟，\x01",
            "请一定要欣赏一下\x01",
            "『亚宁堡』的威容。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_14B0")

    TalkEnd(0xD)
    Return()

    # Function_12_116C end

    def Function_13_14B4(): pass

    label("Function_13_14B4")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_156B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_151F")

    ChrTalk(    #81
        0xA,
        "唔～我将来的伴侣……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xA,
        (
            "莫非是……\x01",
            "要是牧师先生的话㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xA,
        "哎呀，我该怎么办呢！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1568")

    label("loc_151F")


    ChrTalk(    #84
        0xA,
        (
            "啊？　我这个人\x01",
            "男人运是不是很坏～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xA,
        (
            "怎样做才能改变\x01",
            "命运呢～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1568")

    Jump("loc_1829")

    label("loc_156B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1675")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_15DE")

    ChrTalk(    #86
        0xA,
        (
            "啊，他热心奉献\x01",
            "祈祷的神情真是太棒了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xA,
        (
            "在牧师大人清秀的侧脸上\x01",
            "我能感觉到女神的存在啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1672")

    label("loc_15DE")


    ChrTalk(    #88
        0xA,
        (
            "我听说有年轻的牧师在，\x01",
            "今天就来做礼拜了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xA,
        (
            "虽然他不算个年轻男子，\x01",
            "但还是相当英俊的呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xA,
        (
            "呵呵，要是这种礼拜的话\x01",
            "我每天都能来参加㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1672")

    Jump("loc_1829")

    label("loc_1675")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1748")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_16DC")

    ChrTalk(    #91
        0xA,
        (
            "我是那种容易迷上别人，\x01",
            "不过不会死缠烂打的类型。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xA,
        (
            "呵呵，这样才能\x01",
            "享受恋爱啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1745")

    label("loc_16DC")


    ChrTalk(    #93
        0xA,
        (
            "唔～真可惜。\x01",
            "明明是个很帅的人\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xA,
        (
            "不过既然是要特别当心的人就算了。\x01",
            "我就放弃他去找其他的男人吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1745")

    Jump("loc_1829")

    label("loc_1748")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_1789")

    ChrTalk(    #95
        0xA,
        (
            "唉～怎么收拾也\x01",
            "收拾不完。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xA,
        "真是的，讨厌死了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1829")

    label("loc_1789")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_1829")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_17FA")

    ChrTalk(    #97
        0xA,
        (
            "诞辰庆典也结束了，\x01",
            "最近挺闲的～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xA,
        (
            "虽然经营方面出现困难，\x01",
            "不过我能轻松一些，也挺高兴的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1829")

    label("loc_17FA")


    ChrTalk(    #99
        0xA,
        "欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xA,
        "请随意选择喜欢的座位。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1829")

    TalkEnd(0xA)
    Return()

    # Function_13_14B4 end

    def Function_14_182D(): pass

    label("Function_14_182D")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19F0")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18BC")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0xAD)
    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_18BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19CD")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1995")
    SubMira(1200)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #101
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1987")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x7)"), scpexpr(EXPR_END)), "loc_195B")
    Jump("loc_1987")

    label("loc_195B")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #102
        "\x06\x07\x02东方火锅·力\x07\x00的做法已经学会了。\x02",
    )

    CloseMessageWindow()

    label("loc_1987")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_19BB")

    label("loc_1995")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #103
        "没有足够的米拉。\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_19BB")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xB)
    Return()

    label("loc_19CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19E7")
    FadeToBright(300, 0)
    TalkEnd(0xB)
    Return()

    label("loc_19E7")

    FadeToBright(300, 0)

    label("loc_19F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_1A7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1A2F")

    ChrTalk(    #104
        0xFE,
        "真是的，黛米那家伙～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        "也该回来了吧～\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A78")

    label("loc_1A2F")


    ChrTalk(    #106
        0xFE,
        (
            "哟～欢迎光临～\x01",
            "要点菜找我哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "不知道为什么\x01",
            "女服务员不～在。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1A78")

    Jump("loc_1D29")

    label("loc_1A7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1B63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1AE2")

    ChrTalk(    #108
        0xFE,
        (
            "我在这里也\x01",
            "干了很久了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "不过现在看到顾客吃菜的\x01",
            "一瞬间心里也还是七上八下的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B60")

    label("loc_1AE2")


    ChrTalk(    #110
        0xFE,
        (
            "我在这里也\x01",
            "干了很久了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "不过现在看到顾客吃菜的\x01",
            "一瞬间心里也还是七上八下的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "所以我一直是背对着\x01",
            "客人工作的～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1B60")

    Jump("loc_1D29")

    label("loc_1B63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1BA6")

    ChrTalk(    #113
        0xFE,
        "哟～话已经说完了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "方便的话\x01",
            "在这儿喝杯茶吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D29")

    label("loc_1BA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_1C83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 5)), scpexpr(EXPR_END)), "loc_1C2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1BE3")

    ChrTalk(    #115
        0xFE,
        (
            "哟～欢迎光临～\x01",
            "总算恢复营业了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C2A")

    label("loc_1BE3")


    ChrTalk(    #116
        0xFE,
        (
            "哟～欢迎光临～\x01",
            "总算恢复营业了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "你们可以尝尝\x01",
            "我的新菜谱～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1C2A")

    Jump("loc_1C80")

    label("loc_1C2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1C4B")

    ChrTalk(    #118
        0xFE,
        "唉～真没办法。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C80")

    label("loc_1C4B")


    ChrTalk(    #119
        0xFE,
        "唉～真没办法。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        "不收拾一下都没法营业了～\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1C80")

    Jump("loc_1D29")

    label("loc_1C83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_1D29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1CEB")

    ChrTalk(    #121
        0xB,
        "诞辰庆典之后真闲啊～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xB,
        (
            "因为太闲，\x01",
            "我就开发了新菜谱哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xB,
        "请一～定要试试哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D29")

    label("loc_1CEB")


    ChrTalk(    #124
        0xB,
        (
            "欢迎光临～\x01",
            "欢迎来到食堂。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xB,
        "请随意选择喜欢的座位。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1D29")

    TalkEnd(0xB)
    Return()

    # Function_14_182D end

    def Function_15_1D2D(): pass

    label("Function_15_1D2D")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_1E29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1D8D")

    ChrTalk(    #126
        0xFE,
        (
            "我就在大圣堂里，\x01",
            "你随时都能来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "那么，不好意思，\x01",
            "我也该回去了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E26")

    label("loc_1D8D")


    ChrTalk(    #128
        0xFE,
        (
            "你的烦恼\x01",
            "我完全能理解。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "可是，问题永远\x01",
            "是在你自己身上的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "阻止你和将来的伴侣\x01",
            "相遇的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "不正是你心中那个\x01",
            "『理想的异性』的幻影吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_1E26")

    Jump("loc_20BB")

    label("loc_1E29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1EFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1E9A")

    ChrTalk(    #132
        0xFE,
        "我再来为您祈祷\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "当我们迷失道路时，\x01",
            "请您为我们指路……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "在深远的黑暗中\x01",
            "守护我们……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EFB")

    label("loc_1E9A")


    ChrTalk(    #135
        0xFE,
        "空之女神啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "请保佑聚集\x01",
            "在这里的人们……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "并且请您在高天之上\x01",
            "永远注视我们……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_1EFB")

    Jump("loc_20BB")

    label("loc_1EFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1F92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1F44")

    ChrTalk(    #138
        0xFE,
        "终于收拾好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "那么，差不多该\x01",
            "开始礼拜了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F8F")

    label("loc_1F44")


    ChrTalk(    #140
        0xFE,
        (
            "好像已经\x01",
            "整理完了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "不过天可真热啊。\x01",
            "祭司服好像不适合运动。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_1F8F")

    Jump("loc_20BB")

    label("loc_1F92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_2004")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1FCF")

    ChrTalk(    #142
        0xFE,
        (
            "不过又给\x01",
            "弄乱了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "我也来\x01",
            "帮忙吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2001")

    label("loc_1FCF")


    ChrTalk(    #144
        0xFE,
        (
            "好像没有人\x01",
            "受伤。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        "真是不幸中之大幸。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_2001")

    Jump("loc_20BB")

    label("loc_2004")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_20BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2053")

    ChrTalk(    #146
        0xE,
        (
            "各位士兵都在\x01",
            "努力工作呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xE,
        (
            "我就在这里\x01",
            "再等一会儿吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20BB")

    label("loc_2053")


    ChrTalk(    #148
        0xE,
        (
            "我是从大圣堂来\x01",
            "为士兵们的祈祷的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xE,
        (
            "不过还没有\x01",
            "人过来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xE,
        (
            "嗯，看来大家\x01",
            "都在努力工作呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_20BB")

    TalkEnd(0xE)
    Return()

    # Function_15_1D2D end

    def Function_16_20BF(): pass

    label("Function_16_20BF")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_2105")

    ChrTalk(    #151
        0xFE,
        (
            "来礼拜的人\x01",
            "比平时多啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        "是不是因为发生了地震？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2283")

    label("loc_2105")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_21D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_2157")

    ChrTalk(    #153
        0xFE,
        "呼～终于结束了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "好，牧师先生也来了，\x01",
            "我去做个礼拜吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D0")

    label("loc_2157")


    ChrTalk(    #155
        0xFE,
        "呼～终于结束了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        (
            "因为大家合力的关系，\x01",
            "善后工作比预计的早完成了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "好，牧师先生也来了，\x01",
            "我去做个礼拜吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_21D0")

    Jump("loc_2283")

    label("loc_21D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_2283")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_223C")

    ChrTalk(    #158
        0xFE,
        (
            "我的工作岗位是在外面，\x01",
            "不过现在是紧急情况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "所以离开工作岗位\x01",
            "到里面来帮忙了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2283")

    label("loc_223C")


    ChrTalk(    #160
        0xFE,
        (
            "哨所里到处\x01",
            "都有行李塌下来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "不收拾好的话\x01",
            "也没法好好警戒。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_2283")

    TalkEnd(0xF)
    Return()

    # Function_16_20BF end

    def Function_17_2287(): pass

    label("Function_17_2287")

    Call(0, 18)
    Return()

    # Function_17_2287 end

    def Function_18_228C(): pass

    label("Function_18_228C")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_231E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_22DD")

    ChrTalk(    #162
        0x10,
        (
            "还是不能在\x01",
            "这种地方浪费人生！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x10,
        "总、总之要回王都去！\x02",
    )

    CloseMessageWindow()
    Jump("loc_231B")

    label("loc_22DD")


    ChrTalk(    #164
        0x10,
        (
            "不、不能在\x01",
            "这种地方浪费人生！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x10,
        "好，赶快回王都去！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_231B")

    Jump("loc_24CC")

    label("loc_231E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_23F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_2373")

    ChrTalk(    #166
        0x10,
        (
            "这么躺着\x01",
            "总觉得很烦躁。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x10,
        (
            "我能就这样\x01",
            "每天在这里浪费时间吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23ED")

    label("loc_2373")


    ChrTalk(    #168
        0x10,
        (
            "总觉得这么躺着\x01",
            "心情就会烦躁。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x10,
        (
            "我、我能就这样\x01",
            "每天在这里浪费时间吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x10,
        (
            "不知不觉间一辈子\x01",
            "就过去了，真可怕。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_23ED")

    Jump("loc_24CC")

    label("loc_23F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_24CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_243A")

    ChrTalk(    #171
        0x10,
        "啊，利库斯，告诉我！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x10,
        (
            "我的存在意义\x01",
            "到底是什么？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24CC")

    label("loc_243A")


    ChrTalk(    #173
        0x10,
        (
            "诞辰庆典就失恋……\x01",
            "有地震就差点死……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x10,
        (
            "真悲惨……\x01",
            "我连爬起来的力气也没有了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x10,
        "啊，利库斯，告诉我！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x10,
        (
            "我的存在意义\x01",
            "到底是什么？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_24CC")

    TalkEnd(0x10)
    Return()

    # Function_18_228C end

    def Function_19_24D0(): pass

    label("Function_19_24D0")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_258E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_253A")

    ChrTalk(    #177
        0xFE,
        (
            "冷静一点，安敦。\x01",
            "你着急也不是办法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "反正不管怎样，你\x01",
            "有精神了，我挺高兴的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_258B")

    label("loc_253A")


    ChrTalk(    #179
        0xFE,
        (
            "冷静一点，安敦。\x01",
            "你那么着急也不是办法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "总之我已经装备\x01",
            "要回王都了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_258B")

    Jump("loc_2713")

    label("loc_258E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_262B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_25C6")

    ChrTalk(    #181
        0xFE,
        (
            "安敦那家伙好像\x01",
            "也开始感到无聊了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2628")

    label("loc_25C6")


    ChrTalk(    #182
        0xFE,
        (
            "这里的地板不太\x01",
            "适合午睡。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "还是王城的\x01",
            "空中庭园比较理想。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "那里的草坪\x01",
            "看上去很软。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_2628")

    Jump("loc_2713")

    label("loc_262B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_2713")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_26B3")

    ChrTalk(    #185
        0xFE,
        (
            "抱歉啊，\x01",
            "我阻碍你们走路了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        (
            "时常开始寻找自我\x01",
            "是我的伙伴的臭毛病。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        (
            "没关系的，过几天他腻了\x01",
            "就肯定会复活。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2713")

    label("loc_26B3")


    ChrTalk(    #188
        0xFE,
        "安敦…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "从现在的状况来看，\x01",
            "你的存在意义已经很明确了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        "……对，就是通行的障碍。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_2713")

    TalkEnd(0x13)
    Return()

    # Function_19_24D0 end

    def Function_20_2717(): pass

    label("Function_20_2717")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2728")
    Call(0, 22)

    label("loc_2728")

    EventBegin(0x0)
    OP_4A(0x8, 255)
    SetChrPos(0x8, 6790, 0, 2810, 180)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x101, 6930, 0, 900, 0)
    SetChrPos(0xF7, 5740, 0, 890, 0)
    SetChrPos(0x105, 6640, 0, -190, 0)
    SetChrPos(0x104, 5510, 0, -230, 0)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    OP_4A(0xD, 255)
    OP_4A(0xE, 255)
    TurnDirection(0xD, 0x8, 0)
    OP_6D(6790, 0, 1300, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #191
        0x8,
        (
            "#5P真是的……\x01",
            "游击士真是莫名其妙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x8,
        (
            "#5P如你们所见，大家因为收拾地震的\x01",
            "残局都忙得不可开交。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x8,
        "#5P要调查的话能不能过会儿？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_28D1")

    ChrTalk(    #194
        0x106,
        (
            "#053F#6P抱歉，我们也是为了工作。\x02\x03",

            "#050F不会妨碍你们整理的，\x01",
            "能不能允许我们调查情况？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2924")

    label("loc_28D1")


    ChrTalk(    #195
        0x103,
        (
            "#027F#6P抱歉，我们也是在工作。\x02\x03",

            "不会妨碍你们整理的，\x01",
            "能不能允许我们调查情况？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2924")


    ChrTalk(    #196
        0x8,
        (
            "#5P呼，如果没司令部的指示的话\x01",
            "我已经拒绝你们了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x8,
        (
            "#5P我有紧急的公务在身，\x01",
            "关于地震的发生情况\x01",
            "你们去找塔尔瓦托副队长。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x8,
        (
            "#5P应该在前面房间\x01",
            "深处的仓库里整理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x101,
        "#1006F#2P明白了，是塔尔瓦托副队长吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x8,
        (
            "#5P请尽量不要妨碍其他\x01",
            "人的整理工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x8,
        "#5P那我就先告辞了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 600)

    def lambda_2A4A():
        OP_8E(0x8, 0x58C0, 0x0, 0x96A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2A4A)

    def lambda_2A65():
        OP_6D(18030, 0, 2160, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2A65)

    def lambda_2A7D():
        OP_67(0, 8000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2A7D)

    def lambda_2A95():

        label("loc_2A95")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2A95")

    QueueWorkItem2(0x101, 1, lambda_2A95)

    def lambda_2AA6():

        label("loc_2AA6")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2AA6")

    QueueWorkItem2(0xF7, 1, lambda_2AA6)

    def lambda_2AB7():

        label("loc_2AB7")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2AB7")

    QueueWorkItem2(0x105, 1, lambda_2AB7)

    def lambda_2AC8():

        label("loc_2AC8")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2AC8")

    QueueWorkItem2(0x104, 1, lambda_2AC8)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0x8, 0x1)
    OP_8C(0x8, 17, 600)
    OP_8E(0x8, 0x594C, 0x0, 0xCBC, 0xBB8, 0x0)
    OP_22(0x6, 0x0, 0x64)
    OP_72(0x1, 0x10)
    OP_72(0x1, 0x800)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x13)
    OP_6F(0x1, 19)
    OP_73(0x1)
    OP_8E(0x8, 0x5ADC, 0x0, 0x159A, 0x7D0, 0x0)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x1, 19)
    OP_70(0x1, 0x0)
    OP_73(0x1)
    OP_71(0x1, 0x10)
    OP_71(0x1, 0x800)
    SetChrFlags(0x8, 0x80)

    def lambda_2B63():
        OP_6D(6550, 0, 600, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2B63)

    def lambda_2B7B():
        OP_67(0, 8000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2B7B)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0x105, 0x1)
    OP_44(0x104, 0x1)
    TurnDirection(0x101, 0x104, 400)
    OP_8C(0x105, 0, 400)
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(    #202
        0x101,
        (
            "#1015F#5P唔，好像很忙呢。\x02\x03",

            "我们也帮忙\x01",
            "一起整理吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2C4E")

    ChrTalk(    #203
        0x106,
        (
            "#053F#6P别多管闲事了。\x02\x03",

            "#050F好歹也算是军事施设。\x01",
            "有可能有机密文件什么的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CA5")

    label("loc_2C4E")


    ChrTalk(    #204
        0x103,
        (
            "#020F#6P算了，好歹也算是军事施设，\x01",
            "还是别多管闲事了。\x02\x03",

            "有可能还有机密文件什么的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CA5")


    ChrTalk(    #205
        0x101,
        "#1007F#5P嗯～也对。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x105,
        (
            "#043F不过被害情况\x01",
            "和蔡斯市的地震不同呢。\x02\x03",

            "那时东西没散得\x01",
            "这么乱的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x104,
        (
            "#035F嗯，关于这个差别\x01",
            "也应该确认一下。\x02\x03",

            "#030F接下来就是怪异人物的目击情报了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x101,
        (
            "#1002F#5P那个戴墨镜的男人……\x02\x03",

            "详细情况要首先问一下那个\x01",
            "被称为副队长的人。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x86, 0x4, 0x2)
    OP_28(0x86, 0x4, 0x8)
    OP_28(0x86, 0x1, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, 5460, 0, 420, 0)
    SetChrPos(0xF7, 5460, 0, 420, 0)
    SetChrPos(0x105, 5460, 0, 420, 0)
    SetChrPos(0x104, 5460, 0, 420, 0)
    OP_6D(5460, 0, 420, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    OP_4B(0xD, 255)
    OP_4B(0xE, 255)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_20_2717 end

    def Function_21_2E70(): pass

    label("Function_21_2E70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E8A")
    Call(0, 22)
    FadeToBright(0, 0)

    label("loc_2E8A")

    EventBegin(0x0)
    OP_4A(0x9, 255)
    Fade(1000)
    SetChrPos(0x101, 51640, 0, 26840, 0)
    SetChrPos(0xF7, 50500, 0, 26720, 0)
    SetChrPos(0x105, 51710, 0, 25760, 0)
    SetChrPos(0x104, 50580, 0, 25500, 0)
    OP_6D(51270, 0, 28050, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #209
        0x9,
        (
            "#5P哎呀哎呀……\x01",
            "全部整理完是很辛苦的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x9,
        "#5P得在黄昏前做完……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x101,
        (
            "#1011F#2P那个……\x01",
            "抱歉，在百忙之中打扰你。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x9, 180, 400)

    ChrTalk(    #212
        0x9,
        "#5P啊，你们是……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #213
        (
            "\x07\x05艾丝蒂尔一行介绍了自己的游击士身份之后\x01",
            "说明了自己是来调查地震的事的。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #214
        0x9,
        "#5P是吗，辛苦你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x9,
        (
            "#5P你们想了解\x01",
            "地震的发生情况吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_30A6")

    ChrTalk(    #216
        0x106,
        "#050F#6P嗯，我们想听听详细情况。\x02",
    )

    CloseMessageWindow()
    Jump("loc_30CC")

    label("loc_30A6")


    ChrTalk(    #217
        0x103,
        "#020F#6P嗯，我们想听听详细情况。\x02",
    )

    CloseMessageWindow()

    label("loc_30CC")


    ChrTalk(    #218
        0x9,
        "#5P明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x9,
        (
            "#5P地震发生于下午１点左右……\x01",
            "大概是２小时前。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x9,
        (
            "#5P能让堆积的木箱\x01",
            "倒塌的摇晃\x01",
            "持续了约３０秒吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x101,
        (
            "#1004F#2P咦，那和\x01",
            "沃尔费堡垒的地震比起来……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #222
        "\x18\x07\x05拿这次的地震和沃尔费堡垒的地震比？\x02",
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【摇晃的强度大】\x01",      # 0
            "【摇晃的时间长】\x01",      # 1
            "【两者都有】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3238"),
        (1, "loc_3276"),
        (2, "loc_32B4"),
        (SWITCH_DEFAULT, "loc_32F3"),
    )


    label("loc_3238")

    OP_2B(0x85, 0x1)

    ChrTalk(    #223
        0x105,
        (
            "#043F嗯，是啊……\x02\x03",

            "还有摇晃的时间\x01",
            "好像也变长了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32F3")

    label("loc_3276")

    OP_2B(0x85, 0x1)

    ChrTalk(    #224
        0x105,
        (
            "#043F嗯，是啊……\x02\x03",

            "还有摇晃的强度\x01",
            "好像也变大了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32F3")

    label("loc_32B4")

    OP_2B(0x85, 0x3)

    ChrTalk(    #225
        0x105,
        (
            "#047F是啊……\x02\x03",

            "#042F强度也变大了，\x01",
            "时间也变长了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32F3")

    label("loc_32F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3361")

    ChrTalk(    #226
        0x106,
        (
            "#555F#6P还有我们碰到的\x01",
            "在蔡斯市的地震……\x02\x03",

            "不管从强度还是时间来看\x01",
            "都应该是处于两者中间的位置。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33C3")

    label("loc_3361")


    ChrTalk(    #227
        0x103,
        (
            "#022F#6P还有我们遇到的\x01",
            "蔡斯市的地震……\x02\x03",

            "不管从强度还是时间来看\x01",
            "都应该是处于两者中间的位置。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33C3")


    ChrTalk(    #228
        0x104,
        (
            "#035F#7P就是说，这种局部的地震\x01",
            "每一次都会变得更危险。\x02\x03",

            "#030F或许可以这么说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x101,
        "#1020F#2P那、那岂不是不好办了！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 400)

    ChrTalk(    #230
        0x9,
        "#5P事态确实很严峻呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x9,
        (
            "#5P不过只要是自然现象\x01",
            "就没办法防止了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x9,
        (
            "#5P游击士协会\x01",
            "有什么对策吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x101,
        (
            "#1007F#2P不，还不能确定，\x01",
            "不过稍微有点线索。\x02\x03",

            "#1002F另外地震前后\x01",
            "有没有发生什么奇怪的事？\x02\x03",

            "比如发现可疑人物什么的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x9,
        "#5P可疑人物……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x9,
        (
            "#5P我记得昨天切斯利说\x01",
            "他看到了一个怪异的男人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x9,
        (
            "#5P他正在整理屋顶，\x01",
            "详细情况你们可以去问他。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_35D5")

    ChrTalk(    #237
        0x106,
        (
            "#051F#6P明白了。\x01",
            "屋顶的切斯利是吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35FE")

    label("loc_35D5")


    ChrTalk(    #238
        0x103,
        (
            "#020F#6P明白了。\x01",
            "屋顶的切斯利是吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35FE")


    ChrTalk(    #239
        0x101,
        "#1006F#2P感谢你的帮助。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x9,
        (
            "#5P不不。\x01",
            "你们才辛苦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 0, 400)
    OP_4B(0x9, 255)
    OP_A2(0x1414)
    OP_28(0x86, 0x1, 0x2)
    OP_28(0x86, 0x1, 0x4)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_21_2E70 end

    def Function_22_3659(): pass

    label("Function_22_3659")

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
        (0, "loc_36D3"),
        (1, "loc_36D9"),
        (SWITCH_DEFAULT, "loc_36DF"),
    )


    label("loc_36D3")

    OP_A2(0x1200)
    Jump("loc_36DF")

    label("loc_36D9")

    OP_A2(0x1201)
    Jump("loc_36DF")

    label("loc_36DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_36ED")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_36F1")

    label("loc_36ED")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_36F1")

    Return()

    # Function_22_3659 end

    def Function_23_36F2(): pass

    label("Function_23_36F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37FA")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3771")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_371D")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_3724")

    label("loc_371D")

    TurnDirection(0x106, 0x0, 400)

    label("loc_3724")


    ChrTalk(    #241
        0x106,
        (
            "#050F前面是格兰赛尔地区。\x02\x03",

            "没时间去别的地方了。\x01",
            "现在还是乖乖回去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37DA")

    label("loc_3771")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3787")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_378E")

    label("loc_3787")

    TurnDirection(0x103, 0x0, 400)

    label("loc_378E")


    ChrTalk(    #242
        0x103,
        (
            "#020F前面是格兰赛尔地区。\x02\x03",

            "没时间去其它的地方了，\x01",
            "现在还是乖乖回去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37DA")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)

    label("loc_37FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AC7")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_3868")

    ChrTalk(    #243
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
    Jump("loc_38CF")

    label("loc_3868")


    ChrTalk(    #244
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

    label("loc_38CF")

    Jump("loc_3AAC")

    label("loc_38D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_39C8")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38EF")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_38F6")

    label("loc_38EF")

    TurnDirection(0x106, 0x0, 400)

    label("loc_38F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_3944")

    ChrTalk(    #245
        0x106,
        (
            "#050F雾香应该为我们\x01",
            "准备好了船票。\x02\x03",

            "我们还是乘定期船去王都吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39C5")

    label("loc_3944")


    ChrTalk(    #246
        0x106,
        (
            "#050F虽然都到了这里了，\x01",
            "我们还是乘定期船去王都吧。\x02\x03",

            "不过我记得雾香应该为\x01",
            "我们准备好了船票。\x02\x03",

            "至少移动的时候要\x01",
            "好好享受。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_39C5")

    Jump("loc_3AAC")

    label("loc_39C8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39DE")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_39E5")

    label("loc_39DE")

    TurnDirection(0x103, 0x0, 400)

    label("loc_39E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_3A33")

    ChrTalk(    #247
        0x103,
        (
            "#020F雾香小姐应该\x01",
            "为我们准备好了船票。\x02\x03",

            "我们乘定期船去王都吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AAC")

    label("loc_3A33")


    ChrTalk(    #248
        0x103,
        (
            "#020F虽然已经到了这里，\x01",
            "我们还是乘定期船去王都吧。\x02\x03",

            "雾香小姐也\x01",
            "为我们准备好了船票。\x02\x03",

            "至少移动的时候要\x01",
            "好好享受。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_3AAC")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_3AC7")

    Return()

    # Function_23_36F2 end

    def Function_24_3AC8(): pass

    label("Function_24_3AC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C22")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B2D")

    ChrTalk(    #249
        0x103,
        (
            "#070F哟，前面是蔡斯地区了。\x02\x03",

            "现在没空去其他的地方了，\x01",
            "赶快回去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C07")

    label("loc_3B2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3B9A")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B4A")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_3B51")

    label("loc_3B4A")

    TurnDirection(0x106, 0x0, 400)

    label("loc_3B51")


    ChrTalk(    #250
        0x106,
        (
            "#050F这边是蔡斯地区。\x02\x03",

            "没时间去别的地方了。\x01",
            "现在还是乖乖回去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C07")

    label("loc_3B9A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BB0")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_3BB7")

    label("loc_3BB0")

    TurnDirection(0x103, 0x0, 400)

    label("loc_3BB7")


    ChrTalk(    #251
        0x103,
        (
            "#020F过了这里就是蔡斯地区了。\x02\x03",

            "没时间去其它的地方了，\x01",
            "现在还是乖乖回去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C07")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_3C22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3CBE")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C72")

    ChrTalk(    #252
        0x101,
        (
            "#1002F没时间闲逛了。\x01",
            "……要赶快返回协会才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CA3")

    label("loc_3C72")


    ChrTalk(    #253
        0x109,
        (
            "#1063F没时间闲逛了。\x01",
            "……赶紧去王都协会吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CA3")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_3CBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F39")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_3D37")

    ChrTalk(    #254
        0x108,
        (
            "#070F虽说徒步移动是修行，\x01",
            "但那样太浪费时间。\x02\x03",

            "要去柏斯的话\x01",
            "还是用定期船比较好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DA1")

    label("loc_3D37")


    ChrTalk(    #255
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

    label("loc_3DA1")

    Jump("loc_3F1E")

    label("loc_3DA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3E68")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DC1")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_3DC8")

    label("loc_3DC1")

    TurnDirection(0x106, 0x0, 400)

    label("loc_3DC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_3E22")

    ChrTalk(    #256
        0x106,
        (
            "#053F……要走过去\x01",
            "说实话太浪费时间。\x02\x03",

            "#050F要去柏斯\x01",
            "还是去定期船飞船坪吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E65")

    label("loc_3E22")


    ChrTalk(    #257
        0x106,
        (
            "#050F这边是蔡斯地区。\x02\x03",

            "要去柏斯的话\x01",
            "还是去定期船飞船坪吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_3E65")

    Jump("loc_3F1E")

    label("loc_3E68")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E7E")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_3E85")

    label("loc_3E7E")

    TurnDirection(0x103, 0x0, 400)

    label("loc_3E85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_3EDF")

    ChrTalk(    #258
        0x103,
        (
            "#026F……要走过去\x01",
            "说实话是浪费时间。\x02\x03",

            "#020F要去柏斯\x01",
            "还是去定期船飞船坪吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F1E")

    label("loc_3EDF")


    ChrTalk(    #259
        0x103,
        (
            "#020F这边是蔡斯地区。\x02\x03",

            "要去柏斯\x01",
            "还是去定期船飞船坪吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_3F1E")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_3F39")

    Return()

    # Function_24_3AC8 end

    def Function_25_3F3A(): pass

    label("Function_25_3F3A")

    TalkBegin(0xFF)
    Sleep(400)
    TalkEnd(0xFF)
    Return()

    # Function_25_3F3A end

    SaveToFile()

Try(main)
