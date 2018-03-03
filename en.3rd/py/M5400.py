from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Gilbert',                              # 9
        'Gilbert',                              # 10
        '',                                     # 11
        '',                                     # 12
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
        "Function_4_791",          # 04, 4
        "Function_5_8ED",          # 05, 5
        "Function_6_A42",          # 06, 6
        "Function_7_BCB",          # 07, 7
        "Function_8_CA9",          # 08, 8
        "Function_9_D65",          # 09, 9
        "Function_10_E86",         # 0A, 10
        "Function_11_329E",        # 0B, 11
        "Function_12_32DB",        # 0C, 12
        "Function_13_3A32",        # 0D, 13
        "Function_14_49F8",        # 0E, 14
        "Function_15_4A43",        # 0F, 15
        "Function_16_4D3E",        # 10, 16
        "Function_17_4FDE",        # 11, 17
        "Function_18_5004",        # 12, 18
        "Function_19_502A",        # 13, 19
        "Function_20_5050",        # 14, 20
        "Function_21_5069",        # 15, 21
        "Function_22_5082",        # 16, 22
        "Function_23_50A0",        # 17, 23
        "Function_24_50A6",        # 18, 24
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
            "#1224FY-You're not gonna change your minds after\x01",
            "getting my hopes up, are you?!\x02\x03",

            "#1227FPlease! Do something about this awful barrier!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x10)
    Return()

    # Function_3_6FF end

    def Function_4_791(): pass

    label("Function_4_791")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x579, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x25, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2DC, 1)"), scpexpr(EXPR_END)), "loc_7FF")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #1
        "\x07\x05Found \x1F\xDC\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BC8)
    Jump("loc_867")

    label("loc_7FF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05Found \x1F\xDC\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xDC\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x25, 60)
    OP_70(0x25, 0x0)

    label("loc_867")

    Jump("loc_8DF")

    label("loc_86A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "\x07\x05Inside the chest was absolutely nothing. Nothing after nothing came\x01",
            "bursting out.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x3D, 0x0)

    label("loc_8DF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_791 end

    def Function_5_8ED(): pass

    label("Function_5_8ED")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x579, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9FD")
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
            "\x07\x02Obtained:\x01",
            "#56IEarth Sepith x200\x01",
            "#57IWater Sepith x200\x01",
            "#58IFire Sepith x200\x01",
            "#59IWind Sepith x200\x01",
            "#62ITime Sepith x200\x01",
            "#60ISpace Sepith x200\x01",
            "#61IMirage Sepith x200.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2BC9)
    Jump("loc_A2B")

    label("loc_9FD")


    AnonymousTalk(    #5
        "\x07\x05...But the real treasure is KNOWLEDGE.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_A2B")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0x3E, 0x0)
    Return()

    # Function_5_8ED end

    def Function_6_A42(): pass

    label("Function_6_A42")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x579, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B52")
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
            "\x07\x02Obtained:\x01",
            "#56IEarth Sepith x200\x01",
            "#57IWater Sepith x200\x01",
            "#58IFire Sepith x200\x01",
            "#59IWind Sepith x200\x01",
            "#62ITime Sepith x200\x01",
            "#60ISpace Sepith x200\x01",
            "#61IMirage Sepith x200.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2BCA)
    Jump("loc_BB4")

    label("loc_B52")


    AnonymousTalk(    #7
        (
            "\x07\x05There's a picture of you looting this treasure chest inside. You decide\x01",
            "to leave it alone.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_BB4")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0x3F, 0x0)
    Return()

    # Function_6_A42 end

    def Function_7_BCB(): pass

    label("Function_7_BCB")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x579, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C35")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2C, 0x1E)
    OP_73(0x2C)
    OP_6F(0x2C, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddMira(5000)

    AnonymousTalk(    #8
        "\x07\x05Found \x07\x025,000 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2BCB)
    Jump("loc_C92")

    label("loc_C35")


    AnonymousTalk(    #9
        (
            "\x07\x05The dust in this chest is centuries old. You feel a very historical sneeze\x01",
            "coming on.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_C92")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0x40, 0x0)
    Return()

    # Function_7_BCB end

    def Function_8_CA9(): pass

    label("Function_8_CA9")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x579, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D13")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2D, 0x1E)
    OP_73(0x2D)
    OP_6F(0x2D, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddMira(5000)

    AnonymousTalk(    #10
        "\x07\x05Found \x07\x025,000 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2BCC)
    Jump("loc_D4E")

    label("loc_D13")


    AnonymousTalk(    #11
        "\x07\x05This chest's interior was professionally decorated.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_D4E")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0x41, 0x0)
    Return()

    # Function_8_CA9 end

    def Function_9_D65(): pass

    label("Function_9_D65")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x579, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E3E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2E, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2E1, 1)"), scpexpr(EXPR_END)), "loc_DD3")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x05Found \x1F\xE1\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BCD)
    Jump("loc_E3B")

    label("loc_DD3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "\x07\x05Found \x1F\xE1\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xE1\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2E, 60)
    OP_70(0x2E, 0x0)

    label("loc_E3B")

    Jump("loc_E78")

    label("loc_E3E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05I'll see you in court!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x42, 0x0)

    label("loc_E78")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_D65 end

    def Function_10_E86(): pass

    label("Function_10_E86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 4)), scpexpr(EXPR_END)), "loc_E8E")
    Return()

    label("loc_E8E")

    EventBegin(0x0)
    Fade(500)
    OP_6D(-86410, 0, -294190, 0)
    OP_67(0, 7120, -10000, 0)
    OP_6B(2770, 0)
    OP_6C(45000, 0)
    OP_6E(263, 0)
    SetChrPos(0x109, -88420, 0, -294580, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F27")
    SetChrPos(0x102, -86850, 0, -294760, 0)
    SetChrPos(0xF0, -88780, 0, -296280, 0)
    SetChrPos(0xF1, -87180, 0, -296440, 0)
    Jump("loc_FAC")

    label("loc_F27")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F6B")
    SetChrPos(0x102, -86850, 0, -294760, 0)
    SetChrPos(0xEF, -88780, 0, -296280, 0)
    SetChrPos(0xF1, -87180, 0, -296440, 0)
    Jump("loc_FAC")

    label("loc_F6B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FAC")
    SetChrPos(0x102, -86850, 0, -294760, 0)
    SetChrPos(0xEF, -88780, 0, -296280, 0)
    SetChrPos(0xF0, -87180, 0, -296440, 0)

    label("loc_FAC")

    OP_0D()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x102, 45, 400)

    ChrTalk(    #15
        0x102,
        "#1504F#6POh...\x02",
    )

    CloseMessageWindow()

    def lambda_FEA():
        OP_6D(-78170, 0, -289700, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_FEA)

    def lambda_1002():
        OP_67(0, 7450, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_1002)

    def lambda_101A():
        OP_6B(2950, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_101A)

    def lambda_102A():
        OP_6C(57000, 2000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_102A)

    def lambda_103A():
        OP_6E(253, 2000)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_103A)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1082")

    def lambda_1058():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1058)
    Sleep(100)

    def lambda_106B():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_106B)
    Sleep(100)
    OP_8C(0xF1, 45, 400)
    Jump("loc_10FB")

    label("loc_1082")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10C0")

    def lambda_1096():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1096)
    Sleep(100)

    def lambda_10A9():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_10A9)
    Sleep(100)
    OP_8C(0xF1, 45, 400)
    Jump("loc_10FB")

    label("loc_10C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10FB")

    def lambda_10D4():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_10D4)
    Sleep(100)

    def lambda_10E7():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_10E7)
    Sleep(100)
    OP_8C(0xF0, 45, 400)

    label("loc_10FB")

    WaitChrThread(0xEE, 0x1)
    Sleep(500)

    ChrTalk(    #16
        0x10,
        (
            "#1223F#5PWhy...? Why did this have to happen to me?\x02\x03",

            "If I could just have unraveled the mysteries\x01",
            "of this world and reported them to Ouroboros,\x01",
            "my promotion would've been guaranteed...\x02\x03",

            "#1228FTh-This is all their fault...\x02\x03",

            "Of course it is... All of this is their fault...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(500)
    OP_6D(-82000, 0, -290900, 0)
    OP_67(0, 5260, -10000, 0)
    OP_6B(3150, 0)
    OP_6C(90000, 0)
    OP_6E(282, 0)
    SetChrPos(0x10, -79200, 300, -290790, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12C7")
    SetChrPos(0x109, -86240, 0, -290380, 90)
    SetChrPos(0x102, -86260, 0, -291640, 90)
    SetChrPos(0xF0, -87770, 0, -289630, 90)
    SetChrPos(0xF1, -87510, 0, -292290, 90)
    Jump("loc_136E")

    label("loc_12C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_131C")
    SetChrPos(0x109, -86240, 0, -290380, 90)
    SetChrPos(0x102, -86260, 0, -291640, 90)
    SetChrPos(0xEF, -87770, 0, -289630, 90)
    SetChrPos(0xF1, -87510, 0, -292290, 90)
    Jump("loc_136E")

    label("loc_131C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_136E")
    SetChrPos(0x109, -86240, 0, -290380, 90)
    SetChrPos(0x102, -86260, 0, -291640, 90)
    SetChrPos(0xEF, -87770, 0, -289630, 90)
    SetChrPos(0xF0, -87510, 0, -292290, 90)

    label("loc_136E")

    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -79210, -300, -290270, 0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13B8")
    OP_62(0xEE, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_141F")

    label("loc_13B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E0")
    OP_62(0xEE, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_141F")

    label("loc_13E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1408")
    OP_62(0xEE, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_141F")

    label("loc_1408")

    OP_62(0xEE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_141F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1447")
    OP_62(0xEF, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_14AE")

    label("loc_1447")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_146F")
    OP_62(0xEF, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_14AE")

    label("loc_146F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1497")
    OP_62(0xEF, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_14AE")

    label("loc_1497")

    OP_62(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_14AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D6")
    OP_62(0xF0, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_153D")

    label("loc_14D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14FE")
    OP_62(0xF0, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_153D")

    label("loc_14FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1526")
    OP_62(0xF0, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_153D")

    label("loc_1526")

    OP_62(0xF0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_153D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1565")
    OP_62(0xF1, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_15CC")

    label("loc_1565")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_158D")
    OP_62(0xF1, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_15CC")

    label("loc_158D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15B5")
    OP_62(0xF1, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_15CC")

    label("loc_15B5")

    OP_62(0xF1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_15CC")

    Sleep(1800)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1618")

    ChrTalk(    #17
        0x10F,
        "#1801F#6P...Apparently, we're quite an easy target.\x02",
    )

    CloseMessageWindow()

    label("loc_1618")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1650")

    ChrTalk(    #18
        0x101,
        "#1016F#6PHe's same old, same old.\x02",
    )

    CloseMessageWindow()
    Jump("loc_16C9")

    label("loc_1650")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_168E")

    ChrTalk(    #19
        0x10B,
        "#416F#6PSeriously... He hasn't changed.\x02",
    )

    CloseMessageWindow()
    Jump("loc_16C9")

    label("loc_168E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16C9")

    ChrTalk(    #20
        0x106,
        "#555F#6PSeriously... He hasn't changed.\x02",
    )

    CloseMessageWindow()

    label("loc_16C9")


    ChrTalk(    #21
        0x109,
        (
            "#1841F#6P*sigh* How in Aidios' name did you end up\x01",
            "captured here?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_1732():
        OP_6D(-81370, 700, -291000, 1000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1732)

    def lambda_174A():
        OP_67(0, 2400, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_174A)

    def lambda_1762():
        OP_6B(3350, 1000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1762)

    def lambda_1772():
        OP_6E(280, 1000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1772)
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_22(0xCB, 0x0, 0x64)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    ClearChrFlags(0x10, 0x800)
    SetChrFlags(0x10, 0x1)

    def lambda_17AD():
        OP_96(0xFE, 0xFFFECC8A, 0x1F4, 0xFFFB8F48, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_17AD)
    OP_8C(0x10, 270, 0)
    WaitChrThread(0x10, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    ChrTalk(    #22
        0x10,
        (
            "#1224F#5PY-You! H-How did you all get here?!\x02\x03",

            "You came to laugh at me, didn't you?!\x01",
            "I bet you did!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x109,
        (
            "#1068F#6PSorry, but we totally forgot you were even here.\x02\x03",

            "#1060FSo, what? You got whisked here the same way\x01",
            "you ended up in the forest?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10,
        (
            "#1222F#5P...Hmph. As a matter of fact, yes.\x02\x03",

            "This appears to be another recreation of a\x01",
            "real place just like the capital was.\x02\x03",

            "#1223FAs I was starting to take in my surroundings,\x01",
            "I was surrounded by Vogels and knocked out\x01",
            "by electric shocks...\x02\x03",

            "Then when I woke up, I found myself here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x109,
        "#1840F#6PW-Wow... Must've been a blast...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x102,
        (
            "#1505F#6P(He seems pretty mentally drained...)\x02\x03",

            "#1500FHold on, Gilbert.\x02\x03",

            "If we mess with the panel over there, we should\x01",
            "be able to disable this barrier and get you out of \x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 90, 400)
    Sleep(300)

    ChrTalk(    #27
        0x10,
        (
            "#1223F#5PHmph... Forget it and leave me be.\x02\x03",

            "Even if by some miracle I manage to make it out\x01",
            "of this world, I'll just end up as Lord Campanella's\x01",
            "plaything again.\x02\x03",

            "#1228FAs if a guy like me had any real shot of being\x01",
            "promoted in Ouroboros...\x02\x03",

            "Why did I ever get my hopes up? Ugh...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C36")
    OP_62(0xEE, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1C9D")

    label("loc_1C36")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C5E")
    OP_62(0xEE, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1C9D")

    label("loc_1C5E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C86")
    OP_62(0xEE, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1C9D")

    label("loc_1C86")

    OP_62(0xEE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_1C9D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CC5")
    OP_62(0xEF, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1D2C")

    label("loc_1CC5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CED")
    OP_62(0xEF, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1D2C")

    label("loc_1CED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D15")
    OP_62(0xEF, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1D2C")

    label("loc_1D15")

    OP_62(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_1D2C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D54")
    OP_62(0xF0, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1DBB")

    label("loc_1D54")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D7C")
    OP_62(0xF0, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1DBB")

    label("loc_1D7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DA4")
    OP_62(0xF0, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1DBB")

    label("loc_1DA4")

    OP_62(0xF0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_1DBB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DE3")
    OP_62(0xF1, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1E4A")

    label("loc_1DE3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E0B")
    OP_62(0xF1, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1E4A")

    label("loc_1E0B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E33")
    OP_62(0xF1, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1E4A")

    label("loc_1E33")

    OP_62(0xF1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_1E4A")

    Sleep(1800)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EB1")

    ChrTalk(    #28
        0x10F,
        (
            "#1446F#6P(Poor thing's gotten himself caught up in a spiral\x01",
            "of negativity.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F53")

    label("loc_1EB1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F12")

    ChrTalk(    #29
        0x104,
        (
            "#1544F#6P(Poor thing's found himself caught up in a spiral\x01",
            "of negativity.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F53")

    label("loc_1F12")


    ChrTalk(    #30
        0x109,
        "#1068F#6P(Poor guy's tripped up in a spiral of negativity.)\x02",
    )

    CloseMessageWindow()

    label("loc_1F53")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FA3")

    ChrTalk(    #31
        0x105,
        "#1165F#6P(I can't help but feel kind of sorry for him...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_203E")

    label("loc_1FA3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FF2")

    ChrTalk(    #32
        0x10A,
        "#819F#6P(I can't help but feel kind of sorry for him...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_203E")

    label("loc_1FF2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_203E")

    ChrTalk(    #33
        0x107,
        "#562F#6P(I can't help but feel kind of sorry for him...)\x02",
    )

    CloseMessageWindow()

    label("loc_203E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2072")

    ChrTalk(    #34
        0x103,
        "#1534F#6P(*sigh* Oh, dear...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_20F2")

    label("loc_2072")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_209D")

    ChrTalk(    #35
        0x108,
        "#573F#6P(Oh, boy...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_20F2")

    label("loc_209D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20C9")

    ChrTalk(    #36
        0x10E,
        "#176F#6P(Oh, dear...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_20F2")

    label("loc_20C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20F2")

    ChrTalk(    #37
        0x10C,
        "#115F#6P(Oh, dear...)\x02",
    )

    CloseMessageWindow()

    label("loc_20F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2120")

    ChrTalk(    #38
        0x106,
        "#552F#6P(What a loser.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_214E")

    label("loc_2120")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_214E")

    ChrTalk(    #39
        0x10D,
        "#276F#6P(What a weakling.)\x02",
    )

    CloseMessageWindow()

    label("loc_214E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_218F")

    ChrTalk(    #40
        0x10B,
        "#212F#6P(Ugh... Just watching him annoys me.)\x02",
    )

    CloseMessageWindow()

    label("loc_218F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2716")

    ChrTalk(    #41
        0x110,
        (
            "#263F#6PI don't think you're wrong, though.\x02\x03",

            "#1306FAfter all, this is a world on a higher plane\x01",
            "that's beyond any technology the society\x01",
            "has.\x02\x03",

            "I bet the Thirteen Factories would be over\x01",
            "the moon if they had someone to tell them\x01",
            "aaall about it.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22FC")

    def lambda_22C6():
        TurnDirection(0xFE, 0x110, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_22C6)
    Sleep(100)

    def lambda_22D9():
        TurnDirection(0xFE, 0x110, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_22D9)
    Sleep(100)

    def lambda_22EC():
        TurnDirection(0xFE, 0x110, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_22EC)
    Sleep(100)
    Jump("loc_238D")

    label("loc_22FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2346")

    def lambda_2310():
        TurnDirection(0xFE, 0x110, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_2310)
    Sleep(100)

    def lambda_2323():
        TurnDirection(0xFE, 0x110, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2323)
    Sleep(100)

    def lambda_2336():
        TurnDirection(0xFE, 0x110, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_2336)
    Sleep(100)
    Jump("loc_238D")

    label("loc_2346")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_238D")

    def lambda_235A():
        TurnDirection(0xFE, 0x110, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_235A)
    Sleep(100)

    def lambda_236D():
        TurnDirection(0xFE, 0x110, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_236D)
    Sleep(100)

    def lambda_2380():
        TurnDirection(0xFE, 0x110, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_2380)
    Sleep(100)

    label("loc_238D")

    OP_8C(0x10, 270, 400)
    Sleep(300)

    ChrTalk(    #42
        0x10,
        (
            "#1221F#5PYou really think so?!\x02\x03",

            "#1222FWait... You're...\x02",
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
        "#1224F#5PL-L-L...\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #44
        0x10,
        "#1224F#5P#4SLady Renne?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #45
        0x10,
        (
            "#1224F#5PWhy are you...? I mean, what brings you here?!\x02\x03",

            "You didn't come here to finish me off because\x01",
            "you think I've betrayed Ouroboros, did you?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x110,
        (
            "#264F#6POh? I wasn't aware you'd betrayed Ouroboros.\x02\x03",

            "#263FHeehee. Dealing with traitors isn't usually part\x01",
            "of my job.\x02\x03",

            "#1306FI can make a special exception for you if you\x01",
            "want.\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x10, 0x0, 0x0, 0xB)
    Sleep(500)

    ChrTalk(    #47
        0x10,
        "#1224F#5PE-Eeeeeek!\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #48
        0x10,
        (
            "#1227F#5P#3SI didn't betray anyone!\x01",
            "I promise!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #49
        0x102,
        "#1512F#5PThat's enough, Renne...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2669")

    ChrTalk(    #50
        0x107,
        "#067F#5PR-Renne...\x02",
    )

    CloseMessageWindow()

    label("loc_2669")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26C0")

    ChrTalk(    #51
        0x101,
        (
            "#1016F#5PC'mon, Renne. He's already a sad enough sight\x01",
            "as it is.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26FE")

    label("loc_26C0")


    ChrTalk(    #52
        0x109,
        "#1840F#5PHaha... Don't bully the poor guy too much, now.\x02",
    )

    CloseMessageWindow()

    label("loc_26FE")


    ChrTalk(    #53
        0x110,
        "#261F#6PTeehee!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FD9")

    label("loc_2716")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A77")

    ChrTalk(    #54
        0x101,
        "#1019F#6P*sigh* I swear...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #55
        0x101,
        "#1022F#3S#6PGet a hold of yourself, man!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #56
        0x101,
        (
            "#1005F#6PYou're an adult, aren't you?\x01",
            "Start acting like one!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2835")

    def lambda_27FF():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_27FF)
    Sleep(100)

    def lambda_2812():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_2812)
    Sleep(100)

    def lambda_2825():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_2825)
    Sleep(100)
    Jump("loc_28C6")

    label("loc_2835")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_287F")

    def lambda_2849():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_2849)
    Sleep(100)

    def lambda_285C():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_285C)
    Sleep(100)

    def lambda_286F():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_286F)
    Sleep(100)
    Jump("loc_28C6")

    label("loc_287F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28C6")

    def lambda_2893():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_2893)
    Sleep(100)

    def lambda_28A6():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_28A6)
    Sleep(100)

    def lambda_28B9():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_28B9)
    Sleep(100)

    label("loc_28C6")

    OP_8C(0x10, 270, 400)
    Sleep(300)

    ChrTalk(    #57
        0x10,
        "#1224FWh-What...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        (
            "#1007F#6PYou might still be one of Ouroboros' lackeys,\x01",
            "but that doesn't mean I can leave you to rot\x01",
            "here in a cell.\x02\x03",

            "#1019FThat's not how bracers do things.\x02\x03",

            "You're either gonna come with me of your own\x01",
            "free will, or I'm gonna have to drag you out here. \x01",
            "Pick which one you want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x10,
        "#1225F#5PUgh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x102,
        "#1514F#5PEstelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x109,
        "#1840F#5PHaha... There's that feisty girl I know and love.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FD9")

    label("loc_2A77")


    ChrTalk(    #62
        0x102,
        "#1505F#6P...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x109, 400)
    Sleep(300)

    ChrTalk(    #63
        0x102,
        (
            "#1502F#11PWell, it looks as though staying here any longer\x01",
            "will be a waste of our time.\x02\x03",

            "We should get back to work.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B59")

    def lambda_2B23():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_2B23)
    Sleep(100)

    def lambda_2B36():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_2B36)
    Sleep(100)

    def lambda_2B49():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_2B49)
    Sleep(300)
    Jump("loc_2BEA")

    label("loc_2B59")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BA3")

    def lambda_2B6D():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_2B6D)
    Sleep(100)

    def lambda_2B80():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2B80)
    Sleep(100)

    def lambda_2B93():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_2B93)
    Sleep(300)
    Jump("loc_2BEA")

    label("loc_2BA3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BEA")

    def lambda_2BB7():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_2BB7)
    Sleep(100)

    def lambda_2BCA():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2BCA)
    Sleep(100)

    def lambda_2BDD():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_2BDD)
    Sleep(300)

    label("loc_2BEA")


    ChrTalk(    #64
        0x109,
        "#1064F#5PHuh...?\x02",
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
            "#1225F#5PW-Wait a second!\x02\x03",

            "I-I thought you were a bracer now!\x02\x03",

            "Aren't bracers all about saving people?!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D04")

    def lambda_2CBB():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2CBB)
    Sleep(100)

    def lambda_2CCE():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_2CCE)
    Sleep(100)

    def lambda_2CE1():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_2CE1)
    Sleep(100)

    def lambda_2CF4():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_2CF4)
    Sleep(400)
    Jump("loc_2DBB")

    label("loc_2D04")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D61")

    def lambda_2D18():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2D18)
    Sleep(100)

    def lambda_2D2B():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_2D2B)
    Sleep(100)

    def lambda_2D3E():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2D3E)
    Sleep(100)

    def lambda_2D51():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_2D51)
    Sleep(400)
    Jump("loc_2DBB")

    label("loc_2D61")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DBB")

    def lambda_2D75():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2D75)
    Sleep(100)

    def lambda_2D88():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_2D88)
    Sleep(100)

    def lambda_2D9B():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2D9B)
    Sleep(100)

    def lambda_2DAE():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_2DAE)
    Sleep(400)

    label("loc_2DBB")


    ChrTalk(    #66
        0x102,
        (
            "#1505F#6PA bracer's duty is to protect civilians.\x02\x03",

            "#1502FYou, meanwhile, are a member of an illegal group\x01",
            "and a wanted criminal. You can't honestly expect\x01",
            "we would feel obliged to protect you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x10,
        "#1224F#5PB-But...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x102,
        (
            "#1500F#6PThat doesn't mean I wouldn't be allowed to save\x01",
            "you--the guild code does leave a fair amount of\x01",
            "room for personal interpretation.\x02\x03",

            "#1509FIf you're specifically refusing my help, however,\x01",
            "then I see no reason to play semantics.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #69
        0x10,
        "#1227F#5PI-I never said I didn't want to be helped!\x02",
    )

    CloseMessageWindow()

    label("loc_2FD9")


    def lambda_2FDF():
        OP_6D(-82520, 0, -290940, 1800)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_2FDF)

    def lambda_2FF7():
        OP_67(0, 4050, -10000, 1800)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2FF7)

    def lambda_300F():
        OP_6B(3170, 1800)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_300F)

    def lambda_301F():
        OP_6E(270, 1800)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_301F)
    OP_44(0x10, 0x0)
    OP_22(0xCB, 0x0, 0x64)

    def lambda_3038():
        OP_96(0xFE, 0xFFFEC460, 0x0, 0xFFFB8F48, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3038)
    WaitChrThread(0x10, 0x1)
    ClearChrFlags(0x10, 0x4)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_3065():
        OP_8E(0xFE, 0xFFFEB7E0, 0x0, 0xFFFB8F48, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_3065)

    def lambda_3080():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_3080)
    Sleep(100)

    def lambda_3093():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_3093)
    Sleep(100)

    def lambda_30A6():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_30A6)
    Sleep(100)

    def lambda_30B9():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_30B9)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0xEE, 0x1)
    Sleep(300)

    ChrTalk(    #70
        0x10,
        (
            "#1225F#5POkay, fine! FINE!\x02\x03",

            "#1227FGet rid of this damn barrier and get me out of\x01",
            "here, pleeease! I'll do anything!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31AB")

    ChrTalk(    #71
        0x101,
        (
            "#1006F#6PHeheh. Why didn't you just say that in the first\x01",
            "place, you big dummy?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31AB")


    ChrTalk(    #72
        0x102,
        "#1513F#6P...As you wish.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x109,
        (
            "#1068F#6P*sigh* You really are a special thing, aren't you?\x02\x03",

            "#1066FAll righty, then. Let's mess with that panel over\x01",
            "there and get him out of here.\x02",
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

    # Function_10_E86 end

    def Function_11_329E(): pass

    label("Function_11_329E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_32DA")
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1000)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1500)
    Jump("Function_11_329E")

    label("loc_32DA")

    Return()

    # Function_11_329E end

    def Function_12_32DB(): pass

    label("Function_12_32DB")

    EventBegin(0x0)
    Fade(500)
    OP_6D(-86510, 0, -342000, 0)
    OP_67(0, 6850, -10000, 0)
    OP_6B(2920, 0)
    OP_6C(45000, 0)
    OP_6E(245, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3374")
    SetChrPos(0x109, -87710, 0, -342990, 90)
    SetChrPos(0x102, -88310, 0, -344500, 45)
    SetChrPos(0xF0, -88930, 0, -342520, 90)
    SetChrPos(0xF1, -89500, 0, -344070, 90)
    Jump("loc_3462")

    label("loc_3374")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33C9")
    SetChrPos(0x109, -87710, 0, -342990, 90)
    SetChrPos(0x102, -88310, 0, -344500, 45)
    SetChrPos(0xEF, -88930, 0, -342520, 90)
    SetChrPos(0xF1, -89500, 0, -344070, 90)
    Jump("loc_3462")

    label("loc_33C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_341E")
    SetChrPos(0x109, -87710, 0, -342990, 90)
    SetChrPos(0x102, -88310, 0, -344500, 45)
    SetChrPos(0xEF, -88930, 0, -342520, 90)
    SetChrPos(0xF0, -89500, 0, -344070, 90)
    Jump("loc_3462")

    label("loc_341E")

    SetChrPos(0x0, -87710, 0, -342990, 90)
    SetChrPos(0x1, -88310, 0, -344500, 45)
    SetChrPos(0x2, -88930, 0, -342520, 90)
    SetChrPos(0x3, -89500, 0, -344070, 90)

    label("loc_3462")

    OP_0D()
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3485")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A26")
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #74
        "\x18\x07\x05Please select the barrier you wish to unlock.\x18\x02",
    )


    Menu(
        0,
        -1,
        150,
        1,
        (
            "1\x01",      # 0
            "2\x01",      # 1
            "3\x01",      # 2
            "4\x01",      # 3
            "5\x01",      # 4
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
        (0, "loc_3524"),
        (1, "loc_361D"),
        (2, "loc_3716"),
        (3, "loc_380F"),
        (4, "loc_3908"),
        (SWITCH_DEFAULT, "loc_3A03"),
    )


    label("loc_3524")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35C9")
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
    Jump("loc_3A10")

    label("loc_35C9")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Synthesized Voice")

    AnonymousTalk(    #75
        "\x07\x05Barrier 1 has already been disabled.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_3A10")

    label("loc_361D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36C2")
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
    Jump("loc_3A10")

    label("loc_36C2")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Synthesized Voice")

    AnonymousTalk(    #76
        "\x07\x05Barrier 2 has already been disabled.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_3A10")

    label("loc_3716")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37BB")
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
    Jump("loc_3A10")

    label("loc_37BB")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Synthesized Voice")

    AnonymousTalk(    #77
        "\x07\x05Barrier 3 has already been disabled.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_3A10")

    label("loc_380F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38B4")
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
    Jump("loc_3A10")

    label("loc_38B4")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Synthesized Voice")

    AnonymousTalk(    #78
        "\x07\x05Barrier 4 has already been disabled.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_3A10")

    label("loc_3908")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39AF")
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

    label("loc_39AF")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Synthesized Voice")

    AnonymousTalk(    #79
        "\x07\x05Barrier 5 has already been disabled.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_3A10")

    label("loc_3A03")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3A10")

    label("loc_3A10")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3485")

    label("loc_3A26")

    FadeToBright(300, 0)
    EventEnd(0x0)
    Return()

    # Function_12_32DB end

    def Function_13_3A32(): pass

    label("Function_13_3A32")

    EventBegin(0x0)
    SetChrPos(0x109, -88230, 0, -297890, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A89")
    SetChrPos(0x102, -87150, 0, -298730, 0)
    SetChrPos(0xF0, -88720, 0, -300010, 0)
    SetChrPos(0xF1, -87070, 0, -300720, 0)
    Jump("loc_3B0E")

    label("loc_3A89")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3ACD")
    SetChrPos(0x102, -87150, 0, -298730, 0)
    SetChrPos(0xEF, -88720, 0, -300010, 0)
    SetChrPos(0xF1, -87070, 0, -300720, 0)
    Jump("loc_3B0E")

    label("loc_3ACD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B0E")
    SetChrPos(0x102, -87150, 0, -298730, 0)
    SetChrPos(0xEF, -88720, 0, -300010, 0)
    SetChrPos(0xF0, -87070, 0, -300720, 0)

    label("loc_3B0E")

    Sleep(500)

    ChrTalk(    #80
        0x10,
        "#1225F#5PIt's open!\x02",
    )

    CloseMessageWindow()

    def lambda_3B32():
        OP_6D(-86350, 0, -288930, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3B32)
    OP_8E(0x10, 0xFFFEA9E4, 0x0, 0xFFFB92D6, 0x1388, 0x0)
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #81
        0x10,
        (
            "#1221F#5PHahaha! I'm free! I'm freeeee!\x02\x03",

            "#1226FThe Goddess has not forsaken me after all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x109,
        (
            "#1066F#1PYou wouldn't believe he was asking to be left\x01",
            "alone a minute ago, would you?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3C1D():
        OP_6D(-86170, 0, -290780, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_3C1D)

    def lambda_3C35():
        OP_67(0, 6540, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_3C35)

    def lambda_3C4D():
        OP_6B(2370, 3000)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_3C4D)

    def lambda_3C5D():
        OP_6E(336, 3000)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_3C5D)

    def lambda_3C6D():
        OP_8F(0xFE, 0xFFFEA6EC, 0x0, 0xFFFB8804, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3C6D)
    OP_8C(0x10, 180, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CEB")

    def lambda_3C9D():
        OP_8F(0xFE, 0xFFFEAC28, 0x0, 0xFFFB878C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3C9D)

    def lambda_3CB8():
        OP_8F(0xFE, 0xFFFEA570, 0x0, 0xFFFB8246, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_3CB8)

    def lambda_3CD3():
        OP_8F(0xFE, 0xFFFEAB1A, 0x0, 0xFFFB8156, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_3CD3)
    Jump("loc_3DAC")

    label("loc_3CEB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D4D")

    def lambda_3CFF():
        OP_8F(0xFE, 0xFFFEAC28, 0x0, 0xFFFB878C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3CFF)

    def lambda_3D1A():
        OP_8F(0xFE, 0xFFFEA570, 0x0, 0xFFFB8246, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_3D1A)

    def lambda_3D35():
        OP_8F(0xFE, 0xFFFEAB1A, 0x0, 0xFFFB8156, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_3D35)
    Jump("loc_3DAC")

    label("loc_3D4D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DAC")

    def lambda_3D61():
        OP_8F(0xFE, 0xFFFEAC28, 0x0, 0xFFFB878C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3D61)

    def lambda_3D7C():
        OP_8F(0xFE, 0xFFFEA570, 0x0, 0xFFFB8246, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_3D7C)

    def lambda_3D97():
        OP_8F(0xFE, 0xFFFEAB1A, 0x0, 0xFFFB8156, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_3D97)

    label("loc_3DAC")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0xEE, 0x1)
    Sleep(300)

    ChrTalk(    #83
        0x10,
        (
            "#1222F#5PB-Bah! K-Keep in mind that this hardly spells\x01",
            "a victory over me, though!\x02\x03",

            "#1226FOrdinarily, I wouldn't feel compelled to thank\x01",
            "my enemies, no matter what they did...\x02\x03",

            "#1221F...but I'll make an exception just this once and\x01",
            "give you this. I hope you appreciate it!\x02",
        )
    )

    CloseMessageWindow()
    OP_8F(0x10, 0xFFFEA9E4, 0x0, 0xFFFB8C46, 0xBB8, 0x0)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #84
        "\x07\x05Gilbert thrust a \x1F\x37\x03\x07\x05 into Kevin's hands.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x337, 1)
    OP_8F(0x10, 0xFFFEA9E4, 0x0, 0xFFFB8FA2, 0x7D0, 0x0)
    Sleep(300)

    ChrTalk(    #85
        0x102,
        "#1504F#11PHey...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FB1")

    ChrTalk(    #86
        0x101,
        "#1004F#11PIsn't this...?\x02",
    )

    CloseMessageWindow()

    label("loc_3FB1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4012")

    ChrTalk(    #87
        0x10B,
        (
            "#213F#11PThis is one of those cards we got when we were\x01",
            "in the real Glorious!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4012")


    ChrTalk(    #88
        0x10,
        (
            "#1226F#5PHeh. That's the very latest Glorious security card.\x02\x03",

            "#1220FIt's something I was given back in the real world\x01",
            "before coming here, though, so who knows if it'll\x01",
            "actually be of use to you?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_40E0():

        label("loc_40E0")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_40E0")

    QueueWorkItem2(0xEE, 3, lambda_40E0)

    def lambda_40F1():

        label("loc_40F1")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_40F1")

    QueueWorkItem2(0xEF, 3, lambda_40F1)

    def lambda_4102():

        label("loc_4102")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_4102")

    QueueWorkItem2(0xF0, 3, lambda_4102)

    def lambda_4113():

        label("loc_4113")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_4113")

    QueueWorkItem2(0xF1, 3, lambda_4113)

    def lambda_4124():
        OP_6D(-86550, 0, -294630, 1800)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_4124)
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
            "#1221F#12PAnd that's not my problem! I bid you all farewell!\x02\x03",

            "The next time we meet, we will once again be foes!\x01",
            "Don't expect any mercyyy!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 180, 400)

    def lambda_4215():
        OP_6D(-86550, 0, -296000, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_4215)

    def lambda_422D():
        OP_8E(0xFE, 0xFFFEA96C, 0x0, 0xFFFB4CE0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_422D)
    WaitChrThread(0x10, 0x0)
    SetChrFlags(0x10, 0x80)
    WaitChrThread(0xEE, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4274")
    OP_62(0xEE, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_42CC")

    label("loc_4274")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4297")
    OP_62(0xEE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_42CC")

    label("loc_4297")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42BA")
    OP_62(0xEE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_42CC")

    label("loc_42BA")

    OP_62(0xEE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_42CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42EF")
    OP_62(0xEF, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_4347")

    label("loc_42EF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4312")
    OP_62(0xEF, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_4347")

    label("loc_4312")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4335")
    OP_62(0xEF, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_4347")

    label("loc_4335")

    OP_62(0xEF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_4347")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_436A")
    OP_62(0xF0, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_43C2")

    label("loc_436A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_438D")
    OP_62(0xF0, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_43C2")

    label("loc_438D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43B0")
    OP_62(0xF0, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_43C2")

    label("loc_43B0")

    OP_62(0xF0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_43C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43E5")
    OP_62(0xF1, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_443D")

    label("loc_43E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4408")
    OP_62(0xF1, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_443D")

    label("loc_4408")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_442B")
    OP_62(0xF1, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_443D")

    label("loc_442B")

    OP_62(0xF1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_443D")

    Sleep(1500)

    def lambda_4448():
        OP_6D(-86660, 0, -292380, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_4448)

    def lambda_4460():
        OP_6B(2220, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_4460)
    WaitChrThread(0xEE, 0x0)
    OP_63(0xEE)
    OP_63(0xEF)
    OP_63(0xF0)
    OP_63(0xF1)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_44A3")

    ChrTalk(    #90
        0x105,
        "#1165F#5PUmm...\x02",
    )

    CloseMessageWindow()

    label("loc_44A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_44D2")

    ChrTalk(    #91
        0x107,
        "#560F#5PThere he goes...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4502")

    label("loc_44D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4502")

    ChrTalk(    #92
        0x10A,
        "#814F#5PWell, there he goes.\x02",
    )

    CloseMessageWindow()

    label("loc_4502")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4539")

    ChrTalk(    #93
        0x10D,
        "#276F#5PWhat was all that about?\x02",
    )

    CloseMessageWindow()
    Jump("loc_456D")

    label("loc_4539")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_456D")

    ChrTalk(    #94
        0x106,
        "#055F#5PWhat was all that about?\x02",
    )

    CloseMessageWindow()

    label("loc_456D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_45E8")

    ChrTalk(    #95
        0x101,
        (
            "#1016F#5PI-I feel like my brain just switched itself off to\x01",
            "avoid having to process what just happened.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_460E")

    ChrTalk(    #96
        0x108,
        "#070F#5PHaha...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4644")

    label("loc_460E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4644")

    ChrTalk(    #97
        0x10C,
        "#119F#5PWhat a peculiar young man.\x02",
    )

    CloseMessageWindow()

    label("loc_4644")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4688")

    ChrTalk(    #98
        0x104,
        "#1541F#5PHe certainly knows how to make an exit.\x02",
    )

    CloseMessageWindow()

    label("loc_4688")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46DC")

    ChrTalk(    #99
        0x10B,
        (
            "#413F#5PHe's a few crayons short of a whole box,\x01",
            "isn't he...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_471D")

    label("loc_46DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_471D")

    ChrTalk(    #100
        0x103,
        "#1527F#5P*sigh* He really is a special one...\x02",
    )

    CloseMessageWindow()

    label("loc_471D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4768")

    ChrTalk(    #101
        0x10F,
        "#1805F#5PPerhaps we shouldn't have let him run free.\x02",
    )

    CloseMessageWindow()
    Jump("loc_47BD")

    label("loc_4768")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47BD")

    ChrTalk(    #102
        0x10E,
        (
            "#178F#5PHmm... Perhaps we ought to have restrained\x01",
            "him ourselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4812")

    ChrTalk(    #103
        0x110,
        (
            "#261F#5PI think I can see why Campy's taken such\x01",
            "a liking to him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4812")


    ChrTalk(    #104
        0x102,
        "#1503F#5P...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 270, 400)
    Sleep(300)

    ChrTalk(    #105
        0x102,
        (
            "#1513F#11PDespite what he said, Kevin...\x02\x03",

            "#1500F...I think we may actually be able to use\x01",
            "this security card here.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48E6")

    def lambda_48BC():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_48BC)
    Sleep(100)

    def lambda_48CF():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_48CF)
    Sleep(100)
    OP_8C(0x109, 90, 400)
    Jump("loc_495F")

    label("loc_48E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4924")

    def lambda_48FA():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_48FA)
    Sleep(100)

    def lambda_490D():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_490D)
    Sleep(100)
    OP_8C(0x109, 90, 400)
    Jump("loc_495F")

    label("loc_4924")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_495F")

    def lambda_4938():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_4938)
    Sleep(100)

    def lambda_494B():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_494B)
    Sleep(100)
    OP_8C(0x109, 90, 400)

    label("loc_495F")

    Sleep(300)

    ChrTalk(    #106
        0x109,
        (
            "#1075F#6PFunny. I was thinking the same thing.\x02\x03",

            "#1078FIf we pass anywhere it looks like we can\x01",
            "use it, let's give it a whirl.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2B25)
    OP_28(0x3A, 0x1, 0x20)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_13_3A32 end

    def Function_14_49F8(): pass

    label("Function_14_49F8")

    OP_8C(0xFE, 225, 400)
    OP_8E(0xFE, 0xFFFEA264, 0x0, 0xFFFB8AFC, 0x1B58, 0x0)
    OP_8E(0xFE, 0xFFFEA264, 0x0, 0xFFFB7CF6, 0x1B58, 0x0)
    OP_8E(0xFE, 0xFFFEA87C, 0x0, 0xFFFB759E, 0x1B58, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_14_49F8 end

    def Function_15_4A43(): pass

    label("Function_15_4A43")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4A63")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4D3A")

    Menu(
        0,
        -1,
        150,
        1,
        (
            "Open Door\x01",       # 0
            "Don't Open\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4AAA"),
        (SWITCH_DEFAULT, "loc_4D2A"),
    )


    label("loc_4AAA")

    EventBegin(0x0)
    Fade(500)
    OP_6D(61240, 0, -185600, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x109, 60240, 0, -186570, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B43")
    SetChrPos(0x102, 61770, 0, -186620, 0)
    SetChrPos(0xF0, 59990, 0, -188190, 0)
    SetChrPos(0xF1, 62120, 0, -188300, 0)
    Jump("loc_4BC8")

    label("loc_4B43")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B87")
    SetChrPos(0x102, 61770, 0, -186620, 0)
    SetChrPos(0xEF, 59990, 0, -188190, 0)
    SetChrPos(0xF1, 62120, 0, -188300, 0)
    Jump("loc_4BC8")

    label("loc_4B87")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BC8")
    SetChrPos(0x102, 61770, 0, -186620, 0)
    SetChrPos(0xEF, 59990, 0, -188190, 0)
    SetChrPos(0xF0, 62120, 0, -188300, 0)

    label("loc_4BC8")

    OP_0D()
    OP_20(0xBB8)

    def lambda_4BD4():
        OP_6D(60980, 500, -184400, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_4BD4)

    def lambda_4BEC():
        OP_67(0, 5000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_4BEC)

    def lambda_4C04():
        OP_6B(3120, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_4C04)

    def lambda_4C14():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_4C14)
    WaitChrThread(0xEE, 0x0)
    OP_21()
    OP_6F(0x2, 0)
    OP_70(0x2, 0x10E)
    OP_22(0x132, 0x0, 0x64)
    Sleep(500)

    def lambda_4C42():
        OP_67(0, 4500, -10000, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_4C42)

    def lambda_4C5A():
        OP_6B(3500, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_4C5A)
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
    Jump("loc_4D37")

    label("loc_4D2A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4D37")

    label("loc_4D37")

    Jump("loc_4A63")

    label("loc_4D3A")

    TalkEnd(0xFF)
    Return()

    # Function_15_4A43 end

    def Function_16_4D3E(): pass

    label("Function_16_4D3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E0D")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(7680)
    Sleep(500)
    Jump("loc_4E10")

    label("loc_4E0D")

    TalkBegin(0xFF)

    label("loc_4E10")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #107
        "\x07\x05Select an Option\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4E4C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4FAD")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "Restore HP/EP\x01",          # 0
            "Shop\x01",                   # 1
            "Synthesize Quartz\x01",      # 2
            "End\x01",                    # 3
        )
    )

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4EA8"),
        (1, "loc_4F41"),
        (2, "loc_4F6F"),
        (SWITCH_DEFAULT, "loc_4F9D"),
    )


    label("loc_4EA8")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 1)), scpexpr(EXPR_END)), "loc_4F0E")
    OP_1D(0xEA)
    Jump("loc_4F22")

    label("loc_4F0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 0)), scpexpr(EXPR_END)), "loc_4F20")
    OP_1D(0xB6)
    OP_1F(0x46, 0x64)
    Jump("loc_4F22")

    label("loc_4F20")

    OP_1D(0xEA)

    label("loc_4F22")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4FAA")

    label("loc_4F41")

    OP_A9(0x26)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #108
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_4FAA")

    label("loc_4F6F")

    OP_A9(0x9)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #109
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_4FAA")

    label("loc_4F9D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4FAA")

    label("loc_4FAA")

    Jump("loc_4E4C")

    label("loc_4FAD")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FDA")
    OP_A2(0x25A0)
    EventEnd(0x1)
    Jump("loc_4FDD")

    label("loc_4FDA")

    TalkEnd(0xFF)

    label("loc_4FDD")

    Return()

    # Function_16_4D3E end

    def Function_17_4FDE(): pass

    label("Function_17_4FDE")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x240147, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    TalkEnd(0xFF)
    Return()

    # Function_17_4FDE end

    def Function_18_5004(): pass

    label("Function_18_5004")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x240148, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    TalkEnd(0xFF)
    Return()

    # Function_18_5004 end

    def Function_19_502A(): pass

    label("Function_19_502A")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x24014E, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    TalkEnd(0xFF)
    Return()

    # Function_19_502A end

    def Function_20_5050(): pass

    label("Function_20_5050")

    OP_A3(0x2B6A)
    OP_A2(0x2B6B)
    OP_A3(0x2B6C)
    OP_A3(0x2B6D)
    OP_A3(0x2B6E)
    OP_A3(0x2B6F)
    OP_A3(0x2B70)
    OP_A3(0x2B71)
    Return()

    # Function_20_5050 end

    def Function_21_5069(): pass

    label("Function_21_5069")

    OP_A3(0x2B6A)
    OP_A3(0x2B6B)
    OP_A2(0x2B6C)
    OP_A3(0x2B6D)
    OP_A3(0x2B6E)
    OP_A3(0x2B6F)
    OP_A3(0x2B70)
    OP_A3(0x2B71)
    Return()

    # Function_21_5069 end

    def Function_22_5082(): pass

    label("Function_22_5082")

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

    # Function_22_5082 end

    def Function_23_50A0(): pass

    label("Function_23_50A0")

    SetMapFlags(0x2000000)
    Return()

    # Function_23_50A0 end

    def Function_24_50A6(): pass

    label("Function_24_50A6")

    OP_1D(0xB6)
    OP_1F(0x46, 0x64)
    Return()

    # Function_24_50A6 end

    SaveToFile()

Try(main)
