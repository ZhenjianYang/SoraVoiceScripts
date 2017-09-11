from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2101   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T2101   ._SN',
            'ED6_DT01/T2101_1 ._SN',
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
        'Deen',                                 # 9
        'Rais',                                 # 10
        'Rocco',                                # 11
        'Picaro',                               # 12
        'Mayor Dalmore',                        # 13
        'Steward Gilbert',                      # 14
        'Sieg',                                 # 15
        'Harg',                                 # 16
        'Camera',                               # 17
        'Benoit',                               # 18
        'Nial',                                 # 19
        'Simon',                                # 20
        'Portos',                               # 21
        'Kuper',                                # 22
        'Brenda',                               # 23
        'Boat',                                 # 24
        'Portos',                               # 25
        'Aurian Causeway',                      # 26
        'Ruan - North Block',                   # 27
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
        'ED6_DT07/CH01390 ._CH',             # 00
        'ED6_DT07/CH02410 ._CH',             # 01
        'ED6_DT07/CH02420 ._CH',             # 02
        'ED6_DT07/CH02320 ._CH',             # 03
        'ED6_DT07/CH01020 ._CH',             # 04
        'ED6_DT07/CH02063 ._CH',             # 05
        'ED6_DT07/CH01140 ._CH',             # 06
        'ED6_DT07/CH01680 ._CH',             # 07
        'ED6_DT07/CH01500 ._CH',             # 08
        'ED6_DT07/CH01460 ._CH',             # 09
        'ED6_DT07/CH01110 ._CH',             # 0A
        'ED6_DT07/CH02510 ._CH',             # 0B
        'ED6_DT07/CH02520 ._CH',             # 0C
        'ED6_DT07/CH02530 ._CH',             # 0D
        'ED6_DT06/CH20051 ._CH',             # 0E
        'ED6_DT06/CH20161 ._CH',             # 0F
    )

    AddCharChipPat(
        'ED6_DT07/CH01390P._CP',             # 00
        'ED6_DT07/CH02410P._CP',             # 01
        'ED6_DT07/CH02420P._CP',             # 02
        'ED6_DT07/CH02320P._CP',             # 03
        'ED6_DT07/CH01020P._CP',             # 04
        'ED6_DT07/CH02063P._CP',             # 05
        'ED6_DT07/CH01140P._CP',             # 06
        'ED6_DT07/CH01680P._CP',             # 07
        'ED6_DT07/CH01500P._CP',             # 08
        'ED6_DT07/CH01460P._CP',             # 09
        'ED6_DT07/CH01110P._CP',             # 0A
        'ED6_DT07/CH02510P._CP',             # 0B
        'ED6_DT07/CH02520P._CP',             # 0C
        'ED6_DT07/CH02530P._CP',             # 0D
        'ED6_DT06/CH20051P._CP',             # 0E
        'ED6_DT06/CH20161P._CP',             # 0F
    )

    DeclNpc(
        X                   = 1200,
        Z                   = 4000,
        Y                   = 16700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1200,
        Z                   = 4000,
        Y                   = 16700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1200,
        Z                   = 4000,
        Y                   = 16700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 49950,
        Z                   = 1000,
        Y                   = 2460,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 1200,
        Z                   = 4000,
        Y                   = 16700,
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
        X                   = 1200,
        Z                   = 4000,
        Y                   = 16700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 800,
        Z                   = 6000,
        Y                   = -13810,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4620,
        Z                   = -1800,
        Y                   = 22750,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 0,
    )

    DeclNpc(
        X                   = 800,
        Z                   = 6000,
        Y                   = -13810,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 15900,
        Z                   = -1800,
        Y                   = 25200,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 65090,
        Z                   = -1700,
        Y                   = 32900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 24700,
        Z                   = 0,
        Y                   = 24500,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 20070,
        Z                   = 0,
        Y                   = 26530,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 7100,
        Z                   = 0,
        Y                   = 28900,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 58900,
        Z                   = 0,
        Y                   = 29500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
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

    DeclNpc(
        X                   = 23560,
        Z                   = 1000,
        Y                   = 1760,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 73210,
        Z                   = 0,
        Y                   = -16650,
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

    DeclNpc(
        X                   = 50980,
        Z                   = 400,
        Y                   = 77990,
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
        X                   = 32790,
        Y                   = 2000,
        Z                   = 13300,
        Range               = 26260,
        Unknown_10          = 0xFFFFFC18,
        Unknown_14          = 0x2ADA,
        Unknown_18          = 0x0,
        Unknown_1C          = 11,
    )

    DeclEvent(
        X                   = 49000,
        Y                   = 2000,
        Z                   = 26550,
        Range               = 46940,
        Unknown_10          = 0xFFFFFC18,
        Unknown_14          = 0x4B82,
        Unknown_18          = 0x0,
        Unknown_1C          = 12,
    )

    DeclEvent(
        X                   = 76190,
        Y                   = 0,
        Z                   = 0,
        Range               = 70000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFFF830,
        Unknown_18          = 0x0,
        Unknown_1C          = 14,
    )

    DeclEvent(
        X                   = 31200,
        Y                   = 0,
        Z                   = 25340,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 17,
    )

    DeclEvent(
        X                   = 77280,
        Y                   = 0,
        Z                   = 22060,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 18,
    )


    DeclActor(
        TriggerX            = 41040,
        TriggerZ            = -1650,
        TriggerY            = 32140,
        TriggerRange        = 1400,
        ActorX              = 41040,
        ActorZ              = -6350,
        ActorY              = 32140,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 17000,
        TriggerZ            = 0,
        TriggerY            = 29200,
        TriggerRange        = 3500,
        ActorX              = 17050,
        ActorZ              = 3500,
        ActorY              = 29200,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 50320,
        TriggerZ            = 1000,
        TriggerY            = 2450,
        TriggerRange        = 800,
        ActorX              = 50320,
        ActorZ              = 2000,
        ActorY              = 2450,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 50320,
        TriggerZ            = 1000,
        TriggerY            = 9400,
        TriggerRange        = 800,
        ActorX              = 50320,
        ActorZ              = 2000,
        ActorY              = 9400,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 31960,
        TriggerZ            = 1000,
        TriggerY            = 3430,
        TriggerRange        = 800,
        ActorX              = 31960,
        ActorZ              = 2000,
        ActorY              = 3430,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 23540,
        TriggerZ            = 1000,
        TriggerY            = 3430,
        TriggerRange        = 800,
        ActorX              = 23540,
        ActorZ              = 2000,
        ActorY              = 3430,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_502",          # 00, 0
        "Function_1_5A6",          # 01, 1
        "Function_2_74D",          # 02, 2
        "Function_3_8CA",          # 03, 3
        "Function_4_B0A",          # 04, 4
        "Function_5_107C",         # 05, 5
        "Function_6_142E",         # 06, 6
        "Function_7_1D96",         # 07, 7
        "Function_8_25E0",         # 08, 8
        "Function_9_2666",         # 09, 9
        "Function_10_29F2",        # 0A, 10
        "Function_11_33FD",        # 0B, 11
        "Function_12_36C6",        # 0C, 12
        "Function_13_5C15",        # 0D, 13
        "Function_14_63FA",        # 0E, 14
        "Function_15_6829",        # 0F, 15
        "Function_16_6878",        # 10, 16
        "Function_17_687F",        # 11, 17
        "Function_18_6883",        # 12, 18
    )


    def Function_0_502(): pass

    label("Function_0_502")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_516")
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8)
    Jump("loc_579")

    label("loc_516")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_53B")
    SetChrPos(0x15, 19270, 0, 30790, 225)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8)
    Jump("loc_579")

    label("loc_53B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_559")
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8)
    Jump("loc_579")

    label("loc_559")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_568")
    ClearChrFlags(0x12, 0x80)
    Jump("loc_579")

    label("loc_568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_579")
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8)

    label("loc_579")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_587")
    OP_A3(0x3FA)
    Event(0, 13)

    label("loc_587")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_594")
    ClearChrFlags(0xB, 0x80)

    label("loc_594")

    OP_51(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_502 end

    def Function_1_5A6(): pass

    label("Function_1_5A6")

    OP_16(0x2, 0xFA0, 0xFFFEA840, 0xFFFE7960, 0x30048)
    OP_72(0x16, 0x10)
    OP_6F(0x16, 60)
    OP_71(0x18, 0x4)
    OP_71(0x19, 0x4)
    OP_71(0x1A, 0x4)
    OP_71(0x1B, 0x4)
    OP_71(0x1C, 0x4)
    OP_71(0x1D, 0x4)
    OP_71(0x1E, 0x4)
    OP_71(0x1F, 0x4)
    OP_72(0x14, 0x10)
    OP_72(0x15, 0x10)
    OP_64(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60E")
    OP_72(0x13, 0x10)
    OP_65(0x2, 0x1)
    Jump("loc_613")

    label("loc_60E")

    OP_1C(0x13, 0x0, 0x10)

    label("loc_613")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x1, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_631")
    OP_64(0x0, 0x1)

    label("loc_631")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x8000)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_650")
    OP_64(0x1, 0x1)

    label("loc_650")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_65A")
    Jump("loc_6E3")

    label("loc_65A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_670")
    OP_6F(0x11, 1020)
    OP_72(0x21, 0x2)
    Jump("loc_6E3")

    label("loc_670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_67A")
    Jump("loc_6E3")

    label("loc_67A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_690")
    OP_6F(0x11, 1020)
    OP_72(0x21, 0x2)
    Jump("loc_6E3")

    label("loc_690")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 2)), scpexpr(EXPR_END)), "loc_6A6")
    OP_6F(0x11, 1020)
    OP_72(0x21, 0x2)
    Jump("loc_6E3")

    label("loc_6A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_6B0")
    Jump("loc_6E3")

    label("loc_6B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_6BA")
    Jump("loc_6E3")

    label("loc_6BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 1)), scpexpr(EXPR_END)), "loc_6D0")
    OP_6F(0x11, 1020)
    OP_72(0x21, 0x2)
    Jump("loc_6E3")

    label("loc_6D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_6E3")
    OP_6F(0x11, 1020)
    OP_72(0x21, 0x2)

    label("loc_6E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_747")
    LoadEffect(0x0, "map\\\\mp022_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 41040, -6550, 32140, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)

    label("loc_747")

    OP_22(0x1C5, 0x1, 0x64)
    Return()

    # Function_1_5A6 end

    def Function_2_74D(): pass

    label("Function_2_74D")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_772")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_8B4")

    label("loc_772")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78B")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_8B4")

    label("loc_78B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A4")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_8B4")

    label("loc_7A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BD")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_8B4")

    label("loc_7BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D6")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_8B4")

    label("loc_7D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7EF")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_8B4")

    label("loc_7EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_808")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_8B4")

    label("loc_808")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_821")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_8B4")

    label("loc_821")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83A")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_8B4")

    label("loc_83A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_853")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_8B4")

    label("loc_853")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86C")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_8B4")

    label("loc_86C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_885")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_8B4")

    label("loc_885")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89E")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_8B4")

    label("loc_89E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B4")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_8B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8C9")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_8B4")

    label("loc_8C9")

    Return()

    # Function_2_74D end

    def Function_3_8CA(): pass

    label("Function_3_8CA")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC8")
    EventBegin(0x0)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #0
        0xFE,
        (
            "What's a bunch of little kids\x01",
            "doin' here?\x02\x03",

            "Hey, this place is off limits!\x02\x03",

            "You brats ain't gettin' in,\x01",
            "so scram!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        (
            "#004FWe never even said we wanted\x01",
            "to come in...\x02\x03",

            "#000FBut, mister...why do you look\x01",
            "so nervous?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "Y-You can tell...?\x02\x03",

            "Never mind!\x01",
            "You're not allowed here!\x02\x03",

            "Just go, already!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x102,
        (
            "#015F(I think we may need to handle\x01",
            "this one with some care...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#009F(Well, he's sure acting strange.\x01",
            "I wonder what's up with him?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x136,
        "#043F(...)\x02",
    )

    CloseMessageWindow()
    OP_A2(0x447)
    OP_A2(0x9)
    EventEnd(0x1)
    Jump("loc_B06")

    label("loc_AC8")


    ChrTalk(    #6
        0xFE,
        (
            "Just go, already!\x02\x03",

            "You brats ain't gettin' in,\x01",
            "so scram!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B06")

    TalkEnd(0xB)
    Return()

    # Function_3_8CA end

    def Function_4_B0A(): pass

    label("Function_4_B0A")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_CF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C44")
    OP_A2(0x4)

    ChrTalk(    #7
        0xFE,
        (
            "Mayor Dalmore took tourism\x01",
            "waaaaay too seriously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "I knew he'd never buy replacements\x01",
            "for our equipment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "A real mayor would do what's\x01",
            "best for his citizens, NOT\x01",
            "what makes him the most money.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "If the boss got elected as mayor,\x01",
            "it'd make things a lot less\x01",
            "stressful on us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CED")

    label("loc_C44")


    ChrTalk(    #11
        0xFE,
        (
            "Mayor Dalmore had no intention\x01",
            "of helping us replace this shoddy\x01",
            "old equipment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "If the boss got elected as mayor,\x01",
            "it'd make things a lot less\x01",
            "stressful on us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CED")

    Jump("loc_1078")

    label("loc_CF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_D63")

    ChrTalk(    #13
        0xFE,
        (
            "We haven't seen those delinquents\x01",
            "around in the past few days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "Maybe the mayor drove them out?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1078")

    label("loc_D63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_E19")

    ChrTalk(    #15
        0xFE,
        (
            "Those punks in the warehouse\x01",
            "are old enough to get some\x01",
            "honest work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "I don't imagine their parents would\x01",
            "shed any tears if the kids stopped\x01",
            "sponging off of them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1078")

    label("loc_E19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_E82")

    ChrTalk(    #17
        0xFE,
        (
            "The Ravens have seemed really\x01",
            "on edge lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "No doubt they're up to no good,\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1078")

    label("loc_E82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_F2A")

    ChrTalk(    #19
        0xFE,
        (
            "I don't know why the mayor hasn't\x01",
            "done something to get rid of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "If they're just allowed to run amok,\x01",
            "they're just going to keep getting\x01",
            "worse.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1078")

    label("loc_F2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_1078")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FFD")
    OP_A2(0x4)

    ChrTalk(    #21
        0xFE,
        "You kids are travelers, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "Just to give you fair warning,\x01",
            "you'll probably want to avoid\x01",
            "the warehouse district.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "There are some real unsavory\x01",
            "types hanging out down there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1078")

    label("loc_FFD")


    ChrTalk(    #24
        0xFE,
        (
            "You'll probably want to avoid the\x01",
            "warehouse district.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "There are some real unsavory\x01",
            "types hanging out down there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1078")

    TalkEnd(0x11)
    Return()

    # Function_4_B0A end

    def Function_5_107C(): pass

    label("Function_5_107C")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_11AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1140")
    OP_A2(0x5)

    ChrTalk(    #26
        0xFE,
        (
            "Looks like the Ravens are\x01",
            "coming back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "Maybe it's just me, but they\x01",
            "seem pretty out of sorts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "Could just be the gravity of\x01",
            "everything that happened,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11A8")

    label("loc_1140")


    ChrTalk(    #29
        0xFE,
        (
            "Looks like the Ravens are\x01",
            "coming back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "Maybe it's just me, but they\x01",
            "seem pretty out of sorts.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11A8")

    Jump("loc_142A")

    label("loc_11AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_125F")

    ChrTalk(    #31
        0xFE,
        (
            "Chief Portos has something on\x01",
            "his mind again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "When something's bothering you, I think\x01",
            "it's best to relax sometimes. It can \x01",
            "help you come up with a solution.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_142A")

    label("loc_125F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_12F1")

    ChrTalk(    #33
        0xFE,
        (
            "The equipment's been in sorry\x01",
            "shape lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "It's going to get a lot worse unless\x01",
            "we get a Zeissian engineer in to\x01",
            "fix things.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_142A")

    label("loc_12F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1333")

    ChrTalk(    #35
        0xFE,
        "Oh, the bridge is up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        "Time to get some lunch.\x02",
    )

    CloseMessageWindow()
    Jump("loc_142A")

    label("loc_1333")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_13A3")

    ChrTalk(    #37
        0xFE,
        "Ahh, now that's satisfying.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "Nothing like some real physical\x01",
            "work to get your blood pumping.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_142A")

    label("loc_13A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_142A")

    ChrTalk(    #39
        0xFE,
        (
            "This is where we unload cargo\x01",
            "from overseas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "Foreign goods pass through\x01",
            "customs here and get\x01",
            "shipped all over Liberl.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_142A")

    TalkEnd(0x15)
    Return()

    # Function_5_107C end

    def Function_6_142E(): pass

    label("Function_6_142E")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_165A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14BF")
    OP_28(0x21, 0x1, 0x8000)

    ChrTalk(    #41
        0xFE,
        "Thank ya for your help, earlier.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "Hopefully, I can count on you if\x01",
            "I get myself into a fix again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1657")

    label("loc_14BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15A0")
    OP_28(0x21, 0x1, 0x4000)

    ChrTalk(    #43
        0xFE,
        (
            "Man, that fake Portos was just\x01",
            "like the real deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "Not just the way he looked, but\x01",
            "he even talked an' moved the\x01",
            "same way. It's downright creepy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        "The world is full of amazing people.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1657")

    label("loc_15A0")


    ChrTalk(    #46
        0xFE,
        (
            "It's hard not to look at Chief Portos,\x01",
            "and not feel a little sorry for how\x01",
            "stressed out the man is all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "Still, when the chips are down,\x01",
            "he's a boss we can rely on.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1657")

    Jump("loc_1D92")

    label("loc_165A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_18E2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16E8")
    OP_28(0x21, 0x1, 0x8000)

    ChrTalk(    #48
        0xFE,
        "Thank ya for your help, earlier.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "Hopefully, I can count on you if\x01",
            "I get myself into a fix again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18DF")

    label("loc_16E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17C9")
    OP_28(0x21, 0x1, 0x4000)

    ChrTalk(    #50
        0xFE,
        (
            "Man, that fake Portos was just\x01",
            "like the real deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "Not just the way he looked, but\x01",
            "he even talked an' moved the\x01",
            "same way. It's downright creepy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        "The world is full of amazing people.\x02",
    )

    CloseMessageWindow()
    Jump("loc_18DF")

    label("loc_17C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1896")
    OP_A2(0x6)

    ChrTalk(    #53
        0xFE,
        (
            "Chief Portos may not look\x01",
            "like much, but he's sharp\x01",
            "and dependable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "No matter what, he always looks\x01",
            "out for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "And however much we grumble\x01",
            "sometimes, we really like the\x01",
            "boss.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18DF")

    label("loc_1896")


    ChrTalk(    #56
        0xFE,
        (
            "Chief Portos may not look\x01",
            "like much, but he's sharp\x01",
            "and dependable.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18DF")

    Jump("loc_1D92")

    label("loc_18E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1BA2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1970")
    OP_28(0x21, 0x1, 0x8000)

    ChrTalk(    #57
        0xFE,
        "Thank ya for your help, earlier.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "Hopefully, I can count on you if\x01",
            "I get myself into a fix again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B9F")

    label("loc_1970")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A51")
    OP_28(0x21, 0x1, 0x4000)

    ChrTalk(    #59
        0xFE,
        (
            "Man, that fake Portos was just\x01",
            "like the real deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "Not just the way he looked, but\x01",
            "he even talked an' moved the\x01",
            "same way. It's downright creepy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        "The world is full of amazing people.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B9F")

    label("loc_1A51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B17")
    OP_A2(0x6)

    ChrTalk(    #62
        0xFE,
        (
            "Let's see...next one in should be\x01",
            "a Republican vessel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "If they have to wait offshore, then\x01",
            "Chief Portos has to answer for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "It's too bad the harbor ain't\x01",
            "a bit wider.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B9F")

    label("loc_1B17")


    ChrTalk(    #65
        0xFE,
        (
            "Let's see...next one in should be\x01",
            "a Republican vessel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "If they have to wait offshore, then\x01",
            "Chief Portos has to answer for it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B9F")

    Jump("loc_1D92")

    label("loc_1BA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1BE6")

    ChrTalk(    #67
        0xFE,
        (
            "Hmm...maybe I should clean up\x01",
            "the cargo around here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D92")

    label("loc_1BE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_1CAB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1C4C")

    ChrTalk(    #68
        0xFE,
        "Thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "Hopefully, I can count on you if\x01",
            "I get myself into a fix again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CA8")

    label("loc_1C4C")


    ChrTalk(    #70
        0xFE,
        "Damn it... Where'd I drop it...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "I have to get it back before anyone\x01",
            "finds out...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CA8")

    Jump("loc_1D92")

    label("loc_1CAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_1D14")

    ChrTalk(    #72
        0xFE,
        (
            "I'm in charge of the Warehouse Key\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "I need to go and get it from\x01",
            "Chief Portos.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D92")

    label("loc_1D14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_1D92")

    ChrTalk(    #74
        0xFE,
        (
            "Let's see...the containers from\x01",
            "the Empire are down this way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "They have to go on an airship\x01",
            "bound for Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D92")

    TalkEnd(0xF)
    Return()

    # Function_6_142E end

    def Function_7_1D96(): pass

    label("Function_7_1D96")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1F82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ED8")
    OP_A2(0x7)

    ChrTalk(    #76
        0xFE,
        (
            "The Dalmores have truly fallen\x01",
            "far, if the mayor really had a\x01",
            "hand in those crimes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "He'll never seem like a real\x01",
            "mayor again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "More importantly, I just worry\x01",
            "about those poor kids from the\x01",
            "orphanage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "I can't do much of anything to\x01",
            "help, but I can at least dote\x01",
            "on them a little.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F7F")

    label("loc_1ED8")


    ChrTalk(    #80
        0xFE,
        (
            "The Dalmores have truly fallen\x01",
            "far, if the mayor really had a\x01",
            "hand in those crimes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "More importantly, I just worry\x01",
            "about those poor kids from the\x01",
            "orphanage.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F7F")

    Jump("loc_25DC")

    label("loc_1F82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_20E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_204D")
    OP_A2(0x7)

    ChrTalk(    #82
        0xFE,
        (
            "Some guy with a weird haircut\x01",
            "and really ugly, gaudy clothes\x01",
            "went into the mayor's estate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "Which reminds me, I heard\x01",
            "that some kind of bigwig is\x01",
            "staying somewhere in Ruan.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20E6")

    label("loc_204D")


    ChrTalk(    #84
        0xFE,
        (
            "I saw a strange man go into the mayor's home a bit\x01",
            "ago. I didn't know whether to laugh or cry, his\x01",
            "taste in clothes was so bad. And that haircut...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20E6")

    Jump("loc_25DC")

    label("loc_20E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_221C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21D2")
    OP_A2(0x7)

    ChrTalk(    #85
        0xFE,
        "The weather's nice again today...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "I used to come down to the\x01",
            "harbor and goof off when I\x01",
            "was little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "I loved running around all the street\x01",
            "vendors and roadside markets.\x01",
            "It always made me feel good.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2219")

    label("loc_21D2")


    ChrTalk(    #88
        0xFE,
        (
            "I used to come down to the\x01",
            "harbor and goof off when I\x01",
            "was little.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2219")

    Jump("loc_25DC")

    label("loc_221C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_23A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2314")
    OP_A2(0x7)

    ChrTalk(    #89
        0xFE,
        (
            "Mayor Dalmore is really into\x01",
            "sightseeing in Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "I think he wants to see about\x01",
            "starting up businesses in\x01",
            "every city he visits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "This place used to be absolutely\x01",
            "packed with sailors, but not so\x01",
            "much these days...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23A4")

    label("loc_2314")


    ChrTalk(    #92
        0xFE,
        (
            "Mayor Dalmore is really into\x01",
            "sightseeing in Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "This place used to be absolutely\x01",
            "packed with sailors, but not so\x01",
            "much these days...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23A4")

    Jump("loc_25DC")

    label("loc_23A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_250A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2492")
    OP_A2(0x7)

    ChrTalk(    #94
        0xFE,
        (
            "There's a very fine mansion on\x01",
            "this side of the river.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "It's the residence of Ruan's\x01",
            "mayor, Morris Dalmore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "The job of mayor has typically\x01",
            "been held by the head of House\x01",
            "Dalmore, for generations now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2507")

    label("loc_2492")


    ChrTalk(    #97
        0xFE,
        (
            "There's a very fine mansion on\x01",
            "this side of the river.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "It's the residence of Ruan's\x01",
            "mayor, Morris Dalmore.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2507")

    Jump("loc_25DC")

    label("loc_250A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_25DC")

    ChrTalk(    #99
        0xFE,
        (
            "The far side of the river has seen\x01",
            "a lot of growth lately, mostly\x01",
            "centered on trade and tourism.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "The harbor facilities and the\x01",
            "residential district have been\x01",
            "side-by-side for a very long time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25DC")

    TalkEnd(0x16)
    Return()

    # Function_7_1D96 end

    def Function_8_25E0(): pass

    label("Function_8_25E0")

    TalkBegin(0x12)

    ChrTalk(    #101
        0xFE,
        (
            "#140FNow, then...where should I\x01",
            "focus my investigation next?\x02\x03",

            "I should probably start by walking\x01",
            "over to the crime scene.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x12)
    Return()

    # Function_8_25E0 end

    def Function_9_2666(): pass

    label("Function_9_2666")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_2859")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2797")
    OP_A2(0x2)

    ChrTalk(    #102
        0xFE,
        (
            "Long ago, Ruan was built\x01",
            "entirely around foreign trade\x01",
            "and commercial fishing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "Nowadays, the harbor brings in\x01",
            "the least money of anywhere in\x01",
            "the business district.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "I'm of the opinion that it started\x01",
            "turning into a tourist trap as soon\x01",
            "as Mayor Dalmore was sworn in.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2856")

    label("loc_2797")


    ChrTalk(    #105
        0xFE,
        (
            "Long ago, Ruan was built\x01",
            "entirely around foreign trade\x01",
            "and commercial fishing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "I'm of the opinion that it started\x01",
            "turning into a tourist trap as soon\x01",
            "as Mayor Dalmore was sworn in.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2856")

    Jump("loc_29EE")

    label("loc_2859")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_2954")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28F7")
    OP_A2(0x2)

    ChrTalk(    #107
        0xFE,
        (
            "Okay...looks like the cargo's\x01",
            "good to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "I need to finish up the customs\x01",
            "clearance and get this container\x01",
            "on its way to Bose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2951")

    label("loc_28F7")


    ChrTalk(    #109
        0xFE,
        (
            "I need to finish up the customs\x01",
            "clearance and get this container\x01",
            "on its way to Bose.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2951")

    Jump("loc_29EE")

    label("loc_2954")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_29EE")

    ChrTalk(    #110
        0xFE,
        (
            "It'll cost a fortune for a load\x01",
            "this big to fly...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "Guess I can always send it by boat,\x01",
            "as long as none of it's a rush order\x01",
            "or anything.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29EE")

    TalkEnd(0x13)
    Return()

    # Function_9_2666 end

    def Function_10_29F2(): pass

    label("Function_10_29F2")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2CC6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B65")
    OP_28(0x20, 0x1, 0x4000)

    ChrTalk(    #112
        0xFE,
        (
            "Ah, it's you. I'm sorry for getting\x01",
            "so angry earlier. I didn't know\x01",
            "the full story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "Harg tells me that my doppelganger\x01",
            "truly was the spitting image of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "It's a shame, really. If you'd caught him,\x01",
            "I could've made HIM do all the work around\x01",
            "here, and no one'd be any the wiser!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        "Ha ha ha! Just kidding, of course.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CC3")

    label("loc_2B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C2C")
    OP_A2(0x3)

    ChrTalk(    #116
        0xFE,
        (
            "It's hard to believe what the\x01",
            "mayor's let himself become.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "And I'd been hoping to discuss\x01",
            "the condition of the harbor's\x01",
            "equipment with him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        "Hmm...so, now what do we do?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CC3")

    label("loc_2C2C")


    ChrTalk(    #119
        0xFE,
        (
            "It's hard to believe what the mayor's\x01",
            "let himself become.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "And I'd been hoping to discuss\x01",
            "the condition of the harbor's\x01",
            "equipment with him...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CC3")

    Jump("loc_33F9")

    label("loc_2CC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_2F87")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E36")
    OP_28(0x20, 0x1, 0x4000)

    ChrTalk(    #121
        0xFE,
        (
            "Ah, it's you. I'm sorry for getting\x01",
            "so angry earlier. I didn't know\x01",
            "the full story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "Harg tells me that my doppelganger\x01",
            "truly was the spitting image of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "It's a shame, really. If you'd caught him,\x01",
            "I could've made HIM do all the work around\x01",
            "here, and no one'd be any the wiser!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        "Ha ha ha! Just kidding, of course.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F84")

    label("loc_2E36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EFA")
    OP_A2(0x3)

    ChrTalk(    #125
        0xFE,
        (
            "This crane is so old...I'd love to\x01",
            "be able to buy a replacement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "Just one more thing I need to take\x01",
            "up with the mayor, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        "*sigh* It's getting to be a problem...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F84")

    label("loc_2EFA")


    ChrTalk(    #128
        0xFE,
        (
            "This crane is so old...I'd love to\x01",
            "be able to buy a replacement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "Just one more thing I need to take\x01",
            "up with the mayor, I guess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F84")

    Jump("loc_33F9")

    label("loc_2F87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_316F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_30F7")
    OP_28(0x20, 0x1, 0x4000)

    ChrTalk(    #130
        0xFE,
        (
            "Ah, it's you. I'm sorry for getting\x01",
            "so angry earlier. I didn't know\x01",
            "the full story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "Harg tells me that my doppelganger\x01",
            "truly was the spitting image of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "It's a shame, really. If you'd caught him,\x01",
            "I could've made HIM do all the work around\x01",
            "here, and no one'd be any the wiser!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        "Ha ha ha! Just kidding, of course.\x02",
    )

    CloseMessageWindow()
    Jump("loc_316C")

    label("loc_30F7")


    ChrTalk(    #134
        0xFE,
        (
            "All of the equipment in this\x01",
            "facility is gradually wearing\x01",
            "out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "Ah, well...shouldn't go\x01",
            "borrowing trouble.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_316C")

    Jump("loc_33F9")

    label("loc_316F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_3284")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3223")
    OP_A2(0x3)

    ChrTalk(    #136
        0xFE,
        (
            "I'd discussed the delinquents in\x01",
            "the warehouse with the mayor\x01",
            "before all this started...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "...but I never heard anything back\x01",
            "about it. What a pain...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3281")

    label("loc_3223")


    ChrTalk(    #138
        0xFE,
        (
            "I'd discussed the delinquents in\x01",
            "the warehouse with the mayor\x01",
            "before all this started...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3281")

    Jump("loc_33F9")

    label("loc_3284")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_33F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3367")
    OP_A2(0x3)

    ChrTalk(    #139
        0xFE,
        (
            "We have a lot of foreign goods\x01",
            "just packed into the ships.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "It's not a surprise to anyone that\x01",
            "most of it's orbment-related,\x01",
            "these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "Liberl-made orbments are the\x01",
            "most famous in the world.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33F9")

    label("loc_3367")


    ChrTalk(    #142
        0xFE,
        (
            "Most of what's packed up onto\x01",
            "the foreign trade ships are\x01",
            "orbment-related goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "Liberl-made orbments are the\x01",
            "most famous in the world.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33F9")

    TalkEnd(0x14)
    Return()

    # Function_10_29F2 end

    def Function_11_33FD(): pass

    label("Function_11_33FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36C5")
    OP_A2(0x416)
    EventBegin(0x0)
    OP_51(0x136, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x136, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3426():
        OP_6C(156000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3426)

    def lambda_3436():
        OP_6B(4100, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3436)

    def lambda_3446():
        OP_6D(28940, 0, 430, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3446)
    Sleep(5000)
    Fade(1000)
    OP_6C(135000, 0)
    OP_6B(2800, 0)
    OP_6D(29580, 0, 8940, 0)
    SetChrPos(0x101, 29440, 0, 8189, 180)
    SetChrPos(0x102, 30100, 0, 9570, 180)
    SetChrPos(0x136, 28520, 0, 9990, 180)
    OP_0D()

    ChrTalk(    #144
        0x101,
        (
            "#004FMan, there sure are a lot of\x01",
            "big buildings around here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x136,
        (
            "#040FThat's because this is the\x01",
            "warehouse district.\x02\x03",

            "Cargo from foreign countries\x01",
            "is kept here for safekeeping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x101,
        (
            "#000FI see. Kinda depressing place, though.\x01",
            "Seems really lonely and desolate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x136,
        (
            "#040FWell, since the advent of airships,\x01",
            "not much cargo is transported by\x01",
            "sea anymore.\x02\x03",

            "So these warehouses don't get a\x01",
            "lot of new shipments these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x101,
        "#000FYeah, that makes sense.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x102,
        (
            "#010FLooks like some of the warehouses\x01",
            "are abandoned, too.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)

    label("loc_36C5")

    Return()

    # Function_11_33FD end

    def Function_12_36C6(): pass

    label("Function_12_36C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C14")
    OP_A2(0x417)
    EventBegin(0x0)
    OP_51(0x136, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x136, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xD, 0x40)
    SetChrPos(0xC, 50970, 0, 35000, 0)
    SetChrPos(0xD, 50970, 0, 34260, 0)
    SetChrPos(0x8, 37400, 0, 23790, 0)
    SetChrPos(0x9, 37400, 0, 21720, 0)
    SetChrPos(0xA, 37400, 0, 22740, 0)

    NpcTalk(    #150
        0x8,
        "Young Man's Voice",
        "Hold it, you lot.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(48730, 0, 23120, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(261, 0)
    SetChrPos(0x101, 50170, 0, 23370, 270)
    SetChrPos(0x102, 50380, 0, 22120, 270)
    SetChrPos(0x136, 51330, 0, 22810, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)

    def lambda_3813():
        OP_8E(0xFE, 0xBC98, 0x0, 0x5CE4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3813)
    Sleep(200)

    def lambda_3833():
        OP_8E(0xFE, 0xBBA8, 0x0, 0x54D8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3833)
    Sleep(200)

    def lambda_3853():
        OP_8E(0xFE, 0xBA86, 0x0, 0x58D4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3853)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0xA, 0x1)

    ChrTalk(    #151
        0x101,
        "#004FWho, us?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x8,
        (
            "#3PWell, well...\x01",
            "Must be our lucky day!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xA,
        (
            "Not too many womenfolk come\x01",
            "'round these parts. You're a\x01",
            "real sight for sore eyes!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x136,
        (
            "#040FAnd what business have\x01",
            "you here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x8,
        (
            "#3PHa ha ha... Oh, this and that.\x01",
            "We've been here for quite a\x01",
            "while, actually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x8,
        (
            "#3PIf you honeys got time to spare,\x01",
            "how about you entertain us, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x136,
        "#043FI, uh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x101,
        (
            "#007FAre you seriously trying to\x01",
            "pick up girls in an empty,\x01",
            "old warehouse lot?\x02\x03",

            "#006FSorry, but we have plans already.\x01",
            "You know, places to go, things to\x01",
            "see...\x02\x03",

            "So, yeah...not interested.\x01",
            "Feel free to go away now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x9,
        (
            "Oh, check you out! I like tough women.\x01",
            "I'll take all the abuse you can dish! ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x101,
        (
            "#004FIf your goal was to creep me out\x01",
            "even more, consider your mission\x01",
            "accomplished...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xA,
        (
            "Hey, you know, if you ladies are\x01",
            "playing tourist, then maybe we\x01",
            "can show you around, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xA,
        (
            "You can ditch that little kid with\x01",
            "you, and we'll have some fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x102,
        "#014F...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #164
        0x101,
        (
            "#009FHey, now! Who are you calling\x01",
            "a little kid?!\x02\x03",

            "Punks like you couldn't\x01",
            "take on Joshua if you--\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 0, 400)

    ChrTalk(    #165
        0x102,
        (
            "#010F#5PIt's okay, Estelle.\x01",
            "It doesn't bother me.\x02\x03",

            "What good is getting angry\x01",
            "going to do?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    ChrTalk(    #166
        0x101,
        "#003FB-But...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(    #167
        0x8,
        (
            "#3PAww... You holding back for our\x01",
            "sake, kid? How sweet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xA,
        (
            "Where does this brat get off,\x01",
            "hanging around with two hotties?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x9,
        (
            "Heh heh... I think he needs a\x01",
            "lesson in just how unfair life\x01",
            "can be, don'cha think?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3E17():
        OP_92(0xFE, 0x102, 0x640, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3E17)
    Sleep(100)

    def lambda_3E31():
        OP_92(0xFE, 0x102, 0x640, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3E31)
    Sleep(100)

    def lambda_3E4B():
        OP_92(0xFE, 0x102, 0x6A4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3E4B)
    Sleep(400)
    OP_8C(0x101, 225, 400)

    ChrTalk(    #170
        0x101,
        "#005FJust a second...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x136,
        "#043FP-Please, stop!\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x102)

    ChrTalk(    #172
        0x102,
        (
            "#015F#5PIf my presence has somehow offended\x01",
            "you, then I apologize.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 270, 400)
    Sleep(500)
    OP_92(0x102, 0xA, 0x3E8, 0x7D0, 0x0)

    ChrTalk(    #173
        0x102,
        (
            "#012F#4PBut if you lay a finger on the\x01",
            "ladies, I'll make certain that\x01",
            "you regret it.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_3FAE():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3FAE)
    Sleep(100)

    def lambda_3FC9():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3FC9)
    Sleep(100)

    def lambda_3FE4():
        OP_94(0x1, 0xFE, 0xB4, 0x2BC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3FE4)
    WaitChrThread(0xA, 0x1)

    ChrTalk(    #174
        0x9,
        "Wha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xA,
        (
            "J-Just who do you think\x01",
            "you are?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x8,
        "#3PH-He's just bluffing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x8,
        (
            "#3PHeh, I get that you want to look\x01",
            "all cool in front of the ladies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x8,
        (
            "#3PBut you're about to experience\x01",
            "a world of pain.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #179
        0xD,
        "Young Man's Voice",
        "#3PWhat do you think you're doing?!\x02",
    )

    CloseMessageWindow()

    def lambda_410D():
        OP_6D(50290, 0, 24500, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_410D)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)

    def lambda_412F():

        label("loc_412F")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_412F")

    QueueWorkItem2(0x101, 1, lambda_412F)

    def lambda_4140():

        label("loc_4140")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_4140")

    QueueWorkItem2(0x102, 1, lambda_4140)

    def lambda_4151():

        label("loc_4151")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_4151")

    QueueWorkItem2(0x136, 1, lambda_4151)

    def lambda_4162():

        label("loc_4162")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_4162")

    QueueWorkItem2(0x8, 1, lambda_4162)

    def lambda_4173():

        label("loc_4173")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_4173")

    QueueWorkItem2(0x9, 1, lambda_4173)

    def lambda_4184():

        label("loc_4184")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_4184")

    QueueWorkItem2(0xA, 1, lambda_4184)
    OP_8E(0xD, 0xC60C, 0x0, 0x6770, 0xBB8, 0x0)

    ChrTalk(    #180
        0x9,
        "Eh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xA,
        "Oh, great. Another nuisance.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xD,
        (
            "#674FI can't believe you guys would\x01",
            "start again with this delinquency!\x02\x03",

            "You're old enough to know better!\x01",
            "You should be ashamed of yourselves!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x8,
        (
            "#3PSh-Shut up! What do you care\x01",
            "what we do?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x8,
        (
            "#3PYou're just one of the\x01",
            "mayor's yes-men!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xD,
        "#671FHow dare you denigrate my work!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #186
        0xC,
        "Man's Voice",
        (
            "#3PHow dare you, indeed.\x01",
            "Gilbert is a valuable\x01",
            "member of my staff.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x136, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)

    def lambda_4363():

        label("loc_4363")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_4363")

    QueueWorkItem2(0x101, 1, lambda_4363)

    def lambda_4374():

        label("loc_4374")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_4374")

    QueueWorkItem2(0x102, 1, lambda_4374)

    def lambda_4385():

        label("loc_4385")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_4385")

    QueueWorkItem2(0x136, 1, lambda_4385)

    def lambda_4396():

        label("loc_4396")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_4396")

    QueueWorkItem2(0x8, 1, lambda_4396)

    def lambda_43A7():

        label("loc_43A7")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_43A7")

    QueueWorkItem2(0x9, 1, lambda_43A7)

    def lambda_43B8():

        label("loc_43B8")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_43B8")

    QueueWorkItem2(0xA, 1, lambda_43B8)

    def lambda_43C9():
        OP_8E(0xFE, 0xC60C, 0x0, 0x6770, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_43C9)
    TurnDirection(0xD, 0xC, 400)
    Sleep(500)
    OP_8E(0xD, 0xCBE8, 0x0, 0x6266, 0x7D0, 0x0)
    OP_8C(0xD, 270, 400)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0xC, 0x1)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x136, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)

    ChrTalk(    #187
        0x9,
        "D-Dalmore?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xA,
        "Bah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x101,
        (
            "#002F(Whoa, who's that? He's way too\x01",
            "well-dressed for this part of\x01",
            "town...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x136,
        (
            "#040F(That's Dalmore, the mayor of Ruan.)\x02\x03",

            "(And the younger one is Gilbert,\x01",
            "his private secretary, I think.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xC,
        (
            "#664FRuan has always been\x01",
            "a free city.\x02\x03",

            "I have no intention of lodging\x01",
            "a complaint about your manner\x01",
            "of speech, or your attire.\x02\x03",

            "#662FBut bothering outsiders...\x01",
            "who may be paying guests...\x01",
            "is NOT permissible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x8,
        (
            "#3PStuff it, old man! You think\x01",
            "you're such a big shot...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x8,
        (
            "#3PWe ain't interested in a thing\x01",
            "you have to say!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x8, 400)

    ChrTalk(    #194
        0xD,
        (
            "#674FH-How dare you speak to the\x01",
            "mayor in such a fashion!\x02\x03",

            "How would you like for us\x01",
            "to report you to the Bracer\x01",
            "Guild again?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x9,
        "Hmph... Bracer, shmacer.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x9,
        (
            "Always hiding behind them...\x01",
            "Can'cha do anything on your own?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xA,
        (
            "Besides, it's not like the bracers would\x01",
            "get here right away. We'd have plenty of\x01",
            "time to...enjoy the altercation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xA,
        (
            "And then we'd be gone without\x01",
            "a trace before anyone was the\x01",
            "wiser.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4853():
        OP_6D(49220, 0, 23720, 1000)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_4853)
    Sleep(500)

    def lambda_4870():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4870)
    Sleep(200)

    def lambda_4883():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4883)
    Sleep(200)

    def lambda_4896():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_4896)
    WaitChrThread(0xC, 0x1)

    ChrTalk(    #199
        0x101,
        (
            "#007F#2PUm... I hate to ruin your masterful\x01",
            "plan, but...\x02\x03",

            "I'm afraid we're already here.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4907():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4907)

    def lambda_4915():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4915)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #200
        0x8,
        "#1P...Wait, what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x101,
        (
            "#006F#2PMan...you mean you STILL haven't\x01",
            "noticed the badges?\x02\x03",

            "Maybe you guys need glasses\x01",
            "or something.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #202
        (
            "\x07\x05With great deliberation and exaggerated movements, Estelle pointed out\x01",
            "the bracer emblem on her chest. She then raised her eyebrows for further\x01",
            "emphasis.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #203
        0x9,
        "Ahh, crap...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xA,
        "You guys are bracers?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xA,
        (
            "So wait, this little punk\x01",
            "you're with...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x102,
        "#010F#2P...is also a bracer, yes.\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    OP_8C(0x9, 0, 400)

    ChrTalk(    #207
        0x9,
        "(Wh-What do we do now?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x9,
        (
            "(I can't believe that little\x01",
            "squirt is actually a bracer!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xA,
        "#3P(You're actually worried?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xA,
        (
            "(Even if they ARE bracers, it's\x01",
            "just a coupla girls and some kid!)\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)

    ChrTalk(    #211
        0x8,
        (
            "#4P(Dumbass! You can't judge a\x01",
            "book by its cover, y'know?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x8,
        (
            "#4P(You remember what happened the last time\x01",
            "we took on a chick bracer?! Even with three\x01",
            "people, she wiped the floor with us!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x8,
        (
            "#4P(Going up against two bracers, even\x01",
            "if they DO look like pipsqueaks, is\x01",
            "totally NOT a good idea!)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)
    OP_8C(0x8, 90, 400)

    ChrTalk(    #214
        0x8,
        (
            "#1PO-Okay, we're gonna let you off\x01",
            "the hook...for now!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 90, 400)

    ChrTalk(    #215
        0x9,
        (
            "If we see you again, though,\x01",
            "you'll be in for some real pain!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xA,
        "Catch you later!\x02",
    )

    CloseMessageWindow()

    def lambda_4E70():

        label("loc_4E70")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_4E70")

    QueueWorkItem2(0x101, 1, lambda_4E70)

    def lambda_4E81():

        label("loc_4E81")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_4E81")

    QueueWorkItem2(0x102, 1, lambda_4E81)

    def lambda_4E92():

        label("loc_4E92")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_4E92")

    QueueWorkItem2(0x136, 1, lambda_4E92)

    def lambda_4EA3():

        label("loc_4EA3")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_4EA3")

    QueueWorkItem2(0xC, 1, lambda_4EA3)

    def lambda_4EB4():

        label("loc_4EB4")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_4EB4")

    QueueWorkItem2(0xD, 1, lambda_4EB4)
    OP_8C(0xA, 270, 400)

    def lambda_4ECC():
        OP_6D(48000, 0, 24000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4ECC)

    def lambda_4EE4():
        OP_8E(0xFE, 0x9088, 0x0, 0x58D4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4EE4)
    OP_8C(0x8, 270, 400)

    def lambda_4F06():
        OP_8E(0xFE, 0x9088, 0x0, 0x5CEE, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4F06)
    OP_8C(0x9, 270, 400)

    def lambda_4F28():
        OP_8E(0xFE, 0x9088, 0x0, 0x54D8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4F28)
    WaitChrThread(0x9, 0x1)

    ChrTalk(    #217
        0x101,
        (
            "#007FGeez... Now THOSE were punks.\x01",
            "I mean, could they BE any more\x01",
            "stereotypical?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x102,
        (
            "#010FEhh, no harm done. And don't we\x01",
            "have somewhere we need to be?\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x136, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xC, 0xFF)
    OP_8C(0xC, 180, 400)

    ChrTalk(    #219
        0xC,
        (
            "#660F#4PI must apologize. I loathe when\x01",
            "our city's guests are bothered.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_504F():
        OP_6D(50450, 0, 24070, 1500)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_504F)

    def lambda_5067():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5067)
    OP_8E(0xC, 0xC60C, 0x0, 0x63D8, 0x7D0, 0x0)

    def lambda_5089():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5089)

    def lambda_5097():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_5097)
    TurnDirection(0x101, 0xC, 400)
    WaitChrThread(0xC, 0x2)

    ChrTalk(    #220
        0xC,
        (
            "#660FForgive my lack of an introduction,\x01",
            "as well. I am Dalmore, mayor\x01",
            "of Ruan.\x02\x03",

            "#660FAnd this is my steward,\x01",
            "Gilbert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xD,
        (
            "#670FA pleasure, I'm sure. You are\x01",
            "bracers, are you not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x101,
        (
            "#000FYep. I'm Estelle,\x01",
            "from Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x102,
        (
            "#010FAnd I am Joshua, also\x01",
            "from Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xC,
        (
            "#660FJean did mention some promising\x01",
            "new faces soon to arrive.\x02\x03",

            "Might he have been referring\x01",
            "to you, perchance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x101,
        (
            "#008FHa ha... Well, I don't know about\x01",
            "the 'promising' part, but yeah,\x01",
            "I think he meant us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x102,
        (
            "#010FWe came to Ruan in search of\x01",
            "work, actually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xC,
        (
            "#661FAh, how delightful!\x02\x03",

            "We've had some hard times of\x01",
            "late, you see. So any help we\x01",
            "can get is simply wonderful.\x02\x03",

            "I'm sure your presence here\x01",
            "will be a great boon to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x102,
        (
            "#014FHard times?\x01",
            "What do you mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xC,
        (
            "#660FWell, Jean would be the one best\x01",
            "able to supply the details.\x02\x03",

            "...As an aside, is that a campus\x01",
            "uniform I spy, young lady?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x136,
        (
            "#040FYes, sir. I'm Kloe Rinz. I'm a\x01",
            "second-year student at the\x01",
            "royal academy.\x02\x03",

            "It's a pleasure to meet you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xC,
        (
            "#660FCharmed. Dean Collins is a\x01",
            "friend of mine, actually.\x02\x03",

            "Hmm... Didn't you graduate from\x01",
            "the Royal Academy yourself,\x01",
            "Gilbert?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xD,
        (
            "#670FYes, sir.\x02\x03",

            "You said your name was Kloe?\x01",
            "I've heard a great deal about\x01",
            "you.\x02\x03",

            "You ran against Jill for head\x01",
            "of the Student Council, right?\x02\x03",

            "You must be proud to have been\x01",
            "a contender, as a junior.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x136,
        "#045FOh... You flatter me, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xC,
        (
            "#661FHa ha ha. I'm looking forward\x01",
            "to the campus festival.\x02\x03",

            "I trust you'll be giving your\x01",
            "all to help make it a memorable\x01",
            "one, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x136,
        "#040FYes, sir. I absolutely will.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xC,
        (
            "#661FWell, I think we'd best be going.\x02\x03",

            "If those Ravens start making\x01",
            "trouble again, feel free to drop\x01",
            "by and let me know.\x02\x03",

            "It is my duty, as mayor of Ruan, to\x01",
            "ensure that these streets are safe\x01",
            "for tourists and residents alike!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_57A9():
        OP_6D(52270, 0, 23490, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_57A9)

    def lambda_57C1():

        label("loc_57C1")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_57C1")

    QueueWorkItem2(0x101, 1, lambda_57C1)

    def lambda_57D2():

        label("loc_57D2")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_57D2")

    QueueWorkItem2(0x102, 1, lambda_57D2)

    def lambda_57E3():

        label("loc_57E3")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_57E3")

    QueueWorkItem2(0x136, 1, lambda_57E3)
    OP_8E(0xC, 0xCD6E, 0x0, 0x5ADC, 0xBB8, 0x0)

    def lambda_5808():
        OP_8E(0xFE, 0xFB54, 0x0, 0x5334, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5808)
    Sleep(500)
    OP_8E(0xD, 0xD156, 0x0, 0x594C, 0xBB8, 0x0)

    def lambda_583C():
        OP_8E(0xFE, 0xFB54, 0x0, 0x5334, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_583C)
    WaitChrThread(0xD, 0x1)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x136, 0xFF)

    ChrTalk(    #237
        0x101,
        (
            "#000FWell, he was certainly a\x01",
            "dignified one!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x102,
        (
            "#010FYes, indeed. His manner and\x01",
            "actions were perfectly suited\x01",
            "to the mayor of a city.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_58F6():
        OP_6D(50520, 0, 23090, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_58F6)
    Sleep(500)
    OP_8C(0x136, 270, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #239
        0x136,
        (
            "#040F#4PHouse Dalmore is made up of a long\x01",
            "line of well-bred aristocrats.\x02\x03",

            "Though we no longer have real nobles,\x01",
            "he's about as close as it gets.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 400)

    ChrTalk(    #240
        0x101,
        (
            "#501FWow... It's like he's from a\x01",
            "totally different world.\x02\x03",

            "#007FOn the other hand, though, you still\x01",
            "have all the low-lifes, like those\x01",
            "guys who tried hitting on us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x136,
        (
            "#043F#4PYes...\x01",
            "That was quite unsettling.\x02\x03",

            "I'm very sorry for leading you\x01",
            "into such a place unprepared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x102,
        (
            "#010FNo need to apologize.\x02\x03",

            "It's not like we sought them\x01",
            "out or anything.\x02\x03",

            "We should probably keep our distance from\x01",
            "the back end of the warehouse district,\x01",
            "though, to avoid any further altercations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x101,
        (
            "#009FEhhh... Well, I don't like being\x01",
            "restricted like that, but whatever.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xB, 0x80)
    OP_64(0x2, 0x1)
    OP_71(0x13, 0x10)
    EventEnd(0x0)

    label("loc_5C14")

    Return()

    # Function_12_36C6 end

    def Function_13_5C15(): pass

    label("Function_13_5C15")

    EventBegin(0x0)
    FadeToBright(2000, 0)
    OP_22(0xD4, 0x0, 0x64)
    LoadEffect(0x4, "map\\\\mp013_00.eff")
    LoadEffect(0x5, "map\\\\mp013_01.eff")
    PlayEffect(0x4, 0x0, 0x17, 0, 0, 2200, 180, 0, 0, 1000, 100, 3000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0x1, 0x17, 0, 0, -1800, 180, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x17, -1310, -2900, 14370, 270)
    SetChrFlags(0x17, 0x40)
    OP_A1(0x17, 0x20)
    OP_72(0x20, 0x4)
    OP_72(0x20, 0x2)
    OP_71(0x20, 0x400)
    OP_71(0x20, 0x40)
    OP_48()
    ClearChrFlags(0x0, 0x4)
    ClearChrFlags(0x1, 0x4)
    ClearChrFlags(0x2, 0x4)
    SetChrPos(0x102, -2350, -2870, 14350, 270)
    SetChrPos(0x101, -1030, -2800, 14700, 90)
    SetChrPos(0x136, -910, -2840, 13890, 90)
    SetChrFlags(0x0, 0x20)
    SetChrFlags(0x1, 0x20)
    SetChrFlags(0x2, 0x20)
    OP_6D(8670, -1800, 15130, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(158000, 0)
    OP_6E(262, 0)
    Sleep(1000)

    def lambda_5D80():
        OP_6D(18890, -1800, 11040, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D80)

    def lambda_5D98():
        OP_6C(134000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5D98)
    SetChrFlags(0x17, 0x40)
    SetChrFlags(0x17, 0x4)
    WaitChrThread(0x17, 0x1)

    def lambda_5DB7():
        OP_8F(0xFE, 0x46FA, 0xFFFFF4AC, 0x343A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_5DB7)
    Sleep(500)
    OP_82(0x0, 0x2)
    PlayEffect(0x4, 0x2, 0x17, 0, 0, 2200, 180, 0, 0, 600, 100, 3000, 0xFF, 0, 0, 0, 0)
    OP_82(0x1, 0x2)

    def lambda_5E12():
        OP_8F(0xFE, 0x46FA, 0xFFFFF4AC, 0x343A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_5E12)
    Sleep(500)

    def lambda_5E32():
        OP_8F(0xFE, 0x46FA, 0xFFFFF4AC, 0x343A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_5E32)
    WaitChrThread(0x17, 0x1)
    OP_82(0x2, 0x2)
    ClearChrFlags(0x0, 0x20)
    ClearChrFlags(0x1, 0x20)
    ClearChrFlags(0x2, 0x20)

    def lambda_5E64():

        label("loc_5E64")

        TurnDirection(0xFE, 0x136, 400)
        OP_48()
        Jump("loc_5E64")

    QueueWorkItem2(0x101, 1, lambda_5E64)

    def lambda_5E75():

        label("loc_5E75")

        TurnDirection(0xFE, 0x136, 400)
        OP_48()
        Jump("loc_5E75")

    QueueWorkItem2(0x102, 1, lambda_5E75)
    OP_8C(0x136, 180, 400)
    OP_51(0x136, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x136, 0x1000)
    SetChrSubChip(0x136, 4)

    def lambda_5EA2():
        OP_99(0xFE, 0x4, 0x6, 0x7D0)
        ExitThread()

    QueueWorkItem(0x136, 3, lambda_5EA2)
    SetChrFlags(0x136, 0x4)
    OP_96(0x136, 0x47AE, 0xFFFFF8F8, 0x2EC2, 0x5DC, 0x1F40)
    OP_51(0x136, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x136, 0x1000)
    ClearChrFlags(0x136, 0x4)
    OP_8E(0x136, 0x4B64, 0xFFFFF8F8, 0x2C56, 0xBB8, 0x0)
    TurnDirection(0x136, 0x101, 400)

    def lambda_5EFE():

        label("loc_5EFE")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_5EFE")

    QueueWorkItem2(0x136, 1, lambda_5EFE)
    OP_44(0x101, 0xFF)
    SetChrFlags(0x101, 0x4)
    OP_8E(0x101, 0x4768, 0xFFFFF510, 0x3296, 0xBB8, 0x0)
    OP_51(0x101, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x101, 0x1000)
    SetChrSubChip(0x101, 0)

    def lambda_5F41():
        OP_99(0xFE, 0x0, 0x2, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5F41)
    SetChrFlags(0x101, 0x4)
    OP_96(0x101, 0x47AE, 0xFFFFF8F8, 0x2EC2, 0x5DC, 0x1F40)
    OP_51(0x101, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x101, 0x4)
    OP_8E(0x101, 0x472C, 0xFFFFF8F8, 0x2A58, 0xBB8, 0x0)
    TurnDirection(0x101, 0x102, 400)

    def lambda_5F9D():

        label("loc_5F9D")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_5F9D")

    QueueWorkItem2(0x136, 1, lambda_5F9D)

    def lambda_5FAE():

        label("loc_5FAE")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_5FAE")

    QueueWorkItem2(0x101, 1, lambda_5FAE)
    OP_44(0x102, 0xFF)
    OP_8E(0x102, 0x42AE, 0xFFFFF542, 0x3296, 0xBB8, 0x0)
    OP_51(0x102, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x102, 0x1000)
    SetChrSubChip(0x102, 0)
    SetChrFlags(0x102, 0x4)

    def lambda_5FF1():
        OP_99(0xFE, 0x0, 0x2, 0x7D0)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_5FF1)
    OP_96(0x102, 0x434E, 0xFFFFF8F8, 0x2D46, 0x5DC, 0x1F40)
    OP_51(0x102, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x102, 0x1000)
    SetChrSubChip(0x102, 0)
    ClearChrFlags(0x102, 0x4)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #244
        0x101,
        (
            "#002FThis is the southernmost part of\x01",
            "the warehouse district.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x197, 0x0, 0x64)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x4)
    SetChrFlags(0xE, 0x40)
    SetChrPos(0xE, 31110, 6000, 15480, 0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x136, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x136, 0xFF)

    def lambda_60F7():

        label("loc_60F7")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_60F7")

    QueueWorkItem2(0x101, 2, lambda_60F7)

    def lambda_6108():

        label("loc_6108")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_6108")

    QueueWorkItem2(0x102, 2, lambda_6108)

    def lambda_6119():

        label("loc_6119")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_6119")

    QueueWorkItem2(0x136, 2, lambda_6119)

    def lambda_612A():
        OP_6D(20890, -1800, 11040, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_612A)
    OP_22(0x8C, 0x0, 0x64)
    OP_92(0xE, 0x136, 0x1388, 0x1F40, 0x0)
    OP_92(0xE, 0x136, 0xFA0, 0x1770, 0x0)
    OP_92(0xE, 0x136, 0xBB8, 0xFA0, 0x0)
    OP_92(0xE, 0x136, 0x7D0, 0x7D0, 0x0)
    OP_8E(0xE, 0x4D58, 0xFFFFFCE0, 0x2CEC, 0x5DC, 0x0)
    OP_44(0x136, 0xFF)
    SetChrFlags(0x136, 0x20)

    def lambda_619C():
        OP_8C(0xFE, 315, 200)
        ExitThread()

    QueueWorkItem(0x136, 3, lambda_619C)
    SetChrChipByIndex(0x136, 14)
    SetChrSubChip(0x136, 2)
    OP_8F(0xE, 0x4C2C, 0xFFFFF9C0, 0x2CBA, 0x3E8, 0x0)
    WaitChrThread(0xE, 0x3)
    Sleep(100)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    Fade(250)
    SetChrFlags(0xE, 0x80)
    SetChrSubChip(0x136, 0)
    OP_0D()

    ChrTalk(    #245
        0x101,
        "#004FSieg?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0xE,
        (
            "#310F#1PScree!\x02\x03",

            "#310FScree! Screeee!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x136,
        (
            "#049F#2POkay, I understand.\x02\x03",

            "#042F#2P...Looks like he's gone as\x01",
            "far in as you can go.\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    ClearChrFlags(0xE, 0x80)
    SetChrSubChip(0x136, 2)
    OP_0D()

    def lambda_6290():

        label("loc_6290")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_6290")

    QueueWorkItem2(0x101, 2, lambda_6290)

    def lambda_62A1():

        label("loc_62A1")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_62A1")

    QueueWorkItem2(0x102, 2, lambda_62A1)

    def lambda_62B2():

        label("loc_62B2")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_62B2")

    QueueWorkItem2(0x136, 2, lambda_62B2)

    def lambda_62C3():
        OP_6D(18890, -1800, 11040, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_62C3)
    OP_22(0x8C, 0x0, 0x64)

    def lambda_62E0():
        OP_8E(0xFE, 0xC7A6, 0x1770, 0x3C78, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_62E0)
    Sleep(400)

    def lambda_6300():
        OP_8E(0xFE, 0xC7A6, 0x1770, 0x3C78, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6300)
    Sleep(400)
    SetChrChipByIndex(0x136, 65535)
    ClearChrFlags(0x136, 0x20)
    SetChrSubChip(0x136, 0)

    def lambda_632F():
        OP_8E(0xFE, 0xC7A6, 0x1770, 0x3C78, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_632F)
    WaitChrThread(0xE, 0x1)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x136, 0xFF)
    TurnDirection(0x102, 0x136, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #248
        0x102,
        (
            "#012FLet's get a move on, then.\x01",
            "That's probably where we'll\x01",
            "find the hideout.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_63BA():
        TurnDirection(0x136, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_63BA)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #249
        0x101,
        "#005F#6PRoger that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x136,
        "#042FOkay!\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xE, 0x80)
    EventEnd(0x0)
    Return()

    # Function_13_5C15 end

    def Function_14_63FA(): pass

    label("Function_14_63FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 2)), scpexpr(EXPR_EXEC_OP, "OP_40(0x334)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x332)"), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6412")
    Call(1, 10)
    Jump("loc_6828")

    label("loc_6412")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_653B")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_64A6")
    TurnDirection(0x102, 0x1, 400)

    ChrTalk(    #251
        0x102,
        (
            "#012FThis is the way out to the highway.\x02\x03",

            "We should hang around the estate\x01",
            "until the Royal Army gets here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_651D")

    label("loc_64A6")

    TurnDirection(0x102, 0x0, 400)

    ChrTalk(    #252
        0x102,
        (
            "#012FThis is the way out to the highway.\x02\x03",

            "We should hang around the estate\x01",
            "until the Royal Army gets here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_651D")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_6828")

    label("loc_653B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_65D0")
    EventBegin(0x2)
    TurnDirection(0x136, 0x0, 400)

    ChrTalk(    #253
        0x105,
        (
            "#042FThis is the way out to the highway.\x02\x03",

            "Let's get to the warehouse\x01",
            "district and find Clem.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_6828")

    label("loc_65D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_67AB")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_672E")
    OP_A2(0x8)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_667A")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #254
        0x102,
        (
            "#010FWe should stop by the guild\x01",
            "before we leave.\x02\x03",

            "Jean may have some work\x01",
            "for us.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #255
        0x101,
        "#000FOh, good thought.\x02",
    )

    CloseMessageWindow()
    Jump("loc_672B")

    label("loc_667A")

    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #256
        0x101,
        "#000FOh... Are we leaving already?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #257
        0x102,
        (
            "#010FNo, we should stop by the\x01",
            "guild first.\x02\x03",

            "Jean may have some work\x01",
            "for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x101,
        "#006FOkay, that sounds like a plan.\x02",
    )

    CloseMessageWindow()

    label("loc_672B")

    Jump("loc_678D")

    label("loc_672E")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #259
        0x102,
        (
            "#010FWe should stop by the guild\x01",
            "before we leave.\x02\x03",

            "Jean may have some work\x01",
            "for us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_678D")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_6828")

    label("loc_67AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6828")
    EventBegin(0x2)
    TurnDirection(0x136, 0x0, 400)

    ChrTalk(    #260
        0x136,
        (
            "#040FThat exit leads to the Aurian Causeway.\x02\x03",

            "How about we go back to town?\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_6828")

    Return()

    # Function_14_63FA end

    def Function_15_6829(): pass

    label("Function_15_6829")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #261
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_15_6829 end

    def Function_16_6878(): pass

    label("Function_16_6878")

    TalkBegin(0xFF)
    TalkEnd(0xFF)
    Return()

    # Function_16_6878 end

    def Function_17_687F(): pass

    label("Function_17_687F")

    SetPlaceName(0x69)
    Return()

    # Function_17_687F end

    def Function_18_6883(): pass

    label("Function_18_6883")

    SetPlaceName(0x52)
    Return()

    # Function_18_6883 end

    SaveToFile()

Try(main)
