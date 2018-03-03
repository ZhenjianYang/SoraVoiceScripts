from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C1500   ._SN',
        MapName             = 'Bose',
        Location            = 'C1500.x',
        MapIndex            = 61,
        MapDefaultBGM       = "ed60125",
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
        'Monster',                              # 9
        'Strange Monster',                      # 10
        'Krone Trail - Checkpoint',             # 11
        'West Bose Highway',                    # 12
        'Target Character',                     # 13
        'Target Camera',                        # 14
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
        'ED6_DT09/CH10200 ._CH',             # 00
        'ED6_DT29/CH14370 ._CH',             # 01
        'ED6_DT26/CH20700 ._CH',             # 02
        'ED6_DT26/CH20701 ._CH',             # 03
        'ED6_DT26/CH20702 ._CH',             # 04
        'ED6_DT26/CH20703 ._CH',             # 05
        'ED6_DT26/CH20704 ._CH',             # 06
        'ED6_DT26/CH20705 ._CH',             # 07
        'ED6_DT29/CH14371 ._CH',             # 08
        'ED6_DT29/CH14372 ._CH',             # 09
        'ED6_DT29/CH14373 ._CH',             # 0A
        'ED6_DT26/CH20709 ._CH',             # 0B
        'ED6_DT29/CH14373 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT09/CH10200P._CP',             # 00
        'ED6_DT29/CH14370P._CP',             # 01
        'ED6_DT26/CH20700P._CP',             # 02
        'ED6_DT26/CH20701P._CP',             # 03
        'ED6_DT26/CH20702P._CP',             # 04
        'ED6_DT26/CH20703P._CP',             # 05
        'ED6_DT26/CH20704P._CP',             # 06
        'ED6_DT26/CH20705P._CP',             # 07
        'ED6_DT29/CH14371P._CP',             # 08
        'ED6_DT29/CH14372P._CP',             # 09
        'ED6_DT29/CH14373P._CP',             # 0A
        'ED6_DT26/CH20709P._CP',             # 0B
        'ED6_DT29/CH14373P._CP',             # 0C
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -140810,
        Z                   = 6010,
        Y                   = -31010,
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
        X                   = -119390,
        Z                   = -60,
        Y                   = 180920,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1EE,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        X                   = -155740,
        Y                   = 3980,
        Z                   = 128479,
        Range               = -152500,
        Unknown_10          = 0xFFFFF8B2,
        Unknown_14          = 0x1FB58,
        Unknown_18          = 0x0,
        Unknown_1C          = 19,
    )


    DeclActor(
        TriggerX            = -153280,
        TriggerZ            = 4000,
        TriggerY            = 97180,
        TriggerRange        = 1500,
        ActorX              = -153280,
        ActorZ              = 4500,
        ActorY              = 97180,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 32,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -144990,
        TriggerZ            = 1960,
        TriggerY            = 163750,
        TriggerRange        = 1500,
        ActorX              = -144990,
        ActorZ              = 2460,
        ActorY              = 163750,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 33,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -156650,
        TriggerZ            = 2000,
        TriggerY            = 117940,
        TriggerRange        = 1500,
        ActorX              = -156650,
        ActorZ              = 2500,
        ActorY              = 117940,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 34,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -123200,
        TriggerZ            = 4070,
        TriggerY            = 93650,
        TriggerRange        = 1500,
        ActorX              = -123200,
        ActorZ              = 4570,
        ActorY              = 93650,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 35,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -152490,
        TriggerZ            = 2050,
        TriggerY            = 139950,
        TriggerRange        = 1500,
        ActorX              = -152490,
        ActorZ              = 2550,
        ActorY              = 139950,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 36,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2A6",          # 00, 0
        "Function_1_35B",          # 01, 1
        "Function_2_4C0",          # 02, 2
        "Function_3_63D",          # 03, 3
        "Function_4_6A9",          # 04, 4
        "Function_5_25DE",         # 05, 5
        "Function_6_2651",         # 06, 6
        "Function_7_268F",         # 07, 7
        "Function_8_271A",         # 08, 8
        "Function_9_279D",         # 09, 9
        "Function_10_27FA",        # 0A, 10
        "Function_11_2B14",        # 0B, 11
        "Function_12_2B75",        # 0C, 12
        "Function_13_2C00",        # 0D, 13
        "Function_14_2C81",        # 0E, 14
        "Function_15_2CA1",        # 0F, 15
        "Function_16_2CCD",        # 10, 16
        "Function_17_2D78",        # 11, 17
        "Function_18_2DAD",        # 12, 18
        "Function_19_2DDF",        # 13, 19
        "Function_20_31FA",        # 14, 20
        "Function_21_322F",        # 15, 21
        "Function_22_37B9",        # 16, 22
        "Function_23_3819",        # 17, 23
        "Function_24_3A9C",        # 18, 24
        "Function_25_49CA",        # 19, 25
        "Function_26_49FF",        # 1A, 26
        "Function_27_4A3D",        # 1B, 27
        "Function_28_4B68",        # 1C, 28
        "Function_29_4C09",        # 1D, 29
        "Function_30_4C20",        # 1E, 30
        "Function_31_4C4A",        # 1F, 31
        "Function_32_4C85",        # 20, 32
        "Function_33_4D4D",        # 21, 33
        "Function_34_4E11",        # 22, 34
        "Function_35_4ED5",        # 23, 35
        "Function_36_4FB6",        # 24, 36
    )


    def Function_0_2A6(): pass

    label("Function_0_2A6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 5)), scpexpr(EXPR_END)), "loc_2D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D7")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -152740, 4000, 101020, 32)

    label("loc_2D7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35A")
    OP_A3(0x1)
    OP_A3(0x2)
    OP_A3(0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_30E")
    OP_A3(0x2506)
    OP_A2(0x3)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 24)
    Jump("loc_35A")

    label("loc_30E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_330")
    OP_A3(0x2505)
    OP_A2(0x2)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 23)
    Jump("loc_35A")

    label("loc_330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_349")
    OP_A3(0x2504)
    OP_A2(0x1)
    SetMapFlags(0x10000000)
    Event(0, 10)
    Jump("loc_35A")

    label("loc_349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35A")
    SetMapFlags(0x10000000)
    Event(0, 4)

    label("loc_35A")

    Return()

    # Function_0_2A6 end

    def Function_1_35B(): pass

    label("Function_1_35B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_37D")
    OP_A3(0x2)
    OP_B1("C1500_2")
    OP_71(0x5, 0x0)
    ExitThread()
    OP_71(0x405, 0x0)
    ExitThread()
    Jump("loc_3D8")

    label("loc_37D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B4")
    OP_A3(0x1)
    OP_B1("C1500_1")
    OP_71(0x7, 0x0)
    ExitThread()
    OP_71(0x407, 0x0)
    ExitThread()
    OP_71(0x8, 0x0)
    ExitThread()
    OP_71(0x408, 0x0)
    ExitThread()
    Jump("loc_3D8")

    label("loc_3B4")

    OP_A3(0x3)
    OP_B1("C1500_0")
    OP_71(0x7, 0x0)
    ExitThread()
    OP_71(0x407, 0x0)
    ExitThread()
    OP_71(0x8, 0x0)
    ExitThread()
    OP_71(0x408, 0x0)
    ExitThread()

    label("loc_3D8")

    OP_11(0xFF, 0xFF, 0xFF, 0x9470, 0x1FBD0, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40D")
    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    OP_B2(0x0, 0x0, 0x80)

    label("loc_40D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 3)), scpexpr(EXPR_END)), "loc_418")
    OP_64(0x0, 0x1)

    label("loc_418")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 4)), scpexpr(EXPR_END)), "loc_423")
    OP_64(0x1, 0x1)

    label("loc_423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 5)), scpexpr(EXPR_END)), "loc_42E")
    OP_64(0x2, 0x1)

    label("loc_42E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 6)), scpexpr(EXPR_END)), "loc_439")
    OP_64(0x3, 0x1)

    label("loc_439")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 7)), scpexpr(EXPR_END)), "loc_444")
    OP_64(0x4, 0x1)

    label("loc_444")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 6)), scpexpr(EXPR_END)), "loc_450")
    OP_B2(0x0, 0x0, 0x80)

    label("loc_450")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BF")
    OP_71(0x0, 0x0)
    ExitThread()
    OP_71(0x400, 0x0)
    ExitThread()
    OP_71(0x200, 0x0)
    ExitThread()
    OP_71(0x1, 0x0)
    ExitThread()
    OP_71(0x401, 0x0)
    ExitThread()
    OP_71(0x201, 0x0)
    ExitThread()
    OP_71(0x2, 0x0)
    ExitThread()
    OP_71(0x402, 0x0)
    ExitThread()
    OP_71(0x202, 0x0)
    ExitThread()
    OP_71(0x3, 0x0)
    ExitThread()
    OP_71(0x403, 0x0)
    ExitThread()
    OP_71(0x203, 0x0)
    ExitThread()
    OP_71(0x4, 0x0)
    ExitThread()
    OP_71(0x404, 0x0)
    ExitThread()
    OP_71(0x204, 0x0)
    ExitThread()
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x1A6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4BF")

    Return()

    # Function_1_35B end

    def Function_2_4C0(): pass

    label("Function_2_4C0")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E5")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_627")

    label("loc_4E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FE")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_627")

    label("loc_4FE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_517")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_627")

    label("loc_517")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_530")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_627")

    label("loc_530")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_549")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_627")

    label("loc_549")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_562")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_627")

    label("loc_562")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57B")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_627")

    label("loc_57B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_594")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_627")

    label("loc_594")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AD")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_627")

    label("loc_5AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C6")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_627")

    label("loc_5C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DF")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_627")

    label("loc_5DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F8")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_627")

    label("loc_5F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_611")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_627")

    label("loc_611")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_627")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_627")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_63C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_627")

    label("loc_63C")

    Return()

    # Function_2_4C0 end

    def Function_3_63D(): pass

    label("Function_3_63D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_688")

    def lambda_64D():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_64D)

    ChrTalk(    #0
        0xFE,
        "Brrr... Hurry up, please!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xFE, 0x2)
    Jump("loc_6A5")

    label("loc_688")


    ChrTalk(    #1
        0xFE,
        "P-Pleeease hurry up!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_6A5")

    TalkEnd(0xFE)
    Return()

    # Function_3_63D end

    def Function_4_6A9(): pass

    label("Function_4_6A9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(2000)
    OP_11(0xFF, 0xFF, 0xFF, 0x9470, 0x1FBD0, 0x0)
    OP_6D(-144160, 5720, -27100, 0)
    OP_67(0, 5360, -10000, 0)
    OP_6C(344000, 0)
    OP_6B(3000, 0)
    OP_6E(262, 0)
    OP_6A(0x14E)
    OP_C4(0x0, 0x40)
    SetChrPos(0x14E, -144160, 5920, -28200, 315)

    def lambda_727():
        OP_8E(0xFE, 0xFFFDE20C, 0x17C0, 0xFFFFB834, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_727)
    FadeToBright(2000, 0)

    def lambda_74B():
        OP_6B(3160, 11000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_74B)

    def lambda_75B():
        OP_6E(352, 11000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_75B)

    def lambda_76B():
        OP_6C(314000, 11000)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_76B)
    OP_0D()

    ChrTalk(    #2 op#A
        0x14E,
        "#1717F#3S#15APolly!#2S\x02",
    )

    OP_7C(0x96, 0x96, 0xBB8, 0x12C)
    Sleep(2000)
    OP_56(0x0)

    ChrTalk(    #3 op#A
        0x14E,
        "#1717F#3S#15AAnswer me, Polly!#2S\x02",
    )

    OP_7C(0x96, 0x96, 0xBB8, 0x12C)
    Sleep(2000)
    OP_56(0x0)
    Sleep(1500)

    ChrTalk(    #4
        0x14E,
        "#1716F*sigh* Where, oh, where have you gone...?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    WaitChrThread(0x14E, 0x1)
    Sleep(300)
    Fade(1000)
    OP_6A(0xFF)
    OP_6D(-139330, 6050, -17610, 0)
    OP_67(0, 4700, -10000, 0)
    OP_6B(2160, 0)
    OP_6C(314000, 0)
    OP_6E(337, 0)
    OP_0D()
    OP_8C(0x14E, 0, 400)
    Sleep(1000)
    OP_8C(0x14E, 90, 400)
    Sleep(500)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x0, 0x1, 0xC8, 0x3)
    Sleep(1000)
    OP_63(0x14E)

    ChrTalk(    #5
        0x14E,
        (
            "#1714F...Huh? Where am I?\x02\x03",

            "#1713F(I-I've never been this far from the\x01",
            "orphanage before...)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14E, 0x0, 1600, 0x18, 0x1B, 0xC8, 0x2)
    Sleep(2000)
    OP_63(0x14E)
    Sleep(500)

    ChrTalk(    #6
        0x14E,
        (
            "#1713FIt looks like Polly's not the only one\x01",
            "who's lost...\x02\x03",

            "...\x02\x03",

            "#1901FWhat am I doing?\x02\x03",

            "I need to be strong and look after\x01",
            "the other children!\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_8C(0x14E, 315, 400)
    Sleep(800)

    ChrTalk(    #7
        0x14E,
        "#1713FI've got to find Polly.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(1000)
    OP_6D(-138740, 6080, -18380, 0)
    OP_67(0, 5360, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    OP_6A(0x14E)

    def lambda_A3E():
        OP_6C(270000, 12000)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_A3E)

    def lambda_A4E():
        OP_8E(0xFE, 0xFFFDBEBC, 0x1770, 0xFFFFD6AC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_A4E)
    Sleep(2000)

    ChrTalk(    #8
        0x14E,
        "#1713FThis is all my fault. It's all my fault...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #9
        0x14E,
        (
            "#1713FI never should've believed in that silly story...\x01",
            "I should never have taken Polly so far from\x01",
            "the orphanage...\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x14E, 0x1)

    ChrTalk(    #10
        0x14E,
        "#1901FHow could I have messed up so badly...?\x02",
    )

    CloseMessageWindow()
    OP_62(0x14E, 0x0, 1600, 0x18, 0x1B, 0xC8, 0x2)
    Sleep(2000)
    OP_63(0x14E)
    Sleep(500)
    OP_9E(0x14E, 0xF, 0x0, 0x12C, 0xBB8)

    ChrTalk(    #11
        0x14E,
        "#1901F#60W...\x02",
    )

    CloseMessageWindow()
    OP_6A(0xFF)
    SetChrFlags(0x14E, 0x40)

    def lambda_BA5():
        OP_6D(-151340, 5820, -7880, 1500)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_BA5)

    def lambda_BBD():
        OP_67(0, 4040, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_BBD)

    def lambda_BD5():
        OP_6C(282000, 1500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_BD5)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x40)
    SetChrPos(0x10, -159140, 6000, -400, 142)
    OP_43(0x10, 0x2, 0x0, 0xB)
    WaitChrThread(0x15, 0x0)
    Sleep(500)
    OP_43(0x14E, 0x2, 0x0, 0xC)
    Sleep(2000)

    def lambda_C1D():
        OP_6D(-149730, 5950, -12330, 5000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_C1D)

    def lambda_C35():
        OP_6C(257000, 5000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_C35)
    WaitChrThread(0x10, 0x2)

    def lambda_C4A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_C4A)
    WaitChrThread(0x10, 0x2)
    SetChrFlags(0x10, 0x80)
    WaitChrThread(0x15, 0x0)

    ChrTalk(    #12
        0x14E,
        "#1716FWhew...\x02",
    )

    CloseMessageWindow()

    def lambda_C7E():
        OP_6D(-149230, 5980, -10480, 3000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_C7E)

    def lambda_C96():
        OP_6C(269000, 3000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_C96)
    OP_44(0x14E, 0x3)

    def lambda_CAA():
        OP_8E(0xFE, 0xFFFDAFE4, 0x1734, 0xFFFFD2D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_CAA)
    WaitChrThread(0x14E, 0x1)

    def lambda_CCA():
        OP_8E(0xFE, 0xFFFDBE9E, 0x175C, 0xFFFFD7EC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_CCA)
    WaitChrThread(0x14E, 0x1)
    Sleep(300)
    OP_8C(0x14E, 135, 350)
    Sleep(800)
    WaitChrThread(0x15, 0x0)

    ChrTalk(    #13
        0x14E,
        (
            "#1713F#6PI've got to find Polly.\x02\x03",

            "#1712FIf a monster like that finds her before I do...!\x01",
            "I don't even want to think about it!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14E, 0x0, 1600, 0x28, 0x2B, 0x64, 0x0)
    Sleep(400)
    OP_8C(0x14E, 315, 600)
    OP_63(0x14E)

    ChrTalk(    #14
        0x14E,
        "#1717F#6PPlease! Be safe, Polly!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x14E, 0x0, 1600, 0x28, 0x2B, 0x64, 0x0)

    def lambda_DE1():
        OP_8E(0xFE, 0xFFFD86B8, 0x177A, 0xDD4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_DE1)
    Sleep(2000)
    Fade(1000)
    OP_44(0x14E, 0x1)
    OP_6D(-160450, 3980, 38710, 0)
    OP_67(0, 4560, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    SetChrPos(0x14E, -159720, 4059, 27990, 0)

    def lambda_E58():
        OP_8E(0xFE, 0xFFFD8F64, 0xF78, 0x9970, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_E58)
    OP_0D()
    WaitChrThread(0x14E, 0x1)
    OP_43(0x14E, 0x2, 0x0, 0xE)

    ChrTalk(    #15
        0x14E,
        "#1717F#3S#5PPolly! Pollyyy!#2S\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0xC8)
    CloseMessageWindow()
    WaitChrThread(0x14E, 0x2)
    WaitChrThread(0x14E, 0x2)

    def lambda_EBF():
        OP_8E(0xFE, 0xFFFD85DC, 0xF82, 0xBEA0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_EBF)
    Sleep(1200)
    Fade(1000)
    OP_44(0x14E, 0x1)
    OP_6D(-135440, 1980, 56260, 0)
    OP_67(0, 4560, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x14E, -142940, 2029, 64879, 135)

    def lambda_F36():
        OP_8E(0xFE, 0xFFFDF15C, 0x7A8, 0xDBC4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_F36)
    OP_0D()
    WaitChrThread(0x14E, 0x1)
    OP_43(0x14E, 0x2, 0x0, 0xF)

    ChrTalk(    #16
        0x14E,
        (
            "#1717F#3S#5PWhere are you, Polly?!\x01",
            "Answer me! Please!#2S\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0xC8)
    CloseMessageWindow()
    WaitChrThread(0x14E, 0x2)

    def lambda_FB2():
        OP_8E(0xFE, 0xFFFDD4CE, 0x7D0, 0xB734, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_FB2)
    Sleep(1800)
    Fade(1000)
    OP_44(0x14E, 0x1)
    OP_6D(-150400, 6340, 8980, 0)
    OP_67(0, 4560, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    SetChrPos(0x14E, -164560, 5990, 4120, 90)

    def lambda_1029():
        OP_8E(0xFE, 0xFFFDB480, 0x1798, 0x2314, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_1029)
    OP_0D()
    WaitChrThread(0x14E, 0x1)
    OP_63(0x14E)
    Sleep(500)

    ChrTalk(    #17
        0x14E,
        "#1716F#12P*pant* *pant*\x02",
    )

    CloseMessageWindow()

    def lambda_106F():
        OP_6D(-149400, 6280, 9140, 2000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_106F)

    def lambda_1087():
        OP_67(0, 4560, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1087)

    def lambda_109F():
        OP_6C(224000, 2000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_109F)

    def lambda_10AF():
        OP_6B(2560, 2000)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_10AF)

    def lambda_10BF():
        OP_8E(0xFE, 0xFFFDB868, 0x175C, 0x23B4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_10BF)

    def lambda_10DA():
        OP_9E(0xFE, 0xF, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x14E, 3, lambda_10DA)
    WaitChrThread(0x15, 0x0)
    WaitChrThread(0x14E, 0x1)

    ChrTalk(    #18
        0x14E,
        (
            "#1901F#12PPolly...please...\x02\x03",

            "#1901FJust come out...\x02\x03",

            "I know I messed up... So please,\x01",
            "just come out...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_116F():
        OP_6D(-148400, 6280, 9140, 2000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_116F)

    def lambda_1187():
        OP_8E(0xFE, 0xFFFDBB88, 0x175C, 0x23B4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_1187)
    WaitChrThread(0x14E, 0x1)
    Fade(100)
    SetChrChipByIndex(0x14E, 4)
    SetChrSubChip(0x14E, 0)
    SetChrFlags(0x14E, 0x2)
    SetChrFlags(0x14E, 0x800)
    SetChrFlags(0x14E, 0x20)
    SetChrFlags(0x14E, 0x4)

    def lambda_11CA():
        OP_99(0xFE, 0x0, 0x4, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_11CA)

    def lambda_11DA():
        OP_8F(0xFE, 0xFFFDBC50, 0x16EE, 0x23B4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_11DA)

    ChrTalk(    #19 op#A op#5
        0x14E,
        "#1902F#3S#4P#10A#12PEeek!\x05\x02",
    )

    OP_22(0x8E, 0x0, 0x28)
    OP_22(0xD1, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0xC8)
    CloseMessageWindow()
    Sleep(1000)

    def lambda_1235():
        OP_9E(0xFE, 0xF, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14E, 3, lambda_1235)

    ChrTalk(    #20
        0x14E,
        "#1901F#12PUgh...\x02",
    )

    CloseMessageWindow()
    OP_59()
    Sleep(800)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    SetChrSubChip(0x14E, 5)
    Sleep(1000)

    ChrTalk(    #21
        0x14E,
        (
            "#1901F#12P...\x02\x03",

            "#1901F(I mustn't cry... I mustn't cry...)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1500)

    def lambda_12C2():
        OP_9E(0xFE, 0xA, 0x0, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14E, 3, lambda_12C2)

    def lambda_12DC():
        OP_99(0xFE, 0x6, 0x7, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_12DC)

    ChrTalk(    #22
        0x14E,
        "#1901F#12P*sniffle*...*sob*...\x02",
    )

    CloseMessageWindow()
    Sleep(1000)

    def lambda_1315():
        OP_9E(0xFE, 0xA, 0x0, 0x0, 0x2EE)
        ExitThread()

    QueueWorkItem(0x14E, 3, lambda_1315)
    OP_43(0x14E, 0x0, 0x0, 0x8)
    StopSound(0x64, 0xC350, 0xFA0)
    Sleep(2000)

    def lambda_1348():
        OP_9E(0xFE, 0xA, 0x0, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14E, 3, lambda_1348)
    Sleep(2000)
    OP_44(0x14E, 0x3)
    Sleep(1000)
    StopSound(0x3DB8, 0xEA60, 0xBB8)
    Sleep(4000)
    SetChrPos(0x11, -143440, 4000, 20700, 200)

    NpcTalk(    #23
        0x11,
        "Voice",
        (
            "Bleeech... It's mad chilly this time of year,\x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1000, 0x2, 0x7, 0x96, 0x1)
    Sleep(1000)
    OP_63(0x14E)
    Fade(200)
    SetChrChipByIndex(0x14E, 65535)
    SetChrSubChip(0x14E, 0)
    SetChrPos(0x14E, -148400, 5970, 9140, 90)
    ClearChrFlags(0x14E, 0x2)
    ClearChrFlags(0x14E, 0x800)
    ClearChrFlags(0x14E, 0x20)
    ClearChrFlags(0x14E, 0x4)
    OP_95(0x14E, 0x0, 0x0, 0x0, 0x190, 0xFA0)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(300)
    OP_62(0x14E, 0x0, 1600, 0x28, 0x2B, 0x64, 0x0)

    def lambda_1457():
        OP_6D(-147340, 6140, 10920, 5000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_1457)

    def lambda_146F():
        OP_6C(234000, 5000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_146F)

    def lambda_147F():
        OP_6B(2980, 5000)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_147F)

    def lambda_148F():
        OP_67(0, 3760, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_148F)

    def lambda_14A7():
        OP_6E(264, 5000)
        ExitThread()

    QueueWorkItem(0x14E, 3, lambda_14A7)

    def lambda_14B7():
        OP_8E(0xFE, 0xFFFDBFD4, 0x17C0, 0x16D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_14B7)
    WaitChrThread(0x14E, 0x1)

    def lambda_14D7():
        OP_8E(0xFE, 0xFFFDC308, 0x1798, 0x17E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_14D7)
    WaitChrThread(0x14E, 0x1)
    OP_63(0x14E)
    OP_8C(0x14E, 0, 500)
    SetChrFlags(0x11, 0x800)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x40)
    OP_4A(0x11, 255)
    SetChrChipByIndex(0x11, 8)
    SetChrSubChip(0x11, 0)

    def lambda_151E():
        OP_8E(0xFE, 0xFFFDC650, 0x175C, 0x2ECC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_151E)
    WaitChrThread(0x11, 0x1)
    SetChrChipByIndex(0x11, 1)
    SetChrSubChip(0x11, 0)
    WaitChrThread(0x15, 0x0)
    OP_8C(0x11, 90, 280)
    Sleep(800)
    SetChrName("Mary")

    ChrTalk(    #24
        0x14E,
        "#1714F#2P...?!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrChipByIndex(0x11, 8)
    SetChrSubChip(0x11, 3)

    def lambda_1582():
        OP_9E(0xFE, 0x14, 0x0, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_1582)
    Sleep(300)
    WaitChrThread(0x11, 0x3)
    SetChrChipByIndex(0x11, 1)
    SetChrSubChip(0x11, 0)
    Sleep(300)
    SetChrName("Strange Monster")

    ChrTalk(    #25
        0x11,
        (
            "*yaaawn* Maybe I should go catch some\x01",
            "more ZZZs...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_1603():
        OP_6D(-149100, 6060, 7000, 2500)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_1603)

    def lambda_161B():
        OP_6C(210000, 2500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_161B)
    OP_8C(0x11, 225, 600)
    Sleep(500)
    SetChrChipByIndex(0x11, 8)
    SetChrSubChip(0x11, 0)

    def lambda_1641():
        OP_8E(0xFE, 0xFFFDBA98, 0x175C, 0x2314, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1641)
    Sleep(1000)
    SetChrFlags(0x14E, 0x4)

    def lambda_1666():
        OP_8E(0xFE, 0xFFFDC6AA, 0x17AC, 0x196E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_1666)
    WaitChrThread(0x14E, 0x1)

    def lambda_1686():
        OP_8E(0xFE, 0xFFFDC6C8, 0x17AC, 0x2788, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_1686)
    WaitChrThread(0x14E, 0x1)
    ClearChrFlags(0x14E, 0x4)
    OP_8C(0x14E, 260, 500)

    def lambda_16B2():

        label("loc_16B2")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_16B2")

    QueueWorkItem2(0x14E, 3, lambda_16B2)

    ChrTalk(    #26
        0x14E,
        "#1714FWh-Who are you?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x11, 0x1)

    ChrTalk(    #27
        0x11,
        "#2P...Huh?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 80, 500)
    Sleep(500)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x11, 0x0, 2300, 0x2, 0x7, 0xC8, 0x1)
    Sleep(200)
    OP_95(0x11, 0x0, 0x190, 0x0, 0x190, 0x1388)
    Sleep(1000)
    OP_63(0x11)

    def lambda_173A():
        OP_6D(-146880, 6090, 5530, 1500)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_173A)

    def lambda_1752():
        OP_67(0, 3480, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1752)

    def lambda_176A():
        OP_6C(180000, 1500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_176A)
    OP_8C(0x11, 180, 600)
    OP_22(0x81, 0x0, 0x64)
    ClearChrFlags(0x11, 0x800)

    def lambda_178B():
        OP_8E(0xFE, 0xFFFDC09C, 0x178E, 0x1892, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_178B)
    WaitChrThread(0x11, 0x1)

    def lambda_17AB():
        OP_9E(0xFE, 0xF, 0x0, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_17AB)
    OP_44(0x14E, 0x3)
    WaitChrThread(0x15, 0x0)

    ChrTalk(    #28
        0x11,
        (
            "#3S#2PWh-Wh-Wh-What's the b-big deal?\x01",
            "Don't scare a dragon like that!#2S\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_44(0x11, 0x0)
    Sleep(300)

    ChrTalk(    #29
        0x11,
        (
            "#2PI thought my heart was gonna go pumpin'\x01",
            "right outta my ch-chest!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1873():
        OP_6D(-147360, 5980, 3220, 2000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_1873)

    def lambda_188B():
        OP_67(0, 2920, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_188B)

    def lambda_18A3():
        OP_6B(3070, 2000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_18A3)

    def lambda_18B3():
        OP_6C(180000, 2000)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_18B3)

    def lambda_18C3():
        OP_8E(0xFE, 0xFFFDC02E, 0x173E, 0x2134, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_18C3)
    WaitChrThread(0x14E, 0x1)
    OP_8C(0x14E, 180, 400)
    WaitChrThread(0x15, 0x0)

    ChrTalk(    #30
        0x14E,
        "#1714F#6P...Huh...\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2300, 0x28, 0x2B, 0x64, 0x2)
    TurnDirection(0x11, 0x14E, 600)
    Sleep(500)

    ChrTalk(    #31
        0x11,
        (
            "#11P...Whuzzat?\x02\x03",

            "Somethin' on my face, lil' buddy?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x11, 0x3)

    ChrTalk(    #32
        0x14E,
        (
            "#1903F#6PPffft...#3S Hahahaha!\x01",
            "You're weird! #2S\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x14E,
        "#1903F#6P#3SAhahahahahaha!#2S\x02",
    )

    OP_7C(0x64, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x11, 0x0, 2300, 0x28, 0x2B, 0x64, 0x2)
    Sleep(1000)

    ChrTalk(    #34
        0x11,
        (
            "#11P#40WHeeeeeey...#200W \x01",
            "#20WIt's WAY not cool to laugh that much!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x14E,
        (
            "#1718F#6PHeeheehee... Sorry. What are you doing here,\x01",
            "anyway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x11,
        "#11PWho, me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x11,
        (
            "#11PI was just keeping my head low while\x01",
            "all that scary stuff was going down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x14E,
        "#1714F#6PScary stuff? Like what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x11,
        (
            "#11PLike the Glorious and the Aureole and junk...\x01",
            "Didn't you hear about them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x14E,
        "#1900F#6PI... I don't think so?\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_1B77():
        OP_6B(3000, 3000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1B77)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(-144710, 2210, 47660, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(280000, 0)
    OP_6E(325, 0)
    SetChrPos(0x14E, -140720, 2020, 46040, 45)
    SetChrPos(0x11, -142140, 2000, 47480, 45)
    SetChrFlags(0x11, 0x800)
    SoundLoad(16)

    def lambda_1BFE():
        OP_8E(0xFE, 0xFFFDE5A4, 0x7F8, 0xC030, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_1BFE)
    SetChrChipByIndex(0x11, 8)
    SetChrSubChip(0x11, 0)

    def lambda_1C23():
        OP_8E(0xFE, 0xFFFDDE60, 0x7D0, 0xC5A8, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1C23)
    OP_43(0x14E, 0x3, 0x0, 0x9)
    FadeToBright(2000, 0)

    def lambda_1C4E():
        OP_6D(-140810, 2070, 50260, 4500)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_1C4E)

    def lambda_1C66():
        OP_6C(267000, 4500)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_1C66)
    WaitChrThread(0x15, 0x0)
    Fade(1000)
    OP_6D(-141100, 2029, 49930, 0)
    OP_67(0, 5390, -10000, 0)
    OP_6B(3060, 0)
    OP_6C(267000, 0)
    OP_6E(250, 0)
    OP_0D()
    WaitChrThread(0x14E, 0x1)
    WaitChrThread(0x11, 0x1)
    SetChrChipByIndex(0x11, 1)
    SetChrSubChip(0x11, 0)
    TurnDirection(0x14E, 0x11, 500)
    Sleep(100)
    TurnDirection(0x11, 0x14E, 500)
    Sleep(500)

    ChrTalk(    #41
        0x14E,
        "#1710FHuh... Okay. Are you a baby dragon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x11,
        "#2PYuppers! I'm only 320 years old!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x14E,
        "#1714FWhat?! Really?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x11,
        "#2PWhy're you so surprised? That's totally normal.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x14E,
        (
            "#1714FI-It is?\x02\x03",

            "#1900FI'm not so sure about that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x11,
        "#2PAnyway, I'm bored. I want some grub!!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 45, 400)
    Sleep(800)
    OP_8C(0x11, 180, 400)
    Sleep(800)

    ChrTalk(    #47
        0x11,
        (
            "#2PDo you know if there any dandelions that\x01",
            "bloom around here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x14E,
        "#1714FIs that what you eat?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 145, 400)
    Sleep(400)

    ChrTalk(    #49
        0x11,
        (
            "#2PSunflowers are yummylicious, too!\x02\x03",

            "They taste just like the sun! No lie! ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x14E,
        "#1900FI didn't know that...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x14E, 0x0, 1600, 0x26, 0x27, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x14E)

    ChrTalk(    #51
        0x14E,
        "#1718FOh, I know!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x14E, 235, 400)
    Sleep(300)
    OP_62(0x14E, 0x0, 1600, 0x18, 0x1B, 0xC8, 0x2)
    Sleep(1000)
    OP_63(0x14E)
    Sleep(500)
    TurnDirection(0x14E, 0x11, 400)
    Sleep(100)
    OP_62(0x14E, 0x0, 1600, 0x26, 0x27, 0xFA, 0x1)

    ChrTalk(    #52
        0x14E,
        (
            "#1711FTa-daaa! You can have one of my super-special\x01",
            "sandwiches!\x02\x03",

            "They haven't got any dandelions or sunflowers in\x01",
            "them, but they've got some plants from our garden\x01",
            "in them! \x02\x03",

            "#1718FSo I'm sure they'll have a sunny taste to them!\x02\x03",

            "Okaaay! Open wide, now...\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x11, 8)
    SetChrSubChip(0x11, 3)
    Sleep(250)

    def lambda_2092():
        OP_6D(-141090, 2050, 50180, 1000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_2092)

    def lambda_20AA():
        OP_6B(2940, 1000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_20AA)

    def lambda_20BA():
        OP_8F(0xFE, 0xFFFDE248, 0x7D0, 0xC1D4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_20BA)
    WaitChrThread(0x14E, 0x1)
    WaitChrThread(0x15, 0x0)
    Sleep(300)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_20E9():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x258, 0xFA0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_20E9)
    WaitChrThread(0x14E, 0x1)
    Sleep(300)
    SetChrChipByIndex(0x11, 8)
    SetChrSubChip(0x11, 7)
    Sleep(300)
    OP_22(0x10, 0x0, 0x64)
    OP_9E(0x11, 0x0, 0x14, 0x3E8, 0x3E8)
    Sleep(1000)

    ChrTalk(    #53
        0x14E,
        "#1710FSo? What do you think?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x11,
        "#2P*munch* *munch*\x02",
    )

    CloseMessageWindow()
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x11, 0x0, 2300, 0x2, 0x7, 0xC8, 0x1)
    Sleep(1000)
    OP_63(0x11)

    ChrTalk(    #55
        0x11,
        "#2PThat was SO GOOD!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x14E,
        (
            "#1719FI made it all myself, too.\x02\x03",

            "Heehee. Aren't I amazing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x11,
        "#2PW-Wow! You're crazy amazing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x11,
        "#2PCan I have another one?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x14E,
        (
            "#1714FAnother one?! But I've only got one left,\x01",
            "and that one's supposed to be mine...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x11,
        "#2PGimme half, then! Pretty pleeease?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x14E,
        (
            "#1710FWell...I suppose I could.\x02\x03",

            "#1711FOkay. You win!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xF, 0x0, 0x64)
    OP_62(0x11, 0x0, 2200, 0x8, 0x9, 0xC8, 0x5)
    Sleep(2000)
    OP_63(0x11)
    OP_43(0x11, 0x3, 0x0, 0x5)
    Sleep(2000)

    def lambda_2323():
        OP_6B(2900, 3000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2323)
    FadeToDark(2000, 0, -1)
    OP_0D()
    WaitChrThread(0x15, 0x1)
    Sleep(1000)
    OP_6D(-153950, 2009, 119810, 0)
    OP_67(0, 9000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(251000, 0)
    OP_6E(262, 0)
    StopSound(0x3DB8, 0x15F90, 0x0)

    def lambda_2392():
        OP_6C(280000, 10000)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_2392)
    SetChrPos(0x14E, -155900, 2040, 132380, 156)
    SetChrPos(0x11, -155900, 2040, 132380, 156)
    SetChrChipByIndex(0x11, 8)
    SetChrSubChip(0x11, 0)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_43(0x14E, 0x3, 0x0, 0x6)
    OP_43(0x14E, 0x2, 0x0, 0x7)
    Sleep(500)
    OP_43(0x11, 0x3, 0x0, 0x6)
    WaitChrThread(0x14E, 0x3)

    def lambda_23FB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14E, 0, lambda_23FB)

    def lambda_240D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_240D)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x14E, 0x2)
    OP_44(0x15, 0x3)
    Sleep(1000)
    OP_6D(-155120, 2000, 120200, 0)
    OP_67(0, 6280, -10000, 0)
    OP_6B(3060, 0)
    OP_6C(298000, 0)
    OP_6E(262, 0)
    OP_9F(0x14E, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x14E, -156480, 2009, 118340, 250)
    SetChrPos(0x11, -149000, 2040, 120990, 250)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_24B7():
        OP_8F(0xFE, 0xFFFDB0A2, 0x7BC, 0x1D5F6, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_24B7)
    Sleep(1500)

    def lambda_24D7():
        OP_8C(0xFE, 70, 400)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_24D7)
    WaitChrThread(0x14E, 0x2)
    Sleep(300)
    OP_62(0x14E, 0x0, 1600, 0x18, 0x1B, 0xC8, 0x2)
    Sleep(1000)
    OP_63(0x14E)
    Sleep(500)

    def lambda_250E():
        OP_8C(0xFE, 250, 500)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_250E)
    WaitChrThread(0x14E, 0x2)
    Sleep(500)

    def lambda_2526():
        OP_8F(0xFE, 0xFFFDA738, 0x7E4, 0x1D254, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2526)
    Sleep(1000)

    def lambda_2546():
        OP_8C(0xFE, 70, 700)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_2546)
    WaitChrThread(0x14E, 0x2)
    OP_44(0x11, 0x1)
    OP_62(0x11, 0x0, 2200, 0x10, 0x13, 0xC8, 0x1)
    Sleep(1000)
    OP_9E(0x11, 0x14, 0x0, 0x3E8, 0x7D0)
    Sleep(1000)
    OP_62(0x14E, 0x0, 1600, 0x26, 0x27, 0xC8, 0x2)
    OP_95(0x14E, 0x0, 0x12C, 0x0, 0x12C, 0x1388)
    OP_95(0x14E, 0x0, 0x12C, 0x0, 0x12C, 0x1388)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/C1500   ._SN", 100, 0, 1)
    IdleLoop()
    Return()

    # Function_4_6A9 end

    def Function_5_25DE(): pass

    label("Function_5_25DE")

    Fade(250)
    SetChrChipByIndex(0x11, 8)
    SetChrSubChip(0x11, 3)
    Sleep(250)
    Sleep(500)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_2602():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x258, 0xFA0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_2602)
    WaitChrThread(0x14E, 0x1)
    Sleep(300)
    SetChrChipByIndex(0x11, 8)
    SetChrSubChip(0x11, 7)
    Sleep(300)
    OP_22(0x10, 0x0, 0x64)
    OP_9E(0x11, 0x0, 0x14, 0x3E8, 0x3E8)
    Sleep(1000)
    Return()

    # Function_5_25DE end

    def Function_6_2651(): pass

    label("Function_6_2651")

    OP_8F(0xFE, 0xFFFDAEF4, 0x7C6, 0x1D740, 0x1388, 0x0)
    OP_97(0xFE, 0xFFFDA6CA, 0x1D33A, 0x57E40, 0x1388, 0x1)
    OP_8F(0xFE, 0xFFFDBE26, 0xECE, 0x1B346, 0x1388, 0x0)
    Return()

    # Function_6_2651 end

    def Function_7_268F(): pass

    label("Function_7_268F")

    Sleep(500)
    OP_62(0x14E, 0x0, 1600, 0x26, 0x27, 0xC8, 0x2)
    Sleep(400)
    OP_62(0x11, 0x0, 2500, 0x26, 0x27, 0xC8, 0x2)
    Sleep(2000)
    OP_62(0x14E, 0x0, 1600, 0x26, 0x27, 0xC8, 0x2)
    Sleep(400)
    OP_62(0x11, 0x0, 2500, 0x26, 0x27, 0xC8, 0x2)
    Sleep(2000)
    OP_62(0x14E, 0x0, 1600, 0x26, 0x27, 0xC8, 0x2)
    Sleep(400)
    OP_62(0x11, 0x0, 2500, 0x26, 0x27, 0xC8, 0x2)
    Return()

    # Function_7_268F end

    def Function_8_271A(): pass

    label("Function_8_271A")

    OP_22(0x1C3, 0x1, 0x1E)
    Sleep(200)
    OP_24(0x1C3, 0x28)
    Sleep(200)
    OP_24(0x1C3, 0x32)
    Sleep(200)
    OP_24(0x1C3, 0x3C)
    Sleep(200)
    OP_24(0x1C3, 0x46)
    Sleep(200)
    OP_24(0x1C3, 0x50)
    Sleep(200)
    OP_24(0x1C3, 0x5A)
    Sleep(4000)
    OP_24(0x1C3, 0x50)
    Sleep(200)
    OP_24(0x1C3, 0x46)
    Sleep(200)
    OP_24(0x1C3, 0x3C)
    Sleep(200)
    OP_24(0x1C3, 0x32)
    Sleep(200)
    OP_24(0x1C3, 0x28)
    Sleep(200)
    OP_24(0x1C3, 0x1E)
    Sleep(200)
    OP_24(0x1C3, 0x14)
    Sleep(200)
    OP_23(0x1C3)
    Return()

    # Function_8_271A end

    def Function_9_279D(): pass

    label("Function_9_279D")

    Sleep(1200)
    OP_62(0x14E, 0x0, 1600, 0x26, 0x27, 0xC8, 0x2)
    Sleep(800)
    OP_62(0x11, 0x0, 2300, 0x26, 0x27, 0xC8, 0x2)
    Sleep(1600)
    OP_62(0x14E, 0x0, 1600, 0x26, 0x27, 0xC8, 0x2)
    Sleep(800)
    OP_62(0x11, 0x0, 2300, 0x26, 0x27, 0xC8, 0x2)
    Return()

    # Function_9_279D end

    def Function_10_27FA(): pass

    label("Function_10_27FA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(2000)
    OP_6D(-152660, 4800, 102120, 0)
    OP_67(0, 4820, -10000, 0)
    OP_6B(3340, 0)
    OP_6C(248000, 0)
    OP_6E(282, 0)
    SetChrPos(0x14E, -151400, 4040, 103280, 202)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x40)
    OP_4A(0x11, 255)
    SetChrPos(0x11, -152740, 4000, 101020, 32)

    def lambda_287E():
        OP_6B(2740, 5000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_287E)

    def lambda_288E():
        OP_6E(262, 5000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_288E)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_62(0x14E, 0x0, 1600, 0x26, 0x27, 0xC8, 0x2)
    Sleep(1000)
    OP_62(0x11, 0x0, 2200, 0x26, 0x27, 0xC8, 0x2)
    Sleep(1000)
    OP_62(0x14E, 0x0, 1600, 0x26, 0x27, 0xC8, 0x3)
    Sleep(1000)
    OP_62(0x11, 0x0, 2200, 0x26, 0x27, 0xC8, 0x3)
    OP_0D()
    WaitChrThread(0x15, 0x1)
    OP_63(0x14E)
    OP_63(0x11)
    OP_43(0x14E, 0x3, 0x0, 0x12)
    Sleep(2000)
    OP_9E(0x11, 0x14, 0x0, 0x3E8, 0x7D0)
    Sleep(1000)
    OP_8C(0x11, 350, 400)
    Sleep(800)
    OP_8C(0x11, 100, 400)
    Sleep(800)

    ChrTalk(    #62
        0x11,
        "#5PBrrr... It's sure getting chilly now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x14E,
        (
            "#1900F#12PY-You think?\x02\x03",

            "#1714FDo you have trouble dealing with the cold?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 32, 400)
    Sleep(400)

    ChrTalk(    #64
        0x11,
        (
            "#5PN-Nuh-uh!\x02\x03",

            "I do awesome with the cold! I swear!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x14E,
        (
            "#1710F#12PIt's nothing to be ashamed of! I'll go gather\x01",
            "some firewood, okay? \x02\x03",

            "#1718FIt'll get a lot warmer if we start a fire.\x02\x03",

            "...Just wait here, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x11,
        (
            "#5PO-Okay...\x02\x03",

            "Can you be fast, though? Please?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    ClearChrFlags(0x14E, 0x40)
    ClearChrFlags(0x11, 0x40)
    OP_4B(0x11, 255)
    OP_A3(0x2F1B)
    OP_A3(0x2F1C)
    OP_A3(0x2F1D)
    OP_A3(0x2F1E)
    OP_A3(0x2F1F)
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    OP_A2(0x2F25)
    EventEnd(0x0)
    Return()

    # Function_10_27FA end

    def Function_11_2B14(): pass

    label("Function_11_2B14")


    def lambda_2B1A():
        OP_8F(0xFE, 0xFFFDB700, 0x1798, 0xFFFFE7C8, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2B1A)
    WaitChrThread(0x10, 0x1)

    def lambda_2B3A():
        OP_8F(0xFE, 0xFFFDC86C, 0x175C, 0xFFFFCC0C, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2B3A)
    WaitChrThread(0x10, 0x1)

    def lambda_2B5A():
        OP_8F(0xFE, 0xFFFDD938, 0x17D4, 0xFFFFC284, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2B5A)
    WaitChrThread(0x10, 0x1)
    Return()

    # Function_11_2B14 end

    def Function_12_2B75(): pass

    label("Function_12_2B75")

    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x2, 0x7, 0x78, 0x1)
    Sleep(1000)
    OP_63(0x14E)
    OP_62(0x14E, 0x0, 1600, 0x28, 0x2B, 0x64, 0x0)

    def lambda_2BAC():
        OP_8E(0xFE, 0xFFFDAF6C, 0x1734, 0xFFFFD29C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_2BAC)
    WaitChrThread(0x14E, 0x1)

    def lambda_2BCC():
        OP_8E(0xFE, 0xFFFDAC88, 0x1734, 0xFFFFD4E0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_2BCC)
    WaitChrThread(0x14E, 0x1)

    def lambda_2BEC():

        label("loc_2BEC")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_2BEC")

    QueueWorkItem2(0x14E, 3, lambda_2BEC)
    Sleep(500)
    OP_63(0x14E)
    Return()

    # Function_12_2B75 end

    def Function_13_2C00(): pass

    label("Function_13_2C00")


    def lambda_2C06():
        OP_8E(0xFE, 0xFFFDB1D8, 0x17FC, 0xFFFFEE44, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_2C06)
    WaitChrThread(0x14E, 0x1)

    def lambda_2C26():
        OP_8E(0xFE, 0xFFFD907C, 0x175C, 0xFFFFFD44, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_2C26)
    WaitChrThread(0x14E, 0x1)

    def lambda_2C46():
        OP_8E(0xFE, 0xFFFD9C84, 0x177A, 0x1CAC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_2C46)
    WaitChrThread(0x14E, 0x1)

    def lambda_2C66():
        OP_8E(0xFE, 0xFFFDB480, 0x1798, 0x2314, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_2C66)
    WaitChrThread(0x14E, 0x1)
    Return()

    # Function_13_2C00 end

    def Function_14_2C81(): pass

    label("Function_14_2C81")

    OP_8C(0x14E, 315, 500)
    Sleep(600)
    OP_8C(0x14E, 90, 500)
    Sleep(600)
    OP_8C(0x14E, 0, 500)
    Return()

    # Function_14_2C81 end

    def Function_15_2CA1(): pass

    label("Function_15_2CA1")

    OP_8C(0x14E, 90, 500)
    Sleep(600)
    OP_8C(0x14E, 270, 500)
    Sleep(600)
    OP_8C(0x14E, 15, 500)
    Sleep(600)
    OP_8C(0x14E, 225, 500)
    Return()

    # Function_15_2CA1 end

    def Function_16_2CCD(): pass

    label("Function_16_2CCD")


    def lambda_2CD3():
        OP_6D(-158840, 6000, -40, 3900)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_2CD3)

    def lambda_2CEB():
        OP_67(0, 5700, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2CEB)

    def lambda_2D03():
        OP_6C(166000, 4000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_2D03)

    def lambda_2D13():
        OP_6B(2580, 4000)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_2D13)
    WaitChrThread(0x15, 0x1)

    def lambda_2D28():
        OP_6D(-150400, 6340, 8980, 3000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_2D28)

    def lambda_2D40():
        OP_67(0, 4560, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2D40)

    def lambda_2D58():
        OP_6C(224000, 2000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_2D58)

    def lambda_2D68():
        OP_6B(2700, 3000)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_2D68)
    WaitChrThread(0x15, 0x0)
    Return()

    # Function_16_2CCD end

    def Function_17_2D78(): pass

    label("Function_17_2D78")

    SetChrChipByIndex(0x11, 8)
    SetChrSubChip(0x11, 0)

    def lambda_2D88():
        OP_8F(0xFE, 0xFFFDB6A6, 0x17AC, 0x21A2, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2D88)
    WaitChrThread(0x11, 0x1)
    SetChrChipByIndex(0x11, 1)
    SetChrSubChip(0x11, 0)
    Return()

    # Function_17_2D78 end

    def Function_18_2DAD(): pass

    label("Function_18_2DAD")

    OP_22(0x1C3, 0x0, 0x64)
    Sleep(2500)
    OP_24(0x1C3, 0x50)
    Sleep(200)
    OP_24(0x1C3, 0x3C)
    Sleep(200)
    OP_24(0x1C3, 0x28)
    Sleep(200)
    OP_24(0x1C3, 0x14)
    Sleep(200)
    OP_23(0x1C3)
    Return()

    # Function_18_2DAD end

    def Function_19_2DDF(): pass

    label("Function_19_2DDF")

    EventBegin(0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_C4(0x0, 0x20000000)
    EventBegin(0x0)
    OP_6D(-154790, 2070, 128600, 0)
    OP_67(0, 4570, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(297000, 0)
    OP_6E(262, 0)
    SetChrPos(0x14E, -153300, 2110, 126400, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x40)
    OP_4A(0x11, 255)
    SetChrPos(0x11, -151220, 1980, 119660, 0)

    def lambda_2E67():
        OP_8E(0xFE, 0xFFFDA36E, 0x74E, 0x1FA72, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_2E67)
    FadeToBright(2000, 0)
    Sleep(1500)
    OP_43(0x11, 0x3, 0x0, 0x14)
    WaitChrThread(0x14E, 0x1)
    OP_62(0x14E, 0x0, 1600, 0x26, 0x27, 0xFA, 0x1)
    Sleep(500)
    OP_63(0x14E)
    OP_8C(0x14E, 180, 400)
    Sleep(500)

    ChrTalk(    #67
        0x14E,
        "#1714FHuh? I thought you were going to wait for me?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x11, 0x3)

    ChrTalk(    #68
        0x11,
        "B-But it's getting dark now!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x11,
        "B-Being out in the dark alone is kinda scary...\x02",
    )

    CloseMessageWindow()

    def lambda_2F57():
        OP_8E(0xFE, 0xFFFDA878, 0x802, 0x1F0FE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_2F57)
    WaitChrThread(0x14E, 0x1)
    OP_22(0xD1, 0x0, 0x64)

    def lambda_2F7C():
        OP_9E(0x11, 0x14, 0x0, 0x7D0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_2F7C)

    ChrTalk(    #70
        0x14E,
        "#1719F#2P*hug*\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x14E, 0x2)
    Sleep(500)

    def lambda_2FB4():
        OP_8F(0xFE, 0xFFFDA63E, 0x7E4, 0x1F5F4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_2FB4)
    WaitChrThread(0x14E, 0x1)
    Sleep(300)

    ChrTalk(    #71
        0x14E,
        "#1710F#2PThere, there. Feel any better now?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrChipByIndex(0x11, 8)
    SetChrSubChip(0x11, 0)

    def lambda_3019():
        OP_8E(0xFE, 0xFFFDA7BA, 0x7ED, 0x1F1C6, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3019)
    WaitChrThread(0x11, 0x1)
    SetChrChipByIndex(0x11, 1)
    SetChrSubChip(0x11, 0)
    Sleep(300)

    def lambda_3048():
        OP_9E(0x14E, 0xA, 0x0, 0x7D0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_3048)

    ChrTalk(    #72
        0x14E,
        (
            "#1903F#2PHeehee. Stop that! You're tickling me!\x02\x03",

            "You're so soft, and you smell so nice...\x02\x03",

            "#1714F(Huh? This smells like...)\x02\x03",

            "(...I can't remember. This smell is just somehow\x01",
            "familiar...)\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x14E, 0x2)
    Sleep(500)
    SetChrChipByIndex(0x11, 8)
    SetChrSubChip(0x11, 0)

    def lambda_3136():
        OP_8F(0xFE, 0xFFFDA9CC, 0x83E, 0x1EDC0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3136)
    WaitChrThread(0x11, 0x1)
    SetChrChipByIndex(0x11, 1)
    SetChrSubChip(0x11, 0)
    Sleep(300)

    ChrTalk(    #73
        0x11,
        (
            "I'll help you look for firewood, too!\x02\x03",

            "That way we'll both be warmer!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x14E,
        "#1718F#2PThat sounds great!\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    ClearChrFlags(0x11, 0x1)
    AddParty(0x4F, 0xFF, 0xFF)
    SetChrPos(0x150, -153140, 2110, 126400, 0)
    OP_A2(0x2F26)
    OP_B2(0x0, 0x0, 0x80)
    EventEnd(0x0)
    Return()

    # Function_19_2DDF end

    def Function_20_31FA(): pass

    label("Function_20_31FA")

    SetChrChipByIndex(0x11, 8)
    SetChrSubChip(0x11, 0)

    def lambda_320A():
        OP_8E(0xFE, 0xFFFDA9CC, 0x83E, 0x1EDC0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_320A)
    WaitChrThread(0x11, 0x1)
    SetChrChipByIndex(0x11, 1)
    SetChrSubChip(0x11, 0)
    Return()

    # Function_20_31FA end

    def Function_21_322F(): pass

    label("Function_21_322F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x20000000)
    OP_6D(-165040, 6000, 3720, 0)
    OP_67(0, 7260, -10000, 0)
    OP_6B(3040, 0)
    OP_6C(284000, 0)
    OP_6E(280, 0)
    SoundLoad(270)
    SetChrPos(0x14E, -162570, 6010, 3090, 280)
    RemoveParty(0x4F, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x11, 0x8)
    SetChrFlags(0x11, 0x1)
    SetChrPos(0x11, -166680, 5990, 6400, 140)
    OP_4A(0x11, 255)
    SetChrPos(0x14, -163760, 6800, 3390, 0)
    OP_72(0x7, 0x0)
    ExitThread()
    OP_72(0x407, 0x0)
    ExitThread()
    LoadEffect(0x0, "map\\\\bigfire.eff")
    LoadEffect(0x1, "monster\\\\ms30703.eff")

    def lambda_3306():
        OP_6D(-166920, 5980, 4190, 4000)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_3306)

    def lambda_331E():
        OP_67(0, 4720, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_331E)

    def lambda_3336():
        OP_6B(2660, 4000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3336)

    def lambda_3346():
        OP_6E(262, 4000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_3346)
    FadeToBright(2000, 0)
    OP_0D()
    OP_43(0x14E, 0x3, 0x0, 0x16)
    WaitChrThread(0x15, 0x0)
    WaitChrThread(0x14E, 0x3)

    ChrTalk(    #75
        0x14E,
        (
            "#1718F#5POkay. This should do.\x02\x03",

            "#1900F...Wait. We're going to need some fire\x01",
            "to get this started, aren't we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x11,
        "#2PDon't sweat it! I got this.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x14E, 320, 500)
    Sleep(200)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x0, 0x1, 0xC8, 0x3)
    Sleep(1000)
    OP_63(0x14E)

    def lambda_3432():
        OP_6D(-167740, 5970, 4630, 1300)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_3432)

    def lambda_344A():
        OP_6B(2560, 1300)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_344A)

    def lambda_345A():
        OP_6C(257000, 1300)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_345A)

    def lambda_346A():
        OP_8E(0xFE, 0xFFFD75D8, 0x1766, 0xFDB, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_346A)
    WaitChrThread(0x14E, 0x1)
    OP_8C(0x14E, 100, 500)
    WaitChrThread(0x15, 0x0)
    Sleep(300)
    SetChrChipByIndex(0x11, 8)
    SetChrSubChip(0x11, 0)

    def lambda_34A5():
        OP_8E(0xFE, 0xFFFD772C, 0x1766, 0x16BC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_34A5)
    WaitChrThread(0x11, 0x1)
    SetChrChipByIndex(0x11, 1)
    SetChrSubChip(0x11, 0)
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x11, 3)
    SetChrSubChip(0x11, 0)
    Sleep(800)
    SetChrPos(0x14, -163760, 6800, 3390, 0)

    def lambda_34F9():

        label("loc_34F9")

        OP_7C(0x32, 0x32, 0xBB8, 0x3E8)
        OP_48()
        Jump("loc_34F9")

    QueueWorkItem2(0x14, 3, lambda_34F9)
    OP_22(0x26D, 0x0, 0x64)
    PlayEffect(0x1, 0x0, 0x11, 500, 1040, 500, 0, -30, 0, 500, 500, 500, 0x14, 0, 0, 0, 0)
    Sleep(1000)
    PlayEffect(0x0, 0x1, 0xFF, -163760, 6100, 3390, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_71(0x7, 0x0)
    ExitThread()
    OP_71(0x407, 0x0)
    ExitThread()
    OP_72(0x8, 0x0)
    ExitThread()
    OP_72(0x408, 0x0)
    ExitThread()
    Sleep(1000)
    OP_44(0x14, 0x3)
    OP_22(0x10E, 0x1, 0x5A)
    Sleep(1500)
    Fade(500)
    SetChrChipByIndex(0x11, 1)
    SetChrSubChip(0x11, 0)
    Sleep(800)

    ChrTalk(    #77
        0x14E,
        "#1714F#5PW-Wow! You can really breathe fire?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x11,
        "#2PAnyone can do it if they practice enough!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x14E, 340, 500)
    Sleep(400)

    ChrTalk(    #79
        0x14E,
        "#1712FNo, they can't!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 160, 600)
    Sleep(400)

    ChrTalk(    #80
        0x11,
        "#2PUh-HUH! They can!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x11,
        "#2PI only learned how to do it recently, too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x14E,
        (
            "#1714FOh, really?\x02\x03",

            "#1900FI-I wonder if I'd be able to do it if\x01",
            "I practiced enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x11,
        (
            "#2PI'm sure you could if you practiced\x01",
            "for 320 years like me.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14E, 0x0, 1600, 0x28, 0x2B, 0x64, 0x2)
    Sleep(300)

    ChrTalk(    #84
        0x14E,
        "#1717FI-I'm not even going to live that long!\x02",
    )

    CloseMessageWindow()

    def lambda_3791():
        OP_6B(2660, 3000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3791)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_21()
    OP_A2(0x2505)
    NewScene("ED6_DT21/C1500   ._SN", 100, 0, 1)
    IdleLoop()
    Return()

    # Function_21_322F end

    def Function_22_37B9(): pass

    label("Function_22_37B9")


    def lambda_37BF():

        label("loc_37BF")

        TurnDirection(0xFE, 0x14, 500)
        OP_48()
        Jump("loc_37BF")

    QueueWorkItem2(0x14E, 2, lambda_37BF)

    def lambda_37D0():
        OP_8F(0xFE, 0xFFFD808C, 0x1770, 0x1130, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_37D0)
    WaitChrThread(0x14E, 0x1)
    Sleep(600)

    def lambda_37F5():
        OP_8F(0xFE, 0xFFFD7B50, 0x1770, 0xE88, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_37F5)
    WaitChrThread(0x14E, 0x1)
    OP_44(0x14E, 0x2)
    Sleep(300)
    Return()

    # Function_22_37B9 end

    def Function_23_3819(): pass

    label("Function_23_3819")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-155620, 6060, 2700, 0)
    OP_67(0, 8540, -10000, 0)
    OP_6B(3680, 0)
    OP_6C(286000, 0)
    OP_6E(424, 0)
    SetChrFlags(0x14E, 0x4)
    SetChrPos(0x14E, -164800, 5820, 5800, 150)
    SetChrFlags(0x14E, 0x2)
    SetChrChipByIndex(0x14E, 5)
    SetChrSubChip(0x14E, 0)

    def lambda_388D():

        label("loc_388D")

        OP_99(0xFE, 0x0, 0x7, 0x1F4)
        OP_48()
        Jump("loc_388D")

    QueueWorkItem2(0x14E, 2, lambda_388D)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x800)
    SetChrPos(0x11, -165320, 6020, 5520, 150)
    OP_4A(0x11, 255)
    SetChrFlags(0x11, 0x2)
    SetChrChipByIndex(0x11, 2)
    SetChrSubChip(0x11, 0)

    def lambda_38D3():

        label("loc_38D3")

        OP_99(0xFE, 0x0, 0x7, 0x1F4)
        OP_48()
        Jump("loc_38D3")

    QueueWorkItem2(0x11, 2, lambda_38D3)
    OP_72(0x5, 0x0)
    ExitThread()
    OP_72(0x405, 0x0)
    ExitThread()

    def lambda_38F2():
        OP_6D(-165320, 6020, 5520, 9000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_38F2)

    def lambda_390A():
        OP_6B(3180, 9000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_390A)
    FadeToBright(4000, 0)
    WaitChrThread(0x15, 0x0)
    Sleep(500)
    Fade(1000)
    OP_6D(-165320, 6420, 5520, 0)
    OP_67(0, 4600, -10000, 0)
    OP_6B(2860, 0)
    OP_6C(286000, 0)
    OP_6E(250, 0)
    Sleep(2000)

    def lambda_3974():
        OP_6B(2660, 15000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_3974)

    ChrTalk(    #85
        0x14E,
        "#1719F#60WMmm...\x02",
    )

    CloseMessageWindow()
    Sleep(800)

    ChrTalk(    #86
        0x14E,
        "#1719F#60WYou're so soft...\x02",
    )

    CloseMessageWindow()
    Sleep(800)

    ChrTalk(    #87
        0x14E,
        "#1719F#60WAnd I'm sure I know this scent from somewhere...\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_44(0x14E, 0x2)
    Fade(500)
    SetChrChipByIndex(0x14E, 11)
    SetChrSubChip(0x14E, 0)
    OP_0D()
    OP_99(0x14E, 0x0, 0x3, 0x3E8)
    Sleep(300)

    ChrTalk(    #88
        0x14E,
        "#1719F#60WBut where...?\x02",
    )

    CloseMessageWindow()
    FadeToDark(4000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #89
        "\x07\x00\x18This is so warm...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_20(0xBB8)
    OP_21()
    OP_A2(0x2506)
    NewScene("ED6_DT21/C1500   ._SN", 100, 0, 1)
    IdleLoop()
    Return()

    # Function_23_3819 end

    def Function_24_3A9C(): pass

    label("Function_24_3A9C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-165320, 6420, 5520, 0)
    OP_67(0, 4600, -10000, 0)
    OP_6B(2760, 0)
    OP_6C(286000, 0)
    OP_6E(250, 0)
    StopSound(0x64, 0xEA60, 0x0)
    SetChrFlags(0x14E, 0x4)
    SetChrPos(0x14E, -164800, 5820, 5800, 150)
    SetChrFlags(0x14E, 0x2)
    SetChrChipByIndex(0x14E, 5)
    SetChrSubChip(0x14E, 0)

    def lambda_3B1D():

        label("loc_3B1D")

        OP_99(0xFE, 0x0, 0x7, 0x1F4)
        OP_48()
        Jump("loc_3B1D")

    QueueWorkItem2(0x14E, 2, lambda_3B1D)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    SetChrFlags(0x11, 0x1)
    OP_72(0x7, 0x0)
    ExitThread()
    OP_72(0x407, 0x0)
    ExitThread()
    LoadEffect(0x2, "map\\mp087_00.eff")
    FadeToBright(2000, 0)
    OP_0D()
    OP_9E(0x14E, 0xA, 0x0, 0x12C, 0xBB8)
    OP_44(0x14E, 0x2)
    Sleep(300)

    ChrTalk(    #90
        0x14E,
        "#1716F#12PAchoo!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_59()
    OP_44(0x14E, 0x2)
    Fade(1000)
    SetChrChipByIndex(0x14E, 6)
    SetChrSubChip(0x14E, 0)
    OP_0D()

    ChrTalk(    #91
        0x14E,
        "#1713F#12PMm... Mmm...?\x02",
    )

    CloseMessageWindow()

    def lambda_3BDD():
        OP_99(0xFE, 0x0, 0x4, 0x320)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_3BDD)
    WaitChrThread(0x14E, 0x2)

    def lambda_3BF2():
        OP_99(0xFE, 0x4, 0x3, 0x320)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_3BF2)
    WaitChrThread(0x14E, 0x2)

    def lambda_3C07():
        OP_99(0xFE, 0x3, 0x4, 0x320)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_3C07)
    WaitChrThread(0x14E, 0x2)

    def lambda_3C1C():
        OP_99(0xFE, 0x4, 0x2, 0x320)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_3C1C)
    WaitChrThread(0x14E, 0x2)
    Sleep(200)
    Fade(500)
    SetChrSubChip(0x14E, 5)
    OP_0D()

    ChrTalk(    #92
        0x14E,
        "#1714F#12P...!\x02",
    )

    CloseMessageWindow()

    def lambda_3C55():
        OP_67(0, 5260, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_3C55)

    def lambda_3C6D():
        OP_6B(2860, 4000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3C6D)

    def lambda_3C7D():
        OP_6E(316, 4000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_3C7D)
    Sleep(500)
    SetChrSubChip(0x14E, 7)
    Sleep(1000)
    SetChrSubChip(0x14E, 5)
    Sleep(150)
    SetChrSubChip(0x14E, 6)
    Sleep(1350)
    OP_22(0x8F, 0x0, 0x64)
    Fade(300)
    SetChrChipByIndex(0x14E, 65535)
    SetChrSubChip(0x14E, 0)
    ClearChrFlags(0x14E, 0x4)
    ClearChrFlags(0x14E, 0x2)
    SetChrPos(0x14E, -164800, 6020, 5800, 150)
    Sleep(500)
    OP_62(0x14E, 0x0, 1600, 0x18, 0x1B, 0xC8, 0x2)
    Sleep(2000)
    OP_63(0x14E)
    WaitChrThread(0x15, 0x0)

    def lambda_3D03():
        OP_6D(-164300, 5990, 6610, 4000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_3D03)
    OP_8C(0x14E, 65, 400)

    def lambda_3D22():
        OP_8E(0xFE, 0xFFFD84EC, 0x175C, 0x1824, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_3D22)
    WaitChrThread(0x14E, 0x1)
    Sleep(500)
    OP_8C(0x14E, 320, 400)
    Sleep(1000)
    OP_8C(0x14E, 150, 400)
    Sleep(1000)

    def lambda_3D5F():
        OP_6D(-161920, 6020, 3830, 4000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_3D5F)

    def lambda_3D77():
        OP_8E(0xFE, 0xFFFD8BB8, 0x1784, 0xDD4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_3D77)
    WaitChrThread(0x14E, 0x1)
    Sleep(500)
    OP_8C(0x14E, 220, 400)
    Sleep(1000)
    OP_8C(0x14E, 65, 400)
    Sleep(1000)

    ChrTalk(    #93
        0x14E,
        "#1714F#5PHe's gone...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x14E, 285, 400)
    Sleep(1000)

    ChrTalk(    #94
        0x14E,
        (
            "#1713F#5P...\x02\x03",

            "#1713FI guess that's it...\x02",
        )
    )

    CloseMessageWindow()
    StopSound(0x64, 0x1ADB0, 0xFA0)
    Sleep(1000)
    OP_22(0x1C2, 0x0, 0x64)
    Sleep(4000)
    OP_8C(0x14E, 45, 400)
    Sleep(1000)

    ChrTalk(    #95
        0x14E,
        "#1713F#5P...I guess I'll go home.\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_3E5D():
        OP_8E(0xFE, 0xFFFDA71A, 0x1784, 0x218E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_3E5D)
    Sleep(500)
    FadeToDark(2000, 0, -1)
    OP_24(0x1C2, 0x5A)
    Sleep(200)
    OP_24(0x1C2, 0x50)
    Sleep(200)
    OP_24(0x1C2, 0x46)
    Sleep(200)
    OP_24(0x1C2, 0x3C)
    Sleep(200)
    OP_24(0x1C2, 0x32)
    Sleep(200)
    OP_24(0x1C2, 0x28)
    Sleep(200)
    OP_24(0x1C2, 0x1E)
    Sleep(200)
    OP_24(0x1C2, 0x14)
    OP_0D()
    OP_23(0x1C2)
    OP_44(0x14E, 0x1)
    Sleep(1500)
    OP_1D(0x7D)
    ClearMapFlags(0x10)
    OP_6D(-135320, 2410, 61200, 0)
    OP_67(0, 6590, -10000, 0)
    OP_6B(2770, 0)
    OP_6C(191000, 0)
    OP_6E(311, 0)

    def lambda_3F1B():
        OP_6D(-141720, 2410, 61000, 10000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_3F1B)
    SetChrPos(0x14E, -136060, 1970, 57120, 0)

    def lambda_3F44():
        OP_8E(0xFE, 0xFFFDD064, 0x794, 0x111D4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_3F44)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x15, 0x0)
    OP_6D(-146820, 4000, 90050, 0)
    OP_67(0, 7770, -10000, 0)
    OP_6B(2980, 0)
    OP_6C(261000, 0)
    OP_6E(305, 0)

    def lambda_3FBA():
        OP_6D(-143670, 4000, 94700, 10000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_3FBA)
    OP_44(0x14E, 0x1)
    SetChrPos(0x14E, -141620, 4019, 89840, 330)

    def lambda_3FE7():
        OP_8E(0xFE, 0xFFFDC7A4, 0xF96, 0x16698, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_3FE7)
    FadeToBright(2000, 0)
    WaitChrThread(0x14E, 0x1)

    def lambda_4010():
        OP_8E(0xFE, 0xFFFDCC04, 0x10A4, 0x17444, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_4010)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x15, 0x0)
    PlayEffect(0x2, 0xFF, 0xFF, -146100, -5000, 68530, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, -133390, -5000, 66740, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, -143890, -5000, 73350, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, -138880, -5000, 73210, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, -137110, -5000, 70530, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, -134110, -5000, 68170, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, -133040, -5000, 66590, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, -133050, -5000, 70070, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, -139440, -5000, 76200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, -136720, -5000, 75940, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_44(0x14E, 0x1)
    Sleep(1500)
    StopSound(0x64, 0x186A0, 0x0)
    OP_6D(-140240, 2480, 64239, 0)
    OP_67(0, 5060, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(294000, 0)
    OP_6E(330, 0)
    SetChrPos(0x14E, -140100, 2000, 64180, 5)

    def lambda_42B5():
        OP_6D(-144130, 2650, 72560, 6500)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_42B5)

    def lambda_42CD():
        OP_6B(2460, 6500)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_42CD)

    def lambda_42DD():
        OP_6E(316, 6500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_42DD)

    def lambda_42ED():
        OP_67(0, 4019, -10000, 6500)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_42ED)

    def lambda_4305():
        OP_6C(298000, 6500)
        ExitThread()

    QueueWorkItem(0x14E, 3, lambda_4305)

    def lambda_4315():
        OP_8E(0xFE, 0xFFFDD49C, 0x82A, 0x10F18, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_4315)
    FadeToBright(2000, 0)
    OP_0D()
    OP_43(0x14E, 0x3, 0x0, 0x1E)
    WaitChrThread(0x15, 0x0)
    WaitChrThread(0x14E, 0x1)
    Sleep(500)

    ChrTalk(    #96
        0x14E,
        "#1713F...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_4364():
        OP_6D(-145110, 2720, 74470, 8000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_4364)
    SetChrFlags(0x14E, 0x4)

    def lambda_4381():
        OP_8E(0xFE, 0xFFFDD2B2, 0x82A, 0x118A0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_4381)
    WaitChrThread(0x14E, 0x1)

    def lambda_43A1():
        OP_9E(0xFE, 0x14, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_43A1)
    Sleep(500)

    def lambda_43C0():
        OP_8E(0xFE, 0xFFFDD15E, 0x91A, 0x11D14, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_43C0)
    WaitChrThread(0x14E, 0x1)

    def lambda_43E0():
        OP_9E(0xFE, 0x14, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_43E0)
    Sleep(500)

    def lambda_43FF():
        OP_8E(0xFE, 0xFFFDD104, 0xAD2, 0x120DE, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_43FF)
    WaitChrThread(0x14E, 0x1)

    def lambda_441F():
        OP_9E(0xFE, 0x14, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_441F)
    Sleep(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_44(0x14E, 0x1)
    SetChrFlags(0x14E, 0x20)
    OP_22(0x58, 0x0, 0x64)
    Sleep(200)

    def lambda_445F():
        OP_6D(-143820, 2650, 74500, 300)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_445F)

    def lambda_4477():
        OP_67(0, 3430, -10000, 300)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_4477)

    def lambda_448F():
        OP_D0(1000, 300)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_448F)

    def lambda_449F():

        label("loc_449F")

        OP_9E(0xFE, 0x32, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_449F")

    QueueWorkItem2(0x14E, 3, lambda_449F)

    def lambda_44BC():
        OP_8F(0xFE, 0xFFFDD366, 0xAD2, 0x1216A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_44BC)
    OP_20(0x0)

    def lambda_44DC():
        OP_7C(0x64, 0x64, 0xBB8, 0x12C)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_44DC)

    ChrTalk(    #97 op#A
        0x14E,
        "#6P#3S#5A...Oh!#2S\x02",
    )

    OP_22(0x14D, 0x0, 0x46)
    OP_22(0x16D, 0x0, 0x64)
    Sleep(800)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_451F():
        OP_6D(-143820, 1500, 74500, 1000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_451F)

    def lambda_4537():
        OP_D0(5000, 1000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_4537)
    Fade(250)
    SetChrPos(0x14E, -143100, 2670, 73950, 354)
    ClearChrFlags(0x14E, 0x100)
    SetChrFlags(0x14E, 0x800)
    ClearChrFlags(0x14E, 0x1)
    OP_D1(334, 35000, 300000, 0, 0)
    SetChrFlags(0x14E, 0x4)
    SetChrFlags(0x14E, 0x20)

    def lambda_4589():
        OP_96(0x14E, 0xFFFDD938, 0xFFFFF254, 0x12264, 0x12C, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_4589)

    def lambda_45A7():
        OP_D1(254, 35000, 300000, -45000, 1000)
        ExitThread()

    QueueWorkItem(0x14E, 3, lambda_45A7)

    def lambda_45C1():
        OP_8C(0x14E, 270, 200)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_45C1)
    OP_22(0xBD, 0x0, 0x64)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(2000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    LoadEffect(0x3, "map\\mp253_01.eff")
    LoadEffect(0x4, "map\\mp253_04.eff")
    SoundLoad(128)
    SoundLoad(612)
    SoundLoad(215)
    OP_44(0x14E, 0xFF)
    SetChrFlags(0x14E, 0x100)
    ClearChrFlags(0x14E, 0x800)
    SetChrFlags(0x14E, 0x20)
    SetChrFlags(0x14E, 0x1000)
    SetChrPos(0x14E, -87660, 5200, -1140, 90)
    SetChrFlags(0x14E, 0x2)
    SetChrChipByIndex(0x14E, 7)
    SetChrSubChip(0x14E, 0)

    def lambda_465A():

        label("loc_465A")

        OP_99(0xFE, 0x0, 0x3, 0xBB8)
        OP_48()
        Jump("loc_465A")

    QueueWorkItem2(0x14E, 2, lambda_465A)
    OP_72(0x8, 0x0)
    ExitThread()
    OP_72(0x408, 0x0)
    ExitThread()
    OP_6D(-87660, -800, -1140, 0)
    OP_67(0, 3860, -10000, 0)
    OP_6B(750, 0)
    OP_6C(270000, 0)
    OP_6E(946, 0)
    OP_D0(0, 0)
    OP_22(0x85, 0x1, 0x3C)

    def lambda_46C4():

        label("loc_46C4")

        OP_7C(0x32, 0x32, 0xBB8, 0x64)
        OP_48()
        Jump("loc_46C4")

    QueueWorkItem2(0x10, 3, lambda_46C4)
    OP_43(0x14E, 0x0, 0x0, 0x1C)
    StopSound(0x64, 0xAAB4, 0x1)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1500)
    WaitChrThread(0x14E, 0x0)
    WaitChrThread(0x15, 0x0)
    Sleep(2000)

    def lambda_4711():
        OP_6B(650, 16000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_4711)
    OP_C4(0x0, 0x800)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #98
        "\x07\x0C\x18#60W#3SMatron...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #99
        "\x07\x0C\x18#60W#3SI'm sorry...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_77(0xB4, 0xB4, 0xB4, 0x0, 0x3E8)
    Sleep(1000)
    SetChrPos(0x11, -87120, 2500, 1760, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x11, 0x1)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x11, 0x20)
    ClearChrFlags(0x11, 0x8)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4A(0x11, 255)
    SetChrChipByIndex(0x11, 9)
    SetChrSubChip(0x11, 0)

    def lambda_47E8():

        label("loc_47E8")

        OP_99(0x11, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_47E8")

    QueueWorkItem2(0x10, 2, lambda_47E8)
    OP_43(0x11, 0x3, 0x0, 0x1F)
    OP_22(0x146, 0x1, 0x3C)
    PlayEffect(0x3, 0x0, 0x11, 0, 0, 0, 0, 2800, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_22(0x80, 0x0, 0x64)
    OP_97(0x11, 0xFFFEA994, 0xFFFFFB8C, 0x57E40, 0xDAC, 0x1)
    OP_97(0x11, 0xFFFEA994, 0xFFFFFB8C, 0x2BF20, 0xDAC, 0x1)
    WaitChrThread(0x11, 0x3)
    OP_8C(0x11, 45, 400)
    Sleep(500)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
    OP_22(0x264, 0x0, 0x64)
    OP_22(0xD7, 0x0, 0x64)
    OP_23(0x146)
    Fade(500)
    PlayEffect(0x4, 0x1, 0x11, 0, 0, 0, -500, 5000, 0, 1100, 1100, 1100, 0xFF, 0, 0, 0, 0)
    OP_51(0x11, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8C(0x11, 45, 0)
    SetChrChipByIndex(0x11, 9)
    SetChrSubChip(0x11, 0)

    def lambda_48E9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_48E9)
    OP_43(0x11, 0x0, 0x0, 0x1D)

    def lambda_4902():

        label("loc_4902")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_4902")

    QueueWorkItem2(0x11, 2, lambda_4902)
    OP_82(0x0, 0x2)
    Sleep(1000)
    OP_82(0x1, 0x2)
    Sleep(2000)

    def lambda_4925():

        label("loc_4925")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_4925")

    QueueWorkItem2(0x11, 2, lambda_4925)

    def lambda_4938():
        OP_8F(0xFE, 0xFFFEA9F8, 0xFFFFF448, 0xFFFFF614, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4938)
    WaitChrThread(0x11, 0x1)

    def lambda_4958():
        OP_8F(0xFE, 0xFFFEBDE4, 0x76C, 0x19B4, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4958)
    Sleep(200)
    OP_22(0x8F, 0x0, 0x64)
    SetChrFlags(0x14E, 0x8)

    def lambda_4982():
        OP_8F(0xFE, 0xFFFEBDE4, 0x9C4, 0x19B4, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4982)
    WaitChrThread(0x11, 0x1)
    OP_43(0x14E, 0x0, 0x0, 0x19)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x11, 0x1)
    SetMapFlags(0x100000)
    ClearChrFlags(0x14E, 0x8)
    OP_A2(0x2506)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_24_3A9C end

    def Function_25_49CA(): pass

    label("Function_25_49CA")

    OP_24(0x85, 0x32)
    Sleep(300)
    OP_24(0x85, 0x28)
    Sleep(300)
    OP_24(0x85, 0x1E)
    Sleep(300)
    OP_24(0x85, 0x14)
    Sleep(300)
    OP_24(0x85, 0xA)
    Sleep(300)
    OP_24(0x85, 0x0)
    OP_23(0x85)
    Return()

    # Function_25_49CA end

    def Function_26_49FF(): pass

    label("Function_26_49FF")

    OP_24(0x120, 0x3C)
    Sleep(150)
    OP_24(0x120, 0x32)
    Sleep(150)
    OP_24(0x120, 0x28)
    Sleep(150)
    OP_24(0x120, 0x1E)
    Sleep(150)
    OP_24(0x120, 0x14)
    Sleep(150)
    OP_24(0x120, 0xA)
    Sleep(150)
    OP_24(0x120, 0x0)
    OP_23(0x120)
    Return()

    # Function_26_49FF end

    def Function_27_4A3D(): pass

    label("Function_27_4A3D")


    def lambda_4A43():
        OP_8F(0xFE, 0xFFFEA610, 0xFFFFEA84, 0xFFFFF9FC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4A43)
    Sleep(700)

    def lambda_4A63():
        OP_8C(0xFE, 135, 100)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4A63)

    def lambda_4A71():
        OP_8F(0xFE, 0xFFFEA610, 0xFFFFEA84, 0xFFFFF9FC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4A71)
    Sleep(600)

    def lambda_4A91():
        OP_8C(0xFE, 90, 100)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4A91)

    def lambda_4A9F():
        OP_8F(0xFE, 0xFFFEA610, 0xFFFFEA84, 0xFFFFF9FC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4A9F)
    Sleep(500)

    def lambda_4ABF():
        OP_8F(0xFE, 0xFFFEA610, 0xFFFFEA84, 0xFFFFF9FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4ABF)
    WaitChrThread(0xFE, 0x1)

    def lambda_4ADF():
        OP_8C(0xFE, 45, 100)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4ADF)

    def lambda_4AED():
        OP_8F(0xFE, 0xFFFEA9F8, 0xFFFFF31C, 0xFFFFF420, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4AED)
    Sleep(200)

    def lambda_4B0D():
        OP_8F(0xFE, 0xFFFEA9F8, 0xFFFFF31C, 0xFFFFF420, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4B0D)
    Sleep(300)

    def lambda_4B2D():
        OP_8F(0xFE, 0xFFFEA9F8, 0xFFFFF31C, 0xFFFFF420, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4B2D)
    Sleep(300)

    def lambda_4B4D():
        OP_8F(0xFE, 0xFFFEA9F8, 0xFFFFF31C, 0xFFFFF420, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4B4D)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_27_4A3D end

    def Function_28_4B68(): pass

    label("Function_28_4B68")


    def lambda_4B6E():
        OP_8F(0xFE, 0xFFFEA994, 0xFFFFF830, 0xFFFFFB8C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_4B6E)
    Sleep(500)

    def lambda_4B8E():
        OP_8F(0xFE, 0xFFFEA994, 0xFFFFF830, 0xFFFFFB8C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_4B8E)
    Sleep(500)

    def lambda_4BAE():
        OP_8F(0xFE, 0xFFFEA994, 0xFFFFF830, 0xFFFFFB8C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_4BAE)
    Sleep(400)

    def lambda_4BCE():
        OP_8F(0xFE, 0xFFFEA994, 0xFFFFF830, 0xFFFFFB8C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_4BCE)
    Sleep(400)

    def lambda_4BEE():
        OP_8F(0xFE, 0xFFFEA994, 0xFFFFF830, 0xFFFFFB8C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_4BEE)
    WaitChrThread(0x14E, 0x1)
    Return()

    # Function_28_4B68 end

    def Function_29_4C09(): pass

    label("Function_29_4C09")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4C1F")
    OP_22(0x120, 0x0, 0x46)
    Sleep(1400)
    Jump("Function_29_4C09")

    label("loc_4C1F")

    Return()

    # Function_29_4C09 end

    def Function_30_4C20(): pass

    label("Function_30_4C20")

    OP_22(0x1C3, 0x1, 0x14)
    Sleep(500)
    OP_24(0x1C3, 0x28)
    Sleep(500)
    OP_24(0x1C3, 0x3C)
    Sleep(500)
    OP_24(0x1C3, 0x50)
    Sleep(500)
    OP_24(0x1C3, 0x64)
    Return()

    # Function_30_4C20 end

    def Function_31_4C4A(): pass

    label("Function_31_4C4A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4C84")
    OP_51(0x11, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x2), scpexpr(EXPR_PUSH_LONG, 0x898), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4C7C")
    OP_51(0x11, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x898), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4C84")

    label("loc_4C7C")

    Sleep(10)
    Jump("Function_31_4C4A")

    label("loc_4C84")

    Return()

    # Function_31_4C4A end

    def Function_32_4C85(): pass

    label("Function_32_4C85")


    ChrTalk(    #100
        0x14E,
        "#1711FYay! Found some!\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #101
        "\x07\x05Mary picked up some firewood.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2F1B)
    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D49")

    ChrTalk(    #102
        0x14E,
        "#1710FI think this should be enough.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 21)

    label("loc_4D49")

    TalkEnd(0xFF)
    Return()

    # Function_32_4C85 end

    def Function_33_4D4D(): pass

    label("Function_33_4D4D")

    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #103
        "\x07\x05Mary picked up some firewood.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #104
        0x14E,
        "#1718FHere's some!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F1C)
    OP_64(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E0D")

    ChrTalk(    #105
        0x14E,
        "#1710FI think this should be enough.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 21)

    label("loc_4E0D")

    TalkEnd(0xFF)
    Return()

    # Function_33_4D4D end

    def Function_34_4E11(): pass

    label("Function_34_4E11")


    ChrTalk(    #106
        0x14E,
        "#1718FHere's some!\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #107
        "\x07\x05Mary picked up some firewood.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2F1D)
    OP_64(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4ED1")

    ChrTalk(    #108
        0x14E,
        "#1710FI think this should be enough.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 21)

    label("loc_4ED1")

    TalkEnd(0xFF)
    Return()

    # Function_34_4E11 end

    def Function_35_4ED5(): pass

    label("Function_35_4ED5")


    ChrTalk(    #109
        0x14E,
        "#1714FOooh... I didn't think I'd find any here.\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #110
        "\x07\x05Mary picked up some firewood.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2F1E)
    OP_64(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4FB2")

    ChrTalk(    #111
        0x14E,
        "#1710FI think this should be enough.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 21)

    label("loc_4FB2")

    TalkEnd(0xFF)
    Return()

    # Function_35_4ED5 end

    def Function_36_4FB6(): pass

    label("Function_36_4FB6")


    ChrTalk(    #112
        0x14E,
        "#1711FGot some!\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #113
        "\x07\x05Mary picked up some firewood.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2F1F)
    OP_64(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5073")

    ChrTalk(    #114
        0x14E,
        "#1710FI think this should be enough.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 21)

    label("loc_5073")

    TalkEnd(0xFF)
    Return()

    # Function_36_4FB6 end

    SaveToFile()

Try(main)
