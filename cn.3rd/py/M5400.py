from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M5400   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5400.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60234",
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
        '基尔巴特',                             # 9
        '基尔巴特',                             # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT27/CH03750 ._CH',             # 00
        'ED6_DT26/CH20501 ._CH',             # 01
        'ED6_DT29/CH15020 ._CH',             # 02
        'ED6_DT29/CH15021 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT27/CH03750P._CP',             # 00
        'ED6_DT26/CH20501P._CP',             # 01
        'ED6_DT29/CH15020P._CP',             # 02
        'ED6_DT29/CH15021P._CP',             # 03
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 4050,
        Z                   = 0,
        Y                   = -1110,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x299,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -88010,
        Z                   = 0,
        Y                   = -1210,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x299,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -42980,
        Y                   = -1000,
        Z                   = 75190,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 20,
    )

    DeclEvent(
        X                   = -36920,
        Y                   = -1000,
        Z                   = -67150,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 21,
    )

    DeclEvent(
        X                   = 70070,
        Y                   = -1000,
        Z                   = -234030,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 22,
    )

    DeclEvent(
        X                   = -91280,
        Y                   = -1000,
        Z                   = -292000,
        Range               = -85000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0xFFFB7FA8,
        Unknown_18          = 0x0,
        Unknown_1C          = 10,
    )

    DeclEvent(
        X                   = 60940,
        Y                   = 50,
        Z                   = -184220,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 23,
    )


    DeclActor(
        TriggerX            = 67810,
        TriggerZ            = 0,
        TriggerY            = -229130,
        TriggerRange        = 1000,
        ActorX              = 67810,
        ActorZ              = 2000,
        ActorY              = -229130,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -87000,
        TriggerZ            = 0,
        TriggerY            = -342900,
        TriggerRange        = 1000,
        ActorX              = -87000,
        ActorZ              = 1000,
        ActorY              = -343080,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 61080,
        TriggerZ            = 0,
        TriggerY            = -184550,
        TriggerRange        = 1000,
        ActorX              = 61080,
        ActorZ              = 1000,
        ActorY              = -184550,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -37430,
        TriggerZ            = 0,
        TriggerY            = 73910,
        TriggerRange        = 1000,
        ActorX              = -37430,
        ActorZ              = 1000,
        ActorY              = 73910,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -38100,
        TriggerZ            = 0,
        TriggerY            = -71790,
        TriggerRange        = 1000,
        ActorX              = -38100,
        ActorZ              = 1000,
        ActorY              = -71790,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -83920,
        TriggerZ            = 0,
        TriggerY            = -346980,
        TriggerRange        = 1000,
        ActorX              = -83920,
        ActorZ              = 1000,
        ActorY              = -346980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -127350,
        TriggerZ            = 0,
        TriggerY            = -58920,
        TriggerRange        = 1000,
        ActorX              = -126610,
        ActorZ              = 0,
        ActorY              = -58850,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -131900,
        TriggerZ            = 0,
        TriggerY            = 10590,
        TriggerRange        = 1000,
        ActorX              = -131900,
        ActorZ              = 0,
        ActorY              = 11210,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 61000,
        TriggerZ            = 0,
        TriggerY            = -27060,
        TriggerRange        = 1000,
        ActorX              = 61000,
        ActorZ              = 1000,
        ActorY              = -27060,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 52900,
        TriggerZ            = 0,
        TriggerY            = -53160,
        TriggerRange        = 1000,
        ActorX              = 52880,
        ActorZ              = 1000,
        ActorY              = -52540,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -79360,
        TriggerZ            = 0,
        TriggerY            = -318070,
        TriggerRange        = 1000,
        ActorX              = -78700,
        ActorZ              = 0,
        ActorY              = -318100,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -79400,
        TriggerZ            = 0,
        TriggerY            = -298090,
        TriggerRange        = 1000,
        ActorX              = -78740,
        ActorZ              = 0,
        ActorY              = -298130,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_392",          # 00, 0
        "Function_1_3FA",          # 01, 1
        "Function_2_582",          # 02, 2
        "Function_3_6FF",          # 03, 3
        "Function_4_772",          # 04, 4
        "Function_5_898",          # 05, 5
        "Function_6_9EF",          # 06, 6
        "Function_7_B46",          # 07, 7
        "Function_8_BE6",          # 08, 8
        "Function_9_C86",          # 09, 9
        "Function_10_DAC",         # 0A, 10
        "Function_11_2EDE",        # 0B, 11
        "Function_12_2F1B",        # 0C, 12
        "Function_13_36AB",        # 0D, 13
        "Function_14_44DA",        # 0E, 14
        "Function_15_4525",        # 0F, 15
        "Function_16_4826",        # 10, 16
        "Function_17_4ADC",        # 11, 17
        "Function_18_4B02",        # 12, 18
        "Function_19_4B28",        # 13, 19
        "Function_20_4B4E",        # 14, 20
        "Function_21_4B67",        # 15, 21
        "Function_22_4B80",        # 16, 22
        "Function_23_4B9E",        # 17, 23
        "Function_24_4BA4",        # 18, 24
    )


    def Function_0_392(): pass

    label("Function_0_392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 5)), scpexpr(EXPR_END)), "loc_39C")
    Jump("loc_3F9")

    label("loc_39C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 4)), scpexpr(EXPR_END)), "loc_3CB")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x10, 0x1)
    SetChrPos(0x10, -84150, 0, -290050, 270)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    Jump("loc_3F9")

    label("loc_3CB")

    OP_44(0x10, 0xFF)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -78800, 300, -290790, 0)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)
    ClearChrFlags(0x10, 0x1)
    SetChrFlags(0x10, 0x4)

    label("loc_3F9")

    Return()

    # Function_0_392 end

    def Function_1_3FA(): pass

    label("Function_1_3FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40B")
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x83, 0x0)

    label("loc_40B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56E, 2)), scpexpr(EXPR_END)), "loc_41F")
    OP_6F(0x3, 50)
    OP_71(0x403, 0x0)
    ExitThread()

    label("loc_41F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56E, 3)), scpexpr(EXPR_END)), "loc_433")
    OP_6F(0x4, 50)
    OP_71(0x404, 0x0)
    ExitThread()

    label("loc_433")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56E, 4)), scpexpr(EXPR_END)), "loc_447")
    OP_6F(0x5, 50)
    OP_71(0x405, 0x0)
    ExitThread()

    label("loc_447")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56E, 5)), scpexpr(EXPR_END)), "loc_45B")
    OP_6F(0x6, 50)
    OP_71(0x406, 0x0)
    ExitThread()

    label("loc_45B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56E, 6)), scpexpr(EXPR_END)), "loc_46F")
    OP_6F(0x7, 50)
    OP_71(0x407, 0x0)
    ExitThread()

    label("loc_46F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47B")
    OP_64(0x1, 0x1)

    label("loc_47B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48C")
    OP_72(0x1002, 0x0)
    ExitThread()
    Jump("loc_49D")

    label("loc_48C")

    OP_72(0x1002, 0x0)
    ExitThread()
    OP_6F(0x2, 270)
    OP_64(0x2, 0x1)

    label("loc_49D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 1)), scpexpr(EXPR_END)), "loc_4A7")
    Jump("loc_4D5")

    label("loc_4A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 0)), scpexpr(EXPR_END)), "loc_4D5")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7D), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x81), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4D5")
    Call(0, 24)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)

    label("loc_4D5")

    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x579, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FD")
    OP_6F(0x25, 0)
    Jump("loc_504")

    label("loc_4FD")

    OP_6F(0x25, 60)

    label("loc_504")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x579, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_516")
    OP_6F(0x26, 0)
    Jump("loc_51D")

    label("loc_516")

    OP_6F(0x26, 60)

    label("loc_51D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x579, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52F")
    OP_6F(0x2B, 0)
    Jump("loc_536")

    label("loc_52F")

    OP_6F(0x2B, 60)

    label("loc_536")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x579, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_548")
    OP_6F(0x2C, 0)
    Jump("loc_54F")

    label("loc_548")

    OP_6F(0x2C, 60)

    label("loc_54F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x579, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_561")
    OP_6F(0x2D, 0)
    Jump("loc_568")

    label("loc_561")

    OP_6F(0x2D, 60)

    label("loc_568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x579, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57A")
    OP_6F(0x2E, 0)
    Jump("loc_581")

    label("loc_57A")

    OP_6F(0x2E, 60)

    label("loc_581")

    Return()

    # Function_1_3FA end

    def Function_2_582(): pass

    label("Function_2_582")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A7")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_6E9")

    label("loc_5A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C0")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_6E9")

    label("loc_5C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D9")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_6E9")

    label("loc_5D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F2")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_6E9")

    label("loc_5F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60B")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_6E9")

    label("loc_60B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_624")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_6E9")

    label("loc_624")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_63D")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_6E9")

    label("loc_63D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_656")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_6E9")

    label("loc_656")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66F")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_6E9")

    label("loc_66F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_688")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_6E9")

    label("loc_688")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A1")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_6E9")

    label("loc_6A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6BA")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_6E9")

    label("loc_6BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D3")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_6E9")

    label("loc_6D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E9")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_6E9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6FE")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_6E9")

    label("loc_6FE")

    Return()

    # Function_2_582 end

    def Function_3_6FF(): pass

    label("Function_3_6FF")

    TalkBegin(0x10)

    ChrTalk(    #0
        0x10,
        (
            "#1224F你、你们该不会说\x01",
            "改变主意什么的吧……！？\x02\x03",

            "#1227F拜托了！\x01",
            "请把这该死的障壁消除吧！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x10)
    Return()

    # Function_3_6FF end

    def Function_4_772(): pass

    label("Function_4_772")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x579, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_857")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x25, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2DC, 1)"), scpexpr(EXPR_END)), "loc_7E6")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #1
        "\x07\x00得到了\x1F\xDC\x02\x07\x00。\x02",
    )

    Jump("loc_7CB")

    label("loc_7CB")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BC8)
    Jump("loc_854")

    label("loc_7E6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "宝箱里装有\x1F\xDC\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xDC\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_835")

    label("loc_835")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x25, 60)
    OP_70(0x25, 0x0)

    label("loc_854")

    Jump("loc_88A")

    label("loc_857")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_88A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_772 end

    def Function_5_898(): pass

    label("Function_5_898")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x579, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C1")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x26, 0x1E)
    OP_73(0x26)
    OP_6F(0x26, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 0xC8)
    AddSepith(0x1, 0xC8)
    AddSepith(0x2, 0xC8)
    AddSepith(0x3, 0xC8)
    AddSepith(0x4, 0xC8)
    AddSepith(0x5, 0xC8)
    AddSepith(0x6, 0xC8)

    AnonymousTalk(    #4
        (
            "\x07\x00得到了：\x01",
            "\x07\x02#56I地之耀晶片×２００\x01",
            "\x07\x02#57I水之耀晶片×２００\x01",
            "\x07\x02#58I火之耀晶片×２００\x01",
            "\x07\x02#59I风之耀晶片×２００\x01",
            "\x07\x02#62I时之耀晶片×２００\x01",
            "\x07\x02#60I空之耀晶片×２００\x01",
            "\x07\x02#61I幻之耀晶片×２００\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2BC9)
    Jump("loc_9DD")

    label("loc_9C1")


    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_9DD")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_898 end

    def Function_6_9EF(): pass

    label("Function_6_9EF")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x579, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B18")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2B, 0x1E)
    OP_73(0x2B)
    OP_6F(0x2B, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 0xC8)
    AddSepith(0x1, 0xC8)
    AddSepith(0x2, 0xC8)
    AddSepith(0x3, 0xC8)
    AddSepith(0x4, 0xC8)
    AddSepith(0x5, 0xC8)
    AddSepith(0x6, 0xC8)

    AnonymousTalk(    #6
        (
            "\x07\x00得到了：\x01",
            "\x07\x02#56I地之耀晶片×２００\x01",
            "\x07\x02#57I水之耀晶片×２００\x01",
            "\x07\x02#58I火之耀晶片×２００\x01",
            "\x07\x02#59I风之耀晶片×２００\x01",
            "\x07\x02#62I时之耀晶片×２００\x01",
            "\x07\x02#60I空之耀晶片×２００\x01",
            "\x07\x02#61I幻之耀晶片×２００\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2BCA)
    Jump("loc_B34")

    label("loc_B18")


    AnonymousTalk(    #7
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_B34")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_9EF end

    def Function_7_B46(): pass

    label("Function_7_B46")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x579, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2C, 0x1E)
    OP_73(0x2C)
    OP_6F(0x2C, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddMira(5000)

    AnonymousTalk(    #8
        "\x07\x00得到了\x07\x02５０００米拉\x07\x00。\x02",
    )

    Jump("loc_BA6")

    label("loc_BA6")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2BCB)
    Jump("loc_BD4")

    label("loc_BB8")


    AnonymousTalk(    #9
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_BD4")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_B46 end

    def Function_8_BE6(): pass

    label("Function_8_BE6")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x579, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C58")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2D, 0x1E)
    OP_73(0x2D)
    OP_6F(0x2D, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddMira(5000)

    AnonymousTalk(    #10
        "\x07\x00得到了\x07\x02５０００米拉\x07\x00。\x02",
    )

    Jump("loc_C46")

    label("loc_C46")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2BCC)
    Jump("loc_C74")

    label("loc_C58")


    AnonymousTalk(    #11
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_C74")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_BE6 end

    def Function_9_C86(): pass

    label("Function_9_C86")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x579, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D6B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2E, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2E1, 1)"), scpexpr(EXPR_END)), "loc_CFA")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x00得到了\x1F\xE1\x02\x07\x00。\x02",
    )

    Jump("loc_CDF")

    label("loc_CDF")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BCD)
    Jump("loc_D68")

    label("loc_CFA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "宝箱里装有\x1F\xE1\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xE1\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_D49")

    label("loc_D49")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2E, 60)
    OP_70(0x2E, 0x0)

    label("loc_D68")

    Jump("loc_D9E")

    label("loc_D6B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_D9E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_C86 end

    def Function_10_DAC(): pass

    label("Function_10_DAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 4)), scpexpr(EXPR_END)), "loc_DB4")
    Return()

    label("loc_DB4")

    EventBegin(0x0)
    Fade(500)
    OP_6D(-86410, 0, -294190, 0)
    OP_67(0, 7120, -10000, 0)
    OP_6B(2770, 0)
    OP_6C(45000, 0)
    OP_6E(263, 0)
    SetChrPos(0x109, -88420, 0, -294580, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E4D")
    SetChrPos(0x102, -86850, 0, -294760, 0)
    SetChrPos(0xF0, -88780, 0, -296280, 0)
    SetChrPos(0xF1, -87180, 0, -296440, 0)
    Jump("loc_ED2")

    label("loc_E4D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E91")
    SetChrPos(0x102, -86850, 0, -294760, 0)
    SetChrPos(0xEF, -88780, 0, -296280, 0)
    SetChrPos(0xF1, -87180, 0, -296440, 0)
    Jump("loc_ED2")

    label("loc_E91")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ED2")
    SetChrPos(0x102, -86850, 0, -294760, 0)
    SetChrPos(0xEF, -88780, 0, -296280, 0)
    SetChrPos(0xF0, -87180, 0, -296440, 0)

    label("loc_ED2")

    OP_0D()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x102, 45, 400)

    ChrTalk(    #15
        0x102,
        "#1504F#6P啊……\x02",
    )

    CloseMessageWindow()

    def lambda_F18():
        OP_6D(-78170, 0, -289700, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_F18)

    def lambda_F30():
        OP_67(0, 7450, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_F30)

    def lambda_F48():
        OP_6B(2950, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_F48)

    def lambda_F58():
        OP_6C(57000, 2000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_F58)

    def lambda_F68():
        OP_6E(253, 2000)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_F68)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FB0")

    def lambda_F86():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_F86)
    Sleep(100)

    def lambda_F99():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_F99)
    Sleep(100)
    OP_8C(0xF1, 45, 400)
    Jump("loc_1029")

    label("loc_FB0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FEE")

    def lambda_FC4():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_FC4)
    Sleep(100)

    def lambda_FD7():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_FD7)
    Sleep(100)
    OP_8C(0xF1, 45, 400)
    Jump("loc_1029")

    label("loc_FEE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1029")

    def lambda_1002():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1002)
    Sleep(100)

    def lambda_1015():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1015)
    Sleep(100)
    OP_8C(0xF0, 45, 400)

    label("loc_1029")

    WaitChrThread(0xEE, 0x1)
    Sleep(500)

    ChrTalk(    #16
        0x10,
        (
            "#1223F#5P……呜呜………\x01",
            "为什么会变成这样………\x02\x03",

            "只要解开这个世界的谜团\x01",
            "报告给『结社』，\x01",
            "就一定可以出人头地了……\x02\x03",

            "#1228F所、所有的事情\x01",
            "都是那些家伙的错……\x02\x03",

            "呜呜……\x01",
            "一定是那些家伙不好……\x02",
        )
    )

    Jump("loc_111C")

    label("loc_111C")

    CloseMessageWindow()
    Sleep(150)
    Fade(500)
    OP_6D(-82000, 0, -290900, 0)
    OP_67(0, 5260, -10000, 0)
    OP_6B(3150, 0)
    OP_6C(90000, 0)
    OP_6E(282, 0)
    SetChrPos(0x10, -79200, 300, -290790, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11CA")
    SetChrPos(0x109, -86240, 0, -290380, 90)
    SetChrPos(0x102, -86260, 0, -291640, 90)
    SetChrPos(0xF0, -87770, 0, -289630, 90)
    SetChrPos(0xF1, -87510, 0, -292290, 90)
    Jump("loc_1271")

    label("loc_11CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_121F")
    SetChrPos(0x109, -86240, 0, -290380, 90)
    SetChrPos(0x102, -86260, 0, -291640, 90)
    SetChrPos(0xEF, -87770, 0, -289630, 90)
    SetChrPos(0xF1, -87510, 0, -292290, 90)
    Jump("loc_1271")

    label("loc_121F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1271")
    SetChrPos(0x109, -86240, 0, -290380, 90)
    SetChrPos(0x102, -86260, 0, -291640, 90)
    SetChrPos(0xEF, -87770, 0, -289630, 90)
    SetChrPos(0xF0, -87510, 0, -292290, 90)

    label("loc_1271")

    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -79210, -300, -290270, 0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12BB")
    OP_62(0xEE, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1322")

    label("loc_12BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12E3")
    OP_62(0xEE, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1322")

    label("loc_12E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_130B")
    OP_62(0xEE, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1322")

    label("loc_130B")

    OP_62(0xEE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_1322")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_134A")
    OP_62(0xEF, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_13B1")

    label("loc_134A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1372")
    OP_62(0xEF, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_13B1")

    label("loc_1372")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_139A")
    OP_62(0xEF, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_13B1")

    label("loc_139A")

    OP_62(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_13B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13D9")
    OP_62(0xF0, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1440")

    label("loc_13D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1401")
    OP_62(0xF0, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1440")

    label("loc_1401")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1429")
    OP_62(0xF0, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1440")

    label("loc_1429")

    OP_62(0xF0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_1440")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1468")
    OP_62(0xF1, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_14CF")

    label("loc_1468")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1490")
    OP_62(0xF1, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_14CF")

    label("loc_1490")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B8")
    OP_62(0xF1, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_14CF")

    label("loc_14B8")

    OP_62(0xF1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_14CF")

    Sleep(1800)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1510")

    ChrTalk(    #17
        0x10F,
        "#1801F#6P……不要背后说人坏话啊。\x02",
    )

    CloseMessageWindow()

    label("loc_1510")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1560")

    ChrTalk(    #18
        0x101,
        (
            "#1016F#6P嗯，虽然有一阵子没见，\x01",
            "你好像完全没变呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15E3")

    label("loc_1560")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15A3")

    ChrTalk(    #19
        0x10B,
        (
            "#416F#6P真是的……\x01",
            "看来还是老样子呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15E3")

    label("loc_15A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15E3")

    ChrTalk(    #20
        0x106,
        (
            "#555F#6P真是的……\x01",
            "看来还是老样子呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15E3")


    ChrTalk(    #21
        0x109,
        (
            "#1841F#6P唉……\x01",
            "为什么又被抓到这种地方来了啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_1640():
        OP_6D(-81370, 700, -291000, 1000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1640)

    def lambda_1658():
        OP_67(0, 2400, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1658)

    def lambda_1670():
        OP_6B(3350, 1000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1670)

    def lambda_1680():
        OP_6E(280, 1000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1680)
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_22(0xCB, 0x0, 0x64)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    ClearChrFlags(0x10, 0x800)
    SetChrFlags(0x10, 0x1)

    def lambda_16BB():
        OP_96(0xFE, 0xFFFECC8A, 0x1F4, 0xFFFB8F48, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_16BB)
    OP_8C(0x10, 270, 0)
    WaitChrThread(0x10, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    ChrTalk(    #22
        0x10,
        (
            "#1224F#5P你、你们是……\x01",
            "什么时候到这里来的！？\x02\x03",

            "对、对了，\x01",
            "你们是来嘲笑我的吧！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x109,
        (
            "#1068F#6P哎呀～\x01",
            "不好意思，说实话我早就已经把你忘了。\x02\x03",

            "#1060F小哥你又是\x01",
            "被卷进『漩涡』\x01",
            "来到这种地方的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10,
        (
            "#1222F#5P……哼，一点不错。\x02\x03",

            "看来这里也和王都一样\x01",
            "是被仿造出来的地方啊……\x02\x03",

            "#1223F我当时瞬间就被哨戒机包围，\x01",
            "沐浴在电击中……\x02\x03",

            "醒来就发现在这里了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x109,
        "#1840F#6P原、原来如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x102,
        (
            "#1505F#6P（精神上似乎\x01",
            "  受了很大打击啊……）\x02\x03",

            "#1500F……请稍微等一下。\x02\x03",

            "大概操作那边的终端\x01",
            "就能解除这道障壁。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 90, 400)
    Sleep(300)

    ChrTalk(    #27
        0x10,
        (
            "#1223F#5P哼……\x01",
            "不用管我……\x02\x03",

            "反正就算回去了，\x01",
            "也只会被肯帕雷拉大人\x01",
            "欺负和嘲笑……\x02\x03",

            "#1228F什么出人头地……\x01",
            "在『结社』出人头地\x01",
            "对我来说是不可能的……\x02\x03",

            "………（嘀嘀咕咕）……………\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A3C")
    OP_62(0xEE, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1AA3")

    label("loc_1A3C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A64")
    OP_62(0xEE, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1AA3")

    label("loc_1A64")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A8C")
    OP_62(0xEE, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1AA3")

    label("loc_1A8C")

    OP_62(0xEE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_1AA3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ACB")
    OP_62(0xEF, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1B32")

    label("loc_1ACB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AF3")
    OP_62(0xEF, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1B32")

    label("loc_1AF3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B1B")
    OP_62(0xEF, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1B32")

    label("loc_1B1B")

    OP_62(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_1B32")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B5A")
    OP_62(0xF0, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1BC1")

    label("loc_1B5A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B82")
    OP_62(0xF0, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1BC1")

    label("loc_1B82")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BAA")
    OP_62(0xF0, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1BC1")

    label("loc_1BAA")

    OP_62(0xF0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_1BC1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BE9")
    OP_62(0xF1, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1C50")

    label("loc_1BE9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C11")
    OP_62(0xF1, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1C50")

    label("loc_1C11")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C39")
    OP_62(0xF1, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1C50")

    label("loc_1C39")

    OP_62(0xF1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_1C50")

    Sleep(1800)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CA3")

    ChrTalk(    #28
        0x10F,
        (
            "#1446F#6P（思考似乎开始\x01",
            "  陷入恶性循环了呢……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D34")

    label("loc_1CA3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CF3")

    ChrTalk(    #29
        0x104,
        (
            "#1544F#6P（唔，思考似乎开始\x01",
            "  陷入恶性循环了呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D34")

    label("loc_1CF3")


    ChrTalk(    #30
        0x109,
        (
            "#1068F#6P（思、思考似乎开始\x01",
            "  陷入恶性循环了呢……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D34")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D78")

    ChrTalk(    #31
        0x105,
        (
            "#1165F#6P（实在是……\x01",
            "  有点可怜呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E07")

    label("loc_1D78")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DC1")

    ChrTalk(    #32
        0x10A,
        (
            "#819F#6P（嗯、嗯……\x01",
            "  实在是有点可怜呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E07")

    label("loc_1DC1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E07")

    ChrTalk(    #33
        0x107,
        (
            "#562F#6P（实、实在是……\x01",
            "  有点可怜呢……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E07")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E40")

    ChrTalk(    #34
        0x103,
        "#1534F#6P（呼～真是的……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EE7")

    label("loc_1E40")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E76")

    ChrTalk(    #35
        0x108,
        "#573F#6P（哎呀哎呀……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EE7")

    label("loc_1E76")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EB4")

    ChrTalk(    #36
        0x10E,
        "#176F#6P（……哎呀哎呀…………）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EE7")

    label("loc_1EB4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EE7")

    ChrTalk(    #37
        0x10C,
        "#115F#6P（哎呀哎呀……）\x02",
    )

    CloseMessageWindow()

    label("loc_1EE7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F21")

    ChrTalk(    #38
        0x106,
        "#552F#6P（……真没用………）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F58")

    label("loc_1F21")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F58")

    ChrTalk(    #39
        0x10D,
        "#276F#6P（……真软弱………）\x02",
    )

    CloseMessageWindow()

    label("loc_1F58")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F9C")

    ChrTalk(    #40
        0x10B,
        (
            "#212F#6P（真是的……\x01",
            "  看着就叫人着急。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F9C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_249A")

    ChrTalk(    #41
        0x110,
        (
            "#263F#6P嗯，\x01",
            "不过着眼点不是还不错吗。\x02\x03",

            "#1306F这个『影之国』，\x01",
            "存在于超越结社技术的次元。\x02\x03",

            "如果能够提出报告，\x01",
            "『十三工房』应该会很高兴的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20B4")

    def lambda_207E():
        TurnDirection(0xFE, 0x110, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_207E)
    Sleep(100)

    def lambda_2091():
        TurnDirection(0xFE, 0x110, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_2091)
    Sleep(100)

    def lambda_20A4():
        TurnDirection(0xFE, 0x110, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_20A4)
    Sleep(100)
    Jump("loc_2145")

    label("loc_20B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20FE")

    def lambda_20C8():
        TurnDirection(0xFE, 0x110, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_20C8)
    Sleep(100)

    def lambda_20DB():
        TurnDirection(0xFE, 0x110, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_20DB)
    Sleep(100)

    def lambda_20EE():
        TurnDirection(0xFE, 0x110, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_20EE)
    Sleep(100)
    Jump("loc_2145")

    label("loc_20FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2145")

    def lambda_2112():
        TurnDirection(0xFE, 0x110, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_2112)
    Sleep(100)

    def lambda_2125():
        TurnDirection(0xFE, 0x110, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2125)
    Sleep(100)

    def lambda_2138():
        TurnDirection(0xFE, 0x110, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_2138)
    Sleep(100)

    label("loc_2145")

    OP_8C(0x10, 270, 400)
    Sleep(300)

    ChrTalk(    #42
        0x10,
        (
            "#1221F#5P这……是真的吗！？\x02\x03",

            "#1222F──哎，你不是……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #43
        0x10,
        "#1224F#5P玲、玲、玲……\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #44
        0x10,
        "#1224F#5P#4S玲大人！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #45
        0x10,
        (
            "#1224F#5P为什么『歼灭天使』……\x01",
            "不，您会在这种地方！？\x02\x03",

            "难、难不成认为我背叛了，\x01",
            "打算来处置我！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x110,
        (
            "#264F#6P哎呀……\x01",
            "大哥哥，你背叛了吗？\x02\x03",

            "#263F嘻嘻，\x01",
            "虽然处理背叛者不是玲的工作……\x02\x03",

            "#1306F要是你希望的话，\x01",
            "我倒也可以特别给你点惩罚哦？\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x10, 0x0, 0x0, 0xB)
    Sleep(500)

    ChrTalk(    #47
        0x10,
        "#1224F#5P呜、呜哇……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #48
        0x10,
        (
            "#1227F#5P#3S我没背叛！\x01",
            "没背叛啦！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #49
        0x102,
        "#1512F#5P……玲。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2407")

    ChrTalk(    #50
        0x107,
        "#067F#5P玲、玲……\x02",
    )

    CloseMessageWindow()

    label("loc_2407")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2445")

    ChrTalk(    #51
        0x101,
        (
            "#1016F#5P喂喂……\x01",
            "别太欺负他啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_247A")

    label("loc_2445")


    ChrTalk(    #52
        0x109,
        (
            "#1840F#5P哈哈……\x01",
            "欺负人也要有个限度啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_247A")


    ChrTalk(    #53
        0x110,
        "#261F#6P嘻嘻……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C63")

    label("loc_249A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2790")

    ChrTalk(    #54
        0x101,
        "#1019F#6P唉……真是的。\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #55
        0x101,
        (
            "#1022F#3S#6P喂！\x01",
            "给我振作点！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #56
        0x101,
        (
            "#1005F#6P都一把年纪了吧！？\x01",
            "不觉得丢脸吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25B0")

    def lambda_257A():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_257A)
    Sleep(100)

    def lambda_258D():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_258D)
    Sleep(100)

    def lambda_25A0():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_25A0)
    Sleep(100)
    Jump("loc_2641")

    label("loc_25B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25FA")

    def lambda_25C4():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_25C4)
    Sleep(100)

    def lambda_25D7():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_25D7)
    Sleep(100)

    def lambda_25EA():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_25EA)
    Sleep(100)
    Jump("loc_2641")

    label("loc_25FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2641")

    def lambda_260E():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_260E)
    Sleep(100)

    def lambda_2621():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2621)
    Sleep(100)

    def lambda_2634():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_2634)
    Sleep(100)

    label("loc_2641")

    OP_8C(0x10, 270, 400)
    Sleep(300)

    ChrTalk(    #57
        0x10,
        "#1224F怎、怎么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        (
            "#1007F#6P你还是不是\x01",
            "结社的走狗\x01",
            "都不关我的事。\x02\x03",

            "#1019F不过，\x01",
            "身为游击士也不能把你就这么扔下不管。\x02\x03",

            "再这么婆婆妈妈的说下去……\x01",
            "我就把绳子拴在你脖子上拖走哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x10,
        "#1225F#5P呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x102,
        "#1514F#5P艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x109,
        (
            "#1840F#5P哈哈……\x01",
            "还是老样子啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C63")

    label("loc_2790")


    ChrTalk(    #62
        0x102,
        "#1505F#6P………………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x109, 400)
    Sleep(300)

    ChrTalk(    #63
        0x102,
        (
            "#1502F#11P……凯文先生。\x01",
            "看来我们是在浪费时间呢。\x02\x03",

            "还是扔下他继续探索吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2871")

    def lambda_283B():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_283B)
    Sleep(100)

    def lambda_284E():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_284E)
    Sleep(100)

    def lambda_2861():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_2861)
    Sleep(300)
    Jump("loc_2902")

    label("loc_2871")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28BB")

    def lambda_2885():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_2885)
    Sleep(100)

    def lambda_2898():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2898)
    Sleep(100)

    def lambda_28AB():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_28AB)
    Sleep(300)
    Jump("loc_2902")

    label("loc_28BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2902")

    def lambda_28CF():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_28CF)
    Sleep(100)

    def lambda_28E2():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_28E2)
    Sleep(100)

    def lambda_28F5():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_28F5)
    Sleep(300)

    label("loc_2902")


    ChrTalk(    #64
        0x109,
        "#1064F#5P哎……\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x10, 270, 600)
    Sleep(300)

    ChrTalk(    #65
        0x10,
        (
            "#1225F#5P等、等一下！\x02\x03",

            "你、你……脱离结社\x01",
            "回到游击士协会了吧！？\x02\x03",

            "怎么能对我见死不救啊！？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A2A")

    def lambda_29E1():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_29E1)
    Sleep(100)

    def lambda_29F4():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_29F4)
    Sleep(100)

    def lambda_2A07():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_2A07)
    Sleep(100)

    def lambda_2A1A():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_2A1A)
    Sleep(400)
    Jump("loc_2AE1")

    label("loc_2A2A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A87")

    def lambda_2A3E():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2A3E)
    Sleep(100)

    def lambda_2A51():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_2A51)
    Sleep(100)

    def lambda_2A64():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2A64)
    Sleep(100)

    def lambda_2A77():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_2A77)
    Sleep(400)
    Jump("loc_2AE1")

    label("loc_2A87")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AE1")

    def lambda_2A9B():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2A9B)
    Sleep(100)

    def lambda_2AAE():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_2AAE)
    Sleep(100)

    def lambda_2AC1():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2AC1)
    Sleep(100)

    def lambda_2AD4():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_2AD4)
    Sleep(400)

    label("loc_2AE1")


    ChrTalk(    #66
        0x102,
        (
            "#1505F#6P……游击士的守护义务\x01",
            "只以民间人士为对象。\x02\x03",

            "#1502F你身为非法组织成员，\x01",
            "还是指名通缉犯，\x01",
            "难道觉得自己包括在内吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x10,
        "#1224F#5P呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x102,
        (
            "#1500F#6P不过，怎样看待规则\x01",
            "经常也要看游击士各自的判断。\x02\x03",

            "#1509F说到底，\x01",
            "特地去帮助拒绝帮助的人\x01",
            "我倒不认为有这必要。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #69
        0x10,
        (
            "#1227F#5P我、我从来没说过\x01",
            "不想要你们帮忙啊！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C63")


    def lambda_2C69():
        OP_6D(-82520, 0, -290940, 1800)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_2C69)

    def lambda_2C81():
        OP_67(0, 4050, -10000, 1800)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2C81)

    def lambda_2C99():
        OP_6B(3170, 1800)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_2C99)

    def lambda_2CA9():
        OP_6E(270, 1800)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_2CA9)
    OP_44(0x10, 0x0)
    OP_22(0xCB, 0x0, 0x64)

    def lambda_2CC2():
        OP_96(0xFE, 0xFFFEC460, 0x0, 0xFFFB8F48, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2CC2)
    WaitChrThread(0x10, 0x1)
    ClearChrFlags(0x10, 0x4)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_2CEF():
        OP_8E(0xFE, 0xFFFEB7E0, 0x0, 0xFFFB8F48, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2CEF)

    def lambda_2D0A():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_2D0A)
    Sleep(100)

    def lambda_2D1D():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_2D1D)
    Sleep(100)

    def lambda_2D30():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_2D30)
    Sleep(100)

    def lambda_2D43():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_2D43)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0xEE, 0x1)
    Sleep(300)

    ChrTalk(    #70
        0x10,
        (
            "#1225F#5P啊啊，知道啦！\x01",
            "既然你都说到这份上就算我求你了！\x02\x03",

            "#1227F要什么酬劳我都答应，\x01",
            "拜托把这该死的障壁给消除掉吧！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E1E")

    ChrTalk(    #71
        0x101,
        (
            "#1006F#6P哼哼。\x01",
            "早这么说不就完了～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E1E")


    ChrTalk(    #72
        0x102,
        "#1513F#6P……明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x109,
        (
            "#1068F#6P唉～真是麻烦的小哥啊。\x02\x03",

            "#1066F也罢，\x01",
            "赶快去操作一下那边的终端试试吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2B24)
    OP_28(0x3A, 0x1, 0x10)
    OP_65(0x1, 0x1)
    SetChrFlags(0x11, 0x80)
    Sleep(300)
    Fade(1000)
    ClearChrFlags(0x10, 0x1)
    SetChrPos(0x10, -84150, 0, -290050, 270)
    OP_43(0x10, 0x0, 0x0, 0x2)
    EventEnd(0x0)
    Return()

    # Function_10_DAC end

    def Function_11_2EDE(): pass

    label("Function_11_2EDE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2F1A")
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1000)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1500)
    Jump("Function_11_2EDE")

    label("loc_2F1A")

    Return()

    # Function_11_2EDE end

    def Function_12_2F1B(): pass

    label("Function_12_2F1B")

    EventBegin(0x0)
    Fade(500)
    OP_6D(-86510, 0, -342000, 0)
    OP_67(0, 6850, -10000, 0)
    OP_6B(2920, 0)
    OP_6C(45000, 0)
    OP_6E(245, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FB4")
    SetChrPos(0x109, -87710, 0, -342990, 90)
    SetChrPos(0x102, -88310, 0, -344500, 45)
    SetChrPos(0xF0, -88930, 0, -342520, 90)
    SetChrPos(0xF1, -89500, 0, -344070, 90)
    Jump("loc_30A2")

    label("loc_2FB4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3009")
    SetChrPos(0x109, -87710, 0, -342990, 90)
    SetChrPos(0x102, -88310, 0, -344500, 45)
    SetChrPos(0xEF, -88930, 0, -342520, 90)
    SetChrPos(0xF1, -89500, 0, -344070, 90)
    Jump("loc_30A2")

    label("loc_3009")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_305E")
    SetChrPos(0x109, -87710, 0, -342990, 90)
    SetChrPos(0x102, -88310, 0, -344500, 45)
    SetChrPos(0xEF, -88930, 0, -342520, 90)
    SetChrPos(0xF0, -89500, 0, -344070, 90)
    Jump("loc_30A2")

    label("loc_305E")

    SetChrPos(0x0, -87710, 0, -342990, 90)
    SetChrPos(0x1, -88310, 0, -344500, 45)
    SetChrPos(0x2, -88930, 0, -342520, 90)
    SetChrPos(0x3, -89500, 0, -344070, 90)

    label("loc_30A2")

    OP_0D()
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_30C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_369F")
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #74
        "\x18\x07\x05输入想解除的障壁号码\x18\x02",
    )


    Menu(
        0,
        -1,
        150,
        1,
        (
            "【１号】\x01",      # 0
            "【２号】\x01",      # 1
            "【３号】\x01",      # 2
            "【４号】\x01",      # 3
            "【５号】\x01",      # 4
        )
    )

    Jump("loc_316C")

    label("loc_316C")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_31AC"),
        (1, "loc_32A2"),
        (2, "loc_3398"),
        (3, "loc_348E"),
        (4, "loc_3584"),
        (SWITCH_DEFAULT, "loc_367C"),
    )


    label("loc_31AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3251")
    OP_6D(-81410, 0, -332940, 2000)
    OP_22(0xAA, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x23)
    OP_22(0xE1, 0x0, 0x64)
    OP_73(0x3)
    Sleep(500)
    OP_6F(0x3, 35)
    OP_70(0x3, 0x32)
    OP_22(0x6D, 0x0, 0x64)
    OP_73(0x3)
    OP_A2(0x2B72)
    Fade(500)
    OP_6D(-86510, 0, -342000, 0)
    OP_67(0, 6850, -10000, 0)
    OP_6B(2920, 0)
    OP_6C(45000, 0)
    OP_6E(245, 0)
    OP_0D()
    Sleep(300)
    Jump("loc_3689")

    label("loc_3251")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("合成音")

    AnonymousTalk(    #75
        (
            "\x07\x05１号的锁\x01",
            "已经被解除。\x02",
        )
    )

    Jump("loc_3293")

    label("loc_3293")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_3689")

    label("loc_32A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3347")
    OP_6D(-83240, 0, -320400, 3000)
    OP_22(0xAA, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x23)
    OP_22(0xE1, 0x0, 0x64)
    OP_73(0x4)
    Sleep(500)
    OP_6F(0x4, 35)
    OP_70(0x4, 0x32)
    OP_22(0x6D, 0x0, 0x64)
    OP_73(0x4)
    OP_A2(0x2B73)
    Fade(500)
    OP_6D(-86510, 0, -342000, 0)
    OP_67(0, 6850, -10000, 0)
    OP_6B(2920, 0)
    OP_6C(45000, 0)
    OP_6E(245, 0)
    OP_0D()
    Sleep(300)
    Jump("loc_3689")

    label("loc_3347")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("合成音")

    AnonymousTalk(    #76
        (
            "\x07\x05２号的锁\x01",
            "已经被解除。\x02",
        )
    )

    Jump("loc_3389")

    label("loc_3389")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_3689")

    label("loc_3398")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_343D")
    OP_6D(-83240, 0, -309340, 3000)
    OP_22(0xAA, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x5, 0)
    OP_70(0x5, 0x23)
    OP_22(0xE1, 0x0, 0x64)
    OP_73(0x5)
    Sleep(500)
    OP_6F(0x5, 35)
    OP_70(0x5, 0x32)
    OP_22(0x6D, 0x0, 0x64)
    OP_73(0x5)
    OP_A2(0x2B74)
    Fade(500)
    OP_6D(-86510, 0, -342000, 0)
    OP_67(0, 6850, -10000, 0)
    OP_6B(2920, 0)
    OP_6C(45000, 0)
    OP_6E(245, 0)
    OP_0D()
    Sleep(300)
    Jump("loc_3689")

    label("loc_343D")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("合成音")

    AnonymousTalk(    #77
        (
            "\x07\x05３号的锁\x01",
            "已经被解除。\x02",
        )
    )

    Jump("loc_347F")

    label("loc_347F")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_3689")

    label("loc_348E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3533")
    OP_6D(-83240, 0, -299470, 3000)
    OP_22(0xAA, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x6, 0)
    OP_70(0x6, 0x23)
    OP_22(0xE1, 0x0, 0x64)
    OP_73(0x6)
    Sleep(500)
    OP_6F(0x6, 35)
    OP_70(0x6, 0x32)
    OP_22(0x6D, 0x0, 0x64)
    OP_73(0x6)
    OP_A2(0x2B75)
    Fade(500)
    OP_6D(-86510, 0, -342000, 0)
    OP_67(0, 6850, -10000, 0)
    OP_6B(2920, 0)
    OP_6C(45000, 0)
    OP_6E(245, 0)
    OP_0D()
    Sleep(300)
    Jump("loc_3689")

    label("loc_3533")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("合成音")

    AnonymousTalk(    #78
        (
            "\x07\x05４号的锁\x01",
            "已经被解除。\x02",
        )
    )

    Jump("loc_3575")

    label("loc_3575")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_3689")

    label("loc_3584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_362B")
    OP_44(0x10, 0xFF)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x10, -83790, 0, -290050, 270)
    SetChrFlags(0x10, 0x1)
    OP_6D(-83240, 0, -289000, 3000)
    OP_22(0xAA, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x7, 0)
    OP_70(0x7, 0x23)
    OP_22(0xE1, 0x0, 0x64)
    Sleep(300)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_73(0x7)
    Sleep(500)
    OP_6F(0x7, 35)
    OP_70(0x7, 0x32)
    OP_22(0x6D, 0x0, 0x64)
    OP_73(0x7)
    OP_A2(0x2B76)
    Call(0, 13)
    Return()

    label("loc_362B")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("合成音")

    AnonymousTalk(    #79
        (
            "\x07\x05５号的锁\x01",
            "已经被解除。\x02",
        )
    )

    Jump("loc_366D")

    label("loc_366D")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_3689")

    label("loc_367C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3689")

    label("loc_3689")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_30C5")

    label("loc_369F")

    FadeToBright(300, 0)
    EventEnd(0x0)
    Return()

    # Function_12_2F1B end

    def Function_13_36AB(): pass

    label("Function_13_36AB")

    EventBegin(0x0)
    SetChrPos(0x109, -88230, 0, -297890, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3702")
    SetChrPos(0x102, -87150, 0, -298730, 0)
    SetChrPos(0xF0, -88720, 0, -300010, 0)
    SetChrPos(0xF1, -87070, 0, -300720, 0)
    Jump("loc_3787")

    label("loc_3702")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3746")
    SetChrPos(0x102, -87150, 0, -298730, 0)
    SetChrPos(0xEF, -88720, 0, -300010, 0)
    SetChrPos(0xF1, -87070, 0, -300720, 0)
    Jump("loc_3787")

    label("loc_3746")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3787")
    SetChrPos(0x102, -87150, 0, -298730, 0)
    SetChrPos(0xEF, -88720, 0, -300010, 0)
    SetChrPos(0xF0, -87070, 0, -300720, 0)

    label("loc_3787")

    Sleep(500)

    ChrTalk(    #80
        0x10,
        "#1225F#5P哦哦哦！？\x02",
    )

    CloseMessageWindow()

    def lambda_37B2():
        OP_6D(-86350, 0, -288930, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_37B2)
    OP_8E(0x10, 0xFFFEA9E4, 0x0, 0xFFFB92D6, 0x1388, 0x0)
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #81
        0x10,
        (
            "#1221F#5P哈哈哈！\x01",
            "成功了，成功了！！\x02\x03",

            "#1226F这就是命运！\x01",
            "就是女神的指引啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x109,
        (
            "#1066F#1P哎呀哎呀……\x01",
            "真是容易得意忘形的小哥啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_387F():
        OP_6D(-86170, 0, -290780, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_387F)

    def lambda_3897():
        OP_67(0, 6540, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_3897)

    def lambda_38AF():
        OP_6B(2370, 3000)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_38AF)

    def lambda_38BF():
        OP_6E(336, 3000)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_38BF)

    def lambda_38CF():
        OP_8F(0xFE, 0xFFFEA6EC, 0x0, 0xFFFB8804, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_38CF)
    OP_8C(0x10, 180, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_394D")

    def lambda_38FF():
        OP_8F(0xFE, 0xFFFEAC28, 0x0, 0xFFFB878C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_38FF)

    def lambda_391A():
        OP_8F(0xFE, 0xFFFEA570, 0x0, 0xFFFB8246, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_391A)

    def lambda_3935():
        OP_8F(0xFE, 0xFFFEAB1A, 0x0, 0xFFFB8156, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_3935)
    Jump("loc_3A0E")

    label("loc_394D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39AF")

    def lambda_3961():
        OP_8F(0xFE, 0xFFFEAC28, 0x0, 0xFFFB878C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3961)

    def lambda_397C():
        OP_8F(0xFE, 0xFFFEA570, 0x0, 0xFFFB8246, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_397C)

    def lambda_3997():
        OP_8F(0xFE, 0xFFFEAB1A, 0x0, 0xFFFB8156, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_3997)
    Jump("loc_3A0E")

    label("loc_39AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A0E")

    def lambda_39C3():
        OP_8F(0xFE, 0xFFFEAC28, 0x0, 0xFFFB878C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_39C3)

    def lambda_39DE():
        OP_8F(0xFE, 0xFFFEA570, 0x0, 0xFFFB8246, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_39DE)

    def lambda_39F9():
        OP_8F(0xFE, 0xFFFEAB1A, 0x0, 0xFFFB8156, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_39F9)

    label("loc_3A0E")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0xEE, 0x1)
    Sleep(300)

    ChrTalk(    #83
        0x10,
        (
            "#1222F#5P哼、哼……\x01",
            "可别以为这样就赢了哦？\x02\x03",

            "#1226F本来，\x01",
            "对身为敌人的你们没必要道谢……\x02\x03",

            "#1221F这次我就特别把这个给你们，\x01",
            "你们可要感激涕零啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_8F(0x10, 0xFFFEA9E4, 0x0, 0xFFFB8C46, 0xBB8, 0x0)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #84
        "\x07\x00得到了\x1F\x37\x03\x07\x00。\x02",
    )

    Jump("loc_3B1A")

    label("loc_3B1A")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x337, 1)
    OP_8F(0x10, 0xFFFEA9E4, 0x0, 0xFFFB8FA2, 0x7D0, 0x0)
    Sleep(300)

    ChrTalk(    #85
        0x102,
        "#1504F#11P咦……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B97")

    ChrTalk(    #86
        0x101,
        "#1004F#11P这是……\x02",
    )

    CloseMessageWindow()

    label("loc_3B97")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BCD")

    ChrTalk(    #87
        0x10B,
        "#213F#11P那个时候的……！？\x02",
    )

    CloseMessageWindow()

    label("loc_3BCD")


    ChrTalk(    #88
        0x10,
        (
            "#1226F#5P呼，\x01",
            "是刚刚更新过的最新安全卡。\x02\x03",

            "#1220F不过，\x01",
            "这是我到这个世界以前获得的东西，\x01",
            "应该不会很有用就是了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3C55():

        label("loc_3C55")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_3C55")

    QueueWorkItem2(0xEE, 3, lambda_3C55)

    def lambda_3C66():

        label("loc_3C66")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_3C66")

    QueueWorkItem2(0xEF, 3, lambda_3C66)

    def lambda_3C77():

        label("loc_3C77")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_3C77")

    QueueWorkItem2(0xF0, 3, lambda_3C77)

    def lambda_3C88():

        label("loc_3C88")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_3C88")

    QueueWorkItem2(0xF1, 3, lambda_3C88)

    def lambda_3C99():
        OP_6D(-86550, 0, -294630, 1800)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_3C99)
    OP_43(0x10, 0x0, 0x0, 0xE)
    WaitChrThread(0x10, 0x0)
    OP_44(0xEE, 0x3)
    OP_44(0xEF, 0x3)
    OP_44(0xF0, 0x3)
    OP_44(0xF1, 0x3)
    OP_8C(0xEE, 180, 0)
    OP_8C(0xEF, 180, 0)
    OP_8C(0xF0, 180, 0)
    OP_8C(0xF1, 180, 0)
    WaitChrThread(0xEE, 0x1)
    Sleep(300)

    ChrTalk(    #89
        0x10,
        (
            "#1221F#12P那么，别了诸位！\x02\x03",

            "下次再见时就是敌人了……\x01",
            "做好心理准备吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 180, 400)

    def lambda_3D53():
        OP_6D(-86550, 0, -296000, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_3D53)

    def lambda_3D6B():
        OP_8E(0xFE, 0xFFFEA96C, 0x0, 0xFFFB4CE0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_3D6B)
    WaitChrThread(0x10, 0x0)
    SetChrFlags(0x10, 0x80)
    WaitChrThread(0xEE, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DB2")
    OP_62(0xEE, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3E0A")

    label("loc_3DB2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DD5")
    OP_62(0xEE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3E0A")

    label("loc_3DD5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DF8")
    OP_62(0xEE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3E0A")

    label("loc_3DF8")

    OP_62(0xEE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_3E0A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E2D")
    OP_62(0xEF, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3E85")

    label("loc_3E2D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E50")
    OP_62(0xEF, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3E85")

    label("loc_3E50")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E73")
    OP_62(0xEF, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3E85")

    label("loc_3E73")

    OP_62(0xEF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_3E85")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EA8")
    OP_62(0xF0, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3F00")

    label("loc_3EA8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3ECB")
    OP_62(0xF0, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3F00")

    label("loc_3ECB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EEE")
    OP_62(0xF0, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3F00")

    label("loc_3EEE")

    OP_62(0xF0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_3F00")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F23")
    OP_62(0xF1, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3F7B")

    label("loc_3F23")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F46")
    OP_62(0xF1, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3F7B")

    label("loc_3F46")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F69")
    OP_62(0xF1, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3F7B")

    label("loc_3F69")

    OP_62(0xF1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_3F7B")

    Sleep(1500)

    def lambda_3F86():
        OP_6D(-86660, 0, -292380, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_3F86)

    def lambda_3F9E():
        OP_6B(2220, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_3F9E)
    WaitChrThread(0xEE, 0x0)
    OP_63(0xEE)
    OP_63(0xEF)
    OP_63(0xF0)
    OP_63(0xF1)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FEA")

    ChrTalk(    #90
        0x105,
        "#1165F#5P……哎。\x02",
    )

    CloseMessageWindow()

    label("loc_3FEA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_401E")

    ChrTalk(    #91
        0x107,
        "#560F#5P走、走掉了呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_404D")

    label("loc_401E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_404D")

    ChrTalk(    #92
        0x10A,
        "#814F#5P……走掉了。\x02",
    )

    CloseMessageWindow()

    label("loc_404D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4083")

    ChrTalk(    #93
        0x10D,
        "#276F#5P……这算什么啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_40B2")

    label("loc_4083")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40B2")

    ChrTalk(    #94
        0x106,
        "#055F#5P这算什么……\x02",
    )

    CloseMessageWindow()

    label("loc_40B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40FF")

    ChrTalk(    #95
        0x101,
        (
            "#1016F#5P好、好像在刚才的一瞬间，\x01",
            "脑子转不过来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4131")

    ChrTalk(    #96
        0x108,
        "#070F#5P哎呀哎呀……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4162")

    label("loc_4131")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4162")

    ChrTalk(    #97
        0x10C,
        "#119F#5P……哎呀哎呀。\x02",
    )

    CloseMessageWindow()

    label("loc_4162")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41B0")

    ChrTalk(    #98
        0x104,
        (
            "#1541F#5P呼……\x01",
            "还是一个喜欢\x01",
            "把好处都占掉的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41F3")

    ChrTalk(    #99
        0x10B,
        (
            "#413F#5P怎么说呢……\x01",
            "那也算是天性吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4234")

    label("loc_41F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4234")

    ChrTalk(    #100
        0x103,
        (
            "#1527F#5P怎么说呢……\x01",
            "那也算是天性吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4234")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_427C")

    ChrTalk(    #101
        0x10F,
        (
            "#1805F#5P呼……\x01",
            "早知道就应该把他关起来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42C0")

    label("loc_427C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42C0")

    ChrTalk(    #102
        0x10E,
        (
            "#178F#5P唔……\x01",
            "早知道就应该把他关起来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4313")

    ChrTalk(    #103
        0x110,
        (
            "#261F#5P嘻嘻……\x01",
            "我好像有点明白\x01",
            "为什么肯帕雷拉中意他了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4313")


    ChrTalk(    #104
        0x102,
        "#1503F#5P…………………………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 270, 400)
    Sleep(300)

    ChrTalk(    #105
        0x102,
        (
            "#1513F#11P……凯文先生。\x02\x03",

            "#1500F这个安全卡，\x01",
            "说不定能意外的派上用场呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43E8")

    def lambda_43BE():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_43BE)
    Sleep(100)

    def lambda_43D1():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_43D1)
    Sleep(100)
    OP_8C(0x109, 90, 400)
    Jump("loc_4461")

    label("loc_43E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4426")

    def lambda_43FC():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_43FC)
    Sleep(100)

    def lambda_440F():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_440F)
    Sleep(100)
    OP_8C(0x109, 90, 400)
    Jump("loc_4461")

    label("loc_4426")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4461")

    def lambda_443A():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_443A)
    Sleep(100)

    def lambda_444D():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_444D)
    Sleep(100)
    OP_8C(0x109, 90, 400)

    label("loc_4461")

    Sleep(300)

    ChrTalk(    #106
        0x109,
        (
            "#1075F#6P啊啊，\x01",
            "我也正有这种想法。\x02\x03",

            "#1078F遇到像是可以用的地方，\x01",
            "就先试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2B25)
    OP_28(0x3A, 0x1, 0x20)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_13_36AB end

    def Function_14_44DA(): pass

    label("Function_14_44DA")

    OP_8C(0xFE, 225, 400)
    OP_8E(0xFE, 0xFFFEA264, 0x0, 0xFFFB8AFC, 0x1B58, 0x0)
    OP_8E(0xFE, 0xFFFEA264, 0x0, 0xFFFB7CF6, 0x1B58, 0x0)
    OP_8E(0xFE, 0xFFFEA87C, 0x0, 0xFFFB759E, 0x1B58, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_14_44DA end

    def Function_15_4525(): pass

    label("Function_15_4525")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4545")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4822")

    Menu(
        0,
        -1,
        150,
        1,
        (
            "打开门\x01",      # 0
            "放弃\x01",        # 1
        )
    )

    Jump("loc_4576")

    label("loc_4576")

    MenuEnd(0x0)
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4592"),
        (SWITCH_DEFAULT, "loc_4812"),
    )


    label("loc_4592")

    EventBegin(0x0)
    Fade(500)
    OP_6D(61240, 0, -185600, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x109, 60240, 0, -186570, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_462B")
    SetChrPos(0x102, 61770, 0, -186620, 0)
    SetChrPos(0xF0, 59990, 0, -188190, 0)
    SetChrPos(0xF1, 62120, 0, -188300, 0)
    Jump("loc_46B0")

    label("loc_462B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_466F")
    SetChrPos(0x102, 61770, 0, -186620, 0)
    SetChrPos(0xEF, 59990, 0, -188190, 0)
    SetChrPos(0xF1, 62120, 0, -188300, 0)
    Jump("loc_46B0")

    label("loc_466F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46B0")
    SetChrPos(0x102, 61770, 0, -186620, 0)
    SetChrPos(0xEF, 59990, 0, -188190, 0)
    SetChrPos(0xF0, 62120, 0, -188300, 0)

    label("loc_46B0")

    OP_0D()
    OP_20(0xBB8)

    def lambda_46BC():
        OP_6D(60980, 500, -184400, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_46BC)

    def lambda_46D4():
        OP_67(0, 5000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_46D4)

    def lambda_46EC():
        OP_6B(3120, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_46EC)

    def lambda_46FC():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_46FC)
    WaitChrThread(0xEE, 0x0)
    OP_21()
    OP_6F(0x2, 0)
    OP_70(0x2, 0x10E)
    OP_22(0x132, 0x0, 0x64)
    Sleep(500)

    def lambda_472A():
        OP_67(0, 4500, -10000, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_472A)

    def lambda_4742():
        OP_6B(3500, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_4742)
    OP_1D(0xB6)
    OP_1F(0x46, 0x64)
    OP_73(0x2)
    OP_64(0x2, 0x1)
    OP_A2(0x2B28)
    OP_28(0x3A, 0x1, 0x100)
    Sleep(1000)
    WaitChrThread(0xEE, 0x1)
    Fade(500)
    OP_6D(60990, 0, -186440, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 60990, 0, -186440, 0)
    SetChrPos(0x1, 60990, 0, -186440, 0)
    SetChrPos(0x2, 60990, 0, -186440, 0)
    SetChrPos(0x3, 60990, 0, -186440, 0)
    OP_0D()
    EventEnd(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_481F")

    label("loc_4812")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_481F")

    label("loc_481F")

    Jump("loc_4545")

    label("loc_4822")

    TalkEnd(0xFF)
    Return()

    # Function_15_4525 end

    def Function_16_4826(): pass

    label("Function_16_4826")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48F5")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(7680)
    Sleep(500)
    Jump("loc_48F8")

    label("loc_48F5")

    TalkBegin(0xFF)

    label("loc_48F8")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #107
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_4922")

    label("loc_4922")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4935")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4AAB")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "回复ＨＰ·ＥＰ\x01",      # 0
            "获得武具\x01",            # 1
            "合成结晶回路\x01",        # 2
            "结束\x01",                # 3
        )
    )

    Jump("loc_4987")

    label("loc_4987")

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_49A4"),
        (1, "loc_4A3D"),
        (2, "loc_4A6C"),
        (SWITCH_DEFAULT, "loc_4A9B"),
    )


    label("loc_49A4")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 1)), scpexpr(EXPR_END)), "loc_4A0A")
    OP_1D(0xEA)
    Jump("loc_4A1E")

    label("loc_4A0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 0)), scpexpr(EXPR_END)), "loc_4A1C")
    OP_1D(0xB6)
    OP_1F(0x46, 0x64)
    Jump("loc_4A1E")

    label("loc_4A1C")

    OP_1D(0xEA)

    label("loc_4A1E")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4AA8")

    label("loc_4A3D")

    OP_A9(0x26)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #108
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_4A69")

    label("loc_4A69")

    Jump("loc_4AA8")

    label("loc_4A6C")

    OP_A9(0x9)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #109
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_4A98")

    label("loc_4A98")

    Jump("loc_4AA8")

    label("loc_4A9B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4AA8")

    label("loc_4AA8")

    Jump("loc_4935")

    label("loc_4AAB")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AD8")
    OP_A2(0x25A0)
    EventEnd(0x1)
    Jump("loc_4ADB")

    label("loc_4AD8")

    TalkEnd(0xFF)

    label("loc_4ADB")

    Return()

    # Function_16_4826 end

    def Function_17_4ADC(): pass

    label("Function_17_4ADC")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x240147, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    TalkEnd(0xFF)
    Return()

    # Function_17_4ADC end

    def Function_18_4B02(): pass

    label("Function_18_4B02")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x240148, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    TalkEnd(0xFF)
    Return()

    # Function_18_4B02 end

    def Function_19_4B28(): pass

    label("Function_19_4B28")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x24014E, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    TalkEnd(0xFF)
    Return()

    # Function_19_4B28 end

    def Function_20_4B4E(): pass

    label("Function_20_4B4E")

    OP_A3(0x2B6A)
    OP_A2(0x2B6B)
    OP_A3(0x2B6C)
    OP_A3(0x2B6D)
    OP_A3(0x2B6E)
    OP_A3(0x2B6F)
    OP_A3(0x2B70)
    OP_A3(0x2B71)
    Return()

    # Function_20_4B4E end

    def Function_21_4B67(): pass

    label("Function_21_4B67")

    OP_A3(0x2B6A)
    OP_A3(0x2B6B)
    OP_A2(0x2B6C)
    OP_A3(0x2B6D)
    OP_A3(0x2B6E)
    OP_A3(0x2B6F)
    OP_A3(0x2B70)
    OP_A3(0x2B71)
    Return()

    # Function_21_4B67 end

    def Function_22_4B80(): pass

    label("Function_22_4B80")

    ClearMapFlags(0x2000000)
    OP_A3(0x2B6A)
    OP_A3(0x2B6B)
    OP_A3(0x2B6C)
    OP_A2(0x2B6D)
    OP_A3(0x2B6E)
    OP_A3(0x2B6F)
    OP_A3(0x2B70)
    OP_A3(0x2B71)
    Return()

    # Function_22_4B80 end

    def Function_23_4B9E(): pass

    label("Function_23_4B9E")

    SetMapFlags(0x2000000)
    Return()

    # Function_23_4B9E end

    def Function_24_4BA4(): pass

    label("Function_24_4BA4")

    OP_1D(0xB6)
    OP_1F(0x46, 0x64)
    Return()

    # Function_24_4BA4 end

    SaveToFile()

Try(main)
