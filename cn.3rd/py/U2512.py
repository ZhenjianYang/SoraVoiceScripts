from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U2512   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U2512.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60231",
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
        '',                                     # 9
        '',                                     # 10
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
        'ED6_DT29/CH15140 ._CH',             # 00
        'ED6_DT29/CH15141 ._CH',             # 01
        'ED6_DT29/CH14650 ._CH',             # 02
        'ED6_DT29/CH14651 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT29/CH15140P._CP',             # 00
        'ED6_DT29/CH15141P._CP',             # 01
        'ED6_DT29/CH14650P._CP',             # 02
        'ED6_DT29/CH14651P._CP',             # 03
    )

    DeclMonster(
        X                   = 30970,
        Z                   = 0,
        Y                   = 450,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x275,
        Unknown_18          = 11084,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -5500,
        Z                   = 0,
        Y                   = -820,
        Unknown_0C          = 90,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x276,
        Unknown_18          = 11085,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 5580,
        Z                   = 4000,
        Y                   = -810,
        Unknown_0C          = 90,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x274,
        Unknown_18          = 11086,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 30970,
        Z                   = 0,
        Y                   = 450,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x274,
        Unknown_18          = 11084,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -5500,
        Z                   = 0,
        Y                   = -820,
        Unknown_0C          = 90,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x274,
        Unknown_18          = 11085,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 5580,
        Z                   = 4000,
        Y                   = -810,
        Unknown_0C          = 90,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x274,
        Unknown_18          = 11086,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -61400,
        Z                   = 0,
        Y                   = 29000,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x279,
        Unknown_18          = 11088,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -121050,
        Z                   = 0,
        Y                   = 50,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x27A,
        Unknown_18          = 11089,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -60820,
        Z                   = 0,
        Y                   = -1580,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x278,
        Unknown_18          = 11090,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -61400,
        Z                   = 0,
        Y                   = 29000,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x278,
        Unknown_18          = 11088,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -121050,
        Z                   = 0,
        Y                   = 50,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x278,
        Unknown_18          = 11089,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -60820,
        Z                   = 0,
        Y                   = -1580,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x278,
        Unknown_18          = 11090,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 0,
        Y                   = 0,
        Z                   = 0,
        Range               = 0,
        Unknown_10          = 0x0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x20,
        Unknown_1C          = 4,
    )


    DeclActor(
        TriggerX            = -120540,
        TriggerZ            = 0,
        TriggerY            = 29700,
        TriggerRange        = 1000,
        ActorX              = -120540,
        ActorZ              = 3000,
        ActorY              = 30510,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 29540,
        TriggerZ            = 0,
        TriggerY            = 30490,
        TriggerRange        = 1000,
        ActorX              = 29540,
        ActorZ              = 1000,
        ActorY              = 30490,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -59080,
        TriggerZ            = 0,
        TriggerY            = 25630,
        TriggerRange        = 1000,
        ActorX              = -59080,
        ActorZ              = 1000,
        ActorY              = 25630,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2A6",          # 00, 0
        "Function_1_476",          # 01, 1
        "Function_2_5E0",          # 02, 2
        "Function_3_706",          # 03, 3
        "Function_4_82C",          # 04, 4
        "Function_5_97D",          # 05, 5
        "Function_6_9D6",          # 06, 6
        "Function_7_A2F",          # 07, 7
        "Function_8_A88",          # 08, 8
        "Function_9_AE1",          # 09, 9
        "Function_10_CC6",         # 0A, 10
        "Function_11_EAB",         # 0B, 11
        "Function_12_F1F",         # 0C, 12
        "Function_13_1234",        # 0D, 13
        "Function_14_12EA",        # 0E, 14
    )


    def Function_0_2A6(): pass

    label("Function_0_2A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_2BC")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    Event(0, 14)
    Jump("loc_2E9")

    label("loc_2BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_2D4")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_B5(0x0)
    Event(0, 9)
    Jump("loc_2E9")

    label("loc_2D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_2E9")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_B5(0x0)
    Event(0, 10)

    label("loc_2E9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 6)), scpexpr(EXPR_END)), "loc_356")
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    Jump("loc_389")

    label("loc_356")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x569, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_370")
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    Jump("loc_389")

    label("loc_370")

    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)

    label("loc_389")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x569, 4)), scpexpr(EXPR_END)), "loc_39D")
    SetChrFlags(0x10, 0x80)

    label("loc_39D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x569, 5)), scpexpr(EXPR_END)), "loc_3A9")
    SetChrFlags(0x11, 0x80)

    label("loc_3A9")

    Jump("loc_475")

    label("loc_3AC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_475")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 6)), scpexpr(EXPR_END)), "loc_422")
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    Jump("loc_455")

    label("loc_422")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43C")
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    Jump("loc_455")

    label("loc_43C")

    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)

    label("loc_455")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_475")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56A, 0)), scpexpr(EXPR_END)), "loc_469")
    SetChrFlags(0x16, 0x80)

    label("loc_469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56A, 1)), scpexpr(EXPR_END)), "loc_475")
    SetChrFlags(0x17, 0x80)

    label("loc_475")

    Return()

    # Function_0_2A6 end

    def Function_1_476(): pass

    label("Function_1_476")

    OP_B1("U2512_n")
    OP_82(0x80, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xB, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_492")
    OP_82(0x81, 0x0)
    Jump("loc_495")

    label("loc_492")

    OP_82(0x82, 0x0)

    label("loc_495")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AD")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x275), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B2")
    OP_CE(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x276), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C7")
    OP_CE(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4C7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x274), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DC")
    OP_CE(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4DC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x279), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F1")
    OP_CE(0x3, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4F1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x27A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_506")
    OP_CE(0x3, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_506")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x278), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51B")
    OP_CE(0x3, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_51B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x569, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x569, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_532")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x569, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_532")
    Event(0, 5)

    label("loc_532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56A, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56A, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_549")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_549")
    Event(0, 6)

    label("loc_549")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x569, 6)), scpexpr(EXPR_END)), "loc_57B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x569, 7)), scpexpr(EXPR_END)), "loc_55E")
    Event(0, 7)
    Jump("loc_57B")

    label("loc_55E")

    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    OP_A3(0x2B4C)
    OP_A3(0x2B4D)
    OP_A3(0x2B4E)

    label("loc_57B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56A, 2)), scpexpr(EXPR_END)), "loc_5AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56A, 3)), scpexpr(EXPR_END)), "loc_590")
    Event(0, 8)
    Jump("loc_5AD")

    label("loc_590")

    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    OP_A3(0x2B50)
    OP_A3(0x2B51)
    OP_A3(0x2B52)

    label("loc_5AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x574, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BF")
    OP_6F(0x15, 0)
    Jump("loc_5C6")

    label("loc_5BF")

    OP_6F(0x15, 60)

    label("loc_5C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x574, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D8")
    OP_6F(0x16, 0)
    Jump("loc_5DF")

    label("loc_5D8")

    OP_6F(0x16, 60)

    label("loc_5DF")

    Return()

    # Function_1_476 end

    def Function_2_5E0(): pass

    label("Function_2_5E0")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x574, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C5")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x15, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1B9, 1)"), scpexpr(EXPR_END)), "loc_654")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xB9\x01\x07\x00。\x02",
    )

    Jump("loc_639")

    label("loc_639")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BA4)
    Jump("loc_6C2")

    label("loc_654")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xB9\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xB9\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_6A3")

    label("loc_6A3")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x15, 60)
    OP_70(0x15, 0x0)

    label("loc_6C2")

    Jump("loc_6F8")

    label("loc_6C5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_6F8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_5E0 end

    def Function_3_706(): pass

    label("Function_3_706")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x574, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EB")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x16, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1B6, 1)"), scpexpr(EXPR_END)), "loc_77A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xB6\x01\x07\x00。\x02",
    )

    Jump("loc_75F")

    label("loc_75F")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BA5)
    Jump("loc_7E8")

    label("loc_77A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xB6\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xB6\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_7C9")

    label("loc_7C9")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x16, 60)
    OP_70(0x16, 0x0)

    label("loc_7E8")

    Jump("loc_81E")

    label("loc_7EB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_81E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_706 end

    def Function_4_82C(): pass

    label("Function_4_82C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x569, 7)), scpexpr(EXPR_END)), "loc_8AC")
    OP_C0(0x1F, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_8CE")

    label("loc_8AC")

    OP_C0(0x1F, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)

    label("loc_8CE")

    Jump("loc_97C")

    label("loc_8D1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_97C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56A, 3)), scpexpr(EXPR_END)), "loc_95A")
    OP_C0(0x1F, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_97C")

    label("loc_95A")

    OP_C0(0x1F, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)

    label("loc_97C")

    Return()

    # Function_4_82C end

    def Function_5_97D(): pass

    label("Function_5_97D")

    EventBegin(0x0)
    Sleep(1000)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(1000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_A3(0x2B4C)
    OP_A3(0x2B4D)
    OP_A3(0x2B4E)
    OP_A2(0x2B4F)
    OP_28(0x37, 0x1, 0x20)
    OP_A2(0x2504)
    NewScene("ED6_DT21/U2512   ._SN", 100, 0, 1)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_5_97D end

    def Function_6_9D6(): pass

    label("Function_6_9D6")

    EventBegin(0x0)
    Sleep(1000)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(1000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_A3(0x2B50)
    OP_A3(0x2B51)
    OP_A3(0x2B52)
    OP_A2(0x2B53)
    OP_28(0x37, 0x1, 0x20)
    OP_A2(0x2505)
    NewScene("ED6_DT21/U2512   ._SN", 109, 0, 1)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_6_9D6 end

    def Function_7_A2F(): pass

    label("Function_7_A2F")

    EventBegin(0x0)
    Sleep(1000)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(1000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_A3(0x2B4C)
    OP_A3(0x2B4D)
    OP_A3(0x2B4E)
    OP_A3(0x2B4F)
    OP_28(0x37, 0x1, 0x40)
    OP_A2(0x2504)
    NewScene("ED6_DT21/U2512   ._SN", 100, 0, 1)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_7_A2F end

    def Function_8_A88(): pass

    label("Function_8_A88")

    EventBegin(0x0)
    Sleep(1000)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(1000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_A3(0x2B50)
    OP_A3(0x2B51)
    OP_A3(0x2B52)
    OP_A3(0x2B53)
    OP_28(0x37, 0x1, 0x40)
    OP_A2(0x2505)
    NewScene("ED6_DT21/U2512   ._SN", 109, 0, 1)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_8_A88 end

    def Function_9_AE1(): pass

    label("Function_9_AE1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B26")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x568, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x568, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x569, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x569, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56A, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56A, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B26")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x2506)
    NewScene("ED6_DT21/U2500   ._SN", 100, 0, 1)
    IdleLoop()
    Return()

    label("loc_B26")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BAC")
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 30790, 0, -1170, 180)
    SetChrPos(0x1, 30790, 0, -1170, 180)
    SetChrPos(0x2, 30790, 0, -1170, 180)
    SetChrPos(0x3, 30790, 0, -1170, 180)
    OP_69(0x0, 0x0)
    Jump("loc_CB5")

    label("loc_BAC")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C32")
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -2350, 0, -1840, 135)
    SetChrPos(0x1, -2350, 0, -1840, 135)
    SetChrPos(0x2, -2350, 0, -1840, 135)
    SetChrPos(0x3, -2350, 0, -1840, 135)
    OP_69(0x0, 0x0)
    Jump("loc_CB5")

    label("loc_C32")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB5")
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 5580, 4000, -810, 270)
    SetChrPos(0x1, 5580, 4000, -810, 270)
    SetChrPos(0x2, 5580, 4000, -810, 270)
    SetChrPos(0x3, 5580, 4000, -810, 270)
    OP_69(0x0, 0x0)

    label("loc_CB5")

    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_9_AE1 end

    def Function_10_CC6(): pass

    label("Function_10_CC6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x568, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x568, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x569, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x569, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56A, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56A, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D0B")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x2506)
    NewScene("ED6_DT21/U2500   ._SN", 100, 0, 1)
    IdleLoop()
    Return()

    label("loc_D0B")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D91")
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -61400, 0, 29000, 180)
    SetChrPos(0x1, -61400, 0, 29000, 180)
    SetChrPos(0x2, -61400, 0, 29000, 180)
    SetChrPos(0x3, -61400, 0, 29000, 180)
    OP_69(0x0, 0x0)
    Jump("loc_E9A")

    label("loc_D91")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E17")
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -121080, 0, 550, 180)
    SetChrPos(0x1, -121080, 0, 550, 180)
    SetChrPos(0x2, -121080, 0, 550, 180)
    SetChrPos(0x3, -121080, 0, 550, 180)
    OP_69(0x0, 0x0)
    Jump("loc_E9A")

    label("loc_E17")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E9A")
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -60820, 0, 580, 180)
    SetChrPos(0x1, -60820, 0, 580, 180)
    SetChrPos(0x2, -60820, 0, 580, 180)
    SetChrPos(0x3, -60820, 0, 580, 180)
    OP_69(0x0, 0x0)

    label("loc_E9A")

    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_10_CC6 end

    def Function_11_EAB(): pass

    label("Function_11_EAB")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05打开『门』吗？\x18\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_F08")

    label("loc_F08")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Return()

    # Function_11_EAB end

    def Function_12_F1F(): pass

    label("Function_12_F1F")

    EventBegin(0x0)
    OP_22(0x222, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x0, -120000, 0, 28020, 0)
    SetChrPos(0x1, -121300, 0, 28070, 0)
    SetChrPos(0x2, -120130, 0, 26350, 0)
    SetChrPos(0x3, -121510, 0, 26180, 0)
    OP_6D(-121100, 0, 28410, 0)
    OP_67(0, 5440, -10000, 0)
    OP_6B(3660, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xB, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FF5")
    OP_28(0xB, 0x4, 0x2)
    OP_82(0x81, 0x2)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_FF5")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xB, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_106C")

    AnonymousTalk(    #7
        (
            "\x07\x05#40W      道路既已打开……\x01",
            "#500W\x01",
            "#40W      穿越此『门』吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1103")

    label("loc_106C")


    AnonymousTalk(    #8
        (
            "\x07\x05#40W　 　米拉流通于天下……\x01",
            "　　   虽时而失去，\x01",
            "   必将轮回成为汝等之粮。\x01",
            "#500W\x01",
            "#40W　　请奉上『５万米拉』。\x01",
            "   如此，则『门』将开启……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1103")

    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xB, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1213")
    SetMessageWindowPos(-1, 90, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "\x07\x05奉上『５万米拉』，\x01",
            "打开『门』吗？\x18\x02",
        )
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_1192")

    label("loc_1192")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1210")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0xC350), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11F6")
    SubMira(50000)
    OP_22(0x14, 0x0, 0x64)
    SetMessageWindowPos(-1, 90, -1, -1)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x05支付了５万米拉！\x18\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Call(0, 13)
    Jump("loc_1210")

    label("loc_11F6")


    AnonymousTalk(    #11
        "\x07\x05没有足够的米拉。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1210")

    Jump("loc_1228")

    label("loc_1213")

    Call(0, 11)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1228")
    Call(0, 13)

    label("loc_1228")

    FadeToBright(300, 0)
    EventEnd(0x0)
    Return()

    # Function_12_F1F end

    def Function_13_1234(): pass

    label("Function_13_1234")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x14, 0)
    OP_70(0x14, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x14)
    Sleep(500)

    def lambda_129D():
        OP_6B(3010, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_129D)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_E3(0x0, 0x13, 0, 0x0)
    NewScene("ED6_DT21/P9001   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_1234 end

    def Function_14_12EA(): pass

    label("Function_14_12EA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x0, -120000, 0, 28020, 0)
    SetChrPos(0x1, -121300, 0, 28070, 0)
    SetChrPos(0x2, -120130, 0, 26350, 0)
    SetChrPos(0x3, -121510, 0, 26180, 0)
    OP_6D(-121100, 0, 28410, 0)
    OP_67(0, 5440, -10000, 0)
    OP_6B(3660, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    EventEnd(0x0)
    Return()

    # Function_14_12EA end

    SaveToFile()

Try(main)
