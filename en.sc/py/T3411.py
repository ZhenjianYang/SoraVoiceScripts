from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Ricky',                                # 20
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
        "Function_8_D06",          # 08, 8
        "Function_9_D0B",          # 09, 9
        "Function_10_11D4",        # 0A, 10
        "Function_11_1818",        # 0B, 11
        "Function_12_181D",        # 0C, 12
        "Function_13_1CEE",        # 0D, 13
        "Function_14_22A0",        # 0E, 14
        "Function_15_29C9",        # 0F, 15
        "Function_16_3027",        # 10, 16
        "Function_17_32EB",        # 11, 17
        "Function_18_32F0",        # 12, 18
        "Function_19_36AD",        # 13, 19
        "Function_20_39FC",        # 14, 20
        "Function_21_4483",        # 15, 21
        "Function_22_4F61",        # 16, 22
        "Function_23_4FF9",        # 17, 23
        "Function_24_56EB",        # 18, 24
        "Function_25_5CED",        # 19, 25
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_8A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_7E7")

    ChrTalk(    #0
        0xC,
        (
            "Tammy's at service, apparently.\x01",
            "That happens about as often as\x01",
            "...earthquakes. Ha.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xC,
        (
            "My guess is, the priest that came\x01",
            "by today is a real looker.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89E")

    label("loc_7E7")


    ChrTalk(    #2
        0xC,
        (
            "Tammy's at service, apparently.\x01",
            "Believe me, that NEVER happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xC,
        "I don't think she's all that devout.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xC,
        (
            "My guess? She's only going because\x01",
            "the priest is a real looker.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_89E")

    Jump("loc_D02")

    label("loc_8A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_A72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_9D6")

    ChrTalk(    #5
        0xC,
        (
            "Some only start praying once disaster\x01",
            "strikes. Hmph! How disrespectful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xC,
        (
            "If you're only going to pray when it's\x01",
            "convenient for you, why pray at all?\x01",
            "Poor Aidios must feel so used.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xC,
        (
            "If I were the Goddess, I'd think about\x01",
            "dropping some divine punishment on\x01",
            "a few ungrateful heads!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A6F")

    label("loc_9D6")


    ChrTalk(    #8
        0xC,
        (
            "I was told that a priest from the\x01",
            "cathedral's come to visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xC,
        (
            "Given the earthquake we had earlier,\x01",
            "I suppose I should go and pray some\x01",
            "more.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_A6F")

    Jump("loc_D02")

    label("loc_A72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_BC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_B0B")

    ChrTalk(    #10
        0xC,
        (
            "All of our storage's gone and\x01",
            "collapsed on us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xC,
        (
            "This wouldn't have been a problem\x01",
            "if SOMEONE had put everything away\x01",
            "properly!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BBF")

    label("loc_B0B")


    ChrTalk(    #12
        0xC,
        "That sure was a big earthquake.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xC,
        (
            "Haven't felt anything like that in\x01",
            "a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xC,
        (
            "One way or another, I've got some\x01",
            "cleaning up to do... Might as well get\x01",
            "started.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_BBF")

    Jump("loc_D02")

    label("loc_BC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_D02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_C65")

    ChrTalk(    #15
        0xC,
        (
            "You should go to the cafeteria nearby\x01",
            "for your meals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xC,
        (
            "Everyone who goes there says\x01",
            "they've got both good prices and\x01",
            "good food to match.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D02")

    label("loc_C65")


    ChrTalk(    #17
        0xC,
        "Welcome to Sanktheim Gate!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xC,
        (
            "This lodge is open to any and all\x01",
            "weary travelers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xC,
        (
            "Just let me know and I'll book you\x01",
            "for the night, all right?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_D02")

    TalkEnd(0xC)
    Return()

    # Function_7_701 end

    def Function_8_D06(): pass

    label("Function_8_D06")

    Call(0, 9)
    Return()

    # Function_8_D06 end

    def Function_9_D0B(): pass

    label("Function_9_D0B")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_E95")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_DCD")

    ChrTalk(    #20
        0x8,
        (
            "The earthquake issue has been resolved\x01",
            "about as much as it can be for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "But there's still too much we don't know\x01",
            "about it. We'll need to stay alert for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E92")

    label("loc_DCD")


    ChrTalk(    #22
        0x8,
        (
            "The earthquake issue has been resolved\x01",
            "about as much as it can be for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "Still, there's just so much we don't\x01",
            "understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "Hmph... Suppose we'll need to stay\x01",
            "on alert for while.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_E92")

    Jump("loc_11D0")

    label("loc_E95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_FAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_EFD")

    ChrTalk(    #25
        0x8,
        "We'll continue standing guard here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        "There's no way to fight an earthquake...\x02",
    )

    CloseMessageWindow()
    Jump("loc_FA8")

    label("loc_EFD")


    ChrTalk(    #27
        0x8,
        (
            "So this time there was an earthquake\x01",
            "at Leiston Fortress. Hmm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "All of them have struck at critical\x01",
            "military facilities. I can't believe that's\x01",
            "a coincidence.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_FA8")

    Jump("loc_11D0")

    label("loc_FAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_10D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 4)), scpexpr(EXPR_END)), "loc_1027")

    ChrTalk(    #29
        0x8,
        "Oh, did you still need something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        (
            "Sorry, but I'm afraid I'm much too\x01",
            "busy to speak with you now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10CE")

    label("loc_1027")


    ChrTalk(    #31
        0x8,
        (
            "If you need assistance of some kind,\x01",
            "you can speak to Talbot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "I've already told you where he is. For now,\x01",
            "I have urgent business that requires\x01",
            "my attention.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10CE")

    Jump("loc_11D0")

    label("loc_10D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_11D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_116B")

    ChrTalk(    #33
        0x8,
        "...I believe I said I am working.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "Should you continue to make a nuisance\x01",
            "of yourself, I'll have you removed from the\x01",
            "premises.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11D0")

    label("loc_116B")


    ChrTalk(    #35
        0x8,
        "What do you all want?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x8,
        (
            "Sorry, but I'm very busy right now.\x01",
            "Don't get in the way, please.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_11D0")

    TalkEnd(0x8)
    Return()

    # Function_9_D0B end

    def Function_10_11D4(): pass

    label("Function_10_11D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11E5")
    Call(0, 21)
    Return()

    label("loc_11E5")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_1341")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1284")

    ChrTalk(    #37
        0x9,
        (
            "The brass have all been pretty\x01",
            "active lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x9,
        (
            "I wonder if the remnants of the\x01",
            "old Intelligence Division finally\x01",
            "hit the network.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_133E")

    label("loc_1284")


    ChrTalk(    #39
        0x9,
        (
            "The central factory sent out a\x01",
            "message that the earthquakes\x01",
            "are finished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x9,
        (
            "We've received a similar report\x01",
            "from headquarters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x9,
        (
            "So these weren't some unusual\x01",
            "phenomena...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_133E")

    Jump("loc_1814")

    label("loc_1341")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_149B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_13F0")

    ChrTalk(    #42
        0x9,
        (
            "All soldiers stationed here are on\x01",
            "high alert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x9,
        (
            "We won't publicly announce the\x01",
            "earthquake at the fortress until we\x01",
            "can fully assess the damage done.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1498")

    label("loc_13F0")


    ChrTalk(    #44
        0x9,
        (
            "Damage to Leiston Fortress was,\x01",
            "thank the Goddess, kept to a minimum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x9,
        (
            "They were apparently aware that an\x01",
            "earthquake would strike beforehand.\x01",
            "Imagine that.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1498")

    Jump("loc_1814")

    label("loc_149B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1542")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_14EF")

    ChrTalk(    #46
        0x9,
        "Ahhh! I'm finally done cleaning!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x9,
        "What a pain THAT was...\x02",
    )

    CloseMessageWindow()
    Jump("loc_153F")

    label("loc_14EF")


    ChrTalk(    #48
        0x9,
        "All done cleaning here!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x9,
        (
            "Time go to check up on the other\x01",
            "sections.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_153F")

    Jump("loc_1814")

    label("loc_1542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_1721")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_15D2")

    ChrTalk(    #50
        0x9,
        (
            "Yeah, the chief is really busy\x01",
            "these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x9,
        (
            "His fuse is real short as a result,\x01",
            "so try not to ask him too much, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_171E")

    label("loc_15D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 5)), scpexpr(EXPR_END)), "loc_167D")

    ChrTalk(    #52
        0x9,
        (
            "Hi there, bracers! How goes the\x01",
            "investigation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x9,
        "We should be finished cleaning soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x9,
        (
            "I'm hoping to have us all squared\x01",
            "away again by this evening.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_171B")

    label("loc_167D")


    ChrTalk(    #55
        0x9,
        (
            "Chelsey'd mentioned something\x01",
            "about spotting a suspicious figure\x01",
            "yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x9,
        (
            "He's cleaning up on the roof, so you\x01",
            "should go ask him for the details.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_171B")

    OP_A2(0x1)

    label("loc_171E")

    Jump("loc_1814")

    label("loc_1721")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_1814")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_17BD")

    ChrTalk(    #57
        0x9,
        (
            "If you climb the stairs in the back, you\x01",
            "can reach the top of the Ahnenburg Wall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x9,
        (
            "It's a real hot spot for tourists\x01",
            "swinging by.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1814")

    label("loc_17BD")


    ChrTalk(    #59
        0x9,
        "Oh, welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x9,
        (
            "Should you need an explanation\x01",
            "of facilities here, just ask.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1814")

    TalkEnd(0x9)
    Return()

    # Function_10_11D4 end

    def Function_11_1818(): pass

    label("Function_11_1818")

    Call(0, 12)
    Return()

    # Function_11_1818 end

    def Function_12_181D(): pass

    label("Function_12_181D")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_18A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_186C")

    ChrTalk(    #61
        0xD,
        "Cleanup is DONE! YES!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xD,
        "Man, oh, man! What a mess.\x02",
    )

    CloseMessageWindow()
    Jump("loc_18A0")

    label("loc_186C")


    ChrTalk(    #63
        0xD,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xD,
        "Feel free to pass on through.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_18A0")

    Jump("loc_1CEA")

    label("loc_18A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_19D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1937")

    ChrTalk(    #65
        0xD,
        (
            "Going to service every now and\x01",
            "again helps calm my nerves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xD,
        (
            "Maybe for my next day off, I should\x01",
            "go pray at the cathedral.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19D5")

    label("loc_1937")


    ChrTalk(    #67
        0xD,
        (
            "What better time is there to pray to\x01",
            "Aidios than with these earthquakes\x01",
            "going on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xD,
        (
            "We just have to remember: even these\x01",
            "earthquakes are Her will.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_19D5")

    Jump("loc_1CEA")

    label("loc_19D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1AEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1A68")

    ChrTalk(    #69
        0xD,
        (
            "The priest offered to help\x01",
            "of his own accord.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xD,
        (
            "He may be young, but he's a real man\x01",
            "of the cloth through and through.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AE7")

    label("loc_1A68")


    ChrTalk(    #71
        0xD,
        (
            "*pheeew* And that takes care of\x01",
            "the cleaning!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xD,
        (
            "All thanks to the priest helping out.\x01",
            "Talk about holy intervention!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1AE7")

    Jump("loc_1CEA")

    label("loc_1AEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_1BC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1B69")

    ChrTalk(    #73
        0xD,
        "Those tremors were incredible!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xD,
        (
            "Not that I'm upset, but it's almost\x01",
            "strange that nobody was injured.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BC0")

    label("loc_1B69")


    ChrTalk(    #75
        0xD,
        "What a mess, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xD,
        (
            "The tremors from that earthquake\x01",
            "were something else.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1BC0")

    Jump("loc_1CEA")

    label("loc_1BC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_1CEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1C74")

    ChrTalk(    #77
        0xD,
        (
            "The birthday celebrations are over,\x01",
            "so there haven't been many tourists\x01",
            "lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xD,
        (
            "Makes my job nice and easy, though,\x01",
            "so I can't say I mind it one bit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CEA")

    label("loc_1C74")


    ChrTalk(    #79
        0xD,
        "Welcome to the Sanktheim Gate!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xD,
        (
            "Since you're here, why not admire the\x01",
            "Ahnenburg Wall as you pass through?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1CEA")

    TalkEnd(0xD)
    Return()

    # Function_12_181D end

    def Function_13_1CEE(): pass

    label("Function_13_1CEE")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_1E05")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1DA5")

    ChrTalk(    #81
        0xA,
        (
            "Oooooh! I can't stop dreaming\x01",
            "of my future husband...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xA,
        (
            "And that priest is EVERY bit the\x01",
            "dreamboat I've been searching\x01",
            "for. ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xA,
        "Augh! It's terrible...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E02")

    label("loc_1DA5")


    ChrTalk(    #84
        0xA,
        "I have the WORST luck with men.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xA,
        (
            "What must I do to turn this tragic\x01",
            "fate around?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1E02")

    Jump("loc_229C")

    label("loc_1E05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1FDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1ED4")

    ChrTalk(    #86
        0xA,
        (
            "Aaah... His face is sooo perfect when\x01",
            "he's praying...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xA,
        (
            "I can feel Aidios' presence just emanating\x01",
            "through him. I should know--I stare at him\x01",
            "for aaaages whenever he's praying. Hee!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FDA")

    label("loc_1ED4")


    ChrTalk(    #88
        0xA,
        (
            "Everyone was talking about how this\x01",
            "young priest was visiting, so I came by\x01",
            "to loo--er, PRAY. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xA,
        (
            "And, Sweet Aidios, JACKPOT. He's not\x01",
            "just young--he's SUPER handsome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xA,
        (
            "If that hot piece was MY priest, I'd be\x01",
            "coming to church every single day.  ㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1FDA")

    Jump("loc_229C")

    label("loc_1FDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_214C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_209B")

    ChrTalk(    #91
        0xA,
        (
            "I know I fall for guys easily, but I'm\x01",
            "just as quick to give up and move on\x01",
            "to the next one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xA,
        (
            "Teehee! What's the harm in indulging\x01",
            "love in all its wonderful forms?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2149")

    label("loc_209B")


    ChrTalk(    #93
        0xA,
        (
            "Awww. It's such a pity. He was really\x01",
            "cool, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xA,
        (
            "But if he's a wanted man, there's not\x01",
            "much I can do, even if he IS hot.\x01",
            "Time to move on to the next one, I say!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_2149")

    Jump("loc_229C")

    label("loc_214C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_21AC")

    ChrTalk(    #95
        0xA,
        (
            "*sigh* No matter how much I clean\x01",
            "and clean, it never ends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xA,
        "Ugh, I hate it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_229C")

    label("loc_21AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_229C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_226D")

    ChrTalk(    #97
        0xA,
        (
            "The birthday celebrations are over,\x01",
            "so it's back to having nothing to do\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xA,
        (
            "I'm sure management hates it,\x01",
            "but far be it from me to complain\x01",
            "about taking it easy!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_229C")

    label("loc_226D")


    ChrTalk(    #99
        0xA,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xA,
        "Sit wherever you'd like.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_229C")

    TalkEnd(0xA)
    Return()

    # Function_13_1CEE end

    def Function_14_22A0(): pass

    label("Function_14_22A0")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2462")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_232B")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0xAD)
    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_232B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_243F")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2405")
    SubMira(1200)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #101
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23F7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x7)"), scpexpr(EXPR_END)), "loc_23C6")
    Jump("loc_23F7")

    label("loc_23C6")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #102
        "\x06Learned [#2CMacho Meat Stew#0C] recipe.\x02",
    )

    CloseMessageWindow()

    label("loc_23F7")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_242D")

    label("loc_2405")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #103
        "Insufficient mira.\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_242D")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xB)
    Return()

    label("loc_243F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2459")
    FadeToBright(300, 0)
    TalkEnd(0xB)
    Return()

    label("loc_2459")

    FadeToBright(300, 0)

    label("loc_2462")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_2545")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_24A7")

    ChrTalk(    #104
        0xFE,
        "Damn it, Tammy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        "Get BACK HERE, already!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2542")

    label("loc_24A7")


    ChrTalk(    #106
        0xFE,
        (
            "Welcome, welcome! I'd be happy\x01",
            "to take your order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "The waitress isn't here for some\x01",
            "reason, so not like I have a choice\x01",
            "in the matter anyway.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2542")

    Jump("loc_29C5")

    label("loc_2545")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_26CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_25E0")

    ChrTalk(    #108
        0xFE,
        (
            "I've been working here for what\x01",
            "feels like forever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "And yet my heart still bursts with\x01",
            "excitement when a customer eats\x01",
            "my food.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26CB")

    label("loc_25E0")


    ChrTalk(    #110
        0xFE,
        (
            "I've been working here for what\x01",
            "feels like forever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "And yet my heart still bursts with\x01",
            "excitement when a customer eats\x01",
            "my food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "That's why I always work with my\x01",
            "back facing everyone. My face would\x01",
            "give me right away.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_26CB")

    Jump("loc_29C5")

    label("loc_26CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_2738")

    ChrTalk(    #113
        0xFE,
        "Heeey there! Done talkin'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "If you are, go ahead and take\x01",
            "a break here, if you'd like.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29C5")

    label("loc_2738")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_28A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 5)), scpexpr(EXPR_END)), "loc_27FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2783")

    ChrTalk(    #115
        0xFE,
        (
            "Welcome! We're open for business!\x01",
            "...Somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27FC")

    label("loc_2783")


    ChrTalk(    #116
        0xFE,
        (
            "Welcome! We're open for business!\x01",
            "...Somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "Go ahead and try out our new menu.\x01",
            "You won't be disappointed!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_27FC")

    Jump("loc_289D")

    label("loc_27FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_282B")

    ChrTalk(    #118
        0xFE,
        "*sigh* This is a disaster...\x02",
    )

    CloseMessageWindow()
    Jump("loc_289D")

    label("loc_282B")


    ChrTalk(    #119
        0xFE,
        "*sigh* This is a disaster...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "No way I can keep the business\x01",
            "open without cleaning up a little\x01",
            "first.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_289D")

    Jump("loc_29C5")

    label("loc_28A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_29C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2961")

    ChrTalk(    #121
        0xB,
        (
            "There's not too much to do here\x01",
            "after the birthday celebrations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xB,
        (
            "I've been so bored out of my mind,\x01",
            "I decided to come up with a brand\x01",
            "new recipe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xB,
        "Go on! Try it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_29C5")

    label("loc_2961")


    ChrTalk(    #124
        0xB,
        "Welcome to the cafeteria!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xB,
        (
            "Have a seat anywhere you'd like,\x01",
            "and I'll be right with you.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_29C5")

    TalkEnd(0xB)
    Return()

    # Function_14_22A0 end

    def Function_15_29C9(): pass

    label("Function_15_29C9")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_2B97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2A57")

    ChrTalk(    #126
        0xFE,
        (
            "I will be at the cathedral, so feel free\x01",
            "to come by any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "I'm very sorry, but I'd best be returning\x01",
            "soon...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B94")

    label("loc_2A57")


    ChrTalk(    #128
        0xFE,
        (
            "I can understand your troubles as\x01",
            "if they were my own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "However, the answer to this kind of\x01",
            "problem always lies within.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "I do have an idea on what could be\x01",
            "preventing you from meeting your\x01",
            "future spouse. Will you hear me out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "Perhaps this 'ideal man' you seek\x01",
            "is nothing more than a false image?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_2B94")

    Jump("loc_3023")

    label("loc_2B97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_2D1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2C5F")

    ChrTalk(    #132
        0xFE,
        "I shall pray again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "Please, let light shine on the path\x01",
            "beneath our feet when we stray...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "Please, protect us from the darkness\x01",
            "that lies in the depths of our hearts...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D1A")

    label("loc_2C5F")


    ChrTalk(    #135
        0xFE,
        "Goddess of the sky, Aidios...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "I ask you grant your protection to\x01",
            "those gathered here before you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "And, I ask you to watch over us to\x01",
            "the end from your grand heights...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_2D1A")

    Jump("loc_3023")

    label("loc_2D1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_2E3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2D97")

    ChrTalk(    #138
        0xFE,
        "We've managed to clean everything up...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "With that done, I should like to resume\x01",
            "services soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E3B")

    label("loc_2D97")


    ChrTalk(    #140
        0xFE,
        "We've managed to clean everything up...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "I must say, however, that these vestments\x01",
            "are not well suited to exercise. I've worked\x01",
            "up quite a sweat! Haha.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_2E3B")

    Jump("loc_3023")

    label("loc_2E3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_2F04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2E9C")

    ChrTalk(    #142
        0xFE,
        "Still, this is a terrible mess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        "I hope they'll allow me to help...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F01")

    label("loc_2E9C")


    ChrTalk(    #144
        0xFE,
        (
            "It brings me great joy to say that\x01",
            "no one was injured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        "Every cloud has a silver lining.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_2F01")

    Jump("loc_3023")

    label("loc_2F04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_3023")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2F80")

    ChrTalk(    #146
        0xE,
        (
            "It seems the soldiers are well\x01",
            "dedicated to their tasks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xE,
        "I will take the time to wait for a bit.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3023")

    label("loc_2F80")


    ChrTalk(    #148
        0xE,
        (
            "I came from the cathedral to lead\x01",
            "the soldiers in prayer, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xE,
        "No one has come yet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xE,
        (
            "It seems everyone is dedicating\x01",
            "themselves to their tasks.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_3023")

    TalkEnd(0xE)
    Return()

    # Function_15_29C9 end

    def Function_16_3027(): pass

    label("Function_16_3027")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_3097")

    ChrTalk(    #151
        0xFE,
        (
            "There's more people here at service\x01",
            "than normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        "Probably thanks to the earthquake, huh.\x02",
    )

    CloseMessageWindow()
    Jump("loc_32E7")

    label("loc_3097")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_31D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_311B")

    ChrTalk(    #153
        0xFE,
        "Phew! Finally done.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "Since a priest's come all the way from the\x01",
            "capital, I should probably go to service.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31D4")

    label("loc_311B")


    ChrTalk(    #155
        0xFE,
        "Phew! Finally done.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        (
            "We cleaned up faster than expected\x01",
            "since everyone helped out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "Since a priest's come all the way from the\x01",
            "capital, I should probably go to service.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_31D4")

    Jump("loc_32E7")

    label("loc_31D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_32E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3267")

    ChrTalk(    #158
        0xFE,
        (
            "My post's outside, but we've got a bit\x01",
            "of an unexpected situation, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        "I'm away from post helping out inside.\x02",
    )

    CloseMessageWindow()
    Jump("loc_32E7")

    label("loc_3267")


    ChrTalk(    #160
        0xFE,
        (
            "Seems like stuff's collapsed\x01",
            "all over the guard post.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "It'll be hard to guard anything until\x01",
            "we clean this mess up.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_32E7")

    TalkEnd(0xF)
    Return()

    # Function_16_3027 end

    def Function_17_32EB(): pass

    label("Function_17_32EB")

    Call(0, 18)
    Return()

    # Function_17_32EB end

    def Function_18_32F0(): pass

    label("Function_18_32F0")

    OP_EA(0x1, 0xB, 0x0, 0x0)
    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_33F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_337B")

    ChrTalk(    #162
        0x10,
        (
            "I really don't want to throw away\x01",
            "my life in a place like this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x10,
        "A-Anyway let's get back to the capital!\x02",
    )

    CloseMessageWindow()
    Jump("loc_33F2")

    label("loc_337B")


    ChrTalk(    #164
        0x10,
        (
            "I-I don't really want to throw away\x01",
            "my life in a place like this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x10,
        "A-Anyway let's get back to the capital!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_33F2")

    Jump("loc_36A9")

    label("loc_33F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_3538")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_3472")

    ChrTalk(    #166
        0x10,
        (
            "Lying down like this is just making\x01",
            "me irritated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x10,
        "Do I really want to waste my days like this...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3535")

    label("loc_3472")


    ChrTalk(    #168
        0x10,
        (
            "Lying down like this is just making\x01",
            "me irritated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x10,
        "D-Do I really want to waste my days like this...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x10,
        (
            "When I came to my senses, I was so scared.\x01",
            "I thought I was a goner for sure.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_3535")

    Jump("loc_36A9")

    label("loc_3538")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_36A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_3596")

    ChrTalk(    #171
        0x10,
        "Ahh, Ricky, tell me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x10,
        "What on earth is the meaning of my existence?\x02",
    )

    CloseMessageWindow()
    Jump("loc_36A9")

    label("loc_3596")


    ChrTalk(    #173
        0x10,
        (
            "The birthday celebration comes and all I have to\x01",
            "show is a broken heart... Then an earthquake\x01",
            "comes and all I get is nearly dying...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x10,
        (
            "How pitiful...\x01",
            "I haven't even the will to stand up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x10,
        "Ahh, Ricky, tell me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x10,
        "What on earth is the meaning of my existence?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_36A9")

    TalkEnd(0x10)
    Return()

    # Function_18_32F0 end

    def Function_19_36AD(): pass

    label("Function_19_36AD")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_37A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_372B")

    ChrTalk(    #177
        0xFE,
        (
            "Calm down, Anton.\x01",
            "No point in freaking out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "Well, I'm just glad you've\x01",
            "gotten your energy back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_379F")

    label("loc_372B")


    ChrTalk(    #179
        0xFE,
        (
            "Calm down, Anton.\x01",
            "No point in freaking out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "Well, either way, I'd planned\x01",
            "on returning to the capital.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_379F")

    Jump("loc_39F8")

    label("loc_37A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_38A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_37EE")

    ChrTalk(    #181
        0xFE,
        (
            "Seems like Anton's starting to get bored\x01",
            "of this too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_389E")

    label("loc_37EE")


    ChrTalk(    #182
        0xFE,
        (
            "The floor here isn't real well suited\x01",
            "to sleeping on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "Ideally, this'd be the elevated\x01",
            "gardens in the royal castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        "I bet the grass there'd be perfectly soft.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_389E")

    Jump("loc_39F8")

    label("loc_38A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_39F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_3987")

    ChrTalk(    #185
        0xFE,
        (
            "Sorry. I know we're making\x01",
            "it hard to use the hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        (
            "To spontaneously embark on little soul-searching\x01",
            "trips is my friend's bad habit, I'm afraid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        (
            "Don't worry, he'll eventually get bored\x01",
            "and recover.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39F8")

    label("loc_3987")


    ChrTalk(    #188
        0xFE,
        "Anton...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "It's pretty clear what your raison d'etre is\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        "... Yes, you are a roadblock.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_39F8")

    TalkEnd(0x13)
    Return()

    # Function_19_36AD end

    def Function_20_39FC(): pass

    label("Function_20_39FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A0D")
    Call(0, 22)

    label("loc_3A0D")

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
            "#6PWhat the hell is with you\x01",
            "fool bracers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x8,
        (
            "#6PCan't you see we're in the middle\x01",
            "of clean-up after the earthquake?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x8,
        (
            "#6PIf you have to nose around,\x01",
            "I'd prefer you do it later.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3C1C")

    ChrTalk(    #194
        0x106,
        (
            "#053F#6PSorry, sir, but this is our job.\x02\x03",

            "#050FWe won't get in the way of the clean-up.\x01",
            "Do you mind if we do a little questioning?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CB7")

    label("loc_3C1C")


    ChrTalk(    #195
        0x103,
        (
            "#027F#6PI'm afraid this is our job, sir,\x01",
            "clean-up or no.\x02\x03",

            "You have my word we won't get\x01",
            "in the way. May we ask a few\x01",
            "questions of the gate residents?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CB7")


    ChrTalk(    #196
        0x8,
        (
            "#6PTch. If HQ hadn't ordered it,\x01",
            "I'd tell you lot to clear out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x8,
        (
            "#6PI've got some urgent business to take\x01",
            "care of. You can get the details from my\x01",
            "second-in-command, Warrant Officer Talbot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x8,
        (
            "#6PHe's in the storage area over\x01",
            "there, cleaning up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x101,
        "#1006F#4POkay, we'll talk to him. Thanks!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x8,
        (
            "#6PJust make damn sure you don't interfere\x01",
            "with any actual work going on here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x8,
        "#6PNow if you'll excuse me...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 600)

    def lambda_3E6B():
        OP_8E(0x8, 0x58C0, 0x0, 0x96A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3E6B)

    def lambda_3E86():
        OP_6D(18030, 0, 2160, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3E86)

    def lambda_3E9E():
        OP_67(0, 8000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3E9E)

    def lambda_3EB6():

        label("loc_3EB6")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_3EB6")

    QueueWorkItem2(0x101, 1, lambda_3EB6)

    def lambda_3EC7():

        label("loc_3EC7")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_3EC7")

    QueueWorkItem2(0xF7, 1, lambda_3EC7)

    def lambda_3ED8():

        label("loc_3ED8")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_3ED8")

    QueueWorkItem2(0x105, 1, lambda_3ED8)

    def lambda_3EE9():

        label("loc_3EE9")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_3EE9")

    QueueWorkItem2(0x104, 1, lambda_3EE9)
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

    def lambda_3F84():
        OP_6D(6550, 0, 600, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3F84)

    def lambda_3F9C():
        OP_67(0, 8000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3F9C)
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
            "#1015F#6PWhoa, it, uh, really IS kind of bad in here.\x02\x03",

            "Do you think we should help out a little?\x01",
            "I mean, just to be friendly?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4131")

    ChrTalk(    #203
        0x106,
        (
            "#053F#6PTo be honest, I'd keep your hands to yourself.\x02\x03",

            "#050FThis IS a military facility, remember.\x01",
            "There might be secret documents or something\x01",
            "scattered around that we aren't supposed to see.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_420B")

    label("loc_4131")


    ChrTalk(    #204
        0x103,
        (
            "#020F#6PThis IS a military facility, Estelle. I'd suggest\x01",
            "we simply finish our business and go.\x02\x03",

            "There may be secret documents or some\x01",
            "such in this mess that the military doesn't\x01",
            "want us 'lowly civilians' to see.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_420B")


    ChrTalk(    #205
        0x101,
        "#1007F#6POh... Yeah, good point, I guess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x105,
        (
            "#043FStill, this is...quite a bit more damage\x01",
            "than the City of Zeiss earthquake, isn't it?\x02\x03",

            "That didn't cause nearly as\x01",
            "much of a mess...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x104,
        (
            "#6P#035FThe ferocity of the quake should\x01",
            "be a primary line of inquiry, then.\x02\x03",

            "#030FAs well as asking about our mystery man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x101,
        (
            "#1002F#6PYeah, that guy in the sunglasses.\x02\x03",

            "Well, first things first. Let's talk to\x01",
            "that second-in-command guy.\x02",
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

    # Function_20_39FC end

    def Function_21_4483(): pass

    label("Function_21_4483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_449D")
    Call(0, 22)
    FadeToBright(0, 0)

    label("loc_449D")

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
            "#3PCrap... This is going to\x01",
            "be such a pain to clean up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x9,
        (
            "#3PDale'll have my hide if it isn't\x01",
            "done by nightfall, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x101,
        (
            "#1011F#7PUm, excuse me!\x01",
            "Sorry to disturb you.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x9, 180, 400)

    ChrTalk(    #212
        0x9,
        "#3PHmm? And you are?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #213
        (
            "\x07\x05Estelle and company introduced themselves as\x01",
            "bracers, and explained they were investigating\x01",
            "the earthquake.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #214
        0x9,
        (
            "#3PAh, I see. Thanks for the concern, even\x01",
            "if Dale doesn't share my thanks!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x9,
        (
            "#3PSo you want to know what the situation\x01",
            "was like when the earthquake happened,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_47AA")

    ChrTalk(    #216
        0x106,
        (
            "#050F#6PYeah, in as much detail\x01",
            "as you can give us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47D9")

    label("loc_47AA")


    ChrTalk(    #217
        0x103,
        "#020F#6PYes, and please, spare no detail.\x02",
    )

    CloseMessageWindow()

    label("loc_47D9")


    ChrTalk(    #218
        0x9,
        "#3PUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x9,
        (
            "#3PThe earthquake began at roughly\x01",
            "1300 hours--two hours ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x9,
        (
            "#3PThe earthquake lasted around thirty\x01",
            "seconds and was strong enough to\x01",
            "knock down big, piled-up boxes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x101,
        (
            "#1004F#7PWait, so, compared to the\x01",
            "quake at the Wolf Fort...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #222
        (
            "\x18\x07\x05What made this earthquake different\x01",
            "from the one at the Wolf Fort?\x02",
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "The Shaking Was Stronger\x01",      # 0
            "It Lasted Longer\x01",              # 1
            "Both\x01",                          # 2
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
        (0, "loc_49BF"),
        (1, "loc_4A0C"),
        (2, "loc_4A5B"),
        (SWITCH_DEFAULT, "loc_4AB7"),
    )


    label("loc_49BF")

    OP_2B(0x85, 0x1)

    ChrTalk(    #223
        0x105,
        (
            "#043FYes, that's true...\x02\x03",

            "But it shook for longer too, I think.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AB7")

    label("loc_4A0C")

    OP_2B(0x85, 0x1)

    ChrTalk(    #224
        0x105,
        (
            "#043FYes, that's true...\x02\x03",

            "But it was stronger here, too, I think.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AB7")

    label("loc_4A5B")

    OP_2B(0x85, 0x3)

    ChrTalk(    #225
        0x105,
        (
            "#047FYes.\x02\x03",

            "#042FThe entire earthquake was worse--\x01",
            "stronger and longer lasting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AB7")

    label("loc_4AB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4B22")

    ChrTalk(    #226
        0x106,
        (
            "#555F#6PAnd then there was that one in the city.\x02\x03",

            "That'd fall about in the middle, I guess.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B9B")

    label("loc_4B22")


    ChrTalk(    #227
        0x103,
        (
            "#022F#6PAnd then there was the one\x01",
            "which welcomed us to Zeiss.\x02\x03",

            "That would, I think, fall in between\x01",
            "the other two.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B9B")


    ChrTalk(    #228
        0x104,
        (
            "#035F#2PMeaning, then, that the quakes are\x01",
            "getting more powerful each time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x101,
        "#1020F#7PThat's, uh...kinda BAD, isn't it?!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 400)

    ChrTalk(    #230
        0x9,
        "#3PThe situation does seem to be worsening...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x9,
        (
            "#3PBut these are natural occurrences.\x01",
            "I don't see how we could stop them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x9,
        (
            "#3PI don't suppose the Bracer Guild\x01",
            "has any ideas?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x101,
        (
            "#1007F#7PUm, well, we're not really sure yet,\x01",
            "but we're, uh, pursuing a few leads.\x02\x03",

            "#1002FSpeaking of which...did anything,\x01",
            "um...weird happen before or after\x01",
            "the earthquake?\x02\x03",

            "Like, were there any suspicious\x01",
            "people walking around?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x9,
        "#3PSuspicious people? Hmm.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x9,
        (
            "#3PCome to think of it, Chesley mentioned\x01",
            "something about a strange man yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x9,
        (
            "#3PHe's cleaning the roof, if you want\x01",
            "to hear the details from him.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4EC5")

    ChrTalk(    #237
        0x106,
        (
            "#051F#PChesley on the roof, right?\x01",
            "Thanks!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EF2")

    label("loc_4EC5")


    ChrTalk(    #238
        0x103,
        (
            "#020F#6PChesley on the roof?\x01",
            "Very well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EF2")


    ChrTalk(    #239
        0x101,
        "#1006F#7PThanks for helping us out, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x9,
        "#3PNot at all. Good luck!\x02",
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

    # Function_21_4483 end

    def Function_22_4F61(): pass

    label("Function_22_4F61")

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
        (0, "loc_4FDA"),
        (1, "loc_4FE0"),
        (SWITCH_DEFAULT, "loc_4FE6"),
    )


    label("loc_4FDA")

    OP_A2(0x1200)
    Jump("loc_4FE6")

    label("loc_4FE0")

    OP_A2(0x1201)
    Jump("loc_4FE6")

    label("loc_4FE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_4FF4")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_4FF8")

    label("loc_4FF4")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_4FF8")

    Return()

    # Function_22_4F61 end

    def Function_23_4FF9(): pass

    label("Function_23_4FF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_51B3")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_507C")

    ChrTalk(    #241
        0x101,
        (
            "#1000FWe don't have any business on the capital side.\x01",
            "Let's hurry up and finish our questioning.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5195")

    label("loc_507C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5111")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5099")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_50A0")

    label("loc_5099")

    TurnDirection(0x106, 0x0, 400)

    label("loc_50A0")


    ChrTalk(    #242
        0x106,
        (
            "#050FWe don't have any business with the capital side.\x01",
            "Let's just hurry up and finish our investigation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5195")

    label("loc_5111")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5127")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_512E")

    label("loc_5127")

    TurnDirection(0x103, 0x0, 400)

    label("loc_512E")


    ChrTalk(    #243
        0x103,
        (
            "#027FWe don't have anything to do on the capital side.\x01",
            "Let's just quickly finish our questioning.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5195")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_530E")

    label("loc_51B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_530E")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5255")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51DE")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_51E5")

    label("loc_51DE")

    TurnDirection(0x106, 0x0, 400)

    label("loc_51E5")


    ChrTalk(    #244
        0x106,
        (
            "#050FPast here's the Grancel region.\x02\x03",

            "We ain't got time to visit other regions.\x01",
            "Let's just turn around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52EE")

    label("loc_5255")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_526B")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_5272")

    label("loc_526B")

    TurnDirection(0x103, 0x0, 400)

    label("loc_5272")


    ChrTalk(    #245
        0x103,
        (
            "#020FPast this point is the Grancel region.\x02\x03",

            "We don't have time to go to the other\x01",
            "regions. Let's just return for now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52EE")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)

    label("loc_530E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56EA")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5429")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_539D")

    ChrTalk(    #246
        0x108,
        (
            "#070FAs I recall, Kilika arranged air tickets for us.\x02\x03",

            "Let's ride the airships to get to the capital.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5426")

    label("loc_539D")


    ChrTalk(    #247
        0x108,
        (
            "#070FPast here is the capital.\x02\x03",

            "As I recall, Kilika arranged air tickets for us.\x02\x03",

            "Let's ride the airships to get to the capital.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_5426")

    Jump("loc_56CF")

    label("loc_5429")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5584")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5446")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_544D")

    label("loc_5446")

    TurnDirection(0x106, 0x0, 400)

    label("loc_544D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_54B0")

    ChrTalk(    #248
        0x106,
        (
            "#050FKilika should have tickets ready for us.\x02\x03",

            "Let's go via airship to the capital.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5581")

    label("loc_54B0")


    ChrTalk(    #249
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

    label("loc_5581")

    Jump("loc_56CF")

    label("loc_5584")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_559A")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_55A1")

    label("loc_559A")

    TurnDirection(0x103, 0x0, 400)

    label("loc_55A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_560F")

    ChrTalk(    #250
        0x103,
        (
            "#020FKilika should have tickets already\x01",
            "prepared for us.\x02\x03",

            "Let's go via airship to the capital.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56CF")

    label("loc_560F")


    ChrTalk(    #251
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

    label("loc_56CF")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_56EA")

    Return()

    # Function_23_4FF9 end

    def Function_24_56EB(): pass

    label("Function_24_56EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58C6")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_577D")

    ChrTalk(    #252
        0x103,
        (
            "#070FAh, past here's the Zeiss region.\x02\x03",

            "We don't have time to stop in at other\x01",
            "regions. Let's just turn around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58AB")

    label("loc_577D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_581A")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_579A")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_57A1")

    label("loc_579A")

    TurnDirection(0x106, 0x0, 400)

    label("loc_57A1")


    ChrTalk(    #253
        0x106,
        (
            "#050FLooks like Zeiss is this way.\x02\x03",

            "We don't have time to hang around the\x01",
            "other regions. Let's just turn around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58AB")

    label("loc_581A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5830")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_5837")

    label("loc_5830")

    TurnDirection(0x103, 0x0, 400)

    label("loc_5837")


    ChrTalk(    #254
        0x103,
        (
            "#020FPast here is the Zeiss region.\x02\x03",

            "We don't have time to go to the other\x01",
            "regions. Let's just return for now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58AB")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_58C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_59AE")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_593B")

    ChrTalk(    #255
        0x101,
        (
            "#1002FWe don't have time to waste on side trips.\x01",
            "...Let's hurry back to the guild.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5993")

    label("loc_593B")


    ChrTalk(    #256
        0x109,
        (
            "#1063FWe don't have time to waste... We have\x01",
            "to hurry to the guild in the capital.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5993")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_59AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5CEC")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_5A55")

    ChrTalk(    #257
        0x108,
        (
            "#070FWalking is good training, but it's\x01",
            "also a waste of time.\x02\x03",

            "If we're going to Bose, the wise\x01",
            "choice is to use the airship.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AF3")

    label("loc_5A55")


    ChrTalk(    #258
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

    label("loc_5AF3")

    Jump("loc_5CD1")

    label("loc_5AF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5BE3")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B13")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_5B1A")

    label("loc_5B13")

    TurnDirection(0x106, 0x0, 400)

    label("loc_5B1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_5B88")

    ChrTalk(    #259
        0x106,
        (
            "#053FWalking is a waste of time.\x02\x03",

            "#050FIf we're going to Bose, let's\x01",
            "head to the landing port.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5BE0")

    label("loc_5B88")


    ChrTalk(    #260
        0x106,
        (
            "#050FThis way's Zeiss.\x02\x03",

            "If we're going to Bose, let's\x01",
            "head to the landing port.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_5BE0")

    Jump("loc_5CD1")

    label("loc_5BE3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BF9")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_5C00")

    label("loc_5BF9")

    TurnDirection(0x103, 0x0, 400)

    label("loc_5C00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_5C78")

    ChrTalk(    #261
        0x103,
        (
            "#026FWalking is, frankly, a waste of time.\x02\x03",

            "#020FIf we're going to Bose, let's\x01",
            "head to the landing port.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CD1")

    label("loc_5C78")


    ChrTalk(    #262
        0x103,
        (
            "#020FThis way is Zeiss.\x02\x03",

            "If we're going to Bose, let's\x01",
            "head to the landing port.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_5CD1")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_5CEC")

    Return()

    # Function_24_56EB end

    def Function_25_5CED(): pass

    label("Function_25_5CED")

    TalkBegin(0xFF)
    Sleep(400)
    TalkEnd(0xFF)
    Return()

    # Function_25_5CED end

    SaveToFile()

Try(main)
